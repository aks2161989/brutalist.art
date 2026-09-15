# PROMPTS.md — The hai Skill

The paste-ready prompts shown or referenced in the film.

## B00 — Cold open composer

```
What does the `hai` skill actually do to a reel? Read skills/make/hai/SKILL.md and tell me — I want the mental model, not the README summary.
```

Expected 3-line output shown on screen:
- forks the reel into a new hai- directory
- rewrites the register to Plain + adds a CLI exercise
- source beat_sheet.json is never modified

## B10 — Your Turn composer (paste-ready)

```
Read skills/make/hai/SKILL.md. Then, WITHOUT shipping the reel:

1. Pick one of my delivered reels at youtube/<my-slug>/.
2. Record its beat_sheet.json SHA-256.
3. Run: python3 runtime/scripts/brand_variant.py youtube/<my-slug> hai
4. Compare the source's SHA-256 to the pre-run value. Assert equal.
5. Draft the Plain-register rewrite of ONE body beat in the new hai-<my-slug>/beat_sheet.hai.json. It MUST have three lines:
   (a) method — what it is, what it produces;
   (b) when to use it;
   (c) when NOT to and where it fails.
6. Draft the CLI worked exercise for the second-to-last beat using the five-part schema: lane (BUILD or RESEARCH), ask, output_description, change, output2_description, next_step. The ask must be a claude "…" command a practitioner can run today against their own data.

Do NOT run generate_audio_kokoro.py or compile.py. Do NOT touch the source beat_sheet.json.
```

Rubric shown as the composer's 3-line output:
- check: source beat_sheet.json SHA-256 unchanged after scaffold?
- check: rewritten beat names a specific failure mode ("do not use when …")?
- check: CLI ask runs on real data today — not illustrative, not synthetic?

## Referenced but not typed on screen

- The batch-mode shell block from SKILL.md §162 (rendered inside the B07 body text as prose, not as a runnable card).
- The verbatim SKILL.md quotes shown in B04, B05, B06, B07, B08 are line-cited in `FACTCHECK.md`.
