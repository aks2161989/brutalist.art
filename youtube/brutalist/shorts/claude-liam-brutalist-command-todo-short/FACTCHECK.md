# FACTCHECK — Brutalist Command: art todo — Short (9:16)

Derivative of the parent 16:9/vertical FACTCHECK. This Short retains the 9
beats that carry claims still made on-screen or spoken. Claims that live only
in dropped beats (B05 six-field entry anatomy, B06 five-lane table detail,
B10 look-for rubric) are NOT made in this Short and are therefore not
re-audited here — see the parent factcheck for those. Every claim below is
present in a retained beat's narration or on-screen text.

Source of truth: `runtime/scripts/todo.py` (SHA-256
`dff5d4bcbae5e188af335c892033ac030626f0a97442036c1da50a101275fb80`) and
`runtime/scripts/beat_plan.py`.

## Claims retained in this Short and evidence

| # | Claim (retained beat) | Verified against | Verdict |
|---|-----------------------|------------------|---------|
| 1 | (B01/B02/B09) `art todo` is a *receipt* of `beat_sheet.json`, not a hand-editable list. | `todo.py:12` — "…never hand-edit it — change the beat sheet instead". | ✓ verbatim intent. |
| 2 | (B00/B02/B09) Reads `<reel>/beat_sheet.json`, writes `<reel>/todo.json` + `<reel>/STATUS.md` + `<reel>/ToDo.md`. | `todo.py:103–105`. | ✓. |
| 3 | (B03) Three optional flags: `--open`, `--method`, `--json`; one positional reel folder. | `todo.py:93–99`. | ✓. |
| 4 | (B03) `--method` values: `manim | remotion | ai-video-prompt | historical-image | user-capture`. | `beat_plan.py` case-branches; CLI help `todo.py:94–96`. | ✓. |
| 5 | (B04) Live run output shape: header `[todo] example-reel: 0/5 filled → todo.json + STATUS.md + ToDo.md` and one row per beat with id/status/method/who/slot. | Reproduced against parent's `demo/example-reel` (parent `demo/RUN-LOG.md`). | ✓. |
| 6 | (B04/B09) Two lanes (`remotion`, `manim`) are pipeline; three (`historical-image`, `user-capture`, `ai-video-prompt`) are human. | `beat_plan.py` — every branch returns `{"responsible": …}`. | ✓. |
| 7 | (B07/B09) `--method <name> --open` filters the ledger to one lane's needs-fill beats; agent walks the queue, renders each, re-runs, empty rows drop off. | `todo.py:110–112` — filter matches on `e["method"]` OR `e["scene_hint"]`. | ✓. |
| 8 | (B08/B09) Missing `beat_sheet.json` → `sys.exit(f"[todo] no beat_sheet.json in {folder}")`, exit 1. Recovery is not a flag: author the sheet or point at a folder that has one. | `todo.py:50–51`. Live-verified in the parent's `demo/empty-reel/` run log. | ✓ reproduced. |

## Claims deliberately NOT made in this Short

- The Short does not enumerate the six-field entry anatomy (parent B05).
- The Short does not present the five-lane methods table (parent B06); the
  five method names appear only via the `--method` effect chip in B03 and via
  the five rows in the B04 live run.
- The Short does not read the paste-ready Claude Code prompt or the
  three-item look-for rubric aloud (parent B10). The 16:9 long-form / vertical
  companion carries those.
- No claim that `art todo` renders anything itself — the ledger only reports;
  rendering is `compile.py` / `remotion_scenes.py`.
- No claim that `ToDo.md` is auto-committed or auto-emailed.

## Claims deliberately NOT made

- The reel never promises `art todo` renders anything itself — it only writes
  the ledger. Rendering is separate (`compile.py`, `remotion_scenes.py`).
- No claim that `ToDo.md` gets committed anywhere or emailed anywhere. The
  compiler writes it into the reel folder; the human decides what to do with
  it. (Consistent with `docs/PIPELINE-SAFETY.md`.)
- No claim that the fill-source suggestions in `ToDo.md` are the only good
  archives — the source clearly documents these as defaults with topic-based
  extensions (`_topic_extra`), and the reel doesn't spend a beat on that
  extension logic.
- No claim that `--method` is required; every flag is optional.

## Corrections carried over from parent authoring

- Parent draft B03 first said "three flags"; source has four arguments
  (positional `reel` + three flags). Retained wording says "four surfaces,
  three of them optional" — matches source.
- Parent draft B06 originally said the ledger "renders remotion and manim
  scenes"; the ledger only *reports* them. Rendering happens in
  `remotion_scenes.py` / `render_manim_scenes.py`. Corrected in parent
  (B06 dropped in this Short; correction still holds where relevant).

## Registry / gaps recorded honestly

- `docs/PIPELINE-SAFETY.md` and `docs/FELLOWS-SUBMISSION.md` reference
  historical checkers (`scripts/type_check.py`, `reference/type-spec.md`) that
  are not currently shipping in this toolkit snapshot. `TYPECHECK.md` records
  this explicitly for the Short — the current type QC is visual (PNG frame
  read + Pillow bbox on the compiled Short), not the legacy static checker.
