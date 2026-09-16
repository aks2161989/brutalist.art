# SHOTLIST.md — What Is Brutalist?

*Aspect: 16:9 landscape, 3840×2160. Ten beats, four bookends, six body beats.
Every non-UI beat is a concept illustration (ILLUSTRATE LAW). Renderer:
Remotion via `runtime/scripts/remotion_scenes.py` — no hand-rolled
`npx remotion render`.*

| # | ID | Duration | Scene id | Class | What the viewer WATCHES |
|---|---|---|---|---|---|
| 0 | B00 | 16.79 s | `ClaudeComposerAsk` | SHOW · UI ask | Cream Claude page. Topic eyebrow "HUMANITARIANS AI · BRUTALIST", segment "What Is Brutalist?". Greeting `Ciao, Liam` resolves. Prompt types itself; the send button arms; three concrete result lines settle beneath. |
| 1 | B01 | 20.03 s | `BrutalistHesitantWriter` | SHOW · type-then-correct | Serif on cream types "Brutalist is a video editor for AI clips." — pauses on the wrong phrase; the phrase turns terracotta; the writer deletes it and types "the plain-text recipe your film is built from." Final sentence stands corrected before the cut. Lead silence 0.8 s per beat sheet — timing verified ≥ 9 s window. |
| 2 | B02 | 16.49 s | `WibRecipe` | SHOW · framework | Left card: `beat_sheet.json` file tab, 12 JSON lines reveal one at a time (narration strings in terracotta). Terracotta arrow. Right card: the rendered composer that the JSON describes — greeting `Ciao, Liam` above the ask, send button armed. Spark line "Read the JSON. Read the film." |
| 3 | B03 | 19.52 s | `WibPipeline` | SHOW · worked example | Horizontal rail of six labeled stage cards (BRIEF → BEAT SHEET → AUDIO → SCENES → COMPILE → 4K MASTER). Cards spring in on cue; the final stage lights terracotta. Sparkline: "The audio is the clock. Every scene conforms to it." |
| 4 | B04 | 18.11 s | `WibChange` | SHOW · worked example | Left card: JSON line `"greeting": "Ciao, Liam"`; the wrong word is struck through and "EDITED" flips to terracotta; shell line prints `python3 remotion_scenes.py --only B00`; then "→ re-rendering B00.mp4…". Right card: rendered composer greeting swaps from Ciao to Hola. Caption: "Spanish hello." |
| 5 | B05 | 21.61 s | `WibDivision` | SHOW · division of labor | Two lanes side by side. LEFT lane header "HUMAN · JUDGMENT — You" with terracotta accent; four rows drop in: brief, watch, ask, approve. RIGHT lane header "AGENT · EXECUTION — Claude"; five rows drop in: beat sheet, narration, scenes, master, verify. |
| 6 | B06 | 20.46 s | `WibNotClaims` | SHOW · falsifiability | Three stacked rows; each row a terracotta claim + an ink body. Row 1: "Not a publisher." + "It renders a 4K file. You upload it." Row 2: "Not a paid API." + "Kokoro runs locally. Claude runs on your subscription." Row 3: "Not a judge of taste." + "It will render any bad idea. Watching the cut is your job." |
| 7 | B07 | 14.44 s | `ClaudeVerdictArtifact` | SHOW · UI verdict | Artifact card on cream. Title "Verdict", heading "Film as code, in three lines." Three numbered lines arrive on cue: the recipe is text · the film is a pure function of the recipe · judgment stays with you. |
| 8 | B08 | 17.98 s | `ClaudeComposerAsk` | SHOW · UI handoff | Cream Claude page. Greeting `Your Turn`. The paste-ready prompt types itself into the composer verbatim (the narration reads it aloud). Running indicator "paste this into Claude…" appears; three expected-outcome lines settle beneath. |
| 9 | B09 | 4.86 s | `WibOutro` | SHOW · outro | Poster serif title restates: "What Is Brutalist?" with terracotta question mark. `@HumanitariansAI` handle fades in beneath. "LIAM, IN FOR BEAR." subline arrives last. |

## Bookend spine (four beats, all present)

- Cold open: **B00** `ClaudeComposerAsk`.
- Executive summary (Beat 2 BLUF, EXECUTIVE-SUMMARY LAW): **B01**
  `BrutalistHesitantWriter`. Audio window 20.03 s ≥ 9 s minimum.
- Verdict: **B07** `ClaudeVerdictArtifact`.
- Handoff (HANDOFF LAW, `greeting: "Your Turn"`, paste-ready prompt read
  aloud): **B08** `ClaudeComposerAsk`.
- Title-restate outro (OUTRO LAW, on the HAI channel — hardcoded handle):
  **B09** `WibOutro`.

## Teaching arc (SHOW/HOLD/CARD)

- FRAMEWORK beat before the first example: **B02** `WibRecipe`.
- WORKED EXAMPLE using the framework: **B03** `WibPipeline` and **B04**
  `WibChange`.
- FALSIFIABILITY / edge case: **B06** `WibNotClaims`.
- SCAFFOLDED viewer task: **B08** paste-ready prompt with expected artifacts
  (beat sheet, portrait companion) and the test of success (Bear can read the
  cut).
- No unresolved slates. Every beat classifies SHOW.

## Aspect variants

Every scene id above renders both 16:9 (this shotlist) and 9:16 (see
`vertical/SHOTLIST.md`). The 9:16 variants for the WhatIsBrutalist family were
authored as native compositions (`Wib*916`) — layouts reflow, not crop.
`ClaudeComposerAsk` / `BrutalistHesitantWriter` / `ClaudeVerdictArtifact` are
already aspect-aware components (they read `useVideoConfig()`), so their 9:16
compositions are registered separately with the same schema.
