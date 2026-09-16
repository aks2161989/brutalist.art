# FACTCHECK.md — The hai Skill

Every factual claim the narration makes, with the source line that carries it.

## B00 (ASK)

Claim: "`hai` is the audience-preset that forks any reel into a Humanitarians AI cut."
Evidence: `skills/make/hai/SKILL.md` lines 1–13 (frontmatter) and line 16: "Creates a **new `hai-` directory** from any source input and writes the HAI beat sheet as `beat_sheet.hai.json` inside it." Also line 20: "The canonical source (`beat_sheet.json`, build scripts, media) is **never modified**."

## B01 (BLUF)

Claim: "The source stays byte-identical." Evidence: SKILL.md line 20 above + line 246: "Source files (`beat_sheet.json`, build scripts, media) are **never modified**." Verified in the demo — pre/post scaffold SHA-256 of the fixture's `beat_sheet.json` matches (`22e0a614bc69fead4b56e494f705bb8f78771d813a79abfa1464be93e29befbf`), see `demo/` and `SOURCES.md`.

## B02 (ANATOMY)

Claim: "hai places a sibling directory next to whatever you pointed it at — for a reel, `hai-<slug>` beside the reel; for a lecture, into `hai-lectures/`."
Evidence: SKILL.md lines 34–43 (Output directory convention table) plus the demo output — `hai-example-reel/` sat beside `example-reel/` after the scaffold ran.

Claim: "Inside that directory sits `beat_sheet.hai.json`, a metadata block already stamped for the humanitarians channel, and a `_variant_todo` checklist."
Evidence: SKILL.md lines 60–71 (the JSON block: audience/persona/engine/voice_kokoro/palette/typography/register/outro_source/derived_from) and lines 40–43 (list of files inside the hai- dir). Verified: `beat_sheet.hai.json` from the demo contains all listed fields plus a `_variant_todo` list (see `demo/fixture-book/youtube/hai-example-reel/`).

## B03 (PIPELINE)

Claim: "Six steps." Evidence: SKILL.md §46 "Flow (per reel or lecture)" lists Step 1 through Step 6 explicitly.

Claim: "Scaffold first — deterministic, no spend, no writes to the source."
Evidence: SKILL.md lines 48 ("Scaffold (deterministic, no spend)") and 71 ("No API calls, no spend.").

Claim: "Optional: at most one Irreducibly-Human tangent."
Evidence: SKILL.md §94: "Irreducibly-Human tangent (0–1 per video)" and line 100: "**Most reels get none.** Do not force it."

Claim: "Second-to-last, insert one CLI worked exercise."
Evidence: SKILL.md §102: "CLI worked exercise (SECOND-TO-LAST beat)" and line 104: "Insert **one beat** before the outro."

Claim: "Last beat, replace with the Humanitarians AI outro."
Evidence: SKILL.md §144: "Outro (LAST beat)".

## B04 (NON-DESTRUCTIVE FORK)

Claim: "The scaffolder even refuses to overwrite its own output — you get an 'already exists, use --force' error."
Evidence: `runtime/scripts/brand_variant.py` lines 76–77:
```
if out.exists() and not a.force:
    sys.exit(f"[variant] {out} already exists (use --force to reset it from canonical)")
```
Verified in the demo — rerunning without `--force` printed exactly that message (see `demo/scaffold-run.log`).

Claim: "The doctrine reads: source files are never modified."
Evidence: SKILL.md line 246 (verbatim): "Source files (`beat_sheet.json`, build scripts, media) are **never modified**."

## B05 (PLAIN REGISTER)

Claim: "Every rewritten beat leads with method, states when to use it, and, required, states when NOT to and where it fails."
Evidence: SKILL.md lines 80–84:
```
- Lead with **method**: what it is, what it produces.
- State clearly **when to use it** — the decision trigger.
- Required: **when NOT to and where it fails** — the AI main event for
  busy practitioners. This is not hedging; it is the diagnostic the audience
  needs. Do not skip.
```

## B06 (CLI EXERCISE)

Claim: "The schema has five parts. A paste-ready `claude` ask. A concrete OUTPUT description. One CHANGE. The second OUTPUT after the change. And a next step."
Evidence: SKILL.md lines 114–119 (verbatim):
```
- Paste-ready `claude "…"` **ASK** that a practitioner can run today.
- **OUTPUT** — what the run produces (concrete description).
- One **CHANGE** — a single diff that deepens or stress-tests the result.
- **OUTPUT 2** — what the revised run produces.
- **NEXT STEP** = "Run it on your own `[data/question]`." — always concrete.
```

Claim: "Genuinely runnable. Not illustrative. Not synthetic."
Evidence: SKILL.md line 119 verbatim.

Claim: "BUILD vs RESEARCH lane classification."
Evidence: SKILL.md lines 106–111.

## B07 (BATCH MODE)

Claim: "Point `hai` at a book directory and it scaffolds every reel and every lecture inside it — one `find`, one loop, one `brand_variant.py` per source."
Evidence: SKILL.md §162 "Batch mode (book input)" and the two shell blocks at lines 167–174 — a `find` piped through `while read d; do python3 runtime/scripts/brand_variant.py "$d" hai; done` for reels, and the same for lectures.

Claim: "What batch mode does not do is the Plain-register rewrite, the tangent, the exercise, or the outro."
Evidence: SKILL.md line 176: "Then perform Steps 2–6 for each resulting `hai-` directory." Batch mode only scaffolds (Step 1); Steps 2–6 are per-video.

## B08 (FALSIFIABILITY — voice-field disagreement)

This is a real finding produced by reading the three source files together.

- Claim: `SKILL.md` says af_kore.
  Evidence: `skills/make/hai/SKILL.md` line 10: "Persona / voice: Kore with Kokoro af_kore."

- Claim: The runtime scaffolder writes af_bella.
  Evidence: `runtime/scripts/brand_variant.py` line 40: `"engine": "kokoro", "voice_kokoro": "af_bella"` (in the `AUD["hai"]` dict). Verified in the demo — the scaffolded output shows `"voice_kokoro": "af_bella"`.

- Claim: The brand spec at `brands/hai.md` says am_onyx.
  Evidence: `brands/hai.md` lines 32–34:
  ```
  | Engine | Default | Override |
  |---|---|---|
  | Kokoro | `am_onyx` | —      |
  ```

- Claim: "after ElevenLabs was removed in September."
  Evidence: `brands/hai.md` line 36: "**There is no paid voice.** ElevenLabs was permanently removed on 2026-09-03."

- Claim: "This teardown IS a claude-liam reel, so we ship am_onyx with Liam's sign-off."
  Evidence: `OUTRO-LOCK.md` and the `metadata.voice` field of this reel's `beat_sheet.json` (am_onyx). The IN-FOR-BEAR LAW in `skills/make/ai-explainer/SKILL.md` §Liam requires the sign-off wording.

## B09 (VERDICT)

Recapitulates B02–B08. No new claims.

## B10 (YOUR TURN)

The prompt is a `plan-only` dry run of the scaffolder against the viewer's own reel plus a Plain-register beat rewrite. It does not require any paid capability. Every check it names is objectively verifiable: SHA equality, presence of a failure-mode line, runnability of the CLI ask.

## B11 (OUTRO)

Recapitulates title only.

## Corrections applied to the source

None. The voice-field disagreement is a finding, not a correction — the SKILL.md was not modified by this build (per its own doctrine and per the toolkit sandbox). The fix belongs upstream in the DOT repository.
