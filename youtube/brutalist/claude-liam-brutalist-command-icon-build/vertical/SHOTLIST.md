# SHOTLIST — Brutalist Command: art icon-build (vertical / 9:16)

12 beats · Kokoro `am_onyx` · Claude fidelity palette · @HumanitariansAI folder chip · @NikBearBrown outro (locked)

Same script and same beat spine as the landscape cut; every scene is a native
portrait (`*916`) variant. No cropping: components reflow for the taller frame.

| # | Beat | Scene / pattern | Duration | Portrait notes |
|---|---|---|---|---|
| B00 | ASK — cold open | `ClaudeComposerAsk916` | ~17 s | Composer + greeting stack vertically; result lines wrap into the wider ink block. |
| B01 | BLUF — hesitant writer | `BrutalistHesitantWriter916` | ~15 s | Text stacked over 4 lines: `art / icon-build / downloads / new icons.` (fontSize 150, lineSpacing 2.5). Portrait scale patch applied (see feedback memory). |
| B02 | FRAMEWORK — dispatcher | `ClaudeCodeBeat916` | ~15 s | Code card fills the tall safe area; spark line drops beneath. |
| B03 | MECHANISM — the problem | `ClaudeCodeBeat916` | ~20 s | 8-row `du -sh` table + total. |
| B04 | MECHANISM — the four rules | `ClaudeCodeBeat916` | ~26 s | Four numbered rules stack down. |
| B05 | MECHANISM — the 44 pt math | `ClaudeCodeBeat916` | ~28 s | Constants block + formula + `icons.json → render` block. |
| B06 | WORKED EXAMPLE — dry-run | `ClaudeCodeBeat916` | ~26 s | Full `--dry-run` transcript. |
| B07 | WORKED EXAMPLE — artifacts | `ClaudeCodeBeat916` | ~21 s | Tree + JSON header + NOTICE preamble. |
| B08 | FALSIFIABILITY — the drops | `ClaudeCodeBeat916` | ~26 s | Four excluded libraries, each with the rule that dropped it. |
| B09 | VERDICT — the surface | `ClaudeVerdictArtifact916` | ~24 s | 7 lines; artifact card stretched for portrait. |
| B10 | YOUR TURN | `ClaudeComposerAsk916` | ~30 s | Composer + expected-outcome stack. |
| B11 | OUTRO — title restate | `ClaudeTitleOutro916` | ~6 s | "Brutalist Command: art icon-build."; hardcoded `@NikBearBrown` (OUTRO-LOCK); slug-seeded mascot. |

## Portrait-specific patches (applied in this workspace only)

- **BrutalistHesitantWriter portrait scale patch** — replaces the shipped `const scale = Math.min(width/1920, height/1080)` with `height > width ? Math.min(width/1080, height/1920) : Math.min(width/1920, height/1080)`. Without this patch, portrait BLUF sits at ~13 % safe-area coverage and Gate V fails as MAJOR underfill. See `feedback-brutalist-hesitant-writer-portrait-scale-patch`.
- **ClaudeCodeBeat916 registration** — added to `Root.tsx` (was absent from this workspace snapshot). Same component as landscape, rebound to 1080×1920. Pattern taken from the ep-24 (`command-icons`) reference toolkit.
- **Node modules shadow + Chrome wrapper** — see `PROMPTS.md § Rendering`.

## Compiler SKIN-LINT expected notice

The compiler emits `SKIN-LINT: palette=claude but the cold open is 'ClaudeComposerAsk916'`
and the equivalent for `ClaudeTitleOutro916`. These are false positives — those
are the correct portrait wrappers around the same underlying components. The
same wording appears on the ep-24 (`command-icons`) vertical build.

## Visual language

Identical to landscape (Claude fidelity — cream page `#FAF9F5`, warm ink
`#3D3929`, terracotta spark `#D97757`). EB Garamond serif for greetings and
titles; SF Mono for terminal/code lines.
