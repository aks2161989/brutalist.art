# Sources

## Primary source (the skill we're tearing down)

- `skills/make/explainer/SKILL.md` — SOURCE-SNAPSHOT SHA-256
  `8208b85178b5dae0656773e822d96809f5dec3c2d77acdfad0df1a28851e1597`.
  Supervisor `episode.source_sha256`:
  `9439e59ca95a9e7b5ec57b4e5c3f4ea360053fc78e8d57b0bf51a59c14b939d1`.
  Verbatim quotes shown on-screen in B04 (laundering function), B05 (two-axis
  system), B06 (slot contract), B07 (VOX LAW). Every quote appears exactly as
  written in the SKILL.md.

## Related toolkit doctrine (context, not on-screen)

- `skills/make/ai-explainer/SKILL.md` — child skill (cold open + hesitant
  writer + verdict + your-turn + outro structure; skill-teardown modifier
  auto-arms because this reel's source is a SKILL.md; ai-explainer explicitly
  documents `explainer` as its parent under §"Lineage: an EXTENSION of
  `explainer`").
- `skills/make/nopunt/SKILL.md` — SHOW/HOLD/CARD classification and
  teaching-arc checklist.
- `runtime/prose/teardown/PROSE.md` — Teardown register (Feynman × MKBHD).
- `CLAUDE-BRAND.md` — palette + typography lock (cream `#F3EBDD`, ink
  `#2F2A26`, terracotta `#D97757`).
- `OUTRO-LOCK.md` — `@NikBearBrown` handle is hardcoded in `ClaudeTitleOutro`
  regardless of channel; `@HumanitariansAI` appears as the folder chip in the
  composer beats only.
- `docs/PIPELINE-SAFETY.md` — audio-first policy, pending approvals policy.
- `CLAUDE-CODE-VISUAL-QC-CHECK.md` — the 9-point rubric applied in Gate V.

## Read-only example leads (NOT reused as this run's outputs)

Per BRIEF.md, these are LEADS whose beat sheets informed act structure
adaptation; nothing prose or signature was reused.

- `rohan-v/2026-08-28-agent-first-brutalist/beat_sheet.json` — Your Weekly
  Video, Handled (SHA-256 `746409a8715e70aab6186145e963c08d088469b809b28fe39d44f5d8d06b1a22`).
  Adaptation: this reel's spine follows the same skill-teardown act structure
  (framework → mechanism → falsifiability → verdict → handoff) established by
  the exemplar reels. No prose reused; no signature attributed.
- `sanjana-rao/09-02-2026 monte-carlo-schedule-risk-explainer/beat_sheet.json` —
  Monte Carlo Schedule Risk: When Will This Project Really Finish?
  (SHA-256 `86452e39919248a4bec3bb521fab376697aa4b61e1ca2b9a5e86155075b49c63`).
  Adaptation: a peer example of an explainer teardown at multi-minute length
  with a clearly-earned verdict beat; used to sanity-check that a doctrine
  teardown that ends "zero vox is a correct outcome" reads as a verdict, not
  a refusal.

## Facts corrected vs. source

None. The SKILL.md is treated as authoritative — the reel *quotes and judges*
it in the Teardown register. Where the SKILL.md itself hedges (e.g. VOX LAW
supersedes prior share targets "2026-09-02"), the reel carries the hedge
without hardening it.

## Corrections applied to stale toolkit guidance

- Older versions of the parent explainer skill's SKILL.md sometimes referenced
  `skills/animated-deck/…` for rhetorical patterns, `EQUATIONS.md` (brutalist
  root vs. bundled beside the skill), or `SPEC.md` for the hesitant writer.
  The reel names the doctrine files present in the current source snapshot
  (SKILL.md, MOTION.md, REMOTION.md, EQUATIONS.md — the four the SKILL text
  itself points at in this version). Not shown on-screen: any legacy path
  that would date the video.
- ILLUSTRATIONS.md is not shipped in this snapshot; the ai-explainer child
  skill references it as `runtime/remotion/src/illustrations/…` — recorded in
  CHECKS-REPORT.md as a known gap rather than claimed as present.

## Runtime scripts referenced

- `runtime/scripts/generate_audio_kokoro.py` — used to produce the 11 mp3s.
  Voice `am_onyx` (Liam, in for Bear), free and local, $0.00 for the run.
- `runtime/scripts/remotion_scenes.py` — used to render each beat to
  `media/[beat].mp4`.
- `runtime/scripts/compile.py` — used to assemble the 4K master.
- `runtime/qc/final_frame_check.py` — Gate V frame-level visual QC.

## Chrome dependencies

- `chrome-headless-shell` v149.0.7790.0 (Chrome for Testing binary from
  `runtime/remotion/node_modules/.remotion/chrome-headless-shell/…`),
  wrapped with `runtime/scripts/chrome_wrap.sh` (`--single-process
  --in-process-gpu --disable-crash-reporter --no-sandbox`) to survive the
  Apple App Sandbox Mach-port block.

## Runtime script gaps recorded honestly (not run)

- `scripts/type_check.py` (GATE T) — referenced in `CLAUDE.md` but not
  shipped in this toolkit snapshot. Visual typography reviewed by reading
  Gate V frames.
- `slate cut` self-demo — the reel *explains* the command; running it would
  produce a different reel. The B09 handoff prompt is paste-ready so a fellow
  can execute it themselves.
- `pantry.py` — not run; the reel has zero pantry stills by design (VOX LAW
  makes zero-vox a correct outcome for a doctrine teardown).
