# CHECKS-REPORT — vertical (9:16, 2160×3840)

Episode 33 · run_id `9bd89bb7cb05441183300f026a38f958` (source update — commit ba2d0e0; B04+B06 ClaudeCodeBeat916 re-rendered with corrected line numbers 454-466/803-825 and updated code; vertical recompiled with --force)

## Beat classification (per PROOF GATE)

Same 12 beats as landscape, rewired to `*916` scene ids by `art vertical` and
re-rendered natively at 2160×3840. `channel_title` metadata deliberately
omitted on portrait per `feedback_channel_title_portrait_bleed` — the wordmark
overlay would extend past SAFE916 on portrait aspect and trip Gate V. Landscape
carries it; portrait does not.

## Teaching arc checklist

Identical to landscape (FRAMEWORK ✓, WORKED EXAMPLE ✓, FALSIFIABILITY ✓,
SCAFFOLDED TASK ✓, BOOKENDS ✓, NO SOURCE, NO VERDICT ✓). B10 Your Turn
prompt was shortened to fit the portrait composer's narrower width (segment
title trimmed to "Verify your export against its receipt"; 5-step body
compressed to 4 steps; output list trimmed from 3 lines to 2). The
verification workflow is unchanged.

## Gate F (paperwork triad)

`FACTCHECK.md`, `SHOTLIST.md`, `PROMPTS.md` copied from landscape and still
accurate for this aspect (no portrait-specific claim). Nonempty, all present.

## Gate V (frame-level QC on the encoded candidate)

Ran inside `./art final` against the vertical candidate mp4:

```
$ python3 runtime/qc/final_frame_check.py <REEL>/vertical \
    --mp4 <REEL>/exports/vertical/claude-liam-brutalist-command-final-vertical.mp4 \
    --sheet <REEL>/vertical/beat_sheet.json
[gate-v] frames=24 BLOCKER=0 MAJOR=0
```

24 frames sampled. Clean.

### Portrait iteration history (for the record)

Gate V required three passes to reach clean on the BLUF beat:

1. **B01 fontSize 130 / lineSpacing 2.6** → underfill 19% (below the 55% floor).
2. **B01 fontSize 260 / lineSpacing 3.0** → edge-bleed top/bottom (stanza too tall).
3. **B01 fontSize 230 / lineSpacing 2.5** → clean.

Also caught the first pass: B10 (Your Turn) portrait composer had the 3rd
output line running past SAFE916.b — trimmed to 2 output lines + shortened
command; passed the second pass. Everything else compiled clean on first pass.

## Frame-by-frame AI visual review

Eight representative frames extracted from the finished 4K vertical master and
read individually. Frame paths + SHA-256 recorded in `VISUAL-REVIEW.json`.
What each still confirms:

- `start.png` (B00, t=1s) — portrait cream page, greeting "Hei, Liam" in serif above the composer, ask fills a comfortable multi-line composer card, folder chip `@HumanitariansAI`. Output cascade beneath.
- `bluf.png` (B01, t=6s) — 3-line serif stanza "art final / verifies / twice." filling portrait safe area at fontSize 230 / lineSpacing 2.5. Terracotta caret at rest.
- `framework-b02.png` (B02, t=44s) — `art:111-116` code card (corrected from art:90-95; art file grew with new skills). Long lines truncate at the card's right edge in portrait — the ink stays inside the card so Gate V passes; the salient part of every line (`case`, `final)`, `--height` check, `exec python3 …compile.py "$@"`) is readable. Full lines visible in landscape master + preserved verbatim in FACTCHECK.md and demo/RUN-LOG.txt.
- `worked.png` (B05, t=100s) — verbatim `$ ./art final /tmp/…-demo …` transcript. Same portrait truncation on long stdout / verified.json lines; the identifying data (command shape, `[exit 0]`, `verified.json` keys) is legible.
- `mechanism-b06.png` (B06, t=126s) — `compile.py:800-822` atomic-replace pattern (corrected from 805-827). Same portrait truncation caveat.
- `failure.png` (B08 region, t=200s) — one of the failure/recovery or verdict cards. Same truncation caveat.
- `your-turn.png` (B10, t=225s) — portrait Your Turn composer. Full shortened 4-step prompt visible, 2 output lines below.
- `end.png` (B11, t=237s) — outro card, title "Brutalist Command: art final." wraps to 3 lines in portrait, terracotta period on `final`, `@NikBearBrown` handle beneath, mascot at fixed pixel-art size.

## Known limitation — portrait code beats

Long monospace code lines in the portrait `ClaudeCodeBeat916` beats (B02-B08)
truncate at the white card's right edge. The card itself is inside SAFE916 so
Gate V passes; the salient part of every line is legible in the frame. **Full
lines are preserved verbatim in the landscape master and in
`demo/RUN-LOG.txt`.** Same behaviour shipped in eps 29 (`art run`), 30
(`art shorts`), 31 (`art vertical`), 32 (`art approvals`). Documented, not
suppressed. Fellows reading raw code should prefer the landscape master.

## Skin-lint

Two expected warnings on portrait, both matching the ep 29-32 pattern:

```
B00: palette=claude but the cold open is 'ClaudeComposerAsk916' — COLD OPEN LAW wants ClaudeComposerAsk
B11: palette=claude but the outro is 'ClaudeTitleOutro916' — OUTRO LAW wants ClaudeTitleOutro
```

The linter checks the shipped landscape scene names; portrait uses the `916`
suffixed native variants (registered in Root.tsx). Same code, portrait wrapper.
Not a defect — expected warning for `art vertical` builds.

## Motion histogram

Same as landscape: `code-cascade:7 type-on:2 hesitant-type:1 artifact-in:1 outro-card:1`. Warning about `code-cascade` over the ~40% cap accepted for the same reason (see landscape CHECKS-REPORT).

## Conclusion

Vertical 2160×3840 · 239.2s · H.264 + AAC. Native portrait layout (not upscaled crop of landscape). Source rebuild (run_id 0a9fea2f48c44753a0f1e81f0f6c1c60): B02 and B06 re-rendered with corrected on-screen titles (art:111-116, compile.py:800-822). Gate V clean. Sibling `verified.json` matches the shipped file byte-for-byte (SHA-256 `36fd564ca9b149826f47ee65e72792458aa19d9a0dbaf524e7dca1d86011fe4c`). Human review pending.
