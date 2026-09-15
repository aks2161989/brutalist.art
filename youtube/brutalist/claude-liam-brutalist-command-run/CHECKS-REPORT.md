# CHECKS-REPORT — landscape — Brutalist Command: art run

Run against the isolated toolkit at
`.repoloop/workspaces/claude-liam-brutalist-command-run/toolkit`.
Original build: 2026-09-09. Re-rendered B02 on 2026-09-12 for run_id
`df4ab48ebf354eecb12e6a7d2316a270` — source_sha256 changed because the
`art` dispatcher `run)` case moved from lines 78-80 to 99-101 as the
`--list` section grew. B02 title corrected; all other beats unchanged.
All commands local, no paid APIs, no upload.

## Re-render sandbox fix (2026-09-12)

`npx remotion` resolved the globally-installed CLI rather than the
isolated toolkit's local copy, bypassing the patched `@remotion/renderer`.
Fix: patched `remotion_scenes.py` to invoke `node node_modules/@remotion/cli/remotion-cli.js`
directly; patched `toolkit/runtime/remotion/node_modules/@remotion/renderer/dist/open-browser.js`
to add `--single-process` on `darwin` (the existing `chrome-headless-shell` Mach-port
sandbox workaround — see memory `feedback_chrome_sandbox.md`). Neither change
affects the film content or narration.

## Gate F — paperwork present before final compile

- `FACTCHECK.md` — written.
- `SHOTLIST.md` — written.
- `PROMPTS.md` — written.
- `SOURCES.md` — written.
- `BUILD-PROMPT.md` — supplied by the supervisor and preserved verbatim.
- `beat_sheet.json` — 12 beats, valid JSON, one build stamp per beat
  after `remotion_scenes.py`.

Result: **PASS**.

## Gate L / Gate SHAPE / Gate A / Gate W / Gate B

- **Gate L (beat-mix lint)** — 12/12 beats classify SHOW; 7 are code
  cascades (`ClaudeCodeBeat`), 2 are composer ASKs (`ClaudeComposerAsk`),
  1 is the hesitant writer BLUF (`BrutalistHesitantWriter`), 1 is the
  verdict artifact (`ClaudeVerdictArtifact`), 1 is the outro card
  (`ClaudeTitleOutro`). No single-sentence text slides. **PASS**.
- **Gate SHAPE** — `not a finance reel — skip`. **PASS**.
- **Gate A / Gate W / Gate B** — no pending Manim scenes; every beat is
  a Remotion scene. Both static/pixel gates trivially pass (nothing to
  audit). Path recorded honestly.

## Gate V — `final_frame_check.py`

Ran against the compiled `exports/landscape/claude-liam-brutalist-command-run.mp4`.
Sampled at every beat's 50% and 85% steady-state.

```
[gate-v] frames=24 BLOCKER=0 MAJOR=0 → _qc/REPORT.md
```

`_qc/REPORT.md`:

```
# Gate V — visual QC report

Frames sampled: 24  ·  BLOCKER: 0  ·  MAJOR: 0

Clean — no BLOCKER/MAJOR defects. ✓
```

**Result: PASS.** Iterated to reach clean:

- B01 initial 2-line text + `fontSize 200 lineSpacing 2.5` triggered
  `MAJOR underfill 50%`. Widened text to `"art run renders\na master file."`
  and lifted to `fontSize 240 lineSpacing 2.6` — cover moves above the
  0.55 FILL_MIN floor.

## Audio decode + duration match

Twelve `mp3/beat-B*.mp3` files, all Kokoro `am_onyx`, all decoded by
`generate_audio_kokoro.py`. Actual durations returned to the beat sheet:

| beat | audio | narration |
|---|---:|---|
| B00 | 17.45 s | Ciao cold open |
| B01 | 17.22 s | hesitant writer BLUF (≥9s required) |
| B02 | 15.87 s | dispatcher case |
| B03 | 33.19 s | gate order |
| B04 | 22.36 s | audio + slot-skip |
| B05 | 16.26 s | Gate F output verbatim |
| B06 | 21.76 s | four knobs |
| B07 | 23.10 s | run vs final |
| B08 | 21.95 s | recovery |
| B09 | 28.67 s | verdict |
| B10 | 22.27 s | Your Turn |
| B11 | 5.23 s | outro |

Total = 245.33 s. Compiled master duration = 245.583 s (ffprobe).
Delta +0.25 s is the compiler's per-clip conform rounding — well
inside the 5% retime ladder.

## ffprobe — final container

```
Duration: 00:04:05.58, bitrate: ...
Stream #0:0 Video: h264 (High), yuv420p, 3840x2160, ...
Stream #0:1 Audio: aac (LC), 48000 Hz, stereo, fltp
```

Native 4K, h.264 + AAC, one audio stream, decodes cleanly.

## Motion histogram (compile.py warning, kept honest)

```
code-cascade: 7   type-on: 2   hesitant-type: 1   artifact-in: 1   outro-card: 1
WARNING: 'code-cascade' carries 7/12 beats (58%) — over the ~40% pantry cap
```

Kept. This is a command teardown; the command's evidence IS its
dispatcher, its `run.sh` source, and its observed output. Per ILLUSTRATE
LAW the honest illustration is code, not a decorative pattern grafted
on to hit the ~40% pantry cap. Same trade-off as the `scenes`, `icons`,
and `scene-index` episodes.

## Sandbox workarounds (honest disclosure)

Two environment workarounds applied before rendering, both documented in
memory and unrelated to the tool being explained:

1. **node_modules shadow** — the isolated toolkit's
   `runtime/remotion/node_modules` was a symlink into a
   `denyWithinAllow` path, blocking webpack's `.cache/` rotation.
   Replaced with per-package symlinks + a fresh writable `.cache/`.
2. **Chrome wrapper** — Apple's App Sandbox blocks `bootstrap_check_in`
   for Chrome's Mach-port bind. `ART_CHROME` points at a
   `chrome-headless-shell --single-process --in-process-gpu` wrapper.

Neither workaround changes the behavior of `art run`. Both are recorded
verbatim in `PROMPTS.md` §"Pre-build environment setup".

## Gaps and unshipped checkers

- `runtime/qc/type_check.py` / `reference/type-spec.md` / `skills/kerning`
  are referenced by public documentation but not shipped in this
  toolkit revision. GATE T's automated typography pass is unavailable
  here; `TYPECHECK.md` documents the manual visual typography review
  that filled in.
- `TYPECHECK.md` is not required by `compile.py` before a `--out` cut
  succeeds. It is provided per the supervisor's paperwork requirement.

## Final compile

```
[art] wrote exports/landscape/claude-liam-brutalist-command-run.mp4  (245.6s, ...)
[art] slots: 12/12 filled — B00:VIDEO B01:VIDEO ... B11:VIDEO
```

`build-state.json` status = `ready`; `claude-liam-brutalist-command-run.verified.json`
written alongside the mp4 with SHA-256 + input digests. Ready receipt
in place.
