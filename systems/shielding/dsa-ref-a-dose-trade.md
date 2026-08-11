# DSA-Ref-A — Dose vs. Areal Density & Active/Passive Shielding Trade

**Status:** Quantitative trade framework  
**Reference Design:** DSA-Ref-A  
**Owner:** Autonomicity Games Inc.  
**Last Updated:** 2026-08-11

## 1. Objective

Determine the minimum-mass shielding approach that keeps crew dose within acceptable limits for the reference mission duration.

## 2. Passive Shielding — Areal Density Guidance

Long-duration GCR protection typically requires substantial areal density. Representative planning values from space radiation literature:

| Areal Density (g/cm²) | Approximate Effect | Notes |
|-----------------------|--------------------|-------|
| 10–20 | Meaningful SPE protection, limited GCR reduction | Minimum for storm shelters |
| 20–40 | Better GCR reduction | Common planning range for long missions |
| 40–60+ | Stronger GCR attenuation | Mass becomes very large |

Water and polyethylene are preferred because of high hydrogen content (lower secondary production than high-Z materials).

## 3. Dual-Use Water Strategy

For DSA-Ref-A the life-support water inventory should be deliberately located to provide as much of the required areal density as possible around primary living volumes and storm shelters. Dedicated shielding mass is added only for the shortfall.

## 4. Active Magnetic Shielding Trade

Active systems can deflect charged particles and thereby reduce the required passive mass. The trade must account for:

- Coil mass and structural support
- Continuous or peak power demand
- Cryogenic / superconducting system mass and reliability
- Effectiveness against the GCR spectrum (high-energy particles are harder to deflect)

**Decision rule for DSA-Ref-A:**  
Adopt active shielding only if the total mass + power system mass is clearly lower than the pure passive mass required for the same dose target, and if reliability is acceptable under TOLC 8.

## 5. Current Planning Stance

- Storm shelters sized for high areal density (SPE protection)
- Primary living volumes protected by a combination of dual-use water + moderate dedicated passive mass
- Active magnetic shielding kept as a high-priority trade study, not yet baseline
- Forward particle shield treated separately (physical impact protection)

## 6. Required Quantitative Work

- Mission-specific dose calculations (GCR + SPE) for 10–25 year exposure
- Optimal water placement geometry
- Active shielding performance vs. mass/power curves at Seed Vessel scale
- Updated shielding mass allocation in the top-level budget

---

**This trade framework is now the basis for replacing shielding mass uncertainty with calculated values.**
