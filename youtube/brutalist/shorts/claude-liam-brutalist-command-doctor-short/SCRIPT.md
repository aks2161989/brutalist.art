# SCRIPT — Brutalist Command: art doctor — Short

8 beats · 140.75 s · 2160×3840 · Kokoro `am_onyx` · Liam, in for Bear.

Whole-beat cut of the parent vertical companion; retained narration is
copied verbatim from the parent beat sheet (no rewrites in this Short).

## B00 · ASK (9.54 s)

> Jambo, this is Liam, in for Bear. The ask — before I fill a single beat
> sheet, tell me what's actually installed on this box. Do not install
> anything. Just verify.

## B01 · BLUF (14.92 s, 0.8 s lead silence)

> Watch the writer walk this back. Art doctor does not install dependencies.
> It verifies them, live — it imports every Python module, runs ffmpeg, and
> makes Kokoro actually speak. A green row is a spoken proof, not a receipt
> from a package manager.

## B03 · FRAMEWORK (22.08 s)

> Two modes. Bare art doctor: verify and print the readiness table. Add
> dash dash install, and it first installs the core Python dependencies,
> Remotion's node modules, the two bundled font families, and downloads the
> Kokoro voice model — then runs the same verification. Both modes end at
> the same seven-row FEATURE table. The install step's own exit code is
> reported, but never substitutes for a check.

## B04 · WORKED EXAMPLE (15.75 s)

> Here is a ready toolkit. Ffmpeg on the path, Python packages importable,
> Node twenty for Remotion, the two font families installed, and the Kokoro
> model files present. Seven rows, all green. Cost line: zero dollars.
> Exit code: zero. That is a doctor pass.

## B06 · MECHANISM (23.46 s)

> And here is the subtle part. Readiness is decided ONLY by live
> verification. A successful pip install is not enough. For the audio
> feature to turn green, setup runs setup underscore smoke underscore kokoro
> dot py, which synthesizes one real test phrase and checks that the decoded
> audio's mean volume exceeds negative forty decibels. A silent WAV is a
> failure. Kokoro has to actually speak to earn the green row.

## B08 · FAILURE / RECOVERY (27.17 s)

> One failure worth showing. Move the Kokoro onnx file aside — the model is
> the one thing not in the git repo, because it's three hundred megabytes.
> Re-run art doctor. Audio row goes red. Two hint lines print underneath:
> the model files are missing, and the synth-and-decode phrase failed.
> Every other row stays green. Exit code: one. Recovery: put the file back,
> or on a fresh install, run art doctor with dash dash install. The exit
> code is the whole reason the command exists — a red row never ships
> a build.

## B09 · VERDICT (22.67 s)

> So — art doctor. A live-verification readiness checker. One dispatcher
> case, one script, two modes. It imports every Python module, runs ffmpeg,
> makes Kokoro speak, checks the fonts, and prints the table. It exits zero
> when every one of the seven features is green, one the moment one is red
> — with the fix line printed underneath. Run this before you fill a beat
> sheet, and downstream failures with cryptic messages become failures with
> a checklist.

## B11 · OUTRO (5.17 s)

> Brutalist Command: art doctor. Liam, in for Bear, for at Humanitarians A I.

## Beats dropped from the Short

- B02 (FRAMEWORK, 13.00 s) — dispatcher case walkthrough
- B05 (MECHANISM, 20.21 s) — bash 3.2 `check()` + `OK_<id>/MISS_<id>` via eval
- B07 (MECHANISM, 21.12 s) — aggregation-loop walkthrough
- B10 (YOUR_TURN, 21.75 s) — Claude Code composer with paste-ready prompt

See `CUT-PLAN.json` for per-beat reasoning. All four are preserved in the
parent 16:9 master and the vertical companion.
