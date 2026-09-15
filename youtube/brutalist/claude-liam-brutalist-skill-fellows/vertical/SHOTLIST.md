# Shotlist — vertical (2160×3840, 24 fps)

Every beat is a **portrait-native** registered Remotion composition. The 916
variants of the three SkillTeardown scenes were copied into this isolated
toolkit for this run (`scene-source-manifest.json`). `motion` names the beat's
dominant device; `show` in `beat_sheet.json` records the event timing.

| Beat | Composition | Motion | Actual (s) | What happens on screen |
|---|---|---|---|---|
| B00 | `ClaudeComposerAsk916` | type-on | 13.16 | Portrait composer, greeting *Hallo, Liam* above, ask command types, terracotta send button, three result lines. `@HumanitariansAI` folder chip. |
| B01 | `BrutalistHesitantWriter` (portrait scale via `useVideoConfig`) | type-on | 14.38 | Five-line reflow: `The fellows skill / re-cuts the / fellows video. / The fellows report / plays untouched.` `re-cuts → frames` correction lands mid-timeline. **fontSize=118, lineSpacing=2.2** (portrait-specific; landscape keeps 148, 1.2). Seed: `fellows-bluf-vertical-e71dd104-v2`. |
| B02 | `SkillTeardownAnatomy916` | reveal | 21.65 | Vertical stack of the folder tree (SKILL.md accented terracotta, then fellow's episode folder + transcript, media/B04.mp4, NOTES.md, beat_sheet.json, BUILD-LOG.md, plus channel + voice links). Callout box beneath. Spark line at bottom-left safe. |
| B03 | `SkillTeardownPipeline916` | reveal | 19.78 | Vertical stack (down-arrows): INPUT ↓ ASK ↓ SUMMARY ×2–3 ↓ THE REPORT (terracotta, accented) ↓ BEAR'S NOTES ×2 ↓ YOUR TURN + HAI OUTRO ↓ OUTPUT. Footer note names the invariant. |
| B04 | `SkillTeardownMechanism916` | reveal | 23.72 | MECHANISM · ACT 1 · heading "The report is the clock." Portrait typography ramp — body 40 px, quote 34 px mono. Verdict pill "inverts audio-first, for beat 4." |
| B05 | `SkillTeardownMechanism916` | reveal | 22.55 | MECHANISM · ACT 2 · heading "The carve-out." Verdict pill "the receipt is the point." |
| B06 | `SkillTeardownMechanism916` | reveal | 27.43 | MECHANISM · ACT 3 · heading "GATE N." Verdict pill "no bypass, no AI signature." |
| B07 | `SkillTeardownMechanism916` | reveal | 26.84 | MECHANISM · ACT 4 · heading "Persistent voice." Verdict pill "never pitch · never stretch · never re-voice." |
| B08 | `SkillTeardownMechanism916` | reveal | 26.26 | FALSIFIABILITY · ACT 5 · heading "A deliberate sibling break." Verdict pill (negative polarity) "wrong outro = defect." |
| B09 | `ClaudeVerdictArtifact916` | reveal | 26.73 | Portrait artifact card, heading "A frame. Not a re-edit.", six numbered lines reveal in order. |
| B10 | `ClaudeComposerAsk916` | type-on | 35.73 | Portrait composer, greeting *Your Turn*, paste-ready dry-run prompt types, three-line rubric appears as output. |
| B11 | `ClaudeTitleOutro916` | hold | 3.37 | Cream or ink polarity (slug-seeded); title "The fellows Skill." with terracotta period; hardcoded `@NikBearBrown` handle beneath; slug-seeded mascot. No subline. |

## Duration budget

Actual narration total: **261.60 s** (same as landscape).
Compiled portrait duration: **261.88 s** (per-beat frame-alignment padding).

## Portrait-specific notes

- The three `SkillTeardown*916` wrappers use the same schemas as their landscape
  siblings (they import them directly); a schema change on the landscape side
  flows into the portrait automatically.
- `channel_title` metadata deliberately omitted from the vertical beat sheet
  because the compile's centered channel_title overlay renders past the safe
  bottom at portrait dimensions (memory `feedback_channel_title_portrait_bleed`).
  The `folderLabel` in the composer beats (`@HumanitariansAI`) and the outro
  handle (`@NikBearBrown`, hardcoded per OUTRO-LOCK.md) both remain correct.
- `BrutalistHesitantWriter` — the shipped landscape-only scale formula
  (`Math.min(width/1920, height/1080)`) collapses to ~0.56 on 1080-wide portrait,
  which is why the fashionista reel's portrait pass patched it (memory
  `feedback_hesitant_writer_portrait_scale`). Same patch applied here in the
  isolated toolkit only.
- B01's portrait-specific props (fontSize=118, lineSpacing=2.2, five-line reflow
  of the same four-idea sentence) were tuned to satisfy Gate V's `FILL_MIN=0.55`
  canvas-fill requirement. Final coverage 56%.
