# PROMPTS — Brutalist Command: art icon-build — Short

No paid API was used in this build. No AI-generated media. Every visual is a deterministic Remotion scene, driven by the parent vertical beat sheet. The Short reuses the parent's native 2160×3840 renders unchanged.

## Composer prompt (B00 — cold open ASK)

Typed into the on-screen `ClaudeComposerAsk916`:

> 12 GB of raw svg upstream. How do you get to a shippable icon set?

Result lines rendered under the composer (verifiable claims):

- `12 GB / 2.4 M files  →  30 MB / 7,330 icons  (~400× smaller)`
- `one geometry (viewBox 0 0 24 24), one stroke (2), one color (currentColor)`
- `one dispatcher branch: ./art icon-build  →  build_icon_set.py`

## Not in this Short

The B10 Your-Turn composer prompt (a four-step audit exercise) belongs to the long. It was cut from the Short per the Shorts prompt's guidance ("a detailed CTA can be cut; the Short need not read the long film's full exercise aloud"). See the parent vertical / landscape reels for the full exercise.

## Kokoro TTS

Voice: `am_onyx` (Liam-in-for-Bear default). Engine: local Kokoro-82M via `kokoro-onnx`. No API, no key, no meter. Six per-beat MP3s reused as-is from the parent vertical; per-beat duration is the master clock.

## Rendering

- No Remotion re-render for this Short — every beat's clip is the parent's native 2160×3840 mp4, copied independently under `media/`.
- Assembly + 4K master via `runtime/scripts/compile.py --height 3840`. No `--review` pass.
