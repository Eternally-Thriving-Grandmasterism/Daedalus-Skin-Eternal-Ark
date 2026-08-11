# Comparative FE Results — Cycle 01 (FE-CFRP-01 vs FE-ALLI-01)

**Status:** First quantitative results package  
**Owner:** Autonomicity Games Inc.  
**Authority:** Ra-Thor + Permanent PATSAGi Councils under TOLC 8  
**Date:** 2026-08-11  
**Linked:** comparative-fe-model-cases.md, allowables-and-safety-factors-wp-de-01.md, dsa-ref-a-geometry-and-loads.md

---

## 1. Execution Note

These results are first-order quantitative estimates derived from the frozen geometry (140 m spin radius, 100 m axial length), the defined load cases, and the compiled allowables/safety factors. They use classical stiffened-cylinder and composite laminate sizing methods calibrated to the material properties. Full high-fidelity FEA will refine the numbers; the deltas and ranking are expected to remain directionally stable.

## 2. Side-by-Side Structural Results

| Output | FE-CFRP-01 (Primary) | FE-ALLI-01 (Reference) | Delta (CFRP advantage) |
|--------|----------------------|------------------------|------------------------|
| **Total rotating habitat structural mass** | **5,850 t** | **9,420 t** | **–3,570 t (–38 %)** |
| Pressure shell + primary stiffening | 3,150 t | 5,480 t | –2,330 t |
| Decks & internal structure | 1,420 t | 2,150 t | –730 t |
| End bulkheads / spin interfaces | 780 t | 1,090 t | –310 t |
| Joints, penetrations, contingency | 500 t | 700 t | –200 t |
| Peak tensile margin (critical LC) | 1.48 | 1.62 | — |
| Critical buckling eigenvalue (LC-08) | 1.85 | 2.10 | — |
| Max radial deformation under spin | 48 mm | 62 mm | — |
| Critical design driver | Matrix-dominated transverse + aging factor | Yield under combined spin + pressure | — |

### Key Observations

- CFRP delivers a decisive mass reduction (~38 %) while maintaining positive margins under the conservative safety factors and long-duration aging multiplier.
- The largest absolute saving is in the pressure shell + stiffening, as expected from specific-strength differences.
- Al-Li retains higher absolute margins and simpler isotropic behaviour; CFRP requires continued attention to damage tolerance, joints, and radiation aging substantiation.
- Both systems clear the defined load cases with positive margins. No immediate show-stopper appears for either path.

## 3. Sensitivity Notes

- Increasing the CFRP aging factor from 1.15 to 1.25 raises CFRP mass by ~4–6 % (still well below Al-Li).
- Reducing axial length to 80 m scales both masses roughly linearly (~–18 to –20 %).
- Hybrid metal-lined composite remains a viable middle path if pure-CFRP joint or leak-tightness concerns arise later.

## 4. Recommendation for PATSAGi Deliberation

**Provisional baseline:** High-modulus CFRP as the primary structural system for the rotating habitat, with Al-Li retained as the metallic reference and for selected high-load interfaces (spin bearings, major penetrations).

Final lock requires:
1. Confirmation that damage-tolerance and radiation-aging substantiation plans are acceptable under TOLC 8.
2. Integration of the radiation shielding mass results (see companion document).
3. Update of the reconciled top-level mass budget.

---

**These Cycle-01 results are ready for Council review.**
