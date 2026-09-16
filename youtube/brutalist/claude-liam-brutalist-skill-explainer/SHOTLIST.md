# SHOTLIST — The explainer Skill

Landscape reel (3840×2160 output, composed at 1920×1080 native).
All beats render via `runtime/scripts/remotion_scenes.py` — no hand-rolled
`npx remotion render`, no unresolved slates.

| Beat | Composition (16:9) | Type | Duration (s) | What appears |
|---|---|---|---|---|
| B00 | `ClaudeComposerAsk` | ASK (UI, cold open) | 15.42 | Cream page; composer card; greeting "Aloha, Liam" types in; command "What is the `explainer` skill?" types in; send button arms terracotta; three result lines fade in (pipeline not style; two-axis type × source; still is evidence). |
| B01 | `BrutalistHesitantWriter` | BLUF (typing) | 18.84 | Serif text writes itself: "The explainer / skill is a / style."; "style" flashes terracotta then deletes; "pipeline" types in; final couplet "Sources never match. / The treatment does." types in. `lead_silence_s: 0.8`. |
| B02 | `SkillTeardownAnatomy` | FRAMEWORK (folder tree) | 23.82 | Eyebrow SKILL · ANATOMY; title "The parent explainer folder."; folder tree reveals row by row: `skills/make/explainer/` → `SKILL.md` (accent, doctrine) → `MOTION.md` → `REMOTION.md` → `EQUATIONS.md` → governs: ai-explainer · cli-explainer · deep-explainer → runtime belt: generate_audio_kokoro · pantry · compile · outro. Terracotta callout: "Every other explainer inherits this chassis." |
| B03 | `SkillTeardownPipeline` | FRAMEWORK (flow) | 21.70 | Eyebrow SKILL · PIPELINE; title "One clock. Four sources."; input node "script · beats"; four phase nodes — **audio · Kokoro** (terracotta) · media (Manim · stills · footage) · remotion (annotation plane) · compile (conform + concat); output node "watchable master"; footer "Every beat is a per-beat mp4. Nothing gets baked before its audio window is measured." |
| B04 | `SkillTeardownMechanism` | MECHANISM · ACT 1 | 22.53 | Heading "The laundering function."; body about one treatment sitting under every source; quote card "Not a style — a laundering function. Sources never match; the treatment does."; verdict pill "kills the style-vs-substance debate" (positive). |
| B05 | `SkillTeardownMechanism` | WORKED EXAMPLE / MECHANISM · ACT 2 | 29.27 | Heading "Two axes. Free swaps."; body enumerates `shot.type ∈ {STILL, FOOTAGE, DOCUMENT, GRAPHIC, COMPOSITE, CARD}` × `shot.source ∈ {archive, ai, own}`; quote card "Collapsing them makes every swap a re-edit; separating them makes swaps free."; verdict pill "swaps stay free" (positive). |
| B06 | `SkillTeardownMechanism` | MECHANISM · ACT 3 | 28.50 | Heading "The slot contract."; body walks precedence ladder `media/[beat].mp4 > manim/[beat].mp4 > media/[beat].png > SLATE`; quote card "Rebuild recompiles ONLY slots whose input hash changed, then re-concats."; verdict pill "first pass is always watchable" (positive). |
| B07 | `SkillTeardownMechanism` | FALSIFIABILITY (DESIGN · TELL) | 29.50 | Heading "A still is evidence."; body walks the swap test — Princeton's admissions record vs. a stock photo of a university; quote card "There is no share to hit… any prior guidance stating a target percentage of vox body beats is superseded by this law."; verdict pill "zero vox is a correct outcome" (negative — permission not mandate). |
| B08 | `ClaudeVerdictArtifact` | VERDICT (UI, artifact page) | 26.71 | Artifact card scales in; heading "A pipeline. Not a style."; six verdict lines reveal one at a time (chassis; Kokoro clock; two-axis swaps; precedence ladder; VOX LAW; watchable first pass). |
| B09 | `ClaudeComposerAsk` | YOUR TURN (UI, handoff) | 32.58 | Cream page; composer; greeting "Your Turn"; the full paste-ready `slate cut` prompt types in; three-line rubric appears as output. Liam reads the prompt aloud and discusses the three checks. |
| B10 | `ClaudeTitleOutro` | OUTRO | 3.48 | Cream/ink; slug-seeded mascot; title "The explainer Skill." with terracotta period; handle `@NikBearBrown` beneath (locked per OUTRO-LOCK.md). |

Total narration ≈ **252 s** (~4 min 12 s). Landing in the 3–4 minute band the
sibling duration-planner SKILL predicts for a multi-decision mechanism
teardown (five design decisions covered). Not padded to a round number.

## Portrait companion (vertical)

Same 11 beats, native 1080×1920 compositions (see `vertical/SHOTLIST.md`).
Every SkillTeardown* component reads `useVideoConfig()` for width/height, so
the layout math naturally reflows tall — headings, folder-tree, mechanism
cards stack vertically. Pipeline uses proportional `boxW = min(200, (w*0.78)/n − 20)`
so nodes compress cleanly at portrait width for four phases (six nodes total).
The Claude UI compositions use their dedicated 916 variants
(`ClaudeComposerAsk916`, `ClaudeVerdictArtifact916`, `ClaudeTitleOutro916`,
`BrutalistHesitantWriter916`) already registered in the toolkit; the three
`SkillTeardown*916` wrappers were added to this isolated toolkit's `Root.tsx`
for this build (share source with the landscape components; reflow via
`useVideoConfig()`).
