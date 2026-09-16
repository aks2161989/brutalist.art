# CHECKS-REPORT — portrait 9:16

Every check run against the final portrait master
(`exports/vertical/claude-liam-brutalist-skill-guests-vertical.mp4`,
SHA-256 `3d99d32a70dfc8189eeae5f0e673a9a25e6f203118553ee41d4c115598868880`).
Portrait review is independent of the landscape review.

## GATE F — required paperwork

- `FACTCHECK.md` — present ✅
- `SHOTLIST.md` — present ✅
- `PROMPTS.md` — present ✅
- Also present: `SOURCES.md`, `TYPECHECK.md`, `BUILD-PROMPT.md` (bundled by
  supervisor).

## Beat sheet + audio integrity

- Audio was NOT regenerated for portrait — the narration is identical to
  landscape, so the same 12 mp3s are used (copied into `vertical/mp3/`).
- Sheet updated: aspect_ratio → `9:16`, slug → `claude-liam-brutalist-skill-guests-vertical`,
  every applicable pattern name suffixed with `916`, and B01 authored with a
  portrait-native layout (5-line split, fontSize 130, lineSpacing 2.4).
- `metadata.channel_title` deliberately omitted (memory
  `feedback_channel_title_portrait_bleed`).

## Render — every beat filled by a REGISTERED `*916` composition

- 12/12 beats rendered to `media/B##.mp4` at 1080×3840 upscaled per `scale=2`
  for a true 2160×3840 supersample; no slates; every pattern resolved.
- Render infrastructure: same chrome-headless-shell wrapper + `ART_CHROME`
  path used by landscape.

## Compile — beat pack + atomic verification

`runtime/scripts/compile.py <REEL>/vertical --height 3840 --out <REEL>/exports/vertical`

- Encoded to a candidate, verified, atomically replaced. `.verified.json`
  written next to the final mp4 with real ffprobe measurements.
- Duration 292.9 s, aac audio present, per-beat timeline preserved.
- Motion histogram same as landscape (structural).
- Compiler skin-lint warnings:
  - `B00: palette=claude but the cold open is 'ClaudeComposerAsk916' — COLD OPEN LAW wants ClaudeComposerAsk`
  - `B11: palette=claude but the outro is 'ClaudeTitleOutro916' — OUTRO LAW wants ClaudeTitleOutro`
  Same warnings the sibling `fellows` portrait companion emitted — expected
  portrait-native trade-off (the `*916` variants render native 9:16 layouts
  from shared source; the lint rule matches aspect-blind landscape names).
  NOT defects.

## Gate V — visual QC

- Frames sampled: 24 (steady state at each beat's 50 %/85 %).
- **BLOCKER: 0 · MAJOR: 0** — clean pass.
- One iteration on B01 portrait: initial (fontSize 118 / lineSpacing 2.2, 4-line
  wrap) gave 53 % coverage; bumped to fontSize 130 / lineSpacing 2.4 → 55 %+
  coverage. Root cause fixed in the sheet, not the checker.

## Hero-frame inspection

Extracted at B01, B03, B09, B10, B11 midpoints and read directly:

- B01 portrait shows the 5-line correction landed at readable serif size.
- B03 pipeline reflows to a vertical INPUT ↓ COLD OPEN ↓ SUMMARY ↓ THE VIDEO
  (terracotta) ↓ RECAP ↓ YOUR TURN + HAI OUTRO ↓ OUTPUT column, footer note
  visible.
- B09 verdict card visible (contact sheet confirms all six lines).
- B10 Your Turn composer stacks with the paste-ready prompt and the 3-check
  rubric legible in the mono block.
- B11 outro carries `The guests Skill.` and hardcoded `@NikBearBrown` on the
  dark ground, framed with the double-rule bars (portrait outro chrome).

## Content-integrity checks

Same as landscape (`../CHECKS-REPORT.md`) — no captions, no unresolved
slates, no paid demo, no impersonation of any real board member or the
Professor. Portrait companion is NOT a center-crop of the landscape master;
it is authored natively.
