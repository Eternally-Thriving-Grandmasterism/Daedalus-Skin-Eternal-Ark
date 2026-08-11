# Top-Level Power Budget Framework

**Status:** Baseline framework (WP-04 complete)  
**Owner:** Autonomicity Games Inc.  
**Last Updated:** 2026-08-11

## 1. Power Sources

Primary: D–³He fusion reactors (shared with or dedicated from the propulsion system).
Secondary / backup: Additional fusion modules, energy storage, and limited radioisotope or other emergency sources.

## 2. Major Continuous Loads (Qualitative Ranking)

1. Propulsion / magnetic nozzle systems (during burn)
2. Life support — especially plant and photobioreactor lighting
3. Active magnetic radiation shielding (if used at high power)
4. Habitat systems (thermal control, air handling, water processing, computing)
5. Manufacturing / maintenance workshops
6. Communications, sensors, and governance computing

## 3. Scaling Behavior

- Life support power scales strongly with population (lighting dominated).
- Structural and spin systems have more modest continuous power needs.
- Propulsion power is enormous during boost but zero during pure coast.
- Design must size the power system for the highest continuous demand case (usually full population + life support + shielding + hotel loads) with margin.

## 4. Design Rules

- Multiple independent reactor clusters with isolation capability.
- No single failure shall cause loss of critical life support power.
- Large radiator area required; radiator mass is a significant dry-mass contributor.
- Energy storage sized for peak loads and emergency ride-through.

## 5. Open Quantitative Work

- Reference power demand table for 10,000 and 25,000 population cases
- Radiator area and mass estimates
- Reactor specific power (kW/kg) targets
- Power distribution architecture and redundancy model

---

**PATSAGi note:** Power is a critical zero-harm system. Redundancy and graceful degradation are mandatory.
