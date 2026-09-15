# FACTCHECK.md — The sri-explainer Skill

Every claim traced back to `skills/make/sri-explainer/SKILL.md` (SHA-256
`63a052f7ab70c7c7ee29b0b16f70652eb5a07afc5180e43396446977afdb755b`) or
to a named parent skill file.

| Claim (as shown/said) | Verdict | Source location |
|---|---|---|
| Sri-explainer takes ONE chapter of a Prof Sridhar book and turns it into a video. | Supported | SKILL.md description block; `## When this skill (and when not)`; `## The chapter → beat spine`. |
| It is narrated in the register of the book itself. | Supported | Description ("in Sridhar's own written voice"); `## The Sridhar register`. |
| Extends `ai-explainer` (single-mechanism chapter) or `deep-explainer` (multi-section). | Supported | `## Lineage — what governs when`; `## When this skill (and when not)`. |
| Nothing below repeals a parent law. | Supported (verbatim). | `## Lineage — what governs when` — "nothing below repeals a parent law; this file adds the genre's own contracts." |
| Persona is Prof Sridhar in first person; NOT Liam / Bear / HAI. | Supported | `## Persona & channel` — "Sridhar narrates in first person as the chapter's author, the way the book itself is voiced." |
| Channel key is `claude-sri`. | Supported | `## Persona & channel` — table row Channel key = `claude-sri`. |
| Kokoro `am_onyx` reused from claude-liam as interim default; not yet in ALLOWED_VOICES / brand_variant.py. | Supported (verbatim). | Skill preamble ("BRUTALIST (pared-down) EDITION"): "Kokoro is the ONLY TTS engine. … giving Sri a voice of his own means extending `ALLOWED_VOICES` there first, which has NOT been done yet." Also `## Persona & channel` — "Not yet wired into `generate_audio_kokoro.py` (`ALLOWED_VOICES`) or `brand_variant.py`'s channel table — do that as a follow-up before the first real build." |
| Register move: NEGATE before AFFIRM. | Supported | `## The Sridhar register` — "state what a result is NOT before affirming what it IS." Also Hard rule 3: NEGATION-BEFORE-AFFIRMATION. |
| Sridhar prefers short punch-sentences after a longer explanatory one; concrete physical scale; number always anchored (an eV, room-temperature k_B T). | Supported | `## The Sridhar register` — Voice bullet, quoted directly. |
| DERIVATION-COMPRESSION LAW: never all N steps; extract 2–4 decision points, one beat each. | Supported | `## Hard rules` #1 — quoted verbatim. |
| GOLDEN-TEST-ON-SCREEN LAW: any number shown carries its own check, spoken and shown. | Supported | `## Hard rules` #2 — quoted verbatim (with "sharper than the parent's generic DOUBLE-CHECK LAW"). |
| HANDOFF-FROM-THE-CHAPTER LAW: YOUR TURN comes from the chapter's own "LLM Exercises." | Supported | `## Hard rules` #4 — quoted verbatim. |
| BRIDGE-HONESTY LAW: verdict states what the chapter did NOT resolve. | Supported | `## Hard rules` #5. |
| One chapter, one video — never combine chapters without an explicit ask. | Supported | `## Hard rules` #6. |
| Two visual looks (Cream default / Notebook dark). | Supported | `## Visual look (body beats)` — table. Not staged on-screen in this reel (mentioned only in narration cover) — no visual claim beyond the mention. |
| Reference files listed: `reference/prof-sridhar-style.md` and `reference/notebook-look.md`. | Supported | `## Reference files (this folder)`. Two files match B02's anatomy card. |
| Slug convention for a real build: `claude-sri-[chapter-slug]` inside the owning book's `youtube/` folder. | Supported | `## Output contract`. |

## Corrections applied

- **No versioned model claims.** The narration never cites a specific
  Claude model version. Skill file does not name a version, so the
  film does not either.
- **No promise of unlimited generation.** BUILD-PROMPT reminded that
  free path uses Kokoro locally; script never suggests unlimited paid
  use.
- **No fabricated chapter demo.** B10 explicitly documents the
  limitation (a real Sridhar chapter file was not available for this
  run). No chapter prose is quoted; no numeric "worked example" is
  invented.
- **Persona clarity.** The narrator is Liam, in for Bear (this is a
  Brutalist playlist film ABOUT the skill). The film explicitly
  distinguishes that from the skill's own persona (Prof Sridhar) that a
  live sri-explainer build would voice.

## Known limitations (documented in film)

- B10 restates: this reel demonstrates the *mechanism* of sri-explainer
  from its own SKILL.md; it does NOT execute a real chapter →
  video pipeline. That would require a Sridhar chapter file, the
  claude-sri voice added to `ALLOWED_VOICES` / `brand_variant.py`,
  and a factcheck pass on that chapter's own numbers.
