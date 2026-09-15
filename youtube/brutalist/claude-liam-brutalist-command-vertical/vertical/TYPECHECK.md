# TYPECHECK.md — vertical (9:16)

## Scope

Same as landscape: `scripts/type_check.py`, `type-spec.md`, and the
kerning skill are not in this toolkit revision. This file does not
claim they passed — they were never invoked.

What DID run:

1. The compiler's Gate V — pixel-level checks on the compiled portrait
   MP4. Passed on second attempt with 0 BLOCKER / 0 MAJOR after the
   B01 BLUF was tightened; first-attempt BLOCKER (B01 left edge-bleed
   from "preserves beats" at fontSize 180) was fixed by shortening the
   phrases. See `CHECKS-REPORT.md`.
2. Manual visual typography review — 36 portrait frames read with the
   image-capable Read tool.

## Manual visual typography audit (portrait)

Portrait safe area: `SAFE916 = {x: 54, y: 96, r: 1026, b: 1824,
w: 972, h: 1728}` (1080×1920 design canvas, per `layout.ts`).

| Beat | Pattern | Typography check |
|---|---|---|
| B00 | ClaudeComposerAsk916 | greeting "Hola, Liam" serif fits centered; shortened ask fits inside the composer card at 3 wrapped lines; output lines in mono, all inside SAFE916. |
| B01 | BrutalistHesitantWriter916 | 4-line BLUF at fontSize 180 / lineSpacing 2.6; each line ≤ 11 chars; corrected sentence `vertical / preserves. / rewires it. / graphics.` sits comfortably inside SAFE916. Gate V clean on 2nd compile. |
| B02–B08 | ClaudeCodeBeat916 | code card portrait; short code lines fit; long file-path/import lines clip at the right edge of the card (MINOR — same treatment Ep 30 shipped with). Essential structural tokens visible in every frame. |
| B09 | ClaudeVerdictArtifact916 | 8 numbered lines wrap to 2 lines each in portrait; terracotta numerals; heading serif "art vertical — the whole surface"; all inside SAFE916. |
| B10 | ClaudeComposerAsk916 | shortened Your Turn prompt fits inside composer at 6 wrapped lines; output lines in mono, 2 wrapped lines each. |
| B11 | ClaudeTitleOutro916 | poster serif "Brutalist Command: art vertical." wraps to 3 lines in portrait; terracotta full-stop lands as a distinct accent; @NikBearBrown handle beneath. Matches OUTRO-LOCK. |

## Legibility

Every beat's text is legible at 4K portrait playback. No font falls
below 24 px effective. B00, B10, B11 fully inside SAFE916.

## Contrast

Same as landscape: warm ink on cream ~11:1; terracotta used as the
one accent per beat.

## MINOR limitations (accepted)

- Code beats' right-edge clipping on long lines (see CHECKS-REPORT).
  Ships as-is, mirroring Ep 30's accepted behavior.
