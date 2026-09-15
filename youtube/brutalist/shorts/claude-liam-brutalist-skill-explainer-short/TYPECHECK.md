# TYPECHECK — The explainer Skill · Short (9:16)

Run id: `c6d1a9178c344f429dac903948551b82`.

The historically-referenced `scripts/type_check.py` is NOT SHIPPED in the
snapshot at this run_id (documented in the parent's TYPECHECK); the Short
inherits that absence. This report records the current type-adjacent checks
that DID run against the Short.

## Runtime checks that ran on this Short

- `build_safety.validate_project` — ran twice (before shorts.py wrote the
  Short's beat_sheet.json; before compile.py loaded it). No schema errors.
- `build_safety.require_short_duration` — ran during shorts.py cap-check
  (planned 116.92 s < 180.0 s) and again during compile.py (measured
  116.917 s < 180.0 s). ✓
- `build_safety.positive_duration` — ran per beat in shorts.py's `beat_dur`
  helper. All six retained beats have positive `render_duration_s` and
  `actual_duration_s`. ✓
- `math_layout_check.math_layout_errors` — ran inside `validate_project`.
  No FormACard/WantQuote pattern used in this Short; zero math-layout errors. ✓
- ffprobe stream schema — verified h264/2160×3840/24fps + aac tracks.

## Remotion prop schema (retained beats)

No Remotion component was re-rendered for this Short. All retained beat mp4s
are native portrait copies from the updated parent vertical, which passed the
parent's TYPECHECK against Root.tsx's zod schema for `ClaudeComposerAsk916`,
`BrutalistHesitantWriter916`, `SkillTeardownPipeline916`,
`SkillTeardownMechanism916`, `ClaudeVerdictArtifact916`, `ClaudeTitleOutro916`.
Prop schema for the Short's beat_sheet was preserved untouched by shorts.py.
B07's updated props (`verdictPositive: true`, `verdictLabel: "execute it — render it"`,
`cite: "explainer SKILL.md · VOX LAW + EXECUTABLE-EVIDENCE.md"`) were verified
against the SkillTeardownMechanism916 zod schema in Root.tsx by the parent build.

## Not applicable to this run

- No new Python module was authored; nothing to `mypy`.
- No new TypeScript React component was authored; nothing to `tsc`.
- No new prompt file was authored; nothing for the prompt-lint step.
- No new SKILL.md was edited; nothing for skill-frontmatter check.

## Absent legacy checks (honestly recorded)

- `runtime/scripts/type_check.py` — absent in this snapshot. Same status as
  the parent. Not fabricated as passing.
- `reference/type-spec.md` — absent in this snapshot. Not fabricated.
