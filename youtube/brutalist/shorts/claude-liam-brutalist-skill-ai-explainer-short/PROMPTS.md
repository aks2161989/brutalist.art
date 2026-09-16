# PROMPTS — Short cut

## The cold-open ask (B00, on screen only, unchanged from parent)

Not for the viewer to paste — it's the receipt of what the parent long-form
reel asked Claude to do, and this Short reuses B00 unchanged:

```
Tear down the ai-explainer skill. Read the whole SKILL.md, explain the
mechanism, and show what happens when I run it.
```

## Your-Turn prompt (dropped in the Short cut)

The parent B09 read a paste-ready prompt aloud. That extended Your Turn was
removed for this Short (see CUT-PLAN.json → `dropped_beats[1]`). The full
paste-ready prompt still lives in the parent reel's `PROMPTS.md` and the
long-form 16:9/9:16 companion; the Short does not reproduce it because
REPOLOOP-SHORTS-PROMPT.md explicitly permits omitting the long's full
exercise.

## Build-side prompt for this Short (kept for provenance)

```
Cut the parent claude-liam-brutalist-skill-ai-explainer/vertical (11 beats,
186.65s) into a Short strictly under 3:00. Whole-beat cut first:
  drop B02 (generic skill-folder anatomy — belongs in the long)
  drop B09 (extended Your Turn — REPOLOOP-SHORTS-PROMPT.md override)
Keep B00 B01 B03 B04 B05 B06 B07 B08 B10 (all internal numbered references
resolve). Reuse native portrait media unchanged. No audio regeneration.
No endcard, no outro rewrite. Compile at --height 3840. Verify
strictly < 180s across container, video, and audio streams.
```

Executed as:

```
python3 runtime/scripts/shorts.py \
  youtube/brutalist/claude-liam-brutalist-skill-ai-explainer/vertical \
  --output-dir youtube/brutalist/shorts/claude-liam-brutalist-skill-ai-explainer-short \
  --slug claude-liam-brutalist-skill-ai-explainer-short \
  --drop B02 B09 --no-endcard --no-outro-rewrite
python3 runtime/scripts/compile.py \
  youtube/brutalist/shorts/claude-liam-brutalist-skill-ai-explainer-short \
  --height 3840 \
  --out youtube/brutalist/shorts/claude-liam-brutalist-skill-ai-explainer-short/exports/short
```

No API result was faked. No paid service was called.
