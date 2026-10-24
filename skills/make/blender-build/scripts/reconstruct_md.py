#!/usr/bin/env python3
"""Write RECONSTRUCT.md: the guide a person follows to rebuild a model, from the build record.

  reconstruct_md.py --record build-record/record.json --steps build-record/BUILD-STEPS.jsonl
                    --out build-record/RECONSTRUCT.md

The guide opens with an executive summary (what this is, why read it, what the record found and
did not do), then the verification status, what to have before starting, the two ways to follow it
(the script door and the hands door), one section per stage with each step as a card, the repeated
work, the corrections, and what the guide cannot tell you. Everything it says about how sure it is
comes from the record: tiers, the interface translation's source, the replay and by-hand checks.
It writes nothing the record does not hold. Paths inside the guide are relative to the record
folder."""
import argparse
import json
from pathlib import Path
import sys

TIER_TEXT = {
    'recorded': 'recorded: a tape or transcript line shows this was sent to Blender and what came back',
    'scripted': 'scripted: a script in the project ran; the steps are a translation of its calls',
    'inspected': 'inspected: read from the finished file; nothing records how it was made',
    'demonstrated': 'demonstrated: redone afterwards to show the move; not the original work',
    'inferred': 'inferred: a plausible method, not evidence',
}
STAGE_ORDER_HINT = ('01-define', '02-dimensions', '03-organize', '04-blockout', '05-route-or-silhouette',
                    '06-modules', '07-detail', '08-materials', '09-dress-light', '10-camera', '11-render-export')


def load_steps(path):
    out = []
    for i, line in enumerate(Path(path).read_text().splitlines(), 1):
        if line.strip():
            try:
                out.append(json.loads(line))
            except ValueError as e:
                raise SystemExit(f'{path}:{i}: not JSON ({e})')
    return out


def tier_counts(steps):
    c = {}
    for s in steps:
        c[s.get('tier', '?')] = c.get(s.get('tier', '?'), 0) + 1
    return c


def gui_lines(step):
    return [ln for ln in step['operation'].get('gui', []) if ln.strip()]


def n_unmapped(step):
    return sum(1 for ln in gui_lines(step) if ln.lstrip().startswith('UNMAPPED'))


def card(step, record):
    op = step['operation']
    ex = step.get('excluded_from_procedure')
    tier = step.get('tier', '?')
    head = f"### {step['id']} — {step.get('goal') or '(goal not yet written)'}"
    meta = [tier]
    if step.get('module'):
        meta.append(f"module {step['module']}")
    py = op.get('python') or {}
    if py.get('ref'):
        meta.append(py['ref'])
    out = [head, f"*{' · '.join(meta)}*", '']
    if ex:
        out += ['**This command failed.** It is not part of the procedure. '
                'What went wrong is on the step that corrected it.', '']
        return out
    if step.get('start_state'):
        out += [f"**Start from.** {step['start_state']}", '']
    gl = gui_lines(step)
    src = op.get('gui_source', 'none')
    if gl:
        label = {'draft': '**Do** *(a draft translation of the recorded Python; no person has followed these '
                          'steps yet)*',
                 'human': '**Do**'}.get(src, '**Do**')
        out += [label, '']
        out += [(f'- {ln}' if not ln.startswith(' ') else f'  - {ln.strip()}') for ln in gl]
        out.append('')
    elif op.get('no_gui_reason'):
        out += [f"**Do.** There is no interface route for this step: {op['no_gui_reason']}", '']
    if op.get('bl_idnames'):
        out += [f"**Blender operators used.** {', '.join(f'`{x}`' for x in op['bl_idnames'])}", '']
    if step.get('settings'):
        out += ['| Setting | Value |', '|---|---|']
        out += [f'| {k} | {v} |' for k, v in step['settings'].items()]
        out.append('')
    res = step.get('result') or {}
    measured = res.get('measured') or {}
    if measured:
        out += ['**Result (measured).** ' + '; '.join(f'{k} = {v}' for k, v in measured.items()), '']
    elif res.get('reply'):
        out += [f"**Result (what Blender replied).** `{res['reply'].strip().splitlines()[0][:160]}`", '']
    if step.get('why'):
        out += [f"**Why.** {step['why']}", '']
    if step.get('correction'):
        c = step['correction']
        out += [f"**Corrects {c['of']}.** {c.get('evidence', '')}", '']
    rep = step.get('repeats')
    if rep:
        out += [f"**Repeated.** {rep.get('rule', '')} ({rep.get('instances', '?')} instances"
                + (f"; placements in `{rep['table']}`" if rep.get('table') else '') + ').', '']
    if step.get('uses_external_asset'):
        a = step['uses_external_asset']
        out += [f"**Uses an outside asset.** {a.get('name', '')} (credit {a.get('credit_id', '?')}).", '']
    if tier == 'demonstrated':
        out += [f"**This is a demonstration** of {step.get('demonstration_of', '?')}, redone to show the move.", '']
    return out


def build(record, steps):
    m = record['model']
    stages = record['stages']
    by_stage = {}
    for s in steps:
        by_stage.setdefault(s.get('stage', ''), []).append(s)
    proc = [s for s in steps if not s.get('excluded_from_procedure')]
    failed = [s for s in steps if s.get('excluded_from_procedure')]
    tiers = tier_counts(proc)
    draft = [s for s in proc if s['operation'].get('gui_source') == 'draft' and gui_lines(s)]
    unmapped = sum(n_unmapped(s) for s in proc)
    needs = [s for s in proc if s.get('needs_author')]
    rc = record.get('reconstruction', {})
    replay = rc.get('replay', {'status': 'pending'})
    byhand = rc.get('by_hand', {'status': 'pending'})

    L = [f"# How {m['name']} was made — a reconstruction guide", '', '## Executive summary', '']
    L += [f"**What this is.** The record of how the Blender model **{m['name']}** was built "
          f"({', '.join(m.get('built_by', [])) or 'builder not recorded'}), written so a person can rebuild it: "
          f"{len(proc)} steps in {len([s for s in stages if by_stage.get(s['id'])])} stages, each with what to do, "
          f"the settings, what happened, and why.", '']
    L += ['**Why read it.** A finished model hides its history. This guide says what was done in what order, '
          'which parts are proven by a recording and which are only inferred, and where a person following '
          'along will have to use judgment or the script instead of the mouse.', '']
    tier_bits = ', '.join(f'{n} {t}' for t, n in sorted(tiers.items(), key=lambda x: -x[1]))
    found = [f'Steps by evidence: {tier_bits}.']
    if failed:
        found.append(f'{len(failed)} command(s) failed and were corrected; the corrections are kept.')
    found.append(f'Replay (rebuild by script and compare): **{replay.get("status", "pending")}**. '
                 f'Followed by hand: **{byhand.get("status", "pending")}**.')
    if draft:
        found.append(f'{len(draft)} step(s) carry an interface translation that is still a DRAFT (nobody has '
                     f'followed it).')
    if unmapped:
        found.append(f'{unmapped} line(s) could not be translated and are marked UNMAPPED.')
    L += ['**What it found.** ' + ' '.join(found), '']
    L += ['**What it does not do.** It does not prove the model on disk still matches the record '
          '(check the census signature below), it does not teach Blender, and where a step was only inferred '
          'or inspected it says so rather than telling it as history.', '']

    L += ['## Verification status', '',
          '| Check | Status | What it means |', '|---|---|---|',
          f'| Replay | {replay.get("status", "pending")} | {replay.get("how", "Rebuild the model headless from the recorded scripts and compare the census signature.")} |',
          f'| Followed by hand | {byhand.get("status", "pending")} | '
          + (f'{byhand.get("by", "")} rebuilt {byhand.get("module", "one module")} in a fresh file on {byhand.get("date", "")}; {byhand.get("note", "")}'
             if byhand.get('status') == 'done' else 'No person has yet followed the interface steps in a fresh file. Treat every "Do" list as a draft.')
          + ' |',
          f'| Interface translation | {len(draft)} draft step(s) | Translated from the recorded Python; menu paths come from the manual and have not been followed click by click. |',
          f'| Judgment written | {len(proc) - len(needs)} of {len(proc)} | Steps whose goal and why a person or agent wrote (the rest are drafts). |',
          '', f"Model census signature: `{m.get('census_signature', 'not recorded')}`  ", '']

    L += ['## Before you start', '',
          f"- **Blender:** {m.get('blender', 'not recorded')}. Menu names and a few properties differ across versions "
          f"(Blender 4.x to 5.x removed and renamed several); check the version before trusting a path.",
          f"- **Units:** {record.get('units', 'metres, unit scale 1 (assumed; check the census)')}.",
          f"- **Final model:** `{Path(m.get('path', '')).name}`, hash `{(m.get('sha256') or 'not recorded')[:16]}`…"]
    for src in record.get('sources', []):
        L.append(f"- **Source {src['id']}** ({src['kind']}): `{src['path']}`")
    for c in record.get('credits', []):
        L.append(f"- **Credit {c['id']}:** {c.get('what', '')} — {c.get('source', '')} ({c.get('licence', '')})")
    L.append('')

    L += ['## The two ways to follow this', '',
          '**The script door (exact).** Each step points at the recorded Python (`tape/…#N` or a script). '
          'Run the scripts in Blender in order and you get the same model; the replay check says whether that '
          'was verified. Use this for anything repeated hundreds of times.', '',
          '**The hands door (by the mouse).** Each "Do" list is the interface route. Do one module this way '
          'and compare it with the census before doing the rest. Bulk steps (placing many parts from a '
          'table) are marked with the rule and the table, and are meant to be done once by hand and then by '
          'script.', '']

    for st in stages:
        ss = by_stage.get(st['id'], [])
        L += [f"## {st['title']}", '']
        if st.get('summary'):
            L += [st['summary'], '']
        ms = st.get('milestone_summary')
        if ms:
            L += [ms, '']
        for v in st.get('views', []):
            L += [f'![{st["title"]} — {v["name"]}]({v["path"]})', '']
        if not ss:
            L += [f"*No steps recorded for this stage.{(' ' + st['skipped_reason']) if st.get('skipped_reason') else ''}*", '']
            continue
        for s in ss:
            L += card(s, record)

    reps = [s for s in proc if s.get('repeats')]
    if reps:
        L += ['## Repeated work', '', 'One instance is documented in full; the rest follow the rule.', '']
        for s in reps:
            r = s['repeats']
            L.append(f"- **{s['id']}** — {r.get('rule', '')} ({r.get('instances', '?')} instances"
                     + (f"; `{r['table']}`" if r.get('table') else '') + ')')
        L.append('')
    corr = [s for s in proc if s.get('correction')]
    if corr:
        L += ['## Corrections', '', 'What went wrong, and the step that fixed it.', '']
        for s in corr:
            L.append(f"- **{s['id']}** corrected {s['correction']['of']}: {s['correction'].get('evidence', '')}")
        L.append('')

    L += ['## What this guide cannot tell you', '']
    gaps = []
    for t in ('inspected', 'inferred', 'demonstrated'):
        if tiers.get(t):
            gaps.append(f"{tiers[t]} step(s) are **{t}**: " + TIER_TEXT[t].split(': ', 1)[1] + '.')
    if unmapped:
        gaps.append(f'{unmapped} interface line(s) are UNMAPPED: use the script or work out the route by hand.')
    if needs:
        gaps.append(f'{len(needs)} step(s) have no written goal or why yet.')
    gaps.append('The model\'s look in a render, mesh detail beyond counts and dimensions, and anything done '
                'outside Blender are not covered by the census.')
    L += [f'- {g}' for g in gaps]
    L.append('')
    return '\n'.join(L).rstrip() + '\n'


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__.split('\n\n')[0])
    ap.add_argument('--record', required=True)
    ap.add_argument('--steps', required=True)
    ap.add_argument('--out', required=True)
    a = ap.parse_args(argv)
    record = json.loads(Path(a.record).read_text())
    steps = load_steps(a.steps)
    text = build(record, steps)
    Path(a.out).write_text(text)
    print(f'wrote {a.out}: {len(steps)} step(s), {len(text.splitlines())} lines')
    return 0


if __name__ == '__main__':
    sys.exit(main())
