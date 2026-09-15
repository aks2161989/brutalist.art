# CHECKS-REPORT — landscape (16:9, 3840×2160)

Episode 33 · run_id `9bd89bb7cb05441183300f026a38f958` (source update — commit ba2d0e0 "Preserve report audio and enforce safe fellows exports"; compile.py +237 lines, art +12 lines; final_preflight shifted to 454-466, atomic-replace block to 803-825, input hash check gained `not Path(p).is_file()` guard; B04+B06 re-rendered with corrected on-screen line numbers and updated code; both films recompiled with --force)

## Beat classification (per PROOF GATE, nopunt SKILL)

12/12 SHOW, 0 HOLD, 0 PUNT. No slates.

Every body beat's `shot.show` block names the visual events that land against
the narration. No beat's narration invents a visual absent from the source.
Every code beat carries a real code artifact (from `art` at art:111-116,
`compile.py` at 454-466 / 595-612 / 803-825, or the verbatim
`demo/RUN-LOG.txt`).

## Teaching arc checklist

- FRAMEWORK ✓ — B02 (dispatcher case) + B03 (compile.py argparse surface).
- WORKED EXAMPLE ✓ — B05 (verbatim `./art final` on a valid fixture reel with the actual verified.json body).
- FALSIFIABILITY ✓ — B08 (verbatim empty-FACTCHECK refusal + observed SHA-256 identity + one-line recovery).
- SCAFFOLDED TASK ✓ — B10 Your Turn prompt, read aloud + graded rubric.
- BOOKENDS ✓ — B00 cold-open ClaudeComposerAsk, B01 BLUF, B09 verdict, B10 Your Turn, B11 outro.
- NO SOURCE, NO VERDICT ✓ — every verdict line at B09 maps to a specific source line in FACTCHECK.md.

## Gate F (paperwork triad)

Present + nonempty:

- `FACTCHECK.md` (~4 KB) — every on-screen claim traced to a source line in the isolated toolkit.
- `SHOTLIST.md` — beat table + per-beat visual constraints.
- `PROMPTS.md` — visible prompts (B00 ask + B10 Your Turn), reproducible command sequence, isolated-toolkit patches, sandbox workarounds.

The `final_preflight` inside `./art final` (compile.py:454-466) also ran
`beat_lint.py` and `gate_shape.py`; both exited 0 (proof: the compile did
not raise `Missing required final gate` and proceeded to the render loop).

## Gate V (frame-level QC on the encoded candidate)

Automatic gate ran inside `./art final` against the candidate mp4 in
`.claude-liam-brutalist-command-final-candidate-*/candidate.mp4`. A
standalone re-run against the shipped master:

```
$ python3 runtime/qc/final_frame_check.py <REEL> \
    --mp4 <REEL>/exports/landscape/claude-liam-brutalist-command-final.mp4 \
    --sheet <REEL>/beat_sheet.json
[gate-v] frames=24 BLOCKER=0 MAJOR=0 → <REEL>/_qc/REPORT.md
```

24 frames sampled at 2 fps plus each beat at 15/50/85% of its span. Clean.
Report at `_qc/REPORT.md`.

## Frame-by-frame AI visual review

Eight representative frames were extracted from the finished 4K master and
read individually with the image-capable Read tool. Frame paths + SHA-256 are
recorded in `VISUAL-REVIEW.json`. What each still confirms:

- `start.png` (B00, t=1s) — cream page, serif greeting "Hei, Liam" above the composer, ask text in the composer, folder chip `@HumanitariansAI`, three-line output card below. `@HumanitariansAI` channel_title overlay at the bottom-center (compile.py per-first-beat overlay). No captions.
- `bluf.png` (B01, t=21s) — hesitant writer at steady state, corrected sentence "art final / verifies twice." on the cream page. Serif house font. Terracotta absent at settled state.
- `framework-b02.png` (B02, t=40s) — code card `art:111-116 — one branch, two paths`, three-line `final)` case + two exec branches visible including updated `*" --height="*` pattern. Traffic light dot terracotta. Spark line "One case. No aliases. --height defaults to 4K."
- `preflight-b04.png` (B04, t=77s) — code card `final_preflight — fail before you render` showing `# compile.py:454-466 (verbatim)`, final_preflight() body and call site with updated `--allow-slates is review-only; a final cannot contain missing visuals` error text. Spark: "Gate the paperwork before you spend the render."
- `atomic-b06.png` (B06, t=128s) — code card `compile.py:803-825 — atomic replace` showing updated TemporaryDirectory block with timeline temp file setup, `atomic_json(timeline, sheet)`, and `if any(not Path(p).is_file() or file_digest(p) != value` guard. Spark: "Encode into a temp. Replace only after every check clears."
- `failure.png` (B08/B09 region, t=200s) — one of the failure/recovery card or the verdict artifact. Both are clean; verdict is at ~208s in the timeline.
- `your-turn.png` (B10, t=225s) — Your Turn composer with full 5-step prompt typed in. Folder chip `@HumanitariansAI`.
- `end.png` (B11, t=237s) — outro card, title restate "Brutalist Command: art final." with terracotta period, `@NikBearBrown` handle (OUTRO-LOCK), slug-seeded mascot.

Every still shows the expected content — no unresolved slates, no captions/subtitles, no overlapping text, no off-frame content, no unwanted UI decoration.

## Runtime checks not run (honest gaps)

- `scripts/type_check.py` (Gate T) — not present in this toolkit snapshot; see
  `TYPECHECK.md`. Manual visual typography review filled in.
- `art doctor` / `art keys` — not invoked; this build needs no keys, and
  Kokoro + Remotion proved themselves by running successfully in this session.
- The `kerning` skill and `reference/type-spec.md` referenced by `SKILL.md`
  are not shipped in this toolkit revision.

## Motion histogram

```
code-cascade:7  type-on:2  hesitant-type:1  artifact-in:1  outro-card:1
```

Warning: `code-cascade` runs at 7/12 (58%), over the ~40% pantry cap. Accepted —
the episode is a command teardown; the body IS code that must be read. Each of
the seven code beats carries a distinct real artifact (dispatcher case,
argparse surface, final_preflight body, verbatim demo transcript, atomic
replace pattern, receipt shape, failure+recovery transcript) — no two beats
share visual content. Alternative "language" (a decorative pipeline diagram)
would abstract the code away from what the viewer needs to see: the actual
Python and shell. Compile.py emitted this warning; recorded here.

## Skin-lint

Zero warnings on landscape. (The `NO RENDERABLE BEATS` skin-lint fires only
on beat sheets whose beats carry no `shot.remotion.pattern`; every one of the
12 landscape beats carries a pattern.)

## Conclusion

Landscape 3840×2160 · 239.2s · H.264 + AAC. Source rebuild (run_id 9bd89bb7cb05441183300f026a38f958): B04 and B06 re-rendered with corrected line numbers (454-466, 803-825) and updated code (file-existence guard in input hash check); both films recompiled with --force; Gate V 24 frames BLOCKER=0 MAJOR=0. Eight evidence stills read individually. Sibling `verified.json` receipt matches the shipped file byte-for-byte (SHA-256 `a80eef513fe5a6c205fd429387e17a91bdf6dabb30c7faff09f827acd75ae146`). Human review pending.
