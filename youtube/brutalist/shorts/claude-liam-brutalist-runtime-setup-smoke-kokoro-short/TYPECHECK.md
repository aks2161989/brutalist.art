# TYPECHECK — Brutalist Utility: setup_smoke_kokoro.py — Short

**Run ID:** `410f7e79dc5a4f6a84b220a3230b02d2`  
**Short export:** `exports/short/claude-liam-brutalist-runtime-setup-smoke-kokoro-short.mp4`

## Beat type verification

All retained beats use native portrait clips from the approved parent vertical. The 916 Remotion compositions were rendered during the parent build and verified there. This Short reuses those renders unchanged.

| Beat | Scene | Type | Status |
|---|---|---|---|
| B00 | ClaudeComposerAsk916 | REMOTION | Native portrait, reused |
| B01 | BrutalistHesitantWriter916 | REMOTION | Native portrait, reused |
| B06 | ClaudeCodeBeat916 | REMOTION | Native portrait, reused |
| B08 | ClaudeVerdictArtifact916 | REMOTION | Native portrait, reused |
| B09 | ClaudeComposerAsk916 | REMOTION | Native portrait, reused |
| B10 | ClaudeTitleOutroHAI916 | REMOTION | Native portrait, reused |

## Known skin lint

- B00: `palette=claude` but composition is `ClaudeComposerAsk916` — COLD OPEN LAW expects `ClaudeComposerAsk`. Intentional: the 916 portrait variant is required for native 9:16.
- B10: `palette=claude` but composition is `ClaudeTitleOutroHAI916` — OUTRO LAW expects `ClaudeTitleOutro`. Intentional: `ClaudeTitleOutroHAI916` is the correct HAI-locked component for @HumanitariansAI reels.

## Missing type_check.py

`scripts/type_check.py` is not present in the toolkit. Visual typography was verified by frame review at _qc/. No typography bleed or overflow detected on retained beats at Gate V sample points.
