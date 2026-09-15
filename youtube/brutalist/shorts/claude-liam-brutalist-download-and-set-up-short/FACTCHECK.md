# FACTCHECK — Download Brutalist with Claude Code — Short

Every load-bearing claim in the six retained beats of the Short, with its source in the isolated toolkit snapshot (`SOURCE-SNAPSHOT.json`, revision `ba2d0e0`). Claims that only appeared in dropped parent beats (B01/B02/B03/B08) are omitted — the Short does not make them.

| # | Claim (narration) | Beat | Evidence |
|---|-------------------|------|----------|
| 1 | "Brutalist is a git clone plus a free doctor script." | B00 | `README.md` §1 ("The pared-down Brutalist video toolkit"), `setup` — free-by-default dependency doctor. |
| 2 | The public toolkit lives at `https://github.com/nikbearbrown/brutalist.art`. | B00 | Repository URL supplied in the invocation spec and used throughout `CLAUDE.md`. |
| 3 | The doctor runs `./setup --install` once (deps + Kokoro voice model), then `./setup` any time. | B00, B04 | `setup` lines 58–99 (install branch) and 128–174 (readiness table). |
| 4 | The readiness table reports seven features (audio, captions, Manim, Manim eq, Remotion, slates, fonts). | B04 | `setup` lines 142–150 (FEATURES array). The rendered scene mirrors these seven rows. |
| 5 | "Green means the feature is live" and "Red means one dependency is missing." | B04 | `setup` lines 152–172 (`✅ ready` / `❌ blocked`). |
| 6 | Doctor readings on screen match the local run. | B04 | `demo/setup-output.txt` — every feature reports `✅ ready` on this machine. |
| 7 | The Claude Code subscription is what runs the agent; a paid Anthropic API is a different, optional lane. | B05 | Anthropic public documentation distinguishes Claude Code (subscription) from the Anthropic API (metered per-token). Brutalist itself never spends: `CLAUDE.md` §5 ("Never publish — render instead") and `README.md` line 8 ("Free by default"). |
| 8 | "Kokoro is a local voice model." | B05, B06 | `runtime/scripts/generate_audio_kokoro.py` lines 6–14 ("Kokoro is FREE — a local 82M-parameter Apache-2.0 model…"). |
| 9 | Setup "does download one thing — the Kokoro voice model, about three hundred forty megabytes, straight from a GitHub release." | B06 | `setup` lines 89–99 (`Downloading the Kokoro voice model (~340MB, one-time, free — not in the git repo)` from `github.com/thewh1teagle/kokoro-onnx/releases`). `README.md` line 51 ("`./setup --install` fetches it once from the kokoro-onnx releases"). |
| 10 | "Setup does not sign you into anything — no accounts are created" and "does not upload." | B06 | `setup` (whole file) — no credential prompt, no `curl -X POST`, no auth flow; the only network calls are `curl -fLO` to two GitHub release URLs (Kokoro model files) and an optional Oswald font from Google Fonts (line 76). |
| 11 | Outro title restates the film title with the `@HumanitariansAI` handle. | B09 | Rendered mp4 frame shows "Download Brutalist with Claude Code." title, `@HumanitariansAI` handle, "LIAM, IN FOR BEAR." subline. |

## Rewrites and simplifications (DOUBLE-CHECK LAW)

- **Doctor rows.** The dark-terminal table in B04 shows seven feature rows verbatim from `setup` FEATURES (lines 142–150). The dependency column is compressed to what fits legibly rather than the full IDs the shell script uses; the rows still map 1:1 to the script.
- **Download size.** "~340MB" is used in narration; the setup script says the same on line 90.
- **Register.** Narration is Teardown-warm: mechanism first (what the pipeline actually does), then judgment (free by default, honest boundaries). Verdict lands as three clean lines.

## Known gaps

- The `./setup --install` step is source-labelled ("It is the same script the sandbox in this reel just executed") — the sandbox in this run only ran `./setup` (the doctor), NOT `./setup --install` (that would have re-fetched fonts / re-installed npm deps). Kokoro model already exists on this machine. Narration is accurate: "the readings on screen are real" refers to the doctor readings.
- No live network clone was performed. The B03 file-tree beat that showed the clone contents is cut from the Short — the Short does not make any per-folder claim.

## Claims from parent that are NOT made in this Short

- Filesystem anatomy (`setup`, `art`, `README.md`, `skills/`, `runtime/`, `docs/`, `brands/`, "the fifteen builder recipes") — that was parent B03; the Short does not reference the directory tree.
- The paste-ready handoff prompt and its expected-outcome bullets — that was parent B08; not present in the Short.
- The "downloading Brutalist means running an installer" misconception frame — that was parent B01 (HesitantWriter); the Short states the reframe in B00 without setting up the misconception first.
