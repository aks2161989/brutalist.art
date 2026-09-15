# SHOTLIST.md — The sri-explainer Skill

14 beats. All beats render via `runtime/scripts/remotion_scenes.py`
(foreground, serial). Cream Claude palette (`#FAF9F5` page, `#3D3929`
ink, `#D97757` terracotta accent). No captions, no karaoke. Every
mechanism quote in Mechanism / Anatomy cards is verbatim from
`skills/make/sri-explainer/SKILL.md`.

| Beat | Act | Component | What lands on screen |
|---|---|---|---|
| B00 | ASK cold-open | `ClaudeComposerAsk` | Composer card, greeting "Bonjour, Liam"; command types the sri-explainer ask; 3 RESULT lines fade in. |
| B01 | BLUF | `BrutalistHesitantWriter` | Typed serif line "sri-explainer is\nanother Brutalist explainer" → the phrase "another Brutalist explainer" turns terracotta and is replaced by "a chapter-to-video pipe". |
| B02 | FRAMEWORK / anatomy | `SkillTeardownAnatomy` | Folder-tree reveal of `skills/make/sri-explainer/` — SKILL.md accent, then the two reference/ files, then a callout ("Small doctrine. Big inheritance."). |
| B03 | FRAMEWORK / lineage | `SkillTeardownMechanism` | Heading "It extends its parents.", body block, verbatim quote card with cite, verdict pill "INHERITED · not owned". |
| B04 | FRAMEWORK / pipeline | `SkillTeardownPipeline` | Input node → four phase nodes (HOOK · SETUP · MECHANISM · GROUNDING) → output node OUTRO. Callout under: "This is the chapter's own order." |
| B05 | MECHANISM · Persona | `SkillTeardownMechanism` | Heading "Persona is Sridhar.", body block, verbatim quote card, verdict pill "AUTHOR-VOICED · not Bear, not Liam, not HAI". |
| B06 | MECHANISM · Register | `SkillTeardownMechanism` | Heading "Negate before affirm.", body block, verbatim quote card, verdict pill "REGISTER · from the book itself". |
| B07 | MECHANISM · Derivation-compression | `SkillTeardownMechanism` | Heading "One beat per turn.", body block, verbatim quote card, verdict pill "COMPRESS · never algebra step". |
| B08 | MECHANISM · Golden-test | `SkillTeardownMechanism` | Heading "Every number checks itself.", body block, verbatim quote card, verdict pill "HONESTY · check on screen". |
| B09 | MECHANISM · Handoff | `SkillTeardownMechanism` | Heading "The handoff is the chapter's.", body block, verbatim quote card, verdict pill "HANDOFF · from the chapter". |
| B10 | FALSIFIABILITY · limitation | `SkillTeardownMechanism` | Heading "The honest limitation.", body block naming what a real end-to-end build needs, verdict pill "DOCUMENTED LIMITATION". |
| B11 | VERDICT | `ClaudeVerdictArtifact` | Cream artifact card with title "The sri-explainer Skill" and six verdict lines (bookends inherited · chassis · register · handoff · reach for it · reach elsewhere). |
| B12 | YOUR TURN | `ClaudeComposerAsk` | Composer card, greeting "Your turn."; paste-ready planning prompt types in; runningText "paste this into Claude Code…"; 3-line viewer rubric fades in. |
| B13 | OUTRO | `ClaudeTitleOutro` | Title "The sri-explainer Skill." with terracotta period; hardcoded `@NikBearBrown` handle; slug-seeded mascot animation. |

## Show/Hold/Card classification

- **SHOW × 14** — every beat is a real rendered scene with named
  component; no HOLDs (no archival photographs needed), no bare
  CARDs, no PUNTs, no unresolved slates.

## Motion budget

| Motion | Count |
|---|---|
| type-on | 3 (B00, B01, B12) |
| reveal | 10 (B02–B11) |
| hold | 1 (B13) |

`reveal` carries 10/14 beats (71 %), over the ~40 % pantry cap the
compiler warns about. Accepted, same reason as the nopunt and
deep-explainer skill teardowns before this one: the eight
`SkillTeardownMechanism` beats share their reveal pattern by design —
splitting them into distinct motion languages would sacrifice the
skill-teardown consistency the component was built for.

## Portrait companion

`vertical/beat_sheet.json` mirrors this shotlist with the same 14 beats.
Every scene uses its native `<Pattern>916` composition
(`ClaudeComposerAsk916`, `BrutalistHesitantWriter916`,
`SkillTeardownAnatomy916`, `SkillTeardownPipeline916`,
`SkillTeardownMechanism916`, `ClaudeVerdictArtifact916`,
`ClaudeTitleOutro916`). `SkillTeardown*916` were registered in the
isolated toolkit's `runtime/remotion/src/Root.tsx` for this reel —
they reuse the landscape components' schemas at
`width=1080 height=1920`.
