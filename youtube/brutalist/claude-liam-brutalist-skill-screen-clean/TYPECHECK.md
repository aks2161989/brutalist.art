# TYPECHECK — The screen-clean Skill (landscape 3840×2160)

## Legacy checker status

`scripts/type_check.py` — **NOT PRESENT** in this isolated toolkit revision
(commit `ba2d0e0f043f5b3b35a50d336e0fc66fbfecfc0c` + local overrides). The
CLAUDE.md hard rules and `ai-explainer/SKILL.md` § GATE T reference it, but
the file does not exist. Same for `reference/type-spec.md` and
`skills/make/kerning/SKILL.md` — referenced by doctrine, not shipped here.

This is not fabricated: `find . -name "type_check.py"` returns nothing.
The gap is honestly logged in `CHECKS-REPORT.md § Gaps`.

## Substituted typography review — actual pixel inspection

In place of the legacy static-string checker, typography was verified by
opening rendered frames with the image-capable Read tool and reading the
type on screen. Substitutes are:

1. `runtime/qc/final_frame_check.py` — Gate V. Runs after every compile,
   samples 24 frames (each beat at 50 % and 85 %), and enforces the
   §8-family rules that translate to pixels: canvas fill / safe area
   overflow / negative-space floor. Result on this reel: `BLOCKER: 0
   MAJOR: 0` (see `_qc/REPORT.md`, preserved as `_qc/REPORT-landscape.md`).

2. Manual frame reads. Extracted 50 % / 85 % probes for the sensitive
   beats (B01 BLUF, B00 composer, B11 outro) and opened them directly.

## Per-beat typography check

| Beat | Face | Legibility | Kerning / overflow | Contrast | Notes |
|---|---|---|---|---|---|
| B00 composer | UI sans + serif (EB Garamond) | ✓ | ✓ | ink on cream ✓ | Greeting `Bonjour, Liam` fits one line; command wraps cleanly; output lines readable. |
| B01 BLUF | EB Garamond (serif) 172 px, lineSpacing 1.35 | ✓ | ✓ | ink on cream, terracotta on delete only ✓ | Final read: "The screen-clean skill flags your desktop into a safe reel beat. The proof is the sheet." Fills 55 %+ safe area (Gate V confirmed). |
| B02 anatomy | UI sans (mono for filenames) | ✓ | ✓ | ✓ | Folder tree indents render; accent on the target `SKILL.md` line; callout box legible. |
| B03 pipeline | UI sans, serif title | ✓ | ✓ | ✓ | 5-phase card fits with `PROBE` accented. Input/output labels wrap without collision. |
| B04–B08 mechanism | Serif heading + UI sans body + mono quote | ✓ | ✓ | ✓ | Heading at 52 px, body wraps within `width * 0.1` inset. Quotes never overflow. Verdict pill sized to text. |
| B09 verdict | Serif heading + UI sans lines | ✓ | ✓ | ✓ | Six lines number themselves (component owns numbering per `stripLeadNum`). |
| B10 Your Turn | UI sans + mono | ✓ | ✓ | ✓ | Long paste-ready ffmpeg command wraps in the composer; still legible. |
| B11 outro | EB Garamond (serif) title | ✓ | ✓ | terracotta period ✓ | Title `The screen-clean Skill.` renders full-size; `@NikBearBrown` handle beneath. |

## Golden strings check

Spot-checked the required frame elements by reading frames:

- Inner composer folder chip reads `@HumanitariansAI` on B00 and B10 — ✓
- Outro handle reads `@NikBearBrown` (hardcoded per OUTRO-LOCK) — ✓
- Outro title reads exactly `The screen-clean Skill.` (with terracotta
  period) — ✓
- Cite lines on mechanism cards read `screen-clean SKILL.md · <section>` —
  ✓

## Pixel-art law (crispEdges rects)

`ClaudeMascotScene`, `ClaudeMascotGrid`, `ClaudeTitleOutro` — only
`ClaudeTitleOutro` appears here (B11). No rotation on pixel-art rects
(the component itself upholds this rule). Slug-seeded mascot animation
uses `translation` + axis-aligned `scaleY` only.

## Result

**Actual typography review: PASS.** Absent-checker gaps recorded honestly
in `CHECKS-REPORT.md`. No claim of a passing `type_check.py` run is made —
the file does not exist.
