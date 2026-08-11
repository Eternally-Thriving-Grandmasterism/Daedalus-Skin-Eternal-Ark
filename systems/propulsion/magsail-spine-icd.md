# Magnetic Sail – Non-Rotating Spine Interface Control Document (ICD)

**Status:** First issue  
**Owner:** Autonomicity Games Inc.  
**Authority:** Ra-Thor + Permanent PATSAGi Councils under TOLC 8  
**Date:** 2026-08-11  
**Architecture:** MS-B multi-loop / segmented array (preferred baseline)  
**Linked:** WP-MS-02, magsail-mass-envelope-cycle-01.md

---

## 1. Purpose

Define the physical, electrical, thermal, data, and keep-out interfaces between the magnetic sail system and the non-rotating central spine so that spine structural design, sail packaging, and deployment can proceed without ambiguity.

## 2. Mechanical Interfaces

| Interface | Requirement | Notes |
|-----------|-------------|-------|
| Stowage attachment | Distributed hard-points along spine axial length | Sail stowed during boost and coast |
| Launch / boost loads | Sail package must survive acceleration and vibration environments defined for the spine | |
| Deployment attachment | Release mechanisms and restraint systems that leave no residual mass on the spine after deployment | |
| Deployed stay / tether loads (if any) | Any residual structural links must be designed for continuous tension under dynamic plasma loads | Prefer free-flying or minimally tethered configuration |

**Stowed volume target:** Compatible with available spine diameter and axial real-estate without forcing major dry-mass growth of the spine structure.

## 3. Keep-Out Zones

- Forward particle shield cone and any residual nozzle plume envelope must remain clear of the deployed sail volume.
- Deployed sail must not intersect the rotating habitat clearance volume under any attitude excursion within the control authority.
- Minimum clearance margins to be confirmed by deployment dynamics simulation.

## 4. Electrical & Power Interfaces

| Interface | Requirement |
|-----------|-------------|
| Current leads | High-current superconducting or low-loss leads from spine-mounted power / cryogenic plant to sail loops |
| Power during deployment | Peak power for actuators and initial current ramp |
| Steady-state power | Cryogenic maintenance + attitude control + current regulation |
| Grounding / fault protection | Defined fault-clearing and quench-protection interfaces |

## 5. Thermal & Cryogenic Interfaces

- Cryogenic supply / return lines (if spine-mounted cryo plant is used)
- Radiator or heat-rejection interfaces for cryocooler waste heat
- Thermal isolation between sail package and habitat / spine structure during stowed phase

## 6. Data & Control Interfaces

- High-rate telemetry for current, temperature, attitude, and structural health
- Command uplink for deployment sequencing, current control, and attitude trim
- Integration with PATSAGi monitoring and fault-management protocols

## 7. Failure Modes Affecting the Spine

| Failure | Spine Impact | Mitigation |
|---------|--------------|------------|
| Partial deployment | Asymmetric loads or residual mass | Staged release, redundant actuators |
| Quench / current dump | Thermal and electromagnetic transient | Quench protection, dump resistors located off critical structure |
| Structural tether failure (if used) | Sudden load release | Prefer free-flying design; load-limiting devices |

## 8. Configuration Control

This ICD is the controlling interface definition. Any change to stowage geometry, attachment loads, or keep-out zones requires formal update and PATSAGi notification.

---

**This ICD enables concurrent design of the magnetic sail and the non-rotating spine under a single interface baseline.**
