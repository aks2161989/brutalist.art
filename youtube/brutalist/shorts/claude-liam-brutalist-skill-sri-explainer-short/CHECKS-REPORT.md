# The sri-explainer Skill — Short · CHECKS REPORT

**Run ID:** `8fdcf22fafee4271bc76638c6dceb4b4` · **Date:** 2026-09-12 · **Presenter:** Liam (in for Bear)
**Rendered file:** `exports/short/claude-liam-brutalist-skill-sri-explainer-short.mp4`
**Rendered SHA-256:** `01d6505b886b4674d104848d59fb336fb04c35ad4dd2231e7f7796931a5f1cce`
**Beat-sheet SHA-256:** `68e5b02cf27c6efc9db0e6df26ec898e9bd62938cb74e49099807222dddee987`

## Duration gates — all pass

| Metric | Measured | Requirement | Status |
|---|---:|---|:---:|
| Planned timeline | 171.958 s | < 180.0 s (strict); target ≤ 175 s | ✅ |
| Video stream (`ffprobe stream:v`) | 171.917 s | < 180.0 s | ✅ |
| Audio stream (`ffprobe stream:a`) | 171.958 s | < 180.0 s | ✅ |
| Format container (`ffprobe format`) | 171.958 s | < 180.0 s | ✅ |
| Encoding headroom | 8.042 s under cap | ≥ 4 s | ✅ |

## File integrity

- Container: MP4 · video `h264` 2160×3840 @ 24/1 fps · audio `aac` stereo, per-beat timeline preserved
- Size: 11.66 MB — reasonable for 172s of near-static portrait cards
- No dropped frames, no unmeasurable duration

## Frame evidence (extracted from the final render)

- Contact sheet: 344 frames @ 2 fps → `_qc/contact/f_0001.jpg…f_0344.jpg`
- Per-beat 15% / 50% / 85% frames: 27 frames → `_qc/beat/B##_p##.jpg` (SHA-256 recorded in `VISUAL-REVIEW.json`)
- Portrait framing verified on B00, B01, B03, B05, B06, B07, B10, B11, B13
- Legibility verified: title/heading, body copy, cite label, verdict pill, and outro handle
  all inside the 9:16 safe area on every inspected frame
- Cream/ink/terracotta palette holds; dark palette-inverted outro on B13 is correct per
  OUTRO LOCK

## Audio join analysis (`ffmpeg volumedetect`)

Measured at every cut seam (±0.6 s window) and at both ends:

| Segment | Mean (dB) | Peak (dB) |
|---|---:|---:|
| Start 0.0–0.5 s | −18.1 | −7.9 |
| B00→B01 seam | −22.1 | −7.0 |
| B01→B03 seam | −22.2 | −7.1 |
| B03→B05 seam | −22.4 | −6.6 |
| B05→B06 seam | −23.9 | −5.9 |
| B06→B07 seam | −21.7 | −4.5 |
| B07→B10 seam | −21.5 | −7.7 |
| B10→B11 seam | −23.8 | −7.1 |
| B11→B13 seam | −22.3 | −5.3 |
| Tail last 0.5 s | −62.1 | −55.0 |

Every seam sits in the natural speech range; no clipping (peaks all under −4 dB); tail is
silent as expected (post-outro). Speech is never truncated near the 179 s cap because the
Short ends at 171.958 s.

## Skin lint (compiler)

- `B00: palette=claude but the cold open is 'ClaudeComposerAsk916'` — expected divergence for
  the 916 native portrait composition (inherited unchanged from parent, same accepted lint).
- `B13: palette=claude but the outro is 'ClaudeTitleOutro916'` — same acceptable divergence.
- Motion histogram flagged reveal-dominant (6/9); this is inherited from the parent Skill
  Teardown template; short-length cut preserves the parent's motion mix without introducing
  new pantry patterns.

## Editorial coherence

Numbered transitions "First / Second / Third decision" (B05 → B06 → B07) are contiguous.
Dropped "Fourth / Fifth decision" beats (B08 golden-test, B09 handoff) are recapped in the
verdict artifact (B11) as one-line items — no dangling references. B10 opens on "Now the
limitation" which reads cleanly after B07's compression rule.

## Publishing scope

Render only. No upload, no scheduling metadata, no related-video pairing.

## Sandbox / process

- Foreground shorts.py, single ffmpeg invocation per beat, concurrency 1 for compile.
- No `--review` was used on the compile pass; the compile ran at native 3840 height.
- Parent reel `vertical/` was read-only and untouched.
