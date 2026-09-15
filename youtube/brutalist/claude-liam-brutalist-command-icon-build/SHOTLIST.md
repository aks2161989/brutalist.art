# SHOTLIST — Brutalist Command: art icon-build

12 beats · Kokoro `am_onyx` · Claude fidelity palette · @HumanitariansAI folder chip · @NikBearBrown outro (locked)

| # | Beat | Scene / pattern | Duration | Notes |
|---|---|---|---|---|
| B00 | ASK — cold open | `ClaudeComposerAsk` | ~17 s | Greeting "Merhaba, Liam"; ask + result lines (12 GB → 30 MB, geometry, one-branch dispatcher). Introduces Liam in for Bear. |
| B01 | BLUF — hesitant writer | `BrutalistHesitantWriter` | ~15 s | Corrects "downloads / new" → "cuts / existing". Seeded `command-icon-build-b01`. |
| B02 | FRAMEWORK — dispatcher | `ClaudeCodeBeat` | ~15 s | Real bash `case` block from `art:64-66`: one word `icon-build`, one exec. Contrast with the neighbouring three-alias `icons` branch. |
| B03 | MECHANISM — the problem | `ClaudeCodeBeat` | ~20 s | `du -sh` table: 12 GB total, 9.1 GB in material-design-icons alone. |
| B04 | MECHANISM — the four rules | `ClaudeCodeBeat` | ~26 s | Verbatim from the module docstring: stroke only · one-icon-per-thing · one geometry/weight · B&W. |
| B05 | MECHANISM — the 44pt math | `ClaudeCodeBeat` | ~28 s | Constants + formula: 2/24 × 528 = 44 pt. `RENDER_PX_FOR_44PT = 528` ships in `icons.json`. |
| B06 | WORKED EXAMPLE — dry-run | `ClaudeCodeBeat` | ~26 s | Verbatim `--dry-run` output: five source passes + CANONICAL SET summary. |
| B07 | WORKED EXAMPLE — artifacts | `ClaudeCodeBeat` | ~21 s | `ls icons/` + `icons.json` shape + `NOTICE.md` preamble (the licence obligation, met). |
| B08 | FALSIFIABILITY — the drops | `ClaudeCodeBeat` | ~26 s | The four EXCLUDED libraries and why: material-design (filled + huge), RemixIcon (filled), heroicons (dup), anthropics (no LICENSE). |
| B09 | VERDICT — the surface | `ClaudeVerdictArtifact` | ~24 s | Seven lines: bare / --dry-run / --limit / four rules / four exclusions / 44 pt math / NOTICE.md. |
| B10 | YOUR TURN | `ClaudeComposerAsk` | ~30 s | Paste-ready audit prompt (dry-run → limited trial → JSON count comparison → NOTICE grep). |
| B11 | OUTRO — title restate | `ClaudeTitleOutro` | ~6 s | "Brutalist Command: art icon-build."; hardcoded `@NikBearBrown` (OUTRO-LOCK); slug-seeded mascot. |

## Visual language

- **Palette**: Claude fidelity — cream page `#FAF9F5`, warm ink `#3D3929`, terracotta spark `#D97757`. One terracotta moment per beat.
- **Type**: EB Garamond (serif) for greetings + segment titles; UI sans for chrome; SF Mono for terminal/code lines.
- **Folder chip**: `@HumanitariansAI` on the composer beats (B00, B10).
- **Outro handle**: `@NikBearBrown` — locked constant per `OUTRO-LOCK.md`. Slug-seeded polarity, mascot, and jingle.
- **Motion**: type-on for composer/hesitant beats; code-cascade for ClaudeCodeBeat; artifact-in for the verdict.

## ILLUSTRATE LAW compliance

Claude UI appears only where the UI is the subject:
- B00 — cold-open ASK (the UI is the interface being introduced)
- B10 — HANDOFF ASK (the composer is the paste target)
- B11 — OUTRO title card
- Every other beat (B01–B09) illustrates the concept: hesitant writer (B01), and code cards for the dispatcher (B02), the raw corpus (B03), the four rules (B04), the 44 pt math (B05), the dry-run output (B06), the artifacts (B07), and the exclusions (B08).

## SPARK-LINE LAW compliance

Each ClaudeCodeBeat carries a short serif spark line under the card:
- B02: "One word. One branch. One script."
- B03: "12 GB in. Almost all variants of the same ideas."
- B04: "One weight. One geometry. One color hook."
- B05: "24 viewBox · stroke 2 · 528 px  =  44 pt."
- B06: "1749 + 4134 + 1045 + 26 + 376  =  7,330."
- B07: "svg/ · icons.json · NOTICE.md — one shippable set."
- B08: "Every drop is named. Nothing swept in silently."
