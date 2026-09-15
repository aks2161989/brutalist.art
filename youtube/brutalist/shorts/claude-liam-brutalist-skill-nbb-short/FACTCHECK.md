# FACTCHECK — The nbb Skill — Short

This Short retains only B00, B01, B03, B09, B11 of the parent vertical.
Below is every claim these five beats make on screen or in narration, mapped
to source evidence in `skills/make/nbb/SKILL.md` and
`runtime/scripts/brand_variant.py`. Claims that appear only in the dropped
parent beats (B02, B04–B08, B10) are covered by the parent's own
`FACTCHECK.md` and are NOT re-asserted here — this file is scoped to what
this Short actually shows.

## B00 — cold-open ask (three answer chips)

### Claim: nbb "derives an NBB cut into a NEW nbb- directory"

- Source: SKILL.md §"Output directory convention" — `[book]/youtube/[slug]/
  → [book]/youtube/nbb-[slug]/`.
- Code: `brand_variant.py::get_brand_dir` — `reel.parent / f'{suffix}-{reel.name}'`.

### Claim: "canonical beat_sheet.json is NEVER modified"

- Source: SKILL.md §"Standing rules" — *"Source files (beat_sheet.json,
  build scripts, media) are NEVER modified."*
- Parent-demo evidence (unchanged from the vertical parent's factcheck):
  `demo/nbb-run.log` records identical pre/post SHA-256s of
  `demo/fixture-reel/beat_sheet.json`.

### Claim: "scaffold is deterministic; the rewrite is Claude's job"

- Code: `brand_variant.py` — no calls to `generate_audio*`, no writes to
  `narration_text`; only metadata + drop `actual_duration_s`.
- Source: SKILL.md — the two-halves paragraph explicitly names Python as the
  deterministic scaffolder and Claude as the register rewriter.

## B01 — BLUF (hesitant writer)

### Claim: nbb scaffolds (does NOT rewrite) your reel

- Same evidence as B00 chip 1 and chip 3. The trigger animation swaps a
  common misread ("rewrites") for the accurate verb ("scaffolds").

### Claim: "Source is never modified"

- Same evidence as B00 chip 2.

## B03 — Framework / pipeline (five phases)

### Claim: SCAFFOLD is deterministic, no API calls, no spend

- Code: `brand_variant.py` imports nothing that calls a network TTS/LLM and
  writes only local metadata. No `requests`, no HTTP client, no API keys.

### Claim: REWRITE is "every narration_text → Teardown register (Feynman × MKBHD)"

- Source: SKILL.md §"Step 2 — Rewrite every narration" and
  `runtime/prose/teardown/PROSE.md` (the register spec).

### Claim: LLM EXERCISE is the "second-to-last beat"

- Source: SKILL.md §"Step 3 — LLM exercise (SECOND-TO-LAST beat)".

### Claim: OUTRO is "last beat · NikBearBrown outro from AUTHOR.md"

- Source: SKILL.md §"Step 4 — Append the outro" and `brands/nbb.md` (the
  brand card that names AUTHOR.md as the outro source of truth).

### Claim: VERIFY = "ending order — body → [LLM] → [outro]"

- Source: SKILL.md §"Step 5 — Verify the ending order".

### Claim (footer): "One deterministic step. Four creative ones. The source is untouched."

- Composite of the two-halves paragraph and the standing rule above.

## B09 — Verdict artifact (six numbered lines)

Every verdict line restates a claim already sourced above. Two additional
specifics land only in the verdict:

### Claim (line 2): "beat_sheet.json is byte-identical before and after (same SHA-256)"

- Parent-demo evidence: `demo/nbb-run.log` records the two SHA-256s and they
  match. Not re-run in this Short; taken from the parent's factcheck record.

### Claim (line 5): "No paid voice, no imitation"

- Source: SKILL.md frontmatter — *"ElevenLabs was permanently removed
  2026-09-03"*; SKILL.md §"Standing rules" — *"There is no paid engine
  exists; ElevenLabs was permanently removed 2026-09-03."*
- Corroborated by recent toolkit commit history (commit 7ee2da6: "voice:
  ElevenLabs permanently removed — Liam (Kokoro am_onyx) everywhere").

### Claim (line 6): "brand_variant.py never tries to be clever about the register"

- Code: `brand_variant.py` — the module docstring explicitly says the
  register rewrite is Claude's job, and the code path never writes
  `narration_text`.

## B11 — Outro (title restate + handle)

### Claim: outro handle is `@NikBearBrown` (not `@HumanitariansAI`)

- Source: OUTRO-LOCK.md — this is a claude-liam reel; its outro is
  `ClaudeTitleOutro`, which hardcodes `@NikBearBrown`. The B00 composer
  chip separately uses `folderLabel: "@HumanitariansAI"` for the playlist
  channel — that is intentional, not a mistake.

## Local availability log

- `scripts/type_check.py` — NOT present in this toolkit (documented gap per
  BUILD-PROMPT). Visual typography reviewed by actual frame inspection
  instead (see `TYPECHECK.md`).
- `reference/type-spec.md`, `ILLUSTRATIONS.md`, kerning skills — NOT present
  in this toolkit (documented gap). Not fabricated.
- `runtime/scripts/brand_variant.py` — present in the parent reel's toolkit
  snapshot but NOT executed inside this Short's workspace. All B03/B09
  claims about its behaviour are traced to SKILL.md and to the parent's
  own `demo/nbb-run.log`, not to a re-run here.

## Unknowns / limits carried forward

- This Short does not exercise batch mode, does not run
  `brand_variant.py`, does not rewrite any narration, does not generate any
  audio, and does not compile any derived nbb reel. Those claims are
  described from SKILL.md and from the parent's demo log; they are not
  observed inside this Short's execution.
- The verdict's "byte-identical before and after (same SHA-256)" claim
  relies on the parent's `demo/nbb-run.log` — not re-verified in this Short.
