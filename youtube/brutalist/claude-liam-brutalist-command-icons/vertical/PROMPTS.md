# PROMPTS — Brutalist Command: art icons

No paid API was used in this build. No AI-generated media. Every visual is a
deterministic Remotion scene registered in the toolkit's Root.tsx and driven
by the beat sheet.

## Composer prompt (B00 — cold open ASK)

Typed into the on-screen `ClaudeComposerAsk`:

> Before drawing a mark for a beat, ask the library: is there already an icon for this?

Result lines rendered under the composer (verifiable claims):

- `7,330 icons — 376 brand/logo, viewBox 0 0 24 24, stroke 2`
- `ranked: exact name > every word > prefix > token hit (IDF)`
- `aliases: icons, icon, icon-search — same case branch, same output`

## Composer prompt (B10 — HANDOFF)

Typed into the on-screen `ClaudeComposerAsk` and read aloud verbatim:

> From the brutalist.art toolkit root, run: ./art icons; ./art icons "money";
> ./art icons "risk warning" --top 12; ./art icons "sankey flow";
> ./art icons --check brain-circuit database bogus-icon-name;
> ./art icons --show database | head -3; ./art icons "github" --brands;
> ./art icons "quantum entanglement". Then diff ./art icons "wallet" against
> ./art icon "wallet" and ./art icon-search "wallet" — all three must be
> identical. Finally, run the search on ONE concept from a beat you are
> authoring right now and record the top hit or the miss.

Expected outcome lines:

- top hits are relevant on common queries (money, wallet, risk)
- rare word beats common word: 'sankey flow' finds chart-sankey first
- checks: brain-circuit + database IN SET, bogus not; --show is a raw `<svg>`
- aliases icons/icon/icon-search return byte-identical output
- one honest miss on 'quantum entanglement' — nearby concept or compose

## Kokoro TTS

Voice: `am_onyx` (Liam-in-for-Bear default). Engine: local Kokoro-82M via
`kokoro-onnx`. No API, no key, no meter. One MP3 per beat; per-beat
duration is the master clock.

## Rendering

- Remotion 4.0.486 via `runtime/scripts/remotion_scenes.py` (serial, foreground).
- Chrome for Testing wrapped with `--single-process --in-process-gpu` to
  satisfy the Apple App Sandbox; wrapper at `runtime/scripts/chrome_wrap.sh`.
- Per-beat MP4 rendered at native composition dimensions (1920×1080 for
  landscape, 1080×1920 for vertical). `compile.py --height 2160` upsamples
  the assembled master to 4K (3840×2160).
