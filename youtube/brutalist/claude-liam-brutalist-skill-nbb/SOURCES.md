# Sources — The nbb Skill

## Primary source (episode contract)

- `skills/make/nbb/SKILL.md`
  - Supervisor `episode.source_sha256`: `9b38c9ca6bbf23b7c1517307194ece925b9d970f289edad1c194391f5e6717e2`
  - SOURCE-SNAPSHOT.json SHA-256: `395389a3f3f1b249fda8ab67de2d0668210b50174270d531242b3c737f4626e4`
  - The two hashes differ because the snapshot was captured from the
    isolated toolkit which is at commit ba2d0e0 with local overrides; the
    supervisor hash is from a different revision of the same file. Both
    were read in full; the film explains the mechanism as documented in
    both, and every direct quote is attributed to the SKILL.md line.

## Referenced instruction files (all read in full)

- `skills/make/ai-explainer/SKILL.md` — governs the AI Explainer bookends
- `skills/make/nopunt/SKILL.md` — "if Brutalist can animate it, it never punts"
- `runtime/prose/teardown/PROSE.md` — Feynman × MKBHD register spec
- `runtime/scripts/brand_variant.py` — the actual code the nbb skill invokes
- `runtime/scripts/generate_audio_kokoro.py` — Kokoro TTS entry (voice=am_onyx)
- `runtime/scripts/remotion_scenes.py` — scene renderer (foreground, concurrency 1)
- `runtime/scripts/compile.py` — compiler (`--height 2160 --out`)
- `CLAUDE-BRAND.md`, `OUTRO-LOCK.md`, `CLAUDE-CODE-VISUAL-QC-CHECK.md`
- `docs/PIPELINE-SAFETY.md`, `docs/FELLOWS-SUBMISSION.md`

## Example leads (reference DATA, not verbatim republication)

- `rohan-v/2026-08-28-agent-first-brutalist/beat_sheet.json` — read for
  staging patterns for a submit-style episode. SHA-256
  `746409a8715e70aab6186145e963c08d088469b809b28fe39d44f5d8d06b1a22`.
  No content, prose, or human signature reused verbatim.
- `yatra-r/2026-09-03-this-week-gordy/beat_sheet.json` — read for the
  `WkBluf`/`WkStatus`/`WkTool` style. SHA-256
  `7e3ea1f61c421e605e583be9b2a7b5f554aa8cadfb6e14dabaee66f471856083`.
  Not republished; used only for structural reference.

## Local live demo (safe, source-not-modified)

- `demo/fixture-reel/beat_sheet.json` — synthetic 3-beat fixture created
  in this run, used solely as scaffold input.
- `demo/nbb-fixture-reel/beat_sheet.nbb.json` — the actual output of
  `python3 runtime/scripts/brand_variant.py demo/fixture-reel nbb` run
  from inside the isolated toolkit.
- `demo/nbb-run.log` — captured commands + captured stdout, including the
  before/after SHA-256 proof that the source is byte-identical.

## Not used

- No paid TTS engine (ElevenLabs removed 2026-09-03 per SKILL.md).
- No external network fetch, no `art keys`, no `setup --install` demo.
- No republished private Drive links or human signatures.
