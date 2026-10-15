# TYPECHECK.md — GATE T

Reel: `claude-liam-remotion-skills`  |  Checked: 2026-10-10T17:06  |  Overall: PASS  |  Beats checked: 22  |  FAILs: 0

Spec: `skills/make/kerning/reference/type-spec.md` §8.  Floor: 1.9% frame-height.  Contrast: 4.5:1 WCAG.  Kern threshold: 3.5× expected advance.  Wordy budget: 2 elements.

> **§8.10 REDUNDANCY (advisory — does not block cut):**
> Narration should DISCUSS on-screen text, not recite it.
> Exception: LITERAL beats (viewer types/copies/runs the text) are exempt.

> - §8.10 [BVDT] narration recites the card (0.85) — discuss it, don't read it

| beat | lane | polarity | worst finding | status | fix |
|------|------|----------|---------------|--------|-----|
| B00 | bookend | light | min-size §8.1: hand-drawn pattern (ClaudeComposerAsk) — §8.1 hachure/crossbar fragments ar… | PASS | — |
| B01 | bookend | light | min-size §8.1: min text-run height 62px >= floor 41px (individual-char fallback at 2×) | PASS | — |
| B10 | remotion | dark | no-wordy-card §8.5: no prose payload found | PASS | — |
| B11 | remotion | dark | no-wordy-card §8.5: no prose payload found | PASS | — |
| B20 | remotion | light | no-wordy-card §8.5: no prose payload found | PASS | — |
| B21 | remotion | light | no-wordy-card §8.5: no prose payload found | PASS | — |
| B22 | remotion | light | no-wordy-card §8.5: no prose payload found | PASS | — |
| B23 | remotion | light | no-wordy-card §8.5: no prose payload found | PASS | — |
| B24 | remotion | light | no-wordy-card §8.5: no prose payload found | PASS | — |
| B25 | remotion | light | no-wordy-card §8.5: no prose payload found | PASS | — |
| B26 | remotion | light | no-wordy-card §8.5: no prose payload found | PASS | — |
| B30 | remotion | dark | no-wordy-card §8.5: no prose payload found | PASS | — |
| B31 | remotion | dark | no-wordy-card §8.5: no prose payload found | PASS | — |
| B32 | remotion | light | no-wordy-card §8.5: no prose payload found | PASS | — |
| B39 | remotion | dark | no-wordy-card §8.5: no prose payload found | PASS | — |
| B40 | remotion | light | no-wordy-card §8.5: no prose payload found | PASS | — |
| B41 | remotion | light | no-wordy-card §8.5: no prose payload found | PASS | — |
| B42 | remotion | light | no-wordy-card §8.5: no prose payload found | PASS | — |
| B50 | remotion | dark | no-wordy-card §8.5: no prose payload found | PASS | — |
| BVDT | bookend | light | min-size §8.1: hand-drawn pattern (ClaudeVerdictArtifact) — §8.1 hachure/crossbar fragment… | PASS | — |
| BHTF | bookend | light | min-size §8.1: hand-drawn pattern (ClaudeComposerAsk) — §8.1 hachure/crossbar fragments ar… | PASS | — |
| BOUT | bookend | dark | min-size §8.1: min text-run height 65px >= floor 41px | PASS | — |

---

## Failures requiring action before cut

*None — GATE T PASS.*
---

## Check summary

| Check | Beats checked | FAILs |
|-------|---------------|-------|
| no-wordy-card §8.5 | 17 | 0 |
| min-size §8.1 | 22 | 0 |
| overflow §8.2 | 22 | 0 |
| contrast §8.3 | 22 | 0 |
| contrast-local §8.3b | 22 | 0 |
| bbox-overlap §8.6b | 22 | 0 |
| card-clip §8.13 | 22 | 0 |
| kerning §8.4 | 0 | 0 |
| redundancy §8.10 (advisory) | 7 | 1 (advisory — no exit effect) |

---

*GATE T: any FAIL blocks `./art run` and `./art final`. Fix the flagged beats and re-run `scripts/type_check.py` until green.*
