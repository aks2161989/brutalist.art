# TYPECHECK.md — The deep-explainer Skill (vertical, run_id 9a0276f36c7f460da489b867130af37b)

## Referenced type checker

`scripts/type_check.py` and `reference/type-spec.md` are still absent
in this isolated toolkit — see the landscape-side TYPECHECK.md for the
`ls` confirmation. Nothing in this vertical build claims a pass from
a checker that is not present.

## What actually ran instead

- **runtime/qc/final_frame_check.py (Gate V, portrait mode)** samples
  30 frames from the 2160×3840 mp4 and enforces the portrait SAFE916
  inset (`x=54, y=96, r=1026, b=1824`). Log:
  `vertical/_qc/REPORT.md`.
  - Result: 0 BLOCKER, 0 MAJOR.
- **compile.py `verify_output`** decoded the candidate portrait mp4,
  confirmed exact 2160×3840 dimensions, positive audio duration and
  audio container presence, and atomic-wrote the master plus its
  `.verified.json` receipt.
- **Visual inspection of the portrait-only fixes.**
  - `BrutalistHesitantWriter916`: the patched
    `min(w/1080, h/1920)` scale means the design fontSize=140 renders
    at 140 CSS pixels on 1080-wide, not the 78.75 the old formula
    produced. Sampled at 5.5 s: all four lines are visible and inside
    safe.
  - `ClaudeVerdictArtifact916`: 6-line card fills the tall safe area
    without clipping.
  - `ClaudeComposerAsk916` (B00) verified after the
    `metadata.channel_title` overlay was removed — no more red bar
    below `safe.b`.

## Known cosmetic finding (recorded, not fabricated)

`SkillTeardownPipeline916` B04 shows the "Title outro" node
overlapping the footer note. Gate V's numeric bbox check did not
flag this because the ink lives inside safe; a human reviewer will
see the overlap. Flagged in CHECKS-REPORT.md.

## Conclusion

No fabricated pass from a missing checker. Gate V ran on the actual
final portrait mp4 and reported clean. Human viewing / typography
review remains required.
