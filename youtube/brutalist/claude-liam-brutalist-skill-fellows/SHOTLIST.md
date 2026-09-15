# Shotlist — landscape (3840×2160, 24 fps)

Every beat is a registered Remotion composition. `motion` names the beat's
dominant device; `show` in `beat_sheet.json` records the event timing.

| Beat | Composition | Motion | Actual (s) | What happens on screen |
|---|---|---|---|---|
| B00 | `ClaudeComposerAsk` | type-on | 13.16 | Cream composer card; greeting *Hallo, Liam* types above; command types into composer; send button arms terracotta; three result lines fade in. Folder chip `@HumanitariansAI`; segment title "The fellows Skill." |
| B01 | `BrutalistHesitantWriter` | type-on | 14.38 | 148-px EB Garamond serif on cream. Text writes line by line; the word *re-cuts* flashes terracotta on the delete beat and is replaced by *frames*. Final sentence stands: *"The fellows skill frames the fellows video. The fellows report plays untouched."* Seed: `fellows-bluf-2026-e71dd104`. |
| B02 | `SkillTeardownAnatomy` | reveal | 21.65 | Eyebrow SKILL · ANATOMY; title "The fellows folders."; folder tree reveals row by row (SKILL.md accented terracotta, then fellow's episode folder + transcript/, media/B04.mp4, NOTES.md, beat_sheet.json, BUILD-LOG.md, plus @HumanitariansAI + fellow-chosen Kokoro links). Callout box below: NOTES.md is a human gate. Spark line: "A frame around a fellow's file." |
| B03 | `SkillTeardownPipeline` | reveal | 19.78 | Eyebrow SKILL · PIPELINE; title "Nine beats. One fixed spine."; horizontal flow INPUT `fellow's raw recording` → ASK → SUMMARY ×2–3 → THE REPORT (terracotta accent) → BEAR'S NOTES ×2 → YOUR TURN + HAI OUTRO → OUTPUT `wrapped reel + signed NOTES.md`. Footer note names the "only the middle is the fellow's material" invariant. Spark line: "Bookends around the fellow's file." |
| B04 | `SkillTeardownMechanism` | reveal | 23.72 | MECHANISM · ACT 1 · heading "The report is the clock." Body enumerates the four never-dos; verbatim quote lands with citation `fellows SKILL.md · THE REPORT IS THE CLOCK`; verdict pill (positive) "inverts audio-first, for beat 4." |
| B05 | `SkillTeardownMechanism` | reveal | 22.55 | MECHANISM · ACT 2 · heading "The carve-out." Body: fellow's frames vs everything else; verbatim quote + citation `fellows SKILL.md · FELLOW'S-WORK carve-out`; verdict pill "the receipt is the point." |
| B06 | `SkillTeardownMechanism` | reveal | 27.43 | MECHANISM · ACT 3 · heading "GATE N." Body names both approval fingerprints and the block behavior; verbatim quote + citation; verdict pill "no bypass, no AI signature." |
| B07 | `SkillTeardownMechanism` | reveal | 26.84 | MECHANISM · ACT 4 · heading "Persistent voice." Body: fellow-chosen Kokoro voice + SOUND REPAIR carve-out (loudnorm, afftdn/arnndn, highpass); verdict pill "never pitch · never stretch · never re-voice." |
| B08 | `SkillTeardownMechanism` | reveal | 26.26 | FALSIFIABILITY · ACT 5 · heading "A deliberate sibling break." Body contrasts HAI outro vs ClaudeTitleOutro; verbatim quote from B08 spine + citation; verdict pill (negative polarity) "wrong outro = defect." |
| B09 | `ClaudeVerdictArtifact` | reveal | 26.73 | Artifact card fills frame; heading "A frame. Not a re-edit."; six numbered lines reveal one at a time — the six mechanisms/laws. |
| B10 | `ClaudeComposerAsk` | type-on | 35.73 | Composer with greeting *Your Turn*; segment "Plan a fellows reel without shipping it"; command types the paste-ready dry-run prompt (5 numbered clauses); three-line viewer rubric appears as output below. Folder chip `@HumanitariansAI`. Running text: "paste this into Claude Code…" |
| B11 | `ClaudeTitleOutro` | hold | 3.37 | Cream ground (or ink — polarity is slug-seeded); title "The fellows Skill." with terracotta period; hardcoded `@NikBearBrown` handle beneath; slug-seeded mascot animation. No subline. |

## Motion pantry compliance

Landscape motion histogram (from compile.py):

```
reveal: 7   type-on: 3   hold: 1
```

`reveal` is 7/12 = 58% — over the ~40% pantry cap. This warning is expected for
the skill-teardown modifier: every mechanism act uses the same eyebrow → heading →
body → quote → verdict card and is structurally a reveal. B00, B01, B10 (type-on)
plus the hold outro do the rhythm work. Warning is not a Gate refusal.

## Duration budget

Actual narration total: **261.60 s** (see SCRIPT.md table).
Expected compiled duration: ~262 s (audio-conformed with tiny per-beat padding
for frame alignment).

## Notes on scenes touched

- `ClaudeComposerAsk`, `BrutalistHesitantWriter`, `SkillTeardownAnatomy`,
  `SkillTeardownPipeline`, `SkillTeardownMechanism`, `ClaudeVerdictArtifact`,
  `ClaudeTitleOutro` — all shipped library components. No landscape scene was
  authored or patched for this run.
- Registered 916 variants (`SkillTeardownAnatomy916`, `SkillTeardownPipeline916`,
  `SkillTeardownMechanism916`) were added to `runtime/remotion/src/Root.tsx` in
  the isolated toolkit for the portrait companion. `BrutalistHesitantWriter`
  received a portrait-aware scale patch (per memory `feedback_hesitant_writer_portrait_scale`).
  See `scene-source-manifest.json` and `PROMPTS.md`.
