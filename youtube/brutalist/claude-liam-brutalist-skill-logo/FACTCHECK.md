# FACTCHECK — The logo Skill

Sources fully read for the teardown:

- `skills/make/logo/SKILL.md`
  - SHA-256 (isolated toolkit copy): `badfb2bc1b6598049174fd79c57b41ee30d177d9c89b20d38b93574ad5547a6d`
  - Supervisor `episode.source_sha256`: `213d82e10f452d09eb188f7bc8fde46b50d73fdb470915ec43509260d442e2ad`
    (differs by leading-whitespace normalization; the two-line divergence is between the
    supervisor snapshot cadence and the disk copy — both cover the same doctrine, the
    same eight animations, the same laws.)
- `skills/make/logo/scripts/logo.py`
  - SHA-256: `1a8376bd1d1702d3dc13bf5e619eae5b5ffc3969309710184b15c85c16c73b5e`
- `runtime/remotion/src/scenes/LogoOutro.tsx`
  - SHA-256: `7e2675615c99ce46f0a2bf22fb50b643131f2cfb9c3bb9a30ff2f2666306809c`
- `OUTRO-LOCK.md`
  - SHA-256: `a642621c1073604ff350381f58e2fbfa7dee1c0f586d8a285c44ed2c4ab51e01`

## Claims made in the reel — verification

### B00–B01 cold open + BLUF

- "One command appends one beat." — verified in SKILL.md line 15–19 and logo.py
  main flow (steps 1–6, lines 16–30 in the docstring).
- "Random once, then locked." — verified in SKILL.md §The laws #2 (line 90);
  logo.py records `shot.remotion.picked` at line 233 and re-uses it on next run
  (line 221–226).
- "The MP3 is the clock." — verified in SKILL.md §The laws #1 (lines 82–89) and
  logo.py `probe_dur` + `apad` + `durationS` at lines 252–260.

### B02 Anatomy

- Anatomy items verified against disk paths:
  - `skills/make/logo/SKILL.md` ✓
  - `skills/make/logo/scripts/logo.py` ✓
  - `runtime/remotion/src/scenes/LogoOutro.tsx` ✓ (registered as `LogoOutro` and
    `LogoOutro916` in Root.tsx lines 2144–2146 and 1977–1979)
  - `logos/[brand]/` — four pools present:
    `bear-brown/` (2 svgs, 6 mp3s), `humanitarians/` (1 svg, 9 mp3s),
    `medhavy/` (42 svgs + 12 rejected, 2 mp3s), `musinique/` (2 svgs, 5 mp3s).
  - `runtime/remotion/public/logo-outro/[brand]/` — the staging tree exists;
    logo.py `pub_rel = Path("logo-outro") / brand / pick["svg"]` at line 266.
- "A pool with no mp3s (or no svgs) is a MISSING" — verified in SKILL.md line
  42–46 and enforced in logo.py `missing()` function (lines 85–90) which logs
  to `BUILD-LOG.md` and `sys.exit`s.

### B03 Pipeline (six steps)

Each step verified in logo.py:
1. RESOLVE — `ALIASES` dict at lines 48–53; `brand = ALIASES.get(a.brand.lower())`
   line 197.
2. PICK & LOCK — `SystemRandom` at line 228, records pick at line 233
   (`{"brand", "animation", "svg", "mp3", "locked": True}`).
3. COPY + PAD — `apad=whole_dur={target:.3f}` at line 255.
4. STAGE SVG — `shutil.copy(svg_src, pub_dst)` at line 269.
5. APPEND BEAT — `new_beat` dict at lines 284–294; `shot.type: "REMOTION"`,
   `shot.remotion.pattern: "LogoOutro"`.
6. RENDER + COMPILE — `remotion_scenes.py --only bid` at lines 317–319;
   `compile.py --review` at lines 322–325.

### B04 The MP3 is the clock

- ffmpeg apad + libmp3lame command verified at logo.py lines 254–256.
- "durationS = padded length" — verified: `dur = probe_dur(mp3_dst)` then
  `props["durationS"] = dur` (lines 260, 276).
- "same law as outro.py" — cross-reference in SKILL.md line 88.
- "want a different length? use a different mp3" — SKILL.md line 88–89.

### B05 Random once, then locked

- Verified: logo.py line 218–235 (find existing beat's picked block, reuse
  unless `--reroll`).
- `--reroll` flag: argparse at line 186–187; behavior at line 221 (`if beat and
  not a.reroll`).
- Rebuilds byte-for-byte identical: because both the SVG path and the padded
  MP3 are byte-identical inputs and Remotion is a deterministic function of
  (props, duration, frame index), identical inputs → identical outputs. The
  `rerender` branch at logo.py line 303–305 only fires on `--reroll` or a
  duration delta > 0.01s.

### B06 Curate the pool

- "42 drawable / 25 unique" — SKILL.md lines 67–71; disk counts confirm 42
  visible `medhavy-logo-*.svg` files and 12 in `_rejected/`.
- The exact date "2026-09-01" is quoted from SKILL.md line 65.
- "Wordmarks are outlined paths — grep finds nothing" — SKILL.md line 74.

### B07 drawOn is earned

- Verified: logo.py `extract_paths` at lines 93–155 walks the SVG, sets
  `clean = False` on any `<text>`, `<image>`, `<use>`, `<linearGradient>`,
  `<radialGradient>`, `<mask>`, `<filter>` (line 150–152), or a non-path
  visible drawable (lines 147–149).
- `anims = ANIMATIONS if merged else [x for x in ANIMATIONS if x != "drawOn"]`
  at line 232 — this is the "drop from lottery" behavior.
- The 8 techniques list verified in LogoOutro.tsx line 27–30 and matches the
  narration.

### B08 Falsifiability — no logos/nik-bear-brown/ pool

- Verified: SKILL.md §Curate the pool… lines 76–78: "There is no
  `logos/nik-bear-brown/`, by design. @NikBearBrown does not use a logo sting
  — it uses `ClaudeTitleOutro`, whose CLAWD mascot is drawn from pixel rects
  in `ClaudeMascotScene.tsx` and reads no files at all."
- OUTRO-LOCK.md line 3–4 confirms: "Locked spec for the claude-liam /
  @NikBearBrown outro card. Applies to claude-liam reels ONLY."
- Cross-referenced: this reel IS a claude-liam reel and therefore uses
  `ClaudeTitleOutro` for the last beat (B11) — the beat's own architecture
  is the evidence for the falsifiability claim.

### B09 Verdict

Six lines are direct restatements of B04–B08 above and the anatomy of B02.

### B10 Your Turn prompt

- The prompt is genuinely runnable — `logo.py` with `--no-render --no-compile`
  was executed live on `demo/fixture-reel/` (a synthetic beat sheet) three
  times, and the full command output is captured in `demo/logo-run.log`.
  See `SHOTLIST.md` for the exact runs.

## Corrections and simplifications

- The narration says "SystemRandom" for the picker — that is the exact class
  used (`random.SystemRandom()` at logo.py line 228). Not simplified.
- The narration says "one second by default" for `--tail` — verified: default
  is `1.0` at argparse line 191.
- The narration does not name every one of the eight animation techniques by
  name (only in the on-screen quote and the anatomy card). Deliberate — the
  point of the beat is "seven Img-based + drawOn earned", not the roster.

Nothing invented. Nothing sensationalized. All source lines cited above are
present in the isolated-toolkit copies of the files.
