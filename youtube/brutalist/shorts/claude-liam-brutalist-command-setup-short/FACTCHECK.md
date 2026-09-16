# FACTCHECK.md — Brutalist Command: setup

Every screen claim is traced to a specific line in the source. Verbatim outputs live in `demo/RUN-LOG.txt`.

## B00 — cold-open ask (composer output lines)

- "prints a 7-row FEATURE table — green when every atomic check passes live" — `setup:142-172`; `FEATURES=(...)` is seven entries.
- "installs pip deps + Remotion npm + fonts + Kokoro model, then verifies (only under `--install`)" — `setup:57-100`.
- "exits 0 iff all rows green; exits 1 the moment one is red" — `setup:178`.

## B01 — BLUF (hesitant writer)

Misconception typed first, then corrected:
- typed: "setup installs everything." — plausible reading of the flag list.
- typed after correction: "setup verifies live." — grounded at `setup:20-25` ("Readiness is decided ONLY by live verification below…").
- narration extends the on-screen line out loud with the `--install` caveat, grounded at `setup:57-100`.

Word-level triggers (`installs`→`verifies`, `everything`→`live`) match token-by-token; the component splits on `\s+` (`BrutalistHesitantWriter.tsx:118`), so single tokens are the pattern the component supports. Neither trigger appears in the preserved prefix `setup`, so the FIRST-occurrence collision rule doesn't corrupt the sentence.

## B02 — the setup surface (verbatim shebang + short-help)

Screen code is the byte-for-byte contents of `setup:1-16` and the `set -uo pipefail` line at `setup:16`. See `demo/RUN-LOG.txt` §1.

## B03 — requirements.txt (the pip contract)

Screen code is verbatim `requirements.txt`. Every pin cited:
- `kokoro-onnx>=0.4` — the free voice engine. Requires `numpy>=2.0.2` (its own release pin — this is the reason the file states "numpy>=2.0.2 is required by kokoro-onnx"; see the file's own comment).
- `mutagen>=1.47,<1.48` — MP3 duration measurement (the master clock).
- `Pillow>=10.2,<11` — slates / request cards / previz / stills.
- `numpy>=2.0.2` — pinned above; no upper bound from Manim (Manim `<0.19` has no upper).
- `manim>=0.18,<0.19` + `manimpango>=0.5,<0.6` — animation dependencies.
- `faster-whisper>=1.0,<2` — forced alignment + captions (unused in this reel; captions are off).

The comment at the top of `requirements.txt` is the source-of-truth on why the numpy floor is where it is; the reel quotes it in plain speech, no numbers invented.

## B04 — the all-green table (verbatim)

Every character comes from `demo/RUN-LOG.txt` §2. Cost line `Cost: $0.00.` is from `setup:179`; exit code `0` is `setup:180-184` (the trailing `g "All core features ready…"` after the `[ "$fail" = 1 ]` gate).

## B05 — --install pipeline (four phases)

The `--install` block runs four phases (`setup:57-100`), in order:
1. Python deps (`pip install -r requirements.txt`) — `setup:58-64`.
2. Remotion node deps (`(cd runtime/remotion && npm install)`) — `setup:66-70`.
3. Fonts — bundled family install + Oswald from Google Fonts if not present — `setup:73-85`. `fc-cache -f` if available — `setup:86`.
4. Kokoro model download (only if the two files are missing) — `setup:89-98`. The URL cited on screen matches `setup:93-94`.

The narration's phrase "install step's own exit code is reported but never substitutes for a check" comes from `setup:14-15` and `setup:174-177` (the `INSTALL_FAILED=1` flag that only widens the fail path, never turns a row green).

## B06 — check() + bash 3.2 (dynamic OK_/MISS_ vars)

Code block is a compressed, verbatim quote of `setup:117-127` with two representative checks from `setup:128, 137`. The comment "macOS ships bash 3.2 by default (no declare -A)" comes verbatim from `setup:117-118`. No wording invented.

## B07 — live verification (kokoro_synth)

Screen quotes:
- The `check kokoro_synth` line: `setup:137`.
- The `setup_smoke_kokoro.py` behaviour: `runtime/scripts/setup_smoke_kokoro.py:1-72` — synthesizes `"This is a setup smoke test."` with `af_bella`, decodes via `ffmpeg -af volumedetect`, asserts `mean_volume > -40 dB` (constant `THRESHOLD_DB = -40.0`).
- The rationale quote: `setup:12-15` — kept short so nothing dates.

Nothing on this beat depends on a specific version number.

## B08 — the ElevenLabs guard (setup:102-115)

Screen shows a redacted-safe version of the guard: the `EL_PAT` variable, the `grep -rqiE` sweep, the failure message, and the file-listing branch. The narration explains the pattern intent (functional references only — the pattern is deliberately split by string concatenation so that this guard itself does not match). The file name `setup` is excluded from the sweep for that same reason (`setup:108`).

## B09 — one-file failure and recovery

Verbatim from `demo/RUN-LOG.txt` §3 and §4. On this workstation, "hide the model file" was implemented by unlinking the workspace `runtime/models` symlink; the effect (the two hint lines under a single red row, the identical fix hints) is the same as physically renaming the `.onnx` file, because both check paths (`kokoro_model` at `setup:136`, `kokoro_synth` at `setup:137`) resolve against the same directory.

## B10 — verdict artifact (six lines)

Every artifact line is a compression of one already-cited fact:
1. Two-mode surface → `setup:1-16` and this file, B02.
2. `--install` pipeline → `setup:57-100`, this file, B05.
3. Live verification is the only judge → `setup:12-15`, this file, B01/B07.
4. Thirteen atomic checks aggregate into seven features → `setup:128-140` (13 `check …` calls) → `setup:142-150` (7-row `FEATURES=(...)`).
5. Bash 3.2-safe via `OK_<id>`/`MISS_<id>` → `setup:117-127`, this file, B06.
6. Exit-code discipline → `setup:178-184`.

## B11 — Your Turn prompt

The prompt asks the viewer to run `./setup`, save stdout+stderr, and — without installing — map each red row to its atomic check ID and its fix hint. No claims about the outcome; the reader supplies the results. Deliberately mirrors the doctor episode's prompt shape (verify without remediating) but focuses on `./setup` directly and calls out the ElevenLabs guard as a second thing to look for in the output.

## B12 — outro

Title restate: "Brutalist Command: setup." — matches `metadata.title` exactly. Handle: `@NikBearBrown` per OUTRO-LOCK.md (hardcoded), flagged in README.md so the human reviewer can decide whether to substitute a HAI-branded outro before publication.
