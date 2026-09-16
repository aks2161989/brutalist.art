# CHECKS-REPORT — Brutalist Command: art shorts (Short cut)

Run ID: `c3c149dbdf064d1d99ee95c5f9350955`
Date: 2026-09-12
Output: `exports/short/claude-liam-brutalist-command-shorts-short.mp4`
SHA-256: `d18a9cdf7219f25be0f776933fcb98758439177fd0ab177d4a2c0b63d216d750`

## 0. Rebuild trigger

Parent master SHA changed (old: `4ef22048…4a371`, new: `3481e57f…9fd`).
Diff: B03 media (`media/B03.mp4`) re-rendered in parent vertical
(2026-09-12T17:22:21) — the SHORTS LAW code block was expanded with more
detailed per-rule descriptions; narration and audio for B03 are unchanged.
B00/B01/B07/B09/B11 media and all mp3s are byte-identical to the prior build.
Rebuild: copy new B03.mp4, run compile.py, re-verify.

## 1. Cut plan (whole-beat)

- Strategy: `whole-beat-cut`, no rewrite (`CUT-PLAN.json`).
- Kept: B00, B01, B03, B07, B09, B11 (6 beats).
- Dropped: B02, B04, B05, B06, B08, B10 (6 beats).
- Cut mechanism: `python3 runtime/scripts/shorts.py … --drop … --no-endcard --no-outro-rewrite`.
- Per-beat inputs recorded in `build-state.json/input_sha256` with new B03
  hash (`0ff4ef5b…`) matching current parent vertical.
- Planned duration: 129.18 s. Measured: 124.67 s. Cap: 180 s (strict).

## 2. Compile

Command:
```
python3 runtime/scripts/compile.py <reel> --height 3840 --out <reel>/exports/short
```

Verified by `build-state.json` (`status: ready`, `sha256: d18a9cdf…`), and by
re-probing the finished MP4 (§3 below). Per-input SHA-256 records in
`build-state.json` with updated B03 hash.

## 3. Duration check (strict Shorts law)

`ffprobe -show_entries format=duration:stream=index,codec_type,codec_name,width,height,duration`:

| Stream | Value |
|---|---|
| Container (`format.duration`) | **124.666667 s** ✓ < 180.0 |
| Video (h264, 2160×3840) | **124.666667 s** ✓ < 180.0 |
| Audio (aac, decoded to pcm_s16le) | **124.672000 s** ✓ < 180.0 |

All three durations are strictly under 180.0 s with ≥ 55 s of encoding
headroom.

## 4. Dimensions

Video stream: 2160 × 3840 (native portrait). No crop path, no re-render.
No captions, no burned-in subtitles. Palette = claude cream (#FAF9F5).

## 5. Audio decode

`ffmpeg -i <mp4> -vn -c:a pcm_s16le $TMPDIR/audio.wav` completed without
errors; wav duration = 124.672 s, 48 kHz stereo.

`volumedetect`:
- `mean_volume: -26.8 dB`
- `max_volume: -3.0 dB` (no clipping)

No decode errors; audio duration matches container/video within
expected AAC padding.

## 6. Frame evidence

- 18 beat-relative frames at 15 % / 50 % / 85 % of each of the six
  retained beats (`_qc/frames/B{00,01,03,07,09,11}_{15,50,85}.png`).
- 6-beat contact sheet (`_qc/contact_sheet.png`, SHA-256
  `ffca9df9fd3ce96ed7c3231d8403fc274dcab8c83d700857cd4f409165710d74`).

## 7. Visual review (portrait, per beat)

Read via the image-capable Read tool on the contact sheet and per-beat frames:

- **B00 (ClaudeComposerAsk916).** Cold-open composer on cream. "Salam,
  Liam" greeting above the composer. Ask text legible and centred.
  Two output lines cascade in. `@HumanitariansAI` folder chip visible.
  No caption bar. No crop.
- **B01 (BrutalistHesitantWriter916).** Serif stanza fills the safe
  area vertically ("art shorts / drops beats / and rewires /
  graphics."). Terracotta hesitation settled to corrected words by 85 %.
  No underfill.
- **B03 (ClaudeCodeBeat916, updated render).** Updated SHORTS LAW code
  card — expanded per-rule descriptions (7 lines of rules vs 5 in the
  prior build): CHECK LENGTH FIRST / SHORTEN BY CUTTING / REUSE
  RETAINED NARRATION / PUBLISHING IS SEPARATE / --vertical is NOT a
  Short. Spark line "< 3:00 or it never publishes." at bottom. Text
  fits SAFE916 with expected right-truncation on long monospace lines
  (composition-level layout). No bleed, cream background.
- **B07 (ClaudeCodeBeat916).** Title `$ ./art shorts /tmp/claude-501/…`.
  Cap-check, auto-plan (B02 dropped), ONDA CHECK block (B00–B06 rewires),
  and `~163.5s (2:43.5) OK` all present. Spark line "Plan first. Then
  rewire. Then render." at bottom.
- **B09 (ClaudeVerdictArtifact916).** Artifact card with heading "art
  shorts — the whole surface, in the order you use it" and 8 numbered
  lines. Terracotta numerals, cream ground, no bleed past SAFE916 bottom.
- **B11 (ClaudeTitleOutro916).** Dark outro card with cream serif
  "Brutalist Command: art shorts." title and `@NikBearBrown` handle.
  OUTRO LAW respected.

No blockers. No majors. No caption tracks. No stale wide crop.

## 8. Duration gate

`ffprobe` values above confirm the encoded file stays strictly under
180 s. `beat_sheet.json/metadata.short_validation.status = ready` with
no errors.

## Summary

- Output file: `exports/short/claude-liam-brutalist-command-shorts-short.mp4` (2160×3840, 124.67 s).
- All strict duration checks pass with > 55 s of headroom.
- 5 retained beats reused native portrait media unchanged; B03 replaced
  with updated render from rebuilt parent.
- Visual review of every retained beat via extracted frames — pass.
- Ready for Bear's human review. Not uploaded; not published.
