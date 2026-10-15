---
name: godot-trailer
description: Cut a 60–90 second game trailer from a Godot repo — real gameplay only, one idea escalated, edited to music, ending on one call to action. Music-only by default; add `voice` for sparse Liam (Kokoro am_onyx) voiceover. Reuses the godot-waikthrough capture contract and any existing walkthrough captures; picks the hook instead of covering every feature. Also accepts game-trailer. Does not build a game, make AI footage, or publish.
---

# godot-trailer — sell the game with what it really does

```text
godot-trailer /path/to/game-package
godot-trailer /path/to/game-package --music /path/to/track.wav
godot-trailer /path/to/game-package voice            # Liam voiceover, sparse (Bear: "use the Liam voice")
```

An **agent-driven builder** like [godot-waikthrough](../godot-waikthrough/SKILL.md),
not a shell command. The input is the same: a repo with a Godot game (resolve the
real `project.godot`, often in `godot/`; if several unrelated games exist, ask
which). The difference is the job. A walkthrough **covers** the game for a
student; a trailer **argues** for it to a stranger who owes you nothing and leaves
the moment they are bored or confused. So the trailer *selects*: one hook, one idea
escalated, nothing else. Features that don't serve it are cut, even the ones that
took months.

Output goes in `<game-package>/youtube/<game>-trailer/` (slug `<game>-trailer`,
never `claude-liam-*`: it is the game's piece, not a Liam episode). Preserve the
game, saves, existing films and edits. Making a trailer does not authorize changing
the game, paid generation, a Git push or publishing.

Read this file, then [trailer-craft.md](references/trailer-craft.md) (the rules and
why), [trailer-contract.md](references/trailer-contract.md) (`trailer.json`, what
the gate checks) and [capture-for-trailers.md](references/capture-for-trailers.md)
(capture, trim and mix). Also [RENDER-TARGETS.md](../../../RENDER-TARGETS.md) and
[PIPELINE-SAFETY.md](../../../docs/PIPELINE-SAFETY.md).

## The one test

The viewer silently asks, in order: **What is this? What would I do in it? Why
should I care, when I have other games?** The trailer answers all three, quickly,
mostly with footage. Everything below serves that, and the finished trailer is
judged by a person who has never seen the game (stage 6), not by how it feels to
you, because you already know the game.

## 0. Decide before you capture (`TRAILER-BRIEF.md`)

Write these down first. They steer which footage is worth recording at all.

1. **Trailer type.** Default `store`: the cold, store-page gameplay trailer, 30–90 s,
   for strangers (the workhorse; every rule applies strictest). `announcement`
   allows more tone and mystery but still needs a glimpse of what the player does.
   `launch` may assume awareness, but social proof (quotes, awards) must be real and
   cited, never invented. A vertical social cut is a **separate request**: its own
   native 9:16 beat sheet that shows the hook in the first second or two; never a
   crop of this one.
2. **One audience, one goal.** Who is it for, and what do you want them to do: play,
   wishlist, download, buy? Footage answers *that* audience's questions: a strategy
   player needs to see decisions; a horror player needs vulnerability and tension.
3. **The hook, in one sentence**, built from the mechanic: "you reverse gravity to
   turn hazards into pathways", not "a thrilling platformer". If it won't compress,
   **stop and tell Bear**: a trailer that won't come together is usually a design
   problem showing, and it is cheap to learn that now. Don't edit around it.
4. **The verbs.** What does the player press, and what happens? By the end a viewer
   must be able to say it. Source: input map and a real run, not the GDD's wish list.
5. **The one idea** the trailer escalates, and its **tone** (the music must match it).
6. **The three answers** in plain words (what is this / what would I do / why care).
7. **Feature inventory**, as in the walkthrough: `implemented` or `planned`, from
   source plus a real run. **Planned or broken features can never appear**: a
   trailer is a promise, and the game has to keep it. Log every implemented feature
   you leave out, with the reason, in `CUTS.md` (cutting is the work).
8. **Build status** — `prototype`, `demo`, `early-access`, `released`, `coming-soon`
   — as it is. It decides what the end card may say.

## 1. Capture a shot bank, not a coverage run

Follow the [Godot capture contract](../godot-waikthrough/references/capture-and-coverage.md)
(native 3840×2160 render of the real main scene, normal input path, logged inputs,
isolated copy, separate `user://`, hash every capture) plus
[capture-for-trailers.md](references/capture-for-trailers.md). Differences:

- **Over-capture on purpose.** Record several takes of each planned moment and pick
  the best; a rehearsed run is craft, not cheating. The honesty line is what the
  game did, not how many tries it took.
- **Reuse before recording.** If a walkthrough reel exists for the same game, its
  `capture/` files are a ready shot bank when the `build_id` matches. Hash them,
  don't re-record. A different build means new captures.
- **Capture the moment, not the tour:** a clear *situation → action → consequence*
  per take, the player visible and recognisable, HUD kept where it explains a
  mechanic (health, combo, counters) and clutter hidden (FPS, collider overlays,
  debug prints). Check every take's frames for visual bugs before it enters the bank.
- **No cheats on camera.** No teleport, invincibility, disabled collisions, spawned
  content, time-scale change or slow motion; `integrity` in `trailer.json` attests
  it per capture. A camera the player can't have (a free debug cam) is allowed only
  as a labelled establishing shot, never as the hook or the peak.
- **No AI footage, no mock-ups, no concept art, no re-created gameplay, no
  Higgsfield.** A cinematic would only be the game's own in-engine one, labelled if
  it could be mistaken for gameplay. If the game can't run, report the exact blocker.

## 2. Build the argument (`SHOTLIST.md`, then `trailer.json`)

Shape (a compressed three acts): **hook → establish → escalate → peak → title →
button → one call to action**. A 60-second sketch, not a stopwatch:

| About | Role | What it does |
|---|---|---|
| 0–5 s | hook | the most distinctive, readable moment of the verb; **gameplay in the first five seconds** |
| 5–15 s | establish | genre named by the footage, the player, the core action, the hook shown |
| 15–35 s | escalate | connected situation → action → consequence, choices and results |
| 35–50 s | escalate+ | complication, variety, progression, higher stakes: the same idea, bigger |
| ~50 s | peak | a drop or pause just before, then the memorable payoff |
| 50–60 s | title, button | the title card; an optional short joke/surprise/last great moment |
| last 4–6 s | cta | title, exact platforms, availability, **one** action; held; never a fade to black |

Rules that make it work (the why is in [trailer-craft.md](references/trailer-craft.md)):

- **No logos, studio cards, fade-ins or scenery first.** Logos go at the end. (A famous
  franchise's logo is a hook; an unknown game's is the least interesting opening.)
- **Hook early, and say the genre with footage** (genre by ~10 s, hook by ~15 s).
- **Show the verb.** The player character is on screen, doing things. A flythrough
  answers "what is this?" and skips "what do I do?"
- **One idea, escalated; not a feature tour.** Every shot must show something new
  (mechanic, environment, enemy, progression, UI, payoff) or it is cut. Intensity
  rises; only a declared contrast may dip.
- **Legibility beats intensity.** Each shot lasts long enough to find the player,
  see the action and see its result. Establish the game before you speed up. Pace
  to the experience: cozy breathes, horror lingers, action accelerates.
- **Text is a tax.** Few words, only for what footage can't say (premise, platform,
  player count). No adjectives ("epic", "immersive"): claims need evidence, and the
  footage is the evidence.
- **Edit at normal speed.** Cuts, hard or soft transitions, and at most one
  ≤0.5 s freeze at the peak. No slow motion, speed ramps or time-lapse of gameplay.
- **Stay short.** Cut anything that doesn't earn its seconds: 60–90 s typical.

Write the cut as `trailer.json` ([contract](references/trailer-contract.md)), each
shot with its situation, action, consequence, the feature it shows, and what is new.

## 3. Sound

The trailer is **edited to the music; the music is the master clock** (the
walkthrough's "narration is the clock" does not apply). It has **no narration by
default; add the voice (below) when Bear asks for it** ("use the Liam voice").

1. **Pick the track first, by tone.** In order: the game's own music (honest and
   already on-tone); a track Bear supplies, with its rights recorded in
   `MUSIC.md`; an **original cue generated from code** (`music.source: "generated"`: a
   script inside the reel, hash-bound, no samples and no third-party audio, so no outside
   licence; declared `trailer_only` and disclosed in the description); none. **Generic
   "epic" stock music that doesn't match the game is the most damaging common mistake.**
   Never download music or invent a licence, and never present a trailer score as the
   game's own audio: a silent game stays silent, with no effects synced to its actions.
   A generated cue is unlistened until a person hears it: say so, and measure what you can
   (section energy, drop depth, beat grid, loudness).
2. `python3 skills/make/godot-trailer/scripts/beat_grid.py music/track.wav --out
   music/beats.json` gives tempo, beats, downbeats and onsets. Cut on them; a track
   without a steady beat is declared `rhythm: "free"` instead. Check the grid by ear
   or against onsets; the phase can lock to an off-beat hi-hat.
3. **Design the dynamics:** a pause just before the peak so it lands; contrast
   between sections; sound that directs attention (music for tone, the game's real
   hits and abilities for tangibility, room for impact).
4. Build `audio/trailer-mix.wav` (game audio under/over the music, ducked) to match
   the timeline length; the compiler takes it with `--audio`. Loudness gate it.
5. **Muted test:** the premise, the verb and the key information must survive with the
   sound off. Video often starts muted.

### The voice: Liam, sparse (`vo` in `trailer.json`)

Bear's voice for narrated films is **Liam, in for Bear: Kokoro `am_onyx`, free and local**
(`vo.persona: "liam"`, `vo.voice: "am_onyx"`). In a trailer he is a few dry lines, not a
narrator, because the footage does the arguing:

- **Say only what the screen already shows or says.** Every line carries an
  `on_screen_equivalent` (the HUD, a sign, a popup, the card); a muted viewer must lose nothing
  essential. Use the game's own words where it has them ("Land on top", "The high lane is
  optional"). No adjectives, no claims the footage can't back.
- **No introduction.** No "hello", "this is Liam" or "in for Bear": a trailer opens on gameplay.
  The gate fails it. The end card is spoken as its facts ("A playable prototype. Download it on
  GitHub."), not as the locked `claude-liam-*` outro, and never over the drop before the peak.
- **Sparse.** At most 12 words a line, 60 in all, under about 45 % of the runtime, air between lines
  (the gate enforces all of it). Leave the peak and any deliberate silence alone.
- **Generate, don't fake:** `art godot-trailer --assemble REEL` runs `vo_kokoro.py`: it writes
  `audio/vo/<id>.wav` (trimmed, peak-normalised) and a manifest binding each file to its text, then
  the mix ducks the music under the voice. Pronunciation goes through the Liam dictionary
  (`runtime/pronunciation/liam.json`); add an entry when a word is said wrong.
- **Check it is understood, not just audible.** Transcribe the finished master with a local whisper
  model and compare with the script: a recognizer mishears bare "Shipping Lane" as "shipping line"
  (a common phrase) and hears it right when a word of context follows, so the title line became
  "Clawd in Shipping Lane." It is a proxy for a listener, not a replacement: Bear still listens.
- The film is disclosed as a synthetic voice in the description. The slug stays `<game>-trailer`;
  if Bear wants the `claude-liam-*` naming and its locked outro, that outro is a separate post-roll.

## 4. The end card and the facts on it

One card: **title, exact platforms, availability, one dominant action** (`Wishlist
on Steam`, `Play the demo`, `Download on GitHub`). Not four social handles. Rendered
with the `GameTrailerCard` composition (`kind: "endcard"`), the game's own identity
(near-black ground and off-white type by default, an optional accent, its custom icon
if it has one). **Not** `ClaudeTitleOutro`: the [OUTRO-LOCK](../../../OUTRO-LOCK.md)
covers only `claude-liam-*` episodes, and a trailer ends on its action, not a
sign-off. A channel sign-off, if wanted, is a separate post-roll, never part of the
trailer master.

(If the voice is on, Liam speaks the same facts, once.) Every fact on the card has a recorded source: platforms from `export_presets.cfg`,
the README or the store page; availability and address from the git remote, README or
Bear; never invented. A prototype says so ("Playable prototype"). If nothing
verifiable can be offered as the one action, **stop and ask Bear** what it is.
Never put the engine's default icon on the card as if it were the game's logo.

## 5. Gate, render, hand off

```bash
# From books/ (or brutalist.art/ without the prefix). REEL = <game-package>/youtube/<game>-trailer
./brutalist.art/art godot-trailer --beat-grid REEL/music/track.wav --out REEL/music/beats.json
./brutalist.art/art godot-trailer --vo REEL            # only the Liam lines (assemble also runs this)
./brutalist.art/art godot-trailer --check REEL --game GAME_PACKAGE
./brutalist.art/art godot-trailer --assemble REEL      # frame-exact trims, beat_sheet.json, cards, voice, mix
./brutalist.art/art final REEL --height 2160 --fps 30 --audio REEL/audio/trailer-mix.wav --out REEL/exports/landscape
```

The check is read-only. It fails on structure (hook first, required roles in order,
CTA last), honesty (planned features, cheats, hidden camera, adjectives, unsourced
card facts), evidence (hashes, native 16:9 4K footage, windows inside captures) and
craft limits (runtime, legibility floors, text budget, cuts on the beat, intensity).
Warnings are judgment calls to resolve or justify. It **cannot** tell whether a shot is
legible, whether the music fits, or whether a stranger gets it. Pass
`--require-viewer-test` for the final handoff.

Cowork stage: do the brief, shot bank, `trailer.json` and the music, write the paperwork
(`FACTCHECK.md`, `SHOTLIST.md`, `PROMPTS.md` are required before a final; also
`TRAILER-BRIEF.md`, `CAPTURE.md`, `MUSIC.md`, `CUTS.md`, `description.txt`) and
`BUILD-PROMPT.md` (absolute paths, the remaining commands above in order, the gates, the
traps below), then stop. The Claude Code stage runs `--assemble` and `art final`; cards
render only through `runtime/scripts/remotion_scenes.py`, which the assembler calls. If Bear
asks for an end-to-end build, run it straight through (every step is free). No captions burned in.

**Loudness.** The mix targets −16 LUFS with a −2 dB true-peak ceiling: AAC encoding adds about
half a dB, so a −1.5 target left the first master at −0.7 dB. Check the master, not the mix file.

**Traps already met.** GATE T scans gameplay frames as if they were designed type: the
game's own terracotta sprite reads as low-contrast accent text and its edge-hugging HUD as
overflow. The documented answer is `presentation` in `trailer.json`: the 4K capture is scaled
into the title-safe box (0.9), matted in the game's own background colour, and the real text
(the HUD strips) is tested through named `contrast_regions` with a written reason; never
relabel gameplay as another shot type. GATE V flags title and end cards as "underfill", so the
assembler declares them `sparse_by_design` with a reason. Read both reports (`TYPECHECK.md`,
`_qc/REPORT.md`) and look at frames of the master, not the probe alone.

## 6. The tests only people can run

Never fabricate these; mark them pending until a person has done them.

- **Viewer test.** Show the cut, unexplained, to someone who has never seen the game.
  Stop at 10 s: *what kind of game is it, what does the player do?* After: *what's
  different about it?* Watch their face, not the screen: where attention drifts is
  where to cut. Repeat with a different person **with the sound off**. If they can't
  answer, the footage and sequence are wrong; **revise those before adding polish.**
- **Promise check.** Does any edit imply a mechanic, freedom or visual quality the
  game does not deliver? Bear signs that.

Record them in `checks` in `trailer.json`. Until they're done the report says the
trailer is **not audience-tested**.

## Deliverables

The 4K MP4 (absolute path and a quoted `open` command), runtime, the shot list, what
was cut and why, the gate result with every warning, which tests are pending, and the
limits (scripted-input captures are not a human playtest; they establish what the
game does, not whether it is fun). No upload, publish or push is implied.
