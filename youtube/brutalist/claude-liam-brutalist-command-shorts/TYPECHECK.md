# TYPECHECK — landscape

The legacy `scripts/type_check.py` referenced in older docs is not present in
this toolkit. Instead I performed direct visual typography review of the
finished landscape master by opening a 3×4 sampled contact sheet
(`_qc/final-contact-sheet.png`, hash in `VISUAL-REVIEW.json`) with the
image-capable Read tool, and by inspecting per-beat frames extracted at 50%
and 85% of each beat's span (Gate V's own sampler wrote them into
`_qc/contact_sheet.png`).

## Font stack — as rendered

- **Serif** (`CLAUDE_FONT.serif` — EB Garamond bundled in `runtime/remotion/public/fonts/`)
  — outro title, hesitant-writer BLUF, spark lines under code cards, verdict heading.
  Cross-checked against the outro card: the `Brutalist Command: art shorts.`
  title is a clean serif with intact kerning at 4K; ligatures on `sh` and `rt`
  render correctly.
- **UI sans** (`CLAUDE_FONT.ui`) — Claude composer UI in B00 / B10, verdict
  bullets, folder chip. The `@HumanitariansAI` chip in the composer bar reads
  crisply; no glyph substitution.
- **Mono** (`CLAUDE_FONT.mono`) — code beats B02..B08 filename bar and code
  body. All punctuation renders correctly; unicode arrows (`→`, `←`) present
  in the compiler's status column render as expected.

## Contrast

Every beat rendered on the Claude cream ground (`#FAF9F5`) with ink
`CLAUDE.INK` (dark brown). Gate V's per-beat luminance check (`CONTRAST_MIN
= 0.30`) did not flag any beat. Independent read: the darker terracotta
accent (`CLAUDE.SPARK`) appears only on active traffic-light dots and the
spark line — never as body ink.

## Fill / margin (canvas-fill law)

Gate V's per-beat 50%/85% sample records `cover = bbox / (safe.w * safe.h)`.
The failing first attempt showed `edge-bleed left/right` on B01 (fontSize
240 with a 20-char line ran past safe.x/safe.r); tightening the text to 14
chars per line cleared the check. Every other beat cleared on the first
attempt at 55%+ fill.

## Kerning (informal)

Serif kerning on the outro title, on the two composer greetings (`Salam,
Liam`, `Your Turn`), and on the hesitant BLUF looks clean at 4K: the `l/i`,
`or/ts` and `Yo/ur` pairs sit at expected optical spacing. There is no
shipped kerning skill in this toolkit; this note is direct-look, not a
checker run.

## Not asserted

- Fine-grain font metrics were not measured programmatically; Gate V's ink
  bbox check is the closest available proxy and it passed.
- The `channel_title` PIL overlay was inspected on the first beat only —
  narrower than the burn-in exclude on landscape aspect, so Gate V correctly
  ignored it.
