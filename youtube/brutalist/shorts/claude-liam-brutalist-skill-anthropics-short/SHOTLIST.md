# SHOTLIST.md — The anthropics Skill — Short

*7 retained beats. Every entry is the parent's shot description, kept only if
that beat survived the whole-beat cut. Numbered by `beat_id`.*

## B00 · Cold open — ClaudeComposerAsk916
- **Composition** `ClaudeComposerAsk916` (native portrait).
- **Show:** the Claude composer types the ask `Tear down the anthropics skill. What does it actually do, not just what it says?` The send button arms; three result lines fade in: "reads the artifact, not the docs"; "four modes: --repo, --paper, --content, --capability"; "publishes never." Greeting `Hej, Liam` sits above the composer. Footer chip: `@HumanitariansAI`.
- **Signals:** narration introduces "Liam, in for Bear" in the first breath (IN-FOR-BEAR LAW). ASK is answered on screen (COLD OPEN LAW).

## B01 · BLUF — BrutalistHesitantWriter916
- **Composition** `BrutalistHesitantWriter916`.
- **Show:** serif stack types "The anthropics is a channel"; `channel` flashes terracotta and is replaced by `beat`; second line "reads the artifact" types in.
- **Seed** `anthropics-bluf-2026-vB` (deterministic).
- **`lead_silence_s: 0.8`**.

## B03 · FRAMEWORK · The mode router — SkillTeardownPipeline916
- **Composition** `SkillTeardownPipeline916`.
- **Show:** eyebrow `SKILL · PIPELINE`. Title "Four modes, one router." Input chip: `any Anthropic artifact`. Four phase nodes reveal left-to-right: `--repo → git-explainer`, `--paper → ai-paper`, `--content → what has changed`, `--capability → run it, side by side` (accent = terracotta). Output chip: `episode · or NOT READY`.
- **Footer:** "Read the artifact. Not the paragraph about it."
- **Spark line:** "One router. Four honest questions."

## B04 · MECHANISM · The disqualifier — SkillTeardownMechanism916
- **Composition** `SkillTeardownMechanism916`.
- **Show:** eyebrow `MECHANISM · ACT 1`. Heading "If it could be read off the docs — it isn't this." Body sentence: "Every episode needs at least one spine beat visible only by opening the artifact and running it." Quote block: verbatim SKILL.md sentence. Cite: `anthropics SKILL.md`. Verdict pill: "kills the downstream-of-docs 90%" (positive).
- **Spark line:** "Not the docs."

## B07 · FALSIFIABILITY · Where it bites — SkillTeardownMechanism916
- **Composition** `SkillTeardownMechanism916`.
- **Show:** eyebrow `DESIGN · TELL`. Heading "Where it bites." Body: "Depends on two siblings (git-explainer, ai-paper) — absent from this toolkit snapshot; the router has nowhere to dispatch. And it forbids the generation of images that pose as evidence of a fact." Quote: "Never generate an image that poses as evidence of a fact." Cite: `anthropics SKILL.md · generation-honesty law`. Verdict pill: "hard ceiling · high cost" (neutral — design cost).
- **Spark line:** "Trades pop for credibility."

## B08 · VERDICT — ClaudeVerdictArtifact916
- **Composition** `ClaudeVerdictArtifact916`.
- **Show:** artifact card fills the frame. Title `The anthropics Skill`. Heading "The anthropics beat." Five lines, one per row:
  1. A beat, not a topic — four modes under one router.
  2. Reads the artifact. Not the docs.
  3. Behaviour is the thesis; defaults are the tell.
  4. Independence stated once. Situated. Honest about matches.
  5. Never generates evidence. Never publishes.
- No decorations beyond the fixed card.

## B10 · OUTRO — AntOutro916
- **Composition** `AntOutro916` (native custom outro registered in this reel's isolated toolkit because the shipped `ClaudeTitleOutro` hardcodes `@NikBearBrown` per `OUTRO-LOCK.md`).
- **Show:** eyebrow `BRUTALIST · EPISODE 05`; terracotta rule; poster serif title `The anthropics Skill.` with terracotta period; handle `@HumanitariansAI`; subline `LIAM, IN FOR BEAR.`
- No jingle sound bed; the master audio is Liam's own signoff.

## Dropped from the Short (see CUT-PLAN.json)

- B02 `SkillTeardownAnatomy916` — folder-tree anatomy of `skills/make/anthropics/`.
- B05 `SkillTeardownMechanism916` — six-probe behavioural checklist + `--paper` reproducibility.
- B06 `SkillTeardownMechanism916` — the "register" (independence, situated, matching-claim).
- B09 `ClaudeComposerAsk916` — paste-ready Your Turn prompt + rubric.
