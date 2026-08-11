# Comparative Global FE Model Cases — CFRP vs Al-Li

**Status:** Defined for first execution cycle  
**Owner:** Autonomicity Games Inc.  
**Authority:** Ra-Thor + Permanent PATSAGi Councils under TOLC 8  
**Last Updated:** 2026-08-11  
**Linked:** WP-DE-01, dsa-ref-a-geometry-and-loads.md, allowables-and-safety-factors-wp-de-01.md

---

## 1. Purpose

Define the exact set of comparative finite-element models that will quantify the structural mass and performance difference between the primary (CFRP) and reference (Al-Li) material systems under identical geometry and load cases.

## 2. Model Pair Definition

Two otherwise identical global models shall be built and run:

| Model ID | Material System | Purpose |
|----------|-----------------|---------|
| FE-CFRP-01 | High-modulus CFRP (primary) | Mass-minimising case |
| FE-ALLI-01 | Aluminium-lithium (reference) | Calibrated metallic baseline |

Both models use:
- Identical geometry (140 m spin radius, 100 m axial length, 5 primary decks)
- Identical load cases (LC-01 through LC-08 as frozen)
- Identical mesh density strategy and element types (adjusted only as required by material anisotropy)
- The safety factors and knockdowns defined in `allowables-and-safety-factors-wp-de-01.md`

## 3. Required Output Comparison Table

For each model the following shall be reported side-by-side:

| Output | FE-CFRP-01 | FE-ALLI-01 | Delta |
|--------|------------|------------|-------|
| Total rotating habitat structural mass (t) | | | |
| Pressure shell + stiffening mass (t) | | | |
| Deck & internal structure mass (t) | | | |
| End bulkheads / spin interface mass (t) | | | |
| Peak tensile margin (critical LC) | | | |
| Peak compressive / buckling eigenvalue | | | |
| Maximum radial / axial deformation under spin | | | |
| Critical design driver (which LC / location) | | | |

## 4. Analysis Sequence

1. Build and verify both meshes under pure pressure (LC-01/02) for numerical stability.
2. Run the full load-case suite on both models.
3. Apply the long-duration aging factor to the CFRP results as a sensitivity case.
4. Produce the comparison table and narrative identifying mass drivers and any unexpected critical locations.
5. Present complete package to PATSAGi for baseline material selection deliberation.

## 5. Success Criteria for This Cycle

- Both models converge with positive margins under the defined factors.
- Mass difference is quantified with clear attribution to material properties vs design features.
- Results are configuration-controlled and ready for the next mass-budget revision.

---

**These comparative cases convert the material recommendation into measurable structural performance.**
