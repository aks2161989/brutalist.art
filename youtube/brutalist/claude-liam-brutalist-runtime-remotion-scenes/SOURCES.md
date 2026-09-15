# SOURCES — Brutalist Utility: remotion_scenes.py

## Primary source

| File | Repo-relative path | SHA-256 |
|---|---|---|
| remotion_scenes.py | runtime/scripts/remotion_scenes.py | 3e5faac58d8ecd487bc43c83f267a035d939338375aff954d3a472d14f787996 |

Source hash from SOURCE-SNAPSHOT.json (captured 2026-09-14T06:08:48).

## Supporting sources read during production

- `docs/PIPELINE-SAFETY.md` — quote about failed renders not replacing previous media slot.
  SHA-256: 4619f0d4702317d654cd6498cadc8c277691e4c7565920ef851dbb628aa6298d
- `runtime/scripts/build_safety.py` — atomic_json, validate_project, validate_approvals,
  writable_path (imported by remotion_scenes.py)
- `runtime/remotion/src/Root.tsx` — Composition registration pattern (read in session)

## Demo output

- `demo/list_demo.txt` — real output of `python3 runtime/scripts/remotion_scenes.py demo_reel/ --list`
  (run on synthetic disposable fixture in $TMPDIR, 2026-09-14)

## Example leads (reference only — not reproduced)

- `examples/7e3ea1f61c42.json` — yatra-r/2026-09-03-this-week-gordy beat sheet
  (SHA-256: 7e3ea1f61c421e605e583be9b2a7b5f554aa8cadfb6e14dabaee66f471856083)
  Credit: original reel folder rohan-v/2026-08-28-agent-first-brutalist and
  yatra-r/2026-09-03-this-week-gordy — not republished, patterns adapted.

## New scene components authored this session

- ClaudeCodeBeat916.tsx — portrait 916 code display; same schema as ClaudeCodeBeat
- SkillTeardownPipeline916.tsx — portrait 916 vertical pipeline; same schema as SkillTeardownPipeline
- SkillTeardownMechanism916.tsx — portrait 916 mechanism card; same schema as SkillTeardownMechanism

All three registered in runtime/remotion/src/Root.tsx and indexed via `./art scene-index`.

## Factual claims verified against source

All narration claims verified against the actual remotion_scenes.py source code.
No metrics, publication counts, or external assertions in this episode — it teaches
the tool's own mechanisms.
