"""Closed-form membrane arithmetic for HF-01 Pass A. This is NOT finite element analysis.

This module executes, in code, the hand arithmetic already published in
`simulations/hf-01-pass-a-analytical-sanity.md`. It reads the frozen input deck
`simulations/hf-01-pass-a-input-deck.toml` so the two cannot drift apart.

What it computes: thin-wall hoop thickness for internal pressure, and the mass
of that membrane over two geometries (cylinder wall alone; wall plus two
full-diameter flat heads).

What it ignores: buckling and the 0.50 knockdown, matrix-dominated allowables,
decks, frames, joints, penetrations, spin loads, thermal, LC-04 live load, and
every load case in the deck. Those omissions are the reason this is a toy.

The module therefore refuses to produce a recommended habitat-structure mass.
`recommended_habitat_mass_t()` raises. Pass A is closed by a qualified FEA
report with a mesh-convergence note, not by this file.
"""

from __future__ import annotations

import tomllib
from dataclasses import dataclass
from math import pi
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
DECK_PATH = REPO_ROOT / "simulations" / "hf-01-pass-a-input-deck.toml"

PASS_A_STATUS = "NOT RUN"
METHOD = "closed-form thin-wall membrane (not FEA)"


class PassANotRun(RuntimeError):
    """Raised when caller asks this toy for an answer only a real FEA can give."""


@dataclass(frozen=True)
class MembraneCase:
    name: str
    description: str
    mass_t: float


@dataclass(frozen=True)
class ToyResult:
    method: str
    status: str
    allowable_stress_pa: float
    membrane_thickness_m: float
    cases: tuple[MembraneCase, ...]
    planning_habitat_mass_t: float
    change_rule_upper_t: float
    ignored: tuple[str, ...]

    def case(self, name: str) -> MembraneCase:
        for candidate in self.cases:
            if candidate.name == name:
                return candidate
        raise KeyError(name)

    def recommended_habitat_mass_t(self) -> float:
        raise PassANotRun(
            "Closed-form membrane arithmetic cannot recommend a habitat-structure mass. "
            "Pass A needs FEA with mesh convergence, buckling eigenvalues, and per-load-case "
            f"margins. Pass A status: {self.status}."
        )

    def moves_the_planning_lock(self) -> bool:
        """Always False. A toy does not move a locked number, whatever it prints."""
        return False


def load_deck(path: Path = DECK_PATH) -> dict:
    with path.open("rb") as handle:
        return tomllib.load(handle)


def membrane_allowable_pa(deck: dict) -> float:
    cfrp = deck["cfrp_lower_bound"]
    return cfrp["ftu_long_mpa"] * 1.0e6 / cfrp["fs_ultimate_fibre"] / cfrp["aging_factor"]


def hoop_thickness_m(pressure_pa: float, radius_m: float, allowable_pa: float) -> float:
    return pressure_pa * radius_m / allowable_pa


def run(deck: dict | None = None) -> ToyResult:
    deck = deck if deck is not None else load_deck()
    geometry = deck["geometry"]
    density = deck["cfrp_lower_bound"]["density_kg_m3"]

    radius = geometry["spin_radius_m"]
    length = geometry["axial_length_m"]
    allowable = membrane_allowable_pa(deck)
    thickness = hoop_thickness_m(geometry["internal_pressure_pa"], radius, allowable)

    wall_t = 2.0 * pi * radius * length * thickness * density / 1000.0
    ends_t = 2.0 * pi * radius**2 * thickness * density / 1000.0

    cases = [
        MembraneCase("S", "cylinder wall membrane only, no end closures", wall_t),
        MembraneCase("E", "two full-diameter flat heads at the same thickness", ends_t),
        MembraneCase("S+E", "wall plus two full-diameter flat heads", wall_t + ends_t),
    ]
    for sensitivity_length in geometry["axial_length_sensitivity_m"]:
        cases.append(
            MembraneCase(
                f"S@L={sensitivity_length:g}m",
                "cylinder wall membrane at the axial-length sensitivity bound",
                2.0 * pi * radius * sensitivity_length * thickness * density / 1000.0,
            )
        )

    return ToyResult(
        method=METHOD,
        status=PASS_A_STATUS,
        allowable_stress_pa=allowable,
        membrane_thickness_m=thickness,
        cases=tuple(cases),
        planning_habitat_mass_t=deck["planning_habitat_mass_t"],
        change_rule_upper_t=deck["change_rule_upper_t"],
        ignored=(
            "buckling and the 0.50 knockdown",
            "matrix-dominated and shear allowables",
            "decks, frames, and stiffening",
            "joints, penetrations, and the spin interface",
            "spin, transient, docking, and thermal load cases",
            "LC-04 live load, equipment, and water inventory",
        ),
    )


def summary(result: ToyResult | None = None) -> str:
    result = result if result is not None else run()
    lines = [
        "HF-01 Pass A — closed-form membrane arithmetic",
        "=" * 60,
        f"  Method:                {result.method}",
        f"  Pass A status:         {result.status}",
        f"  Membrane allowable:    {result.allowable_stress_pa / 1e6:.0f} MPa",
        f"  Hoop thickness:        {result.membrane_thickness_m * 1000:.1f} mm",
        "-" * 60,
    ]
    for case in result.cases:
        lines.append(f"  Case {case.name:12} {case.mass_t / 1000:6.2f} kt   ({case.description})")
    lines += [
        "-" * 60,
        f"  Planning lock:         {result.planning_habitat_mass_t:.0f} t",
        f"  Change-rule ceiling:   {result.change_rule_upper_t:.1f} t",
        "",
        "  Ignored by this arithmetic:",
    ]
    lines += [f"    - {item}" for item in result.ignored]
    lines += [
        "",
        "  This is not FEA and does not close Pass A. The planning lock stands at",
        f"  {result.planning_habitat_mass_t:.0f} t. The open question the numbers above raise is a",
        "  geometry question: are the pressure heads full-diameter disks or not?",
    ]
    return "\n".join(lines)


if __name__ == "__main__":
    print(summary())
