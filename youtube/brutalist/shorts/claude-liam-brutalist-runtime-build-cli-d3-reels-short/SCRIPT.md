# SCRIPT — Brutalist Utility: build_cli_d3_reels.py — Short

Whole-beat cut of the 12-beat 9:16 parent (234.8s → 96.96s). Retained narration
is copied verbatim from the parent — the six kept beats already stand alone.

| # | Beat | Kokoro am_onyx narration (verbatim from parent) |
|---|---|---|
| 1 | B00 ASK | Bula, this is Liam, in for Bear. The ask — I've got a folder of D3 simulations already built, one HTML each, and I want a Claude-skin explainer reel for every one of them. Overnight. Unattended. Not a fresh generation. A batch WRAP. |
| 2 | B01 BLUF | Watch the writer walk this back. Build cli d3 reels does not generate the sim. The D3 sim is already built. This tool WRAPS it — the reel around it — from one HTML file per sim. |
| 3 | B02 FRAMEWORK | The pipeline. One config.json in. For each sim: stamp the beat sheet with the fixed ten-beat Claude template. Capture the sim's baseline and change mp4s. Generate Kokoro audio. Render the Claude Remotion beats. Run compile.py review. Append one row to CLI EXPLAINERS OVERNIGHT LOG dot md. One config in, N review cuts out, one line each in the log. |
| 4 | B07 WORKED EXAMPLE | Worked example. Disposable fixture — one sim in the config, one HTML on disk. Run the module — greeting for the slug hashes to Yo. Make title extracts the physics concept from the note. Extract code pulls the sim's inline JS. The stamped beat sheet is ten beats: B00 through B09. That is exactly what the tool writes into every reel folder — no matter how many sims are in the batch. |
| 5 | B09 VERDICT | So — build cli d3 reels dot py. The batch wrapper. One config in, N Claude skin review cuts out, one log row each. The template is fixed — ten beats, three laws, one greeting per slug. The remote dependencies are the tools it shells out to: capture sim, kokoro, remotion, compile. Every subprocess call is time boxed. Every sim can SKIP, BUILT, or FAILED. The overnight run finishes with a counts dictionary and a log file you can grep. |
| 6 | B11 OUTRO | Brutalist Utility: build cli d3 reels dot py. Liam, in for Bear, for at Humanitarians A I. |

## Dropped from the parent (belong in the 16:9 long)

- B03 CLI + config schema code walkthrough
- B04 make_beat_sheet() 10-beat template dict
- B05 extract_code() regex + longest-block + trim walkthrough
- B06 build_one() orchestrator + SKIP guard code
- B08 soft-fail / hard-fail failure-mode teardown + observed log
- B10 extended Your-Turn composer with paste-ready prompt

## Sign-off

- Voice: Kokoro `am_onyx` (Liam, in for Bear). No ElevenLabs. No captions burned in.
- No new narration written; no audio regenerated; parent MP3s copied unchanged.
- Outro handle `@NikBearBrown` unchanged; composer folder chip reads `@HumanitariansAI` on the retained composer beats.
