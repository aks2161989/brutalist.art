# Build evidence ledger

`modelbuild-evidence.json` uses schema version 1 and lives in `film/`.
`model_folder` is the folder holding the model (normally `".."`). All paths in
the ledger are relative to the model folder; none may escape it.

The ledger contains:

- `files`: `{path, sha256, role}` for every build input cited by a beat:
  build/render/compare/export scripts, params, BUILD_NOTES, measurement notes.
  Roles: `build-script`, `params`, `notes`, `measurement`, `compare-script`,
  `export-script`, `render-script`.
- `assets`: `{path, sha256, shows}` for every image a beat shows.
- `views`: map with keys `hero`, `side`, `front`, `rear`, `top` (one path each)
  and `details` (list). Every path must be in `assets` and shown by a `views`
  beat.
- `human_verdicts`: `{round, who, quote, status}`. `status` is `given` or
  `pending`. A given quote must appear verbatim (case-insensitive) in some
  beat's narration, after "Professor Bear said".
- `ai_scores`: `{round, overall, by_view, misses}` from the notes.
- `not_established`: at least one plain sentence; the `not-established` beat
  narrates it.
- `reconstructions`: the beat ids whose `ui_steps` are hand reconstructions.

The ledger is a snapshot of the published model, not a promise about future
rounds. The checker fails on stale hashes, missing files, escaping paths,
unlisted assets, missing view coverage, unquoted verdicts or a missing
not-established beat. It cannot decide whether a reconstruction is the best
way to build the part, or whether the narration is true; that needs a person
who knows Blender to read it.
