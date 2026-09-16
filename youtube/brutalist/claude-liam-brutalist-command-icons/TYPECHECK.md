# TYPECHECK — landscape

## Legacy checker status

- `scripts/type_check.py` — **NOT PRESENT** in this toolkit snapshot
  (revision `ba2d0e0f043f5b3b35a50d336e0fc66fbfecfc0c`). The
  `ai-explainer/SKILL.md` § "GATE T" refers to it, and the docs also mention
  `reference/type-spec.md` and a `skills/make/kerning/` skill; none of
  those files exist in the isolated toolkit.
- Consequence: the automated §8.1–§8.6 checks (min-size, overflow,
  contrast, kerning, no-wordy-card, golden strings) could not be run.
  This is honestly recorded here rather than claimed as a pass.

## Actual visual typography review

Performed by reading the final MP4's frames with the image-capable Read
tool, sampled at 15%/50%/85% of every beat via
`runtime/qc/final_frame_check.py` and the 4×6 contact sheet at
`_qc/contact_sheet.png`.

| Check | Result | Evidence |
|---|---|---|
| Min-size (~24px floor) | ✓ | Composer command 30px+ base, code beat body 24px base, artifact heading 46px, artifact lines 28px. All legible in the 4K contact sheet. |
| Overflow | ✓ | GATE V's `edge-bleed` check ran and returned 0 BLOCKERs on the final master. B01 iterated fontSize 250 → 340 (bleed) → 280 (clean) before ship. |
| Contrast | ✓ | Warm ink `#3D3929` on cream `#FAF9F5` (luminance separation ≈ 0.75); terracotta `#D97757` accent on cream separation ≈ 0.36. GATE V's low-contrast check returned 0 defects. |
| Kerning sanity | ✓ | Serif is EB Garamond (`runtime/fonts`), monospace is SF Mono. No Pango fallback observed on any frame; punctuation and mid-word gaps read clean in the contact sheet at all zoom levels. |
| No wordy card | ✓ | Every code-cascade beat is a real code artifact, not restyled prose. Verdict artifact has 7 short lines; each line ≤ 25 words. |
| Golden strings | ✓ | Segment titles, greeting, folder chip, outro title-restate all match the beat sheet verbatim (checked by rendering, no `drawtext` overlays). |

## Register-specific type discipline

- **Serif for headings and greetings**: EB Garamond throughout the
  composer, artifact, and outro cards.
- **UI sans for chrome**: system sans on chips and small labels.
- **Mono for code / terminal output**: SF Mono in every ClaudeCodeBeat,
  in the composer's typed command, and in the composer's output lines.
- **Terracotta discipline**: one accent moment per beat (the send button,
  the terminal red-lit dot, the spark line, the hesitant writer's about-
  to-be-deleted word). No beat carries two orange elements at once.

## Fills the canvas (FILL-THE-CANVAS LAW)

- GATE V's canvas-fill check (`FILL_MIN = 0.55`) returned 0 underfill
  defects on the final master. B09 iterated from 5 → 7 lines to clear
  the threshold.

## Conclusion

Visual typography passes on frame inspection and on GATE V's shape
checks. The legacy `type_check.py` was not available; this report
distinguishes that gap from the actual review, per the build contract.
Nothing was marked complete on a failure.
