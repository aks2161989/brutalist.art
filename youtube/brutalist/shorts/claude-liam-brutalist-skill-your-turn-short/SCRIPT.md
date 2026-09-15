# SCRIPT — The your-turn Skill (Short)

Derived from `youtube/brutalist/claude-liam-brutalist-skill-your-turn/vertical/beat_sheet.json`
(parent master SHA-256 `bdeb47c89ce4ecf05cf70313aedee7f0e65a4c14a3f793aaaa2bf8362ee12d5a`).
Whole-beat cut — no narration rewritten, no audio regenerated. Kept 8/14 beats.

Total measured: 131.75s @ 2160×3840, 24 fps. All streams < 180s.

## Retained beats

**B00 · ASK · 17.25s · ClaudeComposerAsk916**
> Hallo, this is Liam, in for Bear. There is a skill called your-turn that most fellows will look at and think it is a whole workflow. It is not. It is a closing-block skill that standardizes the last three beats of every claude-explainer reel, then hands off. So I asked Claude to read the SKILL dot m-d and tell me what it actually rewrites.

**B01 · BLUF · 10.21s · BrutalistHesitantWriter916**
> Watch the writer walk this back. Your-turn is not a whole-reel skill. It is a closing-block skill — the last three Liam beats at the end of every claude-explainer reel, standardized.

**B03 · FRAMEWORK · 18.92s · SkillTeardownMechanism916**
> Here is the block, in fixed order. Beat one — VERDICT, on the artifact card, opens with the handoff line then the full recap. Beat two — YOUR TURN, on the composer, shows a prompt relevant to this specific video and Liam reads the whole thing aloud. Beat three — the title outro, poster serif, Liam re-reads the reel's own title. Three beats, one voice, always closing.

**B09 · MECHANISM (worked example) · 20.08s · SkillTeardownMechanism916**
> Now watch it run — on a synthetic fixture in this reel's demo folder. Dry-run only, no real reel is touched. The script scans the sheet, finds the closing YOUR TURN and OUTRO, cleans the verdict, rewrites the three beats, and writes a report. Changed, skipped, needs prompt, errors. Look at the report — one fixture changed, zero errors, and the notes name every edit the transformer made.

**B10 · FALSIFIABILITY · 20.46s · SkillTeardownMechanism916**
> Now what your-turn does NOT do. It never touches the body. It never publishes. Applying the block and even re-rendering the reel is safe — going public is a separate manual step in YouTube Studio. And the re-render itself is human-triggered per reel, because re-uploading replaces the video file via a NEW ID and the old URL and its views are lost. That is why the SKILL says — batch deliberately.

**B11 · VERDICT · 17.46s · ClaudeVerdictArtifact916**
> So the split. Bookends up to the body — INHERITED from ai-explainer. The closing three beats — OWNED. The handoff line is persona-aware. Drafts dot j-son is the human gate before any spend. The verdict card is fixed once, every reel bigger. And reach elsewhere if the sheet has no your-turn or Liam outro — this skill skips it.

**B12 · YOUR TURN · 22.58s · ClaudeComposerAsk916**
> Your turn. Paste this into Claude Code. Read the your-turn SKILL and its apply script. Then pick one of your own reels — or a synthetic beat sheet fixture — and ask Claude to draft a drafts dot j-son entry for it. First surface the reel's own material — the source chapter, the body beats' narration text — and draft one prompt a curious viewer would paste after watching. Then dry-run apply your turn against that draft and read the report before touching a real reel.

**B13 · OUTRO · 4.79s · ClaudeTitleOutro916**
> The your dash turn Skill. Liam, in for Bear, for at Humanitarians A I.

## Dropped beats (long-form only)

- **B02** SkillTeardownAnatomy916 (folder tree with SKILL.md and apply_your_turn.py) — generic skill scaffolding
- **B04** MECHANISM 1 · persona-aware handoff branch — captured in B11 verdict line 3
- **B05** MECHANISM 2 · drafts.json human gate — captured in B11 verdict line 4
- **B06** MECHANISM 3 · verdict-card fixes (84% width + strip leading numbers) — internal repair detail
- **B07** MECHANISM 4 · Liam reads the whole prompt — already asserted in B03 and shown in B12
- **B08** MECHANISM 5 · outro re-reads the title — already asserted in B03 and shown in B13

## Cut coherence

Every join is a natural narration seam:

- B01 closes "…the last three Liam beats … standardized." → B03 opens "Here is the block, in fixed order."
- B03 closes "Three beats, one voice, always closing." → B09 opens "Now watch it run — on a synthetic fixture in this reel's demo folder."
- B09 closes "…notes name every edit the transformer made." → B10 opens "Now what your-turn does NOT do."
- B10 closes "…batch deliberately." → B11 opens "So the split."
- B11 closes "…this skill skips it." → B12 opens "Your turn."
- B12 closes "…read the report before touching a real reel." → B13 outro.

No "First decision / Second decision" scaffolding leaks in from the dropped MECHANISM cards (B04–B08), because none of the retained beats use that numbering pattern.
