# Shot list — Brutalist Utility: provenance.py
# Episode 52 · run_id: 9acc8c13d5d443968a1aed379ed68b66

## Beat classification (SHOW / HOLD / CARD)

| Beat | Class | Scene | Justification |
|---|---|---|---|
| B00 | SHOW | ClaudeComposerAsk | Claude interface IS the subject (cold open). ASK→RESULT: command typed, output lines show real classification. |
| B01 | SHOW | BrutalistHesitantWriter | Writer performs the correction on screen; typing + hesitation is the beat's visual event. BLUF mandated. |
| B02 | SHOW | SkillTeardownPipeline | Three-phase flow diagram reveals as narration names each layer. Phases animate left-to-right with arrows. |
| B03 | SHOW | ClaudeCodeBeat | Source code of `audio_engine()` is the evidence. Lines stagger in with narration. Real file, real logic. |
| B04 | SHOW | SkillTeardownMechanism | Heading + body + verbatim quote + verdict. Quote is on-screen source evidence per DOUBLE-CHECK LAW. |
| B05 | SHOW | ClaudeCodeBeat | Real demo output from fixture run (see `demo/fixture-run.txt`). AUDIO mismatch highlighted in terracotta. |
| B06 | SHOW | FormBCard | Three slot labels with icons. Each item reveals on its spoken cue. Three named things → FormBCard. |
| B07 | SHOW | SkillTeardownAnatomy | File tree with [required] accent on beat_sheet.json. Callout names ffprobe dependency. |
| B08 | CARD | FormACard | Four failure modes as text lines. Justified: these are categorical outcomes with nothing to animate beyond karaoke reveals. Each line is a verifiable code path. |
| B09 | SHOW | ClaudeVerdictArtifact | Verdict artifact card — three numbered deliverables. Named artifact per SHOW contract. |
| B10 | SHOW | ClaudeComposerAsk | Handoff beat — composer shows prompt + expected output. HANDOFF LAW: read aloud + discussed. |
| B11 | SHOW | HaiTitleOutro | Title restate outro with @HumanitariansAI handle. OUTRO LAW. |

**Counts:** 10 SHOW / 0 HOLD / 1 CARD / 0 PUNT

**Teaching arc:**
- FRAMEWORK ✓ — B02 presents the three-layer classification model before any examples
- WORKED EXAMPLE ✓ — B05 walks through real fixture output against the framework
- FALSIFIABILITY ✓ — B06 addresses Capture? ambiguity (what the tool can't resolve); B08 addresses failure modes
- SCAFFOLDED TASK ✓ — B10 prompt is specific: run provenance.py, find Capture? beats, add build.filled_by field
- BOOKENDS ✓ — B00 cold open, B09 verdict, B10 handoff, B11 outro
- NO-SOURCE-NO-VERDICT ✓ — B03 shows source code; B04 shows verbatim quote; B05 shows real output

## Illustration decisions
- B02: SkillTeardownPipeline chosen over a custom flow diagram — existing component covers 3-phase linear flows exactly.
- B03, B05: ClaudeCodeBeat for code beats (code/terminal skin per nopunt catalog).
- B04: SkillTeardownMechanism for the design-tell beat — heading + body + verbatim quote format exactly matches this component's purpose.
- B07: SkillTeardownAnatomy for prerequisites — file tree with accented required node is the right form for "what must be present."
- B08: FormACard for failure modes — four lines of categorical outcomes. Motion would not add clarity here.
- B06: FormBCard for three labels — named things with icons, karaoke reveal.

## Portrait (9:16) mapping
SkillTeardownPipeline, ClaudeCodeBeat, SkillTeardownMechanism, SkillTeardownAnatomy have no registered 916 variants.
Portrait beat sheet maps these to available 916 components:
- B02 SkillTeardownPipeline → FormBCard916 (3 phases as items)
- B03 ClaudeCodeBeat → FormACard916 (key logic as text lines)
- B04 SkillTeardownMechanism → FormACard916 (key insight + quote as text)
- B05 ClaudeCodeBeat → FormACard916 (demo output as text)
- B07 SkillTeardownAnatomy → FormBCard916 (prerequisites as items)
- B08 FormACard → FormACard916 ✓
- B06 FormBCard → FormBCard916 ✓
All other beats use registered 916 components directly.
