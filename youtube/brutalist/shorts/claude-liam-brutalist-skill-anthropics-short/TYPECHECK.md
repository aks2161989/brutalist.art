# TYPECHECK.md — The anthropics Skill — Short

The legacy per-beat type checker is not part of the current runtime; this file
records the actual visual-typography review carried out on the compiled Short
instead of substituting a stale receipt.

## Coverage

Every kept beat had its 15% / 50% / 85% frame extracted and read with the
image-capable Read tool (see `CHECKS-REPORT.md` for the log). Every observation
below is grounded in the actual rendered pixels of the final 2160×3840 MP4
(SHA-256 `d26c2ffcba8d42cac113bc3fd7caa697e977b7909477313e2b05b0fd22c691cf`),
not in the beat sheet's declarative intent.

## Findings

| Beat | Composition | Face / weight | Legibility | Safe-area | Notes |
|------|-------------|---------------|------------|-----------|-------|
| B00 | ClaudeComposerAsk916 | poster serif title + mono composer body | high | inside | greeting "Hej, Liam", topic eyebrow, three result bullets all render distinct |
| B01 | BrutalistHesitantWriter916 | Garamond serif, weight 400 | high | inside | corrected verb ("beat") replaces "channel" without stacking; cursor visible at line end |
| B03 | SkillTeardownPipeline916 | serif title, mono chips | high | inside | five nodes fit vertically; --capability chip terracotta accented, spark line bottom-left |
| B04 | SkillTeardownMechanism916 | serif title, sans body, mono quote | high | inside | verdict pill terracotta outline, quote block indented, cite attribution readable |
| B07 | SkillTeardownMechanism916 | serif title, sans body, mono quote | high | inside | verdict pill neutral (design-cost, not celebration); spark line bottom-left |
| B08 | ClaudeVerdictArtifact916 | poster serif heading, sans body | high | inside | card fills ~85% of vertical safe area; all five items render on one card |
| B10 | AntOutro916 | poster serif, terracotta terminal period | high | inside | eyebrow "BRUTALIST · EPISODE 05", handle "@HumanitariansAI", subline "LIAM, IN FOR BEAR." |

No overlap, no clipped ascenders/descenders, no unwanted captions or subtitle
tracks. Palette (cream page, ink serif, terracotta accent) is consistent across
every beat. Handle is @HumanitariansAI everywhere it appears (B00 chip + B10
outro) — the OUTRO-LOCK-driven decision to use the custom `AntOutro916` in
place of `ClaudeTitleOutro916` was carried through from the parent unchanged.

## Result

Visual typography: **PASS** for all 7 kept beats. Human review pending.
