# SCRIPT — The screen-clean Skill

Playlist: Brutalist. Register: Teardown. Voice: Kokoro `am_onyx` — Liam, in
for Bear. Channel chip inside the reel: `@HumanitariansAI`. Outro handle:
`@NikBearBrown` (per OUTRO-LOCK). Audience: Brutalist fellows already using
Claude Code, plus the guests / fellows pipelines that call this preprocessor
under the hood.

## Beat map

| # | Act | Pattern | Purpose |
|---|---|---|---|
| B00 | ASK | `ClaudeComposerAsk` | Cold open — the ask lands answered; Liam introduces himself. |
| B01 | BLUF | `BrutalistHesitantWriter` | Executive summary — correct the "auto-blurs" misread to "flags". |
| B02 | FRAMEWORK · anatomy | `SkillTeardownAnatomy` | The one file, and who calls it. |
| B03 | FRAMEWORK · pipeline | `SkillTeardownPipeline` | Five passes, one in, one out. |
| B04 | MECHANISM | `SkillTeardownMechanism` | Ignorant of who is speaking (shared preprocessor). |
| B05 | MECHANISM | `SkillTeardownMechanism` | Pass 1 — decode the audio; stop at -40 dB. |
| B06 | MECHANISM | `SkillTeardownMechanism` | Pass 2 — measure the taskbar; cream bars, never black; never crop the top. |
| B07 | MECHANISM | `SkillTeardownMechanism` | Pass 4 — privacy scan flags, never decides. |
| B08 | FALSIFIABILITY | `SkillTeardownMechanism` | The proof is the contact sheet, not the numbers. |
| B09 | VERDICT | `ClaudeVerdictArtifact` | Six lines that recapitulate the skill. |
| B10 | YOUR_TURN | `ClaudeComposerAsk` | Paste-ready dry-run against a synthetic fixture. |
| B11 | OUTRO | `ClaudeTitleOutro` | Title restate, `@NikBearBrown` handle, Liam signoff. |

## B00 · Cold open (ASK)

**Narration.** "Bonjour, this is Liam, in for Bear. Today we tear down the
screen-clean skill. It is the shared preprocessor that turns a screen recording
— Zoom, Teams, Meet, QuickTime — into a beat that fits inside a reel. Five
passes. One review artifact. Never publishes. Here is the mental model."

Composer: greeting `Bonjour, Liam`; topic `BRUTALIST · SKILL TEARDOWN`;
segment `The screen-clean Skill`; command asks what screen-clean actually does;
output lines summarize the answer.

## B01 · Executive summary (BLUF, hesitant writer)

**Narration.** "The name reads like a cleaner. It is not one. screen-clean does
not sanitize your desktop or decide what is embarrassing on your behalf. It
runs five passes over the recording, applies safe defaults, and flags what a
human still needs to look at. The proof of a good pass is not the number of
pixels cropped. It is the contact sheet at the end."

Hesitant writer text:

```
screen-clean
auto-blurs your desktop
into a safe reel beat.
```

Trigger `auto-blurs` → replacement `flags`. Final read: "screen-clean flags
your desktop into a safe reel beat." Correction moment lands on "auto-blurs"
mid-B01. `lead_silence_s: 0.8`. Duration target ≥ 9 s.

## B02 · Anatomy

**Narration.** "First, the anatomy. On disk this is a small skill. One file —
skills slash make slash screen dash clean slash SKILL dot md — the doctrine.
That is it. What matters is who calls it. Fellows calls it. Guests calls it.
Anything else that drops a recorded human into a reel calls it. The point of
this skill is not what it does. It is that it is one skill instead of two."

Anatomy tree shows the file, plus the two known callers (`fellows/SKILL.md`
and `guests/SKILL.md`) as siblings under `skills/make/`, with a callout box:
"Format is orthogonal to relationship — the caller owns the beats; screen-clean
owns the pixels."

## B03 · Pipeline

**Narration.** "The flow is five passes, and only one of them ever decides
anything on your behalf. Pass one — probe the file and decode the audio. Pass
two — aspect fit, measured against the taskbar, padded with cream bars, never
cropped from the top. Pass three — legibility, sampled from real frames at
output size. Pass four — privacy scan, which flags every incidental thing on
screen and waits for a human. Pass five — dead-air trim on the ends. Middle
edits are the caller's job, not this one's."

Pipeline: `<recording>` → PROBE → ASPECT-FIT → LEGIBILITY → PRIVACY-SCAN →
DEAD-AIR-TRIM → `<clean 1920×1080 beat + contact sheet>`.

## B04 · Mechanism 1 — ignorant of who is speaking

**Narration.** "First decision, and it is the whole reason this skill exists.
screen-clean is deliberately ignorant of who is speaking. It does not know
whether the recording is a mentee or a board member or a guest. That relation
belongs to the caller. What screen-clean knows is pixels — a sixteen by ten
capture with a taskbar and someone's whole desktop in frame. Split by format,
not by relationship, and both callers get sharp output. Split by relationship
and one of them ships letterboxed frames — which, per the doctrine, is exactly
the state fellows was in before this skill existed."

Quote (verbatim): "*Format is orthogonal to relationship.* Anything that
ingests a recording calls this." — `screen-clean SKILL.md`.

## B05 · Mechanism 2 — Pass 1 audio gate

**Narration.** "Second decision. Pass one is a gate, not a check. screen-clean
decodes the actual audio — with ffmpeg volumedetect — and if the mean volume is
below negative forty decibels, it stops. Not warns. Stops. Because the
downstream stages will happily build a dead episode around a silent take. The
doctrine is explicit — never infer audio from the presence of an audio
stream. Decode it. On a long recording, sample a ninety-second window from the
middle so volumedetect stays fast."

Quote: "**If mean_volume is below -40 dB, STOP.** … Never infer audio from the
presence of an audio stream — decode it." Followed on-screen by two real
`ffmpeg -af volumedetect` measurements from `demo/screen-clean-run.log`:
`silent-screen-recording.mp4 → mean_volume: -91.0 dB → STOP` and
`voiced-screen-recording.mp4 → mean_volume: -21.1 dB → proceed`.

## B06 · Mechanism 3 — Pass 2 aspect fit

**Narration.** "Third decision. Pass two solves the sixteen by ten problem
without lying about it. A screen recording is sixteen by ten. A reel is
sixteen by nine. Three routes. Route A — pillarbox, no crop, nine hundred
sixteen pixels wide bars each side, taskbar still on screen. Route C — full
crop to sixteen by nine, no bars, but eighty-eight pixels of shared content
come off the bottom with the taskbar. Route B — the default — crop only the
seventy-two pixels of taskbar and pad the rest with cream bars. Nothing shared
is lost. And the bars are Claude cream, never black. Black reads as a
letterboxed upload. Cream reads as in-register. And a rule that never bends —
never crop from the top. The webcam thumbnail lives there. Every removed pixel
comes off the bottom."

Card carries the A/B/C table redrawn from SKILL.md. Quotes: "Measure the
taskbar. Do not assume it." and "Bars are Claude cream `#FAF9F5`, never black."

## B07 · Mechanism 4 — Pass 4 privacy scan

**Narration.** "Fourth decision, and this is the line the skill will not
cross. Pass four is a privacy scan. screen-clean lists every incidental thing
it sees — clock, dock icons, browser tab titles, notification toasts,
filenames, calendar previews. Then it marks which ones the taskbar crop
already removes, and which ones survive into the reel. Then it waits. It does
not auto-blur. It does not decide. Is this embarrassing is a judgment call,
not arithmetic. And the doctrine is explicit — this matters more for fellows,
who are on personal machines with their own life on screen, than for board
members who present deliberately."

Quote (verbatim): "Never auto-blur and never decide on someone's behalf — 'is
this embarrassing' is judgment, not arithmetic, so this pass flags rather than
loops to a fix." — `screen-clean SKILL.md` § Pass 4.

## B08 · Falsifiability — the contact sheet is the proof

**Narration.** "Falsifiability. Numbers do not answer this question. Seventy-two
pixels cropped and fifty-six pixel bars is not something a human can judge in
the abstract. So after applying the default, the skill renders a contact sheet
— four frames sampled across the recording, at ten, thirty-five, sixty and
eighty-five percent, each composited exactly as it will appear in the reel,
bars included, saved as one PNG. Not one frame. Four. Because the shared
screen changes over the recording. A crop that costs nothing while the speaker
is on a web page can clip a terminal six minutes later. The human confirms on
pixels, not on numbers."

Card shows a four-cell contact-sheet mockup with the frame time labels; quote
box: "The proof is the review artifact, not the numbers."

## B09 · Verdict

**Narration.** "The verdict. screen-clean is the shared preprocessor for any
skill that drops a recording into a reel. It is deliberately ignorant of who
is speaking. Format is orthogonal to relationship. Pass one is a gate — mean
volume below negative forty and the build stops. Pass two crops the taskbar,
pads the rest with cream, and never touches the top of the frame. Pass four
flags what is on screen and waits for a human. And the deliverable back to the
caller is a cleaned nineteen twenty by ten eighty video plus a contact sheet
you can actually look at. Small skill. Sharp job."

Verdict card with six lines.

## B10 · Your Turn

**Narration.** "Your turn. Paste this into Claude Code. Make a synthetic
screen recording with ffmpeg — a solid grey rectangle at twenty five sixty by
sixteen hundred, six seconds, silent — so nothing personal is at risk. Then
follow the doctrine of screen-clean's Pass one. Run ffprobe to record the
container, video codec, audio codec, and dimensions. Run ffmpeg dash a f
volumedetect and read the mean volume. If it is below negative forty
decibels, print the STOP verdict and halt. Then reason out loud — with what
you would show on screen for Pass two — the three A B C aspect routes, the
number of pixels each removes, and the width of the bars in each. Do not run
the crop. Do not touch a real recording. This is a doctrine dry run."

Composer greeting `Your Turn`, paste-ready command, three checkable output
lines.

## B11 · Outro

**Narration.** "That was the screen-clean Skill. Liam, in for Bear."

`ClaudeTitleOutro` with `title = "The screen-clean Skill"` and slug
`claude-liam-brutalist-skill-screen-clean` (drives the mascot seed and locks
the `@NikBearBrown` handle per OUTRO-LOCK).
