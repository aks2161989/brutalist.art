# TYPECHECK.md — The hai Skill (landscape 3840×2160)

The legacy `scripts/type_check.py` GATE T checker referenced in some toolkit
doctrine is **not present** in the isolated toolkit snapshot used for this
build (verified: `find toolkit/scripts -name type_check.py` returns nothing;
`toolkit/reference/type-spec.md` also absent). Rather than claim a check that
did not run, this file records the **actual visual typography review** that
was performed against the rendered master.

## Method

For every rendered beat, high-resolution frames from the final MP4 were
extracted with ffmpeg (`fps=2`, plus targeted samples at ~15/50/85% of each
beat's span from the beat sheet) and read as PNGs. The rubric applied:

- §8.1 — minimum on-screen type ≥ 24px effective (measured against 1920×1080 layout tokens, scale 2 at 3840×2160).
- §8.2 — no container overflow; every text element sits inside SAFE (x 96–1824, y 54–1026 at the 1920 reference).
- §8.3 — text vs background luminance separation adequate (subjective read, plus the auto-verified LOW-CONTRAST check inside Gate V).
- §8.4 — no obvious kerning artifacts (Pango fallback catch).
- §8.5 — no wordy card (body beats stay ≤ ~40 words on screen; verdict artifact card at 6 lines is the exception per doctrine).
- §8.6 — golden strings (title restate, handle, persona) render as authored.

## Findings per beat

| Beat | Component | Type check | Notes |
|---|---|---|---|
| B00 | ClaudeComposerAsk | ✓ | Greeting "Hallo, Liam" serif line, command mono ~28px effective, three output serif lines well inside safe. |
| B01 | BrutalistHesitantWriter | ✓ | fontSize=148 (design ref 1920×1080, scales 2× at 4K). After three failed iterations (see CHECKS-REPORT), text now fills ≥55% of safe area without top/bottom edge bleed. Corrected `reformats`→`forks` legible; caret blink stable. |
| B02 | SkillTeardownAnatomy | ✓ | Folder tree monospace ~32px reference (64px at 4K), fits inside 88%-width content column. Callout box below fits. |
| B03 | SkillTeardownPipeline | ✓ | INPUT/phases/OUTPUT node stack legible; footer note wraps inside content column; spark line bottom-left. |
| B04 | SkillTeardownMechanism | ✓ | Heading ~110px effective, body 42px, quote 34px monospace inside terracotta-bordered card. |
| B05 | SkillTeardownMechanism | ✓ | Same schema; longer body still fits card. |
| B06 | SkillTeardownMechanism | ✓ | Body describes five-part schema; still one screen. |
| B07 | SkillTeardownMechanism | ✓ | Body shorter than B06; verdict pill high-contrast. |
| B08 | SkillTeardownMechanism | ✓ | Longest body of the run (three-file-three-voice enumeration). Text wraps inside safe; quote box holds the verbatim line from brands/hai.md. |
| B09 | ClaudeVerdictArtifact | ✓ | Artifact card 6 lines, each on its own row, no overflow. |
| B10 | ClaudeComposerAsk | ✓ | Long command runs into a scrolling composer box (native to the component); three output rubric lines fit. |
| B11 | ClaudeTitleOutro | ✓ | Title "The hai Skill." serif with terracotta period, handle `@NikBearBrown` beneath, slug-seeded mascot in corner. |

## Golden strings (verified verbatim)

- Outro title text: `The hai Skill.` (period is terracotta, per OUTRO-LOCK).
- Outro handle: `@NikBearBrown` (hardcoded by OUTRO-LOCK on claude-liam reels; not a preference — a lock).
- Persona line spoken in B00 and B11: "Liam, in for Bear." (IN-FOR-BEAR LAW).
- Folder chip on every composer beat: `@HumanitariansAI` (the playlist's channel, distinct from OUTRO-LOCK's @NikBearBrown handle on the ClaudeTitleOutro outro; both are correct — the falsifiability beat is exactly about this).

## Kerning / Pango fallback catch

Verified by eye across the sampled frames: EB Garamond serif renders with matched glyph spacing (no fallback substitution to system serif), UI sans (Inter/system) matches Claude tokens, mono renders as SF Mono / bundled monospace. No visible fallback swap.

## Contrast

- Ink `#3D3929` on cream `#FAF9F5` — well above 4.5:1 (measured ~10:1).
- Terracotta `#D97757` used only as accent (send button, verdict pill fill, spark, quote card left border) — never for body text.
- SkillTeardownMechanism quote card uses monospace on cream inside a terracotta-bordered card; every quote reads clearly at 34px.

## Conclusion

No typography defect blocks or majors. The absence of the legacy `type_check.py` is recorded honestly; the image-level review substituted here covers the same rubric points, and Gate V's LOW-CONTRAST auto-check also runs.
