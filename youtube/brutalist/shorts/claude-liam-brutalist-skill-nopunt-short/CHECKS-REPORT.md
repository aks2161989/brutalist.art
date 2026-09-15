# CHECKS-REPORT.md — The nopunt Skill (Short)

Run ID: `3f692902b8e54a40ae696576b15481e1`  ·  aspect: 9:16 Short  ·  cap: strictly < 180.000 s

## 1. Derivation (`runtime/scripts/shorts.py`)

Command:
```
python3 runtime/scripts/shorts.py \
  youtube/brutalist/claude-liam-brutalist-skill-nopunt/vertical \
  --output-dir youtube/brutalist/shorts/claude-liam-brutalist-skill-nopunt-short \
  --slug claude-liam-brutalist-skill-nopunt-short \
  --drop B02 B03 B08 B09 B10 --no-endcard --no-outro-rewrite
```
Result: `7 beats · ~168.2s (2:48.2) OK` — all seven kept beats picked up as
`native portrait reused unchanged`. No pantry overrides needed. No 916 re-render
required (Root.tsx already provides the 916 compositions for every kept beat).

`short_validation` in derivative sheet: `{"status": "ready", "errors": []}`.

## 2. Compile (`runtime/scripts/compile.py`)

Command:
```
python3 runtime/scripts/compile.py \
  youtube/brutalist/shorts/claude-liam-brutalist-skill-nopunt-short \
  --height 3840 \
  --out youtube/brutalist/shorts/claude-liam-brutalist-skill-nopunt-short/exports/short
```
Result: 7/7 slots filled. Motion histogram: `reveal:4  type-on:2  hold:1`.
`--review` was NOT used (final pass). Compiler wrote 168.2 s output.

Skin lint warnings (informational only, inherited from parent — expected for
the 916 outro / cold-open compositions used in the portrait cut):
- `B00: palette=claude but the cold open is 'ClaudeComposerAsk916' — COLD OPEN LAW wants ClaudeComposerAsk`
- `B11: palette=claude but the outro is 'ClaudeTitleOutro916' — OUTRO LAW wants ClaudeTitleOutro`

These are the correct portrait compositions per shorts.py's ONDA CHECK rewiring; the lint text describes the landscape-canonical name.

## 3. Duration (strictly under 180.000 s)

Measured via `ffprobe -show_entries format=duration:stream=duration`:

| Stream | Duration (s) | Pass |
|--------|-------------|------|
| Container | 168.208 | ✓ (< 180.000) |
| Video (h264 2160×3840) | 168.167 | ✓ (< 180.000) |
| Audio (aac) | 168.208 | ✓ (< 180.000) |

Full-decode confirmation (`ffmpeg -vn -f null -`):
`Duration: 00:02:48.21, start: 0.000000, bitrate: 675 kb/s` — decodes end to end without error, no truncation, no framing warnings.

`volumedetect` on the audio track: mean_volume `-27.2 dB`, max_volume `-4.7 dB` (no clipping, present throughout).

Planned duration from `CUT-PLAN.json`: 168.21 s. Measured matches plan within one frame.

## 4. Dimensions

`ffprobe stream=width,height`: `2160×3840` — matches the required Shorts
dimensions `[2160, 3840]` in the invocation payload. No cropping was
performed (source was already 9:16). Files probed:
- Container/video stream — 2160×3840.
- All seven per-beat mp4s copied into `media/` — 2160×3840 (verified by `shorts.py` `native portrait reused unchanged` for each).

## 5. Audio / narration integrity

- All seven per-beat mp3s copied independently from `parent_reel/vertical/mp3/`.
- Voice engine: Kokoro `am_onyx` (per parent metadata; unchanged this session; no API calls).
- No mp3 was regenerated (no outro rewrite; `--no-outro-rewrite`).
- Full audio decode with `-vn -f null -` completes with no error and matches container length.

## 6. Frame evidence

- `_qc/frames-2fps/` — 336 frames extracted at 2 fps across the whole 168.2 s Short (546 × 960 preview scale, JPG).
- `_qc/frames-beat/` — 21 frames at beat-relative 15% / 50% / 85% for each of the 7 kept beats. Hashes recorded in `_qc/frame-hashes.json`.
- `_qc/joins/` — boundary probes (both fast-seek and accurate-seek) at each of the 6 join points; confirms the B07 → B11 transition is a fade-in from the outro composition (single black frame is intrinsic to the parent B11 render, verified against `parent_reel/vertical/media/B11.mp4` first-frame).

## 7. Narrative coherence review

The retained numbered sequence (First / Second / Third / Fourth design
decisions) is contiguous — no dropped beat leaves a dangling number. B05→B06
"catalog above" reference stays coherent because both retained. B07 closes on
the definitive "anything else is a PUNT" line, which the outro cleanly
follows. Cold-open composer bullets (three preview lines) match what the Short
subsequently delivers — HOLD-only-for-photos and unfilled=PUNT are both
covered in kept beats; the anti-punt-catalog frame is the entire subject of
the Short. No dangling reference to dropped material.

## 8. Not run / limitations

- No human review yet. Bear's viewing is next; `FEEDBACK.md` is empty and awaits notes.
- No publish / upload / git push. No YouTube handoff. No related-video selection.
- No captions / subtitle track (Brutalist Shorts render without burned-in captions).
- Nothing was written outside the isolated toolkit + this reel directory.
