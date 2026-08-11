# Reference Seed Vessel — Preliminary Mass & Power Budget

**Status:** Preliminary baseline (WP-13 complete)  
**Reference Design:** DSA-Ref-A  
**Owner:** Autonomicity Games Inc.  
**Last Updated:** 2026-08-11

All figures below are order-of-magnitude engineering estimates intended to anchor further detailed work. They will be refined as subsystem models mature.

---

## 1. Reference Assumptions

- Population capacity: ~300 (design point)
- Spin radius: ~140 m
- Target cruise capability: ~0.05–0.06 c
- Propulsion: D–³He ICF + magnetic nozzle
- Deceleration: Magnetic sail primary + residual thrust
- Triple redundancy on critical systems

## 2. Top-Level Dry Mass Categories (Preliminary)

| Category | Estimated Mass Range | Notes |
|----------|----------------------|-------|
| Structure + rotating habitat | 8,000 – 18,000 t | Dominant structural item |
| Radiation shielding (passive) | 4,000 – 12,000 t | Strongly dual-use with water |
| Life support & habitat outfitting | 1,500 – 4,000 t | Includes growth systems, water processing |
| Power systems (reactors, radiators, distribution) | 1,000 – 3,500 t | |
| Propulsion hardware (engines, nozzles, drivers) | 800 – 2,500 t | Excludes propellant |
| Magnetic sail system | 200 – 800 t | Highly uncertain |
| Spares, manufacturing, docking, other | 500 – 1,500 t | |
| **Total Dry Mass (preliminary)** | **~16,000 – 42,000 t** | Wide range reflects current uncertainty |

## 3. Propellant Mass

Using the performance model and a conservative mass ratio for ~0.05–0.06 c with staging:

- Propellant mass is expected to be several times the dry mass.
- Exact ratio depends on achieved exhaust velocity, tank fraction, and whether any propellant is reserved for deceleration.
- Staging / drop tanks remain mandatory.

A working planning figure for early studies: propellant mass ≈ 3× to 8× dry mass depending on final performance and staging efficiency.

## 4. Power Budget (Continuous, Non-Burn)

| Load | Approximate Scale | Notes |
|------|-------------------|-------|
| Life support (lighting dominant) | Multi-MW | Scales with population and crop area |
| Habitat hotel loads | Hundreds of kW to low MW | |
| Active shielding (if used) | Potentially MW-class | |
| Computing, control, communications | Lower | |
| Manufacturing / maintenance | Variable | |

Total continuous power demand for the reference population is expected in the low-to-mid tens of megawatts, with significant margin required.

During fusion burn the power and thermal loads rise dramatically and are dominated by the propulsion system.

## 5. Key Uncertainties (Highest Impact)

1. Actual structural mass fraction at 140 m class radius
2. Passive shielding areal density required for acceptable dose
3. Magnetic sail mass for useful deceleration times
4. Achieved fusion exhaust velocity and tank dry-mass fraction
5. Life-support volume and power per person under real closed-loop conditions

## 6. Next Refinement Steps

- Break structure and shielding into more detailed areal-density models
- Produce a first multi-stage propellant mass calculation with explicit tank fractions
- Develop crop-area and lighting-power tables for 300 people
- Size the magnetic sail parametrically for 0.05 c class deceleration

---

**This preliminary budget is now the quantitative anchor for the Reference Seed Vessel.** All future detailed models should reconcile against it or explicitly update it.
