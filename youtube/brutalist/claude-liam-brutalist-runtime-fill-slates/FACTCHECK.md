# FACTCHECK — Brutalist Utility: fill_slates.py

**Source of truth:** `runtime/scripts/fill_slates.py` (193 lines total, verified locally)
**Episode source SHA-256 (invocation):** `c0754aba4350818109b6a909922f73dd26fd6b4328b459484da2a31f279bc328`
**Current source SHA-256:** `de9efcbdc25a385a5678bde0d8093d0ede06e81da8c5c7af1efdcab2e4d7863a`
**Re-verified:** 2026-09-13 (run_id c4164e0244ae43b184b1671e8a80a477)

Every narrated claim traces to a specific block of `fill_slates.py`. Quotes in `beat_sheet.json` and the code cards are verbatim from the current file; wrapping/whitespace was trimmed for card legibility only. Nothing was invented.

| Claim / on-screen text | Line range | Evidence in source |
|---|---|---|
| "Dry-run by default; `--apply` stamps + renders + recompiles the review cut." | 12–17 | Module docstring |
| CLI surface: positional `reel`, flags `--apply`, `--books BOOKS` | 124–127 | `argparse` setup in `main()` |
| Default `--books` = `HERE.parent` (i.e. `books/`) | 22, 127 | `HERE = Path(__file__).resolve().parents[1]` then `default=HERE.parent` |
| Slate = no `media/<bid>.mp4`, no `manim/<bid>.mp4`, no `manim/<bid>.mov` | 46–50 | `slate_resolves()` |
| Also skips `silent: true` beats and beats whose `shot.remotion.pattern` is set | 60–63 | `find_slates()` |
| Headline = `_truncate(narration_text, words=11)`, fallback to `beat.name` then `beat_id` | 76–78 | `stamp_slates()` |
| `_truncate` splits on whitespace, keeps first N words, appends `…` if truncated | 29–37 | `_truncate()` |
| Stamp writes `shot.remotion = {pattern:'FormACard', provenance:'proven-core/FormACard', version:'1', props:{lines:[headline], dark:false}}` | 79–88 | `stamp_slates()` body |
| SlateCard was deleted 2026-08-26 by Bear's order; DESIGN-PRINCIPLES §1 banned the eyebrow/kicker card | 68–72 | `stamp_slates` docstring |
| Only writes `beat_sheet.json` if `changed`; write is `json.dumps(sheet, indent=1, ensure_ascii=False)` | 89–92 | `stamp_slates()` tail |
| `render_reel()` first shell-out: `python3 remotion_scenes.py <reel>` | 99–104 | `render_reel()` |
| REMOTION FAIL keeps last 300 chars of stderr and returns — never reaches `run.sh` | 105–107 | Same block |
| `render_reel()` second shell-out: `bash run.sh <reel>` | 109–112 | Same block |
| ART_RUN FAIL keeps last 300 chars of stderr and returns | 113–115 | Same block |
| Recut size report: `f"recut: {review.name} ({sz})"` | 116–118 | Same block |
| Discovery walks `HERE.parent` (books/) for every `<book>/youtube/<reel>/beat_sheet.json` | 129–137 | `main()` reel-discovery loop |
| `_node_env()` prepends the newest `~/.nvm/versions/node/*/bin` onto PATH | 23–32 | `_node_env()` |
| Main-loop status test — any `'FAIL' in a` flags the whole reel | 158 | `status = 'ok' if not any('FAIL' in a for a in acts) else 'FAIL'` |
| Zero-slates dry-run report: `"0 reels, 0 slate beats to fill"` | 141–142 | `print(...)` in `main()` |
| Missing `beat_sheet.json` → `find_slates` returns `([], None)` — reel silently skipped | 53–55 | `find_slates()` guard |

## Named laws / invariants

- **DEFAULT IS DRY-RUN.** The apply flag is opt-in. Any narration that says "fill\_slates does X" without a paired "with --apply" is wrong; the film is careful to say `--apply` every time it means the mutating path.
- **THE FOUR SKIP CONDITIONS** are exhaustive. If a beat has any of {`media/<bid>.mp4`, `manim/<bid>.mp4`, `manim/<bid>.mov`, `silent:true`, `shot.remotion.pattern`}, `fill_slates` will NOT touch it. B04 (mechanism 2) and B07 (worked example) both make this the point.
- **ONE PATTERN ONLY.** `stamp_slates` writes exactly `FormACard`. No branching by act, book, palette. The film calls this out in B05 and again in the verdict.

## Off-camera verifications performed

- Read the whole 155-line source file end-to-end.
- Confirmed live copy at `/Users/bear/Documents/CoWork/bear-textbooks/books/brutalist.art/runtime/scripts/fill_slates.py` matches the isolated toolkit copy (both SHA `de9efcbdc25a385a5678bde0d8093d0ede06e81da8c5c7af1efdcab2e4d7863a`; not the SHA in the invocation because the file was updated after the snapshot).
- Ran `fill_slates.py -h` for the exact `argparse` output shown on B03 (`demo/help.txt`).
- Ran `fill_slates.py --books demo/` for the exact dry-run output shown on B07 (`demo/dryrun.txt`).
- Called `find_slates()` + `stamp_slates()` directly on a copy of the fixture to capture the post-stamp `beat_sheet.json` shown on B07 (`demo/beat_sheet_after_stamp.json`, `demo/stamp-observation.txt`).

## Source changes in current version vs prior build

The file grew from ~155 lines to 193 lines between the prior build and the current invocation. Changes:

1. **Type annotations** added to all function signatures: `slate_resolves(reel: Path, bid: str) -> bool`, `find_slates(reel: Path)`, `_truncate(text: str, words: int = 12) -> str`, `_topic(sheet: dict) -> str`, `stamp_slates(reel: Path, slates: list, sheet: dict)`, `render_reel(reel: Path, env: dict) -> list`. Behavior is identical.
2. **`_topic()` helper** (lines 44–48) added: extracts `topic/series/book` from beat sheet metadata and uppercases it. As of this build, it is **defined but not called** anywhere in the script — no production path invokes it. The B05 code card notes `# unused in current version`. This is accurate.
3. **`find_slates()` docstring** and intermediate `sheet_path = reel / "beat_sheet.json"` variable added. Logic is otherwise identical.
4. **`stamp_slates()` write** now passes `ensure_ascii=False` to `json.dumps`.
5. **Line numbers** shifted ~10 lines throughout. B04 card now shows `:51-74`, B05 `:34-106`, B06 `:109-130`.

## Not claimed / deliberately out of scope

- The film does NOT claim to have executed `--apply` end-to-end against the real books/ tree. `--apply` triggers `remotion_scenes.py` and `run.sh` on every affected reel — that is a batch operation with permanent side-effects on other reels' beat sheets, so we only exercised the dry-run and the stamping halves in isolation on a disposable fixture.
- The film does NOT enumerate every subprocess return-code path — only the two documented ones (REMOTION FAIL, ART_RUN FAIL) plus the two implicit ones (no beat sheet, no slates). Anything else (e.g. `run.sh`'s internal gates) belongs to `run.sh`, not to `fill_slates`.
