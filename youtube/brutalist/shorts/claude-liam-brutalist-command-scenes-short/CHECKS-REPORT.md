# CHECKS-REPORT — Brutalist Command: art scenes — Short

Native 2160×3840 Short derived from the parent's full-length vertical
companion. Every retained beat reused native portrait mp4 unchanged.

**Rebuild:** 2026-09-12 (run_id `06897f7f126e45bf97904e8618225d88`).
Scripts updated since 2026-09-09 build:
`compile.py` → `e06b52ee`, `build_safety.py` → `77ec254b`, `shorts.py` → `7109a3d0`.
`math_layout_check.py` (`dd00f18c`) added to isolated toolkit.
Compile produced byte-identical output (SHA-256 `70b2a5ac` unchanged).

## Duration (Short Law: strictly under 180.0 s)

| Track   | Duration (s) | Result |
|---------|---:|:---|
| Container (format) | 115.083 | PASS |
| Video (h264, 2160×3840, 24 fps) | 115.042 | PASS |
| Audio (aac, 48 kHz, stereo) | 115.083 | PASS |

`ffprobe -v error -show_entries format=duration,size,bit_rate -show_entries stream=codec_type,codec_name,width,height,duration,r_frame_rate,sample_rate,channels`
verified against
`exports/short/claude-liam-brutalist-command-scenes-short.mp4`
(size 6,485,696 bytes; bitrate 450,853 bps;
SHA-256 `70b2a5ac9ee53d540969b6f6d2204df79032e3ab1feed89b10a70bb67998e8f3`).

Encoder headroom to the cap: **64.9 s**. No speech was truncated, sped up, or
cross-faded to fit.

## Per-beat audio verification

Each retained beat's mp3 was probed to confirm it exists and its narrated
length matches the sheet's `render_duration_s`:

| Beat | mp3 duration (s) | render_duration_s | Δ |
|---|---:|---:|---:|
| B00 | 18.645 | 18.667 | +0.022 |
| B01 | 12.352 | 12.375 | +0.023 |
| B04 | 27.349 | 27.375 | +0.026 |
| B05 | 25.920 | 25.958 | +0.038 |
| B08 | 25.344 | 25.375 | +0.031 |
| B11 |  5.312 |  5.333 | +0.021 |

Δ is the sheet's frame-boundary quantisation (24 fps ⇒ 1/24 = 0.0417 s), i.e.
every mp3 fits inside its allotted frame block.

## Compile output receipts

`runtime/scripts/compile.py --height 3840` reported:

```
[art] compiled B00  VIDEO    18.7s  ← B00.mp4
[art] compiled B01  VIDEO    12.4s  ← B01.mp4
[art] compiled B04  VIDEO    27.4s  ← B04.mp4
[art] compiled B05  VIDEO    26.0s  ← B05.mp4
[art] compiled B08  VIDEO    25.4s  ← B08.mp4
[art] compiled B11  VIDEO     5.3s  ← B11.mp4
[art] slots: 6/6 filled — B00:VIDEO B01:VIDEO B04:VIDEO B05:VIDEO B08:VIDEO B11:VIDEO
```

## Cut receipts

`runtime/scripts/shorts.py --drop B02 B03 B06 B07 B09 B10 --no-endcard --no-outro-rewrite`:

```
[short] parent reel: 12 beats · 256.3s (4:16.3) · Shorts cap 3:00
[short] manual plan: dropping B02, B03, B06, B07, B09, B10
[short] B00 native portrait reused unchanged
[short] B01 native portrait reused unchanged
[short] B04 native portrait reused unchanged
[short] B05 native portrait reused unchanged
[short] B08 native portrait reused unchanged
[short] B11 native portrait reused unchanged
[short] 6 beats · ~115.1s (1:55.1) OK
```

No ONDA CHECK rewires (native portrait media already existed for every
retained beat). No pantry overrides. Every media file is an independent copy,
never a symlink.

## Skin lint (inherited from parent — expected)

`compile.py` reported the two skin lints inherited from the parent's
portrait cold-open/outro variants; they are the expected 916-suffix mismatch
that the parent's VISUAL-REVIEW.json also documents as accepted:

```
[art] SKIN LINT: B00: palette=claude but the cold open is 'ClaudeComposerAsk916'
[art] SKIN LINT: B11: palette=claude but the outro is 'ClaudeTitleOutro916'
```

These are recorded, not suppressed; not blockers for a portrait deliverable.

## Frame QC

Extracted 18 review frames (15 %, 50 %, 85 % of each retained beat) at native
2160×3840 into `_qc/frames/`, plus 10 join frames (±0.05 s around each cut)
into `_qc/joins/`. Every join lands on a clean beat boundary — no mid-word
speech and no half-drawn UI on the "before" side of a cut. Full evidence
(with SHA-256 hashes) in `VISUAL-REVIEW.json`.

## Known limitation (inherited)

`ClaudeCodeBeat916` does not word-wrap; long code lines are horizontally
clipped inside the code card in portrait (documented by the parent's
VISUAL-REVIEW.json: "matches icons vertical … fellows should prefer the
landscape master for detailed reading"). Retained beats B04, B05, B08 share
this behaviour. For B05 the visible content is enough to land the message:
the leading score `[ 8.5]` and the composition id `FinanceSankey` — the
narration then names each item aloud.

## What was NOT done

- No new Remotion render (the ONDA CHECK found no rewires needed).
- No narration regenerated (`--no-outro-rewrite` preserves the parent outro).
- No burned-in captions, no subtitle track.
- No upload, no Git push, no publication.
- No parent-film media was modified in place.

## Result

Short renders cleanly under the 3:00 law, all six retained beats fill their
slots with independently copied native portrait media, and coherence review
confirms no dangling references to dropped beats. Ready for human review.
