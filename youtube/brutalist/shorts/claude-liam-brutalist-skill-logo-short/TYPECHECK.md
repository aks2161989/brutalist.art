# TYPECHECK — The logo Skill — Short (9:16)

Visual typography review of the compiled portrait mp4 at
`exports/short/claude-liam-brutalist-skill-logo-short.mp4`
(2160×3840, 155.375 s). The legacy Python type-checker is not part of this
toolkit's runtime checks; type verification here is the direct read of
rendered PIL/Remotion output — the frames actually shown to viewers.

## Method

- Extracted 2 fps sample frames (311 total, `_qc/frames/f001.png` …
  `f311.png`).
- Extracted beat-relative 15% / 50% / 85% frames per retained beat
  (21 PNGs).
- Read each p50 frame directly, plus edge frames (B00-p15/p85, B01-p85,
  B11-p85). Built a 3×7 contact sheet.

## Per-beat typography findings

### B00 · ClaudeComposerAsk916 (0.00 – 15.25 s)

- Eyebrow `BRUTALIST · SKILL TEARDOWN` — geometric mono uppercase, tracked
  wide, fits inside the top portrait safe band.
- Title `The logo Skill` — serif display, single line, no wrap issue.
- Greeting `Hola, Liam` — serif at the composer-aware portrait scale.
- Composer body (3-line ask about `logo` skill mental model) — sans, ~52 px
  ex-height in the frame, ~11 words per line, comfortable inside safe area
  with margin room on both sides.
- Result lines under the folder chip — mono, terracotta asterisk +
  "reading skills/make/logo/SKILL.md…" and three summary lines. No
  overflow, no clipped glyphs.
- Folder chip `📁 @HumanitariansAI` — mono, sits under the composer with
  visible terracotta rule. Chip label is @HumanitariansAI (channel-level),
  hardcoded outro handle in B11 is @NikBearBrown per OUTRO-LOCK — the two
  are correctly distinct.

### B01 · BrutalistHesitantWriter916 (15.25 – 33.42 s)

- Serif body at portrait-aware scale — 5 short lines "The logo skill /
  plays a random / brand sting. / The MP3 / is the clock." — coverage
  visibly at or above the FILL_MIN 0.55 bar (see
  `feedback_hesitant_writer_portrait_bluf_recipe`).
- Trigger-word swap `fixed → random` visible mid-beat at p15 — trigger
  configured as the required single-token `"fixed"`.
- No caret orphaning, no punctuation stranded on a new line — the split
  respects breath units.

### B04 · SkillTeardownMechanism916 · ACT 1 (33.42 – 62.21 s)

- Eyebrow `MECHANISM · ACT 1` — mono, tracked, top-of-content.
- Heading `The MP3 is the clock.` — serif display, single line.
- Body paragraph (5-line block on `apad`, `calculateMetadata`,
  `-shortest`) — sans body scale for portrait, no clipping.
- Verbatim quote block with left terracotta rule and source citation
  `Source: logo SKILL.md · The laws · #1` — legible.
- Verdict pill `TRIM SILENCE, NEVER SOUND` — outline pill,
  centered, ~64 px height.
- Spark `Silence lives IN the clock.` — bottom, italic-serif, sits above
  the bottom portrait safe margin.

### B05 · SkillTeardownMechanism916 · ACT 2 (62.21 – 89.54 s)

- Same template as B04. Body naming SystemRandom, `shot.remotion.picked`,
  `--reroll`; verbatim quote block; verdict pill `--REROLL TO RE-SPIN`
  (leading en dashes render as terracotta `-`-`-` pair, expected pill
  styling); spark `Random across reels. Locked within one.`

### B08 · SkillTeardownMechanism916 · FALSIFIABILITY ACT 5 (89.54 – 123.04 s)

- Same template as B04. Body naming the four brand pools; verbatim quote
  from SKILL.md `Brands and aliases`; verdict pill
  `NBB → CLAUDETITLEOUTRO · EVERYONE ELSE → LOGOOUTRO` — the pill runs
  wider than the ACT 1/ACT 2 pills but still centered within the safe
  band, no truncation. Spark `One skill does not fit all channels.`

### B09 · ClaudeVerdictArtifact916 (123.04 – 152.04 s)

- Artifact card scales to fill the portrait canvas.
- Card head `The logo Skill`, sub-heading `A locked lottery. Silence at
  the end.` in serif display.
- Six numbered lines with terracotta digits `1.` … `6.`; each line wraps
  within the card at portrait scale, no over-flow, no clipped descenders.
- Numbered digits align vertically with the left margin of the line body
  above.

### B11 · ClaudeTitleOutro916 (152.04 – 155.37 s)

- Dark ink ground with cream serif title `The logo Skill.` (terracotta
  period sits inside the title line as designed).
- Handle `@NikBearBrown` in cream serif directly beneath the title,
  hardcoded per OUTRO-LOCK (applies to claude-liam reels only).
- Pixel mascot seeded by slug `claude-liam-brutalist-skill-logo` — the
  parent long's slug is retained for signature continuity across long/
  vertical/Short.
- Top and bottom cream hairlines mark the portrait safe band.

## Aggregate

- No burned-in captions on any beat (per Short spec).
- No dropped or truncated text glyphs.
- No portrait bleed of `channel_title` (metadata deliberately omits it per
  `feedback_channel_title_portrait_bleed`; verified by absence).
- BLUF portrait FILL coverage looks ≥ 55 % of the safe band at 15 / 50 /
  85 % of B01 (per `feedback_gate_v_underfill` and
  `feedback_hesitant_writer_portrait_bluf_recipe`).
- No JS type or Zod prop-shape error surfaced from Remotion — every
  retained beat is the parent's already-rendered mp4, so Zod validation
  happened at the parent's build time and is not re-run for this Short.

Result: **PASS**. Zero blockers, zero majors. Human review by Bear pending.
