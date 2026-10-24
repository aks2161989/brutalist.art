# The Blender camera rig — what was verified, and the commands

## Executive summary

**What this is.** How the walkthrough skill puts a camera into a Blender model, moves it, and
measures what it did, with every Blender fact below checked against the installed Blender rather
than remembered.

**Why read it.** Blender 4.x to 5.x renamed and removed a lot (animation actions, EEVEE, the sky
model). A camera rig written from memory looks right and is wrong in ways a screenshot hides: an
eased move at 1.5× the speed you asked for, a camera that is not the one the render uses, a
vertical that leans by a degree.

**What it found.** Verified on **Blender 5.1.2** (Bear's Mac, 2026-10-18), and covered by
`tests/test_building_walkthrough.py`. Nothing here has been run on Blender 5.2 LTS. If the
installed Blender differs, say so in the report and re-run the tests.

## Verified facts (Blender 5.1.2)

| Fact | How it was checked |
|---|---|
| `FollowPathConstraint` has `use_fixed_location`, `offset_factor`, `use_curve_follow`, `forward_axis`, `up_axis`, `offset`, `use_curve_radius` | read from `bl_rna` |
| With Fixed Position, equal steps of `offset_factor` are **equal distances along the path**, even when the control points are 1 m, 1 m, 18 m apart | stepped 0 → 1 in tenths; each step moved 2.0 m |
| On a *curved* Bezier route with linear keys the camera speed was 0.9336–0.9343 m/s (constant) | `route_check.py` on the test route |
| **`keyframe_insert()` ignores `preferences.edit.keyframe_new_interpolation_type`.** New keys are BEZIER whatever it says | the same rig came out 0 → 1.45 m/s → 0 (peak 1.5× the mean) until the F-curves were set directly |
| In 5.x F-curves live in the channelbag of the assigned slot: `bpy_extras.anim_utils.animdata_get_channelbag_for_assigned_slot(owner.animation_data).fcurves` (`Action.fcurves` is gone) | probed |
| Keyframe `interpolation` values include `LINEAR`, `BEZIER`, `SINE`, `BACK`; `easing` values `AUTO`, `EASE_IN`, `EASE_OUT`, `EASE_IN_OUT` | read from `bl_rna` |
| `TimelineMarker.camera` exists; with a camera bound to a marker, `scene.camera` switches at that frame | `route_check.py` asserts `scene.camera` after `frame_set` |
| A camera parented to an empty that has Follow Path (forward `Y`, up `Z`), with the camera rotated **+90° about X**, looks along the direction of travel and is level (roll < 0.01° across a 360-frame walk) | measured |
| A **Track To** constraint (track `-Z`, up `Y`) keeps the camera level while it looks at a target (roll < 0.01° over a 20 s orbit) | measured |
| **Follow Curve smooths the heading around a corner.** A 90° polyline corner at 1.4 m/s turned the camera at ≤ 21°/s over several metres, not in a snap | measured: yaw is a property of the camera, not the path |
| Cameras: `lens`, `sensor_width`, `sensor_fit`, `shift_x`, `shift_y`, `clip_start`, `clip_end`, and `dof.use_dof`, `dof.aperture_fstop`, `dof.focus_object`, `dof.focus_distance` | read from `bl_rna` |
| Render engines: `BLENDER_EEVEE`, `CYCLES`, `BLENDER_WORKBENCH`. There is no `BLENDER_EEVEE_NEXT` in 5.x | read from `bl_rna` |
| `RenderSettings.use_overwrite` and `use_placeholder` exist (resumable sequences) | read; resume tested: a second run rendered nothing and took 0 s |
| A Workbench still renders headless on this Mac (`-b`) | rendered 320×180, then 960×540 |
| Sky Texture types: `SINGLE_SCATTERING`, `MULTIPLE_SCATTERING`, `PREETHAM`, `HOSEK_WILKIE` | read from `bl_rna` |
| Blender prints `Time: 00:00.13` per frame, which `render_shots.py --time` parses | observed |

**Not verified:** anything on the GPU (this Mac was driven headless), Cycles denoising behaviour
across frames (flicker is *measured* in finished frames, not predicted), a doorframe rig on
moving geometry, Blender 5.2.

## Anatomy of one moving shot

```
PATH_S01      Bezier curve (3D), world coordinates, identity transform
RIG_S01       empty at the world origin; Follow Path -> PATH_S01, Fixed Position,
              Offset Factor keyed 0 at the first frame, 1 at the last (LINEAR unless eased)
CAM_S01       camera, child of RIG_S01, rotation X = 90 deg (looks along travel, level)
   look "target"  ->  LOOK_S01 empty + Track To on the camera
   look "path"    ->  LOOKPATH_S01 + LOOK_S01 riding it in step with the camera, Track To
M_S01         timeline marker on the first frame, camera bound to CAM_S01
```

The rig empty sits at the origin so the path's world coordinates are the camera's. An orbit has
no path: the rig empty is at the centre, its Z rotation is keyed, the camera sits at the radius
and height and a Track To keeps it on the subject. A still is a camera with Track To.

Everything lives in a collection `CAMERA_RIG`. Exclude it, and any glass or reference geometry
that should not count as a wall, from the collision test with `--exclude-collection`.

## Commands

All run from `books/`. `BLENDER` is `/Applications/Blender.app/Contents/MacOS/Blender`. Work on
a copy: `camera_rig.py` refuses to save over the model it opened.

```bash
SK=brutalist.art/skills/make/building-walkthrough/scripts
# describe the model first (bounds, units, triangles, cameras, lights, missing textures)
"$BLENDER" -b MODEL.blend --python $SK/route_check.py -- survey --out REEL/survey.json
# build the rig from the route
"$BLENDER" -b MODEL.blend --python $SK/camera_rig.py -- REEL/route.json --out REEL/rigged.blend
# measure what the camera does, frame by frame
"$BLENDER" -b REEL/rigged.blend --python $SK/route_check.py -- check REEL/route.json --out REEL/route_report.json
# cheap preview, then time three real frames, then render
python3 $SK/render_shots.py REEL/rigged.blend REEL/route.json --engine BLENDER_WORKBENCH --percent 25 --out REEL/preview
python3 $SK/render_shots.py REEL/rigged.blend REEL/route.json --engine CYCLES --samples 128 \
        --time 120:interior 500:exterior 800:detail --out REEL/budget.json
python3 $SK/render_shots.py REEL/rigged.blend REEL/route.json --engine CYCLES --samples 128 --out REEL/renders
```

Arguments to Blender are read in order: settings and `-o` must come before `-a`/`-f`;
`render_shots.py` does this for you. Frame numbers in `renders/<shot>/####.png` are the timeline's
frame numbers.

## What `route_check.py` measures and what it does not

Per frame of each shot it records position, speed, turn rate, roll, pitch, height above the
surface below the camera, and the distance to the nearest geometry along 14 rays (the four sides,
up, eight corners, and the view direction; **not** the frame edges, because walking through a
doorway puts the jamb at the edge of the picture without the camera being near it). It asserts
the shot's camera is the one `scene.camera` becomes at the shot's first frame.

It does **not** see: anything that moves independently of the camera (doors, crowds, physics),
anything disabled in the viewport, material transparency (a glass wall is a wall unless you
exclude it), whether a shot is well framed, or what the pace feels like. Treat PASS as "no gross
fault found". `--ignore-object` and `--exclude-collection` exist for curtains, glass and
reference geometry; list what you ignored in `ROUTE.md`, because an ignored wall is a camera
that can walk through it.

A camera that flies over a low obstacle reads as a height fault ("0.60 m above the surface
below"): the test measures the surface *below the camera*, not the floor. That is deliberate;
it is the camera, not the floor, that the viewer sees.

## Preview and final settings

- Preview: Workbench, 25% resolution. A 960×540 frame took 0.13 s on the test model; a real model
  will be slower. The point is to look at the *route*, not the materials.
- Final: PNG sequence per shot, one folder per shot. Use OpenEXR only when you will composite.
- Keep the **view transform** the same across all shots and record it in the survey; a change
  between shots reads as a change of light.
- Motion blur is a per-shot decision; record it in `ROUTE.md`.
- Render time: frames × seconds per frame, from **three real timed frames** (an interior, an
  exterior, a moving detail). 90 s at 24 fps is 2,160 frames; at two minutes a frame that is
  72 hours before any revision. If the honest estimate is more than about 8 hours on the Mac,
  plan it for Explorer: read `hpc-aicr/skills/hpc/HPC.md` first and ask Bear before any `sbatch`. A kit for
  it exists but has **not been run on Explorer**:
  `/Users/bear/Documents/CoWork/bear-textbooks/books/hpc-aicr/Rendering-Blender-on-Explorer/` (README
  first; its measured Mac figure is 242 s for one 4K frame at 64 samples). Its frames are
  `frame_#####.png` in one folder per shot, which `verify_walkthrough.py --renders` accepts when
  `renders.dir` points at that folder (the gate reads the digits in each file name).
