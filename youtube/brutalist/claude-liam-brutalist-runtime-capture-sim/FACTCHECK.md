# FACTCHECK — Brutalist Utility: capture_sim.py

Every non-obvious claim in `SCRIPT.md` is checked against `runtime/scripts/capture_sim.py` and against the demo run-log below.

Source under check: `runtime/scripts/capture_sim.py` — SHA-256 `ccb75479c75081bede9d63d0d4913075b3497db183a035b5e0648d5dcb5d4a34`, 662 lines.

## B00 — ASK

| Claim | Evidence | Verdict |
|---|---|---|
| "two clean mp4s" in default mode | `capture()` writes `media/output.mp4` (line 162) and `media/change.mp4` (line 248). | ✅ verbatim |
| "no cursor, no audio track" | `webm_to_mp4()` passes `-an` (line 99). No mouse-cursor rendering — Playwright's `record_video_size` is a raw framebuffer, not a display capture. | ✅ |

## B01 — BLUF

| Claim | Evidence | Verdict |
|---|---|---|
| "capture_sim does NOT render" | The tool contains no drawing code. It boots a real headless Chromium (`pw.chromium.launch`, line 133) and records the browser. All D3 rendering happens inside Chromium. | ✅ |
| Correction lands on "capture_sim RECORDS the browser." | Playwright's `record_video_dir` + `record_video_size` (lines 144-146) is what captures. Nothing else in the file draws. | ✅ |

## B02 — FRAMEWORK

| Claim | Evidence | Verdict |
|---|---|---|
| "Local HTTP server on a free port" | `find_free_port()` line 67-70; `start_server()` line 73-86 spawns `HTTPServer` in a daemon thread. | ✅ |
| "file:// blocks CDN requests" | Module docstring line 11-12: "Serves the file via a local HTTP server so CDN requests (D3 v7) are not blocked by Chromium's cross-origin restrictions on file:// URLs." | ✅ |
| "Playwright records webm; ffmpeg remuxes to mp4" | Playwright writes `.webm` into `tmp_dir` (lines 144, 171); `webm_to_mp4()` line 91-108 shells to ffmpeg (`libx264 preset=slow crf=18 pix_fmt=yuv420p -an`). | ✅ |

## B03 — MECHANISM 1 (CLI surface)

| Claim | Evidence | Verdict |
|---|---|---|
| Two required positionals: `sim_html`, `reel_dir` | Lines 568-569 (`ap.add_argument("sim_html", …)`, `ap.add_argument("reel_dir", …)`). | ✅ |
| Default mode = baseline + change | `capture(...)` when neither `--click-through` nor `--script` is passed (line 645-654). | ✅ |
| `--script` and `--click-through` are mutually exclusive | `sys.exit(... "mutually exclusive")` at line 599-600. Reproduced verbatim in `demo/failure-script-and-clickthrough.txt`. | ✅ |
| Verbatim `--help` output shown | `demo/help.txt` — 61 lines captured from `python3 runtime/scripts/capture_sim.py -h`. | ✅ |

## B04 — MECHANISM 2 (`capture()`)

| Claim | Evidence | Verdict |
|---|---|---|
| Two contexts, back-to-back — baseline then change | `ctx_out` created line 141, closed line 155; `ctx_chg` created line 168, closed line 243. | ✅ |
| Waits `networkidle`, then sleeps 1.5s for D3 settle | Lines 149-151 and 176-177. | ✅ |
| Sweep is 40 steps over `change_dur` seconds | `steps = 40; delay = change_dur / steps` — line 198-199. | ✅ |
| Reads element's `min`/`max` off the DOM | `page_chg.evaluate("""sel => {const el = document.querySelector(sel); ...")` — line 186-194. | ✅ |
| Fires `input` and `change` events on each step | Two `dispatchEvent(new Event(...))` calls per step — line 208-209. | ✅ |
| Holds 1.0s at max | `time.sleep(1.0)` line 214. | ✅ |
| Hard error if selector is not a range input | Line 232-236 raises `RuntimeError` listing candidate controls. | ✅ |

## B05 — MECHANISM 3 (`capture_click_through()`)

| Claim | Evidence | Verdict |
|---|---|---|
| Guard: fail if count < 2 | Line 312-317 raises with message "matched N element(s); need ≥ 2". | ✅ |
| Re-queries element on every iteration | `document.querySelectorAll(sel)[idx]` re-executed inside the loop (line 325-329). | ✅ |
| Holds `hold_each` seconds between clicks | `settle_deadline` + `remaining` — lines 333-346. | ✅ |
| One mp4 output at `media/<out_name>.mp4` | Line 359. Default `out_name = "change-clickthrough"` when the flag is set (line 627). | ✅ |

## B06 — MECHANISM 4 (`capture_scripted()`)

| Claim | Evidence | Verdict |
|---|---|---|
| Seven verbs: set / click / check / uncheck / sweep / scroll / wait | Verb dispatch begins line 423; each verb handled in its own `elif` block. Unknown verb raises with "Supported: set / click / check / uncheck / sweep / scroll / wait" (line 545). | ✅ |
| `click` accepts fractional `at:[fx,fy]` via `elementFromPoint` | Lines 439-455. The elementFromPoint dispatch is required because events bubble UP; the container's listener wouldn't fire on a child rect. | ✅ |
| `sweep` reads element `min`/`max` or explicit `from`/`to` | Lines 493-508. | ✅ |
| Every interactive verb asserts the selector matched at least one element | `assert_sel(sel, i)` — defined line 411-420, called by every interactive verb. Raises with "selector '…' matched 0 elements — nothing happened. A silent miss IS the bug." | ✅ |

## B07 — WORKED EXAMPLE

| Claim | Evidence | Verdict |
|---|---|---|
| The fixture has `input#k`, `range 1..6, step 0.1` | `demo/sim-source/00-tiny-wave.html:14` — `<input id="k" type="range" min="1" max="6" value="2" step="0.1">`. | ✅ |
| Script opens with `{"set": ...}`, not `{"wait": ...}` | `demo/scripts/tiny-wave-sweep.json:2` — first step is `{"set":"#k","value":1}`. | ✅ |
| Rule "start with an interactive step, not a wait" is in the docstring | Module docstring line 43-45: "Playwright only records from the first page-activity event. A script that starts with `{"wait": N}` will NOT capture that idle period. Always open with an interactive step (set/click/check) to anchor the recording at t=0." | ✅ verbatim |

## B08 — OBSERVED FAILURE (Apple App Sandbox)

| Claim | Evidence | Verdict |
|---|---|---|
| Chromium exits with a FATAL Mach-port bootstrap denial | `demo/failure-sandbox.txt` — `[FATAL:base/apple/mach_port_rendezvous_mac.cc:159] Check failed: kr == KERN_SUCCESS. bootstrap_check_in org.chromium.Chromium.MachPortRendezvousServer.58727: Permission denied (1100)`. | ✅ observed |
| `capture_sim.py`'s except-block prints `[capture_sim] FAILED: …` and exits 1 | Lines 656-658 (`except Exception as e: … sys.exit(1)`). Output matches — first line is exactly `[capture_sim] FAILED: BrowserType.launch: …`. | ✅ |
| No mp4 is written on failure | After the exception, `finally` block (line 254-256) shuts down the server and rmtrees `tmp_dir`; the `media/` folder from that run has no `output.mp4`/`change.mp4`. Verified — `demo/media/` does not exist after this run. | ✅ |
| Root cause is the SANDBOX, not the tool | Same command outside the Claude Code sandbox (in a normal terminal or CI) is the ordinary happy path — the failure is entirely on the Chromium spawn boundary. This is stated as a limitation, not a workaround. The tool does not currently honor `ART_CHROME`; that is out of scope for this episode. | ✅ |

## B09 — VERDICT

Each of the six lines corresponds directly to a beat above:

1. "A Playwright wrapper for D3 sims" — module docstring line 3.
2. "Serves the file on a local port" — lines 67-86.
3. "Launches headless Chromium" — line 133.
4. "Optionally drives one control" — the three modes (default range sweep / click-through / script).
5. "ffmpeg remuxes webm to mp4 in `media/`" — line 91-108, 162, 248, 359, 557.
6. "Every silent miss is an error, not a static clip" — the assertion pattern in `capture_click_through()` (line 312-317) and `capture_scripted()` (line 411-420).

## B10 — YOUR TURN

The trap called out ("watch for whether Claude opens the script with `wait`") is the same docstring rule cited in B07 evidence — it exists specifically because a leading `wait` produces a silently truncated recording, which is exactly the "silent miss" the tool is otherwise built to reject. Naming the trap out loud is the whole point of the beat.

## B11 — OUTRO

- Title restated verbatim: "Brutalist Utility: capture_sim.py."
- Sign-off "Liam, in for Bear, for @HumanitariansAI."
- Card component is the locked `ClaudeTitleOutro` with hardcoded `@NikBearBrown` handle per `OUTRO-LOCK.md` — flagged in `README.md` for the human reviewer.

## Documented gaps and honest labels

- **No captured mp4** from the actual `capture()` browser path is included in this reel. The B04/B05/B06/B07 code beats teach what the code does, and B08 shows the observed sandbox failure. The reel does not claim to have run Chromium successfully in this session.
- The example beat sheets (`rohan-v/…`, `mohammed-h/…`) informed shot shapes only. None of their captured media, narration, or approvals is reused here.
- Legacy `scripts/type_check.py` and `reference/type-spec.md` referenced by public docs are not present in the toolkit — see `TYPECHECK.md`. Visual typography is reviewed by frame inspection instead.
