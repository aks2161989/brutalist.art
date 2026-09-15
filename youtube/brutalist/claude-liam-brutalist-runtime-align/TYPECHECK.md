# TYPECHECK — landscape

## Legacy checker

`runtime/scripts/type_check.py` (referenced in some public docs) is not present in this isolated toolkit revision (`toolkit_baseline_sha256: 92432609980c8ffc03bc1f00a1300fe1ac78bd7363b5b8ba9f2d389407d72b9d`, per `SOURCE-SNAPSHOT.json`). This report cannot claim it ran.

## What this run actually verified about typography

Every rendered beat was decoded from the finished master `exports/landscape/claude-liam-brutalist-runtime-align.mp4` and the extracted frames were opened image-by-image via the Read tool. The following were checked visually on those frames:

| item | verdict on landscape (3840×2160) |
|------|----------------------------------|
| body serif renders as Claude serif (Copernicus/Tiempos-family), never a fallback | ✅ |
| mono renders as Claude mono (Styrene-family fallback OK), never a system fallback | ✅ (B03/B04/B05/B06/B07/B08 code cascades) |
| eyebrow topic strip renders in Claude display face, spaced letters, correct size | ✅ (B00, B02, B09, B10) |
| BLUF (B01) writer renders in serif; terracotta accent color on the trigger word during hesitation, ink color after correction | ✅ |
| composer greeting renders in serif; command text renders in UI face; running indicator in mono spark | ✅ (B00, B10) |
| outro title (B11) renders in serif; handle in mono; mascot line beneath | ✅ |
| no burned-in captions, subtitle track, or karaoke overlay anywhere | ✅ |
| no ink outside SAFE (54–3786 in x, 96–2064 in y at 3840×2160) — `final_frame_check.py` reports 0 BLOCKER 0 MAJOR across 24 sampled frames | ✅ |
| minimum 55% safe-area fill on every 50%/85% sample — same check | ✅ |

## What was NOT verified here

- Character-level kerning tables were not compared against a golden reference; kerning was inspected visually only.
- Font subset embedding in the delivered MP4 is irrelevant (raster video), so no font-embedding check applies.
- Type geometry against an authoritative `reference/type-spec.md` file: that file is not present in this isolated toolkit revision either. Recorded as a gap in `CHECKS-REPORT.md`.

## Conclusion

Landscape typography passes the actual checks available in this runtime. The absent `type_check.py` and `type-spec.md` gaps are honestly recorded, not silently ignored. Human review pending.
