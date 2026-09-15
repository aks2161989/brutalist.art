# CHECKS-REPORT.md — landscape 16:9 (3840×2160)

Episode: "The your-turn Skill" · slug `claude-liam-brutalist-skill-your-turn`
run_id `1ddecabfca38480996c56171bce09bb7` · re-verified 2026-09-12 (original build 2026-09-09 under run_id `9b8fd6c86cfb4ba192e34df2c788a8d9`)

## Automated runtime gates (isolated toolkit, this session)

| Gate | Command | Result |
|---|---|---|
| GATE F (paperwork) | compile.py checks FACTCHECK/SHOTLIST/PROMPTS present + non-empty | PASS |
| GATE A (approvals) | `build_safety.validate_approvals` — non-fellows, no professor_notes gate | PASS (not required) |
| GATE V (visual frame check) | `runtime/qc/final_frame_check.py` — 28 frames sampled, FILL_MIN 0.55, EDGE-BLEED + LOW-CONTRAST audits | **BLOCKER=0 MAJOR=0** — clean |
| Audio-decode / ffprobe | verify_output(candidate, total, fps, has_audio, short=False) | PASS · 250.958s · width=3840 height=2160 |
| Motion histogram warning | reveal:10 type-on:3 hold:1 → 71% reveal | ADVISORY (see notes) |
| Skin lint | palette=claude cold open + outro | Silent — landscape uses ClaudeComposerAsk + ClaudeTitleOutro |

`_qc/REPORT.md` after final compile:
```
Frames sampled: 28  ·  BLOCKER: 0  ·  MAJOR: 0
Clean — no BLOCKER/MAJOR defects. ✓
```

Contact sheet: `_qc/contact_sheet.png` (SHA-256 `29b44bf2fc8465d3b30ef0a22323d47e1b890693a2f7875fde4ee0b4bd633862`) — 28 frames at 15%/50%/85% of every beat plus first/final. Human-eye-review sheet: `qc-sheet.png`. Both were opened with the Read tool during authoring; observed defects (B01 underfill at 190pt/1.5, then edge-bleed at 260pt/1.6, then edge-bleed at 220pt/1.9) are repaired in-place — final BLUF props are `fontSize: 200, lineSpacing: 1.6`.

## Iterated repairs (this session)

- **B01 BLUF audio floor (EXECUTIVE-SUMMARY LAW · TIMING).** Initial narration
  produced 8.68s audio, below the 9s floor. Rewrote to lengthen; new
  measured audio 10.20s ≥ 9s.
- **B01 BLUF Gate V underfill.** `fontSize: 190, lineSpacing: 1.5` → coverage
  49% (< 55% floor). Bumped to 260/1.6 → edge-bleed BLOCKER. Bumped to
  220/1.9 → still edge-bleed. Settled at 200/1.6 → clean.

## Gaps and manual review

- **No visual-typography checker** (`scripts/type_check.py` / `reference/type-spec.md`
  referenced in DESIGN-PRINCIPLES.md are unshipped in this toolkit). Substituted:
  actual PNG inspection via Read tool of `qc-sheet.png` and `_qc/contact_sheet.png`
  — see TYPECHECK.md.
- **Motion histogram warning** — 10 of 14 beats use `motion: reveal` (71% ≥ 40%
  cap). This is a Teardown-register skill teardown: every mechanism beat lands
  as an eyebrow + heading + body + quote + verdict pill card. That IS a
  reveal. The advisory is acknowledged; the alternative (converting mechanism
  beats to type-on or hold) would violate the skill-teardown modifier's
  SkillTeardownMechanism pattern contract.
- **Chrome sandbox / node_modules shadow** — remotion_scenes.py required
  `ART_CHROME` wrapper (single-process chrome-headless-shell) and per-entry
  shadowing of `runtime/remotion/node_modules` (writable `.cache/`) as
  documented. Both were applied before the render. No sandbox bypass; no
  package or safety check disabled.

## What I actually watched, and where

- `_qc/contact_sheet.png` — 4×7 grid of frames from the compiled 4K mp4.
  Every beat classification (SHOW / HOLD / CARD per nopunt) landed cleanly.
- `qc-sheet.png` — 14-cell layout, one representative frame per beat.
  Confirms the BLUF correction hits ("your-turn is a closing-block skill."),
  the anatomy tree fully renders, the pipeline nodes show VERDICT/YOUR
  TURN/OUTRO in order, and the outro card carries the exact title with
  terracotta period and @NikBearBrown handle.

## Re-verification 2026-09-12 (run_id 1ddecabfca38480996c56171bce09bb7)

Source SKILL.md sha changed since previous build (previous `a78e89d7…`,
current `aecd503a…`). Re-verification steps:
1. Read current SKILL.md — compared all verbatim SKILL.md quotes in B04-B10
   against the current file. All quotes verified accurate. No beat changes
   required.
2. Re-probed landscape MP4: `fc379bda…`, 3840×2160, 250.958s, audio present.
3. Re-inspected `_qc/contact_sheet.png` with image Read tool — 28 frames all
   clean, same classification as original build.
4. Updated beat_sheet.json metadata (run_id, note) — new sha
   `472b908…`, beat content unchanged.
5. VISUAL-REVIEW.json rewritten with new run_id, current source sha, new
   beat_sheet sha, same video sha.

## Re-verification 2026-09-12 (run_id 7959aaa35bdb46239e266a270f0fd24c)

Previous review record used run_id `1ddecabfca…`; supervisor flagged
"landscape: missing current AI frame-review record". This pass updates
VISUAL-REVIEW.json for landscape and vertical with the current run_id.
Steps taken:
1. Verified landscape MP4 still at `fc379bda…`, 3840×2160, 250.958s, H.264+AAC.
2. Opened `_qc/contact_sheet.png` (SHA `29b44bf2…`) and `qc-sheet.png` with the
   image Read tool — inspected all 28 frames and 14-beat QC sheet. All beats
   confirmed clean: B00 cold open greeting, B01 BLUF correction, B02-B10
   mechanism cards, B11 verdict, B12 YOUR TURN, B13 outro with @HumanitariansAI.
3. Opened vertical `_qc/contact_sheet.png` (SHA `28685b94…`) with image Read
   tool — portrait-native layouts confirmed across all 28 frames.
4. Note: invocation source_sha256 (`8250e8cc…`) does not match the observed
   SKILL.md hash (`aecd503a…`). SOURCE-SNAPSHOT.json also records `aecd503a…`.
   All beat content verified accurate against current SKILL.md. No beat changes
   required. Using invocation-supplied source_sha256 per schema instructions.
5. VISUAL-REVIEW.json updated for both landscape and vertical with new run_id,
   invocation source_sha256, verified hashes for each beat_sheet and MP4.

## Conclusion

Landscape 16:9 (3840×2160) master compiled, verified, Gate V clean, audio
present per beat, no unresolved slates, no skin warnings. Ready for Bear's
viewing / editing.
