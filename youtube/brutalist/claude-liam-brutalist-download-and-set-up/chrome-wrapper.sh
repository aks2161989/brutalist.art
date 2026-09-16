#!/usr/bin/env bash
exec "/Users/bear/node_modules/.remotion/chrome-headless-shell/mac-arm64/chrome-headless-shell-mac-arm64/chrome-headless-shell" \
    --single-process --in-process-gpu --disable-crash-reporter "$@"
