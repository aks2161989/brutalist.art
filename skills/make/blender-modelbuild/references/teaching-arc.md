# Teaching arc, beat fields and the AI-versus-hand mapping

## Required acts, in order

Every beat has an `act`. These acts must all appear, in this order (an act may
span several consecutive beats):

| act | what the beat does |
|---|---|
| `views` | Walk around the finished model: hero three-quarter, side, front, rear, top, details. Existing renders only. |
| `brief` | The inputs: reference photos, blueprints, concept image, kit or measurements, and who supplied them. |
| `blockout` | The base shapes: loft, lathe, primitives. AI did / by hand. |
| `proportions` | Where the numbers came from: traced, measured, blueprint ratios, a kit. |
| `parts-order` | The order of the major parts, and why that order. |
| `modifiers` | Which modifiers the script used and which it did not; what a person would use. |
| `materials` | Shader setup, colours, textures, colour management. |
| `lighting-camera` | Lights, world, render engine settings, matched cameras, lenses. |
| `check` | Comparing against the references: compare sheets, overlays, what they caught. |
| `export` | `.glb` export and what does and does not travel with it. |
| `rounds` | The round history: what changed, what was skipped and why. |
| `assessment` | The AI's own scores and misses. |
| `human-verdict` | The human's words ("Professor Bear said …") or "pending". |
| `not-established` | At least one thing the evidence does not establish. |
| `lesson` | The takeaway for a person building it, and the human in the loop. |
| `outro` | "Grok Bot, Built. This is Liam." over the card "Narration: the Liam voice". |

## Beat fields

Standard brutalist fields: `beat_id` (`B00`…), `act`, `segment`,
`narration_text`, `estimated_duration_s`, `t_start`, `actual_duration_s`
(`null` until audio exists), `audio_file` (`null`), `new_visual_element`,
`shot`.

This skill adds:

- `track`: `result` (views), `ai-did`, `by-hand`, `both`, `check`, `verdict`,
  `limits`, `bookend`.
- `shot.type`: `STILL` for existing images (the pantry handles stills),
  `SLATE` for the closing card. `shot.source`: `own`. `shot.motion`:
  `kenburns`, `pan`, `static`, `sequence` (several assets in turn).
- `shot.assets`: list of image paths relative to `film/`, all inside the model
  folder. `shot.view`: for `views` beats, any of `hero`, `side`, `front`,
  `rear`, `top`, `detail`.
- `shot.label`: the on-screen kicker for the beat.
- `ai_did`: `{summary, evidence: [paths relative to the model folder]}` —
  required on `ai-did` and `both` beats; every path must be in the ledger.
- `ui_steps`: `{label, steps: [...]}` — required on `by-hand` and `both`
  beats. `label` must contain "Blender UI reconstruction". Steps name menus and
  shortcuts as they appear in Blender 4.x; they are teaching steps, not a
  recording.
- Outro beat: `shot.type: SLATE`, `shot.card_title: "Grok Bot, Built."`,
  `shot.card_text: "Narration: the Liam voice"`.

Metadata: `slug`, `title`, `topic`, `skill: "blender-modelbuild"`,
`persona: "Liam"`, `narrator_label: "the Liam voice"`, `voice: "the Liam
voice"`, `clock: "narration"`, `caption_policy: "none"`, `closing_card`,
`model_folder: ".."`, `model_round`, `width`/`height`/`fps`, `render_by`,
`est_runtime_s`, `display_rule`. No TTS product, voice id, engine or speed
fields anywhere.

## AI did → by hand (common mappings)

| Script does | A person in the Blender UI would |
|---|---|
| Lofts a mesh from cross-section tables | Add a cylinder or UV sphere, rotate it along the length, add loop cuts (`Ctrl+R`) and scale each ring (`S`) against a reference image; or skin a curve |
| Lathe / revolve a profile | Draw half the profile as edges or a curve, then a **Screw** modifier (or Spin) about the axis |
| `for side in (1, -1)` loops | A **Mirror** modifier on the axis, with Clipping on |
| Parts placed on the hull surface by math | Snap to Face (`Shift+Tab` snapping) or a **Shrinkwrap** modifier |
| Solidify / Bevel / Subdivision Surface in code | The same modifiers from the Modifier tab; `Ctrl+1`/`Ctrl+2` for subdivision |
| Separate inset parts instead of booleans | Either the same, or a **Boolean** (Difference) cutter, then clean the topology |
| Principled BSDF per colour from hex | Material tab → New → Principled BSDF; set Base Color hex and Roughness |
| Cameras from (azimuth, elevation, distance, lens) | Add camera, `Numpad 0`, Lock Camera to View, align to the photo set as a camera background image |
| Compare script stacks render over photo | Render, then compare in the Image Editor or with the photo as camera background at reduced opacity |
| `export_scene.gltf(..., export_apply=True)` | File → Export → glTF 2.0, Format: glTF Binary (.glb), Apply Modifiers on |

Only use a mapping when the script really does the left-hand side. Say plainly
when the script used no Mirror or no Boolean.
