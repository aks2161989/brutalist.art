# SCRIPT — The logo Skill

12 beats. Persona: Liam, in for Bear. Voice: Kokoro `am_onyx`. Register: Teardown.

## B00 — Cold open (ClaudeComposerAsk)

> Hola, this is Liam, in for Bear. Today we tear down the logo skill. It is
> the one command that appends a brand sting after a reel's last beat — one
> random pick of animation, mark, and jingle, locked into the beat forever.
> The mp3 is the clock. Here is the mental model.

## B01 — BLUF (BrutalistHesitantWriter, lead_silence 0.8s)

> The easy read — the one the word logo invites — is that every reel gets the
> same fixed brand sting. It does not. The logo skill spins a wheel across
> the brand's mark pool and jingle pool, one random pick per reel, then locks
> the pick into the beat so every rebuild is byte-for-byte identical. Random
> across reels, locked within one.

## B02 — Framework (SkillTeardownAnatomy)

> First, the anatomy. On the toolkit side there is SKILL.md — the doctrine,
> the laws, and the pool contract. Next to it, scripts slash logo dot py, a
> small deterministic scaffolder. The scene it drives is LogoOutro dot tsx —
> eight animation techniques, aspect-aware, duration derived from props.
> Alongside the toolkit sits logos slash brand slash — a flat pool of dot svg
> marks and dot mp3 jingles. And a staging tree under public slash logo-outro
> where the chosen svg is copied so Remotion's staticFile can serve it. Small
> on disk. Random where it matters.

## B03 — Framework (SkillTeardownPipeline)

> The flow is six steps. Resolve the brand alias — nbb to bear-brown, hai to
> humanitarians, muz to musinique. Pick, or reuse the locked pick — animation,
> svg, mp3 chosen once by the system random. Copy the mp3 into the reel's
> audio folder and pad it with a silence tail so nothing gets cut. Stage the
> svg into the Remotion public tree so staticFile can find it. Append the
> beat after the last beat — type REMOTION, pattern LogoOutro, props carrying
> the pick. Then render via remotion scenes dot py and recompile. Same shape
> every reel.

## B04 — Mechanism Act 1 (SkillTeardownMechanism)

> First design decision, and it is the whole architecture. The MP3 is the
> clock. When logo dot py copies the jingle, it pads it with a trailing
> silence — one second by default — using ffmpeg apad. The padded length
> becomes the beat's durationS, and Remotion's calculateMetadata derives the
> frame count from it. The audible jingle therefore ends strictly inside the
> beat. Frame rounding, clip conform, and mux dash shortest can only ever
> trim silence. Never sound. Same law as the outro. Want a different length?
> Use a different mp3.

## B05 — Mechanism Act 2

> Second decision, and it is the one that makes rebuilds honest. The pick is
> random exactly once. Animation, svg, mp3 — chosen by SystemRandom, then
> written into the beat itself at shot dot remotion dot picked. Every
> subsequent run finds that block and reuses it, so your review cut and your
> final master are byte-for-byte the same sting. Want a fresh spin? Dash dash
> reroll discards the lock, picks again, and force re-renders. That is the
> whole random-versus-deterministic contract in one field.

## B06 — Mechanism Act 3

> Third decision, and this one bites. The draw is uniform over every dot svg
> in the brand pool, which means the pool IS the quality bar. On September
> first, twenty twenty-six, logos slash medhavy shipped with two failure
> modes at once. Four marks belonged to a different company entirely — a
> wrong mark is drawable if it is in the pool. And twenty-two selected files
> were byte-identical renames of existing designs, so those combinations came
> up twice as often. Forty-two drawable files. Twenty-five unique designs.
> The fix was a rejected subdirectory that drops files from the glob without
> deleting anything.

## B07 — Mechanism Act 4

> Fourth decision. Seven of the eight animation techniques render the svg
> file itself — via Remotion's Img and staticFile — so any mark works,
> gradients, groups, whatever. But drawOn is different. It rasterises the
> mark's paths into a stroke that draws itself, then flood-fills. That
> requires clean path data. So logo dot py parses the svg first. If it finds
> a text element, an image, a gradient, a mask, or any visible non-path
> shape, drawOn is dropped from the lottery for that reel. Every other
> technique still competes. drawOn is earned.

## B08 — Falsifiability (SkillTeardownMechanism)

> Falsifiability. Read the sources together and you find a deliberate hole.
> There is no logos slash nik-bear-brown pool. Not missing. Not a bug. By
> design. The at NikBearBrown channel uses ClaudeTitleOutro instead — a
> Remotion scene whose pixel mascot is drawn from tiny rects in code, seeded
> by the reel slug, and reads no files at all. That is the OUTRO-LOCK
> contract. Which is why this teardown's outro is ClaudeTitleOutro — the
> falsifiability beat's own evidence is that the logo skill is not universal.
> Every other channel gets the random sting. The Bear channel gets the
> deterministic mascot card.

## B09 — Verdict (ClaudeVerdictArtifact)

> The verdict. The logo skill appends one brand sting per reel — random once,
> locked forever. The mp3 is the clock, padded with a silence tail so the
> jingle is never cut. The draw is uniform over the pool, so curating the
> pool is the actual quality work. drawOn is earned — it needs clean path
> data or it is dropped from the lottery. Aspect follows the reel — nine
> sixteen or sixteen nine, no re-code. And the at NikBearBrown channel
> deliberately opts out — that channel uses ClaudeTitleOutro's pixel mascot,
> not this skill.

## B10 — Your Turn (ClaudeComposerAsk, greeting "Your Turn")

> Your turn. Paste this into Claude Code. Read the logo skill's SKILL dot md.
> Pick one of your delivered reels — a real one — and pick a brand pool that
> fits it. Run logo dot py on the reel with the dash dash no-render and dash
> dash no-compile flags. That gives you the appended beat and the padded mp3
> without touching your rendered master. Then check three things. Does the
> reel's beat sheet now carry a shot dot remotion dot picked block. Is the
> padded mp3's length equal to the jingle's length plus your tail. And if you
> re-run without dash dash reroll, does the pick stay identical. If all three
> answer yes, the lottery is locked and honest.

## B11 — Outro (ClaudeTitleOutro)

> That was the logo Skill. Liam, in for Bear.
