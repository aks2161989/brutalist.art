# CHECKS-REPORT — Brutalist Utility: capture_sim.py (Short)

Every finding below reflects the actual run of this Short's build in the isolated toolkit workspace.

## Build inputs

- Parent reel (read-only): `youtube/brutalist/claude-liam-brutalist-runtime-capture-sim/vertical/`
- Parent master SHA-256: `fedfb0ca5e06ee130b855af4fc688bae02293fe05182660c39946f5079d686ab`
- This invocation's `episode.source_sha256`: `b5db05e266bb6645717f324a04548c779522f0d770245c45679a57dbecab7d75`
- This invocation's `run_id`: `a4ebd93adf44479e83f30c032daf338a`
- Previous `run_id`: `3ad75bda3d804b798a7d10d87c431d44` (source_sha256 changed; REPOLOOP-SHORTS-PROMPT.md updated; media clips unchanged)

## Cut strategy

- **Strategy:** `whole-beat-cut` (see `CUT-PLAN.json`).
- **Kept beats:** B00, B01, B02, B07, B08, B09, B11 (7 of 12).
- **Dropped beats:** B03, B04, B05, B06, B10 (long-form MECHANISM + YOUR TURN — retained in the vertical parent).
- **Estimated cut duration:** 139.2 s. **Measured:** 139.208 s (container).

## Recompile result (this run)

Source clips and audio are unchanged from the previous build (parent_master_sha256 unchanged). `compile.py` was re-run with the updated beat_sheet.json (new run_id + source_sha256 stamped). Output SHA-256 is bit-identical: `7813f8e5ccfbf17dcbaa34f214ba61c9843420b28746e0f7783a2e07241fc3cb`.

```
[art] motion histogram: code-cascade:2  type-on:1  hesitant-type:1  phase-flow:1  artifact-in:1  outro-card:1
[art] SKIN LINT: B00: palette=claude but the cold open is 'ClaudeComposerAsk916' — COLD OPEN LAW wants ClaudeComposerAsk
[art] SKIN LINT: B11: palette=claude but the outro is 'ClaudeTitleOutro916' — OUTRO LAW wants ClaudeTitleOutro
[art] build stamp → beat_sheet.json (7/7 filled)
[art] wrote exports/short/claude-liam-brutalist-runtime-capture-sim-short.mp4  (139.2s, audio: per-beat timeline, drawtext: no — PIL overlays)
[art] slots: 7/7 filled — B00:VIDEO B01:VIDEO B02:VIDEO B07:VIDEO B08:VIDEO B09:VIDEO B11:VIDEO
```

Skin-lint warnings are expected — portrait 916 compositions are the correct pattern for 9:16; the lint fires because the metadata palette field says `claude` but the beat uses the portrait variant `ClaudeComposerAsk916` / `ClaudeTitleOutro916`. Not a defect.

## `runtime/scripts/compile.py` output

- Command: `python3 runtime/scripts/compile.py <reel> --height 3840 --out <reel>/exports/short`
- Produced: `exports/short/claude-liam-brutalist-runtime-capture-sim-short.mp4`
- Verified manifest: `exports/short/claude-liam-brutalist-runtime-capture-sim-short.verified.json` (`status: ready`)

## Duration gates (strictly < 180 s required; measured with ffprobe)

| Measurement            | Value (s) | Under 180.0 s? |
|------------------------|----------:|:-------------:|
| Container `format.duration`   | 139.208 | ✅ |
| Video stream `duration`       | 139.167 | ✅ |
| Audio stream `duration`       | 139.208 | ✅ |
| Concatenated `render_duration_s` sum | 139.208 | ✅ |

## Dimensions & codec

- Container: MP4
- Video: h264, **2160 × 3840**, 24/1 fps (native portrait — no crop of a landscape master)
- Audio: aac, 48000 Hz, 2 channels

## Gate V (compile-integrated frame QC)

`_qc/REPORT.md`:

```
Frames sampled: 14  ·  BLOCKER: 0  ·  MAJOR: 0
Clean — no BLOCKER/MAJOR defects. ✓
```

## Frame QC (re-verified this run)

All 25 PNG files in `_qc/frames/` and contact sheets were re-hashed and compared against `VISUAL-REVIEW.json`. All hashes match — content is bit-identical to the verified previous build. Key reads:

- `first.png` — B00 composer, `@HumanitariansAI` folder chip, `Tere, Liam`, topic `BRUTALIST · UTILITY: CAPTURE_SIM.PY`. Legible.
- `B00-85.png` — ask + 3 cascade output lines inside SAFE916. No bleed.
- `B01-85.png` — hesitant-writer settled on `capture_sim / RECORDS / the browser.` with full BLUF coverage.
- `B02-50.png` — `Serve. Launch. Drive. Record. Remux.` heading + body + spark line inside SAFE916.
- `B07-50.png` — worked example HTML + JSON + docstring footer legible.
- `B08-50.png` — verbatim Mach-port failure log + honest environmental fix commentary.
- `B09-50.png` — 6-line verdict artifact, clean numbered list.
- `final.png` — outro card, `Brutalist Utility: capture_sim.py.` + `@NikBearBrown` handle (OUTRO-LOCK; flagged in README for human review).

## Audio decode QC

Audio decoded from previous build (`_qc/audio.wav`, 48 kHz stereo, 139.221 s). Output is bit-identical so findings are unchanged:
- `16.4–17.0 s` (0.6 s) — natural pause between B00 ASK and B01 BLUF; matches B01's declared `lead_silence_s: 0.8`.
- `122.0–122.7 s` (0.7 s) — natural pause between verdict lines inside B09.
- `138.7–139.2 s` (0.5 s) — trailing silence on the outro card, expected.
- No dropped audio at any beat join. No clipping.

## Metadata gates on the derivative beat sheet

- `kind: short` ✅
- `aspect_ratio: 9:16` ✅
- `playlist: Brutalist` ✅
- `voice: am_onyx`, `voice_kokoro: am_onyx` ✅
- `captions: false` ✅
- `run_id: a4ebd93adf44479e83f30c032daf338a` (stamped for this invocation)
- `source_sha256: b5db05e266bb6645717f324a04548c779522f0d770245c45679a57dbecab7d75` (stamped for this invocation)
- `parent_master_sha256: fedfb0ca5e06ee130b855af4fc688bae02293fe05182660c39946f5079d686ab` (recorded)

## Safety / provenance gates

- No `--review` was used as a final pass.
- No `ART_CHROME` bypass, no alternate renderer, no fabricated approvals, no invented URLs.
- No modifications to the parent reel, its exports, its source media, or the public toolkit.
- Independent file copies (not symlinks or hardlinks) in `media/` and `mp3/`.
- Human review pending; `README.md` in the vertical parent already flags the `@NikBearBrown` OUTRO-LOCK handle for `@HumanitariansAI` review before publication.

## Result

**PASS** — Short is ready for offline human review. Final file: `exports/short/claude-liam-brutalist-runtime-capture-sim-short.mp4` (139.208 s, 2160×3840, SHA-256 `7813f8e5ccfbf17dcbaa34f214ba61c9843420b28746e0f7783a2e07241fc3cb`).
