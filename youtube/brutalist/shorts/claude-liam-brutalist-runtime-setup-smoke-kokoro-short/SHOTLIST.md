# SHOTLIST — Brutalist Utility: setup_smoke_kokoro.py — Short

**Short cut: B00, B01, B06, B08, B09, B10. Dropped: B02, B03, B04, B05, B07.**

All beats are SHOW (Remotion scenes) — zero HOLD, zero PUNT.

| Beat | Classification | Scene | Props / Content | Source |
|---|---|---|---|---|
| B00 | SHOW | ClaudeComposerAsk | greeting:"Selam, Liam" / command: why ./setup synthesizes / 3 output lines | remotion |
| B01 | SHOW | BrutalistHesitantWriter | "import"→"synthesis" / "enough"→"insufficient" correction / seed:54321 | remotion |
| B02 | SHOW | SkillTeardownPipeline | 5 phases: model files → ffmpeg → kokoro_onnx → synthesize → volumedetect | remotion |
| B03 | SHOW | ClaudeCodeBeat | Guard section verbatim (lines 31–39 of source) | remotion / verbatim |
| B04 | SHOW | ClaudeCodeBeat | Synthesis block (lines 41–51, WAV loop condensed) | remotion / verbatim |
| B05 | SHOW | ClaudeCodeBeat | Volume gate (lines 53–68: subprocess.run + parse + threshold) | remotion / verbatim |
| B06 | SHOW | ClaudeCodeBeat | All 5 failure messages + success message from fail() + success path | remotion / verbatim |
| B07 | SHOW | ClaudeCodeBeat | try/finally block (lines 52–72) with cleanup | remotion / verbatim |
| B08 | SHOW | ClaudeVerdictArtifact | 5 artifact lines — summary of all 3 mechanism acts + design choice | remotion |
| B09 | SHOW | ClaudeComposerAsk | greeting:"Your turn." / TTS backend adaptation prompt + 3 result lines | remotion |
| B10 | SHOW | ClaudeTitleOutro | title restate + @HumanitariansAI + mascotAnimation:"bounce" | remotion |

## Portrait (vertical) beat assignments

| Beat | Scene (9:16) |
|---|---|
| B00 | ClaudeComposerAsk916 |
| B01 | BrutalistHesitantWriter916 (lineSpacing:2.5) |
| B02 | ClaudeCodeBeat916 (pipeline as annotated comments) |
| B03 | ClaudeCodeBeat916 |
| B04 | ClaudeCodeBeat916 |
| B05 | ClaudeCodeBeat916 |
| B06 | ClaudeCodeBeat916 |
| B07 | ClaudeCodeBeat916 |
| B08 | ClaudeVerdictArtifact916 |
| B09 | ClaudeComposerAsk916 |
| B10 | ClaudeTitleOutro916 |

## No-HOLD justification

All visual content is rendered Remotion code: the utility source file is pure Python with no real-world artifacts (no diagrams, charts, or archival images needed). Every beat is fully animated from the source text.

## PUNT status

Zero PUNTs. All beats classified SHOW.
