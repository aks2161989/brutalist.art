# SHOTLIST.md — What Is Brutalist? · 9:16 portrait companion

*Aspect: 9:16 portrait, 2160×3840. Full-length companion — every beat of the
landscape reel is present; no cap, no dropping, no endcard. Native portrait
compositions (`Wib*916` / `ClaudeComposerAsk916` / `BrutalistHesitantWriter916`
/ `ClaudeVerdictArtifact916` — see `art vertical` planner), NOT a center-cut
of the landscape master. Renderer:
`python3 runtime/scripts/remotion_scenes.py <reel>/vertical` (foreground,
concurrency 1).*

| # | ID | Duration | Portrait scene id | Class | Reflow move |
|---|---|---|---|---|---|
| 0 | B00 | 16.79 s | `ClaudeComposerAsk916` | SHOW · UI ask | R3 rescale — the composer scene reads `useVideoConfig()` and reflows its chrome + result-line stack to portrait height. |
| 1 | B01 | 20.03 s | `BrutalistHesitantWriter916` | SHOW · type-then-correct | R4 serialize — text splits into 6 short lines (`Brutalist\nis a\nvideo\neditor.\nActually,\ntext.`) at `fontSize: 380` for the taller 9:16 safe area; the swap `editor → recipe` still lands the framing correction. |
| 2 | B02 | 16.49 s | `WibRecipe916` | SHOW · framework | R4 serialize — the landscape's left/right panels stack vertically. beat_sheet.json card is above, terracotta arrow points down, the rendered composer card is below. |
| 3 | B03 | 19.52 s | `WibPipeline916` | SHOW · worked example | R4 serialize — the six horizontal stage cards become a vertical stack; connector arrow rotates 90°; final `4K MASTER` node lit terracotta. |
| 4 | B04 | 18.11 s | `WibChange916` | SHOW · worked example | R4 serialize — the JSON-edit panel sits above the rendered-composer panel; the `Ciao` → `Hola` swap happens on the top panel and the bottom panel updates in place. |
| 5 | B05 | 21.61 s | `WibDivision916` | SHOW · division of labor | R4 serialize — HUMAN lane (four rows, terracotta accent) above AGENT lane (five rows). |
| 6 | B06 | 20.46 s | `WibNotClaims916` | SHOW · falsifiability | R3 rescale — the three-row not-list stays vertical; each row's label + body reflow to a two-line stack in portrait. |
| 7 | B07 | 14.44 s | `WibVerdict916` | SHOW · verdict | R3 rescale — the artifact card fills the entire safe area (top/bottom padding = 130 px, side padding = 96 px) with three numbered lines wrapping to two lines each. |
| 8 | B08 | 17.98 s | `ClaudeComposerAsk916` | SHOW · UI handoff | R3 rescale — same composer chrome as B00; the paste-ready prompt types into the composer and three expected-artifact result lines settle below. |
| 9 | B09 | 4.86 s | `WibOutro916` | SHOW · outro | R3 rescale — eyebrow at top, title wraps to two lines, `@HumanitariansAI` handle centered, `LIAM, IN FOR BEAR.` subline at bottom. |

## Bookend spine and teaching-arc coverage

Same as landscape (see `../SHOTLIST.md`) — every beat classifies SHOW, no
unresolved slates, framework beat before examples, worked example present,
falsifiability beat present, scaffolded viewer task in the handoff.

## Portrait-specific safety adjustments

- **All Wib components use `pad = 96` and `padY = portrait ? 130 : 82`.**
  Portrait safe.y = 96 and safe.x = 54, so the uniform 96 px horizontal pad
  keeps everything inside safe.x with a cushion. `padY = 130` keeps the
  eyebrow/title inside the top safe band. This is the fix for the top-edge
  bleed the first portrait compile reported on B02–B07.
- **B01 uses portrait-specific props.** Landscape B01 renders at fontSize 200
  with three lines; portrait B01 renders at fontSize 380 with six short lines.
  The narrower 1080-wide canvas would clip the landscape word
  `plain-text-recipe` at that size, so portrait uses the shorter
  `editor → recipe` swap. The hesitant-writer misconception-correction
  pattern is preserved.
- **WibVerdict portrait uses padY for the card top/bottom offsets** so the
  card never crosses the 96 px top safe band or the 1824 px bottom safe band.
- **WibOutro portrait spreads eyebrow → title → handle → subline vertically**
  (top:130 / top:300 / top:1150 / bottom:140) so the ink bbox covers >55% of
  the tall safe area.

## Where portrait diverges from the landscape SHOW notes

- B01 shows the alternate short text as described above; the semantic beat
  (the misconception "video editor" being corrected to "recipe/text") is
  preserved even though the exact phrase differs.
- All other beats show the same content as landscape; layout reflows only.
