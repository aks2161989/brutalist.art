# BUILD-PROMPT — The riff Skill (Portrait Companion)
**Episode:** claude-liam-brutalist-skill-riff-vertical
**Run ID:** 323e3dfe085b4cdb8f0ad3c6529bd878
**Date:** 2026-09-11
**Parent:** claude-liam-brutalist-skill-riff

---

Portrait companion. Build was driven by the same BUILD-PROMPT.md as the landscape aspect.

See parent: `../BUILD-PROMPT.md`

Portrait-specific notes:
- Compiled with `python3 runtime/scripts/compile.py --height 3840 --out .../exports/vertical`
- FormBCard916 beats replaced with FormACard916 (anatomy/pipeline) to pass Gate V underfill check
- ClaudeVerdictArtifact916 and ClaudeComposerAsk916 beats replaced with FormACard916 where they caused edge-bleed or underfill
- BrutalistHesitantWriter916 patched with portrait-aware scale and lineSpacing 2.0 to achieve 65%+ FILL_MIN
- All paperwork (FACTCHECK.md, SHOTLIST.md, PROMPTS.md, SOURCES.md, CHECKS-REPORT.md, TYPECHECK.md, VISUAL-REVIEW.json) present in this directory
