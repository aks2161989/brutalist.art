# PROMPTS — vertical (9:16)

Recipes and prompts identical in intent to the landscape master; see
[`../PROMPTS.md`](../PROMPTS.md) for the full paste-ready command list.
The portrait cut only differs by:

- `beat_sheet.json` remotion patterns end in `916`.
- B01 uses `fontSize: 155`, `lineSpacing: 2.9`, and 3-line text so the
  hesitant writer clears the Gate V 55% underfill floor.
- B10 uses a tightened paste prompt to keep the composer card inside the
  portrait safe area. Same four steps, shorter phrasing.

## Portrait build recipe (only after the landscape build has passed)

```bash
export ART_CHROME=/tmp/claude/chrome-single-process.sh
export ART_CHROME_MODE=chrome-for-testing
REEL=/Users/bear/Documents/CoWork/bear-textbooks/books/brutalist.art/youtube/brutalist/claude-liam-brutalist-command-scene-index

python3 runtime/scripts/generate_audio_kokoro.py "$REEL/vertical"
python3 runtime/scripts/remotion_scenes.py     "$REEL/vertical"
python3 runtime/scripts/compile.py             "$REEL/vertical" \
    --height 3840 --out "$REEL/exports/vertical" --force
```

Output: `exports/vertical/claude-liam-brutalist-command-scene-index-vertical.mp4`,
2160×3840 · h.264 + AAC.

## Reformat law

Portrait is a different beat sheet, not a crop. Every beat re-renders
inside a native `*916` composition. No center-cut media. Long code
lines that don't wrap in the portrait card are documented, not hidden.
