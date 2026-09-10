"""Realism lint tests.

The first class is the lint itself running over every markdown file in the
repository: it fails the build if a document starts asserting a validated ship,
or if the README loses its critical realism statement.

The remaining classes test the lint, because a lint that silently matches nothing
is worse than no lint. They check that it catches over-claims, that it leaves
legitimate forward-looking language alone, and that a document may quote a
forbidden phrase in order to forbid it.
"""

from __future__ import annotations

import sys
import unittest
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from tools import realism_lint  # noqa: E402


class TheRepositoryIsClean(unittest.TestCase):
    def test_no_document_reads_as_a_validated_ship(self) -> None:
        findings = realism_lint.scan_repository()
        self.assertEqual(
            findings,
            [],
            "realism lint findings:\n" + "\n".join(str(f) for f in findings),
        )

    def test_readme_keeps_the_critical_realism_statement(self) -> None:
        missing = realism_lint.missing_required_statements()
        self.assertEqual(missing, [], "README lost a required statement:\n" + "\n".join(missing))

    def test_the_realism_document_exists_and_names_its_gaps(self) -> None:
        realism = (REPO_ROOT / "docs" / "TECHNOLOGY-READINESS-AND-REALISM.md").read_text(
            encoding="utf-8"
        )
        for gap in ("ICF", "³He", "life support", "magnetic sail", "reliability"):
            with self.subTest(gap=gap):
                self.assertIn(gap, realism)

    def test_the_lint_actually_scans_the_document_set(self) -> None:
        files = realism_lint.markdown_files()
        self.assertGreater(len(files), 50)
        names = {path.name for path in files}
        for expected in ("README.md", "PROOF_LADDER.md", "OPEN-WORK.md", "PHASE-STATUS.md"):
            with self.subTest(document=expected):
                self.assertIn(expected, names)


class TheLintCatchesOverClaims(unittest.TestCase):
    def assert_flagged(self, text: str) -> None:
        findings = realism_lint.scan_text(text, Path("synthetic.md"))
        self.assertTrue(findings, f"lint failed to flag: {text!r}")

    def assert_clean(self, text: str) -> None:
        findings = realism_lint.scan_text(text, Path("synthetic.md"))
        self.assertEqual(findings, [], f"lint wrongly flagged: {text!r}")

    def test_validated_design(self) -> None:
        self.assert_flagged("DSA-Ref-A is a validated design ready for detailed drawings.")

    def test_proven_hardware(self) -> None:
        self.assert_flagged("The magnetic nozzle is proven technology.")

    def test_flight_proven(self) -> None:
        self.assert_flagged("The sail deployment mechanism is flight-proven.")

    def test_construction_readiness(self) -> None:
        self.assert_flagged("The baseline is construction-ready.")
        self.assert_flagged("The lattice is ready for construction.")
        self.assert_flagged("The seed vessel is ready to build.")

    def test_trl_nine_claim(self) -> None:
        self.assert_flagged("Habitat structure sits at TRL 9.")

    def test_first_person_demonstration_claim(self) -> None:
        self.assert_flagged("We have demonstrated the 5,850 t structural number.")

    def test_fea_confirmation_claim(self) -> None:
        self.assert_flagged("The 5,850 t figure is confirmed by FEA.")
        self.assert_flagged("Shielding mass is confirmed by Monte-Carlo transport.")

    def test_guaranteed_performance(self) -> None:
        self.assert_flagged("Cruise is a guaranteed velocity of 0.055 c.")

    def test_future_tense_certainty(self) -> None:
        self.assert_flagged("The vessel will achieve 0.055 c on the locked propellant load.")

    def test_empty_risk_claim(self) -> None:
        self.assert_flagged("With Cycle-01 closed there is no remaining technical risk.")


class TheLintLeavesHonestLanguageAlone(unittest.TestCase):
    def assert_clean(self, text: str) -> None:
        findings = realism_lint.scan_text(text, Path("synthetic.md"))
        self.assertEqual(findings, [], f"lint wrongly flagged: {text!r}")

    def test_requirements_to_validate_are_not_claims(self) -> None:
        self.assert_clean("Use validated radiation transport codes with secondary production.")
        self.assert_clean("Pulse rate and reliability over decades must be proven.")
        self.assert_clean("Treat sail performance as a risk until validated simulations exist.")

    def test_gap_language_is_not_a_claim(self) -> None:
        self.assert_clean(
            "No multi-decade validated large rotating habitat exists; the gap is scale."
        )

    def test_not_run_language_is_not_a_claim(self) -> None:
        self.assert_clean("WP-HF-01 Pass A is not run. The 5,850 t number is a planning lock.")

    def test_readiness_for_testing_is_not_readiness_to_build(self) -> None:
        self.assert_clean("The lattice is ready for physical testing and higher-fidelity computation.")

    def test_denying_confirmation_is_allowed(self) -> None:
        self.assert_clean("None of these numbers has been confirmed by FEA or hardware test.")
        self.assert_clean("No mass in the table is confirmed by Monte-Carlo transport.")


class TheDenialExemptionIsNarrow(unittest.TestCase):
    def test_denial_must_sit_in_the_same_clause(self) -> None:
        text = "This is not a rumour. The 5,850 t mass is confirmed by FEA."
        self.assertTrue(realism_lint.scan_text(text, Path("synthetic.md")))

    def test_only_one_pattern_accepts_denial(self) -> None:
        accepting = [pattern for pattern, _, denial_allowed in realism_lint.BANNED if denial_allowed]
        self.assertEqual(len(accepting), 1)

    def test_denial_does_not_excuse_other_patterns(self) -> None:
        text = "It is not a toy, it is a validated design."
        self.assertTrue(realism_lint.scan_text(text, Path("synthetic.md")))


class QuotedProhibitionsAreAllowed(unittest.TestCase):
    def test_a_document_may_quote_a_phrase_in_order_to_forbid_it(self) -> None:
        text = 'Consensus: physically allowed, not engineering-ready. “Ready to build” is not.'
        self.assertEqual(realism_lint.scan_text(text, Path("synthetic.md")), [])

    def test_straight_quotes_work_too(self) -> None:
        text = 'Never write "the design is construction-ready" in this repository.'
        self.assertEqual(realism_lint.scan_text(text, Path("synthetic.md")), [])

    def test_stripping_quotes_does_not_hide_an_unquoted_claim(self) -> None:
        text = 'The “seed vessel” is construction-ready.'
        self.assertTrue(realism_lint.scan_text(text, Path("synthetic.md")))


class MissingStatementsAreReported(unittest.TestCase):
    def test_a_readme_without_the_statement_fails(self) -> None:
        import tempfile

        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / "README.md").write_text("# A ship\n\nIt is great.\n", encoding="utf-8")
            missing = realism_lint.missing_required_statements(root)
            self.assertEqual(len(missing), len(realism_lint.REQUIRED_IN_README))


if __name__ == "__main__":
    unittest.main()
