# SOURCES.md — Brutalist Command: art smoke — Short

Every claim shown or heard in this Short is anchored in the parent reel's
sources. The parent reel is `youtube/brutalist/claude-liam-brutalist-command-smoke/`
and the full-length native portrait is at `.../claude-liam-brutalist-command-smoke/vertical/`.

## Primary sources (unchanged from the parent long)

- `art` (the dispatcher script) — case `smoke)` at art:100-102, exec of
  `runtime/scripts/smoke_test.sh` forwarding `"$@"`. Referenced in narration
  (B08) as "one dispatcher case, no flags."
- `runtime/scripts/smoke_test.sh` — the actual pipeline described in B03:
  fixture copy → Kokoro narration → run.sh → three decoded gates (SIZE,
  TYPE, AUDIO). Quoted verbatim in the code card behind B03.
- `runtime/scripts/build_safety.py:186-187` — the slug regex
  `[A-Za-z0-9][A-Za-z0-9._-]*` whose refusal of `_smoke` is the failure
  reproduced in B07. Quoted verbatim in the code card.
- `examples/_smoke/beat_sheet.json` — the shipped fixture whose
  `slug: "_smoke"` field is what B07 shows being rejected.
- Verbatim runtime observations captured on the parent's workstation
  (`demo/RUN-LOG.txt` in the parent reel) — the `mean_volume: -24.2 dB`,
  `636229 bytes`, and `[exit $?] = 0` figures shown briefly inside the B07
  AFTER block.

## Parent evidence retained inside this Short

- `CUT-PLAN.json` — this Short's editorial record: strategy `whole-beat-cut`,
  focus, kept/dropped beat IDs with per-beat reasons, planned duration.
- `beat_sheet.json` — kept beats only (B00, B01, B03, B07, B08, B10) with
  each `shot.remotion.pattern` rewired to the `…916` portrait composition
  by shorts.py's Onda check. `metadata.kind: short`,
  `aspect_ratio: 9:16`, `voice_kokoro: am_onyx`, `captions: false`.
- `media/B<bid>.mp4` — six native portrait renders copied verbatim from the
  parent's `vertical/media/` (each was produced by the parent's remotion
  compositions).
- `mp3/beat-B<bid>.mp3` — six Kokoro `am_onyx` narration files copied
  verbatim from the parent's `vertical/mp3/`.

## Read-only leads (BRIEF.md; not used as this run's evidence)

- `rohan-v/2026-08-28-agent-first-brutalist/beat_sheet.json` — example only.
- `anjana-s/2026-08-21-ecis-explained/beat_sheet.json` — example only.

Neither example was quoted, copied, or re-signed. Both are leads for cut
strategy comparison only.

## Not sources

- No paid API, no upload, no publishing, no network calls, no fabricated
  human approvals.
- No new material was authored for this Short beyond CUT-PLAN.json,
  CHECKS-REPORT.md, TYPECHECK.md, VISUAL-REVIEW.json, README.md and this
  document itself.
