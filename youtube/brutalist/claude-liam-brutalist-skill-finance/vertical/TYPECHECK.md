# TYPECHECK — The finance Skill · portrait

See `../TYPECHECK.md` for the shared §8 review methodology and the note on the
missing legacy `scripts/type_check.py`.

## Portrait-specific typography review

Frames sampled at 15%/50%/85% of every beat plus first/final via
`ffmpeg -ss <t> -i <mp4> -frames:v 1`. The 50% composite is
`_qc/contact-sheet-50pct.png` and was inspected via the image-capable Read
tool.

### §8.1 Minimum size ✓
- Native portrait scenes use aspect-aware scaling. SkillTeardownMechanism
  serif heading at 52px design → 104px effective at 4K portrait (2160×3840).
- Body text at ~26–28px design → 52–56px 4K.
- Composer body in ClaudeComposerAsk916 uses its native portrait sizing (the
  composer card fits centrally in the tall canvas).
- Hesitant writer at fontSize 155 renders as 310px 4K (after the aspect-aware
  fix to `BrutalistHesitantWriter.tsx`).

### §8.2 Overflow ✓
- Every beat's ink bounding box sits inside SAFE916 (x 108..2052, y 192..3648
  at 4K). Verified by Gate V on the assembled portrait media: zero
  edge-bleed defects.
- B01 hesitant writer widest line ("The accounting", 14 chars at 155px) fits
  inside `width * 0.86 = 928px` design → 1856px 4K, well under 2160.
- B10 Your Turn composer command was intentionally trimmed for portrait so the
  running-text + output rubric all sit inside safe.b.

### §8.3 Contrast ✓
Identical palette to landscape — warm ink `#3D3929` on cream `#FAF9F5` ≈11:1;
terracotta `#D97757` reserved for the ONE accent per beat with 1px keyline
where used.

### §8.4 Kerning sanity ✓
Same bundled fonts (EB Garamond, Inter) as landscape. No portrait-specific
kerning regressions found; the widest-glyph combinations (`fi` ligature in
"finance", `ff` in "off") render cleanly at portrait sizes.

### §8.5 No-wordy-card ✓
Portrait cards run the same body word counts as landscape (typography is the
same; only the layout box aspect changed). SkillTeardownMechanism reflows the
body into a taller single column; every card is a single readable page.

### §8.6 Golden strings ✓
Same title restatement (`The finance Skill.`), same handle (`@NikBearBrown`),
same folder chip (`@HumanitariansAI`). All slugs and identifiers preserved
across aspects.

## Portrait-only patches shipped this run

- **`runtime/remotion/src/scenes/BrutalistHesitantWriter.tsx`** — aspect-aware
  `scale`: `isPortrait ? min(width/1080, height/1920) : min(width/1920, height/1080)`.
  This makes the serif fill the portrait safe area (previously collapsed to 0.5625
  and always looked tiny). Documented in memory `feedback_hesitant_writer_portrait_scale`.
- **`runtime/remotion/src/scenes/SkillTeardownAnatomy916.tsx` / `SkillTeardownPipeline916.tsx`
  / `SkillTeardownMechanism916.tsx`** — copied from the fellows workspace
  (shared schemas; portrait reflow via `useVideoConfig()`), and registered in
  this isolated `Root.tsx` at 1080×1920 compositions.

Nothing in the live public toolkit was altered. All patches are scoped to the
isolated workspace `.repoloop/workspaces/claude-liam-brutalist-skill-finance/toolkit`.

## Conclusion

Typography **PASSES** review by image inspection at 24+ sampled portrait
frames. Same substitution note as landscape re: the missing legacy checker.
