# PROMPTS — The finance Skill teardown

Nothing in this reel calls a paid API. The only paste-ready prompt in the film
is the B10 Your Turn — a planning exercise the viewer runs on their own
Claude Code install. It never invokes the network.

## B00 — the Ask (visualized in the composer, not a prompt to run)

```
What is the `finance` skill? Read skills/make/finance/SKILL.md and tell me what it really does with a public company's filings.
```

Displayed inside `ClaudeComposerAsk`. The output lines beneath show what the
teardown will explain — three receipts a viewer joining mid-frame can read.

## B10 — the Your Turn prompt (viewer-paste, planning only)

```
Read skills/make/finance/SKILL.md. Then, WITHOUT running any network calls,
plan (DO NOT BUILD) a dry-run finance episode for a hypothetical ticker.

Draft, on paper:
  1. The ClaudeComposerAsk cold open (greeting + typed command + expected
     output lines a viewer joining mid-frame could read).
  2. The executive summary card headline for the fiscal year.
  3. The source card — form, period, filed date, and a clearly-labeled
     FIXTURE accession number (never a fabricated real one).
  4. Prop blocks for the four chart components — FinanceSankey (income),
     FinanceSankey (cash flow), FinanceMirroredBar (balance sheet),
     FinanceStackedBar (segments) — each with tiny sample data drawn from
     the skill's own example structure. Do not invent XBRL tag names —
     use the ones the SKILL.md names.
  5. For each chart, name the SKILL.md rule that fixed that chart type.

Then answer three questions in the same reply:
  a. Does every rendered number on every chart trace back to a single facts
     file, or is any component holding a hard-coded numeric constant?
  b. Is every profit / loss distinction encoded twice — by colour AND by
     geometry, sign, or label?
  c. Would the two audits (RECONCILE + SOURCE) both wire up cleanly on the
     props you drafted? If AUDIT-SOURCE would have nothing to compare
     against, say so and mark the fixture accordingly.

Do NOT call sec.gov, do NOT fabricate a real accession number, and do NOT
run generate_audio_kokoro.py or compile.py. Read what Claude wrote before
you build anything.
```

## Why this handoff earns the beat

- It EXTENDS the film's argument (shape-lock, never-retyped, two audits,
  greyscale test) into the viewer's own work.
- It is safe: dry-run, no network, no fabrication, no build. It teaches the
  gate discipline the film argues for.
- It reads and discusses: the narration (see B10 in SCRIPT.md) reads the
  prompt aloud verbatim and then names the three questions the viewer
  should look for in Claude's answer.

## No other paste-ready prompts

Nothing else in this film is a prompt the viewer should copy. The composer
appearance at B00 is an *ask* being answered on screen, not a task to hand
off. Body beats are concept illustrations, not command lines.
