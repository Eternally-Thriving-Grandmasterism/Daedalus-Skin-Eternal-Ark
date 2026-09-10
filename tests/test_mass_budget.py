"""Consistency tests for the locked DSA-Ref-A mass and cruise numbers.

These tests check that the repository is internally consistent with itself.
They are NOT physical validation. Passing here says the 15.0 kt target still
sits inside the published dry-mass band and that the public floor has not
quietly become the internal lock. It says nothing about whether a ship can be
built, and it does not close WP-HF-01 Pass A, B, or C.
"""

from __future__ import annotations

import sys
import unittest
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from tools.mass_budget import (  # noqa: E402
    UnitError,
    fraction_of_c_to_m_s,
    load,
    quantities,
    to_tonnes,
)

KNOWN_UNITS = {"t", "kt", "c", "m/s", "t/kt", "1"}


class UnitsPresent(unittest.TestCase):
    """Every quantity has a unit."""

    def setUp(self) -> None:
        self.document = load()

    def test_every_quantity_declares_a_known_unit(self) -> None:
        for name, entry in self.document["quantities"].items():
            with self.subTest(quantity=name):
                self.assertIn("unit", entry, f"{name} has no unit")
                self.assertIn(entry["unit"], KNOWN_UNITS)

    def test_every_constant_declares_a_known_unit(self) -> None:
        for name, entry in self.document["constants"].items():
            with self.subTest(constant=name):
                self.assertIn("unit", entry, f"{name} has no unit")
                self.assertIn(entry["unit"], KNOWN_UNITS)

    def test_every_allocation_line_declares_a_unit(self) -> None:
        for line in self.document["allocation_15kt"]["line"]:
            with self.subTest(category=line["category"]):
                self.assertEqual(line["unit"], self.document["allocation_15kt"]["line_unit"])

    def test_quantity_parsing_rejects_a_missing_unit(self) -> None:
        with self.assertRaises(UnitError):
            quantities({"quantities": {"nameless": {"kind": "point", "value": 1.0}}})

    def test_conversion_rejects_a_non_mass_unit(self) -> None:
        with self.assertRaises(UnitError):
            to_tonnes(0.05, "c")


class BandShape(unittest.TestCase):
    def setUp(self) -> None:
        self.quantities = quantities()

    def test_bands_are_ordered_and_positive(self) -> None:
        for name, quantity in self.quantities.items():
            if not quantity.is_band:
                continue
            with self.subTest(quantity=name):
                self.assertIsNotNone(quantity.minimum)
                self.assertIsNotNone(quantity.maximum)
                self.assertGreater(quantity.minimum, 0.0)
                self.assertLessEqual(quantity.minimum, quantity.maximum)

    def test_points_carry_a_value(self) -> None:
        for name, quantity in self.quantities.items():
            if quantity.is_band:
                continue
            with self.subTest(quantity=name):
                self.assertIsNotNone(quantity.value)


class SeedTargetSitsInsideTheDryMassBand(unittest.TestCase):
    def setUp(self) -> None:
        self.quantities = quantities()
        self.band = self.quantities["dry_mass_band"]
        self.seed = self.quantities["collaboration_seed_dry_mass"]
        self.center = self.quantities["dry_mass_planning_center"]

    def test_seed_target_is_inside_the_band(self) -> None:
        self.assertTrue(
            self.band.contains(self.seed),
            "15.0 kt seed target must stay inside the 12.4-20.15 kt dry-mass band",
        )

    def test_seed_target_is_15000_t(self) -> None:
        self.assertEqual(to_tonnes(self.seed.value, self.seed.unit), 15_000.0)

    def test_planning_center_is_inside_the_band(self) -> None:
        low = to_tonnes(self.band.minimum, self.band.unit)
        high = to_tonnes(self.band.maximum, self.band.unit)
        self.assertGreaterEqual(to_tonnes(self.center.minimum, self.center.unit), low)
        self.assertLessEqual(to_tonnes(self.center.maximum, self.center.unit), high)

    def test_seed_target_sits_below_the_planning_center(self) -> None:
        """The seed target is a squeeze, not a relaxation: it must be a reduction."""
        self.assertLess(
            to_tonnes(self.seed.value, self.seed.unit),
            to_tonnes(self.center.minimum, self.center.unit),
        )

    def test_locked_component_masses_fit_under_the_seed_target(self) -> None:
        seed_t = to_tonnes(self.seed.value, self.seed.unit)
        dry_components = [
            "rotating_habitat_structure",
            "dedicated_shielding",
            "magnetic_sail_ms_b",
            "residual_tankage_dry",
        ]
        worst_case = 0.0
        for name in dry_components:
            quantity = self.quantities[name]
            upper = quantity.maximum if quantity.is_band else quantity.value
            worst_case += to_tonnes(upper, quantity.unit)
        self.assertLess(
            worst_case,
            seed_t,
            "locked dry categories at their upper bounds must still leave room inside 15.0 kt",
        )


class ResidualPropellantIsNotDryMass(unittest.TestCase):
    def setUp(self) -> None:
        self.quantities = quantities()

    def test_residual_propellant_band_is_recorded(self) -> None:
        propellant = self.quantities["residual_fusion_propellant"]
        self.assertEqual((propellant.minimum, propellant.maximum, propellant.unit), (1800.0, 3500.0, "t"))

    def test_residual_tankage_band_is_recorded(self) -> None:
        tankage = self.quantities["residual_tankage_dry"]
        self.assertEqual((tankage.minimum, tankage.maximum, tankage.unit), (250.0, 500.0, "t"))

    def test_propellant_alone_would_break_the_dry_band_if_counted_as_dry(self) -> None:
        """Guards against a future edit that folds wet residual propellant into dry mass."""
        propellant = self.quantities["residual_fusion_propellant"]
        seed = self.quantities["collaboration_seed_dry_mass"]
        habitat = self.quantities["rotating_habitat_structure"]
        self.assertGreater(
            to_tonnes(propellant.maximum, propellant.unit) + to_tonnes(habitat.value, habitat.unit),
            0.5 * to_tonnes(seed.value, seed.unit),
        )


class PublicFloorIsNotTheInternalLock(unittest.TestCase):
    def setUp(self) -> None:
        self.document = load()
        self.quantities = quantities(self.document)
        self.floor = self.quantities["public_cruise_floor"]
        self.lock = self.quantities["internal_cruise_lock"]

    def test_floor_and_lock_are_different_numbers(self) -> None:
        self.assertNotEqual(self.floor.value, self.lock.value)

    def test_public_floor_is_conservative(self) -> None:
        self.assertLess(self.floor.value, self.lock.value)

    def test_floor_and_lock_are_labelled_by_disclosure(self) -> None:
        entries = self.document["quantities"]
        self.assertEqual(entries["public_cruise_floor"]["disclosure"], "public")
        self.assertEqual(entries["internal_cruise_lock"]["disclosure"], "internal")

    def test_delta_v_between_floor_and_lock(self) -> None:
        c = self.document["constants"]["speed_of_light"]["value"]
        delta = fraction_of_c_to_m_s(
            self.lock.value - self.floor.value, "c", c
        )
        self.assertAlmostEqual(delta / 1.0e6, 1.5, places=1)


class AllocationClosesToTheSeedTarget(unittest.TestCase):
    def setUp(self) -> None:
        self.document = load()
        self.allocation = self.document["allocation_15kt"]
        self.quantities = quantities(self.document)

    def test_lines_sum_to_the_target(self) -> None:
        total = sum(line["value"] for line in self.allocation["line"])
        target = to_tonnes(self.allocation["target_value"], self.allocation["target_unit"])
        self.assertAlmostEqual(total, target, places=6)

    def test_line_values_respect_their_locked_bands(self) -> None:
        for line in self.allocation["line"]:
            band_name = line.get("band")
            if band_name is None:
                continue
            quantity = self.quantities[band_name]
            with self.subTest(category=line["category"]):
                value_t = to_tonnes(line["value"], line["unit"])
                if quantity.is_band:
                    self.assertGreaterEqual(value_t, to_tonnes(quantity.minimum, quantity.unit))
                    self.assertLessEqual(value_t, to_tonnes(quantity.maximum, quantity.unit))
                else:
                    self.assertEqual(value_t, to_tonnes(quantity.value, quantity.unit))

    def test_every_line_category_is_unique(self) -> None:
        categories = [line["category"] for line in self.allocation["line"]]
        self.assertEqual(len(categories), len(set(categories)))


class ChangeRule(unittest.TestCase):
    def test_fifteen_percent_trigger_matches_the_frozen_pass_a_deck(self) -> None:
        """The HF-01 Pass A deck hard-codes 6727.5 t; it must stay 5850 t + 15 %."""
        quantity = quantities()
        habitat = to_tonnes(
            quantity["rotating_habitat_structure"].value,
            quantity["rotating_habitat_structure"].unit,
        )
        fraction = quantity["change_rule_fraction"].value
        self.assertAlmostEqual(habitat * (1.0 + fraction), 6727.5, places=6)


if __name__ == "__main__":
    unittest.main()
