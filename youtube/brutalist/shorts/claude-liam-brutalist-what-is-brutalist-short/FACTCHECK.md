# FACTCHECK.md — What Is Brutalist? — Short (9:16, 94.79 s)

*One row per on-screen or spoken claim in the retained cut. Only claims
belonging to kept beats (B00, B01, B04, B06, B07, B09) are listed. Rows for
dropped beats (B02, B03, B05, B08) are removed rather than left dangling.*

| Claim | Where in the Short | Source of truth | Result |
|---|---|---|---|
| "Brutalist is a video toolkit for Humanitarians AI fellows." | B00 narration | `README.md` and `CLAUDE.md` ("brutalist.art is a Brutalist video toolkit for Humanitarians AI fellows and collaborators."). | ✔ verified |
| "It isn't a video editor. It's film as code." | B00 + B01 narration | Editorial framing consistent with the toolkit's doctrine (`CLAUDE.md §Rules 3, 5`, `docs/PIPELINE-SAFETY.md`). | ✔ framing supported |
| "The recipe lives on GitHub, the rendered film lives on Drive, and the version history lives in commits." | B00 narration | `docs/FELLOWS-SUBMISSION.md §GitHub for source; Drive for media`. | ✔ verified |
| "Brutalist is the plain-text recipe your film is built from." | B01 corrected line + narration | `runtime/prose/teardown/PROSE.md` and the schema (every beat has `narration_text`, `shot`, `actual_duration_s`). | ✔ verified against schema |
| "Change the recipe, run the pipeline, and a new film comes out." | B01 narration | `runtime/scripts/compile.py` reads `beat_sheet.json` and produces `<slug>.mp4` — the observed loop. | ✔ demonstrated |
| Edited-field demo: `"greeting": "Ciao, Liam"` → `"Hola, Liam"` yields a swap in only that beat. | B04 WibChange visuals + narration | Verified during authoring of the parent: WibChange's rendered greeting is a pure function of the schema; the on-screen before/after matches what a `--only B00` re-render would produce. | ✔ demonstrated |
| Shell line: `python3 remotion_scenes.py --only B00` | B04 WibChange overlay | Actual documented flag (`python3 runtime/scripts/remotion_scenes.py --help`). | ✔ verified against script |
| "Brutalist does not upload." / "renders a 4K file and stops." | B06 narration + WibNotClaims row 1 | `CLAUDE.md §Rule 5` ("Never publish — render instead. There is no publishing machinery here: no staging folder, no credentials, no upload."). | ✔ verbatim doctrine |
| "Kokoro is local, and Claude runs on your subscription." | B06 narration + WibNotClaims row 2 | `README.md` ("Free by default — Kokoro, Manim, Remotion, no account required."), `setup` script, `CLAUDE.md §OPTIONAL UPGRADE`. | ✔ verified |
| "Not a judge of taste. It will render any bad idea." | B06 narration + WibNotClaims row 3 | `skills/make/ai-explainer/SKILL.md §Hard rules — VISUAL QC LAW / DOUBLE-CHECK LAW` (judgment on the human). | ✔ framing supported |
| Three-line verdict (recipe is text / pure function / judgment stays yours) | B07 WibVerdict artifact | Each line points back at a beat the viewer just watched: line 1 ↔ B01, line 2 ↔ B04, line 3 ↔ B06. | ✔ internally consistent |
| "For Humanitarians AI." + `@HumanitariansAI` handle | B09 outro | `CLAUDE-BRAND.md §Channels` and `docs/FELLOWS-SUBMISSION.md §Review and publishing responsibilities`. `WibOutro916` hardcodes the handle because `OUTRO-LOCK.md` locks `ClaudeTitleOutro` to `@NikBearBrown`. | ✔ correct handle |

## Claims deliberately NOT made in the Short

- No promise of "unlimited Claude use."
- No implication that a local 4K master implies YouTube 4K processing.
- **No paste-ready clone / `./setup --install` instructions** — B08's fellows
  CTA is dropped from this cut. Anyone the Short reaches on Shorts distribution
  should be routed to the 16:9 long or the parent 9:16 companion for the
  installer, not to instructions the Short itself did not read aloud.
- No fabricated Professor Bear or fellow signatures.
- No claim about six pipeline stages (B03 dropped) or four-vs-five labor split
  (B05 dropped). The Short does not restate what it did not show.

## Framing decisions inherited from the parent

- "Read the JSON, read the film" (B07 verdict line 1) remains a rhetorical
  compression, not a quote. It restates the correction B01 made on screen.
- The `@HumanitariansAI` handle in `WibOutro916` is a HAI-channel substitute
  for the `ClaudeTitleOutro`'s locked `@NikBearBrown`, per `OUTRO-LOCK.md`.

## Approval status

All `metadata.approvals.voice.status = pending` — carried from the parent
9:16 companion. No approvals are fabricated for this Short. Bear watches the
cut before any human decision to publish.
