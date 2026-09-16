# TYPECHECK — Brutalist Utility: align.py — Short

No TypeScript or Remotion source was modified for this Short. Every retained
beat is a portrait render already produced and validated by the parent reel's
build; `shorts.py` reused the native 2160×3840 mp4s unchanged (no zod-schema
prop change, no re-render, no tsc pass required).

## What was and wasn't invoked

| Tool | Invoked? | Reason |
|------|----------|--------|
| `runtime/scripts/shorts.py` | YES | derived the whole-beat cut into `youtube/brutalist/shorts/claude-liam-brutalist-runtime-align-short/` — reported all 6 kept beats as "native portrait reused unchanged" |
| `runtime/scripts/compile.py` | YES | assembled per-beat clips into the final 90.25s master; `--height 3840`, no `--review` |
| `runtime/scripts/remotion_scenes.py` | NO | not needed — no `ONDA CHECK` rewire (parent renders re-used verbatim) |
| `runtime/remotion/ tsc / eslint` | NO | no TSX changed; the parent's portrait compositions were built and typechecked at the parent's build time |
| `build_safety.require_short_duration(90.25)` | YES (manual sanity) | returned OK |

## Beat-sheet schema validation

`shorts.py` calls `validate_project(derivative)` before writing the new
`beat_sheet.json`. That call passed (script would have raised `BuildError`
otherwise), which confirms the schema contract for the retained beats. Final
metadata (as required by the brief):

```
kind:           short
aspect_ratio:   9:16
playlist:       Brutalist
voice:          am_onyx
voice_kokoro:   am_onyx
captions:       false
derived_from:   claude-liam-brutalist-runtime-align-vertical
dropped_beats:  [B03, B04, B05, B06, B08, B10]
short_validation.status: ready
total_estimated_duration_seconds: 90.25
```

## Retained Remotion patterns (portrait 916)

| Beat | pattern | schema owner |
|------|---------|--------------|
| B00 | `ClaudeComposerAsk916` | runtime/remotion/src/Root.tsx |
| B01 | `BrutalistHesitantWriter916` | runtime/remotion/src/Root.tsx |
| B02 | `SkillTeardownMechanism916` | runtime/remotion/src/Root.tsx |
| B07 | `ClaudeCodeBeat916` | runtime/remotion/src/Root.tsx |
| B09 | `ClaudeVerdictArtifact916` | runtime/remotion/src/Root.tsx |
| B11 | `ClaudeTitleOutro916` | runtime/remotion/src/Root.tsx |

Props for each retained beat are the parent's approved props (see
`beat_sheet.json → beats[].shot.remotion.props`). None were mutated by
`shorts.py` because no re-render was triggered.

## Verdict

Nothing to type-check on this workspace. Short is a media derivative; no source
code changed.
