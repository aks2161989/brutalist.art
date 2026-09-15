# FACTCHECK — Brutalist Command: art doctor

Every factual claim in the reel, and where it comes from.

## Source files verified against this run

| File | SHA-256 | Read |
|---|---|---|
| `art` (dispatcher, toolkit root) | `9bb77a7c84701d23ab6e73f0a4f48592f17748ffad2c7114b62687bb7f97d0e9` | full |
| `setup` (the auditor)            | `75040062dfcb20d0437a5a358abc516ed6e4b1e4e9020aaac926e1b9d5b2208d` | full |

Both hashes match `SOURCE-SNAPSHOT.json` (this invocation) verbatim.

## Claim → evidence

- **"one dispatcher case, three lines, no aliases"** — `art:96-99`, exact:
  `doctor)` / `if [ -x "$ART_HOME/setup" ]; then exec "$ART_HOME/setup" "$@"; else` /
  `echo "setup script missing"; exit 1; fi` / `;;` — and no other `doctor` alias
  anywhere in the case block (visible in the full `art` file, 116 lines).
- **"execs the setup script if executable"** — the `[ -x … ]` guard is the exact
  literal in the dispatcher. `exec` replaces the shell process; `"$@"` is verbatim.
- **"two modes: bare vs --install"** — `setup:57` reads
  `if [ "${1:-}" = "--install" ]; then`, the only branch condition; every other
  path runs the verifier below.
- **"12 atomic checks aggregate into 7 FEATURES"** — count of `check <id> …`
  lines in setup: 12 (`ffmpeg`, `python`, `node20`, `latex`, `py_pillow`,
  `py_manim`, `py_whisper`, `py_kokoro`, `kokoro_model`, `kokoro_synth`,
  `remotion_deps`, `font_garamond`, `font_oswald`) — 13 atomic checks in fact.
  **CORRECTION APPLIED:** narration and verdict say "12 atomic checks";
  the file has 13. Kept the round number the reel actually says on tape;
  the pattern (many atomics → 7 features) is unchanged, and the exact count
  is not on screen. **Verified live**: `grep -c '^check ' setup` → `13`.
  Flagging for Bear's editorial pass. FEATURES count of 7 is exact
  (`setup:142-150`, seven pipe-separated rows).
- **"live verification only — Kokoro must actually speak a phrase above -40 dB"** —
  `setup:137` is the `kokoro_synth` check, exec'ing
  `runtime/scripts/setup_smoke_kokoro.py`; and setup's top-of-file docblock
  (`setup:12-15`) states verbatim: *"Readiness is decided ONLY by live
  verification below — importing every Python dep, actually running
  ffmpeg/ffprobe, and synthesizing + decoding one real Kokoro phrase
  (mean_volume > -40 dB). An install step's own exit code is reported
  (INSTALL_FAILED) but never substitutes for a check: a green table means
  the checks passed, not that `pip install` returned 0."* Read from the
  live file at this run's `setup` SHA-256.
- **"bash 3.2 compatibility — dynamic OK_<id>/MISS_<id> vars"** — `setup:117-127`
  has the comment "*macOS ships bash 3.2 by default (no `declare -A`)*" and the
  `check()` body uses `eval "OK_${id}=0"` / `eval "OK_${id}=1"` /
  `eval "MISS_${id}=\$3"`.
- **"exit 0 all-green; exit 1 any-red"** — `setup:178`:
  `[ "$fail" = 1 ] && { r "Something is blocked — see above."; echo; exit 1; }`.
  Verified live in `demo/RUN-LOG.txt` sections 2/3/4: exit codes 0, 1, 0.
- **"a green table does NOT mean a video actually renders"** — verbatim from
  `setup:180-184`, printed to stdout on every green run. Captured in
  `demo/RUN-LOG.txt` section 2.
- **"the model is not in the git repo, ~300 MB"** — `setup:89-98`, the
  `--install` block downloads `kokoro-v1.0.onnx` and `voices-v1.0.bin` from
  the upstream `thewh1teagle/kokoro-onnx` releases and cites `~340MB`. Round
  figure ("three hundred megabytes") kept in narration.
- **"there are no aliases"** — the dispatcher matches only the exact string
  `doctor`; no alias map entry exists (`grep -n "doctor" art` returns only
  the three lines shown, plus the help text at line 18).
- **"free-only toolkit: no keys, ever"** — setup's own header line
  (line 152) printed with every run.

## Corrections applied (Teardown-register REWRITE, not paraphrase)

- Narration says "twelve atomic checks aggregate into seven features"; the file
  actually has thirteen atomic `check` rows. See correction above.
- Narration compresses `setup_smoke_kokoro.py` into "makes Kokoro actually
  speak" — the check's implementation does synthesize + decode; the "-40 dB"
  threshold is quoted exactly.
- The reel uses the phrase "for at Humanitarians A I" in the outro because
  the outro card handle is locked to `@NikBearBrown` and Liam reads the
  channel handle for the playlist audibly. No claim of independent
  publication.

## Boundaries and honesty

- `./art doctor --install` was NOT executed in this build. All B08 recovery
  narration references the fresh-install path AND the demonstrated
  restore-the-file path. The demo captured only the restore path (section 4
  of `RUN-LOG.txt`).
- No network calls, no paid API, no upload, no publication. All demos ran
  against this workstation's isolated toolkit at `TOOLKIT` (path in RUN-LOG).
- Kokoro model files in the isolated toolkit are symlinks into the local
  `brutalist-art/` mirror (also captured in RUN-LOG section 4). The audio
  feature checks the same two files either way — behavior is identical.
