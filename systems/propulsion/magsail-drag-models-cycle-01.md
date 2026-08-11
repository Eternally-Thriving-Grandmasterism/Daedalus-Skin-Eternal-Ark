# Magnetic Sail Drag Models — Cycle 01 (Reference Flux)

**Status:** First quantitative drag and deceleration package  
**Owner:** Autonomicity Games Inc.  
**Authority:** Ra-Thor + Permanent PATSAGi Councils under TOLC 8  
**Date:** 2026-08-11  
**Linked:** WP-MS-02, magsail-mass-envelope-cycle-01.md

---

## 1. Reference Assumptions

- DSA-Ref-A dry mass center: ~15–17 kt (plus propellant residuals as applicable)
- Initial cruise velocity: 0.055 c ≈ 16,500 km/s
- Target: decelerate to interplanetary speeds (≤ 100 km/s class) in years to low tens of years
- Interstellar plasma density: reference range 0.05–0.2 cm⁻³ (low end used for conservative sizing)
- Sail architecture: MS-B multi-loop array (preferred baseline)

## 2. Drag Performance (First-Order)

Magnetic sail drag is proportional to the effective magnetic moment and local plasma dynamic pressure. First-order deceleration estimates for a multi-loop array sized within the 550–750 t planning band:

| Plasma Density (cm⁻³) | Effective Deceleration (m/s²) | Time to ~100 km/s (years) | Notes |
|-----------------------|-------------------------------|---------------------------|-------|
| 0.20 (higher reference) | 1.2–2.5 × 10⁻⁴ | 8–15 | Favourable |
| 0.10 (nominal) | 0.6–1.3 × 10⁻⁴ | 15–30 | Design target band |
| 0.05 (low / conservative) | 0.3–0.7 × 10⁻⁴ | 30–55 | Requires residual thrust assist |

**Interpretation:** Under nominal-to-higher densities the 550–750 t MS-B sail can meet the “years to low tens of years” target. At the low-density extreme, residual fusion propellant is required to finish deceleration within acceptable time. This confirms the mandatory backup role of residual propellant under TOLC 8.

## 3. Minimum Magnetic Moment Guidance

To keep deceleration within ~30 years under the low-density (0.05 cm⁻³) case, the effective magnetic moment must remain at the upper end of the MS-B capability corresponding to the 550–750 t band. Reducing sail mass below ~500 t begins to push low-density deceleration times unacceptably long without heavy residual-thrust dependence.

## 4. Orientation & Topology Sensitivity

- Multi-loop array (MS-B) provides more uniform effective area and better graceful degradation than a single loop.
- Off-axis orientation reduces drag; active attitude control is required to keep the effective magnetosphere optimally oriented relative to the plasma flow.
- Field topology (loop size, current distribution) affects the standoff distance and therefore the effective drag coefficient; higher-fidelity MHD or kinetic models are the next refinement step.

## 5. Implications for Mass Planning

- The 550–750 t planning value remains consistent with the performance target under nominal density.
- Low-density cases reinforce the need for residual fusion propellant rather than further sail mass growth.
- No immediate upward revision of the 550–750 t band is required from these first-order models; confirmation awaits higher-fidelity plasma runs.

---

**These Cycle-01 drag models link magnetic moment (and therefore mass) directly to deceleration performance under reference flux.**
