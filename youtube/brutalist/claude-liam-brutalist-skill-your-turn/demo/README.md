# demo/ — safe, local your-turn demo

Everything in this folder is a synthetic fixture used to demonstrate the
your-turn skill's mechanism WITHOUT touching a real reel. Zero paid API
calls. Zero network. The transformer runs against `fixture-beat_sheet.json`
and writes reports here.

## Files

- `fixture-beat_sheet.json` — synthetic input; body beats voiced `elevenlabs`
  (Bear) so the transformer must select the "Thanks Bear, let's recap with
  Claude." handoff. Existing verdict artifactLines carry `1.` / `2.` / `3.`
  prefixes so the leading-number stripper has something to remove. The YOUR
  TURN and OUTRO beats hold obvious placeholders the transformer must rewrite.
- `drafts.json` — the human-reviewed draft that pairs the fixture's slug with
  a real, video-relevant prompt (3-part ask, first person). `recap` is null
  because the fixture already has a verdict card.
- `demo-report.json` — dry-run output. What the transformer WOULD do.
- `demo-applied-report.json` — full apply output. Same notes.
- `demo-idempotent-report.json` — re-run of full apply. Byte-identical output
  (md5 of `fixture-beat_sheet.applied.json` is unchanged) — idempotency.
- `fixture-beat_sheet.applied.json` — the fixture after the transformer runs.
- `diff.txt` — the diff between the input and the applied fixture.

## Commands (verbatim, run 2026-09-09)

```
$ cd youtube/brutalist/claude-liam-brutalist-skill-your-turn/demo
$ python3 …/skills/make/your-turn/scripts/apply_your_turn.py \
    fixture-beat_sheet.json --drafts drafts.json \
    --report demo-report.json --dry-run
changed=1 inserted_verdict=0 skipped=0 needs_prompt=0 errors=0 (dry-run)
report -> demo-report.json

$ cp fixture-beat_sheet.json fixture-beat_sheet.applied.json
$ python3 …/skills/make/your-turn/scripts/apply_your_turn.py \
    fixture-beat_sheet.applied.json --drafts drafts.json \
    --report demo-applied-report.json
changed=1 inserted_verdict=0 skipped=0 needs_prompt=0 errors=0

$ md5sum fixture-beat_sheet.applied.json
78c9dbf88a8bb124431f1f938e6afd46  fixture-beat_sheet.applied.json
$ python3 …/skills/make/your-turn/scripts/apply_your_turn.py \
    fixture-beat_sheet.applied.json --drafts drafts.json \
    --report demo-idempotent-report.json
changed=1 inserted_verdict=0 skipped=0 needs_prompt=0 errors=0
$ md5sum fixture-beat_sheet.applied.json
78c9dbf88a8bb124431f1f938e6afd46  fixture-beat_sheet.applied.json
```

The apply script reports `changed=1` on the second run because it always
re-writes the block (the notes are the same), but the file bytes do not
change — the transformer is idempotent as documented.

## What the diff proves (see `diff.txt`)

- **VERDICT** — `"1. Owned"` / `"2. Inherited"` / `"3. Idempotent"` had their
  leading numbers stripped. `"Thanks Bear, let's recap with Claude."` was
  prepended to `narration_text` because the previous beat's `engine` is
  `elevenlabs`. `lead_silence_s: 0.5` was added.
- **YOUR TURN** — `narration_text` and `props.command` were both replaced by
  the drafts.json prompt (single string, identical in both slots).
- **OUTRO** — `narration_text` and `props.title` were both replaced by
  `metadata.title` (`"The Fictional Skill"`). `props.handle` was set to
  `@NikBearBrown`.
