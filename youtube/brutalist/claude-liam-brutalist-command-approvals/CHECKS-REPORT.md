# CHECKS-REPORT — landscape

## Beat classification (per PROOF GATE, nopunt SKILL)

12/12 SHOW, 0 HOLD, 0 PUNT. No slates.

Each body beat's `shot.show` block names the visual events that land against the narration.
No beat's narration invents a visual absent from the source. Every code beat is a real code
artifact (either from `art`/`build_safety.py` or the verbatim `demo/RUN-LOG.txt`).

## Teaching arc checklist

- FRAMEWORK ✓ — B02 (dispatcher case) + B03 (two verbs + metadata.approvals shape).
- WORKED EXAMPLE ✓ — B04 (plain command reel, silent pass) + B05 (fellows reel, --fingerprints).
- FALSIFIABILITY ✓ — B08 (stale-approval refusal + recovery, both verbatim).
- SCAFFOLDED TASK ✓ — B10 Your Turn prompt, read aloud + graded rubric.
- BOOKENDS ✓ — B00 cold-open ClaudeComposerAsk, B01 BLUF, B09 verdict, B10 Your Turn, B11 outro.
- NO SOURCE, NO VERDICT ✓ — every verdict line at B09 maps to a specific source line in FACTCHECK.md.

## Gate F (paperwork triad)

- FACTCHECK.md · ~7 KB · every claim mapped to a source line.
- SHOTLIST.md · beat table + per-beat visual constraints.
- PROMPTS.md · the two visible prompts (B00 ask + B10 Your Turn) documented; no image/video generators called.

## Gate V (frame-level QC on the finished MP4)

```
$ python3 runtime/qc/final_frame_check.py \
    <REEL> \
    --mp4  <REEL>/exports/landscape/claude-liam-brutalist-command-approvals.mp4 \
    --sheet <REEL>/clips/_work/resolved-sheet.json
[gate-v] frames=24 BLOCKER=0 MAJOR=0 → <REEL>/_qc/REPORT.md
```

24 frames sampled at 2 fps plus each beat at 15/50/85% of its span. Clean. Report at `_qc/REPORT.md`.

## Frame-by-frame AI visual review

Beyond Gate-V's layout heuristic, ten representative frames were extracted from the
finished 4K master and read individually with the image-capable Read tool. Frame paths + SHA-256
are recorded in `VISUAL-REVIEW.json`. What each still confirms:

- `start.png` (B00, t=0.5s) — cream page, serif greeting "Selam, Liam", composer, folder chip `@HumanitariansAI`. Ask hasn't landed yet at this frame.
- `bluf.png` (B01, t=15s) — hesitant writer near steady state, corrected sentence "art approvals / inspects subjects." on screen.
- `framework.png` (B02, t=30s) — code card "art:108-110 — one branch, no aliases" with the three-line `approvals)` case visible.
- `worked-cmd.png` (B04, t=70s) — verbatim `$ ./art approvals /tmp/…-command --fingerprints` transcript with `{}` output and `[exit 0]`.
- `worked-fellows.png` (mid-B06, t=100s) — the five-field record contract with the exact fail-close conjunct from `build_safety.py:155-164`.
- `mechanism.png` (B07, t=130s) — `digest()` + `approval_subjects()` bodies from `build_safety.py`.
- `failure.png` (B09, t=168s) — Verdict artifact card (label is timing-based, not narrative-based).
- `verdict.png` (B10, t=188s) — Your Turn composer with the full prompt typed in.
- `your-turn.png` (B10-end, t=198s) — Your Turn composer near end.
- `end.png` (B11, t=200.5s) — outro card, title restate with terracotta period, `@NikBearBrown` handle (OUTRO-LOCK).

Every still shows the expected content — no unresolved slates, no captions/subtitles, no
overlapping text, no off-frame content, no unwanted UI decoration. Skin-lint's warning about
`@HumanitariansAI` composer folder chip beside `@NikBearBrown` outro is the accepted playlist
adaptation (called out in README.md).

## Runtime checks not run (honest gaps)

- `scripts/type_check.py` (Gate T) — not present in this toolkit snapshot; see TYPECHECK.md.
- `art doctor` / `art keys` — not invoked; this build does not need any key, and Kokoro + Remotion
  proved themselves by running successfully in this session.
- Skill-teardown lint (`skills/make/ai-explainer/*.py`) — none available in this snapshot.

## Motion histogram

```
code-cascade:7  type-on:2  hesitant-type:1  artifact-in:1  outro-card:1
```

Warning: `code-cascade` runs at 7/12 (58%), over the ~40% pantry cap. Accepted —
the episode is a command teardown; the body is code that must be read. Each code
beat carries a DIFFERENT code artifact (dispatcher, argparse+shape, two verbatim
transcripts, record contract, digest bodies, stale-approval recovery) — no two
beats share visual content. Alternative "language" (a diagram) would abstract the
code away from what the viewer needs to see: the actual Python. Flagged for
Bear's human review before publication.

## Conclusion

Landscape 3840x2160 · 200.875s · H.264 + AAC. Every gate that exists in this toolkit
snapshot passed. Ten evidence stills were read individually and each confirms the
expected content. Human review pending.
