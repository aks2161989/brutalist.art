# FACTCHECK.md — Your First Brutalist Project (Short, 9:16)

Every on-screen claim in the retained beats of this Short is checked against the isolated toolkit that built the parent reel. Nothing here rests on outside quotes or unverifiable metrics. Beats dropped from the parent are not covered — see `SHOTLIST.md` for the mapping.

## Structural claims (on screen in the retained beats)

| Beat | Claim on screen | Verified against | Notes |
|---|---|---|---|
| B00 | The pipeline "reads skills/make/ai-explainer / drafts beat_sheet.json (12 beats) / generates Kokoro am_onyx narration / renders scenes, compiles review cut" | `runtime/scripts/compile.py`, `runtime/scripts/generate_audio_kokoro.py`, `runtime/scripts/remotion_scenes.py`, `runtime/scripts/shorts.py`. `skills/make/ai-explainer/SKILL.md` is present in the isolated toolkit. | The four-line answer is the same sequence `compile.py` performs end-to-end. |
| B01 | "Your first Brutalist project is a claim / Evidence in a short film" (correction from `demo` → `claim` in terracotta) | Landscape parent's B01 narration and the BLUF LAW in `skills/make/ai-explainer/SKILL.md`. The HesitantWriter916 correction is a scripted `triggerWords: "demo"` / `replacementWords: "claim"` swap. | This is the reel's editorial claim, not an empirical measurement — presented as such. |
| B03 | Paste-ready ask: `claude "use ai-explainer to make a 60s reel on how ribosomes read mRNA. 12 beats, am_onyx, review cut only."` | `skills/make/ai-explainer/SKILL.md` accepts a topic, length, beat count and voice; `compile.py` supports "review cut only" as `--review`. | Not run against a paid model in this build; the local Kokoro + Remotion pipeline is what actually produced these clips. |
| B04 | Seven concrete things Claude Code does: `reads skills/make/ai-explainer/SKILL.md` → `drafts beat_sheet.json` → `generates mp3/beat-*.mp3` → `renders media/*.mp4` → `compiles clips/ → review-cut.mp4 at 4K` → `writes CHECKS-REPORT.md and _qc/ frames` → `stops for you to watch` | Each step is an actual script in `runtime/scripts/` (`shorts.py`, `generate_audio_kokoro.py`, `remotion_scenes.py`, `compile.py`) plus this Short's own `CHECKS-REPORT.md` and `_qc/` directory. | This is the reel's spine — same seven items the parent lists. |
| B05 | `review-cut.mp4`: "twelve conformed per-beat clips in clips/ / muxed to one review-cut.mp4 at 3840 x 2160 / narration is the master clock — visuals conform / a per-beat manifest hashes each input for cache / not a Short, not a published master, a receipt / human review is a separate step — you watch it" | `compile.py` conforms per-beat clips to `clips/<BID>.mp4`, muxes to one master, keeps a per-slot SHA manifest, and writes a `.verified.json` receipt. Publication is not automated in this toolkit. | The "twelve" line refers to the parent long's twelve conformed clips (the film the review-cut describes), not this Short's seven — because the retained narration is talking about what `review-cut.mp4` looks like when the standard 12-beat AI Explainer runs. |
| B10 | Paste-ready handoff prompt with `[my tiny question]` placeholder; GOOD/BAD contrast | Same paste-ready pattern as B03; `skills/make/ai-explainer/SKILL.md` HANDOFF LAW documents the review-cut stop. | Viewers are meant to swap in their topic, not run the exact prompt shown. |
| B11 | Title restate + `@HumanitariansAI` + Brutalist-03 sub-mark; Liam sign-off | Isolated `ClaudeTitleOutroHAI916` composition in `runtime/remotion/src/Root.tsx`; narration follows IN-FOR-BEAR LAW. | Stock `ClaudeTitleOutro` hardcodes `@NikBearBrown` — the HAI variant is used precisely so the handle is honest. |

## Persona / channel claims

| Claim | Verification |
|---|---|
| "Liam, in for Bear" — narrator | Kokoro voice `am_onyx` is the working default for `claude-liam` per `skills/make/ai-explainer/SKILL.md` Channels table. B00 narration introduces him; B11 signs off. |
| Handle: `@HumanitariansAI` | Brutalist playlist targets `@HumanitariansAI` per the episode contract. Uses `ClaudeTitleOutroHAI916` which accepts `handle` as a prop; the live stock outro was not modified. |
| No captions, no burned-in transcript | `metadata.captions: false`. `compile.py` did not emit SRT/VTT. |

## What is NOT claimed on screen (in the retained beats)

- **No** claim of paid Claude API or unlimited use. The composers show paste-ready prompts and the artifact cards describe what the local pipeline does; no live model calls happened during this build.
- **No** claim that this Short (or the parent) is published. B05 explicitly frames the compile as a receipt with human review still ahead; the Short itself is not uploaded by this pipeline.
- **No** `./setup --install`, `./art keys`, or live `git clone` shown or claimed.
- **No** fellow's name or private Drive URL.

## Gaps recorded honestly

- **`scripts/type_check.py` and `reference/type-spec.md`** are absent in this isolated toolkit — same gap as the parent. See `TYPECHECK.md`; manual visual typography review was performed instead.
- The dropped parent beats (B02, B06, B07, B08, B09) are not fact-checked here because they are not on screen in this Short. They remain fact-checked in the parent portrait companion's own `FACTCHECK.md`.
