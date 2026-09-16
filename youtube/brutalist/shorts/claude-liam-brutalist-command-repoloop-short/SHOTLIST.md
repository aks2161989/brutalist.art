# SHOTLIST — Brutalist Command: repoloop.sh — Short (9:16 portrait, 2160×3840)

6 beats. Each is an independent copy of the parent vertical reel's native
2160×3840 Remotion render (no re-render, no crop). No manim, no captured media,
no slates, no endcard.

| Beat | Pattern | Motion | Audio (s) | Purpose in the Short |
|------|---------|--------|-----------|----------------------|
| B00 | `ClaudeComposerAsk916` | type-on | 11.07 | Cold open. Greeting `Vanakkam, Liam`. Introduces Liam in for Bear and poses the ask that motivates the loop. |
| B01 | `BrutalistHesitantWriter916` | hesitant-type | 11.80 | BLUF. Types `repoloop.sh / is not a / render loop. / It spawns / fellows.` → hesitates → replaces `fellows` with `workers`. Seed `repoloop-b01-vertical-v3`. |
| B05 | `ClaudeCodeBeat916` | code-cascade | 18.47 | WORKED_EXAMPLE. `./repoloop.sh --dry` verbatim excerpt — 56-film inventory abridged so viewers see the loop derives its list from the toolkit itself. |
| B09 | `ClaudeVerdictArtifact916` | artifact-in | 19.86 | VERDICT. Six-line artifact naming the whole surface (shim / discover / merge_queue / snapshot_toolkit / worker_settings + spawn / verify_film). Carries the fail-closed caveat. |
| B10 | `ClaudeComposerAsk916` | type-on | 26.82 | YOUR_TURN. Greeting `Your Turn`. Paste-ready prompt for the viewer to run `--dry` / `--status` and walk `merge_queue()`; forbids `--once/--forever/--start/--stop`. |
| B11 | `ClaudeTitleOutro916` | outro-card | 5.67 | OUTRO. Title `Brutalist Command: repoloop.sh.`, slug-seeded mascot. Handle hardcoded `@NikBearBrown` (see README.md for HAI review flag). |

Planned total (from `render_duration_s`): **93.83s / 1:33.8** — well under the
3:00 Shorts cap. Final measured container duration is recorded in
CHECKS-REPORT.md after compile.

## Dropped beats (from the 12-beat vertical parent)

- **B02** — three-line shim `ClaudeCodeBeat` (line-level bash anatomy; the
  verdict names the shim in one line).
- **B03** — repoloop.py `discover / merge_queue / build_one` code cascade
  (the verdict enumerates each phase in one line).
- **B04** — `worker_settings + worker_environment` sandbox walkthrough
  (the verdict states the sandbox contract and the ANTHROPIC_* strip).
- **B06** — `--status` live demo (overlaps with B05's `--dry` demo; one
  worked example is enough for a Short).
- **B07** — `verify_film` fail-closed guard cascade (the verdict already
  states the fail-closed refusal as this command's essential caveat).
- **B08** — recovery worked example on an unknown `--only` id (belongs in
  the long; Your Turn already sends viewers to run `--dry` themselves).

## Frame checks that must be true

- **Aspect:** every beat is a native 2160×3840 portrait render inherited
  from the parent vertical reel; no cropping, scaling, or re-render.
- **Fit:** `pad` — the compiler contains each clip inside the portrait
  frame without cropping.
- **Ground:** cream `#FAF9F5` on every beat (Claude palette).
- **Type:** EB Garamond serif in headings/spark lines; SF Mono for code;
  SF Pro / system sans for UI chrome.
- **Accent:** exactly one terracotta `#D97757` moment per beat.
- **Safe area (SAFE916):** all content sits inside the portrait 5% inset;
  each beat's per-beat portrait safe-area QC was verified in the parent's
  own `_qc/REPORT.md`.
- **Corner brand bug:** `ClaudeComposerAsk916` and `ClaudeCodeBeat916` do
  not render a corner logo bug by design. B11 renders the mascot per
  OUTRO-LOCK.md.
- **No captions:** no `.srt`, no `.vtt`, no burned-in transcript.
  `metadata.captions: false`.

## Timing sanity

Every kept beat's `show[]` events are the same fractions in `[0.0, 1.0]` of
its own audio window as in the parent vertical. `compile.py` conforms clip
durations to `actual_duration_s` so a `"at": "0.55"` event lands at 55% of
that beat's measured audio duration. Because the mp3s were copied unchanged
from the parent (bit-identical), reveal timing is identical to the source.
