# CHECKS REPORT — Brutalist Utility: pantry.py

**run_id:** fe9516e11ca34baf8eca2990dd34a561  
**date:** 2026-09-14  
**aspect:** landscape (3840×2160)  
**duration:** 184.708s  
**beats:** 12 (B00–B11)  
**output:** exports/landscape/claude-liam-brutalist-runtime-pantry.mp4  
**video_sha256:** 56cacb0fba30574382ec28269978e4d6373e36c420839ed56409fc983cf28fb3

## Compile run

```
python3 runtime/scripts/compile.py <reel> \
  --height 2160 \
  --out <reel>/exports/landscape
```

Output: 12/12 filled — B00:VIDEO B01:VIDEO B02:VIDEO B03:VIDEO B04:VIDEO
B05:VIDEO B06:VIDEO B07:VIDEO B08:VIDEO B09:VIDEO B10:VIDEO B11:VIDEO  
Motion histogram: line-reveal:4 stagger-in:3 type-on:2 type-on correcting:1 left-to-right-reveal:1 fade-in:1  
Gate V ran inside compile.py: BLOCKER=0 MAJOR=0

## Gate V — Visual QC

```
Frames sampled: 24  ·  BLOCKER: 0  ·  MAJOR: 0

Clean — no BLOCKER/MAJOR defects. ✓
```

## Frame inspection (Read tool, actual images)

| Timestamp | Beat | Scene | Finding |
|-----------|------|-------|---------|
| t=5s | B00 | ClaudeComposerAsk | Bula Liam greeting, @HumanitariansAI chip, correct command, 3 output lines. Clean. |
| t=30s | B02 | SkillTeardownMechanism | UTILITY · DESIGN LAW eyebrow, Pantry Law heading, quote card, IDEMPOTENT verdict, sparkLine. Fills safe area. |
| t=92s | B06 | ClaudeCodeBeat | Video-path code: portrait detection, b-roll audio stripping, duration check. Legible at 3840×2160. |
| t=157s | B09 | ClaudeVerdictArtifact | "The naming law works." 6 verdict lines, terracotta numbering. Clean layout. |
| last | B11 | ClaudeTitleOutro | "Brutalist Utility: pantry.py." @NikBearBrown bear mascot on charcoal. OUTRO-LOCK compliant. |

## Beat Inventory

| Beat | Scene | Duration | Status |
|------|-------|----------|--------|
| B00 | ClaudeComposerAsk | 13.29s | VIDEO |
| B01 | BrutalistHesitantWriter | 10.75s | VIDEO |
| B02 | SkillTeardownMechanism | 18.375s | VIDEO |
| B03 | ClaudeCodeBeat | 14.79s | VIDEO |
| B04 | SkillTeardownPipeline | 15.125s | VIDEO |
| B05 | ClaudeCodeBeat | 16.708s | VIDEO |
| B06 | ClaudeCodeBeat | 18.083s | VIDEO |
| B07 | SkillTeardownMechanism | 18.417s | VIDEO |
| B08 | ClaudeCodeBeat | 17.333s | VIDEO |
| B09 | ClaudeVerdictArtifact | 16.208s | VIDEO |
| B10 | ClaudeComposerAsk | 17.625s | VIDEO |
| B11 | ClaudeTitleOutro | 8.0s | VIDEO |

## Checklist

- [x] No captions / burned-in transcript
- [x] No edge bleed
- [x] No unresolved slates
- [x] @HumanitariansAI handle present (B00, B10)
- [x] Outro @NikBearBrown (OUTRO-LOCK.md)
- [x] Liam sign-off in B11 narration
- [x] Audio: per-beat timeline, source audio preserved
- [x] Video: h264, 3840×2160, aac, 184.708s
