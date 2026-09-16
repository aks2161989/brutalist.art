#!/usr/bin/env bash
# Wrapper to invoke chrome-headless-shell with --single-process so Remotion
# can render inside Apple's App Sandbox (Mach-port bind is blocked for
# child processes; collapsing them all into main dodges it).
exec "/Users/bear/node_modules/.remotion/chrome-headless-shell/mac-arm64/chrome-headless-shell-mac-arm64/chrome-headless-shell" \
    --single-process --in-process-gpu --disable-crash-reporter "$@"
