# CHECKS-REPORT — Brutalist Command: art keys — Short

Run: `b1097e088b3744ed874f3bcc50a2cebb` · Date: 2026-09-13

## The Shorts Cap (Gate D)

| Measurement | Value |
|---|---|
| Container duration (`ffprobe format.duration`) | **99.625 s** |
| Video stream duration | **99.625 s** |
| Audio stream duration | **99.625 s** |
| Shorts cap | 180.000 s |
| Headroom | 80.375 s |

All three measurements are strictly below 180.0 s. Compile.py enforces
`require_short_duration()` at the end of the build; this Short passed.

## Gate V — visual QC (compile.py)

```
Frames sampled: 12  ·  BLOCKER: 0  ·  MAJOR: 0
Clean — no BLOCKER/MAJOR defects. ✓
```

## Gate A — audio integrity

| Item | Value |
|---|---|
| Codec | aac |
| Sample rate | 48000 Hz |
| Channels | 2 |
| Duration | 99.625 s |
| `mean_volume` | −27.1 dB |
| `max_volume` | −4.2 dB (no clipping) |

No silence padding was inserted for retained beats; the source Kokoro mp3s
were concat'd verbatim by compile.py. Peaks remain safely under 0 dBFS.

## Per-beat integrity

| Beat | Source dims | Duration (s) | media/ sha256 | mp3/ sha256 |
|---|---|---|---|---|
| B00 | 2160×3840 | 11.583 | 15d0952021240aec2027dc28e04c2d5b14aed3dfca3ed05009390b8ce31f7bec | 2fb9eb044b82bf6e2942eca223c9dfcbc9eba5b6f9f0522fb4030d19c37c0eb6 |
| B01 | 2160×3840 | 14.083 | e4975e0038d8334b545c73faa699a717cbb6d21a6037e759536e7c0edbaeef2a | 13df1b61d78d5b9ba5b9863597fdbaa4f86f04b0a02b02ab679c6ad912a36692 |
| B04 | 2160×3840 | 18.375 | a0b3c22b421752e821081c07b856e762a175912a4006359957b292aecb2138c3 | c47666e190aff5e2ce11a6ba775f6c25f6e6e76fd3e49173b384d84e812af407 |
| B08 | 2160×3840 | 32.042 | 1e7d404671e65134d2c90a58f10b4c8485f0d4ad7ae10f89f78134572f2317bb | 3eb037dab141ee6e52fff8eb44627fc1dc69f02dd556fa08f7924488d89c0551 |
| B09 | 2160×3840 | 18.125 | 995d4df8af531cab587ab8526e5e92b1c0c9c4d5a6a8937ee6caa2eb985e4d5c | 1a7fe018a7932be2e6b2819e4c50d2728438382a055d9833d1bd6e4e8a07d191 |
| B11 | 2160×3840 | 5.417 | dcc5a5fdb55aacc9407459e76bd5a4a7ac62ea4839fb5a61ca389521ab327cfa | 8270450b9d52f41684352440169b13774fc4d60f2b51511dffabfc4c3ebc5a96 |

Every media file matches the delivery canvas (2160×3840) natively — no
center-cut was performed, no re-render was needed. Every mp3 is an
independent copy of the parent's Kokoro `am_onyx` render. All sha256 values
confirmed identical to the 2026-09-10 verified build; rebuild triggered by
SKILL.md source_sha256 update only.

## Skin lints (informational)

- `B00`: 916 shim (`ClaudeComposerAsk916`) — expected under portrait
  law, not a defect.
- `B11`: 916 shim (`ClaudeTitleOutro916`) — expected, per OUTRO-LOCK.

## Final artifact

- Path: `exports/short/claude-liam-brutalist-command-keys-short.mp4`
- SHA-256: `00cb6edf90a3e82ab932642c4d5888aec235a8b86dd0b654cb798a98f135c5a5`
- Beat sheet SHA-256: `024a36c6fe96a928790b3686bab2e4d3b58984e603399575a16f69fb37618ef2`
- Codec: h264 · 2160×3840 · 24 fps · AAC 48 kHz stereo

Ready for review; not queued for publication.
