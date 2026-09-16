# CHECKS-REPORT.md — The deep-explainer Skill (vertical, run_id 9a0276f36c7f460da489b867130af37b)

Written after compile.py final compile and Gate V (final_frame_check.py) for this
invocation (2026-09-11). Supersedes the 2026-09-08 report.

## Aspect

- 9:16, 2160×3840 (native portrait composed at 1080×1920, rendered --scale=2), 24fps.
- File: `exports/vertical/claude-liam-brutalist-skill-deep-explainer-vertical.mp4`
- Duration: 216.2 s (previous: 214.0 s; diff: B07 narration extended from 14.89s to 17.13s).

## Source change since 2026-09-08 render

Same as landscape — SKILL.md shifted to "executed examples, data and diagrams" as preferred
body mode; B07 updated to reflect this. See landscape CHECKS-REPORT.md for full diff.

## Portrait structure

Native portrait — every beat uses a 916-suffix composition variant:
- B00: ClaudeComposerAsk916
- B01: BrutalistHesitantWriter916 (portrait-aware scale patch applied in previous build)
- B02/B12: SkillTeardownAnatomy916
- B03/B06/B07/B08/B10/B11/B13: SkillTeardownMechanism916
- B04: SkillTeardownPipeline916
- B14: ClaudeVerdictArtifact916
- B15: ClaudeComposerAsk916 (Your turn.)
- B16: ClaudeTitleOutro916

No beats cut from landscape — all 15 beats present in portrait.

## Gate V — final_frame_check.py

```
python3 runtime/qc/final_frame_check.py <vertical_reel> \
  --mp4 <reel>/exports/vertical/...mp4
```

Result: `Frames sampled: 30 · BLOCKER: 0 · MAJOR: 0 — Clean.`
Gate V uses SAFE916 (x=54, y=96, r=1026, b=1824) for portrait frames.

Report: `vertical/_qc/REPORT.md`. Beat sample frames inspected:
- B00-50pct: ClaudeComposerAsk916 — stacked portrait layout, no bleed.
- B07-50pct: SkillTeardownMechanism916 — "Executed examples first." heading, body text
  wraps cleanly to 1080px portrait width, quote card multi-line readable,
  "EXECUTED EXAMPLES FIRST" verdict pill within SAFE916. Good canvas fill.
- B16-50pct: ClaudeTitleOutro916 — title and @NikBearBrown within portrait safe area.

## Known skin-lint false positives

compile.py prints skin-lint warnings for B00 (ClaudeComposerAsk916 vs expected
ClaudeComposerAsk) and B16 (ClaudeTitleOutro916 vs expected ClaudeTitleOutro). These are
documented false positives — the lint matches only the exact landscape pattern names, not
their 916 portrait siblings. Not Gate V defects.

## Known cosmetic finding (carry-over from previous render)

SkillTeardownPipeline916 in B04: the last "Title outro" node overlaps the footer note and
spark line. Gate V's ink-bbox sampling did not flag this (bbox is fine). Flagged for human
reviewer; component fix out of scope for this episode.

## Previous portrait-specific repairs (from 2026-09-08, still in place)

- **BrutalistHesitantWriter portrait scale patch** — portrait-aware min(w/1080, h/1920)
  scale; portrait B01 uses fontSize=140, lineSpacing=2.5, 4-line text.
- **channel_title portrait bleed fix** — metadata.channel_title removed from vertical
  beat_sheet.json; handle appears in outro and folder chip only.

## Post-render conclusion

Gate V clean. Master mp4 decoded, exact-dimension and audio-decode verified by compile.py.
Human viewing/editing is next.

## Addendum — verification run_id 3675182de1474e65a36f82973472df95 (2026-09-12)

This invocation resumed after a Claude usage-limit pause. No rebuild was needed;
the video file hash (`cca06ebdf6fc…`) is unchanged. Fresh QC frames extracted at
`vertical/_qc/frames-3675182de1474e65a36f82973472df95/`. All frames inspected via Read
tool and confirmed matching the prior Gate V report: correct portrait scene content,
no bleed, no slates, no captions. VISUAL-REVIEW.json updated with current run_id.

## Addendum — verification run_id 2a3fc66d1cac49888a8086a1c9781797 (2026-09-12)

This invocation resumed after a Claude usage-limit pause. No rebuild was needed;
the video file hash (`cca06ebdf6fc0f2ca17974bf9ce8d0da2c35674ffad1840a5051b45e03ec1d05`) is
unchanged. Fresh QC frames extracted at
`vertical/_qc/frames-2a3fc66d1cac49888a8086a1c9781797/`. All frames inspected via Read
tool: first-frame (ClaudeComposerAsk916 portrait cold-open, @HumanitariansAI chip, correct
breadcrumb), B01-50pct (BrutalistHesitantWriter916 4-line "deep-explainer / is / a deeper /
ai-|" filling portrait safe area, excellent BLUF coverage), B07-50pct
(SkillTeardownMechanism916 "Executed examples first." heading, body text reflowed cleanly to
portrait width, quote card 2-line wrap, verdict pill within SAFE916), B16-50pct
(ClaudeTitleOutro916 title wraps to two lines, @NikBearBrown per OUTRO-LOCK.md, horizontal
rule borders at top/bottom, no bleed). All frame hashes match prior run_id 1acd0dfc…
extraction — video byte-identical. VISUAL-REVIEW.json updated with current run_id.
