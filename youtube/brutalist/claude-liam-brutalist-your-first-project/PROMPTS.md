# PROMPTS.md — Your First Brutalist Project

Every prompt that appears in a composer beat is recorded here verbatim. These
are paste-ready — they will resolve against the local toolkit for a fellow who
already has Claude Code installed and the `brutalist.art` repository cloned.

## B00 — the cold-open ask (illustrative first ask)

```
claude "make me a 60-second Brutalist AI Explainer about how ribosomes read mRNA — 12 beats, Kokoro am_onyx, stop at the review cut"
```

Purpose: shows a real starter ask on screen. Not run against a live model in
this build; the isolated toolkit's `ai-explainer` skill and the local Kokoro
would carry it if it were.

## B03 — the specific first ask (worked example)

```
claude "in this folder, use skills/make/ai-explainer to make a 60-second AI Explainer on how ribosomes read mRNA. 12 beats, Kokoro am_onyx, review cut only."
```

The extra "in this folder" and "review cut only" phrasing is the point the beat
teaches: a specific ask names its skill, its target length, its voice, and a
hard stop before anything final is built.

## B06 — the one-beat revision ask

```
claude "beat five is too long. cut the narration to twenty words, regenerate its audio, re-render its scene, and rebuild only the review cut."
```

Purpose: the ONE-BEAT REVISION LAW. Names the beat, gives the constraint,
names the three actions the pipeline should chain (audio → media → clip →
review-cut). The B07 diff card shows what actually gets modified on disk.

## B10 — the "Your Turn" handoff prompt

```
claude "in this folder, use skills/make/ai-explainer to make a 60-second Brutalist AI Explainer about [my one tiny question]. 12 beats, Kokoro am_onyx, stop at the review cut so I can watch it before anything is submitted."
```

This is the reel's actual handoff — the viewer is meant to swap in their own
tiny question. Narration reads the prompt aloud and then discusses what a good
vs bad first ask looks like, per HANDOFF LAW.

## What was NOT put into a live model

- No live `claude` invocation against a paid API was made to build this reel.
  The audio, visuals and cut were all produced by the local free pipeline
  (Kokoro `am_onyx` + Remotion + `compile.py`).
- No `./setup --install` or `./art keys` run was performed as a "demo" —
  those would touch remote services and are explicitly banned by the brief.
  The isolated toolkit is already installed and its readiness was verified
  by `./art scenes --check` calls logged in `demo/scenes-check.log`.
