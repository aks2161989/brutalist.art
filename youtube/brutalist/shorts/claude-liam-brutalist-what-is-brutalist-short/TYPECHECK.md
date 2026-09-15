# TYPECHECK.md — What Is Brutalist? — Short

*Type/schema and structural checks executed for this 9:16 Short derivation.
Nothing was regenerated for this Short; native portrait renders and audio are
reused verbatim from the parent's `vertical/` companion, so most of the
per-scene zod checks that would apply to a re-render did not run here — the
compiler consumed the existing `.mp4` files unchanged.*

## Sheet-level

| Check | Method | Result |
|---|---|---|
| `metadata.aspect_ratio` == `9:16` | `beat_sheet.json` inspection | ✔ `9:16` |
| `metadata.kind` == `short` | `beat_sheet.json` inspection | ✔ `short` |
| `metadata.slug` | `beat_sheet.json` inspection | ✔ `claude-liam-brutalist-what-is-brutalist-short` |
| `metadata.playlist` | `beat_sheet.json` inspection | ✔ `Brutalist` |
| `metadata.voice` / `metadata.voice_kokoro` | `beat_sheet.json` inspection | ✔ `am_onyx` / `am_onyx` |
| `metadata.captions` | `beat_sheet.json` inspection | ✔ `false` |
| `metadata.dropped_beats` = ["B02","B03","B05","B08"] | shorts.py stamped | ✔ matches CUT-PLAN.json |
| `metadata.short_validation.status` | shorts.py stamped | ✔ `ready` (no ONDA / duration blockers) |
| `metadata.total_estimated_duration_seconds` | shorts.py stamped | ✔ 94.79 s (matches measured) |
| `validate_project(sheet)` | `build_safety.validate_project` invoked by shorts.py | ✔ pass |
| `require_short_duration(total, "Planned Short")` | `build_safety.require_short_duration` invoked by shorts.py | ✔ pass (94.79 s < 180.0 s) |

## Kept-beat inventory

| Beat | Pattern (portrait) | Registered in Root.tsx? | Portrait render present in `media/` | Audio present in `mp3/` |
|---|---|---|---|---|
| B00 | `ClaudeComposerAsk916` | ✔ | ✔ `media/B00.mp4` | ✔ `mp3/beat-B00.mp3` |
| B01 | `BrutalistHesitantWriter916` | ✔ | ✔ `media/B01.mp4` | ✔ `mp3/beat-B01.mp3` |
| B04 | `WibChange916` | ✔ | ✔ `media/B04.mp4` | ✔ `mp3/beat-B04.mp3` |
| B06 | `WibNotClaims916` | ✔ | ✔ `media/B06.mp4` | ✔ `mp3/beat-B06.mp3` |
| B07 | `WibVerdict916` | ✔ | ✔ `media/B07.mp4` | ✔ `mp3/beat-B07.mp3` |
| B09 | `WibOutro916` | ✔ | ✔ `media/B09.mp4` | ✔ `mp3/beat-B09.mp3` |

Renders were copied independently by `shorts.py` (native 9:16 branch — line
338-353 of `runtime/scripts/shorts.py`), verified against `ffprobe`
2160×3840. No `remotion_scenes.py` invocation was needed for this Short.

## Compiler results (`runtime/scripts/compile.py --height 3840`)

- `[art] compiled B00 VIDEO 16.8s ← B00.mp4`
- `[art] compiled B01 VIDEO 20.0s ← B01.mp4`
- `[art] compiled B04 VIDEO 18.1s ← B04.mp4`
- `[art] compiled B06 VIDEO 20.5s ← B06.mp4`
- `[art] compiled B07 VIDEO 14.5s ← B07.mp4`
- `[art] compiled B09 VIDEO 4.9s ← B09.mp4`
- `[art] motion histogram: type-on:1  type-then-correct:1  edit-and-rerender:1  rows-arrive:1  artifact-lines:1  restate:1`
- `[art] build stamp → beat_sheet.json (6/6 filled)`
- `[art] slots: 6/6 filled — B00:VIDEO B01:VIDEO B04:VIDEO B06:VIDEO B07:VIDEO B09:VIDEO`

## Skin lint (inherited from the parent's vertical)

`[art] SKIN LINT: B00: palette=claude but the cold open is
'ClaudeComposerAsk916' — COLD OPEN LAW wants ClaudeComposerAsk`

`[art] SKIN LINT: B09: palette=claude but the outro is 'WibOutro916' — OUTRO
LAW wants ClaudeTitleOutro`

Both are **expected and documented**: the parent explicitly substitutes
`WibOutro916` for `ClaudeTitleOutro` because `OUTRO-LOCK.md` hardcodes
`@NikBearBrown` in the shipped outro and this reel is on the HAI channel; and
`ClaudeComposerAsk916` is the portrait sibling of `ClaudeComposerAsk` that
the skin lint has not yet been updated to accept. Neither is a Short-specific
regression.

## What did NOT need to run

- `runtime/scripts/generate_audio_kokoro.py` — no audio regeneration
  (`--no-outro-rewrite`; all six kept beats' mp3s copied unchanged).
- `runtime/scripts/remotion_scenes.py` — no portrait re-render (native
  portrait renders exist for every kept beat; ONDA check reported nothing
  rewired and nothing blocked).
- `--recut` on `shorts.py` — no center-cut fallback; the parent is already
  native portrait.

## Final container

`exports/short/claude-liam-brutalist-what-is-brutalist-short.mp4`

| Stream | Codec | Dimensions / rate | Duration |
|---|---|---|---|
| video | h264 | 2160×3840 | 94.791667 s |
| audio | aac | 48000 Hz, 2 ch | 94.791000 s |
| container | mp4 | — | 94.791667 s |

Container, video and audio durations are **each strictly < 180.0 s** and
match the shorts.py planned duration to sub-second precision.
