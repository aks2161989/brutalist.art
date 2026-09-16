# PROMPTS — Brutalist Command: art final (ep 33)

## On-screen prompts (2)

### B00 — the ask, in the Claude composer

> Compile this reel to a verified 4K master. Refuse on thin paperwork or an
> unfilled slate. If the new export fails any check, keep the last good file
> in place. Do not print ready unless the file on disk really is.

### B10 — Your Turn, in the Claude composer

> From the brutalist.art toolkit root against a reel folder I finished this
> week: (1) run `./art final <reel> --out /tmp/verify-<reel> --height 2160`.
> (2) Wait for exit 0 and note the last-line mp4 path. (3) `cat` the sibling
> `<slug>.verified.json` and copy the `sha256` field. (4) Independently hash
> the mp4 with `shasum -a 256 <mp4>`. (5) Report whether the two strings
> match character-for-character; if they do not, list every file that was
> modified inside the export directory in the last minute and tell me what
> wrote to it. Do not hash from `build-state.json` or the beat sheet — hash
> the mp4 you would ship.

No AI image/video generators were called during this build. No paid API. The
only external process is `chrome-headless-shell` (installed locally, offline).

## Reproducible command sequence

The whole reel builds from these commands run against the isolated toolkit
copy at
`.repoloop/workspaces/claude-liam-brutalist-command-final/toolkit/` and the
reel folder at
`youtube/brutalist/claude-liam-brutalist-command-final/`.

```bash
export TOOLKIT=/Users/bear/…/toolkit
export REEL=/Users/bear/…/claude-liam-brutalist-command-final

# 1. Kokoro TTS (free, local; measures durations back into beat_sheet.json)
cd "$TOOLKIT"
python3 runtime/scripts/generate_audio_kokoro.py "$REEL"

# 2. Render every Remotion beat (fill media/<BID>.mp4)
ART_CHROME=/tmp/claude-501/art-final-chrome/chrome-wrapper.sh \
ART_CHROME_MODE=chrome-for-testing \
python3 runtime/scripts/remotion_scenes.py "$REEL"

# 3. Compile the verified 4K landscape master
./art final "$REEL" --out "$REEL/exports/landscape" --height 2160

# 4. Portrait companion: independent beat sheet in vertical/, then compile
./art vertical "$REEL"
python3 runtime/scripts/remotion_scenes.py "$REEL/vertical"
./art final "$REEL/vertical" --out "$REEL/exports/vertical" --height 3840

# 5. Gate V (frame-level QC) — already run inside ./art final on the candidate
#    mp4, but re-run standalone to inspect the report:
python3 runtime/qc/final_frame_check.py "$REEL" \
    --mp4 "$REEL/exports/landscape/claude-liam-brutalist-command-final.mp4" \
    --sheet "$REEL/beat_sheet.json"
```

## Isolated-toolkit patches applied

Two changes to the isolated toolkit's Remotion source only (both documented in
`feedback_brutalist_hesitant_writer_portrait_scale_patch` and
`feedback_isolated_toolkit_node_modules_shadow` memories from prior builds):

1. **BrutalistHesitantWriter.tsx** — replaced the single `scale = min(w/1920, h/1080)`
   line with the portrait-aware ternary so `BrutalistHesitantWriter916` fills the
   9:16 canvas properly. Landscape math unchanged.
2. **Root.tsx** — registered `ClaudeCodeBeat916` (1080×1920 wrapper of the shared
   `ClaudeCodeBeat` component). It was missing from this toolkit revision but
   both the ep-29 and ep-32 vertical beat sheets already reference it, so the
   vertical build needs it.

The isolated toolkit is a *copy* under
`.repoloop/workspaces/…/toolkit/`; the shared public toolkit at
`brutalist.art/` is unchanged.

## Sandbox workarounds

- `runtime/remotion/node_modules` was a symlink into a `denyWithinAllow` path.
  Shadowed with per-entry symlinks + fresh writable `.cache/` so webpack can
  rotate cache packs (per `feedback_isolated_toolkit_node_modules_shadow`).
- Remotion browser launch collapsed to `--single-process --in-process-gpu`
  via `ART_CHROME` + `ART_CHROME_MODE=chrome-for-testing` (per
  `feedback_chrome_sandbox`). Wrapper at `/tmp/claude-501/art-final-chrome/`.

Neither workaround changes what `art final` does; both are documented in
`CHECKS-REPORT.md`.
