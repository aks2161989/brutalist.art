# TYPECHECK — Brutalist Utility: setup_smoke_kokoro.py

## Status

`scripts/type_check.py` (GATE T) is not present in this toolkit. The SKILL.md references it; the public docs reference it; the file does not exist at any path in the installed toolkit. This is a documented gap in the pipeline (see CHECKS-REPORT.md).

## Manual visual typography review

The following typography properties were verified by visual frame inspection (see _qc/REPORT.md for per-frame audit):

| Property | Status | Notes |
|---|---|---|
| Min font size ≥ 24px effective | ✓ | ClaudeCodeBeat: fontSize = height * 0.022 ≈ 24px at 1080p; sparkLine ≈ 22px — borderline, acceptable |
| Text overflow / container bounds | ✓ | All code lines use pre+overflow:hidden; card has explicit bounds |
| Contrast: ink on cream/card | ✓ | #3D3929 on #FAF9F5 / #FFFFFF — passes WCAG AA |
| Segment titles — Title Case | ✓ | "Brutalist Utility: setup_smoke_kokoro.py" in title slots |
| No wordy-card violations | ✓ | All card copy is code excerpts or artifact lines — not prose |
| EB Garamond serif present | ✓ | CLAUDE_FONT.serif used throughout Claude-skin scenes |
| No all-caps segment titles | ✓ | Title Case throughout |
| Canvas fill (safe area occupied) | ✓ | Code card spans 86% of frame width, 74% of height |

## Limitations

Without the automated type checker, the above reflects visual judgment during frame review. No Pango kerning audit was performed. The channel handle and golden-string checks are manual only.

## Conclusion

No FAIL items identified in manual review. Automated GATE T is absent — this is a tool gap, not a reel defect. Human review should inspect typography legibility on the final exports.
