"""Report which physics solvers are present on this machine.

The point of this module is to make an absence checkable. WP-HF-01 needs finite
element analysis and Monte-Carlo radiation transport. Neither is installed in
this repository's CI image, and a run card that says "not run" is stronger when
a program can confirm the tool is simply not there.

Presence of a binary is necessary, not sufficient. Finding `ccx` on PATH would
mean a solver exists, not that a qualified Pass A run has been performed.
"""

from __future__ import annotations

import shutil
from dataclasses import dataclass

# Export-controlled codes (MCNP among them) are deliberately absent from this
# list. This repository does not seek, vendor, or wrap them.
FEA_SOLVERS: dict[str, str] = {
    "ccx": "CalculiX",
    "as_run": "Code_Aster",
    "ElmerSolver": "Elmer FEM",
    "sfepy-run": "SfePy",
}

TRANSPORT_SOLVERS: dict[str, str] = {
    "openmc": "OpenMC",
    "geant4-config": "Geant4",
    "phits": "PHITS",
}


@dataclass(frozen=True)
class SolverStatus:
    binary: str
    name: str
    role: str
    path: str | None

    @property
    def present(self) -> bool:
        return self.path is not None


def probe() -> list[SolverStatus]:
    statuses: list[SolverStatus] = []
    for role, table in (("fea", FEA_SOLVERS), ("transport", TRANSPORT_SOLVERS)):
        for binary, name in table.items():
            statuses.append(
                SolverStatus(binary=binary, name=name, role=role, path=shutil.which(binary))
            )
    return statuses


def available(role: str | None = None) -> list[SolverStatus]:
    return [s for s in probe() if s.present and (role is None or s.role == role)]


def summary() -> str:
    lines = ["Physics solver probe", "=" * 60]
    for status in probe():
        mark = f"present at {status.path}" if status.present else "absent"
        lines.append(f"  [{status.role:9}] {status.name:12} ({status.binary}): {mark}")
    lines.append("-" * 60)
    fea = available("fea")
    transport = available("transport")
    lines.append(f"  FEA solvers available:       {len(fea)}")
    lines.append(f"  Transport solvers available: {len(transport)}")
    if not fea:
        lines.append("  => WP-HF-01 Pass A cannot be run here. Status stays NOT RUN.")
    if not transport:
        lines.append("  => WP-HF-01 Pass B cannot be run here. Status stays NOT RUN.")
    lines.append("  => WP-HF-01 Pass C needs a physical test article. No CI equivalent exists.")
    return "\n".join(lines)


if __name__ == "__main__":
    print(summary())
