# Brutalist Utility: capture_sim.py

Episode 42 of the Brutalist playlist (order 47 in full sequence). AI Explainer teardown of `runtime/scripts/capture_sim.py` — the Playwright wrapper that records D3 HTML simulations as clean mp4s (baseline `output.mp4`, range-sweep `change.mp4`, or a custom `--script`/`--click-through` cut), served from a local HTTP port and remuxed with ffmpeg.

- **Voice:** Kokoro `am_onyx` (Liam, in for Bear)
- **Playlist:** Brutalist · Channel: `@HumanitariansAI`
- **Run ID:** `d5030c4cf83c4be7abdb281854682ab7` (re-verification 2026-09-13; original build `91c96a0989324688820852264379a94d`; Gate V re-confirmed 0/0 both aspects)
- **Length:** 278.1 s across 12 beats, both aspects (portrait length independent — see `vertical/CHECKS-REPORT.md`)

## Deliverables (both native 4K, Gate V clean)

| Aspect | File | Dimensions |
|---|---|---|
| Landscape | `exports/landscape/claude-liam-brutalist-runtime-capture-sim.mp4` | 3840×2160 |
| Vertical  | `exports/vertical/claude-liam-brutalist-runtime-capture-sim-vertical.mp4` | 2160×3840 |

SHA-256 hashes are in each aspect's `VISUAL-REVIEW.json`.

## Contents

- `beat_sheet.json` (12 beats, landscape) · `vertical/beat_sheet.json` (12 beats, portrait)
- `SCRIPT.md`, `SOURCES.md`, `FACTCHECK.md`, `SHOTLIST.md`, `PROMPTS.md`, `TYPECHECK.md`, `CHECKS-REPORT.md` — landscape
- `vertical/` mirror of the six paperwork files (shared where accurate; per-aspect `TYPECHECK.md` + `CHECKS-REPORT.md`)
- `demo/` — disposable synthetic fixtures used to demonstrate the tool source-backed. Includes:
  - `sim-source/00-tiny-wave.html` — a one-file D3 v7 sine wave with `input#k` slider
  - `scripts/tiny-wave-sweep.json` — a 5-step DSL example that opens with a `set` verb (per module docstring)
  - `help.txt` — verbatim `capture_sim.py -h`
  - `failure-sandbox.txt` — verbatim Apple App Sandbox Mach-port denial (the observed limitation taught in B08)
  - `failure-sim-not-found.txt`, `failure-bad-script-shape.txt`, `failure-script-and-clickthrough.txt` — pre-browser guard evidence
  - `RUN-LOG.txt` — the consolidated observation log
- `media/`, `mp3/`, `clips/`, `_qc/` — per-beat working files (landscape); mirrored under `vertical/`
- `VISUAL-REVIEW.json` — AI review record (this invocation's `run_id`, current SHAs, real frame evidence hashes)

## Playlist adaptation flag for the human reviewer

The **OUTRO card is locked** by `OUTRO-LOCK.md` — it stamps the hardcoded `@NikBearBrown` handle even though this reel lives in the Brutalist playlist under `@HumanitariansAI`. Playlist adaptation IS on for:

- the metadata `channel` field (`@HumanitariansAI`)
- the composer `folderLabel` prop on B00 and B10 (`@HumanitariansAI`)
- this README

**If the human reviewer wants the outro card to show `@HumanitariansAI`**, that requires either editing `runtime/remotion/src/scenes/ClaudeTitleOutro.tsx` and `ClaudeTitleOutro916.tsx` to accept a handle prop, or restating the outro doctrine — same call-out flagged on ep39, ep40, ep41.

## Honest limitation surfaced

`capture_sim.py` itself needs Chromium to spawn a child process. Inside Claude Code's Apple App Sandbox, Chromium's Mach-port bootstrap is denied (`Permission denied (1100)`). B08 quotes the exact failure verbatim. **No captured mp4 from a live browser run** is included in this reel; every code beat teaches the source directly, and the reel presents the sandbox failure as a real finding rather than faking a clip. Running `capture_sim.py` outside the sandbox — in a normal terminal or CI — is the ordinary path; that is a fellow instruction, not a shortcut we took here.

## Human review next

Bear watches the two files and can leave notes in `FEEDBACK.md`. Nothing has been published, uploaded, or committed to git.
