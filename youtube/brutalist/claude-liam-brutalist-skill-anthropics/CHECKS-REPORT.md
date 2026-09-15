# CHECKS-REPORT.md — The anthropics Skill (landscape 3840×2160)

*Every current runtime check run against the final master. Outputs are quoted
verbatim from the tool. Failures are repaired in the reel, not in the check.*

## Environment

- Toolkit: isolated workspace copy under
  `/Users/bear/Documents/CoWork/bear-textbooks/books/brutalist.art/.repoloop/workspaces/claude-liam-brutalist-skill-anthropics/toolkit`
  (read-only public toolkit not modified).
- Run: `3d80d6c77f6e4febae4b0621b229c773` (re-review; original build run `485d27366b4f49a9b54a62d76e99a56b` 2026-09-08).
- Date: 2026-09-11.
- Browser (Remotion): `chrome-headless-shell` via
  `runtime/chrome-wrapper.sh` (`--single-process --in-process-gpu
  --no-sandbox`) with `ART_CHROME_MODE=chrome-for-testing` — the Apple App
  Sandbox blocks the system Chrome, so the wrapper points Remotion at the
  cached chrome-for-testing binary. Documented in
  `feedback_chrome_sandbox.md`.

## Gate V — final_frame_check.py

```
$ python3 runtime/qc/final_frame_check.py <reel> \
    --mp4 <exports/landscape>/…/candidate.mp4 \
    --sheet <clips/_work>/resolved-sheet.json
```

Read `_qc/REPORT.md`:

> # Gate V — visual QC report
>
> Frames sampled: 22  ·  BLOCKER: 0  ·  MAJOR: 0
>
> Clean — no BLOCKER/MAJOR defects. ✓

22 frames = 11 beats × (50 %, 85 %) steady-state sample. `_qc/frames/*.png`
persist per beat; `_qc/contact_sheet.png` covers the reel at a glance.

## Compiler final gate — atomic verified.json

The compiler writes an atomic receipt beside the master:

```
$ ls exports/landscape/
claude-liam-brutalist-skill-anthropics.mp4
claude-liam-brutalist-skill-anthropics.verified.json
```

The `verified.json` pins the master's SHA-256 and every input
(`media/B00.mp4 … B10.mp4`, `mp3/beat-B00.mp3 … B10.mp3`) that fed it. If
any input changes, the receipt no longer verifies without a re-compile.

Master SHA-256:
`0a7cf8e4535532f32fdd04089490cc9244928b7b2314fd687ad2e56d721ebc00`.
Duration: 228.875 s.

## ffprobe — decode + audio

```
$ ffprobe -v error -show_streams -of json exports/landscape/*.mp4
```

- Video stream: `h264 yuv420p 3840×2160 30 fps`, duration 228.87 s.
- Audio stream: `aac 48 kHz stereo`, duration 228.87 s.
- No orphaned or truncated frames; the file decodes cleanly with a hard
  refuse from ffprobe on any header or index defect.

## Motion histogram (compiler)

```
[art] motion histogram: reveal:7  type-on:3  hold:1
[art] WARNING: 'reveal' carries 7/11 beats (63%) — over the ~40% pantry cap;
      convert the excess to another language (MOTION.md)
```

**Disposition:** WARNING, not a blocker. The skill teardown template is
built out of four `SkillTeardownMechanism` acts (B04/B05/B06/B07) that share
one reveal grammar, plus the anatomy and pipeline reveals — that is the
teardown modifier's design, and swapping them would break the "one motion
per act type" grammar the modifier locks in. Documented here; not repaired.

## Skin lint (compiler)

```
[art] SKIN LINT: B00: palette=claude but the cold open is 'ClaudeComposerAsk916'
      — COLD OPEN LAW wants ClaudeComposerAsk
[art] SKIN LINT: B10: palette=claude but the outro is 'AntOutro916' —
      OUTRO LAW wants ClaudeTitleOutro
```

**Disposition:** intentional, both:

- `ClaudeComposerAsk916` is the native 9:16 registration of the same
  `ClaudeComposerAsk` component (BUILD-PROMPT: "Cold open: ClaudeComposerAsk
  (or a native portrait variant with that prefix)"). The landscape reel
  uses the same component — this line fires on both. Not a defect.
- `AntOutro916` is the native custom outro registered *only* in this
  reel's isolated toolkit to encode `@HumanitariansAI` (the shipped
  `ClaudeTitleOutro` hardcodes `@NikBearBrown` per `OUTRO-LOCK.md`). The
  channel adaptation is the whole point of writing a native variant per
  the BUILD-PROMPT ("This playlist belongs to @HumanitariansAI"). Not a
  defect; recorded in `SOURCES.md` under "Scenes used and their sources".

## Missing checks (honest gaps)

- `scripts/type_check.py` — referenced in older docs, not present in this
  toolkit snapshot. Typography inspection was done visually against the
  Gate V frames (see `TYPECHECK.md`).
- `reference/type-spec.md` and `ILLUSTRATIONS.md` — referenced in older
  docs, not present. Not a Gate V check; recorded so the reviewer knows
  what was and was not run.
- No kerning-lint tool ran; kerning was inspected visually on frames at
  full 4K resolution.

## Visual inspection log

Sample frames opened with the image-capable Read tool during the review:

- `_qc/frames/B00_85pct.png` — cold-open composer, greeting, ask, three
  answer lines, `@HumanitariansAI` chip, terracotta rule.
- `_qc/frames/B01_85pct.png` — hesitant writer showing the corrected
  sentence.
- `_qc/frames/B10_85pct.png` — outro card, terracotta period on the
  title, `@HumanitariansAI`, `LIAM, IN FOR BEAR.`
- `_qc/contact_sheet.png` — reel at a glance.

## Conclusion

All current runtime checks pass or resolve to intentional design (motion
histogram, skin lint). Master receipt is atomic. Gate V is clean. Visual
review is recorded in `VISUAL-REVIEW.json`. Human review pending —
Bear's viewing and editing is the next stage.
