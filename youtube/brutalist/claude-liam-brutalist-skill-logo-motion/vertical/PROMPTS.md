# PROMPTS — The logo-motion Skill

Every generative surface used in this reel, verbatim. No paid API was called.
Kokoro `am_onyx` synthesised every narration beat locally via
`runtime/scripts/generate_audio_kokoro.py`.

## Cold-open composer (B00)
- **greeting:** `Hola, Liam`
- **command:**
  > What does the `logo-motion` skill actually do? Read
  > `skills/make/logo-motion/SKILL.md` and tell me — the mental model, not the
  > README.
- **runningText:** `reading skills/make/logo-motion/SKILL.md…`
- **output lines (result):**
  - `ONE parametric composition (LogoMotion.tsx) drives every mark`
  - `a new brand = traced parts + props block, no new scene file`
  - `the transition curve is the clock — narration waits for it`

## Hesitant-writer misconception (B01)
- **text (final, corrected):** `A new logo / needs a traced props block. / One
  composition. Every mark.`
- **triggerWords:** `new scene file`
- **replacementWords:** `traced props block`
- **seed:** `logo-motion-bluf-2026-633ec861`

## Your Turn prompt (B10) — the paste-ready one
Read verbatim by Liam and discussed in the narration.

```text
Read skills/make/logo-motion/SKILL.md and reference/TIMING.md. Take a logo
sting I already have (any format Remotion can decode). Extract 1 fps with
ffmpeg (`ffmpeg -i sting.mp4 -vf fps=1 _qc/frames/%03d.png`). Compute the luma
std-dev inside the mark's bounding box for every frame; write it out as a CSV
column. Find the p (fraction of total runtime) where std-dev crosses 5%, 50%,
and 95% of the plateau. Report crossings vs. the reference (0.36 / 0.64 / 0.80).
Do NOT modify the source sting; write CSV + plot into _qc/ only.
```

## No image / no video generation prompts
No AI image or video generation model was invoked. Every visual is a
deterministic Remotion scene rendered from typed props at 3840×2160 (landscape)
or 2160×3840 (portrait) via `runtime/scripts/remotion_scenes.py` with
`--scale=2 --image-format=png --crf=16`.
