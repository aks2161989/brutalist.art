# TYPECHECK — Brutalist Command: art approvals — Short (9:16)

## Python scripts touched on the Short path

Each parsed with `ast.parse` from the isolated toolkit at `.repoloop/shorts/workspaces/claude-liam-brutalist-command-approvals-short/toolkit/`.

- `runtime/scripts/build_safety.py` — AST-parses OK. Source of `is_source_report`, `validate_project`, `atomic_json`, `copy_asset`, `writable_path`, `positive_duration`, `SHORTS_CAP_S`, `require_short_duration`. Also the module the Short's teardown quotes (`approval_subjects`, `validate_approvals`, `digest`).
- `runtime/scripts/shorts.py` — AST-parses OK. Ran successfully with the manual `--drop B02 B04 B07 B10 --no-endcard --no-outro-rewrite` plan.
- `runtime/scripts/compile.py` — AST-parses OK. Compiled `exports/short/claude-liam-brutalist-command-approvals-short.mp4` with `--height 3840` (per BUILD-PROMPT); the compiler stamped `8/8 slots filled` and wrote the encoded MP4 in one pass. Rebuild run_id `9183b88ae09845c39f780928e0b7b10a` recompiled B06 and B09 from updated parent vertical media.

## Beat sheet schema

- `beat_sheet.json` parses as valid JSON.
- 8 beats: `['B00', 'B01', 'B03', 'B05', 'B06', 'B08', 'B09', 'B11']`.
- `metadata.short_validation.status = "ready"`, `errors = []` (from the shorts.py cap check + the compiler's `validate_project`).
- `metadata.aspect_ratio = "9:16"`, `metadata.kind = "short"`, `metadata.captions = false`, `metadata.voice = "am_onyx"`, `metadata.voice_kokoro = "am_onyx"`, `metadata.playlist = "Brutalist"`.
- `metadata.dropped_beats = ["B02", "B04", "B07", "B10"]`, `metadata.derived_from = "claude-liam-brutalist-command-approvals-vertical"`.
- `metadata.total_estimated_duration_seconds = 126.75` matches the measured file duration exactly.

## Remotion 916 patterns referenced

Every kept beat's `shot.remotion.pattern` already ends in `916` (parent is native portrait). No ONDA-check rewire was required; no re-renders were triggered:

| Beat | Pattern | Root.tsx composition |
|---|---|---|
| B00 | ClaudeComposerAsk916 | registered |
| B01 | BrutalistHesitantWriter916 | registered |
| B03 | ClaudeCodeBeat916 | registered |
| B05 | ClaudeCodeBeat916 | registered |
| B06 | ClaudeCodeBeat916 | registered |
| B08 | ClaudeCodeBeat916 | registered |
| B09 | ClaudeVerdictArtifact916 | registered |
| B11 | ClaudeTitleOutro916 | registered |

Verified by the parent vertical build (`build.filled = 12/12` on the parent) and by `shorts.py` reporting "native portrait reused unchanged" for every kept beat.

## Media / audio invariants

- Every kept beat has an independent copy of its `mp3/beat-<bid>.mp3` and `media/<bid>.mp4` in the short reel folder (no symlinks, no hardlinks — `shutil.copy2` via `copy_asset`).
- Every source `media/<bid>.mp4` probes at 2160x3840 h264 (portrait 4K).
- The compiled export is 2160x3840, h264, 24 fps, aac 48 kHz — matches the compiler contract.

## Limitations

- No TypeScript check was run on `runtime/remotion/src/*.tsx` in this Short build path; the Short reuses the parent's already-rendered portrait MP4s, so the parent build's TS check is the authoritative one for these compositions.
- No third-party linter or formatter is invoked in this workspace; the Short build path only exercises `shorts.py` + `compile.py`.
