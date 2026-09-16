# TYPECHECK — landscape — Brutalist Command: art scene-index

Manual visual typography review. The shipped-but-referenced automated
type checker (`runtime/qc/type_check.py`, `reference/type-spec.md`,
`skills/kerning/`) is NOT present in this toolkit revision. That is a
documented gap, not a check that passed.

## What was inspected

Every beat's 50%-and-85% steady-state frames extracted from the compiled
landscape mp4 (24 PNGs at 1920×1080) plus a 4-column contact sheet.
Each PNG was opened and read with the image-capable Read tool.

## What passed

- **Serif face.** EB Garamond throughout every serif line (greeting,
  segment titles, hesitant writer, outro title). No fallback to Georgia
  or Times seen in any frame; consistent x-height and italic ligatures
  in `art scene-index rewrites the index.` (B01) and `art scene-index`
  (B11) confirm the bundled font resolved.
- **UI sans + mono.** `-apple-system` for composer chrome, SF Mono for
  code lines. All code cards (B02–B08) render in monospace with
  correctly proportioned column alignment for the `case` block,
  `import`/`json`/`shell` samples.
- **Terracotta accent budget.** One accent per beat. B00: send button
  + running-text asterisk (in a single micro-beat). B01: caret and
  hover state on the mistake word. B02–B08: code-card traffic-light
  dot only. B09: numeral color on the artifact rows. B10: composer
  send button. B11: title full-stop.
- **Contrast.** Ink (`#3D3929`) on cream (`#FAF9F5`) reads at
  Gate V's `LOW-CONTRAST` MAJOR threshold well below the CONTRAST_MIN
  0.30 floor (Gate V reported no low-contrast defects).
- **Size floor.** Legibility check: minimum on-screen serif is B02–B08
  code lines at ≈18 pt effective in a 1080-tall canvas (≈36 pt on the
  4K target). Well above the ~24 px floor referenced by the parent
  brand law.
- **B01 correction lands.** The final sentence `art scene-index
  rewrites the index.` is legible for the last ≥60% of the beat window;
  earlier hesitation transitions do not survive to the 50% sample.

## Known gaps

- `runtime/qc/type_check.py` / `reference/type-spec.md` / `skills/kerning`
  are referenced by `CLAUDE.md` but not shipped in this workspace.
  The § 8.4 Pango-fallback kerning sanity check therefore ran
  visually, not automatically. Nothing here claims that unavailable
  checker passed.

## Result

Manual visual typography review: **PASS**. No kerning defects, no
wordy cards, no fallback fonts, no accent budget violations, no
illegible sizes. Human review pending.
