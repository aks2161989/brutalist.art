# TYPECHECK — vertical

## Legacy checker

`runtime/scripts/type_check.py` is not present in this isolated toolkit revision (`toolkit_baseline_sha256: 92432609980c8ffc03bc1f00a1300fe1ac78bd7363b5b8ba9f2d389407d72b9d`, per `SOURCE-SNAPSHOT.json`). This report cannot claim it ran.

## What this run actually verified about typography on portrait

Every rendered beat was decoded from the finished portrait master `exports/vertical/claude-liam-brutalist-runtime-align-vertical.mp4` and the extracted frames were opened image-by-image via the Read tool.

| item | verdict on portrait (2160×3840) |
|------|---------------------------------|
| Claude serif renders correctly (no fallback), same face used across B00 greeting, B01 writer, B02 heading, B09 verdict lines, B11 outro title | ✅ |
| Claude mono renders correctly for code beats (B03/B04/B05/B06/B07/B08) and for the composer footer/output lines | ✅ |
| Claude UI/display face renders correctly for the eyebrow topic strips (B00, B02, B09, B10) | ✅ |
| BLUF (B01) writer renders in serif with the terracotta accent on the hesitating trigger; final settled text reads `align dot py / times / the audio then / knows the / spoken words.` | ✅ |
| The portrait scale patch to `BrutalistHesitantWriter.tsx` (Root already contains the height>width branch) puts the design coord at 1080×1920, so fontSize/lineSpacing scale correctly instead of collapsing to 0.5625 | ✅ verified: patched code path at line 224 of the isolated toolkit's `BrutalistHesitantWriter.tsx` |
| No burned-in captions, subtitle track, or karaoke overlay anywhere | ✅ |
| No ink outside SAFE916 (54–1026 in x, 96–1824 in y at the 1080×1920 design coord; scaled 2× to physical for the 2160×3840 canvas) — `final_frame_check.py` reports 0 BLOCKER 0 MAJOR across 24 sampled frames | ✅ |
| Minimum 55% safe-area fill on every 50%/85% sample — same check | ✅ (was the previous-attempt blocker on B01; now passes) |

## What was NOT verified here

- Character-level kerning tables were not compared against a golden reference; kerning was inspected visually only.
- `reference/type-spec.md` is not present in this isolated toolkit — recorded as a gap in `CHECKS-REPORT.md`.

## Conclusion

Portrait typography passes the actual checks available in this runtime. The absent `type_check.py` and `type-spec.md` gaps are honestly recorded. Human review pending.
