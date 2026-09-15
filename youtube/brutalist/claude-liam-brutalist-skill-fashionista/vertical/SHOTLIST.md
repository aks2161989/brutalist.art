# Shot list — landscape (16:9, 3840×2160)

All 12 beats are native Remotion. No stock footage, no still photography, no
paid generation. Composition ids are registered in the isolated toolkit's
`runtime/remotion/src/Root.tsx`.

| Beat | Act | Duration (s) | Composition | Motion / show note |
|---|---|---|---|---|
| B00 | ASK — cold open | 15.00 | ClaudeComposerAsk | Composer types the ask about the fashionista skill; send arms terracotta; three result lines fade in. |
| B01 | BLUF — hesitant writer | 15.23 | BrutalistHesitantWriter | 4-line serif types out; `tutorial` flashes terracotta then swaps to `experiment`; corrected sentence stands. `lead_silence_s: 0.8` written on the beat per the ai-explainer contract. |
| B02 | FRAMEWORK — anatomy | 27.01 | SkillTeardownAnatomy | Folder tree of `skills/make/fashionista/` reveals row by row; callout notes the CALLS.json artifact. |
| B03 | FRAMEWORK — pipeline | 25.47 | SkillTeardownPipeline | Three-node horizontal flow: INTRO → THE VIDEO (accent) → OUTRO; INPUT = source video, OUTPUT = one trial · one CALLS row. |
| B04 | MECHANISM 1 — GATE ASK | 21.06 | SkillTeardownMechanism | Heading + body + verbatim quote from SKILL.md ("NEVER name the garment in the ask…"). |
| B05 | MECHANISM 2 — Video is the master clock | 24.75 | SkillTeardownMechanism | Heading + body + verbatim quote ("Video is the master clock. If the narration runs long: CUT WORDS. The video does not move."). |
| B06 | MECHANISM 3 — Stated confidence | 26.90 | SkillTeardownMechanism | Heading + body + verbatim quote ("Hedging is content, not weakness…"). |
| B07 | FALSIFIABILITY — Two error sources | 25.45 | SkillTeardownMechanism | Heading + body + verbatim quote ("Nobody else is doing this and it is the most interesting thing the series does."). |
| B08 | DESIGN TELL — CALLS ledger | 28.52 | SkillTeardownMechanism | Heading + body (schema fields) + verbatim quote about the null verdict slot. |
| B09 | VERDICT | 28.65 | ClaudeVerdictArtifact | Artifact card, 6 verdict lines revealed one at a time. |
| B10 | YOUR TURN — handoff | 34.05 | ClaudeComposerAsk | greeting `Your Turn`; the paste-ready dry-run planning prompt types in; three-line viewer rubric as output. Liam reads and discusses. |
| B11 | OUTRO | 3.67 | ClaudeTitleOutro | Title "The fashionista Skill." + hardcoded `@NikBearBrown` handle (OUTRO-LOCK.md) + slug-seeded mascot. Liam signs off. |

Master duration (sum of `render_duration_s`): ≈ 275.7 s (≈ 4:36).

## Timing notes

- Every duration above is the `actual_duration_s` measured from the Kokoro
  MP3, not an author estimate. See `mp3/beat-B*.mp3`.
- No slates, no hand-added media, no Manim, no external footage.

## No captions

Confirmed by `metadata.captions: false` and by the absence of any subtitle
track, karaoke component, or SRT/VTT file. Body beats teach through legible
labels, diagrams, and short quoted lines — not transcript overlays.
