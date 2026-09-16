# PROMPTS — Brutalist Command: art icons — Short

No paid API was used in this build. No AI-generated media. No Kokoro
regeneration for this Short — every kept beat's MP3 is copied byte-for-byte
from the parent long. Every visual is a deterministic Remotion scene that
already shipped in the parent's native portrait render; nothing was
re-rendered.

## On-screen composer prompt in this Short — B00 (cold open ASK)

Typed into `ClaudeComposerAsk916` (visible on-screen, never sent to any API):

> Before drawing a mark for a beat, ask the library: is there already an
> icon for this?

Result lines rendered under the composer (verifiable claims — see
`SOURCES.md` for the parent fact table):

- `7,330 icons — 376 brand/logo, viewBox 0 0 24 24, stroke 2`
- `ranked: exact name > every word > prefix > token hit (IDF)`
- `aliases: icons, icon, icon-search — same case branch, same output`

## No handoff composer in this Short

The parent long's B10 ("Your turn") composer prompt was DROPPED from this
cut per the Shorts contract, which explicitly overrides the extended
Your Turn requirement. Consequently, this Short does NOT read the parent
long's paste-ready audit prompt aloud. The prompt still lives in the parent
long (`youtube/brutalist/claude-liam-brutalist-command-icons/vertical/PROMPTS.md`,
B10 section) for the fellow who wants the full audit exercise.

## Kokoro TTS

Voice: `am_onyx` (Liam-in-for-Bear default). Engine: local Kokoro-82M via
`kokoro-onnx`. No API, no key, no meter. Every MP3 in this Short's `mp3/`
directory is a byte-for-byte copy of the parent long's corresponding
`vertical/mp3/beat-*.mp3`; no regeneration was performed for the Short.

## Rendering

- No Remotion re-render for this Short. `runtime/scripts/shorts.py` reused
  each retained beat's native 2160×3840 render byte-for-byte from
  `youtube/brutalist/claude-liam-brutalist-command-icons/vertical/media/`
  (log output: "native portrait reused unchanged" for all 7 kept beats).
- Compilation via `runtime/scripts/compile.py --height 3840` (guarded).
  No `--review` pass; the `--out` argument produced the final container.
- All frame extraction / audio decode into `_qc/` used the system
  `ffmpeg` / `ffprobe`.
