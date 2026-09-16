# FACTCHECK.md — The nopunt Skill

Every on-screen claim is traced back to `skills/make/nopunt/SKILL.md`
(episode `source_sha256`
`db5dbdc4e0f8f59497d64b7e5665a89405a57e6f93e906a17bd632f1a00b5bf8`;
current isolated-toolkit SHA-256
`ef38a574fe22f2fca1dfa0774bc51681252776f8ef2bd6f2b1e52d6478cab505`) or to
observed toolkit state captured live in `demo/nopunt-run.log`.

## Verifiable facts on screen

| Claim | Source |
|---|---|
| The skill lives at `skills/make/nopunt/SKILL.md` — one file | Observed in the isolated toolkit: `ls skills/make/nopunt/` shows only `SKILL.md`. |
| It answers "can I draw this, and how?" | SKILL.md opening paragraph — verbatim question. |
| HOLD = a genuine archival photograph of a real person, place, document, or event — or a judgment only the creator can make | SKILL.md §"The one rule: HOLD vs PUNT" — quoted directly in B04 verdict pill and B07 body. |
| PUNT = a slot the system can draw/show itself but deferred; every catalog row is animatable, so an unfilled catalog row is a bug | SKILL.md §"The one rule: HOLD vs PUNT". |
| Step zero is `./art scenes "<needs>"` then `./art scenes --check <Name>` | SKILL.md §"Step zero — ask the library"; live-verified in `demo/nopunt-run.log` — three real `./art scenes` invocations captured with real output. |
| A hit is a LEAD; a miss is a design card logged to `TEMPLATE-MISSES.md` | SKILL.md §"Step zero". The miss-logging behavior is described in the skill; the fourth demo command (`ThisSceneDoesNotExist`) shows the `NOT RENDERABLE` return from `./art scenes --check`. |
| Tool routing: Manim owns moving mechanism / math / geometry / transform / plotted curve; Remotion owns composed card / stat / typography / icon-grid / UI / document / karaoke text; the app SKIN shows real code / terminal / app / config / schema / diff / trace | SKILL.md §"How to choose the tool" — verbatim bullets. |
| A short list of named things → FormB card; a few words with nothing to show → FormA card | SKILL.md §"How to choose the tool" — last two bullets. |
| The catalog has six families: Data & quantity; Structure & relationship; Math & mechanism; Enumerated concepts; Code / app / interface; Text (last resort) & bookends | SKILL.md — section headings under "## The catalog". |
| Five punt costumes: (1) gen-AI clip / pantry still for a concept; (2) unfilled `fill_slates` / `remotion_scenes` slate in the master; (3) FormA card whose narration NAMES a visual; (4) DoodleScene / DoodleChart; (5) STILL src=archive as concept stand-in | SKILL.md §"Punt costumes to reject" — verbatim list. |
| SHOW / HOLD / CARD is the per-beat classification vocabulary | SKILL.md §"SHOW / HOLD / CARD" — verbatim heading and definitions. |
| Anything outside SHOW / HOLD / CARD is a PUNT — a bug, not a style choice | SKILL.md §"SHOW / HOLD / CARD" closing line — verbatim. |
| Whole-sheet checklist requires FRAMEWORK beat, WORKED EXAMPLE, FALSIFIABILITY beat, SCAFFOLDED viewer task, four bookends, no source no verdict | SKILL.md §"Whole-sheet teaching-arc checklist" — six checkboxes referenced in B10 handoff. |
| Sibling skills (ai-explainer, deep-explainer, cli-explainer) reference nopunt rather than repeat them | SKILL.md §"Keep in sync" — the catalog is the single source; sibling skills reference it. Confirmed by opening the three sibling files and grepping for `nopunt` references. |

## Live demo transcript (demo/nopunt-run.log)

Four real `./art scenes` invocations were captured 2026-09-08:

1. `./art scenes "a funnel narrowing through three stages"` — 8 real hits
   including `ValuesCompressionFunnel916`, `SycCurriculumStages`,
   `ValuesCompressionFunnel`, `DtlScale`. A hit is a LEAD — open the file.
2. `./art scenes --check ClaudeVerdictArtifact` → `RENDERABLE  16:9  props:
   artifactTitle, artifactHeading, artifactLines`.
3. `./art scenes --check DoodleScene` → `RENDERABLE 16:9` — the tool reports
   renderability truthfully; nopunt's block-list is the reason it is still
   banned as a costume for animatable content.
4. `./art scenes --check ThisSceneDoesNotExist` → `NOT RENDERABLE — no
   <Composition> in Root.tsx. Authoring this is a punt.` — the exact
   miss-shape the skill describes.

## Facts deliberately NOT on screen

- No model name (Claude 3.x / 4.x, Sonnet / Opus). The skill body is model-neutral.
- No claim that any component listed in the catalog is guaranteed present in a
  future toolkit revision — the skill explicitly requires the catalog to stay
  synced with `runtime/remotion/src/scenes/` and the Manim scene library.
- No render times, no version numbers, no "current package" claims.

## Handoff prompt (B10) — verified paste-ready

The prompt asks the viewer to (a) read `skills/make/nopunt/SKILL.md`, (b) open
one of their delivered reels' `beat_sheet.json`, and (c) classify every beat as
SHOW / HOLD / CARD and flag any beat that fits none of the three. The rubric is
grounded in three concrete checks: FRAMEWORK beat present, FALSIFIABILITY beat
present, YOUR TURN carries a scorable rubric — each of which is defined
verbatim in SKILL.md §"Whole-sheet teaching-arc checklist". Safe to run: the
prompt AUDITS, it never rewrites.

## Adaptations / corrections applied

- **Channel handle** — the shipped `ClaudeTitleOutro` hardcodes
  `@NikBearBrown` per `OUTRO-LOCK.md`; the outro's on-screen handle is
  therefore `@NikBearBrown`, not `@HumanitariansAI`. That is per-lock, not a
  bug. Composer beats (B00, B10) use `folderLabel: "@HumanitariansAI"` so the
  inner-composer folder chip reflects the playlist.
- **BrutalistHesitantWriter** — B01 uses a single-token trigger word
  (`linter` → `catalog`) per the trigger-syntax feedback memory.
- **Live demo** — three of the four `./art scenes` invocations in
  `demo/nopunt-run.log` were run against the isolated toolkit copy; the fourth
  is a deliberate miss. No network calls, no publishing, no external services.

## What is NOT claimed

- No claim that this reel has been reviewed by any human. Bear's viewing is next.
- No claim that the reel is published or uploaded — nothing is pushed to Git or
  a streaming service in this session.
- No claim that `./art scenes` (or its `--check` mode) proves a component is
  ideal for a given beat — it proves renderability and returns lead metadata.
  Judgment is still the author's job.
- No claim that a specific model version, package version, or file line count
  is stable across future toolkit revisions.
