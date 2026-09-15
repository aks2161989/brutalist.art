# Script — The fashionista Skill (Short cut)

Derivative Short of the full portrait reel
`claude-liam-brutalist-skill-fashionista` (see `CUT-PLAN.json` for the cut
strategy). Eight kept beats, native portrait 2160×3840, Kokoro `am_onyx`,
no captions, no publishing. Measured 160.83 s.

## B00 — ASK · cold open (15.00 s)

> Hallo, this is Liam, in for Bear. Today we tear down the fashionista skill.
> Read the name and you expect a fashion series. It is not. It is an experiment
> about AI describability, running one trial per episode, and you are the
> scoring function. Here is the mental model.

## B01 — BLUF · hesitant writer (15.25 s)

> The easy read — the one the name invites — is that this is a fashion
> tutorial. It is not. Fashionista is a confidence experiment. Every episode is
> one trial. You are the judge. The whole machine exists to log one row of
> guesses and their confidences, then wait for you to correct them.

## B04 — MECHANISM 1 · GATE ASK (21.08 s)

> First design decision, and it is the sharpest. GATE ASK — the cold-open ask
> never contains the garment name. The default is `Hey Claude, what is she
> wearing?` or `Hey Claude, what is he wearing?` — that pattern, nothing more.
> If the ask text contains any garment term from the beat sheet, the build
> fails. The naming is the AI's job, on camera. That rule guarantees the video
> is a real test — the answer cannot leak into the question.

## B05 — MECHANISM 2 · Video is the master clock (24.75 s)

> Second design decision. Every other skill in this toolkit is audio-first —
> the narration is generated, then the visuals conform to it. Fashionista
> inverts that law and says so in every build log. The video is the master
> clock. Extract frames first, build a motion timeline — what happens at what
> second. Write the call against that timeline. And if the narration runs
> long — do not stretch the clip, do not loop it, do not freeze-pad it, do not
> slow it. Cut words. The video does not move.

## B06 — MECHANISM 3 · Stated confidence (26.92 s)

> Third decision. The register is sports announcer with stated confidence.
> Present tense. Short sentences. Energy. And every garment term is spoken with
> a confidence the viewer can hear. `That's a sherwani — I'm confident.` Or:
> `I want to say lehenga, but the length is fighting me on that.` Hedging is
> not weakness. It is the content. And when the announcer catches themselves
> reaching for the famous word over the precise one — lehenga, kimono, kaftan,
> blazer — they name that failure mode out loud. That is the honest signal the
> audience is scoring.

## B07 — FALSIFIABILITY · Two error sources (25.46 s)

> Falsifiability, and this is where the skill earns its keep. These are
> generated garments. So a wrong episode can be wrong in two distinct ways.
> Generator error — the render shows something no real garment of that type
> does. The image is wrong. Describer error — the render is coherent and the
> name is wrong. The call is wrong. When they are separable, the announcer says
> which one. When they are not, they say that too. Nobody else in AI video
> separates those two lanes, and that is the most interesting thing this series
> does.

## B09 — VERDICT · artifact card (28.67 s)

> The verdict. Fashionista is an experiment, not a fashion series. Every
> episode is one trial. The audience is the scoring function, and the
> uncertainty is the subject. Gate ask keeps the answer out of the question.
> Video is the master clock. Every garment term is spoken with stated
> confidence — hedging is content. And two stacked error sources — generator
> versus describer — get logged in a CALLS.json ledger with a verdict slot
> waiting for you. Skip the correction ask and the loop evaporates. Do it well
> and the series has something to falsify.

## B11 — OUTRO · title lock (3.71 s)

> That was the fashionista Skill. Liam, in for Bear.

## Dropped from the long

- B02 (skill-folder anatomy) — generic skill-teardown scaffolding.
- B03 (three-beat pipeline) — structural setup covered elsewhere.
- B08 (CALLS.json ledger schema walk-through) — condensed into B09's verdict.
- B10 (Your-Turn extended paste-in) — 34 s handoff belongs in the long.

Reference the 16:9 long for the full anatomy, pipeline, CALLS-ledger deep dive
and Your-Turn dry-run.
