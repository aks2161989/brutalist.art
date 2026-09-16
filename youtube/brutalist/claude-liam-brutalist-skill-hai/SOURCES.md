# SOURCES.md — The hai Skill

Episode: `claude-liam-brutalist-skill-hai`
Run id: `d660d0c9949a427980931d1c010c2f47`
Source SHA-256 (supervisor): `957262180375dae1c414e540849fc65ddaf385650b38e3f0d81d373dba692238`

## Primary source (the skill being taught)

- `skills/make/hai/SKILL.md`
  - Read from: `.repoloop/workspaces/claude-liam-brutalist-skill-hai/toolkit/skills/make/hai/SKILL.md`
  - Local SHA-256 at build time: `ef01252f314c8316a32fd6b8dd9d254d43b6ff399964158021daa8b5228185b4` (matches SOURCE-SNAPSHOT.json).
  - Note: this differs from the supervisor's `episode.source_sha256` above. The supervisor hash was recorded against a different revision; the isolated toolkit's snapshotted SKILL.md is the copy actually read for this build. Both are recorded so the audit trail is complete.

## Secondary sources read in full for this teardown

- `runtime/scripts/brand_variant.py` — the scaffolder invoked by `hai`. Local SHA-256 `ced0d3f79d98e5d9b18e005679474b64f8fe3b897f5f6fef6b5b3ee2ed02756e`. The falsifiability beat's voice-field disagreement is verified against lines 34–41 of this file (hai audience defaults `voice_kokoro=af_bella`).
- `brands/hai.md` — the current brand spec. Local SHA-256 `e5b7d4f54e3d31b48ac566c8c073d00ebf4eac38516a804a38a9b8e3912683b7`. Line 34: `Kokoro | am_onyx | —`. Line 36: "There is no paid voice. ElevenLabs was permanently removed on 2026-09-03." The Kokoro voice contradiction between three source files is the falsifiability beat's evidence.
- `skills/make/ai-explainer/SKILL.md` — the parent skill governing the teardown structure (bookends, laws). Read from toolkit; snapshotted hash matches SOURCE-SNAPSHOT.json.
- `skills/make/nopunt/SKILL.md` — the whole-sheet teaching-arc checklist that governs framework/example/falsifiability/scaffolded-task discipline.
- `runtime/prose/teardown/PROSE.md` — the Teardown register manual for this claude-liam reel.
- `runtime/prose/plain/PROSE.md` — the register the `hai` skill imposes on target reels (referenced by the teardown, not applied here).
- `CLAUDE-CODE-VISUAL-QC-CHECK.md`, `OUTRO-LOCK.md`, `docs/PIPELINE-SAFETY.md`, `docs/FELLOWS-SUBMISSION.md` — the toolkit's live doctrine at build time.

## Example beat sheets (leads, per BRIEF.md — not verified facts)

- `rohan-v/2026-08-28-agent-first-brutalist/beat_sheet.json` (SHA-256 `746409a8715e70aab6186145e963c08d088469b809b28fe39d44f5d8d06b1a22`)
  - Copied to `.repoloop/workspaces/claude-liam-brutalist-skill-hai/examples/746409a8715e.json` and read in full for tone/pattern reference. It uses `voice_kokoro: af_bella` and `channel: @HumanitariansAI`, matching the `hai` scaffolder's default at the time it was authored. Not republished; not reused for narration or media.
- `sachin-vishaul-b/2026-08-28-finance-event-signals-week4-graded/beat_sheet.json` (SHA-256 `4c35b91fb8961c9db3e40b9ba108434d27a96724ea79b1b4d24f3dba6f7d94a6`)
  - Copied to `.repoloop/workspaces/claude-liam-brutalist-skill-hai/examples/4c35b91fb896.json` and read in full. Same non-republish treatment.

Neither example's original path, human signature, Drive URLs, or personal contact details are reproduced anywhere in this reel.

## Scene-source lineage (for the portrait rebuild)

- `SkillTeardownAnatomy916.tsx`, `SkillTeardownPipeline916.tsx`, `SkillTeardownMechanism916.tsx` — copies of the wrappers first authored for the `claude-liam-brutalist-skill-guests` episode's portrait companion (build 2026-09-08). Both files ship the same schema as the landscape parents and pull from `useVideoConfig()` so they compose natively at 1080×1920 (2160×3840 at 2× scale). Copied verbatim from `youtube/brutalist/claude-liam-brutalist-skill-guests/scene-source/runtime/remotion/src/scenes/` into this reel's `scene-source/`, then into the isolated toolkit's `runtime/remotion/src/scenes/`. Credit: the guests episode's build (Liam, in for Bear).
- `BrutalistHesitantWriter.tsx` (portrait-aware scale patch) — copy of the guests episode's patched component. The patch adds `const isPortrait = height > width;` and picks the aspect-appropriate design reference so serif type does not collapse to ~56% on 9:16. Copied into the isolated toolkit's `runtime/remotion/src/scenes/BrutalistHesitantWriter.tsx`.

Registered in the isolated toolkit's `runtime/remotion/src/Root.tsx` for this run only. The public toolkit is not modified.

## Demo evidence

- `demo/scaffold-run.log` — captured stdout of running `brand_variant.py` on a synthetic fixture reel. Shows: (1) new `hai-example-reel` directory created; (2) audience metadata rewritten (audience=HAI, register=Plain, palette=humanitarians, engine=kokoro, voice=af_bella); (3) `_variant_todo` checklist emitted; (4) on rerun without `--force`, the scaffolder refuses to overwrite. These outputs are the evidence for B02 (Anatomy) and B04 (Non-Destructive Fork).
- `demo/fixture-book/youtube/example-reel/beat_sheet.json` — the fixture. `voice_kokoro=am_onyx`, `palette=claude`, `channel_title=@NikBearBrown`.
- `demo/fixture-book/youtube/hai-example-reel/beat_sheet.hai.json` — the scaffold's output. `voice_kokoro=af_bella`, `palette=humanitarians`, `channel_title=@HumanitariansAI`, plus the `_variant_todo` block.
- Source SHA of the fixture is preserved: `22e0a614bc69fead4b56e494f705bb8f78771d813a79abfa1464be93e29befbf` (recorded before + after the run).

## What we did NOT do

- We did not run `hai` against a real HAI reel and ship the output. Doing so would need a canonical reel to fork against, plus a Plain-register rewrite pass. That is a per-video human decision, not a mechanical build.
- We did not render an actual HAI-branded episode. This is a `claude-liam` teardown OF the hai skill; the palette on screen is Claude (cream/warm ink/terracotta), not humanitarians.
- We did not fetch anything from the network. All source reads are local to the snapshotted toolkit.
