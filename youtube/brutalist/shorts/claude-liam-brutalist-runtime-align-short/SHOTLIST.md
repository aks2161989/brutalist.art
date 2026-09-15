# SHOTLIST — Brutalist Utility: align.py — Short

6 beats, native 2160×3840 portrait, 90.25s total. Derived from
`claude-liam-brutalist-runtime-align/vertical` by whole-beat cut; no re-render.
Every retained beat is a Remotion 916 pattern reused unchanged from the parent.

| Beat | Act | Pattern (916) | What appears (before narration lands) |
|------|-----|---------------|----------------------------------------|
| B00 | ASK | `ClaudeComposerAsk916` | Composer card fades in; `Shalom, Liam` greeting types; the ask fills the composer ("The audio is generated, the beats are timed to it, and I want a per-word clock…"); running text "invoking align.py…" appears; three output lines cascade under the composer. |
| B01 | BLUF | `BrutalistHesitantWriter916` | Cream page holds; "align dot py / transcribes / the audio then / guesses the / spoken words." types; `transcribes` turns terracotta, hesitates, backspaces, types `times`; `guesses` turns terracotta, hesitates, backspaces, types `knows`. Final settle corrects the misconception. |
| B02 | FRAMEWORK | `SkillTeardownMechanism916` | Eyebrow `UTILITY · PIPELINE`; heading "The word clock — one pass, one file."; body states the phase chain (`Beat sheet + mp3 → WHISPER → MATCH → INTERPOLATE → EMIT`); pull-quote cites `align.py:3-8`; verdict chip `one narration · three consumers`; spark line "Known text · measured audio · one clock." |
| B07 | MECHANISM | `ClaudeCodeBeat916` | Card in; title `align.py:104-109 + 158-165 — even_spread + [warn]`; `even_spread()` body types; caller branch inside `main()` types; the `[warn]` print line types (`NO anchors — even spread over {dur}s (word-keyed tracks on this beat are unreliable)`); spark line "Fallback exists. Warning exists. Rendering continues." |
| B09 | VERDICT | `ClaudeVerdictArtifact916` | Artifact card in; heading "align.py — the whole surface, in the order it does its job"; six numbered bullets cascade (input → recognise → align → interpolate → emit → fallback). |
| B11 | OUTRO | `ClaudeTitleOutro916` | Cream page in; title `Brutalist Utility: align.py.` types; handle `@NikBearBrown` appears; slug-seeded mascot animates below. |

## What was dropped (whole-beat cut)

- B03 `align.py --help` CLI listing — internal reference detail; belongs in the long.
- B04 Single-beat `words.json` layout — code cascade; the Verdict states the same.
- B05 `whisper_words()` function listing — CPU int8 detail; belongs in the long.
- B06 `align_words()` SequenceMatcher listing — 33-line code cascade; the Framework and Verdict state it at high level.
- B08 The 1926 number-drift worked example — a second concrete case not required for the Short's high-level explanation.
- B10 `Your Turn` composer — 28s exercise prompt; the Short skips it per cut-first brief.

## Portrait framing

Every retained clip is a native 2160×3840 render from the parent's `vertical/media/`.
`shorts.py` verified portrait dimensions and reused each unchanged (no crop, no re-render).
SAFE916 area is respected; no ink bleeds beyond the safe margin in any retained beat.

## Aspect note

The parent's landscape (16:9) film has a separate SHOTLIST recording the 3840×2160
compositions; that document is not superseded here. This Short is 9:16 native.
