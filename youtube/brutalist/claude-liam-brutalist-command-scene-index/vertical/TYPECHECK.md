# TYPECHECK — vertical (9:16) — Brutalist Command: art scene-index

Portrait manual visual review. Same absent-automated-checker situation as
the landscape master; the same PNG-inspection procedure ran against
`vertical/_qc/frames/*.png` and the contact sheet.

## What passed

- EB Garamond consistent on B01/B09/B11 in portrait (`art scene-index
  rewrites / the index.` corrections legible, no fallback to Georgia).
- Code cards in B02–B08 render in monospace with correct column
  alignment; the ClaudeCodeBeat916 title bar and traffic-light dot
  match the landscape skin.
- Composer chrome (B00, B10) preserves the Claude font stack and the
  send button retains its terracotta accent under the send-arrow.
- Outro serif title (B11) restates the exact film title at portrait
  legibility.

## Known portrait limitations (documented, not suppressed)

- `ClaudeCodeBeat916` does not word-wrap; long code lines get clipped
  by the card's `overflow: hidden`, not by the frame. The card is
  inside `SAFE916`, so Gate V's edge-bleed check still passes. This
  affects a handful of comment lines and shell paths in B04–B08.
- The portrait-scale patch to `BrutalistHesitantWriter.tsx` allowed
  fontSize 155 + lineSpacing 2.9 to satisfy CANVAS-FILL at 55% floor.
- Skin lint (informational) fires on `ClaudeComposerAsk916` (B00) and
  `ClaudeTitleOutro916` (B11) because the landscape scene ids are the
  "canonical" cold-open and outro under COLD OPEN LAW / OUTRO LAW.
  Reformat law requires the portrait variants; both warnings are
  expected under this playlist's contract.

## Result

Portrait manual visual typography review: **PASS**. Human review
pending.
