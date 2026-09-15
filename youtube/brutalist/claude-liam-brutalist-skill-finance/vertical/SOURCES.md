# SOURCES — The finance Skill teardown

## Primary source

- `skills/make/finance/SKILL.md` — SHA-256 `b9827d21ef03a945c8fe106e32d30f804867eb083a2a63649ec16a8a8ba40eca`
  (as captured 2026-09-08 in `SOURCE-SNAPSHOT.json`; supervisor's `episode.source_sha256`
  is `00d9241ce2b96c5487542ed7807b6b3ebcad69c4ae65c855f92b4a43a33c36fe`, an earlier
  revision of the same file. This teardown reads the copy present in the isolated
  toolkit — the version that the audience will encounter today.)

## Referenced doctrine (read but not quoted)

- `skills/make/ai-explainer/SKILL.md` — skill-teardown modifier and house laws
- `skills/make/nopunt/SKILL.md` — proof gate, SHOW/HOLD/CARD classification
- `runtime/prose/teardown/PROSE.md` — register for the narration
- `CLAUDE-BRAND.md` — cream/ink/terracotta palette
- `OUTRO-LOCK.md` — @NikBearBrown outro lock for claude-liam
- `CLAUDE-CODE-VISUAL-QC-CHECK.md` — QC procedure (frame extraction + read)
- `docs/PIPELINE-SAFETY.md`, `docs/FELLOWS-SUBMISSION.md`

## Example leads (read, not republished)

Both examples are listed in `../.repoloop/workspaces/claude-liam-brutalist-skill-finance/example-sources.json`:

- `rohan-v/2026-08-28-agent-first-brutalist/beat_sheet.json` (SHA-256 `746409a8...`) — pattern
  reference for the composer ask + HAI submit patterns. Not quoted here.
- `sachin-vishaul-b/2026-08-28-finance-event-signals-week4-graded/beat_sheet.json`
  (SHA-256 `4c35b91f...`) — pattern reference for a finance-themed reel. Not quoted here.

Neither fellow's work is transcribed, reused, or presented as this run's output. Their names
and slugs remain in their own read-only folders.

## Facts asserted in the film — every one is in the primary source

| Beat | Assertion | SKILL.md anchor |
|---|---|---|
| B00 | 11 beats, 5 charts, every quarter, every ticker | §"The eleven beats" table + §"Series positioning" |
| B01 | Chart type is fixed by the accounting standard, not by build-time judgement | §opening + §"Shape logic, locked" |
| B02 | SEC EDGAR XBRL is Rung-1 data; facts land in `data/facts.json`; charts read only from that file | §"Data — EDGAR XBRL, Rung 1, never retyped" |
| B03 | Eleven-beat spine; no beat ever dropped; absence of disclosure is a data point | §"The eleven beats" + §opening rule 8 |
| B04 | Flow → Sankey; Snapshot → mirrored bar; Composition × time → stacked bar | §"Shape logic, locked" |
| B04 | A balance sheet Sankey reads as "assets become liabilities," which is false | §"Shape logic, locked" + §rule 3 |
| B05 | Every fact carries `accn`, `form`, `fy`, `fp`, `end` on-chart provenance | §"Data — EDGAR XBRL" |
| B05 | User-Agent required (else 403); 10 req/sec max (else 429) | §"Data — EDGAR XBRL" |
| B05 | Grep the components for hard-coded numerics and fail if any exist | §"AUDIT-SOURCE" |
| B06 | Two independent, deterministic audits; both fail the build | §"The two audits" |
| B06 | Balance sheet A = L + E computed from line items, not a stored total | §"AUDIT-RECONCILE" |
| B06 | Every rendered number equals its XBRL fact by tag and value | §"AUDIT-SOURCE" |
| B07 | Okabe-Ito profit `#009E73` and loss `#D55E00`; 1.13:1 luminance vs each other | §"Palette / Profit and loss" |
| B07 | Colour may reinforce profit/loss but never be the only channel | §"Palette / THE CONDITION" |
| B07 | Greyscale test enforced | §"GREYSCALE TEST" |
| B08 | Banks have no COGS — net interest income instead; insurers, REITs also different | §"Known trap — the template does not fit banks" |
| B08 | Nasdaq-100 excludes financials by construction — the better batch target | §"Known trap" |
| B10 | Trigger is `finance <TICKER>`, optional `--form 10-Q` | §"Trigger" |

## Feasibility note (SELF-DEMO LAW fallback)

The skill's live self-demo would require:

- A network call to `https://www.sec.gov/files/company_tickers.json` and to
  `https://data.sec.gov/api/xbrl/companyfacts/CIK##########.json` for a chosen ticker.
- A User-Agent header naming an organization and a contact email (or SEC returns 403).
- Rate-limited execution (10 req/sec max) plus SEC XBRL semantics for tag selection.
- The four chart-component renders and the two audits.

This build runs under the toolkit's isolated sandbox with no permitted outbound network
except localhost/127.0.0.1. A live EDGAR pull is therefore out of scope for this
invocation. Per SELF-DEMO LAW's feasibility fallback (ai-explainer SKILL.md §skill-
teardown modifier), the mechanism is taught via source-backed illustrations of the
skill's documented shape logic, audit gates, palette rules, and known trap. Every
claim on screen is anchored to a specific `SKILL.md` line in the table above.
