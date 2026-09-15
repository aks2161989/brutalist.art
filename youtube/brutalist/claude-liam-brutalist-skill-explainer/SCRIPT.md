# SCRIPT — The explainer Skill

Voice: Kokoro `am_onyx` (Liam, in for Bear). Register: Teardown.
All narration in this file matches `beat_sheet.json` verbatim.

## B00 — ASK (cold open)

> Aloha, this is Liam, in for Bear. Today we tear down the skill every other
> explainer inherits from — the one just called `explainer`. Not the AI cut,
> not the CLI cut, not the deep cut. The parent. What is it, really? And how
> does it decide what ends up on screen? Here is the mental model.

## B01 — BLUF (BrutalistHesitantWriter)

> The easy mistake — the one every fellow makes first — is thinking Vox is a
> look. Cream paper, editorial serif, hand-drawn ring. It is not. Vox is a
> pipeline. It laundered any source you throw at it — an archive photo, a
> Manim fragment, a public-domain reel — through one treatment. Sources
> never match. The treatment does. That is why the film reads as one film.

Trigger word: `style` → `pipeline` (single-token per BrutalistHesitantWriter
contract). Correction reads: "The explainer skill is a pipeline." — the
reel's actual claim, not a synonym swap. `lead_silence_s: 0.8` written on
the beat so the typing has room before the voice enters.

## B02 — FRAMEWORK (anatomy)

> First, a skill is a folder Claude reads before working. The explainer
> folder is bigger than most because it governs everything downstream.
> SKILL.md is the doctrine. MOTION.md holds the pantry of seven motion
> languages. REMOTION.md is the annotation-plane spec. EQUATIONS.md is the
> equation-tangent template. The scripts folder is the runtime belt — the
> audio maker, the pantry cropper, the compiler, the outro machine. Every
> other explainer extends this file.

## B03 — FRAMEWORK (pipeline)

> Here is the pipeline. Script becomes beats. Beats become a Kokoro
> voiceover — free, local, and the master clock. Then media flows in per
> beat from four sources: Manim fragments, treated stills over Ken Burns,
> public-domain footage, and Remotion annotations. Compile conforms every
> slot to the audio window and hands out one watchable master. That is the
> whole loop. Anything else is a modifier on top of it.

## B04 — MECHANISM · ACT 1 (the laundering function)

> First design decision, and it is the thesis. Quote from the SKILL file:
> Vox is not a style, it is a laundering function. Any source you feed it —
> an archival photo, a FLUX still, a public-domain reel, a Manim fragment,
> a Remotion card — passes through one treatment. Desaturate about eighty
> percent. Contrast raised to about one-point-fifteen. Seated on a real
> newsprint scan. That is why mixed media reads as a single film. The
> sources never match. The treatment does.

## B05 — WORKED_EXAMPLE / MECHANISM · ACT 2 (two axes)

> Second decision. Every beat has two independent tags. Shot dot type is
> the presentation form — is it a still, a piece of footage, a document, a
> graphic, a composite, or a title card. Type gets locked at the plan gate
> and never changes. Shot dot source is the provenance — did it come from
> an archive, an AI generator, or your own file. Source is late-bound and
> swappable. Collapse the two and every media swap becomes a re-edit.
> Separate them and swaps are free. Drop a new file in media, the reel
> rebuilds, only that slot recompiles.

## B06 — MECHANISM · ACT 3 (the slot contract)

> Third decision — the slot contract. Every beat on the timeline is one
> conformed per-beat mp4. The precedence at compile is: a hand-added mp4 in
> media beats a Manim mp4 in manim beats a still image with Ken Burns
> beats a slate. That means the very first pass is always a watchable
> film. A slate is a standard production stand-in, not a bug — it says
> fill this slot later. Change a slot's input and only that clip
> recompiles. The rest of the reel is byte-for-byte identical. That is why
> swaps cost nothing.

## B07 — FALSIFIABILITY (VOX LAW + EXECUTABLE-EVIDENCE.md)

> Here is where the skill bites. VOX LAW: a still exists for exactly one
> reason — the still IS the evidence. The actual record the argument turns
> on. The updated skill adds a sharper edge. If your evidence is locally
> reproducible — a table, a chart, a test run, code output — execute it
> and render it. A terminal photograph is decoration. The running output
> is the evidence. Princeton's actual admissions record — yes. A stock
> photo of a university — no. The test: could this still be swapped for
> any other still of the same subject without changing what the beat
> proves? If yes, it is decoration. Cut it.

## B08 — VERDICT (artifact card)

> The verdict. The explainer skill is the chassis every other explainer
> bolts onto. It is a compositing pipeline, not a style. The Kokoro
> voiceover is the master clock, and free. The two-axis shot system
> separates presentation from provenance so swaps stay cheap. The slot
> contract makes the first pass a watchable film with slates. And VOX LAW
> keeps every still that reaches the timeline load-bearing. Do this well,
> and mixed media reads as one film. Break the last rule, and you shipped
> a slide show.

## B09 — YOUR TURN (handoff, paste-ready prompt)

> Your turn. Paste this into Claude Code inside a fresh reels folder: run
> slate cut on the concept — write a short script, plan the beats,
> generate Kokoro audio, and produce a watchable review cut with slates in
> every human-media slot. Then read the film back and check three things.
> Does every body beat have a specific job — a comparison, a mechanism, a
> claim on screen — that only that beat can do? Is every planned still a
> piece of evidence, not atmosphere? And if you swapped any one still for
> another of the same subject, would the beat still prove what it claims?
> If it would, cut that still and let a Remotion or Manim beat carry the
> idea.

Prompt is read aloud verbatim; the three-check rubric under it is
discussion of *what the viewer should look for*, satisfying HANDOFF LAW's
read-and-discuss requirement.

## B10 — OUTRO

> That was the explainer Skill. Liam, in for Bear.

Title restated; `ClaudeTitleOutro` locks `@NikBearBrown` (OUTRO-LOCK.md)
and seeds the mascot animation from the slug.

---

## Measured audio durations (Kokoro am_onyx, is-the-clock)

| Beat | Duration (s) |
|---|---|
| B00 | 15.42 |
| B01 | 18.84 |
| B02 | 23.82 |
| B03 | 21.70 |
| B04 | 22.53 |
| B05 | 29.27 |
| B06 | 28.50 |
| B07 | 30.59 |
| B08 | 26.71 |
| B09 | 32.58 |
| B10 | 3.48 |
| **Total** | **~253.63 s (4:14) — compile-writeout 253.67 s** |

B07 was regenerated 2026-09-11 (+1.09s) to cover the EXECUTABLE-EVIDENCE.md
addition to VOX LAW. Landing just above the 3–4 minute band the sibling
duration-planner SKILL predicts for a mechanism teardown with five design
decisions covered. Not padded to a round number; the compile pads audio to
match render frames by fractional seconds.
