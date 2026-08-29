# ADR-0003 — 15 kt Seed Dry-Mass Target and 0.05 c Public Cruise Floor

**Status:** Accepted  
**Date:** 2026-08-29  
**Owner:** Autonomicity Games Inc.  
**Authority:** Ra-Thor + Permanent PATSAGi Councils under TOLC 8  
**Contact:** info@Rathor.ai

## Context

DSA-Ref-A already locks a dry-mass band of 12.4–20.15 kt (center 15.5–16.5 kt) and an internal cruise of ~0.055 c. Collaborators asked for a single seed mass and a single public cruise number that can be lofted in sections from lunar factories and assembled in orbit.

## Decision

1. Collaboration-protocol seed dry-mass target is **15.0 kt**.
2. Public multi-generation cruise floor is **0.05 c**.
3. Internal locked cruise remains **~0.055 c** until exhaust velocity is measured.
4. Dry mass is lofted in sections; propellant is a separate ISRU / tanker campaign.
5. Cycle-01 category locks (5,850 t CFRP habitat, 450–750 t shielding, MS-B 550–750 t) are not reopened by this ADR.

## Consequences

- Interface control: [01-mass-budget-propulsion-interface.md](../interfaces/01-mass-budget-propulsion-interface.md).
- Mass budget file remains authoritative for category bands.
- Open physical gates stay open: higher-fidelity FEA, Monte-Carlo radiation transport, Gate E1 magsail tests.

## Alternatives rejected

- Treating 15.5–16.5 kt as the only public number (too wide for loft planning).
- Rewriting cruise down to 0.05 c internally (would hide the locked 0.055 c target).
- Lofting wet mass on the driver (85–145 kt is not a section payload).
