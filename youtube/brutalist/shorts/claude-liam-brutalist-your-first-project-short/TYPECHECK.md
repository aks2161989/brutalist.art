# TYPECHECK.md — Your First Brutalist Project (Short, 9:16)

## Absent legacy checker

`runtime/scripts/type_check.py` and `runtime/reference/type-spec.md` are NOT present in this isolated toolkit. The AI Explainer SKILL.md references GATE T (type-scale enforcement) but the checker binary does not ship in this cut. Repair path (per the brief): **fix the reel, not the check** — no bypass, no invented run, no stubbed script. The parent portrait companion documented the same gap.

## What was actually checked (manual visual typography)

Every retained beat's media file was inherited unchanged from the parent portrait companion (verified via SHA-256 in `exports/short/*.verified.json`), so the parent's Gate-V-tuned typography carries into this Short. In addition, this Short's own final MP4 was sampled and inspected via the image-capable Read tool at beat-relative 15%, 50% and 85% steady-state frames.

Per-beat typography verdict:

| Beat | Composition | Face/size class | Verdict on this Short's sample |
|---|---|---|---|
| B00 | `ClaudeComposerAsk916` | Sans monospace command; serif "Your First Project" heading; sans folder chip | Clean; command reads on one to two lines; four-line answer readable at 85%. Terracotta only on send. |
| B01 | `BrutalistHesitantWriter916` | Serif poster, tuned to `fontSize 340 / lineSpacing 1.24` | Six stacked lines span ≥70% of safe height at steady state; correction sweep visible earlier; period lands. |
| B03 | `ClaudeComposerAsk916` | Same class as B00 | Command wraps to two lines; three-line output resolves. |
| B04 | `ClaudeVerdictArtifact916` | Serif card title/heading; sans line list with terracotta numerals | Card sizing (post-tune: title 0.024, heading 0.034, line 0.023) fills safe area; seven numbered lines all legible. |
| B05 | `ClaudeVerdictArtifact916` | Same class as B04 | Six numbered lines legible; "review-cut.mp4" title in code face; no line clipped. |
| B10 | `ClaudeComposerAsk916` | Same class as B00 | Paste-ready command wraps to four lines with placeholder visible; GOOD/BAD output in terracotta highlight. |
| B11 | `ClaudeTitleOutroHAI916` | Serif poster title; sans handle; small-caps sub-mark | Title fills two lines; terracotta period; handle beneath; "BRUTALIST — 03" sub-mark; hairline rules top/bottom. |

## Ratio / dimension

`ffprobe` on the final MP4 reports `2160×3840`. Each source `media/<BID>.mp4` is `2160×3840` (native portrait). No cropping or upscaling was performed by `shorts.py` (the "native portrait reused unchanged" fast path was taken for all seven retained beats).

## Captions

`metadata.captions: false`. No SRT/VTT/burned-in transcript exists for this Short. The compiler did not emit any.

## Gaps recorded honestly

- No automated type-metric numbers (font-height ratio, line-height ratio, column width) because the checker binary is absent. Manual inspection at three moments per beat is what stands in for it.
- No live type-spec regression testing between the parent and this derivative — the retained beats share byte-identical media with the parent (SHA-256 verified), so no drift is possible.
