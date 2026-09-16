# SHOTLIST.md — The deep-explainer Skill

Every beat is machine-fillable. No pantry stills required (VOX LAW correctly
returns zero for a film whose evidence is a SKILL.md — see B07 argument).
Register: Teardown; palette: `claude` (cream `#FAF9F5`, ink `#3D3929`,
terracotta `#D97757`); footer: `@HumanitariansAI`.

| Beat | Kind | Scene / composition | What's on screen |
|---|---|---|---|
| B00 | REMOTION (cold open) | `ClaudeComposerAsk` | Greeting "Namaste, Liam"; command types the ask; running indicator; RESULT lines answer |
| B01 | REMOTION (BLUF) | `BrutalistHesitantWriter` (landscape) / `BrutalistHesitantWriter916` (portrait) | Text written, misconception typed, terracotta-marked, replaced with the corrected framing |
| B02 | REMOTION | `SkillTeardownAnatomy` | Skill folder tree: `SKILL.md` (accent) plus `reference/continuity.md`, `reference/shopping-list.md`, `reference/vox-beats.md` |
| B03 | REMOTION | `SkillTeardownMechanism` | Heading "It extends its parents."; verbatim quote card from SKILL.md; cite line |
| B04 | REMOTION | `SkillTeardownPipeline` | 6-node flow: COLD OPEN → HESITANT WRITER → ACTS I–N → VERDICT → YOUR TURN → OUTRO; terracotta arrows; footer note "acts are 4–8 beats each." |
| ~~B05~~ | ~~FormACard~~ | ~~Act II divider~~ | REMOVED — the divider CARD failed Gate V FILL_MIN≥0.55 by design; narration flows into B06 without an interstitial. |
| B06 | REMOTION | `SkillTeardownMechanism` | Heading "Multi-act, not padded."; quote "If the arc lands at 4:40, ship 4:40."; verdict pill "PACING → duration is an OUTPUT" |
| B07 | REMOTION | `SkillTeardownMechanism` | Heading "The vox quota is dead."; quote "A film whose evidence is text, code, or data correctly has zero vox beats."; verdict pill "VOX LAW (2026-09-02)" |
| B08 | REMOTION | `SkillTeardownMechanism` | Heading "Continuity is scoped."; quote "Never attempt frame-continuity across the whole episode."; verdict pill "MAX RUN = 3 BEATS" |
| ~~B09~~ | ~~FormACard~~ | ~~Act III divider~~ | REMOVED — same Gate V reason; narration flows into B10. |
| B10 | REMOTION | `SkillTeardownMechanism` | Heading "Gate D1 — the slate previz."; quote "Never present a previz as a finished cut."; verdict pill "FIRST DELIVERABLE" |
| B11 | REMOTION | `SkillTeardownMechanism` | Heading "Gate D2 — the shopping list."; quote "SHOPPING.md is written after audio lock (never before)."; verdict pill "TRIM > STRETCH" |
| B12 | REMOTION | `SkillTeardownAnatomy` | Output-contract folder tree: beat_sheet.json (accent), BUILD-PROMPT.md, BUILD-LOG.md, FACTCHECK.md, SHOPPING.md, SOURCES.md, plus `pantry/  media/  manim/  clips/  mp3/` slot dirs |
| B13 | REMOTION | `SkillTeardownMechanism` | Heading "The honest limitation."; body describes what a full end-to-end run needs; verdict pill "DOCUMENTED LIMITATION" |
| B14 | REMOTION (verdict) | `ClaudeVerdictArtifact` / `ClaudeVerdictArtifact916` | Artifact card, heading "The deep-explainer split.", six numbered lines (INHERITED bookends, OWNED middle, Gate D1, Gate D2, REACH FOR IT, REACH ELSEWHERE) |
| B15 | REMOTION (YOUR TURN) | `ClaudeComposerAsk` | Greeting "Your turn."; command types the paste-ready prompt; runningText "paste this into Claude…"; RESULT empty (viewer runs it) |
| B16 | REMOTION (outro) | `ClaudeTitleOutro` / `ClaudeTitleOutro916` | Title "The deep-explainer Skill." — locked outro card with slug-seeded mascot |

## Fill / conform notes

- All beats render as native Remotion compositions. `runtime/scripts/remotion_scenes.py`
  renders each into `media/<BID>.mp4` at the correct aspect ratio.
- `runtime/scripts/compile.py` conforms each clip to the measured Kokoro
  audio duration and concats.
- No slates in the final export. No pantry stills. No Manim (this session's
  isolated toolkit has no Manim-render dependency verified; no beat depends
  on Manim).
- Portrait companion: same beat sheet re-authored in `vertical/` with
  `<Pattern>916` where a native portrait composition exists. Registered new
  portrait variants `SkillTeardownAnatomy916`, `SkillTeardownPipeline916`,
  and `SkillTeardownMechanism916` in the isolated toolkit for the three
  scenes that had no portrait variant shipped.

## Legibility contract per beat

- Cream `#FAF9F5` ground; ink `#3D3929`; ONE terracotta accent per beat.
- All essential text sits inside the 5% title-safe inset (16:9: x 96–1824,
  y 54–1026; 9:16: portrait safe zone).
- Every text container has `maxWidth`; boxes size to content or wrap.
- Un-highlighted elements stay ≥40% opacity; no gray-on-gray.
