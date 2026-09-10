"""Realism lint: fail the build when a document starts to read like a validated ship.

Two rules.

**Required statements.** The README must carry the critical realism statement and
link to `docs/TECHNOLOGY-READINESS-AND-REALISM.md`. Deleting either one is a red
build, not a quiet edit.

**Banned phrasings.** Markdown is scanned for constructions that assert demonstrated
performance: a validated design, proven hardware, construction readiness, TRL 9.
Patterns are written narrowly so that legitimate forward-looking use survives —
"use validated transport codes" and "pulse rate must be proven" are requirements,
not claims, and neither matches.

Text inside quotation marks is stripped before matching, so a document may quote a
forbidden phrase in order to forbid it.

One pattern — a claim of confirmation by FEA or Monte-Carlo — also accepts denial,
because "none of these has been confirmed by FEA" is the sentence the repository most
needs to be able to write. Denial is judged on the clause containing the match, not the
whole line, so a denial elsewhere in the sentence does not launder a later claim. No
other pattern gets this exemption: negation heuristics are a reliable way to smuggle an
over-claim past a lint, and they are used here once, deliberately, and narrowly.

This lint governs wording. It cannot detect an over-claim written in careful prose,
matching is line-by-line so a banned phrase split across a line break is missed, and
passing it is not a review.
"""

from __future__ import annotations

import re
from dataclasses import dataclass
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]

SKIP_DIRECTORIES = {".git", ".github", "node_modules", "__pycache__"}

# This module and its tests necessarily contain the banned phrases as data.
SELF_REFERENTIAL = {
    Path("tools/realism_lint.py"),
    Path("tests/test_realism_lint.py"),
}

QUOTED_SPAN = re.compile(r"“[^”]*”|\"[^\"]*\"|‘[^’]*’")
CLAUSE_BREAK = re.compile(r"[.;:—]")
DENIAL = re.compile(r"\b(?:no|none|not|never|nothing|nor|cannot|without)\b", re.IGNORECASE)

# (pattern, reason, denial_allowed)
BANNED: tuple[tuple[str, str, bool], ...] = (
    (
        r"\bvalidated (?:ship|vessel|worldship|design|baseline|architecture)\b",
        "asserts a validated design; state the TRL and the gap instead",
        False,
    ),
    (
        r"\bproven (?:design|technology|hardware|vessel|ship|performance|system)\b",
        "asserts proven hardware; name what has actually been demonstrated and at what scale",
        False,
    ),
    (
        r"\bflight[-\s]proven\b",
        "no element of this concept has flown",
        False,
    ),
    (
        r"\bfully (?:validated|verified|qualified|tested|proven)\b",
        "nothing here is fully validated; give the gap",
        False,
    ),
    (
        r"\bconstruction[-\s]ready\b",
        "construction authorization is gated on Threads A, B and C reaching Gate 2 with real data",
        False,
    ),
    (
        r"\bready (?:to|for)\s+(?:full[-\s]scale\s+)?(?:build|construct|construction|assembly|fly|flight)\b",
        "readiness to build is gated; say which gate is open",
        False,
    ),
    (
        r"\bready for [\w\s]{0,24}construction\b",
        "readiness to build is gated; say which gate is open",
        False,
    ),
    (
        r"\bTRL[-\s]?9\b",
        "no subsystem is at TRL 9; cite the actual readiness level",
        False,
    ),
    (
        r"\b(?:we|the program|this repository|the councils)\s+(?:have\s+|has\s+)?(?:proved|proven|demonstrated|validated)\b",
        "claims a demonstration; the Proof Ladder requires artifacts and provenance",
        False,
    ),
    (
        r"\bguaranteed (?:performance|velocity|mass|dose|reliability)\b",
        "no performance is guaranteed; give the band and its basis",
        False,
    ),
    (
        r"\bwill achieve\b",
        "future-tense certainty; use a target or a planning value",
        False,
    ),
    (
        r"\bno (?:remaining|further) (?:technical |engineering )?risk\b",
        "the risk register is never empty; see governance/integrated-risk-picture.md",
        False,
    ),
    (
        r"\b(?:confirmed|measured) by (?:FEA|Monte[-\s]Carlo)\b",
        "WP-HF-01 Passes A and B have not been run",
        True,
    ),
)

REQUIRED_IN_README: tuple[tuple[str, str], ...] = (
    (
        "remain well beyond demonstrated technology",
        "the critical realism statement must stay in the README",
    ),
    (
        "docs/TECHNOLOGY-READINESS-AND-REALISM.md",
        "the README must link the technology readiness and realism statement",
    ),
    (
        "not a claim of near-term constructability",
        "the README must keep the near-term constructability disclaimer",
    ),
)

COMPILED = tuple(
    (re.compile(pattern, re.IGNORECASE), reason, denial_allowed)
    for pattern, reason, denial_allowed in BANNED
)


@dataclass(frozen=True)
class Finding:
    path: Path
    line_number: int
    matched: str
    reason: str

    def __str__(self) -> str:
        return f"{self.path}:{self.line_number}: {self.matched!r} — {self.reason}"


def strip_quoted(line: str) -> str:
    """Blank out quoted spans so a document can quote a phrase in order to forbid it."""
    return QUOTED_SPAN.sub(" ", line)


def is_denied(line: str, start: int) -> bool:
    """True when the clause leading up to `start` negates the phrase that follows."""
    clause = CLAUSE_BREAK.split(line[:start])[-1]
    return DENIAL.search(clause) is not None


def scan_text(text: str, path: Path) -> list[Finding]:
    findings: list[Finding] = []
    for number, raw_line in enumerate(text.splitlines(), start=1):
        line = strip_quoted(raw_line)
        for pattern, reason, denial_allowed in COMPILED:
            match = pattern.search(line)
            if not match:
                continue
            if denial_allowed and is_denied(line, match.start()):
                continue
            findings.append(
                Finding(path=path, line_number=number, matched=match.group(0), reason=reason)
            )
    return findings


def markdown_files(root: Path = REPO_ROOT) -> list[Path]:
    files: list[Path] = []
    for path in sorted(root.rglob("*.md")):
        relative = path.relative_to(root)
        if SKIP_DIRECTORIES & set(relative.parts):
            continue
        files.append(path)
    return files


def scan_repository(root: Path = REPO_ROOT) -> list[Finding]:
    findings: list[Finding] = []
    for path in markdown_files(root):
        relative = path.relative_to(root)
        if relative in SELF_REFERENTIAL:
            continue
        findings.extend(scan_text(path.read_text(encoding="utf-8"), relative))
    return findings


def missing_required_statements(root: Path = REPO_ROOT) -> list[str]:
    readme = (root / "README.md").read_text(encoding="utf-8")
    return [reason for needle, reason in REQUIRED_IN_README if needle not in readme]


def main() -> int:
    findings = scan_repository()
    missing = missing_required_statements()
    for reason in missing:
        print(f"MISSING: {reason}")
    for finding in findings:
        print(f"OVERCLAIM: {finding}")
    if findings or missing:
        print(f"\nrealism lint failed: {len(missing)} missing, {len(findings)} overclaims")
        return 1
    print(f"realism lint clean across {len(markdown_files())} markdown files")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
