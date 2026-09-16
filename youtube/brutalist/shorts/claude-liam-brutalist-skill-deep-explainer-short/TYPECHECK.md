# TYPECHECK.md — The deep-explainer Skill — Short

No new TypeScript/Remotion code was authored for this Short. Every
retained beat reuses its parent's native portrait render as an
independent file copy; no `<Pattern>916` composition was added, removed,
or edited in the isolated toolkit's `runtime/remotion/src/Root.tsx`.

## Files touched in the isolated toolkit

- (none — see `git status` in the toolkit workspace)

## Compositions referenced by the retained beats

All exist in the parent's Root.tsx and rendered clean in the parent long.

- `ClaudeComposerAsk916` — B00
- `BrutalistHesitantWriter916` — B01
- `SkillTeardownMechanism916` — B03, B06, B07, B10, B11
- `ClaudeVerdictArtifact916` — B14
- `ClaudeTitleOutro916` — B16

## Beat-sheet validation

- `build_safety.validate_project` passed at `shorts.py` write time
- `build_safety.validate_project` passed again at `compile.py` read time
- `require_short_duration(119.79, "Planned Short")` passed
- 9/9 beats stamped with `build.status: VIDEO` and a valid `src`

## Python scripts invoked

- `runtime/scripts/shorts.py` — exit 0
- `runtime/scripts/compile.py` — exit 0 (no `--review`; native 3840
  target; explicit `--out` per BUILD-PROMPT §"Reuse native footage")

## Runtime environment

- ffmpeg / ffprobe on PATH (sandbox-permitted)
- No Node/Remotion invocation (all portrait renders inherited from parent)
- No paid API, no upload, no publish
