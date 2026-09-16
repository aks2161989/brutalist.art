#!/bin/bash
# 02_referenced_siblings.sh — checks whether the SKILL file's --repo and
# --paper modes have their sibling skills available inside THIS toolkit
# snapshot. Local only, no network.
set -u
TK="/Users/bear/Documents/CoWork/bear-textbooks/books/brutalist.art/.repoloop/workspaces/claude-liam-brutalist-skill-anthropics/toolkit"

for sib in git-explainer ai-paper; do
  path="$TK/skills/make/$sib"
  if [ -d "$path" ]; then
    echo "PRESENT: $path"
  else
    echo "ABSENT:  $path (—$sib dispatch has nowhere to go)"
  fi
done

echo
echo "All skills present under skills/make/ in this toolkit:"
ls "$TK/skills/make/" | sort
