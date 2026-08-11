# Propulsion Performance Model

**Status:** Accepted baseline (WP-01 complete)  
**Owner:** Autonomicity Games Inc.  
**Related:** ADR-0001  
**Last Updated:** 2026-08-11

## 1. Design Baseline

| Parameter | Value / Range | Notes |
|-----------|---------------|-------|
| Drive type | High-repetition-rate ICF | Magnetic nozzle |
| Fuel | Deuterium + Helium-3 (D–³He) | Aneutronic-leaning |
| Exhaust velocity (v_ex) | 9,000 – 12,000 km/s | Target design point 10,500 km/s |
| Specific Impulse | ~920,000 – 1,220,000 s | |
| Pulse rate | ≥ 100–250 Hz | Continuous thrust feel |
| Target cruise velocity | 0.05 – 0.12 c | Mission dependent |
| Boost acceleration | 0.001 – 0.01 g | Crew comfort + structural |

## 2. Rocket Equation & Mass Ratios

Δv = v_ex × ln(m₀ / m_f)

### Reference Cases (one-way Δv ≈ cruise velocity, no deceleration propellant yet)

| Target Cruise | v_ex = 9,000 km/s | v_ex = 10,500 km/s | v_ex = 12,000 km/s |
|---------------|-------------------|--------------------|--------------------|
| 0.05 c (15,000 km/s) | mass ratio ≈ 5.3 | ≈ 4.2 | ≈ 3.5 |
| 0.08 c (24,000 km/s) | ≈ 14.4 | ≈ 9.8 | ≈ 7.4 |
| 0.10 c (30,000 km/s) | ≈ 28 | ≈ 17.5 | ≈ 12.2 |
| 0.12 c (36,000 km/s) | ≈ 55 | ≈ 30.5 | ≈ 20.1 |

**Conclusion:** Even at optimistic 12,000 km/s, a 0.1c cruise already demands a mass ratio > 12. Staging and drop tanks are mandatory. Full propulsive deceleration roughly doubles the required Δv and makes pure rocket deceleration impractical for high cruise speeds. Magnetic sail + residual reverse thrust is the baseline deceleration strategy.

## 3. Staging Philosophy

- Multi-stage or drop-tank architecture modeled after Daedalus principles but scaled for crewed Worldship.
- Early stages carry the bulk of propellant and are jettisoned after boost.
- Final stage retains enough propellant for mid-course corrections, residual reverse thrust, and emergency maneuvers.
- Structural mass fraction of tanks must be aggressively minimized.

## 4. Acceleration & Mission Timeline (Example)

For a reference 0.1c cruise with 0.005 g average acceleration:

- Boost time ≈ (0.1c) / (0.005 × 9.81) ≈ 7.1 years
- Distance covered during boost is significant but still leaves a long coast for multi-light-year targets.
- Low continuous acceleration keeps structural loads and crew comfort acceptable.

## 5. Deceleration Baseline

1. Primary: Magnetic sail interacting with interstellar medium / stellar wind.
2. Secondary: Residual fusion reverse thrust.
3. Future: Beamed energy / laser infrastructure at destination systems.

## 6. Key Engineering Risks & Open Items

- Achieving and sustaining high fusion gain with D–³He at required pulse rates.
- Magnetic nozzle thermal management and lifetime.
- Pellet fabrication, injection, and reliability over multi-year burns.
- Tank structural mass fraction at Worldship scale.
- ³He acquisition cost and logistics.

## 7. Next Supporting Analyses Required

- Detailed pellet energy balance and driver requirements.
- Magnetic nozzle efficiency vs. mass and thermal rejection.
- Full multi-stage mass breakdown for a reference seed vessel and full Worldship.
- Magnetic sail sizing for deceleration from 0.05–0.12 c.

---

**PATSAGi / TOLC 8 note:** This propulsion baseline remains the highest-valence realistic option under known physics. All subsequent mass budgets must respect the mass-ratio implications above.
