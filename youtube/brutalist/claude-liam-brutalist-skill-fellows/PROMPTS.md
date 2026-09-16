# Prompts on screen + scene-source additions

## B00 · cold-open composer command

```
What is the `fellows` skill? Read skills/make/fellows/SKILL.md and tell me
what it really does with a fellow's video.
```

Ask lands answered — three result lines below the composer:

- a frame around a fellow's own recording
- branded bookends · Professor Bear's notes · HAI outro
- the report plays untouched — audio and timing

Greeting: `Hallo, Liam` (German world-language hello, one-word cue, persona slot).
Folder chip `@HumanitariansAI`. Segment title "The fellows Skill." No subline.

## B10 · Your Turn composer command (paste-ready)

```
Read skills/make/fellows/SKILL.md. Then plan (DO NOT RUN) a dry-run fellows
episode for a hypothetical fellow with a 2-min report:
(1) the ClaudeComposerAsk cold open;
(2) two summary beats from a fabricated transcript LABELED as a fixture;
(3) a starter NOTES.md with feedback + next steps;
(4) a Your Turn prompt;
(5) metadata.approvals for voice and professor_notes as PENDING records
    with real subject fingerprints.
Do not run generate_audio_kokoro.py or compile.py.
```

Rubric that appears as output below the composer — the three checks Liam
reads aloud:

- check: does B04 declare `kind: source_report` + `audio_policy: preserve`?
- check: are both approvals PENDING with real fingerprints (never fake sign-offs)?
- check: does the outro name the standard HAI outro, not `ClaudeTitleOutro`?

Greeting: `Your Turn`. Segment: "Plan a fellows reel without shipping it."
Running text: `paste this into Claude Code…`.

## Verbatim on-screen quotes (with sources)

Each MECHANISM/FALSIFIABILITY beat carries a verbatim quote card + citation:

| Beat | Quote (verbatim from fellows SKILL.md) | Cite line on screen |
|---|---|---|
| B04 | *"THE REPORT IS THE CLOCK (the one exception to audio-first). Everywhere else narration MP3s are the master clock. The report beat's clock is the report's own measured runtime."* | `fellows SKILL.md · THE REPORT IS THE CLOCK` |
| B05 | *"The fellow's artifact is the receipt; rebuilding it would falsify it. Everything that is NOT the fellow's own material is rebuilt native, REBUILD LAW unchanged."* | `fellows SKILL.md · FELLOW'S-WORK carve-out` |
| B06 | *"The notes beats never go to audio until Bear has edited or signed NOTES.md. The runtime blocks pending or stale records; --no-gate is not a bypass. Never have an AI sign a human's approval record."* | `fellows SKILL.md · GATE N` |
| B07 | *"Never pitch-shift, never time-stretch, never re-voice. Every filter applied is logged in BUILD-LOG.md."* | `fellows SKILL.md · SOUND REPAIR` |
| B08 | *"NOT the @NikBearBrown outro — fellows is a HAI channel reel; ClaudeTitleOutro and its lock (OUTRO-LOCK.md) do NOT apply here."* | `fellows SKILL.md · B08 OUTRO` |

VERBATIM QUOTE LAW respected: exact wording, citation once per figure, small
sans, `CLAUDE.GHOST` colour beneath the quote block.

## Scene-source additions in the isolated toolkit

For the portrait companion this run added three native 916 wrappers and one
scale patch to shipped code. All changes live in the isolated toolkit only;
the real public toolkit is not modified.

### New (copied from the fashionista reel's scene-source, same design)

- `runtime/remotion/src/scenes/SkillTeardownAnatomy916.tsx`  (1080×1920 reflow of the landscape schema)
- `runtime/remotion/src/scenes/SkillTeardownPipeline916.tsx` (vertical stack of the pipeline flow)
- `runtime/remotion/src/scenes/SkillTeardownMechanism916.tsx` (portrait typography ramp of the mechanism card)

### Modified

- `runtime/remotion/src/Root.tsx` — three new `<Composition>` registrations under
  the existing `SkillTeardown-Generic` folder (`SkillTeardownAnatomy916`,
  `SkillTeardownPipeline916`, `SkillTeardownMechanism916`, each 1080×1920@30, 600 frames).
- `runtime/remotion/src/scenes/BrutalistHesitantWriter.tsx` — the shipped scale
  formula was `Math.min(width / 1920, height / 1080)`. Applied to a 1080×1920
  canvas it collapses to `~0.5625`, so the serif never fills the portrait safe
  area. Patched to aspect-appropriate reference: portrait uses `min(w/1080, h/1920)`,
  landscape unchanged. Same fix documented in memory `feedback_hesitant_writer_portrait_scale`.

### Not modified

Zero landscape components were changed. The three 916 variants import the schemas
from their landscape siblings (`SkillTeardownAnatomySchema`, etc.), so any future
schema change on the landscape side flows into the portrait automatically.
