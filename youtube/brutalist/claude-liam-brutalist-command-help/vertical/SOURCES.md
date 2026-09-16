# SOURCES — Brutalist Command: art help (9:16 vertical companion)

Same primary source and demo captures as the landscape reel — see
`../SOURCES.md`. Every scene here is a **native portrait composition**, not a
cropped landscape master.

## Portrait-specific scene notes

- `ClaudeComposerAsk916` (B00, B10) — same schema as landscape; reflow lays
  the composer, greeting, and output lines down the tall column.
- `BrutalistHesitantWriter916` (B01) — same component as landscape; uses the
  design-box patch applied in this isolated toolkit
  (`runtime/remotion/src/scenes/BrutalistHesitantWriter.tsx`) so `min(w/1080,
  h/1920)` in portrait yields a full-size serif, not the shipped 0.5625
  landscape scale collapse. Uses a **portrait-specific 4-line stack** with a
  single trigger swap (skill → command) so the writer animation completes
  well before the 50% Gate V sample point.
- `ClaudeCodeBeat916` (B02–B08) — this workspace **registers a new
  1080×1920 composition** for `ClaudeCodeBeat` in `Root.tsx`; the component
  is unchanged (its layout is already viewport-relative). Registration only
  applies inside this workspace; the public toolkit stays untouched.
- `ClaudeVerdictArtifact916` (B09) — same schema as landscape; font sizes
  (`FONT_TITLE`, `FONT_HEADING`, `FONT_LINE`) bumped inside this workspace
  to fill portrait's tall safe area (was 0.018 / 0.024 / 0.017 of height,
  now 0.028 / 0.040 / 0.028) and `CARD_W` widened from 0.90 to 0.92 of
  frame width.
- `ClaudeTitleOutro916` (B11) — same locked outro (per `OUTRO-LOCK.md`);
  `@NikBearBrown` handle hardcoded, slug-seeded mascot, no subline.

## Human signatures / private assets

Not present. This is a technical command teardown built from the toolkit's
own `art` file; no fellow's video report is wrapped or excerpted here.
