# PROMPTS — Brutalist Utility: capture_sim.py (Short)

The Short reuses the parent's narration verbatim for every kept beat. The only prompt read aloud in the Short is the B00 cold-open ask; the extended Your Turn (parent B10) was dropped as long-form material.

## Cold-open ask (B00, spoken by Liam)

> The ask — I've got a one-file D3 simulation on disk and I need two clean mp4s to drop into the reel. Baseline at rest. Then the same page while the main control moves. Headless. No cursor. No audio track. Something the compile step can concatenate without babysitting.

**Expected `capture_sim.py` behavior:**
- Start a local HTTP server on a free port serving the sim's parent directory.
- Launch headless Chromium (Playwright); load the served URL; wait for `networkidle`; sleep 1.5 s for D3 settle; hold `--duration` seconds → `media/output.mp4`.
- Repeat load; find `input[type=range]` (or `--selector`); sweep min→max in 40 steps firing `input`+`change` on each; hold 1 s at max → `media/change.mp4`.
- ffmpeg remuxes both webms with `libx264 preset=slow crf=18 pix_fmt=yuv420p -an`.

## Failure text quoted verbatim in B08

Full evidence in the parent reel's `demo/failure-sandbox.txt`. Trimmed for the code card:

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
[pid=58727] <process did exit: signal=SIGTRAP>
# exit 1
```

The Brutalist workaround for OTHER browser pipelines (Remotion rendering) is to set `ART_CHROME` to a `chrome-headless-shell + --single-process` wrapper. `capture_sim.py` uses the Playwright API directly and does not honor `ART_CHROME` today — teaching it to would be a separate change; this episode does not modify the tool.

## Dropped prompt (belongs in the long)

Parent B10's Your Turn ("Point Claude Code at any single-file D3 simulation of your own…") is not read aloud in this Short. The full text lives in the vertical parent's `PROMPTS.md`.

## No "invented" prompts

Every prompt above is either quoted from `SCRIPT.md`, quoted from the module source, or captured by running the actual tool on this workstation. No prompt is manufactured to imply a signature, endorsement, or completed action that did not happen.
