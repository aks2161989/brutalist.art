# TYPECHECK — The logo-motion Skill — Short

Automated structural checks run on the derivative beat sheet + compiled MP4.

## Beat sheet — schema

- `runtime/scripts/shorts.py`'s `validate_project` accepted the derivative
  beat_sheet.json. Metadata carries `kind: short`, `aspect_ratio: 9:16`,
  `voice: am_onyx`, `voice_kokoro: am_onyx`, `captions: false`,
  `playlist: Brutalist`.
- `metadata.derived_from: claude-liam-brutalist-skill-logo-motion-vertical`.
- `metadata.dropped_beats: [B02, B03, B06, B07, B08, B10]`.
- `metadata.short_validation.status: ready` (no blockers reported by the cut
  utility; `require_short_duration` accepts 139.04 s < 180.0 s).

## Beat count and IDs

Kept: `B00, B01, B04, B05, B09, B11`. Six beats total, matching CUT-PLAN.json.
All six IDs are also present in the parent portrait companion beat sheet
(source `beat_sheet.json` at parent).

## Per-beat status after compile

| Beat | Scene | Source frame | Status |
|---|---|---|---|
| B00 | `ClaudeComposerAsk916` | `media/B00.mp4` | VIDEO |
| B01 | `BrutalistHesitantWriter916` | `media/B01.mp4` | VIDEO |
| B04 | `SkillTeardownMechanism916` | `media/B04.mp4` | VIDEO |
| B05 | `SkillTeardownMechanism916` | `media/B05.mp4` | VIDEO |
| B09 | `ClaudeVerdictArtifact916` | `media/B09.mp4` | VIDEO |
| B11 | `ClaudeTitleOutro916` | `media/B11.mp4` | VIDEO |

Compile stamp: `6/6 filled`.

## Container / stream typecheck (ffprobe)

- Container duration: **139.041667 s** (< 180.0 s ✓).
- Video: `h264`, 2160 × 3840, duration 139.041667 s.
- Audio: `aac`, duration 139.041000 s.
- No caption stream, no subtitle stream (spec: `captions: false`).

## Skin lint (compile.py)

- B00: `palette=claude but the cold open is 'ClaudeComposerAsk916' — COLD OPEN
  LAW wants ClaudeComposerAsk`. **Non-blocker.** This is the standard warning
  for every native portrait companion since the `*916` wrappers were added;
  documented in the parent's VISUAL-REVIEW ("non-blocker for native portrait
  wrappers").
- B11: `palette=claude but the outro is 'ClaudeTitleOutro916' — OUTRO LAW
  wants ClaudeTitleOutro`. **Non-blocker.** Same root cause; same disposition.

Both fire on the parent portrait companion and were accepted there. Nothing
about this Short's cut changes their status.

## No forbidden bypasses

- Compiler was not invoked with `--review` (final pass, per REPOLOOP-SHORTS
  requirement).
- No `--no-verify`, no signing bypass, no `--force` flag.
- No `pantry/` override, no hand-cut center crop; every media reference is a
  copy of an existing native portrait render.
