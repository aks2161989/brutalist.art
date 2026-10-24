"""Read-only checks for a blender-modelbuild film folder (beat sheet + evidence ledger).

Usage: verify_modelbuild.py <model-folder>/film
Checks structure, act order, view coverage, asset paths and hashes, AI-did
evidence, hand-reconstruction labels, human-verdict quotes, the
not-established beat, the closing card and banned voice/caption terms.
It does not judge teaching quality or truth.
"""
import argparse
import hashlib
import json
import re
import sys
from pathlib import Path

ACTS = ['views', 'brief', 'blockout', 'proportions', 'parts-order', 'modifiers',
        'materials', 'lighting-camera', 'check', 'export', 'rounds', 'assessment',
        'human-verdict', 'not-established', 'lesson', 'outro']
VIEW_KEYS = ['hero', 'side', 'front', 'rear', 'top']
CLOSING = 'Narration: the Liam voice'
RECON = 'Blender UI reconstruction'
WPS, PAD = 3.0, 0.4
# Viewers only ever hear "the Liam voice": no TTS product names, voice ids,
# engine or speed config. Patterns, so this file never spells them out.
BANNED_TEXT = [re.compile(p, re.I) for p in (
    r'k[o0]k[o0]r[o0]', r'\b[abejz][fm]_[a-z]{2,}\b', r'eleven\s*labs', r'\bvoice_id\b')]
BANNED_KEYS = {'engine', 'speed', 'voice_id', 'tts', 'tts_engine'}
MEDIA_BANNED = {'.srt', '.vtt', '.ass', '.mp4', '.mov', '.mp3', '.wav', '.m4a', '.aac'}
IMAGES = {'.png', '.jpg', '.jpeg', '.webp'}


def require(ok, msg):
    if not ok:
        raise ValueError(msg)


def present(v):
    return isinstance(v, str) and bool(v.strip())


def sha(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()


def resolve(root, rel, base=None):
    require(present(rel) and not Path(rel).is_absolute(), 'Expected relative path: %r' % rel)
    p = ((base or root) / rel).resolve()
    require(p.is_relative_to(root) and p.is_file(), 'Missing or escaping path: ' + rel)
    return p


def walk_keys(obj, where='root'):
    if isinstance(obj, dict):
        for k, v in obj.items():
            require(k not in BANNED_KEYS, 'Banned TTS config key %r at %s' % (k, where))
            walk_keys(v, where + '.' + k)
    elif isinstance(obj, list):
        for i, v in enumerate(obj):
            walk_keys(v, '%s[%d]' % (where, i))


def estimate(beats):
    return round(sum(b.get('estimated_duration_s') or (len(b['narration_text'].split()) / WPS + PAD) for b in beats), 1)


def verify(film):
    film = Path(film).resolve()
    sheet = json.loads((film / 'beat_sheet.json').read_text())
    data = json.loads((film / 'modelbuild-evidence.json').read_text())
    require(data.get('schema_version') == 1, 'Unknown evidence schema')
    model = (film / data.get('model_folder', '..')).resolve()
    meta = sheet.get('metadata', {})
    beats = sheet.get('beats', [])
    require(beats, 'No beats')

    # banned files and text anywhere in film/
    for p in film.rglob('*'):
        if p.is_file():
            require(p.suffix.lower() not in MEDIA_BANNED, 'No video/audio/caption files in film/: ' + p.name)
            if p.suffix.lower() in ('.json', '.md', '.txt'):
                t = p.read_text()
                for rx in BANNED_TEXT:
                    require(not rx.search(t), 'Banned voice term (%s) in %s' % (rx.pattern, p.name))
    walk_keys(sheet)
    require(meta.get('skill') == 'blender-modelbuild', 'metadata.skill must be blender-modelbuild')
    require(meta.get('narrator_label') == 'the Liam voice', 'narrator_label must be "the Liam voice"')
    require(meta.get('voice', 'the Liam voice') == 'the Liam voice', 'voice must be "the Liam voice"')
    require(meta.get('caption_policy') == 'none', 'caption_policy must be "none"')
    require(meta.get('closing_card') == CLOSING, 'closing_card must be %r' % CLOSING)

    ids = [b.get('beat_id') for b in beats]
    require(len(set(ids)) == len(ids), 'Duplicate beat ids')
    for b in beats:
        bid = b.get('beat_id')
        require(isinstance(bid, str) and re.fullmatch(r'B[0-9A-Z]+', bid), 'Bad beat_id %r' % bid)
        require(present(b.get('narration_text')), 'Beat lacks narration: ' + bid)
        require(isinstance(b.get('shot'), dict) and present(b['shot'].get('type')), 'Beat lacks shot.type: ' + bid)
        require(b.get('act') in ACTS, 'Unknown act %r in %s' % (b.get('act'), bid))
        require(b.get('actual_duration_s') is None and b.get('audio_file') is None,
                'Beat sheets only: no measured audio in ' + bid)

    # act order: all required, in order, contiguous
    seq = []
    for b in beats:
        if not seq or seq[-1] != b['act']:
            seq.append(b['act'])
    require(seq == ACTS, 'Acts must appear once each, in order: %s (got %s)' % (ACTS, seq))
    require(beats[0]['narration_text'].startswith('This is Liam.'), 'First beat must open "This is Liam."')

    # assets
    assets = {a['path']: a for a in data.get('assets', [])}
    for p, a in assets.items():
        f = resolve(model, p)
        require(f.suffix.lower() in IMAGES, 'Asset must be an image: ' + p)
        require(sha(f) == a.get('sha256'), 'Asset hash mismatch: ' + p)
        require(present(a.get('shows')), 'Asset needs "shows": ' + p)
    shown = set()
    for b in beats:
        for rel in b['shot'].get('assets', []):
            f = resolve(model, rel, base=film)
            key = f.relative_to(model).as_posix()
            require(key in assets, 'Shot asset not in ledger: ' + rel)
            shown.add(key)
        if b['act'] != 'outro':
            require(b['shot'].get('assets'), 'Beat shows nothing: ' + b['beat_id'])
    require(shown == set(assets), 'Ledger lists assets no beat shows: %s' % sorted(set(assets) - shown))

    # view coverage
    views = data.get('views', {})
    view_beats = [b for b in beats if b['act'] == 'views']
    view_shown = {Path((film / r).resolve()).relative_to(model).as_posix()
                  for b in view_beats for r in b['shot'].get('assets', [])}
    for k in VIEW_KEYS:
        require(present(views.get(k)) and views[k] in view_shown, 'Views must show %s in a views beat' % k)
    require(views.get('details') and all(d in view_shown for d in views['details']), 'Views must show details')

    # source files
    files = {f['path']: f for f in data.get('files', [])}
    require(files, 'Ledger lists no build files')
    for p, f in files.items():
        require(sha(resolve(model, p)) == f.get('sha256'), 'Source hash mismatch: ' + p)
        require(present(f.get('role')), 'Source needs a role: ' + p)
    recon = set(data.get('reconstructions', []))
    tracks = {}
    for b in beats:
        t = b.get('track')
        tracks[t] = tracks.get(t, 0) + 1
        if t in ('ai-did', 'both'):
            ad = b.get('ai_did') or {}
            require(present(ad.get('summary')) and ad.get('evidence'), 'ai_did needs summary+evidence: ' + b['beat_id'])
            for p in ad['evidence']:
                require(p in files, 'ai_did evidence not in ledger: ' + p)
        if t in ('by-hand', 'both'):
            ui = b.get('ui_steps') or {}
            require(RECON in ui.get('label', ''), 'by-hand beat must be labelled %r: %s' % (RECON, b['beat_id']))
            require(ui.get('steps'), 'by-hand beat lacks steps: ' + b['beat_id'])
            require(b['beat_id'] in recon, 'Reconstruction not listed in ledger: ' + b['beat_id'])
    require(tracks.get('ai-did', 0) + tracks.get('both', 0) >= 4, 'Too few AI-did beats')
    require(tracks.get('by-hand', 0) + tracks.get('both', 0) >= 4, 'Too few by-hand beats')

    # human verdicts
    narr = ' '.join(b['narration_text'] for b in beats).lower()
    hv = data.get('human_verdicts', [])
    require(hv, 'No human verdicts recorded')
    for v in hv:
        require(v.get('status') in ('given', 'pending'), 'Verdict status must be given/pending')
        if v['status'] == 'given':
            require(present(v.get('quote')) and v['quote'].lower() in narr, 'Verdict quote not narrated: %r' % v.get('quote'))
    require('professor bear said' in narr, 'Narration never attributes "Professor Bear said"')
    require(data.get('not_established'), 'Name at least one thing the evidence does not establish')

    # closing card
    last = beats[-1]
    require(last['act'] == 'outro' and last['shot'].get('card_text') == CLOSING,
            'Last beat must be the outro card %r' % CLOSING)
    total = estimate(beats)
    return {'status': 'PASS', 'beats': len(beats), 'est_runtime_s': total,
            'est_runtime': '%d:%02d' % divmod(round(total), 60), 'assets': len(assets),
            'source_files': len(files), 'reconstructed_beats': len(recon),
            'scope': 'Structure, paths, hashes, labels and quotes; not teaching quality or truth.'}


if __name__ == '__main__':
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument('film')
    a = ap.parse_args()
    try:
        print(json.dumps(verify(a.film), indent=2))
    except (ValueError, OSError, KeyError, TypeError, json.JSONDecodeError) as exc:
        print('blender-modelbuild FAIL: ' + str(exc), file=sys.stderr)
        sys.exit(1)
