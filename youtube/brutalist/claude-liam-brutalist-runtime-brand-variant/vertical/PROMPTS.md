# PROMPTS — Brutalist Utility: brand_variant.py

## Cold-open ask (B00)

```
I have one canonical beat_sheet.json and I need three audience variants — Claude,
NikBearBrown, Humanitarians AI — without touching the original. Stamp the
metadata deterministically (engine, kokoro voice, palette, register, outro
source, typography). Leave the register rewrite for me; I want a to-do list in
the variant metadata telling me exactly what to do next.
```

Composer output lines (what the ask lands with):

- reads `reel/beat_sheet.json` — writes a sibling `<suffix>-<slug>/beat_sheet.<suffix>.json`
- stamps audience metadata: engine=kokoro, kokoro voice, palette, register, outro source
- writes `_variant_todo` — the instructions Claude follows to rewrite each beat

## Your-Turn prompt (B10, verbatim)

```
Point Claude Code at any reel folder that already has a canonical
beat_sheet.json:
  (1) run `python3 runtime/scripts/brand_variant.py <that folder> hai`;
  (2) load the canonical .metadata and the new <hai>-<slug>/beat_sheet.hai.json
      .metadata into your context;
  (3) tell me — which keys were ADDED (present in variant, absent in canonical),
      which were CHANGED (present in both, different values), which were POPPED
      (present in canonical, absent in variant).
  (4) Do NOT edit any narration_text on this pass. Explain in one line why
      brand_variant.py leaves that job to the audience-specific skill
      (skills/make/hai/SKILL.md) rather than doing it itself.
```

## What the fellow should look for

- **ADDED** on a fresh sheet: `audience`, `derived_from`, `register`, `palette`,
  `outro_source`, `voice_kokoro`, `_variant_todo`, plus `typography` for hai/nbb
  and `channel_title` for hai. On a canonical that already has any of these,
  they are **CHANGED**, not added.
- **CHANGED**: `engine` (usually `kokoro` in a Brutalist canonical, but a
  legacy `elevenlabs` value would be stamped over — see `demo/canonical` for
  the deliberately stale fixture).
- **POPPED**: `voice_id` — the paid-engine identifier from earlier eras. This
  is the one deliberate deletion in the whole script (`brand_variant.py:91`).
- The single-line note the fellow should produce: the register rewrite (Plain,
  Teardown) is a creative act that only Claude can do coherently; the utility
  keeps the deterministic transform separate so it stays diffable, replayable,
  and safe to `--force`.

## Prompts NOT to paste

The following are red flags in a fellow's follow-up. If Claude Code offers to
run any of them, hold the fellow back:

- `brand_variant.py <reel> claude-liam --force` immediately after a fresh
  run — it silently discards any partial rewrite already in the variant.
  The `--force` flag is a "reset to canonical", not a "regenerate keeping my
  edits".
- Any `sed`/`jq` script that adds keys to `_variant_todo` — the todo list is
  the ai-explainer / hai / nbb SKILL.md contract; editing it detaches the
  variant from the skill's expected inputs.
- `rm -rf demo/canonical/beat_sheet.json` and rebuild — the canonical is the
  authority; deleting it forces every downstream variant to reconstruct their
  narration by hand.
- `python3 brand_variant.py <reel> elevenlabs` or any audience string not in
  `{claude-liam, nbb, hai}` — argparse rejects with `invalid choice`; a
  fellow tempted to add a fourth key should read the AUD dict first (there is
  no paid-engine slot on purpose).
