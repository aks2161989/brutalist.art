# Shotlist — Brutalist Utility: beat_lint.py

Classification: SHOW / HOLD / CARD per nopunt SKILL.md

| Beat | Classification | Scene | What renders |
|---|---|---|---|
| B00 | SHOW | ClaudeComposerAsk | Claude composer types the ask; result lines animate in |
| B01 | SHOW | BrutalistHesitantWriter | Writer types BLUF, hesitates, swaps "placeholder beats" → "text-card beats wearing illustration clothes" |
| B02 | SHOW | BeatLintPipeline | Flow diagram: beat_sheet.json → beat_lint.py → pass branch / fail branch; phases animate on narration cues |
| B03 | SHOW | ClaudeCodeBeat | Source code: TEXT_CARD_PATTERNS, EXEMPT_LANES, GRAPHIC_LANES constants; exempt check sequence |
| B04 | SHOW | ClaudeCodeBeat | Source code: the RULE 3 condition `if lane == "remotion" and patt in TEXT_CARD_PATTERNS:` with defect append |
| B05 | SHOW | ClaudeCodeBeat | Code card: legal STILL and vox-anim placeholder syntax; "Two legal forms. Everywhere else: defect." spark line |
| B06 | SHOW | ClaudeCodeBeat | Clean run code card: `$ python3 runtime/qc/beat_lint.py …` → `[beat-lint] clean — beat mix OK`; "Exit 0. The build continues." |
| B07 | SHOW | ClaudeCodeBeat | Defect run code card: two [single-sentence-remotion] messages with fix instructions; "Exit 2. Fix the beat sheet first." |
| B08 | SHOW | ClaudeVerdictArtifact | Verdict artifact: what beat_lint catches / what it doesn't catch |
| B09 | SHOW | ClaudeCodeBeat | Code card: brand_labels.json mapping; Rule 7 branding contract; "Edit brand_labels.json. No code change." |
| B10 | SHOW | ClaudeComposerAsk | "Your turn." — paste-ready Claude Code prompt; narration reads it aloud |
| B11 | SHOW | ClaudeTitleOutroHAI | Title card: "Brutalist Utility: beat_lint.py" with @HumanitariansAI handle |

## Teaching arc check

- [x] FRAMEWORK beat: B02 (lint pipeline diagram — shows phases before examples)
- [x] WORKED EXAMPLE: B06+B07 (clean run then defect run, both from real CLI)
- [x] FALSIFIABILITY: B08 (verdict — explicit statement of what the tool does not catch)
- [x] SCAFFOLDED viewer task: B10 (prompt with rubric: "look for exit 0 and real illustration patterns")
- [x] Four bookends: B00 (ask), B08 (verdict), B10 (your turn), B11 (outro)
- [x] No source, no verdict: all factual claims shown on screen as code, shell output, or diagram

## SHOW / HOLD / CARD summary: 12 SHOW / 0 HOLD / 0 CARD / 0 PUNT
