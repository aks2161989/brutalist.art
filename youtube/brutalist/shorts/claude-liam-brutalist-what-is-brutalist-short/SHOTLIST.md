# SHOTLIST.md — What Is Brutalist? — Short (9:16 portrait)

*Aspect: 9:16 portrait, 2160×3840. Six beats, 94.79 s measured. Native portrait
renders reused unchanged from the parent 9:16 companion; no re-render, no
center-cut. No endcard — the Short ends on the sign-off frame.*

| # | ID | Duration | Portrait scene id | Class | On-screen essentials |
|---|---|---|---|---|---|
| 0 | B00 | 16.79 s | `ClaudeComposerAsk916` | SHOW · UI ask | Cream Claude page, eyebrow `HUMANITARIANS AI · BRUTALIST`, title `What Is Brutalist?`, greeting `Ciao, Liam`, composer types ask, three result lines settle. |
| 1 | B01 | 20.03 s | `BrutalistHesitantWriter916` | SHOW · type-then-correct | Six short serif lines `Brutalist / is a / video / editor. / Actually, / text.` — `editor` turns terracotta and swaps to `recipe`. |
| 2 | B04 | 18.11 s | `WibChange916` | SHOW · pure-function demo | JSON edit panel above (`"greeting": "Ciao, Liam"` struck through → `"Hola, Liam"`, `remotion_scenes.py --only B00`) with rendered composer card below flipping from `Ciao, Liam. Italian "hello."` to `Hola, Liam. Spanish "hello."`. |
| 3 | B06 | 20.46 s | `WibNotClaims916` | SHOW · falsifiability | Eyebrow `BRUTALIST · THE HONEST NOT-LIST`, title `What Brutalist isn't.`, three stacked rows: Not a publisher / Not a paid API / Not a judge of taste. |
| 4 | B07 | 14.44 s | `WibVerdict916` | SHOW · verdict | Artifact card with heading `Film as code, in three lines.` and three numbered lines; italic spark `That is what Brutalist actually is.` |
| 5 | B09 |  4.86 s | `WibOutro916` | SHOW · outro | Eyebrow `BRUTALIST · EPISODE 01`, title `What Is Brutalist?` (question mark terracotta), `@HumanitariansAI` centered, `LIAM, IN FOR BEAR.` at the bottom. |

## Bookend spine and teaching-arc coverage (Short)

- **Cold-open ask** (B00) frames the question inside the Claude composer.
- **BLUF** (B01) delivers the answer with a misconception correction.
- **Worked example** (B04) shows the pure-function claim on-screen.
- **Falsifiability** (B06) names the three honest limits.
- **Verdict** (B07) recaps in three numbered lines.
- **Outro** (B09) signs off for @HumanitariansAI.

No unresolved slates, every beat is SHOW, and the essential safety limitation
(B06) is preserved as the Shorts prompt requires.

## What is NOT in this Short

Dropped from the parent for the cut. Their portrait renders remain in the
parent `vertical/media/`, unchanged and unrelinked from this Short.

- **B02** `WibRecipe916` — beat_sheet.json anatomy.
- **B03** `WibPipeline916` — six-stage pipeline.
- **B05** `WibDivision916` — human vs agent labor lanes.
- **B08** `ClaudeComposerAsk916` — the paste-ready fellows CTA.

## Portrait safety notes carried in unchanged

Native portrait props (composer typography, HesitantWriter fontSize/lineSpacing,
Wib* padY/pad values) match the parent's tested portrait build. No layout
recompute happened; the compiler re-muxed existing 2160×3840 renders.
