# TYPECHECK.md — Brutalist Command: art smoke (vertical companion)

## The absent legacy checker

Same gap as the landscape sibling — `scripts/type_check.py` and
`reference/type-spec.md` are not shipped in this toolkit revision. No
fabricated PASS is claimed here. What follows is the visual typography
review that stands in for it, this time on the native 2160×3840 portrait
master.

## Per-beat typography review (portrait)

Composition · portrait treatment · legibility verdict.

| Beat | Composition | Portrait treatment | Verdict |
|---|---|---|---|
| B00 | ClaudeComposerAsk916 | Topic band top; large serif greeting "Aloha, Liam"; composer card centered; folder chip + running indicator + 3 output lines below; SPARK rule under all of it. Base UI font `height * 0.016` (~30px CSS in portrait). | Legible; inside SAFE916. |
| B01 | BrutalistHesitantWriter916 | Serif at fontSize 155, lineSpacing 7.0, portrait design box (patched local component). Two lines occupy upper-third and lower-third of the frame. Trigger word turns terracotta before the correction fires. | Legible; canvas-fill floor cleared. |
| B02–B07 | ClaudeCodeBeat916 | Adaptive fontSize now considers both line-count and longest-line width (local component patch). Traffic-light dots + filename in title bar; code body in SF Mono ink; spark line in EB Garamond italic below the card. | Legible; no horizontal clipping. |
| B08 | ClaudeVerdictArtifact916 | Portrait artifact card; six numbered lines; numbers in terracotta. | Legible. |
| B09 | ClaudeComposerAsk916 (Your Turn) | Portrait composer; SHORTENED prompt (landscape carries the full 5-step version). Running indicator "paste into Claude Code…" at bottom. | Legible; matches on-screen narration. |
| B10 | ClaudeTitleOutro916 | Dark ground; title wraps across three lines in portrait ("Brutalist / Command: art / smoke."), `@NikBearBrown` handle beneath. No mascot in the 916 outro variant. | Legible; outro-lock honored. |

## Portrait-specific patches applied to the isolated toolkit

Documented in `scene-source-manifest.json` and preserved in `scene-source/`
after build. Nothing was pushed to the shared toolkit.

1. `runtime/remotion/src/Root.tsx` — added a `ClaudeCodeBeat916` composition
   entry (width 1080, height 1920) so the portrait variant is renderable.
   Prior state: `./art scenes --check ClaudeCodeBeat916` returned
   `NOT RENDERABLE — no <Composition> in Root.tsx`.
2. `runtime/remotion/src/scenes/BrutalistHesitantWriter.tsx` — scale line
   patched so portrait aspect uses a 1080×1920 design reference (per
   feedback recipe). Landscape unchanged.
3. `runtime/remotion/src/scenes/ClaudeCodeBeat.tsx` — code font sizing is
   now the min of (base, height-limited, width-limited) so long snippets
   fit both dimensions of the card.

## Fonts / mins / contrast (portrait)

- Faces unchanged from the landscape sibling — EB Garamond serif, system
  sans, SF Mono / Menlo.
- Minimum body text size after adaptive scaling: the mono composer output
  lines in B09 and the smallest ClaudeCodeBeat916 lines in B07 both sit at
  roughly 28px CSS in portrait — comfortably above the ~24px floor.
- No missing-glyph tofu observed. Contrast unchanged.

## Verdict

Portrait visual typography review is clean across all 11 beats. GATE V
reports 0 BLOCKER / 0 MAJOR on the compiled 4K portrait master. Not a
claim about the missing legacy type_check.py; a claim about the frames
actually inspected.
