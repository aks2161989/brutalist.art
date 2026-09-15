# TYPECHECK — Short 9:16

No source code was modified in this derivative. The Short is a whole-beat cut of
the parent vertical companion's finished 2160×3840 Remotion renders; every kept
beat's mp4 was copied unchanged. No Root.tsx edits, no schema changes, no new
compositions were required for this build.

## Schema / renderer invariants

- Root.tsx already registers the 916 compositions used by the parent vertical
  companion (verified by `shorts.py`: every kept beat's `native portrait reused
  unchanged` line, no ONDA CHECK rewire or blocked entry). No re-render needed,
  so no zod-schema mismatch surface for this Short.
- `beat_sheet.json` passes `validate_project` inside `shorts.py`
  (`short_validation.status = ready`, empty errors list).
- `runtime/scripts/build_safety.py` enforces the Shorts cap at plan time
  (`SHORTS_CAP_S = 180`); the planner reported 140.8 s and printed `OK`.

## Runtime versions in use

- ffmpeg / ffprobe: shipping system binaries (used for probe + audio decode +
  frame extraction only; no re-encode of any beat).
- Python 3 with Pillow (unused this run — no PNG endcard, `--no-endcard`).
- Node/Remotion: not invoked — every kept beat's portrait render was reused
  from the parent vertical companion.

## Result

No type errors. No new code compiled. No schema drift. The only writes to the
toolkit/reel are the derivative beat sheet, the derivative mp4, the QC report,
the extracted evidence frames and this documentation set.
