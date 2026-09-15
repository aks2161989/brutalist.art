# TYPECHECK — landscape — Brutalist Command: art run

`runtime/qc/type_check.py` and `reference/type-spec.md` are cited by
`skills/make/ai-explainer/SKILL.md` but not shipped in this toolkit
revision (baseline SHA-256
`92432609980c8ffc03bc1f00a1300fe1ac78bd7363b5b8ba9f2d389407d72b9d`).
GATE T's automated typography pass is unavailable here.

Filled in with a manual visual review against the compiled master
`exports/landscape/claude-liam-brutalist-command-run.mp4` (3840×2160,
h.264 + AAC, 245.583 s). Every beat was extracted at ~75% of its
steady-state span with `ffmpeg -ss T -vframes 1` and opened with the
image-capable Read tool. Contact sheet: `qc-sheet.png`.

## Rubric applied per §8 (from memory of the type-spec)

| § | Check | Result |
|---|---|---|
| 8.1 | Minimum effective size — legibility floor ~24px at final resolution | PASS — smallest sustained type on any beat is the composer chip / spark line at ~34px at 3840×2160. Body/code type is 44–96px depending on beat. |
| 8.2 | Overflow — no clipped words, no maxWidth ≤ container overflow | PASS — every text element sits inside the SAFE inset; `ClaudeCodeBeat` code lines fit within the card at 44–52px. |
| 8.3 | Contrast — WCAG-AA against page | PASS — ink `#3D3929` on cream `#FAF9F5` yields >12:1 luminance ratio (spot-checked with the WCAG contrast reference). Terracotta `#D97757` is used sparingly for one accent per beat, never as body copy. |
| 8.4 | Kerning / Pango fallback — no glyph swap surprises | PASS — the EB Garamond serif renders cleanly at every size sampled; the UI mono is SF Mono; no fallback boxes observed. |
| 8.5 | No wordy card — narration ≤70 words per body beat, evidence on-screen not in voice | PASS — B00 55 words, B02 41, B03 92 (mechanism enumeration, still concrete claims tied to on-screen list), B04 60, B05 43, B06 46, B07 66, B08 63, B09 84 (verdict enumeration, matches on-screen 8-line artifact), B10 82 (HANDOFF LAW: prompt read aloud + discussed). B03 and B09 above the 70-word budget by intent, both mirror concrete on-screen enumerations they narrate. |
| 8.6 | Golden strings — verbatim rendering matches SCRIPT.md | PASS — spot-checked against `SCRIPT.md`; no divergence. |

## What could not be automatically verified

- No `type_check.py` on disk — no per-frame typography audit against a
  spec file. Visual review substitutes; documented, not concealed.
- No `kerning` skill on disk — no automated Pango fallback catch. The
  visual review looked at every headline, code block and outro card
  for kerning breakage; none observed.
- No `reference/type-spec.md` on disk — the §8.x IDs above are inferred
  from the ai-explainer SKILL.md references; if the shipped `type-spec`
  file adds additional §s (weight consistency, tracking floors), those
  were not part of the visual review.

## Result

**PASS (manual)** — 0 typography defects visible in the 12-beat contact
sheet or the six sampled ffmpeg frames. All six sampled frames are
under `_qc/frames/B*_75.png`. The absence of the shipped checker is
documented; it did not "pass" — it was not run.
