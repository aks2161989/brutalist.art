# SHOTLIST — Brutalist Utility: brand_variant.py

12 beats. Every one is SHOW per SHOW-DON'T-TELL LAW; classifications per nopunt SKILL.md.

| Beat | Act | Scene component | Kind | What appears (before narration lands) |
|------|-----|-----------------|------|----------------------------------------|
| B00 | ASK | `ClaudeComposerAsk` (landscape) / `ClaudeComposerAsk916` (portrait) | UI | Composer card fades in, `Yassou, Liam` greeting types, the ask fills the composer, running text "invoking brand_variant.py…" appears, three output lines cascade. |
| B01 | BLUF | `BrutalistHesitantWriter` / `BrutalistHesitantWriter916` | Illustration | Cream page holds; "brand_variant.py / rewrites narration." types; `rewrites` turns terracotta, hesitates, backspaces, types `stamps`; `narration` turns terracotta, hesitates, backspaces, types `metadata`; final settle: "brand_variant.py / stamps metadata." |
| B02 | FRAMEWORK | `SkillTeardownPipeline` / `SkillTeardownMechanism916` | Illustration | Eyebrow UTILITY · PIPELINE; title "The audience-variant scaffold"; INPUT box `reel/beat_sheet.json + {claude-liam|nbb|hai}`; four phases (`RESOLVE`, `STAMP`, `TODO`, `EMIT`); OUTPUT box `<suffix>-<slug>/beat_sheet.<suffix>.json`; terracotta arrows in order; spark line. (Portrait: same content stated vertically via `SkillTeardownMechanism916`.) |
| B03 | MECHANISM | `ClaudeCodeBeat` / `ClaudeCodeBeat916` | Code | Card in; title `brand_variant.py — CLI surface`; the verbatim `-h` block types (usage + positional args + `--force`); the audience-key legend comment types; spark line. |
| B04 | WORKED_EXAMPLE | `ClaudeCodeBeat` / `ClaudeCodeBeat916` | Code | Card in; title `demo/hai-canonical/beat_sheet.hai.json`; the two `[variant]` status lines type; the emitted metadata block types row by row; spark line. |
| B05 | MECHANISM | `ClaudeCodeBeat` / `ClaudeCodeBeat916` | Code | Card in; title `brand_variant.py:28-41 — AUD lookup`; the three-brand dict types row by row (claude-liam → nbb → hai); spark line. |
| B06 | MECHANISM | `ClaudeCodeBeat` / `ClaudeCodeBeat916` | Code | Card in; title `brand_variant.py:44-50 — get_brand_dir()`; the function body types; the two directory examples (reel + lecture) type; spark line. |
| B07 | MECHANISM | `ClaudeCodeBeat` / `ClaudeCodeBeat916` | Code | Card in; title `brand_variant.py:62-135 — main() body`; the existence-check block types; the metadata-stamp block types; the strip-stale-timings loop types; spark line. |
| B08 | WORKED_EXAMPLE | `ClaudeCodeBeat` / `ClaudeCodeBeat916` | Code | Card in; title `demo — the refusal cases`; the second-run refusal (`exit 1`) types; the `--force` success types; the missing-canonical refusal (`exit 1`) types; spark line. |
| B09 | VERDICT | `ClaudeVerdictArtifact` / `ClaudeVerdictArtifact916` | Illustration | Artifact card in; heading `brand_variant.py — the whole surface, in the order it does its job`; six bullet lines cascade. |
| B10 | YOUR_TURN | `ClaudeComposerAsk` (`greeting: "Your Turn"`) / `ClaudeComposerAsk916` | UI | Composer in; `Your Turn` greeting types; the paste-ready prompt fills the composer; running text `paste this into Claude Code…`; three grading lines cascade. |
| B11 | OUTRO | `ClaudeTitleOutro` / `ClaudeTitleOutro916` | Card | Cream page in; title `Brutalist Utility: brand_variant.py.` types; handle `@NikBearBrown` (locked) appears; slug-seeded mascot animates. |

## Aspect-specific notes

- **Landscape (3840×2160).** `SkillTeardownPipeline` renders horizontally — INPUT ▶ phases ▶ OUTPUT with terracotta arrows; sized responsively via the component's `boxW = min(200, floor(width*0.78 / n) - 20)` formula.
- **Portrait (2160×3840).** `SkillTeardownPipeline` cannot fit its horizontal phase strip inside the 9:16 SAFE inset (documented in memory `feedback_skillteardown_pipeline_portrait.md`); B02 in the portrait beat sheet swaps to `SkillTeardownMechanism916`, restating the same INPUT→PHASES→OUTPUT structure as a large heading + body + verbatim excerpt from `brand_variant.py`'s docstring. Everything else is a native 916 composition of the same component (`ClaudeCodeBeat916` uses `useVideoConfig()` width/height fractions, so line-height and card padding reflow naturally). Registered by adding the missing `<Composition id="ClaudeCodeBeat916">` and `<Composition id="SkillTeardownMechanism916">` entries in Root.tsx (parity with the align.py reel), then rebuilding `scenes.json`.
- **Outro.** The card is the locked `ClaudeTitleOutro` (per `OUTRO-LOCK.md`) which hardcodes `@NikBearBrown`. This adaptation for @HumanitariansAI is called out in `README.md` for the human reviewer.

## Sub-beat markers

Every code beat's `shot.show` block anchors the reveal at `~0.05` (card in), `~0.20–0.85` (line-by-line reveal), `~0.94` (spark line lands). No motion is invented — reveals are driven by the component's own `REVEAL_START` + `LINE_STRIDE`, so the reveal cadence matches the audio-conformed clip length automatically. No word-level timing plane is drawn; `words.json` is not consumed by these beats (this reel is a `brand_variant.py` teardown, not a karaoke pass).
