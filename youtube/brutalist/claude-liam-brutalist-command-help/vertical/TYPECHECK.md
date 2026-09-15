# TYPECHECK — Brutalist Command: art help

## Runtime typography checker

- `runtime/scripts/type_check.py` referenced in the public docs — **NOT
  present** in this isolated workspace's `runtime/scripts/` directory.
- `reference/type-spec.md` — **NOT present** in this workspace.
- The legacy GATE T therefore did not run in this session. This is recorded
  honestly — not a claim of pass.

## Actual typography review performed

For each finished export I extracted per-beat frames at 50% and 85% of each
beat's span, opened them via the image-capable Read tool, and audited the
following rubric against the Brutalist standards documented in
`CLAUDE-BRAND.md` (§Type) and `CLAUDE-CODE-VISUAL-QC-CHECK.md` (§8.1–§8.6):

- **8.1 min-size** — every essential glyph reads clearly at the 4K native
  resolution. Serif greeting `Namaste, Liam` uses `EB Garamond` (bundled),
  size scales with viewport height. Code cards use `SF Mono / Menlo` fallback
  at `height * 0.022` = ~48px at 2160 native. All well above the ~24px floor.
- **8.2 overflow** — Gate V (`_qc/REPORT.md`) confirms zero edge-bleed and
  zero clipped content across 24 sampled frames per aspect. Every line either
  wraps within its container's `maxWidth` (variable-length copy) or fits in
  its designed column (short spark lines, header labels).
- **8.3 contrast** — INK (`#3D3929`) on PAGE (`#FAF9F5`) — luminance
  separation well above the CONTRAST_MIN threshold used by Gate V (no
  low-contrast defects raised). Terracotta accent (`#D97757`) is used only
  for the ONE moment per beat as required by ACCENT LAW.
- **8.4 kerning sanity** — the shipped serif is `EB Garamond`; no proprietary
  Tiempos fallback was requested. Visual review of the composer greeting
  (`Namaste, Liam`), the outro title (`Brutalist Command: art help.`) and
  the verdict card heading shows no visible Pango-fallback kerning glitches.
- **8.5 no-wordy-card** — the verdict card at B09 has 4 numbered lines
  averaging 12 words each; well within the readability envelope. The Your
  Turn composer at B10 has a longer prompt block (paste-ready), which is
  allowed by HANDOFF LAW because the narration reads it aloud.
- **8.6 golden strings per frame** — Title in B00's segment reads `art help`;
  outro title in B11 reads `Brutalist Command: art help.` verbatim — the two
  golden strings the episode is required to carry.

## Terracotta discipline

Per-beat audit — one terracotta focal moment per beat:

| Beat | Terracotta element |
|---|---|
| B00 | send button + world-hello spark line under output |
| B01 | the trigger word (`skill`) about to be replaced |
| B02–B08 | active traffic-light dot on the code card; MONO language tag |
| B09 | numbered digits (`1. 2. 3. 4.`) |
| B10 | send button on the composer |
| B11 | slug-seeded mascot (or ink polarity for dark bg) |

No beat has two competing terracotta subjects.

## Conclusion

Every applicable §8 typography rule was verified by direct frame inspection.
The absent legacy `type_check.py` and `reference/type-spec.md` are explicitly
noted here; no other check was skipped, and no fabricated pass is claimed.
Human review pending.
