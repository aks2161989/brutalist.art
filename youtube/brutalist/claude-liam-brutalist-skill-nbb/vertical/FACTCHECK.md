# FACTCHECK — The nbb Skill

Every claim the film makes, mapped to source evidence in
`skills/make/nbb/SKILL.md` and `runtime/scripts/brand_variant.py`, plus the
observed output of the local demo in `demo/nbb-run.log`.

## Claim: nbb creates a new nbb- directory next to the source

- Source: SKILL.md §"Output directory convention" — `[book]/youtube/[slug]/
  → [book]/youtube/nbb-[slug]/`.
- Code: `brand_variant.py::get_brand_dir` — `reel.parent / f'{suffix}-{reel.name}'`.
- Demo evidence: `demo/fixture-reel/` → `demo/nbb-fixture-reel/` (sibling
  directory, not a subdir of the source).

## Claim: canonical `beat_sheet.json` is never modified

- Source: SKILL.md §"Standing rules" — *"Source files (beat_sheet.json,
  build scripts, media) are NEVER modified."*
- Demo evidence: `demo/nbb-run.log` records two SHA-256s of
  `demo/fixture-reel/beat_sheet.json` — before and after the run — both
  `9ee2f785d74523ce5c030d567b9bda7e49bf397bc08e28d1de081b635d28b879`.

## Claim: rerun refuses without `--force`

- Code: `brand_variant.py::main` — `if out.exists() and not a.force:
  sys.exit("… already exists (use --force to reset it from canonical)")`.
- Demo evidence: second run in `demo/nbb-run.log` emitted exactly that
  refusal, with exit code non-zero.

## Claim: metadata written is audience/palette/register/engine/voice/typography/outro_source

- Code: `brand_variant.py::main` — the AUD table and the `meta["…"] = …`
  assignments; `_variant_todo` is written for `nbb` audience.
- Diff in `demo/nbb-run.log` shows all seven fields land on the derived
  sheet.

## Claim: audience is "NikBearBrown", palette is "teardown", voice is am_onyx

- Code: `brand_variant.py` — `AUD["nbb"] = {"audience": "NikBearBrown",
  "palette": "teardown", "voice_kokoro": "am_onyx", …}`.
- Demo evidence: the emitted sheet's metadata matches all three.

## Claim: `_variant_todo` is a 5-step checklist for Claude

- Code: `brand_variant.py::main` — the `elif a.audience == "nbb":` branch
  writes exactly five items: (1) rewrite in Teardown, (2) LLM exercise as
  second-to-last, (3) NikBearBrown outro, (4) verify order, (5) build.
- Demo evidence: `demo/nbb-fixture-reel/beat_sheet.nbb.json` carries all
  five verbatim.

## Claim: script never rewrites narration or generates audio

- Code: `brand_variant.py` — no calls to `generate_audio*`, no writes to
  `narration_text`. Only `actual_duration_s` and stale `shot.rendered` are
  dropped so downstream stages recompute.
- Demo evidence: `beat_sheet.nbb.json` `narration_text` fields are
  byte-identical to the source's canonical strings.

## Claim: ElevenLabs was permanently removed 2026-09-03

- Source: SKILL.md frontmatter — *"ElevenLabs was permanently removed
  2026-09-03"*, and SKILL.md §"Standing rules" — *"No paid engine exists;
  ElevenLabs was permanently removed 2026-09-03."*
- Corroborated by recent toolkit commit history (commit 7ee2da6: "voice:
  ElevenLabs permanently removed — Liam (Kokoro am_onyx) everywhere").

## Claim: batch mode iterates every reel + every lecture

- Source: SKILL.md §"Batch mode (book input)" — the two find pipelines,
  one over `[book]/youtube/` and one over `[book]/lectures/`.
- Not exercised in the demo (synthetic single-reel fixture only), but the
  code path is documented and reachable.

## Claim: LLM-exercise beat has a paste-ready prompt + dig-deeper follow-up

- Source: SKILL.md §"Step 3 — LLM exercise (SECOND-TO-LAST beat)" — the
  beat schema shows `llm_exercise.prompt` and `llm_exercise.dig_deeper`.

## Claim: outro is ClaudeTitleOutro with `@NikBearBrown` handle on this reel

- Source: OUTRO-LOCK.md — this is a claude-liam reel; its outro is
  `ClaudeTitleOutro`, which hardcodes `@NikBearBrown`. The inner composer
  chips use `folderLabel: "@HumanitariansAI"` for the playlist channel.
- Beat sheet B11 uses `ClaudeTitleOutro`; B00 and B10 composer beats
  set `folderLabel: "@HumanitariansAI"`.

## Local availability log

- `./art scenes` — did not query; landscape scenes selected are already
  registered in Root.tsx (ClaudeComposerAsk, BrutalistHesitantWriter,
  SkillTeardownAnatomy/Pipeline/Mechanism, ClaudeVerdictArtifact,
  ClaudeTitleOutro). Portrait companions (`SkillTeardownAnatomy916`
  etc.) were not registered in the base toolkit; added natively in this
  isolated toolkit via the existing `*916.tsx` files shipped with the
  logo episode's scene-source (same schema, portrait reflow).
- `scripts/type_check.py` — NOT present in this toolkit (documented gap
  per BUILD-PROMPT). Visual typography reviewed by actual frame
  inspection instead (see TYPECHECK.md).
- `reference/type-spec.md`, `ILLUSTRATIONS.md`, kerning skills — NOT
  present in this toolkit (documented gap). Not fabricated.

## Unknowns / limits carried forward

- The film does not exercise batch mode against a real book. The fixture
  is a single reel. Claim documented from SKILL.md, not observed.
- The film does not run generate_audio_kokoro.py against the scaffolded
  sheet or compile the derived cut — that would require the full Step 2
  rewrite first, which is a creative act outside this teardown's scope.
