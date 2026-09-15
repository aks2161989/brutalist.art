# PROMPTS.md — The sri-explainer Skill

## Cold-open ask (B00, ClaudeComposerAsk)

```
What does the `sri-explainer` skill actually do? Read
skills/make/sri-explainer/SKILL.md and tell me the mental model — one
chapter in, what comes out, and what it inherits vs. owns.
```

RESULT lines shown on screen:

- chapter-to-video pipe; extends deep-explainer OR ai-explainer
- narrated in Sridhar's OWN written voice (not Bear, not Liam, not HAI)
- 7 hard rules: derivation-compress, golden-test, negate-before-affirm…

## YOUR TURN prompt (B12, ClaudeComposerAsk, `Your turn.`)

```
Read skills/make/sri-explainer/SKILL.md and skills/make/deep-explainer/SKILL.md.
Then pick ONE chapter of a textbook you know well (a Prof Sridhar
book if you have one; otherwise any physics/CS/stats chapter you can
paste in). Do NOT author beats yet. First surface the chapter's own
act map — HOOK, SETUP, MECHANISM, GROUNDING, DYNAMICS (if present) —
and pick the 2-4 derivation turns worth a beat each. Report which
sibling — sri-explainer, deep-explainer, ai-explainer, cli-explainer —
is actually the right skill for this source, and why.
```

Viewer rubric shown as `output` lines:

- check: did Claude surface the chapter's own act order (not invented)?
- check: 2-4 decision points named — not one beat per algebra step?
- check: honest reroute if the source is not a Sridhar chapter?

## Outro (B13, ClaudeTitleOutro)

Title only. `title: "The sri-explainer Skill"`, `slug:
"claude-liam-brutalist-skill-sri-explainer"`. Handle is hardcoded
`@NikBearBrown` per OUTRO-LOCK.md. Mascot is one of the 18 blessed
crisp-safe animations, picked deterministically from the slug.

## Prompts NOT included on-screen

- Any prompt that would require reading a real Prof Sridhar chapter
  file (not available for this run — see FACTCHECK.md · limitations).
- Any prompt that would run `setup --install`, `art keys`, `git
  clone`, or a paid API call.

## Provenance

Both interactive prompts are original to this reel — they were written
to satisfy the sri-explainer skill's own contracts (chapter as input;
audit-map-before-beats; sibling routing) and were not lifted from any
other reel's beat sheet.
