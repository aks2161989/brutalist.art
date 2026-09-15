# CHECKS-REPORT — Brutalist Utility: brand_variant.py — Short

Run ID `becb052db31446b88e60ea9de19dfbaf`. This Short is a whole-beat cut of the
long-form utility teardown at
`youtube/brutalist/claude-liam-brutalist-runtime-brand-variant/vertical/`.

## Editorial decision — cut first

- Read the parent's 12-beat portrait sheet in full.
- Kept six beats in source order: B00, B01, B02, B04, B09, B11.
- Dropped six middle beats: B03, B05, B06, B07, B08, B10. Reasons per beat are
  recorded in `CUT-PLAN.json`. Every dropped beat is a code-detail or
  mechanism-detail beat; every safety claim, audience-list claim and one
  concrete worked example remain.
- Strategy is `whole-beat-cut`; no narration was rewritten, no audio regenerated.

## Source change in this run

The parent's B04 was re-rendered on 2026-09-13T18:01:13 with corrected code
formatting (title updated to "verbatim from demo/RUN-LOG.txt §2+5"; the status
lines reformatted to match the actual demo run log verbatim). The Short refreshes
B04 from the updated parent native portrait clip. All other kept beats (B00, B01,
B02, B09, B11) are byte-identical to the prior Short (SHA-256 unchanged). No
audio was regenerated; the B04 narration did not change.

## Compile command (actually run)

```
PYTHONPATH=<toolkit>/runtime/scripts python3 <toolkit>/runtime/scripts/compile.py \
  <short> --height 3840 --out <short>/exports/short
```

Output:
```
[art] compiled B04  VIDEO    21.0s  ← B04.mp4
[art] build stamp → beat_sheet.json (6/6 filled)
[art] wrote …/exports/short/claude-liam-brutalist-runtime-brand-variant-short.mp4  (92.3s, …)
[art] slots: 6/6 filled — B00:VIDEO B01:VIDEO B02:VIDEO B04:VIDEO B09:VIDEO B11:VIDEO
```

Skin-lint warnings on B00 (`ClaudeComposerAsk916`) and B11 (`ClaudeTitleOutro916`)
are inherited from the parent; the components are portrait-native by design
and every prior playlist episode carries the same cosmetic note. Not blockers.

## Duration verification

```
$ ffprobe -v error -show_entries format=duration -of json <mp4>
format.duration = 92.291667

$ ffprobe -v error -show_entries stream=codec_name,width,height,r_frame_rate,duration <mp4>
video: h264  2160×3840  24/1  92.291667s
audio: aac                    92.291000s
```

All three durations are strictly below the 180.0s hard cap; the closest
measurement is 87.71s below the cap.

## Dimensions

Native portrait 2160×3840 h264 @ 24fps. Every source beat mp4 was verified
2160×3840 by the parent's build record before reuse.

## Media integrity — kept clips are independent copies

| Slot | SHA-256 |
|------|---------|
| media/B00.mp4 | `f978476dab27b9926248381b0bd9772b2008c888911298be4ae849a657bf53d6` |
| media/B01.mp4 | `b382455040458e34ca338b1aadc07be7f0ba422a967c4843d0a10fabc4545dc1` |
| media/B02.mp4 | `1a807355497384649ee08d985682056dbcd2302d19c8afd8f7611b1798766801` |
| media/B04.mp4 | `2144c408e4047b30a4ae0b42e044d829742351f56e17b0d6060d8ad9ea17b346` |
| media/B09.mp4 | `825d50413e4f6dd8c9452a0a7800bde28a5f8cdec8025c874ad9bde0dc2e90a9` |
| media/B11.mp4 | `38466cbe035b3fb4083dce502bc55ae0e7fd63fa63da13c4aa372b7bde4397c3` |
| mp3/beat-B00.mp3 | `47a7d07b687efbbdfdc072872b82c2c830a11a1cd7d957deecb958cd4c9e68cf` |
| mp3/beat-B01.mp3 | `baa9f34a7bf316675ebba44568757415f776ab04a9a57d9cae0745c9d46af221` |
| mp3/beat-B02.mp3 | `3d5605ab45a13441728d093ff7ff28500e162e856ce9be4d504ab9ac9eb8a90b` |
| mp3/beat-B04.mp3 | `07ac4640207b570feedaefe41f4aef38ff2546c259e70c6d27d6571734c73e0b` |
| mp3/beat-B09.mp3 | `743269aead11229fa6eeb63d32ad0a6b70d5a7338a550b7e405dbf6d7e5ce07b` |
| mp3/beat-B11.mp3 | `1dee237c2fd6b0b269a810158fbbbb1881ee146d33b38c25320c78fb8ec039f1` |

B04.mp4 is the updated parent render (2026-09-13). All other clips are
byte-identical to the prior Short.

## Frame evidence

18 frames extracted from the final mp4 at beat-relative 15/50/85 percent into
`_qc/beat_frames/`. Hashes recorded in `VISUAL-REVIEW.json`. Frames inspected:

- B00 mid — greeting `Yassou, Liam`, topic `BRUTALIST · UTILITY: BRAND_VARIANT.PY`,
  composer card with the ask and three output lines.
- B01 late — corrected serif lines settle: "the brand.py variant just sits and
  stamps the metadata." (correction fully visible).
- B02 mid — SkillTeardownMechanism916 with UTILITY · PIPELINE heading, the
  RESOLVE→STAMP→TODO→EMIT body, deterministic-half quote block, spark chip.
- B04 mid — code cascade showing the verbatim `[variant]` status lines and the
  emitted `.metadata` block (updated render, title now reads
  "verbatim from demo/RUN-LOG.txt §2+5").
- B09 late — six-line Verdict artifact fully rendered.
- B11 mid — locked title outro with `@NikBearBrown` handle and terracotta dot.

No dropped/truncated audio, no clipped text, no edge bleed.

## Publishing / uploads / paid services

None. No API was called; no Kokoro or ElevenLabs run; no YouTube touch; no
Git push. This report is the render receipt only.

## Output

- Short mp4: `exports/short/claude-liam-brutalist-runtime-brand-variant-short.mp4`
  · SHA-256 `f06280e5578db039c38f60acd8247670029da21712b48be1415771a3b7ebcf85`
  · container 92.292s · 2160×3840 h264 24fps · audio 92.291s.
- Final beat sheet: `beat_sheet.json`
  · SHA-256 `7f50be29535b3de8aa631f353307de704052393551f9b9d8362aa2f403fb2ea6`.
- Parent vertical beat sheet (source for this run):
  · SHA-256 `7dde19bc103196daf5864804dc2b194fbd6d2d5b9b9576933bf5551f70479edb`.
- Parent long (16:9) remains untouched
  · SHA-256 `030d552849d7d9f9836d7fbf048a3bdee6280b816fe675b395c8f6c7e98f5117`.
