# PROMPTS — Brutalist Utility: brand_variant.py — Short

This Short retains B00's cold-open ask; the long-form Your-Turn exercise (B10)
was cut. The paste-ready prompt below is preserved from the parent for the
handful of viewers who want to try `brand_variant.py` on their own reel after
watching the 9:16 cut. It is not spoken in this Short.

## Cold-open ask (B00, verbatim)

```
One canonical beat_sheet.json, three audience variants — Claude, NikBearBrown,
Humanitarians AI. Stamp the metadata deterministically. Never touch the
canonical. Leave the creative rewrite to me.
```

Composer output lines shown under the ask:

- reads `reel/beat_sheet.json`
- writes sibling `<suffix>-<slug>/beat_sheet.<suffix>.json`
- stamps audience metadata + `_variant_todo` list

## For viewers who want to try it (not read on-screen)

```
Point Claude Code at any reel folder that already has a canonical
beat_sheet.json:
  (1) run `python3 runtime/scripts/brand_variant.py <that folder> hai`;
  (2) diff the canonical .metadata and the new hai-<slug>/beat_sheet.hai.json
      .metadata blocks;
  (3) name the ADDED, CHANGED, POPPED keys.
  Do NOT edit narration_text on this pass — that is the hai skill's job.
```

Expected diff, from FACTCHECK:

- **ADDED** on a fresh sheet: `audience`, `derived_from`, `register`, `palette`,
  `outro_source`, `voice_kokoro`, `_variant_todo`, `typography`, `channel_title`.
- **CHANGED**: `engine` (canonical was `elevenlabs` in the demo fixture; stamp is
  always `kokoro`).
- **POPPED**: `voice_id` — the one deliberate deletion, `brand_variant.py:91`.

## Prompts NOT to paste

- `brand_variant.py <reel> <audience> --force` immediately after a fresh
  run — `--force` is "reset to canonical", not "regenerate keeping my edits".
- Any `sed`/`jq` script that appends to `_variant_todo` — the list is the
  ai-explainer / hai / nbb SKILL.md contract; editing it detaches the variant
  from the skill's expected inputs.
- Any audience string outside `{claude-liam, nbb, hai}` — argparse rejects with
  `invalid choice`; there is no paid-engine slot on purpose.
