# TYPECHECK — vertical (9:16, 2160×3840)

The `scripts/type_check.py` referenced by `SKILL.md` is not shipped in this
toolkit revision. Manual visual typography review filled in.

Same standard as landscape (`CLAUDE-BRAND.md` §Type). Portrait-specific
adjustments:

## Portrait-specific font-size decisions

- **B01 BLUF (BrutalistHesitantWriter916):** fontSize 230 / lineSpacing 2.5 —
  reached after three tuning passes (see CHECKS-REPORT §Portrait iteration
  history). Three-line stanza `art final\nrenders\nonce.` fills ~68% of
  SAFE916 without edge-bleed; corrected sentence "art final / verifies /
  twice." legible and comfortably spaced.
- **B10 Your Turn (ClaudeComposerAsk916):** segment title shortened to
  "Verify your export against its receipt" so it fits one serif line at the
  portrait width. Prompt reduced from 5 numbered steps to 4 to keep the
  wrapped command inside SAFE916 vertically. Two output lines below the
  composer (not the landscape's three).

## Golden strings verified on portrait

- B00 composer: "Hei, Liam" — `_qc/frames-vertical/B00_50.png`.
- B01 BLUF: "art final / verifies / twice." (three lines) —
  `_qc/frames-vertical/B01_50.png`.
- B11 outro: title wraps to `Brutalist / Command: art / final.` (three
  lines) in portrait; terracotta period on `final`; `@NikBearBrown` handle
  beneath — `_qc/frames-vertical/B11_50.png`.

## Portrait-only limitations (documented)

- **Long monospace code lines truncate horizontally.** The
  `ClaudeCodeBeat916` component does not word-wrap. Frame-safe check passes
  (ink stays inside the card, which stays inside SAFE916). Fellows reading
  raw source should use the landscape master. Same as ep 29-32.

## Sanity checks

- **EDGE-BLEED** (Gate V rubric #1) — clean per Gate V's 24-frame audit.
- **CONTAINER OVERFLOW** — composer wraps naturally; verdict card lines wrap
  or are short by design; the code card's INSIDE is the only place lines
  clip (see limitation above).
- **BRAND BUG** — outro mascot inside SAFE916.
- **LEGIBILITY** — comment lines at `#8B8878` on cream — well above the WCAG
  AA floor for large text at the sizes rendered.

No FAILs from the manual review. Ready for Bear's human portrait review.
