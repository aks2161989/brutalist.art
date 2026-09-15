# SHOTLIST.md — The hai Skill

Each beat's rendered component, key show events, and prop summary. Full props live in `beat_sheet.json`.

| # | Beat | Component | Purpose |
|---|---|---|---|
| B00 | ASK | ClaudeComposerAsk | Cold open — the question about hai and its answer, on the Claude UI |
| B01 | BLUF | BrutalistHesitantWriter | The overview typed in front of viewer; "reformats" → "forks" correction |
| B02 | FRAMEWORK | SkillTeardownAnatomy | Toolkit-side + output-side folder tree; callout on `_variant_todo` |
| B03 | FRAMEWORK | SkillTeardownPipeline | The six-step flow, INPUT → 6 phases → OUTPUT, with the CLI beat highlighted |
| B04 | MECHANISM 1 | SkillTeardownMechanism | "Non-destructive fork" — quote from SKILL.md line 20, verdict pill |
| B05 | MECHANISM 2 | SkillTeardownMechanism | "Plain register" — the three-line checklist, "when NOT to" quote |
| B06 | MECHANISM 3 | SkillTeardownMechanism | "The CLI exercise" — the five-part schema, "genuinely runnable" quote |
| B07 | MECHANISM 4 | SkillTeardownMechanism | "Batch mode" — one find, one loop; Steps 2–6 stay per-video |
| B08 | FALSIFIABILITY | SkillTeardownMechanism | Voice-field disagreement across SKILL.md / brand_variant.py / brands/hai.md |
| B09 | VERDICT | ClaudeVerdictArtifact | Six-line summary artifact card |
| B10 | YOUR TURN | ClaudeComposerAsk | Paste-ready dry-run prompt for the viewer's own reel |
| B11 | OUTRO | ClaudeTitleOutro | Title restate + `@NikBearBrown` handle + slug-seeded mascot |

## Layout notes

- Landscape master: 3840×2160 (scale = 2 on 1920×1080 compositions).
- Portrait companion: 2160×3840 (scale = 2 on 1080×1920 compositions).
- The three SkillTeardown* portrait wrappers reflow the same schemas natively — not a crop. See `SOURCES.md` for their lineage.
- BrutalistHesitantWriter uses the portrait-aware scale patch (aspect-appropriate design reference) so serif type does not collapse.

## Timing

Audio is the clock. Actual per-beat durations are written back into `beat_sheet.json` after `generate_audio_kokoro.py`. Estimates in the sheet are planning aids only.
