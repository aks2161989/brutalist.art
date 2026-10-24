---
name: blender-build
description: Teach how to build a similar Blender model from finished renders, GitHub images or video screenshots, with a step-by-step film, Blender concepts and copyable coding-agent prompts. Defaults to an image-based reconstruction lesson, not the original build history; no original model, drawings or scripts required. Explicit record/history/build-breakdown requests retain the recorded-build workflow.
---

# blender-build — teach a build from the images

```text
blender-build /path/to/rendered-images/
blender-build https://github.com/owner/repo/tree/main/model-gallery
blender-build /path/to/video-or-screenshots/
blender-build /path/to/model-folder record   # explicit historical workflow
```

This skill makes a **teaching film and a usable reconstruction lesson**. Its
question is: “If a learner had these finished images and a coding agent, how
could they build something like this in Blender?” It is not, by default, a
retelling of how the original author or agent made the asset. The companion
[blender-walkthrough](../blender-walkthrough/SKILL.md) tours the finished result.

The primary evidence is the model's rendered images: quarter, side, rear, top,
front and details where available. Viewers may obtain them from the public
GitHub gallery or screenshots of the YouTube film. **Do not require the original
`.blend`, `.glb`, STL parts, private drawings, scripts or session logs**, even if
those happen to be locally available. Do not secretly import that geometry into
the demonstration. The lesson must still work for someone who only has images.

## Choose the right mode

Default to the **image-based lesson** below, including when a supplied project
folder also contains model files. A source file's presence is not a request for
an exact replay. Prefer “one way to construct a similar model” over “here is how
we built it.” Different topology and sensible alternative techniques are valid.

For an explicit original-build history, recording, replay, `record`, or
`build-breakdown` request, read
[recorded-build.md](references/recorded-build.md). That preserves the existing
tape, reconstruction guide, original-scene census and verification workflow.
The existing `--check`, `--draft`, `--guide` and `--tape` CLI utilities still apply
to that historical record format; they are **not** validators for this image
lesson. Do not impose signature equality, original build logs or original
source files on an image-based reconstruction.

## Gather references and state what can be known

Follow the image/source handling in
[blender-walkthrough](../blender-walkthrough/SKILL.md): inspect original render
assets, retain source links/revisions/timestamps, and keep selected image copies
with the lesson. Public links and frame timestamps must let a viewer locate the
same visual evidence; a local-only path is not a public learning resource. If no
public link exists, say so and provide the available image reference pack without
inventing a URL or claiming it has been uploaded.

Separate three kinds of statement in `BUILD-LESSON.md` and narration:

- **Observed:** silhouette, visible parts, color boundaries, repeated features.
- **Proposed:** a modeling approach, chosen working scale, hidden structure,
  material parameters, topology or modifier strategy inferred from appearance.
- **Demonstrated:** an operation actually run in a fresh Blender scene for this
  lesson, with its real result and validation.

A rendered seam may be geometry, a texture or lighting. A bevel, subdivision
stack, exact dimensions, interior or functioning joint cannot be recovered with
certainty from a picture. Explain the chosen solution without asserting it was
the original method. Original reported mesh/triangle counts describe the source
asset; the learner need not reproduce them and they are not a likeness metric.

## Build the teaching sequence

Create a sequence of achievable modeling checkpoints. Adapt to the subject;
use the following progression where it fits:

1. Read the images: axes, symmetry, major volumes, relative proportions and
   perspective ambiguity. Choose units and a clearly stated working scale.
2. Block out the silhouette with a few editable forms. Compare front/side/quarter
   views before adding detail; explain why a flattering angle can hide errors.
3. Shape the main surfaces: justify mesh editing, profiles, curves, extrusion,
   modifiers or procedural generation according to what the shape needs.
4. Add secondary forms and one repeated detail, then teach its duplication rule.
   Explain origins, local/world axes and transforms when they affect the result.
5. Add materials, trim and fine surface details after proportions hold. Teach
   shading/normals and bevel decisions where visible evidence calls for them.
6. Set lights and comparison cameras; inspect actual renders against the source.
   Demonstrate a useful correction and explain the evidence for it.
7. Save and export a sensible deliverable. Explain what an export retains,
   scale/units and what still needs testing. Treat rigging or moving mechanisms
   as a separate extension unless the lesson includes a real demonstration.

Every checkpoint needs: **goal → evidence image/region → Blender concept →
operation → coding-agent prompt → expected visible result → learner check →
correction prompt if the check fails**. Explain unfamiliar terms when introduced.
Include a practical manual Blender route alongside the prompt where feasible;
if raw mesh generation has no reasonable click-by-click equivalent, teach its
geometric principle and the script interface honestly. Do not dump a giant
script or a single “make this model” prompt and call that instruction.

Keep full prompts in `PROMPTS.md` for copying; in the film, show a readable
excerpt while explaining its intent and verification. Each prompt includes the
needed image references, current stage, requested change and success check.
The starter prompt must work in a fresh chat, without this conversation, hidden
local paths or the original asset. State what tools the learner's agent needs;
if it cannot control Blender, it can provide a script for Blender's Scripting
workspace or manual steps. Never imply an agent ran a tool without evidence.

Read [image-lesson-example.md](references/image-lesson-example.md) for a worked
prompt pattern based on a rendered spaceship. It is an example, not a mandate
that all subjects have hulls, fins or a particular polygon count.

## Make the film from evidence and teaching demonstrations

Use [lecture](../lecture/SKILL.md), the toolkit's `CLAUDE.md`,
[render targets](../../../RENDER-TARGETS.md),
[pipeline safety](../../../docs/PIPELINE-SAFETY.md) and
[outro lock](../../../OUTRO-LOCK.md) for production. Default: Liam in for Nik Bear
Brown, free local Kokoro `am_onyx`, measured narration, Brutalist opening,
recap, Your Turn and `@NikBearBrown` outro. Runtime follows the teaching, not an
arbitrary step count. Search the scene library and inspect props before authoring.

Start with the finished rendered target and state that the film teaches **a
possible reconstruction from images**. Use those images throughout as evidence,
with restrained crops/overlays and before/after comparisons. A new scratch-scene
Blender demonstration is encouraged when it makes a concept easier to learn;
it must use the image-based recipe and be labeled as a new teaching demonstration,
not archival footage of the original build. Preserve the original assets.

Show actual Blender UI for operations demonstrated in Blender. Keep panels and
settings readable; show one complete example before accelerating repetition.
Explanatory diagrams may clarify geometry, but must not masquerade as screenshots,
source topology, original intermediate stages or executed coding-agent sessions.
A lesson made solely from stills and diagrams is valid if it clearly says the
construction steps are proposed and does not claim a tested rebuild. It still
needs concrete operations, prompts and visual checkpoints, not only a gallery tour.

## Verify the lesson and deliver

Check that a learner can start with only the provided images and instructions,
that each prompt has enough context, and that every stage has a visible acceptance
check. Check Blender-version-sensitive operations against the actual installed
version or official documentation before asserting they work. Run any delivered
code in a fresh scratch scene when possible and report exactly what was tested.
A successful script is not evidence of an accurate likeness; inspect its renders.
If Blender is unavailable, disclose that the procedure/code remains untested
without demanding the original model as a substitute.

Record demonstration status and unresolved assumptions in `BUILD-LESSON.md`.
Do not call a lesson learner-tested unless someone actually followed it. End
with a small practice change and two visible checks, giving the learner a next
step rather than pretending every aspect of Blender has been covered.

Output to the subject project's `youtube/<slug>-build/` (or the chosen destination):
film, narration/captions, `BUILD-LESSON.md`, `PROMPTS.md`, `SOURCES.md`, shot list,
beat sheet, QC results, and any actual demonstration scripts/captures. The guide
and prompt pack accompany the film. When blocked, distinguish the completed
lesson materials from an unrendered film. No uploading, paid generation or
publication is authorized merely by invoking this skill.
