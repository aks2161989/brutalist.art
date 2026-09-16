# CHECKS-REPORT — landscape — Brutalist Command: art scene-index

Run against the isolated toolkit at
`.repoloop/workspaces/claude-liam-brutalist-command-scene-index/toolkit`
on 2026-09-09 (initial build) and 2026-09-12 (source-update rebuild, run 88f42532).
All commands local, no paid APIs, no upload.

## 2026-09-12 Rebuild — source_sha256 6704da9d... (run 88f42532)

Source changes triggering rebuild:
- `art` file: `vertical` and `approvals` cases inserted above `scene-index`, shifting
  its line position from 71-74 to 92-95. B02 title prop and B09 verdict line corrected.
- Root.tsx: ClaudeCodeBeat916 now registered (from previous build), raising scene count
  from 619 to 620. B00/B05/B07/B09 narration and B05/B09 visual props updated.

Beats regenerated: B00, B02, B05, B07, B09 re-rendered; B00/B05/B07/B09 audio regenerated.
B09 render_duration_s corrected (26.667→26.75) to avoid audio truncation.
Both landscape and vertical recompiled with --force.

## Gate F — paperwork present before final compile

- `FACTCHECK.md` — written.
- `SHOTLIST.md` — written.
- `PROMPTS.md` — written.
- `SOURCES.md` — written.
- `BUILD-PROMPT.md` — supplied by the supervisor and preserved verbatim.
- `beat_sheet.json` — 12 beats, valid JSON, one build stamp per beat
  after `remotion_scenes.py`.

Result: PASS.

## Gate V — final_frame_check.py

Ran against the compiled `exports/landscape/claude-liam-brutalist-command-scene-index.mp4`.
Sampled at every beat's 50% and 85% steady-state (24 frames, beat-aware).

```
[gate-v] frames=24 BLOCKER=0 MAJOR=0 → _qc/REPORT.md
```

Contact sheet written to `_qc/contact_sheet.png` and reviewed via image-capable Read tool.
Individual beat frames extracted from media/B02.mp4, B05.mp4, B09.mp4 and confirmed:
- B02: title bar "art:92-95" ✓
- B05: first output line "620 renderable, 118 undocumented, 0 unresolved" ✓
- B09: verdict line 3 "writes scenes.json (620 entries...)", line 5 "art:92-95" ✓

Result: PASS (2026-09-12 rebuild). Original iteration notes:
- B01 initial fontSize 260 → 200 → 175 with lineSpacing 2.5 to clear
  both edge-bleed (BLOCKER at 200) and underfill (MAJOR at 170).
- B09 verdict card lifted from 6 to 8 lines to clear the 55% underfill floor.

## Audio decode + duration match

Twelve `mp3/beat-B*.mp3` files, all Kokoro `am_onyx`, all decoded by
`generate_audio_kokoro.py`. Actual durations returned to the beat sheet:

| beat | audio | narration | note |
|---|---:|---|---|
| B00 | 15.70 s | Bonjour cold open | regenerated 2026-09-12 (619→620) |
| B01 | 13.80 s | hesitant writer BLUF (≥9s required) | |
| B02 | 20.03 s | dispatcher case | re-rendered 2026-09-12 (art:71-74→art:92-95) |
| B03 | 21.74 s | THE LAW | |
| B04 | 29.78 s | three passes | |
| B05 | 21.93 s | scene-index output verbatim | regenerated 2026-09-12 (619→620) |
| B06 | 29.40 s | documented vs derived | |
| B07 | 22.23 s | SCENE-DOC-TODO head | regenerated 2026-09-12 (619→620) |
| B08 | 28.71 s | orphan scene falsifiability | |
| B09 | 26.73 s | verdict | regenerated 2026-09-12 (619→620) |
| B10 | 32.45 s | Your Turn | |
| B11 | 5.59 s | outro | |

Total audio = 267.09 s. Compiled master duration = 268.3 s (ffprobe). Delta
+1.21 s is the compiler's per-clip conform rounding — well inside the 5% retime ladder.

## ffprobe — final container (2026-09-12 rebuild)

```
Duration: 268.3s
Stream video: h264, 3840x2160
Stream audio: aac, 48000 Hz
```

Native 4K, h.264 + AAC, one audio stream, decodes cleanly.

## Motion histogram (compile.py warning, kept honest)

```
code-cascade: 7   type-on: 2   hesitant-type: 1   artifact-in: 1   outro-card: 1
WARNING: 'code-cascade' carries 7/12 beats (58%) — over the ~40% pantry cap
```

Kept. The command's evidence IS the tool's source + observed output; per
ILLUSTRATE LAW the honest illustration is code, not a decorative pattern
grafted on to hit a histogram bucket. Documented, not "fixed" by
swapping in animation that would misrepresent the tool. Same trade-off
as the scenes / icons episodes.

## Gaps and unshipped checkers

- `runtime/qc/type_check.py` / `reference/type-spec.md` / `skills/kerning`
  are referenced by public documentation but not shipped in this
  toolkit revision. GATE T's automated typography pass is unavailable
  here; TYPECHECK.md documents the manual visual typography review that
  filled in.
- `TYPECHECK.md` is not required by compile.py before a `--out` cut
  succeeds. It is provided per the supervisor's paperwork requirement.

## Final compile

```
[art] wrote exports/landscape/claude-liam-brutalist-command-scene-index.mp4  (268.3s, ...)
[art] slots: 12/12 filled — B00:VIDEO B01:VIDEO ... B11:VIDEO
```

`build-state.json` status = `ready`; `verified.json` written alongside
the mp4 with SHA-256 + input digests. Ready receipt is in place.
SHA-256: `06e3a14d9012795f7dcdb93b29254fd08d2684a60544269c083cd4013db1758e`
