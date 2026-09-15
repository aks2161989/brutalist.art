# TYPECHECK — Brutalist Command: art icon-build (landscape)

## Legacy `scripts/type_check.py` — NOT PRESENT in this toolkit snapshot

The `ai-explainer/SKILL.md` § "Hard rules" references `scripts/type_check.py`
and `skills/make/kerning/SKILL.md` as GATE T. Neither is shipped in this
toolkit revision (baseline SHA `92432609980c8ffc03bc1f00a1300fe1ac78bd7363b5b8ba9f2d389407d72b9d`).
This report does **not** claim the missing checker passed.

## What WAS run instead — visual typography review

The runtime `GATE V` (`runtime/qc/final_frame_check.py`) enforces the
subset of the type-lock spec that is implementable from frame inspection:
edge-bleed / clipping, title-safe margins, container overflow, and CANVAS
FILL (per FILL-THE-CANVAS LAW). Result:

```
[gate-v] frames=24 BLOCKER=0 MAJOR=0
```

Every sampled PNG (24 frames — 12 beats × 50 % / 85 %) was opened with the
image-capable Read tool and audited against the 9-point rubric in
`CLAUDE-CODE-VISUAL-QC-CHECK.md`:

| # | Rubric item | Landscape result |
|---|---|---|
| 1 | Edge bleed / clipping (title-safe inset) | ✓ zero |
| 2 | Container overflow (text past its box) | ✓ zero |
| 3 | Collision (elements overlapping) | ✓ zero |
| 4 | Offscreen anchors | ✓ zero |
| 5 | Legibility (min effective 24 px, contrast) | ✓ all beats above floor |
| 6 | Brand-bug placement inside title-safe | ✓ folder chip within safe |
| 7 | Aspect (16:9 native, no letterbox) | ✓ 3840×2160 |
| 8 | Canvas fill (no dead space under undersized content) | ✓ verdict + code cards fill safe area |
| 9 | Palette discipline (one terracotta per beat) | ✓ spark line / send button / one accent |

## §8-family checks the missing checker would have covered

The full type-lock spec (`reference/type-spec.md` — also absent) enumerates
sub-checks like §8.4 kerning sanity (Pango fallback catch) and §8.6 golden
strings per rendered frame. These are not directly reproducible without the
checker's implementation. The visual review above is the honest substitute
for the parts we CAN inspect from frames; the parts we cannot (subpixel
kerning drift below what a 3840×2160 sample would reveal) are unverified
and logged here rather than falsely claimed as passed.

## Fonts actually used

- **Serif greetings + titles**: EB Garamond (bundled in `runtime/fonts/`),
  as required by CLAUDE-BRAND (Tiempos is proprietary, EB Garamond is the
  effective default).
- **UI sans (chrome, folder chip, output lines)**: system sans-serif
  (Inter-family on the isolated toolkit) — inherits from
  `runtime/remotion/src/tokens/claude.ts`.
- **Mono (code cards, terminal output)**: `SF Mono` (system font stack
  falls through to it on macOS render host).

## Conclusion

- Legacy `scripts/type_check.py` was not run because it does not exist in
  this toolkit snapshot. This is a limitation of the runtime, not of the
  reel; the film's typography was reviewed by opening every sampled frame.
- All items in the 9-point rubric that are inspectable from frames pass on
  every landscape beat.
- Kerning-level subpixel checks that would need a live Pango fallback probe
  are unverified and honestly logged as such.
