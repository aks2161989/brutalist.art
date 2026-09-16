# SHOTLIST — Brutalist Utility: align.py

12 beats. Every one is SHOW per SHOW-DON'T-TELL LAW; classifications per nopunt SKILL.md.

| Beat | Act | Scene component | Kind | What appears (before narration lands) |
|------|-----|-----------------|------|----------------------------------------|
| B00 | ASK | `ClaudeComposerAsk` (landscape) / `ClaudeComposerAsk916` (portrait) | UI | Composer card fades in, `Habari, Liam` greeting types, the ask fills the composer, running text "invoking align.py…" appears, three output lines cascade. |
| B01 | BLUF | `BrutalistHesitantWriter` / `BrutalistHesitantWriter916` | Illustration | Cream page holds; "align.py / transcribes audio." types; `transcribes` turns terracotta, hesitates, backspaces, types `times`; `audio` turns terracotta, hesitates, backspaces, types `words`; final settle: "align.py / times the words." |
| B02 | FRAMEWORK | `SkillTeardownPipeline` / `SkillTeardownMechanism916` | Illustration | Eyebrow SKILL · PIPELINE; title "The word clock"; INPUT box `beat_sheet.json + mp3/*.mp3`; four phases (`WHISPER`, `SEQUENCEMATCHER`, `INTERPOLATE`, `EMIT`); OUTPUT box `mp3/words.json`; terracotta arrows in order; spark line. (Portrait: same content stated vertically via `SkillTeardownMechanism916`.) |
| B03 | MECHANISM | `ClaudeCodeBeat` / `ClaudeCodeBeat916` | Code | Card in; title `align.py — CLI surface`; the `usage: align.py [-h] [--model MODEL] [--language LANGUAGE] [--only [ONLY ...]] folder` block types verbatim; spark line lands. |
| B04 | WORKED_EXAMPLE | `ClaudeCodeBeat` / `ClaudeCodeBeat916` | Code | Card in; title `demo/single-beat/mp3/words.json`; the ten-word words.json block types; spark line lands. |
| B05 | MECHANISM | `ClaudeCodeBeat` / `ClaudeCodeBeat916` | Code | Card in; title `align.py:49-66 — whisper_words()`; the function body types; spark line lands. |
| B06 | MECHANISM | `ClaudeCodeBeat` / `ClaudeCodeBeat916` | Code | Card in; title `align.py:69-101 — align_words()`; the function body types (norm + SequenceMatcher + interpolation loop); spark line lands. |
| B07 | MECHANISM | `ClaudeCodeBeat` / `ClaudeCodeBeat916` | Code | Card in; title `align.py:104-109 + 158-165 — even_spread + warning`; `even_spread()` body types, then the fallback branch and the `[warn]` print line; spark line lands. |
| B08 | WORKED_EXAMPLE | `ClaudeCodeBeat` / `ClaudeCodeBeat916` | Code | Card in; title `demo/number-drift/mp3/words.json — the drift case`; three verbatim rows: input narration text, whisper spoken tokens, resulting `1926,` entry in words.json. Spark line. |
| B09 | VERDICT | `ClaudeVerdictArtifact` / `ClaudeVerdictArtifact916` | Illustration | Artifact card in; heading `align.py — the whole surface, in the order it does its job`; six bullet lines cascade. |
| B10 | YOUR_TURN | `ClaudeComposerAsk` (`greeting: "Your Turn"`) / `ClaudeComposerAsk916` | UI | Composer in; `Your Turn` greeting types; the paste-ready prompt fills the composer; running text `paste this into Claude Code…`; three grading lines cascade. |
| B11 | OUTRO | `ClaudeTitleOutro` / `ClaudeTitleOutro916` | Card | Cream page in; title `Brutalist Utility: align.py.` types; handle `@NikBearBrown` (locked) appears; slug-seeded mascot animates. |

## Aspect-specific notes

- **Landscape (3840×2160).** `SkillTeardownPipeline` renders horizontally — INPUT ▶ phases ▶ OUTPUT with terracotta arrows; sized responsively via the component's `boxW = min(200, floor(width*0.78 / n) - 20)` formula.
- **Portrait (2160×3840).** `SkillTeardownPipeline` cannot fit its horizontal phase strip inside the 9:16 SAFE inset (documented in memory `feedback_skillteardown_pipeline_portrait.md`); B02 in the portrait beat sheet swaps to `SkillTeardownMechanism916`, restating the same INPUT→PHASES→OUTPUT structure as a large heading + body + verbatim excerpt from `align.py`'s docstring. Everything else is a native 916 composition of the same component (`ClaudeCodeBeat916` uses `useVideoConfig()` width/height fractions, so line-height and card padding reflow naturally).
- **Outro.** The card is the locked `ClaudeTitleOutro` (per `OUTRO-LOCK.md`) which hardcodes `@NikBearBrown`. This adaptation for @HumanitariansAI is called out in `README.md` for the human reviewer.

## Sub-beat markers

Every code beat's `shot.show` block anchors the reveal at `~0.05` (card in), `~0.20-0.85` (line-by-line reveal), `~0.94` (spark line lands). No motion is invented — reveals are driven by the component's own `REVEAL_START` + `LINE_STRIDE`, so the reveal cadence matches the audio-conformed clip length automatically. No word-level timing plane is drawn on top of the code beats; `words.json` is what THIS video EXPLAINS but is not itself consumed by these beats.
