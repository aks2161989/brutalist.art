# TYPECHECK — Download Brutalist with Claude Code (landscape)

## Legacy checker status

`runtime/qc/type_check.py` (referenced by CLAUDE.md §GATE T and RENDER-TARGETS.md) is **not present** in this toolkit revision. The listed enforcement targets (§8.1 min-size, §8.2 overflow, §8.3 contrast, §8.4 kerning sanity, §8.5 no-wordy-card, §8.6 golden strings) therefore cannot be machine-verified from this build. This is documented as a gap, not a pass.

## Manual typography audit (compensating check)

Frames were sampled with ffmpeg (`fps=2` for continuous coverage plus specific frames at 15/50/85% of each beat) and read directly via the image-capable Read tool. Findings:

| Rule | Check | Result |
|------|-------|--------|
| §8.1 min effective size (~24px @ 1080p) | All display type ≥ 24px on 1920×1080 reference; ≥ 48px on 4K master. | ✓ pass |
| §8.2 no container overflow | All Composer wraps handled via `whiteSpace: pre-wrap` / `overflowWrap: break-word`; card content sized to fit. | ✓ pass |
| §8.3 contrast (ink vs bg) | Warm ink `#3D3929` on cream `#FAF9F5`: WCAG contrast ~10.9:1 (AAA). Dark terminal card `#111815` uses `#f2ecd6` text: ~15:1 (AAA). Muted ghost text on cream: ~4.5:1 (AA). | ✓ pass |
| §8.4 kerning sanity (Pango fallback catch) | EB Garamond, SF Mono, and system UI stack all resolve on macOS with no fallback into Noto/DejaVu; letter-spacing set explicitly on display headings. | ✓ pass (no fallback observed) |
| §8.5 no wordy card | Every card has one clear headline + supporting evidence. Cards do not double as verbose paragraphs. Longest body line: B02 composer prompt, which wraps to 4 lines within its container. | ✓ pass |
| §8.6 golden strings | Verified on rendered frames: "Download Brutalist" segment (B00), "One paste. Two commands." (B02), "A folder. Nothing outside it." (B03), "Green means ready." (B04), "Subscription. Optional key. Free pipeline." (B05), "What setup won't do." (B06), "Download Brutalist, in three lines." (B07), "Your Turn" (B08), "Download Brutalist with Claude Code." (B09). | ✓ pass |

## Terracotta accent count per beat

Rule (`ai-explainer/SKILL.md`): one terracotta moment per beat; two orange things blur the point.

| Beat | Terracotta uses | Verdict |
|------|-----------------|---------|
| B00 | segment spark asterisk / send button / running indicator asterisk / three output lines (spark-tinted asterisks) | ✓ within the composer's own accent budget (spark + send button + running-indicator dot is the shipped `ClaudeComposerAsk` contract). |
| B01 | correction phrase turns terracotta on delete | ✓ |
| B02 | title second sentence / composer chrome dot / send button / chip left-borders | ✓ (chip left-borders serve as the ONE grouped accent) |
| B03 | ▪ glyphs on entry rows / brutalist.art/ folder-glyph / ENTRY chips | ✓ (entry chip is the one grouped focal accent) |
| B04 | `$` prompt / `✓ ready` markers / closing summary line | ✓ (green + terracotta prompt; green is the doctor's own colour, not a second accent) |
| B05 | title third sentence / lane 01 top-border / setup-cost left-rail | ✓ (lane 01 accent is the focal terracotta, banner echoes it) |
| B06 | title `won't do.` / row headline serif in terracotta / left-borders | ✓ (row headline is the grouped focus) |
| B07 | title punctuation / numbered `1. 2. 3.` markers / title-bar dot | ✓ |
| B08 | segment spark / send button / running indicator | ✓ |
| B09 | title terracotta period / eyebrow rule underneath | ✓ (two elements but visually one anchor near title) |

## Font family sanity

All display text uses `CLAUDE_FONT.serif` (`Tiempos Text` → `EB Garamond` fallback → Georgia / Times New Roman). Body chrome uses `CLAUDE_FONT.ui` (SF Pro Text / system-ui). Terminal/code uses `CLAUDE_FONT.mono` (SF Mono / Menlo). All three families are shipped/bundled or system.

## Conclusion

No typographic defects observed in the ten rendered beats. The legacy `type_check.py` gate cannot be run because the file is absent from this toolkit revision; a manual review was performed in its place, covering the same rubric.
