#!/usr/bin/env python3
"""seis_composite.py — the seis-composite skill's engine (skills/make/seis-composite).

  python3 seis_composite.py plan.json --out film.mp4
plan.json (the editing brief's timeline as data):
  {"open": {"eyebrow": "SEIS · Alumni", "lines": ["Look what our people", "have gone on to do."], "seconds": 4},
   "sections": [{"eyebrow": "Who they are now", "lines": [...optional card...], "seconds": 2.5, "clips": ["clips/jay-01.mp4", ...]}, ...],
   "stat": {"eyebrow": "SEIS", "lines": ["112 spotlight stories", "…"], "emphasis": 0, "seconds": 4},          # optional, before the closing beat
   "bridge": {"lines": ["The name is changing.", "The mission isn’t."], "emphasis": 1, "seconds": 3, "dark": true},
   "end_seconds": 10, "music": "path/to/bed.mp3", "music_gain": 0.12}
Clips are the seis-extract outputs (or any mp4). Warns on any clip > 15 s. Composition SeisFilm. Never publishes.
"""
import argparse, json, math, shutil, subprocess, sys
from pathlib import Path
HERE = Path(__file__).resolve().parent; TOOLKIT = HERE.parent.parent
REM = TOOLKIT / 'runtime' / 'remotion'; PUB = REM / 'public' / 'seis-film'; FPS = 30

def dur(p): return float(subprocess.run(['ffprobe', '-v', 'error', '-show_entries', 'format=duration', '-of', 'csv=p=0', str(p)], capture_output=True, text=True).stdout.strip())
def card(c, default_s=2.5, dark=False):
    return {'kind': 'card', 'frames': int(math.ceil(c.get('seconds', default_s) * FPS)), 'src': '', 'audio': '', 'duck': False, 'eyebrow': c.get('eyebrow', ''), 'lines': c.get('lines', []), 'emphasis': c.get('emphasis', -1), 'dark': c.get('dark', dark)}

def voiced(it, spec, stem):
    """Attach Bella narration to a card and stretch the card to fit her read.
    `narration_speed` overrides the global read speed for this card only (a long quote needs pace)."""
    if not spec.get('narration'): return it
    it['audio'], d = narrate(spec['narration'], stem, spec.get('narration_speed'))
    it['frames'] = max(it['frames'], int(math.ceil((d + 1.5) * FPS))); it['duck'] = True
    return it

def narrate(text, stem, speed=None):
    """Bella speaks the card. AUDIO-FIRST: the mp3's length is the card's clock."""
    sys.path.insert(0, str(HERE))
    from seis_extract import ask_voice, ASK_SPEED
    mp3 = PUB / f'{stem}.mp3'
    return f'seis-film/{mp3.name}', ask_voice(text, mp3, speed=float(speed) if speed else ASK_SPEED)

def main():
    ap = argparse.ArgumentParser(); ap.add_argument('plan'); ap.add_argument('--out', required=True); a = ap.parse_args()
    plan = json.loads(Path(a.plan).read_text()); base = Path(a.plan).parent; PUB.mkdir(parents=True, exist_ok=True)
    items = []
    if plan.get('logo'):
        items.append({'kind': 'logo', 'frames': int(math.ceil(plan['logo'].get('seconds', 4.5) * FPS)), 'src': '', 'audio': '', 'duck': False,
                      'eyebrow': '', 'lines': [], 'emphasis': -1, 'dark': True})
    if plan.get('open'):
        it = card(plan['open'], 4)
        if plan['open'].get('narration'):
            it['audio'], d = narrate(plan['open']['narration'], 'open-vo')
            it['frames'] = int(math.ceil((d + 1.4) * FPS)); it['duck'] = True
        items.append(it)
    for sec in plan.get('sections', []):
        if sec.get('lines'): items.append(card(sec))
        for c in sec.get('clips', []):
            src = (base / c) if not Path(c).is_absolute() else Path(c); d = dur(src)
            if d > 15.5 + 6: print(f"  ! {src.name}: {d:.1f}s total — answer likely over the brief's 15 s cap")
            dst = PUB / src.name; shutil.copy2(src, dst)
            items.append({'kind': 'clip', 'frames': int(math.floor(d * FPS)), 'src': f'seis-film/{dst.name}', 'audio': '', 'duck': True, 'eyebrow': '', 'lines': [], 'emphasis': -1, 'dark': False})
    if plan.get('stat'): items.append(voiced(card(plan['stat'], 4), plan['stat'], 'stat-vo'))
    if plan.get('bridge'): items.append(voiced(card(plan['bridge'], 3, dark=True), plan['bridge'], 'bridge-vo'))
    if plan.get('end_logo'):
        # the brief's close: logo resolving out of blur, nothing else
        items.append({'kind': 'logo', 'frames': int(math.ceil(float(plan.get('end_logo_seconds', 4.5)) * FPS)), 'src': '', 'audio': '', 'duck': False,
                      'eyebrow': '', 'lines': [], 'emphasis': -1, 'dark': True})
        plan['_skip_end'] = True
    end_it = {'kind': 'end', 'frames': int(plan.get('end_seconds', 10) * FPS), 'src': '', 'audio': '', 'duck': False, 'eyebrow': '', 'lines': [], 'emphasis': -1, 'dark': False}
    if plan.get('end_narration') and not plan.get('_skip_end'):
        end_it['audio'], d = narrate(plan['end_narration'], 'end-vo'); end_it['duck'] = True
        end_it['frames'] = int(math.ceil(max(plan.get('end_seconds', 10), d + 2.0) * FPS))
    if not plan.get('_skip_end'): items.append(end_it)
    music = ''
    if plan.get('music'):
        m = Path(plan['music']); m = m if m.is_absolute() else (base / m)   # relative to the plan, like clips
        dst = PUB / m.name; shutil.copy2(m, dst); music = f'seis-film/{dst.name}'
    props = {'items': items, 'music': music, 'musicGain': plan.get('music_gain', 0.12), 'musicDuck': plan.get('music_duck', 0.035)}
    pj = Path(a.out).with_suffix('.props.json'); pj.write_text(json.dumps(props, ensure_ascii=False))
    total = sum(i['frames'] for i in items); print(f"{len(items)} items · {total/FPS:.1f}s")
    r = subprocess.run(['npx', 'remotion', 'render', 'src/index.ts', 'SeisFilm', str(Path(a.out).resolve()), f'--props={pj.resolve()}', '--codec=h264', '--crf=18', '--concurrency=2', '--timeout=300000', '--log=error'], cwd=str(REM), capture_output=True, text=True)
    if r.returncode != 0: sys.exit(r.stderr[-1500:])
    print('wrote', a.out, f'({dur(a.out):.1f}s)')

if __name__ == '__main__': main()
