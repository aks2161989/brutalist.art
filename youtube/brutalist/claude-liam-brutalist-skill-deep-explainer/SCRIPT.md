# SCRIPT.md — Claude, Deepened. (The deep-explainer Skill)

Episode: 07 · Brutalist playlist · @HumanitariansAI
Persona: Liam, in for Bear · Voice: Kokoro `am_onyx`
Source: `skills/make/deep-explainer/SKILL.md` (SHA-256 c268b6d698fcf117f2cb89f4f5c9efb1bed007c294ea64a5016726a4988c601e)
Register: Teardown

---

## B00 — cold open (ClaudeComposerAsk)

> Namaste — this is Liam, in for Bear. There is a skill called deep-explainer that most fellows will skip past thinking it is just a longer version of ai-explainer. It is not. So I asked Claude to read the whole SKILL.md and tell me what makes it its own thing.

## B01 — hesitant writer BLUF (BrutalistHesitantWriter)

Typed text (before correction):
> The deep-explainer skill is\njust ai-explainer,\nmade longer.

Correction: `just ai-explainer, made longer` → `act-structured, with two extra gates`

Final read aloud:
> The deep-explainer skill is act-structured, with two extra gates.

Narration (~30 words, ≥9s window with lead_silence 0.8):
> Watch the writer walk this back. Deep-explainer is not ai-explainer stretched to five minutes. It is act-structured, with two hard gates its parent chassis does not have.

## B02 — anatomy (SkillTeardownAnatomy)

> Every skill on this toolkit is a folder Claude reads before working. Deep-explainer is a SKILL.md plus three reference files — continuity, shopping-list, and vox-beats. The doctrine is small. What it inherits is not.

## B03 — lineage (SkillTeardownMechanism)

> Read the second line of the SKILL and it says the quiet part out loud. Deep-explainer extends ai-explainer, which extends explainer. Nothing below repeals a parent law. So the four bookends, the show-don't-tell law, the illustrate law — those all come in for free.

Quote: `This skill EXTENDS ai-explainer, which extends explainer. Nothing below repeals a parent law; this file only adds the genre's own contracts.`

## B04 — the spine (SkillTeardownPipeline)

> Here is the spine, fixed. Cold open. Hesitant-writer overview. Then acts one through N — the documentary body. Then the verdict recap, the YOUR TURN prompt, and the title outro. The middle is what deep-explainer owns.

## B05 — act card (FormACard) — Act II divider

> Act two — what actually makes it deep.

## B06 — multi-act, not padded (SkillTeardownMechanism)

> The first rule is a rule about restraint. The five-to-ten minute band is a natural landing zone for a multi-act concept — never a target to pad toward. Deep-explainer is not "make it longer." It is: this idea needs several linked mechanisms, each with its own evidence.

Quote: `If the arc lands at 4:40, ship 4:40.`

## B07 — VOX LAW (SkillTeardownMechanism)

> The old skill had a vox quota — twenty to twenty-five percent of body beats had to be pantry stills. That quota is dead. The new law: a still earns its beat only when the still IS the evidence. Not atmosphere. Not decoration. And zero vox beats can be a correct outcome.

Quote: `A film whose evidence is text, code, or data correctly has zero vox beats.`

## B08 — continuity scoped (SkillTeardownMechanism)

> Documentary continuity is expensive. Deep-explainer scopes it hard: continuity chains only inside a vox run — two or three consecutive vox beats authored as one camera move. A run never crosses an act boundary, and the max length is three beats. Everywhere else, a hard cut.

Quote: `Never attempt frame-continuity across the whole episode.`

## B09 — act card (FormACard) — Act III divider

> Act three — the two hard gates.

## B10 — Gate D1 (SkillTeardownMechanism)

> Gate D-one: the first compile is always a full-length watchable previz. Vox beats render as slates — beat id plus narration line. Manim and Remotion render for real. Audio is real. This is honest by design. At this length, the pantry is the bottleneck, and the previz is what a human reviews for pacing.

Quote: `Never present a previz as a finished cut.`

## B11 — Gate D2 (SkillTeardownMechanism)

> Gate D-two: the shopping list. Written AFTER audio lock, never before. A card written before the beat's real length is known can only ask for "a clip of X." After lock, it asks for at least seven point two seconds of X. Then trimming — lossless — becomes the default. Stretching — lossy — never has to happen.

Quote: `SHOPPING.md is written after audio lock (never before).`

## B12 — output contract (SkillTeardownAnatomy)

> Here is what a finished deep-explainer folder actually contains. The beat sheet is the heart. The build prompt, the build log, the factcheck, the sources, the shopping list. Then the working slots — pantry, media, manim, clips, mp3. Every reel builds into its owning book, never into the toolkit.

## B13 — the honest limitation (SkillTeardownMechanism)

> Now the limitation of this film. Actually running deep-explainer end to end would take pantry sourcing, a human review pass, and five to ten minutes of narration. What you have watched is the skill's mechanism read from its own SKILL.md — quotes verbatim, cites shown. When you run it yourself, this is the doctrine your Claude is following.

## B14 — verdict recap (ClaudeVerdictArtifact)

Heading: The deep-explainer split.

Lines:
1. Bookends inherited from ai-explainer — cold open, hesitant writer, verdict, YOUR TURN, outro.
2. Middle owned by this skill — multi-act body, VOX LAW, pantry, shopping list.
3. Two hard gates on top — slate previz first, shopping list after audio lock.

Narration:
> So the split. Bookends inherited. Middle owned. Two gates on top. Reach for deep-explainer when the source is multi-act — several mechanisms, each needing its own evidence. Reach for ai-explainer when it is one insight.

## B15 — YOUR TURN (ClaudeComposerAsk)

Greeting: `Your turn.`
Command:
```
claude "read skills/make/deep-explainer/SKILL.md, then plan a 5-10 minute deep-explainer of a chapter I care about. Show me the act map and the lane histogram before you author a single beat. If the source is one insight, tell me to use ai-explainer instead."
```

Narration (read aloud + discussed):
> Your turn. Paste this into Claude. It asks the skill to plan an episode of a chapter you care about — and to show you the act map and the lane histogram BEFORE it authors a single beat. Look for two things in the reply. First, does it name several linked mechanisms? Second, does it push back and send you to ai-explainer when your source is really one insight? Both answers matter.

## B16 — outro (ClaudeTitleOutro)

Title: `The deep-explainer Skill.`

Narration:
> The deep-explainer Skill. Liam, in for Bear, for at Humanitarians A-I.
