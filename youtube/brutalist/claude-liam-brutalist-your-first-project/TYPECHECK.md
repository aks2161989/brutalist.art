# TYPECHECK.md — Your First Brutalist Project (landscape 16:9)

## The legacy checker is missing from this cut

`skills/make/ai-explainer/SKILL.md` (line 786-787) and `run.sh` reference a **`scripts/type_check.py`** that runs a `TYPECHECK.md` gate for §8.1 min-size, §8.2 overflow, §8.3 contrast, §8.4 kerning, §8.5 no-wordy-card, §8.6 golden strings.

The isolated toolkit for this run contains **no** `scripts/type_check.py`. `reference/type-spec.md` is also absent.

```
$ find /Users/bear/Documents/CoWork/bear-textbooks/books/brutalist.art/.repoloop/workspaces/claude-liam-brutalist-your-first-project/toolkit -name "type_check.py" -o -name "type-spec.md"
(no matches)
```

Per the invocation brief:

> Record such gaps honestly, use the available runtime checks and actual image inspection, and never claim a missing checker passed.

This file records what was checked and how.

## What DID run — Gate V (`runtime/qc/final_frame_check.py`)

Gate V is a frame-level visual QC gate that samples every beat at 50% and 85% and checks:

- **EDGE-BLEED** (BLOCKER) — ink outside the 5% title-safe inset (`SAFE = {x:96, y:54, w:1728, h:972}` in 1920x1080; scaled to 3840x2160).
- **CANVAS-FILL / UNDERFILL** (MAJOR) — ink bounding box coverage of SAFE below `FILL_MIN = 0.55`.
- **LOW-CONTRAST** (MAJOR) — ink vs. background luminance separation below 0.30.
- **CLUSTERED** (MAJOR) — width or height span below 0.5 of SAFE (large empty band).

**Result:** `Frames sampled: 24  ·  BLOCKER: 0  ·  MAJOR: 0`. Clean. Full report: `_qc/REPORT.md`.

## Manual visual typography review (image-capable Read tool)

Each beat's mid-frame was extracted at 4K native (later downscaled for review) and read via the image tool. Typography observations:

| Beat | Typeface | Sizes | Result |
|---|---|---|---|
| B00 | Serif greeting (EB Garamond), sans UI labels, mono command line | Greeting ~72px, command ~54px, folder chip ~48px, running text ~44px | Legible from a room. Terracotta only on send button. No overflow. |
| B01 | Serif (EB Garamond), 132px | 4 lines, centered, 1.24 leading | Correction from `demo` to `claim` is unambiguous. No overflow. |
| B02 | Mono code + serif spark | Code ~47px (h * 0.022), title bar ~28px, spark ~22px | All JSON fits inside the card body. Spark italic reads clearly. |
| B03 | Composer (serif greeting + mono command) | Same class as B00 | Command wraps to 2 lines within card. |
| B04 | Artifact card — serif heading + sans lines | Heading ~46px, lines ~28px, numeral 700-weight | All 7 lines fit; numerals in terracotta. |
| B05 | Artifact card | Same class | 6 lines fit comfortably; card fills width. |
| B06 | Composer + output | Same as B00 | 4 output lines fit; running text runs terracotta. |
| B07 | Diff code card | Same as B02 | 5 modified files + 2 comment lines fit; sparse enough to breathe. |
| B08 | Artifact card | Same as B04 | 7 lines fit; dimensions text reads without wrapping. |
| B09 | Artifact card | Same as B04 | 7 lines; the URLs collapse to filename/PR wording (no raw URLs on-screen). |
| B10 | Composer + output | Same as B00 | Command wraps to 2 lines; GOOD/BAD lines terracotta on cue. |
| B11 | Serif title outro | Title ~108px, handle ~64px, sub-mark ~34px | Fills poster; terracotta on terminal period only. |

**Findings.** No sub-24px effective text found. No overflow of card borders. No overlap. Terracotta appears on exactly one focal element per beat (the accent law).

## Golden-string audit (manual)

Every user-facing string that carries a specific claim was read against source:

- "@HumanitariansAI" — per invocation brief (playlist channel).
- "Kokoro am_onyx" — per `skills/make/ai-explainer/SKILL.md` Channels table and `runtime/scripts/generate_audio_kokoro.py` docstring.
- "review-cut.mp4 at 3840 x 2160" — per compile output `[art] wrote … (147.9s, audio: per-beat timeline …)`.
- "twelve conformed per-beat clips in clips/" — matches `ls clips/` (12 files).
- "art vertical PLANS the portrait sheet" — matches `./art` CLI dispatcher's own line ("full-length 9:16 companion (no shortening)").

No fabricated numbers on screen.

## Not checked (with reason)

- **§8.4 kerning** — the spec references a kerning skill that does not ship in this cut. Fonts used are EB Garamond and system UI sans/mono, both bundled or system-default. No missing-glyph substitution observed.
- **§8.6 golden strings automated** — no `reference/type-spec.md` shipped, so no automated golden list to compare against. Manual audit above.

## Conclusion

The absent legacy type checker is a documented gap, not a claim of pass. Gate V ran clean, and the manual visual audit above found zero typographic blockers. Bear's viewing is next.
