#!/bin/bash
# 01_sha_and_lines.sh — verifies the two file-level numbers the reel cites.
# Local only, no network.
set -euo pipefail
TK="/Users/bear/Documents/CoWork/bear-textbooks/books/brutalist.art/.repoloop/workspaces/claude-liam-brutalist-skill-anthropics/toolkit"
FILE="$TK/skills/make/anthropics/SKILL.md"

echo "==> SHA-256 of the SKILL file:"
shasum -a 256 "$FILE"

echo
echo "==> wc -l of the SKILL file:"
wc -l "$FILE"

echo
echo "==> ls of the skill folder (should show only SKILL.md):"
ls "$(dirname "$FILE")"
