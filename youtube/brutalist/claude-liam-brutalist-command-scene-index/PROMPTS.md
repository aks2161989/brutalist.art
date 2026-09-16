# PROMPTS — Brutalist Command: art scene-index

## The rebuild recipe (paste into Claude Code from `books/`)

```
cd .repoloop/workspaces/claude-liam-brutalist-command-scene-index/toolkit
REEL=/Users/bear/Documents/CoWork/bear-textbooks/books/brutalist.art/youtube/brutalist/claude-liam-brutalist-command-scene-index

# One-time: shadow the isolated toolkit's node_modules so webpack can
# rotate its cache pack files inside the workspace.
SHARED=/Users/bear/Documents/CoWork/bear-textbooks/books/brutalist.art/runtime/remotion/node_modules
TOOLKIT=$(pwd)/runtime/remotion/node_modules
if [ -L "$TOOLKIT" ]; then rm "$TOOLKIT"; fi
mkdir -p "$TOOLKIT" "$TOOLKIT/.cache"
for entry in "$SHARED"/*; do
  base=$(basename "$entry"); [ "$base" = ".cache" ] && continue
  ln -s "$entry" "$TOOLKIT/$base"
done
for entry in "$SHARED"/.*; do
  base=$(basename "$entry")
  [ "$base" = "." ] || [ "$base" = ".." ] || [ "$base" = ".cache" ] || \
    ln -s "$entry" "$TOOLKIT/$base" 2>/dev/null
done

# Chrome wrapper for the Apple App Sandbox Mach-port block
export ART_CHROME=/tmp/claude/chrome-single-process.sh
export ART_CHROME_MODE=chrome-for-testing

# 1. Audio (durations are ground truth)
python3 runtime/scripts/generate_audio_kokoro.py "$REEL"

# 2. Render all 12 beats as native Remotion mp4s
python3 runtime/scripts/remotion_scenes.py "$REEL"

# 3. Compile landscape master at native 4K
python3 runtime/scripts/compile.py "$REEL" --height 2160 \
    --out "$REEL/exports/landscape" --force

# 4. Vertical companion (separate sheet under $REEL/vertical/)
python3 runtime/scripts/generate_audio_kokoro.py "$REEL/vertical"
python3 runtime/scripts/remotion_scenes.py "$REEL/vertical"
python3 runtime/scripts/compile.py "$REEL/vertical" --height 3840 \
    --out "$REEL/exports/vertical" --force
```

Landscape output: `exports/landscape/claude-liam-brutalist-command-scene-index.mp4`
(3840x2160 · h.264 + AAC).
Vertical output: `exports/vertical/claude-liam-brutalist-command-scene-index-vertical.mp4`
(2160x3840 · h.264 + AAC).

## The demo prompts (captured verbatim in demo/RUN-LOG.txt)

Baseline / the two files the tool writes:

```
./art scene-index
ls -l runtime/remotion/src/scenes.json  SCENE-DOC-TODO.md
head -12 runtime/remotion/src/scenes.json
head -20 SCENE-DOC-TODO.md
```

Failure and recovery:

```
# hard failure — no Root.tsx at the given path
python3 runtime/scripts/build_scene_index.py /tmp/no-such-dir --todo
# recovery — let the wrapper choose the path
./art scene-index
```

Falsifiability — the orphan scene demo (verbatim in RUN-LOG):

```
# scratch toolkit at $FT, with two .tsx files in scenes/
# and only one <Composition> in Root.tsx
python3 runtime/scripts/build_scene_index.py "$FT/src" --todo
# -> 1 renderable, orphan invisible

# add <Composition id="OrphanNewScene" .../> to Root.tsx
python3 runtime/scripts/build_scene_index.py "$FT/src" --todo
# -> 2 renderable, both visible
```

## Handoff prompt (B10 — read aloud verbatim on screen)

> From the brutalist.art toolkit root: (1) run `./art scene-index` and
> record `X renderable, Y undocumented, 0 unresolved`. (2) Add a real
> `<Composition id="YourNewScene" .../>` to `runtime/remotion/src/Root.tsx`
> for a component you are about to author (or one already sitting
> invisible in `scenes/`). (3) Re-run `./art scene-index`; confirm
> `renderable = X + 1`. (4) Open `SCENE-DOC-TODO.md`, pick one row, add a
> one-sentence header at the top of its `.tsx`, re-run; confirm
> `undocumented = Y - 1`. If either number does not move, the edit did
> not save or the import path in Root.tsx does not resolve.

## Cold-open composer copy (B00)

- Greeting: `Bonjour, Liam` (French, one word).
- Topic: `BRUTALIST · COMMAND: ART SCENE-INDEX`.
- Segment: `art scene-index`.
- Command: "After adding a Remotion component, re-read Root.tsx and
  regenerate the scene index the library-first search uses."
- runningText: `reading Root.tsx…`.
- Output cascade:
  - `wraps: python3 runtime/scripts/build_scene_index.py runtime/remotion/src --todo`
  - `writes: runtime/remotion/src/scenes.json + SCENE-DOC-TODO.md`
  - `law: a scene is renderable only if Root.tsx declares a <Composition> for it`

## Nothing here calls a paid API

Kokoro (`am_onyx`) is local; Remotion renders via a local Chrome; the
toolkit's isolated `node_modules` is shadowed with symlinks so webpack
can rotate its own cache pack inside the workspace. No key, no upload,
no publication.
