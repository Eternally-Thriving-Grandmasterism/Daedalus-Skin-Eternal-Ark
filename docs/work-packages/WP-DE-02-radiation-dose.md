# WP-DE-02 — Radiation Transport & Dose Calculation Work Package

**Phase:** Detailed Engineering, Simulation & Technology Maturation  
**Priority:** P1  
**Owner:** Autonomicity Games Inc.  
**Authority:** Ra-Thor + Permanent PATSAGi Councils under TOLC 8  
**Status:** Open — Ready for execution  
**Created:** 2026-08-11

---

## 1. Objective

Replace broad areal-density planning ranges with mission-specific, calculated annual and career dose numbers for the DSA-Ref-A reference mission (10–25 years), and determine the minimum-mass shielding configuration that satisfies dose limits.

## 2. Scope

### 2.1 Mission Dose Targets (Planning)
- Annual effective dose limit (planning): consistent with current space-agency long-duration guidance or more conservative (to be locked by PATSAGi)
- Career dose limit: conservative multi-decade value
- Storm shelter: ability to ride out a major SPE with residual dose within short-term limits

### 2.2 Radiation Environments to Model
1. Galactic Cosmic Rays (GCR) — solar-minimum and solar-maximum spectra
2. Solar Particle Events (SPE) — design-basis events (e.g., historical extreme events scaled)
3. Secondary radiation produced in shielding materials
4. Forward particle shield contribution (interstellar dust / high-energy particles)

### 2.3 Geometry & Material Configurations
- Primary living volumes with dual-use water tanks in optimised locations
- Dedicated polyethylene / hydrogen-rich layers
- Storm shelter high-areal-density configuration
- Sensitivity to water mass placement (central vs peripheral)
- Optional active magnetic deflection cases (performance vs mass/power trade)

### 2.4 Analysis Method Requirements
- Use validated radiation transport codes (or documented equivalents) capable of handling the GCR spectrum and secondary production
- Report dose equivalent (Sv) and organ-specific doses where relevant
- Uncertainty quantification on transport results
- Clear mapping from calculated dose to required areal density and mass

## 3. Deliverables

1. Dose calculation report for baseline passive + dual-use water configuration
2. Optimised water placement geometry recommendation
3. Active vs passive shielding quantitative trade (mass + power system mass)
4. Updated shielding mass allocation for the top-level mass budget
5. Storm shelter design requirements document
6. Formal recommendation on whether active magnetic shielding enters the baseline

## 4. Success Criteria

- Dose numbers are traceable to specific transport runs and geometry
- Shielding mass uncertainty is reduced to a level comparable with other major mass categories
- PATSAGi accepts the dose targets and the resulting mass allocation

## 5. Dependencies

- Inputs: life-support water inventory, habitat volume allocation, structural geometry from WP-DE-01
- Parallel with structural work (water tanks affect both mass and load paths)

## 6. Governance

Dose limits and the final shielding approach require explicit TOLC 8 valence review (crew safety is high-valence).

---

**This package closes the second-largest remaining mass uncertainty that can still be advanced analytically.**
