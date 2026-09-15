# Brutalist Command: art vertical — Ep 31

Playlist: **Brutalist** · Channel: **@HumanitariansAI** · Voice: Liam
(Kokoro `am_onyx`, local, free) · Register: Teardown.

## What this episode teaches

`./art vertical <reel>` is a case in the `art` dispatcher (art:84-86)
that execs `python3 runtime/scripts/shorts.py <reel> --vertical`. It
is the full-length 9:16 sibling of `art shorts`: same script, opposite
editorial contract. This film shows:

- the exact dispatcher case, verbatim (B02);
- the module-docstring rule that IS the contract (B03);
- the three-line guardrail in `main()` that makes the refusal
  by-construction (B04);
- how the ONDA CHECK rewires every REMOTION beat to its `<pattern>916`
  composition, same as shorts (B05);
- the one line that separates the two: `if not a.vertical:
  require_short_duration(...)` (B06);
- a real invocation against a synthetic fixture reel (B07 — verbatim
  from `demo/VERTICAL-LOG.txt`);
- the `--vertical + --drop` refusal, both spellings, and the recovery
  (B08).

## Deliverables (local, unpublished)

- **Landscape 16:9** —
  `exports/landscape/claude-liam-brutalist-command-vertical.mp4`
  (3840×2160 · 247.46 s · h.264 + AAC).
- **Vertical 9:16** —
  `exports/vertical/claude-liam-brutalist-command-vertical-vertical.mp4`
  (2160×3840 · 247.46 s · h.264 + AAC — native portrait 4K, not an
  upscaled crop).

Both files carry `verified.json` receipts with per-input SHA-256s.
Both have a passing `VISUAL-REVIEW.json` with real frame hashes and
this invocation's `run_id` (`a6810945561e4cb29004aafd59c560fe` —
resume of `5f733dcd6d2249fea636151601143428`; media unchanged, but
the vertical review's frame paths were regenerated under
`vertical/_qc/vertical/` and both reviews' hashes/run_id refreshed
against the current master MP4s).

## Paperwork

Landscape (this dir): `SCRIPT.md`, `SOURCES.md`, `FACTCHECK.md`,
`SHOTLIST.md`, `PROMPTS.md`, `CHECKS-REPORT.md`, `TYPECHECK.md`,
`BUILD-PROMPT.md`, `VISUAL-REVIEW.json`, `beat_sheet.json`, `_qc/`.

Portrait (`vertical/`): `beat_sheet.json` (derived by
`shorts.py --vertical` from the landscape sheet, then tuned per
recipe), `FACTCHECK.md`, `SHOTLIST.md`, `PROMPTS.md`, `SOURCES.md`
(shared), `BUILD-PROMPT.md` (shared), `CHECKS-REPORT.md`,
`TYPECHECK.md`, `VISUAL-REVIEW.json`.

Demo log: `demo/VERTICAL-LOG.txt` — five verbatim invocations against
the fixture reel `/tmp/claude-501/claude-shorts-demo`, including the
`--vertical + --drop` refusal (both spellings) and the `--output-dir
<source>` refusal.

## What is next

**Bear's viewing / editing.** These files have NOT been transcoded,
uploaded, pushed to GitHub, scheduled, or announced. Publishing to
`@HumanitariansAI` YouTube is a separate authorized human workflow.

## Known limitations (accepted)

- Portrait code beats (B02–B08) render with the responsive
  `ClaudeCodeBeat916` composition. Long lines like the full
  `runtime/scripts/shorts.py` file path clip at the right edge of the
  code card. Every essential structural token (`case`, `shorts)`,
  `vertical)`, `exec python3 …`, `if a.vertical:`, `raise
  BuildError(…)`) is visible; this matches the treatment Ep 30
  (`art shorts`) shipped with and passed Gate V + human review. A
  portrait-specific ClaudeCodeBeat that word-wraps or auto-shrinks
  would be a future improvement — out of scope here.
- Skin-lint on the portrait build correctly flags
  `ClaudeComposerAsk916` and `ClaudeTitleOutro916` as departures from
  COLD OPEN LAW / OUTRO LAW. That IS the rewire the `shorts.py
  --vertical` contract performs (the whole point of the film) — the
  lint predates the portrait naming convention and Ep 30 accepted the
  same warning.
- No `type_check.py` / `type-spec.md` / kerning skill in this toolkit
  revision. Visual typography was audited manually by reading
  extracted frames with the image-capable Read tool. See `TYPECHECK.md`
  in each aspect dir.
