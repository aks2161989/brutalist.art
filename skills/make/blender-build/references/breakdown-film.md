# The build breakdown film — stages, shots, honesty, and the reveal

## Executive summary

**What this is.** How to turn a build record into a film that explains how a Blender model was made:
the stage skeleton to organise it, what to capture at each stage, how to explain each step, and how to
show a model "going together" without implying an order that was not the real one.

**Why read it.** A breakdown film that is only a speed-run of the finished model teaches nothing, and
one that animates parts rising in a tidy order can quietly claim a history that never happened. The
rules here make every step explain a *decision*, show the evidence for it, and say whether it was
recorded, scripted or demonstrated.

**What it found.** The stage skeleton and the per-step pattern come from the first pasted source (a
plan for two companion films). The construction-reveal techniques come from the second; two of its
details are out of date for Blender 5.x and are corrected below. Both reveal techniques were built
as scripts and **measured by rendering** (a height wipe took a cube from 0 to half to full opaque
pixels on schedule; a staggered drop hid a piece until its start frame and landed it), and the choice
of order is recorded in the file so the film cannot forget to disclose it.

## The stage skeleton (a default, not a law)

Use the stages the build really had. Each stage has a milestone: a saved version, a census, and
renders from the **same fixed comparison cameras** at every stage so the progression is visible.

| Stage id | What was done in Blender | Capture for the film |
|---|---|---|
| `01-define` | gather references, state the purpose, list the spaces/parts, sketch the intended route (building) or silhouette (asset) | the references and a sentence of intent |
| `02-dimensions` | choose units; verify imported or modelled dimensions; add a human-scale reference | a dimensioned view that shows the scale decision |
| `03-organize` | separate architecture, furniture, landscape, lights, cameras, reference into named collections | the Outliner, readable, and why it is organised that way |
| `04-blockout` | simple geometry for floors, walls, ceilings, openings, major masses | a plain shaded overview; an early camera test |
| `05-journey` (building) / `05-silhouette` (asset) | rough cameras; check entrances, sightlines, clearances; revise the blockout | before and after of one layout improvement |
| `06-modules` | recurring windows, doors, columns, stairs, facade sections, with consistent dimensions and origins | ONE module built in full, then repeated |
| `07-detail` | thickness, recesses, bevels, trim, silhouette detail according to the planned camera distance | close-ups showing what each refinement adds |
| `08-materials` | UVs, consistent texture scale, material variation, surface detail | a UV check, the node setup, before and after |
| `09-dress-light` | props, landscape, daylight and practical lights | dressing and lighting shown separately |
| `10-camera` | camera animation: movement, framing, focus, shot length, transitions | the camera path, the keys, the matching preview |
| `11-render-export` | test frames, render, edit; or export for the engine | preview against finished frame, or the validator run |

**Game asset variant** (after Walker's `BLENDER.md` §6): `01-define`, `02-dimensions`, `03-organize`,
`04-blockout`, `05-engine-test`, `06-geometry` (deformation geometry), `07-detail`,
`08-uv-materials`, `09-rig`, `10-bake-export`, `11-validate` (the validator and a real engine import).
Skip stages that did not happen and say so (`skipped_reason`); do not invent them.

## One pattern for every explanation

Each step the film explains answers, in this order: **goal** (what changes), **starting state**,
**operation** (what is done, where in the interface), **the settings that matter**, **the result**
(measured), **the reason**. A line like "I built one window module, put its origin at the lower corner
so every copy snaps with one number, and reused it across the façade" carries the operation *and* the
decision. If a step has no reason you can state and defend, it is not ready to film.

## Showing Blender

- Show **the real Blender window** (a tool is shown as itself: `lecture` SHOW-THE-THING). Enlarge the
  panels being discussed (Preferences ▸ Interface ▸ Resolution Scale), isolate the object (Local View,
  View ▸ Local View ▸ Toggle Local View), and hold the important settings on screen long enough to read.
- Capture at native resolution; a 1080p recording scaled to 4K is not a 4K capture.
- **One complete example of repeated work, then accelerate.** Build one window carefully, then show the
  rest by the rule and the placement table. The record's `repeats` field carries the rule.
- **Same cameras every time.** The milestone renders come from `record.comparison_views`; the film
  cross-fades nothing: it shows the stage-by-stage change from the identical viewpoint.
- **Corrections are content.** When a doorway moved, a material changed or a step failed, show the
  evidence that prompted it (the error, the measurement, the render) and then the fix. The record's
  `correction` field holds the evidence; a failed command stays in the record.
- **Show only what was done.** Anything not recorded is either said aloud as untested, or labelled
  a demonstration (below). If a beat needs a session that has not happened, write the exact session for
  Bear to run and record instead of faking it.

## Recorded, scripted, demonstrated: what the narrator may say

| Tier | The film says | The picture is |
|---|---|---|
| `recorded` | "we did", "the MCP ran" | the tape, the transcript, the real session, or the milestone |
| `scripted` | "the script does" | the script on screen, its census result, the replay |
| `demonstrated` | "here is how you would do it; this is a rebuild of one module for the film" | a fresh recording, labelled on screen and aloud |
| `inspected` | "the file contains" | the census, the Outliner |
| `inferred` | "one way to get this is" (never history) | clearly conceptual |

The gate (`--film`) fails any step in `film.told_as_history` that is not recorded or scripted.
Do not credit a tool that did not run: if the guide says Walker or the MCP built something, a tape or
transcript shows it; if only assembly went through the MCP and the parts were built by parallel headless
workers, say that.

## The construction reveal (verified)

A model going together piece by piece is a *picture of an order*. Two states of that claim:

- **`recorded`** — the pieces appear in the order they were modelled; each item names the
  build-record step it came from. The gate checks the steps exist and the order matches.
- **`explanatory`** — an order chosen to explain how the parts fit (foundations, frame, walls, roof,
  fittings). Legitimate and useful, but the film must **say** it is not the order the model was built in
  (`labelled_in_film`), because the viewer will otherwise assume it is.

`reveal.py` builds both techniques on a copy, from an `order.json` that must state `order_source`:

```bash
"$BLENDER" -b MODEL.blend --python $SK/reveal.py -- wipe    REEL/reveals/order.json --out revealed.blend
"$BLENDER" -b MODEL.blend --python $SK/reveal.py -- stagger REEL/reveals/order.json --out revealed.blend
```

| Technique | How it works (measured on Blender 5.1.2, Cycles) | Use for | Not for |
|---|---|---|---|
| **Height wipe** (`wipe`) | each object gets its own copy of its materials with a bounding-box height threshold (0 at its base to 1 at its top), keyed over the item's frames; above the line it is a Transparent BSDF; a thin emissive band rides the front. A cube went 0 → 200 → 400 opaque pixels at frames 1, 13, 25 | pieces that should grow up from their base; columns, walls, whole floors | anything needing exact world-height alignment across objects (the threshold is per object) |
| **Staggered drop** (`stagger`) | each object is hidden until its start frame, then keyed to drop in from `drop_height_m` above with a `BACK` interpolation and `EASE_OUT` easing; objects stay hidden before their start | panels, slabs, roof pieces, furniture | a smooth "growth" |
| **Build modifier** (not scripted) | Add Modifier ▸ Generate ▸ Build: faces appear over time. Properties checked: `frame_start`, `frame_duration`, `use_random_order`, `use_reverse`, `seed` | line-by-line generation of a truss, a stair, timber framing | an ordered assembly of separate parts |

Neither scripted technique changes geometry. Both write `reveal_order_source` into the scene so the
file itself says which kind of order it shows. Render the wipe with film transparency and Cycles (or EEVEE
with a blended or dithered surface render method). Offset the start frames of neighbouring pieces by a few
frames for a cascade rather than everything at once; the order and offsets are in `order.json`.

Keep real structure honest: organise collections by construction phase (foundations, structure, shell,
openings, partitions, fittings) *only if* you are telling the explanatory order; for a recorded order the
sequence comes from the build record, not from the tidy collection list.

## Credits and reused assets

Every outside asset (a texture, a mesh, an HDRI) has a credit entry (what, source, licence) and a step that
uses it (`uses_external_asset`). The film names its own contribution and the reused parts separately.

## Release checks

| Check | Passes when |
|---|---|
| Spatial and stage clarity | a viewer can say what changed at each stage and why |
| Evidence | each step the narrator tells as history is `recorded` or `scripted`; demonstrations are labelled |
| Same cameras | every milestone shows the same comparison views |
| Reconstruction | the replay passed, or a person followed a module by hand: and the film says which |
| Honest order | any build-up animation states whether its order is recorded or explanatory |
| Asset completeness | the model reopens from a clean checkout; textures and links resolve (survey it) |
| Credits | every outside asset is credited; the film distinguishes reused from original |
| Delivery | frame rate, 4K resolution, colour treatment, loudness and credits are consistent |

## Corrections to the pasted sources (Blender 5.1.2)

- The second source names the **Nishita** sky. Sky Texture in 5.1.2 offers `SINGLE_SCATTERING`,
  `MULTIPLE_SCATTERING`, `PREETHAM`, `HOSEK_WILKIE`.
- It names "EEVEE Next". The engine id is `BLENDER_EEVEE` since 5.0.
- It says to animate with "Back Out interpolation". The key's `interpolation` is `BACK` and its `easing`
  is `EASE_OUT`; both are set on the F-curve keys (in 5.x through the slot's channelbag), because
  `keyframe_insert()` ignores the default-interpolation preference.
- It suggests a Freestyle or wireframe overlay for CAD-style edges. That was **not tried** here; treat it
  as unverified until a render has been looked at.
