# TYPECHECK — vertical 9:16

## Runtime type checker (Gate T)

Not present in this toolkit snapshot; see landscape TYPECHECK.md for the same note.

## Visual typography review — portrait

Twelve stills from the 9:16 2160×3840 master reviewed:

- **EB Garamond serif** — headings, card titles, brand label. Scales by `height * N`
  so font sizes track portrait height correctly; no fixed-pixel font lock.
- **UI sans / mono** — ClaudeCodeBeat916 code block; ClaudeComposerAsk chrome.
- **Terracotta accent** — hesitation trigger (B01), send button (B00/B10), verdict
  bullets (B09), outro title period (B11). One accent color only.
- **No overflow** — Gate-V clean on 24 portrait frames; safe zone SAFE916 respected.

## Portrait-specific typography notes

- **B01 BrutalistHesitantWriter916**: `lineSpacing 3.4` — body serif large enough to
  read on phone screen; not so large that 6 lines overflow the frame.
- **B06 ClaudeCodeBeat916**: adaptive `codeFontSize = min(baseFontSize, cardContentW /
  (maxLineLen * 0.62))` — long bash lines shrink to fit portrait card width.
- **B09 ClaudeVerdictArtifact916**: `FONT_HEADING = height * 0.024` ≈ 92px at 3840px.
  Card occupies 90% of portrait width; heading and lines readable at phone scale.

## §8 checks — portrait

- **§8.1 min-size** — body copy at `height * 0.017` ≈ 65px at 3840px height; legible
  at portrait phone display sizes.
- **§8.2 overflow** — 0 BLOCKERs in Gate V; no ink outside SAFE916 on any sampled frame.
