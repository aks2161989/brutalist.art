# TYPECHECK.md — The hai Skill (portrait 2160×3840)

The legacy `scripts/type_check.py` GATE T checker is not present in this
snapshot of the isolated toolkit (same finding as the landscape TYPECHECK).
This file records the actual image-level typography review of the portrait
master.

## Method

Same rubric as the landscape `TYPECHECK.md`: min type size, no overflow,
adequate contrast, no kerning artifacts, no wordy card, golden strings intact.
Portrait design reference is 1080×1920 (SAFE916: x 54–1026, y 96–1824);
the 4K render is scale=2. Frames extracted with ffmpeg and read as PNGs.

## Findings per beat

| Beat | Component (portrait wrapper) | Type check | Notes |
|---|---|---|---|
| B00 | ClaudeComposerAsk916 | ✓ | Composer stack native to 9:16; greeting serif, three output serif lines all inside SAFE916. |
| B01 | BrutalistHesitantWriter916 (portrait-scale patch active) | ✓ | fontSize=130, lineSpacing=2.65, 5 lines. The scale patch picks the 1080×1920 design ref so serif does not collapse to ~56% of intended size. Correction `reformats`→`forks` renders on cue; caret blink visible. |
| B02 | SkillTeardownAnatomy916 | ✓ | Folder tree reflows to full column width; monospace path names wrap where needed; callout box beneath, all inside SAFE916. |
| B03 | SkillTeardownPipeline916 | ✓ | Portrait vertical rotation (R1 reflow) — INPUT → 4 phases → OUTPUT stacked, arrows point down, all inside SAFE916. Footer note "The middle is your reel." fits above the spark line. |
| B04–B08 | SkillTeardownMechanism916 | ✓ | Portrait reflow uses R2 typography ramp; heading 82px, body 40px, quote 34px monospace inside terracotta-bordered card. Each body wraps inside content column. Verdict pill inside SAFE916. |
| B09 | ClaudeVerdictArtifact916 | ✓ | Six verdict lines, artifact card fills portrait content column, all inside SAFE916. |
| B10 | ClaudeComposerAsk916 | ✓ | Rewritten portrait command (shorter than landscape) fits composer card without overflow. Rubric output lines fit beneath. |
| B11 | ClaudeTitleOutro916 | ✓ | Title restate + `@NikBearBrown` handle + slug-seeded mascot, all native to 9:16. |

## Golden strings (verified verbatim)

- Outro title: `The hai Skill.` (terracotta period).
- Outro handle: `@NikBearBrown` (OUTRO-LOCK — hardcoded on claude-liam reels).
- Persona lines B00 + B11: "Liam, in for Bear."
- Composer folder chip on B00 + B10: `@HumanitariansAI`.

## Kerning / Pango fallback catch

Verified by eye. EB Garamond serif, UI sans, mono all match landscape rendering (same tokens, same fonts bundled in `runtime/fonts`). No visible fallback substitution.

## Contrast

Same tokens as landscape — ink `#3D3929` on cream `#FAF9F5` (~10:1). Terracotta accent used only for the send button, verdict pill, spark, and quote card border. Gate V's LOW-CONTRAST auto-check reports clean.

## Conclusion

No typography defects. Portrait reflows use their native 916 wrappers everywhere except the ClaudeVerdictArtifact-family which already has the wrapper. The BrutalistHesitantWriter's portrait-aware scale patch is what makes serif type read at 9:16 without collapse.
