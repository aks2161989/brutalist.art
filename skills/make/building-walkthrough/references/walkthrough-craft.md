# Walkthrough craft — the rules, their defaults, and when to break them

## Executive summary

**What this is.** The craft rules for walking a viewer through a 3D model: a building, a game
environment, or a single game asset. Each rule has a default, the reason for it, when you may
break it, and whether a gate measures it.

**Why read it.** A walkthrough fails in quiet ways: the viewer cannot tell where they are, the
camera drifts through a wall, every shot is the same distance from the subject, or the film
quietly implies the model is more than it is. These rules turn "make it look good" into
choices you can defend and, where possible, measure.

**What it found.** Three pasted sources (below) agree on most things and disagree on two. The
disagreements are settled in the text. Several numbers in them were advice, not standards, so
every number here is a *starting point* and says so. Two statements in the second source are out
of date for Blender 5.x and are corrected (sky model name, EEVEE name). The Crystal Palace brief
holds six lessons that apply to every walkthrough, and a history that is **unverified** and must
not be narrated until it has been fact-checked.

## Where these rules came from

| Source | Pasted by Bear | How it is used |
|---|---|---|
| **A** — a plan for two companion films (walkthrough + build breakdown), a Blender build table, a camera rig, release checks, with Blender-manual links | 2026-10-18 | Basis of the rules and of the release checks. Its numbers are labelled "starting points" by its own text. |
| **B** — a second set of walkthrough rules plus a "construction reveal" technique | 2026-10-18 | Cross-checked against A. The reveal technique went to the `blender-build` skill. Two items corrected (see "Corrections"). |
| **C** — a first-person design brief for walking the 1851 Crystal Palace | 2026-10-18 | Source of the six lessons below. **Its historical claims are from model memory, not from a checked source. Nothing from it may be narrated without a `FACTCHECK.md` row.** |

Rules that a script measures are tagged **[gate]**; the rest need a person.

## The eleven rules

**1. One central idea.** Decide what the viewer should remember: a monumental entrance, a quiet
courtyard, an abandoned plant, a small home with clever circulation. Write it in one sentence
(`brief.idea`). Every shot serves it or is cut. *Break it when:* never; if it will not compress
into a sentence the film is a tour, and a tour is the `godot-waikthrough` job, not this one.

**2. Orient before detail.** Default sequence: **site → approach → entrance → main space →
connected spaces → closing**, with close looks (`detail`) allowed anywhere. Show enough
surroundings to say how the building sits. *Break it when* the film is an interior only or a
single room, and say so in the brief. **[gate]** section order, a required `main` and `closing`,
`closing` last. A recommended-but-missing section is a warning you answer in writing.

**3. A route a stranger can follow.** Move through real openings. Establish a stair before you
arrive on the floor above it. Keep a recognisable landmark across cuts. For a complicated plan,
show the floor plan once with the camera path drawn on it. **[human]** the orientation test
(rule 11).

**4. Every shot has a job.** One of: orientation, scale, connection, material, atmosphere,
feature. Write what it *reveals* that no earlier shot did (`reveals`). A shot that repeats
information is cut, however pretty. **[gate]** purpose, `reveals`, and a repeated `reveals` warns.

**5. Move the camera deliberately.** Start from a slow forward move, a sideways move, a gentle
pan, or a held frame. Combine movements only when the result stays easy to follow. No abrupt
turns, no unintended roll, no repeated starting and stopping. **[gate]** speed, turn rate, roll,
mid-shot acceleration, a "still" that drifts.

| Quantity | Default | Why | Break it when |
|---|---|---|---|
| Walking speed | at most 1.5 m/s; usually 0.7–1.2 | a brisk real walk is ~1.4 m/s and film reads faster than life | an aerial or crane move (the gate allows more by shot type) |
| Turn rate | at most 30°/s | a faster pan loses the space | a deliberate whip, declared per shot |
| Roll | within 0.5° | verticals lean | a dutch angle is the idea (declare it) |
| Pitch | within 8° on a walk | tilting makes verticals converge | looking up at a vault: declare it, or tilt nothing and use lens shift |
| Acceleration | under 3 m/s² mid-shot | a jolt reads as a stumble | the shot starts or ends at rest: ease in or out there |

Speed is only as constant as the keys. Linear keys on a Follow Path rig gave 0.934 m/s ± 0.0005
on a curved path (Blender 5.1.2, measured); the same rig left on Blender's default interpolation
ran 0 → 1.45 m/s → 0 on that path, which is an eased move at 1.5× the intended peak.

**6. A human viewpoint for the main journey.** About **1.6 m** above the floor for a standing
adult. Use aerial views to set the site; use a lower viewpoint only for a reason. For a game, the
player controller's real eye height and field of view win. Keep the camera clear of walls,
furniture and door frames. **[gate]** height above the surface below the camera (±0.10 m),
distance to the nearest geometry (at least 0.30 m, and never inside the near clip).

**7. Lenses that describe the architecture honestly.** On a 36 mm sensor:

| Focal length | Horizontal field of view | Use |
|---|---|---|
| 24 mm | 73.7° | rooms, when space is tight |
| 28 mm | 65.5° | the default interior |
| 35 mm | 54.4° | exteriors; rooms with room to spare |
| 50 mm | 39.6° | details; a "normal" lens on this sensor |
| 85 mm | 23.9° | selected details, façade compression |

An extremely wide view exaggerates a room's size. Keep the camera level and use lens **shift** to
frame, so vertical lines stay vertical. Report the real lens in the survey. *Break it when* the
model is a cramped game interior seen through the game's own 90° field of view.

**8. Alternate information with detail.** Wide shots explain the room, medium shots show
relationships, close shots show craft. Include held frames so the viewer can inspect. **[gate]**
four of the same framing in a row warns.

**9. One lighting logic.** Decide the time, the weather and the mood, and keep them across
connected shots. A change (day to dusk, outside to inside) is a decision with a reason. Warm
interior fixtures (about 2700–3000 K) against cool daylight (about 5500–6500 K) is a useful
contrast, not a law. For a historical place the light must match what is known, or the departure
is disclosed (rule in "Honesty", below). **[gate]** every shot names a declared look; changing
look inside a section without a `look_change.reason` fails.

**10. Sound belongs to the place.** Wind outside, room tone inside, footsteps only where the
viewpoint suggests a walking person. Any recorded or licensed sound has its rights written in
`SOUND.md`. A sound that never existed in the place is never presented as history. The voice is
Liam, sparse, and the picture carries the film (see SKILL.md §7).

**11. Preview before you spend.** Make a cheap preview (Workbench or a few Cycles samples, simple
materials), run the route gate, and *look at frames*. Time three real frames before promising a
render time. **[human]** the orientation test: show the preview to someone who has not seen the
model and ask them to describe the route and how the spaces connect. Until that has happened the
film is **not audience-tested**, and the report says so.

## Pace — settling the disagreement

Source A says a first portfolio piece is **60–120 s with 10–16 shots** (average 6–7 s). Source B
says each camera move should run **at least 8–10 s**. They cannot both be minimums for 16 shots.
Bear's toolkit also says duration is an *output*, not a target (no length cap).

So: a moving shot has a **floor of 3 s** (the gate fails below it), a **default of 6–10 s** (the
gate warns under 6 s), a still has a floor of 1.5 s, and a turntable has a floor of 8 s. The
real length comes from the distance to cover at a walking speed and from the time the narration
needs. The gate also checks that a narration line can be *spoken* inside its shot, using an
assumed 2.4 words a second; once Kokoro has generated the audio, the measured durations replace
that estimate and are the clock. Average shot under 3 s warns "montage".

## What the Crystal Palace brief teaches every walkthrough

1. **Density, not skeleton, is the experience.** A perfect empty frame reads as a parking
   structure. Spend the effort on the hero places the route passes, and instance the rest.
2. **Show only sightlines the evidence supports.** The model had long see-through aisles that the
   real building divided into courts. A long view that did not exist is a claim. Check each
   long view against the sources.
3. **Pick a day.** Variants (a quiet day, a packed day) can reuse one geometry. Name the variant
   in `brief.variant`; never blend them.
4. **Scale is a design decision.** A realistic nave takes minutes to walk. Decide whether to
   compress, speed up, or pace landmarks so something pulls the eye every hundred metres.
5. **Colour and light are claims.** The renders were cream and white with hard shadows; the real
   interior was painted and softly lit. A model that omits something known must say so in the
   opening: this is what `disclosure` and `departures` are for.
6. **The model has no crowd, no sound, no heat.** Say what the film leaves out; do not let
   music or a voice-over imply it was there.

The Crystal Palace history in source C (exhibits, ticket prices, anecdotes) is *not* in this
skill. It is a list of leads for `FACTCHECK.md`.

## Honesty: two kinds of fact

- **Model facts** — what is in the file: dimensions, counts, bounds, what was built from what.
  They come from `route_check.py survey` or the `blender-build` census, or from a controls file.
  Narration cites them with `source: "model"` and an `evidence` key.
- **World facts** — what was true of the place or the object. They need a row in `FACTCHECK.md`
  with a source and a verdict. Narration cites them with `source: "world"` and a `fact` id.

A model is never the world. The opening says which kind of model this is (`measured`,
`interpretive`, `stylized`, `invented`) and what it leaves out. An interpretive model that lists
no departures from its sources has not been examined, and the gate warns.

## Asset mode

For one game asset, replace "route" with "views": establish → silhouette → scale → detail →
material → topology → closing. Turntable at constant angular speed, at least 8 s a turn.
50–85 mm. A neutral background and a three-point key. **Show scale** with a 1.8 m figure, a grid or a ruler.
Topology shots quote the *evaluated* triangle count from the survey (a count that ignores a
modifier is wrong). Claim "in the engine" only with a recorded import (the `walker` validator and
an engine capture); otherwise say the asset has not been imported. A rigged asset's articulation
is shown by a pose rendered from the rig, never a crossfade between stills.

## Corrections to the pasted sources (Blender 5.1.2)

- Source B names the **Nishita** sky. Blender 5.1.2's Sky Texture lists `SINGLE_SCATTERING`,
  `MULTIPLE_SCATTERING`, `PREETHAM`, `HOSEK_WILKIE`. Use `MULTIPLE_SCATTERING` for a physical sky.
- Source B says "EEVEE Next". Since Blender 5.0 the engine id is `BLENDER_EEVEE`.
- Neither source says what speed a Follow Path rig actually produces. Measured on 5.1.2:
  **Offset Factor with Fixed Position moves at constant speed along the path's length, even
  where control points are unevenly spaced, but only when the keyframes are LINEAR**, and
  Python's `keyframe_insert()` ignores the preference that sets the default interpolation, so
  the keys must be set on the F-curves. See the rig reference.
