# CHECKS REPORT — The riff Skill (Short)
**Episode:** claude-liam-brutalist-skill-riff-short
**Run ID:** 38b1b690aae440d8b19e5c87ff7513ab
**Date:** 2026-09-12

---

## 1. Source validation

```
sha256 of parent vertical beat_sheet.json (captured at snapshot):
  079a0f6428db7119cdd7f66ee830743d8ec6d6f11067ae00d4816809b6aa254f
```

Parent vertical beat_sheet confirmed 12 beats, all with VIDEO status and native 9:16 media.

## 2. Dimension check (source clips, kept beats)

```
ffprobe -v error -select_streams v:0 -show_entries stream=width,height ...
B00: 2160,3840   (9:16 ✓)
B01: 2160,3840   (9:16 ✓)
B04: 4320,7680   (9:16 ✓)
B08: 4320,7680   (9:16 ✓)
B09: 4320,7680   (9:16 ✓)
B11: 2160,3840   (9:16 ✓)
```

All kept beats confirmed native portrait. No center-cutting of generated graphics.

## 3. shorts.py run

```
python3 runtime/scripts/shorts.py \
  .../claude-liam-brutalist-skill-riff/vertical \
  --output-dir .../claude-liam-brutalist-skill-riff-short \
  --slug claude-liam-brutalist-skill-riff-short \
  --drop B02 B03 B05 B06 B07 B10 \
  --no-endcard --no-outro-rewrite

[short] parent reel: 12 beats · 234.5s (3:54.5) · Shorts cap 3:00
[short] manual plan: dropping B02, B03, B05, B06, B07, B10
[short] B00 native portrait reused unchanged
[short] B01 native portrait reused unchanged
[short] B04 native portrait reused unchanged
[short] B08 native portrait reused unchanged
[short] B09 native portrait reused unchanged
[short] B11 native portrait reused unchanged
[short] 6 beats · ~102.7s (1:42.7) OK
[short] dropped: B02, B03, B05, B06, B07, B10 · ends on the last beat (no endcard)
```

No ONDA-blocked beats. All retained beats reused native portrait without crop.

## 4. Compile

```
python3 runtime/scripts/compile.py \
  .../claude-liam-brutalist-skill-riff-short \
  --height 3840 \
  --out .../claude-liam-brutalist-skill-riff-short/exports/short

[art] compiled B00  VIDEO    15.5s  ← B00.mp4
[art] compiled B01  VIDEO    12.7s  ← B01.mp4
[art] compiled B04  VIDEO    21.0s  ← B04.mp4
[art] compiled B08  VIDEO    26.4s  ← B08.mp4
[art] compiled B09  VIDEO    19.1s  ← B09.mp4
[art] compiled B11  VIDEO     8.0s  ← B11.mp4
[art] motion histogram: graphic:6
[art] SKIN LINT: B00: palette=claude but the cold open is 'ClaudeComposerAsk916'
[art] SKIN LINT: B11: palette=claude but the outro is 'ClaudeTitleOutro916'
[art] build stamp → beat_sheet.json (6/6 filled)
[art] wrote .../claude-liam-brutalist-skill-riff-short.mp4  (102.7s ...)
[art] slots: 6/6 filled — B00:VIDEO B01:VIDEO B04:VIDEO B08:VIDEO B09:VIDEO B11:VIDEO
```

Skin lint warnings are inherited from parent vertical (palette vs. 916 pattern name convention) and are not blockers.

## 5. Duration check

```
ffprobe -v error -show_entries format=duration -of csv=p=0 ...
Container: 102.666667s  (<180.0 ✓)

ffprobe video stream: 102.666667s, 2160×3840
ffprobe audio stream: 102.666000s
```

All three duration readings (timeline, video stream, audio stream) < 180.0s. ✓

## 6. Frame review

Extracted 18 frames at beat-relative 15%, 50%, 85% for all 6 kept beats.
Frames stored in _qc/ with SHA-256 hashes recorded in VISUAL-REVIEW.json.

Visual inspection results:
- B00: ClaudeComposerAsk916 — portrait framing correct, text legible, Liam greeting present ✓
- B01: BrutalistHesitantWriter916 — post-correction text visible, contextTitle/brand labels correct ✓
- B04: FormACard916 — mechanism card, all lines legible, no overflow ✓
- B08: FormACard916 — design-tell card, quoted rule visible, both consequences rendered ✓
- B09: FormACard916 — verdict card, all four numbered rules visible ✓
- B11: ClaudeTitleOutro916 — dark bg, "The riff Skill." + @NikBearBrown correct ✓

No burned-in captions, no cropped text, no portrait overflow detected.

## 7. Gaps

- final_frame_check.py not present in isolated toolkit's runtime/scripts/qc/; ran manual frame extraction via ffmpeg instead.
- Gate V (ink-coverage at 50%/85% of each beat) not run — the script is in the main toolkit's runtime/qc, not accessible here. Frame inspection confirms legible content throughout.

## Conclusion

No blockers. No majors. Short is 102.7s (1:42.7), strictly under 180s. All 6 beats confirmed VIDEO with native portrait dimensions. Human review pending.
