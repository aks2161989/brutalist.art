# SHOTLIST.md — The deep-explainer Skill — Short

Derivative Short at native 2160×3840. Every retained beat reuses the
parent's native portrait render unchanged (dimensions verified 2160×3840,
16:9 aspect check passes). No pantry stills. No new visuals authored.

| Beat | Kind | Scene (portrait) | What's on screen |
|---|---|---|---|
| B00 | REMOTION (cold open) | `ClaudeComposerAsk916` | Greeting "Namaste, Liam"; command types the deep-explainer question; running indicator; three RESULT lines |
| B01 | REMOTION (BLUF) | `BrutalistHesitantWriter916` | Writer types the misconception in serif; "longer" turns terracotta; replacement types in "deeper"; corrected sentence stands |
| B03 | REMOTION (mechanism) | `SkillTeardownMechanism916` | Heading "It extends its parents."; verbatim SKILL.md quote card; verdict pill "INHERITED · not owned" |
| B06 | REMOTION (mechanism) | `SkillTeardownMechanism916` | Heading "Multi-act, not padded."; quote "If the arc lands at 4:40, ship 4:40."; verdict pill "PACING · duration is an OUTPUT" |
| B07 | REMOTION (mechanism) | `SkillTeardownMechanism916` | Heading "The vox quota is dead."; quote "A film whose evidence is text, code, or data correctly has zero vox beats."; verdict pill "VOX LAW · 2026-09-02" |
| B10 | REMOTION (mechanism) | `SkillTeardownMechanism916` | Heading "Gate D1 — the slate previz."; quote "Never present a previz as a finished cut."; verdict pill "FIRST DELIVERABLE" |
| B11 | REMOTION (mechanism) | `SkillTeardownMechanism916` | Heading "Gate D2 — the shopping list."; quote "SHOPPING.md is written after audio lock (never before)."; verdict pill "TRIM > STRETCH" |
| B14 | REMOTION (verdict) | `ClaudeVerdictArtifact916` | Artifact card; heading "The deep-explainer split."; six numbered lines (INHERITED bookends, OWNED middle, Gate D1, Gate D2, REACH FOR IT, REACH ELSEWHERE) |
| B16 | REMOTION (outro) | `ClaudeTitleOutro916` | Title "The deep-explainer Skill." with terracotta period; locked handle @NikBearBrown; slug-seeded mascot |

## Cut decisions (dropped beats)

- B02 (anatomy folder tree) — generic skill anatomy; belongs to the long
- B04 (fixed-spine 6-node reveal) — structural detail; belongs to the long
- B08 (continuity is scoped) — internal contract; without pantry context it does not land
- B12 (output-contract folder tree) — repeats project anatomy already implied by B14
- B13 (extended limitation callback) — the Short's own honesty is that it derives from the long
- B15 (YOUR TURN paste-in) — long-form exercise; not read aloud in a Short

## Fill / conform notes

- All beats reused as `media/<BID>.mp4` (independent copies from the parent).
- `runtime/scripts/compile.py` conformed each clip to its Kokoro audio duration and concatted.
- No endcard (`--no-endcard`), no outro rewrite (`--no-outro-rewrite`) — the parent B16 remains as-is.
- Motion histogram flagged `illustrate: 5/9 (55%)` over the ~40% guideline; the retained pool is small and the source `illustrate` beats are the load-bearing mechanism cards. No pantry to convert.

## Legibility contract per beat

- Cream ground; ink text; ONE terracotta accent per beat.
- All essential text sits inside the portrait safe zone (verified via
  parent's Gate V review; no re-layout was performed).
- Every text container has `maxWidth`; boxes size to content or wrap.
- Un-highlighted elements ≥40% opacity; no gray-on-gray.
