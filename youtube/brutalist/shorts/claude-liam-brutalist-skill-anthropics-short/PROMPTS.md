# PROMPTS.md — The anthropics Skill — Short

*Every prompt shown on screen inside the retained beats. No prompt was written
or regenerated for this Short. No paid API was called; no external service was
contacted.*

## On-screen prompt (B00 · Cold open — `ClaudeComposerAsk916`)

```
Tear down the anthropics skill. What does it actually do, not just what it says?
```

Result lines shown under the composer (three, on-brand):

- `reads the artifact, not the docs`
- `four modes: --repo, --paper, --content, --capability`
- `publishes never.`

## Prompts intentionally cut from this Short

- **B09 Your Turn** (`ClaudeComposerAsk916` with a paste-ready
  `--capability` prompt + 3-item rubric) was dropped whole. Fellows who want
  the paste-ready assignment should watch the 16:9 long — the Short does not
  reproduce it and does not paraphrase it.

## Audio (retained, not regenerated)

Every kept beat's `mp3/beat-<Bxx>.mp3` was copied bit-for-bit from the parent's
`vertical/mp3/` folder. Voice: Kokoro `am_onyx` (local). No re-tts.

## Compile — 4K portrait

```
python3 runtime/scripts/compile.py \
  youtube/brutalist/shorts/claude-liam-brutalist-skill-anthropics-short \
  --height 3840 \
  --out youtube/brutalist/shorts/claude-liam-brutalist-skill-anthropics-short/exports/short
```

The compile runs the built-in Gate V and atomic verification. `--review` is NOT
used; the command above is the final. Output:
`exports/short/claude-liam-brutalist-skill-anthropics-short.mp4`.
