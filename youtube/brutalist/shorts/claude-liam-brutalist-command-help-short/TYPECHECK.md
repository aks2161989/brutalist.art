# TYPECHECK — Brutalist Command: art help (9:16 Short)

There is no legacy static type checker for this reel. This file records the
**visual typography review** the reviewer actually performed, per the parent
convention.

Every retained beat's rendered mp4 was reused unchanged from the parent's
vertical companion, so the typographic decisions are inherited. The check
below confirms that the inherited typography still holds in the 8-beat cut
(no beat was resized, re-rendered, or restacked by shorts.py).

## Sampled frames

Beat-relative 15% / 50% / 85% (24 frames) written to `_qc/frames_beat/`.
Every file's SHA-256 is recorded in `VISUAL-REVIEW.json`.

## Type observations by beat

- **B00 `ClaudeComposerAsk916`** — chip header "BRUTALIST · COMMAND: ART
  HELP" (small caps, ink); topic word `art help` (serif, ink);
  greeting "Namaste, Liam" (serif, large, centered); composer card body
  (sans, ink); folder chip `@HumanitariansAI` (mono, small); output list
  (mono, ink; the leading line in terracotta). All type fits inside
  SAFE916 at every sampled frame. No overlap with the composer chrome.
- **B01 `BrutalistHesitantWriter916`** — serif stack, portrait scale patch
  applied (parent's isolated toolkit — carries over as we reuse the
  parent's rendered mp4 unchanged). Font size 210, lineSpacing 1.55.
  Four lines fill the vertical safe area comfortably; the trigger swap
  `skill` → `command` completes before the 50% sample. Terracotta hesitation
  colour visible; final "command." reads clearly with the caret.
- **B03/B04/B05/B06 `ClaudeCodeBeat916`** — monospaced code, single accent
  in the language pill (terracotta `PYTHON`), grey title-bar text, ink
  body. Same known behaviour as the parent film: wide code lines bleed
  past the right edge of the card container; the leading columns
  (commands, comment stems) are always legible. Narration carries the
  trailing detail on wide lines. No new type regression.
- **B09 `ClaudeVerdictArtifact916`** — enlarged portrait fonts (`FONT_TITLE
  0.028`, `FONT_HEADING 0.040`, `FONT_LINE 0.028` of frame height per
  parent's SOURCES.md). Four numbered lines fit inside the artifact card;
  card fits inside SAFE916.
- **B11 `ClaudeTitleOutro916`** — locked outro. Title "Brutalist Command:
  art help." wraps to three lines in the safe area; handle `@NikBearBrown`
  reads clearly; mascot below. Ink-on-dark contrast strong.

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
