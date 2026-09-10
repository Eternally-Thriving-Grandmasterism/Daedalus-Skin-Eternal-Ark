# Documentation QA Tooling

This repository is a cross-referenced systems-engineering documentation lattice.
Its coherence depends on internal links resolving and the TOML data decks
staying machine-readable. These scripts are the "development workflow" for the
lattice.

## Prerequisites

- Python 3.11+ (standard library only — no packages to install)
- Node.js + npm (for Markdown linting via `markdownlint-cli2`, fetched on demand
  by `npx`)

Both are provided by the default Cloud Agent environment.

## Commands

| Command | Purpose |
|---------|---------|
| `python3 scripts/validate_docs.py` | Check that every internal Markdown link resolves and every TOML deck parses. |
| `npx markdownlint-cli2 "**/*.md"` | Lint Markdown with the lenient profile in `.markdownlint-cli2.jsonc`. |
| `./scripts/validate.sh` | Run the full documentation-QA workflow (integrity + lint). |

Each command exits non-zero on failure, so they are suitable for pre-commit
hooks or CI.
