# DSA-Ref-A — Sail Under-Performance Sensitivity Analysis

**Status:** Quantitative sensitivity baseline  
**Reference Design:** DSA-Ref-A  
**Owner:** Autonomicity Games Inc.  
**Last Updated:** 2026-08-11

## 1. Purpose

Quantify how magnetic sail under-performance propagates into residual fusion propellant demand and total initial mass, so that the program can set rational margins and decision triggers.

## 2. Baseline Assumption

- Primary deceleration is provided by the magnetic sail.
- Only a modest residual fusion propellant load is retained for final maneuvers, contingency, and partial backup deceleration.
- Cruise velocity planning point: ~0.055 c.

## 3. Sensitivity Logic

If the sail delivers only a fraction of the expected deceleration Δv, the shortfall must be made up by fusion reverse thrust (or the mission timeline / terminal velocity must be relaxed).

Because rocket Δv is exponential in mass ratio, even moderate sail shortfalls can drive large increases in required residual propellant if the ship attempts to recover the full planned terminal condition with thrust alone.

## 4. Planning Scenarios

| Sail Performance vs. Prediction | Program Response | Mass / Timeline Impact |
|---------------------------------|------------------|------------------------|
| 100% (nominal) | Baseline residual propellant | Nominal |
| 70–90% | Accept longer deceleration time and/or modest extra residual propellant | Moderate |
| 40–70% | Significant residual propellant increase or major timeline extension | High |
| <40% | Mission redesign or acceptance of higher arrival velocity / longer coast | Severe |

## 5. Design Rules Derived from Sensitivity

1. Size the residual propellant budget for at least a 30% sail under-performance case without breaking the mission.
2. Treat sail performance as a continuous risk until in-space calibration data exists (FT-3 and beyond).
3. Do not allow the residual propellant allocation to erode below the level needed for the 30% under-performance case plus emergency margins.
4. If higher-fidelity models or early tests show expected performance below ~70% of current planning assumptions, immediately revisit cruise velocity target or total mass ratio.

## 6. Next Quantitative Work

- Produce explicit Δv shortfall → propellant mass curves for the reference dry mass
- Link sail mass growth options against residual propellant mass in a joint trade
- Update the reconciled mass budget when the preferred margin case is selected

---

**This sensitivity analysis keeps deceleration risk visible and financially/ structurally honest.**
