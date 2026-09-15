# TYPECHECK — The logo-motion Skill (landscape 16:9)

## Static `type_check.py` — not shipped in this toolkit

`scripts/type_check.py` (referenced by `CLAUDE.md` and the ai-explainer SKILL as
GATE T) is not present in this isolated toolkit snapshot. This gap is honest:
it is not a build failure, and no fabricated result is claimed. It's the same
gap noted in every recent Brutalist skill-teardown TYPECHECK.md.

Search performed:
- `ls runtime/scripts/type_check.py` → not found
- `ls runtime/qc/type_check.py` → not found
- `reference/type-spec.md` → not present in the isolated toolkit

## Visual typography review (what actually ran)

Runs both automatically (Gate V — `runtime/qc/final_frame_check.py`) and by
frame inspection (Read-tool inspection of the sampled PNGs the Gate V
contact-sheet groups).

### Gate V (visual QC) — actual result

`runtime/qc/final_frame_check.py` samples 2 fps + 15/50/85 % per beat and
audits against `_safe_for(w, h)` (safe-area inset), the ink/background contrast
threshold (`CONTRAST_MIN = 0.30`), and the canvas-fill floor
(`FILL_MIN = 0.55`).

Sampled: 24 frames from the final 3840×2160 landscape master.

```
Frames sampled: 24  ·  BLOCKER: 0  ·  MAJOR: 0
Clean — no BLOCKER/MAJOR defects. ✓
```

### Frame-level Read-tool inspection

- **B00 (cold open composer):** cream page, terracotta spark, greeting "Hola,
  Liam" in serif, command visible, three result lines land after send. Type
  reads at a distance; no bleed past SAFE inset.
- **B01 (hesitant writer):** three-line serif overview at effective ~184 px
  (= 168 × landscape scale 1.0). "scene" → "prop" swap is visible and lands
  the corrected sentence "A new logo / needs a new prop. / One prop, not a
  file." Left/right edges clear inside SAFE.
- **B02 (SkillTeardownAnatomy):** folder tree renders each file entry with
  monospaced icon + mono label; the `LogoMotion.tsx` row is accent
  terracotta; callout at bottom is legible.
- **B03 (SkillTeardownPipeline):** four numbered phase nodes; `SET PHASE MAP`
  lit terracotta; input+output caps present; footer note wraps within SAFE.
- **B04–B08 (SkillTeardownMechanism ×5):** heading serif 82 px, body sans, a
  monospaced quote block boxed with 6-px terracotta rule on the left. Each
  verdict pill sits above SAFE bottom.
- **B09 (ClaudeVerdictArtifact):** six recap lines each visible; artifact
  card stays inside SAFE at 3840×2160 render.
- **B10 (Your Turn composer):** greeting "Your Turn", command block wraps
  cleanly, three output lines fit without wrap.
- **B11 (title outro):** pixel mascot, title "The logo-motion Skill." with
  terracotta period, hardcoded @NikBearBrown handle (per OUTRO-LOCK).

## Kerning / min-size

- Serif greetings (B00 / B10 / B11): EB Garamond bold at ≥ 72 px — well
  above the 24 px legibility floor.
- Mono code lines / quotes (B04-B08 quote block): 32-40 px — legible.
- Sans body copy (SkillTeardown scenes): ≥ 40 px — legible.

No kerning defects observed on inspected frames. Native pango fallback (the
Gate T §8.4 concern) did not activate — the toolkit's bundled EB Garamond
family loaded successfully in Remotion Chromium.

## Conclusion

**PASS (visual review).** The absence of the legacy static checker is a
documented gap, not a claim of pass. The available runtime checks (Gate V) plus
a manual pass over sampled PNGs are the substitute, and they returned clean.
