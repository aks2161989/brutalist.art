# Brutalist Utility: pantry.py

**Playlist:** Brutalist  
**Episode:** 51 (pending channel assignment)  
**run_id:** `fe9516e11ca34baf8eca2990dd34a561`  
**Date:** 2026-09-14  
**Presenter:** Liam (in for Bear) · Kokoro am_onyx voice  
**Channel:** @HumanitariansAI

## Exports

| Aspect | File | Duration | SHA-256 |
|--------|------|----------|---------|
| Landscape | `exports/landscape/claude-liam-brutalist-runtime-pantry.mp4` | 184.708s | `56cacb0fba30574382ec28269978e4d6373e36c420839ed56409fc983cf28fb3` |
| Portrait | `exports/vertical/claude-liam-brutalist-runtime-pantry-vertical.mp4` | 184.708s | `912b1076d47765d9a51d7af44cafe3a3e629957687080a212fb0d81a3a5df845` |

## Source

- **Script:** `runtime/scripts/pantry.py`
- **SHA-256:** `5b059be171601690a436487ba1eb1d0ebefd58d4d4b0b796e971a427e201ba35`

## Beat Structure

12 beats (B00–B11):

| Beat | Scene | Topic |
|------|-------|-------|
| B00 | ClaudeComposerAsk | Cold open — what pantry.py does |
| B01 | BrutalistHesitantWriter | BLUF — stands between raw media and film |
| B02 | SkillTeardownMechanism | The Pantry Law — raw media → pantry/ |
| B03 | ClaudeCodeBeat | BID_RE prefix regex |
| B04 | SkillTeardownMechanism | Intake steps: detect, process, place |
| B05 | ClaudeCodeBeat | Image intake — DOCUMENT vs STILL |
| B06 | ClaudeCodeBeat | Video intake — portrait detection, 916 tag |
| B07 | SkillTeardownMechanism | Sidecar .source.txt provenance |
| B08 | ClaudeCodeBeat | Hard stops — missing pantry, invalid BID |
| B09 | ClaudeVerdictArtifact | Verdict + 6 artifact lines |
| B10 | ClaudeComposerAsk | Your Turn — Claude audit prompt |
| B11 | ClaudeTitleOutro | Sign-off: Liam, in for Bear |

## QC

- Landscape Gate V: BLOCKER 0 · MAJOR 0 (24 frames sampled)
- Portrait Gate V: BLOCKER 0 · MAJOR 0 (24 frames sampled)

See `VISUAL-REVIEW.json`, `CHECKS-REPORT.md`, `TYPECHECK.md` for full records.  
Portrait: `vertical/VISUAL-REVIEW.json`, `vertical/CHECKS-REPORT.md`, `vertical/TYPECHECK.md`.

**Next step: Bear's viewing and editing.** These files are local 4K renders; no upload or publication has occurred.

## Portrait Notes

Portrait beats B01–B08 rendered with portrait-native 916 compositions added to Root.tsx
this session (`ClaudeCodeBeat916`, `SkillTeardownMechanism916`). B01 lineSpacing set to
8.2 (derived empirically) to achieve ≥55% fill in the 9:16 safe area. Banner omitted
from B01 portrait to prevent top edge-bleed at portrait scale.
