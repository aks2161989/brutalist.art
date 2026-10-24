---
name: blender-walkthrough
description: Make a narrated Brutalist film touring a finished Blender model through its existing rendered images, gallery or video frames, with source-backed stats, details and limitations. Use for a film version of a model's HTML/README gallery; no model file or new Blender renders required. For teaching how to recreate a similar model from images, use blender-build.
---

# blender-walkthrough — the finished model, shown through its images

```text
blender-walkthrough /path/to/model-gallery/
blender-walkthrough https://github.com/owner/repo/tree/main/model-folder
blender-walkthrough /path/to/rendered-images/ --stats /path/to/audit.json
```

An agent-driven film workflow. `./art blender-walkthrough --help` displays this
skill; invoking `./art` does not itself generate a film. The source is the
**images rendered from a model**, not the `.blend`, `.glb` or STL files. An HTML
review page is the editorial outline: forward quarter, side, rear, top, front,
close-ups, statistics and known limitations, adapted to what actually exists.

This skill tours the result. [blender-build](../blender-build/SKILL.md) teaches
how a learner could make something similar from those images. The separate
[building-walkthrough](../building-walkthrough/SKILL.md) renders a measured camera
route from a model file; do not invoke it merely because this film needs motion.

## Read for production

Use [lecture](../lecture/SKILL.md) for Brutalist's narrated opening, measured
Liam audio, recap, Your Turn and channel outro. Read the toolkit's `CLAUDE.md`,
[render targets](../../../RENDER-TARGETS.md),
[pipeline safety](../../../docs/PIPELINE-SAFETY.md) and
[outro lock](../../../OUTRO-LOCK.md) before making the film. The body here is a
visual tour, not a lecture about the toolkit. Default voice: Liam in for Nik Bear
Brown, local Kokoro `am_onyx`, default channel `@NikBearBrown`. Follow a user-specified
channel through the existing channel rules. Free production by default; no upload
or paid generation is implied.

## Gather the actual evidence

- Resolve the gallery's original image assets; prefer full-size renders to page
  screenshots or thumbnails. A local gallery, GitHub images, a supplied video or
  accessible YouTube frames are all valid starting points. Preserve source URLs,
  repository revision when available, video timestamps and local filenames in
  `SOURCES.md`; keep image copies in the reel for a reproducible cut.
- Inspect every selected view. Record its actual viewing direction, resolution,
  what it reveals and any crop. Do not trust filenames blindly, mirror asymmetric
  features to fake the opposite side, or call a perspective image orthographic.
- Use the README, audit or build notes for counts, dimensions, units, material
  and texture status, Blender version, rig/animation state, authorship and review
  verdict. Label numbers as **reported by that source**, tied to its revision.
  Rendered pixels cannot establish polygon counts, topology or physical size.
  If numbers conflict, explain the discrepancy or omit them; do not silently
  select the most attractive figure. Missing stats do not block an image tour.
- No model access is required. Do not open the original scene or recompute its
  statistics as a prerequisite. If a useful angle is missing, use what exists
  and disclose the limitation; do not invent an unseen view with AI imagery.

## Turn the gallery into a film

Write `WALKTHROUGH.md` with the central observation, credits, source-backed stats
and a concise description of what the finished model includes and leaves out.
Write `SHOTLIST.md` mapping each narrated claim to an image and visible region.
A useful order is establishing quarter view → side silhouette → rear structure
→ top/front relationships → selected detail close-ups → limitations and recap.
Adapt the order to the subject and available images; avoid repeating a view just
to fill a fixed number of beats.

Each body beat should answer **where to look, what is visible, why it matters**.
Introduce stats when they explain the work: for example, mesh count describes
separate objects, triangle count describes geometric density, and a static
assembly does not demonstrate working hinges. Distinguish materials from image
textures and a model's chosen scale from the real subject's size. Do not turn an
unverified number into a claim of performance or production readiness.

Use the actual rendered images as the visual body: whole-object framing,
restrained pan/zoom, detail crops, labels, arrows and side-by-side comparisons.
Keep labels outside the feature being discussed. Still-image motion is an edit,
not an orbit or proof of 3D depth. Never synthesize intermediate views, animate a
hinge from a still as if tested, or replace evidence with a prettier generated
model. Enlarging a small source into a 4K master does not add source detail.

Show limitations in the image that illustrates them, without presenting every
difference from another design as an error. Preserve the distinction between
original geometry authorship, assembly/material work and film production. A
human-review status remains pending until there is an actual verdict.

## Produce, check and deliver

Search the existing scene library before composing beats and read the chosen
composition's props. Image evidence is the subject; do not replace it with a
text-card slideshow. Follow the SVG selection workflow only when additional
illustrations/icons are actually needed. Generate and measure narration before
setting shot durations. Use the existing Brutalist render/compile tools and
inspect real frames for clipping, labels, crop accuracy and legibility; listen
for whether speech points to the feature currently visible.

Check the source mapping, numerical claims, view coverage, credit, limitations,
opening and closing against the actual cut. Report unperformed checks honestly.
A film passes editorial review only when the viewer can locate the features and
understand what the model does and does not demonstrate.

Output to the model/project's own `youtube/<slug>-walkthrough/`, or the user's
chosen destination. If starting from remote images alone, create a local project
folder. Deliver the rendered film, narration/captions, `SOURCES.md`,
`WALKTHROUGH.md`, `SHOTLIST.md`, beat sheet and QC results. Link the public
reference gallery in the description when available. A plan is not a rendered
film; clearly identify any remaining production blocker. No publishing is implied.
