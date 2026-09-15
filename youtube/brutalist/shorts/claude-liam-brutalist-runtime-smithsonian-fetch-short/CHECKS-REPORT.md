# Checks Report — Brutalist Utility: smithsonian_fetch.py — Short

run_id: 7d5225769ced4a06a72051a66def374b  
date: 2026-09-14  
aspect: 9:16 Short

## Gate V — final_frame_check.py

```
python3 runtime/qc/final_frame_check.py \
  <reel> \
  --mp4 <reel>/exports/short/claude-liam-brutalist-runtime-smithsonian-fetch-short.mp4 \
  --sheet <reel>/beat_sheet.json
```

Result: frames=12 BLOCKER=0 MAJOR=0

## Container verification (ffprobe)

- Container duration: 110.250000s
- Video stream: h264, 2160×3840, 110.250000s
- Audio stream: aac, 110.250000s
- All three durations strictly < 180.0s ✓

## SHA256

- video: 7bcb09584bd7bd108b2795fdfdd07404236b9b5fa87c71f14eeaf217650c3122
- beat_sheet: fe239109466b4b1ab0338054497a42896b8b3967eeffea160ca451c0d2221a65
- contact_sheet: 73a338bdc8a163e53066e2c97d069d040edeef6a5125fba79fd9fbcaa689b98a

## Beat compile summary

6/6 beats filled VIDEO. No slates. Native portrait reuse from vertical/media/ (all 6 beats confirmed 2160×3840 before copy). Skin lint warnings (ClaudeComposerAsk916, ClaudeTitleOutroHAI916 vs palette=claude) are expected — they are the correct HAI-channel portrait compositions.

## Cut plan validation

Planned duration: 110.25s. Measured: 110.25s. Consistent ✓

## Gaps / limitations

- No per-frame PNG files extracted separately from contact_sheet — Gate V passed with beat-relative sampling (50%/85% of each beat).
- Human review of contact_sheet.png and final viewing pending.
