# SHOTLIST.md — The hai Skill (Short)

Kept beats only. Each row is the rendered Remotion component copied from the
parent reel's native 9:16 render at 2160×3840 (no re-render, no crop). Full
props live in `beat_sheet.json`; dropped beats (B02, B06, B07, B10) are
recorded in `CUT-PLAN.json`.

| # | Beat | Component (9:16) | Purpose |
|---|---|---|---|
| B00 | ASK | ClaudeComposerAsk916 | Cold open — the question about hai and its answer, on the Claude UI |
| B01 | BLUF | BrutalistHesitantWriter916 | The overview typed in front of the viewer; "reformats" → "forks" correction |
| B03 | FRAMEWORK | SkillTeardownPipeline916 | The six-step flow, INPUT → 6 phases → OUTPUT, with the CLI beat highlighted |
| B04 | MECHANISM 1 | SkillTeardownMechanism916 | "Non-destructive fork" — quote from SKILL.md line 20, verdict pill |
| B05 | MECHANISM 2 | SkillTeardownMechanism916 | "Plain register" — the three-line checklist, "when NOT to" quote |
| B08 | FALSIFIABILITY | SkillTeardownMechanism916 | Voice-field disagreement across SKILL.md / brand_variant.py / brands/hai.md |
| B09 | VERDICT | ClaudeVerdictArtifact916 | Six-line summary artifact card |
| B11 | OUTRO | ClaudeTitleOutro916 | Title restate + `@NikBearBrown` handle + slug-seeded mascot |

## Layout notes

- Portrait render: 2160×3840 (scale = 2 on 1080×1920 compositions).
- The three SkillTeardown* portrait wrappers reflow the same schemas natively
  — not a crop. See `SOURCES.md` for their lineage.
- BrutalistHesitantWriter916 uses the portrait-aware scale patch so serif
  type does not collapse on 9:16.

## Timing

Audio is the clock. Actual per-beat durations are inherited from the parent
reel's post-render `beat_sheet.json` (no audio was regenerated for this Short
— `--no-outro-rewrite` was set). Every beat's mp3 and mp4 were copied as
independent files, not symlinks.
