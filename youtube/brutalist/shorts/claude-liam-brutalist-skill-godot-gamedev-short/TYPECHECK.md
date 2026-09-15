# TYPECHECK.md — The godot-gamedev Skill — Short
# Run ID: 91d8e873ca5e413e8379a0c0c9179ed4 · 2026-09-12

## Beat sheet validation

Validated by `shorts.py → validate_project()` and `compile.py → validate_project()`.

| Field | Value | Status |
|-------|-------|--------|
| metadata.kind | short | OK |
| metadata.aspect_ratio | 9:16 | OK |
| metadata.voice | am_onyx | OK |
| metadata.voice_kokoro | am_onyx | OK |
| metadata.captions | false | OK |
| metadata.playlist | Brutalist | OK |
| metadata.channel | @HumanitariansAI | OK |
| metadata.in_for_bear | true | OK |
| short_validation.status | ready | OK |
| short_validation.errors | [] | OK |

## Beat types

All 9 kept beats have `shot.type: GRAPHIC` and `shot.source: remotion`. All are pre-rendered as native 9:16 portrait clips; no Remotion re-render required for this cut.

## Audio files

All 9 narrated beats have independent copies in `mp3/` (copied by shorts.py, not symlinked). B12 has `audio_policy: silence` — no mp3 file required.

## Duration check

`require_short_duration` called by shorts.py on planned total 159.6s → OK (strictly < 180.0s).
Final container/video/audio duration 159.625s → PASS.

## No type errors.
