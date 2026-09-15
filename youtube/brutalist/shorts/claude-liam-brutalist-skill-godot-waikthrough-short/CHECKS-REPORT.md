# Checks Report — The godot-waikthrough Skill — Short

run_id: b5f2c3a4defc4e56aa6012dc9e7f7ccd
Built: 2026-09-12

## Duration

| Measure | Value | Limit | Status |
|---|---|---|---|
| Measured timeline | 158.0s | < 180.0s | PASS |
| Container duration | 158.04s | < 180.0s | PASS |
| Video stream | 158.04s | < 180.0s | PASS |
| Audio stream | 158.04s | < 180.0s | PASS |

## Dimensions

| Measure | Value | Status |
|---|---|---|
| Width × Height | 2160 × 3840 | PASS |
| Aspect ratio | 9:16 | PASS |
| Source media | Native portrait (no crop) | PASS |

## Beat Fill

| Beat | Duration | Source | Status |
|---|---|---|---|
| B00 | 16.2s | media/B00.mp4 (native portrait) | VIDEO |
| B01 | 15.6s | media/B01.mp4 (native portrait) | VIDEO |
| B02 | 22.7s | media/B02.mp4 (native portrait) | VIDEO |
| B06 | 20.5s | media/B06.mp4 (native portrait) | VIDEO |
| B08 | 21.7s | media/B08.mp4 (native portrait) | VIDEO |
| B10 | 20.5s | media/B10.mp4 (native portrait) | VIDEO |
| B11 | 33.8s | media/B11.mp4 (native portrait) | VIDEO |
| B12 | 7.0s | media/B12.mp4 (native portrait) | VIDEO |

8/8 slots filled. 0 slates.

## Dropped Beats

| Beat | Reason |
|---|---|
| B03 | Anatomy/folder structure — belongs in 16:9 long |
| B04 | Phase 1 detail — worked example for long film |
| B05 | Phase 2 capture terminal — implementation detail |
| B07 | Walker mode bookend ordering — advanced detail |
| B09 | Falsifiability self-demo — B08 covers honesty contract; B10 names the limitation |

## Content Checks

| Check | Status | Note |
|---|---|---|
| Liam introduction | PASS | B00: "Annyeong — this is Liam, in for Bear" |
| Liam sign-off | PASS | B11 narration ends "Liam, in for Bear." B12 @NikBearBrown |
| No captions | PASS | captions: false |
| No URL invented | PASS | No fabricated links |
| No paid API | PASS | Kokoro am_onyx local only |
| No publish/upload | PASS | Render only |
| Source audio preserved | PASS | Per-beat timeline from vertical source |

## Visual Review

All 24 extracted frames inspected (beat-relative 15%/50%/85% for each kept beat).

- Portrait framing: PASS — all native 2160×3840, no cropping
- Legibility: PASS — all text readable at safe-area margins
- Safe-area coverage: PASS — content present in upper and lower thirds across all beats
- Coherence: PASS — transitions clean, no dangling references

## Skin Lint

Two SKIN LINT warnings inherited from vertical source beat sheet (documented in vertical/beat_sheet.json build.skin_warnings):
- B00: ClaudeComposerAsk916 instead of ClaudeComposerAsk (portrait variant — by design)
- B12: ClaudeTitleOutro916 instead of ClaudeTitleOutro (portrait variant — by design)

These are not blockers. The 916 variants are the correct portrait compositions per feedback_skillteardown_pipeline_portrait.md and OUTRO-LOCK.md.

## Output

```
exports/short/claude-liam-brutalist-skill-godot-waikthrough-short.mp4
SHA-256: b21995abfff4b7341cca60f95b88523ba44679f4f5a41d49afebec5cb36fdbc8
```
