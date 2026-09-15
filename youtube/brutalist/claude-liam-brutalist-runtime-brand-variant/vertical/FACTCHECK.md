# FACTCHECK — Brutalist Utility: brand_variant.py

Every claim the film makes about `brand_variant.py` is verified against the source file at
`runtime/scripts/brand_variant.py` (invocation source SHA-256 `1ab627266e10e1ed8a0e4e704f38180f261b647013dd27eeac51767b61381560`;
working-toolkit copy SHA-256 `ced0d3f79d98e5d9b18e005679474b64f8fe3b897f5f6fef6b5b3ee2ed02756e` per `SOURCE-SNAPSHOT.json`)
and the live demo output in `demo/RUN-LOG.txt`.

| # | Claim on screen / in narration | Source line(s) | Verified? |
|---|--------------------------------|----------------|-----------|
| 1 | "brand_variant.py — scaffold an audience variant beat sheet from the canonical one" | `brand_variant.py:2` | ✅ verbatim in docstring |
| 2 | "three brands only — claude-liam, nbb, hai" | `brand_variant.py:4` docstring; `brand_variant.py:28-41` AUD dict; `brand_variant.py:65` `choices=list(AUD)` | ✅ |
| 3 | "Kokoro is the ONLY engine" | `brand_variant.py:5`; every AUD entry `"engine": "kokoro"` | ✅ verbatim |
| 4 | "Two voices ship: am_onyx (claude-liam + nbb), af_bella (hai)" | `brand_variant.py:32, 36, 40` `voice_kokoro` values | ✅ |
| 5 | "Every reel starts with beat_sheet.json (the canonical cut)" | `brand_variant.py:9-10` docstring | ✅ |
| 6 | "A variant is written as beat_sheet.<suffix>.json inside a new <suffix>- directory" | `brand_variant.py:10-11` docstring; `brand_variant.py:75-76` `out = out_dir / f"beat_sheet.{cfg['suffix']}.json"` | ✅ |
| 7 | "The canonical beat_sheet.json is NEVER modified" | `brand_variant.py:11-12` docstring; script only calls `src.read_text()` on canonical, writes only to `out_dir` | ✅ (no write to `src`) |
| 8 | "Deterministic half — audience metadata (engine, voice, palette, register); creative half done by Claude" | `brand_variant.py:13-16` docstring | ✅ verbatim |
| 9 | "Directory convention: <book>/youtube/<slug>/ → <book>/youtube/<suffix>-<slug>/; lectures → <suffix>-lectures/<chapter>-lecture/" | `brand_variant.py:18-20` docstring; `brand_variant.py:44-50` `get_brand_dir()` | ✅ |
| 10 | "Usage: python3 scripts/brand_variant.py <REEL_OR_LECTURE> {claude-liam|nbb|hai}" | `brand_variant.py:22-23` docstring; `brand_variant.py:63-66` argparse | ✅ verbatim |
| 11 | "Refuses to overwrite an existing variant unless --force" | `brand_variant.py:77-78` `if out.exists() and not a.force: sys.exit(...)` | ✅ |
| 12 | "Refuses if canonical is missing" | `brand_variant.py:72-73` `if not src.exists(): sys.exit(...)` | ✅ |
| 13 | "Stamps audience, derived_from, register, palette, outro_source, engine, voice_kokoro" | `brand_variant.py:84-90` | ✅ |
| 14 | "Pops legacy voice_id key (no paid engines)" | `brand_variant.py:91` `meta.pop("voice_id", None)` | ✅ verbatim |
| 15 | "hai adds typography (EB Garamond serif, Montserrat sans) and channel_title @HumanitariansAI" | `brand_variant.py:92-94` | ✅ verbatim |
| 16 | "nbb adds typography (Montserrat display, EB Garamond serif, PT Mono mono)" | `brand_variant.py:95-96` | ✅ verbatim |
| 17 | "Writes _variant_todo — the audience-specific instructions Claude follows" | `brand_variant.py:98-127` (three per-audience branches) | ✅ |
| 18 | "hai todo mentions runtime/prose/plain/PROSE.md + brands/hai.md, optional Irreducibly-Human tangent, CLI worked exercise, Humanitarians AI outro" | `brand_variant.py:99-109` | ✅ verbatim |
| 19 | "nbb todo mentions runtime/prose/teardown/PROSE.md + brands/nbb.md, LLM exercise second-to-last, NikBearBrown outro" | `brand_variant.py:110-121` | ✅ verbatim |
| 20 | "claude-liam todo: Teardown rewrite, IN-FOR-BEAR LAW at B00 + outro, generate_audio_kokoro.py → palette=claude → compile" | `brand_variant.py:122-127` | ✅ verbatim |
| 21 | "Strips actual_duration_s and shot.rendered stamps so the new variant recomputes its own durations" | `brand_variant.py:129-135` | ✅ verbatim; also handles segments |
| 22 | "Prints a two-line [variant] summary — path, audience/register/palette/engine/voice + beat-count next-step" | `brand_variant.py:144-147` | ✅ verbatim |
| 23 | "Copies any build scripts (build_deck.py, render.py, make_audio*.py) from the canonical into the variant folder" | `brand_variant.py:53-59` `copy_build_scripts()`; called at `brand_variant.py:138-140` | ✅ (demo/canonical has none, so no 'copied build scripts' line in RUN-LOG — function returns empty list) |

## Live-demo verifications

| # | Demo assertion | Source of truth |
|---|----------------|-----------------|
| D1 | `python3 runtime/scripts/brand_variant.py -h` prints the usage block used on screen | `demo/RUN-LOG.txt` §1 |
| D2 | `demo/canonical/ hai` produces `demo/hai-canonical/beat_sheet.hai.json` and canonical SHA-256 is unchanged before/after (`7da66eeff7b59c7af7304d555ba2529caca28b932155ffec69fea508b640dd16`) | `demo/RUN-LOG.txt` §2 + §4 + §14 |
| D3 | The written metadata contains the exact keys and values shown on screen (audience=HAI, register=Plain, palette=humanitarians, engine=kokoro, voice_kokoro=af_bella, channel_title=@HumanitariansAI, typography.serif=EB Garamond, typography.sans=Montserrat, `_variant_todo` list with the five hai instructions) | `demo/RUN-LOG.txt` §5 |
| D4 | Same canonical → nbb writes to `demo/nbb-canonical/beat_sheet.nbb.json` with audience=NikBearBrown, register=Teardown, palette=teardown, voice_kokoro=am_onyx, typography.{display, serif, mono}, and the five nbb todo instructions | `demo/RUN-LOG.txt` §6 + §7 |
| D5 | Same canonical → claude-liam writes to `demo/claude-liam-canonical/beat_sheet.claude-liam.json` with audience=Claude, register=Teardown, palette=claude, voice_kokoro=am_onyx, and the three claude-liam todo instructions (IN-FOR-BEAR LAW included) | `demo/RUN-LOG.txt` §8 + §9 |
| D6 | Re-running hai without `--force` exits with `[variant] ... already exists (use --force to reset it from canonical)` and exit code 1 | `demo/RUN-LOG.txt` §10 |
| D7 | Re-running hai with `--force` re-emits the same file (deterministic) | `demo/RUN-LOG.txt` §11 |
| D8 | Pointing at a folder with no `beat_sheet.json` exits with `[variant] no beat_sheet.json in <folder>` and exit code 1 | `demo/RUN-LOG.txt` §12 |
| D9 | Lecture layout: `<book>/lectures/<chapter>-lecture/` → sibling `<book>/hai-lectures/<chapter>-lecture/beat_sheet.hai.json`; both the canonical and its `<book>/lectures/<chap>/beat_sheet.json` remain unchanged | `demo/RUN-LOG.txt` §13 + §14 |

## Two silent transforms worth stating explicitly

- The canonical's own `engine`, `voice`, and `voice_id` fields are **not** protected from stamping — `engine` is overwritten to `kokoro`, `voice_id` is popped, and any leftover `voice` field is left as-is (the script does not touch it; `voice_kokoro` is the one consumed by `generate_audio_kokoro.py`). In `demo/canonical/` the seed sheet had `engine: "elevenlabs"` and `voice_id: "legacy-eleven-id-should-be-dropped"`; the variant metadata shows `engine: "kokoro"` and no `voice_id`. See RUN-LOG §5, §7, §9.
- The strip-stale-timings loop in `brand_variant.py:130-133` also visits `sheet.get("segments", [])` (some deep-explainer sheets use `segments[].beats[]`), even though `demo/canonical` has none — see RUN-LOG §5, no `segments` in output.

## Known limitation, honestly labelled

- `brand_variant.py` does not validate that the referenced `charter` file (`CLAUDE-BRAND.md`, `brands/nbb.md`, `brands/hai.md`) exists on disk — it only stamps the path into metadata. On this workstation all three files exist; a broken installation would not be caught until the downstream rewrite step reads them.

## Nothing else claimed

The film does not claim `brand_variant.py` calls Claude, calls Kokoro, or generates audio. The film shows `copy_build_scripts()` in B07 code and mentions it in narration (claim #23). The demo does not print `[variant] copied build scripts:` because `demo/canonical` has no such scripts — that behaviour is consistent with the source (`copy_build_scripts` returns an empty list when the source folder has no matching files).
