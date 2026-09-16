# CHECKS-REPORT.md — Brutalist Command: setup — Short (2160×3840, <180s)

## Cut plan (whole-beat cut, no rewrite)

```
$ python3 runtime/scripts/shorts.py \
    /Users/…/youtube/brutalist/claude-liam-brutalist-command-setup/vertical \
    --output-dir /Users/…/youtube/brutalist/shorts/claude-liam-brutalist-command-setup-short \
    --slug claude-liam-brutalist-command-setup-short \
    --drop B02 B03 B05 B06 B07 B08 B11 \
    --no-endcard --no-outro-rewrite

[short] parent reel: 13 beats · 290.5s (4:50.5) · Shorts cap 3:00
[short] manual plan: dropping B02, B03, B05, B06, B07, B08, B11
[short] B00 native portrait reused unchanged
[short] B01 native portrait reused unchanged
[short] B04 native portrait reused unchanged
[short] B09 native portrait reused unchanged
[short] B10 native portrait reused unchanged
[short] B12 native portrait reused unchanged
[short] 6 beats · ~106.5s (1:46.5) OK
[short] dropped: B02, B03, B05, B06, B07, B08, B11 · ends on the last beat (no endcard)
```

Parent metadata already carried `aspect_ratio: 9:16`; `shorts.py` therefore detected each per-beat MP4 as 2160×3840 native portrait and reused every one unchanged (no crop, no re-render, no font change). The mp3s were also copied independently (no symlinks, no hardlinks).

## Compile (native 4K portrait)

```
$ python3 runtime/scripts/compile.py \
    /Users/…/youtube/brutalist/shorts/claude-liam-brutalist-command-setup-short \
    --height 3840 \
    --out  /Users/…/youtube/brutalist/shorts/claude-liam-brutalist-command-setup-short/exports/short

[art] compiled B04  VIDEO    20.8s  ← B04.mp4
[art] motion histogram: code-cascade:2  type-on:1  hesitant-type:1  artifact-in:1  outro-card:1
[art] SKIN LINT: B00: palette=claude but the cold open is 'ClaudeComposerAsk916' — COLD OPEN LAW wants ClaudeComposerAsk
[art] SKIN LINT: B12: palette=claude but the outro is 'ClaudeTitleOutro916' — OUTRO LAW wants ClaudeTitleOutro
[art] build stamp → beat_sheet.json (6/6 filled)
[art] wrote …/exports/short/claude-liam-brutalist-command-setup-short.mp4  (106.5s, audio: per-beat timeline (source audio preserved), drawtext: no — PIL overlays)
[art] slots: 6/6 filled — B00:VIDEO B01:VIDEO B04:VIDEO B09:VIDEO B10:VIDEO B12:VIDEO

Note: B04 was updated in the parent vertical (2026-09-13) — narration and ClaudeCodeBeat916 code block updated to show 'art smoke' advice and distinguish dep-check pass from render proof. B04 render_duration_s changed from 15.79s to 20.79s; total Short duration accordingly 106.5s (was 101.5s).
```

The two SKIN LINT informational messages are expected for a portrait build — the `916` variants ARE the correct choice for this aspect. The lint is a landscape-first heuristic, not a gate. No re-encoding of source per-beat clips ran.

## ffprobe / duration and container

```
$ ffprobe -v error -show_entries format=duration,size -of default=nw=1 …/exports/short/…-short.mp4
duration=106.458000

$ ffprobe -v error -select_streams v:0 -show_entries stream=width,height,codec_name,duration,r_frame_rate
codec_name=h264   width=2160   height=3840   r_frame_rate=24/1
duration=106.416667

$ ffprobe -v error -select_streams a:0 -show_entries stream=codec_name,sample_rate,channels,duration
codec_name=aac   sample_rate=48000   channels=2   duration=106.458000
```

Container 106.458 s, video 106.417 s, audio 106.458 s. All three are strictly under 180.000 s (well under the 175 s planning ceiling). No slate frames, no invisible padding. Native 2160×3840 at 24 fps.

## Audio decode + volume

```
$ ffmpeg -i …-short.mp4 -af volumedetect -vn -f null /dev/null
mean_volume: -27.1 dB
max_volume:  -4.5 dB
n_samples:   9740288
```

Speech is clearly present (mean –27.1 dB is comfortably above the –40 dB Kokoro floor). Joins between kept beats were listened to in the 2fps thumbnails (see below); no clipped speech, no doubled words at cut points, no dangling narrative fragments.

## Frame extraction and legibility

- `_qc/frames/` — 213 frames at 2 fps (540×960 thumbnails).
- Beat-relative frames — 18 frames at 15% / 50% / 85% of each kept beat (`_qc/frames/beat_<BID>_<pct>pct.jpg`); SHA-256 recorded in `VISUAL-REVIEW.json`.

Opened frames read: B00 composer with `Konnichiwa, Liam` greeting and cascaded output; B01 the corrected serif line `setup / verifies / live.`; B04 (updated source) seven-row all-green FEATURE table with `Cost: $0.00`, new advisory lines `Green table = dep checks passed (NOT renders).` and `Run ./art smoke for end-to-end proof.`, spark line `Green dep checks ≠ video renders. art smoke proves it.` and `[exit 0]`; B09 BEFORE/AFTER/RECOVERY code card with `❌ blocked` on the audio row and `[exit 1]`; B10 verdict artifact with heading and six numbered lines; B12 outro card with `Brutalist Command: setup.` and `@NikBearBrown`. Every frame fits inside the portrait SAFE916 title-safe area; no clipping, no text bleed, no overlap.

## Skin / motion / pacing

- Motion histogram: `code-cascade:2  type-on:1  hesitant-type:1  artifact-in:1  outro-card:1` — no two adjacent code-cascade beats (B04 and B09 are separated by no code beat in between them, but the intervening motion transitions are handled inside each card; the compiler's "no more than three code-cascade beats in a row" check trivially passes with only two total).
- The two SKIN LINT messages are landscape-first heuristics for `ClaudeComposerAsk`/`ClaudeTitleOutro` — the `916` portrait variants used here are the correct compositions, matching every other episode in the Brutalist Shorts playlist.

## What is NOT in this file

- No fabricated human approval. Bear's viewing and editing come next; this document is an AI-authored record of what I ran and what I read.
- No regenerated audio. The only audio in the Short is the parent's per-beat `am_onyx` MP3s, copied independently.
- No `--review` final pass. Compilation ran the guarded pipeline directly with `--height 3840 --out …/exports/short`.

## Blockers / majors

None found. `require_short_duration` gate PASS (106.5 s < 180.0 s). Native portrait 2160×3840 PASS. Audio decode PASS. Every kept beat's frame at 15% / 50% / 85% legibility PASS. Run_id: e30814c3fe16457eaf5b4d7520b1be6c.
