# TYPECHECK — landscape (3840×2160)

## Actual typography review

The public docs reference `scripts/type_check.py` and `reference/type-spec.md`; neither is present in this isolated toolkit snapshot. This TYPECHECK.md is the actual visual typography review that stood in for the absent legacy checker, per the BUILD-PROMPT guidance ("record such gaps honestly, use the available runtime checks and actual image inspection, and never claim a missing checker passed").

## What I actually did

- Ran `runtime/qc/final_frame_check.py` on the finished 4K master. Beyond BLOCKER/MAJOR edge-bleed and canvas-fill defects, this script also flags low-contrast ink and clustered-content patterns; none were raised on any of the 24 sampled frames.
- Read `_qc/contact_sheet.png` (24-tile grid, every beat at 50% and 85%) with the image-capable Read tool and inspected each tile for:
  - Line spacing (no lines butting into each other; no lines with orphan words).
  - Character kerning in serif titles and ClaudeVerdictArtifact headings (no dropped or overlapping glyphs).
  - Monospace legibility in code cards at 3840×2160 (all indents preserved; no truncated lines mid-token).
  - Accent-color consistency — the terracotta accent used only for numeric bullets, running indicator, brand rule, and hesitant-writer corrections.
  - Comma-vs-period rendering in narration cues that end sentences (all round dots present).

## Font stack in use

- CLAUDE_FONT.serif — Claude's serif face for titles and BLUF text (B01, B09 heading, B11 title).
- CLAUDE_FONT.ui — Claude's UI sans for composer chrome, folder labels, spark lines, verdict body.
- CLAUDE_FONT.mono — monospace for ClaudeCodeBeat code cards (B03–B08) and composer output lines.

All three families are shipped with the isolated toolkit's Remotion bundle and are visible at 4K without any fallback substitution.

## Notes

- No unshipped `scripts/type_check.py` was invoked. If/when it returns to the toolkit, this episode should be re-checked against it.
- The compiler's `SKIN LINT` warnings (recorded in CHECKS-REPORT.md) are informational and do not indicate a typography problem.
- Human typography review is pending Bear's playback.
