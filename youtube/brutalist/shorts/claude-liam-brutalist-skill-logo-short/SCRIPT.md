# SCRIPT — The logo Skill — Short (9:16)

Retained narration only. Every line below is byte-identical to the parent
vertical's `beat_sheet.json` at the same beat id. Kokoro `am_onyx` (Liam, in
for Bear). No captions. Total measured run: 155.375 s (< 3:00 cap).

## B00 · ASK · 15.25 s · ClaudeComposerAsk916

Hola, this is Liam, in for Bear. Today we tear down the logo skill. It is the
one command that appends a brand sting after a reel's last beat — one random
pick of animation, mark, and jingle, locked into the beat forever. The mp3 is
the clock. Here is the mental model.

## B01 · BLUF · 18.17 s · BrutalistHesitantWriter916 (lead_silence_s 0.8)

The easy read — the one the word logo invites — is that every reel gets the
same fixed brand sting. It does not. The logo skill spins a wheel across the
brand's mark pool and jingle pool, one random pick per reel, then locks the
pick into the beat so every rebuild is byte-for-byte identical. Random across
reels, locked within one.

## B04 · MECHANISM ACT 1 · 28.79 s · SkillTeardownMechanism916 — "The MP3 is the clock."

First design decision, and it is the whole architecture. The MP3 is the
clock. When logo dot py copies the jingle, it pads it with a trailing silence
— one second by default — using ffmpeg apad. The padded length becomes the
beat's durationS, and Remotion's calculateMetadata derives the frame count
from it. The audible jingle therefore ends strictly inside the beat. Frame
rounding, clip conform, and mux dash shortest can only ever trim silence.
Never sound. Same law as the outro. Want a different length? Use a different
mp3.

## B05 · MECHANISM ACT 2 · 27.33 s · SkillTeardownMechanism916 — "Random once, then locked."

Second decision, and it is the one that makes rebuilds honest. The pick is
random exactly once. Animation, svg, mp3 — chosen by SystemRandom, then
written into the beat itself at shot dot remotion dot picked. Every
subsequent run finds that block and reuses it, so your review cut and your
final master are byte-for-byte the same sting. Want a fresh spin? Dash dash
reroll discards the lock, picks again, and force re-renders. That is the
whole random-versus-deterministic contract in one field.

## B08 · FALSIFIABILITY ACT 5 · 33.50 s · SkillTeardownMechanism916 — "No nik-bear-brown pool."

Falsifiability. Read the sources together and you find a deliberate hole.
There is no logos slash nik-bear-brown pool. Not missing. Not a bug. By
design. The at NikBearBrown channel uses ClaudeTitleOutro instead — a
Remotion scene whose pixel mascot is drawn from tiny rects in code, seeded
by the reel slug, and reads no files at all. That is the OUTRO-LOCK
contract. Which is why this teardown's outro is ClaudeTitleOutro — the
falsifiability beat's own evidence is that the logo skill is not universal.
Every other channel gets the random sting. The Bear channel gets the
deterministic mascot card.

## B09 · VERDICT · 29.00 s · ClaudeVerdictArtifact916

The verdict. The logo skill appends one brand sting per reel — random once,
locked forever. The mp3 is the clock, padded with a silence tail so the
jingle is never cut. The draw is uniform over the pool, so curating the pool
is the actual quality work. drawOn is earned — it needs clean path data or
it is dropped from the lottery. Aspect follows the reel — nine sixteen or
sixteen nine, no re-code. And the at NikBearBrown channel deliberately opts
out — that channel uses ClaudeTitleOutro's pixel mascot, not this skill.

## B11 · OUTRO · 3.33 s · ClaudeTitleOutro916

That was the logo Skill. Liam, in for Bear.

## Structural notes

- No "Third design decision" or "Fourth design decision" appears in the
  retained cut: parent B06 (ACT 3, pool curation) and B07 (ACT 4, drawOn
  earned) are both dropped, so the numbered sequence stops at "Second".
  B08's opening word "Falsifiability" reads as the natural pivot after the
  two design laws.
- The verdict (B09) still names the pool and drawOn rules in one line each;
  those claims survive the Short as verdict-artifact bullets rather than
  standalone mechanism beats.
- B11 is the only mention of "@NikBearBrown" spoken by the presenter —
  Liam's sign-off. The handle is written on-screen inside `ClaudeTitleOutro`
  per OUTRO-LOCK, not narrated.
