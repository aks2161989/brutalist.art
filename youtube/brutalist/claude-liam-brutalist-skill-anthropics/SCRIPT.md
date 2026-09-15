# SCRIPT.md — The anthropics Skill

*Brutalist playlist · Episode 05 · @HumanitariansAI ·
Liam (in for Bear) · Kokoro `am_onyx` · No captions.*

Skill-teardown of `skills/make/anthropics/SKILL.md`
(SHA-256 `9189aa89c3995fc581d9f0ef1fa0b4a4913cd253e6fbfb791b4085f86c890755`).
The register is Teardown (Feynman × MKBHD): explain the mechanism, judge the design.

---

## B00 — Cold open (ClaudeComposerAsk)

> Hej, this is Liam, in for Bear. Today we tear down a skill that isn't about
> making a Brutalist reel. It's about reading a whole company's output — code,
> papers, content, capabilities — and reporting from your own bench, not from
> the press release. It's called `anthropics`. Here's how it actually works.

## B01 — BLUF (BrutalistHesitantWriter)

> The easy read of a skill named for a company is that it's another Claude
> tutorial series. It isn't. It's a beat — journalism sense — that reads the
> artifact, not the docs. Everything the skill does exists to keep it honest
> when the docs would rather do the explaining for it.

Hesitant text (final, corrected): "The anthropics skill is a tutorial channel.\nIt reads the artifact, not the docs."
Trigger phrase: `tutorial channel` → `journalism beat`.

## B02 — FRAMEWORK · Anatomy (SkillTeardownAnatomy)

> A skill is a folder Claude reads first. The anthropics skill is small on
> disk: one SKILL file, one hundred and forty-two lines, sitting under
> skills slash make. What's big is what the file references — two sibling
> engines, four modes, and one hard disqualifier that every episode has to
> pass. The doctrine is short because the discipline is what does the work.

## B03 — FRAMEWORK · The mode router (SkillTeardownPipeline)

> One router, four modes. Dash-repo dispatches to git-explainer's analysis
> engine. Dash-paper dispatches to ai-paper. Dash-content asks what has
> changed since the material was published. Dash-capability runs the thing
> and shows the real output — often side by side against a competitor. That
> last mode is the whole reason this skill exists. No vendor channel will
> ever ship it.

## B04 — MECHANISM · The disqualifier (SkillTeardownMechanism)

> First design decision, and it's the whole thesis. Quote from the SKILL
> file: "If the episode could be made by reading the docs, it is not this
> series." Every episode needs at least one spine beat that is only visible
> by opening the artifact and running it. Point at that beat, or the
> episode is not ready. The skill will report the gap rather than build
> around it. That single rule kills the ninety per cent of AI content that
> is downstream of the same three landing pages.

## B05 — WORKED EXAMPLE · The behavioural probes (SkillTeardownMechanism)

> Second decision. Structure and history come free from a repo. Behaviour is
> the thesis. So the SKILL file lists reusable probes: every URL contacted,
> every file read outside the working directory, the default value of every
> safety and privacy feature — because, quote, a feature that exists but
> ships off tells a different story than the paragraph describing it. For
> dash-paper the sharpest fair question is: does the released code
> reproduce the published claim? The honest answer is often partially, and
> that is a more interesting finding than either open-science tick or sham.

## B06 — MECHANISM · The register (SkillTeardownMechanism)

> Third decision. Register is a machine of its own. Another perspective, not
> a correction — never they're wrong or they're behind. Independence stated
> once, plainly, no hedging: builds with Claude daily, nobody's paying for
> this. Situated in a date and a real task, so the episode becomes history
> instead of going stale. And a matching claim is a finding — some repos
> are exactly what they say, and manufacturing a gap where none exists is
> the dishonesty this beat is positioned against.

## B07 — FALSIFIABILITY · Where it bites (SkillTeardownMechanism)

> Here is where the skill bites. It leans on two sibling engines — git
> dash-explainer and ai dash-paper — that aren't shipped inside this
> toolkit snapshot. Point dash-repo or dash-paper at a target and the
> router has nowhere to dispatch. The fix is to install those skills, not
> to fake the analysis. Second bite: the generation honesty law. Never
> generate an image that poses as evidence of a fact. That's a hard ceiling
> — it rules out most of what makes a video pop, and the skill accepts the
> trade because the credibility is the whole product.

## B08 — VERDICT (ClaudeVerdictArtifact)

> The verdict. The anthropics skill is a beat, not a topic. Four modes,
> one router, one disqualifier, one register. It reads the artifact rather
> than the artifact's press release, and it says so out loud. Its cost is
> depending on siblings that have to be present, and its cheat code is a
> comparison shot no vendor channel can ever ship.

## B09 — YOUR TURN (ClaudeComposerAsk)

> Your turn. Paste this into Claude Code, inside a cloned Brutalist toolkit
> where you also have the git dash-explainer and ai dash-paper skills
> installed: use the anthropics skill in dash-capability mode to compare
> Claude and one other model on a real task from your own work — a real
> file, a real prompt, a dated bench log. Then check the three questions
> the SKILL file names. Is there at least one spine beat visible only by
> running the artifact? Is every claim cited to a file line or an on-screen
> output? Did a matching claim survive? If any answer is no, don't build the
> episode. Report it instead.

## B10 — OUTRO (AntOutro / AntOutro916)

> That was the anthropics skill. Liam, in for Bear.

Restated title: **The anthropics Skill.** Handle: `@HumanitariansAI`.
Subline: `LIAM, IN FOR BEAR.`
