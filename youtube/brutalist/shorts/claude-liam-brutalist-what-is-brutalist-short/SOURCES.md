# SOURCES.md — What Is Brutalist? — Short

*Brutalist playlist · claude-liam · @HumanitariansAI. This is the 9:16 Short
derivative; the sources below are what the cut reads from. Nothing new was
authored — narration, audio and native portrait renders are reused unchanged
from the parent's `vertical/` companion.*

## Primary — the parent reel

Every kept beat's video, audio and text are inherited from the parent 9:16
companion. Nothing is regenerated.

| Path (repo-relative) | SHA-256 | Role |
|---|---|---|
| `youtube/brutalist/claude-liam-brutalist-what-is-brutalist/vertical/beat_sheet.json` | `f6863d413ceaa724757c0929cd5b280debcc6d90a07dfa3c4962802edb1ab361` | Source beat sheet (all ten beats). |
| `youtube/brutalist/claude-liam-brutalist-what-is-brutalist/exports/vertical/claude-liam-brutalist-what-is-brutalist-vertical.mp4` | `c339f1b5555e847096f3ea975249042c50b86714c8a29fee20d3eb58398c3f9c` | Parent 9:16 master (170.29 s, native 2160×3840). Not this Short — evidence that the parent existed and was not overwritten. |
| `youtube/brutalist/claude-liam-brutalist-what-is-brutalist/vertical/media/B00.mp4` … `B09.mp4` | reused | Native portrait renders, copied independently into `media/`. |
| `youtube/brutalist/claude-liam-brutalist-what-is-brutalist/vertical/mp3/beat-B00.mp3` … `beat-B09.mp3` | reused | Kokoro `am_onyx` audio, copied independently into `mp3/`. |

The parent 16:9 master under
`exports/claude-liam-brutalist-what-is-brutalist.mp4` was not read for this
cut — the Short derives from the 9:16 companion, not from a landscape crop.

## Toolkit files consulted for this Short

Read for this invocation, per `BUILD-PROMPT.md`:

- `REPOLOOP-SHORTS-PROMPT.md` — the cut-first, strictly-under-3:00 rulebook.
- `runtime/scripts/shorts.py` — the derivation utility (native-portrait reuse
  branch; no re-render).
- `runtime/scripts/compile.py` — the guarded compiler (height 3840 out).
- `runtime/scripts/build_safety.py` — where `SHORTS_CAP_S` and
  `require_short_duration` live.
- `skills/make/ai-explainer/SKILL.md`, `skills/make/nopunt/SKILL.md`,
  `skills/make/explainer/SKILL.md` was searched for but is not present in the
  isolated toolkit — logged as an availability gap in `CHECKS-REPORT.md`.
- `CLAUDE.md`, `CLAUDE-BRAND.md`, `OUTRO-LOCK.md` — brand, palette and outro
  handle locks; the `WibOutro916` handle stays `@HumanitariansAI`.

## Read-only example leads (BRIEF.md)

These beat sheets were read for staging patterns only and are not republished:

| Repo path | SHA-256 | Title |
|---|---|---|
| `rohan-v/2026-08-28-agent-first-brutalist/beat_sheet.json` | `746409a8715e70aab6186145e963c08d088469b809b28fe39d44f5d8d06b1a22` | Your Weekly Video, Handled. |
| `tanmay-kulkarni/2026-08-05-lemonade-claims-bot-mycroft/beat_sheet.json` | `af7fab0f3824887444dd96ade8363a97e28e9011a2dcddffc1ae7b095d15cab6` | I Built Lemonade's Claims Bot — Here's What Production Would Actually Need |

No signatures, private Drive links, personal contacts, or claimed outputs from
those runs are carried forward.

## Public setup URL used on screen

`https://github.com/nikbearbrown/brutalist.art` — the public DOT toolkit
repository named in `REPOLOOP-PROMPT.md`. It only appears in the parent's B08
composer; **B08 is dropped from this Short**, so no clone/install URL is
spoken aloud or read on screen in the retained cut.

## Native custom scenes actually used in this Short

Registered as portrait `Wib*916` / `Claude*916` ids in the isolated toolkit's
`runtime/remotion/src/Root.tsx`. Only the six kept beats' compositions are
exercised; the compiler reads their existing `media/<BID>.mp4`, no
re-rendering happened for this Short.

- `ClaudeComposerAsk916` — B00 cold-open ask.
- `BrutalistHesitantWriter916` — B01 misconception correction.
- `WibChange916` — B04 pure-function demonstration.
- `WibNotClaims916` — B06 honest not-list.
- `WibVerdict916` — B07 three-line verdict artifact.
- `WibOutro916` — B09 title restate with hardcoded `@HumanitariansAI`.

The Short does not use `WibRecipe916` (B02), `WibPipeline916` (B03),
`WibDivision916` (B05) or the second `ClaudeComposerAsk916` instance for B08
— those beats were dropped.

## No paid sources, no uploads, no fabricated approvals

No paid API, no Higgsfield, no ElevenLabs, no stock media, no invented
signature. All audio was authored in the parent by Kokoro `am_onyx` at $0.00
and is reused unchanged here. The Short is a local file; nothing was uploaded
or published from this invocation.
