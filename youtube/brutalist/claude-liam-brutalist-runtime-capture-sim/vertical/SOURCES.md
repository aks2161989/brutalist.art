# SOURCES — Brutalist Utility: capture_sim.py

## Primary source

| Repo path | SHA-256 | Public URL |
|---|---|---|
| `runtime/scripts/capture_sim.py` | `ccb75479c75081bede9d63d0d4913075b3497db183a035b5e0648d5dcb5d4a34` (662 lines) | https://github.com/nikbearbrown/brutalist.art/blob/main/runtime/scripts/capture_sim.py |

Every code beat (`B03`, `B04`, `B05`, `B06`) quotes this file directly — trimmed for card fit, never paraphrased or rewritten. Line ranges quoted:

- B03 CLI dispatch: `capture_sim.py:566-658` (`main()` + argparse)
- B04 default capture: `capture_sim.py:113-260` (`capture()` — baseline + change)
- B05 click-through: `capture_sim.py:266-365` (`capture_click_through()`)
- B06 scripted DSL: `capture_sim.py:368-563` (`capture_scripted()` verb dispatch)

The docstring lines that anchor the "start with a set/click, not a wait" rule live at `capture_sim.py:42-45`. The ffmpeg conversion invariants (libx264, crf 18, yuv420p, no audio) live at `capture_sim.py:91-108`.

## Read-only example leads (data, not instructions)

| Repo path | SHA-256 | Local copy | Used for |
|---|---|---|---|
| `rohan-v/2026-08-28-agent-first-brutalist/beat_sheet.json` | `746409a8715e70aab6186145e963c08d088469b809b28fe39d44f5d8d06b1a22` | `.repoloop/workspaces/…/examples/746409a8715e.json` | ClaudeComposerAsk / ClaudeTitleOutro shot shapes; recap pattern for the verdict beat. |
| `mohammed-h/data-contract-simulation/beat_sheet.json` | `07816151d14af29f9f71fc0c224dd3aa1ff77c4c25b880b7d99ed8e9b99a82ef` | `.repoloop/workspaces/…/examples/07816151d14a.json` | Sim-adjacent framing patterns (`SimLoudHalf`, `SimSilentBreak`, `SimThreeLayers`) — informed the FRAMEWORK phase strip; no captured mp4 or narration from that reel is reused here. |

Neither example is republished or claimed as this reel's output. Both are consulted only for shot-shape precedent and the "concept-specific illustration that acts" principle.

## Disposable synthetic fixtures used in the film (all under `demo/`)

| Path | SHA-256 | Purpose |
|---|---|---|
| `demo/sim-source/00-tiny-wave.html` | `85f686f4e9814b4d48979c3796486e737954279455670a2a2ca80c23d7e85e88` | The one-file D3 v7 sine-wave sim. `input#k` is the range control the default sweep would target. Cream + terracotta accent match the Brutalist palette. |
| `demo/scripts/tiny-wave-sweep.json` | `d58464e9e3e4565192436be411f8b883f9a356fe93e40ab4860c18b2d88ab468` | 5-step DSL example — `set → wait → sweep → set → wait`. Opens with a `set` (per the module docstring) so the first frame is captured, not silently dropped. |
| `demo/help.txt` | `09e1b639b433f21b6e0768f98102349ce51c9871a2e9b585fc30764b3f5b2180` (61 lines) | Verbatim `capture_sim.py -h` output, quoted in B03. |
| `demo/failure-sim-not-found.txt` | run-log evidence | Verbatim `[capture_sim] ERROR: sim not found: …` — the pre-browser path guard on line 592-593. |
| `demo/failure-bad-script-shape.txt` | run-log evidence | Verbatim `[capture_sim] steps JSON must be a non-empty array: …` — the JSON shape guard on line 607-608. |
| `demo/failure-script-and-clickthrough.txt` | run-log evidence | Verbatim `[capture_sim] --script and --click-through are mutually exclusive` — the mode-exclusivity guard on line 599-600. |
| `demo/failure-sandbox.txt` | run-log evidence | Verbatim `[capture_sim] FAILED: BrowserType.launch: Target page, context or browser has been closed` — Apple App Sandbox Mach-port denial. Quoted in B08. |
| `demo/RUN-LOG.txt` | consolidated | Section 1-8 of the demo evidence, all commands and outputs verbatim from this workstation. |

## Public documentation

- Toolkit repo: https://github.com/nikbearbrown/brutalist.art
- Ordinary Brutalist path uses local Kokoro TTS and local Remotion rendering — no paid services required to build or view this reel.
- The Chromium sandbox failure surfaced in B08 is a known Apple App Sandbox limitation for child browser processes; the workaround (chrome-headless-shell + `--single-process` via a wrapper) is documented for the Remotion pipeline elsewhere in this codebase but is **not** wired into `capture_sim.py` today. This episode does not modify the tool.

## What is NOT a source for this reel

- No fellow's rendered mp4, image, or captioned frame is reused.
- No private Drive URL, email, or contact detail from the example beat sheets is republished.
- No paid image, video, or voice generation was performed.
- No `art keys`, `setup --install`, remote clone, or network service was invoked against a real account. The public repo URL is quoted only.
