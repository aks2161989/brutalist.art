# SHOTLIST — The duration-planner Skill

Landscape reel (3840×2160 output, composed at 1920×1080 native).
All beats render via `runtime/scripts/remotion_scenes.py` — no hand-rolled
`npx remotion render`, no unresolved slates.

| Beat | Composition (16:9) | Type | Duration (s) | What appears |
|---|---|---|---|---|
| B00 | `ClaudeComposerAsk` | ASK (UI, cold open) | 14.57 | Cream page; composer card; greeting "Sawadee, Liam" types in; command "How long should this video be?" types in; send button arms terracotta; three result lines fade in (duration-is-output; two levers; content_type sets floor). |
| B01 | `BrutalistHesitantWriter` | BLUF (typing) | 15.00 | Serif text writes itself; "target" flashes terracotta then deletes; "output" types in; second couplet "Size the script. Hold to the floor." types in. `lead_silence_s: 0.8`. |
| B02 | `SkillTeardownAnatomy` | FRAMEWORK (folder tree) | 18.79 | Eyebrow SKILL · ANATOMY; title "Small file. Load-bearing rule."; folder tree reveals row by row: `skills/make/duration-planner/` → `SKILL.md` (accent) → `reference/duration-evidence.md` → `scripts/pace_check.py` → the two files the skill READS (`mp3/timings.json`, `beat_sheet.json content_type`); terracotta callout lands: "Duration is an OUTPUT, never a target." |
| B03 | `SkillTeardownPipeline` | FRAMEWORK (flow) | 20.16 | Eyebrow SKILL · PIPELINE; title "Five phases. Runtime is a byproduct."; input node "beat_sheet + timings.json"; four phase nodes — content_type · measure · **floor → hold** (terracotta) · ceiling → split; output node "total runtime · reported" (terracotta ring); footer "Advisory only. The skill never edits the sheet." |
| B04 | `SkillTeardownMechanism` | MECHANISM · ACT 1 | 21.70 | Heading "Duration is an output."; body about 3–4-min mechanism vs 30–60s definition; quote card "Duration is an OUTPUT, never a target."; verdict pill "kills the 30s/1min production myth" (positive). |
| B05 | `SkillTeardownMechanism` | WORKED EXAMPLE | 22.51 | Heading "The consolidation floor."; body reveals the six floor rows inline (title 3–5s; realworld 4–5s; structure 6–8s; data 6–8s; mechanism 6–10s; equation 7–12s); quote card "Floors are minimums, enforced with holds."; verdict pill "the load-bearing rule". |
| B06 | `SkillTeardownMechanism` | MECHANISM · ACT 3 | 25.86 | Heading "HOLD_FLOOR — built in at render."; body describes scene-base holds + assemble.py silence padding + off-switch; quote card "Re-render AND re-assemble together; rendering with one and assembling with the other would desync."; verdict pill "consolidation built in · no manual holds". |
| B07 | `SkillTeardownMechanism` | FALSIFIABILITY (DESIGN · TELL) | 24.32 | Heading "Padding is a coherence violation."; body debunks the 6-minute rule; quote card "Padding to reach 1:00 is as wrong as compressing to reach 0:30."; verdict pill "trades watchtime for schema" (negative — the real cost). |
| B08 | `ClaudeVerdictArtifact` | VERDICT (UI, artifact page) | 18.58 | Artifact card scales in; heading "Small file. Long discipline."; five verdict lines reveal one at a time (output not target; content_type = floor; Kokoro = clock; splits break over-full beats; never pads). |
| B09 | `ClaudeComposerAsk` | YOUR TURN (UI, handoff) | 28.57 | Cream page; composer; greeting "Your Turn"; the full paste-ready duration-planner prompt types in; three-line rubric appears as output. Liam reads the prompt aloud and discusses the three checks. |
| B10 | `ClaudeTitleOutro` | OUTRO | 3.95 | Cream/ink; slug-seeded mascot (18 crisp-safe animations); title "The duration-planner Skill." with terracotta period; handle `@NikBearBrown` beneath (locked per OUTRO-LOCK.md). |

Total narration ≈ **214 s** (3 min 34 s). Landing squarely in the 3–4 minute
band the SKILL.md predicts for multi-decision mechanism content. Not
production-target-shaped.

## Portrait companion (vertical)

Same 11 beats, native 1080×1920 compositions (see `vertical/SHOTLIST.md`).
Every SkillTeardown* component reads `useVideoConfig()` for width/height, so
the layout math naturally reflows tall — headings, folder-tree, mechanism
cards stack vertically. Pipeline uses proportional `boxW = min(200, (w*0.78)/n − 20)`
so nodes compress cleanly at portrait width. The Claude UI compositions have
their own dedicated 916 variants (`ClaudeComposerAsk916`,
`ClaudeVerdictArtifact916`, `ClaudeTitleOutro916`, `BrutalistHesitantWriter916`)
already registered in the toolkit.
