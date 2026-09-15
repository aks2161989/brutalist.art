# Math in films — all builders, both aspects

Mathematical notation must communicate its structure, not imitate it with a
line of prose. This applies to every film, including AI/deep/CLI explainers,
game-development films, reviews and Shorts. The tool is optional; the result
is not. Use MathTex, KaTeX, MathJax, MathText SVG, MathML or an equivalent
structured layout. No LaTeX installation is required if another route works.

- Set fractions with a real fraction bar when the grouping matters. Keep
  numerator and denominator visibly grouped. Use proper subscripts,
  superscripts, radicals, summation indices and sized delimiters. Variables
  are italic; operators such as exp/log/max are upright.
- Never place raw TeX, underscore indices, caret powers, or long ambiguous
  `a / b * c` / `a ÷ Σ b` strings in ordinary quote/title/text cards. Short
  unambiguous arithmetic or single symbols are fine; actual program source
  remains verbatim code and is labeled as code, not a typeset equation.
- Never silently fall back from a missing math renderer to ordinary text.
  Select another working renderer or report the affected beat as blocked.
- Verify the algebra separately from the typography: free versus bound
  indices, signs, factors, domains (e.g. T > 0), equality versus approximation,
  and at least one reproducible numerical case where applicable. Pretty
  typography is not a correctness check.
- Reveal a derivation in readable stages. Align relations, explain symbols,
  and leave each expression long enough to read. Split across beats instead
  of shrinking the complete derivation. Do not animate through invalid equalities.
- Inspect actual equation frames at their revealed states and at 15/50/85%
  of each affected beat, in the final output aspect. Check fraction bars,
  indices, glyphs, clipping and readability at ordinary viewing size, not
  only a 4K probe or a general text-density score. Record results in the
  reel's QC report and algebra corrections in FACTCHECK.md.

Existing films: preserve the previous review, correct the authored source and
beat sheet, regenerate only changed visuals/audio, and recompile through the
normal gates. An unrelated slate remains a slate; a math repair does not
certify a previously incomplete film as a final.
