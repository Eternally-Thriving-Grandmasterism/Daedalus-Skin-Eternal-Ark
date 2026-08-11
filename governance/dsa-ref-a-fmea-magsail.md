# DSA-Ref-A FMEA — Magnetic Sail Deployment & Operation

**Status:** First population  
**Reference Design:** DSA-Ref-A  
**Owner:** Autonomicity Games Inc.  
**Authority:** PATSAGi Councils under TOLC 8  
**Last Updated:** 2026-08-11

Severity / Occurrence / Detection: 1–10. RPN = S × O × D.

## Critical Magnetic Sail Failure Modes

| ID | Function | Failure Mode | Cause | Effect on Crew / Mission | S | O | D | RPN | Current Controls | Recommended Actions |
|----|----------|--------------|-------|---------------------------|---|---|---|-----|------------------|---------------------|
| MS-01 | Deployment | Incomplete or failed deployment | Mechanism jam, structural binding, power loss | Loss of primary deceleration method | 9 | 3 | 4 | 108 | Redundant deployment actuators, ground deployment tests | Full-scale deployment demonstrations in relevant environment |
| MS-02 | Structural integrity | Conductor or support structure failure under load | Dynamic loads, thermal stress, micrometeoroid | Partial or total loss of magnetic moment | 8 | 3 | 5 | 120 | Conservative structural design, shielding of critical elements | Dynamic load analysis + impact testing |
| MS-03 | Superconducting performance | Loss of superconductivity or excessive power demand | Thermal excursion, radiation damage, joint failure | Reduced or zero drag | 9 | 3 | 4 | 108 | Thermal control, shielding, redundant cooling paths | Long-duration cryogenic + radiation testing |
| MS-04 | Attitude & stability | Unstable interaction with plasma / ship dynamics | Control algorithm limits, plasma variability | Oscillation, structural stress, pointing loss | 8 | 4 | 5 | 160 | Advanced control laws, simulation, residual thruster backup | High-fidelity plasma–sail–ship coupled simulations |
| MS-05 | Performance shortfall | Drag significantly below prediction | Density lower than assumed, model error | Deceleration timeline becomes unacceptable | 8 | 4 | 6 | 192 | Conservative density assumptions, residual fusion propellant | Validated drag models + in-space calibration flights |

## Priority Observations

- MS-05 (performance shortfall) currently carries the highest RPN because detection is difficult until real interstellar conditions are encountered.
- MS-04 (stability) is also high and drives the need for sophisticated control and simulation work.
- Residual fusion propellant is the primary operational backup for all sail-related failures.

---

**Magnetic sail FMEA is now live. Core system FMEA coverage (Propulsion, Habitat, Life Support, Sail) is complete.**
