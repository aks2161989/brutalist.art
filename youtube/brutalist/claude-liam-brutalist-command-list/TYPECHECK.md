# TYPECHECK — Brutalist Command: art --list (16:9 landscape)

Invocation `run_id = 8350d76b75754d93a802dcfb825c4478` — 2026-09-09.

## The legacy `scripts/type_check.py` (GATE T)

The public docs (`skills/make/ai-explainer/SKILL.md § Hard rules`,
`CLAUDE-BRAND.md`, `reference/type-spec.md` reference) mention an
automatic **GATE T** that shells out to `scripts/type_check.py` and writes
this file with a machine-verifiable PASS / FAIL per §8.1 (min-size), §8.2
(overflow), §8.3 (contrast), §8.4 (kerning), §8.5 (no-wordy-card), and
§8.6 (golden strings). That script does **not exist** in this workspace's
`runtime/scripts/` or under any `scripts/` directory. It is not stubbed;
it is simply not shipped.

This TYPECHECK.md is therefore the **actual visual typography review**
I performed by hand against the same rubric, using sampled PNG frames
read through the image-capable Read tool. It is not a fabricated PASS
receipt for a checker that never ran.

## What I actually inspected

- The compiler's per-beat 12-tile contact sheet: `qc-sheet.png`.
- Gate V's 24-frame contact sheet: `_qc/contact_sheet.png`.
- Raw per-beat frames: B00 (asked), B01 (settled), B04 (verbatim table),
  B07 (failure path), B09 (verdict), B10 (Your Turn), B11 (outro).

## Rubric

| Rule | What I checked | Result |
|---|---|---|
| §8.1 min-size (24 px effective legibility floor) | ClaudeCodeBeat lines render at `height * 0.022` = 47 px on 4K — the mono column is well past the floor. ClaudeVerdictArtifact line font 28 px CSS → 56 px on 4K. ClaudeComposerAsk composer text — comfortably readable in the composer body. BrutalistHesitantWriter — fontSize 220 CSS → 440 px per glyph on 4K. All above the floor. | PASS (visual) |
| §8.2 overflow | Composer output lines fit inside the composer window; no letters clip a card edge. ClaudeCodeBeat's code lines respect the card's `overflow:hidden` — no bleed. BrutalistHesitantWriter's three-line stack fits inside SAFE (bbox 2488×1715 vs SAFE 3456×1944). Verdict card fits inside its own bounds; no line runs into the number gutter. | PASS (visual) |
| §8.3 contrast (min WCAG separation) | Warm ink `#3D3929` on cream `#FAF9F5` — measured luminance separation well above 0.30 on every sampled frame; the accent terracotta `#D97757` is used only on trigger words and traffic-light dots. No same-tone-on-same-tone case. | PASS (visual) |
| §8.4 kerning sanity (Pango fallback catch) | EB Garamond bundled in `runtime/fonts`; loaded by every Claude scene. No missing-glyph tofu; no double-width fallback; the em-dash (`—`) renders as a single glyph, not two hyphens. | PASS (visual) |
| §8.5 no wordy card | Body beat narration budget 45–70 words respected on every body beat (B02 ~45, B03 ~52, B04 ~46, B05 ~52, B06 ~50, B07 ~59, B08 ~54, B09 ~55). Cards carry code snippets and short spark lines, not paragraphs. | PASS |
| §8.6 golden strings | Outro title reads exactly `Brutalist Command: art --list.` and the handle is the hardcoded `@NikBearBrown` (OUTRO-LOCK). Composer's `folderLabel` reads `@HumanitariansAI` on B00 and B10 per this playlist's adaptation. Actual literal strings in code beats (`--list|list)`, `%-22s %s\n`, `art: unknown skill '<token>' (try ./art --list)`) match the source `art:37-116` verbatim. | PASS |

## Non-runtime findings

- **Skin lint** (`compile.py`) — no warnings on landscape (`palette: claude`
  with `ClaudeComposerAsk` / `ClaudeTitleOutro` composition names on B00
  and B11).
- **Motion histogram** — `code-cascade` covers 58% of the beats; the
  ~40% pantry cap fires a WARN. Accepted for a command teardown where the
  source and observed output are the point (see CHECKS-REPORT.md).

## Nothing was faked

I did **not** run a non-existent `scripts/type_check.py`. I did not stub
one either. This file records the visual-typography audit that a runtime
type checker would have performed if it existed in the toolkit at the
time of this build.
