# DSA-Ref-A — Magnetic Sail Drag Performance vs. Plasma Density

**Status:** Quantitative guidance  
**Reference Design:** DSA-Ref-A (cruise ~0.055 c)  
**Owner:** Autonomicity Games Inc.  
**Last Updated:** 2026-08-11

## 1. Objective

Provide working quantitative relationships so that sail size, mass, and deceleration time can be traded against realistic interstellar plasma densities.

## 2. Key Dependencies

Drag force on a magnetic sail scales with:
- Magnetic moment (or effective magnetospheric cross-section)
- Relative velocity between ship and plasma
- Local plasma mass density and velocity distribution

Interstellar medium density is low and spatially variable. Typical orders of magnitude used in planning are ~0.05–0.2 particles/cm³ for protons, with significant uncertainty and local variation.

## 3. Design Consequences for DSA-Ref-A

- Even optimistic densities require a very large effective magnetic moment to produce useful deceleration from 0.055 c in less than several decades.
- Sail mass grows with the conductor and structural system needed to create and support that moment.
- Deceleration time is likely measured in years to tens of years; mission architecture must accept this.
- Residual fusion propellant remains essential for final braking, trajectory correction, and contingency.

## 4. Current Quantitative Stance

Until validated high-fidelity simulations exist, the program adopts the following planning rules:

- Size the sail for the lower end of expected interstellar densities (conservative).
- Accept multi-year deceleration timelines.
- Keep sail system mass inside or near the current 200–800 t allocation; if higher-fidelity work shows this is impossible for acceptable timelines, the residual propellant budget and overall mass ratio must be revisited.
- Treat sail performance as a top technology risk until flight-relevant data or validated simulations close the uncertainty.

## 5. Required Next Calculations

- Drag force vs. magnetic moment curves at 0.03–0.07 c across a density range of ~0.01–0.5 cm⁻³
- Translation of required moment into conductor mass and structural mass
- Sensitivity of total mission Δv budget to sail under-performance

---

**This guidance keeps magnetic sail expectations realistic and directly linked to mass and timeline consequences.**
