# FACTCHECK — Brutalist Command: art doctor — Short

Every factual claim in the *retained* narration of this Short, and where it
comes from. The Short is a whole-beat cut of the parent vertical companion
(SHA-256 `6841c2a078a80271abf298ffe2db0e8b4e571101373abc2d50144523effcb67d`);
dropped beats' claims are not in scope here — see the parent
`youtube/brutalist/claude-liam-brutalist-command-doctor/FACTCHECK.md` for the
full audit.

## Source files verified against the parent build (unchanged this run)

| File | SHA-256 | Read |
|---|---|---|
| `art` (dispatcher, toolkit root) | `9bb77a7c84701d23ab6e73f0a4f48592f17748ffad2c7114b62687bb7f97d0e9` | full |
| `setup` (the auditor)            | `75040062dfcb20d0437a5a358abc516ed6e4b1e4e9020aaac926e1b9d5b2208d` | full |

Hashes match the parent build's `SOURCE-SNAPSHOT.json` verbatim. No source
file was modified for this Short.

## Retained-narration claims → evidence

- **B01 "art doctor does not install; it verifies live"** — `setup:57` reads
  `if [ "${1:-}" = "--install" ]; then`, the only branch condition; the
  default path runs the verifier below. The BLUF corrects the misconception
  that the bare invocation installs anything.
- **B03 "two modes: bare `./art doctor` verifies; `--install` installs pip
  deps + Remotion npm + fonts + Kokoro model, THEN verifies"** — the same
  `setup:57` branch guard, plus the seven-row `FEATURES` array at
  `setup:142-150` printed verbatim.
- **B03 / B04 "seven features"** — `setup:142-150`, exact count of seven
  pipe-separated rows.
- **B04 "verbatim ready run: 7 rows green, Cost $0.00, exit 0"** — captured
  in the parent reel's `demo/RUN-LOG.txt` section 2; the code beat renders
  the exact stdout of a green run on this workstation.
- **B06 "live verification only — Kokoro must actually SPEAK a phrase above
  -40 dB"** — `setup:137` is the `kokoro_synth` check, exec'ing
  `runtime/scripts/setup_smoke_kokoro.py`; setup's top-of-file docblock
  (`setup:12-15`) states verbatim: *"Readiness is decided ONLY by live
  verification below — importing every Python dep, actually running
  ffmpeg/ffprobe, and synthesizing + decoding one real Kokoro phrase
  (mean_volume > -40 dB). An install step's own exit code is reported
  (INSTALL_FAILED) but never substitutes for a check: a green table means
  the checks passed, not that `pip install` returned 0."*
- **B08 "hide the model file, audio row goes red, two hint lines print,
  exit 1"** — captured verbatim in the parent reel's `demo/RUN-LOG.txt`
  sections 3 and 4 (the model file was temporarily moved aside to force one
  red row; nothing else on the workstation was changed). Recovery paths
  quoted from `setup:89-98` (`--install` re-fetches the model from
  `thewh1teagle/kokoro-onnx` releases).
- **B09 "bare invocation wraps setup with $@ forwarded"** — `art:96-99`,
  exact `exec "$ART_HOME/setup" "$@"`.
- **B09 "13 atomic checks → 7 features"** — verified live in the parent
  build: `grep -c '^check ' setup` → `13`; FEATURES count is exactly 7
  (`setup:142-150`).
- **B09 "bash 3.2-safe: dynamic OK_<id>/MISS_<id> vars via eval"** —
  `setup:117-127`, comment "*macOS ships bash 3.2 by default (no
  `declare -A`)*"; the `check()` body uses `eval "OK_${id}=0"` /
  `eval "OK_${id}=1"` / `eval "MISS_${id}=\$3"`.
- **B09 "exit 0 all-green; exit 1 any-red"** — `setup:178`,
  `[ "$fail" = 1 ] && { r "Something is blocked — see above."; echo; exit 1; }`.
  Verified live in `demo/RUN-LOG.txt` sections 2/3/4: exit codes 0, 1, 0.
- **B11 outro "Brutalist Command: art doctor. Liam, in for Bear, for at
  Humanitarians A I."** — Liam is Kokoro `am_onyx`, in for Bear; the outro
  card handle is doctrine-locked to `@NikBearBrown` per `OUTRO-LOCK.md`
  and Liam reads the channel handle audibly. No claim of independent
  publication.

## Corrections carried from the parent (unchanged this run)

- Narration in the dropped beat B07 said "twelve atomic checks aggregate into
  seven features"; the file actually has thirteen atomic `check` rows. Since
  B07 is dropped from this Short, only the verdict line (B09) which says
  "13 atomic checks → 7 features" is on tape — that matches the file exactly.
- The `-40 dB` threshold is quoted exactly from `setup_smoke_kokoro.py`.

## Boundaries and honesty (this Short)

- `./art doctor --install` was NOT executed in this Short's build; nor was
  it executed in the parent build. All B08 recovery narration references the
  restore-the-file path AND the fresh-install path.
- No network calls, no paid API, no upload, no publication. The Short reuses
  audio and video that were already rendered for the parent's vertical
  companion; nothing was regenerated.
- Kokoro model files in the isolated toolkit are symlinks into the local
  `brutalist.art/` mirror; the audio feature checks the same two files
  either way, behavior is identical.
- The Short does not point at a published 16:9 URL because the parent has
  not been published yet. B09 ends the Short cleanly on its own.
