# Brutalist Command: art icon-build

Episode #25 in the Brutalist playlist for **@HumanitariansAI**. Narration by
**Liam, in for Bear** (Kokoro `am_onyx`, local, free). 12 beats.

## Deliverables

- Landscape (16:9, native 4K):
  `exports/landscape/claude-liam-brutalist-command-icon-build.mp4` — 3840×2160, 253.04 s
- Vertical (9:16, native 4K):
  `exports/vertical/claude-liam-brutalist-command-icon-build-vertical.mp4` — 2160×3840, 248.33 s

Bear's viewing / editing is next. **These files are NOT published**; the
publishing / YouTube upload step happens later in the human pipeline.
Local 4K files are not proof of YouTube's 4K processing or approval.

## The 12 beats

| # | Beat | Purpose |
|---|---|---|
| B00 | ASK | Cold open — Claude composer types the ask "12 GB of raw svg upstream. How do you get to a shippable icon set?"; result lines introduce the 400× reduction and one-branch dispatcher. |
| B01 | BLUF | Hesitant writer: "art icon-build **downloads new icons**" → "art icon-build **cuts existing icons**". |
| B02 | FRAMEWORK | The `case` branch in `art:64-66` — one word, no aliases, execs `build_icon_set.py`. |
| B03 | MECHANISM | The problem: 12 GB in `svg/`, 2.4 M files, 9.1 GB in `material-design-icons` alone. Not shippable, not searchable. |
| B04 | MECHANISM | The four rules, verbatim from the docstring: stroke only · one-icon-per-thing · one geometry/weight · B&W. |
| B05 | MECHANISM | The 44 pt math: stroke 2 in a 24 viewBox at 528 px = 44 pt exactly. Constant ships in `icons.json`. |
| B06 | WORKED EX | `./art icon-build --dry-run` — verbatim source-pass table (1749/4134/1045/26/376 = 7,330). |
| B07 | WORKED EX | Output artifacts: `icons/svg/` (~29 MB, 7,330 files) + `icons.json` (index) + `NOTICE.md` (licence obligation, met). |
| B08 | FALSIFIABILITY | The four principled drops: material-design (filled + huge), RemixIcon (filled), heroicons (dup lucide), anthropics (no LICENSE). |
| B09 | VERDICT | Seven lines: bare / `--dry-run` / `--limit` / four rules / four exclusions / 44 pt math / NOTICE. |
| B10 | YOUR TURN | Paste-ready audit prompt: dry-run → limited trial → NOTICE grep. |
| B11 | OUTRO | Title restate; `@NikBearBrown` (OUTRO-LOCK); slug-seeded mascot. |

## Where the paperwork lives

Every claim ties back to a source file in the isolated toolkit:

- `FACTCHECK.md` — every factual claim mapped to `build_icon_set.py`, `icons.json`, or the `art` dispatcher.
- `SOURCES.md` — hashes and roles for `art` (`9bb77a…`), `build_icon_set.py` (`75bdb9…`), doctrine files, examples, tools, and all eight upstream libraries with the reason each was kept or dropped.
- `SHOTLIST.md` — beat-by-beat visual plan (landscape); `vertical/SHOTLIST.md` for portrait-specific notes.
- `SCRIPT.md` — every narration line, verbatim.
- `PROMPTS.md` — the on-screen composer prompts (B00 ask, B10 handoff).
- `CHECKS-REPORT.md` — PROOF GATE, GATE V (0 BLOCKER / 0 MAJOR), audio decode, dimensions.
- `TYPECHECK.md` — visual typography review; documents the absent legacy `scripts/type_check.py`.
- `BUILD-PROMPT.md` — the full supervisor invocation contract, unchanged.
- `VISUAL-REVIEW.json` — schema-valid review record with real file hashes and run_id.
- `demo/RUN-LOG.md` — real captures of `./art icon-build` on this workspace (`--dry-run`, `--limit`, `--help`, missing-`svg/` failure, `--bogus` argparse error, `du -sh` on every source dir, and a peek at the shipped `NOTICE.md`).

The vertical variant has its own `vertical/` folder with the same paperwork.
Shared docs (FACTCHECK, SOURCES, PROMPTS, BUILD-PROMPT) are copied when accurate;
SHOTLIST, CHECKS-REPORT, TYPECHECK, VISUAL-REVIEW are portrait-specific.

## Known limitations

- **Motion histogram flags `code-cascade` at 58 %** (7 of 12 beats). Expected
  for a command teardown — each of those beats is a different real code
  artifact (dispatcher, `du -sh` table, four rules, 44 pt math, `--dry-run`
  output, shipped artifacts, four exclusions). Same warning appears on the
  reference episodes `claude-liam-brutalist-command-help` and
  `claude-liam-brutalist-command-icons`, which shipped. Logged in
  `CHECKS-REPORT.md`.
- **Legacy `scripts/type_check.py`** (referenced in `ai-explainer/SKILL.md`)
  is not present in this toolkit snapshot. Visual typography was verified
  by frame inspection instead; distinguished honestly in `TYPECHECK.md`.
- **Compiler SKIN-LINT** flags `ClaudeComposerAsk916` and `ClaudeTitleOutro916`
  in the vertical cut. These are false positives — those are the correct
  portrait wrappers around the required scenes. Same wording appears on the
  reference episodes' vertical cuts. Documented in `vertical/CHECKS-REPORT.md`.
- **`icons/` numbers may drift.** The 7,330 / 376 counts are snapshotted from
  `icons/icons.json` at commit `ba2d0e0f043f5b3b35a50d336e0fc66fbfecfc0c`.
  Future runs against a changed `svg/` will produce different numbers.
- **Icon-build was NOT run without `--dry-run`** during this build. No new
  bytes were written to the public `brutalist.art/icons/` tree. Every capture
  in `demo/RUN-LOG.md` preserves the shipped set.

## Never-do log

- No paid API was called. No API key was requested. No account was created.
- No `setup --install`, `art keys`, or remote clones were run.
- No captions, subtitles, karaoke, or SRT/VTT tracks were generated.
- The original example beat sheets (`rohan-v/…`, `tanmay-kulkarni/…`) were
  read as leads only; their files and human signatures are untouched.
- The shipped canonical set `brutalist.art/icons/` was NOT rewritten by any
  demo run in this build (every `icon-build` invocation used `--dry-run`).
- No git push, no upload, no publication.
