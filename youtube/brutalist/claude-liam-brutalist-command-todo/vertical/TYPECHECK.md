# TYPECHECK — vertical (9:16)

Run: `e66ff34b0ab34b038ee5d5d5b8cb13b4`

## The legacy checker

Same absent-checker gap as landscape: `scripts/type_check.py`,
`reference/type-spec.md`, kerning skill — none shipped in this toolkit.
Documented gap, not passed.

## What ran instead

`runtime/qc/final_frame_check.py` (Gate V) sampled 24 frames (mid + 85%
of every beat) and returned clean AFTER the two typography-related fixes
documented in `CHECKS-REPORT.md` (SparkLine portrait bump + B01 hesitant
writer restructure).

```
Frames sampled: 24  ·  BLOCKER: 0  ·  MAJOR: 0
```

## Manual visual review

Opened the vertical contact sheet plus six per-beat proof frames:

| Beat | Composition               | Notes                                                                                       |
|------|---------------------------|---------------------------------------------------------------------------------------------|
| B00  | ClaudeComposerAsk916      | Stacked native portrait — greeting, composer bar, folder chip, three answer lines all fit.  |
| B01  | BrutalistHesitantWriter916| After restructure: three big serif lines 'art todo / is a / receipt.' — 64% coverage.       |
| B02  | TodoPipeline916           | Vertical arrow chain: beat_sheet.json → ./art todo → three receipt cards. SparkLine cleared.|
| B06  | TodoMethods916            | Five-lane methods table with terracotta HUMAN chips. SparkLine sits close to METHOD header. |
| B09  | ClaudeVerdictArtifact916  | Five-line recap card — nothing clipped, generous vertical leading.                          |
| B11  | ClaudeTitleOutro916       | Title + @NikBearBrown handle (OUTRO-LOCK) + mascot — no glyph substitution.                 |

No BLOCKER, no MAJOR. Minor: B06's SparkLine crowds the METHOD eyebrow
in the portrait re-layout (side effect of the +60 bump). Recorded as an
aesthetic note; the safe-area check still passes.

## Conclusion

Vertical typography passes the current available checks (Gate V + manual
frame review). The legacy typography checker is unavailable; that gap is
acknowledged in `CHECKS-REPORT.md`.
