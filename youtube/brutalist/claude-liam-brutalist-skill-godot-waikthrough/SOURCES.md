# SOURCES — The godot-waikthrough Skill
# run_id: 4d4269b669dd4b84a92a266e5bff804f
# episode.source_sha256: a0cfc6ba0c3e56fd162d80c940e4fbf31594739d7c7283dcfe3c9a0ae90c39ed
# Re-verified 2026-09-12: SKILL.md §4 changed; §1–§3 unchanged.

## Primary source

| File | SHA-256 | Role |
|---|---|---|
| `skills/make/godot-waikthrough/SKILL.md` | `089bfb9410bf8d423dbc22867288181aaef4085a1b9d5c4df962f5d717b141d4` | Episode primary source (from SOURCE-SNAPSHOT.json captured 2026-09-12) |
| `skills/make/godot-waikthrough/references/capture-and-coverage.md` | (not individually hashed in snapshot) | Capture and coverage contract, coverage.json schema |
| `skills/make/riff/SKILL.md` | (local toolkit copy) | Riff mechanic description — cited in B06 |

All paths are relative to the isolated toolkit root. SHA-256 values are from
SOURCE-SNAPSHOT.json where available.

## Supporting doctrine read

| File | Status |
|---|---|
| `skills/make/ai-explainer/SKILL.md` | Read (skill-teardown modifier) |
| `skills/make/nopunt/SKILL.md` | Read (SHOW/HOLD/CARD classification) |
| `runtime/prose/teardown/PROSE.md` | Read (Teardown register) |
| `CLAUDE-BRAND.md` | Read (palette, type, illustrate law) |
| `OUTRO-LOCK.md` | Read (outro card: @NikBearBrown, slug-seeded mascot, no subline) |
| `CLAUDE-CODE-VISUAL-QC-CHECK.md` | Read (QC procedure) |
| `docs/PIPELINE-SAFETY.md` | Read (compile, review, final export gates) |
| `docs/FELLOWS-SUBMISSION.md` | Read (submission requirements) |
| `runtime/remotion/src/scenes/WalkerGodotSetup.tsx` | Read (scene props: mode, title, labels, details, cueSeconds) |
| `runtime/remotion/src/scenes/GodotDesignBoard.tsx` | Read (scene props: layout, cards, cues) |
| `runtime/remotion/src/scenes/GodotDevWorkbench.tsx` | Read (scene props: mode, code, cues, notes) |

## Verbatim quotes on screen

| Beat | Quote | Source |
|---|---|---|
| B08 | "Do not secretly fix the game to make a demonstration succeed. If it cannot run, report the exact blocker; no fake gameplay in place of an engine run." | `skills/make/godot-waikthrough/SKILL.md §2` — verified verbatim |
| B09 | "Run `./art godot-waikthrough --check REEL` before final assembly and after changes. It validates the coverage contract, clip hashes, dimensions, time ranges, input-log presence, and beat references." | `skills/make/godot-waikthrough/references/capture-and-coverage.md` — verified verbatim |

## Observations and gaps

- `ILLUSTRATIONS.md` referenced in ai-explainer SKILL.md not found in toolkit — noted; illustration selection proceeded using available scene library.
- `scripts/type_check.py` referenced in GATE T — not present in isolated toolkit; TYPECHECK.md documents this gap honestly.
- `reference/type-spec.md` not present — gap recorded; visual typography reviewed manually from frame inspection.
- `skills/make/kerning/SKILL.md` not present — gap recorded.
- No Godot game project available in this isolated build — self-demo limitation documented in B09 per SELF-DEMO LAW feasibility fallback.
- `godot-walkthrough` alias: SKILL.md notes this as valid alias. Episode uses canonical `godot-waikthrough` spelling per episode.slug.
- coverage.json schema shown in B04 is a teaching illustration from capture-and-coverage.md — labeled as such; no actual capture files exist in this reel (no game project available).

## Example leads (read-only reference)

| File | SHA-256 | Title | Use |
|---|---|---|---|
| `rohan-v/2026-08-28-agent-first-brutalist/beat_sheet.json` | `746409a8...` | Your Weekly Video, Handled. | ClaudeComposerAsk staging reference |
| `yatra-r/2026-09-03-this-week-gordy/beat_sheet.json` | `7e3ea1f6...` | This Week, Gordy. | ClaudeVerdictArtifact staging reference |

No human signatures, private Drive URLs, or old recordings from these examples were reused.
