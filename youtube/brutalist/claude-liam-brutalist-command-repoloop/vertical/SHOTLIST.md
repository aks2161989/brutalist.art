# SHOTLIST — Brutalist Command: repoloop.sh (16:9 landscape, 3840×2160)

12 beats. All 12 rendered via `runtime/scripts/remotion_scenes.py`, then
conformed to per-beat measured audio by `runtime/scripts/compile.py`. No
manim, no human media, no slates.

| Beat | Pattern | Motion | Actual audio (s) | Purpose |
|------|---------|--------|------------------|---------|
| B00 | `ClaudeComposerAsk` | type-on | 11.07 | Cold open. Greeting `Vanakkam, Liam`. Ask + `runningText: planning the queue…` + three answer lines. Narrator introduces Liam in for Bear. |
| B01 | `BrutalistHesitantWriter` | hesitant-type | 12.14 | BLUF. Types `repoloop.sh / builds videos.`, corrects to `orchestrates workers.` on the two terracotta words. Seed `repoloop-b01`. `lead_silence_s: 0.8` in beat sheet. |
| B02 | `ClaudeCodeBeat` | code-cascade | 13.99 | FRAMEWORK. The 3-line bash shim `repoloop.sh` verbatim + explanation of `REPOLOOP_ROOT`. |
| B03 | `ClaudeCodeBeat` | code-cascade | 22.89 | FRAMEWORK. `discover()` inventory sketch + `merge_queue()` pending-on-change logic + the drain loop. |
| B04 | `ClaudeCodeBeat` | code-cascade | 25.47 | FRAMEWORK. `worker_settings()` allow/deny block + `worker_environment()` env-var strip. |
| B05 | `ClaudeCodeBeat` | code-cascade | 18.47 | WORKED_EXAMPLE. `./repoloop.sh --dry` output — 56-film inventory abridged for legibility, final total line kept. |
| B06 | `ClaudeCodeBeat` | code-cascade | 16.34 | WORKED_EXAMPLE. `./repoloop.sh --status` verbatim — the `building` item is THIS reel. |
| B07 | `ClaudeCodeBeat` | code-cascade | 29.06 | MECHANISM. `verify_film()` fail-closed conjunct: every `raise BuildError(...)` shown. |
| B08 | `ClaudeCodeBeat` | code-cascade | 19.39 | FAILURE_RECOVERY. Verbatim run: `./repoloop.sh --only totally-fake-id --dry` → `Unknown --only ID`. Recovery via `--dry`. |
| B09 | `ClaudeVerdictArtifact` | artifact-in | 19.86 | VERDICT. Six-line artifact: shim / discover / merge_queue / snapshot_toolkit / worker_settings+spawn / verify_film. |
| B10 | `ClaudeComposerAsk` | type-on | 26.82 | YOUR_TURN. Greeting `Your Turn`. Paste-ready prompt. Explicit forbids on `--once/--forever/--start/--stop`. |
| B11 | `ClaudeTitleOutro` | outro-card | 5.67 | OUTRO. Title `Brutalist Command: repoloop.sh.`, slug-seeded mascot. Handle hardcoded `@NikBearBrown` (see README.md for HAI review flag). |

Total: **220.28s / 3:40**.

## Frame checks that must be true

- **Aspect:** every beat renders at 3840×2160 (Composition width×height 1920×1080 × Remotion `--scale=2`).
- **Fit:** `contain` — the compiler never crops content off the safe area.
- **Ground:** cream `#FAF9F5` from the Claude palette on every beat.
- **Type:** EB Garamond serif in headings/spark lines; SF Mono for code
  bodies; SF Pro / system sans for UI chrome.
- **Accent:** exactly one terracotta `#D97757` moment per beat (spark,
  send button, active traffic-light dot, terracotta correction word,
  terracotta artifact heading).
- **Legibility floor:** `ClaudeCodeBeat` uses `fontSize = height * 0.022`,
  i.e. ~24 CSS px on the 1920×1080 source, ~48 px on the 3840×2160 output.
  Longest line in any code beat ≤ 78 monospace chars — comfortably inside
  the ~114-char code-card width.
- **Safe area:** all content sits inside the 5% title-safe inset via
  `runtime/remotion/src/tokens/layout.ts` helpers used by every Claude
  scene. Verified per beat in `_qc/REPORT.md` after render.
- **Corner brand bug:** `ClaudeComposerAsk` and `ClaudeCodeBeat` do not
  render a corner logo bug by design — the composer's folder chip
  (`@HumanitariansAI`) is the channel wordmark on those cards. B11 shows
  the mascot full-size per OUTRO-LOCK.md.
- **No captions:** no `.srt`, no `.vtt`, no burned-in transcript
  anywhere. `metadata.captions: false`.

## Shot.show timing sanity

Every beat's `show[]` events are expressed as fractions in `[0.0, 1.0]`
of that beat's audio window. compile.py conforms clip durations to
`actual_duration_s` (see the mp3/timings map), so a `"at": "0.55"` event
lands at 55% of the measured audio duration. Reveals were authored so
each event lands ON or JUST AFTER the spoken phrase that names it.
