# FACTCHECK — The finance Skill — Short

This Short is a whole-beat cut derived from the parent portrait master
(SHA-256 `15c8209ca63fc8c820fc4f78112955dec5f81c12b1d9eab02f0887d1754b353b`).
The retained beats are B00, B01, B04, B05, B06, B09, B11 — see `CUT-PLAN.json`
and `SCRIPT.md`. Every factual claim in the retained narration is verified
against a specific span of the primary source, `skills/make/finance/SKILL.md`
(SHA-256 as recorded in the parent's `SOURCE-SNAPSHOT.json`). Nothing in
this Short asserts a claim not present there. Claims 8–11 below trace to
dropped beats (B02/B03/B07/B08/B10) and are retained here only for parity
with the parent's fact-check — the Short does not utter them, apart from
the compact restatement inside the B09 verdict (colour double-encoding;
Nasdaq-100 scope limit).

## Claims and their source spans

1. **"Same eleven beats, same five charts."**
   SKILL.md §description: "Same ELEVEN beats, same five charts, same order,
   every company, every quarter — nothing is chosen at build time except the
   ticker, because GAAP already fixed the shape."
   Verified: eleven-beat table at §"The eleven beats" (B01–B11).
   Five charts = Sankey (income), Sankey (cash flow), mirrored bar (balance),
   stacked bar (segments), dot plot (vs sector).

2. **"The accounting standard picks the chart; the skill only draws it."**
   SKILL.md §opening: "The template is not a shortcut — it is the accounting
   standard, rendered."
   SKILL.md §0.0: "…picking otherwise is a factual misrepresentation, not a
   style choice."

3. **"A bar chart where the specification calls for a Sankey is the failure mode."**
   SKILL.md §0.0: "…a bar chart where the spec calls for a Sankey is not a
   near-miss, it is the failure mode. It is the exact thing the series is
   defined against."

4. **"Data from SEC EDGAR XBRL — every number a JSON fact, never retyped."**
   SKILL.md §"Data — EDGAR XBRL, Rung 1, never retyped": "ticker -> CIK",
   "filing index", "every tagged fact", "sector population". "Every fact
   carries its own accn, form, fy, fp, end — on-chart provenance for free.
   Write the pull to `data/facts.json`; charts read only from that file. No
   numeric constant is ever typed into a component."

5. **"User-Agent required (else 403); 10 requests/second maximum (else 429)."**
   SKILL.md §"Two hard requirements or it fails": "A User-Agent naming your
   org and a contact email. Without it SEC returns 403." "10 requests/second
   maximum. Sleep ~0.12s between calls or you get 429s."

6. **"Flow → Sankey. Snapshot → mirrored bar. Composition × time → stacked bar."**
   SKILL.md §"Shape logic, locked": exact phrasing preserved.

7. **"A balance sheet Sankey reads 'assets become liabilities' — false."**
   SKILL.md §"Shape logic, locked": "ribbons read as motion, and a viewer's
   gut reading of a balance-sheet Sankey is 'assets become liabilities,' which
   is false." Also §rule 3.

8. **"Two independent, deterministic audits; both fail the build."**
   SKILL.md §"The two audits — both deterministic, both fail the build":
   AUDIT-RECONCILE + AUDIT-SOURCE.
   AUDIT-RECONCILE checks: income statement columns reconcile, cash-flow
   sources = uses (no negative ribbon), balance sheet A = L + E computed from
   line items not a stored total, per-period segments sum to that period's
   total AND periods sum to fiscal year, every non-terminal Sankey node's
   inflow = outflow. AUDIT-SOURCE checks: every rendered number = its XBRL
   fact by tag and value; every back-solved figure is dashed AND listed in B09;
   grep components for hard-coded numerics and fail if any exist.
   "They are independent by construction: one checks internal arithmetic, the
   other checks external truth. They cannot fail the same way."
   Referenced restraint: "Never render past a failed audit" (§"Never").

9. **"Profit `#009E73` and loss `#D55E00` — Okabe-Ito; 1.13:1 luminance."**
   SKILL.md §"Profit and loss — green and red, with a hard condition":
   the exact colours and contrast values are in the table.

10. **"THE CONDITION — colour may reinforce, may never be the only thing."**
    SKILL.md §"Palette": "Colour may reinforce profit-versus-loss. It may
    never be the only thing carrying it."
    Encoding channels: geometry / sign on the number / label. Each named
    explicitly in §"Palette" bullet list.

11. **"Greyscale test enforced."**
    SKILL.md §"GREYSCALE TEST, enforced": desaturate the rendered frame; if
    profit and loss become ambiguous, the beat fails.

12. **"Banks have no COGS — net interest income instead. Nasdaq-100 excludes
    financials by construction."**
    SKILL.md §"Known trap — the template does not fit banks":
    "Banks have no COGS; they have net interest income. Insurers run on
    premiums and reserves; REITs headline funds-from-operations."
    "The Nasdaq-100 excludes financials by construction, which makes it the
    better batch target."

13. **"Trigger: `finance <TICKER>`, optional `--form 10-Q`."**
    SKILL.md §"Trigger": exact.

14. **"Absence of a disclosure is itself a data point."**
    SKILL.md §"The eleven beats" trailing paragraph: "No beat is ever dropped.
    A company with no segment disclosure still renders B07 and says so — a
    filer who never trips the 10%-customer threshold has thereby proven no
    customer exceeds ~10% of revenue. *Absence of disclosure is a finding.*"
    Also §rule 8.

## De-sensationalization / rewriting the source

- SKILL.md's ten design rules and eleven beats are the doctrine; the reel
  compresses them to the four decisions that most differentiate this skill
  (shape lock, XBRL never-retyped, two audits, colour + geometry), plus the
  bank-trap falsifiability. That compression preserves each claim's substance
  and cites it above.
- "Cost of goods sold" is spoken in full in the narration (per SKILL.md
  §0.2 "Expand every acronym on first use"). The `COGS` acronym never
  appears on a card in the film, so no gloss line is required.
- "Central index key" is expanded on first use in B05 for the same reason.
- "SEC" and "GAAP" are the only bare acronyms that appear in the source
  itself; SEC is expanded once in narration ("U.S. Securities and Exchange
  Commission"). GAAP is not spoken in this reel — the term is replaced with
  "the accounting standard" throughout, which avoids the acronym entirely.
- No source datum (accession numbers, tickers, dollar figures) is fabricated
  in this reel. The mechanism is taught abstractly.

## Freshness / what may date

- The skill's referenced EDGAR URLs may change; they are true today and are
  read as documented values, not as promises about SEC's infrastructure.
- The eleven-beat spine is doctrine — it may be revised in future SKILL.md
  edits; the reel's beat count is a snapshot of the version whose SHA-256 is
  logged above.

## What is NOT claimed on screen

- No live EDGAR pull. No specific ticker's numbers. No specific accession
  number. No specific revenue or margin figure. The film teaches the
  mechanism and cites the doctrine; a full self-demo remains a per-ticker
  build that this teardown episode does not perform.
