# PROMPTS.md — Your First Brutalist Project (Short, 9:16)

Every prompt that appears in the retained composer beats is recorded here verbatim. These are paste-ready — they will resolve against the local toolkit for a fellow who already has Claude Code installed and the `brutalist.art` repository cloned. The Short only shows composer beats B00, B03 and B10; the parent's B06 revision prompt was dropped and is not on screen here.

## B00 — the cold-open ask (illustrative first ask)

```
claude "make me a 60-second AI Explainer about how ribosomes read mRNA — 12 beats, Kokoro am_onyx"
```

Purpose: shows a real starter ask on screen. Not run against a live model in this build; the isolated toolkit's `ai-explainer` skill and the local Kokoro would carry it if it were.

## B03 — the specific first ask (worked example)

```
claude "use ai-explainer to make a 60s reel on how ribosomes read mRNA. 12 beats, am_onyx, review cut only."
```

The "review cut only" phrasing is the point the beat teaches: a specific ask names its skill, its target length, its voice, and a hard stop before anything final is built.

## B10 — the "Your Turn" handoff prompt

```
claude "use skills/make/ai-explainer to make a 60s Brutalist AI Explainer about [my tiny question]. 12 beats, am_onyx, stop at the review cut."
```

This is the reel's actual handoff — the viewer is meant to swap in their own tiny question. Narration reads the prompt aloud and then contrasts a good vs bad first ask.

## What was NOT put into a live model

- No live `claude` invocation against a paid API was made to build this Short. The audio, visuals and cut were all produced by the local free pipeline (Kokoro `am_onyx` + Remotion + `compile.py`) — for both the parent portrait companion and this derivative.
- The Short reuses the parent's per-beat `mp3/` and `media/` files unchanged; no regeneration happened for retained beats. The compile receipt at `exports/short/*.verified.json` lists the input SHA-256s.

## Prompts dropped with the parent beats (recorded for traceability)

The B06 one-beat revision prompt and B10-parent's longer form both live in the parent portrait companion's `PROMPTS.md`. They are not on screen in this Short.
