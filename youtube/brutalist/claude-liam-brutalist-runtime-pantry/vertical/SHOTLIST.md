# SHOTLIST — Brutalist Utility: pantry.py
## run_id: 1df027e6acef4cf1ad6843ed3815ffb7

All beats are native Remotion compositions. No human-supplied media required.
No slates. Classification: SHOW for every beat.

| Beat | Classification | Scene | Props summary | Duration est. |
|---|---|---|---|---|
| B00 | SHOW | ClaudeComposerAsk | greeting "Bula, Liam"; command types; 3 output lines | ~17s |
| B01 | SHOW | BrutalistHesitantWriter | "media"→"pantry", "optional"→"mandatory"; seed pantry-bluf-2026 | ~13s |
| B02 | SHOW | SkillTeardownMechanism | Pantry Law verbatim quote; IDEMPOTENT pill | ~22s |
| B03 | SHOW | ClaudeCodeBeat | BID_RE pattern + valid/invalid examples | ~17s |
| B04 | SHOW | SkillTeardownPipeline | INPUT→Detect→Normalize(accent)→Slot→OUTPUT | ~18s |
| B05 | SHOW | ClaudeCodeBeat | DOCUMENT crop, RGB convert, width warning | ~20s |
| B06 | SHOW | ClaudeCodeBeat | portrait suffix, report audio, slow-mo warn | ~20s |
| B07 | SHOW | SkillTeardownMechanism | sidecar law; Higgsfield detection quote | ~21s |
| B08 | SHOW | ClaudeCodeBeat | sys.exit hard stop; logged skips | ~22s |
| B09 | SHOW | ClaudeVerdictArtifact | 4-line verdict: idempotency, provenance, 2 bites | ~21s |
| B10 | SHOW | ClaudeComposerAsk | "Your turn." prompt; intake audit command | ~25s |
| B11 | SHOW | ClaudeTitleOutro | slug-seeded mascot + @NikBearBrown | ~8s |

**Total estimated: ~224s ≈ 3m 44s**

## SHOW / HOLD / CARD classification

- 12 SHOW beats
- 0 HOLD beats
- 0 CARD beats
- 0 PUNT-flagged beats

## Teaching arc

- FRAMEWORK: B02 (The Pantry Law — core design principle before examples) ✓
- WORKED EXAMPLE: B03 (prefix rule) + B04 (pipeline) + B05 (image path) + B06 (video path) ✓
- FALSIFIABILITY: B08 (what stops the run — real failure modes) ✓
- SCAFFOLDED TASK: B10 (paste-ready audit prompt with explicit success criteria) ✓
- BOOKENDS: B00, B09, B10, B11 ✓
- NO-SOURCE-NO-VERDICT: All code beats show actual pantry.py lines; verdict recapitulates ✓

## ILLUSTRATE LAW check

- ClaudeComposerAsk: B00 (cold open — UI is the subject) ✓, B10 (handoff — UI is the subject) ✓
- Inner beats B02-B09: concept illustrations (SkillTeardownMechanism, SkillTeardownPipeline, ClaudeCodeBeat, ClaudeVerdictArtifact) — no wallpaper ✓
- No two consecutive beats share the same visual scheme ✓

## Portrait (9:16) notes

- B04: SkillTeardownPipeline (landscape) → SkillTeardownMechanism (portrait) per portrait feedback
- B01: lineSpacing 2.5 for portrait BLUF coverage
- B00, B10: ClaudeComposerAsk916
- B09: ClaudeVerdictArtifact916
- B11: ClaudeTitleOutro916
- No channel_title in portrait metadata (bleed fix)
