# Shot list — Short (9:16, 2160×3840)

Eight kept beats, all native portrait Remotion renders copied unchanged from
the parent portrait reel `claude-liam-brutalist-skill-fashionista/vertical/`
via `runtime/scripts/shorts.py --drop B02 B03 B08 B10 --no-endcard
--no-outro-rewrite`. No re-render, no crop, no endcard, parent outro preserved.

| Beat | Act | Duration (s) | Composition (Root.tsx) | Notes |
|---|---|---|---|---|
| B00 | ASK — cold open | 15.00 | ClaudeComposerAsk916 | Composer types the ask about the fashionista skill; send arms terracotta; three result lines fade in. |
| B01 | BLUF — hesitant writer | 15.25 | BrutalistHesitantWriter916 | 4-line serif types out; trigger `tutorial` swaps to `experiment` (single-token trigger per feedback_hesitant_writer_triggers). Portrait fontSize 168 / lineSpacing 1.12 per feedback_hesitant_writer_portrait_scale. |
| B04 | MECHANISM 1 — GATE ASK | 21.08 | SkillTeardownMechanism916 | Heading + body + verbatim quote from SKILL.md ("NEVER name the garment in the ask…"). |
| B05 | MECHANISM 2 — Video is the master clock | 24.75 | SkillTeardownMechanism916 | Heading + body + verbatim quote ("Video is the master clock. If the narration runs long: CUT WORDS. The video does not move."). |
| B06 | MECHANISM 3 — Stated confidence | 26.92 | SkillTeardownMechanism916 | Heading + body + verbatim quote ("Hedging is content, not weakness."). |
| B07 | FALSIFIABILITY — Two error sources | 25.46 | SkillTeardownMechanism916 | Heading + body + verbatim quote ("Nobody else is doing this and it is the most interesting thing the series does."). |
| B09 | VERDICT | 28.67 | ClaudeVerdictArtifact916 | Artifact card, 6 verdict lines revealed one at a time. |
| B11 | OUTRO | 3.71 | ClaudeTitleOutro916 | Title "The fashionista Skill." + hardcoded `@NikBearBrown` handle (OUTRO-LOCK.md). Liam signs off. |

## Dropped beats (from parent portrait reel)

| Beat | Act | Duration (s) | Reason for cut |
|---|---|---|---|
| B02 | FRAMEWORK — anatomy | 27.04 | Generic skill-folder tree; belongs in the 16:9 long. |
| B03 | FRAMEWORK — pipeline | 25.50 | Three-node INTRO/VIDEO/OUTRO diagram; retained mechanism beats carry the same content. |
| B08 | DESIGN TELL — CALLS ledger | 28.54 | Ledger schema deep dive; B09 verdict still names the ledger and the null verdict slot. |
| B10 | YOUR TURN — handoff | 34.08 | 34-second paste-in prompt; Your-Turn is a documented permissible cut for a Short. |

## Motion / brand posture

- Motion histogram (compiler): `reveal:5  type-on:2  hold:1` — compiler warned
  the `reveal` share (5/8 = 62%) exceeds the ~40% pantry cap. This is a
  Short-length artefact: dropping four middle mechanism beats leaves the
  remaining acts weighted toward `reveal`. Documented, not repaired — see
  CHECKS-REPORT.md.
- Skin lint carried forward from the parent's compile: `ClaudeComposerAsk916`
  and `ClaudeTitleOutro916` do not match the landscape-only COLD OPEN LAW /
  OUTRO LAW string check. The 916 portrait wrappers are the correct portrait
  compositions; no repair.
