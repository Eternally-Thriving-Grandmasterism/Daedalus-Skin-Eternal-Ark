"""Tests for the HF-01 Pass A toy and the solver probe.

Two jobs here. First, keep the closed-form arithmetic in `tools/hf01_pass_a_toy.py`
locked to the figures published in `simulations/hf-01-pass-a-analytical-sanity.md`,
so the code and the note cannot drift. Second, and more important, assert that the
toy refuses to behave like a Pass A result: it will not emit a recommended habitat
mass, and it reports NOT RUN.
"""

from __future__ import annotations

import sys
import unittest
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from tools import solver_probe  # noqa: E402
from tools.hf01_pass_a_toy import (  # noqa: E402
    PassANotRun,
    hoop_thickness_m,
    load_deck,
    membrane_allowable_pa,
    run,
    summary,
)


class TheToyRefusesToCloseTheGate(unittest.TestCase):
    def setUp(self) -> None:
        self.result = run()

    def test_status_is_not_run(self) -> None:
        self.assertEqual(self.result.status, "NOT RUN")

    def test_method_says_it_is_not_fea(self) -> None:
        self.assertIn("not FEA", self.result.method)

    def test_asking_for_a_recommended_mass_raises(self) -> None:
        with self.assertRaises(PassANotRun):
            self.result.recommended_habitat_mass_t()

    def test_it_never_claims_to_move_the_planning_lock(self) -> None:
        self.assertFalse(self.result.moves_the_planning_lock())

    def test_it_names_what_it_ignores(self) -> None:
        self.assertGreaterEqual(len(self.result.ignored), 5)
        joined = " ".join(self.result.ignored).lower()
        for omission in ("buckling", "decks", "joints", "live load"):
            with self.subTest(omission=omission):
                self.assertIn(omission, joined)

    def test_summary_carries_the_not_run_banner(self) -> None:
        text = summary(self.result)
        self.assertIn("NOT RUN", text)
        self.assertIn("does not close Pass A", text)


class ArithmeticMatchesThePublishedNote(unittest.TestCase):
    """Figures from simulations/hf-01-pass-a-analytical-sanity.md sections 2 to 4."""

    def setUp(self) -> None:
        self.deck = load_deck()
        self.result = run(self.deck)

    def test_membrane_allowable_is_720_mpa(self) -> None:
        self.assertAlmostEqual(membrane_allowable_pa(self.deck) / 1.0e6, 720.0, places=6)

    def test_hoop_thickness_is_about_20_mm(self) -> None:
        self.assertAlmostEqual(self.result.membrane_thickness_m * 1000.0, 19.7, places=1)

    def test_case_s_wall_membrane(self) -> None:
        self.assertAlmostEqual(self.result.case("S").mass_t / 1000.0, 2.69, places=2)

    def test_case_e_full_diameter_heads(self) -> None:
        self.assertAlmostEqual(self.result.case("E").mass_t / 1000.0, 3.76, places=2)

    def test_case_s_plus_e_total(self) -> None:
        self.assertAlmostEqual(self.result.case("S+E").mass_t / 1000.0, 6.45, places=2)

    def test_full_diameter_heads_overshoot_the_planning_lock(self) -> None:
        """The note's live risk, kept visible: with full-diameter flat heads the bare
        membrane already exceeds 5,850 t before any deck, frame, or knockdown."""
        self.assertGreater(self.result.case("S+E").mass_t, self.result.planning_habitat_mass_t)

    def test_wall_alone_stays_under_the_planning_lock(self) -> None:
        """Case T in the note: without full-diameter heads the geometry is still open."""
        self.assertLess(self.result.case("S").mass_t, self.result.planning_habitat_mass_t)

    def test_hoop_thickness_is_linear_in_radius(self) -> None:
        base = hoop_thickness_m(101300.0, 140.0, 720.0e6)
        self.assertAlmostEqual(hoop_thickness_m(101300.0, 280.0, 720.0e6), 2.0 * base, places=12)


class DeckIsFrozenAndComplete(unittest.TestCase):
    def setUp(self) -> None:
        self.deck = load_deck()

    def test_required_top_level_fields_present(self) -> None:
        for field in (
            "deck_id",
            "deck_revision",
            "planning_habitat_mass_t",
            "change_rule_fraction",
            "change_rule_upper_t",
        ):
            with self.subTest(field=field):
                self.assertIn(field, self.deck)

    def test_change_rule_ceiling_is_internally_consistent(self) -> None:
        expected = self.deck["planning_habitat_mass_t"] * (1.0 + self.deck["change_rule_fraction"])
        self.assertAlmostEqual(self.deck["change_rule_upper_t"], expected, places=6)

    def test_all_eight_load_cases_are_declared(self) -> None:
        ids = self.deck["load_cases"]["ids"]
        self.assertEqual(len(ids), 8)
        for index, identifier in enumerate(ids, start=1):
            with self.subTest(load_case=identifier):
                self.assertEqual(identifier, f"LC-0{index}")
                self.assertIn(identifier.replace("-", "").lower(), self.deck["load_cases"])

    def test_deck_asserts_that_a_blank_run_is_not_a_pass(self) -> None:
        self.assertTrue(self.deck["pass_fail"]["blank_run_is_not_a_pass"])


class SolverProbe(unittest.TestCase):
    def test_probe_covers_both_roles(self) -> None:
        roles = {status.role for status in solver_probe.probe()}
        self.assertEqual(roles, {"fea", "transport"})

    def test_probe_reports_a_path_only_when_present(self) -> None:
        for status in solver_probe.probe():
            with self.subTest(solver=status.name):
                self.assertEqual(status.present, status.path is not None)

    def test_no_export_controlled_code_is_referenced(self) -> None:
        binaries = set(solver_probe.FEA_SOLVERS) | set(solver_probe.TRANSPORT_SOLVERS)
        self.assertNotIn("mcnp", {b.lower() for b in binaries})

    def test_summary_states_the_consequence_for_each_pass(self) -> None:
        text = solver_probe.summary()
        for pass_id in ("Pass A", "Pass B", "Pass C"):
            with self.subTest(pass_id=pass_id):
                self.assertIn(pass_id, text)


if __name__ == "__main__":
    unittest.main()
