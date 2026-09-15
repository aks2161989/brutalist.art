# CHECKS-REPORT — The finance Skill — Short

- run_id: `13d2d44505974808943797b6a8c480ca`
- source_sha256 (supervisor episode source): `0eee85f3f27b9cd70551e72ed18783981da21d0b4a6562d87f5014676fe4c102`
- parent portrait master SHA-256: `15c8209ca63fc8c820fc4f78112955dec5f81c12b1d9eab02f0887d1754b353b`
- final Short: `exports/short/claude-liam-brutalist-skill-finance-short.mp4`
  - SHA-256: `2fa8d4b0d4770c243f42ae05e743a7052462833f6d60281f108334b1808a02c4`
  - Container duration: **169.917s** — strictly under 180.0s (headroom ≈ 10.08s)
  - Video stream: h264, 2160×3840, 169.917s
  - Audio stream: aac, 48 kHz, 169.916s, mean −27.2 dB / max −4.3 dB (no clipping)
- beat_sheet.json SHA-256: `806f44290ce176d799e657fb91ffe66125edca806446bff055b7e0f34a19e0da`

## Gate: strictly under 3:00

| Measure | Value | Cap | Pass |
|---|---|---|---|
| Planned duration (sum of retained render_duration_s) | 169.87s | < 180.0s | ✅ |
| Container ffprobe duration | 169.917s | < 180.0s | ✅ |
| Video stream duration | 169.917s | < 180.0s | ✅ |
| Audio stream duration | 169.916s | < 180.0s | ✅ |
| Headroom below cap | ≈ 10.08s | — | ✅ |

`runtime/scripts/build_safety.py::require_short_duration` gate is satisfied
and `shorts.py` printed `short_validation: {status: ready, errors: []}`.

## Gate: whole-beat cut

`CUT-PLAN.json` records `strategy: whole-beat-cut` with `rewrite_reason: null`.

- Kept beats (7): B00, B01, B04, B05, B06, B09, B11
- Dropped beats (5): B02, B03, B07, B08, B10 (rationales in CUT-PLAN.json)
- Every retained beat is used **unchanged** from the parent portrait master
  (`shorts.py` logged "native portrait reused unchanged" for all seven).
- No narration was regenerated. Kokoro am_onyx audio, no ElevenLabs.

## Gate: aspect + dimensions

- All seven retained media files are 2160×3840 (native portrait) per
  `ffprobe` inspection of the parent `vertical/media/` sources before copy.
- Compiler output is 2160×3840, matching `--height 3840`.
- `beat_sheet.json.metadata.aspect_ratio = "9:16"`, `kind = "short"`,
  `voice = am_onyx`, `voice_kokoro = am_onyx`, `captions = false`,
  `playlist = "Brutalist"`.

## Gate: narration coherence

See `VISUAL-REVIEW.json.joins_review` for a per-join analysis. The retained
narration numbering resolves as First → Second → Third → Verdict; the
dropped "Fourth" decision (colour + geometry, B07) and the dropped
falsifiability beat (B08) are compactly restated inside the B09 verdict,
so no downstream reference is left dangling.

## Gate: audio

- Silencedetect (`-40 dB`, ≥0.6s) reports 10 gaps, all ≤ 0.76s. Each maps
  to either a natural mid-sentence pause copied from the parent narration,
  a beat boundary, or the room-tone tail after the outro. No 2s+ gap.
- Mean volume −27.2 dB, max −4.3 dB → no clipping.

## Gate: visual evidence

- `_qc/frames/` contains 21 native portrait frames (540×960 review scale)
  at beat-relative 15% / 50% / 85% for every retained beat, each with
  SHA-256 recorded in `VISUAL-REVIEW.json.frames[]`.
- `_qc/contact.png` is a 15×8 tile at 2 fps across the full 169.9s.
- Every frame was inspected. No blockers, no majors.

## Compiler skin-lint notes (informational)

The compiler emitted two SKIN LINT notes carried over from the parent
portrait master:

- B00 `palette=claude` but the cold open is `ClaudeComposerAsk916` — the
  registered native portrait companion for `ClaudeComposerAsk`.
- B11 `palette=claude` but the outro is `ClaudeTitleOutro916` — the
  registered native portrait companion for `ClaudeTitleOutro`.

These are lint entries, not gate failures. Both compositions were accepted
in the parent 9:16 master and are reused unchanged here.

## Human review

- No human review captured in this run. `FEEDBACK.md` is empty pending
  Bear's review. The Short is agent-verified only.

## Result

**READY for Bear's review.** Not published. Not uploaded. No git push.
