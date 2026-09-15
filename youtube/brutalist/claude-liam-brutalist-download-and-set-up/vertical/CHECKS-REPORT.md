# CHECKS-REPORT — Download Brutalist with Claude Code (vertical / portrait)

Aspect: 9:16 · Master: `exports/vertical/claude-liam-brutalist-download-and-set-up-vertical.mp4`

The vertical is a **native 9:16 build**, not a crop of the landscape. Each beat re-renders through the same reel-local components (`DbcPasteReady916`, `DbcCloneTree916`, `DbcDoctor916`, `DbcLanes916`, `DbcNotClaims916`, `DbcVerdict916`, `DbcOutro916`) plus the shipped `ClaudeComposerAsk916` and `BrutalistHesitantWriter916`. Layouts stack/reflow off `useVideoConfig()`.

## Beat classification (SHOW / HOLD / CARD)

Same as landscape — every beat classifies as SHOW. The narration timing is unchanged (same Kokoro mp3s), so the master clock is identical.

## Teaching arc — same as landscape

- FRAMEWORK before EXAMPLES ✓ | WORKED EXAMPLE ✓ | FALSIFIABILITY ✓ | SCAFFOLDED TASK ✓ | BOOKENDS ✓ | NO-SOURCE-NO-VERDICT ✓

## Portrait-specific tuning (per Gate V)

The default portrait render of `BrutalistHesitantWriter916` was flagged twice by Gate V for `underfill` (18–35 % coverage instead of the ≥55 % floor). The fix (referenced in the toolkit memory as the "Gate V underfill (FILL_MIN 0.55)" pattern):

- Break the BLUF into **6 short lines** so vertical coverage crosses the 55 % floor.
- Enlarge to `fontSize: 320` with `lineSpacing: 1.35` — matching the shipped WIB portrait recipe.
- Rewrite `text`, `triggerWords`, `replacementWords` for six single-word rows so the correction pass still lands.

Final `B01.props` (portrait):
```
text:              "Downloading\nBrutalist\nis\nrunning\nan\ninstaller."
triggerWords:      "running, an, installer"
replacementWords:  "just, a, git-clone"
fontSize:          320
lineSpacing:       1.35
```

`DbcLanes916` was also tuned once: `laneStartY` moved from 300→400 in portrait so the 2-line title has clearance from the first lane card.

## Frame-level QC — Gate V

Final report:
```
Frames sampled: 20  ·  BLOCKER: 0  ·  MAJOR: 0
Clean — no BLOCKER/MAJOR defects. ✓
```

Two prior iterations recorded in the build history:
1. Initial vertical render — B01 flagged as `underfill` 18 % (short 3-line BLUF at fontSize 170).
2. Bumped to fontSize 220, 3 wide lines — flagged as `edge-bleed` on B01 (widest line overflowed portrait safe width).
3. Final: 6 short lines at fontSize 320 — passes.

## Compiler final verification

`exports/vertical/claude-liam-brutalist-download-and-set-up-vertical.verified.json`:
- status: `ready`
- duration: 165.1s
- video codec: h264, 2160×3840
- audio codec: aac, 165.1s

## Manual visual inspection

Frames sampled at 65 % of each beat's span (steady state), scaled to 400 px, then Read. Contact sheet at `vertical/_qc/vertical-contact-sheet.png` (5×2 grid).

- B00 portrait composer stacks vertically (segment eyebrow, greeting, composer card, response lines) — @HumanitariansAI chip present. ✓
- B01 6-line hesitant writer fills the safe area; correction "running an installer" → "just a git-clone" lands cleanly. ✓
- B02 paste-ready prompt card + 3 chips stack vertically. ✓
- B03 tree card with all 7 rows, entry chips terracotta. ✓
- B04 dark terminal card, all 7 rows green (dependency column wraps to 2-4 lines per row — legible). ✓
- B05 three lanes stack; setup-cost banner well inside safe area (post-fix). ✓
- B06 three limitation rows. ✓
- B07 verdict artifact card, numbered lines readable. ✓
- B08 Your Turn composer with the paste-ready prompt visible. ✓
- B09 DbcOutro916 with hardcoded @HumanitariansAI handle. ✓

## Additional gates

`beat_lint.py`, `gate_shape.py`, `validate_project` — all pass (invoked internally by compile.py).

## Gaps / limitations honestly recorded

- `type_check.py` — same absence as landscape; documented in `TYPECHECK.md`.
- Skin-lint warnings on B00 (`ClaudeComposerAsk916` for the cold open — expected) and B09 (`DbcOutro916` for HAI handle — expected).
- B04 portrait dark-terminal card has dependency-column text that wraps to multiple lines (visual density is higher than landscape); the rows are still clearly readable and no BLOCKER/MAJOR is flagged.

## Re-verification pass — invocation 841e7161 (2026-09-11)

Source change since run 92aed5ea: `REPOLOOP-PROMPT.md` added to repo. Episode content unaffected. No beats re-rendered. ffprobe confirms vertical export unchanged: h264 2160×3840, 165.04s video + 165.08s audio. Vertical contact sheet re-read in this session; all 10 portrait beats verified (see VISUAL-REVIEW.json run_id 841e7161). VISUAL-REVIEW.json updated to new run_id and source_sha256.

## Re-verification pass — invocation ce92be0cfd8c406eb1f61da85c13df17 (2026-09-11)

Source change since run 841e7161: `README.md` updated (Godot skill rows added) and `art` script updated; composite source_sha256 changed. Episode content unaffected. No beats re-rendered. ffprobe confirms vertical export unchanged: h264 2160×3840, 165.04s video + 165.08s audio. Vertical contact sheet read in this session; all 10 portrait beats verified (see VISUAL-REVIEW.json run_id ce92be0c…). MP4 hash 77e741e2… unchanged. VISUAL-REVIEW.json updated to new run_id and source_sha256.

## Re-verification pass — invocation db8a5a5b2c0f4d74a8c148cc6c2b2e9e (2026-09-11)

Source changes since run ce92be0c: `docs/PIPELINE-SAFETY.md` and `docs/FELLOWS-SUBMISSION.md` newly added; `art` script updated with `vertical` and `approvals` commands. Episode content unaffected. No beats re-rendered. ffprobe confirms vertical export unchanged: h264 2160×3840, 165.04s video + 165.08s audio. Vertical contact sheet read in this session; all 10 portrait beats verified (see VISUAL-REVIEW.json run_id db8a5a5b…). MP4 hash 77e741e2… unchanged. VISUAL-REVIEW.json updated to new run_id (db8a5a5b…) and source_sha256 (eaeb9039…).

## Conclusion

Vertical master `claude-liam-brutalist-download-and-set-up-vertical.mp4` (2160×3840, 165.1s, h264+aac) passes every enabled gate. Ready for Bear's human review.
