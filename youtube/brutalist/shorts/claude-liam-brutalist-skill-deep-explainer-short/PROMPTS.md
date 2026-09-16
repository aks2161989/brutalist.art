# PROMPTS.md — The deep-explainer Skill — Short

Derivative cut. No new prompts were authored; no narration was regenerated;
no LLM text generation happens at render time. This file records the
prompts that are still visible in the retained beats.

## Retained on-screen prompts

### Cold-open ask (B00, on screen)

```
what does the deep-explainer skill actually do differently from ai-explainer?
```

Displayed RESULT lines (three, cold-open answer):

```
extends ai-explainer; adds an act structure
vox is evidence, not texture — no quota
two hard gates the parent chassis lacks
```

## What is NOT in this Short

- The long's B15 YOUR TURN paste-in (a full paste-ready `claude "…"` command)
  was dropped for length. It remains in the parent long's `PROMPTS.md`.
- No new prompts were generated for this Short.

## Titles / greetings (authored deterministically upstream)

- Cold-open greeting: `Namaste, Liam` (Hindi one-word hello).
- Outro title: `The deep-explainer Skill.` (locked to the supervisor's `episode.title`).
- Hesitant-writer seed: `deep-explainer-2026-09-08` — deterministic; identical performance every render.

## What was NOT prompted

- No external image generation (no Higgsfield, no Flux, no nano-banana).
- No Kokoro voice was cloned; `am_onyx` is a preset.
- No third-party assets pulled from the web at render time.
- No new audio was regenerated in this cut (`--no-outro-rewrite`).
