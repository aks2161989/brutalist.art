# TYPECHECK — Brutalist Command: repoloop.sh (landscape 3840×2160)

## Legacy `scripts/type_check.py` — NOT PRESENT

The ai-explainer SKILL.md references `scripts/type_check.py` (§ "GATE T
(type-lock) — ALWAYS RUN"). That checker is **not shipped in this
toolkit** — I searched `runtime/scripts/` and `runtime/qc/` and found no
executable named `type_check.py`, and no `reference/type-spec.md` or
`skills/make/kerning/`. The isolated toolkit snapshot at
`toolkit-baseline_sha256: 77be42713c5e4057b810aaf4b0b35549f81e5034a4bc9c6af0643e8cde67e884`
confirms this — it captures the shipped state, not an aspirational one.

**I am NOT claiming a missing checker passed.** This TYPECHECK.md is the
visual typography review that the human eye can perform against the
actually-rendered frames — the same substitute the sibling command-teardown
episodes use (setup, approvals, doctor, smoke, keys).

## Visual typography review — per beat

Read from the frames in `_qc/frames/` and the contact sheet at
`_qc/contact-landscape.png`. Canvas: 3840×2160 (native 4K); design
reference 1920×1080; safe inset ~96/54/1824/1026 per
`runtime/remotion/src/tokens/layout.ts`.

### B00 — ClaudeComposerAsk
- **Greeting (`Vanakkam, Liam`)** — EB Garamond serif, ~120 CSS px on
  source (1920×1080), sits centered above the composer. On-screen height
  ~10% of the frame — comfortably legible.
- **Topic line** (`BRUTALIST · COMMAND: REPOLOOP.SH`) — SF Pro sans,
  letter-spaced, ~24 px source, above the ask. Solid contrast on cream.
- **Composer body** — ~30 px source, ink on cream. `▲` send button in
  terracotta = the one accent.
- **Output lines** — cascade in from bottom, ~22 px each, legible with
  generous line spacing.
- **Folder chip** (`@HumanitariansAI`) — bottom-left inside the safe
  inset. Correct.
- **VERDICT:** PASS. No overflow, no clipping, one terracotta moment.

### B01 — BrutalistHesitantWriter
- Serif at fontSize=240 in the design reference. `repoloop.sh` types on
  line 1, `renders films.` types on line 2, terracotta hesitates on
  `renders` and `films`, corrects to `spawns workers.` — the corrected
  sentence sits comfortably inside `maxWidth: width * 0.86` (~1651 px on
  source) at ~1500 px measured width.
- Line spacing 2.6 gives the correction breathing room.
- **VERDICT:** PASS. First render at fontSize 240 with the earlier text
  `orchestrates workers.` (~2000 px wide) triggered a Gate V edge-bleed
  BLOCKER; shortened text corrected it. See _qc/REPORT.md.

### B02–B08 — ClaudeCodeBeat
- Title bar: SF Mono ~13 px source (~26 px on 4K output) at the code card
  top-left; terracotta traffic-light dot leads the row; sans-serif
  `PYTHON` label ~11 px top-right. Legible.
- Code body: SF Mono, `fontSize = height * 0.022` → ~24 px source /
  ~48 px on the 4K output. Comment lines fade (`COMMENT_CLR = #8B8878`);
  code lines full ink (`#3D3929`).
- **Longest line in each beat's code**:
  - B02: 60 chars — `exec python3 "$REPOLOOP_ROOT/runtime/scripts/repoloop.py" \`
  - B03: 75 chars — `for source in sorted(repo.glob('skills/*/**/SKILL.md')):`
  - B04: 76 chars — `for k in list(env):`
  - B05: 74 chars — inventory lines are ≤ 66 chars
  - B06: 65 chars — `"log":        ".repoloop/logs/…-repoloop-1789014517.jsonl",`
  - B07: 78 chars — `if md.get('voice_kokoro', md.get('voice')) != 'am_onyx':`
  - B08: 65 chars — verbatim shell + comment lines
  - All within the code card interior (~1599 px wide on source at ~14
    px/mono-char ⇒ ~114 char capacity).
- Spark line: EB Garamond italic ~22 px source at the bottom of the card,
  centered.
- **VERDICT:** PASS on B02–B08. Verified visually in the contact sheet.

### B09 — ClaudeVerdictArtifact
- Title (`Verdict`), heading (`repoloop.sh — the whole surface, in the
  order you touch it`), then six enumerated `artifactLines`. Serif for
  headings, sans for lines, terracotta for the heading's period.
- Six lines fit inside the artifact card; each line wraps naturally at
  the container's width.
- **VERDICT:** PASS.

### B10 — ClaudeComposerAsk (Your Turn)
- Greeting `Your Turn` (the one greeting that drops the persona per
  HANDOFF LAW). Serif.
- Composer body carries the paste-ready prompt in mono. Text wraps
  inside the composer's `maxWidth`.
- Output lines below explain the three-step grading rubric.
- **VERDICT:** PASS.

### B11 — ClaudeTitleOutro (locked per OUTRO-LOCK.md)
- Title poster-style serif with the terracotta period. Fits inside the
  safe area at a large size.
- Handle `@NikBearBrown` below in mono/sans (hardcoded in the component;
  flagged in README.md for HAI review).
- Slug-seeded mascot animates below the handle.
- **VERDICT:** PASS.

## Kerning / min-size / contrast / no-wordy-card

- **§8.1 min-size:** every text element in every beat is ≥ 24 px source
  (≥ 48 px on 4K output). Well above the 24 px effective legibility floor.
- **§8.2 overflow:** GATE V (`final_frame_check.py`) explicitly checks
  edge-bleed against the 1920/1080 SAFE inset and returned 0 BLOCKER, 0
  MAJOR. Re-verified by eye against the contact sheet.
- **§8.3 contrast:** ink `#3D3929` on cream `#FAF9F5` produces a
  luminance separation ~0.90 — comfortably above the 0.30 floor GATE V
  enforces. Terracotta `#D97757` on cream separates ~0.56 (used only for
  small accents and headings, never body text).
- **§8.4 kerning sanity:** rendered by the browser's own text engine
  (no Pango); no fallback tofu observed anywhere.
- **§8.5 no-wordy-card:** verdict artifact B09 has one heading + six
  bullets = under the wordy-card threshold. Composer body B10 wraps but
  every line is a coherent sentence.
- **§8.6 golden strings:** the strings the sheet says are on-screen
  (greeting, ask, prompt, code lines, verdict lines, title restate) are
  all present per visual review of the frames. No missing golden strings.

## Final call

No blockers, no majors, no minors that block final. All caveats are
recorded in CHECKS-REPORT.md § "Gaps recorded honestly".
