# SCRIPT — Brutalist Utility: capture_sim.py

**Episode:** `claude-liam-brutalist-runtime-capture-sim`
**Voice:** Kokoro `am_onyx` (Liam, in for Bear)
**Register:** Teardown
**Channel adaptation:** composer chip reads `@HumanitariansAI`; outro card stays the locked `ClaudeTitleOutro` (hardcoded `@NikBearBrown` per `OUTRO-LOCK.md`) and is flagged in `README.md` for the human reviewer before publish.
**Word-budget:** body beats 45–70 words per `ai-explainer/SKILL.md`; ask / BLUF / handoff / verdict exempt where they earn it.

---

## B00 — ASK (cold open, `ClaudeComposerAsk`)
Greeting: `Tere, Liam` (Estonian, one word, fresh — not used in the `claude-liam-brutalist-*` series so far).

> Tere, this is Liam, in for Bear. The ask — I've got a one-file D3 simulation on disk and I need two clean mp4s to drop into the reel. Baseline at rest. Then the same page while the main control moves. Headless. No cursor. No audio track. Something the compile step can concatenate without babysitting.

## B01 — BLUF (hesitant writer, `BrutalistHesitantWriter`)
Correction is the reel's actual misconception. Text starts `capture_sim / renders / the sim.` and settles on `capture_sim / RECORDS / the browser.` — because the file NEVER draws anything itself; it drives a real headless Chromium against the sim and screen-captures what the browser paints.

> Watch the writer walk this back. Capture sim does not render the simulation. The simulation is a D three HTML file. Capture sim launches a headless browser, points it at that file, and RECORDS what the browser paints. The browser draws. The tool records.

## B02 — FRAMEWORK (concept illustration, `SkillTeardownPipeline`)
INPUT `sim.html + reel_dir` → phases `SERVE → LAUNCH → DRIVE → RECORD → REMUX` → OUTPUT `media/*.mp4`.

> The pipeline. Start a local HTTP server on a free port — file colon slash slash blocks CDN requests, and D three loads from a CDN. Launch Playwright's headless Chromium and open that URL. Optionally drive a control — sweep a range, click through a set, run a script. Playwright records a web m the whole time. When the page closes, hand the web m to ffmpeg for a well-muxed mp4. Two mp4s in the default mode. One mp4 in click through and script modes.

## B03 — MECHANISM 1 (code, `ClaudeCodeBeat`)
CLI surface, verbatim from `--help` — two positionals, four capture-shaping flags, three mode-selecting flags.

> The command surface. Two required positionals — the sim's html path, and the reel folder where media slash will be created. The default mode records two mp4s: output for the baseline hold, change for the range sweep. Dash dash click through switches to a discrete click list. Dash dash script switches to an ordered step list. Dash dash script and dash dash click through are mutually exclusive.

## B04 — MECHANISM 2 (code, `ClaudeCodeBeat`)
`capture()` — the default two-recording path. Baseline, then range sweep.

> Default mode. Two browser contexts, back to back. First — the baseline. Open the URL, wait for network idle, let D three settle a beat and a half, then hold for the requested duration. Playwright writes a web m. Second — the change. Same load, then find the first input type equals range, read its min and max off the element, and step from min to max in forty frames. Fire input and change events on every step so listeners actually run. Hold one second at max. Write the second web m. ffmpeg turns both into mp4s in media slash.

## B05 — MECHANISM 3 (code, `ClaudeCodeBeat`)
`capture_click_through()` — the discrete-controls path with an anti-silent-miss guard.

> Click through mode. For UIs where the control is not a slider — mode buttons, tabs, radios. Give it a selector, get one clip. Query the count on the page. If the count is under two, raise. A single element selector silently records nothing new — that is the bug the guard exists to catch. Otherwise: hold a beat, then click each element in DOM order, re querying every iteration so live DOM mutations don't invalidate old handles. Wait hold each seconds between clicks so the animation settles. Write one mp4 with the stem you named.

## B06 — MECHANISM 4 (code, `ClaudeCodeBeat`)
`capture_scripted()` — the ordered step DSL: `set`, `click`, `check`, `uncheck`, `sweep`, `scroll`, `wait`.

> Script mode. The DSL is seven verbs. Set writes a value and fires input and change. Click clicks — optionally at fractional coordinates within the element, which lets you hit a D three rect with its own handler through elementFromPoint. Check and uncheck flip a checkbox and fire change. Sweep animates a range with explicit from, to, steps, step delay — or reads the element's own min and max. Scroll scrolls into view. Wait sleeps. Every interactive verb asserts the selector matched at least one element; a silent miss is treated as a failure.

## B07 — WORKED EXAMPLE (code, `ClaudeCodeBeat`)
The disposable synthetic fixture and its prepared script — quoted verbatim from `demo/`.

> Worked example. One HTML on disk — a tiny D three sine wave with a slider called hash k, one through six. One script JSON — set hash k to one, wait four tenths, sweep hash k from one to six over thirty steps, land at three point five, hold six tenths. The script opens with set — not with wait — because Playwright only records from the first page activity event. A leading wait would silently drop that first second. That rule is in the module docstring.

## B08 — FAILURE / COUNTEREXAMPLE (code, `ClaudeCodeBeat`)
The observed sandbox failure — verbatim from `demo/failure-sandbox.txt`. This is what a fellow will see running `capture_sim.py` inside Claude Code on macOS.

> The observed failure — verbatim on this workstation. Same command a fellow would type. Chromium tries to bootstrap a Mach port, macOS App Sandbox refuses, the child process dies with a fatal, capture sim prints FAILED and exits one. The tool caught it — no zero byte mp4 got written. The fix is not in capture sim. The fix is to run capture sim in a normal terminal, outside Claude Code's sandbox, or in CI. A limitation is a real finding — not a reason to fake a clip.

## B09 — VERDICT (`ClaudeVerdictArtifact`)
The whole file in the order it does its job. Six lines.

> So — capture sim dot py. A Playwright wrapper for D three sims. It serves the file on a local port, launches headless Chromium, optionally drives one control — a range sweep, a click list, or an ordered script — and screen records the browser. ffmpeg remuxes web m to mp4 in media slash. Every selector is asserted before it runs. Every silent miss is an error, not a static clip. The tool records. The browser draws.

## B10 — YOUR TURN (`ClaudeComposerAsk`, greeting `Your Turn`)
Prompt read aloud verbatim, then discussed.

> Your turn. Paste this into Claude Code, pointed at any of your own single file D three sims. Ask Claude to write a five step script JSON for capture sim that OPENS with a set or click verb — never with wait — and drives the sim's main interactive control from its natural minimum to its natural maximum, ending on a distinctive middle value. Then dry read the JSON back at you and tell you what the first captured frame will look like. Watch for whether Claude opens the script with wait. That is the trap the module docstring calls out — a leading wait silently records nothing.

## B11 — OUTRO (`ClaudeTitleOutro`, slug-seeded mascot, hardcoded `@NikBearBrown`)

> Brutalist Utility: capture sim dot py. Liam, in for Bear, for at Humanitarians A I.
