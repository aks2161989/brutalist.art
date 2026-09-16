# CHECKS-REPORT — The nbb Skill — Short (9:16 derivative)

Run ID `ceee469d2f3449e6b11a0b74027039df`. All commands were run from the
isolated toolkit at
`.repoloop/shorts/workspaces/claude-liam-brutalist-skill-nbb-short/toolkit`.

## Cut (whole-beat, before any rewrite)

```
python3 runtime/scripts/shorts.py \
  /Users/bear/.../brutalist/claude-liam-brutalist-skill-nbb/vertical \
  --output-dir /Users/bear/.../brutalist/shorts/claude-liam-brutalist-skill-nbb-short \
  --slug claude-liam-brutalist-skill-nbb-short \
  --drop B02 B04 B05 B06 B07 B08 B10 \
  --no-endcard --no-outro-rewrite
```

Output (excerpt):

```
[short] parent reel: 12 beats · 346.0s (5:46.0) · Shorts cap 3:00
[short] manual plan: dropping B02, B04, B05, B06, B07, B08, B10
[short] B00 native portrait reused unchanged
[short] B01 native portrait reused unchanged
[short] B03 native portrait reused unchanged
[short] B09 native portrait reused unchanged
[short] B11 native portrait reused unchanged
[short] 5 beats · ~108.2s (1:48.2) OK
[short] dropped: B02, B04, B05, B06, B07, B08, B10 · ends on the last beat (no endcard)
```

No re-render, no crop; every native 2160×3840 render was copied unchanged.
No outro rewrite; no endcard; the parent's Kokoro `am_onyx` mp3s were copied
independently.

## Compile

```
python3 runtime/scripts/compile.py \
  /Users/bear/.../brutalist/shorts/claude-liam-brutalist-skill-nbb-short \
  --height 3840 --out .../exports/short
```

Output (excerpt):

```
[art] compiled B00  VIDEO    16.3s  ← B00.mp4
[art] compiled B01  VIDEO    19.4s  ← B01.mp4
[art] compiled B03  VIDEO    34.8s  ← B03.mp4
[art] compiled B09  VIDEO    34.2s  ← B09.mp4
[art] compiled B11  VIDEO     3.5s  ← B11.mp4
[art] motion histogram: type-on:2  reveal:2  hold:1
[art] SKIN LINT: B00: palette=claude but the cold open is 'ClaudeComposerAsk916' — COLD OPEN LAW wants ClaudeComposerAsk
[art] SKIN LINT: B11: palette=claude but the outro is 'ClaudeTitleOutro916' — OUTRO LAW wants ClaudeTitleOutro
[art] build stamp → beat_sheet.json (5/5 filled)
[art] wrote .../exports/short/claude-liam-brutalist-skill-nbb-short.mp4
       (108.2s, audio: per-beat timeline (source audio preserved),
        drawtext: no — PIL overlays)
[art] slots: 5/5 filled — B00:VIDEO B01:VIDEO B03:VIDEO B09:VIDEO B11:VIDEO
```

Two carry-over palette lint warnings (B00/B11 name `*916` compositions on a
`palette=claude` reel) — inherited from the vertical parent; portrait-native
trade-off, not defects.

## Duration gates (strictly under 180 s)

```
$ ffprobe -v error -show_entries format=duration,size:stream=codec_type,codec_name,duration,width,height \
    -of default=noprint_wrappers=1 exports/short/claude-liam-brutalist-skill-nbb-short.mp4
codec_name=h264
codec_type=video
width=2160
height=3840
duration=108.166667
codec_name=aac
codec_type=audio
duration=108.208000
duration=108.208000
size=7385620
```

- Timeline sum (sheet `render_duration_s`): **108.21 s** — `require_short_duration` passed inside `shorts.py` and `compile.py`.
- Container duration: **108.208 s** — well under 180 s (~72 s of headroom).
- Video stream duration: **108.167 s** — well under 180 s.
- Audio stream duration: **108.208 s** — well under 180 s.
- Dimensions: **2160×3840** (native portrait 4K, no upscale, no crop).

## Audio decode

```
$ ffmpeg -v error -i exports/short/claude-liam-brutalist-skill-nbb-short.mp4 -vn -f null - && echo AUDIO_DECODE_OK
AUDIO_DECODE_OK
```

Full AAC stream decoded without error; per-beat mp3 concat preserved. No
speech is clipped, sped up or truncated — each retained beat is the parent's
original Kokoro `am_onyx` render, unchanged.

## Visual review

- Extracted 216 sample frames at 2 fps (`_qc/frames/f001.png` … `f216.png`).
- Extracted beat-relative 15%/50%/85% frames per kept beat into `_qc/beats/`.
- Built a 3×5 contact sheet at `_qc/contact-sheet.png` (SHA-256 recorded in
  `VISUAL-REVIEW.json`).
- Read the p50 frames for B00, B01, B03, B09, B11 and edge frames
  (B03-p85, B11-p85) directly with the image-capable Read tool. Findings
  recorded in `VISUAL-REVIEW.json` — no blockers, no majors. B09-p50 and
  B09-p85 hash identically because the verdict artifact card is fully static
  after its reveals complete — expected for a card-and-lines composition.

## Provenance

- Parent vertical beat sheet SHA-256:
  `3faefa0e4dea5ddd393f93c0d9eea9b663c465acab478ece99b87b9d6d73f24c`.
- Parent vertical master SHA-256 (`episode.parent_master_sha256`):
  `f25109b859ced3b9c08ff0ea9179af7caf11d32d06c4d289a4756af74addaef9`.
- Invocation `episode.source_sha256`:
  `8328fa28423a5e15fca115dbae264a2031801c1cea8b45a2fd557943a4ec8691`.
- This Short's beat sheet SHA-256:
  `0a67f3967c0ec50f2143470e0bfaafca61bf14307aa3f73e8c986f4976539402`.
- This Short's export SHA-256:
  `00758e069585949844d71f4be7f1d23bd48d0894f98310e8006fc0eec1c86db6`.

## Human approvals

`metadata.approvals = {}`. `runtime/scripts/build_safety.py::validate_approvals`
runs inside `compile.py` and did not raise — this reel is a skill teardown with
no fellows profile, no professor_notes, and no impersonated guest signature.
Nothing was auto-approved. Every retained narration line is the parent
vertical's own audio, unchanged.

## Conclusion

The Short is 108.208 s of native portrait 4K, strictly under 3:00 with ~72 s
of headroom, using only the vertical parent's native renders and Kokoro
`am_onyx` audio, unchanged. Written at
`exports/short/claude-liam-brutalist-skill-nbb-short.mp4`. Human review is
pending.
