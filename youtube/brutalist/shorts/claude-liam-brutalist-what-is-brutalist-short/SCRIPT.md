# SCRIPT.md — What Is Brutalist? — Short

*Brutalist playlist · claude-liam · @HumanitariansAI · Kokoro am_onyx ·
Teardown register · No captions. 9:16 native (2160×3840). Derived from
`youtube/brutalist/claude-liam-brutalist-what-is-brutalist` (parent master
SHA-256 `c339f1b5555e847096f3ea975249042c50b86714c8a29fee20d3eb58398c3f9c`).*

Six beats kept from the parent's ten; audio and native portrait renders reused
unchanged. Measured render at 2026-09-08: **94.79 s** container, video and
audio streams. All strictly under the 180 s Shorts cap.

---

## B00 — ASK (16.79 s)  · `ClaudeComposerAsk916`

> Ciao. This is Liam, in for Bear. Brutalist is a video toolkit for
> Humanitarians AI fellows, but it isn't a video editor. It's film as code.
> The recipe lives on GitHub, the rendered film lives on Drive, and the version
> history lives in commits. Here is what that actually means when you sit down
> to build one.

Liam's disclosure lands in the first breath. The Claude composer plants the
ask "Explain what Brutalist actually is. Not the slogan — the thing on disk."
and the three-line result seeds the Short's argument.

## B01 — BLUF · hesitant writer (20.03 s, `lead_silence_s: 0.8`)  · `BrutalistHesitantWriter916`

> Most people hear video toolkit and picture an editor. Timelines, drag and
> drop, sliders. That is not what this is. Brutalist is the plain-text recipe
> your film is built from. Change the recipe, run the pipeline, and a new film
> comes out. That is the whole idea, and it is worth caring about because it
> means your film is versionable, reviewable, and rebuildable — like any other
> piece of code.

On-screen the writer types **"Brutalist is a video editor. Actually, text."**
The word `editor` turns terracotta and swaps to `recipe`; the final line
carries the misconception correction the narration argues.

## B04 — WORKED EXAMPLE · pure function (18.11 s)  · `WibChange916`

> Watch what change actually costs. Here is beat zero's greeting field —
> Ciao, Liam. Edit that one string to Hola, re-render only beat zero, and the
> greeting on screen becomes Hola. Nothing else moves. No timeline nudge, no
> manual conform. Every visual is a pure function of the recipe. Change one
> field, one thing on screen changes.

The one concrete demonstration in the Short. "Beat zero" refers directly to
B00 — the viewer just watched the Ciao, Liam composer, so the swap has
grounded evidence.

## B06 — FALSIFIABILITY (20.46 s)  · `WibNotClaims916`

> Now the honest part — the part every practical tool needs. Brutalist does
> not upload. It renders a four K file and stops. Brutalist does not require a
> paid API. Kokoro is local, and Claude runs on your subscription. And
> Brutalist is not a judge of taste. It will render any bad idea you feed it.
> Watching the cut and deciding it is worth releasing is your job. Those three
> limits are the shape of the tool.

The essential limitation the Shorts prompt explicitly instructs never to cut.

## B07 — VERDICT (14.44 s)  · `WibVerdict916`

> Verdict, in three lines. The recipe is text — read the JSON, read the film.
> The film is a pure function of the recipe — change one property, one thing
> on screen changes. And the judgment is yours — everything else can be
> automated. That is what Brutalist actually is.

The three-line recap. Every line points back at a beat that already ran:
line 1 → B01, line 2 → B04, line 3 → B06.

## B09 — OUTRO (4.86 s)  · `WibOutro916`

> That was What Is Brutalist? Liam, in for Bear. For Humanitarians AI.

Native `WibOutro916` — hardcoded `@HumanitariansAI` handle. The shipped
`ClaudeTitleOutro` locks `@NikBearBrown` per `OUTRO-LOCK.md`, so the parent's
native variant is reused unchanged. No endcard follows; the Short ends on the
sign-off frame.

---

## Beats dropped from the parent (with reason)

| ID | Act | Parent duration | Reason for cut |
|---|---|---|---|
| B02 | FRAMEWORK · `beat_sheet.json` anatomy | 16.49 s | Overlaps B01's "plain-text recipe" definition and B04's live demonstration. Belongs in the 16:9 long. |
| B03 | WORKED EXAMPLE · pipeline (six stages) | 19.52 s | Internal anatomy; the Short answers "what is it", not "how do the stages fit". |
| B05 | DIVISION OF LABOR (human/agent lanes) | 21.61 s | Restates what B06's not-list already lands — "watching the cut is your job." Longest middle beat. |
| B08 | YOUR TURN (paste-ready prompt) | 17.98 s | Reads the long-form CTA aloud; the Shorts prompt explicitly says to omit the detailed exercise. |

The parent 9:16 companion (170.29 s) preserves all four dropped beats and
remains available at `../claude-liam-brutalist-what-is-brutalist/vertical/`.
