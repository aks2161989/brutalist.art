# Checks Report — Brutalist Utility: smithsonian_fetch.py (16:9)

run_id: 1a4ffa0c26f947dd953ed2a12232c1e9  
aspect: 16:9 — 3840×2160  
export: exports/landscape/claude-liam-brutalist-runtime-smithsonian-fetch.mp4  
sha256: 4b02ca5fa76fc1ad74703ddab7c8b72d3a2eb6263d18b1fa9bd437d58dac1867  
duration: 239.7s  

## Gate V (final_frame_check.py)

| Result | Frames sampled | BLOCKERs | MAJORs |
|--------|---------------|----------|--------|
| **PASS** | 24 | 0 | 0 |

## Beat slot audit

| Beat | Scene | Duration | Status |
|------|-------|----------|--------|
| B00 | ClaudeComposerAsk | 20.5s | VIDEO |
| B01 | BrutalistHesitantWriter | 19.0s | VIDEO |
| B02 | SkillTeardownPipeline | 19.75s | VIDEO |
| B03 | SkillTeardownMechanism | 17.875s | VIDEO |
| B04 | SkillTeardownMechanism | 18.042s | VIDEO |
| B05 | ClaudeCodeBeat | 23.375s | VIDEO |
| B06 | SkillTeardownMechanism | 20.542s | VIDEO |
| B07 | SkillTeardownMechanism | 19.292s | VIDEO |
| B08 | ClaudeCodeBeat | 21.375s | VIDEO |
| B09 | SkillTeardownMechanism | 25.583s | VIDEO |
| B10 | ClaudeComposerAsk | 26.333s | VIDEO |
| B11 | ClaudeTitleOutroHAI | 8.0s | VIDEO |

12/12 beats filled — 0 slates.

## Compile flags

- height: 2160 (4K output)
- drawtext: no (PIL overlays)
- audio: per-beat timeline, source audio preserved
- captions: false

## Skin warnings (non-blocking)

- B11: palette=claude but outro is ClaudeTitleOutroHAI — expected; this is the @HumanitariansAI channel

## Summary

Clean delivery. No slates, no blockers, no majors.
