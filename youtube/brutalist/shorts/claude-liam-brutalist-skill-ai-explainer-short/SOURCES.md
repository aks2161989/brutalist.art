# SOURCES — Short cut

Every claim on screen or in the retained narration traces to one of two
primary sources, both read in the isolated per-invocation toolkit copy.

## Primary — read for THIS Short

- `skills/make/ai-explainer/SKILL.md` (toolkit copy) — the skill being torn
  down. All quoted text and every mechanism claim in the retained beats
  ultimately points here; see FACTCHECK.md for the beat-by-beat map.
- `skills/make/explainer/SKILL.md` (toolkit copy) — parent chassis the
  ai-explainer skill extends (referenced by B03 pipeline claim about the
  shared audio-first, phase-gated machinery).
- `skills/make/nopunt/SKILL.md` (toolkit copy) — cross-referenced by
  ai-explainer SKILL.md's GATE L; retained narration does not quote it,
  but the "unread paragraph is a silent bug" claim in B07 rests on the
  Skill's own "read the whole SKILL.md" rule.

## Parent build artifacts (used unchanged)

- `youtube/brutalist/claude-liam-brutalist-skill-ai-explainer/vertical/beat_sheet.json`
  — SHA-256 `2a3180835a89524f132558d6de7b83fcaf384cc5e8e1c9f9cc3cbb0030e308e5`.
  Source of the retained beat structure and narration text.
- `youtube/brutalist/claude-liam-brutalist-skill-ai-explainer/exports/vertical/claude-liam-brutalist-skill-ai-explainer-vertical.mp4`
  — SHA-256 `d8dca0f414440a0816284375159ce89da59284b549735f26aaa9dc7bf46e9cb5`.
  The parent's 2160×3840 master; individual retained beats reused from
  `parent/vertical/media/<BID>.mp4` (not from this master).
- `youtube/brutalist/claude-liam-brutalist-skill-ai-explainer/vertical/mp3/beat-<BID>.mp3`
  — nine Kokoro `am_onyx` MP3s (B00, B01, B03, B04, B05, B06, B07, B08, B10)
  copied byte-for-byte.

## Toolkit runtime relied on

- `runtime/scripts/shorts.py` — cut planner (drop B02 B09, no-endcard, no
  outro rewrite, native portrait reuse).
- `runtime/scripts/compile.py` — mux + verify Short cap (< 180s).
- `runtime/scripts/build_safety.py` — SHORTS_CAP_S=180.0 enforced on both
  timeline plan and encoded container/stream durations.

## Not used

- No external URLs were fetched. No paid API was called. No credentials or
  secrets were read or written. Kokoro was not invoked (no audio
  regeneration). Remotion was not invoked (no visual re-render). No human's
  signature was reused. No fabricated approvals were added.

## Read-only example leads (from BRIEF.md)

- `rohan-v/2026-08-28-agent-first-brutalist/beat_sheet.json` — noted only.
  Original files not opened or modified; results not represented as this
  Short's results.
- `sanjana-rao/09-02-2026-monte-carlo-schedule-risk-explainer/beat_sheet.json`
  — noted only. Original files not opened or modified.
