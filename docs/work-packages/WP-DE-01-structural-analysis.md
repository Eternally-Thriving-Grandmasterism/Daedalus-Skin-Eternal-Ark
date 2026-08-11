# WP-DE-01 — Structural Analysis Work Package

**Phase:** Detailed Engineering, Simulation & Technology Maturation  
**Priority:** P1 (Close largest mass & performance uncertainties)  
**Owner:** Autonomicity Games Inc.  
**Authority:** Ra-Thor + Permanent PATSAGi Councils under TOLC 8  
**Status:** Open — Ready for execution  
**Created:** 2026-08-11

---

## 1. Objective

Replace the current wide analytical structural mass range (~4,700–12,200 t for the rotating habitat) with a material-specific, finite-element-confirmed mass number that can be locked into the reconciled mass budget.

## 2. Scope

### 2.1 Geometry Freeze (DSA-Ref-A)
- Spin radius to main deck centreline: **140 m**
- Habitat form: Pressurized cylinder (or short torus equivalent)
- Axial length (pressure vessel): **100 m** (baseline; sensitivity ±20 m)
- Internal design pressure: **101.3 kPa** (Earth sea-level)
- Design artificial gravity: **0.90 g** at main deck
- Number of primary living decks: 4–6 (to be confirmed from deck layout)

### 2.2 Load Cases (Minimum Set)
1. Internal pressure only (proof and ultimate)
2. Spin + pressure (steady-state cruise)
3. Spin + pressure + maximum deck live load + equipment
4. Spin-up / spin-down transient
5. Docking / berthing load at non-rotating interface
6. Combined thermal + structural (extreme temperature cases)
7. Buckling / stability under compression and shear

### 2.3 Material Selection Task (Must Complete First)
Define and document a short-list of candidate material systems with published or qualified allowables suitable for multi-decade space service:

| Candidate Class | Examples | Priority for First FE Cycle |
|-----------------|----------|-----------------------------|
| High-strength aluminium-lithium alloys | 2195, 2099, etc. | High |
| Titanium alloys | Ti-6Al-4V, beta alloys | High |
| Carbon-fibre / polymer composites | High-modulus CFRP with space-qualified resin | Highest |
| Hybrid metal-composite | Metal-lined composite pressure vessel | Medium |
| Advanced metallic (optional) | Beryllium or Al-Be alloys (toxicity & cost flagged) | Low |

For each short-listed material, record:
- Design allowable (tension, compression, shear, fatigue)
- Density
- Fracture toughness / damage tolerance data
- Vacuum, radiation, and thermal cycling performance notes
- Manufacturing feasibility for 140 m class diameter sections

### 2.4 Finite-Element Model Requirements
- Global model of the complete rotating habitat pressure vessel + primary stiffening + main decks
- Local models of critical joints, spin-bearing interfaces, and penetrations
- Mesh density and element type justified for the dominant load cases
- Safety factors and knockdown factors explicitly stated and traceable to aerospace practice (or more conservative)
- Output: mass breakdown by major structural element, peak stresses, margins, and buckling eigenvalues

## 3. Deliverables

1. Material Candidate Matrix & Selection Recommendation (with PATSAGi review)
2. Geometry and Load Case Specification (configuration-controlled)
3. Global FE model description + results summary
4. Updated rotating-habitat structural mass number (with uncertainty bounds)
5. Recommended design changes (if any) to reduce mass while preserving margins
6. Formal update to `manufacturing/reference-seed-mass-budget.md`

## 4. Success Criteria

- Structural mass for the rotating habitat is reduced from a factor-of-2.5 range to a ±15–20 % band
- All primary load cases show positive margins under the chosen material system
- The mass number is accepted by PATSAGi and human authority for the next mass-budget revision

## 5. Dependencies & Interfaces

- Inputs: `systems/structure/dsa-ref-a-structural-mass-estimate.md`, deck layout, volume allocation
- Outputs feed: top-level mass budget, risk picture, industrial capacity analysis
- Parallel: WP-DE-02 (Radiation Dose) may share water-tank geometry that affects structural load paths

## 6. Governance

All material recommendations and final mass numbers require PATSAGi deliberation and TOLC 8 valence check before the reconciled mass budget is updated.

---

**This work package is the single highest-leverage activity remaining that can still be advanced with analysis before physical hardware is required.**
