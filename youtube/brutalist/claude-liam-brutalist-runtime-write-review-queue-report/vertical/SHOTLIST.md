# SHOTLIST — Brutalist Utility: write_review_queue_report.py

run_id: aef36acf6a354924acd1af29d9d319cf

All beats are SHOW — Remotion scenes, no pantry requests, no slates.

| Beat | Class | Pattern | Props summary |
|---|---|---|---|
| B00 | SHOW | ClaudeComposerAsk | greeting: Merhaba/Liam; command: audit-to-report question; output: AUDIT.md written |
| B01 | SHOW | BrutalistHesitantWriter | text: 3-line correction; triggers: generates→formats, inspects→reads; seed: 73 |
| B02 | SHOW | SkillTeardownPipeline | 2-input 1-output flow; read-only footer |
| B03 | SHOW | ClaudeCodeBeat | sys.argv[1] + audit.json + review-notes.json reads; schema comments |
| B04 | SHOW | ClaudeCodeBeat | main for loop; str(n) key lookup; beat_sheet.json read |
| B05 | SHOW | ClaudeCodeBeat | 3 pantry spellings + comment; if-path branch |
| B06 | SHOW | SkillTeardownMechanism | AUDIT.md section list; hardcoded quote |
| B07 | SHOW | ClaudeCodeBeat | 4 failure modes with error types; no try-except |
| B08 | SHOW | SkillTeardownMechanism | 12-frame/70% heuristic; pantry=metadata; scope quote |
| B09 | SHOW | ClaudeVerdictArtifact | 3 verdict lines; brandLabel: @HumanitariansAI |
| B10 | SHOW | ClaudeComposerAsk | greeting: Your Turn; paste-ready prompt |
| B11 | SHOW | ClaudeTitleOutroHAI | title restate; slug-seeded mascot |

## Teaching arc checklist

- [x] FRAMEWORK beat — B02: SkillTeardownPipeline showing the two-input/one-output pipeline
- [x] WORKED EXAMPLE — B03/B04/B05: actual code lines walked through with explanations
- [x] FALSIFIABILITY / edge-case beat — B07: four concrete failure modes with actual error types
- [x] SCAFFOLDED viewer task — B10: paste-ready prompt with explicit evaluation rubric (pantry flags? probe accuracy? report structure?)
- [x] Four bookends — B00 (cold open), B09 (verdict), B10 (Your Turn), B11 (outro)
- [x] No source, no verdict — all claims backed by on-screen code from the actual source file

## No pantry requests

Zero pantry requests in this episode. All body beats use native Remotion scenes.

## No human-hold beats

No archival photographs required. Zero HOLD beats.

## PUNT check

No PUNTs. Every beat classifies as SHOW using the nopunt catalog:
- Code/script → ClaudeCodeBeat (skin — show the real artifact)
- Pipeline diagram → SkillTeardownPipeline (Remotion structural illustration)
- Mechanism/limits → SkillTeardownMechanism (Remotion mechanism illustration)
- Verdict → ClaudeVerdictArtifact
- Bookends → ClaudeComposerAsk / ClaudeTitleOutroHAI
