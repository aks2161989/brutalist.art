# TYPECHECK — Brutalist Command: art final — Short (ep 33)

This project has no legacy type-checker step; typography and layout are
inspected by opening real rendered frames. This file records that visual
typography review, distinct from a language type check.

## Fonts / weight / colour

| Beat | Pattern | Face | On-screen sample | Verdict |
|---|---|---|---|---|
| B00 | ClaudeComposerAsk916 | Claude serif for `art final` title, house sans for composer body, mono for output cards | 'Hei, Liam' greeting; 'Compile this reel to a verified 4K master…' ask; three output lines in fixed-width | Legible at 2160×3840; no clipping inside SAFE916. |
| B01 | BrutalistHesitantWriter916 | Serif (Georgia-family), fontSize 230, lineSpacing 2.5 | Three big-serif lines: `art final` / `verifies` / `twice.` (post-flip). Terracotta accent on the caret. | Big-serif fills the frame without overflowing SAFE916. Matches `feedback_hesitant_writer_portrait_bluf_recipe` (lineSpacing not fontSize is the lift). |
| B06 | ClaudeCodeBeat916 | SF Mono for the code block, sans title bar | Verbatim from `compile.py:803-825`. Card title 'compile.py:803-825 — atomic replace' (updated 2026-09-13 from parent). `timeline = work / 'resolved-sheet.json'`, `atomic_json(timeline, sheet)`, and file-existence guard `if any(not Path(p).is_file()` visible. Spark: 'Encode into a temp. Replace only after every check clears.' | Card inside SAFE916; long code lines truncate at the right edge of the card, as documented (readers wanting raw script go to the landscape master). |
| B07 | ClaudeCodeBeat916 | Same as B06 | Verbatim receipt shape + read-side pattern + three '#' publication caveats + spark 'Ready is a machine claim. Publication is a human step.' | Same layout constraints; card fits, no ink outside SAFE916. |
| B09 | ClaudeVerdictArtifact916 | Serif heading, sans body, terracotta numerals | Heading 'art final — the whole surface, in the order you use it'; six numbered lines. | All six lines visible; terracotta line numbers accent, no orphaned words. |
| B11 | ClaudeTitleOutro916 | Serif for the title restate, sans for the handle | 'Brutalist Command: art final.' (terracotta period), '@NikBearBrown', slug-seeded mascot | OUTRO-LOCK layout; centered, well inside SAFE916. |

## Colour palette (Claude)

- Cream ground `#FAF9F5` (verified from B00/B01/B09/B11 backgrounds — no
  colour cast at 2160×3840).
- Ink text `~#3D3929` (verified from serif hesitant-writer letters and verdict lines).
- Terracotta accent `~#D97757` (verified on B00 running dot, B01 doomed
  tokens' caret, B09 numerals, B11 title period).
- Code card is white on the cream ground with a subtle grey border and a
  terracotta traffic-light dot (verified on B06/B07 title bars).

## Safe-area / SAFE916

Every retained beat's ink stays inside SAFE916 at the 15%/50%/85% percentiles
recorded in VISUAL-REVIEW.json. The parent's original portrait build already
passed Gate V for these same source mp4s; this Short is a subset of them, and
Gate V passed again on the new candidate encode before `os.replace`
(evidence: `<slug>.verified.json` was written and `build-state.json.status =
"ready"`).

## Captions

None. `metadata.captions = false`. No burned-in transcript, no SRT/VTT track,
no drawtext.

## Verdict

**PASS.** Typography, colour, and safe-area constraints hold on all inspected
frames. No blocker, no major fault. B06 updated with the corrected
`compile.py:803-825` reference and file-existence guard — verified in frame.
Long code lines in B06/B07 truncate horizontally inside SAFE916 as documented
— this is the accepted trade-off for the portrait aspect (matches parent behaviour).
