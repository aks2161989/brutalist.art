# Script — Brutalist Utility: capture_sim.py (Short)

Slug: `claude-liam-brutalist-runtime-capture-sim-short`
Aspect: 9:16 native (2160×3840)
Duration: 139.208 s (0 clipped audio, strictly < 180 s)
Voice: Kokoro `am_onyx` — Liam, in for Bear
Captions: false

This is a whole-beat cut of the vertical parent `claude-liam-brutalist-runtime-capture-sim-vertical`. Narration and native portrait video for each kept beat are reused unchanged; nothing was rewritten. Beats B03/B04/B05/B06 (deep CLI + code walks) and B10 (Your Turn) were dropped as long-form material.

## Beats retained (in order)

### B00 — ASK · 17.00 s · `mp3/beat-B00.mp3`
> Tere, this is Liam, in for Bear. The ask — I've got a one-file D3 simulation on disk and I need two clean mp4s to drop into the reel. Baseline at rest. Then the same page while the main control moves. Headless. No cursor. No audio track. Something the compile step can concatenate without babysitting.

### B01 — BLUF · 14.58 s · `mp3/beat-B01.mp3`
> Watch the writer walk this back. Capture sim does not render the simulation. The simulation is a D three HTML file. Capture sim launches a headless browser, points it at that file, and records what the browser paints. The browser draws. The tool records.

### B02 — FRAMEWORK · 26.71 s · `mp3/beat-B02.mp3`
> The pipeline. Start a local HTTP server on a free port — file colon slash slash blocks CDN requests, and D three loads from a CDN. Launch Playwright's headless Chromium and open that URL. Optionally drive a control — sweep a range, click through a set, run a script. Playwright records a web m the whole time. When the page closes, hand the web m to ffmpeg for a well muxed mp4. Two mp4s in the default mode. One mp4 in click through and script modes.

### B07 — WORKED EXAMPLE · 25.38 s · `mp3/beat-B07.mp3`
> Worked example. One HTML on disk — a tiny D three sine wave with a slider called hash k, one through six. One script JSON — set hash k to one, wait four tenths, sweep hash k from one to six over thirty steps, land at three point five, hold six tenths. The script opens with set — not with wait — because Playwright only records from the first page activity event. A leading wait would silently drop that first second. That rule is in the module docstring.

### B08 — FAILURE / COUNTEREXAMPLE · 26.67 s · `mp3/beat-B08.mp3`
> The observed failure — verbatim on this workstation. Same command a fellow would type. Chromium tries to bootstrap a Mach port, macOS App Sandbox refuses, the child process dies with a fatal, capture sim prints FAILED and exits one. The tool caught it — no zero byte mp4 got written. The fix is not in capture sim. The fix is to run capture sim in a normal terminal, outside Claude Code's sandbox, or in CI. A limitation is a real finding — not a reason to fake a clip.

### B09 — VERDICT · 22.83 s · `mp3/beat-B09.mp3`
> So — capture sim dot py. A Playwright wrapper for D three sims. It serves the file on a local port, launches headless Chromium, optionally drives one control — a range sweep, a click list, or an ordered script — and screen records the browser. ffmpeg remuxes web m to mp4 in media slash. Every selector is asserted before it runs. Every silent miss is an error, not a static clip. The tool records. The browser draws.

### B11 — OUTRO · 6.04 s · `mp3/beat-B11.mp3`
> Brutalist Utility: capture sim dot py. Liam, in for Bear, for at Humanitarians A I.

## Dropped beats

- **B03** (`CLI --help` verbatim, ~21.3 s) — long-form MECHANISM detail.
- **B04** (`capture()` default two-context sweep code, ~29.7 s) — long-form MECHANISM detail.
- **B05** (`capture_click_through()` code + `count>=2` guard, ~28.6 s) — long-form MECHANISM detail.
- **B06** (`capture_scripted()` 7-verb DSL dispatch code, ~28.1 s) — B07's worked example teaches the DSL by concrete usage.
- **B10** (Your Turn assignment, ~31.1 s) — Shorts prompt permits omission; verdict → outro closes cleanly.
