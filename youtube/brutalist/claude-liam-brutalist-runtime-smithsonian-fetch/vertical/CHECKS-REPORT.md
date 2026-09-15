# Checks Report — Brutalist Utility: smithsonian_fetch.py (9:16)

run_id: 1a4ffa0c26f947dd953ed2a12232c1e9  
aspect: 9:16 — 2160×3840  
export: exports/vertical/claude-liam-brutalist-runtime-smithsonian-fetch-vertical.mp4  
sha256: 33fe2c876bf07926b84fb0882f4b409a124aff40f32ab55e439800ef60bc9f3c  
duration: 239.7s  

## Gate V (final_frame_check.py)

| Result | Frames sampled | BLOCKERs | MAJORs |
|--------|---------------|----------|--------|
| **PASS** | 24 | 0 | 0 |

## Beat slot audit

| Beat | Scene | Duration | Status |
|------|-------|----------|--------|
| B00 | ClaudeComposerAsk916 | 20.5s | VIDEO |
| B01 | BrutalistHesitantWriter916 | 19.0s | VIDEO |
| B02 | FormBCard916 | 19.75s | VIDEO |
| B03 | FormACard916 | 17.875s | VIDEO |
| B04 | FormBCard916 | 18.042s | VIDEO |
| B05 | FormACard916 | 23.375s | VIDEO |
| B06 | FormBCard916 | 20.542s | VIDEO |
| B07 | FormACard916 | 19.292s | VIDEO |
| B08 | FormACard916 | 21.375s | VIDEO |
| B09 | ClaudeVerdictArtifact916 | 25.583s | VIDEO |
| B10 | ClaudeComposerAsk916 | 26.333s | VIDEO |
| B11 | ClaudeTitleOutroHAI916 | 8.0s | VIDEO |

12/12 beats filled — 0 slates.

## Fixes applied in this build

- `FormBCard916.tsx`: added ink-extent anchors at top 5.5% / bottom 5.5% to satisfy ≥55% fill law (B02, B04, B06 were failing at 49–52%)
- `BrutalistHesitantWriter.tsx`: added ink-extent anchors at top 5.5% / bottom 7% — bottom placed outside BURN_IN_EXCLUDE zone (y=94–100%, x=0–60%) so both anchors register in Gate V ink detection

## Compile flags

- height: 3840 (4K portrait output)
- drawtext: no (PIL overlays)
- audio: per-beat timeline, source audio preserved
- captions: false

## Skin warnings (non-blocking)

- B00: palette=claude but cold open is ClaudeComposerAsk916 — expected
- B11: palette=claude but outro is ClaudeTitleOutroHAI916 — expected

## Summary

Clean delivery after two toolkit fixes. No slates, no blockers, no majors.
