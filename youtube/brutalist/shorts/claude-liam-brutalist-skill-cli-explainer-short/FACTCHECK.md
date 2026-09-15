# FACTCHECK.md — The cli-explainer Skill

Every on-screen claim traced back to `skills/make/cli-explainer/SKILL.md`
(sha256 `16104901b8037bcf936ea12069bfa40a1495b9bbf2cd439d94254fa40da7071b`,
episode `source_sha256`
`e9e2b5b8f01eb8eb056d2612664cc23d617db0f02937bb0f76cf68d9e5aecf8f`) or to
observed toolkit state in the isolated copy.

## Verifiable facts on screen

| Claim | Source |
|---|---|
| The skill is a folder at `skills/make/cli-explainer/` | Observed via `ls skills/make/cli-explainer/` in the isolated toolkit. Contents: `SKILL.md`, `reference/example-cli-beat_sheet.json`. |
| `SKILL.md` is 365 lines / 3,262 words of plain markdown | `wc -l` and `wc -w` on the isolated toolkit copy. |
| Trigger syntax `cli [concept] [--tool …] [--persona …] [--out …]` | SKILL.md §Trigger (verbatim). |
| Aliases: `cli-explainer`, `claude-cli` | SKILL.md §Trigger. Also observed in `./art --list` and `./art cli-explainer` output (demo/01). |
| Skins: `claude`, `onda`, `codex`, `github`, `shell` | SKILL.md §Skins — five keys named explicitly. |
| Personas: `liam`, `bear` (with new personas extendable) | SKILL.md §Trigger and §Persona. |
| The required beat spine has INTRO, PROBLEM, CLI, CODE, OUTPUT (cycle 1), CLI, CODE, OUTPUT (cycle 2), SUMMARY, NEXT STEPS, OUTRO | SKILL.md §"The required beat spine (EVERY CLI video — not optional)". |
| THE REVISION LAW: the 16:9 always contains ≥1 revision cycle; 9:16 shorts ship a single cycle | SKILL.md §"THE REVISION LAW" — verbatim quote used in B06. |
| Skin swap is a rename with props carrying over: ClaudeComposerAsk ↔ CodexComposerAsk, ClaudeCodeBeat ↔ CodexCodeBeat, ClaudeTitleOutro ↔ CodexTitleOutro | SKILL.md near the end of §Skins — verbatim mapping used in B08. |
| The body logic and bookends are IDENTICAL for every tool; only the input-beat skin changes | SKILL.md §Skins opening line — quoted in B09. |
| "Claude reads the file; the file writes the reel." | Paraphrase of the skill's mechanism (Claude Code is the executor; SKILL.md is the instruction set). Consistent with `./art cli-explainer` which resolves to the file, not an executable (demo/01). |
| `./art scenes` is the pre-authoring library search | SKILL.md §"GATE L — library-first". Also demonstrated in demo/03. |

## Facts deliberately NOT on screen (would date the video)

- No specific model name (Claude 3.x/4.x, Sonnet/Opus). SKILL.md §"the DOUBLE-CHECK LAW" explicitly says "strip anything that dates the video (model version numbers)".
- No render times, node counts, or "current" package versions.
- No hardware specs or platform-specific paths visible in the narration.

## Handoff prompt (B11) — verified paste-ready

The prompt is discussed live per HANDOFF LAW. Verification path:
1. `cli-explainer` is a real trigger — see `./art cli-explainer` demo/01.
2. `skills/make/cli-explainer/SKILL.md` exists (SOURCE-SNAPSHOT.json).
3. Asking Claude to *read* the file before drafting is what the SKILL.md
   §"The shared skeleton" and ai-explainer's §"skill-teardown modifier"
   both require ("Read the WHOLE skill first").

## Adaptations / corrections applied

- **Channel handle** — the shipped `ClaudeTitleOutro` component hardcodes
  `@NikBearBrown`. The brief overrides this playlist's handle to
  `@HumanitariansAI`, so the isolated-toolkit component was extended with a
  `handle` prop (default preserved). The beat_sheet.json B12 supplies
  `handle: "@HumanitariansAI"`. Composer beats also carry
  `folderLabel: "@HumanitariansAI"`. Everything else in the outro (title
  restate, slug-seeded polarity, no subline) obeys OUTRO-LOCK.md.
- **BrutalistHesitantWriter scale** — the shipped `Math.min(width/1920,
  height/1080)` scale collapses to 0.5625 on a portrait canvas (memory
  `hesitant-writer-portrait-scale`). Patched to portrait-aware `min` inside
  the isolated toolkit — landscape behavior is unchanged.
- **Portrait compositions** — `ClaudeCodeBeat916`, `SkillTeardownAnatomy916`,
  `SkillTeardownPipeline916`, `SkillTeardownMechanism916` registered in the
  isolated Root.tsx at `width={1080} height={1920}`. No landscape crop.

## What is NOT claimed

- No claim that the render is 4K-YouTube-verified. Compile.py produces a 4K
  layout; the YouTube-side transcoding check happens later in the human
  pipeline.
- No claim that any human approved the reel. VISUAL-REVIEW.json marks
  `reviewer_type: "ai"` and Bear's viewing/editing is next.
- No claim about publishing or upload. Nothing is pushed to Git or a
  streaming service in this session.
