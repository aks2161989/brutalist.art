# SOURCES — Brutalist Command: art shorts (Short cut)

All source material is read-only relative to this Short.

## Parent film

- Reel folder: `youtube/brutalist/claude-liam-brutalist-command-shorts/vertical/`
- Parent master mp4: `.../exports/vertical/claude-liam-brutalist-command-shorts-vertical.mp4`
- Parent master SHA-256: `4ef22048ed097f773e165ac396a040343e886ce5a122ffe4d628151a4304a371`
- Parent beat sheet: `.../vertical/beat_sheet.json` (12 beats, ~296 s planned; 124.67 s retained here)
- This invocation `episode.source_sha256`: `6a0ba5a7bde668c17e41e38c3850f498b78a3d9dbdb396caa80b73af97e61139`

Retained beat media/audio was copied byte-for-byte from the parent's
native portrait build (see `build-state.json/input_sha256`). No crop,
no re-render, no regenerated audio, no endcard, no outro rewrite.

## Toolkit code cited on screen (read-only)

Isolated snapshot at `.repoloop/shorts/workspaces/claude-liam-brutalist-command-shorts-short/toolkit/`.
Baselines recorded in `SOURCE-SNAPSHOT.json`:

- `art` (dispatcher case `shorts)` at `art:81-83`; `vertical)` at `art:84-86`).
- `runtime/scripts/shorts.py` (SHA-256 `7109a3d0c29c00181a876db80e34238eb9c0c146a97a639a2bbab6d95d28d6e5`) —
  auto-plan drops, ONDA CHECK, pantry precedence, `--vertical` bypass.
- `runtime/scripts/build_safety.py` (SHA-256 `479e167ffc80c4a2c235b425149b3922fd96a2e7388a40636f2dfa63b56015bf`) —
  `SHORTS_CAP_S = 180.0` and `require_short_duration()`.
- `runtime/scripts/compile.py` — landscape/vertical compilation and
  atomic verification.

## Prompt/spec sources

- `REPOLOOP-SHORTS-PROMPT.md` (SHA-256 `56d4c809f78f387ca08ff93210bb8b507725c53f9636f0ceba4005baf0f24d89`) —
  the Shorts law: strictly under 3:00, whole-beat cut first, preserve
  the long unchanged.
- `REPOLOOP-PROMPT.md` (SHA-256 `abf55bdc729a9c30216e4375dff0c62b4bf5af4c717ad28be69709de64d5bc97`) —
  the VISUAL-REVIEW schema and check protocol.
- `skills/make/ai-explainer/SKILL.md` — the AI Explainer visual/register
  treatment.
- `skills/make/nopunt/SKILL.md` — no-punt/no-fabrication rules.
- `BRIEF.md` — this Short's production contract.
- `BUILD-PROMPT.md` — this invocation's build brief (preserved unchanged).

## Fellows-example leads

Read-only; consulted for framing precedent, not treated as verified
facts. No signatures reused, no original files overwritten.

- `rohan-v/2026-08-28-agent-first-brutalist/beat_sheet.json`
  (SHA-256 `746409a8715e70aab6186145e963c08d088469b809b28fe39d44f5d8d06b1a22`).
- `anjana-s/2026-08-21-ecis-explained/beat_sheet.json`
  (SHA-256 `1deb9bfc4fd4acf81ae98fccbc1fb3c1c400e370299db7bbc34d3ba527a57516`).
