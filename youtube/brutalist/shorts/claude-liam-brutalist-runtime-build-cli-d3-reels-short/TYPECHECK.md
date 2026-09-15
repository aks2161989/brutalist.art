# TYPECHECK — Brutalist Utility: build_cli_d3_reels.py — Short

No new TypeScript or Python code was authored for this Short. The cut reuses
the parent's native portrait Remotion renders and Kokoro `am_onyx` audio
unchanged. Two Python scripts were invoked from the toolkit; both are
distribution-controlled and exit `0`:

| Tool | Command | Result | Notes |
|---|---|---|---|
| `runtime/scripts/shorts.py` | `<parent>/vertical --output-dir <reel> --slug ...-short --drop B03 B04 B05 B06 B08 B10 --no-endcard --no-outro-rewrite` | exit 0 · `6 beats · ~97.0s (1:37.0) OK` | Every kept beat resolved via `native portrait reused unchanged`. |
| `runtime/scripts/compile.py` | `<reel> --height 3840 --out <reel>/exports/short` | exit 0 · `6/6 filled` · `97.0s` | Wrote 2160×3840 h264/aac MP4. |

## Beat-sheet schema validation

- `validate_project()` (from `build_safety`) passes inside `shorts.py`.
- `require_short_duration()` (`build_safety.SHORTS_CAP_S`) — planned 96.96s under cap; recorded in `metadata.short_validation` as `{status: ready, errors: []}`.
- Every retained beat carries `remotion.pattern` matching a `<Composition id="...">` in `runtime/remotion/src/Root.tsx` (all `*916` variants):
  - `ClaudeComposerAsk916` (B00, B11 wraps via `ClaudeTitleOutro916`)
  - `BrutalistHesitantWriter916` (B01)
  - `SkillTeardownMechanism916` (B02)
  - `ClaudeCodeBeat916` (B07)
  - `ClaudeVerdictArtifact916` (B09)
  - `ClaudeTitleOutro916` (B11)

## No unauthorized dependencies

- No `npm install`, no `pip install`, no `higgsfield` call.
- No network requests from any script invocation (compile + shorts are pure local file I/O + ffmpeg).
- Local Kokoro synthesis was NOT invoked (audio copied unchanged from parent).
- Remotion renderer was NOT invoked (all `*916` renders inherited from parent).

## Static safety checks

- `atomic_json()` used for beat_sheet.json writes.
- `copy_asset()` used for every media/mp3 copy (no symlinks; independent copies).
- `writable_path()` enforced write scope — everything landed inside `<reel>` or `<reel>/exports/`.
- No writes outside the reel dir; no writes into `.repoloop/shorts/workspaces/*/toolkit` (isolated toolkit is read-only from the reel's perspective).

## Pass

All checks green. No blockers, no majors.
