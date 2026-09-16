# CHECKS-REPORT — vertical — Brutalist Command: art run

Run against the isolated toolkit at
`.repoloop/workspaces/claude-liam-brutalist-command-run/toolkit`.
Original build: 2026-09-09. Re-rendered B02 on 2026-09-12 for run_id
`df4ab48ebf354eecb12e6a7d2316a270` — source_sha256 changed because the
`art` dispatcher `run)` case moved from lines 78-80 to 99-101 as the
`--list` section grew. B02 title updated; all other beats and audio unchanged.
Re-rendered B09 on 2026-09-12 for run_id `c1279719c5a743589fcfc4f9dc2a4468` —
vertical B09 clip was stale (still showed art:78-80 in verdict line 6); the
beat_sheet.json already had art:99-101 but the clip was not re-rendered when
landscape B09 was fixed. B09 re-rendered via C binary chrome wrapper
(`--disable-features=MojoIpcz` resolves Apple App Sandbox Mach-port block);
vertical recompiled and Gate V re-run: 0 BLOCKER / 0 MAJOR.
All commands local, no paid APIs, no upload.

## Re-render sandbox fix (2026-09-12)

Same fix as landscape: `npx remotion` resolved the globally-installed CLI,
bypassing the toolkit's patched `@remotion/renderer`. Fix: patched
`remotion_scenes.py` to invoke `node node_modules/@remotion/cli/remotion-cli.js`
directly; patched `toolkit/runtime/remotion/node_modules/@remotion/renderer/dist/open-browser.js`
to add `--single-process` on `darwin`. Visual inspection of
`_qc/b02_mid_vertical.png` confirms title bar reads `art:99-101` (long inline
comments still clip horizontally — documented portrait limitation of
`ClaudeCodeBeat916`; landscape master preserves full content).

## Gate F — paperwork present before final compile

Copies of the landscape paperwork are provided per the supervisor's
"both aspect directories require" clause:

- `FACTCHECK.md` — written (copied from landscape; still accurate).
- `SHOTLIST.md` — written (portrait beats mirror landscape ids and roles).
- `PROMPTS.md` — written.
- `SOURCES.md` — written.
- `BUILD-PROMPT.md` — supplied by the supervisor and preserved verbatim.
- `beat_sheet.json` — 12 beats, `*916` scene ids, valid JSON.

**Result: PASS.**

## Gate V — `final_frame_check.py` (portrait)

Ran against the compiled
`exports/vertical/claude-liam-brutalist-command-run-vertical.mp4`.
Sampled at every beat's 50% and 85% steady-state.

```
[gate-v] frames=24 BLOCKER=0 MAJOR=0
```

`_qc/REPORT.md`:

```
# Gate V — visual QC report

Frames sampled: 24  ·  BLOCKER: 0  ·  MAJOR: 0

Clean — no BLOCKER/MAJOR defects. ✓
```

**Result: PASS.** Iterated:

- **B01 hesitant writer portrait scale** — the shipped
  `BrutalistHesitantWriter.tsx` uses
  `Math.min(width/1920, height/1080)` as its design scale factor, which
  collapses to `0.5625` on the 9:16 canvas and cripples every font-size
  value. Patched to portrait-aware
  `height > width ? min(w/1080, h/1920) : min(w/1920, h/1080)`
  (documented in memory `feedback_brutalist_hesitant_writer_portrait_scale_patch`).
  The landscape branch is unchanged.
- **B01 wording + size after the scale fix** — settled at
  `"art run\nrenders\nthe master\nvideo file."`, `fontSize 180`,
  `lineSpacing 2.6`, single-token triggers `renders → compiles`,
  `master → review`. Final corrected sentence:
  "art run compiles the review video file." — still the reel's real
  claim.
- **B10 Your Turn composer** — shortened the paste-ready `command`
  and reduced `output` to 3 lines; the fuller 4-step task remains
  intact in the landscape B10.

## SKIN LINT (compile.py — kept intentional)

```
[art] SKIN LINT: B00: palette=claude but the cold open is 'ClaudeComposerAsk916' — COLD OPEN LAW wants ClaudeComposerAsk
[art] SKIN LINT: B11: palette=claude but the outro is 'ClaudeTitleOutro916' — OUTRO LAW wants ClaudeTitleOutro
```

Both are expected for a portrait cut — the `*916` variants ARE the
portrait implementations of COLD OPEN LAW and OUTRO LAW. The lint rule
in `compile.py` doesn't distinguish the aspect variant from the
non-portrait id; the on-screen behavior meets the law.

## Audio decode + duration match (portrait)

Identical narration to the landscape; regenerated on the portrait beat
sheet so the mp3 durations belong to the portrait scenes:

| beat | audio | narration |
|---|---:|---|
| B00 | 17.45 s | Ciao cold open |
| B01 | 17.22 s | hesitant writer BLUF (≥9s required) |
| B02 | 15.87 s | dispatcher case |
| B03 | 33.19 s | gate order |
| B04 | 22.36 s | audio + slot-skip |
| B05 | 16.26 s | Gate F output verbatim |
| B06 | 21.76 s | four knobs |
| B07 | 23.10 s | run vs final |
| B08 | 21.95 s | recovery |
| B09 | 28.67 s | verdict |
| B10 | 22.27 s | Your Turn |
| B11 | 5.23 s | outro |

Total = 245.33 s. Compiled master duration = 245.583 s.

## ffprobe — final container

```
Duration: 00:04:05.58, ...
Stream #0:0 Video: h264 (High), yuv420p, 2160x3840, ...
Stream #0:1 Audio: aac (LC), 48000 Hz, stereo, fltp
```

Native 4K portrait (2160×3840), h.264 + AAC.

## Gaps and unshipped checkers

- Same GATE T / `type_check.py` / `reference/type-spec.md` / `kerning`
  gap as landscape. Portrait-specific typography review is in
  `vertical/TYPECHECK.md`.
- **Known portrait limitation**: `ClaudeCodeBeat916` does not word-wrap
  long code lines; the horizontal margin clips. Gate V still passes
  (the card is inside SAFE916 — the clip happens inside the card, not
  at the frame edge), but fellows reading the raw script contents
  should prefer the landscape master. Documented, not concealed.

## Final compile (portrait)

```
[art] wrote exports/vertical/claude-liam-brutalist-command-run-vertical.mp4  (245.6s, ...)
[art] slots: 12/12 filled — B00:VIDEO B01:VIDEO ... B11:VIDEO
```

`claude-liam-brutalist-command-run-vertical.verified.json` written
alongside the mp4 with SHA-256 + input digests. Ready receipt in place.
