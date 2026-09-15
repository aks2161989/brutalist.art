# FACTCHECK — Brutalist Utility: capture_sim.py (Short)

This Short is a whole-beat cut of the vertical parent `claude-liam-brutalist-runtime-capture-sim-vertical`. Only the retained beats (B00, B01, B02, B07, B08, B09, B11) are checked here. Claims from the dropped long-form MECHANISM beats (B03/B04/B05/B06) and the YOUR TURN beat (B10) live in the parent reel's `FACTCHECK.md`; this Short does not repeat them and therefore does not need to re-check them.

Source under check: `runtime/scripts/capture_sim.py` — SHA-256 `ccb75479c75081bede9d63d0d4913075b3497db183a035b5e0648d5dcb5d4a34`, 662 lines. Confirmed unchanged since the parent build.

## B00 — ASK

| Claim | Evidence | Verdict |
|---|---|---|
| "Two clean mp4s in the default mode." | `capture()` writes `media/output.mp4` (line 162) and `media/change.mp4` (line 248). | ✅ |
| "No cursor, no audio track." | `webm_to_mp4()` passes `-an` (line 99). Playwright's `record_video_size` is a raw framebuffer, not a display capture, so no OS cursor is drawn. | ✅ |
| Composer folder chip reads `@HumanitariansAI` | `beat_sheet.json` B00 props `folderLabel: "@HumanitariansAI"`, matches the frame at `_qc/frames/first.png`. | ✅ |

## B01 — BLUF

| Claim | Evidence | Verdict |
|---|---|---|
| "capture_sim does NOT render." | The tool contains no drawing code. It boots headless Chromium (`pw.chromium.launch`, line 133) and records whatever the browser paints. | ✅ |
| Correction lands on "capture_sim RECORDS the browser." | Playwright's `record_video_dir` + `record_video_size` (lines 144-146) is the recording surface. Frame `_qc/frames/B01-85.png` confirms the hesitant-writer settled on the corrected text. | ✅ |

## B02 — FRAMEWORK

| Claim | Evidence | Verdict |
|---|---|---|
| "Local HTTP server on a free port." | `find_free_port()` line 67-70; `start_server()` line 73-86 spawns `HTTPServer` in a daemon thread. | ✅ |
| "`file://` blocks CDN requests." | Module docstring line 11-12. | ✅ |
| "Playwright launches headless Chromium; records webm the whole time." | Line 133 (`launch(headless=True)`); `record_video_dir` on every context. | ✅ |
| "ffmpeg remuxes webm to mp4 in `media/`." | `webm_to_mp4()` line 91-108 shells to ffmpeg (`libx264 preset=slow crf=18 pix_fmt=yuv420p -an`). | ✅ |
| "Two mp4s in default mode; one mp4 in click-through and script modes." | `capture()` opens two contexts; `capture_click_through()` and `capture_scripted()` each open one and write one mp4 named by `--out-name`. | ✅ |

## B07 — WORKED EXAMPLE

| Claim | Evidence | Verdict |
|---|---|---|
| Fixture has `input#k`, `range 1..6, step 0.1` | `demo/sim-source/00-tiny-wave.html:14` — `<input id="k" type="range" min="1" max="6" value="2" step="0.1">`. | ✅ |
| Script opens with `{"set":"#k","value":1}`, not `{"wait":...}`; then `wait 0.4`, `sweep #k from 1 to 6 in 30 steps @ 0.15 step_delay`, `set #k 3.5`, `wait 0.6` | `demo/scripts/tiny-wave-sweep.json` — quoted verbatim on the beat card. | ✅ verbatim |
| Rule "start with an interactive step, not a wait" is in the docstring | Module docstring lines 43-45: "Playwright only records from the first page-activity event. A script that starts with `{"wait": N}` will NOT capture that idle period. Always open with an interactive step (set/click/check) to anchor the recording at t=0." | ✅ verbatim |

## B08 — OBSERVED FAILURE (Apple App Sandbox)

| Claim | Evidence | Verdict |
|---|---|---|
| Chromium exits with a FATAL Mach-port bootstrap denial | `demo/failure-sandbox.txt` — `[FATAL:base/apple/mach_port_rendezvous_mac.cc:159] Check failed: kr == KERN_SUCCESS. bootstrap_check_in org.chromium.Chromium.MachPortRendezvousServer.58727: Permission denied (1100)`. Quoted verbatim on the beat card. | ✅ observed |
| `capture_sim.py`'s except-block prints `[capture_sim] FAILED: …` and exits 1 | Lines 656-658 (`except Exception as e: … sys.exit(1)`). First log line is exactly `[capture_sim] FAILED: BrowserType.launch: …`. | ✅ |
| No zero-byte mp4 is written on failure | `finally` block (line 254-256) shuts down the server and `rmtrees(tmp_dir)`; the `media/` folder for this run has no `output.mp4`/`change.mp4`. | ✅ |
| Root cause is the sandbox, not the tool | Sandbox denial is imposed by macOS on the Chromium spawn boundary; the same command outside Claude Code's sandbox (normal terminal or CI) is the ordinary happy path. The tool does not currently honor `ART_CHROME`; that fix is out of scope for this episode. | ✅ |

## B09 — VERDICT

Each of the six lines corresponds directly to code the reel just discussed:

1. "serve — SimpleHTTPRequestHandler on a random free port; D3 v7 CDN needs http://, not file://" — lines 67-86 + docstring lines 11-12.
2. "launch — Playwright's sync API spawns headless Chromium (chrome-headless-shell); one or two contexts per run." — line 133; contexts created inside `capture()` / `capture_click_through()` / `capture_scripted()`.
3. "drive — default sweeps `input[type=range]`; `--click-through` walks DOM order; `--script` runs a 7-verb DSL." — `capture()` sweep (line ~186-214), `capture_click_through()` (line ~312-346), `capture_scripted()` verb dispatch (line ~423-545).
4. "record — Playwright writes webm the whole time; page.close() flushes it to disk." — Playwright records into `tmp_dir/*` (lines 144, 171); close+context.close flush the webm.
5. "remux — ffmpeg → libx264 preset=slow crf=18 pix_fmt=yuv420p -an in media/<name>.mp4." — `webm_to_mp4()` line 91-108.
6. "assert — every interactive selector is checked; a silent miss is a failure." — `capture_click_through()` count>=2 guard (line 312-317) and `capture_scripted()`'s `assert_sel()` (line 411-420).

## B11 — OUTRO

- Title restated verbatim: "Brutalist Utility: capture_sim.py."
- Sign-off: "Liam, in for Bear, for @HumanitariansAI."
- Card component is the locked `ClaudeTitleOutro916` with hardcoded `@NikBearBrown` handle per `OUTRO-LOCK.md` — same as the vertical parent. Flagged in `README.md` for the human reviewer before publication.

## Documented gaps and honest labels

- **No captured mp4** from the actual `capture()` browser path is included in this reel. B08 shows the observed sandbox failure honestly; the reel does not claim Chromium ran successfully in this session.
- The example beat sheets under `.repoloop/shorts/workspaces/.../examples/` (`rohan-v/…`, `sanjana-rao/…`) informed shot shapes only. None of their captured media, narration, or approvals is reused here.
- Legacy `scripts/type_check.py` and `reference/type-spec.md` referenced by public docs are not present in the toolkit — see `TYPECHECK.md`. Visual typography is reviewed by frame inspection instead.
- Dropped-beat claims (B03 CLI surface, B04-B06 code walks, B10 Your Turn assignment) are checked in the parent reel's `FACTCHECK.md`, not here.
