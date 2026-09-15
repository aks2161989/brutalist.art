# CHECKS-REPORT — The guests Skill — Short (9:16 derivative)

Run ID `2c8cb7d4b9e7486c88488b9396afadba`. All commands were run from the
isolated toolkit at
`.repoloop/shorts/workspaces/claude-liam-brutalist-skill-guests-short/toolkit`.

## Cut (whole-beat, before any rewrite)

```
python3 runtime/scripts/shorts.py \
  /Users/bear/…/brutalist/claude-liam-brutalist-skill-guests/vertical \
  --output-dir /Users/bear/…/brutalist/shorts/claude-liam-brutalist-skill-guests-short \
  --slug claude-liam-brutalist-skill-guests-short \
  --drop B02 B04 B05 B06 B07 B08 B10 \
  --no-endcard --no-outro-rewrite
```

Output (excerpt):

```
[short] parent reel: 12 beats · 292.9s (4:52.9) · Shorts cap 3:00
[short] manual plan: dropping B02, B04, B05, B06, B07, B08, B10
[short] B00 native portrait reused unchanged
[short] B01 native portrait reused unchanged
[short] B03 native portrait reused unchanged
[short] B09 native portrait reused unchanged
[short] B11 native portrait reused unchanged
[short] 5 beats · ~81.7s (1:21.7) OK
[short] dropped: B02, B04, B05, B06, B07, B08, B10 · ends on the last beat (no endcard)
```

No re-render, no crop; every native 2160×3840 render was copied unchanged.
The `math_layout_check` module (present in the main repo, absent from the
isolated toolkit) was shadow-copied to the toolkit scripts before invocation.

## Compile

```
python3 runtime/scripts/compile.py \
  /Users/bear/…/brutalist/shorts/claude-liam-brutalist-skill-guests-short \
  --height 3840 --out …/exports/short
```

Output (excerpt):

```
[art] motion histogram: type-on:2  reveal:2  hold:1
[art] SKIN LINT: B00: palette=claude but the cold open is 'ClaudeComposerAsk916' — COLD OPEN LAW wants ClaudeComposerAsk
[art] SKIN LINT: B11: palette=claude but the outro is 'ClaudeTitleOutro916' — OUTRO LAW wants ClaudeTitleOutro
[art] build stamp → beat_sheet.json (5/5 filled)
[art] wrote …/exports/short/claude-liam-brutalist-skill-guests-short.mp4
       (81.7s, audio: per-beat timeline (source audio preserved), drawtext: no — PIL overlays)
[art] slots: 5/5 filled — B00:VIDEO B01:VIDEO B03:VIDEO B09:VIDEO B11:VIDEO
```

Two carry-over palette lint warnings (B00/B11 name `*916` compositions on a
`palette=claude` reel) — inherited from the vertical parent; portrait-native
trade-off, not defects.

## Duration gates (strictly under 180 s)

```
$ ffprobe -v error -show_entries format=duration,size:stream=codec_type,codec_name,duration,width,height \
    -of default=noprint_wrappers=1 exports/short/claude-liam-brutalist-skill-guests-short.mp4
codec_name=h264
codec_type=video
width=2160
height=3840
duration=81.666667
codec_name=aac
codec_type=audio
duration=81.708000
duration=81.708000
size=5761184
```

- Timeline sum (sheet `render_duration_s`): **81.71 s** — `require_short_duration` passed inside `shorts.py` and `compile.py`.
- Container duration: **81.708 s** — well under 180 s.
- Video stream duration: **81.667 s** — well under 180 s.
- Audio stream duration: **81.708 s** — well under 180 s.
- Dimensions: **2160×3840** (native portrait 4K, no upscale).

## Audio decode

```
$ ffmpeg -v error -i exports/short/…mp4 -vn -f null - && echo OK
AUDIO_DECODE_OK
```

Full AAC stream decoded without error; per-beat mp3 concat preserved. No
speech is clipped, sped up or truncated — each retained beat is the parent's
original Kokoro `am_onyx` render, unchanged.

## Visual review

- Extracted 163 frames at 2 fps (`_qc/frames/f001.png` … `f163.png`).
- Extracted beat-relative 15% / 50% / 85% frame per kept beat (15 PNGs total).
- Built contact sheet at `_qc/contact-sheet.png` (SHA-256 recorded in
  `VISUAL-REVIEW.json`).
- Read p50 frames for B00, B01, B03, B09, B11 directly. Findings:
  - **B00** ClaudeComposerAsk916: cream ground, 'Hallo, Liam' greeting, composer
    card with the ask, three result lines — all inside portrait safe area.
  - **B01** BrutalistHesitantWriter916: post-correction state 'prunes' visible,
    five lines fill portrait safe area (>55% fill, portrait-aware scale active).
  - **B03** SkillTeardownPipeline916: full six-node spine, THE VIDEO node in
    terracotta, sparkline 'Bookends around the guest's file.' legible.
  - **B09** ClaudeVerdictArtifact916: white card, 'A frame. Not a re-edit.',
    all six numbered terracotta verdict lines legible, inside safe area.
  - **B11** ClaudeTitleOutro916: dark ink ground, 'The guests Skill.
    @NikBearBrown' correctly positioned, Liam sign-off confirmed.
- No blockers, no majors.

## Provenance

- Episode source_sha256 (this invocation's `episode.source_sha256`):
  `b414ed2479d64033f05ce67115cdd6ba366b2014b87d5fca20ac17e968c119e0`.
- Parent vertical master SHA-256 (`episode.parent_master_sha256`):
  `3d99d32a70dfc8189eeae5f0e673a9a25e6f203118553ee41d4c115598868880`.
- This Short's beat sheet SHA-256:
  `e6cce757ac6752f574f6bd39437e4cef6fa3a6f8ce01d808407132b9d2bf3336`.
- This Short's export SHA-256:
  `bce582b1f21ec024d7465c47564655a16854c91cd8e291d77a67b451a76d29b7`.

## Human approvals

`metadata.approvals = {}`. `runtime/scripts/build_safety.py::validate_approvals`
runs inside `compile.py` and did not raise — this reel is neither a fellows
profile nor does any retained beat require professor_notes / GATE-N (the very
absence that B01 and B09 name). GATE G is a claim inside the guests skill's
own contract (about hypothetical real guests episodes); this teardown ships
no real guest video and no fabricated guest signature. Nothing was
auto-approved.

## Conclusion

The Short is 81.708 s of native portrait 4K, strictly under 3:00, using only
the vertical parent's native renders and Kokoro `am_onyx` audio, unchanged.
Written at `exports/short/claude-liam-brutalist-skill-guests-short.mp4`. Human
review is pending.
