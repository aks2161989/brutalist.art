# TYPECHECK.md — The sri-explainer Skill (landscape)

## What this file is

A record of the visual-typography review that runs in place of the legacy
`scripts/type_check.py` referenced in some older docs. That legacy checker
is NOT present in this isolated toolkit; claiming it passed would be
false. This file documents the actual review that WAS performed.

## Substitute review

Frames sampled at 50 % and 85 % of every beat (28 frames total for
Gate V), plus per-beat mid-frame extracts opened with the image-capable
Read tool, plus the full 14-thumb contact sheet
(`_qc/contact_sheet.png`). Inspected for:

| Property | Observation |
|---|---|
| Typeface consistency | EB Garamond (serif) for greetings, segment titles, headings, artifact card, outro title. System UI sans for chrome, mechanism body, verdict pills, folder chip. Mono for composer command / output lines. Consistent across all 14 beats. |
| Kerning at large sizes | B01 (`BrutalistHesitantWriter`, fontSize 190 lineSpacing 1.5) shows clean serif tracking at 3840×2160 — no touching glyphs at any sampled frame, terracotta "concept" correction reads cleanly against the cream ground. |
| Line-length legibility | Composer command (B00, B12) wraps at the composer card's own width (~65 characters at that font). Verdict artifact lines (B11) wrap at the artifact's `maxWidth` — no orphaned single words. Mechanism body blocks (B03, B05–B09, B10) sit inside the safe area at readable width. |
| Terracotta contrast | The `#D97757` accent used exclusively on: send button (B00, B12), SKILL.md DOCTRINE tag (B02), HOOK node (B04), verdict pill borders (B03, B05–B09, B10), verdict artifact number bullets (B11), title period (B13). Never used as a body colour. One-terracotta rule holds per beat. |
| Anti-aliasing at 4K | 3840×2160 output source is Remotion at design 1920×1080 rendered at `--scale=2` with `--image-format=png --crf=16` — text edges are crisp at native resolution. |
| Bookend text alignment | ClaudeTitleOutro B13 title landing, terracotta period, and hardcoded `@NikBearBrown` handle are properly stacked and centered inside safe. |
| Composer folder chip | Reads `@HumanitariansAI` on B00 and B12 — matches metadata.folderLabel and playlist adaptation. |

## Gate V typography-adjacent checks

Gate V's underfill (55 % floor) and edge-bleed checks are, in practice,
typography-adjacent because most of this teardown's content is text.
Landscape final passed with `BLOCKER=0 MAJOR=0`. The one iteration was
B01 first coming back at 23 % underfill; addressed by scaling the
hesitant-writer text (see CHECKS-REPORT.md · Gate V note).

## Not claimed

- No claim that a legacy `scripts/type_check.py` ran (it does not exist
  here).
- No claim that a kerning-only linter ran (none is shipped in this
  toolkit).
- No claim that human proofreading has happened for this run. Bear's
  viewing is next.
