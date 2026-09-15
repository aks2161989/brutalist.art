# Fact Check — Brutalist Utility: beat_lint.py

All claims verified against the source file `runtime/qc/beat_lint.py` (read from isolated toolkit).

## Verified claims

| Claim | Verification |
|---|---|
| Exit 2 on any defect, 0 clean | Lines 128–129: `return 2 if defects else 0` |
| Usage: `beat_lint.py <reel_dir_or_beat_sheet.json> [--quiet]` | Lines 116–120: argparse setup |
| TEXT_CARD_PATTERNS includes slatecard, textcard, titlecard, cardtext, quotecard | Line 29 |
| EXEMPT_LANES: bookend, ask, card | Line 30 |
| GRAPHIC_LANES: manim | Line 31 |
| Older sheets without lane are not re-litigated | Lines 104–106: condition `if lane == "remotion"` only fires when lane is explicitly set |
| load_beats() accepts reel dir or direct .json path | Lines 34–37 |
| RULE 7 reads brand_labels.json from same directory as the script | Lines 55–59 |
| Unknown channels skip branding check (returns empty list) | Lines 66–68: `if not want: return out` |
| VOX-ANIM placeholder is exempt | Lines 46–48: checks lane==vox AND (placeholder=="vox-anim" OR scene_type=="vox-anim" OR pattern.lower()=="voxanimslate") |
| STILL placeholder (type STILL or COMPOSITE) is exempt | Lines 41–43 |
| Defect message gives exact fix options | Lines 109–112: "Give it a real illustration pattern OR convert to a VOX-ANIM placeholder" |

## Demo verification (observed outputs, 2026-09-15)

Clean fixture (demo/fixture_clean.json):
```
[beat-lint] clean — beat mix OK (fixture_clean.json)
exit=0
```

Defect fixture (demo/fixture_defect.json) with SlateCard and TextCard in lane:remotion beats:
```
[beat-lint] 2 defect(s) in fixture_defect.json:
  B03  [single-sentence-remotion] lane:remotion beat uses text-card pattern 'SlateCard' — a talking slide. Give it a real illustration pattern OR convert to a VOX-ANIM placeholder (lane:vox, placeholder:vox-anim).
  B05  [single-sentence-remotion] lane:remotion beat uses text-card pattern 'TextCard' — a talking slide. Give it a real illustration pattern OR convert to a VOX-ANIM placeholder (lane:vox, placeholder:vox-anim).
exit=2
```

## Claims NOT made (limitations logged)

- The tool does NOT catch quality problems with illustrations (e.g. a ShellSession showing irrelevant content).
- The tool does NOT check whether vox-anim or STILL placeholders are ever filled.
- The tool does NOT audit patterns not in the TEXT_CARD_PATTERNS set.
- RULE 7 only applies to channels explicitly listed in brand_labels.json. claude-liam is not listed (by design).

## Teardown register check

No forbidden phrases used ("innovative", "revolutionary", "obviously", "clearly", "premium", "sleek" without functional definition). All claims reference observed source code or actual CLI output. Script judges the design: what the tool gets right (plan-time, specific failure mode, fix instruction in the error message) and where it bites (scope limitation, no quality check).
