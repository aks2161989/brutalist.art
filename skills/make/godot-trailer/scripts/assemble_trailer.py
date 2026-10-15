#!/usr/bin/env python3
"""assemble_trailer.py — turn a gated trailer.json into the files the compiler reads.

    python3 assemble_trailer.py REEL                # trim + beat_sheet.json + cards + mix
    python3 assemble_trailer.py REEL --only clips   # or: sheet | cards | vo | mix

Mechanical only; every decision is already in trailer.json. It never retimes
gameplay: each shot is its source window at normal speed, cut frame-exact
(re-encoded, so the cut is on the frame you named) into media/<shot id>.mp4.
Cards (GameTrailerCard) render through runtime/scripts/remotion_scenes.py.
The mix is music ducked under the game's own audio and any voiceover (Liam lines from
vo_kokoro.py), loudness-normalised, written to audio/trailer-mix.wav at exactly the timeline length
for `art final --audio`.

Run verify_trailer.py first. Then:
    ./art final REEL --height 2160 --fps 30 --audio REEL/audio/trailer-mix.wav --out REEL/exports/landscape
"""
import argparse
import json
from pathlib import Path
import subprocess
import sys

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
from verify_trailer import timeline, probe, contained   # noqa: E402
import vo_kokoro                                         # noqa: E402

ART = HERE.parents[3]                                    # brutalist.art/
FPS = 30
TARGET_LUFS, TARGET_TP = -16.0, -2.0   # AAC encoding adds about 0.5 dB of peak


def run(cmd):
    proc = subprocess.run([str(c) for c in cmd], capture_output=True, text=True)
    if proc.returncode != 0:
        raise SystemExit(f'FAILED: {" ".join(str(c) for c in cmd[:6])} …\n{proc.stderr[-1500:]}')
    return proc


def frames(seconds):
    return round(seconds * FPS)


def presentation_filter(pres):
    """Optional inset: the 4K capture is scaled into the title-safe box and matted with the game's own
    background colour, so GATE T sees the game's edge-hugging HUD inside the safe area. Native pixels are
    kept (3456 px wide at 0.9); nothing is cropped or retimed."""
    if not pres:
        return ''
    inner_w = int(round(3840 * pres['inset'] / 2) * 2)
    inner_h = int(round(2160 * pres['inset'] / 2) * 2)
    color = pres['pad_color'].lstrip('#')
    return (f',scale={inner_w}:{inner_h}:flags=lanczos,'
            f'pad=3840:2160:{(3840 - inner_w) // 2}:{(2160 - inner_h) // 2}:color=0x{color}')


def trim_clips(root, data, force):
    caps = data['captures']
    (root / 'media').mkdir(exist_ok=True)
    for shot in data['shots']:
        if shot['kind'] != 'gameplay':
            continue
        out = root / 'media' / f'{shot["id"]}.mp4'
        hold = shot.get('hold_s') or 0.0
        n = frames(shot['out_s'] - shot['in_s'] + hold)
        if out.exists() and not force and probe(out).get('duration_s'):
            continue
        vf = f'fps={FPS}' + (f',tpad=stop_mode=clone:stop_duration={hold:.3f}' if hold else '')
        vf += presentation_filter(data.get('presentation'))
        run(['ffmpeg', '-y', '-v', 'error', '-ss', f'{shot["in_s"]:.4f}', '-i', root / caps[shot['capture']]['path'],
             '-vf', vf, '-frames:v', n, '-c:v', 'libx264', '-preset', 'slow', '-crf', 12,
             '-pix_fmt', 'yuv420p', '-an', out])
        got = run(['ffprobe', '-v', 'error', '-count_frames', '-select_streams', 'v:0',
                   '-show_entries', 'stream=nb_read_frames', '-of', 'csv=p=0', out]).stdout.strip()
        if int(got) != n:
            raise SystemExit(f'{shot["id"]}: trimmed {got} frames, expected {n}')
        print(f'  {shot["id"]}: {shot["capture"]} {shot["in_s"]:.3f}–{shot["out_s"]:.3f}s → {n} frames')


def write_sheet(root, data):
    game = data['game']
    spans, total = timeline(data['shots'])
    beats = []
    for shot in data['shots']:
        t0, t1 = spans[shot['id']]
        n = frames(t1 - t0)
        beat = {'beat_id': shot['id'], 'act': shot['role'].upper(), 'narration_text': '',
                'audio_policy': 'silence', 'actual_duration_s': n / FPS, 'render_duration_s': n / FPS}
        if shot['kind'] == 'gameplay':
            cap = data['captures'][shot['capture']]
            beat['shot'] = {'type': 'FOOTAGE', 'source': 'own', 'lane': 'footage', 'classification': 'SHOW',
                            'visual_intent': f'{shot["situation"]} → {shot["action"]} → {shot["consequence"]}. '
                                             'Real Godot capture, normal speed, no retiming.',
                            'show': [{'at': 0, 'event': shot['consequence']}],
                            'evidence_media': f'media/{shot["id"]}.mp4'}
            beat['source_capture'] = shot['capture']
            beat['source_frames'] = [round(shot['in_s'] * cap.get('fps', FPS)), round(shot['out_s'] * cap.get('fps', FPS))]
            beat['source_fps'] = cap.get('fps', FPS)
            beat['kind'] = 'trailer_gameplay'
            pres = data.get('presentation')
            if pres:
                beat['qc'] = {'full_bleed': False, 'contrast_regions': pres['contrast_regions'],
                              'contrast_reason': pres['contrast_reason']}
            else:
                beat['qc'] = {'full_bleed': True}
        else:
            beat['shot'] = {'type': 'REMOTION', 'source': 'own', 'lane': 'card', 'classification': 'SHOW',
                            'visual_intent': f'{shot["role"]} card from the verified cta block.',
                            'show': [{'at': 0, 'event': f'{shot["role"]} card'}],
                            'remotion': {'pattern': shot['card']['pattern'], 'props': shot['card']['props']}}
            beat['kind'] = 'trailer_card'
            # A title or end card is a few words on a plain ground by design (text is a tax; one dominant
            # action). GATE V's underfill/clustered checks are waived for it, in the sheet, with the reason.
            beat['qc'] = {'sparse_by_design': True,
                          'sparse_reason': f'{shot["role"]} card: a few words on a plain ground by design; '
                                           'edge-bleed, contrast and empty-frame checks still apply.'}
        beats.append(beat)
    slug = data.get('slug') or root.name
    sheet = {'metadata': {'slug': slug, 'title': game['name'] + ' — trailer', 'fps': FPS, 'aspect_ratio': '16:9',
                          'width': 3840, 'height': 2160, 'caption_policy': 'none', 'fit': 'pad',
                          'skill': 'godot-trailer', 'trailer_type': data.get('type'),
                          'authorization': 'Local trailer production only; no paid generation or publication.',
                          'human_review_approved': False},
             'beats': beats}
    (root / 'beat_sheet.json').write_text(json.dumps(sheet, indent=1))
    print(f'  beat_sheet.json: {len(beats)} beats, {total:.2f}s ({frames(total)} frames)')


def render_cards(root):
    cards = [b for b in json.loads((root / 'beat_sheet.json').read_text())['beats']
             if (b['shot'].get('remotion') or {}).get('pattern')]
    if cards:
        proc = subprocess.run([sys.executable, ART / 'runtime/scripts/remotion_scenes.py', root])
        if proc.returncode != 0:
            raise SystemExit('remotion_scenes.py failed')


def build_mix(root, data):
    spans, total = timeline(data['shots'])
    music = data.get('music') or {}
    track = contained(root, music.get('path')) if music.get('source') in ('game', 'supplied', 'generated') else None
    caps = data['captures']
    game_inputs, game_delays = [], []
    for shot in data['shots']:
        if shot['kind'] != 'gameplay':
            continue
        cap_path = root / caps[shot['capture']]['path']
        if probe(cap_path).get('has_audio'):
            game_inputs.append((cap_path, shot['in_s'], shot['out_s'] - shot['in_s']))
            game_delays.append(int(spans[shot['id']][0] * 1000))
    vo_inputs = []
    if data.get('vo'):
        manifest_path = root / 'audio/vo/manifest.json'
        if not manifest_path.is_file():
            raise SystemExit('vo lines declared but audio/vo/manifest.json is missing: run the vo step first')
        manifest = json.loads(manifest_path.read_text())
        for line in data['vo']['lines']:
            start = spans[line['shot']][0] + line['at_s']
            vo_inputs.append((root / manifest[line['id']]['wav'], int(round(start * 1000))))
    if not track and not game_inputs and not vo_inputs:
        print('  no music, no game audio and no voice: nothing to mix (the trailer would be silent)')
        return
    (root / 'audio').mkdir(exist_ok=True)
    out = root / 'audio/trailer-mix.wav'
    cmd, parts = ['ffmpeg', '-y', '-v', 'error'], []
    idx = 0
    if track:
        cmd += ['-i', track]
        parts.append(f'[0:a]aresample=48000,aformat=channel_layouts=stereo,atrim=0:{total:.4f},'
                     f'afade=t=out:st={max(total - 1.0, 0):.3f}:d=1.0,apad,atrim=0:{total:.4f}[music]')
        idx = 1
    game_labels = []
    for k, (path, ss, dur) in enumerate(game_inputs):
        cmd += ['-ss', f'{ss:.4f}', '-t', f'{dur:.4f}', '-i', path]
        parts.append(f'[{idx}:a]aresample=48000,aformat=channel_layouts=stereo,'
                     f'afade=t=in:d=0.01,afade=t=out:st={max(dur - 0.01, 0):.3f}:d=0.01,'
                     f'adelay={game_delays[k]}|{game_delays[k]}[g{k}]')
        game_labels.append(f'[g{k}]')
        idx += 1
    vo_labels = []
    for k, (path, delay) in enumerate(vo_inputs):
        cmd += ['-i', path]
        parts.append(f'[{idx}:a]aresample=48000,aformat=channel_layouts=stereo,adelay={delay}|{delay}[v{k}]')
        vo_labels.append(f'[v{k}]')
        idx += 1
    buses = []
    if game_labels:
        parts.append(''.join(game_labels) + f'amix=inputs={len(game_labels)}:normalize=0,apad,atrim=0:{total:.4f}[game]')
        buses.append('[game]')
    if vo_labels:
        parts.append(''.join(vo_labels) + f'amix=inputs={len(vo_labels)}:normalize=0,apad,atrim=0:{total:.4f}[voice]')
        buses.append('[voice]')
    if len(buses) == 2:
        parts.append('[game][voice]amix=inputs=2:normalize=0[dry]')
        dry = '[dry]'
    else:
        dry = buses[0] if buses else None
    if track and dry:
        # the music steps down under the game's sounds and the voice, then comes back
        parts.append(f'{dry}asplit[dk][dm];[music][dk]sidechaincompress=threshold=0.02:ratio=10:attack=10:release=350[duck];'
                     '[duck][dm]amix=inputs=2:normalize=0[mixed]')
        last = '[mixed]'
    else:
        last = '[music]' if track else dry
    parts.append(f'{last}loudnorm=I={TARGET_LUFS}:TP={TARGET_TP}:LRA=11,aresample=48000,apad,atrim=0:{total:.4f}[out]')
    cmd += ['-filter_complex', ';'.join(parts), '-map', '[out]', '-ar', 48000, '-ac', 2, '-c:a', 'pcm_s16le', out]
    run(cmd)
    what = ' + '.join(n for n, on in (('music', bool(track)), ('game audio', bool(game_inputs)),
                                       (f'{len(vo_inputs)} voice lines', bool(vo_inputs))) if on)
    print(f'  audio/trailer-mix.wav: {probe(out)["duration_s"]:.3f}s for a {total:.3f}s timeline ({what})')


def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('reel', type=Path)
    parser.add_argument('--only', choices=['clips', 'sheet', 'cards', 'vo', 'mix'])
    parser.add_argument('--force', action='store_true', help='re-trim clips that already exist')
    args = parser.parse_args()
    root = args.reel.resolve()
    data = json.loads((root / 'trailer.json').read_text())
    steps = [args.only] if args.only else ['clips', 'sheet', 'cards', 'vo', 'mix']
    if 'clips' in steps:
        print('trimming'); trim_clips(root, data, args.force)
    if 'sheet' in steps:
        print('beat sheet'); write_sheet(root, data)
    if 'cards' in steps:
        print('cards'); render_cards(root)
    if 'vo' in steps and data.get('vo'):
        print('voice'); vo_kokoro.generate(root, force=args.force)
    if 'mix' in steps:
        print('mix'); build_mix(root, data)
    return 0


if __name__ == '__main__':
    sys.exit(main())
