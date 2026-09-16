# Checks Report — Brutalist Utility: provenance.py (Portrait 9:16)

Episode slug: `claude-liam-brutalist-runtime-provenance-vertical`
Run ID: `6c9fce7b6b2a41529b1dea2b81476551` (re-verified; previous passing run: `7cc9e1701cb44aacaccbdc2fde05d86e`)
Date: 2026-09-14

## Dimensions

```
ffprobe: width=2160, height=3840 (h264 + aac 48000Hz stereo)
```

Pass — native 4K 9:16.

## Beat lint

```
python3 runtime/qc/beat_lint.py vertical/beat_sheet.json
[beat-lint] clean — beat mix OK
```

Pass.

## Build completeness

- Beats filled: 12/12
- Slates: none
- Outro narration: "Brutalist Utility — provenance dot py. Liam, in for Bear." ✓

## Gate V — final_frame_check.py

```
python3 runtime/qc/final_frame_check.py <vertical> --mp4 exports/vertical/<slug>-vertical.mp4 --sheet vertical/beat_sheet.json
[gate-v] frames=24 BLOCKER=0 MAJOR=0 → vertical/_qc/REPORT.md
```

Re-run for invocation 6c9fce7b: same result. Pass. Contact sheet: `vertical/_qc/contact_sheet.png`

## Fresh frame inspection (run 6c9fce7b)

Frames extracted from current portrait MP4 (sha256: `a5e41c71...`):
- `vertical/_qc/run-6c9fce7b/frame_B00_mid.png` — B00 @ 6.96s: ClaudeComposerAsk916, @HumanitariansAI, AUDIO/VIDEO/SLOTS ✓
- `vertical/_qc/run-6c9fce7b/frame_B09_mid.png` — B09 @ 228.78s: 8-point verdict list, all text within safe area ✓
- `vertical/_qc/run-6c9fce7b/frame_B11_outro.png` — B11 @ 268.08s: "Brutalist Utility: provenance.py." @HumanitariansAI dark olive ✓

## Channel handle fix (B00, B10)

Initial render used default `folderLabel='@NikBearBrown'` in ClaudeComposerAsk916 (prop was omitted from beat sheet).
Repair: added `"folderLabel": "@HumanitariansAI"` to both B00 and B10 in `vertical/beat_sheet.json`.
Re-rendered B00 and B10 with C chrome wrapper. Re-compiled vertical.
Visual verification: portrait frames at 6.96s (B00) and 253.54s (B10) confirm `@HumanitariansAI`.

## Known warnings (not defects)

- Skin lint B00: `ClaudeComposerAsk916` vs `ClaudeComposerAsk` — 916 suffix is the native portrait variant, expected.
- Skin lint B11: `HaiTitleOutro916` vs `ClaudeTitleOutro` — native portrait HAI variant, expected.
- Remotion pantry cap: 100% remotion beats — architectural note only.

## Conclusion

Portrait export passes all applicable automated checks. Gate V: 0/0. Human review pending.
