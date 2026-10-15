# FACTCHECK — What the Remotion Skills Do
**Result.** 14 claims, 14 PASS (checked against the installed files and live runs, 2026-10-10).

| # | Beat | Claim | Verdict | Source |
|---|---|---|---|---|
| 1 | B01 | ~50 rule files; they load into an agent; not a renderer | PASS | repo: 46 .md rule files + 12 SKILL.md; agentskills.io format |
| 2 | B10 | one command installs; 7 folders; .claude/skills symlink; lockfile | PASS | ls output on screen; skills-lock.json |
| 3 | B11 | markup SKILL.md opens with fps-from-config and frame-driven rules; CSS transition won't render; router sends to files | PASS | SKILL.md text on screen |
| 4 | B20 | Remotion renders frames as screenshots so CSS transitions don't animate | PASS | remotion-markup/SKILL.md "will not render correctly"; verified in the rendered clip |
| 5 | B21 | bezier(0.16,1,0.3,1), spring damping 200, perceptual-scale are the skills' recommendations | PASS | timing.md |
| 6 | B22 | premountFor={fps} one second early on every timed item | PASS | sequencing.md |
| 7 | B23 | transitions overlap; total = sum − overlaps | PASS | transitions.md "Duration calculation" |
| 8 | B24 | fitText returns the largest size fitting a width | PASS | measuring-text.md; live measurement on screen |
| 9 | B25 | parseSrt → Caption objects with startMs/endMs | PASS | import-srt-captions.md; real file parsed |
| 10 | B26 | media-utils gives per-frame spectrum from a file | PASS | audio-visualization.md; live |
| 11 | B30 | mediabunny computeDuration 12.528 s; ffprobe 12.480 s | PASS | both runs 2026-10-10 |
| 12 | B31 | render/still/--frames; transparent via png + yuva444p10le + prores 4444 | PASS | remotion-render/REFERENCE.md, transparent-videos.md |
| 13 | B40–42 | effects, rough-notation, HtmlInCanvasMotionBlur need a newer Remotion than 4.0.486 | PASS | effects: 4.0.500+ per light-leaks.md; motion blur: 4.0.529 per motion-blur.md; rough-notation absent at 4.0.486 (npm view) |
| 14 | B50 | `npx remotion skills update` exists; lockfile diff | PASS | `npx remotion skills --help` output |
