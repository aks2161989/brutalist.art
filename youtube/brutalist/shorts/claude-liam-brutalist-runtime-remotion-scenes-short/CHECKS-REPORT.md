# CHECKS-REPORT — Brutalist Utility: remotion_scenes.py — Short

run_id: fc1776840f424323a7cd87f07c26ff53
Compiled: 2026-09-14

## Gate summary

| Gate | Result | Notes |
|---|---|---|
| Gate V (final_frame_check.py) | PASS — 0 blockers, 0 majors | 16 frames checked |
| Duration (container) | 128.958s — PASS | Strictly < 180s |
| Duration (video stream) | 128.917s — PASS | Strictly < 180s |
| Duration (audio stream) | 128.958s — PASS | Strictly < 180s |
| Slates | 0 — PASS | All 8 beats filled |
| Aspect ratio | 2160×3840 (9:16) — PASS | Native portrait, no crop |
| Captions | false — PASS | No burned-in captions |
| short_validation | ready, 0 errors | |

## Skin lint warnings (inherited, not defects)

- B00: `ClaudeComposerAsk916` — expected 916-variant for vertical/short; COLD OPEN LAW is a landscape-film rule
- B11: `ClaudeTitleOutro916` — expected 916-variant; same note. Shows @NikBearBrown (pre-existing in parent vertical, flagged as expected skin lint in parent VISUAL-REVIEW, not a new defect introduced by this Short)

## Beat build status

| Beat | Status | Duration |
|---|---|---|
| B00 | VIDEO | 16.3s |
| B01 | VIDEO | 12.8s |
| B02 | VIDEO | 21.8s |
| B03 | VIDEO | 13.9s |
| B06 | VIDEO | 17.8s |
| B08 | VIDEO | 23.0s |
| B09 | VIDEO | 17.5s |
| B11 | VIDEO | 6.0s |

## Frame observations

- t5s (B00): Cream portrait, "Sawadee, Liam" greeting, composer UI visible, @HumanitariansAI label — legible, no edge bleed ✓
- t31s (B02): Mechanism card "Four steps, one safe pass.", body text visible in safe area ✓
- t62s (B03): Code card showing JSON shot block, monospace text legible ✓
- t100s (B08): Failure mode card with FAIL: description, quote block, RECOVERY pill — all visible ✓
- t120s (B09): Verdict artifact with 6 numbered lines — all visible ✓
- port_last (B11): Outro — title "Brutalist Utility: remotion_scenes.py." and @NikBearBrown (inherited) ✓
