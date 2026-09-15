# FACTCHECK — Brutalist Command: art todo

Every claim spoken or shown, checked against the actual source in
`runtime/scripts/todo.py` (SHA-256 `dff5d4bcbae5e188af335c892033ac030626f0a97442036c1da50a101275fb80`)
and `runtime/scripts/beat_plan.py`.

## Claims and evidence

| # | Claim (on screen / spoken) | Verified against | Verdict |
|---|---|---|---|
| 1 | `art todo` is a receipt of `beat_sheet.json`, not a hand-editable list. | `todo.py:12` — "…never hand-edit it — change the beat sheet instead". | ✓ verbatim intent. |
| 2 | Reads `<reel>/beat_sheet.json`, writes `<reel>/todo.json` + `<reel>/STATUS.md` + `<reel>/ToDo.md`. | `todo.py:103–105`. | ✓. |
| 3 | Each beat gets six fields: `status`, `on_disk`, `method`, `who`, `slot`, `prompt` (+ `label`). | `todo.py:61–71`. | ✓ — the dictionary literal in `build_ledger`. |
| 4 | `status` is `filled` when a media slot exists on disk, else `needs-fill`. | `todo.py:39–46` (`resolve_slot`) + `todo.py:59–63`. | ✓. |
| 5 | Slot precedence: `media/<BID>.mp4` > `manim/<BID>.mp4` > `manim/<BID>.mov` > `media/<BID>.png` > SLATE. | `todo.py:41–45`. | ✓ verbatim tuple order. |
| 6 | Five fill methods: `manim`, `remotion`, `ai-video-prompt`, `historical-image`, `user-capture`. | `beat_plan.py:9–10` header + case-branches on lines 50–86; CLI help on `todo.py:94–96`. | ✓. |
| 7 | Two of those methods (`manim`, `remotion`) are `pipeline`; the other three are `human`. | `beat_plan.py` — every branch returns `{"responsible": …}`. | ✓. |
| 8 | Flags: `--method`, `--open`, `--json`. | `todo.py:93–99`. | ✓. |
| 9 | `--method` accepts a method name OR a scene hint (`animated_graphics`). | `todo.py:110–112` — matches on `e["method"]` OR `e["scene_hint"]`. | ✓. |
| 10 | Regenerated automatically on every compile via `run.sh`. | `todo.py:14–15` (docstring). Also verified: `runtime/scripts/run.sh` calls `todo.py`. | ✓. |
| 11 | No `beat_sheet.json` → `sys.exit(f"[todo] no beat_sheet.json in {folder}")`, exit 1. | `todo.py:50–51`. Verified with a live run against `demo/empty-reel/` (see `demo/RUN-LOG.md`). | ✓ reproduced. |
| 12 | Positional argument: one reel folder. | `todo.py:93`. | ✓. |
| 13 | `--json` prints `todo.json` (with any filter applied) to stdout. | `todo.py:114–115`. | ✓ reproduced. |
| 14 | `ToDo.md` only lists beats whose owner is `human` AND status is `needs-fill`. | `todo.py:181`. | ✓ verified against the live example — the `remotion` and `manim` beats never appear in `ToDo.md`. |
| 15 | `ToDo.md` fill-source suggestions include Smithsonian Open Access, Wikimedia Commons, Library of Congress by default. | `todo.py:174–175`. | ✓ appear verbatim in the live `demo/example-reel/ToDo.md`. |

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

## Corrections applied during authoring

- Draft narration for B03 first said "three flags"; the source has four
  arguments (positional `reel` + three flags). Corrected to "point it at a
  reel folder … four flags total (one positional, three optional)".
- Draft B06 originally said the ledger "renders remotion and manim scenes";
  the ledger only *reports* them as pipeline-owned. Rendering happens in
  `remotion_scenes.py` / `render_manim_scenes.py`. Corrected.

## Registry / gaps recorded honestly

- `docs/PIPELINE-SAFETY.md` and `docs/FELLOWS-SUBMISSION.md` reference
  historical checkers (`scripts/type_check.py`, `reference/type-spec.md`) that
  are not currently shipping in this toolkit snapshot. TYPECHECK.md records
  this explicitly — the current type QC is visual (Read PNG frames), not the
  legacy static checker.
