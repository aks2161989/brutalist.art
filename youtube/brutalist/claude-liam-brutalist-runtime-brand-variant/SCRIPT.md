# SCRIPT — Brutalist Utility: brand_variant.py

**Episode:** claude-liam-brutalist-runtime-brand-variant
**Voice:** Kokoro `am_onyx` (Liam, in for Bear)
**Register:** Teardown
**Channel adaptation:** composer chip reads `@HumanitariansAI`; outro card stays the locked `ClaudeTitleOutro` (hardcoded `@NikBearBrown` per `OUTRO-LOCK.md`) and is flagged in `README.md` for the human reviewer before publish.

The word count target is the audio-first budget in `ai-explainer/SKILL.md` — body beats 45–70 words; the ask, the BLUF, the handoff and the verdict are exempt where they earn it.

---

## B00 — ASK (cold open, `ClaudeComposerAsk`)
Greeting: `Yassou, Liam` (Greek, one word, fresh — see the `greeting_note` in `beat_sheet.json`).

> Yassou, this is Liam, in for Bear. The ask — I have one canonical beat sheet, and I need three audience variants — Claude, NikBearBrown, Humanitarians AI — without touching the original. Stamp the metadata deterministically. Leave the creative rewrite to me.

## B01 — BLUF (hesitant writer, `BrutalistHesitantWriter`)
Correction is the reel's actual misconception. Text starts `brand_variant.py / rewrites narration.` and settles on `brand_variant.py / stamps metadata.` — because that is what the whole file is arguing: the metadata is deterministic; the register rewrite is Claude's creative job. (The portrait beat uses a 5-line version with the same triggers on late lines so the caret carries the ink bbox past Gate V's 55% coverage floor.)

> Watch the writer walk this back. Brand variant dot py does not rewrite the narration; it stamps the metadata, drops a to-do list, and steps back — Claude does the register rewrite in whichever voice the audience wants.

## B02 — FRAMEWORK (concept illustration, `SkillTeardownPipeline`)
INPUT `reel/beat_sheet.json + audience` → phases `RESOLVE → STAMP → TODO → EMIT` → OUTPUT `<suffix>-<slug>/beat_sheet.<suffix>.json`.

> Here is the pipeline. Take the canonical beat sheet in the reel folder. Pick an audience — Claude, N B B, or H A I. Resolve the destination folder. Stamp the audience metadata. Write the audience specific to-do list. Emit beat sheet dot audience dot json — creative rewrite deferred to Claude.

## B03 — MECHANISM 1 (code, `ClaudeCodeBeat`)
The CLI surface, verbatim from `--help`, plus the audience-key legend.

> The command surface is small. Two required positionals: the reel or lecture folder, and one of three audience keys — claude dash liam, n b b, or h a i. One optional flag: dash dash force resets an existing variant from the canonical. Everything else — voice, palette, register — is stamped from a lookup table.

## B04 — WORKED EXAMPLE (code, `ClaudeCodeBeat`)
Verbatim from `demo/RUN-LOG.txt` §2+§5 — canonical → hai.

> One canonical beat sheet, one audience, one variant. Run brand variant on demo slash canonical with h a i. It writes a sibling folder — h a i dash canonical — and inside it, beat sheet dot h a i dot json. The metadata gets audience H A I, register Plain, palette humanitarians, voice a f bella, and a five step to-do list telling Claude what to rewrite next.

## B05 — MECHANISM 2 (code, `ClaudeCodeBeat`)
The `AUD` lookup — the whole configuration in one dict.

> The audience lookup table is where the whole shape lives. Three keys. Each maps to a suffix, an audience label, a palette, a register, a charter file, an outro author section, an engine — always kokoro — and a kokoro voice. Two voices ship: a m onyx for claude dash liam and n b b, a f bella for h a i. Anything else is not scaffoldable — the choices arg parser rejects it.

## B06 — MECHANISM 3 (code, `ClaudeCodeBeat`)
`get_brand_dir()` — reel vs lecture destination routing.

> The destination folder is routed by a tiny function. If the reel path contains a directory named lectures, the sibling lands in book slash suffix dash lectures slash chapter dash lecture. Otherwise it lands in the reel's parent, as suffix dash reel name. Either way, the canonical folder is left alone and the variant is a real sibling on disk — not an overwrite.

## B07 — MECHANISM 4 (code, `ClaudeCodeBeat`)
`main()` body — refuse, stamp, strip.

> The main function does three things. One — refuse to overwrite an existing variant unless dash dash force is set, and refuse to run at all if the canonical is missing. Two — stamp the audience metadata: audience, register, palette, outro source, engine, voice. Pop the legacy voice id key — there are no paid engines in this toolkit. Three — walk every beat, strip actual duration and shot dot rendered stamps so the new variant recomputes its own timings after Claude finishes.

## B08 — WORKED EXAMPLE 2 (code, `ClaudeCodeBeat`)
The refusal cases — verbatim from `demo/RUN-LOG.txt` §10-§12.

> The safety cases. Re-run brand variant on the same reel with the same audience — no dash dash force — and it refuses with exit code one. The message names the existing file. Add dash dash force and it rewrites. Point it at a folder with no beat sheet dot json and it also refuses, with exit code one and the reason printed. In both refusals, nothing on disk changes.

## B09 — VERDICT (`ClaudeVerdictArtifact`)
The whole file, in the order it does its job. Six lines.

> So — brand variant dot py. The scaffold. It reads one canonical beat sheet, picks an audience from the lookup table, resolves the sibling folder, stamps the metadata, writes the audience specific to-do list, strips stale timings, and emits one variant beat sheet. It refuses to overwrite without dash dash force. It never modifies the canonical. Everything after — the rewrite, the audio, the render — is a separate step.

## B10 — YOUR TURN (`ClaudeComposerAsk`, greeting `Your Turn`)
Prompt is read aloud verbatim then discussed.

> Your turn. Paste this into Claude Code, pointed at any reel that already has a canonical beat sheet: run brand variant with the h a i audience, then diff the two metadata blocks and tell me — which keys were added, which were changed, which were popped. Watch for whether Claude is tempted to also edit narration text on this pass. That is not this script's job. Brand variant dot py stamps metadata and hands the microphone to the rewrite skill.

## B11 — OUTRO (`ClaudeTitleOutro`, slug-seeded mascot, hardcoded `@NikBearBrown`)

> Brutalist Utility: brand variant dot py. Liam, in for Bear, for at Humanitarians A I.
