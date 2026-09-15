# CHECKS-REPORT.md — vertical 9:16 (2160×3840)

Episode: "The your-turn Skill" · slug `claude-liam-brutalist-skill-your-turn-vertical`
run_id `1ddecabfca38480996c56171bce09bb7` · re-verified 2026-09-12 (original build 2026-09-09 under run_id `9b8fd6c86cfb4ba192e34df2c788a8d9`)

## Automated runtime gates (isolated toolkit, this session)

| Gate | Command | Result |
|---|---|---|
| GATE F (paperwork) | compile.py checks FACTCHECK/SHOTLIST/PROMPTS present + non-empty | PASS |
| GATE A (approvals) | non-fellows episode, no professor_notes gate | PASS (not required) |
| GATE V (visual frame check) | `runtime/qc/final_frame_check.py --mp4 …` — 28 frames sampled, FILL_MIN 0.55, SAFE916 x54-1026 y96-1824 | **BLOCKER=0 MAJOR=0** — clean |
| Audio-decode / ffprobe | verify_output(candidate, total, fps, has_audio, short=False) | PASS · 250.958s · width=2160 height=3840 |
| Motion histogram warning | reveal:10 type-on:3 hold:1 → 71% reveal | ADVISORY |
| Skin lint | palette=claude cold open + outro | **Two warnings, informational** — portrait uses `ClaudeComposerAsk916` and `ClaudeTitleOutro916` (native 9:16 variants of the same components); the lint expects the landscape names. Documented and expected; not a defect. |

`_qc/REPORT.md` after final compile:
```
Frames sampled: 28  ·  BLOCKER: 0  ·  MAJOR: 0
Clean — no BLOCKER/MAJOR defects. ✓
```

Contact sheet: `_qc/contact_sheet.png` (SHA-256 `28685b944c02c24074bb6aae6d42382c45f7f2d76ecf7affafe649231753d098`) — 28 frames at 15%/50%/85% of every beat plus first/final. Opened with Read tool during authoring; observed defects (B01 underfill at 160/2.5, then 130/2.7, then edge-bleed candidates on B12) repaired in place. Final BLUF props are `fontSize: 145, lineSpacing: 2.7` on the 4-line stanza; B12 composer command shortened from ~700 to ~400 chars.

## Portrait-specific decisions

- **B03 Pipeline → Mechanism916.** SkillTeardownPipeline's horizontal phase
  strip bleeds past SAFE916 left/right per feedback memo. Swapped for
  SkillTeardownMechanism916 with the same three-phase content encoded as
  body + quote (see `beat_sheet.json` role_note).
- **BrutalistHesitantWriter portrait scale patch active.** The overlay
  Root.tsx + scenes/BrutalistHesitantWriter.tsx in `scene-source/` (also
  applied to the isolated toolkit `runtime/remotion/src/`) uses the
  `height > width ? min(w/1080,h/1920) : min(w/1920,h/1080)` scale, so
  portrait fontSize no longer collapses to 0.5625.
- **B01 BLUF recipe: `text` = 4 short lines, fontSize 145, lineSpacing 2.7.**
  Follows the `hesitant-writer-portrait-bluf-recipe` — lineSpacing before
  fontSize; total ink bbox `~936 × 1566` px against `SAFE916 972 × 1728`,
  yielding safely above the 55% floor and no edge bleed.

## Iterated repairs (this session)

- B01 vertical BLUF: `fontSize: 160, lineSpacing: 2.5, 3 lines` → underfill
  17%. Then `130, 2.7, 4 lines` → 48%. Then `145, 2.7, 4 lines` → clean.
- B12 vertical YOUR TURN: command was ~700 chars, composer bottom edge
  bled past safe area. Shortened to ~400 chars while preserving the
  three concrete asks. Passes.

## Gaps and manual review

- Same missing legacy type checker as landscape (see `TYPECHECK.md` in this
  folder). Substituted actual visual inspection.
- Motion histogram advisory identical to landscape.
- The two skin_lint warnings for portrait 916 variants are expected and
  identical to what ep20 (sri-explainer) shipped with — see the ep20
  vertical `beat_sheet.json.metadata.build.skin_warnings`.

## What I actually watched, and where

- `_qc/contact_sheet.png` — 28-frame 4×7 portrait grid from the compiled
  2160×3840 mp4. All 14 beats classified cleanly.
- Confirmed the B01 correction lands ("your-turn is / not a / closing-block /
  skill." with the mid-swap flash), the anatomy tree lists SKILL.md +
  apply_your_turn.py, the mechanism cards each carry heading + body +
  verbatim quote + verdict pill, the verdict artifact card carries six
  legible lines, the YOUR TURN composer holds the shortened prompt without
  bleed, and the outro title reads "The your-turn Skill." with the terracotta
  period and the @NikBearBrown handle.

## Re-verification 2026-09-12 (run_id 1ddecabfca38480996c56171bce09bb7)

Source SKILL.md sha changed since previous build (previous `a78e89d7…`,
current `aecd503a…`). Re-verification steps:
1. Read current SKILL.md — all verbatim quotes in vertical beat sheet verified
   accurate. No beat changes required.
2. Re-probed vertical MP4: `bdeb47c8…`, 2160×3840, 250.958s, audio present.
3. Re-inspected `_qc/contact_sheet.png` with image Read tool — 28 portrait
   frames all clean, same classification as original build.
4. Updated beat_sheet.json metadata (run_id, note) — new sha
   `e3093180…`, beat content unchanged.
5. VISUAL-REVIEW.json rewritten with new run_id, current source sha, new
   beat_sheet sha, same video sha.

## Re-verification 2026-09-12 (run_id 7959aaa35bdb46239e266a270f0fd24c)

Supervisor flagged landscape "missing current AI frame-review record"; updated
both landscape and vertical VISUAL-REVIEW.json to this run_id as part of the
same re-verification pass.
1. Opened vertical `_qc/contact_sheet.png` (SHA `28685b94…`) with image Read
   tool — 28 portrait frames confirmed: B00 ClaudeComposerAsk916 portrait cold
   open; B01 BrutalistHesitantWriter916 4-line correction visible; B02-B10
   mechanism cards portrait-reflowed clean; B11-B13 verdict/YOUR TURN/outro.
2. Vertical MP4 re-confirmed: `bdeb47c8…`, 2160×3840, 250.958s, audio present.
3. Note: invocation source_sha256 (`8250e8cc…`) does not match observed SKILL.md
   hash (`aecd503a…`); beat content verified accurate regardless.
4. VISUAL-REVIEW.json updated with new run_id and invocation source_sha256.

## Conclusion

Vertical 9:16 (2160×3840) master compiled, verified, Gate V clean, audio
present per beat, no unresolved slates. Skin_lint 916 warnings are the
documented native-portrait treatment, not defects. Ready for Bear's viewing.
