# PROMPTS — The guests Skill (portrait companion)

The on-screen composer prompts (B00 cold open + B10 Your Turn) are IDENTICAL
in wording to the landscape master — see `../PROMPTS.md` for the full text.
The composer chrome reflows via `useVideoConfig()` inside `ClaudeComposerAsk916`;
no wording differs.

## Portrait-specific authoring

- B01 hesitant writer text is re-wrapped to five lines to keep the widest
  line inside the portrait safe area: `"The guests skill\ncopies the\nfellows spine.\nA board member\nis not a fellow."` — landscape uses four lines. The correction is unchanged: `copies → prunes`.
- `metadata.channel_title` deliberately omitted for the portrait pass — the
  compile-overlay bleeds past portrait `safe.b` (memory
  `feedback_channel_title_portrait_bleed`). The folder chip inside the
  composer beats still carries `@HumanitariansAI`, so the channel context
  is not lost.

## Scene changes inside the isolated toolkit (shared with landscape)

Documented in `../PROMPTS.md`. The three `SkillTeardown*916` wrappers and the
portrait-aware `BrutalistHesitantWriter` scale patch are the same files the
sibling `claude-liam-brutalist-skill-fellows` episode saved into its
`scene-source/` directory (copied verbatim). Their content is not this run's
original work; credit is preserved in `SOURCES.md`.
