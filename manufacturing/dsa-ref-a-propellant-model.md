# DSA-Ref-A — Multi-Stage Propellant Mass Model

**Status:** Detailed baseline  
**Reference Design:** DSA-Ref-A  
**Owner:** Autonomicity Games Inc.  
**Last Updated:** 2026-08-11

## 1. Design Point Assumptions

| Parameter | Value | Notes |
|-----------|-------|-------|
| Target cruise velocity | 0.055 c (≈ 16,500 km/s) | Conservative for Seed Vessel |
| Exhaust velocity (v_ex) | 10,500 km/s | Mid-range of performance model |
| Dry mass (from preliminary budget) | 25,000 t (planning center) | Midpoint of 16–42 kt range |
| Tank structural fraction | 8–12% of propellant mass | Aggressive but plausible with advanced composites |
| Staging | Two-stage + residual propellant on final stage | |

## 2. Rocket Equation Application

Required Δv for boost ≈ 16,500 km/s  
Mass ratio (ideal) = exp(Δv / v_ex) = exp(16,500 / 10,500) ≈ exp(1.571) ≈ **4.81**

### With Realistic Staging & Tank Fractions

Assuming two stages and 10% tank fraction:

- Stage 1 carries the majority of propellant and is jettisoned.
- Stage 2 + residual propellant remains with the ship.

**Planning figures for DSA-Ref-A:**

| Item | Mass (t) | Notes |
|------|----------|-------|
| Dry mass (ship) | 25,000 | Center of current estimate |
| Stage 1 propellant | ~70,000 – 90,000 | Dominant |
| Stage 1 tanks + structure | ~7,000 – 11,000 | Jettisoned |
| Stage 2 + residual propellant | ~25,000 – 40,000 | Remains with ship |
| Stage 2 tanks | ~2,500 – 5,000 | |
| **Total initial mass (order of magnitude)** | **~130,000 – 170,000 t** | |

These numbers are still preliminary and will tighten as dry mass and achieved v_ex are refined.

## 3. Deceleration Propellant

Baseline assumes magnetic sail provides the majority of deceleration.  
Only a modest residual propellant load (included above) is retained for final maneuvers, course correction, and emergency thrust.

## 4. Sensitivity

- Every 1,000 km/s improvement in v_ex significantly reduces propellant mass.
- Tank fraction is a high-leverage structural technology target.
- Dry mass growth has a multiplying effect on total propellant required.

## 5. Next Refinements

- Replace planning center dry mass with a more detailed bottom-up estimate
- Explicit three-stage vs two-stage trade
- Include mid-course correction and residual Δv budgets more precisely

---

**This model is now the working propellant baseline for DSA-Ref-A.**
