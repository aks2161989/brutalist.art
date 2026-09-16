# PROMPTS — Brutalist Command: art icon-build

No paid API was used in this build. No AI-generated media. Every visual is a
deterministic Remotion scene registered in the toolkit's Root.tsx and driven
by the beat sheet.

## Composer prompt (B00 — cold open ASK)

Typed into the on-screen `ClaudeComposerAsk`:

> 12 GB of raw svg upstream. How do you get to a shippable icon set?

Result lines rendered under the composer (verifiable claims):

- `12 GB / 2.4 M files  →  30 MB / 7,330 icons  (~400× smaller)`
- `one geometry (viewBox 0 0 24 24), one stroke (2), one color (currentColor)`
- `one dispatcher branch: ./art icon-build  →  build_icon_set.py`

## Composer prompt (B10 — HANDOFF)

Typed into the on-screen `ClaudeComposerAsk` and read aloud verbatim:

> From the brutalist.art toolkit root: (1) `./art icon-build --dry-run` and note
> the CANONICAL SET count. (2) `./art icon-build --limit 3 --dry-run` and
> confirm it stops at 3 in the first source only. (3) `python3 -c 'import json;
> d = json.load(open("icons/icons.json")); print(d["count"], sum(1 for i in
> d["icons"] if i["brand"]))'` and compare to (1). (4) `grep -c '^## '
> icons/NOTICE.md` and open the file: at least an ISC block (lucide) and an MIT
> block (tabler / iconoir / feather) must be present.

Expected outcome lines:

- (1) dry-run reports 7,330 concepts (376 brand/logo) — priority order preserved
- (2) `--limit 3 --dry-run` stops in lucide only; other sources not touched
- (3) `icons.json` count == dry-run count (drift means the set is stale)
- (4) `NOTICE.md` contains an ISC block AND an MIT block, verbatim from upstream

## Kokoro TTS

Voice: `am_onyx` (Liam-in-for-Bear default). Engine: local Kokoro-82M via
`kokoro-onnx`. No API, no key, no meter. One MP3 per beat; per-beat duration
is the master clock.

## Rendering

- Remotion 4.0.486 via `runtime/scripts/remotion_scenes.py` (serial, foreground).
- Chrome for Testing wrapped with `--single-process --in-process-gpu` to satisfy
  the Apple App Sandbox; wrapper at `runtime/scripts/chrome_wrap.sh`, invoked
  via `ART_CHROME` + `ART_CHROME_MODE=chrome-for-testing`.
- Per-beat MP4 rendered at native composition dimensions (1920×1080 for
  landscape, 1080×1920 for vertical). `compile.py --height 2160` upsamples the
  assembled master to 4K (3840×2160).
