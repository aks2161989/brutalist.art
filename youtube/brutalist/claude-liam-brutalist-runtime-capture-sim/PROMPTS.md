# PROMPTS — Brutalist Utility: capture_sim.py

## Cold-open ask (B00, spoken by Liam)

> The ask — I've got a one-file D3 simulation on disk and I need two clean mp4s to drop into the reel. Baseline at rest. Then the same page while the main control moves. Headless. No cursor. No audio track. Something the compile step can concatenate without babysitting.

**Expected `capture_sim.py` behavior:**
- Start a local HTTP server on a free port serving the sim's parent directory.
- Launch headless Chromium (Playwright); load the served URL; wait for `networkidle`; sleep 1.5 s for D3 settle; hold `--duration` seconds → `media/output.mp4`.
- Repeat load; find `input[type=range]` (or `--selector`); sweep min→max in 40 steps firing `input`+`change` on each; hold 1 s at max → `media/change.mp4`.
- ffmpeg remuxes both webms with `libx264 preset=slow crf=18 pix_fmt=yuv420p -an`.

## Your-Turn prompt (B10, read aloud verbatim then discussed)

> Point Claude Code at any single-file D3 simulation of your own. Ask Claude to write a five-step script JSON for `capture_sim.py` that OPENS with a `set` or `click` verb — never with `wait` — and drives the sim's main interactive control from its natural minimum to its natural maximum, ending on a distinctive middle value. Then have Claude dry-read the JSON back to you and describe what the first captured frame will look like. Watch for whether Claude opens the script with `wait` — that is the trap the module docstring calls out. A leading `wait` silently records nothing until the next interactive step; the tool will not error, the first N seconds are just missing.

**Expected artifact:** a JSON array of 5 step objects, first step key ∈ {`set`, `click`, `check`, `uncheck`, `sweep`}, valid CSS selectors, all numeric bounds within the control's actual range. Second-to-last step lands on a distinctive middle value; last step is a short `wait` (0.5–1.0 s) for the freeze frame.

**Test of success:**
```
python3 runtime/scripts/capture_sim.py path/to/sim.html /tmp/test-reel \
    --script your-script.json --out-name your-run
ls /tmp/test-reel/media/your-run.mp4
# → an mp4 whose first frame is the RESULT of step 1, not a blank page.
```
(This will only run outside the Claude Code Apple App Sandbox — see B08.)

## Failure text quoted verbatim in B08

Full evidence in `demo/failure-sandbox.txt`. Trimmed for the code card:

```
$ python3 runtime/scripts/capture_sim.py \
      demo/sim-source/00-tiny-wave.html demo --duration 1 --change-dur 1
[capture_sim] sim=00-tiny-wave.html  reel=…/demo
[capture_sim] FAILED: BrowserType.launch: Target page, context or browser has been closed
<launched> pid=58727
[pid=58727][err] [FATAL:base/apple/mach_port_rendezvous_mac.cc:159]
                 Check failed: kr == KERN_SUCCESS.
                 bootstrap_check_in org.chromium.Chromium.MachPortRendezvousServer.58727:
                 Permission denied (1100)
[pid=58727] <process did exit: exitCode=null, signal=SIGTRAP>
# exit 1
```

The Brutalist workaround for OTHER browser pipelines (Remotion rendering) is to set `ART_CHROME` to a `chrome-headless-shell + --single-process` wrapper. `capture_sim.py` uses the Playwright API directly and does not honor `ART_CHROME` today — teaching it to would be a separate change; this episode does not modify the tool.

## No "invented" prompts

Every prompt above is either quoted from `SCRIPT.md`, quoted from the module source, or produced by running the actual tool on this workstation. No prompt is manufactured to imply a signature, endorsement, or completed action that did not happen.
