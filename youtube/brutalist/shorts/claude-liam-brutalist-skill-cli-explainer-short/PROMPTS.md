# PROMPTS.md — The cli-explainer Skill

Every composer beat in the reel shows a text field the viewer could paste back
into their own Claude Code session. All four are anchored to real skill triggers
present in `skills/make/cli-explainer/SKILL.md`.

## B00 — the cold-open ask

Ask: `What does typing \`cli\` at Claude actually do in this toolkit?`

Result lines rendered on the composer card:
1. `it resolves to skills/make/cli-explainer/SKILL.md`
2. `365 lines of markdown Claude reads before drafting`
3. `the file writes the reel — not a screen recorder`

Verified against `./art cli-explainer` (demo/01) and `wc -l skills/make/cli-explainer/SKILL.md`.

## B04 — the actual trigger

Command: `cli The cli-explainer Skill`

Verbatim shape from SKILL.md §Trigger: `cli [concept | chapter | idea] [--tool …] [--persona …] [--out …]`. The concept slot here IS this episode's title.

## B07 — the revision (adds --tool codex)

Command: `cli The cli-explainer Skill --tool codex`

`--tool codex` is a real, registered skin per SKILL.md §Skins ("codex → the CODEX
interface — REAL, not reserved. Written by Codex itself…"). The revision demonstrates
the exact behavior called out in §"Converting a sheet between skins".

## B11 — the paste-ready handoff (READ AND DISCUSSED per HANDOFF LAW)

```
Use cli-explainer to build a Brutalist reel about the smallest command in my
own workflow. Read skills/make/cli-explainer/SKILL.md first, then propose a
beat sheet before you draft narration.
```

Discussed in narration: "The bite is the second sentence. You are asking
Claude to read the file, not summarize its name." — the second sentence forces
a real-source read instead of a summary hallucination, and asking for a beat
sheet BEFORE narration matches the SKILL.md's own "the reel USES the skill to
demo the skill" pattern from the skill-teardown modifier.

## Prompts NOT included (would violate reel policy)

- No prompt shows `--dangerously-skip-permissions`. The reel would not
  demonstrate a destructive shortcut.
- No prompt asks Claude to publish or push to Git. Nothing in this reel
  authorizes upload.
- No prompt names an API-key-gated tool as the primary path. The reel's
  default `--persona liam` maps to Kokoro `am_onyx` — free per SKILL.md
  §Trigger.

## Expected artifact + test of success (for B11)

**Expected artifact:** a new folder under `youtube/brutalist/<slug>/` with
`beat_sheet.json`, `SCRIPT.md`, `SOURCES.md`, `SHOTLIST.md`, and the same
supporting paperwork this reel ships with.

**Test of success:** Claude's *first* response should quote at least one line
from `skills/make/cli-explainer/SKILL.md` — proving it read the file. If the
first response is a summary of the file's *name* (or an invented spine that
doesn't match the doctrine), the prompt failed and the viewer should re-ask.
