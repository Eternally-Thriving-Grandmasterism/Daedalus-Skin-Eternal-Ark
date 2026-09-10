#!/usr/bin/env bash
# Full documentation-QA workflow for the Daedalus-Skin Eternal Ark lattice.
#
#   1. Integrity check  - internal links resolve, TOML decks parse (Python stdlib).
#   2. Markdown lint     - lenient markdownlint profile (broken/empty/reversed links).
#
# Usage: ./scripts/validate.sh
set -euo pipefail

REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$REPO_ROOT"

echo "== Documentation integrity =="
python3 scripts/validate_docs.py

echo
echo "== Markdown lint =="
if [ -x "node_modules/.bin/markdownlint-cli2" ]; then
  ./node_modules/.bin/markdownlint-cli2 "**/*.md"
elif command -v markdownlint-cli2 >/dev/null 2>&1; then
  markdownlint-cli2 "**/*.md"
else
  npx --yes markdownlint-cli2 "**/*.md"
fi

echo
echo "All documentation checks passed."
