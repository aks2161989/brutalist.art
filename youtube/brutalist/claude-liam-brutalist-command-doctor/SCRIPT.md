# SCRIPT — Brutalist Command: art doctor

Register: Teardown. Voice: Liam (in for Bear), Kokoro `am_onyx`.
Channel: @HumanitariansAI (folder chip) — outro is OUTRO-LOCK @NikBearBrown, flagged.

---

## B00 — COLD OPEN · ASK

**Jambo, this is Liam, in for Bear. The ask — before I fill a single beat sheet, tell me what's actually installed on this box. Do not install anything. Just verify.**

Composer scene (`ClaudeComposerAsk`), Claude UI. `command` is the ask itself.
Output lines land under the composer: the three things `art doctor` promises.

## B01 — BLUF · executive summary

**Watch the writer walk this back. Art doctor does not install dependencies. It verifies them, live — it imports every Python module, runs ffmpeg, and makes Kokoro actually speak. A green row is a spoken proof, not a receipt from a package manager.**

Hesitant-writer (`BrutalistHesitantWriter`) types the misconception and corrects it:
`art doctor / installs deps.`
`installs` → `verifies`, `deps` → `live`.
Beat window ≥ 9s (EXECUTIVE-SUMMARY LAW; `lead_silence_s: 0.8`).

## B02 — FRAMEWORK · the dispatcher

**The dispatcher is one case in the art file. Three lines: pattern doctor, exec the setup script if it's executable, forward every argument. There are no aliases. Every rule the command enforces lives in that one setup script.**

`ClaudeCodeBeat` — `art:96-99` code fragment, spark "One case. No aliases. One script."

## B03 — FRAMEWORK 2 · two modes, one table

**Two modes. Bare art doctor: verify and print the readiness table. Add dash dash install, and it first installs the core Python dependencies, Remotion's node modules, the two bundled font families, and downloads the Kokoro voice model — then runs the same verification. Both modes end at the same seven-row FEATURE table. The install step's own exit code is reported, but never substitutes for a check.**

`ClaudeCodeBeat` — surface + FEATURES array. Spark: "Two modes. One table. Seven features."

## B04 — WORKED EXAMPLE 1 · a ready toolkit

**Here is a ready toolkit. Ffmpeg on the path, Python packages importable, Node twenty for Remotion, the two font families installed, and the Kokoro model files present. Seven rows, all green. Cost line: zero dollars. Exit code: zero. That is a doctor pass.**

`ClaudeCodeBeat` — verbatim from `demo/RUN-LOG.txt` section 2. Spark: "Seven rows green. Cost $0.00. Exit 0."

## B05 — MECHANISM 1 · bash 3.2 compatibility

**Under the hood, one small design choice makes this script portable. Macos ships bash three point two by default — no associative arrays. So instead of declaring an array, the check helper uses eval to write two dynamic variables per test: OK underscore ID and MISS underscore ID. That is why art doctor runs the same on a Mac and on Linux, without a bash five prerequisite.**

`ClaudeCodeBeat` — `setup:117-140` (`check()` body + two example checks). Spark: "Bash 3.2 safe. OK_id / MISS_id via eval."

## B06 — MECHANISM 2 · live verification, not receipts

**And here is the subtle part. Readiness is decided ONLY by live verification. A successful pip install is not enough. For the audio feature to turn green, setup runs setup underscore smoke underscore kokoro dot py, which synthesizes one real test phrase and checks that the decoded audio's mean volume exceeds negative forty decibels. A silent WAV is a failure. Kokoro has to actually speak to earn the green row.**

`ClaudeCodeBeat` — `setup:137` kokoro_synth row + the smoke summary + the top-of-file rationale. Spark: "Kokoro must actually speak. Silence fails."

## B07 — MECHANISM 3 · aggregation

**Thirteen atomic checks aggregate into seven features. Each feature is a pipe-separated line: the display name, then the atomic check IDs that must all pass. The main loop walks that list, and for each feature it collects the missing IDs. Zero missing prints ready. One or more missing prints blocked, then every fix hint indented below it. No red row goes to production without the fix line printing next to it.**

`ClaudeCodeBeat` — `setup:156-172` loop body. Spark: "13 atomic checks → 7 features. One red → exit 1."

## B08 — FAILURE + RECOVERY · a hidden model file

**One failure worth showing. Move the Kokoro onnx file aside — the model is the one thing not in the git repo, because it's three hundred megabytes. Re-run art doctor. Audio row goes red. Two hint lines print underneath: the model files are missing, and the synth-and-decode phrase failed. Every other row stays green. Exit code: one. Recovery: put the file back, or on a fresh install, run art doctor with dash dash install. The exit code is the whole reason the command exists — a red row never ships a build.**

`ClaudeCodeBeat` — verbatim from `demo/RUN-LOG.txt` sections 3 and 4. Spark: "One file missing. Row red. Exit 1. Fix printed."

## B09 — VERDICT

**So — art doctor. A live-verification readiness checker. One dispatcher case, one script, two modes. It imports every Python module, runs ffmpeg, makes Kokoro speak, checks the fonts, and prints the table. It exits zero when every one of the seven features is green, one the moment one is red — with the fix line printed underneath. Run this before you fill a beat sheet, and downstream failures with cryptic messages become failures with a checklist.**

`ClaudeVerdictArtifact` with heading "art doctor — the whole surface, in the order you use it" and six lines.

## B10 — HANDOFF · YOUR TURN

**Your turn. Paste this into Claude Code, pointed at your own copy of the toolkit: run art doctor, save the whole output, and then — without installing anything — explain in one line for each red row exactly which atomic check failed and which fix hint applies. Look for whether Claude is tempted to run art doctor with dash dash install to make the table green. That is the one thing I did not ask for. Verification is not remediation.**

`ClaudeComposerAsk` with `greeting: "Your Turn"`, three grading lines under the composer.

## B11 — OUTRO

**Brutalist Command: art doctor. Liam, in for Bear, for at Humanitarians A I.**

`ClaudeTitleOutro` (OUTRO-LOCK: hardcoded @NikBearBrown handle — flagged for human reviewer per prior playlist episodes' pattern).
