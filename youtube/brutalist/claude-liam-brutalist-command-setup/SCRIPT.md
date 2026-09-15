# SCRIPT.md — Brutalist Command: setup

Voice: Liam (in for Bear), Kokoro `am_onyx`. Register: Teardown. Playlist: Brutalist. Channel: @HumanitariansAI (footer chip). Outro card handle: @NikBearBrown (locked, flagged for human review).

Greeting: **Konnichiwa, Liam** (Japanese, one word, fresh — does not repeat any prior Brutalist-command greeting).

---

## B00 · ASK — cold open composer

> Konnichiwa, this is Liam, in for Bear. The ask — before I fill a single beat sheet, tell me what's actually installed on this box. Don't install anything. Just verify.

## B01 · BLUF — hesitant writer

> Watch the writer walk this back. Setup does not install everything by default. It verifies, live — imports every Python module, runs ffmpeg, and makes Kokoro actually speak. Only if you add dash dash install does it fetch anything. A green row is a spoken proof, not a receipt from a package manager.

## B02 · FRAMEWORK — the setup surface

> The setup script is the source of truth. Sixteen lines of header at the top: shebang, two modes, one honest sentence about what a green table proves. Bare `./setup` verifies and prints the readiness table. `./setup --install` installs the core Python dependencies, Remotion's node modules, the fonts, and the Kokoro model — then runs the same verification.

## B03 · FRAMEWORK — the pip contract

> Under `--install`, the whole Python surface comes from one file: `requirements.txt`. Kokoro pinned at greater-than-or-equal zero point four — the free voice engine, no key. Mutagen at forty-seven for MP3 duration; that's the master clock. Pillow ten point two for slates. Manim eighteen for animation. Faster-whisper one for captions. And numpy pinned above two point zero point two, because Kokoro's release requires it, and Manim eighteen has no upper bound to fight. Six lines of pinning; that's the whole contract.

## B04 · WORKED_EXAMPLE — the all-green run

> Here is a ready toolkit. Ffmpeg on the path, Python packages importable, Node twenty for Remotion, the two font families installed, and the Kokoro model files present. Seven rows, all green. Cost line: zero dollars. Exit code: zero. That is a setup pass.

## B05 · MECHANISM — the --install pipeline

> Add dash dash install and setup does four things, in order, before it verifies. One: pip installs from requirements dot txt — break-system-packages first for the modern pip, plain second as a fallback. Two: change into runtime slash remotion and npm install. Three: copy the bundled fonts into the user font directory, and download Oswald from Google Fonts if it's missing. Four: only if the Kokoro model files are absent, curl them from the kokoro-onnx releases page. Every step's exit code is captured; every failure widens the fail path — but no install turns a row green on its own.

## B06 · MECHANISM — bash 3.2 safe

> Under the hood, one small design choice makes this script portable. Macos ships bash three point two by default — no associative arrays. So instead of declaring an array, the check helper uses eval to write two dynamic variables per test: OK-underscore-ID and MISS-underscore-ID. That is why setup runs the same on a Mac and on Linux, without a bash five prerequisite.

## B07 · MECHANISM — live verification

> Here is the part that makes the whole script honest. Readiness is decided ONLY by live verification. A successful pip install is not enough. For the audio feature to turn green, setup runs setup-underscore-smoke-underscore-kokoro dot py, which synthesizes one throwaway phrase and checks that the decoded audio's mean volume exceeds negative forty decibels. A silent WAV is a failure. Kokoro has to actually speak to earn the green row.

## B08 · MECHANISM — the ElevenLabs guard

> And one more design choice, unique to this script. Before any check runs, setup greps the whole toolkit for four fingerprints of a paid voice provider: the API-key environment variable, the domain, the engine string in a JSON, and the xi-api-key header. If any of them shows up in a file that isn't this setup script itself, the whole script exits one and lists the offending files. Free-by-default isn't a slogan; it's a guard that refuses to start the day the pattern comes back.

## B09 · FAILURE_RECOVERY — one file missing

> One failure worth showing. Unlink the Kokoro model directory — the models are the one thing not in the git repo, because they're three hundred megabytes. Re-run setup. Audio row goes red. Two hint lines print underneath: the model files are missing, and the synth-and-decode phrase failed. Every other row stays green. Exit code: one. Recovery: put the files back — or on a fresh install, run setup with dash dash install and the fourth phase of the pipeline downloads them for you. The exit code is the whole point — a red row never ships a build.

## B10 · VERDICT — artifact card

> So — setup. A live-verification readiness checker, with an optional install-first mode. Two modes, one script, one seven-row table. It reads requirements dot txt for the pip contract, it makes Kokoro speak for the audio row, it refuses to run if a paid provider is smuggled in, and it exits zero only when every atomic check passes live. Run this before you fill a beat sheet, and downstream failures with cryptic messages become failures with a checklist.

## B11 · YOUR_TURN — HANDOFF

> Your turn. Paste this into Claude Code, pointed at your own copy of the toolkit: run ./setup, save the whole output, then — without installing anything — for each red row, name the atomic check ID that failed and quote the fix hint the script printed underneath. Also grep the toolkit for the four ElevenLabs fingerprints setup guards against, and tell me whether any file outside of setup itself matches. Look for whether Claude is tempted to run ./setup --install to make the table green. That is the one thing I did not ask for. Verification is not remediation.

## B12 · OUTRO

> Brutalist Command: setup. Liam, in for Bear, for at Humanitarians A I.
