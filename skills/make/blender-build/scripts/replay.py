"""Replay a tape: rebuild the model from the commands that built it, in a fresh Blender, and census
the result. This is the check that a record is a recipe. Runs INSIDE Blender (background):

  blender -b --factory-startup --python replay.py -- TAPE.jsonl --out replay.blend
          [--census replay-census.json] [--report replay-report.json]
          [--from N] [--to N] [--skip N,N] [--shared-namespace] [--allow-writes]

Then compare with the delivered model:  python3 census.py compare delivered-census.json replay-census.json

WHAT IT RUNS. Every tape line that changed the scene, succeeded, and carries code, in tape order, each
in a fresh namespace (the observed MCP commands each start with `import bpy`; use --shared-namespace if
a command relies on a variable from an earlier one). A command that raises stops the replay: the
record is not yet a recipe, and the report names the line.

WHAT IT REFUSES TO RUN. A replay re-executes what the tape did, and some commands WRITE FILES: they save
the .blend to its real path, export a glTF, render images, delete or create folders. Replaying those would
overwrite the very deliverable being checked. So any command that looks like a file write (save, export,
render, open for writing, os/shutil file operations, subprocess) is SKIPPED and listed in the report with
the reason. A command that both builds and writes is skipped whole; the census comparison then shows
whether anything was lost. `--allow-writes` runs them anyway: only inside a copy of the project, never
against the real one.

It starts from the factory scene (Blender's default Cube, Camera and Light), which is where a
recorded MCP session starts. It cannot see anything done in the interface, so a model touched by hand
after the tape will not match, and that is the point of the check."""
import argparse
import importlib.util
import json
import os
import re
import sys
import time
import traceback

WRITE_PATTERNS = [
    (r'save_as_mainfile|save_mainfile', 'saves a .blend'),
    (r'export_scene\.|wm\.\w+_export|wm\.usd_export|wm\.alembic_export|wm\.collada_export', 'exports a file'),
    (r'render\.render|render\.opengl|\.save_render\(', 'renders an image'),
    (r'\bopen\([^)]*[\'"][wax]\+?b?[\'"]', 'opens a file for writing'),
    (r'os\.(remove|rmdir|rename|unlink|makedirs|mkdir)|shutil\.', 'creates or deletes files or folders'),
    (r'subprocess|os\.system', 'runs another program'),
    (r'\.write\(|\.save\(', 'writes a file'),
]


def classify(code):
    """Return a reason string if the command looks like it writes files, else None."""
    for pat, why in WRITE_PATTERNS:
        if re.search(pat, code or ''):
            return why
    return None


def select(tape, lo=None, hi=None, allow_writes=False, skip=()):
    """Split tape lines into (to_run, skipped) without touching Blender."""
    run, skipped = [], []
    for rec in tape:
        seq = rec.get('seq')
        if (lo and seq < lo) or (hi and seq > hi):
            continue
        code = rec.get('code')
        if not code:
            continue
        if seq in skip:
            skipped.append({'seq': seq, 'why': 'skipped by --skip (a decision to record in the replay notes)'})
            continue
        if rec.get('mutates') is False:
            skipped.append({'seq': seq, 'why': 'a query: it does not change the scene'})
            continue
        if rec.get('status') == 'error':
            skipped.append({'seq': seq, 'why': 'the command failed when it was recorded'})
            continue
        tool = rec.get('tool', '')
        if not (tool in ('', 'execute_code') or tool.endswith('execute_blender_code')):
            skipped.append({'seq': seq, 'why': f'tool {tool!r} is not Python run inside Blender'})
            continue
        why = None if allow_writes else classify(code)
        if why:
            skipped.append({'seq': seq, 'why': f'looks like it writes files ({why})'})
            continue
        run.append(rec)
    return run, skipped


def load_census_module():
    here = os.path.dirname(os.path.abspath(__file__))
    spec = importlib.util.spec_from_file_location('bb_census_replay', os.path.join(here, 'census.py'))
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


def script_args():
    argv = sys.argv
    return argv[argv.index('--') + 1:] if '--' in argv else argv[1:]


def main():
    ap = argparse.ArgumentParser(prog='replay.py')
    ap.add_argument('tape')
    ap.add_argument('--out', required=True)
    ap.add_argument('--census')
    ap.add_argument('--report')
    ap.add_argument('--from', dest='lo', type=int)
    ap.add_argument('--to', dest='hi', type=int)
    ap.add_argument('--shared-namespace', action='store_true')
    ap.add_argument('--allow-writes', action='store_true')
    ap.add_argument('--skip', default='', help='comma-separated tape numbers to leave out, e.g. a command that only '
                    'reads a file that is not here; say why in reconstruction.replay.how')
    a = ap.parse_args(script_args())
    tape = [json.loads(x) for x in open(a.tape) if x.strip()]
    run, skipped = select(tape, a.lo, a.hi, a.allow_writes,
                          {int(x) for x in a.skip.split(',') if x.strip()})
    import bpy
    shared = {'__name__': '__main__'}
    ran, failed = [], None
    for rec in run:
        ns = shared if a.shared_namespace else {'__name__': '__main__'}
        t0 = time.time()
        try:
            exec(compile(rec['code'], f'<tape#{rec["seq"]}>', 'exec'), ns)
            ran.append({'seq': rec['seq'], 'seconds': round(time.time() - t0, 3)})
        except BaseException:
            failed = {'seq': rec['seq'], 'error': traceback.format_exc()[-800:]}
            break
    report = {'tape': os.path.abspath(a.tape), 'blender': bpy.app.version_string,
              'ran': ran, 'skipped': skipped, 'failed': failed, 'ok': failed is None,
              'namespace': 'shared' if a.shared_namespace else 'fresh per command',
              'writes_allowed': a.allow_writes}
    out = os.path.abspath(a.out)
    os.makedirs(os.path.dirname(out) or '.', exist_ok=True)
    bpy.ops.wm.save_as_mainfile(filepath=out)
    # Census what the saved file holds, not what is left in memory: a deleted object's mesh and
    # material linger in memory with no user and are dropped on save and reload.
    bpy.ops.wm.open_mainfile(filepath=out)
    if a.census:
        cm = load_census_module()
        doc = cm.census()
        with open(a.census, 'w') as fh:
            json.dump(doc, fh, indent=1)
        report['census_signature'] = doc['signature']
        report['totals'] = doc['totals']
    if a.report:
        with open(a.report, 'w') as fh:
            json.dump(report, fh, indent=1)
    print(f'replay: ran {len(ran)} command(s), skipped {len(skipped)}'
          + (f', FAILED at #{failed["seq"]}' if failed else '') + f' -> {out}')
    for s in skipped:
        print(f'  skipped #{s["seq"]}: {s["why"]}')
    if failed:
        print(failed['error'])
    sys.stdout.flush()
    os._exit(1 if failed else 0)


if __name__ == '__main__':
    main()
