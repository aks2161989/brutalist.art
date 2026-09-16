# SHOTLIST — The logo-motion Skill

Landscape 3840×2160 (renders at 1920×1080 with Remotion `--scale=2`). Portrait
companion at 2160×3840 lives in `vertical/SHOTLIST.md`.

| Beat | Duration (s) | Scene (Remotion) | What's on screen |
|---|---|---|---|
| B00 | 16.62 | `ClaudeComposerAsk` | Claude composer with hello + persona; command types the ask about logo-motion; three result lines fade in. |
| B01 | 18.65 | `BrutalistHesitantWriter` | Cream page, serif three-line overview. `"new scene file"` flashes terracotta then deletes to `"traced props block"`. Seed `logo-motion-bluf-2026-633ec861`. |
| B02 | 33.62 | `SkillTeardownAnatomy` | Folder-tree card: `skills/make/logo-motion/`, its `SKILL.md`/`TIMING.md`/`trace_logo.py`, then `runtime/remotion/src/scenes/LogoMotion.tsx`, then `runtime/remotion/src/logos/<brand>.ts`, then `<book>/youtube/<reel>/beat_sheet.json`. Callout: "A new brand adds three things — never a fourth scene file." |
| B03 | 35.14 | `SkillTeardownPipeline` | Four-node flow: raster mark → TRACE PARTS → MEASURE LOCKUP → SET PHASE MAP (accent) → RENDER + LOOK → logo sting. Footer: "One scene, one trace, one props block." |
| B04 | 31.62 | `SkillTeardownMechanism` | Heading "The build is a camera move." Body: extreme close-up · scale 6.5 · rotate -19° · ease `1 − (1 − t)^4`. Quote from TIMING.md ("It's just appearing"). Verdict pill: "pull back, not fade in". |
| B05 | 37.82 | `SkillTeardownMechanism` | Heading "The ghost hold IS the effect." Body: BUILD/GHOST/MATERIALISE/LOCK fractions; the measured crossings 0.36 / 0.64 / 0.80. Quote from TIMING.md ("Half the runtime spent nearly invisible…"). Verdict pill: "44% of the runtime, invisible". |
| B06 | 35.58 | `SkillTeardownMechanism` | Heading "Length is a prop." Body: durationInSeconds → calculateMetadata → durationInFrames; fractions, not frames. Quote from SKILL.md ("Length is a prop, not a re-time"). Verdict pill: "same curve, any length". |
| B07 | 39.79 | `SkillTeardownMechanism` | Heading "The audio-first exception." Body: transition first, voice waits; runtime is transition + speech + tail; Medhavy leading silence 0.88 s. Quote from TIMING.md. Verdict pill: "the curve wins, the voice waits". |
| B08 | 40.55 | `SkillTeardownMechanism` | Heading "Three tells of a cheap sting." Body: (1) full-strength arrival, (2) chrome/gloss/bevel sweep, (3) colour during motion. Quote from TIMING.md. Verdict pill: "the Medhavy first cut had all three". |
| B09 | 30.31 | `ClaudeVerdictArtifact` | Artifact page — title "The logo-motion Skill". Heading "One composition. Every mark." Six recap lines. |
| B10 | 39.57 | `ClaudeComposerAsk` | Greeting "Your Turn". Command types the paste-ready audit prompt (ffmpeg 1 fps + luma-std-dev cross-check vs. 0.36 / 0.64 / 0.80). Three output lines summarise the rubric. |
| B11 | 3.73 | `ClaudeTitleOutro` | Title restate "The logo-motion Skill.", `@NikBearBrown` handle, slug-seeded pixel mascot. |

## Scene selection log

Ran mental scan against the local scene library; the four SkillTeardown scenes
(`ClaudeComposerAsk`, `BrutalistHesitantWriter`, `SkillTeardownAnatomy`,
`SkillTeardownPipeline`, `SkillTeardownMechanism`, `ClaudeVerdictArtifact`,
`ClaudeTitleOutro`) are the canonical bundle for `skill-teardown` and
match the previous 15 Brutalist skill teardowns byte-for-byte in their
Root.tsx registrations. No new scene was authored for landscape.

Portrait companion adds three native 9:16 wrappers (already existed as
`SkillTeardown*916.tsx` in the previous logo-skill workspace overlay) copied
into this workspace's `runtime/remotion/src/scenes/` and registered in
`Root.tsx` beside their landscape peers — no cropping. See
`scene-source-manifest.json`.

## Slate policy

Zero unresolved slates. All twelve beats have `shot.remotion.pattern` set and
render as native Remotion scenes.
