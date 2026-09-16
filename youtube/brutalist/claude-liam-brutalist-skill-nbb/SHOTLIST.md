# SHOTLIST — The nbb Skill

Twelve beats, cream ClaudeBrand ground, terracotta accent. Landscape
3840×2160, portrait companion 2160×3840 (same beats, native reflow).

| # | ID  | Act            | Scene                          | Duration | What lands |
|---|-----|----------------|--------------------------------|---------:|-----------|
| 1 | B00 | ASK            | ClaudeComposerAsk              | 16.28s   | Hola-Liam; ask about nbb; 3 result lines |
| 2 | B01 | BLUF           | BrutalistHesitantWriter        | 19.35s   | "rewrites → scaffolds" correction |
| 3 | B02 | FRAMEWORK      | SkillTeardownAnatomy           | 33.60s   | 5 files on disk; source-never-modified callout |
| 4 | B03 | FRAMEWORK      | SkillTeardownPipeline          | 34.73s   | 5 phases: SCAFFOLD → REWRITE → LLM → OUTRO → VERIFY |
| 5 | B04 | MECHANISM      | SkillTeardownMechanism         | 31.74s   | Source-never-modified; refuse-without-force |
| 6 | B05 | MECHANISM      | SkillTeardownMechanism         | 35.80s   | Deterministic half vs creative half |
| 7 | B06 | MECHANISM      | SkillTeardownMechanism         | 29.23s   | LLM exercise is second-to-last |
| 8 | B07 | MECHANISM      | SkillTeardownMechanism         | 28.84s   | IN-FOR-BEAR LAW; Kokoro am_onyx only |
| 9 | B08 | FALSIFIABILITY | SkillTeardownMechanism         | 38.36s   | Batch scaffolds shells; _variant_todo is a checklist |
|10 | B09 | VERDICT        | ClaudeVerdictArtifact          | 34.22s   | 6-line teardown-palette artifact card |
|11 | B10 | YOUR_TURN      | ClaudeComposerAsk              | 40.11s   | Paste-ready DRY-RUN prompt; 3-check rubric |
|12 | B11 | OUTRO          | ClaudeTitleOutro               | 3.52s    | "The nbb Skill." · @NikBearBrown · mascot |

- Total measured runtime: ~346s = **~5m 46s**.
- Every beat carries `shot.show` events; nothing punts.
- Composer chips: `@HumanitariansAI` on B00 + B10; outro handle
  `@NikBearBrown` on B11 (hardcoded per OUTRO-LOCK.md).
- The teardown-palette artifact card is used only at the verdict per the
  Anatomy → Pipeline → Mechanism → Falsifiability → Verdict rhythm.
