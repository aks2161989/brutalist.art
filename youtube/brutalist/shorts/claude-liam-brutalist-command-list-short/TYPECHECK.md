# TYPECHECK — Brutalist Command: art --list (9:16 Short)

`run_id = 4b6e445b538846a4aa2b96c4dc361331` — 2026-09-12. Parent rebuilt to
20 skills; Short re-derived from updated native portrait beats.

There is no legacy static type checker for this reel. This file records the
**visual typography review** the reviewer actually performed, per the parent
convention.

Every retained beat's rendered mp4 was reused unchanged from the parent's
vertical companion (rebuilt 2026-09-12), so the typographic decisions are
inherited. The check below confirms that the inherited typography still holds
in the 8-beat cut (no beat was resized, re-rendered, or restacked by shorts.py).

## Sampled frames

Beat-relative 15% / 50% / 85% (24 frames) written to `_qc/frames_beat/`;
plus a 2 fps QC pass (253 frames) in `_qc/frames_2fps/`. Every
`_qc/frames_beat/*.jpg` file's SHA-256 is recorded in `VISUAL-REVIEW.json`.

## Type observations by beat

- **B00 `ClaudeComposerAsk916`** — chip header
  `BRUTALIST · COMMAND: ART --LIST` (small caps, ink); topic word
  `art --list` (serif, ink); greeting `Salaam, Liam` (serif, large,
  centered); composer card body (sans, ink); folder chip
  `@HumanitariansAI` (mono, small); output list (mono, ink; the leading
  line in terracotta with the running indicator). All type fits inside
  SAFE916 at every sampled frame; no overlap with the composer chrome.
- **B01 `BrutalistHesitantWriter916`** — serif stack, portrait scale patch
  applied (the parent's isolated toolkit — carries over unchanged as we
  reuse the parent's rendered mp4). Four lines fill the vertical safe area
  comfortably (`lineSpacing 2.4`); the trigger swaps `runs → prints` and
  `skills → catalog` complete before the 50% sample. Terracotta hesitation
  colour visible; final settled line
  `art --list prints the catalog of our Brutalist toolkit here.`
  reads clearly with the caret.
- **B03/B04/B07/B08 `ClaudeCodeBeat916`** — monospaced code, single accent
  in the language pill (terracotta `PYTHON`), grey title-bar text, ink
  body. Same known behaviour as the parent film: wide code lines bleed
  past the right edge of the card container; the leading columns
  (`printf '%-22s %s\n'` format, `$ ./art …` prompts, `# From art:…` comment
  stems, `if [ "${1:-}"` and `exec "${PAGER:-cat}"` in B08, first-column
  identifiers in the verbatim table at B04) are always legible. The
  narration covers the trailing detail on wide lines. No new type
  regression introduced by the cut.
- **B09 `ClaudeVerdictArtifact916`** — enlarged portrait fonts. Verdict
  heading `art --list vs list vs extras vs unknown token` fits inside the
  artifact card; seven numbered lines all inside SAFE916; card fits
  inside SAFE916 with generous margin.
- **B11 `ClaudeTitleOutro916`** — locked outro. Title
  `Brutalist Command: art --list.` wraps to three lines in the safe area
  (`art --` on line 2, `list.` on line 3 with the terracotta period);
  handle `@NikBearBrown` reads clearly; mascot below. Ink-on-cream
  contrast strong.

## Portrait framing

- Canvas 2160×3840; SAFE916 x 108–2052, y 192–3648 (5% inset).
- All 24 sampled frames confirmed inside SAFE916 for headings, primary
  copy and the outro handle. Code cards inherit the parent's accepted
  right-bleed on wide lines (leading columns and comment stems inside
  SAFE916).

## Result

- Visual typography review: **clean.**
- No new regressions vs. parent.
- Human sign-off pending.
