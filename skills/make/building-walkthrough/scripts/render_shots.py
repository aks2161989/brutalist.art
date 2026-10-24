#!/usr/bin/env python3
"""Render a rigged walkthrough, one numbered image sequence per shot, and time frames.

  render_shots.py RIGGED.blend ROUTE.json --out renders [--engine CYCLES] [--samples 128]
                  [--percent 100] [--shots S01,S03] [--format PNG]
  render_shots.py RIGGED.blend ROUTE.json --time 120:interior 500:exterior 800:detail
                  [--engine CYCLES] [--samples 128] [--percent 100] [--out budget.json]

Final animation goes to numbered images, not straight to a movie: if the render stops, every
finished frame is still on disk and a re-run skips them (Overwrite off, Placeholders on).
Images land in OUT/<shot id>/####.<ext> with the frame numbers of the timeline, which is what
verify_walkthrough.py --renders expects.

`--time` renders single frames to a scratch folder and writes `samples_measured` for the
walkthrough.json budget, taken from Blender's own "Time:" line (render time, not start-up).
A timing is for THIS engine, sample count, percent and machine: change any and re-time.
The rig must come from camera_rig.py; this script never edits the .blend."""
import argparse
import json
import os
from pathlib import Path
import re
import shutil
import subprocess
import sys
import tempfile
import time

BLENDER = os.environ.get('BLENDER') or '/Applications/Blender.app/Contents/MacOS/Blender'
EXT = {'PNG': 'png', 'OPEN_EXR': 'exr', 'JPEG': 'jpg'}
TIME_LINE = re.compile(r'Time:\s*(?:(\d+):)?(\d+):(\d+(?:\.\d+)?)')


def setup_expr(engine, samples, percent, fmt):
    parts = ['import bpy', 's = bpy.context.scene', 'r = s.render',
             f'r.engine = {engine!r}', f'r.resolution_percentage = {int(percent)}',
             'r.use_overwrite = False', 'r.use_placeholder = True',
             f'r.image_settings.file_format = {fmt!r}']
    if samples:
        parts.append(f's.cycles.samples = {int(samples)}' if engine == 'CYCLES'
                     else f's.eevee.taa_render_samples = {int(samples)}' if engine == 'BLENDER_EEVEE'
                     else 'pass')
    return '; '.join(parts)


def parse_time(output):
    last = None
    for m in TIME_LINE.finditer(output):
        h, mnt, sec = m.groups()
        last = int(h or 0) * 3600 + int(mnt) * 60 + float(sec)
    return last


def run(blend, expr, extra):
    cmd = [BLENDER, '-b', str(blend), '--python-expr', expr] + extra
    t0 = time.time()
    p = subprocess.run(cmd, capture_output=True, text=True)
    return p, time.time() - t0


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__.split('\n\n')[0])
    ap.add_argument('blend')
    ap.add_argument('route')
    ap.add_argument('--out', default='renders')
    ap.add_argument('--engine', default='CYCLES', choices=['CYCLES', 'BLENDER_EEVEE', 'BLENDER_WORKBENCH'])
    ap.add_argument('--samples', type=int)
    ap.add_argument('--percent', type=int, default=100)
    ap.add_argument('--format', default='PNG', choices=sorted(EXT))
    ap.add_argument('--shots', help='comma-separated shot ids (default: all)')
    ap.add_argument('--time', nargs='+', metavar='FRAME[:kind]',
                    help='time these frames instead of rendering the sequences')
    a = ap.parse_args(argv)
    route = json.loads(Path(a.route).read_text())
    blend = Path(a.blend).resolve()
    expr = setup_expr(a.engine, a.samples, a.percent, a.format)

    if a.time:
        scratch = Path(tempfile.mkdtemp(prefix='walkthrough-time-'))
        results = []
        try:
            for item in a.time:
                frame, _, kind = item.partition(':')
                p, wall = run(blend, expr, ['-o', str(scratch / '####'), '-f', frame])
                spf = parse_time(p.stdout)
                if p.returncode != 0 or spf is None:
                    print(f'frame {frame}: render failed or no "Time:" line\n{p.stdout[-600:]}', file=sys.stderr)
                    return 1
                results.append({'frame': int(frame), 'kind': kind or 'unlabelled',
                                'sec_per_frame': round(spf, 2)})
                print(f'frame {frame} ({kind or "unlabelled"}): {spf:.1f} s')
        finally:
            shutil.rmtree(scratch, True)
        doc = {'engine': a.engine, 'samples': a.samples, 'percent': a.percent,
               'machine': os.uname().nodename, 'blender_file': str(blend),
               'samples_measured': results}
        Path(a.out if a.out.endswith('.json') else 'budget.json').write_text(json.dumps(doc, indent=2) + '\n')
        return 0

    want = set(a.shots.split(',')) if a.shots else None
    out = Path(a.out).resolve()
    ext = EXT[a.format]
    for shot in route['shots']:
        if want and shot['id'] not in want:
            continue
        f0, f1 = shot['frames']
        d = out / shot['id']
        d.mkdir(parents=True, exist_ok=True)
        p, wall = run(blend, expr, ['-o', str(d / '####'), '-s', str(f0), '-e', str(f1), '-a'])
        done = len(list(d.glob(f'*.{ext}')))
        print(f"{shot['id']}: {done}/{f1 - f0 + 1} frames in {d} ({wall:.0f} s wall)")
        if p.returncode != 0 or done != f1 - f0 + 1:
            print(p.stdout[-800:], file=sys.stderr)
            return 1
    return 0


if __name__ == '__main__':
    sys.exit(main())
