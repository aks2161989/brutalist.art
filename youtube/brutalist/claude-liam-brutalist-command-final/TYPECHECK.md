# TYPECHECK — landscape (16:9, 3840×2160)

The `scripts/type_check.py` referenced by `skills/make/ai-explainer/SKILL.md`
is not shipped in this toolkit revision (`.repoloop/workspaces/…/toolkit/`
lacks it and no `TYPECHECK.md` template ships with the skill). This file
records the manual visual typography review that filled in.

Standard applied: `CLAUDE-BRAND.md` §Type + `ai-explainer` SKILL.md §Hard
rules — serif for greetings + segment titles (EB Garamond as the effective
default), UI sans for chrome, mono for terminal / code lines only. Segment
titles Title Case. Legibility floor ~24px effective; 4K master gives us
comfortable headroom.

## Per-beat visual typography review

- **B00** — ClaudeComposerAsk: eyebrow `BRUTALIST · COMMAND: ART FINAL` in UI sans (uppercase, letter-spacing per component). Segment title `art final` in Claude serif. Greeting `Hei, Liam` in Claude serif above the composer. Ask body in the composer's mono / UI mix per component defaults. Folder chip `@HumanitariansAI` sits under the composer inside SAFE. All type comfortably legible at 4K playback size.
- **B01** — BrutalistHesitantWriter: 2-line serif stanza at fontSize 240 (design units) with lineSpacing 2.6. Ink `#3D3929`, accent `#D97757` (applied only to doomed tokens `renders`, `once`). Final settled sentence "art final / verifies twice." legible with generous negative space.
- **B02–B08** — ClaudeCodeBeat: white code card on cream. Filename chip in mono `#8B8878`. Traffic-light dots — the active one is terracotta. Code lines in mono, comment lines in the muted `#8B8878`. Lines are ~24-28px effective on 2160 tall canvas; every line legible without magnification. Card boundary respected — code stays inside padding, no overflow past card edges.
- **B09** — ClaudeVerdictArtifact: card heading in serif; six numbered lines in UI sans with terracotta line numbers; all six visible and legible without scroll. `Verdict` label in the card's top-left chip.
- **B10** — ClaudeComposerAsk (Your Turn): eyebrow `BRUTALIST · YOUR TURN` in UI sans. Segment title in serif. `Your Turn` greeting in serif. Long prompt wraps naturally inside the composer's `maxWidth` — no overflow. Folder chip `@HumanitariansAI`.
- **B11** — ClaudeTitleOutro: title `Brutalist Command: art final.` in Claude serif with the terracotta period per OUTRO-LOCK. `@NikBearBrown` handle beneath in serif. Mascot at fixed pixel-art size. All type inside SAFE.

## Sanity checks against Gate V's typography-adjacent rules

- **EDGE-BLEED** (Gate V rubric #1) — all beats clean per Gate V's 24-frame audit.
- **CONTAINER OVERFLOW** (rubric #3) — the composer input field, code card, and verdict card all size to their content or wrap; no visible overflow.
- **BRAND BUG** (rubric #7) — the outro mascot is inside SAFE; no small corner
  bug is required on inner beats (this toolkit's Claude cut does not carry an
  NBB corner bug on inner beats, per how ep 29-32 shipped).
- **LEGIBILITY** (rubric #6) — every text element resolves at expected size.
  Comment lines in the code beats are the softest color (`#8B8878` on cream
  `#FAF9F5`); contrast is well above WCAG AA floor for large text (>18pt eq).

## Golden strings verified on screen

- B00 composer: greeting "Hei, Liam" verified via `_qc/frames-landscape/B00_50.png`.
- B01 BLUF: final sentence "art final / verifies twice." verified via
  `_qc/frames-landscape/B01_50.png`.
- B02 code card title `art:90-95 — one branch, two paths` verified via
  `_qc/frames-landscape/B02_50.png`.
- B11 outro: title text "Brutalist Command: art final." + handle
  `@NikBearBrown` verified via `_qc/frames-landscape/B11_50.png`.

No FAILs. No unrenderable fonts. Ready for Bear's human review.
