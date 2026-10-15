#!/usr/bin/env python3
"""Read-only trailer gate. Checks the structure, honesty and evidence of
trailer.json against the real capture files. It cannot judge whether a shot is
legible, whether the music fits, or whether a stranger understands the game —
those need frames, ears and a human who has never seen the game."""
import argparse
import hashlib
import json
import math
from pathlib import Path
import re
import shutil
import subprocess
import sys

ROLE_ORDER = ['hook', 'establish', 'escalate', 'peak', 'title', 'button', 'cta']
REQUIRED_ROLES = ['hook', 'establish', 'escalate', 'peak', 'cta']
TYPES = {'store': (30, 90), 'announcement': (30, 120), 'launch': (30, 120)}
HARD_MIN_S, HARD_MAX_S = 15.0, 120.0
BUILD_STATUS = {'prototype', 'demo', 'early-access', 'released', 'coming-soon'}
NEW_INFO = {'mechanic', 'environment', 'enemy', 'progression', 'ui', 'payoff', 'none'}
CTA_SOURCES = {'export_presets.cfg', 'README', 'git-remote', 'bear-stated', 'store-page'}
INTEGRITY = {'teleport': False, 'invincible': False, 'collisions_disabled': False,
             'spawned_content': False}
MIN_SHOT_S = {'hook': 1.5, 'establish': 2.0, 'escalate': 0.8, 'peak': 0.8,
              'title': 1.0, 'button': 0.8}
FLASH_MIN_S, MAX_FLASH = 0.4, 3
MAX_TEXT_WORDS, MAX_TOTAL_TEXT_WORDS = 7, 24
MAX_DEBUG_CAMERA_SHARE, MAX_HOLD_S, MAX_BUTTON_S = 0.15, 0.5, 4.0
HOOK_BY_S, GENRE_BY_S, NO_CARD_BEFORE_S = 15.0, 10.0, 5.0
CTA_MIN_HOLD_S, CTA_S_PER_WORD, CTA_MAX_DIRECTIVE_WORDS = 3.0, 0.3, 8
CUT_TOLERANCE_S, ALIGN_FAIL, ALIGN_WARN = 0.07, 0.60, 0.80
MAX_VO_LINE_WORDS, MAX_VO_WORDS, MAX_VO_SHARE, VO_MIN_GAP_S = 12, 60, 0.45, 0.15
# A trailer opens on gameplay, not on an introduction: no hello, no "this is Liam", no "in for Bear".
GREETING = re.compile(r"^\s*(hello|hi|hey|welcome|good (morning|afternoon|evening)|this is (liam|bear)|i'?m liam)\b"
                      r"|\bin for bear\b", re.I)
FIRST_FRAME_MIN_LUMA = 0.06
# Adjectives are claims; the footage is the evidence. Whole-word, case-insensitive.
BANNED_WORDS = {
    'epic', 'immersive', 'breathtaking', 'stunning', 'amazing', 'incredible', 'awesome',
    'ultimate', 'thrilling', 'unforgettable', 'gorgeous', 'beautiful', 'masterpiece',
    'revolutionary', 'groundbreaking', 'spectacular', 'addictive', 'exciting',
    'innovative', 'next-gen', 'best', 'unique', 'ultimate', 'fantastic', 'insane',
}


class Report:
    def __init__(self):
        self.fails, self.warns = [], []

    def fail(self, where, message):
        self.fails.append(f'{where}: {message}')

    def warn(self, where, message):
        self.warns.append(f'{where}: {message}')

    def need(self, condition, where, message):
        if not condition:
            self.fail(where, message)
        return bool(condition)


def nonempty(value):
    return isinstance(value, str) and bool(value.strip())


def number(value):
    return isinstance(value, (int, float)) and not isinstance(value, bool) and math.isfinite(value)


def sha256(path):
    digest = hashlib.sha256()
    with path.open('rb') as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b''):
            digest.update(chunk)
    return digest.hexdigest()


def contained(root, value):
    """Resolve a relative path that must stay inside the reel; None if it cannot."""
    if not nonempty(value) or Path(value).is_absolute():
        return None
    path = (root / value).resolve()
    if not path.is_relative_to(root) or not path.is_file() or path.stat().st_size == 0:
        return None
    return path


def probe(path):
    out = subprocess.run(['ffprobe', '-v', 'error', '-show_streams', '-show_format',
                          '-of', 'json', str(path)], capture_output=True, text=True,
                         timeout=60, check=True).stdout
    data = json.loads(out)
    videos = [s for s in data.get('streams', []) if s.get('codec_type') == 'video']
    audio = [s for s in data.get('streams', []) if s.get('codec_type') == 'audio']
    duration = float(data.get('format', {}).get('duration') or 0)
    if not videos:
        return {'duration_s': duration, 'has_audio': bool(audio)}
    video = videos[0]
    return {'width': int(video['width']), 'height': int(video['height']),
            'duration_s': float(video.get('duration') or duration), 'has_audio': bool(audio)}


def first_frame_luma(path, at_s):
    """Mean brightness 0..1 of the frame at `at_s`: catches a fade-in from black."""
    proc = subprocess.run(['ffmpeg', '-v', 'error', '-ss', f'{at_s:.3f}', '-i', str(path),
                           '-frames:v', '1', '-vf', 'scale=64:36,format=gray',
                           '-f', 'rawvideo', '-'], capture_output=True, timeout=60)
    if proc.returncode != 0 or not proc.stdout:
        return None
    return sum(proc.stdout) / len(proc.stdout) / 255.0


def window_rms(path, start_s, end_s):
    proc = subprocess.run(['ffmpeg', '-v', 'error', '-ss', f'{max(start_s, 0):.3f}',
                           '-t', f'{max(end_s - start_s, 0.05):.3f}', '-i', str(path),
                           '-vn', '-ac', '1', '-ar', '8000', '-f', 'f32le', '-'],
                          capture_output=True, timeout=60)
    if proc.returncode != 0 or len(proc.stdout) < 8:
        return None
    import array
    samples = array.array('f')
    samples.frombytes(proc.stdout[: len(proc.stdout) // 4 * 4])
    return math.sqrt(sum(x * x for x in samples) / len(samples)) if samples else None


def words(text):
    return re.findall(r"[A-Za-z0-9'’-]+", text or '')


def banned_in(text):
    return sorted({w.lower() for w in words(text) if w.lower() in BANNED_WORDS})


def export_platforms(game_dir):
    """Platform names declared in the project's export_presets.cfg, lowercased."""
    if not game_dir:
        return None
    for candidate in [Path(game_dir), *Path(game_dir).glob('godot'), *Path(game_dir).glob('*')]:
        cfg = candidate / 'export_presets.cfg'
        if cfg.is_file():
            return {m.lower() for m in re.findall(r'^platform="([^"]+)"', cfg.read_text(), re.M)}
    return set()


def timeline(shots):
    """Gameplay plays at normal speed, so its screen time is its source window."""
    t, spans = 0.0, {}
    for shot in shots:
        if shot.get('kind') == 'gameplay' and number(shot.get('in_s')) and number(shot.get('out_s')):
            hold = shot.get('hold_s') if number(shot.get('hold_s')) else 0.0
            dur = shot['out_s'] - shot['in_s'] + hold
        elif shot.get('kind') == 'card' and number(shot.get('duration_s')):
            dur = shot['duration_s']
        else:
            dur = 0.0
        spans[shot.get('id')] = (t, t + dur)
        t += dur
    return spans, t


def check_captures(root, data, build_id, min_height, rep):
    props = {}
    captures = data.get('captures')
    if not rep.need(isinstance(captures, dict) and captures, 'captures', 'no captures recorded'):
        return props
    for cid, cap in captures.items():
        where = f'capture {cid}'
        if not rep.need(isinstance(cap, dict), where, 'invalid record'):
            continue
        rep.need(cap.get('build_id') == build_id, where, 'stale/different game build')
        rep.need(cap.get('method') in ('scripted-input', 'human-input'), where,
                 'method must be scripted-input or human-input')
        rep.need(contained(root, cap.get('input_log')) is not None, where, 'missing input_log')
        rep.need(nonempty(cap.get('state_setup')), where,
                 'state_setup must say how the starting state was reached, as a player could')
        integrity = cap.get('integrity')
        if rep.need(isinstance(integrity, dict), where, 'integrity attestation missing'):
            for key, clean in INTEGRITY.items():
                rep.need(integrity.get(key) is clean or integrity.get(key) == clean, where,
                         f'integrity.{key} must be explicitly {clean} (no cheats in trailer footage)')
            rep.need(integrity.get('time_scale') == 1.0, where,
                     'integrity.time_scale must be 1.0 (no slow motion or speed-up)')
        path = contained(root, cap.get('path'))
        if not rep.need(path is not None, where, 'capture file missing/outside reel'):
            continue
        rep.need(cap.get('sha256') == sha256(path), where, 'capture hash mismatch')
        try:
            p = probe(path)
        except (subprocess.SubprocessError, OSError, ValueError, KeyError) as exc:
            rep.fail(where, f'unreadable media: {exc}')
            continue
        if 'height' not in p:
            rep.fail(where, 'no video stream')
            continue
        rep.need(p['height'] >= min_height and p['width'] >= math.ceil(min_height * 16 / 9), where,
                 f'below native 16:9 {min_height}p')
        rep.need(abs(p['width'] / p['height'] - 16 / 9) < 0.01, where, 'landscape trailer needs 16:9 footage')
        props[cid] = (path, p)
    return props


def check_brief(data, rep):
    brief = data.get('brief')
    if not rep.need(isinstance(brief, dict), 'brief', 'missing'):
        return set()
    for key in ('audience', 'goal', 'genre', 'hook', 'idea', 'tone'):
        rep.need(nonempty(brief.get(key)), 'brief', f'{key} is empty — decide it before capturing')
    if nonempty(brief.get('hook')) and len(words(brief['hook'])) > 30:
        rep.warn('brief.hook', 'more than 30 words is not one sentence; if it will not shorten, '
                              'the design has no hook yet — report that, do not edit around it')
    for adj in banned_in(brief.get('hook', '')):
        rep.fail('brief.hook', f'adjective claim "{adj}" — state the mechanic instead')
    answers = brief.get('answers')
    if rep.need(isinstance(answers, dict), 'brief.answers', 'missing'):
        for key in ('what_is_this', 'what_do_i_do', 'why_care'):
            rep.need(nonempty(answers.get(key)), 'brief.answers', f'{key} unanswered')
    verbs = brief.get('verbs')
    ids = set()
    if rep.need(isinstance(verbs, list) and verbs, 'brief.verbs', 'name what the player presses and what happens'):
        for verb in verbs:
            ok = isinstance(verb, dict) and nonempty(verb.get('id')) and nonempty(verb.get('input')) \
                and nonempty(verb.get('result'))
            if rep.need(ok, 'brief.verbs', 'each verb needs id, input and result'):
                ids.add(verb['id'])
    return ids


def check_presentation(data, rep):
    pres = data.get('presentation')
    if pres is None:
        return
    if not rep.need(isinstance(pres, dict), 'presentation', 'must be an object'):
        return
    rep.need(number(pres.get('inset')) and 0.8 <= pres['inset'] < 1.0, 'presentation',
             'inset must be 0.8–1.0 (exclusive): the capture is matted inside the title-safe box, never cropped')
    rep.need(isinstance(pres.get('pad_color'), str) and re.fullmatch(r'#[0-9A-Fa-f]{6}', pres['pad_color']),
             'presentation', 'pad_color must be #RRGGBB (use the game\'s own background colour)')
    regions = pres.get('contrast_regions')
    if rep.need(isinstance(regions, list) and regions and nonempty(pres.get('contrast_reason')), 'presentation',
                'name the text regions GATE T should test (contrast_regions) and say why (contrast_reason)'):
        for region in regions:
            box = region.get('box') if isinstance(region, dict) else None
            rep.need(isinstance(region, dict) and nonempty(region.get('label')) and isinstance(box, list)
                     and len(box) == 4 and all(number(v) for v in box)
                     and 0 <= box[0] < box[2] <= 1 and 0 <= box[1] < box[3] <= 1, 'presentation',
                     'each region needs a label and a normalised [x0, y0, x1, y1] box')


def check_features(data, rep):
    implemented, planned = set(), set()
    features = data.get('features')
    if not rep.need(isinstance(features, list) and features, 'features', 'no feature inventory'):
        return implemented, planned
    for feat in features:
        if not rep.need(isinstance(feat, dict) and nonempty(feat.get('id')), 'features', 'invalid feature'):
            continue
        if feat.get('status') == 'implemented':
            implemented.add(feat['id'])
        elif feat.get('status') == 'planned':
            planned.add(feat['id'])
            rep.need(nonempty(feat.get('reason')), f'feature {feat["id"]}', 'planned needs a reason')
        else:
            rep.fail(f'feature {feat["id"]}', 'status must be implemented or planned')
    return implemented, planned


def check_music(root, data, total, spans, shots, rep):
    music = data.get('music')
    if not rep.need(isinstance(music, dict), 'music', 'missing — declare source "none" if intentional'):
        return
    source = music.get('source')
    if not rep.need(source in ('game', 'supplied', 'generated', 'none'), 'music',
                    'source must be game, supplied, generated or none'):
        return
    if source == 'none':
        rep.warn('music', 'no music: allowed, but a trailer edited to a score is stronger — '
                          'ask for a track whose rights and tone are recorded')
        return
    rep.need(nonempty(music.get('provenance')), 'music',
             'provenance (who made it, licence, where from) is required — never "unknown"')
    rep.need(nonempty(music.get('tone_note')), 'music',
             'tone_note must say why this music fits THIS game (tone mismatch advertises another game)')
    track = contained(root, music.get('path'))
    if rep.need(track is not None, 'music', 'track missing/outside reel'):
        rep.need(music.get('sha256') == sha256(track), 'music', 'track hash mismatch')
    if source == 'generated':
        script = contained(root, music.get('generator'))
        if rep.need(script is not None, 'music', 'generated music needs its generator script inside the reel'):
            rep.need(music.get('generator_sha256') == sha256(script), 'music', 'generator script changed since the track was made')
        rep.need(music.get('trailer_only') is True, 'music',
                 'generated music must be declared trailer_only: true (the game does not have this audio; say so in the description)')
    rhythm = music.get('rhythm')
    if not rep.need(rhythm in ('metered', 'free'), 'music', 'rhythm must be metered or free'):
        return
    drop = music.get('drop')
    peak_start = next((spans[s['id']][0] for s in shots if s.get('role') == 'peak'), None)
    if isinstance(drop, dict) and number(drop.get('start_s')) and number(drop.get('end_s')):
        if not (drop['end_s'] - drop['start_s'] >= 0.25 and peak_start is not None
                and 0 <= peak_start - drop['end_s'] <= 0.5):
            rep.warn('music.drop', 'the pause should last >= 0.25 s and end within 0.5 s of the peak shot')
    else:
        rep.warn('music.drop', 'no pause before the peak declared; vary the rhythm so the peak lands')
    if rhythm == 'free':
        return
    beats_file = contained(root, music.get('beats'))
    if not rep.need(beats_file is not None, 'music', 'metered music needs a beats file (beat_grid.py)'):
        return
    try:
        grid = json.loads(beats_file.read_text())
        beats = sorted(float(b) for b in grid['beats'])
    except (ValueError, KeyError, TypeError):
        rep.fail('music.beats', 'unreadable beats file')
        return
    cuts = [(s, spans[s['id']][0]) for s in shots[1:] if not s.get('free_cut')]
    if not cuts:
        return
    aligned = sum(1 for _, t in cuts if min(abs(t - b) for b in beats) <= CUT_TOLERANCE_S)
    ratio = aligned / len(cuts)
    msg = f'{aligned}/{len(cuts)} cuts land on a beat (±{CUT_TOLERANCE_S * 1000:.0f} ms)'
    if ratio < ALIGN_FAIL:
        rep.fail('music', msg + '; edit to the rhythm or mark the exceptions free_cut')
    elif ratio < ALIGN_WARN:
        rep.warn('music', msg)
    free = sum(1 for s in shots[1:] if s.get('free_cut'))
    if free > 0.25 * max(len(shots) - 1, 1):
        rep.warn('music', 'more than a quarter of the cuts are free_cut')
    if track and total > 0 and (probe(track)['duration_s'] + 0.15) < total:
        rep.fail('music', 'track is shorter than the trailer')


def check_vo(root, data, shots, spans, total, rep):
    """Voiceover (optional; Liam on request). Sparse, never the only carrier of information."""
    vo = data.get('vo')
    if vo is None:
        return
    if not rep.need(isinstance(vo, dict) and isinstance(vo.get('lines'), list) and vo['lines'], 'vo',
                    'vo needs a non-empty lines list (omit vo for a music-only trailer)'):
        return
    rep.need(vo.get('engine', 'kokoro') == 'kokoro', 'vo', 'the trailer voice is free and local: engine must be kokoro')
    rep.need(nonempty(vo.get('voice')), 'vo', 'voice is required (Liam is am_onyx)')
    if vo.get('persona') == 'liam':
        rep.need(vo.get('voice') == 'am_onyx', 'vo', 'Liam is Kokoro am_onyx')
    manifest_path = contained(root, 'audio/vo/manifest.json')
    manifest = {}
    if rep.need(manifest_path is not None, 'vo', 'no audio/vo/manifest.json: run vo_kokoro.py (--assemble does)'):
        manifest = json.loads(manifest_path.read_text())
    spans_by_shot = {s['id']: spans[s['id']] for s in shots}
    placed, words_total, ids = [], 0, set()
    for line in vo['lines']:
        where = f'vo {line.get("id") if isinstance(line, dict) else "?"}'
        if not rep.need(isinstance(line, dict) and nonempty(line.get('id')) and nonempty(line.get('text')), where,
                        'each line needs id and text'):
            continue
        rep.need(line['id'] not in ids, where, 'duplicate line id')
        ids.add(line['id'])
        n = len(words(line['text']))
        words_total += n
        rep.need(n <= MAX_VO_LINE_WORDS, where, f'{n} words; keep a line under {MAX_VO_LINE_WORDS}: footage carries the trailer')
        for adj in banned_in(line['text']):
            rep.fail(where, f'adjective claim "{adj}" — the footage is the evidence')
        rep.need(nonempty(line.get('on_screen_equivalent')), where,
                 'say what on screen already carries this line: the trailer must work with the sound off')
        shot = line.get('shot')
        if not rep.need(shot in spans_by_shot and number(line.get('at_s')) and line['at_s'] >= 0, where,
                        'needs a real shot and at_s >= 0 (seconds into that shot)'):
            continue
        s0, s1 = spans_by_shot[shot]
        rep.need(s0 + line['at_s'] < s1, where, 'the line must start inside its shot')
        entry = manifest.get(line['id'])
        if not rep.need(isinstance(entry, dict), where, 'not generated yet: run vo_kokoro.py'):
            continue
        rep.need(entry.get('text_sha256') == hashlib.sha256(line['text'].strip().encode()).hexdigest(), where,
                 'the text changed after the audio was made: regenerate it')
        wav = contained(root, entry.get('wav'))
        if not rep.need(wav is not None and entry.get('wav') == f'audio/vo/{line["id"]}.wav', where, 'audio file missing'):
            continue
        rep.need(entry.get('wav_sha256') == sha256(wav), where, 'audio hash mismatch')
        duration = probe(wav)['duration_s']
        rep.need(abs(duration - entry.get('duration_s', -1)) <= 0.05, where, 'manifest duration differs from the file')
        start = s0 + line['at_s']
        placed.append((start, start + duration, line))
    placed.sort(key=lambda p: p[0])
    if placed:
        rep.need(not GREETING.search(placed[0][2]['text']), f'vo {placed[0][2]["id"]}',
                 'a trailer opens on gameplay, not an introduction: no hello, no "this is Liam", no "in for Bear"')
    for (a0, a1, la), (b0, b1, lb) in zip(placed, placed[1:]):
        rep.need(b0 >= a1 + VO_MIN_GAP_S, f'vo {lb["id"]}',
                 f'starts {b0:.2f}s, only {b0 - a1:.2f}s after {la["id"]} ends: leave air between lines')
    for start, end, line in placed:
        rep.need(end <= total + 0.001, f'vo {line["id"]}', f'runs to {end:.2f}s, past the {total:.2f}s trailer')
    rep.need(words_total <= MAX_VO_WORDS, 'vo', f'{words_total} words; the budget is {MAX_VO_WORDS}')
    if total and sum(e - st for st, e, _ in placed) / total > MAX_VO_SHARE:
        rep.warn('vo', f'voice covers over {MAX_VO_SHARE:.0%} of the trailer: leave room for the music and the game')
    drop = (data.get('music') or {}).get('drop')
    if isinstance(drop, dict) and number(drop.get('start_s')) and number(drop.get('end_s')):
        for start, end, line in placed:
            if start < drop['end_s'] and end > drop['start_s']:
                rep.warn(f'vo {line["id"]}', 'speaks through the drop before the peak: keep that pause clean')


def check_cta(root, data, shots, spans, game_dir, rep):
    cta = data.get('cta')
    if not rep.need(isinstance(cta, dict), 'cta', 'missing'):
        return
    status = (data.get('game') or {}).get('build_status')
    for key in ('title', 'availability', 'directive'):
        rep.need(nonempty(cta.get(key)), 'cta', f'{key} is empty')
    platforms = cta.get('platforms')
    rep.need(isinstance(platforms, list) and platforms and all(nonempty(p) for p in platforms),
             'cta', 'exact platforms required')
    directive = cta.get('directive') or ''
    rep.need(len(words(directive)) <= CTA_MAX_DIRECTIVE_WORDS, 'cta',
             f'directive over {CTA_MAX_DIRECTIVE_WORDS} words')
    rep.need(not re.search(r',|;|&|\band\b|\bor\b', directive, re.I), 'cta',
             'one directive, one action — not a list of requests')
    address = cta.get('address')
    rep.need(address is None or nonempty(address), 'cta', 'address, if given, must be a non-empty string')
    rep.need((1 if address else 0) + len(re.findall(r'https?://|www\.|\.com\b|\.io\b|\.org\b',
                                                   directive + ' ' + (cta.get('availability') or ''))) <= 1, 'cta',
             'at most one address on the card (put it in cta.address, not in the directive)')
    for text in (directive, cta.get('availability') or ''):
        for adj in banned_in(text):
            rep.fail('cta', f'adjective claim "{adj}"')
    availability = (cta.get('availability') or '').lower()
    if status == 'prototype':
        rep.need('prototype' in availability, 'cta', 'build_status is prototype: availability must say "prototype"')
    if status == 'demo':
        rep.need('demo' in availability, 'cta', 'build_status is demo: availability must say "demo"')
    sources = cta.get('sources')
    if rep.need(isinstance(sources, dict), 'cta.sources', 'every card fact needs a recorded source'):
        for key in ('platforms', 'availability', 'directive') + (('address',) if address else ()):
            src = sources.get(key)
            if not rep.need(isinstance(src, dict) and src.get('source') in CTA_SOURCES and nonempty(src.get('ref')),
                            'cta.sources', f'{key} needs source in {sorted(CTA_SOURCES)} and a ref'):
                continue
            if key == 'platforms' and src['source'] == 'export_presets.cfg':
                declared = export_platforms(game_dir)
                if declared is None:
                    rep.warn('cta.sources', 'pass --game to verify platforms against export_presets.cfg')
                elif declared:
                    wrong = [p for p in (platforms or []) if not any(p.lower() in d or d in p.lower() for d in declared)]
                    rep.need(not wrong, 'cta.sources', f'not in export_presets.cfg: {wrong}')
                else:
                    rep.fail('cta.sources', 'source says export_presets.cfg but the project has none')
    last = shots[-1]
    props = ((last.get('card') or {}).get('props')) or {}
    rep.need(last.get('kind') == 'card' and props.get('kind') == 'endcard', 'cta',
             'the final shot must be the end card (GameTrailerCard kind "endcard") — never a fade to black')
    for key in ('title', 'availability', 'directive'):
        rep.need(props.get(key) == cta.get(key), 'cta', f'end card {key} differs from the cta block')
    rep.need(props.get('platforms') == cta.get('platforms'), 'cta', 'end card platforms differ from the cta block')
    rep.need((props.get('address') or None) == (address or None), 'cta', 'end card address differs from the cta block')
    start, end = spans[last['id']]
    needed = max(CTA_MIN_HOLD_S, CTA_S_PER_WORD * len(words(' '.join([
        cta.get('title') or '', ' '.join(platforms or []), cta.get('availability') or '', directive,
        address or '']))))
    rep.need(end - start >= needed - 0.001, 'cta', f'hold the end card at least {needed:.1f} s so it can be read')


def verify(root, min_height=2160, game_dir=None, require_viewer_test=False):
    root = Path(root).resolve()
    rep = Report()
    path = root / 'trailer.json'
    if not path.is_file():
        rep.fail('trailer.json', 'missing')
        return finish(rep, {})
    data = json.loads(path.read_text())
    rep.need(isinstance(data, dict) and data.get('schema_version') == 1, 'trailer.json', 'expected schema_version 1')
    game = data.get('game') if isinstance(data.get('game'), dict) else {}
    rep.need(nonempty(game.get('name')), 'game', 'missing name')
    build_id = game.get('build_id', '')
    rep.need(isinstance(build_id, str) and re.fullmatch(r'[a-f0-9]{64}', build_id), 'game',
             'build_id must be a source-snapshot SHA-256')
    rep.need(game.get('build_status') in BUILD_STATUS, 'game', f'build_status must be one of {sorted(BUILD_STATUS)}')
    kind = data.get('type')
    rep.need(kind in TYPES, 'type', f'must be one of {sorted(TYPES)}')
    check_presentation(data, rep)
    verb_ids = check_brief(data, rep)
    implemented, planned = check_features(data, rep)
    caps = check_captures(root, data, build_id, min_height, rep)

    shots = data.get('shots')
    if not rep.need(isinstance(shots, list) and len(shots) >= 5, 'shots', 'need the hook→cta structure (>= 5 shots)'):
        return finish(rep, data)
    if not all(isinstance(s, dict) and nonempty(s.get('id')) for s in shots):
        rep.fail('shots', 'every shot needs an id')
        return finish(rep, data)
    ids = [s['id'] for s in shots]
    rep.need(len(set(ids)) == len(ids), 'shots', 'duplicate shot ids')
    spans, total = timeline(shots)

    # ---- structure: hook → establish → escalate → peak → title → button → cta
    roles = [s.get('role') for s in shots]
    if rep.need(all(r in ROLE_ORDER for r in roles), 'structure', f'roles must be in {ROLE_ORDER}'):
        order = [ROLE_ORDER.index(r) for r in roles]
        rep.need(order == sorted(order), 'structure', 'roles out of order (hook, establish, escalate, peak, title, button, cta)')
        for needed_role in REQUIRED_ROLES:
            rep.need(needed_role in roles, 'structure', f'missing a {needed_role} shot')
        rep.need(roles[-1] == 'cta' and roles.count('cta') == 1, 'structure', 'exactly one cta shot, last')
        rep.need(roles[0] == 'hook', 'structure', 'open on the hook — no logos, splash or establishing pan first')
        if 'title' in roles and 'peak' in roles:
            rep.need(roles.index('title') > max(i for i, r in enumerate(roles) if r == 'peak'), 'structure',
                     'the title comes after the peak')

    # ---- runtime
    lo, hi = TYPES.get(kind, (30, 90))
    rep.need(HARD_MIN_S <= total <= HARD_MAX_S, 'runtime', f'{total:.1f}s is outside {HARD_MIN_S:.0f}–{HARD_MAX_S:.0f}s')
    if HARD_MIN_S <= total <= HARD_MAX_S and not (lo <= total <= hi):
        rep.warn('runtime', f'{total:.1f}s is outside the {lo}–{hi}s window for a {kind} trailer — '
                            'every second beyond it must be earning its place')

    # ---- per-shot
    text_total, flashes, debug_s, holds = 0, 0, 0.0, 0
    seen_windows = {}
    last_intensity = None
    shown_features, shown_verbs = set(), set()
    for shot in shots:
        sid, role = shot['id'], shot.get('role')
        where = f'shot {sid}'
        t0, t1 = spans[sid]
        dur = t1 - t0
        for adj in banned_in(shot.get('text', '')):
            rep.fail(where, f'adjective claim "{adj}" — show the evidence instead')
        if nonempty(shot.get('text')):
            n = len(words(shot['text']))
            text_total += n
            rep.need(n <= MAX_TEXT_WORDS, where, f'text over {MAX_TEXT_WORDS} words — text is a tax')
            rep.need(dur >= 0.5 + 0.3 * n, where, f'{n} words need {0.5 + 0.3 * n:.1f} s on screen')
        if shot.get('kind') == 'card':
            rep.need(number(shot.get('duration_s')) and shot['duration_s'] > 0, where, 'card needs duration_s')
            rep.need(((shot.get('card') or {}).get('pattern')) == 'GameTrailerCard', where,
                     'cards use the GameTrailerCard pattern')
            if role != 'cta':
                rep.need(t0 >= NO_CARD_BEFORE_S, where, f'no card in the first {NO_CARD_BEFORE_S:.0f} s')
            continue
        if not rep.need(shot.get('kind') == 'gameplay', where, 'kind must be gameplay or card'):
            continue
        # gameplay shots
        cap = caps.get(shot.get('capture'))
        in_s, out_s = shot.get('in_s'), shot.get('out_s')
        if not rep.need(number(in_s) and number(out_s) and 0 <= in_s < out_s, where, 'needs 0 <= in_s < out_s'):
            continue
        if cap:
            rep.need(out_s <= cap[1]['duration_s'] + 0.001, where, 'window runs past the end of the capture')
        else:
            rep.fail(where, f'unknown or unverified capture "{shot.get("capture")}"')
        hold = shot.get('hold_s')
        if hold is not None:
            holds += 1
            rep.need(number(hold) and 0 < hold <= MAX_HOLD_S, where, f'hold_s must be 0–{MAX_HOLD_S} s (one freeze, not slow motion)')
            rep.need(role in ('peak', 'escalate'), where, 'a freeze belongs at the peak')
        flash = bool(shot.get('flash'))
        flashes += flash
        floor = FLASH_MIN_S if flash else MIN_SHOT_S.get(role, 0.8)
        rep.need(dur >= floor - 1e-6, where, f'{dur:.2f}s is under the {floor:.1f}s legibility floor for a {role} shot')
        if flash:
            rep.need(role == 'peak', where, 'flash cuts belong in the peak only')
        rep.need(shot.get('screen') == 'gameplay', where,
                 'screen must be "gameplay" (menus, splash screens and loading are not the verb)')
        if role == 'hook':
            rep.need(nonempty(shot.get('verb')), where, 'the hook must show a verb in action')
        if role == 'button':
            rep.need(dur <= MAX_BUTTON_S, where, f'the button is a short beat (<= {MAX_BUTTON_S:.0f} s)')
        for key in ('situation', 'action', 'consequence'):
            if not flash:
                rep.need(nonempty(shot.get(key)), where, f'{key} is empty (situation → action → consequence)')
        if not flash:
            info = shot.get('new_information')
            rep.need(info in NEW_INFO and info != 'none', where,
                     f'new_information must be one of {sorted(NEW_INFO - {"none"})}: a shot that shows nothing new is cut')
        feature = shot.get('feature')
        if rep.need(nonempty(feature), where, 'name the implemented feature this shot shows'):
            rep.need(feature not in planned, where, f'"{feature}" is planned, not built — a trailer is a promise')
            rep.need(feature in implemented, where, f'"{feature}" is not in the feature inventory')
            shown_features.add(feature)
        if shot.get('verb'):
            rep.need(shot['verb'] in verb_ids, where, f'verb "{shot["verb"]}" is not in brief.verbs')
            shown_verbs.add(shot['verb'])
        rep.need(shot.get('camera') in ('player', 'debug'), where, 'camera must be player or debug')
        if shot.get('camera') == 'debug':
            debug_s += dur
            rep.need(nonempty(shot.get('disclosure')), where, 'a camera the player cannot have needs a disclosure')
            rep.need(role not in ('hook', 'peak'), where, 'hook and peak use the player camera')
        rep.need(shot.get('hud') in ('kept', 'hidden'), where, 'hud must be kept or hidden')
        if shot.get('hud') == 'hidden':
            rep.need(nonempty(shot.get('hud_reason')), where, 'hidden HUD needs a reason (clutter only, never a mechanic)')
        rep.need(shot.get('debug_overlay') is False, where, 'debug_overlay must be explicitly false (FPS, colliders, prints)')
        if shot.get('sound_dependent'):
            rep.need(nonempty(shot.get('visual_equivalent')), where, 'must also read with the sound off')
        if role in ('establish', 'escalate', 'peak') and not flash:
            level = shot.get('intensity')
            if rep.need(isinstance(level, int) and 1 <= level <= 5, where, 'intensity must be an integer 1–5'):
                if last_intensity is not None and level < last_intensity and not shot.get('contrast'):
                    rep.fail(where, f'intensity falls {last_intensity}→{level}; escalate one idea, or mark a deliberate contrast')
                last_intensity = level
        # a shot that re-shows footage already used shows nothing new
        windows = seen_windows.setdefault(shot.get('capture'), [])
        for (a, b) in windows:
            overlap = min(b, out_s) - max(a, in_s)
            if overlap > 0.5 * min(b - a, out_s - in_s):
                rep.fail(where, f'reuses source {a:.2f}–{b:.2f}s from {shot.get("capture")}')
        windows.append((in_s, out_s))
        if cap and shot.get('role') == 'hook' and t0 == 0:
            luma = first_frame_luma(cap[0], in_s)
            if luma is not None:
                rep.need(luma >= FIRST_FRAME_MIN_LUMA, where, f'first frame is nearly black ({luma:.2f}) — no fade in from black')
    rep.need(flashes <= MAX_FLASH, 'pacing', f'{flashes} flash cuts; max {MAX_FLASH}')
    rep.need(holds <= 1, 'pacing', 'at most one freeze per trailer')
    if total:
        rep.need(debug_s / total <= MAX_DEBUG_CAMERA_SHARE, 'honesty', 'too much non-player-camera footage')
    rep.need(text_total <= MAX_TOTAL_TEXT_WORDS, 'text', f'{text_total} words of text; the budget is {MAX_TOTAL_TEXT_WORDS}')

    # ---- hook, genre, verbs, features
    hook_t = [spans[s['id']][0] for s in shots if s.get('shows_hook')]
    rep.need(bool(hook_t) and min(hook_t) <= HOOK_BY_S, 'hook', f'show the hook (shows_hook) by {HOOK_BY_S:.0f} s')
    genre_t = [spans[s['id']][0] for s in shots if s.get('establishes_genre')]
    rep.need(bool(genre_t) and min(genre_t) <= GENRE_BY_S, 'hook', f'establish the genre by {GENRE_BY_S:.0f} s')
    for verb in sorted(verb_ids - shown_verbs):
        rep.fail('verbs', f'"{verb}" is a core verb but never shown')
    cut = {c.get('feature') for c in data.get('cuts', []) if isinstance(c, dict)}
    for feature in sorted(implemented - shown_features - cut):
        rep.warn('cuts', f'implemented feature "{feature}" is neither shown nor logged in cuts[] with a reason')
    early = [s for s in shots if spans[s['id']][0] < total * 0.4 and s.get('kind') == 'gameplay']
    if early and sum(1 for s in early if spans[s['id']][1] - spans[s['id']][0] < 1.0) / len(early) > 0.3:
        rep.warn('pacing', 'over 30% of the first 40% is sub-second cutting — establish the game before you speed up')

    check_music(root, data, total, spans, shots, rep)
    check_vo(root, data, shots, spans, total, rep)
    mix = data.get('mix')
    mix_path = contained(root, mix) if mix else None
    if mix_path:
        try:
            rep.need(abs(probe(mix_path)['duration_s'] - total) <= 0.15, 'mix',
                     f'mix length differs from the {total:.2f}s timeline')
        except (subprocess.SubprocessError, OSError, ValueError, KeyError):
            rep.fail('mix', 'unreadable')
        drop = (data.get('music') or {}).get('drop')
        if isinstance(drop, dict) and number(drop.get('start_s')) and number(drop.get('end_s')):
            quiet = window_rms(mix_path, drop['start_s'], drop['end_s'])
            before = window_rms(mix_path, max(drop['start_s'] - 3, 0), drop['start_s'])
            if quiet is not None and before:
                if quiet > 0.6 * before:
                    rep.warn('music.drop', 'the mix is not noticeably quieter in the declared drop')
    else:
        rep.warn('mix', 'no mix yet (audio/trailer-mix.wav); required before a final')

    check_cta(root, data, shots, spans, game_dir, rep)

    # ---- the tests only people can run
    checks = data.get('checks') if isinstance(data.get('checks'), dict) else {}
    muted = checks.get('muted_test') or {}
    if muted.get('status') == 'done':
        rep.need(nonempty(muted.get('notes')), 'checks', 'muted_test done but no notes')
    else:
        rep.warn('checks', 'muted test pending: the premise and the key information must survive with the sound off')
    viewer = checks.get('viewer_test') or {}
    if viewer.get('status') == 'done':
        rows = viewer.get('viewers') or []
        rep.need(len(rows) >= 2 and any(v.get('sound') == 'off' for v in rows) and
                 any(v.get('sound') == 'on' for v in rows), 'checks',
                 'viewer test needs >= 2 viewers who had never seen the game, one with the sound off')
        for v in rows:
            rep.need(all(nonempty(v.get(k)) for k in ('id', 'genre_at_10s', 'player_does', 'what_is_different')), 'checks',
                     'each viewer needs id, genre_at_10s, player_does and what_is_different')
        rep.need(all(v.get('outcome') == 'pass' for v in rows), 'checks',
                 'a viewer could not describe the game: revise the footage and sequence before adding polish')
    else:
        (rep.fail if require_viewer_test else rep.warn)(
            'checks', 'viewer test pending: until a stranger answers the three questions, this trailer is NOT audience-tested')
    return finish(rep, data, total=total, shots=len(shots), spans=spans)


def finish(rep, data, **extra):
    status = 'FAIL' if rep.fails else 'PASS'
    return {'status': status, 'fails': rep.fails, 'warnings': rep.warns,
            'runtime_s': round(extra.get('total', 0.0), 3), 'shots': extra.get('shots', 0),
            'scope': 'Structure, honesty attestations and media evidence only. Legibility, tone, '
                     'music fit, bugs in frame, and whether a stranger understands the game still '
                     'need frame review and a human viewer test.'}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('reel', type=Path)
    parser.add_argument('--game', type=Path, help='game package or project dir (verifies CTA platforms)')
    parser.add_argument('--min-height', type=int, default=2160,
                        help='pilot/test override only; final trailers need native 2160p footage')
    parser.add_argument('--require-viewer-test', action='store_true',
                        help='turn the pending human viewer test into a failure (use at handoff)')
    parser.add_argument('--strict', action='store_true', help='treat warnings as failures')
    args = parser.parse_args()
    try:
        report = verify(args.reel, args.min_height, args.game, args.require_viewer_test)
    except (OSError, ValueError, subprocess.SubprocessError, KeyError, TypeError) as exc:
        print(f'Trailer evidence FAIL: {exc}', file=sys.stderr)
        return 1
    print(json.dumps(report, indent=2))
    return 1 if report['fails'] or (args.strict and report['warnings']) else 0


if __name__ == '__main__':
    sys.exit(main())
