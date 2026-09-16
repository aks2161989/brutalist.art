# SCRIPT — The logo-motion Skill

Persona: Liam (in for Bear). Voice: Kokoro `am_onyx`. Register: Teardown.
Channel: @HumanitariansAI (Brutalist playlist).

## B00 — ASK (cold open, ClaudeComposerAsk)
Hola, this is Liam, in for Bear. Today we tear down the logo-motion skill. It is
the one composition that drives every logo sting — the mark, the wordmark, the
tagline, the palette, and the LENGTH are all props. A new brand is a traced part
list plus a props block. Not a new scene file. Here is the mental model.

## B01 — BLUF (BrutalistHesitantWriter)
The easy read — the one every reel that copied the Musinique sting followed — is
that a new logo needs a new scene file. It does not. logo-motion collapses eight
duplicated showcase files into ONE composition. If you find yourself copying
LogoMotion dot t s x, stop. The thing you want is a prop that does not exist
yet. Add the prop.

## B02 — FRAMEWORK · ANATOMY (SkillTeardownAnatomy)
First, the anatomy. On the skill side, SKILL dot md holds the doctrine and
reference slash TIMING dot m d holds the phase map — measured off two real
stings, not eyeballed. Alongside them, scripts slash trace underscore logo dot
p y turns a raster mark into an animatable part list. The scene it drives is
LogoMotion dot t s x — one composition, all props. It reads from a LOGOS
registry — one line per brand — and each entry points at a per-brand parts dot
t s file. The consumer is the reel's beat sheet — a props block that names the
logo key and passes wordmark, tagline, palette, and length.

## B03 — FRAMEWORK · PIPELINE (SkillTeardownPipeline)
The flow is four steps. Trace the mark into pieces — trace underscore logo dot
p y crops to ink, upsamples four times, labels eight-connected components, and
traces each one separately with potrace. Measure the lockup — take ink bounding
boxes off a settled frame and put them into the scene as fractions, and
position type by cap top, not by box top. Set the phase map — buildStart zero
point zero three, ghost hold to zero point four four, materialise to zero point
eight three. Then render and LOOK — pull a contact sheet. Never trust the
probe. A ghost that is too short is invisible to ffprobe and obvious in a frame
grid.

## B04 — MECHANISM ACT 1 (SkillTeardownMechanism · camera move)
First design decision. The build is a camera move. The naive version staggers
the traced parts inward on their own radial vectors, and calls that the
geometric transition. At ghost opacity nobody can see it. The client's own
words on the first cut of the Medhavy sting were, quote, it's just appearing.
They were right. So the reference opens on an extreme close-up — the mark at
six point five times scale, tilted nineteen degrees, filling and overflowing
the frame — and pulls back to the settled lockup. Ease it hard. The big move
is over early and the last third of the pull-back is a crawl. That is what
makes it land, rather than stop.

## B05 — MECHANISM ACT 2 (SkillTeardownMechanism · ghost hold)
Second decision. This is the whole architecture. The mark enters as a
near-invisible emboss — pressed into the page, readable only as a shadow edge
and a highlight edge — and stays that way for roughly the first half of the
runtime. Then it materialises. One slow, continuous ramp from emboss to full
ink. Measured in luma standard deviation across the reference sting, five
percent contrast at p equals zero point three six, fifty percent at zero point
six four, ninety-five percent at zero point eight zero. Forty-four percent of
the runtime spent nearly invisible is not dead air being tolerated. It is the
mechanism. The materialisation only reads as an arrival because there was
nothing to arrive from.

## B06 — MECHANISM ACT 3 (SkillTeardownMechanism · length is a prop)
Third decision. Length is a prop, not a re-time. durationInSeconds enters as a
prop. calculateMetadata turns it into durationInFrames. Every ramp in the
scene is a fraction of the total — buildStart zero point zero three, ghost
zero point four four, materialise zero point eight three. So a four-second
cut and a nine-second cut are literally the same animation, at different
speeds. Never fork the scene to change length. Never eyeball a re-time. And
this is deliberate — everywhere else in the toolkit duration falls out of
measured narration. A sting is a fixed-length slot; a pre-roll is five seconds
because the channel says five seconds. Length is INPUT here, and only here.

## B07 — MECHANISM ACT 4 (SkillTeardownMechanism · audio-first exception)
Fourth decision, and it is the exception that proves the toolkit rule.
logo-motion is the one place in this toolkit where audio does NOT set the
shape. Every other beat conforms to measured narration. Not this one. A sting
reproduces a known motion. Re-timing the materialisation to land on a spoken
word breaks the curve that makes it work. So the rule inverts. Run the
transition to completion, then start the voice. Runtime becomes an output —
transition, plus silence-trimmed narration, plus a short tail. If a supplied
track carries leading silence, trim it before offsetting, or the voice starts
late by exactly that much. On the Medhavy sting the leading silence was eight
hundred and eighty milliseconds. That would have put the first word almost a
full second inside a dead beat.

## B08 — FALSIFIABILITY (SkillTeardownMechanism · three tells)
Falsifiability. When a sting looks cheap, TIMING dot m d gives you a diagnostic
order. Check three things. Does the mark arrive at full strength? If yes, that
is the bug. There is no ghost phase and nothing can materialise. Is there a
chrome or gloss or bevel sweep? A hard-edged metallic gradient crossing a flat
mark is the clearest tell of a stock template — and it renders the brand
colour wrong for the whole time it passes. Does colour arrive during motion?
Then it reads as part of the motion, rather than as an event. The Medhavy
sting this skill was first used to fix had all three, at once. It popped the
full lockup in two hundred and seventy milliseconds, held, then swept a silver
gradient across a black mark — turning the brand mark grey for twenty percent
of the runtime. Three tells, one wrong sting.

## B09 — VERDICT (ClaudeVerdictArtifact)
The verdict. logo-motion is one composition, every mark — the parts, the
wordmark, the tagline, the palette, and the length are all props. The build
is a camera move — extreme close-up, pull back, ease hard. The ghost hold is
the whole effect — forty-four percent of the runtime nearly invisible, then
one slow materialisation. Length is a prop, never a re-time — every ramp is a
fraction of the total. It is the toolkit's audio-first exception — the
transition curve wins, the voice waits. And a cheap sting fails in a fixed
order — full-strength arrival, chrome sweep, colour during motion.

## B10 — YOUR TURN (ClaudeComposerAsk · greeting "Your Turn")
Your turn. Paste this into Claude Code. Read skills slash make slash
logo-motion slash SKILL dot m d and reference slash TIMING dot m d. Take a
logo sting you already have — any format Remotion can decode. Extract one
frame per second with ffmpeg, and compute the luma standard deviation inside
the mark's bounding box across the whole runtime. Find where contrast crosses
five percent, fifty percent, and ninety-five percent, as fractions of total
runtime. Compare those crossings against zero point three six, zero point
six four, and zero point eight zero. If yours cross earlier, your ghost hold
is too short. If they cross later, your materialisation is too slow. That is
the measurement the skill was built to make cheap.

## B11 — OUTRO (ClaudeTitleOutro)
That was the logo-motion Skill. Liam, in for Bear.
