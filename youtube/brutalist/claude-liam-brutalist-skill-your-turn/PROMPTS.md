# PROMPTS.md — The your-turn Skill (ep 21)

Two composers appear in this reel — B00 (COLD OPEN — the ask) and B12
(HANDOFF — YOUR TURN). Both are typed on screen and Liam narrates them; both
are `ClaudeComposerAsk` on the cream stage with the terracotta accent.

## B00 — Cold open composer (the ask)

- greeting: `Hallo, Liam` (German world-hello; single-word)
- topic: `BRUTALIST · SKILL TEARDOWN`
- segment: `The your-turn Skill`
- effortLabel: `Teardown`
- folderLabel: `@HumanitariansAI` (playlist adaptation)

Command typed in composer:
```
What does the `your-turn` skill actually rewrite? Read skills/make/your-turn/SKILL.md
and tell me which beats it touches, what it changes, and what it leaves alone.
```

Result lines (three lines land answered as the ask finishes):
- `closing-block skill — rewrites the last three beats only`
- `VERDICT · YOUR TURN · TITLE — Liam narrates all three`
- `idempotent; skips reels without a your-turn or Liam outro`

Narration: introduces Liam in for Bear ("Hallo, this is Liam, in for Bear.")
and lands the same three-line answer as prose.

## B12 — Your Turn composer (the handoff)

- greeting: `Your turn.` (fixed by the your-turn skill — no persona in this slot)
- topic: `BRUTALIST · YOUR-TURN · YOUR TURN`
- segment: `Draft a drafts.json entry for one reel`
- effortLabel: `Your Turn`
- folderLabel: `@HumanitariansAI`

Command typed in composer (Liam reads the whole thing — HANDOFF LAW):
```
Read skills/make/your-turn/SKILL.md and skills/make/your-turn/scripts/apply_your_turn.py
in full. Then pick ONE reel of your own — or the synthetic beat sheet fixture in
youtube/brutalist/claude-liam-brutalist-skill-your-turn/demo/. First surface the reel's
own material (metadata.source, the body beats' narration_text) and draft ONE drafts.json
entry for it: a prompt 3-5 sentences long, first person, ending in a concrete
multi-part ask that goes one step DEEPER than the video. Then dry-run
apply_your_turn.py against that draft and read the report before touching any real reel.
```

Result lines (viewer rubric):
- `check: did the drafted prompt name the reel's actual claim?`
- `check: is the prompt first-person, 3-5 sentences, multi-part ask?`
- `check: did dry-run report changed=1, needs_prompt=0, errors=0?`

## drafts.json — the human gate

The reel doesn't include a `drafts.json` for a real reel — that would need
individual human review per slug. It ships a synthetic `demo/drafts.json`
paired with a synthetic fixture (`demo/fixture-beat_sheet.json`) to
demonstrate the transformer, verified live in this session.

## No further prompts

No image API prompts, no LLM generation prompts for prose — the reel is a
skill teardown; every card is written in the beat sheet by hand.
