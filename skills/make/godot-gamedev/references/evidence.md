# Source and component evidence

`gamedev-evidence.json` uses schema version 1. `--game` names the folder holding
`project.godot`, not a broad workspace. All source paths are relative to that
folder; references may not escape through symlinks. Enumerate all authored files
except `.godot/`, `.git/` and generated `.uid` identifiers. Include `.import`
sidecars because they can contain authored import settings. Record omitted
files explicitly with reasons; runtime components must not be omitted simply
because they are hard to teach. A separate asset inventory can include generated
cache artifacts when the import process is itself the subject.

The ledger contains:

- `files`: `{path, sha256, role, component_ids}` for every inventoried file.
- `components`: `{id, explanation, beat_ids, files}`. Each requires nonempty
  source associations and narrated existing beats. A component can span beats.
- `excerpts`: `{beat_id, path, start_line, end_line, text}`. One-based inclusive
  line ranges, UTF-8, newline joined without a final newline. Text must match
  both the actual file and its beat's `shot.remotion.props.code`.
- `exclusions`: `{path, reason}` for files genuinely outside this film's
  component scope. Still counted and visible to the reviewer.

Record render/asset sources separately in `SOURCES.md`: native engine capture
path and hash, source revision, runtime-tree probe, imported asset licenses,
and any actual upstream documentation consulted. No secrets or `.env` contents.
Do not embed absolute developer-machine paths in the reusable skill or scene.

The film's source-code claim is a snapshot, not a promise about future revisions.
The checker fails on stale hashes, source line drift, missing components,
unassociated files, extra unlisted files or invented excerpts. It cannot decide
whether all mechanisms were explained clearly or whether an exclusion is honest.

## Code/result pairing for new films

Set `teaching_contract` to `code-then-result-v1`. Each `code_result_pairs` entry
contains `code_beat`, `result_beat`, `observation`, and `media` with a reel-relative
`path` and `sha256`. Every excerpt beat must have exactly one entry, and its
result beat must be the next beat, contain narration, and not be another code
excerpt. The result beat's `shot.evidence_media` must name the same media path.

The hashed media is the actual clip/preview shown, not an unrelated receipt.
Keep source capture, source revision, time interval, method and any labeled
hold/replay in the usual provenance records. A result beat may reuse existing
same-build evidence, but must make its relation to the preceding code legible.
For a test or configuration result, use actual recorded output or engine evidence;
do not invent successful output. These checks cannot assess explanatory truth.
