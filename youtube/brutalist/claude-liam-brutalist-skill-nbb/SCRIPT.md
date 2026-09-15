# The nbb Skill — script (v1)

> AI Explainer, teardown treatment. Voice: **Kokoro am_onyx** — **Liam, in
> for Bear**. Playlist: Brutalist. Channel: **@HumanitariansAI** on inner
> composer chips; **@NikBearBrown** on the outro card per OUTRO-LOCK.md.
> Run ID: `176246a8e8ea447f812f68cd066bcb46` (original build `fdf9abc5ba3f40eba314b9262f54a0bc`).

## Cold open — B00 · ClaudeComposerAsk (~16s)

> Hola, this is Liam, in for Bear. Today we tear down the nbb skill. It is
> the one command that takes any reel or lecture and derives an NBB channel
> cut of it — a new nbb-directory, a scaffolded beat sheet, and a Teardown
> register waiting to be written. Here is the mental model.

Composer answer lines:
- derives an NBB cut into a NEW nbb- directory
- canonical beat_sheet.json is NEVER modified
- scaffold is deterministic; the rewrite is Claude's job

## BLUF — B01 · BrutalistHesitantWriter (~19s)

Line 1: **The nbb skill**
Line 2 (writes then deletes): **rewrites your reel.** → **scaffolds your reel.**
Line 3: **Source never modified.**

> The easy read — the one the name invites — is that nbb rewrites your reel.
> It does not. The nbb skill scaffolds an empty nbb-container next to your
> source, presets the metadata for the NikBearBrown channel, and hands
> Claude a checklist. The narration rewrite, the LLM exercise, and the
> outro are Claude's work. The canonical source is never touched.

## Framework 1 — B02 · Anatomy (~34s)

The five files on disk:
- `skills/make/nbb/SKILL.md` — doctrine (accent)
- `runtime/scripts/brand_variant.py` — the scaffolder
- `runtime/prose/teardown/PROSE.md` — Feynman × MKBHD register (accent)
- `brands/nbb.md` — NikBearBrown brand card
- `runtime/remotion/src/tokens/vox.ts` — teardown palette

Callout: **Source is NEVER modified.**

## Framework 2 — B03 · Pipeline (~35s)

- input: reel · lecture · or a whole book (batch)
- SCAFFOLD (accent) → brand_variant.py, no spend
- REWRITE → every narration_text → Teardown register
- LLM EXERCISE → second-to-last, paste-ready + dig-deeper
- OUTRO → NikBearBrown outro from AUTHOR.MD
- VERIFY → body → [LLM] → [outro]
- output: `nbb-[slug]/beat_sheet.nbb.json`

## Mechanism 1 — B04 · Source is never modified (~32s)

Standing rule verbatim: *"Source files (beat_sheet.json, build scripts,
media) are NEVER modified."* Second run refuses; `--force` resets from
canonical. Delete the nbb- dir → clean slate.

## Mechanism 2 — B05 · Two halves. Only one is code (~36s)

Deterministic half in `brand_variant.py`: metadata (audience, palette,
register, engine, voice, typography, outro_source). No API. No spend.
Creative half is Claude: register rewrite, LLM exercise, outro. Guided by
SKILL.md + prose/teardown/PROSE.md.

## Mechanism 3 — B06 · Ends with a prompt, not a summary (~29s)

Two-part LLM exercise beat: paste-ready prompt + dig-deeper follow-up.
Card in teardown palette; both parts read by Liam.

## Mechanism 4 — B07 · Liam. In for Bear (~29s)

Voice = Kokoro `am_onyx`. Free, local. IN-FOR-BEAR LAW: Liam introduces
himself in the cold open and signs off the same way; never imitates Bear.
ElevenLabs permanently removed 2026-09-03.

## Falsifiability — B08 · _variant_todo is a checklist, not code (~38s)

Batch mode on a book folder scaffolds every reel and every lecture —
deterministic, no spend. But the register rewrite is Claude's judgment,
not a loop.

## Verdict — B09 · ClaudeVerdictArtifact (~34s)

Six lines, teardown-palette artifact card. See beat_sheet.json B09
`artifactLines`.

## Your Turn — B10 · ClaudeComposerAsk (~40s)

Paste-ready DRY-RUN prompt: run brand_variant.py on a delivered reel with
`nbb` audience, then verify the three checks — new nbb- dir exists,
metadata is right, source SHA-256 unchanged. Do NOT rewrite / render /
compile.

## Outro — B11 · ClaudeTitleOutro (~4s)

> That was the nbb Skill. Liam, in for Bear.

Title card: **The nbb Skill.** Handle: **@NikBearBrown** (OUTRO-LOCK).
