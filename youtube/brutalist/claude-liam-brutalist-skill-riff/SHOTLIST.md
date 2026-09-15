# SHOTLIST — The riff Skill
**Episode:** claude-liam-brutalist-skill-riff  
**Run ID:** deb461319da4431a9518a6feef4fa1ec  
**Date:** 2026-09-12  

---

## Beat classification (SHOW / HOLD / CARD)

| Beat | Scene | Class | Artifact on screen | Hold reason |
|---|---|---|---|---|
| B00 | ClaudeComposerAsk | SHOW | Claude composer UI with typed ask and cascading output lines | — |
| B01 | BrutalistHesitantWriter | SHOW | Hesitant-writer animation: "opinions" deleted, "observations" typed | — |
| B02 | SkillTeardownAnatomy | SHOW | Folder tree: skills/make/riff/SKILL.md with accent and callout | — |
| B03 | SkillTeardownPipeline | SHOW | Pipeline diagram: four phases with terracotta arrows | — |
| B04 | SkillTeardownMechanism | SHOW | Mechanism card with body text + verbatim quote + verdict pill | — |
| B05 | ClaudeCodeBeat | SHOW | Real art scenes output from this build (demo/RUN-LOG.txt) | — |
| B06 | SkillTeardownMechanism | SHOW | Mechanism card: two roles (footage/voice) + verbatim quote + verdict | — |
| B07 | SkillTeardownMechanism | SHOW | Mechanism card: RIFF.md five columns + verbatim quote + verdict | — |
| B08 | SkillTeardownMechanism | SHOW | Design tell card: what it gets right/bites + integrity rule quote | — |
| B09 | ClaudeVerdictArtifact | SHOW | Artifact card with four verdict lines (recapitulates, no new assertions) | — |
| B10 | ClaudeComposerAsk | SHOW | Composer "Your Turn" with paste-ready prompt typed in | — |
| B11 | ClaudeTitleOutro | SHOW | Title card + @NikBearBrown handle + mascot animation | — |

**Beat classification summary:** 12 SHOW / 0 HOLD / 0 CARD / 0 PUNT

## Teaching arc (nopunt whole-sheet checklist)

- [x] **FRAMEWORK beat** — B02 (skill anatomy) + B03 (pipeline) present the model before any examples
- [x] **WORKED EXAMPLE** — B05: real art scenes search from this build, walked through the "look first" framework on screen
- [x] **FALSIFIABILITY / edge-case beat** — B08: design tell explicitly names where the skill bites (can't reach "is it fun?" without a real playtest)
- [x] **SCAFFOLDED viewer task** — B10: specific prompt + rubric (separate what you saw from what you inferred; check every claim against a timecode)
- [x] **Four bookends** — B00 (cold open), B09 (verdict), B10 (YOUR TURN), B11 (title-restate outro)
- [x] **No source, no verdict** — B04/B06/B07/B08 all carry verbatim on-screen quotes from riff SKILL.md. B09/B10 are verdict/YOUR TURN (exempt per nopunt rules)

## No punts

No beat in this sheet is a placeholder, gen-AI clip, unfilled slate, or "drop an image" still. B05 shows real command output from this build session. All mechanism beats use registered RENDERABLE Remotion components.

## ILLUSTRATE LAW compliance

- B00: Claude UI is the subject (cold open bookend) ✓
- B01: BrutalistHesitantWriter — concept illustration (the writer's hesitation is the pedagogy) ✓
- B02-B08: SkillTeardownAnatomy/Pipeline/Mechanism — concept illustrations, not UI wallpaper ✓
- B05: ClaudeCodeBeat — app skin showing real code, not UI decoration ✓
- B09: Claude UI as verdict bookend ✓
- B10: Claude UI as YOUR TURN bookend ✓
- B11: Title outro bookend ✓

No two consecutive beats share the same visual scheme (verified: B04/B05 switch SkillTeardownMechanism → ClaudeCodeBeat → B06 SkillTeardownMechanism).

## SHOW-DON'T-TELL LAW

Every beat has a `show` block in the landscape beat_sheet.json with ordered visual events. Narration reacts to what's on screen; evidence appears on screen rather than being recited in the voice track.
