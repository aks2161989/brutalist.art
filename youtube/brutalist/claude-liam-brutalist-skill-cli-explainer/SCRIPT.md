# SCRIPT.md — The cli-explainer Skill

Playlist: Brutalist · @HumanitariansAI · claude-liam · voice `am_onyx` · captions off.

Narration reads a Teardown-voice skill teardown of `cli-explainer` — what the file
is, what it lists, and how the resulting reel is put together. Every claim on
screen is quoted from the toolkit's actual `skills/make/cli-explainer/SKILL.md`
(sha256 in SOURCES.md); every command shown was run in this session against the
isolated toolkit copy.

## Beat-by-beat narration

**B00 — Cold open (ClaudeComposerAsk).**
> Namaste — this is Liam, in for Bear. I asked Claude what happens when I type
> `cli` at the composer, because half the room already has a Claude subscription
> and no idea a skill by that name exists. The answer, when the answer is a file
> a folder away, is worth watching.

**B01 — Hesitant-writer overview (BrutalistHesitantWriter).**
> Here is the whole video in one breath. `cli-explainer` is not a tool that
> records a terminal; it is a set of written instructions that Claude reads
> before drafting the reel. Twelve minutes from now that distinction is the
> only sentence I want you to keep.

**B02 — Skill anatomy (SkillTeardownAnatomy).**
> A skill in this toolkit is a folder. Two files sit under
> `skills/make/cli-explainer`: `SKILL.md`, three hundred sixty-five lines of
> plain markdown, and a `reference/` directory with one example beat sheet.
> That is the whole skill. No compiled binary, no daemon, no service —
> Claude reads the file, and the file writes the reel.

**B03 — The pipeline (SkillTeardownPipeline).**
> The file is not a suggestion. It fixes the shape of every CLI reel to a
> nine-step spine: cold open, problem, ask, code, output, revision, code
> again, better output, summary, hand-off, outro. Same in every reel. The
> creative work happens inside the frame — the frame itself is locked.

**B04 — Ask beat (ClaudeComposerAsk).**
> The ask, verbatim from the trigger table: `cli The cli-explainer Skill`.
> No model version, no temperature — the trigger tells Claude which skill
> to load. The skin defaults to Claude; a persona defaults to Liam. This
> is the only entry point.

**B05 — Actual code (ClaudeCodeBeat).**
> This is the section that owns the video you are watching. It says: the
> body always contains a revision cycle. Not "if there's time" — always.
> A CLI video without a check-and-change is incomplete. That is a rule
> in the skill, not a note in a review.

**B06 — Mechanism 1: verbatim quote (SkillTeardownMechanism).**
> Read it in the file's own words. THE REVISION LAW. Sixteen-by-nine
> videos always contain at least one revision cycle. The one exception
> is the vertical short, which drops the revision to fit the three-minute
> cap. The doctrine names its own edge case in the same paragraph.

**B07 — The revision (ClaudeComposerAsk).**
> The revision — `cli The cli-explainer Skill --tool codex`. One flag, and
> the same spine renders through the Codex composer instead of Claude's. The
> body logic and the bookends don't move; the interface skin does. Nothing
> in the beat sheet has to be rewritten.

**B08 — Actual code (ClaudeCodeBeat).**
> This is how the skin swap is written in the file. A one-to-one rename:
> `ClaudeComposerAsk` becomes `CodexComposerAsk`; `ClaudeCodeBeat` becomes
> `CodexCodeBeat`; `ClaudeTitleOutro` becomes `CodexTitleOutro`. Props
> carry over. It is a substitution, not a re-authoring.

**B09 — Design tell (SkillTeardownMechanism).**
> Here is the design decision I keep coming back to. The skill separates
> the interface skin — Claude, Codex, Onda, GitHub, Shell — from the
> narrative spine. Choose a new tool and the same lesson still teaches.
> That is the thing the file gets right: the spine survives the skin.

**B10 — Verdict (ClaudeVerdictArtifact).**
> The verdict: `cli-explainer` is instructions, not software. It reads
> like an editorial style guide because that is what it is. It doesn't
> record your terminal — it commissions a reel about what you asked Claude
> for. Reading the SKILL beats watching a tutorial.

**B11 — Handoff (ClaudeComposerAsk, "Your turn.").**
> Your turn — here is the prompt, read it with me. `Use cli-explainer to
> build a Brutalist reel about the smallest command in my own workflow.
> Read skills/make/cli-explainer/SKILL.md first, then propose a beat
> sheet before you draft narration.` The bite is the second sentence —
> you are asking Claude to read the file, not summarize its name.

**B12 — Outro (ClaudeTitleOutro).**
> The cli-explainer Skill. Liam, in for Bear.
