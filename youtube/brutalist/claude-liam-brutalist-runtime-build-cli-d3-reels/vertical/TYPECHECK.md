# TYPECHECK — Brutalist Utility: build_cli_d3_reels.py

**Run:** `d217abfbd7474852bcae31380ec355c8` · **Aspect:** 16:9 · **Date:** 2026-09-10

## Absent legacy type checker

`scripts/type_check.py` and `reference/type-spec.md` are referenced by CLAUDE.md
(Hard rules → "GATE T (type-lock) — ALWAYS RUN") but do not exist in this toolkit revision (`toolkit_baseline_sha256 92432609980c8ffc03bc1f00a1300fe1ac78bd7363b5b8ba9f2d389407d72b9d`). Ep 39 and 40 both recorded the same gap. `./art run` also does not exist as an executable path; the compile pipeline is invoked directly via `runtime/scripts/compile.py`.

Result: no automated §8 report to attach here. This file records what **was** verified in place of the missing checker.

## Actual typography review performed (frame-level)

The pipeline's real type-safety net for this reel:

1. `runtime/scripts/compile.py`'s Gate V (edge-bleed / title-safe / underfill Laplacian audit) is enforced and left ENABLED. Any BLOCKER or MAJOR from Gate V blocks the final master.
2. The 2 fps + 15/50/85% + first/last frame contact sheet is read directly via the image-capable Read tool (see `_qc/`). Legibility, overflow, kerning fallbacks, and spark-line correctness are inspected by eye.
3. The Remotion scene components enforce type safety in code:
   - `ClaudeCodeBeat` — adaptive font bounded by BOTH card height (`availH / (lines * lineH)`) AND card width (`availW / (longest * 0.6)`); the code never overflows the card, in either aspect. See patch note in `feedback_claude_code_beat_adaptive_font.md`.
   - `BrutalistHesitantWriter` — portrait scale patched to use the correct 1080x1920 design box in 9:16 (see `feedback_brutalist_hesitant_writer_portrait_scale_patch.md`). Without this, portrait BLUF collapses to ~56% of design and undermines Gate V's ≥55% underfill floor.
   - Composer, verdict artifact, and outro components all reference `runtime/remotion/src/tokens/layout.ts` `SAFE` inset (5% title-safe); measured against the 3840×2160 landscape master and 2160×3840 portrait master, no text sits outside the safe area.

## Frame-level findings (from Gate V + Read of `_qc/qc-sheet.png`)

- 12/12 beats present, correct order, correct dimensions (see `_qc/REPORT.md`).
- Composer B00, B10 — greetings render in serif; folder chip reads `@HumanitariansAI`; output/greeting/runningText legible; no clipping.
- Hesitant writer B01 — trigger words `builds` and `prompt` swap correctly; corrected sentence reads `the tool wraps the D3 sim from one HTML.`; no residual `builds`/`prompt` visible after 60% of the beat.
- Pipeline B02 — five phase cards fit inside SAFE; INPUT/OUTPUT cards visible; footer note wraps cleanly; spark line legible.
- Code beats B03–B08 — adaptive font kicks in on the longer stanzas; no line clipped at right; comment vs code coloring distinguishable.
- Verdict B09 — six lines fit inside SAFE; heading not truncated.
- Outro B11 — title restated exactly; `@NikBearBrown` handle rendered; mascot animation lands.

## Missing legacy checks (recorded honestly)

- §8.1 min-size — not machine-checked; visually verified body text ≥ ~24 CSS px.
- §8.4 Pango kerning fallback — not machine-checked; visual inspection shows serif and mono render as expected in the current EB Garamond / SF Mono / Menlo bundle.
- §8.6 golden strings — no fixture; visual inspection confirms all beat titles + spark lines match the beat sheet.

## Conclusion

**PASS (visual, no automated checker available).** No BLOCKER or MAJOR typography defect observed. Full frame-level review record in `CHECKS-REPORT.md` and `_qc/REPORT.md`.
