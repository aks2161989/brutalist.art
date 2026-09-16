# SCRIPT — Brutalist Utility: remotion_scenes.py
# Episode 53 · @HumanitariansAI Brutalist playlist
# Persona: Liam, in for Bear · Voice: Kokoro am_onyx

---

## B00 — COLD OPEN (ClaudeComposerAsk)

Sawadee — this is Liam, in for Bear. remotion_scenes.py is the Brutalist
pipeline's Remotion runner. It looks like a thin shell around npx remotion
render. It's not. It's a gated, provenance-stamping layer that makes scene
rendering safe, repeatable, and traceable for every beat in the reel.

---

## B01 — BLUF (BrutalistHesitantWriter)

[Written text, corrected on screen]
"remotion_scenes.py renders ALL your Remotion scenes.
Point it at a reel — every blank beat fills.
It is just a thin wrapper for the Remotion CLI."

[Corrections: ALL → only pattern-tagged slates; thin → gated provenance-stamper]

Narration: remotion_scenes.py renders only pattern-tagged slate beats — not every
scene, not anything you point it at. It's a gated provenance-stamper: it reads the
beat sheet, checks what's already filled, renders the gaps, then writes the receipts.

---

## B02 — FRAMEWORK (SkillTeardownPipeline)

Four steps, one pass. First, detect: slate_resolves checks each beat — if media
slash BXX dot mp4 already exists, skip it. Second, render: npx remotion render,
scale two, CRF sixteen. Third, extend: the last frame freeze-holds to match the
measured audio duration. Fourth, stamp: provenance is written back into beat_sheet.json,
and the consumer index is updated.

---

## B03 — THE ENTRY TICKET (ClaudeCodeBeat)

[Shows: shot.remotion.pattern JSON in a beat]

The script ignores every beat that doesn't have shot dot remotion dot pattern set.
That single field is the entry ticket. No pattern, no render — the beat stays a
slate. The pattern also selects which Remotion composition to render by name.

---

## B04 — THE RENDER CORE (ClaudeCodeBeat)

[Shows: the npx remotion render command assembled in render_beat()]

render_beat builds this command: npx remotion render, the entry point, the
composition name, a temp candidate path, and three quality flags. Scale two
supersamples the 1920 by 1080 composition to true 4K. Image-format png removes
Remotion's default JPEG quality ceiling on flat brand color. CRF sixteen gives
a clean master. Props are written to a temp file and passed with --props.

---

## B05 — MATCHING THE AUDIO CLOCK (ClaudeCodeBeat)

[Shows: the extend_clip_to_duration ffmpeg command]

Remotion compositions end when the animation ends — at a fixed frame count.
Audio beats can be longer. Without intervention, compile.py would slow-motion
stretch a short clip to fill extra time. extend_clip_to_duration prevents that:
it appends freeze-frames by cloning the last frame with ffmpeg's tpad filter,
holding the clip exactly as long as the measured audio duration.

---

## B06 — THREE GATES (FormBCard)

[Shows: three gate functions]

Three gates run before any beat renders. validate_project checks the beat sheet
is structurally sound. validate_approvals is the fellows safety gate — a reel
that requires approval cannot render until it has one. slate_resolves is the
idempotency check: media file already there and no --force flag? Skip. Reruns
are always safe.

---

## B07 — DEMO: --list (ClaudeCodeBeat)

[Shows: actual terminal output from the --list flag demo]

The --list flag shows every beat carrying shot dot remotion dot pattern — without
rendering anything. State is SLATE or filled. B00 and B01 are slates. B02 shows
as filled because media slash B02 dot mp4 exists on disk. B03 has no pattern field
and doesn't appear at all. This is the safe way to audit a reel before a long
render pass.

---

## B08 — FAILURE MODE (SkillTeardownMechanism)

[Shows: FAIL: exit behavior]

When npx remotion render exits nonzero, render_beat returns a FAIL: string with the
pattern name and the last 800 bytes of stderr. The beat goes into the failures list.
The script continues to the next beat. At the end, failures go to stderr and exit
code two is returned. The previous media slot is never overwritten — atomic_json
and os.replace keep it clean. Fix the composition, run again with --force --only BXX.

---

## B09 — VERDICT (ClaudeVerdictArtifact)

The verdict: remotion_scenes.py is the safe boundary between your beat sheet and
Remotion. You get supersampled 4K output, audio-clock-matched clips, idempotent
reruns, approval gates, and failure isolation — none of which npx remotion render
gives you on its own. Run it before compile.py, never after.

---

## B10 — YOUR TURN (ClaudeComposerAsk)

Your turn. Paste this prompt into Claude with your reel path. Ask it to run
remotion_scenes.py, then read the consumer index and confirm the pattern was
recorded. What you should see in Claude's answer: the command, SLATE or filled
status lines, the updated consumers.json entry, and exactly what --force would
re-render versus skip.

---

## B11 — OUTRO (ClaudeTitleOutro)

Brutalist Utility: remotion_scenes.py. Liam, in for Bear. @NikBearBrown.
