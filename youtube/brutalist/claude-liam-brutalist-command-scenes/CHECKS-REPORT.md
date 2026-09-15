# CHECKS-REPORT — landscape (16:9)

`claude-liam-brutalist-command-scenes.mp4` — 3840x2160 @ 30 fps, 256.29 s,
h.264 + AAC. Duration matches sum of measured per-beat MP3s (255.08 s narrated
+ conform padding).

## Gate F — factcheck

- `FACTCHECK.md` present, non-empty; every on-screen claim traces to `art` /
  `runtime/scripts/scene_search.py` / `runtime/remotion/src/scenes.json` in the
  isolated toolkit at revision `ba2d0e0f...`.
- `SOURCES.md` records the two primary source hashes matching
  `SOURCE-SNAPSHOT.json` (`9bb77a7c...` for `art`, `8ec4ece5...` for
  `scene_search.py`).

Pass.

## Gate V — visual QC (final_frame_check.py)

```
Frames sampled: 24  ·  BLOCKER: 0  ·  MAJOR: 0
Clean — no BLOCKER/MAJOR defects. ✓
```

Full report in `_qc/REPORT.md`; contact sheet at `_qc/contact_sheet.png`
(inspected via image-capable Read; see notes in `TYPECHECK.md`).

Pass.

## Audio decode

`ffprobe` confirms a single AAC stream in the final master, matching
per-beat MP3 SHA-256s in `exports/landscape/claude-liam-brutalist-command-scenes.verified.json`.
No beat is silent; narration decodes cleanly across every seam.

Pass.

## Compiler receipts

`exports/landscape/claude-liam-brutalist-command-scenes.verified.json` records:
- `status: ready` (automated export checks passed — human review pending)
- output SHA-256 `6bb15d47b2f32471288bae9e8a5af1a179e3d93e72d90bb4cc8510669a2821b3`
- 12 per-beat mp4 hashes + 12 per-beat mp3 hashes
- 256.29 s duration
- built at `2026-09-09T10:40:39.339580+00:00`

## Skin lint / motion histogram

The compiler noted:
- `code-cascade` carries 7/12 beats (~58%), over the ~40% pantry cap
  suggested by MOTION.md.
  - Decision: kept. The reel teaches a command whose output IS code and
    terminal, so `ClaudeCodeBeat` is the honest illustration per ILLUSTRATE
    LAW; converting body beats to another mechanic would replace the real
    evidence with wallpaper. Recorded, not suppressed.

No SKIN LINT warnings on the landscape cut.

## Known limitations

- The absent legacy `scripts/type_check.py` / `reference/type-spec.md` /
  `kerning` skill mean GATE T's automated typography pass could not run. The
  manual visual review documented in `TYPECHECK.md` fills that role.
- `ILLUSTRATIONS.md` (referenced by SKILL.md) is not shipped; the reel did
  not need a new illustration, so this is a documented gap, not a defect.

Every current runtime check that exists in this toolkit was run against the
episode and returned clean. Nothing was disabled or bypassed.

Human review is pending (Bear's viewing and any edits to `FEEDBACK.md`).
