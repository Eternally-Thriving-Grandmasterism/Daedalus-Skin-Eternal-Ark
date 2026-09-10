#!/usr/bin/env python3
"""Documentation integrity checker for the Daedalus-Skin Eternal Ark lattice.

This repository is a cross-referenced systems-engineering documentation set. The
whole value of the lattice depends on its internal links resolving and its data
decks staying machine-readable, so this checker enforces exactly that:

  1. Every relative Markdown link and image target resolves to a file that
     exists in the repository (external http/https/mailto links are skipped).
  2. Every TOML input/data deck parses without error.

It has no third-party dependencies (standard library only) so it runs on any
machine with Python 3.11+.

Exit code 0 means the documentation lattice is coherent; non-zero means at least
one broken link or malformed TOML deck was found.
"""

from __future__ import annotations

import os
import re
import sys
import tomllib
from urllib.parse import unquote, urlparse

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Markdown inline links and images: [text](target) and ![alt](target).
_LINK_RE = re.compile(r"!?\[[^\]]*\]\(([^)]+)\)")

# Schemes that point outside the repository and should not be resolved on disk.
_EXTERNAL_SCHEMES = {"http", "https", "mailto", "tel", "ftp", "ftps", "data"}

_SKIP_DIRS = {".git", "node_modules", ".venv", "__pycache__"}


def _iter_files(root: str):
    md_files: list[str] = []
    toml_files: list[str] = []
    for dirpath, dirnames, filenames in os.walk(root):
        dirnames[:] = [d for d in dirnames if d not in _SKIP_DIRS]
        for name in filenames:
            path = os.path.join(dirpath, name)
            if name.endswith(".md"):
                md_files.append(path)
            elif name.endswith(".toml"):
                toml_files.append(path)
    return sorted(md_files), sorted(toml_files)


def _clean_target(raw: str) -> str:
    """Extract the path portion of a Markdown link target."""
    target = raw.strip()
    if target.startswith("<") and ">" in target:
        target = target[1 : target.index(">")]
    else:
        # Drop an optional title: [text](path "title").
        for quote in (' "', " '"):
            if quote in target:
                target = target.split(quote, 1)[0]
        target = target.strip()
    return target


def check_links(md_files: list[str]) -> tuple[int, list[tuple[str, str]]]:
    checked = 0
    broken: list[tuple[str, str]] = []
    for path in md_files:
        with open(path, encoding="utf-8") as handle:
            text = handle.read()
        for match in _LINK_RE.finditer(text):
            target = _clean_target(match.group(1))
            if not target:
                continue
            parsed = urlparse(target)
            if parsed.scheme in _EXTERNAL_SCHEMES or target.startswith("//"):
                continue
            if target.startswith("#"):
                # Pure in-page anchor; not a file reference.
                continue
            path_part = unquote(target.split("#", 1)[0])
            if not path_part:
                continue
            resolved = os.path.normpath(
                os.path.join(os.path.dirname(path), path_part)
            )
            checked += 1
            if not os.path.exists(resolved):
                broken.append(
                    (os.path.relpath(path, REPO_ROOT), target)
                )
    return checked, broken


def check_toml(toml_files: list[str]) -> list[tuple[str, str]]:
    bad: list[tuple[str, str]] = []
    for path in toml_files:
        try:
            with open(path, "rb") as handle:
                tomllib.load(handle)
        except (tomllib.TOMLDecodeError, OSError) as exc:
            bad.append((os.path.relpath(path, REPO_ROOT), str(exc)))
    return bad


def main() -> int:
    md_files, toml_files = _iter_files(REPO_ROOT)

    checked, broken = check_links(md_files)
    bad_toml = check_toml(toml_files)

    print(f"Scanned {len(md_files)} Markdown files.")
    print(f"Resolved {checked} internal links.")
    if broken:
        print(f"Broken internal links: {len(broken)}")
        for src, target in broken:
            print(f"  BROKEN  {src} -> {target}")
    else:
        print("Broken internal links: 0")

    print(f"Validated {len(toml_files)} TOML decks.")
    if bad_toml:
        print(f"Malformed TOML decks: {len(bad_toml)}")
        for src, message in bad_toml:
            print(f"  BAD TOML  {src}: {message}")
    else:
        print("Malformed TOML decks: 0")

    if broken or bad_toml:
        print("\nDocumentation lattice check: FAILED")
        return 1

    print("\nDocumentation lattice check: PASSED")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
