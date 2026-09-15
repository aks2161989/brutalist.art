# PROMPTS — Brutalist Command: art run

Reproducible command sequence for this episode's build. All commands
run from the isolated toolkit root:

```
/Users/bear/Documents/CoWork/bear-textbooks/books/brutalist.art/.repoloop/workspaces/claude-liam-brutalist-command-run/toolkit
```

## Pre-build environment setup (sandbox workarounds)

```bash
# 1. Shadow the shared node_modules so webpack's .cache/ is writable
#    inside the workspace (feedback_isolated_toolkit_node_modules_shadow).
SHARED=/Users/bear/Documents/CoWork/bear-textbooks/books/brutalist.art/runtime/remotion/node_modules
TOOLKIT_NM=./runtime/remotion/node_modules
[ -L "$TOOLKIT_NM" ] && rm "$TOOLKIT_NM"
mkdir -p "$TOOLKIT_NM" "$TOOLKIT_NM/.cache"
for e in "$SHARED"/*; do
  b=$(basename "$e"); [ "$b" = ".cache" ] && continue
  ln -s "$e" "$TOOLKIT_NM/$b"
done

# 2. Ensure @remotion/cli and @remotion/renderer are real directories
#    (not symlinks), then patch open-browser.js to add --single-process
#    on darwin (feedback_chrome_sandbox — 2026-09-12 revision).
#    Shell-script wrappers fail with ENOEXEC inside the App Sandbox;
#    the fix is to patch the renderer directly and invoke the local CLI
#    via 'node' so the patched copy is actually loaded.
#    remotion_scenes.py uses REMOTION_CMD = ["node", str(_CLI)] where
#    _CLI = PROJECT/"node_modules/@remotion/cli/remotion-cli.js".
SHARED_REMOTION=/Users/bear/Documents/CoWork/bear-textbooks/books/brutalist.art/runtime/remotion/node_modules/@remotion
TOOLKIT_REMOTION=./runtime/remotion/node_modules/@remotion
for pkg in cli renderer; do
  [ -e "$TOOLKIT_REMOTION/$pkg" ] && rm -rf "$TOOLKIT_REMOTION/$pkg"
  cp -r "$SHARED_REMOTION/$pkg" "$TOOLKIT_REMOTION/$pkg"
done
python3 - <<'PY'
import pathlib, sys
f = pathlib.Path('runtime/remotion/node_modules/@remotion/renderer/dist/open-browser.js')
t = f.read_text()
old = "process.platform === 'linux' &&\n        chromiumOptions.gl !== 'vulkan' &&\n        !enableMultiProcessOnLinux\n        ? '--single-process'"
new = "(process.platform === 'linux' &&\n        chromiumOptions.gl !== 'vulkan' &&\n        !enableMultiProcessOnLinux) ||\n        process.platform === 'darwin'\n        ? '--single-process'"
if old not in t:
    sys.exit('patch anchor not found — check open-browser.js version')
f.write_text(t.replace(old, new, 1))
print('open-browser.js patched for darwin --single-process')
PY
```

## Register the portrait scene (one edit, one re-index)

`ClaudeCodeBeat916` was missing from the isolated toolkit's `Root.tsx`.
Added at Root.tsx:1464 alongside the landscape registration; re-ran
`./art scene-index`; count moved from 619 → 620.

```bash
./art scene-index
# scenes.json — 620 renderable, 118 undocumented, 0 unresolved
```

## Audio (Kokoro am_onyx — the master clock)

```bash
python3 runtime/scripts/generate_audio_kokoro.py \
  /Users/bear/.../youtube/brutalist/claude-liam-brutalist-command-run
```

## Render every Remotion beat (foreground, serial)

```bash
python3 runtime/scripts/remotion_scenes.py \
  /Users/bear/.../youtube/brutalist/claude-liam-brutalist-command-run
```

## Landscape compile (16:9, 4K, review cut)

```bash
python3 runtime/scripts/compile.py \
  /Users/bear/.../youtube/brutalist/claude-liam-brutalist-command-run \
  --review --height 2160 \
  --out /Users/bear/.../youtube/brutalist/claude-liam-brutalist-command-run/exports/landscape
```

## Portrait sibling (9:16, native 4K)

```bash
# Author vertical/beat_sheet.json with aspect_ratio 9:16 and *916 patterns;
# generate audio + render + compile separately:
python3 runtime/scripts/generate_audio_kokoro.py \
  /Users/bear/.../youtube/brutalist/claude-liam-brutalist-command-run/vertical

python3 runtime/scripts/remotion_scenes.py \
  /Users/bear/.../youtube/brutalist/claude-liam-brutalist-command-run/vertical

python3 runtime/scripts/compile.py \
  /Users/bear/.../youtube/brutalist/claude-liam-brutalist-command-run/vertical \
  --review --height 3840 \
  --out /Users/bear/.../youtube/brutalist/claude-liam-brutalist-command-run/exports/vertical
```

## Gate V (Frame QC)

Runs automatically inside `run.sh` after `compile.py`. For a
review-only rebuild via `compile.py` directly (this run), Gate V is
executed manually against the compiled master:

```bash
python3 runtime/qc/final_frame_check.py \
  /Users/bear/.../youtube/brutalist/claude-liam-brutalist-command-run \
  --mp4 /Users/bear/.../youtube/brutalist/claude-liam-brutalist-command-run/exports/landscape/claude-liam-brutalist-command-run.mp4
```

## Frame extraction for visual review

```bash
ffmpeg -i <mp4> -vf fps=2 _qc/frames/%05d.png       # 2 fps sweep
ffprobe -v error -show_entries stream=width,height,codec_name <mp4>
```

## Beat 10 Your-Turn prompt (verbatim, as narrated)

> From the brutalist.art toolkit root against a real reel of yours:
> (1) run ./art run <reel> --height 1080 and record the last four
> lines of the log. (2) If a gate stopped it, fix exactly what the
> message names — FACTCHECK/SHOTLIST/PROMPTS for Gate F; the offending
> beat for Gate L, A, W, B or V. (3) If Remotion stopped it, look at
> the beat id it printed, regenerate that beat's mp3 with
> runtime/scripts/generate_audio_kokoro.py <reel> --only <BID>,
> delete media/<BID>.mp4, and re-run ./art run. (4) On the second
> pass, the log should print '[run] skip <Scene> — <BID> already
> filled' for every slot you did NOT touch. If a slot is not skipped
> that should be, either the file was not written or its name does
> not match the beat id.

Expected outcomes on-screen (B10 output block):
- step 1 — last four log lines record the current gate
- step 2 — the gate's own message names the fix
- step 3 — regenerate one audio + delete one clip; re-run
- step 4 — filled slots skip; the loop shortens by one each pass

## Nothing that spends money

No `setup --install`, no `art keys`, no remote clone, no paid API call.
The demo runs against a fixture reel on the local disk; the only
network-affecting workarounds (chrome-headless-shell) are
sandbox-local.
