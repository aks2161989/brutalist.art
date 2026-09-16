# Prompts and generation choices

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

## On-screen prompt (B10 — Your Turn handoff)

Verbatim what appears in the composer:

```
Read skills/make/fashionista/SKILL.md. Then plan a dry-run trial for a
garment you have in mind:
(1) draft an INTRO ask in the `Hey Claude, what is he/she wearing?` pattern
    that never names the garment;
(2) write a candidate CALLS.json row — term, confidence, reasoning,
    alternatives_considered, verdict:null;
(3) name which error lane (GENERATOR or DESCRIBER) would matter most, or say
    it is not separable.
Do not run any paid API.
```

Viewer rubric shown as output:

1. check: does the ask stay inside the "what is he wearing" pattern?
2. check: does the CALLS row have all six fields, verdict:null?
3. check: does Claude commit to an error lane, or honestly say "not separable"?

Liam reads the prompt aloud and discusses each check line before inviting the
pause (HANDOFF LAW). The prompt intentionally does NOT ask Claude to run the
fashionista skill for real — the skill needs a source video the free pipeline
cannot generate, so the handoff is a documented dry-run planning pass.

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
