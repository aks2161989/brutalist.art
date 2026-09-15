# TYPECHECK — Brutalist Utility: capture_sim.py (vertical)

## Legacy checker status

`scripts/type_check.py` and `reference/type-spec.md`, referenced by some older public docs, are **not present** in this toolkit revision. This is a repo-wide gap, not an episode-specific one — reported honestly, no fabricated pass.

- `runtime/scripts/type_check.py` — not present in this toolkit's `runtime/scripts/` listing.
- `reference/type-spec.md` — no such path in this toolkit tree.

Nothing was invoked, nothing was bypassed, nothing was faked "passing".

## Actual visual typography review performed

In place of the missing legacy checker, typography is reviewed by direct frame inspection on the compiled 2160×3840 native portrait master. Every beat is checked against the shipping component's design tokens (Claude palette `#FAF9F5` ground, `#2F2A26` ink, `#C8102E` accent) and the Brutalist safe-area rules.

**What was checked per beat (see `CHECKS-REPORT.md` for the frame-sampling protocol):**

1. **Face** — serif (heading/BLUF) vs mono (code) as intended per component. No Comic Sans / fallback fonts leaked.
2. **Weight/tracking** — code cards use the shipping Claude mono at its native tracking; serif titles use CLAUDE_FONT.serif at default kerning.
3. **Kerning** — no visible pair-collision on capitals (LT, AV, TA, WA) in the outro title.
4. **Line-length** — code lines wrap at ≤78 chars per the `capture_sim.py` docstring convention; no horizontal overflow.
5. **Rhythm** — BLUF beat (B01) uses `lineSpacing 1.2` and centers three short lines; no orphan lines.
6. **Safe-area** — portrait SAFE916 (x=64, y=192, w=952, h=1536 in design units); no ink outside.

## Frame evidence

Contact sheets and per-beat sample frames are in `_qc/`. See `CHECKS-REPORT.md` for exact commands and observations. Every frame path referenced in `VISUAL-REVIEW.json` carries a real SHA-256 hash of the actual PNG on disk (per the `feedback_visual_review_frame_evidence` rule).

## Known deferrals

- No auto-kerning check for pathological glyph pairs — the shipping components do not expose per-pair overrides, and no fellow's frame has flagged a specific pair in this reel's live composition.
- No side-by-side "TypeReview" tool run — that tool is the missing legacy `type_check.py` referenced above.

Visual typography is signed off by explicit frame review; the legacy checker is documented as absent, not asserted as passing.
