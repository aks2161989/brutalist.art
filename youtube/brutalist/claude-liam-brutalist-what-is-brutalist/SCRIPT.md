# SCRIPT.md — What Is Brutalist?

*Brutalist playlist · claude-liam · @HumanitariansAI · Kokoro am_onyx · Teardown register · No captions.*

Every line below is spoken verbatim by Kokoro `am_onyx` (Liam, in for Bear).
Audio durations measured on 2026-09-07 are the master clock; visuals conform
to them, not the other way around.

---

## B00 — ASK (16.79 s)

> Ciao. This is Liam, in for Bear. Brutalist is a video toolkit for Humanitarians AI fellows, but it isn't a video editor. It's film as code. The recipe lives on GitHub, the rendered film lives on Drive, and the version history lives in commits. Here is what that actually means when you sit down to build one.

## B01 — BLUF · hesitant writer (20.03 s, `lead_silence_s: 0.8`)

> Most people hear video toolkit and picture an editor. Timelines, drag and drop, sliders. That is not what this is. Brutalist is the plain-text recipe your film is built from. Change the recipe, run the pipeline, and a new film comes out. That is the whole idea, and it is worth caring about because it means your film is versionable, reviewable, and rebuildable — like any other piece of code.

On screen, the writer first types **"Brutalist is a video editor for AI clips."**,
pauses, turns the phrase terracotta, deletes it, and types
**"the plain-text recipe your film is built from."** The final sentence sits
corrected — that final sentence is the reel's claim.

## B02 — FRAMEWORK · film as code (16.49 s)

> So what is the recipe? It is one file. beat_sheet dot json. Every beat carries its own line of narration, its own visual, its own timing. Read the JSON top to bottom and you have read the film. Render it and the plan becomes pixels. That is what film as code means — the film is the thing the recipe cooks.

## B03 — WORKED EXAMPLE · pipeline (19.52 s)

> Here is the pipeline the recipe travels through. You write a brief in plain English. Claude drafts the beat sheet from it. Kokoro reads every narration line aloud, locally, for free — and the audio is measured first. Those measurements become the master clock. Then every scene renders, conforms to the voice, and the compiler muxes it all into a four K master. One pass through the machine.

## B04 — WORKED EXAMPLE · pure function (18.11 s)

> Watch what change actually costs. Here is beat zero's greeting field — Ciao, Liam. Edit that one string to Hola, re-render only beat zero, and the greeting on screen becomes Hola. Nothing else moves. No timeline nudge, no manual conform. Every visual is a pure function of the recipe. Change one field, one thing on screen changes.

## B05 — DIVISION OF LABOR (21.61 s)

> This is where fellows miscount the work. Taste is not a step Claude does slowly — it is a step it cannot do. So the pipeline splits the labor. Your lane is judgment. You write the brief, watch the cut, ask for a fix, decide whether it publishes. Claude's lane is execution. It drafts the beat sheet, generates the narration, renders every scene, compiles the master, verifies the file. Four things stay with you. Five things stay with the agent.

## B06 — FALSIFIABILITY (20.46 s)

> Now the honest part — the part every practical tool needs. Brutalist does not upload. It renders a four K file and stops. Brutalist does not require a paid API. Kokoro is local, and Claude runs on your subscription. And Brutalist is not a judge of taste. It will render any bad idea you feed it. Watching the cut and deciding it is worth releasing is your job. Those three limits are the shape of the tool.

## B07 — VERDICT (14.44 s)

> Verdict, in three lines. The recipe is text — read the JSON, read the film. The film is a pure function of the recipe — change one property, one thing on screen changes. And the judgment is yours — everything else can be automated. That is what Brutalist actually is.

## B08 — YOUR TURN (17.98 s)

> Your turn. Open Claude Code in an empty folder and paste this prompt. It clones the public Brutalist toolkit, runs the free installer, and asks you what your first film should be about. When Claude hands back the preview, watch it — the whole way through. If a beat lands wrong, say so in plain English. Rebuild beat five. That is the loop. Now you know what Brutalist is.

The prompt that types into the composer:

> Clone https://github.com/nikbearbrown/brutalist.art into this folder, run ./setup --install for me, then draft a beat sheet for a two-minute Brutalist film about my current project. Keep me out of the terminal — just tell me what to approve.

## B09 — OUTRO (4.86 s)

> That was What Is Brutalist? Liam, in for Bear. For Humanitarians AI.

---

**Total narration:** 170.29 s (≈ 2 min 50 s). Duration follows the content; no
padding was added to reach a target. The compiler conforms every visual clip to
its beat's measured audio window.
