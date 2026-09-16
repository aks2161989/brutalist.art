# SCRIPT — The duration-planner Skill · Short (9:16)

Run id: `de2486504f054fb0952577d82d7fc24c`.
Parent reel: `youtube/brutalist/claude-liam-brutalist-skill-duration-planner/vertical/`.
Voice: Kokoro `am_onyx` (Liam, in for Bear). Captions: none.
Whole-beat cut of the parent film; every retained beat's narration is byte-identical to the parent's per-beat `mp3/`.

## Retained beats — verbatim narration

### B00 · ASK (14.58 s)
Sawadee, this is Liam, in for Bear. Today we tear down a skill that answers a question every fellow keeps hitting: how long should this video be? The honest answer is you don't decide. The content decides. The skill is called duration-planner, and here is how it actually works.

### B01 · BLUF (15.00 s)
The easy assumption is that duration is a target you hit — thirty seconds, one minute, five. The skill argues the opposite. Duration is an output. You size the script and let the content sit for the time it needs to land. Everything else is production convenience or padding.

### B04 · MECHANISM · Act 1 (21.71 s)
First design decision, and it's the thesis. Quote from the SKILL file: duration is an output, never a target. A complex mechanism lands at three or four minutes. A definitional explainer at thirty to sixty seconds. Both are correct. A uniform target has no learning basis — it's a production convenience that either compresses the content and destroys integration, or pads it and adds extraneous load. Either way, learning fails.

### B05 · WORKED EXAMPLE (22.54 s)
Second decision. Every beat has a content_type, and each content_type has a consolidation floor — the minimum time working memory needs to register the new element before the beat cuts. A title beat needs three to five seconds. A structure or geometric beat, six to eight. A mechanism step, six to ten. An equation step, seven to twelve. If your narration lands under the floor, don't shorten the next beat and don't speed up the voice. Add a hold.

### B07 · FALSIFIABILITY (24.33 s)
Here is where the skill bites. Once the idea has landed, adding decorative motion or filler graphics to reach one minute is a coherence violation — extraneous load that degrades learning. Padding to hit thirty seconds is exactly as wrong as compressing to hit it. And the six-minute engagement rule everyone quotes? That's a watch-time finding from open MOOCs. It doesn't replicate in real courses, and it isn't a learning result. The trade the skill accepts: shorter watchtime, cleaner schema.

### B08 · VERDICT (18.58 s)
The verdict. The duration-planner skill is small on disk and long on discipline. Content_type drives the floor. Kokoro drives the clock. Holds land the beats. Splits break up over-full ones. Total runtime is a byproduct — the skill reports it and stops. And it refuses to pad or compress to hit a number production wanted for its own convenience.

### B10 · OUTRO (3.96 s)
That was the duration-planner Skill. Liam, in for Bear.

## Dropped beats (per CUT-PLAN.json)

- **B02 · FRAMEWORK — Skill anatomy** — folder tree walkthrough belongs in the 16:9 long.
- **B03 · FRAMEWORK — Pipeline diagram** — five-phase pipeline is the mechanism proof B04/B05 already carry.
- **B06 · MECHANISM Act 3 — HOLD_FLOOR / assemble.py sync** — implementation detail; the B08 verdict recaps it in one line.
- **B09 · YOUR TURN — paste-ready duration-planner prompt** — long-form CTA; per REPOLOOP-SHORTS-PROMPT §4 a Short doesn't need to read the full exercise aloud.

## Measured runtime

- Total narration (kept beats): 120.71 s.
- Compiled Short: container 120.708 s / video 120.667 s / audio 120.708 s (all strictly < 180.0 s, 59.29 s of headroom).
