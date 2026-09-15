# CHECKS-REPORT — Short (9:16) — Brutalist Command: art scene-index

## Build inputs

- Parent reel: `../claude-liam-brutalist-command-scene-index/`
- Parent vertical companion: `../claude-liam-brutalist-command-scene-index/vertical/`
- Parent master (referenced, unchanged): `parent_master_sha256 =
  f7cbed1ea45539e6025af8a08d3bd2921943bae569b32158c669ad0b60aa11f6`
- Source brief hash: `38ca86b097b8c3ac89f97c04f549f5894f2ccd66ba1bbbfc115615141181f4bd`
- Run id: `7fbbc6577e9d434aa02b367381fe29af`

## Context

The Sep-09 Short (run `ee4b71611b124fb0974870165833bd1e`) was built from a parent
vertical that reported 619 renderable compositions. The parent was rebuilt on 2026-09-12
(adding ClaudeCodeBeat916 to Root.tsx, raising the count to 620). Three beats were
re-rendered in the parent vertical: B00, B05, B09. Those updated 2160×3840 media files
and updated Kokoro mp3s were copied into the Short's media/mp3 folders on 2026-09-12,
but the Short export itself was not recompiled. This run recompiles the Short with those
updated files and updates all review documents. No beat was rewritten; the cut plan and
beat selection (B00/B01/B03/B05/B09/B11) are unchanged from the Sep-09 build.

## Cut plan (unchanged)

- Strategy: whole-beat cut (see `CUT-PLAN.json`).
- Kept: B00, B01, B03, B05, B09, B11.
- Dropped: B02, B04, B06, B07, B08, B10 — reasons in `CUT-PLAN.json`.
- No outro rewrite. No endcard. No pantry override.

## Assets

- `media/B{00,01,03,05,09,11}.mp4` — 2160×3840, h.264, no audio.
  - B00, B05, B09: updated 2026-09-12 from rebuilt vertical (620 count).
  - B01, B03, B11: unchanged from Sep-09 build.
- `mp3/beat-B{00,01,03,05,09,11}.mp3` — Kokoro `am_onyx`.
  - B00, B05, B09: updated 2026-09-12 (narration now says "620" not "619").
  - B01, B03, B11: unchanged from Sep-09 build.

## Compile

Command:

```bash
python3 runtime/scripts/compile.py \
  /Users/bear/Documents/CoWork/bear-textbooks/books/brutalist.art/youtube/brutalist/shorts/claude-liam-brutalist-command-scene-index-short \
  --height 3840 \
  --out /Users/bear/Documents/CoWork/bear-textbooks/books/brutalist.art/youtube/brutalist/shorts/claude-liam-brutalist-command-scene-index-short/exports/short
```

- Slots filled: 6/6 (`B00 B01 B03 B05 B09 B11` all VIDEO).
- Recompiled slots: B00, B05, B09 (changed inputs). B01/B03/B11 reused clips.
- Motion histogram: `code-cascade:2  type-on:1  hesitant-type:1
  artifact-in:1  outro-card:1`.
- Skin lint: two warnings (`B00: palette=claude but cold open is
  ClaudeComposerAsk916`; `B11: palette=claude but outro is
  ClaudeTitleOutro916`). Inherited from the parent vertical — portrait
  variants are the correct scenes for 9:16; landscape-name lint
  is expected.
- No `--review` flag (final pass without review overlays).

## Final container

- Path: `exports/short/claude-liam-brutalist-command-scene-index-short.mp4`
- Size: 7,540,855 bytes.
- Container duration: **105.625 s** (strictly < 180.0 s ✓).
- Video stream: h.264, 2160×3840, **105.625 s** (< 180.0 ✓).
- Audio stream: AAC, **105.625 s** (< 180.0 ✓).
- Video SHA-256: `f29cd53959a8e780af6092a25a8c4d2dfa6066b2f241e86298b7775091b50e16`.

## Duration audit

| Beat | render_duration_s | Cumulative end |
|------|------------------:|---------------:|
| B00  | 15.708            | 15.708 |
| B01  | 13.833            | 29.542 |
| B03  | 21.750            | 51.292 |
| B05  | 21.958            | 73.250 |
| B09  | 26.750            | 100.000 |
| B11  | 5.625             | **105.625** |

Container reads 105.625 s — matches to encoder precision. Headroom
under the strictly-under-180 cap: 74.375 s.

## Visual review

- Contact sheet at 2 fps: `_qc/contact_sheet.png` (SHA-256 recorded in
  `VISUAL-REVIEW.json`).
- Per-beat frames at 15 / 50 / 85 % of `render_duration_s`, saved and
  hashed to `_qc/beats/B{beat}-{pct}.png`. Every hash is recorded in
  `VISUAL-REVIEW.json`.
- Boundary joins sampled pre/post 0.20 s at B00-B01, B01-B03, B03-B05,
  B05-B09, B09-B11: clean cuts on cream/ink baseplate, no residual
  overlay from the outgoing beat.
- Mid-beat frames inspected:
  - **B00** — composer card, greeting "Bonjour, Liam", ask copy,
    runningText "reading Root.tsx…", three output lines
    (wraps/writes/law) and @HumanitariansAI folder chip visible.
  - **B01** — hesitant writer settled to "art scene-index / rewrites /
    the index."; caret parked after the period. No terracotta at 85%.
  - **B03** — ClaudeCodeBeat916 with `build_scene_index.py` header:
    "THE LAW: a scene is usable only if" and "REGISTERED IS THE ONLY
    TR[UTH]" visible (portrait clipping known). Spark line "Registered
    is the only truth." present at bottom.
  - **B05** — ClaudeCodeBeat916: "$ ./art scene-index" → "620
    renderable, 118 un[documented]", echo $? = 0, ls -l showing
    scenes.json (565983 bytes, Sep 12 08:10) and SCENE-DOC-TODO.md.
    Spark line "620 · 118 · 0. Two files on disk." ✓
  - **B09** — ClaudeVerdictArtifact916 — all 8 verdict rows visible
    inside SAFE916, including "no aliases — the dispatcher case at
    art:92-95 matches only the exact string 'scene-index'." ✓
  - **B11** — ClaudeTitleOutro916 — "Brutalist Command: art
    scene-index." and "@NikBearBrown" on dark baseplate (OUTRO-LOCK ✓).
- **Inherited portrait limitation** (parent SHOTLIST): `ClaudeCodeBeat916`
  does not word-wrap; longest source-comment lines in B03 and B05 clip
  horizontally. Essential text (THE LAW, REGISTERED IS THE ONLY TRUTH,
  620/118/0 output, art:92-95) remains legible. Not introduced by this
  Short.

## Audio review

- Full mono 16 kHz decode at `_qc/all.wav` (3,380,644 bytes).
- Silence detection at `-40 dB / ≥0.35 s` returns 12 gaps, all
  intra-narration or boundary joins:
  - 15.039–15.748 s (0.709 s) — B00-B01 join; matches `B01.lead_silence_s = 0.8`.
  - 23.615, 28.958, 35.635, 50.647, 56.356, 72.642, 77.411, 81.750, 95.018 s
    — all 0.44–0.69 s intra-narration pauses; no dropouts.
  - 99.230–100.058 s (0.828 s) — B09-B11 boundary (end of verdict narration).
  - 104.959–105.643 s (0.684 s) — normal end-of-audio tail.
- Max amplitude non-zero throughout. Kokoro `am_onyx` sounds intact.

## Blockers / majors

- **0 blockers · 0 majors.** The inherited portrait-code-clip limitation
  on B03/B05 is a documented minor at the parent level; essential quoted
  text remains legible and does not cross the mid-beat legibility threshold.

## Preservation

- Parent reel and its `vertical/` companion: untouched.
- Previous Short export preserved until recompile passed all checks.
- Toolkit `runtime/**` scripts: read-only; no edits except copying
  `math_layout_check.py` from the main toolkit into the workspace
  toolkit's `runtime/scripts/` (module was missing; needed by compile.py).
- No git push. No upload. No paid API. No credential access.

## Sandbox posture

- All compile / probe / ffmpeg operations ran inside the workspace and
  wrote only under `youtube/brutalist/shorts/claude-liam-brutalist-command-scene-index-short/`.
- `build_safety` guards remained active (`require_short_duration`,
  `validate_project`, `writable_path`, `atomic_json`, etc.).
