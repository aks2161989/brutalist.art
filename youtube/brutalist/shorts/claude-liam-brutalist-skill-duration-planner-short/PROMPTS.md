# PROMPTS — The duration-planner Skill · Short (9:16)

This Short is a whole-beat cut of the parent portrait companion. The only
prompts that appear on-screen are those in the retained beats' Remotion props;
no prompt was rewritten for this cut.

## Retained composer prompt (B00, seen on screen)

```
How long should this video be? Read skills/make/duration-planner/SKILL.md and
tell me how the skill actually decides.
```

Running-text hint (below the composer):
```
reading skills/make/duration-planner/SKILL.md…
```

Three "output" lines below the composer:
- `duration is an OUTPUT, not a target`
- `script-sizing and holds are the two real levers`
- `content_type sets the consolidation floor`

## Dropped composer prompt (B09, NOT in this Short)

The parent film's Your Turn beat carries a paste-ready `pace_check.py` prompt
plus three viewer checks. It is preserved unchanged in the parent 16:9 long
and its native portrait companion. Not present in this Short — see
`CUT-PLAN.json` and `FACTCHECK.md § Delta from parent`.

## Toolkit invocations that produced this Short (not seen on screen)

```bash
python3 runtime/scripts/shorts.py \
  youtube/brutalist/claude-liam-brutalist-skill-duration-planner/vertical \
  --output-dir youtube/brutalist/shorts/claude-liam-brutalist-skill-duration-planner-short \
  --slug claude-liam-brutalist-skill-duration-planner-short \
  --drop B02 B03 B06 B09 \
  --no-endcard \
  --no-outro-rewrite

python3 runtime/scripts/compile.py \
  youtube/brutalist/shorts/claude-liam-brutalist-skill-duration-planner-short \
  --height 3840 \
  --out youtube/brutalist/shorts/claude-liam-brutalist-skill-duration-planner-short/exports/short
```

No `remotion_scenes.py` pass was needed — every retained parent beat was
already native 2160×3840 and copied byte-identical.

## No generation, no upload

- No Kokoro regeneration; every retained `mp3/beat-Bxx.mp3` is byte-identical
  to the parent.
- No Remotion re-render; every retained `media/Bxx.mp4` is byte-identical to
  the parent.
- No paid generation, no upload, no publish, no push. This is a render-only
  Short.
