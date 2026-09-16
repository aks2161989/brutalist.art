# Brutalist Command: setup

Command teardown of `./setup` — the free-by-default readiness checker at the root of the brutalist.art toolkit. Voiced by Liam (in for Bear) via local Kokoro `am_onyx`; visual treatment: the Claude cut with the @HumanitariansAI footer chip.

- Landscape 4K master: [`exports/landscape/claude-liam-brutalist-command-setup.mp4`](exports/landscape/claude-liam-brutalist-command-setup.mp4) — 3840×2160, 290.5 s, h264 + aac.
- Vertical 4K companion: [`exports/vertical/claude-liam-brutalist-command-setup-vertical.mp4`](exports/vertical/claude-liam-brutalist-command-setup-vertical.mp4) — 2160×3840, 290.5 s, native portrait (not a crop).

Bear's viewing and editing is next. Nothing here has been published.

## Structure

- Bookends: **B00** cold-open composer (`Konnichiwa, Liam`), **B01** hesitant writer BLUF (`setup / installs everything.` → `setup / verifies live.`), **B11** Your Turn composer with a paste-ready prompt, **B12** locked outro card.
- Body: **B02** the setup surface (shebang + short-help), **B03** `requirements.txt` (the pip contract, numpy pinning story), **B04** the all-green run (verbatim), **B05** the four-phase `--install` pipeline (pip, npm, fonts, Kokoro model), **B06** the `check()` helper and dynamic `OK_<id>` / `MISS_<id>` vars (bash 3.2 safe), **B07** live verification via `setup_smoke_kokoro.py` (`mean_volume > -40 dB`), **B08** the ElevenLabs guard at `setup:102-115`, **B09** one-file-missing failure and recovery (verbatim from the demo log).
- Verdict artifact: six numbered lines, each traceable to a specific line in `setup` or `requirements.txt`.

## Human review notes

- **Outro handle.** OUTRO-LOCK.md pins the outro card to a hardcoded `@NikBearBrown`, even though this playlist's footer chip is `@HumanitariansAI`. Before publication, decide whether to substitute a HAI-branded outro variant for this episode; the composer's footer chip on B00 and B11 already carries `@HumanitariansAI`.
- **Setup's `--install` mode.** Only the bare `./setup` verification was run locally. The `--install` pipeline is described from `setup:57-100`, not exercised — per the BUILD-PROMPT's "do not run `setup --install`" boundary. The narration is careful about this: `--install` is described, not shown as executed output.
- **Sibling episode.** The `./art doctor` dispatcher case that execs this same `setup` script has its own reel (`claude-liam-brutalist-command-doctor`) — that reel handles the wrapper's angle; this one handles the script itself.

## Paperwork

Both aspects carry their own copy of `FACTCHECK.md`, `SOURCES.md`, `SHOTLIST.md`, `PROMPTS.md`, `CHECKS-REPORT.md`, `TYPECHECK.md` and the `BUILD-PROMPT.md` originally supplied. `SCRIPT.md` is landscape-only (identical narration is used in vertical). `VISUAL-REVIEW.json` in each aspect has real file SHAs and matches this run's `run_id` (`81d4ac79a3f54016801f0269956c2d7c`). **Source rebuild (2026-09-13):** B04 updated to show `./art smoke` advice lines from the current `setup` success output; B05 updated to show the refactored `if !` `--install` pipeline; B04 audio regenerated (20.78 s); total duration 290.5 s.
