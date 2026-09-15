# TYPECHECK — Brutalist Utility: image_fetch.py (portrait)

## Schema validation
All beat_sheet.json props validated against Remotion schema at render time.

| Beat | Scene | Props valid |
|---|---|---|
| B00 | ClaudeComposerAsk916 | ✓ |
| B01 | BrutalistHesitantWriter916 | ✓ seed:string, fontSize:number, lineSpacing:number |
| B02 | BrutalistTerminalOpen916 | ✓ |
| B03 | BrutalistAdaptCLI916 | ✓ |
| B04 | BrutalistAdaptCLI916 | ✓ |
| B05 | BrutalistAdaptCLI916 | ✓ |
| B06 | ClaudeVerdictArtifact916 | ✓ |
| B07 | ClaudeVerdictArtifact916 | ✓ |
| B08 | ClaudeComposerAsk916 | ✓ |
| B09 | ClaudeTitleOutroHAI916 | ✓ title:string, slug:string |

All renders completed without TypeScript/Zod validation errors.

## Visual typography review (portrait)
- B00 portrait ClaudeComposerAsk916: topic/title text legible, request text wraps correctly for 1080px wide portrait card, no overflow
- B01 BrutalistHesitantWriter portrait: large serif (lineSpacing 2.6) fills portrait safe area — min(w/1080,h/1920) scale patch applied
- B03/B04/B05 BrutalistAdaptCLI916: terminal card within portrait safe area; long lines truncated with ellipsis, primary commands legible
- B06/B07 ClaudeVerdictArtifact916: numbered body lines readable in portrait, heading fits within portrait safe width
- B09 ClaudeTitleOutroHAI916: title wraps correctly (overflowWrap:anywhere, wordBreak:break-word), @HumanitariansAI legible below

## Legacy type_check.py
No type_check.py in this toolkit — that is a legacy spec reference. Visual inspection via frame extraction and Read tool constitutes the typography audit.
