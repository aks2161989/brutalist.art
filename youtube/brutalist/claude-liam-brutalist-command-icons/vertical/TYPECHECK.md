# TYPECHECK — vertical (9:16)

Same doctrine and gaps as landscape (see landscape TYPECHECK.md for the
full breakdown of the missing `scripts/type_check.py` and the actual
visual review).

## Portrait-specific notes

- **BLUF (B01) scaling patch** — the shipped `BrutalistHesitantWriter.tsx`
  computes `const scale = Math.min(width/1920, height/1080)` which
  collapses to 0.5625 on 1080×1920 portrait, halving every geometry
  value. The patched form (documented in memory
  `feedback_brutalist_hesitant_writer_portrait_scale_patch`) selects
  the correct design box per aspect:
  ```ts
  const scale = height > width
    ? Math.min(width / 1080, height / 1920)
    : Math.min(width / 1920, height / 1080);
  ```
  Landscape behaviour is unchanged (still picks `Math.min(width/1920, height/1080)`).
- Post-patch, the portrait BLUF with fontSize 170 + lineSpacing 2.7
  clears FILL_MIN 0.55 cleanly.

## Type discipline in portrait

- Same font stack as landscape: EB Garamond (serif), UI sans, SF Mono.
- Composer prompt (B10) uses a SHORTER on-screen typed text than the
  landscape so it fits inside the narrower composer card without
  overflow. The NARRATION is unchanged (same MP3, byte-identical
  duration).
- Segment titles fit inside SAFE916 (x 54–1026); B10 segment was
  shortened from "Audit art icons on your own idea" to "Audit art
  icons" to satisfy the constraint.
- Code cards reflow tighter on portrait; text stays legible at 4K
  (2160×3840). Verdict artifact stacks 7 lines cleanly.

## Conclusion

Visual typography passes on all 24 sampled portrait frames. GATE V:
0 BLOCKER, 0 MAJOR. Legacy `type_check.py` remains absent; that gap is
documented, not silently claimed as a pass.
