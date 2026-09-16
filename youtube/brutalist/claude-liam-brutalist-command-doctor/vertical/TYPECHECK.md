# TYPECHECK — vertical 9:16

## What the legacy `scripts/type_check.py` would have covered

Same GATE T type checker referenced in the landscape TYPECHECK.md — not
shipped in this toolkit revision. Substitute below; missing-checker gap
noted honestly, no claim of passing.

## Substitute — visual-typography review this build actually performed

- `runtime/qc/final_frame_check.py` (Gate V) ran on the finished 4K
  portrait master: 24 beat-aware steady-state samples, BLOCKER 0, MAJOR 0.
- Every portrait frame in `_qc/frames-vertical/*.png` (3 per beat · 36
  stills) was extracted and read with the image-capable Read tool.
- Programmatic bbox/coverage/edge-bleed analysis ran on B01's steady-state
  samples during the portrait tuning loop (values printed in
  `CHECKS-REPORT.md` §"Portrait B01 clearance recipe").

## Per-beat portrait typography notes

- **B00 ClaudeComposerAsk916** — `Jambo, Liam` greeting stacks above the
  composer in the portrait layout; the ask wraps at ~460 CSS-px inside
  the card; `@HumanitariansAI` folder chip and output lines legible below.
- **B01 BrutalistHesitantWriter916** — `fontSize: 210, lineSpacing: 4.5`
  after applying the portrait scale patch. Coverage 64.3% (0.5) and
  60.0% (0.85) of SAFE, no edge overflow.
- **B02-B08 ClaudeCodeBeat916** — Onda-style mono at the shipped 916
  code-card scale. **Known limitation**: some long lines truncate at the
  white card's right edge in portrait; ink stays inside the card, salient
  part of every line remains legible, and the full text is available in
  the landscape master and `demo/RUN-LOG.txt`.
- **B09 ClaudeVerdictArtifact916** — 6 lines, each wrapping across 2-3
  portrait lines. Terracotta numerals per line. Ink/background contrast
  passes Gate V's `CONTRAST_MIN` 0.30 floor.
- **B10 ClaudeComposerAsk916 (Your Turn)** — the paste-ready prompt wraps
  inside the composer card; ✅/❌ emojis in the grading lines render.
- **B11 ClaudeTitleOutro916** — title "Brutalist Command: art doctor."
  breaks across the portrait card centre; `@NikBearBrown` handle beneath
  per OUTRO-LOCK (playlist-adaptation exception, flagged in README).

## Gate V exit state (the substitute type gate that IS shipped)

**BLOCKER 0 · MAJOR 0 · Clean ✓** (`vertical/_qc/REPORT.md`).

## Conclusion

No typography defect surfaced in visual review or in Gate V beyond the
documented portrait-code-beat truncation carried across the playlist.
Bear's editorial pass is welcome to flag any portrait line that reads as
truncated in a way that hurts comprehension; the fix would be to trim the
source code fragment rather than resize the composition.
