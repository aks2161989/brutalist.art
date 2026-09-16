# TYPECHECK — vertical

## Legacy checker

`runtime/scripts/type_check.py` (referenced in some public docs) is not present in this isolated toolkit revision. This report cannot claim it ran.

## What this run actually verified about typography

Every rendered beat was decoded from the finished master `exports/vertical/claude-liam-brutalist-runtime-brand-variant-vertical.mp4` and the 4×4 contact sheet at `vertical/_qc/contact_sheet.png` was opened via the Read tool. Multiple B01 seeds (v3 → v11) were extracted at 50%/85% steady-state and inspected individually to converge on the portrait BLUF that clears the fill floor.

| item | verdict on vertical (2160×3840) |
|------|----------------------------------|
| body serif renders as Claude serif (Copernicus/Tiempos-family), never a fallback | ✅ |
| mono renders as Claude mono (Styrene-family fallback OK), never a system fallback | ✅ (B03/B04/B05/B06/B07/B08 code cascades in `ClaudeCodeBeat916`) |
| eyebrow topic strip renders in Claude display face, spaced letters, correct size | ✅ (B00, B02, B09, B10) |
| BLUF (B01) writer renders in serif at the scale-patched portrait size; terracotta accent on triggers; ink after correction | ✅ (v11 seed) |
| composer greeting renders in serif; command text renders in UI face; running indicator in mono spark | ✅ (B00, B10) |
| outro title (B11) renders in serif; handle in mono; mascot line beneath | ✅ |
| no burned-in captions, subtitle track, or karaoke overlay anywhere | ✅ |
| no ink outside SAFE916 (safe.x=108, safe.r=2052, safe.y=192, safe.b=3648 at 2160×3840) — `final_frame_check.py` reports 0 BLOCKER 0 MAJOR across 24 sampled frames | ✅ |
| minimum 55% safe-area fill on every 50%/85% sample — same check | ✅ |

## What was NOT verified here

- Character-level kerning tables were not compared against a golden reference; kerning was inspected visually only.
- Font subset embedding in the delivered MP4 is irrelevant (raster video), so no font-embedding check applies.
- Type geometry against an authoritative `reference/type-spec.md` file: that file is not present in this isolated toolkit revision either. Recorded as a gap in `vertical/CHECKS-REPORT.md`.

## Conclusion

Vertical typography passes the actual checks available in this runtime. The absent `type_check.py` and `type-spec.md` gaps are honestly recorded, not silently ignored. Human review pending.
