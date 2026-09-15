# SCRIPT — Brutalist Utility: build_cli_d3_reels.py

Narration verbatim from `beat_sheet.json`. Kokoro `am_onyx` (Liam, in for Bear).
Total ~234.79 s across 12 beats.

## B00 — Cold open (13.63s)

Bula, this is Liam, in for Bear. The ask — I've got a folder of D3 simulations already built, one HTML each, and I want a Claude-skin explainer reel for every one of them. Overnight. Unattended. Not a fresh generation. A batch WRAP.

## B01 — BLUF hesitant writer (11.16s)

Watch the writer walk this back. Build cli d3 reels does not generate the sim. The D3 sim is already built. This tool WRAPS it — the reel around it — from one HTML file per sim.

## B02 — Framework: pipeline (20.05s)

The pipeline. One config.json in. For each sim: stamp the beat sheet with the fixed ten-beat Claude template. Capture the sim's baseline and change mp4s. Generate Kokoro audio. Render the Claude Remotion beats. Run compile.py review. Append one row to CLI EXPLAINERS OVERNIGHT LOG dot md. One config in, N review cuts out, one line each in the log.

## B03 — Mechanism 1: CLI + schema (18.09s)

The command surface is small. One required positional: the config JSON path. One optional flag — dash dash log — that overrides the default overnight log file. The config schema is a JSON with one key, sims, an array of rows. Each row carries slug, book, html, note, and an optional title.

## B04 — Mechanism 2: make_beat_sheet (23.25s)

The stamp. Make beat sheet writes the same ten-beat spine for every sim. Cold open ClaudeComposerAsk at B00. ClaudeCodeBeat at B03 — that's the actual code law. Video beats at B04 and B06 — the captured baseline and the captured change. Your turn composer at B08. ClaudeTitleOutro at B09. Metadata locks palette to claude, voice to Kokoro am onyx, register to Teardown.

## B05 — Mechanism 3: extract_code (20.01s)

Extract code. The actual code law. Regex over inline script tags without a source attribute — that filters out the d3 CDN import. Take the LONGEST block. That is the sim's real physics, not the boilerplate. Keep the first twenty meaningful lines. Trim any line longer than seventy-eight characters. Wrap the whole thing with a header comment naming the file, and a footer pointer to the full source.

## B06 — Mechanism 4: build_one (28.27s)

Build one. The per sim orchestrator. Line three fifteen — if the slate mp4 is already there and over fifty kilobytes, print SKIP, append SKIP to the log, return. Otherwise: shell out to capture_sim to make output and change mp4s. Copy them to B04 and B06. Shell out to generate audio kokoro with the no gate flag. Shell out to remotion scenes for the Claude beats. Shell out to compile.py review, then to compile.py master. Every subprocess call is time boxed with a timeout in seconds.

## B07 — Worked example (21.95s)

Worked example. Disposable fixture — one sim in the config, one HTML on disk. Run the module — greeting for the slug hashes to Yo. Make title extracts the physics concept from the note. Extract code pulls the sim's inline JS. The stamped beat sheet is ten beats: B00 through B09. That is exactly what the tool writes into every reel folder — no matter how many sims are in the batch.

## B08 — Mechanism 5: soft/hard fail (22.08s)

When things go wrong. Two failure modes. One — remotion scenes fails. The tool prints a warning to standard error and keeps going. Compile.py then slates every un rendered beat and the reel still ships as a watchable review cut. Two — anything else fails: capture, audio, compile itself. The exception is caught, the log gets a FAILED row with the message, and the loop keeps going to the next sim. Never let one bad sim take down the whole batch.

## B09 — Verdict (23.30s)

So — build cli d3 reels dot py. The batch wrapper. One config in, N Claude skin review cuts out, one log row each. The template is fixed — ten beats, three laws, one greeting per slug. The remote dependencies are the tools it shells out to: capture sim, kokoro, remotion, compile. Every subprocess call is time boxed. Every sim can SKIP, BUILT, or FAILED. The overnight run finishes with a counts dictionary and a log file you can grep.

## B10 — Your Turn (26.01s)

Your turn. Paste this into Claude Code, pointed at any folder of your own D3 sims already saved as one file HTMLs. Ask Claude to write a config.json for build cli d3 reels — with one row per sim, correct slugs, books, notes — then dry run the tool. Watch whether Claude is tempted to invent notes it did not observe. That is the trap the note field exists to catch — the note becomes the beat two problem line and the title, so a fabricated note becomes a fabricated reel.

## B11 — Outro (6.74s)

Brutalist Utility: build cli d3 reels dot py. Liam, in for Bear, for at Humanitarians A I.
