# FACTCHECK — The logo Skill — Short (9:16)

This Short is a whole-beat cut of the parent vertical (12 → 7 beats). No
narration was rewritten. The factual claims below are only for the beats that
survive the cut; the parent's FACTCHECK.md covers the dropped beats (B02, B03,
B06, B07, B10) and is preserved unchanged in the parent reel.

Sources fully read (isolated toolkit copies):

- `skills/make/logo/SKILL.md` — SHA-256 `badfb2bc1b6598049174fd79c57b41ee30d177d9c89b20d38b93574ad5547a6d`
- `skills/make/logo/scripts/logo.py` — SHA-256 `1a8376bd1d1702d3dc13bf5e619eae5b5ffc3969309710184b15c85c16c73b5e`
- `runtime/remotion/src/scenes/LogoOutro.tsx` — SHA-256 `7e2675615c99ce46f0a2bf22fb50b643131f2cfb9c3bb9a30ff2f2666306809c`
- `OUTRO-LOCK.md` — SHA-256 `a642621c1073604ff350381f58e2fbfa7dee1c0f586d8a285c44ed2c4ab51e01`

## Claims made in the retained cut — verification

### B00 Cold open (ClaudeComposerAsk916)

- "One command appends one beat." — verified in SKILL.md §Purpose (lines
  15–19) and logo.py main flow (steps 1–6, docstring lines 16–30).
- "Random-once pick of animation + SVG + MP3, locked." — verified in SKILL.md
  §The laws #2 (line 90); logo.py records `shot.remotion.picked` at line 233.
- "The MP3 is the clock — the jingle is never cut." — verified in SKILL.md
  §The laws #1 (lines 82–89) and logo.py `probe_dur` + `apad` + `durationS`
  at lines 252–260.

### B01 BLUF (BrutalistHesitantWriter916)

- "The word 'logo' invites the fixed read; the skill picks randomly." —
  the same random-once-then-locked contract; SKILL.md §The laws #2. The
  hesitant-writer's `triggerWords: "fixed"` / `replacementWords: "random"`
  matches the single-token contract in `feedback_hesitant_writer_triggers`.

### B04 Mechanism ACT 1 — The MP3 is the clock

- ffmpeg `apad` + `libmp3lame` command verified at logo.py lines 254–256.
- "durationS = padded length" verified: `dur = probe_dur(mp3_dst)` then
  `props["durationS"] = dur` (lines 260, 276).
- "same law as outro" — cross-referenced in SKILL.md line 88.
- "Want a different length? Use a different mp3." — SKILL.md lines 88–89.
- Verbatim quote on the card ("The MP3 is the clock — and the jingle is
  NEVER cut.") is SKILL.md §The laws #1.

### B05 Mechanism ACT 2 — Random once, then locked

- `SystemRandom` at logo.py line 228.
- `shot.remotion.picked` recorded at line 233 as
  `{brand, animation, svg, mp3, locked: True}`.
- Reuse-on-re-run branch at logo.py lines 218–226 (`if beat and not a.reroll`).
- `--reroll` argparse flag at logo.py lines 186–187.
- Byte-for-byte rebuild stability: identical (SVG bytes, padded MP3 bytes,
  props) → Remotion is deterministic → identical output frames.
- Verbatim quote on the card is SKILL.md §The laws #2.

### B08 Falsifiability — no logos/nik-bear-brown/ pool

- SKILL.md §Curate the pool… lines 76–78: "There is no
  `logos/nik-bear-brown/`, by design. @NikBearBrown does not use a logo
  sting — it uses `ClaudeTitleOutro`, whose CLAWD mascot is drawn from
  pixel rects in `ClaudeMascotScene.tsx` and reads no files at all."
- OUTRO-LOCK.md lines 3–4: "Locked spec for the claude-liam /
  @NikBearBrown outro card. Applies to claude-liam reels ONLY."
- Cross-referenced: this Short IS a claude-liam reel; its last beat (B11) is
  `ClaudeTitleOutro916`. The beat's own architecture is the evidence for the
  falsifiability claim it makes.
- The four brand pools named on the card (bear-brown, humanitarians, medhavy,
  musinique) match `logos/` on disk in the isolated toolkit.

### B09 Verdict artifact

The six verdict lines are direct restatements:
1. "Appends ONE brand sting beat per reel — random once, LOCKED at
   shot.remotion.picked." — B04+B05 combined.
2. "The MP3 is the clock — padded with a silence tail (`--tail 1.0s`) so the
   jingle is NEVER cut." — B04.
3. "Draw is uniform over `logos/<brand>/*.svg` — the POOL is the quality
   bar (curate before you trust it)." — parent's dropped B06; still true and
   loaded from SKILL.md line 62 (`glob.glob("logos/<brand>/*.svg")`).
4. "drawOn is EARNED — only enters the lottery when the SVG is path-only
   (no text/image/gradient/mask)." — parent's dropped B07; verified in
   logo.py `extract_paths` lines 93–155 and lottery gate at line 232.
5. "Aspect follows `metadata.aspect_ratio` — 9:16 → 1080×1920, otherwise
   → 1920×1080. No re-code." — LogoOutro.tsx `calculateMetadata` derives
   canvas from `props.aspectRatio`.
6. "@NikBearBrown opts out by design — that channel uses ClaudeTitleOutro's
   slug-seeded pixel mascot." — B08 and OUTRO-LOCK.md.

Because verdict lines 3 and 4 reference laws whose walk-throughs (B06, B07)
are dropped, the retained cut surfaces the rules but does not demonstrate
them. That trade-off is the point of the Short vs. the long; the full
demonstrations remain in the parent vertical / 16:9 films.

### B11 Outro (ClaudeTitleOutro916)

- Title "The logo Skill." and `@NikBearBrown` handle are hardcoded per
  OUTRO-LOCK.md (applies to claude-liam reels only).
- Slug-seeded mascot animation reads no files; `slug` prop is
  `claude-liam-brutalist-skill-logo` — the parent long's slug is retained
  so the mascot animation matches across the parent long, its vertical
  companion, and this Short. That is deliberate — a Short is a derivative of
  the parent, so the outro mascot signature is the same signature.

## Corrections and simplifications retained from the parent

- "SystemRandom" is the exact class used (`random.SystemRandom()`) —
  logo.py line 228. Not simplified.
- "One second by default" for `--tail` — argparse default `1.0` at logo.py
  line 191.
- The narration does not name every one of the eight animation techniques
  (they appear on the on-screen quote in the parent's B07 which is dropped
  here). The retained cut mentions eight techniques only inside the verdict
  artifact line 4 as a category ("path-only SVG"), not by roster.

## Cut-only claims — none

The Short introduces no new claims that are absent from the parent's beat
sheet. Nothing was rewritten. Every retained on-screen and spoken word is
byte-identical to the parent vertical.
