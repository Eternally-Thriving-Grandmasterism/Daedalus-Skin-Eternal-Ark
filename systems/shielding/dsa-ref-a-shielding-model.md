# DSA-Ref-A — Higher-Fidelity Radiation Shielding Model

**Status:** Refined modeling guidance  
**Reference Design:** DSA-Ref-A  
**Owner:** Autonomicity Games Inc.  
**Last Updated:** 2026-08-11

## 1. Design Objective

Keep long-duration crew dose within acceptable limits for a multi-year to multi-decade mission while minimizing mass.

## 2. Shielding Layers (Reference Architecture)

1. **Passive hydrogen-rich mass** — water, polyethylene, or specialized composites placed around primary living volumes
2. **Dual-use life-support water** — deliberately located to serve as shielding
3. **Active magnetic shielding** — superconducting coils to deflect charged particles (trade against power and coil mass)
4. **Storm shelters** — higher areal density zones for solar particle events
5. **Forward particle/dust shield** — physical protection against high-speed interstellar impacts

## 3. Modeling Approach

- Use areal density (g/cm²) as the primary passive shielding metric
- Separate Galactic Cosmic Ray (GCR) and Solar Particle Event (SPE) cases
- Account for secondary radiation production in the shield itself
- Evaluate dose to blood-forming organs and effective dose for career and mission limits
- Perform trades of passive mass vs. active magnetic system power/mass

## 4. Current Guidance for DSA-Ref-A

- Maximize water dual-use before adding dedicated shielding mass
- Size storm shelters for the worst credible SPE with margin
- Treat active magnetic shielding as a high-value option that must prove its mass + power cost is lower than the passive mass it saves
- Forward shield mass is relatively independent of habitat shielding and must be carried regardless

## 5. Required Analyses

- Dose vs. areal density curves for the reference mission duration and solar conditions
- Optimal distribution of water mass around the habitat
- Active shielding effectiveness vs. coil mass and power for the Seed Vessel scale
- Combined passive + active system mass minimum

---

**Shielding mass remains one of the largest dry-mass uncertainties. Higher-fidelity transport calculations are a top priority.**
