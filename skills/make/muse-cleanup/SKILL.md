---
name: muse-cleanup
description: >
  Clean up a film that Muse (Meta's Muse Spark model, or the Muse Code harness) drafted, BEFORE it ships.
  Muse's draft output is rough: Spark makes many mistakes, and its diagrams are the worst of them: boxes with
  nothing in them, a check mark under two blank panels, shapes that do not relate to the sentence being spoken.
  This skill is the second pass a human or Claude (or Codex) does on every Muse-drafted film: DIAGRAM CHECK (is each
  diagram informative and related to its narration?), FACT CHECK (every product claim attributed or sourced),
  VOICE CHECK (no antecedent-less pronouns, no first person, no "the transcript"), TYPE/LAYOUT CHECK (the usual
  gates), then a note-card pre-roll saying the film began as a Muse draft. Use when the user types `muse-cleanup`,
  `muse check`, or hands over a Muse-drafted beat sheet, scenes.py or film. Never publishes.
---

# muse-cleanup: the second pass on anything Muse drafted

**Why this exists (Bear, 2026-10-05).** Muse runs on a simple model, Spark, that makes a lot of mistakes. It is
fine for a rough draft; it is not fine for the finished thing. Cleaning up only the type and spacing is not
enough: a draft can pass every layout gate and still teach nothing. The example that started this skill is a
scene that asked "Could a non-technical person use it?" over two large blank boxes (labelled raw JSON and brief
card) and a check mark. Nothing in either box. No gate caught it because nothing overlapped. Muse's diagrams
generally do not relate to what is being said; that is the failure to look for first.

## The diagram check (the heart of this skill)

For every Manim/Remotion body scene, look at the LAST frame of its clip and the narration for that beat, and answer
all five. A scene that fails any one is rebuilt, not nudged.

1. **Is it informative?** Cover the narration. Does the picture alone say something specific and checkable (a
   number, a labelled flow, a real example of the thing, a before/after with content)? Blank containers, generic
   rectangles, a lone check mark or X, and "boxes with arrows" with no named things all FAIL.
2. **Does it relate?** Every shape, label and mark must map to a noun or claim in that beat's narration. A diagram
   that is merely on-topic (a flow chart in a beat about flow charts) fails if it does not show *this* beat's
   claim. Decoration that the voice never mentions is deleted.
3. **Does the motion carry the claim?** The thing the narration says happens (data filters down, a gate swings
   shut, a count rises) must be what moves, at the moment it is said. The still-frame test: if the last frame
   would make the same point as a bullet list, add the mechanism.
4. **Are the contents real?** Show the real artifact where one exists (the actual JSON keys, the actual brief
   text, the real number from the run), pulled from the film's own source files, never invented. If no real
   content exists, the beat's claim is not ready: attribute it, shorten it, or cut the scene.
5. **Could a non-technical viewer say what they learned?** One sentence. If they cannot, it fails.

Run the scanner first, it finds the blank-container cases cheaply: `python3 empty_diagram_scan.py <film-folder>`
(samples the last frame of every `manim/*.mp4`, flags large boxes with nothing inside). A flag is a prompt to look,
a clean scan proves nothing: you still apply the five questions by LOOKING at the frames (extract them with
ffmpeg and view them).

## The rest of the pass

- **Fact check.** Every Muse product fact, price, number, "Muse has/does X" is checked against the film's source
  files; if it is only the course's claim it is attributed ("the course reports"); if unsupported it is cut.
  Opinion about Spark's capability is attributed to the person who judged it ("in Nik's experience").
- **Voice check.** Name the person once ("Nik", the course instructor) before any "he"; no first-person narration;
  no "the transcript", "the research brief", "this chapter".
- **Layout and type.** The normal gates (A, W, B, V, T) must pass: `python3 muse/muse_film_preflight.py <film>`
  then `./muse/muse_film_build.sh <film>`.
- **The note.** A Muse-drafted film opens with the voiced note card (`muse/preroll/`): this film began as a Muse
  draft; Spark makes many mistakes; Claude cleaned it up; draft in Muse, finish in Claude or Codex; plus the
  useless-diagram example. Add the same note to the YouTube description.

## Output

`MUSE-CLEANUP.md` in the film folder, opening with a plain executive summary (what was wrong, what was fixed), then a
table: scene, narration, verdict on each of the five diagram questions, what changed. Never publish.
