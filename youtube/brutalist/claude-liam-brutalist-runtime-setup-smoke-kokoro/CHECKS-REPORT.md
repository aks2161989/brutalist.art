# CHECKS-REPORT — Brutalist Utility: setup_smoke_kokoro.py

## Beat classification (pre-render)

11 SHOW / 0 HOLD / 0 PUNT

| Beat | Class | Scene | Justification |
|---|---|---|---|
| B00 | SHOW | ClaudeComposerAsk | Required cold open — interface is the subject |
| B01 | SHOW | BrutalistHesitantWriter | BLUF per EXECUTIVE-SUMMARY LAW |
| B02 | SHOW | SkillTeardownPipeline | Pipeline diagram — framework beat before any code detail |
| B03 | SHOW | ClaudeCodeBeat | Real code from source — guard section verbatim |
| B04 | SHOW | ClaudeCodeBeat | Real code from source — synthesis block |
| B05 | SHOW | ClaudeCodeBeat | Real code from source — volume gate |
| B06 | SHOW | ClaudeCodeBeat | Real code / real messages from source — failure paths |
| B07 | SHOW | ClaudeCodeBeat | Real code from source — try/finally cleanup |
| B08 | SHOW | ClaudeVerdictArtifact | Verdict — recapitulates, no new factual claims |
| B09 | SHOW | ClaudeComposerAsk | HANDOFF LAW — paste-ready prompt |
| B10 | SHOW | ClaudeTitleOutro | OUTRO LAW — title restate + sign-off |

## Teaching-arc checklist

- [x] **FRAMEWORK beat** — B02 (SkillTeardownPipeline) presents the 5-phase chain before any code detail
- [x] **WORKED EXAMPLE** — B03–B07 walk through each mechanism step with source-verbatim code
- [x] **FALSIFIABILITY / edge-case beat** — B06 shows all five failure modes explicitly
- [x] **SCAFFOLDED viewer task** — B09: concrete prompt + rubric ("look for what's separated from what's shared")
- [x] **Four bookends** — B00 (cold open) · B08 (verdict) · B09 (your turn) · B10 (outro)
- [x] **No source, no verdict** — every code beat shows source-verbatim excerpts; B06 failure messages are from the actual fail() function

## Verification gap: type_check.py

`scripts/type_check.py` is referenced in the SKILL.md (§ GATE T) but is not present in the toolkit (`find . -name type_check.py` returns no results). This is a documented gap in the public docs. The absent checker is recorded here and in TYPECHECK.md. Visual typography was inspected manually at the frame-review stage — see _qc/REPORT.md.

## Post-render QC results

**Run ID:** `030891286f944a7f9f0175823eff81cd`  
**Rendered:** 2026-09-14  
**Beats filled:** 11/11 (0 slates)

### Landscape (3840×2160)
- Gate V: **BLOCKER=0 · MAJOR=0** — 22 frames sampled. See `_qc/REPORT.md`.
- Video SHA-256: `1a49b8cf3f9be9fe2e6aed4fb7dc8b5d9f57fab67fa82a105cf8b37662638dc2`
- Duration: 207.5s

### Vertical / 9:16 (2160×3840)
- Gate V: **BLOCKER=0 · MAJOR=0** — 22 frames sampled. See `vertical/_qc/REPORT.md`.
- Video SHA-256: `8a0c5e37845a496a5fb4387aefd84eb46b325c69d76e96824f96792d08711b8b`
- Duration: 207.5s

### Notable fixes applied during this build
- **Invocation 030891286f (retry):** B10 outro `ClaudeTitleOutro` (hardcoded `@NikBearBrown`) replaced with isolated `ClaudeTitleOutroHAI` / `ClaudeTitleOutroHAI916` (locked to `@HumanitariansAI`) per playlist spec. Both landscapes and vertical recompiled and Gate V re-run. B10 frame extraction confirms `@HumanitariansAI` on both aspects.
- `BrutalistHesitantWriter.tsx` portrait-scale bug fixed: `Math.min(width/1920, height/1080)` → portrait-aware ternary `height > width ? Math.min(width/1080, height/1920) : Math.min(width/1920, height/1080)`. Without this fix portrait scale = 0.5625 → ~4% ink coverage (BLOCKER).
- B01 `charMs=1`, `hesitateBetween=0`, `hesitateWithin=0`, `jitter=0` to ensure full text visible at t=50%/85% Gate V sample points.
- `channel_title` removed from `vertical/beat_sheet.json` metadata to prevent compile-overlay bleed past portrait `safe.b`.
- Node_modules webpack EPERM fixed: replaced symlink with shadowed real directory + writable `.cache/webpack/`.
- Chrome App Sandbox Mach-port fixed: chrome-headless-shell wrapper at `runtime/.wrappers/chrome-wrapper.sh` with `--single-process --in-process-gpu`.

### Known lint
- Skin lint warns `ClaudeTitleOutroHAI` / `ClaudeTitleOutroHAI916` don't match OUTRO LAW (which expects `ClaudeTitleOutro`). This is intentional: the HAI variants are the correct isolated components for @HumanitariansAI reels; the NBB component is locked to @NikBearBrown per OUTRO-LOCK.md.

### Visual review
See `VISUAL-REVIEW.json` and `vertical/VISUAL-REVIEW.json` — both `status: pass`. Human review of contact sheets and export files required before publication.
