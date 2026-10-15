# professor-bear/ — the Professor Bear portrait library

**What this is.** The master portraits behind the PROFESSOR BEAR LAW (toolkit `CLAUDE.md` rule 9): whenever a beat
needs a person, or Professor Bear, it shows one of these at random within the matching aspect ratio, never a person icon.

**What is in git.** `manifest.json` (the file list by ratio), `MANIFEST.md` (every rename and deletion), this README.
The master PNGs are **not** in git (4+ GB); the toolkit renders from the downscaled JPG copies in
`runtime/remotion/public/professor-bear/`, which are committed. A fresh clone therefore works for Remotion and the
`./art bear --public` path; `./art bear <ratio>` without `--public` and the Manim `professor_bear()` helper need the
masters, which live on Bear's machine (or regenerate them from the public JPGs with a resize).

**Pick one.** `./art bear 1x1 --seed <beat id>` · Manim `professor_bear(ratio, height, seed)` · Remotion
`ProfessorBearPortrait` / `<ProfessorBear>`. Ratios 1x1 · 2x3 · 16x9. Cropping is fine (`--crop circle`, `shape="circle"`).
Counts are hard-coded in `runtime/remotion/src/lib/professorBear.ts` and the show-tell `iso_kit.py`: update both when the set changes.
