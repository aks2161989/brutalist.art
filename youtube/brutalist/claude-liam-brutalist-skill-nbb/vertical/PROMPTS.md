# PROMPTS — The nbb Skill

Every prompt shown on screen or referenced in narration. This file is
the paper trail for a viewer who wants to reproduce the checks.

## B00 cold-open composer command (typed on screen)

```
What does the `nbb` skill actually do to a reel?
Read skills/make/nbb/SKILL.md and tell me — the mental model, not the
README summary.
```

Answer chips shown after "* running…":
- derives an NBB cut into a NEW nbb- directory
- canonical beat_sheet.json is NEVER modified
- scaffold is deterministic; the rewrite is Claude's job

## B10 Your-Turn composer command (paste this into Claude Code)

```
Read skills/make/nbb/SKILL.md.
Pick ONE delivered reel of your own at <book>/youtube/<my-slug>/.
Record `shasum -a 256 <that>/beat_sheet.json` first.
Then run:

    python3 runtime/scripts/brand_variant.py <book>/youtube/<my-slug> nbb

Do NOT rewrite narration, do NOT insert LLM exercise, do NOT append
outro, do NOT run generate_audio_kokoro.py or compile.py — this is a
SCAFFOLD-ONLY check.
```

Three-check rubric shown on screen:
- `<book>/youtube/nbb-<my-slug>/beat_sheet.nbb.json` exists?
- metadata reads `{NikBearBrown, teardown, kokoro, am_onyx}`?
- source `beat_sheet.json` SHA-256 unchanged?

## Local demo command (this reel actually ran, see demo/nbb-run.log)

```
python3 runtime/scripts/brand_variant.py \
    youtube/brutalist/claude-liam-brutalist-skill-nbb/demo/fixture-reel nbb
```

Output captured verbatim in `demo/nbb-run.log`.

## Not shown / not run

- No `art keys`, no `setup --install`.
- No paid TTS call. Voice = Kokoro `am_onyx` locally.
- The Step 2 register rewrite (Claude, guided by SKILL.md) is described
  but not run in this teardown. Doing it against a real reel is the
  viewer's assignment.
