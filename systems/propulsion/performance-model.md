# Propulsion Performance Model — Initial

**Status:** Preliminary / Phase 0.5  
**Owner:** Autonomicity Games Inc.

## Design Baseline

- Drive type: High-repetition-rate Inertial Confinement Fusion (ICF)
- Fuel: Deuterium + Helium-3 (D–³He)
- Exhaust mechanism: Superconducting magnetic nozzle
- Target pulse rate: ≥ 100–250 Hz (to approximate continuous thrust)
- Exhaust velocity (v_ex): 9,000 – 12,000 km/s (Isp ≈ 920,000 – 1,220,000 s)

## Rocket Equation Implications

Δv = v_ex × ln(m₀ / m_f)

For a cruise velocity of 0.1c (≈ 30,000 km/s):

- Required mass ratio (m₀ / m_f) ≈ e^(Δv / v_ex)
- Using v_ex = 10,000 km/s → mass ratio ≈ e³ ≈ 20
- Using v_ex = 12,000 km/s → mass ratio ≈ e^(2.5) ≈ 12.2

This implies that even with optimistic performance, a large fraction of the initial mass must be propellant. Staging and drop tanks are mandatory for practical Worldship designs.

## Acceleration Profile

Continuous low-thrust boost is preferred for crew comfort and structural loads:
- Target acceleration: 0.001 – 0.01 g (≈ 0.01 – 0.1 m/s²)
- Boost duration: years rather than months
- Coast phase dominates for distant targets

## Deceleration

Primary options:
1. Reverse thrust with remaining propellant (expensive in mass)
2. Magnetic sail interacting with interstellar plasma / stellar wind
3. Beamed energy or laser sail from destination infrastructure (future capability)

Hybrid 2 + residual reverse thrust is the baseline for early vessels.

## Open Engineering Tasks

- [ ] Detailed pellet mass, energy driver, and fusion gain model
- [ ] Magnetic nozzle efficiency vs. thermal load analysis
- [ ] Staging architecture and tank jettison strategy
- [ ] Integration with magnetic sail for braking
- [ ] ³He sourcing and ISRU pathways
