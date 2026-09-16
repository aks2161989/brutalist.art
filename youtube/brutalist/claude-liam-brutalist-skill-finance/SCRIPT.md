# SCRIPT — The finance Skill (claude-liam · Brutalist · Teardown)

Persona: **Liam, in for Bear** · Voice: Kokoro `am_onyx` · Channel: @HumanitariansAI

Register: Teardown. Every acronym expanded on first use. Numbers said the way a person says them. The card carries the term; the voice explains what it means.

---

## B00 — Cold open (ClaudeComposerAsk)

> Hola, this is Liam, in for Bear. Today we tear down the finance skill. It is the first fully templatized reel in the toolkit — same eleven beats, same five charts, every company, every quarter — because the accounting standard already fixed the shape. Here is the mental model.

Composer output lines:
- eleven beats, five charts — every quarter, every ticker
- data from SEC EDGAR — never retyped
- two audits gate every render — reconcile · source

---

## B01 — BLUF (BrutalistHesitantWriter)

> The easy read — the one the word "template" invites — is that finance picks a chart. It does not. The accounting standard picks the chart. The skill only draws it. That is why a bar chart where the specification calls for a Sankey is not a near miss — it is the failure mode.

Written text:
```
The finance skill
picks the chart.
The accounting standard
picks the chart.
```
Trigger: `picks the chart.` → `only draws it.`

The correction — read back: "The finance skill / only draws it. / The accounting standard / picks the chart." That is the reel's claim.

---

## B02 — FRAMEWORK · Anatomy (SkillTeardownAnatomy)

> First the anatomy. On the toolkit side, one folder — SKILL markdown, the doctrine, plus a data pull script and four chart components — Sankey, mirrored bar, stacked bar, dot plot. On the fellows side, a per-ticker episode folder holding a JSON file of facts pulled from SEC EDGAR, a source-audit report, and the beat sheet. Every number on screen traces back to that facts file. No number is ever typed into a component.

---

## B03 — FRAMEWORK · Pipeline (SkillTeardownPipeline)

> The spine is fixed. Eleven beats. Trigger, executive summary, source card — then the four charts in order — income statement Sankey, cash flow Sankey, balance sheet mirrored bar, segments stacked bar, sector distribution dot plot. Then what to look out for, your turn, outro. No beat is ever dropped. A company with no segment disclosure still renders beat seven and says so — absence of a disclosure is itself a data point.

---

## B04 — MECHANISM 1 · Shape logic locked (SkillTeardownMechanism)

> First design decision, and it is the sharpest. Shape logic is locked. Flow gets a Sankey — that is the income statement and the cash flow. A snapshot gets a mirrored bar — that is the balance sheet. Composition over time gets a stacked bar — that is segments. And picking otherwise is not a style choice — it is a factual misrepresentation. A balance sheet drawn as a Sankey reads as motion — assets becoming liabilities — which is false. That is why the mirrored bar is the default even though it is less flashy.

---

## B05 — MECHANISM 2 · Never retyped (SkillTeardownMechanism)

> Second decision. No number is ever retyped. The data comes from the U.S. Securities and Exchange Commission's EDGAR XBRL JSON application — ticker to central index key, then company facts for every tagged fact, then frames for the sector comparison. Every fact carries its own accession number, form, fiscal year, and period end — on chart provenance for free. The runtime writes those facts to a data file. The chart components read only from that file. Grep the components for hard coded numbers, and the build fails if any exist. Plus two hard rules from SEC — a user agent naming your organization, and ten requests per second maximum. Without them, the servers return four zero three.

---

## B06 — MECHANISM 3 · The two audits (SkillTeardownMechanism)

> Third decision, and it is where the skill earns its trust. Two independent, deterministic audits gate every render. AUDIT RECONCILE checks the charts against their own arithmetic — income statement columns reconcile, cash flow sources equal uses, balance sheet assets equal liabilities plus equity, computed from line items not a stored total, segments sum to the fiscal year total. AUDIT SOURCE checks the charts against EDGAR — every rendered number equals its XBRL fact by tag and value. They are independent by construction. One checks internal arithmetic. The other checks external truth. They cannot fail the same way. Both fail the build. Never render past a failed audit.

---

## B07 — MECHANISM 4 · Colour is not the only channel (SkillTeardownMechanism)

> Fourth decision, and it is the one that most people get wrong. Profit is bluish green. Loss is vermilion. These are the Okabe Ito colours — they stay distinguishable under red green colour blindness, unlike pure red and green. But — and this is the sharp condition — they have almost the same brightness. In greyscale they become identical blobs. So colour may reinforce profit versus loss. It may never be the only thing carrying it. Every profit loss distinction is also encoded — by geometry, by the sign on the number, or by the label. Desaturate the rendered frame. If profit and loss go ambiguous, the beat fails, regardless of how correct the colours are.

---

## B08 — FALSIFIABILITY · The bank trap (SkillTeardownMechanism)

> Falsifiability, and this is where the template breaks. The income statement Sankey assumes revenue, then cost of goods, then gross profit. Banks have no cost of goods sold — they have net interest income. Insurers run on premiums and reserves. Real estate investment trusts headline funds from operations. Running this template across the S&P five hundred would render structurally meaningless charts for the financial and real estate sectors. So this skill deliberately targets the Nasdaq one hundred, which excludes financials by construction. Financial companies get a second template. If you force a bank through this one, the audit will not catch it — because arithmetically it reconciles. It is just teaching a lie. The skill knows its own limit.

---

## B09 — VERDICT (ClaudeVerdictArtifact)

> The verdict. Finance is the first template in the toolkit that does not need a design decision at build time — the accounting standard already made it. Shape logic is locked, so chart choice is a factual claim about which statement you are drawing. Every number is a JSON fact pulled from EDGAR — not a retyping. Two independent audits gate the build — reconcile checks the arithmetic, source checks against the filing. Profit and loss are always encoded twice, because greyscale kills the colour alone read. And the template knows its limit — it stops at the edge of the Nasdaq one hundred, because banks were never in scope. Skip any one of these, and the reel earns the boilerplate charge it exists to refute.

---

## B10 — YOUR TURN (ClaudeComposerAsk, greeting "Your Turn")

> Your turn. Paste this into Claude Code. Read skills slash make slash finance slash SKILL markdown. Then, without running any network calls, plan — do not build — a dry run finance episode for a hypothetical ticker. Draft the composer ask, the executive summary card, the source card with a fabricated but labelled accession number, and the four chart component prop blocks with tiny sample data. For each chart, write down which SKILL rule fixed that chart type. And answer three questions. Does every chart trace to the facts file. Is every profit loss distinction encoded twice. Would the two audits — reconcile and source — both wire up cleanly on the props you drafted. Read what Claude wrote before you build anything.

---

## B11 — OUTRO (ClaudeTitleOutro)

> That was the finance Skill. Liam, in for Bear.
