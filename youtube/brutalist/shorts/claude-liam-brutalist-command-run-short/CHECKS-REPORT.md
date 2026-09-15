# CHECKS-REPORT — Brutalist Command: art run (Short cut)

Run ID: `d84ca314edcf4438a94f55f21c742c99`
Date: 2026-09-12
Output: `exports/short/claude-liam-brutalist-command-run-short.mp4`
SHA-256: `48780fddbe29f5153927bf726f3f9a4dfa6e009d963ac4a109af5d313cba6e47`

## 1. Cut plan (whole-beat)

- Strategy: `whole-beat-cut`, no rewrite (`CUT-PLAN.json`).
- Kept: B00, B01, B03, B07, B10, B11 (6 beats).
- Dropped: B02, B04, B05, B06, B08, B09 (6 beats).
- Cut mechanism: `python3 runtime/scripts/shorts.py … --drop … --no-endcard --no-outro-rewrite`.
- shorts.py output: every retained beat printed `native portrait reused unchanged`.
- Planned duration: 118.6 s. Cap: 180 s (strict).

## 2. Compile

Command:
```
python3 runtime/scripts/compile.py <reel> --height 3840 --out <reel>/exports/short
```
Result (excerpt):
```
[art] compiled B00  VIDEO    17.5s  ← B00.mp4
[art] compiled B01  VIDEO    17.2s  ← B01.mp4
[art] compiled B03  VIDEO    33.2s  ← B03.mp4
[art] compiled B07  VIDEO    23.1s  ← B07.mp4
[art] compiled B10  VIDEO    22.3s  ← B10.mp4
[art] compiled B11  VIDEO     5.2s  ← B11.mp4
[art] motion histogram: type-on:2  code-cascade:2  hesitant-type:1  outro-card:1
[art] slots: 6/6 filled
```
Skin-lint warnings (inherited from the vertical parent's portrait-pattern
naming; NOT a Short defect): the compiler notes that `ClaudeComposerAsk916`
and `ClaudeTitleOutro916` register under the `-916` names on the palette=claude
skin. Behavior is identical to the parent film that shipped.

## 3. Duration check (strict Shorts law)

`ffprobe -show_entries format=duration:stream=index,codec_type,codec_name,width,height,duration`:

| Stream | Value |
|---|---|
| Container (`format.duration`) | **118.583 s** ✓ < 180.0 |
| Video (h264, 2160×3840) | **118.541667 s** ✓ < 180.0 |
| Audio (aac) | **118.583 s** ✓ < 180.0 |

All three durations are strictly under 180.0 s with ≥ 61 s of encoding
headroom.

## 4. Dimensions

Video stream: 2160 × 3840 (native portrait). No crop path, no re-render.
No captions, no burned-in subtitles. Palette = claude cream (#FAF9F5).

## 5. Audio decode

`ffmpeg -i <mp4> -vn -c:a pcm_s16le _qc/audio.wav` completed without
errors; wav duration = 118.59 s, 48 kHz stereo.

`volumedetect`:
- `mean_volume: -27.1 dB`
- `max_volume: -4.2 dB` (no clipping)

`silencedetect -40dB:0.4s` reported ten short breath gaps (max ~0.7 s),
all at intra- or inter-beat boundaries. No unexpected silences, no
truncated speech, no obvious clicks.

## 6. Frame evidence

- 237 thumbnails at 2 fps (`_qc/frames/f-*.png`).
- 18 beat-relative frames at 15% / 50% / 85% of each of the six retained
  beats (`_qc/beats/B0?-{15,50,85}.png`).
- First frame (`_qc/beats/first-0000.png`) and last frame
  (`_qc/beats/final-last.png`).
- 6-beat contact sheet (`_qc/contact-sheet.png`, SHA-256
  `c806473bdf43471c67a31a45450712ce4e2611ce38963a56b5c48fd2b961813d`).
- First+final side-by-side (`_qc/first-and-final.png`, SHA-256
  `df59bde598f205c2339d41b985788eb85c8ce256b13c23f34c41e0344a9f59cb`).

## 7. Visual review (portrait, per beat)

Read via the image-capable Read tool on the contact sheet and the
first/final sheet:

- **B00 (ClaudeComposerAsk916).** Cold-open composer on cream. "Ciao,
  Liam" greeting above the composer. Ask text is legible and centred.
  Three output lines cascade in. `@HumanitariansAI` folder chip visible.
  No caption bar. No crop.
- **B01 (BrutalistHesitantWriter916).** Serif text stack fills the safe
  area vertically ("art run / compiles / the review / video file."). The
  hesitation/backspace has settled to the corrected words at 85%. No
  underfill (Gate V FILL_MIN ≥ 55%).
- **B03 (ClaudeCodeBeat916).** Full-frame code card, monospace legible
  at 540-wide thumbnail. Title "run.sh — the loop, in order." Spark line
  visible at 85%. Text fits SAFE916 with margin.
- **B07 (ClaudeCodeBeat916).** Title "run vs final — two verbs, two
  files." Both RUN and FINAL blocks present, spark line visible at 85%.
- **B10 (ClaudeComposerAsk916).** "Your turn." composer with the
  paste-ready 4-step prompt. Output lines cascade in at 85%. No bleed
  past SAFE916 bottom.
- **B11 (ClaudeTitleOutro916).** Dark outro card with cream serif
  "Brutalist Command: art run." title and `@NikBearBrown` handle. OUTRO
  LAW respected.

No blockers. No majors. No caption tracks. No stale wide crop.

## 8. Duration gate

`shorts.py` reports `[short] 6 beats · ~118.6s (1:58.6) OK`. `ffprobe`
values above confirm the encoded file also stays under 180 s.

## Summary

- Output file: `exports/short/claude-liam-brutalist-command-run-short.mp4` (2160×3840, 118.58 s).
- All strict duration checks pass with > 60 s of headroom.
- All 6 retained beats reused native portrait media unchanged (hashes verified against updated parent).
- Parent vertical updated since original build: B02 re-rendered with corrected art:99-101 reference (was art:78-80), B09 verdict re-rendered — both are dropped beats; Short content is unchanged.
- Visual review of every retained beat via extracted frames — pass (frames unchanged from original build, hashes verified).
- Ready for Bear's human review. Not uploaded; not published.
