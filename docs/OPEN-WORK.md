# Open Work Packages — Living List

**Last Updated:** 2026-08-11  
**Owner:** Autonomicity Games Inc.  
**How to use:** Both humans and AI systems should update this file when starting or completing major work. Keep entries concrete and linked to files or ADRs where possible.

---

## Priority 1 — Foundation Decisions & Budgets — COMPLETE

| ID | Work Package | Status | Link |
|----|--------------|--------|------|
| WP-01 | Detailed propulsion performance model + staging mass ratios | **Complete** | systems/propulsion/performance-model.md |
| WP-02 | Closed-loop life support mass & power budget (10k–25k) | **Complete** | systems/life_support/mass-balance.md |
| WP-03 | Structural + radiation shielding mass estimates | **Complete** | systems/structure/mass-estimates.md |
| WP-04 | Top-level power budget framework | **Complete** | systems/power/budget.md |

## Priority 2 — Architecture & Interfaces (Now Active)

| ID | Work Package | Status | Owner / Notes |
|----|--------------|--------|---------------|
| WP-05 | Spin radius / comfort analysis for rotating habitats | Not started | systems/habitat/ |
| WP-06 | Interface control documents between major subsystems | Not started | |
| WP-07 | Magnetic sail integration for deceleration | Not started | systems/propulsion/ |
| WP-08 | Daedalus-Skin material requirements and self-healing performance targets | Not started | materials/ |

## Priority 3 — Manufacturing & Safety

| ID | Work Package | Status | Owner / Notes |
|----|--------------|--------|---------------|
| WP-09 | Seed vessel concept (minimum viable first ship) | Not started | manufacturing/ |
| WP-10 | High-level safety case and critical failure modes under TOLC 8 | Not started | governance/ |
| WP-11 | ³He and deuterium acquisition / ISRU pathways | Not started | manufacturing/ |

## Completed / Accepted

| ID | Work Package | ADR / Link |
|----|--------------|------------|
| WP-01 | Propulsion performance model & staging | systems/propulsion/performance-model.md |
| WP-02 | Life support mass & power budget framework | systems/life_support/mass-balance.md |
| WP-03 | Structural + shielding mass framework | systems/structure/mass-estimates.md |
| WP-04 | Top-level power budget framework | systems/power/budget.md |
| — | Primary propulsion choice (ICF D–³He + magnetic nozzle) | ADR-0001 |
| — | Rotating habitats for artificial gravity | ADR-0002 |
| — | Human + AI collaboration protocol | COLLABORATION.md |
| — | Top-level system requirements | docs/requirements/00-system-requirements.md |

---

**Rule:** When a work package is completed, move it to the Completed section and create or update the corresponding ADR or specification file.

**Current Focus:** Priority 2 items are now open for joint human + AI work.
