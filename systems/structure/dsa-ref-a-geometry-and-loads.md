# DSA-Ref-A — Geometry & Load Case Specification (Frozen for First FE Cycle)

**Status:** Configuration-controlled input for WP-DE-01  
**Owner:** Autonomicity Games Inc.  
**Authority:** Ra-Thor + Permanent PATSAGi Councils under TOLC 8  
**Last Updated:** 2026-08-11  
**Linked Work Package:** WP-DE-01 Structural Analysis

---

## 1. Purpose

Provide a single, frozen geometry and load-case definition so that the first global finite-element model of the rotating habitat can be built without ambiguity. All subsequent mass and margin results will be traceable to this specification.

## 2. Reference Geometry (DSA-Ref-A Baseline)

| Parameter | Value | Notes |
|-----------|-------|-------|
| Spin radius to main deck centreline | 140 m | Fixed for this cycle |
| Habitat form | Pressurized cylinder | Short torus approximation permitted only for sensitivity |
| Axial length of pressure vessel | 100 m | Sensitivity cases at 80 m and 120 m |
| Outer diameter (approx.) | 280 m | 2 × spin radius |
| Internal design pressure | 101.3 kPa | Earth sea-level absolute |
| Design artificial gravity at main deck | 0.90 g | 8.83 m/s² |
| Number of primary living decks | 5 | Provisional; refine with deck layout |
| Deck spacing (centre-to-centre) | 3.5–4.0 m | Includes structure + clear height |
| Non-rotating central spine diameter | TBD (interface only) | Not modelled in first global habitat FE |

### 2.1 Primary Structural Elements to Model

- Continuous pressure shell (or modular shell with defined joints)
- Longitudinal and circumferential stiffening (stringers / frames / isogrid or equivalent)
- Main deck structures and their attachment to the shell
- End bulkheads / transition structures at the spin interfaces
- Major penetrations (hatches, utility transfer, viewports) as local features

## 3. Load Cases (Minimum Mandatory Set)

All cases shall be run with the selected material system and the safety / knockdown factors defined in the material selection document.

| ID | Load Case | Description | Criticality |
|----|-----------|-------------|-------------|
| LC-01 | Pressure only (proof) | 1.5 × design pressure, no spin | Strength |
| LC-02 | Pressure only (ultimate) | 2.0 × design pressure (or material-specific ultimate factor) | Strength |
| LC-03 | Spin + pressure (cruise) | Steady 0.90 g + design pressure | Primary operating |
| LC-04 | Spin + pressure + live load | LC-03 + maximum distributed deck live load + equipment mass | Operating |
| LC-05 | Spin-up / spin-down transient | Accelerating torque + residual pressure | Transient |
| LC-06 | Docking / berthing interface | External loads applied at the non-rotating interface while spinning | Interface |
| LC-07 | Thermal + structural | Extreme hot and cold soak combined with LC-03 | Combined |
| LC-08 | Buckling / stability | Critical combinations of pressure, spin, and axial loads | Stability |

### 3.1 Load Factors & Knockdowns (Initial Guidance)

- Use aerospace-standard factors of safety unless a more conservative value is deliberately chosen and justified.
- Apply appropriate buckling knockdowns for large-diameter thin-walled or stiffened cylinders.
- Document every factor used so that results remain auditable.

## 4. Output Requirements from the FE Model

1. Mass breakdown by major structural element (shell, stiffening, decks, bulkheads, joints, contingency)
2. Peak stresses and margins for each critical load case
3. Buckling eigenvalues / critical load factors
4. Deformation under spin (to confirm deck levelness and clearance)
5. Identification of any design features that drive mass disproportionately

## 5. Configuration Control

This document is the frozen input for the first FE cycle. Any change to geometry or load cases after the model is started requires a formal configuration change and PATSAGi notification.

---

**This specification enables the first quantitative structural mass reduction of DSA-Ref-A.**
