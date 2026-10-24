---
name: building-walkthrough
description: Walk a viewer through a 3D model — a building, a game environment seen as a model, or a single game asset — in a Liam-narrated film made from real Blender renders. Plans the central idea, the route and every shot's job; builds the camera rig; MEASURES the camera (speed, turn rate, roll, height, distance to walls) before a frame is rendered; renders numbered image sequences; and discloses, in the opening, what kind of model this is and what it leaves out. Companion to blender-build (how the model was made). Also accepts architectural-walkthrough and asset-walkthrough. Does not build the model, fabricate a viewer test, or publish.
---

# building-walkthrough — walk the model, show only what it contains

```text
building-walkthrough /path/to/model.blend                 # a building (default)
building-walkthrough /path/to/model.blend environment     # a game level, seen as a model
building-walkthrough /path/to/asset.blend asset           # one game asset: orbit, scale, detail
building-walkthrough /path/to/model.blend --brief "the idea in a sentence"
```

An **agent-driven builder**, like [godot-waikthrough](../godot-waikthrough/SKILL.md), not a shell
command. The difference from its siblings:

| Skill | The subject | The footage |
|---|---|---|
| **building-walkthrough** (this) | a **model** (`.blend`/`.glb`) | Blender renders from a camera route we design and measure |
| [godot-waikthrough](../godot-waikthrough/SKILL.md) | a **running game** | captured gameplay |
| [godot-trailer](../godot-trailer/SKILL.md) | a running game, argued to a stranger | captured gameplay, selected |
| [riff](../riff/SKILL.md) | any visual artifact, critiqued | whatever it shows |
| [blender-walkthrough](../blender-walkthrough/SKILL.md) | the finished model through existing images | supplied renders/gallery, no model access required |
| [blender-build](../blender-build/SKILL.md) | how a learner could construct a similar model | image-based lesson and new demonstrations; explicit record mode for original history |

This workflow lets a viewer experience the finished place through a new camera route.
For a tour of already rendered images, use `blender-walkthrough`. Pair either with
`blender-build` for a lesson on making a similar model from images. Request its explicit
record/history mode only when the film should explain the original build process.

Read this file, then [walkthrough-craft.md](references/walkthrough-craft.md) (the rules, their
defaults and when to break them), [blender-camera-rig.md](references/blender-camera-rig.md)
(what was verified on Blender, the commands) and
[walkthrough-contract.md](references/walkthrough-contract.md) (`walkthrough.json`, `route.json`,
what the gate checks). Also [RENDER-TARGETS.md](../../../RENDER-TARGETS.md),
[PIPELINE-SAFETY.md](../../../docs/PIPELINE-SAFETY.md), the walkthrough sibling's
[timing and audio contract](../godot-waikthrough/references/capture-and-coverage.md), and — for
any building with a controls file or a departures ledger, such as a measured historical
reconstruction — walker's `BLENDER.md`.

## The one test

A viewer who has never seen the model must be able to answer, in order: **Where am I? How does
this place connect? What should I notice?** And one more that this skill adds: **What is this a
model *of*, and what does it leave out?** The first three are craft; the last is honesty, and the
film answers it in its first seconds.

Films show only what was actually modelled and rendered (Bear's law for every Brutalist film: base
everything on things actually done). The model is never presented as the world.

## 0. Preconditions: the model, its hash, its card (`MODEL-CARD.md`)

1. **Resolve the model.** The real `.blend`, opened read-only. If several candidates exist, ask which.
   Never open-and-save the master: all work is on copies (`rigged.blend`).
2. **Hash it** (`sha256`) and record the Blender version. Every measurement and render is tied to
   that hash; if the model changes, everything downstream is stale and the gate says so.
3. **Survey it** (does not mutate it):

   ```bash
   "$BLENDER" -b MODEL.blend --python brutalist.art/skills/make/building-walkthrough/scripts/route_check.py -- survey --out REEL/survey.json
   ```

   It reports units, bounds, evaluated triangles, collections and their extents, cameras, lights,
   timeline markers, **scripts embedded in the file**, and missing or absolute texture paths. A
   model with missing textures or absolute paths will not reopen from a clean checkout: fix or
   report that first (release check: asset completeness).
4. **Write `MODEL-CARD.md`** (opens with an executive summary, in plain language): what the model
   represents; its `status` — `measured` (built from measurements, ideally with a controls file the
   model is checked against), `interpretive`, `stylized` or `invented`; what it was built from;
   what it **leaves out or simplifies** (colour, crowds, sound, heat, furniture, wear, anything
   known to have existed); and who/what built it (Walker, the Blender MCP, scripts, by hand: the
   companion `blender-build` film covers the how). A model's departures from its sources are a
   ledger, not a footnote: every departure that would change a viewer's belief gets an entry in
   `departures` and is **disclosed in the film** (see §3).

## 1. Brief (`WALKTHROUGH-BRIEF.md`)

Write these first; they decide which shots exist at all.

1. **Mode:** `building` (a route through a place), `environment` (a game level as a model: the
   player's real eye height and field of view replace the 1.6 m default, and the route must be one
   a player could walk), or `asset` (views, not a route; see §9).
2. **The central idea, one sentence** (`brief.idea`). A monumental entrance, a quiet courtyard, a
   compact home with clever circulation. If it will not compress, stop and tell Bear: a walkthrough
   without an idea is a tour, and a tour is not this skill.
3. **Audience and the variant**: *which* day, weather, state. Variants reuse geometry but are
   never blended (a quiet Saturday and a packed Tuesday are two films).
4. **The viewpoint:** standing adult at 1.6 m, or the game's controller. Write the number.
5. **What the model cannot show.** From the card. This becomes the opening disclosure.

## 2. Route and shots (`ROUTE.md`, `SHOTLIST.md`, `route.json`)

Default sequence: **site → approach → entrance → main space → connected spaces → closing**, with
close looks (`detail`) anywhere. Every shot carries a *job* (orientation, scale, connection,
material, atmosphere, feature) and **what it reveals that no earlier shot did**. A shot that
repeats information is cut. Alternate wide, medium and close; include held frames. Pace comes from
distance at a walking speed and from the time the narration needs, never from a target runtime.
Details, defaults and the reasons are in [walkthrough-craft.md](references/walkthrough-craft.md).

Write the shots as `route.json` (geometry: waypoints, lens, look) and `walkthrough.json`
(editorial: section, purpose, framing, reveals, light, narration). For a complicated plan, draw the
camera path on the floor plan once (a Workbench top view with the curve shown) and use it in the film.

Mark **fact kinds** in the plan as you write each line the narrator will say: a **model fact** (read
from the file: dimensions, counts) or a **world fact** (true of the place, needing a verified row in
`FACTCHECK.md`). A history that came from memory, or from a pasted brief, is a lead for FACTCHECK, not
a script.

## 3. Disclose what the model is and is not

The first two shots carry the `disclosure` (spoken, and on screen as a few words): the model's
status and its largest departures, in plain words. Example: *"This is an interpretive model built
from the original drawings. Its interior is one colour; the real building was painted."* Every
`departures` entry names the shot that discloses it. A film that shows a cream-and-white interior
without saying the original was coloured is making a claim.

## 4. Rig the camera, then measure it

```bash
SK=brutalist.art/skills/make/building-walkthrough/scripts
"$BLENDER" -b MODEL.blend --python $SK/camera_rig.py -- REEL/route.json --out REEL/rigged.blend
"$BLENDER" -b REEL/rigged.blend --python $SK/route_check.py -- check REEL/route.json --out REEL/route_report.json
```

`camera_rig.py` builds, per shot, a path curve, an empty that rides it (Follow Path, Fixed
Position, Offset Factor keyed 0 → 1), a level camera on the empty, an optional look target, and a
timeline marker binding the shot's camera. `route_check.py` then steps **every frame** and
measures speed, turn rate, roll, pitch, height above the surface below, distance to the nearest
geometry, and whether the right camera is active. A fault fails the route: fix the *route*, not the
report. A passing route means "no gross fault found"; it does not mean the film is good.

Two hard-won facts (verified on Blender 5.1.2, see the rig reference): Python's `keyframe_insert()`
ignores the default-interpolation preference (every move came out eased unless the F-curves were set
directly, and `camera_rig.py` does that), and Follow Curve smooths the camera's heading around a
corner, so judge turns by the measured yaw, not by the shape of the path.

Write down in `ROUTE.md` anything you told the checker to ignore (`--ignore-object`,
`--exclude-collection`): an ignored wall is a camera that can walk through it.

## 5. Light looks (`LOOKS.md`)

Decide the time, weather and mood once; name each look (`L1`…); give every shot a look. A change of
look is a decision with a reason (`look_change.reason`); inside one section it fails the gate if
undeclared. Physical sky: Sky Texture `MULTIPLE_SCATTERING` (Blender 5.x has no Nishita). Warm
interior fixtures (about 2700–3000 K) against cool daylight (about 5500–6500 K) is a useful
contrast, not a law. For a historical place the light must agree with what is known or the departure
is disclosed. Depth of field only on detail and material shots.

## 6. Preview, time, render

Free steps run straight through (Bear's no-gate-on-free law): there is no sign-off to *start* a
render. The checks that stop you are measured ones.

1. **Preview** the whole route in Workbench at low resolution, then **look at frames**: a contact
   sheet of every shot at 10%, 50%, 90% (`render_shots.py --engine BLENDER_WORKBENCH --percent 25`).
   Check orientation, framing, collisions, that no wall pops through the lens.
2. **Time three real frames** (an interior, an exterior, a moving detail) with your final engine,
   samples and resolution:

   ```bash
   python3 $SK/render_shots.py REEL/rigged.blend REEL/route.json --engine CYCLES --samples 128 \
           --time 120:interior 500:exterior 800:detail --out REEL/budget.json
   ```

   Frames × seconds per frame is the budget. Over about 8 hours on the Mac, plan the render for
   Explorer: read `hpc-aicr/skills/hpc/HPC.md` first and **ask Bear before any `sbatch`**. 90 s at
   24 fps is 2,160 frames; at two minutes a frame that is 72 hours before any revision. A measured example
   (Crystal Palace nave walk, Mac M4 Pro, 4K, 64 samples): **242 s a frame**, so about 145 Mac-hours for 90 s.
   The cluster route is already worked out, and **nothing in it has run on Explorer yet**: a frame-claiming
   worker pool, a stitch that refuses a shot with a missing or truncated frame, and a Blender install recipe,
   in `/Users/bear/Documents/CoWork/bear-textbooks/books/hpc-aicr/Rendering-Blender-on-Explorer/` (README
   first). It names frames `frame_#####.png` per shot; point `renders.dir` at its `frames/` folder and the
   gate's frame check reads those names.
3. **Render numbered image sequences, one folder per shot** (`render_shots.py … --out REEL/renders`).
   If a render stops, finished frames survive and a re-run skips them. Encode a shot's clip with
   ffmpeg from its numbered frames at the timeline frame rate.
4. Look for flicker, texture shimmer, unstable denoising and geometry errors in the **moving** shots, not
   only in stills. The gate measures still-shot flicker; moving shots need eyes.

## 7. Narration and sound

**Liam, in for Bear** (Kokoro `am_onyx`, free, local), applied as the toolkit's rules define them;
never ask Bear to re-decide voice, persona or outro. Sparse:
the picture carries a walkthrough. At most one fact per shot, every line sourced as in §2, in the
words of the model (what is on screen), no evaluative adjectives (the gate warns), no numbers or
totals for the film. Every line must fit its shot (the gate estimates it; the measured Kokoro
duration is the clock once the audio is generated). Ambient sound is optional; recorded or
licensed sound has its rights in `SOUND.md`, and is never presented as the place's actual sound.

A **person** in the film's own graphics is a Professor Bear portrait, never an icon
(toolkit rule 9). A 1.8 m scale figure *inside the model* is geometry, not an icon, and is labelled
as a scale reference. A company or tool shown visually is its logo (rule 11); a tool shown as itself
(the Blender window) wins over a logo.

## 8. Assemble the film

Slug `claude-liam-<model>-walkthrough`, built into the model's own folder:
`<model folder>/youtube/claude-liam-<model>-walkthrough/`. Never into the toolkit.

**Standard spine** (the same chassis as godot-waikthrough's standard mode; read its
[ai-explainer](../ai-explainer/SKILL.md) render and voice chassis): open on the first establishing
shot with Liam's brief introduction **and the disclosure**; the route as the body (shot clips as
footage beats, pre-trimmed to the exact shot window; follow the sibling's *timing and audio
contract*: the stock compiler can centre-cut and slow footage, so conform narration to the whole
shot, pad with silence, and inspect compiled clips for retiming notices); then a **Verdict** that
separates what the model supports from what it does not (and which departures changed the picture),
a **Your Turn** (one concrete experiment the viewer can do: check one sightline against the plates,
walk the route in their own copy), and the **regular outro** ([OUTRO-LOCK.md](../../../OUTRO-LOCK.md):
`ClaudeTitleOutro`, exact episode title, `@NikBearBrown`, spoken and never scored, 1.0 s tail).

No video numbers anywhere (Bear's rule: films are never numbered, no "N of X"). Captions are not burned in. 4K
(3840×2160) final; the footage is rendered at that size, never a 1080p render scaled up.

## 9. Asset mode

Views, not a route: **establish → silhouette → scale → detail → material → topology → closing**.
Turntable at constant angular speed (at least 8 s a turn), 50–85 mm, a neutral cyclorama, a
three-point key. **Show scale** with a 1.8 m figure, grid or ruler. Topology and material shots use
the *evaluated* counts from the survey. "In the engine" is claimed only with a recorded import
(walker's validator and an engine capture), otherwise the film says the asset has not been imported.
A rigged asset's articulation is a pose rendered from the rig, never a crossfade between stills.

## 10. Gate, hand off

```bash
./brutalist.art/art building-walkthrough --check REEL/walkthrough.json            # contract + route report
./brutalist.art/art building-walkthrough --check REEL/walkthrough.json --final     # + budget, renders, human tests
```

The gate is read-only. It fails on the contract (every shot has a job, the route has not doubled
back, light is one logic, every line is sourced and fits its shot, the disclosure is in the opening,
the model file has not changed under the film) and cross-checks the measured report. It
**cannot** tell whether the route is understandable or the model is right.

**Cowork stage** (higher effort; the two-stage rule in `books/CLAUDE.md`): do §0–§6 through the preview and the budget, write
`MODEL-CARD.md`, `WALKTHROUGH-BRIEF.md`, `ROUTE.md`, `SHOTLIST.md`, `LOOKS.md`, `FACTCHECK.md`,
`PROMPTS.md`, `route.json`, `walkthrough.json`, `survey.json`, `route_report.json`, `budget.json`,
`make_sheet.py` and the narration, then write `BUILD-PROMPT.md` (absolute paths, commands as run from
`books/`, the remaining renders, audio, `art run`, `art final`, gates, the traps below, the STOP line)
and give Bear the Claude Code prompt from `books/CLAUDE.md` "Two-stage builds". Never say a film is built
when only the layout is done. **Claude Code stage:** the full renders (or, for a long one, the Explorer
plan), audio, the review cut, `art final`, every gate to PASS.

### The tests only people can run (never fabricate)

- **Orientation test.** Show the preview to someone who has not seen the model. Ask them to describe
  the route and how the main spaces connect. Where they are lost is where to add an establishing shot.
- **Promise check.** Does anything in the film imply the model has a colour, crowd, sound or detail it
  does not? Bear signs that.

Record them under `checks`; until done, the report says the film is **not audience-tested**.

## Traps already met

- Linear keys on a Follow Path rig are required for constant speed; default keys eased the move to
  1.5× the intended peak. The gate measures it (see the rig reference).
- A camera that passes over a low obstacle fails the *height* test ("0.60 m above the surface below"):
  that is the test working, not a bug.
- Doorways: clearance rays toward the frame edges flagged a legitimate walk through a door, so the
  checker uses rays around the camera, not toward the edges.
- A sky or engine name from memory is a bug: Blender 5.x has no Nishita sky and no `EEVEE_NEXT` id.
- A history narrated from a pasted brief is unverified until FACTCHECK says otherwise.

## Deliverables

The 4K MP4 (absolute path and a quoted `open` command), the gate result with every warning, the
route report, the render budget and where it will run, the model hash and Blender version, the
departures ledger, which human tests are pending, and the limits ("measured, not judged"). No upload,
publish or Git push is implied.
