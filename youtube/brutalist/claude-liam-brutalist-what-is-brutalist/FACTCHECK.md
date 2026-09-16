# FACTCHECK.md — What Is Brutalist?

*One row per on-screen or spoken claim. Every claim is either read from a
source file listed in `SOURCES.md`, verified against the isolated toolkit, or
labeled as an editorial framing.*

| Claim | Where it lives on screen | Source of truth | Result |
|---|---|---|---|
| "Brutalist is a video toolkit for Humanitarians AI fellows." | B00 ask, narration | `README.md` and CLAUDE.md ("brutalist.art is a Brutalist video toolkit for Humanitarians AI fellows and collaborators."). | ✔ verified |
| "It isn't a video editor. It's film as code." | B00, B01 narration + B02 title | Editorial framing consistent with the toolkit's own doctrine ("Videos travel with their book. Build into `<book>/youtube/<slug>/`… the job is *beat sheet → 4K master*", `CLAUDE.md §Rules 3, 5`). | ✔ framing supported |
| "The recipe lives on GitHub, the rendered film lives on Drive, and the version history lives in commits." | B00 narration | `docs/FELLOWS-SUBMISSION.md §GitHub for source; Drive for media` ("Beat sheet, script, README, code… → GitHub. MP4, MOV, MP3… → Drive."). | ✔ verified |
| "Every beat carries its own line of narration, its own visual, its own timing." | B02 narration + WibRecipe left panel | `runtime/prose/teardown/PROSE.md` and the toolkit's own beat sheet schema (see `examples/746409a8715e.json` — every beat has `narration_text`, `shot`, `actual_duration_s`). | ✔ verified against schema |
| The beat_sheet.json snippet shown in WibRecipe | B02 left panel | Excerpt authored from B00 of THIS reel's beat sheet — the greeting, segment, and pattern shown match the actual `beat_sheet.json`. Not a fabrication. | ✔ verified against file |
| "You write a brief in plain English. Claude drafts the beat sheet. Kokoro reads every narration line aloud." | B03 pipeline narration | `skills/make/ai-explainer/SKILL.md §Flow` (scaffold → narration → audio → visuals → assemble) and `runtime/scripts/generate_audio_kokoro.py` (Kokoro-only, free). | ✔ verified |
| "The audio is measured first. Those measurements become the master clock." | B03 narration + WibPipeline sparkline | `skills/make/ai-explainer/SKILL.md §Step 3 — Audio (the master clock)` ("per-beat MP3 durations become the clock everything conforms to"). | ✔ verbatim doctrine |
| "The compiler muxes it all into a four K master." | B03 narration + WibPipeline final node | `docs/PIPELINE-SAFETY.md §Reviews are not finals` and `runtime/scripts/compile.py --height 2160`. | ✔ verified |
| "Change one field, one thing on screen changes." | B04 narration + WibChange | Verified during authoring: WibChange's rendered greeting is a pure function of `wibChangeSchema.parse({sparkLine})` + frame; the on-screen "before/after" is exactly what a `--only B00` re-render produces after editing the `greeting` field in `beat_sheet.json`. | ✔ demonstrated |
| "Kokoro is local, and Claude runs on your subscription." | B06 narration + WibNotClaims row 2 | `README.md` ("Free by default — Kokoro, Manim, Remotion, no account required."), `setup` script ("Core features require no paid services or API keys."), and `CLAUDE.md §OPTIONAL UPGRADE` (paid Higgsfield is opt-in, never fellows-default). | ✔ verified |
| "Brutalist does not upload." / "renders a 4K file and stops." | B06 narration + WibNotClaims row 1 | `CLAUDE.md §Rule 5` ("Never publish — render instead. There is no publishing machinery here: no staging folder, no credentials, no upload."). | ✔ verbatim doctrine |
| "Not a judge of taste. It will render any bad idea." | B06 narration + WibNotClaims row 3 | `skills/make/ai-explainer/SKILL.md §Hard rules — VISUAL QC LAW / DOUBLE-CHECK LAW` (both put judgment on the human) and Rohan's example beat B05 ("Taste is not a step it does slowly. It is a step it cannot do."). | ✔ framing supported |
| The paste-ready prompt at B08 | B08 composer command + narration | Prompt was authored for this reel; the repository URL matches `README.md` and `BUILD-PROMPT.md`. The instruction to run `./setup --install` matches `setup` line 16 ("`./setup --install` … installs the core Python deps + Remotion's node deps"). | ✔ verified against script |
| "For Humanitarians AI." + `@HumanitariansAI` handle | B09 outro | `CLAUDE-BRAND.md §Channels` (claude-hai chip = `@HumanitariansAI`) and `docs/FELLOWS-SUBMISSION.md §Review and publishing responsibilities`. The custom `WibOutro` component hardcodes the handle because `OUTRO-LOCK.md` hardcodes `@NikBearBrown` in `ClaudeTitleOutro` and this reel is on the HAI channel. | ✔ correct handle |

## Framing decisions logged (not "facts")

- The four-vs-five split ("Four things stay with you. Five things stay with the
  agent.") in B05 counts exactly the rows in `WibDivision`: HUMAN = brief,
  watch, ask, approve (4); AGENT = beat sheet, narration, scenes, master,
  verify (5). The split is a reading of the pipeline, not a doctrine sentence.
- "Read the JSON, read the film" is a rhetorical compression, not a quote.
  Nothing prevents a beat's on-screen visual from being a portrait crop of a
  landscape asset, so the sentence is a promise about the *this-toolkit path*
  as designed, not a universal statement.
- WibPipeline names six stages (BRIEF → BEAT SHEET → AUDIO → SCENES → COMPILE →
  4K MASTER). Notably no PUBLISH stage — the shipped
  `HaiBrutalistE01Pipeline` includes a PUBLISH node but publishing is not part
  of the Brutalist toolkit (see `CLAUDE.md §Rule 5`). Adopting a native
  component let the visual match the doctrine.

## What was NOT claimed (deliberately)

- No promise of "unlimited Claude use."
- No implication that a local 4K master implies YouTube 4K processing.
- No claim that a fresh network install happened during this run; the demos in
  `demo/` are captured from the installed isolated toolkit copy.
- No fabricated Professor Bear notes; the reel does not invoke a fellow's
  signature. All approvals in `beat_sheet.json` remain pending.
