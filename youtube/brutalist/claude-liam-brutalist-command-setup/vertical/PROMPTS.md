# PROMPTS.md — Brutalist Command: setup

Every on-screen prompt / command / paste-ready request in one place.

## B00 — cold-open composer

- `greeting`: `Konnichiwa, Liam`
- `topic`: `BRUTALIST · COMMAND: SETUP`
- `segment`: `./setup`
- `command`: `Before I fill a single beat sheet, tell me what's actually installed on this box. Don't install anything. Just verify.`
- `runningText`: `running ./setup…`
- `output`:
  - `prints a 7-row FEATURE table — green when every atomic check passes live`
  - `installs pip deps + Remotion npm + fonts + Kokoro model, then verifies (only under --install)`
  - `exits 0 iff all rows green; exits 1 the moment one is red`
- `folderLabel`: `@HumanitariansAI`
- `modelLabel`: `Claude`
- `effortLabel`: `Sonnet`

## B01 — hesitant writer (BLUF)

- `text`: `setup\ninstalls everything.`
- `triggerWords`: `installs, everything`
- `replacementWords`: `verifies, live`
- Final rendered sentence: **`setup / verifies live.`** — the reel's compressed claim; the narration expands it out loud with the `--install` caveat.
- `seed`: `setup-b01`
- `lead_silence_s`: `0.8`
- Multi-word triggers were considered and rejected: the component splits the text on `\s+` and matches token-by-token (see `runtime/remotion/src/scenes/BrutalistHesitantWriter.tsx:118, 130`), so a space-containing phrase silently never matches. Two comma-separated single tokens is the pattern the doctor episode used and the one this component supports.
- Trigger collision check: neither `installs` nor `everything` appears in the preserved prefix `setup`, so the FIRST-occurrence rule doesn't corrupt the sentence.

## B02 — the setup surface (verbatim shebang + short-help)

```bash
#!/usr/bin/env bash
# setup — the doctor for the brutalist toolkit (free by default).
#
#   ./setup            # check everything, print the readiness table
#   ./setup --install  # install the core Python deps + Remotion's node deps, then check
#
# Core features require no paid services or API keys. Everything below is free
# and local. Optional Higgsfield CLI login unlocks AI video beats; ElevenLabs is
# permanently removed. Exit 0 if all required features are ready; exit 1 otherwise.
#
# Readiness is decided ONLY by live verification below — importing every
# Python dep, actually running ffmpeg/ffprobe, and synthesizing + decoding
# one real Kokoro phrase (mean_volume > -40 dB). An install step's own exit
# code is reported (INSTALL_FAILED) but never substitutes for a check: a
# green table means the checks passed, not that `pip install` returned 0.
set -uo pipefail
```

## B03 — requirements.txt (verbatim; six pinning lines + numpy note)

```pip
# brutalist — Python dependencies (free-only toolkit).
#   pip install -r requirements.txt
# numpy>=2.0.2 is required by kokoro-onnx (every >=0.4 release pins this
# floor); manim 0.18 and its deps have no upper bound on numpy, so there's
# no real conflict — just don't hold numpy below 2.

# ── core: audio-first narration pipeline ────────────────────────────────────
kokoro-onnx>=0.4            # the FREE voice engine (Kokoro-82M, local, no key)
mutagen>=1.47,<1.48         # audio-duration measurement (the master clock)
Pillow>=10.2,<11            # slates / request cards / previz / stills
numpy>=2.0.2

# ── animation ────────────────────────────────────────────────────────────────
manim>=0.18,<0.19           # pulls manimpango, moderngl, etc.
manimpango>=0.5,<0.6

# ── captions + word clock ────────────────────────────────────────────────────
faster-whisper>=1.0,<2      # forced alignment + transcript captions (local, no key)
```

## B11 — Your Turn (paste-ready)

```
From my brutalist.art toolkit root: (1) run ./setup and save the whole
stdout+stderr to /tmp/setup.txt. (2) Do NOT install anything. (3) For every
row that says '❌ blocked', write one line naming the atomic check ID that
failed (the id passed to check() in setup) and quoting the exact fix hint
that printed beneath it. (4) Then grep the toolkit for the four ElevenLabs
fingerprints the guard at setup:102-115 checks — ELEVEN''LABS_API_KEY,
elevenlabs.io, "engine": "elevenlabs" in any JSON, and xi-api-key — and
tell me whether any file outside of setup itself matches. (5) Tell me
whether you were tempted to run ./setup --install to make the table green,
and why you did not.
```

## B12 — outro card

- `title`: `Brutalist Command: setup.`
- `slug`: `claude-liam-brutalist-command-setup` — polarity / mascot / jingle deterministically picked from the slug.

## Not spoken, not on-screen

There is no `./setup --help` command. The short-help is the shebang comment at `setup:1-16`, which is what B02 quotes.
