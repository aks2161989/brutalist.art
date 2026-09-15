# The fashionista Skill — script

Slug: `claude-liam-brutalist-skill-fashionista`
Voice: Liam (in for Bear), Kokoro `am_onyx`, free.
Playlist: Brutalist · @HumanitariansAI.
Register: Teardown (skill-teardown modifier).
Source: `skills/make/fashionista/SKILL.md` (isolated-toolkit SHA-256 22614f44…; supervisor's episode.source_sha256 1b129e85…).

---

## The one sentence

`fashionista` is not a fashion series. It is an experiment in AI describability
run as a repeatable one-trial reel, where the AUDIENCE is the scoring function
and hedging is the interesting content.

## Misconception the hesitant writer fixes

Everyone reads the word "fashionista" and expects a fashion tutorial — a
walkthrough of a look. This skill is the opposite. The writer types
"fashion tutorial", flashes it terracotta, corrects it to "confidence
experiment", and the corrected sentence stands: "Fashionista is a confidence
experiment. Every episode is one trial. You are the judge."

## Beats

- **B00 · ASK** — ClaudeComposerAsk. Greeting `Hallo, Liam`.
  Command: `What is the fashionista skill? Read skills/make/fashionista/SKILL.md and tell me what it is really testing.`
  Result output: three lines — "an experiment, not a series", "the audience is the scoring function", "hedging is the content".
  Narration introduces Liam in for Bear and previews the film's claim.

- **B01 · BLUF (hesitant writer)** — BrutalistHesitantWriter. Types
  "Fashionista is a fashion tutorial. / Every episode is one trial. / You are the judge."
  Single-token trigger `tutorial` → `experiment`. After correction the sentence stands as the reel's claim.
  Narration reads the corrected framing and drops the stakes: this whole video
  is a piece of falsifiability infrastructure.

- **B02 · FRAMEWORK — anatomy** — SkillTeardownAnatomy on the fashionista folder.
  Files: `SKILL.md` (doctrine · terracotta accent), the eight gates, and the
  data artifacts (CALLS.json, media/B01.mp4, media/B02.mp4). Callout notes that
  the skill's contract is the CALLS.json ledger — the machinery exists to
  produce one row of it per episode.

- **B03 · FRAMEWORK — pipeline** — SkillTeardownPipeline: three-beat structure.
  INPUT: a source video. Phases: INTRO (ClaudeComposerAsk — the ask, never
  naming the garment), THE VIDEO (full-frame source, Liam's call over it,
  corner stamp only), OUTRO (ClaudeTitleOutro — spoken correction ask). OUTPUT:
  one trial + a CALLS.json row awaiting a verdict. Total runtime = clip
  duration + ~5 s. Video is the master clock.

- **B04 · MECHANISM 1 — GATE ASK** — SkillTeardownMechanism. The cold-open ask
  is the pattern `Hey Claude — what is she wearing?`. It NEVER contains the
  garment name — the naming is the AI's job, on camera. If the ask contains
  any garment term from the beat sheet, the build fails. This is the skill's
  cleanest design decision: the ask is legible in the title, legible in the
  first two lines of the description, and enforced by a gate.
  Quote: "The naming is the AI's job, on camera."

- **B05 · MECHANISM 2 — VIDEO IS THE MASTER CLOCK** — SkillTeardownMechanism.
  This skill inverts the parent's audio-first law and says so out loud in
  every build log. Write the commentary TO FIT the footage. Never stretch,
  loop, freeze-pad, or slow the video. Extract frames first, build a motion
  timeline, write the call against that timeline. If the narration runs
  long: cut words. The video does not move.
  Quote: "Video is the master clock. If the narration runs long, cut words."

- **B06 · MECHANISM 3 — STATED CONFIDENCE** — SkillTeardownMechanism. Present
  tense. Short sentences. Every garment term is spoken with a confidence the
  viewer can hear. "That's a sherwani — I'm confident." Or: "I want to say
  lehenga, but the length is fighting me on that." Hedging is not weakness —
  it is the content. The failure mode the announcer names out loud when
  caught: reaching for the famous word over the precise one.
  Quote: "Hedging is content, not weakness."

- **B07 · FALSIFIABILITY — TWO ERROR SOURCES** — SkillTeardownMechanism. A
  wrong episode can be wrong in two distinct ways. GENERATOR ERROR: the render
  shows something no real garment of that type does — the image is wrong.
  DESCRIBER ERROR: the render is coherent and the name is wrong — the call is
  wrong. When separable, say which one. When they are not, say that too. This
  is the falsifiability the series depends on; without it the experiment
  collapses to a fashion channel with commentary.
  Quote: "Nobody else is doing this and it is the most interesting thing the series does."

- **B08 · DESIGN TELL — the CALLS ledger** — SkillTeardownMechanism. Every day
  writes `books/fashionista/<date>/CALLS.json` — one row per garment term
  claimed. Term, confidence, reasoning, timestamp, alternatives considered,
  and a VERDICT slot that stays `null` until a human fills it from comments.
  This is why the outro's spoken correction ask is mandatory: without the
  correction feed, the verdict slot never fills, and the correction loop
  evaporates. The ledger is the artifact the skill exists to produce.
  Quote: "The verdict slot stays null until a human fills it from comments."

- **B09 · VERDICT** — ClaudeVerdictArtifact. Six lines:
  1. `fashionista` is an experiment, not a fashion series. Every episode is one trial.
  2. The audience is the scoring function. The uncertainty is the SUBJECT.
  3. GATE ASK: the cold-open ask NEVER names the garment.
  4. Video is the master clock. Write commentary to fit the footage.
  5. Every garment term is spoken with stated confidence — hedging is content.
  6. Two error sources — generator vs. describer — logged in a CALLS.json ledger.

- **B10 · YOUR TURN** — ClaudeComposerAsk, `greeting: Your Turn`. Paste-ready
  Claude Code prompt Liam reads aloud and discusses. The prompt asks Claude to
  do a dry-run planning pass: read the fashionista SKILL, draft an ask that
  never names the garment for a hypothetical portrait clip, write a candidate
  CALLS.json row (term, confidence, reasoning, alternatives, verdict:null),
  and tag which of the two error sources would matter most for that garment.
  Output lines: three checks the viewer applies to Claude's answer.

- **B11 · OUTRO** — ClaudeTitleOutro. "The fashionista Skill." Handle
  (locked @NikBearBrown from OUTRO-LOCK.md). Liam signs off: "Liam, in for Bear."

## Registered composition names (verified via `./art scenes --check`)

Landscape 16:9 (all RENDERABLE at time of authoring):
- `ClaudeComposerAsk`, `BrutalistHesitantWriter`, `SkillTeardownAnatomy`,
  `SkillTeardownPipeline`, `SkillTeardownMechanism`, `ClaudeVerdictArtifact`,
  `ClaudeTitleOutro`.

Portrait 9:16:
- `ClaudeComposerAsk916`, `BrutalistHesitantWriter916`, `ClaudeVerdictArtifact916`,
  `ClaudeTitleOutro916` — all RENDERABLE at authoring time.
- `SkillTeardownAnatomy916`, `SkillTeardownPipeline916`,
  `SkillTeardownMechanism916` — NOT registered in the live library. Authored
  as new wrappers in this isolated toolkit's Root.tsx, using the same source
  components with portrait-adapted layouts (stacked pipeline, larger type,
  narrower body). Never committed to the live library.

## What we do NOT do in this reel

- No live fashion generation, no source video (no NN Higgsfield calls). This
  reel EXPLAINS the fashionista skill; it is not itself a fashionista episode.
  The demo of the CALLS.json ledger is source-backed: we show its literal
  schema from the SKILL.md, not an actual episode row.
- No captions, no subtitle tracks. Instructional labels only, per the
  playlist contract.
- No unresolved slates. Every beat is native Remotion.
- No paid APIs, no publishing.
