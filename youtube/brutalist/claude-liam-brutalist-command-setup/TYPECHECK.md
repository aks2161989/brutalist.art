# TYPECHECK.md — landscape

## Runtime typography gates that DO exist

- `runtime/qc/final_frame_check.py` — GATE V. Frame-level pass over the compiled mp4 for edge-bleed / clipping (BLOCKER), canvas-fill / underfill (MAJOR), low-contrast (MAJOR). Sampled at 15/50/85% of every beat plus first/final frames. **Result on this landscape master (run_id 81d4ac79, 290.5s): 0 BLOCKER / 0 MAJOR** — the compiler's atomic verify succeeded and the master's `.verified.json` was stamped beside the mp4.
- `runtime/scripts/build_safety.py` (project + approvals validators, positive-duration check, source-report guard) — invoked implicitly by `compile.py` and `shorts.py` on every run; no violations reported.
- `runtime/scripts/compile.py` in-line SKIN LINT — reports beat-by-beat when a `palette=claude` beat uses a non-Claude composition (see CHECKS-REPORT.md); the landscape build reported 0 SKIN LINT rows.

## Legacy checker referenced by older prose that does NOT exist here

- `scripts/type_check.py` referenced in the older AI Explainer SKILL.md ("GATE T (type-lock) — ALWAYS RUN") is NOT present in this toolkit revision. `skills/make/kerning/SKILL.md` and `reference/type-spec.md` referenced from the same paragraph are also absent. This is a documentation drift, not an override — per BUILD-PROMPT: "record such gaps honestly, use the available runtime checks and actual image inspection, and never claim a missing checker passed."

## What was actually inspected instead of the absent legacy checker

Manual visual typography QC via image inspection:

- **B00 composer**: greeting "Konnichiwa, Liam" in Claude serif, roman weight, no clipping, no accidental caret carry-over.
- **B01 hesitant writer**: text corrects on the beat's actual audio duration (17.7 s ≥ the 9 s BLUF floor). Terracotta marks ONLY the tokens about to be deleted (per the component's ACCENT LAW). Final on-screen line "setup / verifies live." reads as the reel's compressed claim.
- **B02–B09 ClaudeCodeBeat**: mono face (SF Mono / Menlo family). Adaptive `fontSize` (`min(baseFont, availH/(lines*lineH), availW/(longestLine*0.6))`) keeps every stanza within the card — verified against the URL-bearing B05 pipeline card and the ElevenLabs-guard B08. No wrap, no truncation.
- **B10 verdict artifact**: heading + six lines in Claude serif; each numbered line fits in one row on landscape; kerning is even (Pango fallback did not trip).
- **B11 Your Turn composer**: paste-ready prompt wraps naturally inside the composer box; the three composer output lines are legible; the ↑ send button pill is the ONE terracotta accent on that beat.
- **B12 outro**: "Brutalist Command: setup." with the terracotta period. Handle `@NikBearBrown` (per OUTRO-LOCK.md). Mascot is the slug-seeded crisp-safe pixel-art SVG; translate/scale-only motion (no rotation) — PIXEL-ART LAW satisfied by construction.

## Type sizing law (FILL-THE-CANVAS)

- Landscape 3840×2160 — content occupies most of `SAFE` on the code cards; the artifact card's numbered lines size proportionally to the card and are legible from ~2 m viewing distance at 720p downscale (per manual inspection at 1600×900 crop).
- No content crosses the 5% title-safe inset (Gate V would have flagged edge-bleed; the report shows 0).

## Fonts loaded

- Serif: EB Garamond (bundled at `runtime/fonts/EB_Garamond/`), effective Tiempos replacement.
- Sans: system UI.
- Mono: SF Mono / Menlo family (for code + composer body).
- Oswald: Google Fonts variable (already installed on this workstation per `./setup` all-green).

## Conclusion

Every runtime typography gate that ships in this toolkit passed clean on the landscape master. The absent legacy `type_check.py` was not silently marked passed; it was recorded as a documentation-drift gap and replaced with per-beat image inspection using the 9-point rubric from `CLAUDE-CODE-VISUAL-QC-CHECK.md`.
