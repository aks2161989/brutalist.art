# TYPECHECK.md — Brutalist Command: setup — Short

There is no legacy JS/TS type checker for the Remotion project in this build; the toolkit's `runtime/remotion/` uses per-scene Zod schemas at composition boundaries. This document records the visual typography review actually performed on the 2160×3840 Short.

## Typography review — retained beats

Each kept beat was opened as a 540×960 thumbnail at 15% / 50% / 85% of its duration (`_qc/beats/`) and eye-checked against the portrait SAFE916 title-safe box and Brutalist skin.

| Beat | Composition | Type check |
|---|---|---|
| B00 | `ClaudeComposerAsk916` | `Konnichiwa, Liam` serif greeting sits above the composer body; ask text wraps cleanly inside the composer card; folder chip `@HumanitariansAI` visible; three output lines cascade inside SAFE916 with no bleed. PASS. |
| B01 | `BrutalistHesitantWriter916` | Corrected serif line `setup / verifies / live.` fills the portrait canvas with `fontSize: 218, lineSpacing: 3.45`; no glyph clipping; terracotta hesitation flash on `verifies` and `live` reads clearly. Triggers `installs, everything` are single tokens per the component's `\s+` split rule (Feedback: hesitant-writer-trigger-syntax). PASS. |
| B04 | `ClaudeCodeBeat916` | Updated beat (source changed 2026-09-13): seven FEATURE rows monospace with green ✅ checkmarks; `Cost: $0.00.`, `Green table = dep checks passed (NOT renders).`, `Run ./art smoke for end-to-end proof.` and `[exit 0]` on their own lines; spark line `Green dep checks ≠ video renders. art smoke proves it.` visible beneath the card. Adaptive-fontSize patch fits all lines within SAFE916. PASS. |
| B09 | `ClaudeCodeBeat916` | Longer card (BEFORE/AFTER/RECOVERY); the `❌ blocked` row and the two indented hint lines stay inside SAFE916 with the adaptive-fontSize patch; comment lines (`# BEFORE`, `# AFTER`, `# RECOVERY`) legible; `[exit 1]` and `[exit 0]` land on their own lines. PASS. |
| B10 | `ClaudeVerdictArtifact916` | Heading `setup — the whole surface, in the order you use it` breaks to two lines; six numbered lines type in one at a time with terracotta numerals; every line stays inside SAFE916 with visible right-side padding. PASS. |
| B12 | `ClaudeTitleOutro916` | Serif title `Brutalist Command: setup.` on the dark cream ground; handle `@NikBearBrown` in the smaller face beneath; slug-seeded mascot animates below the handle; no bleed past SAFE916. PASS. |

## Portrait typography rules exercised (and not tripped)

- Adaptive-fontSize patch (Feedback: `claude-code-beat-adaptive-font`) — B09's longer BEFORE/AFTER/RECOVERY card was the tightest fit; it stayed within the code-card body without the fallback shrink.
- Hesitant-writer trigger collision rule (Feedback: `hesitant-writer-trigger-collision`) — neither `installs` nor `everything` appears in the preserved prefix `setup`, so the first-occurrence rule does not corrupt the sentence.
- Hesitant-writer portrait scale patch (Feedback: `brutalist-hesitant-writer-portrait-scale-patch`) — was applied at parent build time; this Short reuses the parent's render, so the patch's benefit is inherited.
- SparkLine baseline (Feedback: `command-todo-sparkline-portrait-bump`) — not applicable to this Short (no CommandTodo* pattern is used).

## Zod schema conformance

All props on retained beats are byte-identical to the parent vertical's `beat_sheet.json`, which was validated by `remotion_scenes.py` at parent build time. `shorts.py` does not modify props; the compiler re-validates on read.

## What was not tested

No typecheck was run for the dropped beats (B02, B03, B05, B06, B07, B08, B11) — they are not in the Short.
