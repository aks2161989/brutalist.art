# CHECKS-REPORT — Brutalist Command: art icon-build — Short (9:16)

Run ID: `cd463d4c846f48aa8632dd051a6c5f93`  ·  parent master SHA-256: `3566906b923fb2b0ef211f5ed1dcb434109b2ad68144d389d43edeeecf4a86a2`

**Re-verified 2026-09-12** — repoloop flagged source/feedback change since prior build (run_id `d9e121a0764e4ebca8b33ca6953d4f46`). All six retained beat media files confirmed byte-identical to parent vertical. Re-compiled; output MP4 is byte-identical (same SHA). Beat_sheet.json build stamp refreshed to `2026-09-12T08:07:24`. Missing `math_layout_check` module copied from main toolkit runtime before compile.

## 1. Cut plan gate

Written **before** rewriting anything. See `CUT-PLAN.json`.

- Strategy: `whole-beat-cut` (no rewrite needed).
- Kept: `B00, B01, B04, B06, B09, B11` (6 beats).
- Dropped: `B02, B03, B05, B07, B08, B10` (6 beats).
- Planned duration: 113.5 s (well below the 175 s target ceiling and the 180 s hard cap).

## 2. Derive the Short cut

Command (from the shared toolkit root):

```
python3 runtime/scripts/shorts.py \
  youtube/brutalist/claude-liam-brutalist-command-icon-build/vertical \
  --output-dir youtube/brutalist/shorts/claude-liam-brutalist-command-icon-build-short \
  --slug claude-liam-brutalist-command-icon-build-short \
  --drop B02 B03 B05 B07 B08 B10 \
  --no-endcard --no-outro-rewrite
```

Result (key lines):

```
[short] parent reel: 12 beats · 248.3s (4:08.3) · Shorts cap 3:00
[short] manual plan: dropping B02, B03, B05, B07, B08, B10
[short] B00 native portrait reused unchanged
[short] B01 native portrait reused unchanged
[short] B04 native portrait reused unchanged
[short] B06 native portrait reused unchanged
[short] B09 native portrait reused unchanged
[short] B11 native portrait reused unchanged
[short] 6 beats · ~113.5s (1:53.5) OK
[short] dropped: B02, B03, B05, B07, B08, B10 · ends on the last beat (no endcard)
```

All six retained beats resolved via the "native portrait reused unchanged" path — no re-render, no crop, no auto-cut. Each beat's mp3 was independently copied under `mp3/`. Metadata is `kind: short`, `aspect_ratio: 9:16`, `playlist: Brutalist`, `voice: am_onyx`, `voice_kokoro: am_onyx`, `captions: false`.

`short_validation` in the derived beat sheet: `{status: ready, errors: []}`.

## 3. Compile (assemble + 4K master, no --review)

```
python3 runtime/scripts/compile.py \
  youtube/brutalist/shorts/claude-liam-brutalist-command-icon-build-short \
  --height 3840 \
  --out youtube/brutalist/shorts/claude-liam-brutalist-command-icon-build-short/exports/short
```

Result (key lines):

```
[art] compiled B00  VIDEO    16.7s  ← B00.mp4
[art] compiled B01  VIDEO    14.6s  ← B01.mp4
[art] compiled B04  VIDEO    25.9s  ← B04.mp4
[art] compiled B06  VIDEO    26.1s  ← B06.mp4
[art] compiled B09  VIDEO    24.5s  ← B09.mp4
[art] compiled B11  VIDEO     5.8s  ← B11.mp4
[art] SKIN LINT: B00: palette=claude but the cold open is 'ClaudeComposerAsk916' — COLD OPEN LAW wants ClaudeComposerAsk
[art] SKIN LINT: B11: palette=claude but the outro is 'ClaudeTitleOutro916' — OUTRO LAW wants ClaudeTitleOutro
[art] build stamp → beat_sheet.json (6/6 filled)
[art] wrote .../exports/short/claude-liam-brutalist-command-icon-build-short.mp4
      (113.5s, audio: per-beat timeline (source audio preserved), drawtext: no — PIL overlays)
[art] slots: 6/6 filled — B00:VIDEO B01:VIDEO B04:VIDEO B06:VIDEO B09:VIDEO B11:VIDEO
```

Two `SKIN LINT` lines are the same false positives noted on every `command-*` episode: `*916` wrappers are the correct portrait scenes for the Claude palette.

## 4. Duration gate (strictly under 180 s)

`ffprobe -v error -show_entries format=duration:stream=codec_type,duration,width,height -of default=noprint_wrappers=0 exports/short/claude-liam-brutalist-command-icon-build-short.mp4`

```
[STREAM] codec_type=video  width=2160  height=3840  duration=113.416667
[STREAM] codec_type=audio  duration=113.458000
[FORMAT] duration=113.458000
```

- Timeline (compile stamp): **113.5 s**
- Container: **113.458 s** (< 180)
- Video stream: **113.417 s** (< 180)
- Audio stream: **113.458 s** (< 180)
- Dimensions: **2160 × 3840** — native 4K portrait, not upscaled.

Headroom against the 180 s cap: **66.5 s**.

## 5. Per-beat mp3 duration sanity

`ffprobe -show_entries format=duration -of csv=p=0` on each `mp3/beat-*.mp3`:

| Beat | mp3 seconds | render_duration_s (padded to 24 fps frame) | Δ |
|---|---:|---:|---:|
| B00 | 16.640 | 16.667 | +0.027 |
| B01 | 14.549 | 14.583 | +0.034 |
| B04 | 25.899 | 25.917 | +0.018 |
| B06 | 26.069 | 26.083 | +0.014 |
| B09 | 24.418 | 24.458 | +0.040 |
| B11 |  5.717 |  5.750 | +0.033 |

Every render leaves a small (<50 ms) tail — no clipped speech at any beat boundary. Sum: 113.28 s speech, 113.46 s render, 113.46 s muxed audio.

## 6. Frame evidence — 15 %, 50 %, 85 % per beat

Beat start/duration derived from `render_duration_s`:

| Beat | start (s) | 15 % | 50 % | 85 % |
|---|---:|---:|---:|---:|
| B00 |   0.000 |  2.500 |  8.333 | 14.167 |
| B01 |  16.667 | 18.854 | 23.958 | 29.062 |
| B04 |  31.250 | 35.137 | 44.208 | 53.279 |
| B06 |  57.167 | 61.079 | 70.208 | 79.337 |
| B09 |  83.250 | 86.919 | 95.479 | 104.038 |
| B11 | 107.708 | 108.570 | 110.583 | 112.595 |

Extracted with `ffmpeg -ss <t> -i <mp4> -frames:v 1 -vf scale=540:960 _qc/frames/t<t>.png` and read back via the image-capable Read tool. SHA-256s recorded in `VISUAL-REVIEW.json → frames[]`.

Also built a 2 fps contact sheet: `_qc/contact-sheet.png`.

### Observations (all six retained beats)

- **B00 (2.500 s, 8.333 s, 14.167 s)** — Merhaba, Liam. Composer card, `art icon-build` topic, three result lines settle cleanly on cream; @HumanitariansAI folder chip present; portrait framing intact.
- **B01 (18.854 s, 23.958 s, 29.062 s)** — Hesitant writer types `art / icon-build / downloads / new icons.`, then rewrites `downloads → cuts` and `new → existing`. Caret and 4-line stack read at full serif weight (portrait-scale patch is baked into the parent render).
- **B04 (35.137 s, 44.208 s, 53.279 s)** — Four rules code card. All four numbered rules and the spark line `One weight. One geometry. One color hook.` are on screen and legible.
- **B06 (61.079 s, 70.208 s, 79.337 s)** — `$ ./art icon-build --dry-run` verbatim. All five source rows + total present. Header text `(priority — first to claim keeps it)` clips its trailing `)` at the composition edge — same behaviour as the parent 9:16, not a regression introduced by the cut. Minor limitation, logged in `VISUAL-REVIEW.json`.
- **B09 (86.919 s, 95.479 s, 104.038 s)** — Verdict artifact card fully in view; all seven numbered lines readable.
- **B11 (108.570 s, 110.583 s, 112.595 s)** — Title outro: `Brutalist Command: art icon-build.` with hardcoded `@NikBearBrown` handle. Portrait crop is centred; terracotta accent dot on the trailing period visible.

## 7. Narration continuity after cutting

- **Opening** — B00 introduces Liam ("Merhaba, this is Liam, in for Bear.") and states the problem; then B01 corrects the misconception directly. No numbered transitions ("rule three...") reference a dropped beat.
- **Mid-cut** — B04's four rules stand alone; the narration says "Four rules do the cutting." No prior beat is referenced. B06 opens `./art icon-build --dry-run` fresh; it does not depend on B02/B03/B05.
- **Verdict** — B09 recaps the whole surface. Every clause (the four rules, the four exclusions, the 44 pt math, NOTICE.md, `--dry-run`, `--limit N`) refers to a fact the film has already established (in B00, B04, B06 within the Short) or that it names on screen in the verdict card itself. No dangling references.
- **Outro** — B11 is unchanged.

## 8. Files on disk

- Master:  `exports/short/claude-liam-brutalist-command-icon-build-short.mp4`  ·  SHA-256 `1c30dfd739a6094f39eaceb5567d4cbff9089e290b4d25d2f62e2f0c5bd78c13`  (byte-identical after re-compile)
- Beat sheet:  `beat_sheet.json`  ·  SHA-256 `d843ba1d6138d7f83adb33a43738080520bdba78fe8485180a646b7b7a938ddc`  (build stamp updated to 2026-09-12T08:07:24)
- Compiler receipt: `exports/short/claude-liam-brutalist-command-icon-build-short.verified.json`
- Frames + contact sheet: `_qc/frames/*.png` and `_qc/contact-sheet.png`

## 9. Blockers / majors

None. 0 blockers, 0 majors. One minor (parent-inherited) observation on B06 header wrap.
