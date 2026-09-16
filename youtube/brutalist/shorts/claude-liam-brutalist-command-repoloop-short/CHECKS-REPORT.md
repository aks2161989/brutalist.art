# CHECKS-REPORT — Brutalist Command: repoloop.sh — Short

Run: `2a3c292801ef4a0fba3291e5a03ab912` · 2026-09-13

## Delivered file

- Path: `exports/short/claude-liam-brutalist-command-repoloop-short.mp4`
- Size: 7.5 MB
- SHA-256: `ee8da1732db647bbc60a9603d8630549e3293c4f1ee6120aea0764a180f06052`

## Duration — STRICTLY UNDER 3:00

| Stream | Duration (s) | < 180.0 ? |
|---|---:|:---:|
| Container (format.duration) | 93.833 | pass |
| Video stream (h264) | 93.791667 | pass |
| Audio stream (aac) | 93.833 | pass |

Headroom to the 180.0s cap: **86.2s** — encoding headroom is generous.

## Dimensions & codecs

| Check | Value | Expected | Result |
|---|---|---|---|
| Video codec | h264 | h264 | pass |
| Video width | 2160 | 2160 | pass |
| Video height | 3840 | 3840 | pass |
| Aspect ratio | 9:16 (2160/3840 = 0.5625) | 9:16 | pass |
| Audio codec | aac | aac | pass |
| Audio channels/rate | stereo 48 kHz | ≥ mono, ≥ 44.1 kHz | pass |

## Audio integrity (ffmpeg volumedetect)

- Mean volume: **-27.0 dB** (verify_film requires > -40 dB — pass)
- Max volume: -4.6 dB (no clipping)
- Total samples: 9,009,152

## Beat sheet shape (Short profile)

| Check | Expected | Actual | Result |
|---|---|---|---|
| beat count | ≥ 3 (Short) | 6 | pass |
| playlist | Brutalist | Brutalist | pass |
| voice_kokoro / voice | am_onyx | am_onyx | pass |
| aspect_ratio | 9:16 | 9:16 | pass |
| kind | short | short | pass |
| captions | false | false | pass |
| First beat pattern | starts with `ClaudeComposerAsk` | `ClaudeComposerAsk916` | pass |
| Second beat pattern | contains `HesitantWriter` | `BrutalistHesitantWriter916` | pass |
| Penultimate greeting | `your turn` | `Your Turn` | pass |
| Outro pattern | starts with `ClaudeTitleOutro` | `ClaudeTitleOutro916` | pass |
| run_id set | present | `2a3c292801ef4a0fba3291e5a03ab912` | pass |

## Independence / no symlinks

- `find <reel> -type l` → 0 results.
- All media/mp3 files have distinct inodes and are byte-independent copies
  of the parent vertical reel's files (recorded in VISUAL-REVIEW.json).
- Parent reel and long export are unmodified.

## Contact sheet & frames

- 2 fps contact sheet extracted to `_qc/contact/` (188 frames, 540×960).
- Per-beat 15% / 50% / 85% frames extracted to `_qc/frames/` (18 total,
  full 2160×3840 quality). Every frame's SHA-256 is recorded in
  VISUAL-REVIEW.json.

## Skin lint (informational)

Compiler printed two SKIN LINT notes:
- `B00: palette=claude but the cold open is 'ClaudeComposerAsk916'` —
  informational; portrait suffix is the correct native 9:16 pattern.
- `B11: palette=claude but the outro is 'ClaudeTitleOutro916'` — same;
  portrait suffix is correct.

Both are the same lint the parent vertical reel prints. verify_film's
`startswith('ClaudeComposerAsk')` and `startswith('ClaudeTitleOutro')`
checks accept the `916` suffix.

## Cut plan verification

- Strategy: `whole-beat-cut` (no narration rewrite, no audio regeneration).
- Kept: B00 · B01 · B05 · B09 · B10 · B11 (6 of 12 parent beats).
- Dropped: B02 · B03 · B04 · B06 · B07 · B08 — reasons in CUT-PLAN.json.
- No dangling references in retained narration to dropped beats (verified
  in VISUAL-REVIEW.json coherence_review and SCRIPT.md).

## Verdict

**PASS** — Short renders at 2160×3840, 93.833s (< 180.0 by 86.2s),
audio mean -27 dB (> -40 dB), shape gates satisfied, VISUAL-REVIEW.json
matches this run's `run_id` (`2a3c292801ef4a0fba3291e5a03ab912`) and
current beat sheet SHA-256. Source_sha256 updated; parent_master_sha256
unchanged — parent vertical film unmodified. Cut plan identical to prior
run; no media re-render required.
