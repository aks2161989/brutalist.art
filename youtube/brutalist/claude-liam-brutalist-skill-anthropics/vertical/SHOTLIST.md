# SHOTLIST.md — The anthropics Skill

*Every beat carries a `shot.show` block naming what the viewer WATCHES —
SHOW-DON'T-TELL LAW binds at authoring time. Numbered by beat_id.*

## B00 · Cold open — ClaudeComposerAsk
- **Composition** `ClaudeComposerAsk` (landscape) / `ClaudeComposerAsk916` (portrait).
- **Show:** the Claude composer types the ask `Tear down the anthropics skill. What does it actually do, not just what it says?` The send button arms; three result lines fade in: "reads the artifact, not the docs"; "four modes: --repo, --paper, --content, --capability"; "publishes never." Greeting `Hej, Liam` sits above the composer. Footer chip: `@HumanitariansAI`.
- **Signals:** narration introduces "Liam, in for Bear" in the first breath (IN-FOR-BEAR LAW). ASK is answered on screen (COLD OPEN LAW).

## B01 · BLUF — BrutalistHesitantWriter
- **Composition** `BrutalistHesitantWriter` (same registered scene for both aspects — geometry scales from a 1920×1080 reference).
- **Show:** the writer types "The anthropics skill is a tutorial channel." The phrase `tutorial channel` flashes terracotta (about-to-be-deleted); it is deleted and replaced with `journalism beat`. Then the second line types in: "It reads the artifact, not the docs." Final sentence stands.
- **Seed** `anthropics-bluf-2026` (deterministic; identical performance every render).
- **`lead_silence_s: 0.8`** so the typing has a head start before narration lands.
- **Signals:** the correction is the reel's actual misconception (per EXECUTIVE-SUMMARY LAW). Palette `ink=CLAUDE.INK`, `accent=CLAUDE.SPARK`, `bg=CLAUDE.PAGE`.

## B02 · FRAMEWORK · Anatomy — SkillTeardownAnatomy
- **Composition** `SkillTeardownAnatomy`.
- **Show:** an eyebrow reads `SKILL · ANATOMY`. A serif title reads "One SKILL file. One hundred and forty-two lines." Below, the folder tree renders one file at a time:
  - `skills/make/anthropics/`
  - `└── SKILL.md  · 142 lines` (accent = terracotta; tag = "doctrine")
  - `references (read too):`
  - `├── skills/make/git-explainer/  · dispatch: --repo`
  - `├── skills/make/ai-paper/  · dispatch: --paper`
- A callout box: "The **SKILL.md is the instruction**. The doctrine is short; the discipline is what does the work."
- **Spark line:** "Small file. Big discipline."

## B03 · FRAMEWORK · The mode router — SkillTeardownPipeline
- **Composition** `SkillTeardownPipeline`.
- **Show:** eyebrow `SKILL · PIPELINE`. Title "Four modes, one router." Input chip: `any Anthropic artifact`. Five phase nodes reveal left-to-right: `--repo → git-explainer`, `--paper → ai-paper`, `--content → what has changed`, `--capability → run it, show output` (accent = terracotta). Output chip: `episode · or NOT READY`.
- **Footer:** "Read the artifact. Not the paragraph about it."
- **Spark line:** "One router. Four honest questions."

## B04 · MECHANISM · The disqualifier — SkillTeardownMechanism
- **Composition** `SkillTeardownMechanism`.
- **Show:** eyebrow `MECHANISM · ACT 1`. Heading "If it could be read off the docs — it isn't this." Body sentence: "Every episode needs at least one spine beat visible only by opening the artifact and running it." Quote block: the exact SKILL.md sentence (bold). Cite: `anthropics SKILL.md`. Verdict pill: "kills the downstream-of-docs 90%" (positive).
- **Spark line:** "Not the docs."

## B05 · WORKED EXAMPLE · Behavioural probes — SkillTeardownMechanism
- **Composition** `SkillTeardownMechanism`.
- **Show:** eyebrow `MECHANISM · ACT 2`. Heading "Behaviour is the thesis." Body: the six probes named — `network` · `filesystem` · `DEFAULTS` · `gating` · `LICENSE` · `maintenance`. Quote block: "a feature that exists but ships off tells a different story than the paragraph describing it." Cite: `anthropics SKILL.md · --repo behavioural probes`. Verdict pill: "reads the code that runs, not the code that ships" (positive).
- **Spark line:** "Behaviour, not blurb."

## B06 · MECHANISM · The register — SkillTeardownMechanism
- **Composition** `SkillTeardownMechanism`.
- **Show:** eyebrow `MECHANISM · ACT 3`. Heading "Another perspective, not a correction." Body: "Independence, stated once. Situated in a date and a real task. A matching claim is a finding." Quote: "Another perspective, not a correction." Cite: `anthropics SKILL.md · The register`. Verdict pill: "the credential a vendor channel cannot hold" (positive).
- **Spark line:** "Situated. Independent. Honest."

## B07 · FALSIFIABILITY · Where it bites — SkillTeardownMechanism
- **Composition** `SkillTeardownMechanism`.
- **Show:** eyebrow `DESIGN · TELL`. Heading "Where it bites." Body: "Two siblings must exist for --repo and --paper. If they don't, the router has nowhere to dispatch. Fix: install the siblings. Never fake the analysis." Quote: "Never generate an image that poses as evidence of a fact." Cite: `anthropics SKILL.md · generation-honesty law`. Verdict pill: "hard ceiling · high cost" (negative — this is the design's real cost).
- **Spark line:** "Depends on siblings. Trades pop for credibility."

## B08 · VERDICT — ClaudeVerdictArtifact
- **Composition** `ClaudeVerdictArtifact`.
- **Show:** artifact card fills the frame. Title `Verdict`. Heading "The anthropics beat." Five lines, one per row:
  1. A beat, not a topic — four modes under one router.
  2. Reads the artifact. Not the docs.
  3. Behaviour is the thesis; defaults are the tell.
  4. Independence stated once. Situated. Honest about matches.
  5. Never generates evidence. Never publishes.
- No decorations beyond the fixed card.

## B09 · YOUR TURN — ClaudeComposerAsk
- **Composition** `ClaudeComposerAsk` (landscape) / `ClaudeComposerAsk916` (portrait).
- **Show:** the composer, greeting fixed to `Your Turn`. Command typed in:
  `Use the anthropics skill in --capability mode. Compare Claude with one other model on a real task from my own work — a real prompt, real file, dated bench log. Then answer the three review questions from the SKILL file. If any answer is no, report the gap — don't build the episode.`
- Running text: `paste this into Claude Code…`. Output lines (viewer's rubric):
  1. expected: one spine beat visible only by running the artifact
  2. expected: every claim cited to file:line or on-screen output
  3. expected: matching claims allowed to survive — no manufactured gap
- Footer chip: `@HumanitariansAI`.
- **Signals:** the prompt is READ ALOUD and DISCUSSED (HANDOFF LAW).

## B10 · OUTRO — AntOutro / AntOutro916
- **Composition** `AntOutro` (landscape) / `AntOutro916` (portrait). Native custom outro registered ONLY in this reel's isolated toolkit, because the shipped `ClaudeTitleOutro` hardcodes `@NikBearBrown` per `OUTRO-LOCK.md`. Same visual grammar — poster serif title with terracotta terminal punctuation, upper-centered; handle mid-lower — but the handle is `@HumanitariansAI`.
- **Show:** eyebrow `BRUTALIST · EPISODE 05`; terracotta rule; title `The anthropics Skill.` with terracotta period; handle `@HumanitariansAI`; subline `LIAM, IN FOR BEAR.`
- No jingle sound bed; the master audio is Liam's own signoff.
