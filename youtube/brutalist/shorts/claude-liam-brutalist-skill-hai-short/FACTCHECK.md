# FACTCHECK.md — The hai Skill (Short)

Every factual claim the RETAINED narration makes, with the source line that
carries it. This Short is a whole-beat cut of the parent
`claude-liam-brutalist-skill-hai` vertical; the parent's evidence for each
kept beat is inherited unchanged. Dropped beats (B02, B06, B07, B10) and their
claims are NOT part of the Short — see CUT-PLAN.json.

## B00 (ASK · cold open)

Claim: "`hai` is the audience-preset that forks any reel into a Humanitarians
AI cut."
Evidence: `skills/make/hai/SKILL.md` lines 1–13 (frontmatter) and line 16:
"Creates a **new `hai-` directory** from any source input and writes the HAI
beat sheet as `beat_sheet.hai.json` inside it." Also line 20: "The canonical
source (`beat_sheet.json`, build scripts, media) is **never modified**."

## B01 (BLUF · reformats → forks)

Claim: "The source stays byte-identical."
Evidence: SKILL.md line 20 (above) + line 246: "Source files
(`beat_sheet.json`, build scripts, media) are **never modified**." Verified
in the parent build's demo — pre/post scaffold SHA-256 of the fixture's
`beat_sheet.json` matches (`22e0a614bc69fead4b56e494f705bb8f78771d813a79abfa1464be93e29befbf`),
see the parent reel's `demo/` and `SOURCES.md`.

## B03 (FRAMEWORK · six-step pipeline)

Claim: "Six steps."
Evidence: SKILL.md §46 "Flow (per reel or lecture)" lists Step 1 through
Step 6 explicitly.

Claim: "Scaffold first — deterministic, no spend, no writes to the source."
Evidence: SKILL.md lines 48 ("Scaffold (deterministic, no spend)") and 71
("No API calls, no spend.").

Claim: "Optional: at most one Irreducibly-Human tangent."
Evidence: SKILL.md §94: "Irreducibly-Human tangent (0–1 per video)" and
line 100: "**Most reels get none.** Do not force it."

Claim: "Second-to-last, insert one CLI worked exercise."
Evidence: SKILL.md §102: "CLI worked exercise (SECOND-TO-LAST beat)" and
line 104: "Insert **one beat** before the outro."

Claim: "Last beat, replace with the Humanitarians AI outro."
Evidence: SKILL.md §144: "Outro (LAST beat)".

## B04 (MECHANISM · Non-destructive fork)

Claim: "The scaffolder even refuses to overwrite its own output — you get an
'already exists, use --force' error."
Evidence: `runtime/scripts/brand_variant.py` lines 76–77:
```
if out.exists() and not a.force:
    sys.exit(f"[variant] {out} already exists (use --force to reset it from canonical)")
```
Verified in the parent build's demo — rerunning without `--force` printed
exactly that message (see the parent reel's `demo/scaffold-run.log`).

Claim: "The doctrine reads: source files are never modified."
Evidence: SKILL.md line 246 (verbatim): "Source files (`beat_sheet.json`,
build scripts, media) are **never modified**."

## B05 (MECHANISM · Plain register)

Claim: "Every rewritten beat leads with method, states when to use it, and,
required, states when NOT to and where it fails."
Evidence: SKILL.md lines 80–84:
```
- Lead with **method**: what it is, what it produces.
- State clearly **when to use it** — the decision trigger.
- Required: **when NOT to and where it fails** — the AI main event for
  busy practitioners. This is not hedging; it is the diagnostic the audience
  needs. Do not skip.
```

## B08 (FALSIFIABILITY · voice-field disagreement)

This is a real finding produced by reading the three source files together.

- Claim: `SKILL.md` says af_kore.
  Evidence: `skills/make/hai/SKILL.md` line 10: "Persona / voice: Kore with
  Kokoro af_kore."

- Claim: The runtime scaffolder writes af_bella.
  Evidence: `runtime/scripts/brand_variant.py` line 40:
  `"engine": "kokoro", "voice_kokoro": "af_bella"` (in the `AUD["hai"]` dict).
  Verified in the parent build's demo — the scaffolded output shows
  `"voice_kokoro": "af_bella"`.

- Claim: The brand spec at `brands/hai.md` says am_onyx.
  Evidence: `brands/hai.md` lines 32–34:
  ```
  | Engine | Default | Override |
  |---|---|---|
  | Kokoro | `am_onyx` | —      |
  ```

- Claim: "after ElevenLabs was removed in September."
  Evidence: `brands/hai.md` line 36: "**There is no paid voice.** ElevenLabs
  was permanently removed on 2026-09-03."

- Claim: "This teardown IS a claude-liam reel, so we ship am_onyx with Liam's
  sign-off."
  Evidence: `OUTRO-LOCK.md` and the `metadata.voice` field of this reel's
  `beat_sheet.json` (am_onyx). The IN-FOR-BEAR LAW in
  `skills/make/ai-explainer/SKILL.md` §Liam requires the sign-off wording.

## B09 (VERDICT)

Recapitulates B01, B03, B04, B05, B08 plus two one-line facts that are not
deep-dived in this Short:

- "The CLI exercise must actually run." Evidence: SKILL.md line 119: "Genuinely
  runnable. Not illustrative. Not synthetic." (Full five-part schema and quote
  are deferred to the 16:9 long — B06 in the parent reel.)

- "Batch mode scaffolds every reel and lecture in a book, but the register
  rewrite is still per-video." Evidence: SKILL.md §162 "Batch mode (book
  input)" plus line 176: "Then perform Steps 2–6 for each resulting `hai-`
  directory." (Full shell invocation is deferred to the 16:9 long — B07 in
  the parent reel.)

No new claims.

## B11 (OUTRO)

Recapitulates title only. Liam sign-off is required by the IN-FOR-BEAR LAW
(see `skills/make/ai-explainer/SKILL.md`).

## Corrections applied to the source

None. The voice-field disagreement remains a finding, not a correction — the
upstream `SKILL.md` was not modified by this build (per its own doctrine and
per the toolkit sandbox). The fix belongs upstream.
