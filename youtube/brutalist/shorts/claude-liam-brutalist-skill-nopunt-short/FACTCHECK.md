# FACTCHECK.md — The nopunt Skill (Short)

The Short reuses the parent reel's Kokoro narration and native-portrait
renders unchanged for the 7 kept beats. Every on-screen claim traces back
to `skills/make/nopunt/SKILL.md` (episode `source_sha256`
`db5dbdc4e0f8f59497d64b7e5665a89405a57e6f93e906a17bd632f1a00b5bf8`;
current isolated-toolkit SHA-256
`ef38a574fe22f2fca1dfa0774bc51681252776f8ef2bd6f2b1e52d6478cab505`)
or to observed toolkit state captured live in the parent's
`demo/nopunt-run.log`.

## Verifiable facts on screen in the Short

| Beat | Claim | Source |
|------|-------|--------|
| B00 | The skill lives at `skills/make/nopunt/SKILL.md` — one file | Observed in the isolated toolkit: `ls skills/make/nopunt/` shows only `SKILL.md`. |
| B00 | It answers "can I draw this, and how?" | SKILL.md opening paragraph — verbatim question. |
| B00, B04 | Only a genuine archival photograph is a legitimate HOLD; everything else animates; unfilled animatable content is a bug | SKILL.md §"The one rule: HOLD vs PUNT" — verbatim quote in B04 quote block. |
| B01 | nopunt is a catalog / routing table you check before filling a beat, not a linter | SKILL.md opening: "Before you place ANY placeholder … consult the catalog below." |
| B05 | Tool routing by shape: Manim = moving mechanism/math/geometry/transform/plotted curve; Remotion = composed card/stat/typography/icon-grid/UI/document/karaoke text; app SKIN = real code/terminal/app/config/schema/diff/trace | SKILL.md §"How to choose the tool" — verbatim bullets quoted on screen. |
| B05 | A short list of named things → FormB card; a few words with nothing to show → FormA card | SKILL.md §"How to choose the tool" — last two bullets. |
| B05 | Six catalog families cover it: Data & quantity; Structure & relationship; Math & mechanism; Enumerated concepts; Code / app / interface; Text bookends | SKILL.md — section headings under "## The catalog". |
| B06 | Five punt costumes: (1) gen-AI clip / pantry still for a concept; (2) unfilled `fill_slates` / `remotion_scenes` slate in the master; (3) FormA card whose narration NAMES a visual; (4) DoodleScene / DoodleChart; (5) STILL src=archive as concept stand-in | SKILL.md §"Punt costumes to reject" — verbatim list quoted on screen. |
| B07 | SHOW / HOLD / CARD is the per-beat classification vocabulary | SKILL.md §"SHOW / HOLD / CARD" — verbatim heading and definitions. |
| B07 | Anything outside SHOW / HOLD / CARD is a PUNT — a bug, not a style choice | SKILL.md §"SHOW / HOLD / CARD" closing line — verbatim. |
| B11 | Handle `@NikBearBrown` on the outro | `OUTRO-LOCK.md` hardcodes the channel handle. Composer beats (B00) use `folderLabel: "@HumanitariansAI"` inside the composer card per the Brutalist playlist. |

## Facts deliberately NOT on screen in the Short

- No model name (Claude 3.x / 4.x, Sonnet / Opus). The skill body is model-neutral.
- No claim that any specific catalog component is guaranteed present in a
  future toolkit revision — the skill explicitly requires the catalog to stay
  synced with `runtime/remotion/src/scenes/` and the Manim scene library.
- No render times, no version numbers, no "current package" claims.
- No handoff / audit prompt (the parent's B10 was dropped for the Short — the
  16:9 long carries the paste-ready audit rubric).
- No `./art scenes` demo screen (parent's B03 was dropped — the pipeline
  walkthrough belongs in the 16:9 long).
- No `TEMPLATE-MISSES.md` reference on screen (parent's B08 was dropped —
  the falsifiability / miss-logging behaviour belongs in the 16:9 long).

## Adaptations preserved from the parent

- **Handle** — `ClaudeTitleOutro916` hardcodes `@NikBearBrown` per
  `OUTRO-LOCK.md`; the composer card on B00 carries `folderLabel:
  "@HumanitariansAI"` for the playlist.
- **B01 hesitant writer** — single-token trigger `linter` → `catalog`, portrait
  design surface, three compact lines to satisfy Gate V's 55% fill minimum at
  2160×3840. Trigger swap intact; audio unchanged.

## What is NOT claimed

- No claim that this Short has been reviewed by any human. Bear's viewing is next.
- No claim that the Short is published or uploaded — nothing is pushed to Git
  or a streaming service in this session.
- No claim that this Short covers everything nopunt does — B02 (anatomy), B03
  (pipeline), B08 (miss-logging), B09 (verdict recap) and B10 (audit prompt)
  are intentionally reserved for the 16:9 long-form teardown.
- No fabricated approvals, no reused human signatures, no invented URLs.
