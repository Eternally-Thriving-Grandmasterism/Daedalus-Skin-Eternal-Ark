"""Loader for data/mass-budget-locked.toml.

Stdlib only (tomllib, Python >= 3.11). This module reads locked numbers; it
never derives a new locked number. Unit handling is deliberately narrow: the
only conversion the mass budget needs is tonne <-> kilotonne, plus fraction-of-c
to m/s for the cruise gates.
"""

from __future__ import annotations

import tomllib
from dataclasses import dataclass
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
DATA_PATH = REPO_ROOT / "data" / "mass-budget-locked.toml"

MASS_UNITS = {"t": 1.0, "kt": 1000.0}


class UnitError(ValueError):
    """Raised when a quantity is missing a unit or carries an unusable one."""


@dataclass(frozen=True)
class Quantity:
    name: str
    unit: str
    kind: str
    value: float | None = None
    minimum: float | None = None
    maximum: float | None = None

    @property
    def is_band(self) -> bool:
        return self.kind == "band"

    def contains(self, other: "Quantity") -> bool:
        """True when `other`'s point value lies within this band, inclusive."""
        if not self.is_band:
            raise TypeError(f"{self.name} is not a band")
        if other.value is None:
            raise TypeError(f"{other.name} has no point value")
        low = to_tonnes(self.minimum, self.unit)
        high = to_tonnes(self.maximum, self.unit)
        point = to_tonnes(other.value, other.unit)
        return low <= point <= high


def to_tonnes(value: float | None, unit: str) -> float:
    if value is None:
        raise UnitError("missing value")
    if unit not in MASS_UNITS:
        raise UnitError(f"{unit!r} is not a mass unit")
    return value * MASS_UNITS[unit]


def fraction_of_c_to_m_s(value: float, unit: str, speed_of_light_m_s: float) -> float:
    if unit != "c":
        raise UnitError(f"{unit!r} is not a fraction-of-light-speed unit")
    return value * speed_of_light_m_s


def load(path: Path = DATA_PATH) -> dict:
    with path.open("rb") as handle:
        return tomllib.load(handle)


def quantities(document: dict | None = None) -> dict[str, Quantity]:
    document = document if document is not None else load()
    parsed: dict[str, Quantity] = {}
    for name, entry in document["quantities"].items():
        unit = entry.get("unit")
        if not isinstance(unit, str) or not unit:
            raise UnitError(f"quantity {name!r} has no unit")
        parsed[name] = Quantity(
            name=name,
            unit=unit,
            kind=entry.get("kind", ""),
            value=entry.get("value"),
            minimum=entry.get("min"),
            maximum=entry.get("max"),
        )
    return parsed
