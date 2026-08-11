# Reference Seed Vessel — Updated Top-Level Mass & Power Budget

**Status:** Reconciled baseline (post-structural estimate)  
**Reference Design:** DSA-Ref-A  
**Owner:** Autonomicity Games Inc.  
**Last Updated:** 2026-08-11

This version absorbs the first analytical structural mass estimate and the current best thinking on shielding, propellant, and systems. Ranges remain deliberately wide where uncertainty is still high.

---

## 1. Reference Assumptions (Unchanged)

- Population capacity: ~300
- Spin radius: ~140 m
- Target cruise: ~0.055 c
- Propulsion: D–³He ICF + magnetic nozzle
- Deceleration: Magnetic sail primary + residual thrust

## 2. Updated Dry Mass Breakdown

| Category | Previous Range | Updated Working Range | Notes |
|----------|----------------|-----------------------|-------|
| Rotating habitat structure (shell, decks, spin interface) | (part of larger bucket) | **4,700 – 12,200 t** | From first analytical estimate |
| Non-rotating spine + propulsion structure | — | 1,500 – 4,000 t | Includes engine supports, tank interfaces |
| Passive radiation shielding (dedicated) | 4,000 – 12,000 t | **2,500 – 8,000 t** | Reduced by aggressive dual-use of water; still large |
| Life support systems + outfitting | 1,500 – 4,000 t | 1,500 – 4,000 t | Includes growth systems, processing |
| Power systems (reactors, radiators, distribution) | 1,000 – 3,500 t | 1,000 – 3,500 t | |
| Propulsion hardware (engines, drivers, nozzle) | 800 – 2,500 t | 800 – 2,500 t | Excludes propellant |
| Magnetic sail system | 200 – 800 t | 200 – 800 t | Still high uncertainty |
| Spares, manufacturing, docking, other | 500 – 1,500 t | 500 – 1,500 t | |
| **Total Dry Mass (reconciled)** | 16–42 kt | **~12,700 – 36,500 t** | Center of gravity still ~20–25 kt |

## 3. Propellant Mass (from multi-stage model)

Using the current propellant model and a ~20–25 kt dry-mass planning center:

- Total initial mass remains dominated by propellant.
- Working planning band for total initial mass: **~110,000 – 180,000 t** depending on final dry mass, achieved exhaust velocity, and staging efficiency.
- Staging and low tank fraction remain mandatory.

## 4. Power (Continuous, Non-Burn)

- Life support (lighting dominant): ~1.2 – 3.5 MW for 300 people
- Hotel + control + manufacturing: additional hundreds of kW to low MW
- Active shielding (if adopted): potentially MW-class
- **Planning continuous power capability: ≥ 5–8 MW** with significant margin

## 5. Largest Remaining Uncertainties (Ranked)

1. Final structural mass after material selection and FE analysis
2. Passive shielding mass after detailed dose calculations and water placement optimization
3. Magnetic sail mass required for acceptable deceleration time
4. Achieved fusion exhaust velocity and tank structural fraction
5. Life-support volume/power under real long-duration closed-loop conditions

## 6. Design Rule Going Forward

Any new detailed analysis that changes a major mass category by more than ~15% must update this document and the risk register.

---

**This reconciled budget is now the single quantitative anchor for DSA-Ref-A.** All future work should reference or update it.
