# SOURCES — Brutalist Command: repoloop.sh — Short

Derived from the parent vertical reel at
`youtube/brutalist/claude-liam-brutalist-command-repoloop/vertical/`.
Every retained beat's props, narration and code are inherited unchanged
from the parent; the parent's sources apply here without modification.

## Parent reel (derivation source)

- Reel: `youtube/brutalist/claude-liam-brutalist-command-repoloop`
- Vertical beat sheet: `.../vertical/beat_sheet.json`
- Parent master (16:9): `.../exports/vertical/claude-liam-brutalist-command-repoloop-vertical.mp4`
  - SHA-256 (recorded in BUILD-PROMPT.md): `5be3541b68c180caacd46db2428d6ff32916131b1d9ee4a374a398589079e66a`

## Primary sources (inherited from the parent's SOURCE-SNAPSHOT.json)

| Repo-relative path | SHA-256 (captured 2026-09-10T04:28:37Z) |
|---|---|
| `repoloop.sh` | `2d10a246b7bbf5b52abecaaa668fc6f065d1ff937e8492be8054654b631477a0` |
| `runtime/scripts/repoloop.py` | `7b82920a93a41eafffd3ddf1c5e62c56d8a79b24576cbc3e06ed9c71dd3020f0` |
| `REPOLOOP-PROMPT.md` | `abf55bdc729a9c30216e4375dff0c62b4bf5af4c717ad28be69709de64d5bc97` |

## Doctrine referenced by the Short

| Path | SHA-256 |
|---|---|
| `REPOLOOP-SHORTS-PROMPT.md` | `56d4c809f78f387ca08ff93210bb8b507725c53f9636f0ceba4005baf0f24d89` |
| `REPOLOOP-PROMPT.md` | `abf55bdc729a9c30216e4375dff0c62b4bf5af4c717ad28be69709de64d5bc97` |
| `skills/make/ai-explainer/SKILL.md` | `a7421d4d861b44a983a31e9fcd7451cd32312a139366e74acc2123dfdefbd3c0` |
| `skills/make/nopunt/SKILL.md` | `ef38a574fe22f2fca1dfa0774bc51681252776f8ef2bd6f2b1e52d6478cab505` |
| `runtime/prose/teardown/PROSE.md` | `6accc1a576ca9b52713abd31507f5deece6dc2612ca90967b25b661e59111786` |
| `docs/PIPELINE-SAFETY.md` | `4619f0d4702317d654cd6498cadc8c277691e4c7565920ef851dbb628aa6298d` |
| `docs/FELLOWS-SUBMISSION.md` | `7825c728f040b0f7a49bbd950a5a2bef70c8a59ff2fbe0538716c8d3381f5223` |
| `runtime/scripts/build_safety.py` | `479e167ffc80c4a2c235b425149b3922fd96a2e7388a40636f2dfa63b56015bf` |
| `runtime/scripts/compile.py` | `047e9fa6d0944f54c284ed16df8b4d847f62737a0e263a0f4bf0bad2b11f446c` |
| `runtime/scripts/shorts.py` | `7109a3d0c29c00181a876db80e34238eb9c0c146a97a639a2bbab6d95d28d6e5` |
| `CLAUDE.md` (toolkit root) | read for framing rules — no code shown |
| `CLAUDE-BRAND.md` | read for palette/typography — cream/ink/terracotta |
| `OUTRO-LOCK.md` | governs B11 (hardcoded @NikBearBrown handle) |

## Read-only example leads (from BRIEF.md)

| Path | Title | SHA-256 |
|---|---|---|
| `rohan-v/2026-08-28-agent-first-brutalist/beat_sheet.json` | Your Weekly Video, Handled. | `746409a8715e70aab6186145e963c08d088469b809b28fe39d44f5d8d06b1a22` |
| `sanjana-rao/08-24-2026-playlist-architecture-as-product-strategy/playlist-architecture-short/beat_sheet.json` | Playlist Architecture — Short | `787621776bcd8810d8719a61f577f3589707bbf59151655fcbbdd10555b318a0` |

Examples were READ only. No signature, media, human name, or Drive URL was
reused. This Short's phrasing and cut decisions are original; the parent's
narration is the ground truth for retained beats.

## Public references

- Toolkit repository: <https://github.com/nikbearbrown/brutalist.art>
  (public DOT repo — the URL is not spoken or shown in this Short).

## Retained-beat evidence

- **B00** — Ask + three answer bullets: inherited from parent vertical
  `beat_sheet.json` `beats[0].shot.remotion.props` (unchanged).
- **B01** — Hesitant-writer text/trigger/replacement: inherited from
  parent vertical `beats[1].shot.remotion.props`. Portrait-tuned
  `fontSize 155 / lineSpacing 2.2` — inherited from parent (no changes).
- **B05** — `--dry` inventory excerpt: inherited from parent vertical
  `beats[5].shot.remotion.props`; source of truth for the underlying
  inventory is `demo/RUN-LOG.txt` in the parent reel.
- **B09** — Six-line verdict artifact: inherited from parent vertical
  `beats[9].shot.remotion.props`.
- **B10** — Your Turn composer command: inherited from parent vertical
  `beats[10].shot.remotion.props` (paste-ready prompt read aloud in
  narration verbatim).
- **B11** — Outro title/slug: inherited from parent vertical
  `beats[11].shot.remotion.props`; hardcoded `@NikBearBrown` handle per
  OUTRO-LOCK.md.

## Deterministic authoring seeds

- BrutalistHesitantWriter B01 seed: `repoloop-b01-vertical-v3` (locked;
  identical performance every render — inherited unchanged).
- ClaudeTitleOutro mascot: slug-seeded from
  `claude-liam-brutalist-command-repoloop` per OUTRO-LOCK.md.

## No paid or upstream API used for this Short

- No Kokoro invocation for the Short (all mp3s copied bit-identical from
  parent).
- No Remotion re-render for the Short (all mp4s copied bit-identical from
  parent).
- No ElevenLabs, no OpenAI, no Anthropic API, no Higgsfield, no
  Smithsonian/pantry fetches, no web search.

## No fellow signatures reused

Rohan and Sanjana's example beat sheets shaped the cut planning and doc
prose only. Their names, media, human review records and Drive URLs are
NOT republished here.
