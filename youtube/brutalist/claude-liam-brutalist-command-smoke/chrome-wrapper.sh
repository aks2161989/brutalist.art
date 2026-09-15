#\!/usr/bin/env node
const { spawnSync } = require("child_process");
const chrome = "/Users/bear/node_modules/.remotion/chrome-headless-shell/mac-arm64/chrome-headless-shell-mac-arm64/chrome-headless-shell";
const args = ["--single-process", "--in-process-gpu", "--disable-crash-reporter", ...process.argv.slice(2)];
const r = spawnSync(chrome, args, { stdio: "inherit" });
process.exit(r.status || 0);
