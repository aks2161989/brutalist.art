# Type check — Short cut

There is no legacy type checker in this toolkit at the paths where a
`typecheck.py`, `mypy` or `tsc --noEmit` would normally live. What follows
is the current runtime's actual gate list applied to this Short, plus an
explicit visual-typography pass on the extracted frames (the "type" in
"typecheck" for this project is the on-screen typography).

## 1. Runtime-schema gates (all passed)

- `build_safety.validate_project(sheet)` — beat sheet loaded, metadata
  object well-formed, `beats` non-empty, each `beat_id` matches
  `[A-Z][A-Z0-9_]*` and is unique. Slug matches
  `[A-Za-z0-9][A-Za-z0-9._-]*`. Ran once inside `shorts.py`
  (`main` line ~488 via `validate_project(derivative)` after atomic write)
  and once at the start of `compile.py`. No BuildError.
- `build_safety.require_short_duration(...)` — invoked three times as
  documented in `CHECKS-REPORT.md` §1 (planning sum 128.71 s, measured
  timeline 128.708 s, encoded container + per-stream ≤ 128.708 s). All
  three strictly < 180.0 s.
- `build_safety.is_source_report()` — returned False for every kept beat
  (no beat is a fellow's report; this teardown is source-backed). Skips
  `--vertical`-only carve-outs that do not apply.
- `positive_duration()` — every kept beat's `render_duration_s` (or
  `actual_duration_s`) is finite and > 0.
- `compile.validate_approvals(folder, sheet)` — `metadata.approvals = {}`,
  no `professor_notes` or `voice` approval is claimed, so the validator
  has nothing pending to gate on and returns cleanly. (This is honest:
  no fellow's `NOTES.md` was drafted, and no fellow's voice is being
  persisted.)
- `compile.require_paperwork(folder)` — `FACTCHECK.md`, `SHOTLIST.md`,
  `PROMPTS.md` all present and non-empty at final-pass time.

## 2. Remotion prop schema gates (all passed)

Every kept beat is a Remotion beat; the compiler wired each to its
registered composition in the isolated toolkit's `Root.tsx` snapshot and
rendered without a zod-schema mismatch. Prop names checked against
`feedback_remotion_prop_names` (name mismatches would silently fall back
to defaults):

- `B00` — `ClaudeComposerAsk916`. `greeting`, `topic`, `segment`,
  `command`, `runningText`, `folderLabel`, `modelLabel`, `effortLabel`,
  `output[]` all populated (unchanged from parent).
- `B01` — `BrutalistHesitantWriter916`. Portrait BLUF recipe: `fontSize`
  118, `lineSpacing` 2.2 (`feedback_hesitant_writer_portrait_bluf_recipe`;
  landscape defaults would produce underfill). `triggerWords` = `re-cuts`,
  `replacementWords` = `frames` — single tokens, no trailing punctuation
  (`feedback_hesitant_writer_triggers`).
- `B03` — `SkillTeardownPipeline916`. `eyebrow`, `title`, `inputLabel`,
  `outputLabel`, `phases[]` (five phases, `THE REPORT` marked `accent: true`),
  `footerNote`, `sparkLine`.
- `B04` / `B06` — `SkillTeardownMechanism916`. `eyebrow`, `heading`,
  `body`, `quote`, `cite`, `verdictLabel`, `verdictPositive`, `sparkLine`.
- `B09` — `ClaudeVerdictArtifact916`. `artifactTitle`, `artifactHeading`,
  `artifactLines[]` (six items).
- `B11` — `ClaudeTitleOutro916`. `title`, `slug` (drives seeded mascot).

No `channel_title` metadata is present on the beat sheet — deliberately
omitted per `feedback_channel_title_portrait_bleed` (compile-overlay
bleeds past portrait safe area on 9:16). Handle `@NikBearBrown` on B11 is
hardcoded via `OUTRO-LOCK.md`; folder chip `@HumanitariansAI` on B00 lands
correctly.

## 3. Visual typography — the "type" review of a typography-heavy piece

Frames extracted at 15 %, 50 %, 85 % of each kept beat plus first and
final, and a 2-fps contact sheet, were opened with the image-capable Read
tool (see `CHECKS-REPORT.md` §5).

**Legibility.** All body/quote text on every frame is readable at the
extracted 540×960 preview scale (native is 2160×3840). No character
clipping, no partial glyph render, no falsely broken ligature. The
BLUF (B01) five-line reflow is fully visible in the safe box after
correction; before correction the terracotta `re-cuts` correction cue
lands as designed.

**Portrait framing.** No text crosses the outer 5 % gutter on any
extracted frame. The `B09` verdict card (widest text block) sits with
comfortable margin. `B11` title/handle centered around the mid-height.

**Palette adherence.** Claude cream (`#F3EBDD`), ink (`#2F2A26`),
terracotta (`#D35F43`) present on every beat. Terracotta is used only as
an accent (send button, verdict pill borders, `THE REPORT` node, hesitant
`re-cuts` cue, outro period).

**No burned captions, no compile-time subtitle overlay.** `captions:
false` in metadata was respected; verified by inspecting each frame.

**BLUF underfill.** The extracted 50 % frame of B01 easily crosses the
`FILL_MIN 0.55` bar (`feedback_gate_v_underfill`) — five lines of serif
text fill the middle of the safe area.

## 4. No untyped or unused metadata

- `metadata.aspect_ratio` = `9:16`. `kind` = `short`. `derived_from`
  points at the parent slug. `dropped_beats` lists all five.
- `total_estimated_duration_seconds` = 128.71. `short_validation.status`
  = `ready`.
- `voice` = `am_onyx`, `voice_kokoro` = `am_onyx`, `engine` = `kokoro`.

## 5. Not-a-typechecker items (kept as blank verifiers, per convention)

- No TypeScript source was authored or changed in this Short — every
  Remotion composition is the same one the parent rendered. Nothing to
  `tsc --noEmit`.
- No Python source was authored or changed. `shorts.py`, `compile.py`,
  `build_safety.py` are the toolkit's copies as-of the isolated snapshot;
  their public behavior is exercised in §1–§2.

## 6. Result

All schema, safety and typography gates pass with the values shown above.
No blockers. No majors. Editorial numbering artifact around "Third
decision" (see `CHECKS-REPORT.md` §7) is documented and knowingly kept;
no other coherence problems.

Re-verified run_id `28dd40173c164f0a85bea3d8084e2ee7`: source change was parent
beat_sheet re-verification only; no media, narration or visual content changed.
`math_layout_check.py` copied from main runtime into isolated toolkit to satisfy
updated `build_safety.validate_project()` import; no beat sheet content affected.
