# CHECKS-REPORT — Download Brutalist with Claude Code (landscape)

Aspect: 16:9 · Master: `exports/landscape/claude-liam-brutalist-download-and-set-up.mp4`

## Beat classification (SHOW / HOLD / CARD)

| Beat | Class | Justification |
|------|-------|---------------|
| B00  | SHOW  | Composer types the ask on cue; running indicator and three response lines land on the last phrase. |
| B01  | SHOW  | Hesitant writer types the wrong framing, deletes, retypes correction — motion IS the pedagogy. |
| B02  | SHOW  | Prompt types itself into the composer card; three step chips arrive after. |
| B03  | SHOW  | Seven tree rows arrive on cue, entry chips light in terracotta. |
| B04  | SHOW  | Terminal card fills in: prompt, header, seven feature rows, all `✓ ready`, closing summary. |
| B05  | SHOW  | Three lanes fill in sequence; setup-cost banner arrives at the close. |
| B06  | SHOW  | Three limitation rows arrive in sequence. |
| B07  | SHOW  | Verdict card arrives, then three lines number by number. |
| B08  | SHOW  | Handoff composer types the paste-ready prompt; three expected-outcome lines settle. |
| B09  | SHOW  | Poster title, handle, subline land in sequence. |

Result: 10 SHOW / 0 HOLD / 0 CARD / 0 PUNT.

## Teaching-arc checklist

| Item | Status | Where |
|------|:---:|-------|
| FRAMEWORK before EXAMPLES | ✓ | B02 (paste-ready) precedes B03 (clone), B04 (doctor). |
| WORKED EXAMPLE | ✓ | B03 shows the actual folder tree; B04 shows the real doctor table. |
| FALSIFIABILITY / not-list | ✓ | B06 names three specific things setup does NOT do, plus the one download it DOES perform. |
| SCAFFOLDED TASK | ✓ | B08 supplies a paste-ready prompt with expected outputs, invites viewer to run. |
| BOOKENDS (4) | ✓ | B00 ask, B01 BLUF, B08 handoff, B09 outro. |
| NO-SOURCE-NO-VERDICT | ✓ | Verdict at B07 is grounded in claims established B02–B06. |

## Frame-level QC (Gate V — final_frame_check.py)

Command:
```
python3 runtime/qc/final_frame_check.py <reel> --mp4 <candidate.mp4> --sheet <resolved-sheet.json>
```

Result (from `_qc/REPORT.md`):
```
Frames sampled: 20  ·  BLOCKER: 0  ·  MAJOR: 0
Clean — no BLOCKER/MAJOR defects. ✓
```

Iterations across original build + this rebuild:

1. (Original) First B05 pass had two BLOCKER `edge-bleed` defects at the setup-cost banner. Fix: reduced `laneH` from 660→580 in `DbcLanes`.
2. (Original) B01 hesitant-writer `triggerWords` used space-separated phrases. Fix: comma-separated single tokens.
3. (Rebuild run 92aed5ea) B04 DbcDoctor: the card's `boxShadow: '0 14px 44px rgba(0,0,0,0.20)'` cast a 14px shadow below the card bottom (1020px at 1080p), just crossing safe.b=1026px. Fix: reduced `cardH` from 780→756 so the card bottom sits at 996px, leaving the shadow clear of safe.b.

After all fixes: Gate V clean.

## Compiler final verification

`exports/landscape/claude-liam-brutalist-download-and-set-up.verified.json`:
- status: `ready`
- duration: 165.1s
- video codec: h264, 3840×2160
- audio codec: aac, 165.1s
- input SHA-256 recorded per beat mp3 + media mp4 (see verified.json)

## Additional gates run

- `runtime/qc/beat_lint.py` (invoked internally by compile.py `final_preflight`) — passed.
- `runtime/qc/gate_shape.py` (invoked internally) — passed.
- `runtime/scripts/build_safety.py validate_project` — passed (10 beats, unique IDs, slug shape ok).

## Manual visual inspection

Frames extracted at 15%, 50%, 75% of each beat via ffmpeg, then Read as PNG images. Inspected:
- B00 late (6.0s): full ask visible, three concrete output lines below, HAI folder chip present. ✓
- B01 mid: hesitant writer typing (mid-correction pass). ✓
- B02 late (12.7s): composer card filled with wrapped prompt, three chips readable, no overlap. ✓
- B03 late (14.5s): tree rows all visible, entry chips terracotta on `setup` and `art`. ✓
- B04 late (15.4s): terminal table all seven rows green, closing summary. ✓
- B05 late (18.3s): three lanes complete, setup-cost banner inside safe area. ✓
- B06 late (14.4s): three limitation rows visible with correct copy. ✓
- B07 mid: verdict card, three numbered lines. ✓
- B08 late (14s): full paste-ready prompt visible in composer, expected-outcome lines below. ✓
- B09 mid: title, HAI handle hardcoded, subline. ✓

## Gaps / limitations honestly recorded

- **`type_check.py` (GATE T)** — not present in this toolkit (`runtime/qc/type_check.py` does not exist). CLAUDE.md §GATE T references it, but the shipped runtime does not include the file. This report cannot claim a GATE T pass; visual typography review was performed manually (see TYPECHECK.md).
- **`kerning/SKILL.md`** — referenced in ai-explainer SKILL.md but not shipped under `skills/`. Not blocking.
- **Skin lint warning** — compile.py logs `"B09: palette=claude but the outro is 'DbcOutro' — OUTRO LAW wants ClaudeTitleOutro"`. This is expected and correct: the shipped `ClaudeTitleOutro` hardcodes `@NikBearBrown` (see `OUTRO-LOCK.md`) and cannot be used on the `@HumanitariansAI` channel. The reel-local `DbcOutro` is the required native custom variant. The warning is a lint hint, not a gate failure.

## Re-verification pass — invocation 841e7161 (2026-09-11)

Source change since run 92aed5ea: `REPOLOOP-PROMPT.md` added to repo (new untracked file). Episode content is unaffected — narration uses "builder recipes" generically with no skill count. No beats re-rendered. ffprobe confirms landscape export unchanged: h264 3840×2160, 165.04s video + 165.08s audio. Both contact sheets re-read in this session; all 10 beats verified visually (see VISUAL-REVIEW.json run_id 841e7161). VISUAL-REVIEW.json updated to new run_id and source_sha256.

## Re-verification pass — invocation ce92be0cfd8c406eb1f61da85c13df17 (2026-09-11)

Source change since run 841e7161: `README.md` updated (Godot skill rows added to builder table) and `art` script updated; composite source_sha256 changed from `a61eb6f2…` to `402542d0…`. Episode content is unaffected — narration teaches clone/setup/doctor and subscription-vs-API with no reference to which skills exist in the builder table. No beats re-rendered. ffprobe confirms landscape export unchanged: h264 3840×2160, 165.04s video + 165.08s audio. Landscape contact sheet read in this session; all 10 beats verified visually. MP4 hash 85c16a2c… unchanged. VISUAL-REVIEW.json updated to new run_id and source_sha256.

## Re-verification pass — invocation db8a5a5b2c0f4d74a8c148cc6c2b2e9e (2026-09-11)

Source changes since run ce92be0c: `docs/PIPELINE-SAFETY.md` and `docs/FELLOWS-SUBMISSION.md` newly added to the repo; `art` script updated with `vertical` and `approvals` commands and updated help text. These are covered by dedicated later episodes (Ep 31 / Ep 32) and do not affect the download/setup teaching in this episode. No beats re-rendered. ffprobe confirms landscape export unchanged: h264 3840×2160, 165.04s video + 165.08s audio. Landscape contact sheet read in this session; all 10 beats verified visually. MP4 hash 85c16a2c… unchanged. VISUAL-REVIEW.json updated to new run_id (db8a5a5b…) and source_sha256 (eaeb9039…).

## Conclusion

Landscape master `claude-liam-brutalist-download-and-set-up.mp4` (3840×2160, 165.1s, h264+aac) passes every gate the toolkit provides. Ready for Bear's human review.
