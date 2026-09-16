# TYPECHECK — Brutalist Command: art icons — Short

Run ID: `5940cae5467d448eb67578534d454790`

## beat_sheet.json — schema and shape

- Parsed: 7 beats (`B00`, `B01`, `B04`, `B05`, `B08`, `B09`, `B11`) — valid JSON.
- SHA-256: `14f0ebf088afe5b7133e187983f528cc333dbb5c799d254696824daa74ba7b0d`
- `metadata.kind`           = `short`         (per Shorts contract)
- `metadata.aspect_ratio`   = `9:16`
- `metadata.playlist`       = `Brutalist`
- `metadata.voice`          = `am_onyx`
- `metadata.voice_kokoro`   = `am_onyx`
- `metadata.engine`         = `kokoro`
- `metadata.captions`       = `false`
- `metadata.channel`        = `@HumanitariansAI`
- `metadata.persona`        = `Liam (in for Bear)`
- `metadata.in_for_bear`    = `true`
- `metadata.derived_from`   = `claude-liam-brutalist-command-icons-vertical`
- `metadata.dropped_beats`  = `["B02", "B03", "B06", "B07", "B10"]`
- `metadata.total_estimated_duration_seconds` = `107.62`
- `metadata.short_validation.status`          = `ready` (errors: 0)

Every beat carries the required fields (`beat_id`, `act`, `narration_text`,
`voice`, `engine`, `estimated_duration_s`, `render_duration_s`, `audio_file`,
`shot.remotion.pattern` / `shot.type`, `build.status = VIDEO`). `shorts.py`
called `validate_project(derivative)` before writing the sheet.

## Cut-plan JSON

- `CUT-PLAN.json` — valid JSON, matches the delivered cut byte-for-byte:
  `kept_beats = ["B00","B01","B04","B05","B08","B09","B11"]`,
  `dropped_beats` = 5 items with per-beat rationale,
  `strategy = "whole-beat-cut"`, `rewrite_reason = null`,
  `planned_duration_s = 107.63` (matches measured 107.625 within 0.005 s).

## Visual-review JSON

- `VISUAL-REVIEW.json` — valid JSON, conforms to the REPOLOOP-PROMPT schema:
  `status`, `reviewer_type`, `run_id`, `source_sha256`, `beat_sheet_sha256`,
  `video_sha256`, `blockers`, `majors`, `frames[]` (each entry with a real
  SHA-256 that resolves to a file inside this reel's `_qc/`), and `notes`.
- `run_id` matches this invocation (`5940cae5467d448eb67578534d454790`,
  not the parent's `0a10fb54495f4890b9564beef6ac84c5`).
- `source_sha256` matches the invocation payload's `source_sha256`.

## Pipeline sources touched

- Read-only: parent vertical `beat_sheet.json`, parent `media/*.mp4`,
  parent `mp3/beat-*.mp3`, parent `FACTCHECK.md`, `SHOTLIST.md`, `PROMPTS.md`
  (copied into this reel by `shorts.py` as the inherited Gate-F evidence),
  the isolated toolkit under `.repoloop/shorts/workspaces/…/toolkit`.
- Written only under this reel (`youtube/brutalist/shorts/claude-liam-brutalist-command-icons-short/`)
  and its `_qc/` subtree. No writes to the parent, its exports, or the
  public toolkit.

## Renderer and safety flags

- Renderer: `runtime/scripts/compile.py` (guarded compiler, no bypass flags).
  `--review` was NOT used as the final pass; the `--out` argument produced
  the final container.
- No `--vertical` flag: this is a Shorts cut with drops, subject to the
  180.0 s cap check inside `shorts.py` and the final ffprobe check in
  `CHECKS-REPORT.md`.
- No `--rewrite-outro` flag: parent outro narration preserved.
- `--no-endcard`: no silent branded endcard appended; the last beat is
  B11 outro ending at 107.625 s.

## Package versions

- Python `runtime/scripts/shorts.py` @ SHA-256
  `7109a3d0c29c00181a876db80e34238eb9c0c146a97a639a2bbab6d95d28d6e5`
  (matches `SOURCE-SNAPSHOT.json`).
- Python `runtime/scripts/compile.py` @ SHA-256
  `047e9fa6d0944f54c284ed16df8b4d847f62737a0e263a0f4bf0bad2b11f446c`.
- Python `runtime/scripts/build_safety.py` @ SHA-256
  `479e167ffc80c4a2c235b425149b3922fd96a2e7388a40636f2dfa63b56015bf`.

No new Remotion compositions were introduced or edited — every retained
beat resolves to a native portrait pattern that already ships in the parent's
`Root.tsx` (`ClaudeComposerAsk916`, `BrutalistHesitantWriter916`,
`ClaudeCodeBeat916`, `ClaudeVerdictArtifact916`, `ClaudeTitleOutro916`).
