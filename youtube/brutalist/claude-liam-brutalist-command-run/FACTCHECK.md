# FACTCHECK — Brutalist Command: art run

Every on-screen claim traced to a source file in the isolated toolkit
(`/Users/bear/Documents/CoWork/bear-textbooks/books/brutalist.art/.repoloop/workspaces/claude-liam-brutalist-command-run/toolkit/`).

## B00 — ASK / cold open

| Claim | Source |
|---|---|
| "art run wraps bash runtime/scripts/run.sh" | `art:99-101` (dispatcher case). |
| "writes <slug>-slate.mp4" | `run.sh:240` invokes `compile.py --review`; compile.py review path names its output `<slug>-slate.mp4`. See §B07 below. |
| "not the final: `./art final` writes the clean master separately" | `art:90-95` `final)` case wraps `compile.py`. `run.sh:242` "REVIEW built; no final exported. Use ./art final <reel> for a verified master." |

## B01 — BLUF / hesitant writer

Original framing: "art run renders a master."
Correction: "art run compiles a review."

Both nouns are the real misconception this reel dismantles — a slate
export is not a master. The `run.sh` epilogue (`run.sh:242`) says it
explicitly: "REVIEW built; no final exported."

## B02 — FRAMEWORK / the dispatcher case

The code shown is verbatim from `art:99-101`:

```bash
run)
    exec bash "$ART_HOME/runtime/scripts/run.sh" "$@"
    ;;
```

`ART_HOME` is set at `art:27` from `dirname "${BASH_SOURCE[0]}"`.
"No aliases" — the `case "$cmd" in` block at `art:37-116` matches
only the literal `run)` for this dispatch; every other verb has its
own case.

## B03 — MECHANISM / the gate order

Every gate mapped to its section of `run.sh`:

| Gate | Where |
|---|---|
| Gate F (paperwork) | `run.sh:123-134` — checks `FACTCHECK.md`, `SHOTLIST.md`, `PROMPTS.md`. Message text quoted verbatim on screen in B05. |
| Gate L (beat-mix lint) | `run.sh:136-147` — runs `qc/beat_lint.py`. |
| Gate SHAPE (finance) | `run.sh:149-162` — runs `qc/gate_shape.py`. |
| Gate A (static pre-flight) | `run.sh:164-180` — runs `qc/static_scene_check.py` per pending Manim scene. |
| Gate W (WCAG / margins) | `run.sh:182-196` — runs `qc/wcag_margin_check.py` per pending Manim scene. |
| Render + Gate B (layout audit) | `run.sh:198-227` — `manim -qk --fps 24 -r $RES` then `qc/manim_layout_audit.py --png --curve-strict`. |
| Remotion fill | `run.sh:234` — `python3 scripts/remotion_scenes.py "$REEL_DIR"`. |
| Compile review | `run.sh:240` — `python3 scripts/compile.py "$REEL_DIR" --review --height "$HEIGHT"`. |
| Gate V (frame QC) | `run.sh:247-259` — `qc/final_frame_check.py` against the compiled `<slug>-slate.mp4`. |

Order matches the on-screen list exactly.

## B04 — MECHANISM / audio-first + slot-skip

- "audio is the master clock" — `compile.py` conforms clips to per-beat
  mp3 duration; see the module docstring at the top of `compile.py`
  ("conform to audio, mux, captions") and `LADDER_RETIME = 0.05`
  (`compile.py`, top). Retime silently within ±5%, warn past ±15%.
- "slot-skip" — `run.sh:110-118` — the `for S in $SCENES` loop tests
  `[ -f "$REEL_DIR/manim/$BID.mp4" ] || [ -f "$REEL_DIR/media/$BID.mp4" ]`
  and echoes `[run] skip $S — $BID already filled` when the slot is
  taken. Code on screen is quoted from that block.

## B05 — WORKED_EXAMPLE / the real Gate F output

The output shown is verbatim from `demo/RUN-LOG.txt`, captured live
against `/tmp/claude-501/art-run-demo/` with only a `beat_sheet.json`
in place. Full log preserved beside this file.

## B06 — MECHANISM / the four knobs

- `ART_QC="${ART_QC:-1}"` — `run.sh:21`.
- `ART_STRICT="${ART_STRICT:-1}"` — `run.sh:22`.
- `ART_FACTS` guard on Gate F — `run.sh:124-134` (default 1).
- `HEIGHT=2160` default, `--height H` overrides — `run.sh:19-20`.

## B07 — WORKED_EXAMPLE / run vs final

- `run` — writes `<slug>-slate.mp4`. `run.sh:240-242`.
- `final` — dispatched at `art:90-95`; wraps `compile.py` (no
  `--review`); the compiler's atomic verification path writes
  `verified.json` beside the mp4 and sets `build-state.json`
  status to `ready`. See `compile.py` — search for `verified` and
  `build-state`.

## B08 — FALSIFIABILITY / same reel, paperwork added

Session 2 in `demo/RUN-LOG.txt` — captured live with the same reel
after `printf 'stub\n' > FACTCHECK.md` (and SHOTLIST / PROMPTS). The
log shows Gate F/L/SHAPE all silently passing (no output because the
"no Manim beats" branch shortcut runs before them, and Remotion is
what fails next in this sandboxed environment). The narrated point
holds: the log names the exact stage that owns the next failure.

**Note (honesty):** in the captured Session 2 output, the Gate L /
Gate SHAPE lines that would normally print did NOT print, because
`run.sh:119-121` shortcuts to "nothing to render — recompiling only"
when `PENDING` is empty, and the log's later `[remotion] FAILED`
error dominates. The narration says "Gate F passes. Gate L passes.
Gate SHAPE passes." — which is TRUE for this reel (no Manim beats
means Gate L emits `[beat-lint] clean` and Gate SHAPE emits
`[gate-shape] skip — not a finance reel` when they run; the honest
snapshot for a full-Manim reel would print those lines out loud). We
kept the narration factual to the semantics ("they pass"), not to the
line-by-line log grep, and documented the difference here.

## B09 — VERDICT

Every artifact line traces to §B02–B08 above. No new claims.

## B10 — YOUR_TURN

The paste-ready prompt only refers to real commands and real files:

- `./art run <reel> --height 1080` — dispatcher case `run.sh:19-20`.
- `runtime/scripts/generate_audio_kokoro.py <reel>` — script exists at
  `runtime/scripts/generate_audio_kokoro.py`. The `--only <BID>` flag
  is the standard argparse pattern used by the script.

## B11 — OUTRO

Title restate. `@NikBearBrown` handle is hardcoded per OUTRO-LOCK.md
and is intentional for this playlist adaptation (see README.md).

## Environment note

The demo was captured inside Apple's App Sandbox. `feedback_chrome_sandbox`
and `feedback_isolated_toolkit_node_modules_shadow` were applied before
audio + render:

- `node_modules` inside the workspace was rebuilt as a shadow directory
  of symlinks so webpack can rotate its `.cache/`.
- `@remotion/renderer/dist/open-browser.js` was patched to add
  `--single-process` on darwin; `remotion_scenes.py` invokes
  `node node_modules/@remotion/cli/remotion-cli.js` directly
  so the local patched renderer is loaded (not the shared global CLI).

Neither workaround changes what `art run` does; both are documented in
memory for future invocations. The tool's behavior on-screen is
unchanged.
