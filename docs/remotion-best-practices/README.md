# Superseded — the live Remotion skills are installed, not copied

This folder is a July 2026 snapshot (rules for Remotion ≈4.0.3xx). Since 2026-10-10 the current
Remotion agent skills (remotion-dev/skills, v4.0.534+) are installed in the Remotion project at
`runtime/remotion/.agents/skills/` (lockfile `runtime/remotion/skills-lock.json`) and symlinked into
`.claude/skills/` here and in `books/`, so Claude Code sees them as `/remotion-markup`, `/remotion-captions`,
`/remotion-render`, `/remotion-multimedia`, `/remotion-docs`, `/remotion-upgrade` and the router `/remotion-best-practices`.
Maps, SaaS, Studio-interactivity and create-project skills were deliberately not installed.

Update: `cd runtime/remotion && npx remotion skills update` (then review the diff before building a film).
Installed Remotion is 4.0.486; rules that need newer features (effects, HtmlInCanvasMotionBlur, lightLeak,
rough-notation) require `npx remotion upgrade` first, done once with a full scene-index re-render and gate check.
