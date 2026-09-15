# Checks — Short cut (9:16)

Run: 2026-09-11 · run_id `199fe630ee9744af96cd435a69ed82e4` · re-verified (source SKILL.md sha updated; media unchanged).

## Cap check (SHORTS LAW #1)

- Parent film (native portrait vertical companion): 13 beats, 194.6s.
- Retained Short: 7 beats, planned 98.71s.
- Compiled `.mp4` container duration: **98.708s**. Video stream 98.667s.
  Audio stream 98.708s. Every measurement is strictly < 180.0s; **PASS**.
- Encoding headroom preserved: parent was 194s; the Short lives at 55% of the
  cap, so container rounding cannot push it into the 180s failure zone.

## Cut plan (SHORTS LAW #2)

Strategy: `whole-beat-cut`. See `CUT-PLAN.json` for the reviewed plan.
- Kept: `B00 B01 B02 B03 B10 B11 B12`.
- Dropped: `B04 B05 B06 B07 B08 B09` (the two revision cycles + the Revision
  Law verbatim quote + the design-tell payoff — a coherent block).
- No parent narration was rewritten; the outro was not regenerated. See
  CUT-PLAN.json § `outro_policy`.

## Portrait reuse (SHORTS LAW #3 / THE REFORMAT RULE)

`shorts.py` reused every kept beat's native 2160×3840 media unchanged:

```
[short] B00 native portrait reused unchanged
[short] B01 native portrait reused unchanged
[short] B02 native portrait reused unchanged
[short] B03 native portrait reused unchanged
[short] B10 native portrait reused unchanged
[short] B11 native portrait reused unchanged
[short] B12 native portrait reused unchanged
```

No REMOTION beat needed re-rendering; no center-cut ran. Every retained
MP3 is byte-for-byte identical to `parent/vertical/mp3/beat-<BID>.mp3`
(copy_asset via `shorts.py`, independent file — no symlink).

## Compile finish gate (`verify_output`)

- Command: `python3 runtime/scripts/compile.py <reel> --height 3840 --out <reel>/exports/short`
- Result: **PASS** — wrote `exports/short/claude-liam-brutalist-skill-cli-explainer-short.mp4`
  (98.7s, 2160×3840 @ 24 fps, h264 video + aac audio).
- File SHA-256: `706ba3773d810caf2ca58c37ef54c55c80e5fb86b6dbc335d1cfb08c88c90815`.

## Frame-level Visual QC (VISUAL QC LAW)

- **2 fps contact sheet**: `_qc/frames/f_0001.jpg` … `f_0197.jpg` (197 frames).
- **Beat-relative samples**: `_qc/beat_frames/<BID>_{015,050,085}.jpg`
  — 7 beats × 3 samples = 21 frames.
- **Every frame hashed** with SHA-256 and recorded in
  `VISUAL-REVIEW.json` and `_qc/frames_hashes.json`.
- **Every frame opened** with the image-capable Read tool during
  authoring (not the mp4 probe alone — VISUAL QC LAW is explicit that the
  file probe never counts as QC).

9-point rubric result:

| # | Check | Result |
|---|---|---|
| 1 | Edge bleed / clipping | clean — no text or graphic crosses SAFE (1944 × 3456) |
| 2 | Title-safe margins | composer beats (B00, B11) sit inside SAFE; anatomy/pipeline/verdict/outro cards inside SAFE column |
| 3 | Container overflow | none — verdict card lines wrap inside the artifact frame; composer lines wrap inside the input box |
| 4 | Collision | none — B02's callout does not overlap the folder tree; B03's phase boxes have consistent 42 px arrow gaps |
| 5 | Offscreen anchors | none |
| 6 | Legibility | serif greetings (Namaste, Liam / Your turn.) fill the top third; body copy legible at portrait scale; verdict's 4 numbered lines fit the safe column with wrap |
| 7 | Brand bug placement | @HumanitariansAI folder chip lower-left of composer beats (B00, B11); outro (B12) restates title + handle in cream on ink |
| 8 | Aspect | 2160×3840 native throughout; no stretch, no letterbox, no crop |
| 9 | CANVAS FILL | B01 hesitant-writer fills 5–6 lines vertically at 50% and 85% (above the FILL_MIN 0.55 floor from prior parent QC); anatomy/pipeline/verdict fill their safe columns; composer beats leave the intended lower half clean per ClaudeComposerAsk portrait layout |

**BLOCKER: 0. MAJOR: 0.**

## Skin-lint warnings (informational only)

`compile.py` printed:
- `B00: palette=claude but the cold open is 'ClaudeComposerAsk916' — COLD OPEN LAW wants ClaudeComposerAsk`
- `B12: palette=claude but the outro is 'ClaudeTitleOutro916' — OUTRO LAW wants ClaudeTitleOutro`

These are the intended ONDA-CHECK portrait rewires (both from the parent's
vertical build). The landscape lint targets the 16:9 file's laws; the 9:16
Short's parent already resolved and shipped these rewires. Not a portrait
defect.

## Preservation checks (protection surface)

| Item | State |
|---|---|
| Approved 16:9 landscape master | untouched — this Short lives under `youtube/brutalist/shorts/…-short/`; the landscape master under `youtube/brutalist/claude-liam-brutalist-skill-cli-explainer/exports/landscape/` was not read from or written to |
| Full-length native portrait companion | untouched — `parent/vertical/beat_sheet.json` sha256 `12f6a1dadf771d58078a7b9ab9221eba7205472df12b4a96673a162ff565ecff` verified (updated after SKILL.md change, same media); `parent/vertical/exports/vertical/*.mp4` sha256 `13cdc99770348dd77eac9ab6870d2d1cdd37cb80bbcfb04d9771cc6dcd74bfaa` matches the invocation's `parent_master_sha256` |
| Fellow example files (read-only) | not written — this Short did not open the local example JSONs (they were used to shape the parent's approach; the Short is a whole-beat cut of the parent, no example re-derivation ran) |
| Public toolkit | not written — build ran entirely inside the isolated workspace toolkit at `.repoloop/…/toolkit/` |
| Symlinks / hardlinks | none — every retained media file is an independent `shutil.copy2` (see `build_safety.copy_asset`) |
| Endcard | **skipped** — `--no-endcard`; the Short ends on the branded outro B12 (title restate + @HumanitariansAI handle) |
| Outro rewrite | **skipped** — `--no-outro-rewrite` is implicit because no `--rewrite-outro` was passed; the parent's B12 narration is unchanged |

## Preservation of prior Short exports

The prior Short (run_id `6d96cd18031749928d463a580129223d`, 2026-09-08) was
preserved until re-verification. This run_id `199fe630ee9744af96cd435a69ed82e4`
re-compiled the same 7-beat cut (media unchanged, SHA-256 identical to prior).
The compiled `.mp4` SHA `706ba3773d810caf2ca58c37ef54c55c80e5fb86b6dbc335d1cfb08c88c90815`
matches the prior run — same content, new provenance tracking to current source hashes.
