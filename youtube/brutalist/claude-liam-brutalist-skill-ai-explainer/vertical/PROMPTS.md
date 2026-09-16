# PROMPTS

## The paste-ready Your-Turn prompt (B09)

Copy-paste target for viewers:

```
Use the ai-explainer skill to build a 200-second reel about a concept in my
field, Liam voice (Kokoro am_onyx), @HumanitariansAI handle, no captions, no
publish. Then check: does the middle ILLUSTRATE (not wallpaper)? Does every
generated visual land after its ASK?
```

Expected artifact: a native `<slug>.mp4` next to the reel folder.
Success tests spoken during B09:

1. No two composer beats in a row anywhere in the middle.
2. Every generated visual (Manim, custom Remotion illustration, code block) is preceded by a composer ask beat carrying the actual generating prompt.

If either test fails, the reel is not done. Ask Claude to rebuild the offending beat, not the whole reel.

## The cold-open ask (B00, on screen only)

Not for the viewer to paste — it's the receipt of what THIS reel asked Claude to do:

```
Tear down the ai-explainer skill. Read the whole SKILL.md, explain the
mechanism, and show what happens when I run it.
```

## Build-side / operator prompts (not for viewers, kept for provenance)

### Author the beat sheet

```
Read skills/make/ai-explainer/SKILL.md end to end plus every file it
references (CLAUDE-BRAND.md, OUTRO-LOCK.md, runtime/prose/teardown/PROSE.md,
docs/PIPELINE-SAFETY.md, skills/make/nopunt/SKILL.md, skills/make/explainer/).
Then author beat_sheet.json for the reel
youtube/brutalist/claude-liam-brutalist-skill-ai-explainer/ with:

  metadata.playlist = "Brutalist"
  metadata.brand = "claude-liam"
  metadata.voice = metadata.voice_kokoro = "am_onyx"
  metadata.channel_title = "@HumanitariansAI"
  metadata.captions = false
  metadata.aspect_ratio = "16:9"

Bookends: B00 ClaudeComposerAsk (Hej, Liam), B01 BrutalistHesitantWriter with
seed and the reel's own misconception→claim correction (min ≥9s window),
B_verdict ClaudeVerdictArtifact, B_your-turn ClaudeComposerAsk with
greeting "Your Turn" and Liam reading the prompt aloud, B_outro
ClaudeTitleOutro. Body beats between them ILLUSTRATE — never two composer
beats in a row.
```

### Generate audio

```
python3 runtime/scripts/generate_audio_kokoro.py \
  youtube/brutalist/claude-liam-brutalist-skill-ai-explainer
```

Uses `metadata.voice_kokoro = am_onyx`. Writes `mp3/beat-B00…B10.mp3` and stamps `actual_duration_s` into every beat.

### Render scenes

```
python3 runtime/scripts/remotion_scenes.py \
  youtube/brutalist/claude-liam-brutalist-skill-ai-explainer
```

Renders every `shot.remotion.pattern` beat to `media/<BID>.mp4` at `--scale=2` (2160-tall for 16:9 comps, 3840-tall for 9:16 comps).

### Compile 4K landscape

```
python3 runtime/scripts/compile.py \
  youtube/brutalist/claude-liam-brutalist-skill-ai-explainer \
  --height 2160 --out youtube/brutalist/claude-liam-brutalist-skill-ai-explainer/exports/landscape
```

### Plan + render + compile portrait

```
./art vertical youtube/brutalist/claude-liam-brutalist-skill-ai-explainer
python3 runtime/scripts/remotion_scenes.py \
  youtube/brutalist/claude-liam-brutalist-skill-ai-explainer/vertical
python3 runtime/scripts/compile.py \
  youtube/brutalist/claude-liam-brutalist-skill-ai-explainer/vertical \
  --height 3840 --out youtube/brutalist/claude-liam-brutalist-skill-ai-explainer/exports/vertical
```
