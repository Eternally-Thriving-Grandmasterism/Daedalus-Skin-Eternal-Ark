# Spin Radius & Comfort Analysis — Rotating Habitats

**Status:** Accepted baseline (WP-05 complete)  
**Owner:** Autonomicity Games Inc.  
**Related:** ADR-0002  
**Last Updated:** 2026-08-11

## 1. Design Goal

Provide continuous artificial gravity of 0.8–1.0 g in primary living areas while keeping Coriolis effects, cross-coupled accelerations, and vestibular disturbance within acceptable long-term comfort limits for a multi-generational population.

## 2. Key Physics

Artificial gravity level:  
$$a = \omega^2 r = \frac{v^2}{r}$$

Where:
- $a$ = centripetal acceleration (target 0.8–1.0 g ≈ 7.85–9.81 m/s²)
- $r$ = spin radius (distance from axis to floor)
- $\omega$ = angular velocity

## 3. Comfort Constraints (Established Guidelines)

Long-duration comfort literature and spacecraft design practice generally recommend:

- Spin rate preferably ≤ 2–3 rpm for most of the population (some adaptation possible up to ~4 rpm)
- Higher radius is strongly preferred because it reduces angular velocity for the same gravity level and reduces Coriolis effects when moving radially or vertically
- Head-to-floor gravity gradient should remain modest

## 4. Reference Design Points

| Target Gravity | Desired Max Spin Rate | Required Radius | Notes |
|----------------|-----------------------|-----------------|-------|
| 1.0 g | 2 rpm | ≈ 224 m | Very comfortable, large structure |
| 1.0 g | 3 rpm | ≈ 99 m | Acceptable for many, more compact |
| 0.9 g | 2 rpm | ≈ 201 m | |
| 0.8 g | 2 rpm | ≈ 179 m | |
| 0.8 g | 3 rpm | ≈ 80 m | Lower bound for good comfort |

**Baseline recommendation for full Worldship:**  
Aim for spin radius ≥ 150–200 m in primary residential cylinders/tori so that spin rate stays near or below 2 rpm at ~0.9–1.0 g. Smaller radii may be accepted in early seed vessels with careful crew selection and adaptation protocols.

## 5. Architectural Implications

- Large radius favors cylindrical or toroidal habitats of significant diameter.
- Counter-rotating pairs are preferred to cancel net angular momentum.
- Non-rotating central spine remains useful for propulsion, docking, industry, and zero-g research.
- Transfer between rotating and non-rotating sections requires carefully designed elevators, ramps, or despin mechanisms.

## 6. Open Refinements

- Exact comfort acceptance curves for multi-generational populations (including children and elderly)
- Gravity gradient limits from head to foot
- Combined effects of residual ship acceleration during boost
- Bearing and structural mass penalties vs. radius

---

**PATSAGi / TOLC 8 note:** Comfort and long-term physiological health are zero-harm issues. Larger radius is preferred even at higher structural cost when feasible.
