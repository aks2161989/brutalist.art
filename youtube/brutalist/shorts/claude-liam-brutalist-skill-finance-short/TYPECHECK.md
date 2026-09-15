# TYPECHECK — The finance Skill — Short

## Beat-sheet schema

`shorts.py` invoked `validate_project(sheet)` and `validate_project(derivative)`
without raising. `beat_sheet.json` validates against the project schema and
carries the required metadata for a Short: `kind: short`, `aspect_ratio: 9:16`,
`voice: am_onyx`, `voice_kokoro: am_onyx`, `captions: false`,
`playlist: Brutalist`, `derived_from: claude-liam-brutalist-skill-finance-vertical`,
`dropped_beats: ["B02","B03","B07","B08","B10"]`,
`short_validation: {status: ready, errors: []}`.

## Remotion prop schemas

No Remotion re-renders were required for this Short — every retained
beat reused the parent's native portrait MP4 unchanged
(`shorts.py` logged `native portrait reused unchanged` for B00, B01, B04,
B05, B06, B09, B11). Because the frames themselves come straight from the
parent 9:16 master, the parent's zod-verified prop schemas remain intact;
no new prop payload was introduced by this Short.

## Compile-time typechecks

`compile.py` was invoked with `--height 3840 --out …/exports/short/` and
completed without raising. It reported:

- 7/7 slots filled, all VIDEO
- motion histogram reveal:4 type-on:2 hold:1
- SKIN LINT: two informational entries (B00 ClaudeComposerAsk916, B11
  ClaudeTitleOutro916) — see CHECKS-REPORT.md
- Emitted `claude-liam-brutalist-skill-finance-short.mp4` at 169.9s

## No Python type errors

No script raised. `build_safety.require_short_duration(169.86, 'Planned Short')`
returned cleanly; `positive_duration` on each beat returned floats > 0.
