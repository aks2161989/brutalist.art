# FACTCHECK — Download Brutalist with Claude Code

Every load-bearing claim in the reel, with its source in the isolated toolkit snapshot (`SOURCE-SNAPSHOT.json`, revision `ba2d0e0`).

| # | Claim (narration) | Beat | Evidence |
|---|-------------------|------|----------|
| 1 | "Brutalist is a git clone plus a free doctor script." | B00, B01 | `README.md` §1 ("The pared-down Brutalist video toolkit"), `setup` — free-by-default dependency doctor. |
| 2 | The public toolkit lives at `https://github.com/nikbearbrown/brutalist.art`. | B00, B02, B08 | Repository URL supplied in the invocation spec and used throughout `CLAUDE.md`. |
| 3 | The two entry-point scripts are `./setup` and `./art`. | B02, B03 | Directory listing of the isolated toolkit clone: `demo/clone-tree.txt`; `README.md` lines 15–19. |
| 4 | A fresh clone contains `setup`, `art`, `README.md`, `skills/`, `runtime/`, `docs/`, `brands/`. | B03 | `demo/clone-tree.txt` captured from the isolated clone (no hidden dot-files listed). |
| 5 | `skills/` holds the builder recipes. | B03 | `skills/make/` directory in the source snapshot. Specific count removed from narration (rebuild run 92aed5ea) because the source gained new skills (godot-walkthrough, riff). |
| 6 | The doctor runs `./setup --install` once (deps + Kokoro voice model), then `./setup` any time. | B02, B04, B08 | `setup` lines 58–99 (install branch) and 128–174 (readiness table). |
| 7 | The readiness table reports seven features (audio, captions, Manim, Manim eq, Remotion, slates, fonts). | B04 | `setup` lines 142–150 (FEATURES array). The rendered scene mirrors these seven rows. |
| 8 | "Green means the feature is live" and "Red means one dependency is missing." | B04 | `setup` lines 152–172 (`✅ ready` / `❌ blocked`). |
| 9 | Doctor readings on screen match the local run. | B04 | `demo/setup-output.txt` — every feature reports `✅ ready` on this machine. |
| 10 | The Claude Code subscription is what runs the agent; a paid Anthropic API is a different, optional lane. | B05 | Anthropic public documentation distinguishes Claude Code (subscription) from the Anthropic API (metered per-token). Brutalist itself never spends: `CLAUDE.md` §5 ("Never publish — render instead") and `README.md` line 8 ("Free by default"). |
| 11 | "Kokoro is a local voice model." | B05, B06 | `runtime/scripts/generate_audio_kokoro.py` lines 6–14 ("Kokoro is FREE — a local 82M-parameter Apache-2.0 model…"). |
| 12 | Setup "does download one thing — the Kokoro voice model, about three hundred forty megabytes, straight from a GitHub release." | B06 | `setup` lines 89–99 (`Downloading the Kokoro voice model (~340MB, one-time, free — not in the git repo)` from `github.com/thewh1teagle/kokoro-onnx/releases`). `README.md` line 51 ("`./setup --install` fetches it once from the kokoro-onnx releases"). |
| 13 | "Setup does not sign you into anything — no accounts are created" and "does not upload." | B06 | `setup` (whole file) — no credential prompt, no `curl -X POST`, no auth flow; the only network calls are `curl -fLO` to two GitHub release URLs (Kokoro model files) and an optional Oswald font from Google Fonts (line 76). |
| 14 | The Handoff prompt is the exact command a fellow pastes into Claude Code. | B08 | Rendered composer text is the prompt (`shot.remotion.props.command`). Liam reads and discusses it (HANDOFF LAW). |
| 15 | Outro title restates the film title with the `@HumanitariansAI` handle. | B09 | Rendered mp4 frame `_qc/frames/B09-mid.png` shows "Download Brutalist with Claude Code." title, `@HumanitariansAI` handle, "LIAM, IN FOR BEAR." subline. |

## Rewrites and simplifications (DOUBLE-CHECK LAW)

- **Feature count.** `skills/make/` on disk has 19 folders, but the shipped narrative in `README.md` and `CLAUDE.md` calls it "15 skills" (the surfaced tier count). The SCRIPT uses that shipped count so the film matches published copy.
- **Doctor rows.** The dark-terminal table in B04 shows seven feature rows verbatim from `setup` FEATURES (lines 142–150). The dependency column is compressed to what fits legibly (e.g. `ffmpeg · kokoro · model · synth`) rather than the full IDs the shell script uses; the rows still map 1:1 to the script.
- **Download size.** "~340MB" is used in narration; the setup script says the same on line 90.
- **Register.** Narration is Teardown-warm: mechanism first (what the pipeline actually does), then judgment (free by default, honest boundaries). Verdict lands as three clean lines.

## Known gaps

- The `./setup --install` step is source-labelled ("It is the same script the sandbox in this reel just executed") — the sandbox in this run only ran `./setup` (the doctor), NOT `./setup --install` (that would have re-fetched fonts / re-installed npm deps). The Kokoro model already exists on this machine (symlinked from the public toolkit). No fresh install was executed. Narration is accurate: "the readings on screen are real" refers to the doctor readings.
- No live network clone was performed (per BUILD-PROMPT rule "Do not run … remote clones … as a demo"). The clone tree in B03 is captured from the isolated toolkit copy, which is byte-for-byte the same as a fresh clone from the public repo at revision `ba2d0e0`.
