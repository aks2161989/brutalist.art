# TYPECHECK.md — The sri-explainer Skill (portrait 9:16)

## What this file is

A record of the visual-typography review that runs in place of the legacy
`scripts/type_check.py` (not present in this isolated toolkit). This file
documents the actual review performed for the portrait aspect.

## Substitute review

Frames sampled at 50 % and 85 % of every beat (28 frames for Gate V),
plus per-beat mid-frame extracts opened with the image-capable Read tool,
plus the 14-thumb portrait contact sheet
(`_qc/contact_sheet.png`). Inspected for:

| Property | Observation |
|---|---|
| Typeface consistency | EB Garamond (serif) for greetings, segment titles, headings, artifact card, outro title, and the B01 hesitant-writer body. System UI sans for chrome, mechanism body, verdict pills, folder chip. Mono for composer command / output. Consistent across all 14 beats. |
| Kerning at large sizes | Patched `BrutalistHesitantWriter` now scales off a 1080×1920 design box in portrait, so `fontSize=240 lineSpacing=2.3` renders at native size, not `0.5625×`. Terracotta "concept" correction reads cleanly against the cream ground. |
| Line-length legibility | Portrait composer (B00, B12) wraps at the composer card width; the shortened B12 command fits inside `SAFE916.bottom`. Portrait verdict artifact (B11) numbered lines wrap inside the card `maxWidth`. Mechanism body blocks (B03, B05–B10, B04 in portrait) reflow to the taller portrait column without overflow. |
| Terracotta contrast | The `#D97757` accent used exclusively on: send button (B00, B12), SKILL.md DOCTRINE tag (B02), verdict pill borders (B03–B10, B04), verdict artifact numeric bullets (B11), title period (B13). One-terracotta rule holds per beat. |
| Anti-aliasing at 4K | 2160×3840 output source is Remotion at design 1080×1920 rendered at `--scale=2` — text edges are crisp at native resolution. |
| Bookend text alignment | ClaudeTitleOutro916 B13 title landing, terracotta period, and hardcoded `@NikBearBrown` handle stack cleanly inside `SAFE916`. |
| Composer folder chip | Reads `@HumanitariansAI` on B00 and B12 — matches metadata.folderLabel. |

## Gate V typography-adjacent checks

Gate V's underfill (55 % floor) and edge-bleed checks are, in practice,
typography-adjacent because most of this teardown's content is text.
Portrait final passed with `BLOCKER=0 MAJOR=0` after three iterations
on B01 (font/lineSpacing tuning under the patched scale), B04 (pattern
swap away from the horizontal pipeline), and B12 (command / output
shortening). See CHECKS-REPORT.md for the exact numbers.

## Not claimed

- No claim that a legacy `scripts/type_check.py` ran (does not exist
  here).
- No claim that a kerning-only linter ran (none shipped).
- No claim that human proofreading has happened. Bear's viewing is
  next.
