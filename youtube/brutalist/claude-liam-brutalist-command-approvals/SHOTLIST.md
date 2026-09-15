# SHOTLIST — Brutalist Command: art approvals

12 beats. Landscape 3840x2160 (composed 1920x1080 @ scale 2). Portrait 2160x3840 (composed 1080x1920 @ scale 2).

| Beat | Pattern (16:9) | Pattern (9:16) | What lands on screen |
|---|---|---|---|
| B00 | ClaudeComposerAsk | ClaudeComposerAsk916 | Serif greeting `Selam, Liam` over the composer; the ask types in; terracotta send arms; three "not this" output lines cascade. Folder chip `@HumanitariansAI`. |
| B01 | BrutalistHesitantWriter | BrutalistHesitantWriter916 | Writer types `art approvals / signs approvals.`; the two trigger words go terracotta, hesitate, backspace, retype to `art approvals / inspects subjects.`; holds ≥2s. |
| B02 | ClaudeCodeBeat | ClaudeCodeBeat916 | Code card, title `art:87-89 — one branch, no aliases`. The 3-line `approvals)` case types in; spark line "One case. No aliases. Two verbs." |
| B03 | ClaudeCodeBeat | ClaudeCodeBeat916 | Code card, title `art approvals — the two verbs`. The argparse surface + `metadata.approvals` shape; spark "Two verbs. Neither one signs." |
| B04 | ClaudeCodeBeat | ClaudeCodeBeat916 | Code card, title `$ ./art approvals /tmp/…-command   (verbatim)`. The two-invocation transcript from RUN-LOG section 2; spark "No gate armed. Nothing to sign." |
| B05 | ClaudeCodeBeat | ClaudeCodeBeat916 | Code card, title `$ ./art approvals … --fingerprints   (verbatim)`. The subject JSON with the two SHA-256s from RUN-LOG section 3; spark "Two gates armed. Two subjects. Two SHAs." |
| B06 | ClaudeCodeBeat | ClaudeCodeBeat916 | Code card, title `validate_approvals — the five-field record`. The record shape + the exact fail-close conjunct from build_safety.py:155-164; spark "Five fields. Human, dated, verbatim." |
| B07 | ClaudeCodeBeat | ClaudeCodeBeat916 | Code card, title `approval_subjects — fingerprints from the source`. Lifts the `digest()` + `approval_subjects()` bodies; spark "Fingerprints from the source. Every run." |
| B08 | ClaudeCodeBeat | ClaudeCodeBeat916 | Code card, title `recovery   (verbatim; one word changed, one gate refuses)`. BEFORE → EDIT → AFTER blocks from RUN-LOG sections 4-5; spark "One word changed. Approval stale. Human decides." |
| B09 | ClaudeVerdictArtifact | ClaudeVerdictArtifact916 | Claude artifact page. Title "Verdict". Heading "art approvals — the whole surface, in the order you use it." Six lines stagger in. |
| B10 | ClaudeComposerAsk | ClaudeComposerAsk916 | Composer, greeting `Your Turn`. Prompt types in as Liam reads it aloud verbatim. Three grading lines cascade. |
| B11 | ClaudeTitleOutro | ClaudeTitleOutro916 | Poster serif title restates with terracotta period. `@NikBearBrown` handle (OUTRO-LOCK — flagged in README.md). Slug-seeded mascot bounces. |

## Type / visual constraints per beat

- All body beats use serif for headings, monospace for code and JSON. Cream page `#FAF9F5`, ink `#3D3929`, terracotta `#D97757` as the one accent.
- B01 (hesitant writer): `fontSize: 240`, `lineSpacing: 2.6`, `align: center`, `seed: "approvals-b01"`. Landscape 2 lines; portrait 3 lines (see vertical beat sheet).
- Code beats (B02-B08): `ClaudeCodeBeat` schema is `{ title, code, sparkLine }`. The code string is preformatted with `\n`; the component renders monospace and staggers lines to match narration pace.
- B09: `ClaudeVerdictArtifact` schema is `{ artifactTitle, artifactHeading, artifactLines[] }`.
- B10: `ClaudeComposerAsk` schema is `{ greeting, topic, segment, command, runningText, output[], folderLabel, modelLabel, effortLabel }`.
- B11: `ClaudeTitleOutro` schema uses `{ title, slug }` — mascot + polarity + jingle seed from slug.

## Duration policy

Duration is an output of the measured Kokoro narration. Each beat's `estimated_duration_s` is a planning number; `actual_duration_s` is the ground truth after `generate_audio_kokoro.py` runs. B01 carries `lead_silence_s: 0.8` and the audio window must land ≥ 9s (EXECUTIVE-SUMMARY LAW). B11 outro is short and silent-tail-friendly.
