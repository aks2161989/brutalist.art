# TYPECHECK.md — The deep-explainer Skill (landscape, run_id 9a0276f36c7f460da489b867130af37b)

## Referenced type checker

The public docs reference `scripts/type_check.py` and `reference/type-spec.md`.
Neither ships in this isolated toolkit copy. Nothing that ran during this build
claims a pass from a checker that is not present.

## What actually ran instead

- **runtime/qc/final_frame_check.py (Gate V)** — sampled 30 frames from the
  final 4K mp4 (each beat at 50% and 85% of duration), enforces FILL_MIN ≥ 0.55
  canvas-fill law plus title-safe edge-bleed and luminance separation.
  Result: 0 BLOCKER, 0 MAJOR.
- **compile.py verify_output** — decoded candidate mp4, confirmed exact
  dimensions and positive audio duration; atomic-wrote master + .verified.json.
- **build_safety.validate_project** — approved project shape (unique beat_ids,
  metadata required keys, audio_file paths, no PUNT).
- **Visual typography inspection (this invocation)** — frames extracted at
  B07 15%/50%/85%, B00 50%, B14 50%, B16 50%, B01 50% and inspected via Read:
  - B07 SkillTeardownMechanism: "Executed examples first." heading EB Garamond
    large serif, legible at render scale; body paragraph in smaller serif,
    full two-line wrap visible; quote card monospace legible; verdict pill
    "EXECUTED EXAMPLES FIRST" terracotta, within safe area.
  - B00 ClaudeComposerAsk: greeting, ask, and output lines legible.
  - B14 ClaudeVerdictArtifact: six verdict lines, all readable.
  - B16 ClaudeTitleOutro: title serif large, handle and mascot clear.

## Conclusion

No fabricated pass from a missing checker. Gate V ran on the actual final 4K mp4
and reported clean. Type and kerning conformance beyond Gate V's heuristics
remains a human-review item.
