# TYPECHECK — The screen-clean Skill — Short

Scope: schema and metadata contracts for this derivative Short. No source
code changes were made in this invocation; only reel authoring.

## beat_sheet.json

- `runtime/scripts/build_safety.py :: validate_project` invoked twice by
  `shorts.py`: once on the parent sheet, once on the derived sheet after the
  cut. Both passed (no `BuildError`).
- Derived `metadata.kind`: `short`
- Derived `metadata.aspect_ratio`: `9:16`
- Derived `metadata.playlist`: `Brutalist`
- Derived `metadata.voice`: `am_onyx` · `voice_kokoro`: `am_onyx`
- Derived `metadata.captions`: `false`
- Derived `metadata.derived_from`:
  `claude-liam-brutalist-skill-screen-clean-vertical`
- Derived `metadata.dropped_beats`: `["B02","B04","B05","B06","B08","B10"]`
- Derived `metadata.total_estimated_duration_seconds`: 128.12
- `short_validation.status`: `ready`; `errors`: `[]`
- Six retained beats each carry a `build` record with
  `status: VIDEO`, `filled_by: remotion:<pattern>916`, and a `src`
  reference under `media/`.

## Remotion props (portrait 916 schemas)

Reused unchanged from the parent's already-rendered 2160×3840 videos. No
Remotion re-render was executed in this invocation, so no zod schema drift
is possible in this cut. Compositions used:

- `ClaudeComposerAsk916` (B00, B11 uses `ClaudeTitleOutro916`)
- `BrutalistHesitantWriter916` (B01)
- `SkillTeardownPipeline916` (B03)
- `SkillTeardownMechanism916` (B07)
- `ClaudeVerdictArtifact916` (B09)

## Runtime scripts touched

- `runtime/scripts/shorts.py` executed with `--drop B02 B04 B05 B06 B08 B10
  --no-endcard --no-outro-rewrite`. Exit 0.
- `runtime/scripts/compile.py` executed with `--height 3840 --out
  <reel>/exports/short`. Exit 0.
- No `--review` flag used on the final compile. No alternate renderer,
  bypass flag, or credential path invoked.

## File contracts

- `writable_path` / `copy_asset` used for every media, mp3 and json write —
  no writes escaped the reel root.
- `atomic_json` used for `beat_sheet.json`.
- No symlinks or hardlinks created in the reel; every media/mp3 file is an
  independent copy of the parent asset.

## Sandbox and safety

- Sandbox filesystem allow-list respected (writes limited to workspace
  toolkit and reel; parent + long exports remained read-only).
- No network calls issued. No paid generation. No publish / upload / push.
