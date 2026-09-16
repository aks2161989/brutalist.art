# FACTCHECK — The logo-motion Skill

Every claim on screen or spoken is either quoted from the isolated toolkit's
copy of `skills/make/logo-motion/SKILL.md` and `reference/TIMING.md` or is a
direct observation of the shipped code. Numbers below carry file:line
citations.

## Claims audited

| # | Claim | Source | Verdict |
|---|---|---|---|
| 1 | "ONE parametric Remotion composition (`LogoMotion`) drives every mark" | SKILL.md L4 ("ONE parametric Remotion composition (`LogoMotion`) drives every mark") | supported verbatim |
| 2 | "eight logo showcase files … 40–75 KB each" (B01 mentions "eight duplicated showcase files") | SKILL.md L27 ("Before this skill, `runtime/remotion/src/` held **eight** logo showcase files … at 40–75 KB each") | supported verbatim |
| 3 | Three-line integration (per-brand parts file · LOGOS registry · props block) | SKILL.md L33-36 (numbered list "1. …/logos/<name>.ts 2. one line in the `LOGOS` registry 3. a props block in the reel's `beat_sheet.json`") | supported verbatim |
| 4 | trace_logo.py pipeline: crop → 4× upsample → 8-connected labels → potrace per part | SKILL.md L79-83 (crop, 4× LANCZOS, 8-connected components, "traces each one separately with potrace"); trace_logo.py L77-101 (same pipeline in code) | supported verbatim |
| 5 | "Position type by cap-top … 0.115em below" | SKILL.md L100-103; scene: `LogoMotion.tsx` L210 (`const CAP_INSET = 0.115`) | supported verbatim |
| 6 | Phase map defaults `buildStart 0.03 · build 0.157 · ghost 0.44 · materialise 0.83` | TIMING.md L71-74; `LogoMotion.tsx` L67 (schema defaults) | supported verbatim |
| 7 | Camera defaults `scale 6.5 · rotate -19 · x 0.16 · y 0.12` | TIMING.md L72; `LogoMotion.tsx` L94 | supported verbatim |
| 8 | Luma std-dev crossings `5% at p=0.36 · 50% at p=0.64 · 95% at p=0.80` | TIMING.md L38 ("Crossings: **5% at p=0.36, 50% at p=0.64, 95% at p=0.80.**") | supported verbatim |
| 9 | Ghost hold is ~44% of runtime | TIMING.md L44 ("Forty-four percent of the runtime spent nearly invisible …") | supported verbatim |
| 10 | "It's just appearing" — client's words on first cut | TIMING.md L58 ("… the client's words were *'it's just appearing.'*") | supported verbatim |
| 11 | Ease `1 − (1 − t)^4` (`easeOut` hard) | TIMING.md L66 ("Ease it hard (`1-(1-t)^4`)") | supported verbatim |
| 12 | Length is a prop; `durationInSeconds → durationInFrames` via calculateMetadata; every ramp is a fraction | SKILL.md L142-145 ("`calculateMetadata` turns `durationInSeconds` into `durationInFrames`, and every ramp in the scene is a fraction of the total. A 4-second cut and a 9-second cut are the same animation at different speeds") | supported verbatim |
| 13 | Audio-first EXCEPTION — transition wins, voice waits | TIMING.md L85-95 ("The transition wins, and the voice waits for it. This is the one place in the toolkit where audio does not set the shape.") | supported verbatim |
| 14 | Medhavy leading silence 0.88 s | TIMING.md L94-96 ("Medhavy's carried 0.88 s. Delaying it by 7.00 s would have put the first word at 7.88 s…") | supported verbatim |
| 15 | Three symptoms of a cheap sting, in diagnostic order | TIMING.md L111-119 (numbered 1-3: full-strength arrival, chrome/gloss/bevel sweep, colour during motion) | supported verbatim |
| 16 | Medhavy first cut had all three (0.27 s pop, 2.80-4.00 s silver sweep on a black mark) | TIMING.md L121-124 ("popped the full lockup in 0.27 s … swept a silver gradient across a black mark from 2.80–4.00 s") | supported verbatim |
| 17 | The build IS a camera move (staggering parts at ghost opacity is invisible) | SKILL.md L133-136; TIMING.md L54-63 | supported verbatim |

## Register test (Teardown vs. read-off)

The narration WAS rewritten. It explains WHY each design decision exists (an
audio-first exception is only defensible because "a sting reproduces a known
motion"; the ghost hold is only defensible because "the materialisation only
reads as an arrival because there was nothing to arrive from"). If the script
could be read directly off SKILL.md, DOUBLE-CHECK LAW would have been skipped.
Verified: the source's structure is inverted from doctrine-first-then-example
to concept-first-then-citation, which is the Teardown move.

## What was NOT claimed

- The reel does not claim to demo a fresh brand traced from a new mark (that
  would require a second raster asset outside scope). The claim is textual:
  "add trace-parts, one LOGOS line, one props block." The shipped Medhavy
  trace is cited as evidence that this integration point exists (LOGOS
  registry in `LogoMotion.tsx` line 101).
- The narration does not overclaim `art scenes` search or `type_check.py`
  results — both are recorded in TYPECHECK.md as gaps.
- No fabricated demo output, no unreachable service, no paid call.
