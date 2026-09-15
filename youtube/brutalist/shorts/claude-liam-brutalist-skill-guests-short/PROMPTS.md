# PROMPTS — The guests Skill — Short (9:16 derivative)

Whole-beat cut from the vertical parent. The Short retains B00, B01, B03, B09,
B11. Dropped: B02, B04, B05, B06, B07, B08, B10. See `CUT-PLAN.json`.

## On-screen composer prompt (B00 cold open, retained)

```
What is the `guests` skill? Read skills/make/guests/SKILL.md and
tell me what it actually does with a board member's video.
```

This is identical to the landscape master — `ClaudeComposerAsk916` reflows
the chrome via `useVideoConfig()`; no wording differs between landscape and
portrait.

## Your Turn (B10, DROPPED)

B10's paste-ready dry-run prompt is present in the 16:9 long and the full-length
vertical companion, but is not included in this Short — the detailed assignment
belongs in the long-form treatment. The Short ends at B09 (verdict) → B11
(outro), which provides a complete and self-standing answer without the exercise.

## Portrait-specific authoring

- B01 hesitant writer text is wrapped to five lines to keep the widest line
  inside the portrait safe area:
  `"The guests skill\ncopies the\nfellows spine.\nA board member\nis not a fellow."`
  The correction token is unchanged: `copies → prunes`.
- `metadata.channel_title` deliberately omitted for the portrait pass — the
  compile-overlay bleeds past portrait `safe.b` (memory
  `feedback_channel_title_portrait_bleed`). The folder chip inside
  `ClaudeComposerAsk916` (B00) still carries `@HumanitariansAI`.

## Scene changes inside the isolated toolkit

The three `SkillTeardown*916` wrappers and the portrait-aware
`BrutalistHesitantWriter` scale patch are copied verbatim from the sibling
`claude-liam-brutalist-skill-fellows` episode's `scene-source/` directory.
Their content is not this run's original work; credit is preserved in
`SOURCES.md`. B03 uses `SkillTeardownPipeline916` from this set; B01 uses
the portrait-aware `BrutalistHesitantWriter916`.
