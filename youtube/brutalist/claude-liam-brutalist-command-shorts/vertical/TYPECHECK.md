# TYPECHECK — vertical

Same font stack as landscape (EB Garamond serif, Claude UI sans, Claude
mono). Direct visual review of `_qc/final-contact-sheet.png` opened with the
image-capable Read tool.

## What is different from landscape

- **B00 composer** — the `command` bubble is shorter (fits portrait width);
  the `output[]` list has two lines instead of three so the whole card sits
  above `safe.b`.
- **B01 hesitant BLUF** — 4 lines instead of 2, `fontSize: 180`,
  `lineSpacing: 2.6`. Serif kerning still clean at 4K portrait. Widest line
  after the trigger swap is `and rewires` at 12 characters.
- **B02..B08 code cards** — same content, wrapped inside the portrait-native
  code card. Font size scales with `height * 0.022`, so at 3840 tall each
  code line is ~85 px — the mono font remains legible when the frame is
  read at typical Shorts viewer distance.
- **B10 Your Turn** — command trimmed to a shorter paste-ready prompt; two
  output lines summarize the expected outcome.
- **B11 outro** — `ClaudeTitleOutro916`. Title `Brutalist Command: art
  shorts.` renders serif on a single line; handle `@NikBearBrown` renders
  below (OUTRO-LOCK; playlist adaptation is on the composer chip only).

## Kerning (informal)

The portrait BLUF `art shorts / drops beats / and rewires / graphics.`
serif reads clean at 4K portrait; no crowding on the wide `sh` cluster;
`ea` in `beats` and `rew` in `rewires` show typical Garamond optical
spacing.

## Fill / margin

Gate V passed 0/0. Manual bbox measurement on midpoint samples:
- B00: y=[199, 1785] of 1920, fill ≈ 85% of safe area.
- B01: y=[175, 1751] of 1920, fill ≈ 73%.
- B10: y=[199, 1785] of 1920, fill ≈ 85%.

## Not asserted

- No shipped kerning checker was run — direct visual only.
- `metadata.channel_title` was intentionally omitted from the vertical
  metadata (per the portrait-bleed rule), so no PIL overlay is added on the
  first beat. The composer chip carries the channel identity instead.
