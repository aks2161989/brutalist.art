# CHECKS-REPORT — Brutalist Command: art help (9:16 vertical companion)

Invocation `run_id = 48e0905963d54723ba7b587f9d86d97e` — 2026-09-12.
Previous build: `run_id = 8bd2a005d9984f9490ef7370c7bb2b2f` — 2026-09-09.
Re-compiled 2026-09-12: art source updated 2026-09-11 (godot-* dispatch added;
line numbers shifted). Vertical beats B03/B04/B07 were re-rendered 2026-09-11
with corrected line numbers; vertical video re-compiled with `--force`.
Slug: `claude-liam-brutalist-command-help-vertical`.

## Beat classification

12 / 12 SHOW · 0 HOLD · 0 PUNT (same beats as landscape, native portrait
compositions per beat).

## Teaching arc

Identical to landscape (see `../CHECKS-REPORT.md`); this cut is a native
portrait reflow, not a shortened Short.

## Portrait-specific decisions

- **B01 hesitant writer** — text was reshaped to a 4-line stack
  (`art help / lists / every / skill.`) and reduced to a single trigger swap
  (`skill → command`) so the correction lands well before the 50% Gate V
  sample point at 4.85s. Font size 210, lineSpacing 1.55, charMs 16 — chosen
  by direct pixel measurement to hit ≥55% bbox coverage of `SAFE916` at both
  the mid and late Gate V samples.
- **B09 verdict card** — font sizes bumped in
  `ClaudeVerdictArtifact916.tsx` to fill portrait's tall column.

## Runtime gates

- **Kokoro audio** — 12 / 12 beats copied from landscape (identical audio).
- **Remotion render** — 12 / 12 beats rendered natively at 1080×2048 through
  `remotion_scenes.py` → `--scale=2` → 2160×3840 native 4K portrait output.
- **compile.py** — verified encode, ran Gate V on candidate, only replaced
  the verified vertical master after clean pass.
- **Gate V** — final report (`_qc/REPORT.md`):
  ```
  Frames sampled: 24  ·  BLOCKER: 0  ·  MAJOR: 0
  Clean — no BLOCKER/MAJOR defects. ✓
  ```
- **Skin lint (non-fatal)** — compile.py logged two SKIN LINT warnings for
  `ClaudeComposerAsk916` (B00) and `ClaudeTitleOutro916` (B11), because its
  COLD OPEN and OUTRO LAWS check for the landscape `ClaudeComposerAsk` /
  `ClaudeTitleOutro` names by default. That is the correct behavior on a
  native portrait beat sheet — the 916 variants ARE the required cold open
  and outro for a 9:16 build. Flagged for human reviewer confirmation.

## Missing legacy checkers

`scripts/type_check.py` and `reference/type-spec.md` — not present in this
workspace. See `TYPECHECK.md`. Not silently passed.

## Frame evidence

- `_qc/REPORT.md` (auto Gate V, 24 sample frames, 0 BLOCKER 0 MAJOR)
- `_qc/contact_sheet_new.png` (5×3 contact sheet, 15 frames — B00/B01/B03/B09/B11
  at 15%/50%/85% each, from the 2026-09-12 re-compile)
- Sample per-beat frames in `_qc/frames_new/` (B00, B01, B03, B09, B11 measured
  directly against Gate V rubrics and Read via image tool).
