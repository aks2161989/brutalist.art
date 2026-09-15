# SHOTLIST — The godot-waikthrough Skill
# run_id: 4d4269b669dd4b84a92a266e5bff804f

All beats: SHOW class (Remotion scenes). No PUNT beats. No HOLD beats (no archival photographs needed).

## Classification

13 SHOW / 0 HOLD / 0 PUNT

Teaching arc: FRAMEWORK ✓ | WORKED EXAMPLE ✓ | FALSIFIABILITY ✓ | SCAFFOLDED TASK ✓ | BOOKENDS ✓ | NO-SOURCE-NO-VERDICT ✓

---

| Beat | Act | Scene | Mode/Props | Class | Notes |
|---|---|---|---|---|---|
| B00 | ASK | ClaudeComposerAsk | greeting "Annyeong, Liam"; 3 result lines | SHOW | COLD OPEN LAW; IN-FOR-BEAR LAW |
| B01 | BLUF | BrutalistHesitantWriter | text/trigger/replacement; seed 4533; lead_silence_s 0.8 | SHOW | EXECUTIVE-SUMMARY LAW; ≥9s (20s); correction "records"→"riffs" |
| B02 | PIPELINE | WalkerGodotSetup | mode='flow'; 5 stages; Riff stage terracotta | SHOW | FRAMEWORK beat; ILLUSTRATE LAW |
| B03 | ANATOMY | SkillTeardownAnatomy | folder tree; callout box; two modes | SHOW | ILLUSTRATE LAW |
| B04 | MECHANISM | GodotDesignBoard | layout='cards'; 4 cards (built/planned/broken/coverage.json); cues | SHOW | WORKED EXAMPLE; labeled teaching illustration |
| B05 | MECHANISM | WalkerGodotSetup | mode='terminal'; capture command + input log lines | SHOW | ILLUSTRATE LAW; different visual from B04 |
| B06 | MECHANISM | GodotDevWorkbench | mode='code'; RIFF.md structure; 5 cues; right-panel notes | SHOW | ILLUSTRATE LAW; different visual from B05 |
| B07 | MECHANISM | WalkerGodotSetup | mode='flow'; 6-stage walker sequence | SHOW | Different flow content from B02; ILLUSTRATE LAW |
| B08 | MECHANISM | SkillTeardownMechanism | verbatim quote; verdict "Honest contract" | SHOW | DESIGN TELL; VERBATIM QUOTE LAW |
| B09 | FALSIFIABILITY | SkillTeardownMechanism | check command quote; verdict "Honest limitation" | SHOW | FALSIFIABILITY beat; SELF-DEMO limitation |
| B10 | VERDICT | ClaudeVerdictArtifact | 4 artifact lines | SHOW | Recapitulates; no-source-no-verdict exempt |
| B11 | HANDOFF | ClaudeComposerAsk | greeting "Your turn."; full prompt; output lines | SHOW | HANDOFF LAW; Liam reads prompt aloud; sign-off |
| B12 | OUTRO | ClaudeTitleOutro | title exact; slug-seeded; audio_policy:silence | SHOW | OUTRO LAW; @NikBearBrown hardcoded; narration_text "Liam, in for Bear." |

## ILLUSTRATE LAW verification

- B02, B03, B04, B05, B06, B07, B08, B09 are all concept illustrations, NOT Claude UI beats ✓
- Claude UI appears only at B00 (cold open), B11 (handoff), B12 (outro) ✓
- No two consecutive beats share the same visual scheme:
  - B02 WalkerGodotSetup(flow) → B03 SkillTeardownAnatomy → B04 GodotDesignBoard → B05 WalkerGodotSetup(terminal) → B06 GodotDevWorkbench → B07 WalkerGodotSetup(flow) → B08 SkillTeardownMechanism → B09 SkillTeardownMechanism ✓
  - Note: B08 and B09 both use SkillTeardownMechanism. Different content (design-tell vs limitation). Accepted — no other registered scene fits both a verbatim-quote card AND an honest-limitation card equally well. Each beat has distinct heading, quote, and verdict.

## Consecutive-scheme note (B08/B09)

Both use SkillTeardownMechanism. The ILLUSTRATE LAW says "two consecutive beats sharing the same visual scheme is the smell." This is the edge case. The beats carry different content, different headings, and different verdicts. The alternative (using GodotDevWorkbench or GodotDesignBoard for B09) would misrepresent the falsifiability concept as an editor view. Accepted with this note.

## Legibility contract (all SHOW beats)

- On-screen artifacts named in shot.show ✓
- Source fields populated on all teaching-illustration beats ✓
- No highlights/fades without shown artifact ✓
