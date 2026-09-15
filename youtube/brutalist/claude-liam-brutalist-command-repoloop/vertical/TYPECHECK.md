# TYPECHECK — Brutalist Command: repoloop.sh (vertical 2160×3840)

## Legacy `scripts/type_check.py` — NOT PRESENT

Same finding as landscape: the ai-explainer SKILL.md's GATE T checker is
not shipped in this toolkit. I am NOT claiming a missing checker passed.
This document is the visual typography review substitute — the same
substitute the sibling command-teardown portrait episodes use.

## Visual typography review — per beat

Read from the frames in `vertical/_qc/frames/` and the contact sheets at
`vertical/_qc/contact_sheet.png` and `vertical/_qc/contact-vertical.png`.
Canvas: 2160×3840 (native 4K portrait); design reference 1080×1920; SAFE916
inset ~54/96/1026/1824 per `runtime/remotion/src/tokens/layout.ts`.

### B00 — ClaudeComposerAsk916
- Greeting `Vanakkam, Liam` reflows as a serif line under the topic strip.
- Composer body reflows to a narrower card that fills the portrait width.
- Output cascade sits under the composer, each line wrapping inside the
  safe width.
- Folder chip `@HumanitariansAI` present.
- **VERDICT:** PASS.

### B01 — BrutalistHesitantWriter916
- 5 lines at fontSize 155 / lineSpacing 2.2, cream `#FAF9F5` ground with ink
  `#3D3929` glyphs. The corrected sentence occupies ~90% of SAFE916 height
  and ~80% of SAFE916 width at the 85% sample point; the 50% sample already
  has the first four lines typed and clears the same floor.
- BrutalistHesitantWriter.tsx received the portrait-aware scale patch in the
  isolated toolkit (`height > width ? min(w/1080, h/1920) : min(w/1920,
  h/1080)`) — without it the component collapses to 0.5625× on portrait and
  no fontSize can clear the 55% coverage floor.
- Terracotta hesitation on `fellows`, backspace + retype to `workers` —
  final sentence `repoloop.sh is not a render loop. It spawns workers.`
- **VERDICT:** PASS.

### B02–B08 — ClaudeCodeBeat916
- Code card fills most of the portrait width. Title bar sits at the top of
  the card with terracotta traffic-light dot leading the row and `PYTHON`
  language label right-aligned.
- Code body uses SF Mono; `fontSize` is bound by min(base, height/lines,
  width/longest-line) — the adaptive-font patch shipped in the toolkit
  ensures long code snippets fit both landscape AND portrait cards without
  overflow (see [[feedback_claude_code_beat_adaptive_font]]).
- Every longest line inspected against the code card interior; all fit
  without horizontal clipping in the contact sheet.
- Spark line at the bottom of each code card is EB Garamond italic.
- **VERDICT:** PASS on B02–B08.

### B09 — ClaudeVerdictArtifact916
- Title and heading reflow to a taller portrait card. Six enumerated
  `artifactLines` each wrap naturally within the safe width.
- **VERDICT:** PASS.

### B10 — ClaudeComposerAsk916 (Your Turn)
- Greeting `Your Turn` breaks across two lines (`Read the repoloop queue —
  do / NOT start the loop`) above the composer, at a comfortable serif
  size. The `Your Turn` slot below sits on one line.
- Composer body carries the paste-ready prompt in mono; text wraps naturally
  inside the portrait-narrower composer maxWidth. Three-step rubric below
  the composer, `@HumanitariansAI` folderLabel visible.
- **VERDICT:** PASS.

### B11 — ClaudeTitleOutro916
- Title stacks on 3 lines (`Brutalist / Command: / repoloop.sh.`) with the
  terracotta period; sits centered inside the safe area.
- Handle `@NikBearBrown` below — hardcoded in the shipped component; flagged
  in README.md for HAI review. Same as every prior shipped Brutalist
  portrait episode.
- **VERDICT:** PASS on typography; handle deferred to human review.

## Kerning / min-size / contrast / no-wordy-card

- **min-size:** every rendered text element sits ≥ 24 px in the design
  reference (≥ 48 px on the 2160×3840 output).
- **overflow:** GATE V (`final_frame_check.py`) checked edge-bleed against
  SAFE916 and returned 0 BLOCKER, 0 MAJOR at both 50% and 85% samples.
- **contrast:** ink/cream separation ~0.90; terracotta accents only on
  small marks. Well above the 0.30 floor.
- **kerning sanity:** rendered by the browser text engine; no tofu.
- **no-wordy-card:** verdict card wraps but stays within the safe area on
  every line; composer bodies wrap coherently.

## Final call

No blockers, no majors, no minors that block final. Caveats recorded in
CHECKS-REPORT.md § "Gaps recorded honestly".
