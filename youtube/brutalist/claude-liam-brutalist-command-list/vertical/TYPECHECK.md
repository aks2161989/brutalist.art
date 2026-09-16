# TYPECHECK — Brutalist Command: art --list (9:16 vertical companion)

Invocation `run_id = 8350d76b75754d93a802dcfb825c4478` — 2026-09-09.

## The legacy `scripts/type_check.py` (GATE T)

Not present in this workspace — same finding as the landscape
TYPECHECK.md. This file records the visual typography review I ran
against the same rubric on the portrait build.

## What I actually inspected

- `_qc/contact_sheet.png` — Gate V's 24-frame sample.
- Individual frames for B00, B01, B04, B07, B09, B10, B11 (extracted
  during authoring for coverage measurement).

## Rubric (portrait — SAFE916)

| Rule | Check | Result |
|---|---|---|
| §8.1 min-size | All portrait scenes render at fontSizes tied to `height` or the patched design scale — text at 2160×3840 stays well above the 24 px effective legibility floor. B01 hesitant writer at fontSize 130 renders at 260 px per glyph. | PASS |
| §8.2 overflow | Every beat's ink bbox sits inside SAFE916 (2160×3840 output: `x ∈ [108, 2052]`, `y ∈ [192, 3648]`). B01's 5-line stack at lineSpacing 2.4 spans ~2400 vertical inside the 3456 safe height; ClaudeCodeBeat916 card fits inside the frame; verdict card fills ~90% width. Gate V ran to 0 BLOCKER. | PASS |
| §8.3 contrast | Same ink/cream/terracotta tokens as landscape; contrast preserved. | PASS |
| §8.4 kerning sanity | Same EB Garamond bundled locally; no missing glyphs; em-dash renders correctly. | PASS |
| §8.5 no wordy card | B01 narration lengthened to accommodate the portrait BLUF (~55 words, ~16s); still one breath of stakes. Body beats keep the same 45–70 word budget as landscape. | PASS |
| §8.6 golden strings | Outro title `Brutalist Command: art --list.` and the hardcoded `@NikBearBrown` handle preserved. Composer folder chip reads `@HumanitariansAI`. Verbatim source strings unchanged from landscape. | PASS |

## Non-runtime findings

- **Skin lint** (`compile.py`) — two WARN entries:
  - `B00: palette=claude but the cold open is 'ClaudeComposerAsk916'`
  - `B11: palette=claude but the outro is 'ClaudeTitleOutro916'`

  Both are expected for a portrait build using the native `-916` variants;
  the same warnings appear on other published `claude-liam-*/vertical`
  reels in this repo. No action; documented in CHECKS-REPORT.md.

## Nothing was faked

No missing checker was pretended to run. This is a hand audit against the
same rubric.
