# CHECKS-REPORT.md — The deep-explainer Skill — Short

Run ID: `686f8111253047dcbb48696669a9eba8`
Source SHA-256 (BUILD-PROMPT.md): `df08fab3f88fd75e63f5c5a7f9df7af4e1b6f4ed752ce4e4196475d667d78659`

## Cut plan

- Strategy: `whole-beat-cut` (no rewrites)
- Kept: B00, B01, B03, B06, B07, B10, B11, B14, B16 (9/15)
- Dropped: B02, B04, B08, B12, B13, B15 (6)
- Planned duration from `render_duration_s` sum: 119.79 s
- Measured container / video / audio duration: 119.792 s / 119.792 s / 119.791 s

## Cap check (SHORTS_CAP_S = 180.0)

- Container 119.792 s → **PASS** (60.208 s below the ceiling)
- Video stream 119.792 s → **PASS**
- Audio stream 119.791 s → **PASS**
- All three probes strictly less than 180.0, per BUILD-PROMPT §3.

## Dimensions

- Final export: 2160×3840 (native portrait), h264 / aac
- Every retained beat's native media was 2160×3840 and reused unchanged
  (aspect check: `width * 16 == height * 9` → 34560 == 34560)

## Compiler output

- `shorts.py` printed: `9 beats · ~119.8s (1:59.8) OK`
- `compile.py` printed: `slots: 9/9 filled` and `119.8s`
- No slate fallbacks; no missing audio
- Skin-lint warnings (inherited from parent, not caused by the cut):
  - `B00 palette=claude cold open is ClaudeComposerAsk916` (accepted)
  - `B16 palette=claude outro is ClaudeTitleOutro916` (accepted)
- Motion histogram warning: `illustrate: 5/9 (55%)` — see VISUAL-REVIEW notes

## Coherence audit (post-concat narration)

- B01 promises "two hard gates" → delivered by B10 (D1) and B11 (D2)
- B03 sets up inheritance → B14 recap line 1 lands on it
- B06 + B07 establish the "owned middle" → B14 recap line 2 lands on them
- No "as we just saw" callbacks reference dropped beats
- No numbered transition breaks
- Liam's introduction (B00) and sign-off (B16) both retained

## Audio decode

- Wav extract at 22050 Hz mono: duration 119.808 s
- Loudness: mean −27.2 dB / max −5.7 dB (no clipping, no dead audio)
- Join frames sampled at each retained transition; no truncated speech

## Visual QC evidence

- 240-frame 2 fps contact sheet: `_qc/contact/f0001..f0240.jpg`
- 27 beat-relative 15/50/85% frames: `_qc/frames/`
- 6 join-edge frames: `_qc/edge/join_*.jpg`
- First/last frames: `_qc/edge/first.jpg`, `_qc/edge/last.jpg`
- All frame paths and SHA-256s recorded in `VISUAL-REVIEW.json`

## Output

- Short: `exports/short/claude-liam-brutalist-skill-deep-explainer-short.mp4`
- SHA-256: `c6491dc4d071be27be05f7ba7569e0e1c200f77b849b1618ca4b817fe986cae5`
- Size: 9,461,862 bytes (~9.02 MB)
- Beat sheet: `beat_sheet.json`
- SHA-256: `dde70823b2b52480aded89b178f66471daa7d901482d8a98c35fe03bb8466b50`

## Blockers / majors

- 0 blockers, 0 majors

## Limitations

- Motion histogram over ~40% `illustrate` — inherent to the retained
  mechanism pool; not fixable in a whole-beat cut without regenerating
  the parent's compositions (out of scope for a derivative).
- Outro card `ClaudeTitleOutro916` hardcodes `@NikBearBrown` per
  `OUTRO-LOCK.md`; the narration reads "at Humanitarians A-I" so the
  channel identity is audible. Human reviewer decides whether to
  replace the outro card before publication.
