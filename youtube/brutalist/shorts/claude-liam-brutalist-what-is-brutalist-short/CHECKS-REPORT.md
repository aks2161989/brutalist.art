# CHECKS-REPORT.md — What Is Brutalist? — Short

*Run 2026-09-08 UTC · run_id `ff2d6d603c3e46d79c7e06edab66781e`.
Isolated toolkit at
`.repoloop/shorts/workspaces/claude-liam-brutalist-what-is-brutalist-short/toolkit`,
reel at `youtube/brutalist/shorts/claude-liam-brutalist-what-is-brutalist-short`.
No new fabricated review — this report describes what was actually observed
in this cut.*

## Result

**PASS** — Short renders at 94.79 s (container, video and audio), well under
the 180.0 s cap, native 2160×3840, no captions, Liam sign-off intact, honest
not-list preserved.

## Decisions and evidence

1. **Cut plan authored before rewriting** — `CUT-PLAN.json` lists strategy
   `whole-beat-cut`, kept `[B00, B01, B04, B06, B07, B09]`, dropped
   `[B02, B03, B05, B08]` with per-beat reasons, planned duration `94.69 s`,
   `rewrite_reason: null`. No rewrite occurred; narration and audio are
   unchanged from the parent.
2. **`shorts.py --drop B02 B03 B05 B08 --no-endcard --no-outro-rewrite`**
   ran successfully. Six retained beats reported "native portrait reused
   unchanged" — no center-cut, no re-render, no regenerated audio.
   `short_validation.status = ready`.
3. **`compile.py --height 3840`** stamped `6/6 filled`, wrote
   `exports/short/claude-liam-brutalist-what-is-brutalist-short.mp4`.
4. **`ffprobe`** on the final file:

   | Stream | Duration | Detail |
   |---|---|---|
   | container | 94.791667 s | mp4 |
   | video | 94.791667 s | h264 · 2160×3840 |
   | audio | 94.791000 s | aac · 48000 Hz · 2ch |

   All strictly < 180.0 s; encoding headroom > 85 s.

## Frame evidence (real hashes, this run)

Contact sheet at `_qc/frames/f_%04d.jpg` (2 fps, 190 frames, 540×960 preview
scale). Beat-relative 15% / 50% / 85% frames extracted at native 1080×1920 in
`_qc/beat_frames/`.

| Frame | SHA-256 |
|---|---|
| `_qc/beat_frames/B00_015.jpg` | `18a09c09c468728e0fcf48dd4eda20edef2d69889f52a84e97061fa976fd3ce2` |
| `_qc/beat_frames/B00_050.jpg` | `39ec9890014327a17f67f714cf0a95afec986abf9ec516a07086d01c775fc608` |
| `_qc/beat_frames/B00_085.jpg` | `c028ba92e27a9e29fa66d5ad17bc2c10eec47e56a05d5e4aead8b5d02eb9711c` |
| `_qc/beat_frames/B01_015.jpg` | `bcd82abe67764b503db01e9d52cd2c47973c0df5149015ea897669d4cdf12a13` |
| `_qc/beat_frames/B01_050.jpg` | `ea43f00d11fc8598c872ccd37946a90f033a66bd8f22a5bf2af7bbbf0d76f522` |
| `_qc/beat_frames/B01_085.jpg` | `0a05dbe8eadf265616cda677136b3ac75224dadee2f9a8d83386fceae6e83590` |
| `_qc/beat_frames/B04_015.jpg` | `c45a7aad087d2d31857a12d72b3a0b1006bf5b11b784d1c629ef492aea11407a` |
| `_qc/beat_frames/B04_050.jpg` | `6b568120ce8234d8a936a373cbb68b917a31ead34e40d633754c0d1b52981625` |
| `_qc/beat_frames/B04_085.jpg` | `84a24f956d26374a339a99f60f09b33edc8bebb0bafac47c10efa2dabe5d2a84` |
| `_qc/beat_frames/B06_015.jpg` | `34b682ec5fe599c7436c4d0ec3c8d1197a53f85a76be796359704a877e7d2fbc` |
| `_qc/beat_frames/B06_050.jpg` | `6feb42e288afadb12b690ef0a77d665f3070fe05e7f3af1d7c773fcc82bf2e3b` |
| `_qc/beat_frames/B06_085.jpg` | `ad1745d7ea5de861ec5bbf2baec09a8c2f8c71b599a366dea2440c764a1759be` |
| `_qc/beat_frames/B07_015.jpg` | `eb9c7adebcf5651c315d65ff022be06563b7413377ef2c4c1c1676fb0e3aec75` |
| `_qc/beat_frames/B07_050.jpg` | `c984d7c0f67012b0d6e1c634e656d62303bc5381059106f371a47a7a0d970947` |
| `_qc/beat_frames/B07_085.jpg` | `df4004c5cf34656e4310bb0cee99740ea60e031ffda3bdb527501ee2db8edfe7` |
| `_qc/beat_frames/B09_015.jpg` | `327036bcce5244e026174ec0b1ea4c1af942e30bfc0a70d64157f7e0edfb3c28` |
| `_qc/beat_frames/B09_050.jpg` | `e910bf49ecb8e8276406235e4d990038673c53668192ad10885d34f577557a2c` |
| `_qc/beat_frames/B09_085.jpg` | `44fcbd3631ded7ecb54a25e4a2ebd5deabb23df9bb9a16538dfd213a3f991dd8` |
| `exports/short/claude-liam-brutalist-what-is-brutalist-short.mp4` | `319b16d67bf5d5284959fafc59594650d67419938f34182d8ec378b0891b2332` |
| `beat_sheet.json` (this Short) | `a9cfca5831462921a9c9c1100666f2b50215aa7550b50c43e5bb4ce3ad01d8c1` |

## Frame-by-frame observations

- **B00_015 / B00_050 / B00_085** — Cream page, portrait-safe eyebrow and
  title, "Ciao, Liam" greeting on centre, composer with the ask
  "Explain what Brutalist actually is…", `@HumanitariansAI` folder chip, the
  three concrete-output lines settle. No text bleeds past safe.x; no
  captions.
- **B01_015 / B01_050 / B01_085** — Serif type-on. `B01_015` catches the
  misconception mid-type ("Brutalist / is a / video / edi|"); `B01_050`
  shows the paused correction ("Brutalist / is a / video / recipe. /
  Actually, / text.") — `editor` has already been struck; `B01_085`
  holds the corrected line to camera.
- **B04_015 / B04_050 / B04_085** — Split card: JSON edit above (`"Ciao"`
  struck through), rendered composer below. `B04_015` shows the pre-edit
  state (Ciao / Italian "hello."); `B04_050` shows the swap in progress with
  `Hola` rendering and `remotion_scenes.py --only B00` under the code;
  `B04_085` shows the post-edit rendered composer (Hola / Spanish "hello.").
  The pure-function demonstration lands on-screen without the parent's
  additional B02/B03 anatomy.
- **B06_015 / B06_050 / B06_085** — Three stacked rows, terracotta accent on
  each "Not a …" heading, italic spark at the bottom
  ("The tool has a shape. That shape is the honesty."). Bodies wrap cleanly
  into two lines; safe area not violated top or bottom.
- **B07_015 / B07_050 / B07_085** — Artifact card with "Verdict" pill,
  heading "Film as code, in three lines.", numbered lines arrive on cue.
  Bottom italic reads "That is what Brutalist actually is."
- **B09_015 / B09_050 / B09_085** — Poster restate: `BRUTALIST · EPISODE 01`
  eyebrow with terracotta rule, title `What Is Brutalist?` (terracotta `?`),
  `@HumanitariansAI` handle, `LIAM, IN FOR BEAR.` at the bottom. Correct
  Humanitarians AI handle (not `@NikBearBrown`, per `OUTRO-LOCK.md`
  substitution).

## Audio join sanity

- Kokoro `am_onyx` throughout; no voice discontinuity.
- No B00→B01→B04 sequence introduces a dangling numbered reference (B01's
  "run the pipeline" resolves against B04's "re-render only beat zero").
- B04→B06 join: "one thing on screen changes." → "Now the honest part —"
  reads as natural continuation.
- B07→B09 join: "That is what Brutalist actually is." → "That was What Is
  Brutalist?" is the parent's intended sign-off pair; unchanged.

## Availability gaps carried from source

- `skills/make/explainer/SKILL.md` is not present in the isolated toolkit
  copy (the parent already flagged this). No Short-specific decision depended
  on it; the ai-explainer skill and REPOLOOP-SHORTS-PROMPT.md contain the
  applicable rules.

## Blockers / majors / minors

- **Blockers:** none.
- **Majors:** none.
- **Minors:** SKIN LINT warnings for `ClaudeComposerAsk916` and
  `WibOutro916` (see TYPECHECK.md) — both are expected and inherited from
  the parent's Claude-palette / native-outro substitution; not a Short
  regression.

## What was NOT altered

- Parent 16:9 master, parent 9:16 companion, parent `vertical/media/`,
  `vertical/mp3/` — untouched.
- Public toolkit — untouched (all edits stayed in the isolated toolkit
  workspace and this reel).
- Any prior finished Short exports elsewhere in `youtube/brutalist/shorts/`
  — not touched by this build.

## Approvals

`metadata.approvals.voice.status = pending`, carried from the parent 9:16
companion. **No approvals fabricated for this Short.**
