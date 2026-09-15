# TYPECHECK — landscape (16:9)

Run: `e66ff34b0ab34b038ee5d5d5b8cb13b4`

## The legacy checker

The public docs reference `scripts/type_check.py`, `reference/type-spec.md`
and a kerning skill; none of those ship in this isolated toolkit. That
absence is a documented gap — the check is unavailable, not passed.
Nothing was faked or disabled to work around it.

## What ran instead

`runtime/qc/final_frame_check.py` (Gate V) is the current runtime check
that audits typography-adjacent defects (edge-bleed, canvas-fill,
low-contrast) frame-by-frame on the compiled master. It sampled 24 frames
(mid + 85% of every beat) and reported clean:

```
Frames sampled: 24  ·  BLOCKER: 0  ·  MAJOR: 0
```

## Manual visual review

I opened the contact sheet at `_qc/contact_sheet.png` and six per-beat
proof frames from the CURRENT master via the image-capable Read tool, and
looked for typography issues each frame at a time:

| Beat | Composition               | Notes                                                                                        |
|------|---------------------------|----------------------------------------------------------------------------------------------|
| B00  | ClaudeComposerAsk         | Serif eyebrow BRUTALIST · COMMAND, serif label 'art todo', 'Hola, Liam' greeting hierarchy readable. |
| B01  | BrutalistHesitantWriter   | Two-line serif 'art todo is a / receipt of shots' — kerning even, correction highlight clean. |
| B04  | TodoRun                   | Terminal SF Mono renders crisply at 30px; terracotta B0x/HUMAN row IDs distinguishable.       |
| B09  | ClaudeVerdictArtifact     | Artifact card sans/serif mix; five numbered lines properly leaded; nothing clipped.           |
| B10  | ClaudeComposerAsk (Your Turn) | Composer command wraps cleanly at one line; three-item grading rubric legible.            |
| B11  | ClaudeTitleOutro          | Poster serif title, terracotta period, sans handle, mascot — no glyph substitution.           |

Nothing looked substituted, clipped, or shimmering. No BLOCKER, no MAJOR.

## Conclusion

Landscape typography passes the current available checks (Gate V + manual
frame review). The legacy typography checker is unavailable; that is a
gap acknowledged in `CHECKS-REPORT.md`, not a claim of passage.
