#!/usr/bin/env python3
"""Read-only gate for a Blender build record (and the guide and film made from it).

  verify_breakdown.py build-record/record.json [--final] [--film] [--recensus]

Checks that the record can be believed: every step has a goal and a reason, a stated evidence tier
that its evidence actually backs, an interface route or an honest reason there is none, repeated
work stated as a rule and a table, corrections tied to what they corrected, outside assets credited,
stage milestones that show the same views every time, and verification claims (replay, followed by
hand) that match what was actually checked.

It CANNOT tell whether a goal or a reason is true, whether an interface route is correct (only that
it has not been followed unless the record says it was), or whether the model is good. Exit status 1
on any failure. `--final` is the handoff to the film: unwritten goals, untranslated lines and an
unverified record fail. `--film` checks that nothing inferred is told as history. `--recensus` runs
Blender on the final model and compares its census signature with the record (catches a model that
changed after the record was written)."""
import argparse
import hashlib
import json

import os
from pathlib import Path
import re
import subprocess
import sys

TIERS = {'recorded', 'scripted', 'inspected', 'demonstrated', 'inferred'}
KINDS = {'building', 'asset', 'environment'}
SOURCE_KINDS = {'tape', 'script', 'transcript'}
GUI_SOURCES = {'draft', 'human', 'none'}
HEX64 = re.compile(r'^[0-9a-f]{64}$')
STAGE_ID = re.compile(r'^\d{2}-[a-z0-9][a-z0-9-]*$')
BLENDER = os.environ.get('BLENDER') or '/Applications/Blender.app/Contents/MacOS/Blender'
CENSUS = Path(__file__).resolve().parent / 'census.py'


class Report:
    def __init__(self):
        self.fails, self.warns, self.notes = [], [], []

    def fail(self, where, msg):
        self.fails.append(f'{where}: {msg}')

    def warn(self, where, msg):
        self.warns.append(f'{where}: {msg}')

    def need(self, cond, where, msg):
        if not cond:
            self.fail(where, msg)
        return bool(cond)


def text(v):
    return isinstance(v, str) and bool(v.strip())


def words(s):
    return re.findall(r"[A-Za-z0-9'’-]+", s or '')


def sha256_file(path):
    h = hashlib.sha256()
    with open(path, 'rb') as f:
        for chunk in iter(lambda: f.read(1 << 20), b''):
            h.update(chunk)
    return h.hexdigest()


def count_lines(path):
    with open(path, 'rb') as f:
        return sum(1 for ln in f if ln.strip())


def load(path, rep, where):
    try:
        return json.loads(Path(path).read_text())
    except (OSError, ValueError) as e:
        rep.fail(where, f'cannot read {path}: {e}')
        return None


def split_ref(ref):
    p, _, n = (ref or '').partition('#')
    return p, int(n) if n.isdigit() else None


def check_record(rec, base, rep):
    m = rec.get('model')
    if rep.need(isinstance(m, dict), 'model', 'missing'):
        rep.need(text(m.get('name')), 'model.name', 'empty')
        rep.need(m.get('kind') in KINDS, 'model.kind', f'one of {sorted(KINDS)}')
        rep.need(isinstance(m.get('built_by'), list) and m['built_by'] and all(text(x) for x in m['built_by']),
                 'model.built_by', 'name who or what built it (Walker, the Blender MCP, scripts, by hand)')
        rep.need(bool(HEX64.match(str(m.get('sha256', '')))), 'model.sha256', 'hash of the delivered file')
        rep.need(bool(HEX64.match(str(m.get('census_signature', '')))), 'model.census_signature',
                 'run census.py on the delivered file and record its signature')
        rep.need(text(m.get('blender')), 'model.blender', 'the Blender version the model was built or last saved in')
        rep.need(text(m.get('path')) and Path(m['path']).is_absolute(), 'model.path', 'absolute path of the final .blend')
    stages = rec.get('stages')
    ids = []
    if rep.need(isinstance(stages, list) and stages, 'stages', 'need a list of stages'):
        for i, s in enumerate(stages):
            if rep.need(STAGE_ID.match(str(s.get('id', ''))), f'stages[{i}]', 'id like "04-blockout"'):
                ids.append(s['id'])
            rep.need(text(s.get('title')), f'stages[{i}]', 'title empty')
        if len(ids) != len(set(ids)):
            rep.fail('stages', 'a stage id is used twice')
    srcs = {}
    for i, s in enumerate(rec.get('sources', [])):
        w = f'sources[{i}]'
        if not (rep.need(text(s.get('id')) and s.get('kind') in SOURCE_KINDS, w, f'id and kind {sorted(SOURCE_KINDS)}')
                and rep.need(text(s.get('path')), w, 'path empty')):
            continue
        srcs[s['id']] = s
        p = base / s['path']
        if not rep.need(p.exists(), w, f'{p} missing'):
            continue
        if s.get('sha256') and sha256_file(p) != s['sha256']:
            rep.fail(w, f'{s["path"]} has changed since it was recorded (hash differs)')
        if not s.get('sha256'):
            rep.warn(w, f'{s["path"]} has no sha256: a later edit would go unnoticed')
    credits = {}
    for i, c in enumerate(rec.get('credits', [])):
        w = f'credits[{i}]'
        rep.need(all(text(c.get(k)) for k in ('id', 'what', 'source', 'licence')), w, 'id, what, source, licence')
        if text(c.get('id')):
            credits[c['id']] = c
    return ids, srcs, credits


def check_steps(steps, rec, stage_ids, srcs, credits, base, rep, final, film):
    by_id = {}
    last_stage = -1
    n_draft = n_unmapped = n_needs = n_inferred = 0
    for i, s in enumerate(steps, 1):
        sid = s.get('id', f'#{i}')
        if not rep.need(text(s.get('id')) and sid not in by_id, f'steps[{i}]', 'id missing or repeated'):
            continue
        by_id[sid] = s
        ex = bool(s.get('excluded_from_procedure'))
        st = s.get('stage')
        if rep.need(st in stage_ids, sid, f'stage "{st}" is not in record.stages'):
            idx = stage_ids.index(st)
            if idx < last_stage and not (s.get('correction') or s.get('revisit')):
                rep.fail(sid, f'stage "{st}" comes after a later stage: mark it a "revisit" or a "correction"')
            last_stage = max(last_stage, idx)
        tier = s.get('tier')
        rep.need(tier in TIERS, sid, f'tier must be one of {sorted(TIERS)}')
        if ex:
            continue
        for k, minw in (('goal', 3), ('why', 3)):
            if not rep.need(text(s.get(k)) and len(words(s[k])) >= minw, sid, f'"{k}" is empty or too short'):
                continue
        op = s.get('operation') or {}
        if s.get('needs_author'):
            n_needs += 1
            (rep.fail if final else rep.warn)(sid, f'still has drafted fields to write: {s["needs_author"]}')
        py = op.get('python') or {}
        gui = [ln for ln in op.get('gui', []) if ln.strip()]
        if tier in ('recorded', 'scripted', 'demonstrated'):
            if rep.need(bool(py.get('ref')), sid, f'a {tier} step must point at the Python it ran (operation.python.ref)'):
                p, n = split_ref(py['ref'])
                fp = base / p
                if rep.need(fp.exists(), sid, f'{p} does not exist'):
                    if n is not None:
                        total = count_lines(fp)
                        rep.need(1 <= n <= total, sid, f'{p} has {total} line(s), no #{n}')
                    known = [x for x in srcs.values() if x['path'] == p]
                    if not known:
                        rep.warn(sid, f'{p} is not listed in record.sources, so its hash is not tracked')
            rep.need(bool(gui) or text(op.get('no_gui_reason')), sid,
                     'give the interface route (operation.gui) or say why there is none (no_gui_reason)')
        gs = op.get('gui_source', 'none')
        rep.need(gs in GUI_SOURCES, sid, f'gui_source must be one of {sorted(GUI_SOURCES)}')
        if gui and gs == 'draft':
            n_draft += 1
        un = sum(1 for ln in gui if ln.lstrip().startswith('UNMAPPED'))
        if un:
            n_unmapped += un
            (rep.fail if final else rep.warn)(sid, f'{un} UNMAPPED interface line(s): translate by hand, or say '
                                                  f'there is no route (no_gui_reason)')
        ev = s.get('evidence') or []
        if tier == 'recorded':
            rep.need(bool(ev), sid, 'a recorded step needs evidence (a tape or transcript line)')
        if tier == 'scripted':
            rep.need(bool(ev) or bool(py.get('ref')), sid, 'a scripted step needs the script that ran')
        if tier == 'inspected':
            rep.need(any('census' in str(e.get('path', '')) or 'milestone' in str(e.get('path', '')) for e in ev),
                     sid, 'an inspected step needs a census or milestone as evidence')
        for e in ev:
            fp = base / str(e.get('path', ''))
            if rep.need(fp.exists(), sid, f'evidence {e.get("path")} missing') and e.get('seq'):
                rep.need(e['seq'] <= count_lines(fp), sid, f'evidence {e["path"]} has no line #{e["seq"]}')
        if tier == 'demonstrated':
            rep.need(s.get('demonstration_of') in by_id or s.get('demonstration_of') in {x.get('id') for x in steps},
                     sid, 'a demonstrated step names the step it demonstrates (demonstration_of)')
        if tier == 'inferred':
            n_inferred += 1
            rep.warn(sid, 'inferred: the record does not support this as history; say so aloud wherever it is used')
        res = s.get('result')
        rep.need(isinstance(res, dict) and (res.get('measured') or text(res.get('reply')) or text(res.get('note'))),
                 sid, 'result needs measured numbers, the reply, or a note')
        rp = s.get('repeats')
        if rp:
            n = rp.get('instances')
            if rep.need(isinstance(n, int) and n > 1 and text(rp.get('rule')), sid,
                        'repeats needs instances (> 1) and the rule'):
                tbl = rp.get('table')
                listed = rp.get('listed')
                if tbl:
                    rep.need((base / tbl).exists(), sid, f'repeat table {tbl} missing')
                else:
                    rep.need(isinstance(listed, list) and len(listed) == n, sid,
                             'give the placement table (repeats.table) or list every instance (repeats.listed)')
        co = s.get('correction')
        if co:
            rep.need(co.get('of') in {x.get('id') for x in steps} and co.get('of') != sid, sid,
                     'correction.of must name another step')
            rep.need(text(co.get('evidence')), sid, 'a correction needs the evidence that prompted it')
        ea = s.get('uses_external_asset')
        if ea:
            rep.need(ea.get('credit_id') in credits, sid, 'an outside asset needs a credit in record.credits')
    if n_draft:
        rep.warn('gui', f'{n_draft} step(s) have an interface translation nobody has followed (gui_source "draft")')
    if film:
        told = (rec.get('film') or {}).get('told_as_history', [])
        for sid in told:
            t = (by_id.get(sid) or {}).get('tier')
            if t not in ('recorded', 'scripted'):
                rep.fail(f'film.told_as_history {sid}', f'tier is "{t}": only recorded or scripted steps may be '
                         f'told as what we did; show others as a demonstration or say they are inferred')
    return by_id


def check_reveals(rec, steps, base, rep):
    """A film that shows the model rising piece by piece is a claim about ORDER. 'recorded' means
    the pieces appear in the order they were built, each tied to the step that built it;
    'explanatory' is allowed only if the film says so."""
    index = {s.get('id'): i for i, s in enumerate(steps)}
    for i, r in enumerate((rec.get('film') or {}).get('reveals', [])):
        w = f'film.reveals[{i}]'
        p = base / str(r.get('order', ''))
        if not rep.need(p.exists(), w, f'{p} missing'):
            continue
        order = load(p, rep, w)
        if not order:
            continue
        src = order.get('order_source')
        if not rep.need(src in ('recorded', 'explanatory'), w, 'order_source must be "recorded" or "explanatory"'):
            continue
        if src == 'explanatory':
            rep.need(r.get('labelled_in_film') is True, w,
                     'an explanatory order is not the order it was built in: the film must say so '
                     '(set labelled_in_film once it does)')
            continue
        last = -1
        for it in order.get('items', []):
            sid = it.get('step')
            if not rep.need(sid in index, w, f'item "{it.get("label")}" names step {sid!r}, which is not a step'):
                continue
            t = steps[index[sid]].get('tier')
            rep.need(t in ('recorded', 'scripted'), w,
                     f'item "{it.get("label")}" is tied to a {t} step: a recorded order needs recorded or scripted steps')
            if index[sid] < last:
                rep.fail(w, f'item "{it.get("label")}" comes before a step that was built earlier: not the recorded order')
            last = max(last, index[sid])


def check_milestones(rec, stage_ids, steps, base, rep):
    required = list(rec.get('comparison_views', []))
    has_steps = {s.get('stage') for s in steps if not s.get('excluded_from_procedure')}
    last_with = None
    for st in rec.get('stages', []):
        ms = st.get('milestone')
        if not ms:
            if st['id'] in has_steps:
                rep.warn(f'stage {st["id"]}', 'no milestone: the breakdown cannot show the model at this stage')
            continue
        p = base / ms
        if not rep.need(p.exists(), f'stage {st["id"]}', f'{p} missing'):
            continue
        m = load(p, rep, f'milestone {st["id"]}')
        if not m:
            continue
        rep.need(bool(HEX64.match(str(m.get('census_signature', '')))), f'milestone {st["id"]}', 'no census signature')
        names = set()
        for v in m.get('views', []):
            vp = p.parent / v['path']
            if rep.need(vp.exists(), f'milestone {st["id"]}', f'view {v["path"]} missing'):
                if v.get('sha256') and sha256_file(vp) != v['sha256']:
                    rep.fail(f'milestone {st["id"]}', f'view {v["path"]} has changed since it was rendered')
                names.add(v['name'])
        for name in required:
            rep.need(name in names, f'milestone {st["id"]}',
                     f'missing comparison view {name}: every stage is shown from the same cameras')
        last_with = (st['id'], m)
    if required == []:
        rep.warn('comparison_views', 'no fixed comparison cameras declared: the stages cannot be compared '
                 'like for like')
    if last_with:
        sig = rec.get('model', {}).get('census_signature')
        sid, m = last_with
        if sig and m.get('census_signature') != sig:
            rep.fail(f'milestone {sid}', 'the last milestone is not the delivered model (census signatures differ): '
                     'add a final milestone, or the model changed after it')


def check_reconstruction(rec, final, rep):
    rc = rec.get('reconstruction') or {}
    replay = rc.get('replay') or {'status': 'pending'}
    by_hand = rc.get('by_hand') or {'status': 'pending'}
    sig = rec.get('model', {}).get('census_signature')
    rs = replay.get('status')
    rep.need(rs in ('pass', 'fail', 'pending'), 'reconstruction.replay', 'status is pass, fail or pending')
    if rs == 'pass':
        rep.need(text(replay.get('how')), 'reconstruction.replay', 'say how the replay was run')
        rep.need(replay.get('census_signature') == sig, 'reconstruction.replay',
                 'a passing replay must have produced the delivered model\'s census signature')
    elif rs == 'fail':
        rep.fail('reconstruction.replay', 'the replay did not reproduce the model: the record is not a recipe yet')
    bs = by_hand.get('status')
    rep.need(bs in ('pass', 'done', 'pending'), 'reconstruction.by_hand', 'status is done or pending')
    if bs in ('done', 'pass'):
        rep.need(all(text(by_hand.get(k)) for k in ('by', 'date', 'module')), 'reconstruction.by_hand',
                 'a finished by-hand check names who, when and which module')
    if final and rs != 'pass' and bs not in ('done', 'pass'):
        rep.fail('reconstruction', 'nothing shows this record rebuilds the model: pass a replay or have a person '
                 'follow a module by hand')
    elif rs != 'pass' and bs not in ('done', 'pass'):
        rep.warn('reconstruction', 'not verified: neither replayed nor followed by hand')
    if bs not in ('done', 'pass'):
        rep.warn('reconstruction.by_hand', 'no person has followed the interface steps: the guide must call them drafts')


def check_guide(base, rep, final):
    g = base / 'RECONSTRUCT.md'
    if not g.exists():
        (rep.fail if final else rep.warn)('RECONSTRUCT.md', 'missing: run reconstruct_md.py')
        return
    body = g.read_text()
    heads = [ln for ln in body.splitlines() if ln.startswith('## ')]
    rep.need(bool(heads) and heads[0].strip() == '## Executive summary', 'RECONSTRUCT.md',
             'the first section must be "## Executive summary" (what, why, what it found)')
    rep.need('## Verification status' in body, 'RECONSTRUCT.md', 'the guide must state its verification status')


def recensus(rec, base, rep):
    m = rec['model']
    p = Path(m['path'])
    if not p.exists():
        rep.warn('recensus', f'{p} is not on this machine')
        return
    if m.get('sha256') and sha256_file(p) != m['sha256']:
        rep.fail('model.sha256', f'{p} has changed since the record was written')
    out = base / '.recensus.json'
    r = subprocess.run([BLENDER, '-b', str(p), '--python', str(CENSUS), '--', 'census', '--out', str(out)],
                       capture_output=True, text=True, timeout=600)
    if r.returncode != 0 or not out.exists():
        rep.fail('recensus', f'Blender census failed: {r.stdout[-300:]}')
        return
    sig = json.loads(out.read_text())['signature']
    out.unlink()
    if sig != m.get('census_signature'):
        rep.fail('model.census_signature', f'the file now has signature {sig[:12]}…, the record says '
                 f'{str(m.get("census_signature"))[:12]}…: the model changed after the record')


def verify(record_path, final=False, film=False, do_recensus=False):
    rep = Report()
    rp = Path(record_path).resolve()
    base = rp.parent
    rec = load(rp, rep, 'record.json')
    if rec is None:
        return rep
    if not rep.need(rec.get('schema_version') == 1, 'schema_version', 'must be 1'):
        return rep
    stage_ids, srcs, credits = check_record(rec, base, rep)
    sp = base / 'BUILD-STEPS.jsonl'
    if not rep.need(sp.exists(), 'BUILD-STEPS.jsonl', f'{sp} missing'):
        return rep
    steps = []
    for i, line in enumerate(sp.read_text().splitlines(), 1):
        if line.strip():
            try:
                steps.append(json.loads(line))
            except ValueError as e:
                rep.fail(f'BUILD-STEPS.jsonl:{i}', f'not JSON ({e})')
    if not rep.need(bool(steps), 'BUILD-STEPS.jsonl', 'no steps'):
        return rep
    check_steps(steps, rec, stage_ids, srcs, credits, base, rep, final, film)
    check_milestones(rec, stage_ids, steps, base, rep)
    check_reveals(rec, steps, base, rep)
    check_reconstruction(rec, final, rep)
    check_guide(base, rep, final)
    if do_recensus and isinstance(rec.get('model'), dict):
        recensus(rec, base, rep)
    return rep


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__.split('\n\n')[0])
    ap.add_argument('record')
    ap.add_argument('--final', action='store_true')
    ap.add_argument('--film', action='store_true')
    ap.add_argument('--recensus', action='store_true')
    ap.add_argument('--json', action='store_true')
    a = ap.parse_args(argv)
    rep = verify(a.record, a.final, a.film, a.recensus)
    if a.json:
        print(json.dumps({'ok': not rep.fails, 'fails': rep.fails, 'warns': rep.warns}, indent=2))
    else:
        for f in rep.fails:
            print('FAIL', f)
        for w in rep.warns:
            print('WARN', w)
        print('BUILD RECORD GATE:', 'FAIL' if rep.fails else 'PASS', f'({len(rep.fails)} fail, {len(rep.warns)} warn)')
    return 1 if rep.fails else 0


if __name__ == '__main__':
    sys.exit(main())
