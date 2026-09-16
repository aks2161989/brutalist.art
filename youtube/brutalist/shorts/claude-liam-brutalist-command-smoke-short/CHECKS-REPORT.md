# CHECKS-REPORT.md — Brutalist Command: art smoke — Short

Reel: `youtube/brutalist/shorts/claude-liam-brutalist-command-smoke-short`
Aspect: 9:16 · Native: 2160×3840 · Voice: Kokoro `am_onyx` · Captions: false
Parent: `youtube/brutalist/claude-liam-brutalist-command-smoke/vertical/`
Run ID: `c8743064e7904da6a10203c4c47185ef`

## Cut plan

```
$ python3 runtime/scripts/shorts.py \
    /Users/bear/…/youtube/brutalist/claude-liam-brutalist-command-smoke/vertical \
    --output-dir /Users/bear/…/youtube/brutalist/shorts/claude-liam-brutalist-command-smoke-short \
    --slug claude-liam-brutalist-command-smoke-short \
    --drop B02 B04 B05 B06 B09 --no-endcard --no-outro-rewrite
[short] parent reel: 11 beats · 238.7s (3:58.7) · Shorts cap 3:00
[short] manual plan: dropping B02, B04, B05, B06, B09
[short] B00 native portrait reused unchanged
[short] B01 native portrait reused unchanged
[short] B03 native portrait reused unchanged
[short] B07 native portrait reused unchanged
[short] B08 native portrait reused unchanged
[short] B10 native portrait reused unchanged
[short] 6 beats · ~127.4s (2:07.4) OK
[short] dropped: B02, B04, B05, B06, B09 · ends on the last beat (no endcard)
```

CUT-PLAN.json in this reel records strategy `whole-beat-cut`, focus, per-beat
drop reasons and cut-first review. No rewrite; `rewrite_reason: null`.

## Compile

```
$ python3 runtime/scripts/compile.py \
    /Users/bear/…/youtube/brutalist/shorts/claude-liam-brutalist-command-smoke-short \
    --height 3840 --out <reel>/exports/short
[art] compiled B00  VIDEO     9.7s  ← B00.mp4
[art] compiled B01  VIDEO    14.4s  ← B01.mp4
[art] compiled B03  VIDEO    33.0s  ← B03.mp4
[art] compiled B07  VIDEO    38.0s  ← B07.mp4
[art] compiled B08  VIDEO    27.2s  ← B08.mp4
[art] compiled B10  VIDEO     5.2s  ← B10.mp4
[art] wrote …/exports/short/claude-liam-brutalist-command-smoke-short.mp4
      (127.4s, audio: per-beat timeline (source audio preserved))
[art] slots: 6/6 filled
```

`compile.py` skin-lint noted the standing OUTRO LAW mismatch inherited from
the parent (`ClaudeComposerAsk916`/`ClaudeTitleOutro916` under palette
`claude`). This is a warning that fires on every Brutalist episode
delivered to `@HumanitariansAI` — it flags a lint rule that expects the
base ComposerAsk/TitleOutro but the parent's design system uses the
`…916` variants for native portrait. Not a blocker; behavior verified in
frame QC.

## Duration (strict < 180 s)

```
$ ffprobe -v error -show_entries format=duration:stream=codec_type,width,height,duration \
    -of default=nk=0 <reel>/exports/short/claude-liam-brutalist-command-smoke-short.mp4
[STREAM] codec_type=video  width=2160  height=3840  duration=127.416667  [/STREAM]
[STREAM] codec_type=audio                             duration=127.416000  [/STREAM]
[FORMAT]                                              duration=127.416667  [/FORMAT]
```

All three durations = **127.42 s** (2:07.42). Headroom to the 180 s cap: 52.58 s.

## Audio decode

```
$ ffmpeg -i <reel>/exports/short/…smoke-short.mp4 -af volumedetect -f null - 2>&1
Duration: 00:02:07.42, start: 0.000000, bitrate: 526 kb/s
mean_volume: -27.0 dB
max_volume:   -4.0 dB
```

Well above the -40 dB floor. No silence. Speech is intact and not sped up.

## Gate V (visual QC after compile)

```
$ cat _qc/REPORT.md
# Gate V — visual QC report
Frames sampled: 12  ·  BLOCKER: 0  ·  MAJOR: 0
Clean — no BLOCKER/MAJOR defects. ✓
```

The compiled contact sheet (`_qc/contact_sheet.png`) tiles the mid-frame of
each of the six kept beats — inspected visually alongside the per-beat
15 / 50 / 85 % frames below.

## Per-beat frames (2 fps + 15 / 50 / 85 %)

Wrote 18 frames to `_qc/per-beat/<BID>_<pct>.png` (6 beats × 3 samples).
Each frame is a native-scaled 540×960 PNG. SHA-256 recorded in
VISUAL-REVIEW.json. Visually inspected:

- **B00_50** — Composer with the ask, folder chip `@HumanitariansAI`,
  three cascade lines all inside safe area. Portrait framing correct.
- **B01_15 / _50 / _85** — Hesitant writer: `checks` in terracotta at 15%
  before correction; `renders video.` in ink at 50%; held at 85%. Words
  centered, sit inside SAFE916.
- **B03_50 / _85** — Onda-style code card, all 15 lines fit inside the card
  and the card fits inside the safe area. Spark line `Scratch dir. Real
  pipeline. Three decoded gates.` lands beneath.
- **B07_50** — Recovery card, BEFORE/WHY/RECOVERY/AFTER blocks visible,
  no clipping.
- **B08_50** — Verdict artifact with heading + six numbered lines. Legible.
- **B10_50 / _85** — OUTRO title "Brutalist Command: art smoke." above
  `@NikBearBrown` on the dark ink polarity (slug char-sum seeded).

No overflow, no clipping, no unresolved visuals, no burned-in captions, no
missing content or padding artifacts across the inspected frames.

## Container / streams / bytes

```
container:   mp4, 8,387,184 bytes
video:       h264, 2160×3840, 24 fps, 127.416667 s
audio:       aac,  127.416000 s
```

## What was NOT run

- No `--review` pass (not a final gate).
- No Kokoro re-narration.
- No Remotion re-render.
- No paid API. No upload. No publishing. No network.

## Limitations / follow-ups

- The two skin-lint warnings on the cold-open and OUTRO patterns are known
  and consistent across the Brutalist playlist. Bear/@HumanitariansAI
  review is the next gate before publication.
- No human sign-off was assumed or fabricated. VISUAL-REVIEW.json is an
  automated ("ai") reviewer record only.
