# PROMPTS — Brutalist Command: art run (Short cut)

Reproducible build for this Short. Every command runs from the isolated
toolkit root:

```
/Users/bear/Documents/CoWork/bear-textbooks/books/brutalist.art/.repoloop/shorts/workspaces/claude-liam-brutalist-command-run-short/toolkit
```

No paid API, no upload, no external network required.

## 1. Whole-beat cut from the native portrait parent

```
python3 runtime/scripts/shorts.py \
  /Users/bear/Documents/CoWork/bear-textbooks/books/brutalist.art/youtube/brutalist/claude-liam-brutalist-command-run/vertical \
  --output-dir /Users/bear/Documents/CoWork/bear-textbooks/books/brutalist.art/youtube/brutalist/shorts/claude-liam-brutalist-command-run-short \
  --slug claude-liam-brutalist-command-run-short \
  --drop B02 B04 B05 B06 B08 B09 \
  --no-endcard \
  --no-outro-rewrite
```

Every retained beat prints `native portrait reused unchanged` — no
re-render, no crop, no regenerated audio.

## 2. Compile the Short at native 3840

```
python3 runtime/scripts/compile.py \
  /Users/bear/Documents/CoWork/bear-textbooks/books/brutalist.art/youtube/brutalist/shorts/claude-liam-brutalist-command-run-short \
  --height 3840 \
  --out /Users/bear/Documents/CoWork/bear-textbooks/books/brutalist.art/youtube/brutalist/shorts/claude-liam-brutalist-command-run-short/exports/short
```

Note: `--review` was NOT passed. The Short is a compiled derivative of a
finished parent film, not a review preview. `run.sh --review` would burn
slate labels onto beats already fully filled from the parent.

## 3. QC and evidence

```
# container + streams
ffprobe -v error -show_entries format=duration:stream=index,codec_type,codec_name,width,height,duration \
  -of json exports/short/claude-liam-brutalist-command-run-short.mp4

# audio decode (silence/level sanity)
ffmpeg -y -v error -i exports/short/<slug>.mp4 -vn -c:a pcm_s16le _qc/audio.wav
ffmpeg -i _qc/audio.wav -af volumedetect -f null -

# 2 fps thumbs
ffmpeg -y -v error -i exports/short/<slug>.mp4 -vf "fps=2,scale=540:-1" _qc/frames/f-%04d.png

# beat-relative 15% / 50% / 85% + first/last (per SCRIPT.md offsets)
ffmpeg -y -v error -ss <t> -i exports/short/<slug>.mp4 -frames:v 1 -q:v 2 _qc/beats/<label>.png
```

## Retained Remotion patterns (portrait)

| Beat | Portrait pattern |
|---|---|
| B00 | ClaudeComposerAsk916 |
| B01 | BrutalistHesitantWriter916 |
| B03 | ClaudeCodeBeat916 |
| B07 | ClaudeCodeBeat916 |
| B10 | ClaudeComposerAsk916 |
| B11 | ClaudeTitleOutro916 |

Props for every retained beat are unchanged from the parent portrait
`beat_sheet.json` (see `beat_sheet.json` in this reel).
