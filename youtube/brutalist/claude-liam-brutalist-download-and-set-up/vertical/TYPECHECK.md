# TYPECHECK — Download Brutalist with Claude Code (vertical / portrait)

## Legacy checker status

`runtime/qc/type_check.py` is not present in this toolkit revision (same gap as landscape). Manual audit performed in its place.

## Portrait-specific typography audit

Compositions use `useVideoConfig()` and reflow off the aspect ratio; each component picks portrait sizes at render time. Rendered frames were sampled at 65 % of each beat's span (steady state) and Read as images.

| Rule | Check | Result |
|------|-------|--------|
| §8.1 min size (~24 px @ 1080) | Every display glyph ≥ 24 px at 1080 reference (≥ 48 px on 4K master). Body-copy sits at 26–34 px composition. | ✓ |
| §8.2 no container overflow | `DbcCloneTree916` rows wrap notes on a max-width container; `DbcDoctor916` dependency column wraps rather than clipping; `ClaudeComposerAsk916` prompt uses `whiteSpace: pre-wrap`. | ✓ |
| §8.3 contrast | Warm ink `#3D3929` on cream `#FAF9F5` (AAA). Dark terminal `#111815` with `#f2ecd6` text (AAA). | ✓ |
| §8.4 kerning | EB Garamond + SF Mono + system-ui all resolve on macOS render host — no Pango fallback observed. Letter-spacing set explicitly on eyebrow lines. | ✓ |
| §8.5 no wordy card | Every card has one headline + supporting evidence. Longest is B04 terminal, which stacks dependency notes but never runs a card-width paragraph. | ✓ |
| §8.6 golden strings | Verified on frames: "Download Brutalist" (B00), corrected "Downloading / Brutalist / is / just / a / git-clone." (B01), "One paste. Two commands." (B02), "A folder. Nothing outside it." (B03), "Green means ready." (B04), "Subscription. Optional key. Free pipeline." (B05), "What setup won't do." (B06), "Download Brutalist, in three lines." (B07), "Your Turn" (B08), "Download Brutalist with Claude Code." (B09). | ✓ |

## Portrait BLUF tuning

Per the "Gate V underfill" pattern (FILL_MIN 0.55), B01 portrait uses:
- 6 short lines
- fontSize 320 (portrait scale factor ≈ 0.56 → rendered ≈ 179 px)
- lineSpacing 1.35

This mirrors the shipped WIB portrait recipe and satisfies both the 55 % fill floor AND the safe-width constraint (longest word "Downloading" ≈ 906 px rendered inside 972 px safe width).

## Terracotta accent count per beat

Same as landscape — one focal accent per beat.

## Conclusion

No typographic defects in the ten rendered portrait beats. Legacy checker absence documented in landscape TYPECHECK.md.
