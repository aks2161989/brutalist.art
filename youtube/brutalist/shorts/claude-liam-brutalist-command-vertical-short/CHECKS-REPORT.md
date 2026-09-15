# CHECKS-REPORT — Brutalist Command: art vertical — Short

## Deliverable

- **File:** `exports/short/claude-liam-brutalist-command-vertical-short.mp4`
- **SHA-256:** `4010be5045fc16eac5bc56483839802837d23e0b7fb2bb14754f9e2cb5a02c0a`
- **Container duration:** 128.916667 s (ffprobe)
- **Video stream duration:** 128.916667 s
- **Audio stream duration:** 128.916 s
- **Dimensions:** 2160 × 3840 (native portrait, no upscale, no crop)
- **Codecs:** h264 video, aac audio
- **Under 3:00 hard cap:** yes — 51.083 s of headroom
- **run_id:** `204e9c1d22ca42279d734e7efef06274`
- **rebuild_trigger:** Parent vertical re-rendered (run_id ac6edaa) — B02 code card corrected: art case line numbers updated from art:78-86 to art:102-107.

## Strategy

`whole-beat-cut` — no narration rewrite, no audio regeneration, no visual re-render.
The parent vertical's native portrait mp4s and mp3s were byte-copied by
`runtime/scripts/shorts.py` into the Short workspace. B02 now reflects the
corrected parent render (art:102-107 verbatim).

## Kept and dropped beats

- **Kept:** B00, B01, B02, B04, B07, B09, B11 (7 beats)
- **Dropped:** B03, B05, B06, B08, B10 (5 beats)

See `CUT-PLAN.json` for the per-drop reason and coherence review.

## Gates

| Gate | Status | Evidence |
|---|---|---|
| Under 3:00 (container) | PASS | ffprobe format.duration = 128.916667 |
| Under 3:00 (video stream) | PASS | ffprobe video duration = 128.916667 |
| Under 3:00 (audio stream) | PASS | ffprobe audio duration = 128.916 |
| Native 2160 × 3840 | PASS | ffprobe width/height |
| No burned-in captions | PASS | beat_sheet.captions = false; no drawtext (compile: "drawtext: no — PIL overlays") |
| Kokoro `am_onyx` voice | PASS | beat_sheet.voice = am_onyx |
| No endcard | PASS | `--no-endcard`; ends on B11 outro |
| No outro rewrite | PASS | `--no-outro-rewrite`; B11 mp3 byte-identical to parent |
| Independent copies (no symlinks) | PASS | `shutil.copy` in shorts.py (no `os.symlink`) |
| Compiler safety enabled | PASS | `runtime/scripts/compile.py` invoked with no bypass flags; PIL overlays only |
| Frame evidence with real SHA-256 | PASS | 21 frames extracted at beat-relative 15/50/85 %, all hashed in `VISUAL-REVIEW.json` under run_id `204e9c1d22ca42279d734e7efef06274`; B02 frames are new (corrected parent render) |
| AI frame-review record current | PASS | `VISUAL-REVIEW.json` `run_id`, `source_sha256`, `beat_sheet_sha256`, and `video_sha256` all match this invocation; `status:"pass"`, `reviewer_type:"ai"`, `blockers:0`, `majors:0` |
| Preserves the long unchanged | PASS | source tree `youtube/brutalist/claude-liam-brutalist-command-vertical/vertical/` untouched — read-only source |

## Compile output

```
[art] compiled B00  VIDEO    18.8s  ← B00.mp4
[art] compiled B01  VIDEO    17.4s  ← B01.mp4
[art] compiled B02  VIDEO    17.1s  ← B02.mp4
[art] compiled B04  VIDEO    19.4s  ← B04.mp4
[art] compiled B07  VIDEO    26.9s  ← B07.mp4
[art] compiled B09  VIDEO    23.8s  ← B09.mp4
[art] compiled B11  VIDEO     5.5s  ← B11.mp4
[art] motion histogram: code-cascade:3  type-on:1  hesitant-type:1  artifact-in:1  outro-card:1
[art] SKIN LINT: B00 ClaudeComposerAsk916 — COLD OPEN LAW wants ClaudeComposerAsk (inherited from parent, correct 916 pattern)
[art] SKIN LINT: B11 ClaudeTitleOutro916  — OUTRO LAW wants ClaudeTitleOutro  (inherited from parent, correct 916 pattern)
[art] slots: 7/7 filled
```

## Blockers / majors / minors

- **Blockers:** none
- **Majors:** none
- **Minors:** the two SKIN LINT lines above are inherited from the parent
  vertical build; they name-check the palette against the non-portrait
  pattern name, but the -916 suffix on both compositions is exactly what the
  portrait deliverable requires.

## Safety and provenance

- No files were written outside the assigned toolkit and reel.
- No uploads. No paid API calls. No publishing.
- Parent master, source beat sheet, and long export are read-only sources;
  their SHA-256s are recorded in `VISUAL-REVIEW.json`.
- `--recut`, `--rewrite-outro`, `--drop` on top of `--vertical` were not used.
- No `--review` fast-check was used as the final pass; the final pass is
  `runtime/scripts/compile.py … --height 3840`.
