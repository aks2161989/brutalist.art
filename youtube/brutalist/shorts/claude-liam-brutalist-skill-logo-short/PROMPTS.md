# PROMPTS — The logo Skill — Short (9:16)

The Short is a whole-beat cut of the parent vertical. No narration was
rewritten; no audio was regenerated for this derivative. The only prompt that
appears on-screen or is spoken is the cold-open ask in B00.

## Cold-open ask (B00, on-screen inside the ClaudeComposerAsk916 card)

> What does the `logo` skill actually do to a reel?
> Read `skills/make/logo/SKILL.md` and tell me — the mental model, not the
> README summary.

Runs against the installed Claude Code subscription; no external services,
no API key. The three result lines shown under the composer are the parent
author's summary of the mental model, not live Claude output.

## Your-Turn dry-run prompt

Dropped from this Short (parent B10). The detailed paste-ready assignment
belongs in the 16:9 long; a viewer who wants to run `logo.py --no-render
--no-compile` on their own reel should watch the parent long.

## Prompts used to produce this Short

- **Cut**: `python3 runtime/scripts/shorts.py <parent>/vertical
  --output-dir <reel> --slug claude-liam-brutalist-skill-logo-short
  --drop B02 B03 B06 B07 B10 --no-endcard --no-outro-rewrite`. Only the
  supervisor and the manual `--drop` selection were used; no LLM prompt
  invoked for the cut itself.
- **Compile**: `python3 runtime/scripts/compile.py <reel> --height 3840
  --out <reel>/exports/short`. Pure Python + ffmpeg; no LLM in the loop.
- **Audio**: none regenerated. The parent's Kokoro `am_onyx` mp3s were
  copied byte-for-byte into `short/mp3/`.
- **Render**: none. Every retained beat is the parent's already-rendered
  native 2160×3840 mp4, verified portrait by `ffprobe` and copied.

No paid API calls were made. The Claude Code subscription authored this
paperwork only. No `ANTHROPIC_API_KEY` fallback. No Higgsfield. No upload.
