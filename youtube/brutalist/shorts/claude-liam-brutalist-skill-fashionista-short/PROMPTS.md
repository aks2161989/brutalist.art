# Prompts and generation choices (Short cut)

Derivative Short of the full portrait reel. The Short retains B00 (cold-open
ask) and B11 (title outro); B10's extended Your-Turn paste-in was cut and its
on-screen prompt does not appear in this Short. All retained on-screen prompts
are unchanged from the parent portrait reel.

## Generative model use in this reel

- **Narration**: Kokoro `am_onyx` (local, free). Run:
  `python3 runtime/scripts/generate_audio_kokoro.py <REEL>`.
- **Visuals**: 100% deterministic Remotion. No AI image or AI video was used
  to make any beat.
- **Text**: The narration was authored against the SKILL.md; every substantive
  claim is fact-checked in FACTCHECK.md.
- **No paid API calls, no uploads, no publishing.**

## On-screen prompt (B00 — cold open)

The composer types this prompt (the ask lands answered — narration reacts):

```
What is the `fashionista` skill? Read skills/make/fashionista/SKILL.md and
tell me what it is really testing.
```

Result lines rendered in the composer output:

1. an experiment, not a fashion series
2. the audience is the scoring function
3. hedging is the content, not weakness

## On-screen prompt (B10 — Your Turn handoff) — CUT FROM THIS SHORT

The 34-second Your-Turn paste-in was dropped from the Short. See the 16:9 long
for the full dry-run prompt, the six-field CALLS row template and the
three-check viewer rubric.

## Portrait scenes authored in this isolated toolkit (PUNT → filled)

Three portrait-native wrappers were authored in this isolated toolkit to
honour the "native portrait, not a crop" rule (RENDER-TARGETS.md §3):

- `SkillTeardownAnatomy916` — vertical stack for the folder tree, larger type.
- `SkillTeardownPipeline916` — vertical (top-to-bottom) flow with down-arrows
  between nodes; portrait-appropriate boxes.
- `SkillTeardownMechanism916` — narrower body, portrait typography ramp.

All three:
- Live only in this isolated toolkit's
  `runtime/remotion/src/scenes/SkillTeardown*916.tsx` and are registered in
  this toolkit's `Root.tsx`. They are NOT committed to the public toolkit.
- Reuse the landscape components' schemas (same props), so the beat sheet's
  `props` blocks are identical shape.
- Use `useVideoConfig()` to compute layout dimensions relative to the
  1080×1920 canvas.

The pre-existing `ClaudeComposerAsk916`, `BrutalistHesitantWriter916`,
`ClaudeVerdictArtifact916`, and `ClaudeTitleOutro916` are library scenes; the
portrait beat sheet uses them directly.

## Chrome / render environment

Remotion needs a browser binary that survives Apple's App Sandbox. Rendering
is done via a wrapper script that invokes
`chrome-headless-shell` with `--single-process --in-process-gpu`, exposed to
Remotion via `ART_CHROME` (with `ART_CHROME_MODE=chrome-for-testing`). This is
the documented Remotion hook, not a sandbox bypass.
