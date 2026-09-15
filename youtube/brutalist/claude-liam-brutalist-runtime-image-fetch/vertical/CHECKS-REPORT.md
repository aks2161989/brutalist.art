# CHECKS-REPORT — Brutalist Utility: image_fetch.py (portrait)

## Run
- run_id: e3271f85256140a6a524dc9dcf74f13e
- at: 2026-09-14
- aspect: portrait 2160×3840
- note: Attempt 7. B09 outro fixed: ClaudeTitleOutro916 (@NikBearBrown) replaced with ClaudeTitleOutroHAI916 (@HumanitariansAI). All other beats unchanged.

## Gate V
- Frames sampled: 20
- BLOCKER: 0
- MAJOR: 0
- Status: PASS ✓
- Gate V run: `python3 qc/final_frame_check.py vertical/ --mp4 exports/vertical/claude-liam-brutalist-runtime-image-fetch-vertical.mp4`

## Beat coverage
| Beat | Scene | Duration | Status |
|---|---|---|---|
| B00 | ClaudeComposerAsk916 | 10.8s | VIDEO |
| B01 | BrutalistHesitantWriter916 | 14.0s | VIDEO |
| B02 | BrutalistTerminalOpen916 | 22.1s | VIDEO |
| B03 | BrutalistAdaptCLI916 | 19.6s | VIDEO |
| B04 | BrutalistAdaptCLI916 | 18.3s | VIDEO |
| B05 | BrutalistAdaptCLI916 | 21.3s | VIDEO |
| B06 | ClaudeVerdictArtifact916 | 20.2s | VIDEO |
| B07 | ClaudeVerdictArtifact916 | 19.6s | VIDEO |
| B08 | ClaudeComposerAsk916 | 18.2s | VIDEO |
| B09 | ClaudeTitleOutroHAI916 | 8.0s | VIDEO |

**Total: 172.2s — 10/10 filled — 0 slates**

## Fixes applied (original build 2026-09-10)
- BrutalistHesitantWriter916: portrait-aware scale patch applied (min(w/1080,h/1920)) so text fills portrait safe area
- B05: BrutalistAdaptCLI916 for reliable portrait fill
- All BLUF text at fontSize:155, lineSpacing:2.8

## Outro fix (this invocation)
- B09 now uses ClaudeTitleOutroHAI916 — hardcoded @HumanitariansAI, ink-extent markers for Gate V fill, light polarity
- Components ClaudeTitleOutroHAI.tsx and ClaudeTitleOutroHAI916.tsx created in isolated toolkit this invocation
- SKIN LINT warnings (cold-open/outro law) expected for portrait variant names

## Audio
- Engine: Kokoro am_onyx (shared from landscape mp3/ folder)
- No ElevenLabs, no API keys used

## Safety
- No captions/subtitles
- No publication
- No credentials accessed
