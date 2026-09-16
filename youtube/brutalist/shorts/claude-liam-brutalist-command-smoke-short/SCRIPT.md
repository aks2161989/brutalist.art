# SCRIPT.md — Brutalist Command: art smoke — Short (9:16, 2:07)

Narration is **verbatim from the parent reel**. Nothing was rewritten. This
Short is a whole-beat cut of
`youtube/brutalist/claude-liam-brutalist-command-smoke/vertical/` (see
CUT-PLAN.json). Voice: Kokoro `am_onyx` (Liam, in for Bear).

## B00 — ASK (9.67 s)

Aloha, this is Liam, in for Bear. The ask — art doctor is all green on this
box. Prove to me the pipeline actually renders a video, not just that the
imports work.

## B01 — BLUF (14.38 s)

Watch the writer walk this back. Art smoke does not check dependencies — art
doctor already does that, in isolation. Smoke renders a real video, decodes
it, and measures the audio. A green result is a decoded mp4, not a passing
import.

## B03 — FRAMEWORK (33.00 s)

What smoke_test.sh actually does. It copies the tiny fixture at examples
slash underscore smoke into a throwaway scratch directory, then walks it
through the real pipeline — Kokoro narration, then run dot sh's render and
compile pass, then three verify gates on the compiled mp4 that actually lands
on disk. Size — greater than twenty thousand bytes. Type — ffprobe decodes
both a video and an audio stream. Audio — ffmpeg volumedetect reads a mean
volume above negative forty decibels. Every one of those numbers comes out
of the DECODED file, not the process exit code.

## B07 — FAILURE_RECOVERY (37.96 s)

One failure worth showing — the real one on tip of tree today. Run art smoke
against the shipped fixture and it exits one at GATE zero, before Kokoro
even loads. The reason is not a missing dependency. It is a static
validator, added recently to fail closed on unsafe slugs, that rejects the
fixture's own slug because it starts with an underscore. And this is exactly
why art smoke exists. Art doctor on the same box is all green — the imports
are fine — but the pipeline cannot render this fixture. Recovery is a
one-line patch: rename the fixture slug from underscore-smoke to smoke, or
widen the regex to accept the fixture the toolkit ships with. Fix that one
thing and the same pipeline lands a green mp4.

## B08 — VERDICT (27.17 s)

So — art smoke. The end-to-end proof. One dispatcher case, no flags. It
builds a bare fixture in a throwaway scratch dir, drives it through Kokoro
and run dot sh's real skip paths, and then reads the compiled mp4 back from
disk with three decoded gates. It exits zero when SIZE, TYPE, and AUDIO all
clear. Run it after art doctor whenever you touch anything in the render or
compile paths. A green art doctor means the deps import. A green art smoke
means a fellow can actually make a video today.

## B10 — OUTRO (5.25 s)

Brutalist Command: art smoke. Liam, in for Bear, for at Humanitarians A I.
