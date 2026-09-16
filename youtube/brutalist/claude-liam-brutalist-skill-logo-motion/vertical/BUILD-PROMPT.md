# BUILD-PROMPT — Portrait 9:16 companion

Portrait companion to the landscape master. Same narration, same clock, same
paperwork inputs (`SCRIPT.md`, `SOURCES.md`, `FACTCHECK.md`, `PROMPTS.md`
next to the landscape master). Scene compositions are the native 9:16
variants registered in `Root.tsx`:

- `ClaudeComposerAsk916` (cold open + Your Turn handoff)
- `BrutalistHesitantWriter916` (BLUF — portrait `lineSpacing 2.5` +
  `fontSize 130` per portrait-BLUF recipe; the scene component was patched to
  a portrait-aware scale `Math.min(w/1080, h/1920)` so `fontSize` no longer
  collapses to 56.25 %)
- `SkillTeardownAnatomy916` / `SkillTeardownPipeline916` /
  `SkillTeardownMechanism916` (portrait wrappers with vertical reflow — the
  folder tree stacks; the pipeline arrows point downward; the mechanism heading
  wraps within the narrower column)
- `ClaudeVerdictArtifact916` (portrait artifact)
- `ClaudeTitleOutro916` (portrait mascot)

Metadata: `aspect_ratio: "9:16"`, slug appends `-vertical`, `channel_title`
removed per `feedback_channel_title_portrait_bleed` so the metadata overlay
does not run past the portrait safe bottom.

Audio re-uses the landscape's `mp3/beat-*.mp3` (identical narration → identical
clock) copied into `vertical/mp3/`. No re-synthesis.

Compile: `runtime/scripts/compile.py … --height 3840 --out
<reel>/exports/vertical --force`. Gate V (`runtime/qc/final_frame_check.py`)
runs internally at portrait dims and is the pass/fail gate.
