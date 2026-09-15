# SCRIPT.md — Brutalist Command: setup — Short

Retained narration, in order. Every line is copied verbatim from the parent vertical's per-beat MP3 audio (no regenerated audio in this derivative).

## B00 — ASK (cold open)

> Konnichiwa, this is Liam, in for Bear. The ask — before I fill a single beat sheet, tell me what's actually installed on this box. Don't install anything. Just verify.

## B01 — BLUF (hesitant writer)

> Watch the writer walk this back. Setup does not install everything by default. It verifies, live — imports every Python module, runs ffmpeg, and makes Kokoro actually speak. Only if you add dash dash install does it fetch anything. A green row is a spoken proof, not a receipt from a package manager.

## B04 — WORKED_EXAMPLE (the green pass)

> Here is a ready toolkit. Ffmpeg on the path, Python packages importable, Node twenty for Remotion, the two font families installed, and the Kokoro model files present. Seven rows, all green. Cost: zero dollars. And setup tells you directly — a green table means the dependency checks passed, not that a video actually renders. Run art smoke for that end-to-end proof. Exit zero.

## B09 — FAILURE_RECOVERY (unlink the models)

> One failure worth showing. Unlink the Kokoro model directory — the models are the one thing not in the git repo, because they're three hundred megabytes. Re-run setup. Audio row goes red. Two hint lines print underneath: the model files are missing, and the synth-and-decode phrase failed. Every other row stays green. Exit code: one. Recovery: put the files back — or on a fresh install, run setup with dash dash install and the fourth phase of the pipeline downloads them for you. The exit code is the whole point — a red row never ships a build.

## B10 — VERDICT

> So — setup. A live-verification readiness checker, with an optional install-first mode. Two modes, one script, one seven-row table. It reads requirements dot txt for the pip contract, it makes Kokoro speak for the audio row, it refuses to run if a paid provider is smuggled in, and it exits zero only when every atomic check passes live. Run this before you fill a beat sheet, and downstream failures with cryptic messages become failures with a checklist.

## B12 — OUTRO

> Brutalist Command: setup. Liam, in for Bear, for at Humanitarians A I.

## Cut coherence

- B00 → B01: the ask ("verify, don't install") is directly answered by the hesitant-writer correction ("setup verifies live").
- B01 → B04: the misconception is corrected, then the next beat shows what a real green pass looks like.
- B04 → B09: green pass → the one failure worth showing (the model dir unlinked).
- B09 → B10: the recovery ends on "the exit code is the whole point"; verdict then re-states the six-line surface.
- B10 → B12: verdict → outro title + handle.

B09 forward-references "the fourth phase of the pipeline"; this is self-explanatory in-line ("run `./setup --install` and the fourth phase downloads them for you") and does not require the cut B05 MECHANISM 1 walkthrough to make sense.
