# PROMPTS.md — The nopunt Skill

## Cold open (B00) — paste-ready ask

Rendered inside `ClaudeComposerAsk` as the visible composer command:

> What does the `nopunt` skill actually do? Read `skills/make/nopunt/SKILL.md`
> and tell me — the mental model, not the section headings.

Composer answer lines shown on screen:

1. the anti-punt catalog — one place to check before ANY placeholder
2. HOLD is only a genuine archival photograph — everything else animates
3. unfilled animatable content = PUNT (a bug, not a style choice)

## Handoff (B10) — the viewer's paste-ready prompt

Rendered inside `ClaudeComposerAsk` with `greeting: "Your Turn"`:

> Read `skills/make/nopunt/SKILL.md`. Pick ONE delivered reel of your own at
> `<book>/youtube/<my-slug>/`. Open `beat_sheet.json` and classify every beat
> as **SHOW**, **HOLD**, or **CARD** (§ SHOW/HOLD/CARD). For any beat that
> fits none of the three — quote its `narration_text` and route it to a
> catalog row. At the sheet level, check: (a) FRAMEWORK beat present before
> the first worked example; (b) FALSIFIABILITY beat present that stress-tests
> the framework; (c) YOUR TURN beat carries a scorable rubric. Report the
> punts. Do NOT rewrite.

Viewer rubric (the three output lines on screen):

1. check: every beat classifies as SHOW / HOLD / CARD?
2. check: FRAMEWORK · WORKED-EXAMPLE · FALSIFIABILITY · SCAFFOLDED-TASK · BOOKENDS · NO-SOURCE-NO-VERDICT?
3. check: any narration that NAMES a visual on a CARD beat = PUNT?

## Why the prompt is safe

- **Audits, never rewrites.** The command explicitly closes with "Do NOT
  rewrite." The viewer's own reel is not at risk.
- **Pick a delivered reel.** The viewer targets their own already-shipped
  work, not an in-flight production or a shared branch.
- **Skill file is public.** `skills/make/nopunt/SKILL.md` lives in the DOT
  repo at `github.com/nikbearbrown/brutalist.art`.
- **No API calls, no paid services.** The audit is a Claude Code session
  against local files.

## Not paste-ready in this reel

- No `art keys`, no `setup --install`, no destructive git commands, no
  publishing steps are demonstrated. Setup-instruction beats are outside the
  scope of a skill teardown.
- No prompt suggests running `art vertical` or `art shorts` against a live
  reel — those are separate episodes with their own scaffolding.
