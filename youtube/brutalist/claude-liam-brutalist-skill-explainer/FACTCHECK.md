# FACTCHECK — The explainer Skill

Every factual claim in the narration is a quote from, or a direct paraphrase
of, `skills/make/explainer/SKILL.md` (SOURCE-SNAPSHOT SHA-256
`b0b761f4…`; invocation `episode.source_sha256`
`c6bf131d…`). No numbers, quotes or mechanisms are invented.

Updated 2026-09-11: B07 narration revised to cover the new EXECUTABLE-EVIDENCE.md
reference added to VOX LAW. The claim "if your evidence is locally reproducible —
execute it and render it" paraphrases the new paragraph verbatim from the updated
SKILL.md §VOX LAW.

## Verbatim quotes shown on screen

| Beat | On-screen quote | Location in SKILL.md |
|---|---|---|
| B04 | "Not a style — a laundering function. Sources never match; the treatment does." | §"What Vox actually is" |
| B05 | "Collapsing them makes every swap a re-edit; separating them makes swaps free." | §"THE TWO-AXIS SHOT SYSTEM" |
| B06 | "Rebuild recompiles ONLY slots whose input hash changed, then re-concats." | §"THE SLOT CONTRACT" |
| B07 | "There is no share to hit… any prior guidance stating a target percentage of vox body beats is superseded by this law." | §"VOX LAW — a still is EVIDENCE, never texture" (also cites EXECUTABLE-EVIDENCE.md for the executable-evidence clause) |

All quotes copy-pasted (with normal ellipsis condensation on B07 where the
skill text is longer than one poster line). No paraphrase-shown-as-quote.

## Narration factual claims — checked against source

| Claim | Source line(s) | Verdict |
|---|---|---|
| "explainer is a PRODUCTION COMPOSITING PIPELINE, not a previz renderer" | SKILL.md §description | verbatim (headline) |
| "any source passes through one treatment — desaturate ~80%, contrast 1.15, seated on a real newsprint scan" | SKILL.md §"Design tokens" and §"What Vox actually is" | matches |
| "sources never match; the treatment does" | SKILL.md §"What Vox actually is" | verbatim |
| "shot.type ∈ {STILL, FOOTAGE, DOCUMENT, GRAPHIC, COMPOSITE, CARD}" | SKILL.md §"THE TWO-AXIS SHOT SYSTEM" (table) | verbatim |
| "shot.source ∈ {archive, ai, own}" | SKILL.md §"THE TWO-AXIS SHOT SYSTEM" | verbatim |
| "shot.type is locked at plan gate; shot.source is late-bound, swappable" | SKILL.md §"THE TWO-AXIS SHOT SYSTEM" | verbatim ("locked at the plan gate, never changes … late-bound, swappable") |
| "precedence: media/[beat].mp4 > manim/[beat].mp4 > media/[beat].png > slate" | SKILL.md §"THE SLOT CONTRACT" first bullet | verbatim |
| "first pass is always a watchable film with slates" | SKILL.md §"THE SLOT CONTRACT" | matches (paraphrase, same content) |
| "rebuild recompiles only slots whose input hash changed" | SKILL.md §"THE SLOT CONTRACT" bullet 2 | verbatim |
| "voiceover (Kokoro) is the master clock; free and local" | SKILL.md §"The clock" | matches ("Kokoro mp3 per beat … free and local") |
| "the still IS the evidence — the swap test" | SKILL.md §"VOX LAW" | matches ("The test, and it is one question…") |
| "if your evidence is locally reproducible — execute it and render it" | SKILL.md §"VOX LAW" new paragraph (2026-09-11 update): "Locally reproducible code, errors, tables and charts must be executed and rendered from their evidence, not sourced as terminal/notebook photographs." | paraphrase matches verbatim |
| "Princeton's admissions record — yes; a stock photo of a university — no" | SKILL.md §"VOX LAW" | verbatim example |
| "a pantry still is the single most expensive beat in the system" | SKILL.md §"VOX LAW · Why the rule is this strict" | matches |
| "every other explainer inherits from this skill" | SKILL.md metadata + ai-explainer's §"Lineage: an EXTENSION of `explainer`" (verified in the sibling skill file) | matches |

## Claims deliberately NOT made

- No promise that any specific runtime script exists in this snapshot beyond
  what the SKILL.md's own file paths reference (`generate_audio_kokoro.py`,
  `pantry.py`/`vox_pantry.py`, `compile.py`, `vox_outro.py`). The B02 anatomy
  tree names the folders and doctrine files but does not claim a `scripts/`
  child exists inside `skills/make/explainer/` — the run-belt scripts live at
  `runtime/scripts/` in the toolkit and are referenced by the skill, not
  bundled inside its folder.
- No promise about a specific total runtime target. B08's verdict states the
  skill produces "a pipeline. Not a style" and that the "first pass is always
  a watchable film."
- No claim that a specific reel has been shipped — the tuning is doctrine, not
  a case study.
- The B03 pipeline diagram is a hand-authored illustration of the phases the
  SKILL.md describes (script → beats → audio → media → assemble), not a
  screenshot of a tool's output.

## Third-party / evidence claims

The SKILL.md references `EQUATIONS.md`, `MOTION.md`, and `REMOTION.md` for
the doctrine that governs specific beat types (equation tangents, motion
languages, annotation-plane spec). These are named in B02 as part of the
anatomy but not quoted verbatim; the reel restates the SKILL.md's own summary
of what each file governs, which is what a teardown should do.

## Corrections / hedges preserved from source

- VOX LAW's "no share to hit" — carefully preserved as a NEGATIVE verdict
  pill ("zero vox is a correct outcome") in B07 so viewers understand it is
  a permission to have no vox beats, not a mandate to have one. That is the
  skill's own emphasis (introduced 2026-09-02 in the SKILL.md history line).
- Design-tokens numbers (desaturate 80%, contrast 1.15) are called out with
  the "about" hedge in narration since the skill uses "~80%" in the source.

## Handoff prompt (B09) — verified paste-ready

The prompt asks the viewer to run `slate cut` on their own concept. This
matches the SKILL.md's own advertised behaviour of the command word:
"`slate cut [candidate card | chapter | concept]` … run the whole chain
end-to-end and STOP at the finished review cut". Nothing in the prompt asks
the skill to do something the SKILL.md doesn't say it does. The three-check
rubric restates the DOUBLE-CHECK, VOX LAW, and shot.type/source rules that
already govern the skill.

## Availability log — what runs locally, what does not

- `generate_audio_kokoro.py` — RUN in this session; produced 11 mp3s
  (mp3/beat-B00..B10.mp3), total ~252 s narration, free/local, $0.00.
- `remotion_scenes.py` — RUN in this session; rendered 11 beats as
  media/B00..B10.mp4. Chrome wrapper (`chrome_wrap.sh`) created to survive the
  Apple App Sandbox Mach-port block, using the cached
  `chrome-headless-shell` from
  `runtime/remotion/node_modules/.remotion/chrome-headless-shell/…`.
- `compile.py` — RUN; landscape master compiled to 3840×2160.
- `final_frame_check.py` — RUN as GATE V.
- `slate cut` self-demo — NOT run in this reel. Running it here would produce
  a second reel, not a teardown of the skill. The B09 handoff prompt is
  paste-ready so a fellow can invoke it in their own environment. Recorded
  honestly in CHECKS-REPORT.md.
- `pantry.py` — NOT run in this reel (no external stills — the reel is
  entirely native scenes on cream by design; VOX LAW makes zero-vox a correct
  outcome for a doctrine teardown).
- `scripts/type_check.py` (GATE T) — NOT SHIPPED in this snapshot. Absence
  recorded honestly; visual typography reviewed manually per Gate V frames.
