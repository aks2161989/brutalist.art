# CHECKS-REPORT — landscape (3840×2160)

## Re-build summary (run_id c4164e0244ae43b184b1671e8a80a477)

Source change: `fill_slates.py` sha256 changed from `b6afa2184…` (prior invocation) to `de9efcbdc…` (current). Changes in source:
- Type annotations added to all function signatures (`slate_resolves`, `find_slates`, `_truncate`, `stamp_slates`, `render_reel`)
- New `_topic(sheet: dict) -> str` helper added (defined but not called in current version)
- `find_slates()` now uses `sheet_path` intermediate variable and has an explicit docstring
- `stamp_slates()` uses `ensure_ascii=False` in the JSON write
- All line numbers shifted ~10 lines

Beats B04, B05, B06 re-rendered with updated code props. Beats B00-B03, B07-B11 unchanged from prior build (media files dated 2026-09-10 preserved).

## Video probe

```
ffprobe -select_streams v -show_entries stream=width,height,duration,codec_name,r_frame_rate
  → codec=h264  width=3840  height=2160  r_frame_rate=24/1  duration=237.0s
ffprobe -select_streams a -show_entries stream=codec_name,duration
  → codec=aac  duration=237.0s
```

Audio track is present and its duration matches the video track exactly.

## Gate V final frame check

`runtime/qc/final_frame_check.py` sampled 24 frames from the finished 4K master.

```
[gate-v] frames=24 BLOCKER=0 MAJOR=0
Clean — no BLOCKER/MAJOR defects. ✓
```

Contact sheet written to `_qc/contact_sheet.png` (SHA-256 `0dbd07156f8ccc82d9412aac77a718caee667b05ecc916e2a0f2c60f10199af8`) and read visually. Additional frames extracted at B04/B05/B06 50% marks and inspected with Read tool — all legible, within safe area, no overlap or clipping.

## Beat visual inspection (updated beats)

- **B04 (frame_78_44.png)**: `fill_slates.py:51-74` title. `slate_resolves(reel: Path, bid: str) -> bool:` and `find_slates(reel: Path):` with docstring, `sheet_path` variable, and existence check — all legible within safe area.
- **B05 (frame_101_48.png)**: `fill_slates.py:34-106` title. `_truncate(text: str, words: int = 12) -> str:`, `_topic(sheet: dict) -> str:  # unused in current version`, `stamp_slates(reel: Path, slates: list, sheet: dict):` — all type annotations correct and visible.
- **B06 (frame_123_51.png)**: `fill_slates.py:109-130` title. `render_reel(reel: Path, env: dict) -> list:` — both subprocess calls legible.

## Compile receipt

`exports/landscape/claude-liam-brutalist-runtime-fill-slates.mp4` (SHA-256 `d33a8d0c8caba5ca865dc8190bd28323b343654c17f83ad1762db8b2af9bcf4e`) compiled with `--height 2160 --force`. All 12/12 beats filled.

## Beat-sheet integrity

- Slug: `claude-liam-brutalist-runtime-fill-slates`
- Aspect: 16:9
- Beats: 12/12 filled (no unresolved slates)
- Total duration (audio-derived): 237.0s
- Beat sheet SHA-256: `36f9eed25aae05bb7ad9c4a4cee40aab0750557cc9612bee271f2f2d57625781`

## Motion histogram

`code-cascade:6  type-on:2  hesitant-type:1  phase-flow:1  artifact-in:1  outro-card:1`

Same as prior build. The 50% code-cascade cap warning is noted and accepted for this utility teardown episode (6 distinct function/branch teachings).

## Deliberately un-run demonstrations

- `fill_slates.py --apply` against a real user's `books/` directory — never executed.
- Upload/publish steps — never executed.
- No paid API calls.

## Known limitations

- The `_topic()` function added in current source is defined but not called in `fill_slates.py`. Its presence is shown in B05 with a `# unused in current version` comment. Noted in FACTCHECK.md.
- `docs/PIPELINE-SAFETY.md` and `docs/FELLOWS-SUBMISSION.md` checks run against toolkit copies; described in TYPECHECK.md.
