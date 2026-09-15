# SHOTLIST — Brutalist Utility: remotion_scenes.py

All beats classified per nopunt/SKILL.md SHOW / HOLD / CARD.

| Beat | Class | Scene | Props summary |
|---|---|---|---|
| B00 | SHOW | ClaudeComposerAsk | greeting Sawadee Liam, command about remotion_scenes.py, 3 output lines |
| B01 | SHOW | BrutalistHesitantWriter | text with ALL→only pattern-tagged slates, thin→gated provenance-stamper |
| B02 | SHOW | SkillTeardownPipeline | 4 phases: detect/render/extend/stamp, input=beat_sheet.json, output=media/BXX.mp4 |
| B03 | SHOW | ClaudeCodeBeat | filename=beat_sheet_example.json, code showing shot.remotion.pattern JSON structure |
| B04 | SHOW | ClaudeCodeBeat | filename=render_beat.py, npx remotion render command with quality flags |
| B05 | SHOW | ClaudeCodeBeat | filename=extend_clip.py, ffmpeg tpad freeze-hold command |
| B06 | SHOW | FormBCard | 3 gate functions: validate_project, validate_approvals, slate_resolves |
| B07 | SHOW | ClaudeCodeBeat | filename=terminal, actual --list output from demo run |
| B08 | SHOW | SkillTeardownMechanism | failure mode: FAIL: return path, exit 2, preserve media |
| B09 | SHOW | ClaudeVerdictArtifact | 6-line verdict artifact |
| B10 | SHOW | ClaudeComposerAsk | Your Turn greeting, handoff prompt, 3 expected output lines |
| B11 | SHOW | ClaudeTitleOutro | title restate + slug seed |

## Teaching arc (nopunt §Whole-sheet checklist)

- [x] FRAMEWORK beat — B02: 4-step pipeline with input/output
- [x] WORKED EXAMPLE — B03+B04: entry ticket (pattern field) → render command
- [x] FALSIFIABILITY / edge case — B08: failure mode, exit 2, media preserved
- [x] SCAFFOLDED viewer task — B10: real paste-ready prompt + 3 checkpoints
- [x] Four bookends — B00 cold open, B09 verdict, B10 handoff, B11 outro
- [x] No source no verdict — every factual claim has on-screen code artifact

## CHECKS-REPORT

12 SHOW / 0 justified-HOLD / 0 PUNT
Teaching arc: FRAMEWORK ✓ | WORKED EXAMPLE ✓ | FALSIFIABILITY ✓
              SCAFFOLDED TASK ✓ | BOOKENDS ✓ | NO-SOURCE-NO-VERDICT ✓
