# CHECKS-REPORT — Brutalist Command: art --list (9:16 Short)

Invocation `run_id = 4b6e445b538846a4aa2b96c4dc361331` — 2026-09-12.
Slug: `claude-liam-brutalist-command-list-short`.
Derived from parent `claude-liam-brutalist-command-list-vertical`
(parent master SHA-256
`77351a7c1e0b79dc268d2968dd6fbc4e2f37504651b205a189a201742d6eab25`,
parent source `beat_sheet.json` SHA-256
`d0f66c7a93173203ef76f94e5395625f55cbfdfa2386abfef9a786d2b1c9c8e4`).

Rebuild reason: parent expanded from 16 to 20 skills (godot-waikthrough,
godot-gamedev, godot-gdd, riff added). Narration and visuals updated throughout;
old Short (2026-09-09, 126.625 s) preserved until this replacement passed gates.

## What this Short is

A **whole-beat cut** of the parent vertical companion. 8 beats retained
(B00, B01, B03, B04, B07, B08, B09, B11); 4 dropped (B02, B05, B06, B10)
per `CUT-PLAN.json`. **No narration rewrite. No new render.** Every retained
beat's rendered mp4 and mp3 were copied from the parent unchanged.

Final export:
`youtube/brutalist/shorts/claude-liam-brutalist-command-list-short/exports/short/claude-liam-brutalist-command-list-short.mp4`

- Container: 127.791 s · 2160×3840 · h264 24 fps · 7.7 MB
- Video stream: 127.791 s · 2160×3840 (h264)
- Audio stream: 127.791 s · aac 48 kHz
- SHA-256: `ffb8c57fe61a1ae68750f864ef7f9cb4d47279819134a9d4b4c56534036cdb79`

## Cut plan

- `python3 runtime/scripts/shorts.py <parent>/vertical --output-dir <reel> --slug <slug> --drop B02 B05 B06 B10 --no-endcard --no-outro-rewrite`
- shorts.py reported `8 beats · ~127.8s (2:07.8) OK`.
- All 8 kept beats hit the "native portrait reused unchanged" path (parent
  media confirmed 2160×3840 by ffprobe on B00.mp4).

## Runtime gates

- **Duration cap** — 127.791 s measured on the container (video 127.791 s,
  audio 127.791 s). Cap is strictly under 180 s; **52.2 s of headroom**. Passes.
- **`shorts.py` short_validation** — `{"status": "ready", "errors": []}`.
- **`compile.py`** — 8 / 8 filled, all VIDEO slots. Audio per-beat timeline
  (source audio preserved). Wrote MP4 with atomic verification.
- **Gate V** — `final_frame_check.py` returned `frames=16 BLOCKER=0 MAJOR=0`.
- **Audio decode** — final container audio stream present, aac, same duration
  as video. Per-beat mp3s copied unchanged from parent.
- **Motion histogram** — `code-cascade:4  type-on:1  hesitant-type:1
  artifact-in:1  outro-card:1`. compile.py logged a non-fatal warning:
  code-cascade at 4/8 = 50% (parent was 6/12 = 50%; cut preserved the
  balance, did not worsen it). Not a blocker.
- **Skin lint** — same two non-fatal warnings the parent already carried:
  `B00 ClaudeComposerAsk916` and `B11 ClaudeTitleOutro916` under
  `palette=claude`. These are 916 twins of the base compositions, both
  approved for portrait in the parent. Not new to this Short.
- **Frame checks** — Beat-relative 15% / 50% / 85% samples for all 8 beats
  (24 total) freshly extracted from this invocation's compiled mp4 and written
  to `_qc/frames_beat`, each with a current SHA-256 in `VISUAL-REVIEW.json`.

## Visual inspection (multimodal frame Read)

- **B00-50** — ClaudeComposerAsk916 card shows updated output: "prints a
  21-line skills table (1 header + 20 skills)". Composer, greeting, folder
  chip, and response lines all inside SAFE916. Cream ground, terracotta
  runningText accent. Clean.
- **B01-50** — BrutalistHesitantWriter916 post-correction state: "art --list
  prints / the catalog / of our / Brutalist / toolkit here." with caret. Large
  serif fills safe area vertically with lineSpacing 2.4. Clean.
- **B03-50** — ClaudeCodeBeat916 code card "art:58-80 — the --list body":
  "# 21 printf calls. 1 header + 20 sk..." visible, godot-waikthrough,
  godot-gamedev, godot-gdd, riff entries visible. Right-edge bleed on wide
  code lines (known parent characteristic; leading tokens inside safe area).
  SparkLine "21 printfs. No lookup." Clean.
- **B09-50** — ClaudeVerdictArtifact916 verdict card: all 7 numbered items
  readable; first line reads "a printer of a hand-typed 21-line table (1
  header + 20 skills)". Inside SAFE916. Clean.
- **B11-50** — ClaudeTitleOutro916 outro: "Brutalist Command: art -- list."
  with terracotta dot, "@NikBearBrown" handle below; all inside SAFE916. Clean.

## Coherence of joins

Retained order B00 → B01 → B03 → B04 → B07 → B08 → B09 → B11 keeps the
teaching arc intact:

- B00 introduces the two claims (aliases share a branch; branch is a
  printer of a hand-typed table of twenty skills).
- B01 BLUF corrects `runs the skills` → `prints the catalog`, twenty rows.
- B03 shows the actual body (21 printfs, godot-* and riff highlighted,
  no lookup, no scan).
- B04 shows the verbatim 21-line output (four godot skills + riff noted)
  and exit 0.
- B07 falsifies — the near-miss `./art -list` exits 2 with a hint on stdout.
- B08 recovery arc — `./art --list` then `./art <skill> --help`.
- B09 verdict summarises the split: twenty skills, extras ignored, recovery.
- B11 outro sign-off.

## Blockers / majors

- Blockers: **0**.
- Majors: **0**.

## Limitations

- **Human review pending.** No human viewing signature was applied.
- **No paid API used, no upload, no publish.** Output is a local file only.
- **Skin-lint 916-twin warnings** carried from the parent (see above).
- **Code-card horizontal bleed** carried from the parent (see above).

## Non-actions (safety)

- Parent vertical/media and mp3 files are untouched.
- No changes to the toolkit, the public `runtime/remotion/`, or any other
  reel's `exports/`.
- No git commit, push, publish, or scheduling side effect.
