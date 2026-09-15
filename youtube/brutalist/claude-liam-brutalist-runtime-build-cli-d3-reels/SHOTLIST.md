# SHOTLIST — Brutalist Utility: build_cli_d3_reels.py

Twelve beats. Both aspects (16:9 and 9:16) use the same script; visuals swap to native `*916` compositions in portrait.

| # | Act | Scene component (16:9 → 9:16) | Motion | What is on screen |
|---|---|---|---|---|
| B00 | ASK (Cold Open) | ClaudeComposerAsk → ClaudeComposerAsk916 | type-on | Composer card on cream. Greeting `Bula, Liam` serif; ask types in; runningText `invoking build_cli_d3_reels.py…`; three output lines cascade under the composer. |
| B01 | BLUF (Beat 2 hesitant writer) | BrutalistHesitantWriter → BrutalistHesitantWriter916 | hesitant-type | 5-line stanza starts as `the tool / builds / the D3 sim / from / one prompt.`; `builds` swaps to `wraps`; `prompt` swaps to `HTML`; final settled sentence: `the tool wraps the D3 sim from one HTML.` (portrait uses the fontSize-150 / lineSpacing-2.25 recipe). |
| B02 | FRAMEWORK | SkillTeardownPipeline → SkillTeardownMechanism916 | phase-flow | Eyebrow `UTILITY · PIPELINE`; title `One config in. N review cuts out. One row each in the log.`; INPUT card `config.json (sims[])`; five phase cards STAMP · CAPTURE · AUDIO · REMOTION · COMPILE (STAMP + COMPILE accented terracotta); OUTPUT card `<slug>-slate.mp4 + log row`; spark line. Portrait swaps to SkillTeardownMechanism916 with the same eyebrow/heading/body/quote/verdict props. |
| B03 | MECHANISM 1 (CLI) | ClaudeCodeBeat → ClaudeCodeBeat916 | code-cascade | Title `build_cli_d3_reels.py — CLI + config schema (verbatim)`; usage block from `argparse`; positional + option; then the config JSON schema from the module docstring. |
| B04 | MECHANISM 2 (make_beat_sheet) | ClaudeCodeBeat → ClaudeCodeBeat916 | code-cascade | Title cites `build_cli_d3_reels.py:125-291 — make_beat_sheet()`; metadata dict; then the six law-anchored beats with their inline `#` comments (COLD OPEN · ACTUAL-CODE · captures · HANDOFF · OUTRO). |
| B05 | MECHANISM 3 (extract_code) | ClaudeCodeBeat → ClaudeCodeBeat916 | code-cascade | Title cites `build_cli_d3_reels.py:69-106 — extract_code()`; the ACTUAL-CODE-LAW docstring; the regex; `js = max(blocks, key=len)`; the line-keep loop with the `max_width` truncation; the wrap-and-return. |
| B06 | MECHANISM 4 (build_one) | ClaudeCodeBeat → ClaudeCodeBeat916 | code-cascade | Title cites `build_cli_d3_reels.py:307-406 — build_one()`; the SKIP-guard block (>50KB → SKIP); the reel folder setup; the extract_code + make_beat_sheet write; the five subprocess.run calls each with timeout; the append_log call; the except branch. |
| B07 | WORKED EXAMPLE | ClaudeCodeBeat → ClaudeCodeBeat916 | code-cascade | Title `demo/config.json → make_beat_sheet() (verbatim)`; the config row; the three observed lines from importing the module (`greeting_for('00-tiny-wave')='Yo'`, `make_title=…`, `extract_code head`); then the 10-beat stamped list. |
| B08 | MECHANISM 5 (falsifiability) | ClaudeCodeBeat → ClaudeCodeBeat916 | code-cascade | Title `the two escape hatches — soft-fail vs hard-fail`; the soft-fail block (lines 376–378: `WARN remotion_scenes failed`); the try/except catch (lines 402–406); then the verbatim `HTML not found` observed failure path. |
| B09 | VERDICT | ClaudeVerdictArtifact → ClaudeVerdictArtifact916 | artifact-in | Title `Verdict`; heading `build_cli_d3_reels.py — the whole surface, in the order it does its job`; six lines summarizing input · stamp · quote · shell out · log · recover. |
| B10 | YOUR TURN (Handoff) | ClaudeComposerAsk → ClaudeComposerAsk916 | type-on | Greeting `Your Turn`; segment `Write a config.json for build_cli_d3_reels.py`; the paste-ready prompt (three steps, no side-effects); runningText `paste this into Claude Code…`; three grading lines. |
| B11 | OUTRO | ClaudeTitleOutro → ClaudeTitleOutro916 | outro-card | Title restated verbatim: `Brutalist Utility: build_cli_d3_reels.py.`; handle `@NikBearBrown` (locked); slug-seeded mascot animates below the handle. |

## Constraints applied

- SHOW-DON'T-TELL: every beat's `shot.show` block enumerates the visual events; narration reacts to what's typed on screen.
- ILLUSTRATE LAW: the Claude UI appears only on B00 (cold open) / B10 (handoff) / B11 (outro) — B02–B09 are code beats + a diagram + an artifact card. Two composer beats in a row is not allowed and the sheet respects that.
- COLD OPEN LAW: B00 is `ClaudeComposerAsk` on cream, ask lands with three RESULT lines.
- HANDOFF LAW: B10 is `ClaudeComposerAsk` with `greeting: Your Turn`; the narration reads the prompt aloud and discusses it.
- OUTRO LAW / OUTRO-LOCK: `@NikBearBrown` handle is hardcoded — playlist adaptation for @HumanitariansAI happens only on the composer folder chip and README flag.
- FILL-THE-CANVAS: code beats use the adaptive font that bounds by both card height AND width; long stanzas fit in portrait too.
