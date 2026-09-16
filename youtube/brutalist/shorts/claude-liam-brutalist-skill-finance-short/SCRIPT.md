# SCRIPT — The finance Skill — Short

Seven kept beats derived from the 12-beat portrait master (parent SHA-256
`15c8209ca63fc8c820fc4f78112955dec5f81c12b1d9eab02f0887d1754b353b`).
Total measured runtime 169.9s. Strictly under 3:00. See `CUT-PLAN.json`
for the whole-beat cut rationale.

## B00 — ASK (cold open, 15.03s)

> Hola, this is Liam, in for Bear. Today we tear down the finance skill.
> It is the first fully templatized reel in the toolkit — same eleven beats,
> same five charts, every company, every quarter — because the accounting
> standard already fixed the shape. Here is the mental model.

Scene: `ClaudeComposerAsk916`. Claude UI cold open.

## B01 — BLUF (14.70s)

> The easy read — the one the word template invites — is that finance picks
> the chart. It does not. The accounting standard sets the chart. The skill
> only renders it. That is why a bar chart where the specification calls for
> a Sankey is not a near miss. It is the failure mode.

Scene: `BrutalistHesitantWriter916`. Typed BLUF with correction.

## B04 — MECHANISM Act 1: Shape logic, locked. (26.70s)

> First design decision, and it is the sharpest. Shape logic is locked. Flow
> gets a Sankey — that is the income statement and the cash flow. A snapshot
> gets a mirrored bar — that is the balance sheet. Composition over time gets
> a stacked bar — that is segments. And picking otherwise is not a style
> choice. It is a factual misrepresentation. A balance sheet drawn as a
> Sankey reads as motion — assets becoming liabilities — which is false.
> That is why the mirrored bar is the default even though it is less flashy.

Scene: `SkillTeardownMechanism916`.

## B05 — MECHANISM Act 2: Never retyped. (37.10s)

> Second decision. No number is ever retyped. The data comes from the U.S.
> Securities and Exchange Commission's EDGAR X B R L application. Ticker to
> central index key, then company facts for every tagged fact, then frames
> for the sector comparison. Every fact carries its own accession number,
> form, fiscal year, and period end — on chart provenance for free. The
> runtime writes those facts to a data file. The chart components read only
> from that file. Grep the components for hard coded numbers, and the build
> fails if any exist. Plus two hard rules from SEC — a user agent naming
> your organization, and ten requests per second maximum. Without them, the
> servers return four oh three.

Scene: `SkillTeardownMechanism916`.

## B06 — MECHANISM Act 3: Two audits. Both fail. (36.90s)

> Third decision, and it is where the skill earns its trust. Two independent,
> deterministic audits gate every render. Audit reconcile checks the charts
> against their own arithmetic — income statement columns reconcile, cash
> flow sources equal uses, balance sheet assets equal liabilities plus
> equity, computed from line items not a stored total, segments sum to the
> fiscal year total. Audit source checks the charts against EDGAR — every
> rendered number equals its X B R L fact by tag and value. They are
> independent by construction. One checks internal arithmetic. The other
> checks external truth. They cannot fail the same way. Both fail the build.
> Never render past a failed audit.

Scene: `SkillTeardownMechanism916`.

## B09 — VERDICT (36.03s)

> The verdict. Finance is the first template in the toolkit that does not
> need a design decision at build time — the accounting standard already
> made it. Shape logic is locked, so chart choice is a factual claim about
> which statement you are drawing. Every number is a JSON fact pulled from
> EDGAR — not a retyping. Two independent audits gate the build — reconcile
> checks the arithmetic, source checks against the filing. Profit and loss
> are always encoded twice, because greyscale kills the colour alone read.
> And the template knows its limit — it stops at the edge of the Nasdaq one
> hundred, because banks were never in scope. Skip any one of these, and the
> reel earns the boilerplate charge it exists to refute.

Scene: `ClaudeVerdictArtifact916`.

## B11 — OUTRO (3.40s)

> That was the finance Skill. Liam, in for Bear.

Scene: `ClaudeTitleOutro916`.

## Dropped in the Short (see the 16:9 long)

- **B02 — Anatomy** (folder layout, doctrine, pipeline script)
- **B03 — Pipeline / eleven-beat spine**
- **B07 — Colour + geometry double-encoding** (compressed inside B09 verdict)
- **B08 — Nasdaq-100 falsifiability edge cases** (compressed inside B09 verdict)
- **B10 — Your Turn planning prompt** (full prompt available in the long)
