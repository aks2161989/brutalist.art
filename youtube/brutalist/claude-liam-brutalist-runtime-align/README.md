# Brutalist Utility: align.py

**Playlist:** Brutalist · **Channel:** @HumanitariansAI · **Voice:** Kokoro `am_onyx` (Liam, in for Bear) · **Register:** Teardown

Source under teardown: `runtime/scripts/align.py` (file SHA-256 `b2ee07253e474cbce79820dc90199929570880e012062e5b8c4980ca31bc3058`, 183 lines) — the word clock that runs at audio lock.

## Deliverables (both native 4K)

- Landscape 3840×2160 — [`exports/landscape/claude-liam-brutalist-runtime-align.mp4`](exports/landscape/claude-liam-brutalist-runtime-align.mp4) · 224.4s · 12/12 beats · Gate V clean · AI frame review in [`VISUAL-REVIEW.json`](VISUAL-REVIEW.json).
- Vertical 2160×3840 — [`exports/vertical/claude-liam-brutalist-runtime-align-vertical.mp4`](exports/vertical/claude-liam-brutalist-runtime-align-vertical.mp4) · 224.4s · 12/12 beats · native portrait compositions (…916 variants) · Gate V clean · AI frame review in [`vertical/VISUAL-REVIEW.json`](vertical/VISUAL-REVIEW.json).

The vertical is a full-length portrait companion (`art vertical` full-length; **not** an `art shorts` cut). If a Short is wanted, it is a separate cut and belongs in a different reel folder.

## What Bear reviews next

This is an **AI frame-review pass only**. Human review and any edits are the next step:

1. Watch each MP4 end to end.
2. Note fixes in [`FEEDBACK.md`](FEEDBACK.md) (top-level, shared by both aspects) — the next automatic attempt will read it.
3. **OUTRO-LOCK note:** the outro card (`ClaudeTitleOutro` / `ClaudeTitleOutro916`) still stamps the hardcoded `@NikBearBrown` handle per `OUTRO-LOCK.md`. The composer folder chip and beat-sheet channel field carry the `@HumanitariansAI` playlist adaptation. Please confirm the OUTRO-LOCK behaviour is intended before publication.

Nothing here has been published. No YouTube upload, no transcoding validation, no Drive sync. `art shorts` was not run for this episode.

## Paperwork

- [`SCRIPT.md`](SCRIPT.md) — beat-by-beat narration.
- [`SHOTLIST.md`](SHOTLIST.md) · [`PROMPTS.md`](PROMPTS.md) — per-beat staging and Remotion props.
- [`FACTCHECK.md`](FACTCHECK.md) — every screen/narration claim mapped to `align.py` line numbers.
- [`SOURCES.md`](SOURCES.md) — source ledger + preserved credit.
- [`CHECKS-REPORT.md`](CHECKS-REPORT.md) + [`vertical/CHECKS-REPORT.md`](vertical/CHECKS-REPORT.md) — actual gates that ran, honest gaps.
- [`TYPECHECK.md`](TYPECHECK.md) + [`vertical/TYPECHECK.md`](vertical/TYPECHECK.md) — visual typography review (distinct from the absent legacy `type_check.py`).
- [`BUILD-PROMPT.md`](BUILD-PROMPT.md) — the full production prompt this run followed.

## Run

- `episode.run_id`: `d295e86979c344a7b9b979f8bdf6d514`
- `episode.source_sha256`: `1a028fbdb1e705ca5005394f40ceda11267d1c2f631fb339ef46c64edc259111`
- Isolated toolkit baseline: `92432609980c8ffc03bc1f00a1300fe1ac78bd7363b5b8ba9f2d389407d72b9d`
