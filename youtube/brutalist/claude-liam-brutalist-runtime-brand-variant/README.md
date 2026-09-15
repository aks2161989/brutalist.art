# Brutalist Utility: brand_variant.py

**Playlist:** Brutalist · **Channel:** @HumanitariansAI · **Voice:** Kokoro `am_onyx` (Liam, in for Bear) · **Register:** Teardown

Source under teardown: `runtime/scripts/brand_variant.py` (invocation source SHA-256 `1ab627266e10e1ed8a0e4e704f38180f261b647013dd27eeac51767b61381560`; working-toolkit copy SHA-256 `ced0d3f79d98e5d9b18e005679474b64f8fe3b897f5f6fef6b5b3ee2ed02756e`) — the 152-line audience-variant scaffolder that stamps deterministic metadata, copies build scripts, writes a per-audience `_variant_todo`, and defers the register rewrite to Claude.

## Deliverables (both native 4K)

- Landscape 3840×2160 — [`exports/landscape/claude-liam-brutalist-runtime-brand-variant.mp4`](exports/landscape/claude-liam-brutalist-runtime-brand-variant.mp4) · 222.8s · 12/12 beats · Gate V clean · AI frame review in [`VISUAL-REVIEW.json`](VISUAL-REVIEW.json).
- Vertical 2160×3840 — [`exports/vertical/claude-liam-brutalist-runtime-brand-variant-vertical.mp4`](exports/vertical/claude-liam-brutalist-runtime-brand-variant-vertical.mp4) · 223.1s · 12/12 beats · native portrait compositions (…916 variants) · Gate V clean · AI frame review in [`vertical/VISUAL-REVIEW.json`](vertical/VISUAL-REVIEW.json).

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
- [`FACTCHECK.md`](FACTCHECK.md) — every screen/narration claim mapped to `brand_variant.py` line numbers.
- [`SOURCES.md`](SOURCES.md) — source ledger + preserved credit.
- [`CHECKS-REPORT.md`](CHECKS-REPORT.md) + [`vertical/CHECKS-REPORT.md`](vertical/CHECKS-REPORT.md) — actual gates that ran, honest gaps.
- [`TYPECHECK.md`](TYPECHECK.md) + [`vertical/TYPECHECK.md`](vertical/TYPECHECK.md) — visual typography review (distinct from the absent legacy `type_check.py`).
- [`BUILD-PROMPT.md`](BUILD-PROMPT.md) — the full production prompt this run followed.

## Run

- `episode.run_id`: `2105289f3f3846c2870c68ad6e4c57dc`
- `episode.source_sha256`: `1ab627266e10e1ed8a0e4e704f38180f261b647013dd27eeac51767b61381560`
- Isolated toolkit baseline: `92432609980c8ffc03bc1f00a1300fe1ac78bd7363b5b8ba9f2d389407d72b9d`
- Re-render from run `0ff7fe5fe3054305bc9f24dfce896045`: corrected B04/B07/B08 code props and B07 narration for updated `brand_variant.py` (single-line output, `copy_build_scripts()`, segment strip).
