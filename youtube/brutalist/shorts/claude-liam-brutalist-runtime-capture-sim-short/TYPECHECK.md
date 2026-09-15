# TYPECHECK — Brutalist Utility: capture_sim.py (Short)

The legacy static type checker (`scripts/type_check.py`) is not present in the toolkit and no `reference/type-spec.md` ships with it, so the classical "type_check" step is inapplicable to this build. In its place the Short uses **visual typography review** on the rendered frames, per the parent reel's convention.

## Visual typography checks performed

For each retained beat, at least one frame at the 15% / 50% / 85% mark was opened and read by the image-capable Read tool. Frames live in `_qc/frames/` and their SHA-256 hashes are enumerated in `VISUAL-REVIEW.json`.

| Beat | Frame read | Typography verdict |
|------|------------|--------------------|
| B00  | `first.png`, `B00-85.png` | Composer serif greeting `Tere, Liam` legible; topic eyebrow `BRUTALIST · UTILITY: CAPTURE_SIM.PY` legible; folder chip `@HumanitariansAI` legible; command + output cascade all within SAFE916. |
| B01  | `B01-85.png` | Hesitant-writer serif at `fontSize 200` / `lineSpacing 2.6` fills the safe area vertically without clipping; final settled text `capture_sim / RECORDS / the browser.` reads cleanly. |
| B02  | `B02-50.png` | `SkillTeardownMechanism916` heading + body + spark all inside safe area; no bleed on left/right (portrait-safe variant, not the pipeline strip that trips SAFE916 in vertical). |
| B07  | `B07-50.png` | `ClaudeCodeBeat916` code lines legible; docstring footer legible; adaptive font (both-axes bound) keeps long lines from overflowing. |
| B08  | `B08-50.png` | Verbatim FATAL log with the Mach-port path fits without wrap-clipping; commentary block legible. |
| B09  | `B09-50.png` | Verdict artifact 6 numbered lines legible; monospace-style enumeration + serif heading render as expected. |
| B11  | `final.png` | Outro title `Brutalist Utility: capture_sim.py.` centered; `@NikBearBrown` handle legible; mascot below the handle. |

## Static analysis of the toolkit change surface

This Short's build made **no source-code changes** to `runtime/scripts/`. All modifications live inside the derivative reel directory (`youtube/brutalist/shorts/claude-liam-brutalist-runtime-capture-sim-short/`). Therefore no Python type/lint diff applies to this build.

## Metadata schema check on the derivative beat sheet

Loaded `beat_sheet.json` and confirmed all required Short-metadata fields resolve to their expected types:

| Field | Type | Value |
|---|---|---|
| `metadata.slug` | str | `claude-liam-brutalist-runtime-capture-sim-short` |
| `metadata.kind` | str | `short` |
| `metadata.aspect_ratio` | str | `9:16` |
| `metadata.playlist` | str | `Brutalist` |
| `metadata.voice` / `voice_kokoro` | str | `am_onyx` |
| `metadata.captions` | bool | `false` |
| `metadata.run_id` | str (hex) | `a4ebd93adf44479e83f30c032daf338a` |
| `metadata.source_sha256` | str (SHA-256 hex) | `b5db05e266bb6645717f324a04548c779522f0d770245c45679a57dbecab7d75` |
| `metadata.parent_master_sha256` | str (SHA-256 hex) | `fedfb0ca5e06ee130b855af4fc688bae02293fe05182660c39946f5079d686ab` |
| `beats[*].beat_id` | str | `B00, B01, B02, B07, B08, B09, B11` |
| `beats[*].render_duration_s` | float | sums to 139.208 s |

All types match; no coercions or missing keys.

## Result

**PASS** — visual typography clean across all sampled frames; derivative beat sheet metadata schema valid; no static-analysis regressions (no code was changed).
