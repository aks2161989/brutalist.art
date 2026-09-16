# SOURCES — Brutalist Command: art help

## Primary source

- Path (isolated toolkit): `toolkit/art`
- Repo-relative path (public toolkit): `art`
- SHA-256 (this invocation): `387d12c338fe3e8e05a3c2202be86ea81beaf548c2fd11ec3ee4876694f8b562`
- Upstream URL: <https://github.com/nikbearbrown/brutalist.art>
- Ownership: Nik Bear Brown / Humanitarians AI

All narration claims about `./art help`, `./art -h`, `./art --help`, `./art`, `./art bogus`,
`./art --list`, and `./art <skill> --help` are verified against the exact case block at
`art:37-116` in this snapshot. See `FACTCHECK.md` for the row-by-row evidence.

## Demonstration outputs (captured in-workspace)

- `demo/RUN-LOG.md` — the verbatim stdout / stderr / exit codes of each command,
  captured 2026-09-09 against the isolated toolkit copy for this episode.
  This is the authoritative reference for the abbreviated code cards on screen.

## Example beat sheets consulted (as staging leads only)

Neither is republished; both are used only as reference for pacing and structure.

- `rohan-v/2026-08-28-agent-first-brutalist/beat_sheet.json`
  · SHA-256 `746409a8715e70aab6186145e963c08d088469b809b28fe39d44f5d8d06b1a22`
  · Title: "Your Weekly Video, Handled." (weekly-submission overview reel)
  · Used to observe the `Hi, Rohan` composer cold-open pattern and the
    numbered artifact-card verdict pattern that we mirror in B00 and B09.
- `mohammed-h/ai-data-engineering-etl/beat_sheet.json`
  · SHA-256 `cff8cb04882905936b4621f93db37f0ecc38b0b842e9d5a0a07f60e4f033ed2b`
  · Title: "ETL, Simplified" (data-engineering explainer)
  · Not used directly — kept as a comparison reference for pacing / narration
    budget on longer teardown beats.

Human signatures, private Drive URLs and personal contact details from the
originals are NOT reused. Only public patterns and structural leads were taken.

## Scenes used (all preloaded in the registered library)

- `ClaudeComposerAsk` (B00, B10) — landscape composer.
- `ClaudeComposerAsk916` (B00, B10 vertical) — portrait composer.
- `BrutalistHesitantWriter` (B01) — landscape hesitant writer.
- `BrutalistHesitantWriter916` (B01 vertical) — portrait hesitant writer, same
  component with the portrait design-box patch applied here in the isolated
  toolkit (`runtime/remotion/src/scenes/BrutalistHesitantWriter.tsx` — the
  landscape/portrait scale ternary).
- `ClaudeCodeBeat` (B02–B08 landscape) — code display card.
- `ClaudeCodeBeat916` (B02–B08 vertical) — portrait code card, newly registered
  in this workspace's `Root.tsx` (using the same `ClaudeCodeBeat` component at
  1080×1920, per REFLOW rule).
- `ClaudeVerdictArtifact` (B09 landscape) — verdict card. Font sizes and card
  width bumped inside the isolated toolkit for CANVAS-FILL compliance at 4K.
- `ClaudeVerdictArtifact916` (B09 vertical) — portrait verdict card. Font sizes
  bumped inside the isolated toolkit for portrait CANVAS-FILL compliance.
- `ClaudeTitleOutro` / `ClaudeTitleOutro916` (B11) — locked outro (per
  `OUTRO-LOCK.md`): `@NikBearBrown` handle hardcoded, slug-seeded mascot,
  no subline.

## Local dependencies

- Kokoro v1.0 ONNX (`kokoro-v1.0.onnx`, `voices-v1.0.bin`) at
  `~/Documents/CoWork/bear-textbooks/books/brutalist-art/runtime/models/kokoro/` —
  invoked via the workspace's `KOKORO_MODEL` / `KOKORO_VOICES` env vars.
- Chrome-headless-shell 149.0.7790.0 via `runtime/scripts/chrome_wrap.sh`
  (`--single-process --no-sandbox --disable-features=MojoIpcz`), needed to
  survive the Apple App Sandbox Mach-port block on this workstation.

No paid APIs. No uploads. No publication.
