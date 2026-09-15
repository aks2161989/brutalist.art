# FACTCHECK — Brutalist Command: art run (Short cut)

Six retained beats only (B00, B01, B03, B07, B10, B11). Every remaining
on-screen claim traces to a source file in the isolated toolkit
(`toolkit/`). Parent factcheck is preserved in the vertical parent reel
for the dropped beats (B02, B04, B05, B06, B08, B09).

## B00 — ASK / cold open

| Claim | Source |
|---|---|
| "art run wraps bash runtime/scripts/run.sh" | `art:78-80` dispatcher case. |
| "writes <slug>-slate.mp4" | `run.sh:240` invokes `compile.py --review`; compile.py review path names its output `<slug>-slate.mp4`. See §B07 below. |
| "not the final: `./art final` writes the clean master separately" | `art:90-95` `final)` case wraps `compile.py`. `run.sh:242` "REVIEW built; no final exported. Use ./art final <reel> for a verified master." |

## B01 — BLUF / hesitant writer

Original framing: "art run renders the master video file."
Correction: "art run compiles the review video file."

Both nouns are the real misconception this reel dismantles — a slate
export is not a master. The `run.sh` epilogue (`run.sh:242`) says it
explicitly: "REVIEW built; no final exported."

## B03 — MECHANISM / the gate order

Every gate mapped to its section of `run.sh`:

| Gate | Where |
|---|---|
| Gate F (paperwork) | `run.sh:123-134` — checks `FACTCHECK.md`, `SHOTLIST.md`, `PROMPTS.md`. |
| Gate L (beat-mix lint) | `run.sh:136-147` — runs `qc/beat_lint.py`. |
| Gate SHAPE (finance) | `run.sh:149-162` — runs `qc/gate_shape.py`. |
| Gate A (static pre-flight) | `run.sh:164-180` — runs `qc/static_scene_check.py` per pending Manim scene. |
| Gate W (WCAG / margins) | `run.sh:182-196` — runs `qc/wcag_margin_check.py` per pending Manim scene. |
| Render + Gate B (layout audit) | `run.sh:198-227` — `manim -qk --fps 24 -r $RES` then `qc/manim_layout_audit.py --png --curve-strict`. |
| Remotion fill | `run.sh:234` — `python3 scripts/remotion_scenes.py "$REEL_DIR"`. |
| Compile review | `run.sh:240` — `python3 scripts/compile.py "$REEL_DIR" --review --height "$HEIGHT"`. |
| Gate V (frame QC) | `run.sh:247-259` — `qc/final_frame_check.py` against the compiled `<slug>-slate.mp4`. |

Order matches the on-screen list exactly.

## B07 — WORKED_EXAMPLE / run vs final

- `run` — writes `<slug>-slate.mp4`. `run.sh:240-242`.
- `final` — dispatched at `art:90-95`; wraps `compile.py` (no
  `--review`); the compiler's atomic verification path writes
  `verified.json` beside the mp4 and sets `build-state.json`
  status to `ready`. See `compile.py` — search for `verified` and
  `build-state`.

## B10 — YOUR_TURN

The paste-ready prompt only refers to real commands and real files:

- `./art run <reel> --height 1080` — dispatcher case `run.sh:19-20`.
- `runtime/scripts/generate_audio_kokoro.py <reel>` — script exists at
  `runtime/scripts/generate_audio_kokoro.py`. The `--only <BID>` flag
  is the standard argparse pattern used by the script.

## B11 — OUTRO

Title restate. `@NikBearBrown` handle is hardcoded per OUTRO-LOCK.md
and is intentional for the playlist adaptation (see parent README.md).

## Derivative provenance

- Parent (native portrait) — `youtube/brutalist/claude-liam-brutalist-command-run/vertical/`, SHA-256 of `claude-liam-brutalist-command-run-vertical.mp4` = `402ba743ae61fdc30b21965ae994055a3bded95e6389cbf0040505362bc6764e`.
- Cut mechanism — `shorts.py --drop B02 B04 B05 B06 B08 B09 --no-endcard --no-outro-rewrite`; every retained beat's `.mp4` + `.mp3` copied byte-for-byte from the parent (no crop, no re-render, no regenerated audio).
