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

Rendered inside `ClaudeComposerAsk916` with `greeting: "Your Turn"` (portrait
variant — command shortened from the landscape version so the composer card
plus three output lines fit inside the portrait title-safe area at 2160×3840):

> Read `skills/make/nopunt/SKILL.md`. Pick ONE delivered reel of your own.
> Open its `beat_sheet.json` and classify every beat as **SHOW**, **HOLD**,
> or **CARD** (see § SHOW/HOLD/CARD). For any beat that fits none, quote its
> narration and route it to a catalog row. Report the punts. Do NOT rewrite.

The landscape reel's `narration` still speaks the full three sheet-level
checks aloud (FRAMEWORK / FALSIFIABILITY / scorable rubric). The portrait
command shortens only the on-screen composer text, not the audio.

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
