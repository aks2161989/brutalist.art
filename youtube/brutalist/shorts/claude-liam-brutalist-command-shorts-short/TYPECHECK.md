# TYPECHECK — Brutalist Command: art shorts (Short cut)

The legacy static type checker (`runtime/scripts/typecheck.py`) is no
longer part of the current pipeline — Remotion beats are Zod-validated
at render time by `runtime/scripts/remotion_scenes.py` on the parent
build. This document records the actual visual-typography inspection
carried out for the Short cut.

## Method

- Run ID: `c3c149dbdf064d1d99ee95c5f9350955`
- Compiled MP4 (`exports/short/claude-liam-brutalist-command-shorts-short.mp4`,
  2160×3840, 124.67 s, SHA-256 `d18a9cdf…d750`).
- Frames extracted at 15 % / 50 % / 85 % of every retained beat
  (18 frames, `_qc/frames/B{00,01,03,07,09,11}_{15,50,85}.png`).
- 6-beat contact sheet (`_qc/contact_sheet.png`, SHA-256 `ffca9df9…d74`) read
  via the image-capable Read tool. B03_50 and B03_85 frames read individually
  to verify the updated SHORTS LAW code card.

## Findings (portrait, 2160×3840)

| Beat | Pattern | Typography check | Result |
|---|---|---|---|
| B00 | ClaudeComposerAsk916 | Greeting "Salam, Liam" + topic chip + composer body + two output lines all inside SAFE916; monospace body legible at thumbnail. | pass |
| B01 | BrutalistHesitantWriter916 | Serif stanza fills SAFE916 (fontSize 180, lineSpacing 2.6); corrected 4-line "art shorts / drops beats / and rewires / graphics." settled by 85 %. No underfill. | pass |
| B03 | ClaudeCodeBeat916 (updated) | Rebuilt from parent's 2026-09-12 render — expanded 7-line SHORTS LAW: CHECK LENGTH FIRST / SHORTEN BY CUTTING / REUSE RETAINED NARRATION / PUBLISHING IS SEPARATE / --vertical is NOT a Short, each with sub-detail. Spark line "< 3:00 or it never publishes." at bottom. Expected right-truncation on long monospace lines (composition-level layout, not a bleed). Cream background, no border bleed. | pass |
| B07 | ClaudeCodeBeat916 | Title `$ ./art shorts /tmp/claude-501/…`; cap-check, auto-plan, ONDA CHECK block and `~163.5s (2:43.5) OK` line all inside SAFE916; spark line at bottom. | pass |
| B09 | ClaudeVerdictArtifact916 | 8 numbered lines (bare invocation → render only) on artifact card; terracotta numbering; no bleed past SAFE916 bottom. | pass |
| B11 | ClaudeTitleOutro916 | Dark outro card with cream serif "Brutalist Command: art shorts." title and `@NikBearBrown` handle; mascot below handle. OUTRO LAW respected. | pass |

## Zod / schema

B00/B01/B07/B09/B11 are byte-identical media from the prior build
(`build-state.json` per-input SHA-256 unchanged). B03 media was replaced
with the parent's updated render; the parent's Zod-validated ClaudeCodeBeat916
props passed at parent build time. No re-render was triggered by this Short
build — compile.py detected the changed B03 input sha and re-encoded only
that clip's timeline slot.

## Skin warnings inherited from parent

`build.skin_warnings` in `beat_sheet.json` notes that on `palette=claude`
COLD OPEN LAW nominally expects `ClaudeComposerAsk` and OUTRO LAW
nominally expects `ClaudeTitleOutro`. The parent film registered and
shipped the `-916` portrait variants under those pattern names by
design (native portrait rewire, not a crop). Behaviour is identical to
the shipped parent — not a Short defect.

## Caption tracks

None. `captions: false` in metadata; no burned-in subtitles observed in
any frame.

## Result

Pass. No typography blockers. Human viewing/review pending.
