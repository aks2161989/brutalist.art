# The riff Skill
**Episode:** claude-liam-brutalist-skill-riff  
**Run ID:** 6bdc7e3501b243bca58d7f9757d9597d  
**Date:** 2026-09-12  
**Channel:** @HumanitariansAI  
**Persona:** Liam, in for Bear  
**Voice:** Kokoro am_onyx  

---

AI Explainer (skill-teardown modifier) — explains the `skills/make/riff/` skill.

## Exports

| Aspect | File | Duration | Resolution | Gate V |
|---|---|---|---|---|
| Landscape | `exports/landscape/claude-liam-brutalist-skill-riff.mp4` | 234.5s | 3840×2160 | BLOCKER:0 MAJOR:0 |
| Portrait | `exports/vertical/claude-liam-brutalist-skill-riff-vertical.mp4` | 234.5s | 2160×3840 | BLOCKER:0 MAJOR:0 |

## Beat summary (12 beats)

| Beat | Scene | Description |
|---|---|---|
| B00 | ClaudeComposerAsk | Cold open |
| B01 | BrutalistHesitantWriter | BLUF — "riff generates opinions" corrects to "observations" |
| B02 | SkillTeardownAnatomy | Folder tree anatomy |
| B03 | SkillTeardownPipeline | 4-phase pipeline |
| B04 | SkillTeardownMechanism | Mechanism 1 |
| B05 | ClaudeCodeBeat | Self-demo: ./art scenes output |
| B06 | SkillTeardownMechanism | Mechanism 2 |
| B07 | SkillTeardownMechanism | Mechanism 3 |
| B08 | SkillTeardownMechanism | Design tell |
| B09 | ClaudeVerdictArtifact | Verdict |
| B10 | ClaudeComposerAsk | Your Turn |
| B11 | ClaudeTitleOutro | Outro — Liam, in for Bear. |

## Paperwork

Both aspect directories contain: FACTCHECK.md, SOURCES.md, SHOTLIST.md, PROMPTS.md,
BUILD-PROMPT.md, CHECKS-REPORT.md, TYPECHECK.md, VISUAL-REVIEW.json.

## Fix applied (run 6bdc7e35)

Vertical B10 (YOUR_TURN) was corrected from `FormACard916` → `ClaudeComposerAsk916` (HANDOFF LAW).
`ClaudeComposerAsk.tsx` segment div received `right: PAD_X` to prevent portrait right-edge overflow.
B10 re-rendered; vertical recompiled (234.5s, 2160×3840); Gate V: BLOCKER:0 MAJOR:0.
Landscape render is unchanged from prior run.

## Next step

**Human viewing and editing by Bear is required before any publication.**  
Gate V passed (AI frame review); Bear's sign-off is the final gate.

Output paths:
- `exports/landscape/claude-liam-brutalist-skill-riff.mp4` — 3840×2160, 234.5s
- `exports/vertical/claude-liam-brutalist-skill-riff-vertical.mp4` — 2160×3840, 234.5s
