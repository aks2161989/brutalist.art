# TYPECHECK — landscape 16:9

## Availability of the legacy checker

The public docs reference `scripts/type_check.py` and `reference/type-spec.md`
in a few places, but **neither exists in this isolated toolkit** (`ls scripts/`
and `ls reference/` confirm the absence). This is the same gap the sibling
`claude-liam-brutalist-skill-fellows` episode documented and not a new
regression. Rather than claim a missing checker passed, I ran a substitute
visual typography review.

## Substitute review (what was actually performed)

Basis: `CLAUDE-BRAND.md` (type, contrast, accent-law) +
`CLAUDE-CODE-VISUAL-QC-CHECK.md` (safe-area, overflow, mid-word truncation) +
Gate V's `final_frame_check.py` (FILL_MIN 0.55, contrast, no clipping).

Method: the image-capable Read tool opened each per-beat hero JPEG
(`_qc/heroes/B##_50.jpg`) at true 3840×2160 and each frame was inspected in
full for the properties below.

## Per-beat findings

| Beat | Type family | Weights on-screen | Safe-area OK | Contrast OK | Mid-word truncation | Result |
|---|---|---|---|---|---|---|
| B00 | serif (greeting) + UI sans (composer chrome + folder chip) + mono (result lines) | regular / regular / regular | ✅ | ✅ (>4.5:1) | none | pass |
| B01 | serif (hesitant-writer body) | regular | ✅ | ✅ | none | pass (after fontSize 148→162 bump) |
| B02 | serif (title) + UI sans (folder tree + callout) + mono (folder rows) | regular / regular / regular | ✅ | ✅ | none | pass |
| B03 | serif (title) + UI sans (labels) + mono (footer) | regular / regular / regular | ✅ | ✅ | none | pass |
| B04–B08 | serif (heading) + UI sans (body + verdict pill) + mono (quote block) | regular / regular / regular | ✅ | ✅ | none | pass (verdict pill negative-polarity on B08 verified) |
| B09 | serif (heading) + UI sans (numbered lines) | regular / regular | ✅ | ✅ | none | pass |
| B10 | serif (greeting) + UI sans (composer chrome) + mono (rubric lines) | regular / regular / regular | ✅ | ✅ | none | pass |
| B11 | serif (title) + serif (handle) | bold / regular | ✅ (background dark; text cream) | ✅ | none | pass |

## Palette-fidelity spot-checks

- Cream page (#FAF9F5 approximate) present on B00–B10; dark-ground on B11
  outro. ✅
- Warm ink (#3D3929 approximate) is the dominant text colour on the cream
  pages. ✅
- Terracotta (#D97757 approximate) confined to ONE accent per beat:
  - B00: send button + running-text spark
  - B01: none in final state (correction has completed; the terracotta
    flash was mid-beat)
  - B02: SKILL.md doctrine chip
  - B03: THE VIDEO node + arrow accents
  - B04–B08: quote-block ribbon + verdict pill
  - B09: numbered-line indices
  - B10: send button + running-text spark
  - B11: mascot + period after the title
  Accent-law respected across the reel. ✅

## Conclusion

No typography defect blocks the landscape pass. Every requested visual QC
check that has a runnable implementation in this isolated toolkit was RUN
(Gate V), and the substitutes for the absent legacy checkers were performed
by image-reading each hero frame directly. Human review pending.
