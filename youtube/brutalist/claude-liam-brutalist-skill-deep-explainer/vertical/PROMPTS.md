# PROMPTS.md — The deep-explainer Skill

Every rendered beat in this reel is a deterministic Remotion composition
driven by props in `beat_sheet.json`. No LLM text generation happens at
render time. This file records the exact prompts used to author the reel
(cold-open ask, YOUR TURN prompt, and the internal "why this shape"
prompts asked while reading the SKILL.md).

## Authoring prompts (session-internal, for the record)

1. "Read `skills/make/deep-explainer/SKILL.md` end to end. What are the two or
   three design decisions that make it its own skill instead of a longer
   `ai-explainer`?" — used to select which sections to quote in the mechanism
   beats.
2. "Which quotes from the SKILL.md are load-bearing for the film's argument
   and short enough to sit on a card without wrapping past the safe zone?" —
   used to pick the six on-screen quotes in B03/B06/B07/B08/B10/B11.
3. "Which lane / composition matches each mechanism beat?" — resolved via
   `./art scenes <need>` (real output logged in `demo/02-scenes-lookup.txt`).

## Cold-open ask (B00, on screen)

```
what does the deep-explainer skill actually do differently from ai-explainer?
```

Displayed RESULT lines (three, terracotta-accent-free — cold-open answer):

```
extends ai-explainer; adds an act structure
vox is evidence, not texture — no quota
two hard gates the parent chassis lacks
```

## YOUR TURN prompt (B15, on screen, read aloud verbatim by Liam)

```
claude "read skills/make/deep-explainer/SKILL.md, then plan a 5-10 minute deep-explainer of a chapter I care about. Show me the act map and the lane histogram before you author a single beat. If the source is one insight, tell me to use ai-explainer instead."
```

**What to look for in Claude's reply** (also spoken):

- Does Claude name several linked mechanisms, or is it padding one insight?
- Does it push back and route you to `ai-explainer` when the source is one
  insight?
- Does it present the act map + lane histogram BEFORE any narration is
  written (that is the plan gate the skill's workflow demands)?

## Titles / greetings authored deterministically

- Cold-open greeting: `Namaste, Liam` (Hindi one-word hello; rotation policy,
  not repeated in this playlist within the batch).
- Outro title: `The deep-explainer Skill.` (locked to the supervisor's
  `episode.title`).
- Hesitant-writer seed: `deep-explainer-2026-09-08`.

## What was NOT prompted

- No external image generation (no Higgsfield, no Flux, no nano-banana).
- No Kokoro voice was cloned; `am_onyx` is a preset.
- No third-party assets pulled from the web at render time.
