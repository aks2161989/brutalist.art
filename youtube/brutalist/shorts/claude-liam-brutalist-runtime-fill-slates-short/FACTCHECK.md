# FACTCHECK — Brutalist Utility: fill_slates.py (Short)

**Source of truth:** `runtime/scripts/fill_slates.py` (155 lines, verified locally)
**Episode source SHA-256 (invocation):** `369d475d7b5ee3640a152eae2cd6b441f4613e122da92af7c0daec94f902e876`
**Parent master SHA-256:** `5f75111fcda2b52b0af8c1f5c49963d0fc45e81e3fe5f811ab4d135b3ee9d159`
**Toolkit baseline SHA-256:** `92432609980c8ffc03bc1f00a1300fe1ac78bd7363b5b8ba9f2d389407d72b9d`
**Date:** 2026-09-10 · run_id `4aa81398c296468f990286536cf84ba3`

Every narrated claim traces to a specific block of `fill_slates.py`. All
retained narration and every retained visual is copied byte-for-byte from
the vertical parent's `mp3/` and `media/` directories — nothing was
re-generated or rewritten for this Short.

## Retained-beat claims (Short cut)

| Beat | Claim / on-screen text | Line range | Evidence in source |
|---|---|---|---|
| B00 | "Three beats across two reels have no video and no remotion pattern." | — | Framing for the cold-open ask (illustrative, not a runtime claim). |
| B00 | "Fill them all with a Form A card so the review cuts play through." | 76–88 | `stamp_slates()` writes `shot.remotion.pattern = 'FormACard'`. |
| B01 | "Fill slates does not rewrite every beat in a reel. It stamps only the empty ones — no media on disk, no pattern in the sheet." | 46–63 | `slate_resolves()` + `find_slates()` skip patterned/rendered/silent beats. |
| B02 | "Walk books slash for every reel that has a beat sheet." | 129–137 | `main()` reel-discovery loop over `HERE.parent`. |
| B02 | Slate = "no media, no manim, no silent flag, no pattern." | 46–63 | `slate_resolves()` file checks + `find_slates()` skips. |
| B02 | Headline = "first eleven words of the narration." | 76 | `_truncate(narration_text, words=11)` (`stamp_slates()` head). |
| B02 | Two shell-outs: `remotion_scenes.py`, then `run.sh`. | 99–115 | `render_reel()` first + second `subprocess.run()`. |
| B02 | "Dry run is the default. Apply is the flag." | 12–17, 124 | Module docstring + `argparse` `--apply` action. |
| B07 | Disposable-fixture 5-beat book: B00/B01 slate, B02 patterned, B03 silent, B04 rendered. | — | Observed on `demo/fixture-book/` (`demo/dryrun.txt`, `demo/beat_sheet_after_stamp.json`). |
| B07 | `--books demo/` dry-run prints `1 reels, 2 slate beats to fill · fixture-book/demo-reel: [B00, B01]`. | — | Observed at capture time (parent's `demo/dryrun.txt`). |
| B08 | Missing `beat_sheet.json` → `find_slates` returns `([], None)`. Reel silently skipped. | 53–55 | `find_slates()` guard. |
| B08 | Non-zero `remotion_scenes.py` → `REMOTION FAIL: <last 300 of stderr>`; never calls `run.sh`. | 105–107 | `render_reel()` first branch. |
| B08 | Non-zero `run.sh` → `ART_RUN FAIL: <last 300 of stderr>`. | 113–115 | `render_reel()` second branch. |
| B08 | Zero slates → main loop reports `0 reels, 0 slate beats to fill`. | 141–142 | `main()` dry-run print. |
| B08 | Main-loop status test — any `'FAIL' in a` flags the reel. | 158 | `status = 'ok' if not any('FAIL' in a for a in acts) else 'FAIL'`. |
| B09 | Six-line verdict, whole surface in order. | 12–92, 99–120 | Composite of `_truncate`, `stamp_slates`, `render_reel`, and module docstring. |

## Named laws / invariants preserved in the Short

- **DEFAULT IS DRY-RUN.** The apply flag is opt-in. Every mutating statement
  in the Short's retained narration says "with `--apply`" or "flip out of
  dry run" explicitly.
- **THE FOUR SKIP CONDITIONS** are exhaustive. B01, B02, B07 and B09 all
  restate them at their own level (bluf, framework, worked example, verdict).
- **ONE PATTERN ONLY.** `stamp_slates` writes exactly `FormACard`. B02 and
  B09 both say so.

## Off-camera verifications inherited from the parent

- Whole 155-line `runtime/scripts/fill_slates.py` was read end-to-end by the
  parent's build; that fact-check is inherited unchanged (this Short changed
  no source claim).
- Live `fill_slates.py -h` output was captured for B03 (dropped in this Short
  but referenced in the parent's factcheck as evidence for the four-flag
  surface).
- Live `fill_slates.py --books demo/` dry-run output was captured for B07
  and is preserved verbatim in this Short.
- `find_slates()` + `stamp_slates()` were called directly on a copy of the
  fixture; the post-stamp `beat_sheet.json` shape shown in B07's footer is
  the observed output, not invented.

## Not claimed / deliberately out of scope

- The Short does not claim to have executed `--apply` end-to-end against
  the real `books/` tree. `--apply` has permanent side-effects on every
  affected reel's `beat_sheet.json`.
- The Short does not enumerate every possible subprocess return-code path
  from `run.sh` — B08 only names the two `render_reel()` failure branches
  and the two implicit ones (no beat sheet; no slates).
- The Short omits the parent's four MECHANISM code-cascade beats (B03-B06)
  and the extended YOUR TURN composer (B10) — the full-length teardown is
  the canonical reference for those.
