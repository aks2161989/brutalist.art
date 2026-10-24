#!/usr/bin/env python3
"""Read-only gate for a building / environment / asset walkthrough.

  verify_walkthrough.py REEL/walkthrough.json [--final] [--renders] [--require-human-tests]
                                              [--no-hash-model] [--json]

Checks the editorial contract (shot jobs, section order, disclosure of what the model is not,
narration that is sourced and fits its shot, one lighting logic, a render budget) and
cross-checks it against route.json and the route_check.py report measured from the model.

It cannot judge whether the route is understandable, whether a shot is beautiful, or whether
the model is right. Those need frames, a person who has not seen the model, and the sources.
Exit status 1 on any failure."""
import argparse
import hashlib
import json
import math
from pathlib import Path
import re
import sys

MODES = ('building', 'environment', 'asset')
SECTIONS = {
    'building': ['site', 'approach', 'entrance', 'main', 'connected', 'closing'],
    'environment': ['site', 'approach', 'entrance', 'main', 'connected', 'closing'],
    'asset': ['establish', 'silhouette', 'scale', 'material', 'topology', 'closing'],
}
FLOATING = {'detail'}                    # a close look may sit anywhere
REQUIRED = {'building': ['main', 'closing'], 'environment': ['main', 'closing'],
            'asset': ['establish', 'scale', 'closing']}
RECOMMENDED = {'building': ['site', 'entrance'], 'environment': ['entrance'], 'asset': ['silhouette']}
PURPOSES = {'orientation', 'scale', 'connection', 'material', 'atmosphere', 'feature'}
FRAMINGS = {'wide', 'medium', 'close'}
STATUSES = {'measured', 'interpretive', 'stylized', 'invented'}
SHOT_TYPES = {'walk', 'still', 'aerial', 'crane', 'orbit'}
MIN_S = {'walk': (3.0, 6.0), 'aerial': (3.0, 6.0), 'crane': (3.0, 6.0), 'still': (1.5, 2.5),
         'orbit': (8.0, 12.0)}
MAX_SHOT_S = 30.0
WORDS_PER_S = 2.4                        # Liam / Kokoro am_onyx reads ~2.4-2.8 words a second
MAX_LINE_WORDS = 40
LOCAL_RENDER_LIMIT_H = 8.0
EVALUATIVE = {'stunning', 'breathtaking', 'gorgeous', 'beautiful', 'magnificent', 'amazing',
              'incredible', 'epic', 'awesome', 'spectacular', 'masterpiece', 'unforgettable',
              'immersive', 'perfect', 'flawless', 'stunningly', 'iconic'}
NUMBERING = re.compile(r'\b(part|episode|ep\.?|video|film)\s*#?\d+\b|\b\d+\s*(of|/)\s*\d+\b', re.I)
BAD_VERDICT = {'', 'fail', 'wrong', 'unverified', 'open', 'unchecked', 'todo', 'pending'}
HEX64 = re.compile(r'^[0-9a-f]{64}$')


class Report:
    def __init__(self):
        self.fails, self.warns, self.notes = [], [], []

    def fail(self, where, msg):
        self.fails.append(f'{where}: {msg}')

    def warn(self, where, msg):
        self.warns.append(f'{where}: {msg}')

    def note(self, msg):
        self.notes.append(msg)

    def need(self, cond, where, msg):
        if not cond:
            self.fail(where, msg)
        return bool(cond)


def text(v):
    return isinstance(v, str) and bool(v.strip())


def num(v):
    return isinstance(v, (int, float)) and not isinstance(v, bool) and math.isfinite(v)


def sha256_file(path):
    h = hashlib.sha256()
    with open(path, 'rb') as f:
        for chunk in iter(lambda: f.read(1 << 20), b''):
            h.update(chunk)
    return h.hexdigest()


def words(s):
    return re.findall(r"[A-Za-z0-9'’-]+", s)


def load_json(path, rep, where):
    try:
        return json.loads(Path(path).read_text())
    except (OSError, ValueError) as e:
        rep.fail(where, f'cannot read {path}: {e}')
        return None


def factcheck_rows(path):
    """{fact_id: (verdict, source)} from the FACTCHECK.md table rows."""
    rows = {}
    if not path.exists():
        return None
    for line in path.read_text().splitlines():
        if not line.lstrip().startswith('|'):
            continue
        cells = [c.strip() for c in line.strip().strip('|').split('|')]
        if len(cells) < 4 or set(cells[0]) <= set('-: '):
            continue
        rows[cells[0]] = (cells[3].lower().strip('* '), cells[4] if len(cells) > 4 else '')
    return rows


def check_model(doc, reel, rep, hash_model):
    m = doc.get('model')
    if not rep.need(isinstance(m, dict), 'model', 'missing'):
        return
    rep.need(text(m.get('name')), 'model.name', 'empty')
    rep.need(m.get('status') in STATUSES, 'model.status', f'must be one of {sorted(STATUSES)}')
    rep.need(bool(HEX64.match(str(m.get('sha256', '')))), 'model.sha256', 'need the 64-hex hash of the file shown')
    rep.need(text(m.get('blender')), 'model.blender', 'record the Blender version it was opened in')
    card = m.get('card')
    if rep.need(text(card), 'model.card', 'a MODEL-CARD.md says what the model is and is not'):
        cp = Path(card) if Path(card).is_absolute() else reel / card
        rep.need(cp.exists(), 'model.card', f'{cp} does not exist')
    mp = m.get('path')
    if rep.need(text(mp) and Path(mp).is_absolute(), 'model.path', 'must be an absolute path'):
        p = Path(mp)
        if not p.exists():
            rep.warn('model.path', f'{p} is not on this machine; the hash cannot be re-checked')
        elif hash_model and HEX64.match(str(m.get('sha256', ''))):
            if sha256_file(p) != m['sha256']:
                rep.fail('model.sha256', f'{p} has changed since the film was laid out; every '
                         f'measurement and render taken before is stale')


def check_brief(doc, rep):
    asset = doc.get('mode') == 'asset'
    b = doc.get('brief')
    if not rep.need(isinstance(b, dict), 'brief', 'missing'):
        return
    for k in ('idea', 'audience', 'variant'):
        rep.need(text(b.get(k)), f'brief.{k}', 'empty')
    if text(b.get('idea')) and len(words(b['idea'])) > 40:
        rep.warn('brief.idea', 'more than 40 words: the film has no single idea yet')
    if not asset:
        rep.need(num(b.get('viewer_height_m')) and 0.2 <= b['viewer_height_m'] <= 2.5,
                 'brief.viewer_height_m', 'the viewpoint height in metres (1.6 for a standing adult)')


def check_shots(doc, route, report, rep):
    mode = doc.get('mode')
    shots = doc.get('shots')
    if not rep.need(isinstance(shots, list) and shots, 'shots', 'need a non-empty list'):
        return {}, 0.0
    sections = SECTIONS[mode]
    ids, durations, order = set(), {}, []
    route_by_id = {s['id']: s for s in (route or {}).get('shots', [])}
    fps = (route or {}).get('fps') or (report or {}).get('fps') or 24
    seen_reveals = {}
    prev_idx = -1
    for i, s in enumerate(shots):
        sid = s.get('id', f'#{i}')
        if not rep.need(text(s.get('id')) and sid not in ids, f'shots[{i}]', 'id missing or repeated'):
            continue
        ids.add(sid)
        sec = s.get('section')
        rep.need(sec in sections or sec in FLOATING, sid,
                 f'section must be one of {sections + sorted(FLOATING)} for mode {mode}')
        if sec in sections:
            idx = sections.index(sec)
            if idx < prev_idx:
                rep.fail(sid, f'section "{sec}" comes after "{sections[prev_idx]}": the route '
                         f'doubles back (sections run {" -> ".join(sections)}; close looks may float)')
            prev_idx = max(prev_idx, idx)
        rep.need(s.get('purpose') in PURPOSES, sid, f'purpose must be one of {sorted(PURPOSES)}')
        rep.need(s.get('framing') in FRAMINGS, sid, f'framing must be one of {sorted(FRAMINGS)}')
        rv = s.get('reveals')
        if rep.need(text(rv), sid, '"reveals" is empty: say what the viewer learns here that '
                                  'no earlier shot taught, or cut the shot'):
            key = re.sub(r'\W+', ' ', rv.lower()).strip()
            if key in seen_reveals:
                rep.warn(sid, f'reveals the same thing as {seen_reveals[key]}')
            seen_reveals[key] = sid
        if sec == 'scale' or s.get('purpose') == 'scale':
            ref = s.get('scale_reference')
            rep.need(isinstance(ref, dict) and ref.get('kind') in ('human', 'grid', 'ruler')
                     and num(ref.get('size_m')), sid,
                     'a scale shot needs scale_reference {"kind": human|grid|ruler, "size_m": n}')
        order.append(s)
        # duration from the measured route
        rs = route_by_id.get(sid)
        if rs:
            f0, f1 = rs['frames']
            dur = (f1 - f0 + 1) / fps
            durations[sid] = dur
            kind = rs.get('type', 'walk')
            lo, soft = MIN_S.get(kind, (3.0, 6.0))
            if dur < lo:
                rep.fail(sid, f'{kind} shot lasts {dur:.1f} s (floor {lo} s): the viewer cannot '
                         f'take the space in')
            elif dur < soft:
                rep.warn(sid, f'{kind} shot lasts {dur:.1f} s (below the {soft} s default)')
            if dur > MAX_SHOT_S and not text(s.get('hold_reason')):
                rep.warn(sid, f'{dur:.0f} s with no "hold_reason": what keeps the viewer?')
        else:
            rep.fail(sid, 'no matching shot in route.json')
    for rid in route_by_id:
        if rid not in ids:
            rep.fail(rid, 'in route.json but not in the walkthrough: delete the rig or add the shot')
    secs = [s.get('section') for s in order]
    for need in REQUIRED[mode]:
        rep.need(need in secs, 'sections', f'mode {mode} needs a "{need}" section')
    for rec in RECOMMENDED[mode]:
        if rec not in secs:
            rep.warn('sections', f'no "{rec}" section: say why the film skips it, or add it')
    if order and order[-1].get('section') != 'closing':
        rep.fail('sections', 'the last shot must be the "closing" section')
    if mode == 'asset' and order and order[0].get('section') != 'establish':
        rep.fail('sections', 'an asset film opens on an "establish" shot')
    # alternation of framing
    run = 1
    for a, b in zip(order, order[1:]):
        run = run + 1 if a.get('framing') == b.get('framing') else 1
        if run == 4:
            rep.warn(b.get('id'), f'four {b.get("framing")} shots in a row: alternate wide, '
                     f'medium and close so the viewer is oriented and then shown detail')
    if durations:
        avg = sum(durations.values()) / len(durations)
        if avg < 3.0:
            rep.warn('pace', f'average shot is {avg:.1f} s: this is a montage, not a walk')
    return durations, fps


def check_looks(doc, rep):
    looks = doc.get('looks')
    if not rep.need(isinstance(looks, dict) and looks, 'looks', 'declare at least one lighting look'):
        return
    for lid, lk in looks.items():
        rep.need(isinstance(lk, dict) and text(lk.get('name')) and text(lk.get('time')),
                 f'looks.{lid}', 'needs name and time of day / condition')
    prev = None
    for s in doc.get('shots', []):
        lid = s.get('look')
        if not rep.need(lid in looks, s.get('id'), f'look "{lid}" is not declared'):
            continue
        if prev and lid != prev.get('look'):
            same_place = s.get('section') == prev.get('section')
            ch = s.get('look_change')
            if not (isinstance(ch, dict) and text(ch.get('reason'))):
                (rep.fail if same_place else rep.warn)(
                    s.get('id'), f'light changes from {prev.get("look")} to {lid} with no '
                    f'"look_change.reason": a change of time or weather must be a decision')
        prev = s


def check_narration(doc, durations, reel, rep):
    facts = factcheck_rows(reel / 'FACTCHECK.md')
    total_words, total_s = 0, sum(durations.values())
    for s in doc.get('shots', []):
        sid = s.get('id')
        n = s.get('narration')
        if n is None:
            continue
        src = n.get('source') if isinstance(n, dict) else None
        if not rep.need(src in ('model', 'world', 'none'), sid, 'narration.source must be model, world or none'):
            continue
        if src == 'none':
            continue
        line = n.get('line')
        if not rep.need(text(line), sid, 'narration.line is empty'):
            continue
        w = words(line)
        total_words += len(w)
        if len(w) > MAX_LINE_WORDS:
            rep.warn(sid, f'{len(w)}-word line: say one thing per shot')
        if NUMBERING.search(line):
            rep.fail(sid, 'a number or total for the film or its parts ("part 2", "3 of 5"): films are never numbered')
        bad = sorted({x.lower() for x in w} & EVALUATIVE)
        if bad:
            rep.warn(sid, f'evaluative word(s) {bad}: the picture is the evidence, the word is a claim')
        if sid in durations:
            need_s = len(w) / WORDS_PER_S
            if need_s > durations[sid]:
                rep.fail(sid, f'the line needs ~{need_s:.1f} s to speak but the shot lasts '
                         f'{durations[sid]:.1f} s: lengthen the shot or cut the line')
        if src == 'model':
            rep.need(text(n.get('evidence')), sid,
                     'a claim about the model needs "evidence" (a survey/census key, a control id, a measured file)')
        else:
            fid = n.get('fact')
            if rep.need(text(fid), sid, 'a claim about the world needs a "fact" id from FACTCHECK.md'):
                if facts is None:
                    rep.fail(sid, f'{reel / "FACTCHECK.md"} does not exist')
                elif fid not in facts:
                    rep.fail(sid, f'fact {fid} has no row in FACTCHECK.md')
                elif facts[fid][0] in BAD_VERDICT:
                    rep.fail(sid, f'fact {fid} is not verified in FACTCHECK.md (verdict "{facts[fid][0]}")')
                elif not facts[fid][1].strip():
                    rep.fail(sid, f'fact {fid} has no source in FACTCHECK.md')
    if total_s and total_words / total_s > 2.2:
        rep.warn('narration', f'{total_words / total_s:.1f} words per second over the whole film: '
                 f'a walkthrough needs quiet to look')
    if NUMBERING.search(str(doc.get('title', ''))):
        rep.fail('title', 'films are never numbered ("part 2", "3 of 5")')


def check_disclosure(doc, rep):
    ids = [s.get('id') for s in doc.get('shots', [])]
    d = doc.get('disclosure')
    if rep.need(isinstance(d, dict), 'disclosure', 'say in the opening what the model is and is not'):
        rep.need(d.get('shot') in ids[:2], 'disclosure.shot',
                 'the disclosure must be spoken or shown in the first two shots')
        rep.need(text(d.get('text')) and len(words(d['text'])) >= 8, 'disclosure.text',
                 'at least a sentence: what kind of model this is and what it does not show')
    dep = doc.get('departures')
    if rep.need(isinstance(dep, list), 'departures', 'a list (empty only for a measured model)'):
        if not dep and (doc.get('model') or {}).get('status') in ('interpretive', 'stylized', 'invented'):
            rep.warn('departures', 'an interpretive model that lists no departures from its sources '
                     'has not been examined; list what it leaves out or simplifies')
        for i, x in enumerate(dep):
            w = f'departures[{i}]'
            for k in ('id', 'what', 'effect'):
                rep.need(text(x.get(k)), w, f'"{k}" is empty')
            rep.need(x.get('disclosed_in') in ids, w, 'disclosed_in must name a shot of this film')


def check_route(doc, reel, rep):
    r = doc.get('route')
    if not rep.need(isinstance(r, dict), 'route', 'missing {"file": ..., "report": ...}'):
        return None, None
    rp = reel / r.get('file', 'route.json')
    rr = reel / r.get('report', 'route_report.json')
    route = load_json(rp, rep, 'route.file') if rep.need(rp.exists(), 'route.file', f'{rp} missing') else None
    report = None
    if not rr.exists():
        rep.fail('route.report', f'{rr} missing: run route_check.py on the rigged model')
    else:
        report = load_json(rr, rep, 'route.report')
    if route and report:
        if report.get('route_sha256') != sha256_file(rp):
            rep.fail('route.report', 'measured against a different route.json than the one in the '
                     'film: re-run route_check.py')
        m = doc.get('model', {})
        if report.get('model', {}).get('sha256') and m.get('sha256') and \
                report['model']['sha256'] != m['sha256']:
            rep.fail('route.report', 'measured on a different model file than model.sha256 names')
        if not report.get('ok'):
            rep.fail('route.report', f'{report.get("fail_count")} route failure(s): '
                     + '; '.join(f"{v['shot']} {v['rule']}" for v in report['violations']
                                 if v['severity'] == 'fail')[:300])
        for v in report.get('violations', []):
            if v['severity'] == 'warn':
                rep.warn(f"route {v['shot']} f{v['frame']}", f"{v['rule']}: {v['message']}")
        checked = {s['id'] for s in report.get('shots', []) if s.get('checked')}
        for s in route.get('shots', []):
            if s['id'] not in checked:
                rep.fail(s['id'], 'not measured in the route report')
    return route, report


def check_budget(doc, route, rep, final):
    b = doc.get('budget')
    if not rep.need(isinstance(b, dict), 'budget', 'missing'):
        return
    for k in ('engine', 'samples'):
        rep.need(text(b.get(k)) or num(b.get(k)), f'budget.{k}', 'empty')
    res = b.get('resolution')
    rep.need(isinstance(res, list) and len(res) == 2 and all(isinstance(x, int) and x > 0 for x in res),
             'budget.resolution', '[width, height]')
    meas = [m for m in b.get('samples_measured', []) if num(m.get('sec_per_frame')) and m['sec_per_frame'] > 0]
    kinds = {m.get('kind') for m in meas}
    if len(meas) < 3 or len(kinds) < 2:
        (rep.fail if final else rep.warn)(
            'budget', 'time at least three real frames of different kinds (interior, exterior, '
            'moving detail) before promising a render time')
    if meas and route:
        frames = sum(s['frames'][1] - s['frames'][0] + 1 for s in route['shots'])
        spf = sum(m['sec_per_frame'] for m in meas) / len(meas)
        hours = frames * spf / 3600.0
        rep.note(f'render estimate: {frames} frames x {spf:.0f} s = {hours:.1f} h on {b.get("where", "?")}')
        if b.get('where') == 'mac' and hours > LOCAL_RENDER_LIMIT_H:
            rep.warn('budget', f'{hours:.0f} h on the Mac: plan the render for Explorer (read '
                     f'hpc-aicr/skills/hpc/HPC.md; ask Bear before any sbatch)')


def check_tests(doc, rep, require):
    ch = doc.get('checks', {})
    for name in ('orientation_test', 'promise_check'):
        v = ch.get(name, 'pending')
        status = v.get('status') if isinstance(v, dict) else v
        if status not in ('pending', 'done'):
            rep.fail(f'checks.{name}', 'must be "pending" or {"status":"done","by":...,"date":...}')
        elif status == 'done':
            if not (isinstance(v, dict) and text(v.get('by')) and text(v.get('date'))):
                rep.fail(f'checks.{name}', 'a finished human test names who did it and when')
        elif require:
            rep.fail(f'checks.{name}', 'still pending: only a person can run this')
        else:
            rep.warn(f'checks.{name}', 'pending: the film is NOT audience-tested')


def check_renders(doc, route, reel, rep):
    if not route:
        return
    r = doc.get('renders') or {}
    base = reel / r.get('dir', 'renders')
    fmt = r.get('format', 'PNG').lower()
    try:
        from PIL import Image
        import numpy as np
    except ImportError:
        Image = None
    for s in route['shots']:
        f0, f1 = s['frames']
        d = base / s['id']
        frames = sorted(d.glob(f'*.{fmt}')) if d.exists() else []
        want = f1 - f0 + 1
        if len(frames) != want:
            rep.fail(s['id'], f'{len(frames)} frames in {d}, expected {want}')
            continue
        nums = [int(re.sub(r'\D', '', p.stem) or -1) for p in frames]
        if nums != list(range(nums[0], nums[0] + want)):
            rep.fail(s['id'], 'frame numbers have a gap')
        if Image and s.get('type') == 'still' and want >= 8:
            prev, diffs = None, []
            for p in frames[:24]:
                a = np.asarray(Image.open(p).convert('L'), dtype=np.int16)
                if prev is not None:
                    diffs.append(float(np.abs(a - prev).mean()))
                prev = a
            if diffs and max(diffs) > 1.0:
                rep.warn(s['id'], f'a still shot flickers: frame-to-frame difference up to '
                         f'{max(diffs):.2f}/255 (unstable denoise or animated noise seed)')


def verify(path, final=False, renders=False, require_human=False, hash_model=True):
    rep = Report()
    path = Path(path).resolve()
    reel = path.parent
    doc = load_json(path, rep, 'walkthrough.json')
    if doc is None:
        return rep
    if not rep.need(doc.get('schema_version') == 1, 'schema_version', 'must be 1'):
        return rep
    if not rep.need(doc.get('mode') in MODES, 'mode', f'must be one of {list(MODES)}'):
        return rep
    check_model(doc, reel, rep, hash_model)
    check_brief(doc, rep)
    route, report = check_route(doc, reel, rep)
    durations, _fps = check_shots(doc, route, report, rep)
    check_looks(doc, rep)
    check_narration(doc, durations, reel, rep)
    check_disclosure(doc, rep)
    check_budget(doc, route, rep, final)
    check_tests(doc, rep, require_human or final)
    if renders or final:
        check_renders(doc, route, reel, rep)
    if durations:
        rep.note(f'runtime of the shots: {sum(durations.values()):.1f} s over {len(durations)} shots')
    return rep


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__.split('\n\n')[0])
    ap.add_argument('walkthrough')
    ap.add_argument('--final', action='store_true', help='final handoff: budget, renders and human tests are required')
    ap.add_argument('--renders', action='store_true', help='check the rendered frame sequences on disk')
    ap.add_argument('--require-human-tests', action='store_true')
    ap.add_argument('--no-hash-model', action='store_true', help='skip re-hashing the .blend')
    ap.add_argument('--json', action='store_true')
    a = ap.parse_args(argv)
    rep = verify(a.walkthrough, a.final, a.renders, a.require_human_tests, not a.no_hash_model)
    if a.json:
        print(json.dumps({'ok': not rep.fails, 'fails': rep.fails, 'warns': rep.warns, 'notes': rep.notes}, indent=2))
    else:
        for f in rep.fails:
            print('FAIL', f)
        for w in rep.warns:
            print('WARN', w)
        for n in rep.notes:
            print('NOTE', n)
        print('WALKTHROUGH GATE:', 'FAIL' if rep.fails else 'PASS',
              f'({len(rep.fails)} fail, {len(rep.warns)} warn)')
    return 1 if rep.fails else 0


if __name__ == '__main__':
    sys.exit(main())
