# SCRIPT.md — Brutalist Command: art smoke

Register: Teardown. Voice: Kokoro `am_onyx`. Persona: Liam, in for Bear.

## B00 — ASK (cold open)

Aloha, this is Liam, in for Bear. The ask — art doctor is all green on
this box. Prove to me the pipeline actually renders a video, not just
that the imports work.

## B01 — BLUF (hesitant writer)

Watch the writer walk this back. Art smoke does not check dependencies —
art doctor already does that, in isolation. Smoke renders a real video,
decodes it, and measures the audio. A green result is a decoded mp4,
not a passing import.

## B02 — FRAMEWORK (dispatcher)

The dispatcher is one case in the art file. Two lines: pattern smoke,
exec the smoke test script, forward every argument. There are no flags —
the command has zero surface area. Every rule the command enforces lives
in that one shell script.

## B03 — FRAMEWORK (pipeline + gates)

What smoke_test.sh actually does. It copies the tiny fixture at
examples slash underscore smoke into a throwaway scratch directory,
then walks it through the real pipeline — Kokoro narration, then run
dot sh's render and compile pass, then three verify gates on the
compiled mp4 that actually lands on disk. Size — greater than twenty
thousand bytes. Type — ffprobe decodes both a video and an audio stream.
Audio — ffmpeg volumedetect reads a mean volume above negative forty
decibels. Every one of those numbers comes out of the DECODED file,
not the process exit code.

## B04 — MECHANISM (the fixture)

The fixture is intentionally minimal. Two narration slates, zero Manim,
zero Remotion. That's the point — smoke is not testing a specific
composition, it's testing that Kokoro, run dot sh's skip paths, and
compile dot py glue together into a watchable file. A brand-new Remotion
scene that broke Ken Burns rendering would still let art doctor come up
green. Smoke is the test that would fail.

## B05 — MECHANISM (GATE AUDIO)

The important gate is GATE AUDIO. It does not read the source mp3s —
those already synthesized fine at GATE zero. It decodes the mp4 that
just landed on disk with ffmpeg volumedetect and pulls the mean volume
out of the log. A silent mp4 with an audio stream still fails, because
a muxed-but-silent track has a mean volume near negative infinity.
Negative forty decibels is the floor. Real narration comes in around
negative twenty.

## B06 — WORKED EXAMPLE (the pass path)

Here is a passing run — the Kokoro model files present, ffmpeg on the
path, and the fixture slug patched in the scratch copy so the new
validator accepts it. Every stage lands. Kokoro synthesizes both beats.
Run dot sh compiles the slate cut. And the three decoded gates read a
real mp4: six hundred thirty six thousand bytes, both streams, mean
volume negative twenty four decibels. Cost: zero dollars. Exit code:
zero. That is a smoke pass.

## B07 — FAILURE / RECOVERY (the shipped-fixture regression)

One failure worth showing — the real one on tip of tree today. Run art
smoke against the shipped fixture and it exits one at GATE zero,
before Kokoro even loads. The reason is not a missing dependency. It
is a static validator, added recently to fail closed on unsafe slugs,
that rejects the fixture's own slug because it starts with an
underscore. And this is exactly why art smoke exists. Art doctor on
the same box is all green — the imports are fine — but the pipeline
cannot render this fixture. Recovery is a one-line patch: rename the
fixture slug from underscore-smoke to smoke, or widen the regex to
accept the fixture the toolkit ships with. Fix that one thing and the
same pipeline lands a green mp4.

## B08 — VERDICT

So — art smoke. The end-to-end proof. One dispatcher case, no flags.
It builds a bare fixture in a throwaway scratch dir, drives it through
Kokoro and run dot sh's real skip paths, and then reads the compiled
mp4 back from disk with three decoded gates. It exits zero when SIZE,
TYPE, and AUDIO all clear. Run it after art doctor whenever you touch
anything in the render or compile paths. A green art doctor means the
deps import. A green art smoke means a fellow can actually make a
video today.

## B09 — YOUR TURN (handoff)

Your turn. Paste this into Claude Code, pointed at your own copy of
the toolkit. Run art smoke, save the whole output, then read smoke
test dot sh in the runtime scripts directory and, without changing
any of it, tell me — in one line each — which of the three decoded
gates the run reached, which one refused, and what one file the
failing gate actually looked at. Watch for whether Claude is tempted
to rewrite the script to make it pass. It should not. The gates are
the point; the fix is upstream.

## B10 — OUTRO

Brutalist Command: art smoke. Liam, in for Bear, for at Humanitarians A I.
