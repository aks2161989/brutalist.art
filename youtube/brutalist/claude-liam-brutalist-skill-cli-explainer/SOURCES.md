# SOURCES.md — The cli-explainer Skill

## Primary source (episode teardown target)

| Repo-relative path | SHA-256 (SOURCE-SNAPSHOT.json) |
|---|---|
| `skills/make/cli-explainer/SKILL.md` | `16104901b8037bcf936ea12069bfa40a1495b9bbf2cd439d94254fa40da7071b` |

The episode source hash (per THIS INVOCATION `episode.source_sha256`):
`e9e2b5b8f01eb8eb056d2612664cc23d617db0f02937bb0f76cf68d9e5aecf8f`. The
`source_sha256` from THIS INVOCATION is authored on the whole source bundle;
the file-level SHA-256 above is the individual `SKILL.md` hash captured in
`SOURCE-SNAPSHOT.json` at `2026-09-08T08:11:40.885303+00:00`.

## Structural references (read in full during authoring)

| Repo-relative path | SHA-256 (SOURCE-SNAPSHOT.json) |
|---|---|
| `skills/make/ai-explainer/SKILL.md` | `a7421d4d861b44a983a31e9fcd7451cd32312a139366e74acc2123dfdefbd3c0` |
| `skills/make/nopunt/SKILL.md` | `ef38a574fe22f2fca1dfa0774bc51681252776f8ef2bd6f2b1e52d6478cab505` |
| `runtime/prose/teardown/PROSE.md` | `6accc1a576ca9b52713abd31507f5deece6dc2612ca90967b25b661e59111786` |
| `docs/PIPELINE-SAFETY.md` | `4619f0d4702317d654cd6498cadc8c277691e4c7565920ef851dbb628aa6298d` |
| `docs/FELLOWS-SUBMISSION.md` | `7825c728f040b0f7a49bbd950a5a2bef70c8a59ff2fbe0538716c8d3381f5223` |
| `REPOLOOP-PROMPT.md` | `abf55bdc729a9c30216e4375dff0c62b4bf5af4c717ad28be69709de64d5bc97` |
| `CLAUDE-BRAND.md` (toolkit) | read in full for palette + handle law |
| `OUTRO-LOCK.md` (toolkit) | read in full — see § below on the @HumanitariansAI adaptation |
| `CLAUDE-CODE-VISUAL-QC-CHECK.md` (toolkit) | read in full for the 9-point rubric |
| `runtime/remotion/src/scenes/ClaudeComposerAsk.tsx` | read for exact prop names |
| `runtime/remotion/src/scenes/ClaudeCodeBeat.tsx` | read for exact prop names |
| `runtime/remotion/src/scenes/BrutalistHesitantWriter.tsx` | read for portrait scale fix |
| `runtime/remotion/src/scenes/SkillTeardownAnatomy.tsx` | read for prop schema |
| `runtime/remotion/src/scenes/SkillTeardownPipeline.tsx` | read for prop schema |
| `runtime/remotion/src/scenes/SkillTeardownMechanism.tsx` | read for prop schema |
| `runtime/remotion/src/scenes/ClaudeTitleOutro.tsx` | read for handle-adaptation |

## Read-only example leads (BRIEF.md)

| Local copy | SHA-256 (example-sources.json) | Title |
|---|---|---|
| `.repoloop/.../examples/746409a8715e.json` (from `rohan-v/2026-08-28-agent-first-brutalist/beat_sheet.json`) | `746409a8715e70aab6186145e963c08d088469b809b28fe39d44f5d8d06b1a22` | "Your Weekly Video, Handled." |
| `.repoloop/.../examples/85f72b7a80bc.json` (from `divyank-s/2026-07-26-cli-explainer-demo/beat_sheet.json`) | `85f72b7a80bcb1cba40328f305ec4ca459ba2b13e54fc7cd3326de43d594f068` | "Claude, Patched." |

The example beat sheets were opened as reference DATA per BRIEF.md — they
adapted staging (13-beat skill-teardown spine, ClaudeVerdictArtifact for the
summary act, ClaudeTitleOutro as the last beat). No original file was overwritten,
no author's human signature was reused, and neither reel's rendered output is
being republished as this run's.

## Isolated-toolkit modifications (this episode only)

The isolated toolkit at
`.repoloop/workspaces/claude-liam-brutalist-skill-cli-explainer/toolkit/` is
scratch — the public toolkit and every fellow folder outside this reel are
read-only. Three edits landed inside the isolated copy for the CLI-Explainer
episode:

1. `runtime/remotion/src/scenes/BrutalistHesitantWriter.tsx` — scale factor
   made portrait-aware (`isPortrait ? min(width/1080, height/1920) :
   min(width/1920, height/1080)`). Prior memory `hesitant-writer-portrait-scale`
   documents that the shipped scale collapses to 0.5625 on a 1080×1920 canvas.
2. `runtime/remotion/src/scenes/ClaudeTitleOutro.tsx` and
   `ClaudeTitleOutro916.tsx` — `handle` prop added; defaults to
   `@NikBearBrown` (respects the OUTRO-LOCK contract) and lets this playlist's
   beat sheet override with `@HumanitariansAI`. OUTRO-LOCK.md §3 fixes the
   handle as one channel per outro; the playlist adaptation is explicit here,
   not silent.
3. `runtime/remotion/src/Root.tsx` — four native portrait 9:16 compositions
   registered: `ClaudeCodeBeat916`, `SkillTeardownAnatomy916`,
   `SkillTeardownPipeline916`, `SkillTeardownMechanism916`. Same components,
   `width={1080} height={1920}`, no landscape crop. `./art scene-index` was
   re-run and `./art scenes --check` confirms each as RENDERABLE 9:16.

## Local live demos (captured in `demo/`)

| File | Command | What it shows |
|---|---|---|
| `demo/01-art-cli-explainer.txt` | `./art cli-explainer` | The alias resolves to `skills/make/cli-explainer/SKILL.md` — the skill is a file, not an executable. |
| `demo/02-scenes-check-composer.txt` | `./art scenes --check ClaudeComposerAsk`, `./art scenes --check ClaudeCodeBeat` | Library confirmation for the two scenes shown in the ask/code beats. |
| `demo/03-scenes-search-prompt-code.txt` | `./art scenes "prompt typed to code"` | Live library-first search — the SKILL.md §GATE L procedure. |

No paid API, no remote clone, no fresh install was executed. All demos ran
against the installed isolated toolkit at Bear's local path.

## Availability log — gaps recorded honestly

- `scripts/type_check.py` — not shipped in this cut. TYPECHECK.md documents
  the fallback (visual review of the same rubric points against sampled frames)
  rather than claiming a missing checker passed.
- `runtime/remotion/src/illustrations/ILLUSTRATIONS.md` — present. Read for
  the illustration family taxonomy but not needed for authored beats here.
- `kerning` skill — not present. Same fallback as `type_check.py` above.

## Corrections logged

- The `divyank-s/2026-07-26-cli-explainer-demo/beat_sheet.json` example used
  `folderLabel: "@NikBearBrown"` on every composer beat. This episode belongs
  to `@HumanitariansAI` per BRIEF.md, so every composer's `folderLabel` was
  set explicitly to `@HumanitariansAI`. Same for the outro `handle` prop
  above.
- The example's beat 8 (`ClaudeVerdictArtifact`) passed a `sparkLine: ""`
  prop that the component's schema does not accept. Not repeated — this
  episode's B10 uses only the documented `artifactTitle` /
  `artifactHeading` / `artifactLines` fields.
