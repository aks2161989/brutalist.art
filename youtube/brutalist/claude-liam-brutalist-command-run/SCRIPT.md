# SCRIPT — Brutalist Command: art run

Voice: Kokoro `am_onyx` (Liam, in for Bear). Register: Teardown.
All beats narrated locally; no captions.

Estimated narrated length: **~272 s** at Kokoro `am_onyx` cadence.
Actual per-beat durations are stamped back into `beat_sheet.json` by
`generate_audio_kokoro.py`.

---

## B00 · ASK · `ClaudeComposerAsk` · greeting `Ciao, Liam`

> Ciao, this is Liam, in for Bear. One command drives the whole review
> loop for a Brutalist reel. Art run is the wrapper. It gates the
> paperwork, lints the beat mix, renders every pending scene, drops each
> clip into a slot, and recompiles a review cut. It writes a slate
> version — not the final master. That is a different verb.

## B01 · BLUF · `BrutalistHesitantWriter`

> Watch the writer walk this back. Art run does not render a final
> master. It compiles a review cut, with slate labels burned in for the
> beats you have not filled yet. Art final is the different verb — no
> beat markers, atomic verification, a real deliverable. Art run is the
> loop you live in until the review is clean.

`lead_silence_s: 0.8`. Correction: `renders → compiles`, `master → review`.

## B02 · FRAMEWORK · `ClaudeCodeBeat`

> The dispatcher is one case in the art file. Three lines: pattern run,
> exec bash on runtime slash scripts slash run dot sh, forward every
> argument. There are no aliases; the dispatcher matches only the exact
> string run. Everything the command does lives in that one shell script.

## B03 · MECHANISM · `ClaudeCodeBeat`

> Here is the loop the script actually runs, in order. Gate F — the
> paperwork triad: FACTCHECK, SHOTLIST, PROMPTS. Gate L — beat-mix
> lint: no single-sentence text slides. Gate SHAPE — finance
> chart-shape enforcement, if this is a finance reel. Gate A — static
> pre-flight on every pending Manim scene. Gate W — WCAG contrast and
> margins on the same scenes. Then it renders each pending Manim scene
> and runs Gate B — layout audit — on it before slotting. Then it fills
> every Remotion beat. Then it compiles a slate cut. Then Gate V —
> frame-level visual QC on the finished mp4. Any gate can stop the build.

## B04 · MECHANISM · `ClaudeCodeBeat`

> Audio is the master clock. The compiler conforms every clip to the
> per-beat mp3 duration — never the other way around. And art run only
> renders pending beats. If a slot is already filled — manim slash B03
> dot mp4 or media slash B03 dot mp4 — the script skips it and moves on.
> That is how you iterate. Change one beat, regenerate its audio, delete
> its old clip, re-run. Nothing else touches the disk.

## B05 · WORKED_EXAMPLE · `ClaudeCodeBeat`

> Here is a real invocation against a fixture reel with only a beat
> sheet in it. No paperwork. Art run reports two lines: no Manim beats,
> nothing to render. Then it hits Gate F, prints exactly which
> paperwork is missing, and stops. This is verbatim from the log.
> Nothing was invented for the video.

## B06 · MECHANISM · `ClaudeCodeBeat`

> Four knobs are worth knowing. ART underscore QC equals zero skips
> every gate. ART underscore STRICT equals zero downgrades gate warnings
> from blockers to slots-anyway. ART underscore FACTS equals zero is
> the previz exception — Gate F alone, off. Dash dash height picks the
> render height; the default is twenty-one sixty for four K. Everything
> else is forwarded to run dot sh unchanged.

## B07 · WORKED_EXAMPLE · `ClaudeCodeBeat`

> Two verbs, two files on disk. Art run writes slug dash slate dot mp4
> — the review cut with beat markers burned in. Art final writes slug
> dot mp4 — the clean master, only after every gate passes and after
> the compiler's atomic verification stamps a receipt beside it. If you
> see a slate label on your export, you ran the wrong verb. Both
> commands compile the same beats — the difference is what gets stamped
> on top and whether the receipt is written.

## B08 · FALSIFIABILITY · `ClaudeCodeBeat`

> And here is the loop in flight. Same fixture reel, same beat sheet,
> paperwork now written. Art run runs again. Gate F passes. Gate L
> passes. Gate SHAPE passes. Remotion is the next stage, and this
> particular workspace fails at browser launch — an environment issue,
> not a bug in the reel. The point is the gate order. Recovery: create
> the three files. Re-run. If the next failure is not yours, the log
> tells you which stage owns it.

## B09 · VERDICT · `ClaudeVerdictArtifact`

> So the surface. Art run gates the paperwork, lints the beat mix,
> pre-flights every pending Manim scene, renders it, audits its layout,
> fills the Remotion beats, compiles a slate cut, then frame-checks the
> finished mp4. It writes slug dash slate dot mp4, and it skips every
> slot already filled. There are no aliases. It is not the final
> command; art final is. Audio is the clock. Every gate can stop it.
> Every environment variable named ART underscore something can quiet
> one of those gates when you know what you are doing.

## B10 · YOUR_TURN · `ClaudeComposerAsk` · greeting `Your turn.`

> Your turn. Paste this into Claude Code from your reel folder. Run
> art run once. Read the last four lines. If a gate is the failure,
> the message names which one and how to unblock. If Remotion is the
> failure, read the beat id it printed and re-run that beat's audio and
> scene alone. Then re-run art run — it will skip every filled slot.
> The loop should shorten by one on every pass. If it does not, a slot
> is not being written, and the message names which one.

## B11 · OUTRO · `ClaudeTitleOutro`

> Brutalist Command: art run. Liam, in for Bear, for at Humanitarians A I.
