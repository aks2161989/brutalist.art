# SOURCES — Brutalist Command: art icons — Short

This Short is a derivative cut of the parent 9:16 companion — every retained
beat's video and audio is copied byte-for-byte from the parent's `vertical/`.
The primary sources of *fact* live in the parent long.

## Parent source (this Short's only visual/audio source)

| # | Source | Path | SHA-256 | Role |
|---|---|---|---|---|
| 1 | Parent vertical beat sheet | `youtube/brutalist/claude-liam-brutalist-command-icons/vertical/beat_sheet.json` | `49f0f3a94bf88ca20885a63d3eecbd311c78d8bd47d0228c8b7c2999e1a1fe27` (from SOURCE-SNAPSHOT.json) | Parent 12-beat vertical companion; 7 of its beats are reused unchanged in this Short. |
| 2 | Parent vertical master | `youtube/brutalist/claude-liam-brutalist-command-icons/exports/vertical/claude-liam-brutalist-command-icons-vertical.mp4` | `d2c828fd84cf71b278bf30fde970d208235c1a645135d02dbd6cdc1243b2b099` | Full 199.29 s vertical; recorded in `CUT-PLAN.json` as `parent_master_sha256`. |
| 3 | Parent per-beat MP3s | `youtube/brutalist/claude-liam-brutalist-command-icons/vertical/mp3/beat-B{00,01,04,05,08,09,11}.mp3` | — | Kokoro `am_onyx` narration, copied independently into this reel's `mp3/`. |
| 4 | Parent per-beat renders | `youtube/brutalist/claude-liam-brutalist-command-icons/vertical/media/B{00,01,04,05,08,09,11}.mp4` | — | Native 2160×3840 Remotion renders, copied independently into this reel's `media/`. |

## Primary sources of fact (from the parent — verified in parent's FACTCHECK)

The narrative claims spoken in this Short's kept beats trace to the actual
skill/command source files (all under the read-only public toolkit):

| # | Claim spoken in the Short | Source file | Verified in |
|---|---|---|---|
| 1 | "seven thousand icons" (B00) / "seven-thousand icon set" (B01) / "3,330 count / 376 brand" (B00 output) / "7,330 icons" (B09) | `icons/icons.json → count` | Parent `FACTCHECK.md` #3, #4 |
| 2 | "aliases: icons, icon, icon-search — same case branch, same output" (B00 output) / "Three aliases all point at the same script" (B09) | `art:60-63` case block | Parent `FACTCHECK.md` #1, #2 |
| 3 | "exact name > every-word > name-prefix > token-hit" (B04) / "IDF re-weighting" (B04, B09) | `runtime/scripts/icon_search.py:14-16`, `:62` | Parent `FACTCHECK.md` #7, #8 |
| 4 | "'sankey flow' finds chart-sankey" (B04) | `demo/RUN-LOG.md` (live capture) | Parent `FACTCHECK.md` #19 |
| 5 | "31 hits" on `./art icons "money"` (B05) / "money-square from Iconoir" | `demo/RUN-LOG.md` (live capture) | Parent `FACTCHECK.md` #18 |
| 6 | "quantum entanglement / no match / exit 0" (B08) | `demo/RUN-LOG.md` (live capture) | Parent `FACTCHECK.md` #21 |
| 7 | "A miss is NOT a licence to draw a one-off." (B08) | `runtime/scripts/icon_search.py:145-147` | Parent `FACTCHECK.md` #14, #15 |
| 8 | "--check answers is-it-in-the-set" (B09) | `runtime/scripts/icon_search.py:119-129` | Parent `FACTCHECK.md` #10 |
| 9 | "--show hands you the raw SVG" (B09) | `runtime/scripts/icon_search.py:112-117` | Parent `FACTCHECK.md` #11 |
|10 | "--brands narrows the corpus to the 376 logos" (B09) | `runtime/scripts/icon_search.py:66-67` | Parent `FACTCHECK.md` #12 |

Every claim is grounded in a parent-verified source; this Short does not
introduce any new factual claim beyond what the parent long already asserted
and verified.

## Doctrinal sources (build governance for this Short)

| Path | SHA-256 (from SOURCE-SNAPSHOT.json) | Purpose |
|---|---|---|
| `REPOLOOP-SHORTS-PROMPT.md` | `56d4c809f78f387ca08ff93210bb8b507725c53f9636f0ceba4005baf0f24d89` | Shorts contract: cut-first, strictly under 3:00, native portrait reuse, evidence-not-assumed-approval. |
| `REPOLOOP-PROMPT.md` | `abf55bdc729a9c30216e4375dff0c62b4bf5af4c717ad28be69709de64d5bc97` | Visual-review schema and run-id/source-sha discipline. |
| `runtime/scripts/shorts.py` | `7109a3d0c29c00181a876db80e34238eb9c0c146a97a639a2bbab6d95d28d6e5` | Derivative-cut utility; reused native portrait media byte-for-byte for every retained beat. |
| `runtime/scripts/compile.py` | `047e9fa6d0944f54c284ed16df8b4d847f62737a0e263a0f4bf0bad2b11f446c` | Guarded compiler; produced the final MP4 at `--height 3840`. |
| `runtime/scripts/build_safety.py` | `479e167ffc80c4a2c235b425149b3922fd96a2e7388a40636f2dfa63b56015bf` | Duration cap + writable-path checks. |
| `skills/make/ai-explainer/SKILL.md` | `a7421d4d861b44a983a31e9fcd7451cd32312a139366e74acc2123dfdefbd3c0` | Register / laws (kept: COLD OPEN, BLUF, ILLUSTRATE, SPARK-LINE, OUTRO). |
| `skills/make/nopunt/SKILL.md` | `ef38a574fe22f2fca1dfa0774bc51681252776f8ef2bd6f2b1e52d6478cab505` | SHOW/HOLD/CARD classification. |
| `docs/PIPELINE-SAFETY.md` | `4619f0d4702317d654cd6498cadc8c277691e4c7565920ef851dbb628aa6298d` | Fellows-safety gates (respected: no upload, no paid API, no push). |

## Read-only example leads (not verbatim, not reused)

| # | Example | Path | SHA-256 | Role |
|---|---|---|---|---|
| 1 | Your Weekly Video, Handled | `rohan-v/2026-08-28-agent-first-brutalist/beat_sheet.json` | `746409a8715e70aab6186145e963c08d088469b809b28fe39d44f5d8d06b1a22` | Read as staging/pacing lead only; no facts, prose or human signatures reused. |
| 2 | ECIS — Episode 3: Three Models, Zero Shortcuts | `anjana-s/2026-08-21-ecis-explained/beat_sheet.json` | `1deb9bfc4fd4acf81ae98fccbc1fb3c1c400e370299db7bbc34d3ba527a57516` | Same. |

## Tools used for the Short

| Tool | Purpose |
|---|---|
| `runtime/scripts/shorts.py` | Produced the derivative cut (kept 7 beats, dropped 5, native-portrait-reuse path). |
| `runtime/scripts/compile.py` (guarded) | Concatenated retained beats and produced the final MP4 at `--height 3840`. |
| `ffmpeg` / `ffprobe` (system) | Duration validation, frame extraction, audio decode into `_qc/`. |

No new Remotion render was produced. No Kokoro TTS regeneration. No API
calls. No uploads. No git push.

## Corrections and honesty log

- The parent's `SOURCES.md` cites "This Week, Gordy" as its example lead #2;
  the Short's assigned examples list (in BRIEF.md) points instead to
  "Your Weekly Video, Handled" and "ECIS — Episode 3". This SOURCES.md
  follows the Short's BRIEF, not the parent's leads.
- The parent's `SOURCES.md` claims `icons.json → count = 7,330` with `376`
  brand — these numbers were spoken in the Short (B00, B09) exactly as
  quoted, on the same snapshot; no drift introduced by this Short.
