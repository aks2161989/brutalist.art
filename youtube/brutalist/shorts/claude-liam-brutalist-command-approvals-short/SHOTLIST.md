# SHOTLIST — Brutalist Command: art approvals — Short (9:16)

8 kept beats · native portrait 2160x3840 (composed 1080x1920 @ scale 2) · reused unchanged from the parent's `vertical/media/` renders.

Dropped from the parent 12-beat cut: B02 (dispatcher case-lines), B04 (no-gate silent-pass example), B07 (`approval_subjects` internal digest mechanics), B10 (Your Turn composer). See `CUT-PLAN.json` for per-beat reasons.

| Beat | Pattern (9:16) | What lands on screen |
|---|---|---|
| B00 | ClaudeComposerAsk916 | Serif greeting `Selam, Liam` above the composer; the ask types in; terracotta send arms; three "not this" output lines cascade under the composer. Folder chip `@HumanitariansAI`. |
| B01 | BrutalistHesitantWriter916 | Writer types `art approvals / signs / files.`; `signs` goes terracotta → backspace → `inspects`; `files` goes terracotta → backspace → `subjects`. Corrected form holds. |
| B03 | ClaudeCodeBeat916 | Code card, title `art approvals — the two verbs`. argparse surface (`reel`, `--fingerprints`) + two-branch `main()` + `metadata.approvals` shape. Spark line "Two verbs. Neither one signs." |
| B05 | ClaudeCodeBeat916 | Code card, title `$ ./art approvals /tmp/…-fellows --fingerprints   (verbatim)`. Fellows fixture metadata + the JSON output with two subject SHA-256s from RUN-LOG section 3. Spark "Two gates armed. Two subjects. Two SHAs." |
| B06 | ClaudeCodeBeat916 | Code card, title `validate_approvals — the five-field record`. Legal record example (status/reviewer_type/reviewed_by/reviewed_at/subject_sha256) + the exact fail-close conjunct from `build_safety.py:155-164`. Spark "Five fields. Human, dated, verbatim." |
| B08 | ClaudeCodeBeat916 | Code card, title `recovery   (verbatim; one word changed, one gate refuses)`. BEFORE → EDIT → AFTER → RECOVERY blocks from RUN-LOG sections 4-5. Spark "One word changed. Approval stale. Human decides." |
| B09 | ClaudeVerdictArtifact916 | Claude artifact page. Title "Verdict". Heading "art approvals — the whole surface, in the order you use it." Six numbered lines stagger in: bare invocation, two verbs, two gates, five fields, live fingerprints, no aliases. |
| B11 | ClaudeTitleOutro916 | Poster serif title `Brutalist Command: art approvals.` with terracotta period. `@NikBearBrown` handle (OUTRO-LOCK). Slug-seeded mascot bounces. |

## Type / visual constraints per kept beat

- Cream page `#FAF9F5`, ink `#3D3929`, terracotta `#D97757` as the one accent. Serif for headings, monospace for code and JSON.
- B01 (hesitant writer): `fontSize: 300`, `lineSpacing: 3.4`, `align: center`, `seed: "approvals-b01"`, `triggerWords: "signs, files"`, `replacementWords: "inspects, subjects"`. Portrait BLUF coverage passes native.
- Code beats (B03/B05/B06/B08): `ClaudeCodeBeat916` schema is `{ title, code, sparkLine }`. Preformatted `\n` strings; long lines soft-wrap inside the terminal card; monospace stagger tracks narration pace.
- B09: `ClaudeVerdictArtifact916` schema is `{ artifactTitle, artifactHeading, artifactLines[] }`. Six lines fit inside the artifact frame.
- B11: `ClaudeTitleOutro916` schema uses `{ title, slug }` — mascot + polarity + jingle seed derive from the parent slug `claude-liam-brutalist-command-approvals`.

## Duration

Container/video/audio all 126.75 s. Every kept beat's `render_duration_s` is inherited from the parent (Kokoro `am_onyx` narration measured on the parent build). No audio was regenerated; no beats were re-rendered. Ends on the parent outro B11 (no silent endcard, per `--no-endcard`).
