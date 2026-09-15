# SHOTLIST.md — Brutalist Command: art smoke — Short (9:16, 2160×3840)

Derived from `youtube/brutalist/claude-liam-brutalist-command-smoke/vertical/`
by whole-beat cut. Five middle beats dropped (see CUT-PLAN.json). Every kept
beat's native portrait video (`vertical/media/<bid>.mp4`) and Kokoro am_onyx
mp3 (`vertical/mp3/beat-<bid>.mp3`) was copied unchanged into this reel — no
re-render, no re-synthesis. The compiled Short measures 127.42 s (2:07.42),
well under the 180 s Shorts cap.

| Beat | Act | Pattern | Duration (s) | On-screen action |
|---|---|---|---|---|
| B00 | ASK | ClaudeComposerAsk916 | 9.67 | Composer types the ask; runningText 'running ./art smoke…'; three output lines cascade in. |
| B01 | BLUF | BrutalistHesitantWriter916 | 14.38 (+0.8 s lead) | Two-line hesitant writer: "art smoke / checks deps." → "art smoke / renders video." Triggers `checks→renders`, `deps→video`. |
| B03 | FRAMEWORK | ClaudeCodeBeat916 | 33.00 | Code card of smoke_test.sh's pipeline: scratch dir + Kokoro + run.sh + the three GATE lines. Spark line "Scratch dir. Real pipeline. Three decoded gates." |
| B07 | FAILURE_RECOVERY | ClaudeCodeBeat916 | 37.96 | Verbatim shipped-fixture failure output + the offending regex + the two one-line recoveries + the AFTER pass. Spark line "One char. Fixture blocked. Doctor still green. Fix: rename." |
| B08 | VERDICT | ClaudeVerdictArtifact916 | 27.17 | Artifact card: heading "art smoke — the whole surface, in the order you use it" + six numbered verdict lines. |
| B10 | OUTRO | ClaudeTitleOutro916 | 5.25 | Title restate "Brutalist Command: art smoke." + @NikBearBrown handle + slug-seeded mascot on dark ink polarity. |

Total actual duration (measured on the compiled mp4): **127.416667 s**.

## Legibility notes

- Every kept beat stays inside the shared SAFE916 inset (x 40-1040, y 192-1728
  at 1080×1920; scaled up to 2160×3840 for the final export).
- B01 uses the portrait-native BrutalistHesitantWriter916 recipe: serif face,
  centered, larger lineSpacing than landscape. Inspected frames B01_15/50/85
  show the correction lands cleanly (`checks` in terracotta at 15%, corrected
  `renders video.` in ink by 50%, held at 85%).
- All ClaudeCodeBeat916 cards use the shipped Onda-style code palette (ink on
  cream) with terracotta spark lines beneath. Code stays inside the card and
  the card stays inside the safe area at every sampled frame.
- B00 output-line cascade fits inside the composer/output stack without
  bleeding past the composer footer.

## Motion

- Every kept beat is a moving action (typing, hesitant correction, code
  cascade, artifact stagger, outro type-in). No static-slide beats.
- The three ClaudeCodeBeat916 beats (B03, B07) are differentiated by their
  content, sparkLine, and typing timing.
- OUTRO follows OUTRO-LOCK: hard-coded @NikBearBrown handle, slug-seeded
  mascot animation on dark ink polarity for the `smoke` slug.

## Audio

- Presenter: Liam (in for Bear). Engine: Kokoro. Voice: `am_onyx`.
- Every kept beat's mp3 is a byte-identical copy of the parent's
  `vertical/mp3/beat-<bid>.mp3` (six files: B00, B01, B03, B07, B08, B10).
- No captions. No burned-in subtitles.
- Compiled mp4 volumedetect: mean_volume −27.0 dB, max_volume −4.0 dB.

## Dropped beats

Whole-beat cut per CUT-PLAN.json — no rewrite:

- **B02** (FRAMEWORK — dispatcher case, 14.0 s)
- **B04** (MECHANISM — fixture body, 21.3 s)
- **B05** (MECHANISM — GATE AUDIO deep-dive, 25.5 s)
- **B06** (WORKED_EXAMPLE — verbatim pass path, 25.4 s)
- **B09** (YOUR_TURN — composer + read-the-script prompt, 25.0 s)

The 16:9 long and the full-length vertical retain every dropped beat.
