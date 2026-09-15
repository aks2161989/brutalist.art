# SCRIPT — The duration-planner Skill

Voice: Kokoro `am_onyx` (Liam, in for Bear). Register: Teardown.
All narration in this file matches `beat_sheet.json` verbatim.

## B00 — ASK (cold open)

> Sawadee, this is Liam, in for Bear. Today we tear down a skill that answers
> a question every fellow keeps hitting: how long should this video be? The
> honest answer is you don't decide. The content decides. The skill is called
> duration-planner, and here is how it actually works.

## B01 — BLUF (BrutalistHesitantWriter)

> The easy assumption is that duration is a target you hit — thirty seconds,
> one minute, five. The skill argues the opposite. Duration is an output. You
> size the script and let the content sit for the time it needs to land.
> Everything else is production convenience or padding.

Trigger word: `target` → `output` (single-token per BrutalistHesitantWriter
contract). Correction reads: "Duration is a[n] output" — the reel's actual
claim, not a synonym swap. `lead_silence_s: 0.8` written on the beat so the
typing has room before the voice enters.

## B02 — FRAMEWORK (anatomy)

> A skill is a folder Claude reads first. The duration-planner folder is small.
> One SKILL file. One short reference file with the evidence and the
> floor-ceiling table. One advisory script that reads timings and reports.
> That's it. The doctrine is short because the discipline is what does the
> work — and the discipline is refusing to treat duration as a target.

## B03 — FRAMEWORK (pipeline)

> Here is the pipeline. Every beat carries a content_type set at storyboard
> time. Storyboard becomes the master clock when Kokoro measures the
> narration. The skill reads those two together against a floor table: if the
> narration is below its content_type's floor, recommend a hold. If it is over
> the ceiling, recommend a split. Total runtime is what falls out. The skill
> reports it and stops.

## B04 — MECHANISM · ACT 1 (the thesis)

> First design decision, and it's the thesis. Quote from the SKILL file:
> duration is an output, never a target. A complex mechanism lands at three or
> four minutes. A definitional explainer at thirty to sixty seconds. Both are
> correct. A uniform target has no learning basis — it's a production
> convenience that either compresses the content and destroys integration, or
> pads it and adds extraneous load. Either way, learning fails.

## B05 — WORKED_EXAMPLE (the consolidation floor)

> Second decision. Every beat has a content_type, and each content_type has a
> consolidation floor — the minimum time working memory needs to register the
> new element before the beat cuts. A title beat needs three to five seconds.
> A structure or geometric beat, six to eight. A mechanism step, six to ten.
> An equation step, seven to twelve. If your narration lands under the floor,
> don't shorten the next beat and don't speed up the voice. Add a hold.

## B06 — MECHANISM · ACT 3 (holds are automatic)

> Third decision. Holds are now automatic. The scene base applies a
> HOLD_FLOOR: after each beat's narration it holds the final frame up to the
> content_type floor. The compile step pads that beat's audio with matching
> silence, so audio and video stay in sync. You can turn it off per video with
> hold_floor false in the metadata. The load-bearing detail: re-render and
> re-assemble together — both read the same pacing table, and rendering with
> one setting while assembling with another desyncs the reel.

## B07 — FALSIFIABILITY (padding is a coherence violation)

> Here is where the skill bites. Once the idea has landed, adding decorative
> motion or filler graphics to reach one minute is a coherence violation —
> extraneous load that degrades learning. Padding to hit thirty seconds is
> exactly as wrong as compressing to hit it. And the six-minute engagement
> rule everyone quotes? That's a watch-time finding from open MOOCs. It
> doesn't replicate in real courses, and it isn't a learning result. The trade
> the skill accepts: shorter watchtime, cleaner schema.

## B08 — VERDICT (artifact card)

> The verdict. The duration-planner skill is small on disk and long on
> discipline. Content_type drives the floor. Kokoro drives the clock. Holds
> land the beats. Splits break up over-full ones. Total runtime is a byproduct
> — the skill reports it and stops. And it refuses to pad or compress to hit
> a number production wanted for its own convenience.

## B09 — YOUR TURN (handoff, paste-ready prompt)

> Your turn. Paste this into Claude Code inside your own reel folder: run the
> duration-planner skill on my beat sheet and timings. For every beat, tell me
> the content_type, the floor, the measured narration, whether it needs a
> hold, and whether any beat is over its ceiling and should split. Report
> total runtime as an output, and do not edit the sheet. Then check three
> things. Are the below-floor beats getting holds, not shorter next beats? Is
> any over-ceiling beat one idea or two? And is anything padded to hit a
> target? If yes, cut the padding — don't ship the coherence violation.

Prompt is read aloud verbatim; the three-check rubric under it is discussion
of *what the viewer should look for*, satisfying HANDOFF LAW's read-and-discuss
requirement.

## B10 — OUTRO

> That was the duration-planner Skill. Liam, in for Bear.

Title restated; `ClaudeTitleOutro` locks `@NikBearBrown` (OUTRO-LOCK.md) and
seeds the mascot animation from the slug.

---

## Measured audio durations (Kokoro am_onyx, is-the-clock)

| Beat | Duration (s) |
|---|---|
| B00 | 14.57 |
| B01 | 15.00 |
| B02 | 18.79 |
| B03 | 20.16 |
| B04 | 21.70 |
| B05 | 22.51 |
| B06 | 25.86 |
| B07 | 24.32 |
| B08 | 18.58 |
| B09 | 28.57 |
| B10 | 3.95 |
| **Total** | **~213.99 s (3:34)** |

Landing in the 3–4 minute band the SKILL.md predicts for a multi-decision
mechanism teardown. Not padded to hit a round number.
