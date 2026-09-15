# TYPECHECK.md — The anthropics Skill (vertical 2160×3840)

*Actual typography review versus the absent legacy checker.*

## The legacy checker

`scripts/type_check.py` / `reference/type-spec.md` are not present in
this toolkit snapshot. See landscape `TYPECHECK.md` for the same
disposition; not claimed as "passed".

## What was actually reviewed

All 22 Gate V steady-state frames plus the vertical contact sheet were
opened at 2160×3840 native and inspected under the same typographic
contract as the landscape review, adjusted for portrait-specific
concerns:

- **Native reflow, not a cropped landscape.** Every 916 composition
  used here is a native portrait registration (composition width 1080,
  height 1920). No mid-air crop. The composer chrome (B00, B09) stacks
  the greeting, ask, and output vertically; the outro (B10) column-lays
  the title with the handle underneath.
- **B01 scale fix.** The shipped `BrutalistHesitantWriter` collapsed to
  `scale = 0.5625` on a 1080×1920 canvas because
  `min(width/1920, height/1080)` locked to the landscape reference.
  The isolated toolkit copy adds a portrait branch —
  `isPortrait ? min(width/1080, height/1920) : min(width/1920, height/1080)`
  — restoring 1.0 scale on portrait so the serif fills legibly and
  covers the safe area. The change is scoped to the isolated scene
  file; the live library is not touched. See
  `runtime/remotion/src/scenes/BrutalistHesitantWriter.tsx` line 222.
- **B01 layout.** 6-line serif block at `fontSize: 195`,
  `lineSpacing: 1.2`, centred, no banner. Longest line
  ("anthropics", 10 chars) measures ≈ 1573 px on the 4K canvas — well
  under the 1944 px `SAFE916` inset. Ink bbox covers 63 % of the
  safe area at both 50 % and 85 % — comfortably above the 55 %
  canvas-fill law.
- **Weight and colour.** Same `CLAUDE.INK / PAGE / SPARK` palette as
  landscape. Gate V's `low-contrast` check reported no frames under
  the 0.30 luminance-separation floor.
- **Numerals + punctuation.** Same on-screen numbers as landscape
  ("142 lines" on B02, "Four modes" on B03). Verify Gate holds by
  construction. The outro period is the one terracotta glyph on B10.
- **Handle.** `@HumanitariansAI` on B00, B09, B10 — no
  `@NikBearBrown` string appears anywhere.
- **In-for-Bear signoff** on B10: `LIAM, IN FOR BEAR.` (verbatim).

## Divergence from landscape SHOTLIST

The vertical B01 shows a punctuation-free 6-line reflow of the same
misconception → correction ("channel" → "beat"). The landscape SHOTLIST
describes a two-sentence layout ("The anthropics skill is a tutorial
channel." → "It reads the artifact, not the docs."). The vertical
delivers the *same journalistic beat* — same trigger word, same
correction, same seed family — in a portrait-shaped layout so Gate V's
canvas-fill law is satisfied honestly, not by disabling the check.
Recorded here so the reviewer can see the divergence.

## Findings

No typographic defects, no accessibility failures, no brand drift, no
crop artefacts, no burned-in captions. Native full-length portrait
companion, not a shortened Short.

## Conclusion

Legacy checker absent — worked around by direct visual inspection.
Human review pending.
