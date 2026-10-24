---
name: blender-modelbuild
description: Write a Liam-narrated film beat sheet for a finished Blender model. The film first shows the model from every angle (front, side, rear, top, three-quarter hero, details), then teaches how a person would build it from scratch in Blender, using the real build evidence (scripts, params, rounds, compare sheets, measurements). Separates what the AI script did from reconstructed hand steps in the Blender UI, includes the human-in-the-loop verdicts, and names what the evidence does not establish. Outputs beat sheets only; does not render, voice or publish.
---

# blender-modelbuild — how would you build this by hand?

```text
blender-modelbuild /path/to/model-folder
blender-modelbuild /path/to/model-folder --round r15
```

This is an agent-driven beat-sheet writer, not a renderer and not a generic
Blender tutorial. The model folder is the published package: renders, compare
sheets, build scripts, params, notes and the `.blend`/`.glb`. Write every output
to `<model-folder>/film/`. Preserve the model, its pages, renders and any user
edits. Writing a beat sheet does not authorize changing the model, rendering,
voicing, uploading or publishing. The human renders the film with other tools.

Read [ai-explainer](../ai-explainer/SKILL.md) for the voice chassis and
[riff](../riff/SKILL.md) for evidence-led commentary. This skill owns the middle:
real build evidence replaces generic "make a spaceship" tutorial steps. Real
renders and compare sheets are evidence, not placeholders to redraw.

## Views first, then the build is the teaching unit

Open on the finished model and walk around it the way the model page does:
three-quarter hero, side, front, rear, top, then the detail close-ups. Every
view beat points at an existing image in the model folder. Only then teach.

The teaching question is: **if a person wanted to build this model from
scratch in Blender, how would they do it?** Each build beat pairs two things:

1. **What the AI did** — the actual build script and params: which primitives,
   lofts or lathes, which modifiers, which numbers. Cite the file. Never invent
   a modifier, value or step the script does not contain.
2. **How a person would do it by hand** — the equivalent steps in the Blender
   UI. These are reconstructions. Label them on screen **"Blender UI
   reconstruction (hypothetical, not a recorded session)"** and record them in
   `ui_steps`. Where the script did something a person would not (a loop over
   `side in (1, -1)` instead of a Mirror modifier), say so; that contrast is the
   lesson.

Cover, in this order: blockout and primitives; proportions from references,
blueprints or measurements; the order of the major parts; modifiers (mirror,
bevel, subdivision, boolean, solidify, screw: what was used and what was not);
materials; lighting and camera; checking against the references; export to
`.glb`. See [teaching-arc.md](references/teaching-arc.md) for the required acts
and the AI-versus-hand mapping.

## Read the whole build

Read the README, BUILD_NOTES, every build/render/compare/export script, the
params file and the compare sheets before writing. Read
[evidence.md](references/evidence.md) before producing the ledger. Where a
number matters, take it from params, notes or a measurement file; do not round
it into a familiar tutorial value. Distinguish built, measured, eyeballed and
proposed. If the folder has no round images, say the rounds from the notes and
show the compare sheets that exist; do not fabricate round renders.

## The human in the loop

The film's theme is humans and AI working together. Include the rounds, the
AI's self-scores and every human verdict. Quote the human's notes as
**"Professor Bear said …"**, word for word from the record. If a verdict is
pending, say it is pending. If the AI made a mistake that cost a round, say
whose mistake it was. Two scores from two judges are a feature, not a conflict
to smooth over.

Name at least one thing the evidence does not establish (a camera matched only
by eye, an assumed angle, an identification by shape, the hand steps never
being timed). The checker requires it.

## Narration and structure

Narrator: **the Liam voice** only. Opening line starts "This is Liam."; the
closing beat is "Grok Bot, Built. This is Liam." over a card that reads
**"Narration: the Liam voice"**. Viewers only ever see or hear "the Liam
voice". Never write a TTS product name, voice id, engine or speed in any output
file, card or line. No subtitles, no captions, no `.srt` or `.vtt`.

Write the visible sequence before the narration. One idea per beat; split dense
beats. Spell out what a voice must say ("G L B", "dot blend"). Duration follows
the words: estimate `words / 3.0 + 0.4` seconds per beat; real timing comes from
the rendered audio later (`actual_duration_s` stays `null`).

## Build and finish

Write into `<model-folder>/film/`:

- `beat_sheet.json` — the machine file, brutalist `beat_sheet.schema.json`
  compatible plus this skill's fields (see teaching-arc.md).
- `beat_sheet.md` — the human-readable table, generated with
  `python3 scripts/beat_sheet_md.py <film-dir>`.
- `modelbuild-evidence.json` — the hashed source ledger (evidence.md).

Shot asset paths are relative to `film/` (for example
`../compare/r15_sheet.jpg`) and must point at real files in the model folder.
No video, audio or caption files go in `film/`.

Run the read-only gate before handing off:

```bash
./art blender-modelbuild --check /path/to/model-folder/film
```

It checks schema shape, act order, view coverage, asset paths, hashes,
reconstruction labels, human-verdict quotes, the not-established beat, the
closing card and banned voice/caption terms, and prints the beat count and
runtime estimate. It cannot judge whether the teaching is clear or true.
Report the beat count, the runtime estimate and the gate result. Do not render,
voice, upload or publish unless separately requested.
