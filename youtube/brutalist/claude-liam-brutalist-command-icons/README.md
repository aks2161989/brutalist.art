# Brutalist Command: art icons

Episode #24 in the Brutalist playlist for **@HumanitariansAI**. Narration by
**Liam, in for Bear** (Kokoro `am_onyx`, local, free). 12 beats.

## Deliverables

- Landscape (16:9, native 4K):
  `exports/landscape/claude-liam-brutalist-command-icons.mp4` — 3840×2160, 199.3 s
- Vertical (9:16, native 4K):
  `exports/vertical/claude-liam-brutalist-command-icons-vertical.mp4` — 2160×3840, 199.3 s

Bear's viewing / editing is next. **These files are NOT published**; the
publishing / YouTube upload step happens later in the human pipeline.
Local 4K files are not proof of YouTube's 4K processing or approval.

Re-verified 2026-09-12 under run_id `9c6d30d53da2466ea7266f53a51cf4ef`:
source SHA updated (SKILL.md and unrelated Remotion component changes);
Gate V re-run on both aspects — 0 BLOCKER / 0 MAJOR; contact sheets
re-inspected; no video, audio, or clip content changed.

## The 12 beats

| # | Beat | Purpose |
|---|---|---|
| B00 | ASK | Cold open — Claude composer types the ask "before drawing a mark, ask the library"; result lines introduce the surface. |
| B01 | BLUF | Hesitant writer: "art icons **draws new icons**" → "art icons **finds existing icons**". |
| B02 | FRAMEWORK | The `case` branch in `art:60-63` — three aliases (icons, icon, icon-search), one exec. |
| B03 | MECHANISM | The canonical set: 7,330 icons, 24-unit viewBox, stroke 2, currentColor. |
| B04 | MECHANISM | The ranker: exact > all-words > prefix > token, IDF re-weighted. |
| B05 | WORKED EX | `./art icons "money"` — 31 hits, top 10 shown verbatim. |
| B06 | WORKED EX | `--check` (anti-redraw) and `--show` (raw SVG). |
| B07 | WORKED EX | `--brands` scope switch — 376 logos vs 6,954 concepts. |
| B08 | FALSIFIABILITY | The miss — "quantum entanglement" returns the anti-redraw doctrine, exit 0. |
| B09 | VERDICT | Seven lines: bare / query / --check / --show / --brands / aliases / miss. |
| B10 | YOUR TURN | Paste-ready audit prompt for Claude Code (nine runs + alias diff + one own concept). |
| B11 | OUTRO | Title restate; `@NikBearBrown` (OUTRO-LOCK); slug-seeded mascot. |

## Where the paperwork lives

Every claim ties back to a source file in the isolated toolkit:

- `FACTCHECK.md` — every factual claim mapped to `icon_search.py`, `icons.json`, or the `art` dispatcher.
- `SOURCES.md` — hashes and roles for `art` (`9bb77a…`), `icon_search.py` (`310f11…`), doctrine files, examples, tools.
- `SHOTLIST.md` — beat-by-beat visual plan (landscape); `vertical/SHOTLIST.md` for portrait-specific notes.
- `SCRIPT.md` — every narration line, verbatim.
- `PROMPTS.md` — the on-screen composer prompts (B00 ask, B10 handoff).
- `CHECKS-REPORT.md` — PROOF GATE, GATE V (0 BLOCKER / 0 MAJOR), audio decode, dimensions.
- `TYPECHECK.md` — visual typography review; documents the absent legacy `scripts/type_check.py`.
- `BUILD-PROMPT.md` — the full supervisor invocation contract, unchanged.
- `VISUAL-REVIEW.json` — schema-valid review record with real file hashes and run_id.
- `demo/RUN-LOG.md` — real captures of `./art icons` on this workspace (money, risk warning, sankey flow, --check, --show, --brands, quantum entanglement, and the alias-equivalence diff).

The vertical variant has its own `vertical/` folder with the same paperwork.
Shared docs (FACTCHECK, SOURCES, PROMPTS) are copied when accurate; SHOTLIST,
CHECKS-REPORT, TYPECHECK, VISUAL-REVIEW are portrait-specific.

## Known limitations

- Motion histogram flags `code-cascade` at 58% (7 of 12 beats). Expected
  for a command teardown — each of those beats is a different real code
  artifact (dispatcher, JSON index, ranker, four worked outputs). Same
  warning appears on the reference episode `claude-liam-brutalist-command-help`,
  which shipped. Logged in `CHECKS-REPORT.md`.
- Legacy `scripts/type_check.py` (referenced in `ai-explainer/SKILL.md`)
  is not present in this toolkit snapshot. Visual typography was verified
  by frame inspection instead; distinguished honestly in `TYPECHECK.md`.
- Compiler SKIN-LINT flags `ClaudeComposerAsk916` and `ClaudeTitleOutro916`
  in the vertical cut. These are false positives — those are the correct
  portrait wrappers around the required scenes. Same wording appears on
  the reference episode's vertical cut. Documented in
  `vertical/CHECKS-REPORT.md`.

## Never-do log

- No paid API was called. No API key was requested. No account was created.
- No `setup --install`, `art keys`, or remote clones were run.
- No captions, subtitles, karaoke, or SRT/VTT tracks were generated.
- The original example beat sheets (`rohan-v/…`, `yatra-r/…`) were read
  as leads only; their files and human signatures are untouched.
- No git push, no upload, no publication.
