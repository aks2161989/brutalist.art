# TYPECHECK — vertical (9:16)

## Runtime type checker (Gate T)

Same gap as landscape: `scripts/type_check.py` is not present in this toolkit snapshot.
No fabricated pass; the honest record is that the runtime checker did not run.

## Frame-level typographic review (portrait)

Ten stills from the finished 4K portrait master read individually. Observations:

- **Serif and mono families** identical to landscape — EB Garamond for greetings,
  segment titles, spark lines, verdict, outro title; SF Mono / Menlo for the code
  cards' body and the mono ticker under the composer.
- **Terracotta is the ONE accent** on every portrait frame that carries it (send
  button on the composer beats, trigger words during B01 hesitation, the traffic-light
  dot on code cards, the period on the outro title).
- **B01 portrait coverage** — the initial 2-line 240px layout produced 32% bbox
  coverage of the portrait safe area (Gate-V MAJOR `underfill`). Restructured to
  three lines at `fontSize: 300`, `lineSpacing: 3.4` — final render clears the 55%
  floor. Frame `bluf.png` confirms.
- **B10 portrait bleed** — the initial `Audit a fellows reel's approvals — do NOT
  sign for me` segment title bled past the title-safe right edge (Gate-V BLOCKER
  `edge-bleed`). Shortened to `Audit — never sign`; abridged command; three tight
  output lines. Frame `your-turn.png` confirms.
- **B02-B08 portrait code** — LIMITATION carried forward from ep 29 `art run`:
  monospace lines wider than the card's inner width truncate at the card's right
  edge. Ink stays inside the white card, so no title-safe bleed. Gate-V passes.
  The salient part of each line — the case pattern, the filename, the flag name,
  the exit status — is preserved. The full lines are on screen in the landscape
  master and in `demo/RUN-LOG.txt`. Not silently swallowed; called out in
  `CHECKS-REPORT.md` and the video's own `_qc/REPORT.md`.

## Kerning / overflow / min-size on portrait

- **§8.1 min-size** — portrait body copy at `height * 0.022` ≈ 42px (1920 tall);
  greetings, segment titles, spark lines even larger. Well above WCAG floor.
- **§8.2 overflow** — final Gate-V pass reports zero edge-bleed after B10 fix.
- **§8.3 contrast** — identical palette; separation clears WCAG.
- **§8.4 kerning sanity** — same bundled TTF families; no substitutions.
- **§8.5 no-wordy-card** — B09 verdict lines stagger through the beat; not a
  wall-of-text.
- **§8.6 golden strings** — every visible string is real: from `art`,
  `build_safety.py`, or `demo/RUN-LOG.txt`.

## Conclusion

Portrait typography reviewed frame by frame. All Gate-V checks pass. Long code
lines truncate on the right in portrait — an accepted limitation shipped by ep 29
and preserved here for review. Human review pending.
