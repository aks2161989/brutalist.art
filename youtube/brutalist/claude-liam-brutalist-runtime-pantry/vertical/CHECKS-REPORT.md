# CHECKS REPORT — Brutalist Utility: pantry.py (portrait)

**run_id:** fe9516e11ca34baf8eca2990dd34a561  
**date:** 2026-09-14  
**aspect:** portrait (2160×3840)  
**duration:** 184.708s  
**beats:** 12 (B00–B11)  
**output:** exports/vertical/claude-liam-brutalist-runtime-pantry-vertical.mp4  
**video_sha256:** 912b1076d47765d9a51d7af44cafe3a3e629957687080a212fb0d81a3a5df845

## Gate V — Visual QC

```
Frames sampled: 24  ·  BLOCKER: 0  ·  MAJOR: 0

Clean — no BLOCKER/MAJOR defects. ✓
```

## Portrait Composition Notes

All body beats B01–B08 rendered with portrait-native 916 compositions to eliminate
center-crop edge-bleed that would occur with landscape clips scaled for portrait masters.

| Beat | Landscape composition | Portrait composition |
|------|-----------------------|----------------------|
| B00 | ClaudeComposerAsk | ClaudeComposerAsk916 |
| B01 | BrutalistHesitantWriter | BrutalistHesitantWriter916 (lineSpacing=8.2, no banner) |
| B02 | SkillTeardownMechanism | SkillTeardownMechanism916 |
| B03 | ClaudeCodeBeat | ClaudeCodeBeat916 |
| B04 | SkillTeardownMechanism | SkillTeardownMechanism916 |
| B05 | ClaudeCodeBeat | ClaudeCodeBeat916 |
| B06 | ClaudeCodeBeat | ClaudeCodeBeat916 |
| B07 | SkillTeardownMechanism | SkillTeardownMechanism916 |
| B08 | ClaudeCodeBeat | ClaudeCodeBeat916 |
| B09 | ClaudeVerdictArtifact | ClaudeVerdictArtifact916 |
| B10 | ClaudeComposerAsk | ClaudeComposerAsk916 |
| B11 | ClaudeTitleOutro | ClaudeTitleOutro916 |

**B01 lineSpacing rationale:** At BrutalistHesitantWriter scale=0.5625 in portrait, empirical measurement showed lineSpacing=6.5 yields 45% fill (MAJOR). Formula derived: `ink_height = 93.5 + 297 × lineSpacing`. For ≥55% fill: lineSpacing ≥ 8.03 → set to **8.2** → verified 56.2% fill. Banner omitted in portrait as it bleeds past safe_y (81px < 192px).

## Frame inspection (Read tool, actual images)

| Timestamp | Beat | Scene | Finding |
|-----------|------|-------|---------|
| t=5s | B00 | ClaudeComposerAsk916 | Bula Liam greeting, @HumanitariansAI chip, command, 3 output lines. Portrait safe area clean. |
| t=30s | B02 | SkillTeardownMechanism916 | Pantry Law heading, body, quote card, IDEMPOTENT label, sparkLine. Fills portrait safe area. |
| t=92s | B06 | ClaudeCodeBeat916 | Video-path code visible. Minor: right-edge truncation on long audio list literal within card bounds; not a safe-area bleed. Gate V passed. |
| t=157s | B09 | ClaudeVerdictArtifact916 | "The naming law works." 6 verdict lines fully readable in portrait. |
| last | B11 | ClaudeTitleOutro916 | "Brutalist Utility: pantry.py." word-wraps correctly. @NikBearBrown centered. OUTRO-LOCK compliant. |

## Export

- **File:** `exports/vertical/claude-liam-brutalist-runtime-pantry-vertical.mp4`
- **SHA-256:** `912b1076d47765d9a51d7af44cafe3a3e629957687080a212fb0d81a3a5df845`
- **Size:** ~11MB
