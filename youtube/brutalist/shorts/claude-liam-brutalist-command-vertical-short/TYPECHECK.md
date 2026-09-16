# TYPECHECK — Brutalist Command: art vertical — Short

## Beat sheet schema

- `metadata.kind` = `short` ✓
- `metadata.aspect_ratio` = `9:16` ✓
- `metadata.captions` = `false` ✓
- `metadata.voice` = `am_onyx`, `voice_kokoro` = `am_onyx` ✓
- `metadata.engine` = `kokoro` ✓
- `metadata.playlist` = `Brutalist` ✓
- `metadata.dropped_beats` = `["B03","B05","B06","B08","B10"]` ✓
- `metadata.short_validation.status` = `ready`, `errors` = `[]` ✓
- `metadata.total_estimated_duration_seconds` = 128.92 ✓ (matches 7 × `render_duration_s` sum)

## Remotion patterns (portrait-only)

Every retained REMOTION beat's `shot.remotion.pattern` ends in `916`:

| Beat | Pattern |
|---|---|
| B00 | `ClaudeComposerAsk916` |
| B01 | `BrutalistHesitantWriter916` |
| B02 | `ClaudeCodeBeat916` |
| B04 | `ClaudeCodeBeat916` |
| B07 | `ClaudeCodeBeat916` |
| B09 | `ClaudeVerdictArtifact916` |
| B11 | `ClaudeTitleOutro916` |

All seven were pre-rendered by the parent vertical build and reused here by
shorts.py via the native-portrait copy path.  B00/B01/B03–B11 at
2026-09-09T18:55–19:02; B02 re-rendered 2026-09-12T17:49:33 (art:102-107
dispatcher line-number correction in the parent).  No `shot.remotion.props`
were mutated in the Short, so no zod schema breakage is possible.

## Media / audio files

All 7 kept beats resolve:

- `media/B00.mp4` … `media/B11.mp4` — independent copies (shutil.copy) of parent
- `mp3/beat-B00.mp3` … `mp3/beat-B11.mp3` — independent copies of parent

No stray files for dropped beats (`B03`, `B05`, `B06`, `B08`, `B10`).

## Compile / ffprobe

- `runtime/scripts/compile.py` reports 7/7 slots filled, all VIDEO source.
- ffprobe container/video/audio durations agree to within 1 ms, all
  strictly below 180.000 s.
- No drawtext filter in the pipeline; all overlays are PIL.

## Result

**PASS.**  Schema is coherent, patterns are portrait, no dropped-beat
references remain in metadata or media, and durations are inside the cap.
