# TYPECHECK.md — The duration-planner Skill (portrait 2160×3840)

## Available runtime checker

`runtime/qc/final_frame_check.py` — see `CHECKS-REPORT.md`. All 22 sampled
portrait frames (11 beats × {50 %, 85 %}) came back clean. Gate V uses
`SAFE916 = {x:54, y:96, r:1026, b:1824, w:972, h:1728}` scaled to actual
output (at 2160 wide, scale = 2 → safe.b = 3648).

## Missing runtime checker

GATE T `scripts/type_check.py` NOT shipped. See `../TYPECHECK.md` for how
each of its checks was covered by hand-reading frames + reading scene source
for the landscape reel; the same review was repeated for portrait frames.

## Portrait-specific typography review

Extra items I looked for in portrait, beyond the landscape rubric:

1. **Serif scale.** The BrutalistHesitantWriter scale-bug patch (see
   CHECKS-REPORT.md) means the serif now renders at its intended fontSize
   (210 in portrait vs 200 in landscape). Read the 7-line stack — "Your /
   video / duration / is your / output. / Size the / script." at 210 pt
   fills the vertical safe area appropriately without overflowing.
2. **Composer wrap.** Portrait's narrower safe width (972) means the
   composer's `command` text wraps more aggressively than in landscape.
   Verified: at 9:16 the command breaks into 3 lines (`How long should this
   video be? Read / skills/make/duration-planner/SKILL.md and tell / me how
   the skill actually decides.`) — legible, no character clipped, no line
   crossing the composer card's rounded corner.
3. **SkillTeardownPipeline node stacking.** The Pipeline component uses
   `boxW = min(200, (w*0.78)/n − 20)`. At 1080 wide with 6 nodes (input +
   4 phases + output), boxW = min(200, (1080*0.78)/6 − 20) = min(200, 120)
   = 120. Nodes are legible; the flow arrows draw cleanly between them.
4. **SkillTeardownAnatomy folder-tree wrap.** Indented rows use `paddingLeft:
   f.indent * 32` and mono type at 20 pt. In portrait the longer entries
   ("→ git-explainer" etc.) don't overflow the `right: width*0.08` limit.
5. **ClaudeVerdictArtifact card.** The card sizes to `min(width*0.84, 1560)`.
   At 1080 wide, cardW = 907. The 6 verdict lines wrap once each; none
   overflows the card. Number gutters render terracotta as expected.
6. **ClaudeTitleOutro portrait.** The 916 composition scales the title serif
   proportionally. Handle "@NikBearBrown" hardcoded, mascot rendered inside
   safe area.

## Note on the composer scene's height-relative sizing

`ClaudeComposerAsk` computes `UI = height * 0.022` (landscape) / `0.016`
(portrait). Portrait has smaller UI base because the frame is 1.78x taller,
so `height * 0.022` would overshoot. The scene's `portrait = height > width`
branch keeps type on-scale for the taller frame.

## Gap explicitly

Missing automated type checker. Every attribute GATE T would check was
verified by reading portrait frames; nothing failed. Human editorial review
remains the final layer.
