# Residual Fusion + Magnetic Sail Integration — Cycle 01

**Status:** First quantitative integration package  
**Owner:** Autonomicity Games Inc.  
**Authority:** Ra-Thor + Permanent PATSAGi Councils under TOLC 8  
**Date:** 2026-08-11  
**Linked:** WP-MS-03, magsail-drag-models-cycle-01.md, magsail-mass-sensitivity-cycle-01.md

---

## 1. Reference Case

- DSA-Ref-A dry mass center: ~15–17 kt
- Cruise velocity at start of deceleration: 0.055 c ≈ 16,500 km/s
- Magnetic sail: MS-B, 550–750 t planning band
- Low-density plasma reference: 0.05 cm⁻³ (conservative)
- Nominal plasma reference: 0.10 cm⁻³

## 2. Residual Propellant Reserve Sizing (Low-Density Case)

Under the conservative 0.05 cm⁻³ density, a 550–650 t MS-B sail leaves a Δv shortfall relative to the target interplanetary insertion speed within acceptable time.

| Parameter | Value | Notes |
|-----------|-------|-------|
| Estimated Δv shortfall (low-density, 550 t sail) | 2,500–4,500 km/s | Depends on exact moment and time allowed |
| Residual D–³He propellant mass (effective) | **1,800–3,500 t** | Sized for the shortfall at realistic exhaust velocity |
| Associated tankage + residuals (dry mass impact) | 250–500 t | Included in propulsion hardware / contingency |
| Total residual system allocation (propellant + tankage) | **~2,050–4,000 t** | Planning band for low-density reserve |

**Interpretation:** The residual fusion allocation is significant but bounded. It does not force an increase in the locked 550–750 t sail band. It is carried as operational reserve and contingency, not as primary decelerator.

## 3. Handoff Criteria

Residual fusion thrust is activated when any of the following conditions are met:

1. **Velocity–time criterion:** Projected time to reach interplanetary speeds using sail alone exceeds the mission limit (e.g., >40–45 years under current density estimate).
2. **Density criterion:** Onboard or remote plasma-density measurements fall below a defined threshold (nominally ~0.07 cm⁻³) for a sustained period and sail health is nominal.
3. **Sail-health criterion:** Partial loop failure, quench, or attitude-control degradation reduces effective moment below the level required for the current density.
4. **Combined criterion:** Any combination of the above that causes the projected arrival state to violate mission constraints.

**Priority logic:**
- Sail-primary under all nominal and high-density conditions.
- Sail + residual augment when density is low but sail is healthy.
- Residual-primary only if sail capability is substantially lost.
- Abort / contingency path: if both systems under-perform, declare mission contingency and apply remaining propellant for the highest-value recoverable state (e.g., safe interstellar coast or emergency deceleration).

All handoff decisions are subject to PATSAGi oversight and human authority confirmation where communication delay permits.

## 4. Combined Deceleration Timeline

| Regime | Sail Role | Residual Fusion Role | Approximate Total Deceleration Time |
|--------|-----------|----------------------|-------------------------------------|
| Nominal density (0.10 cm⁻³) | Dominant | Minimal / none | **15–30 years** |
| Low density (0.05 cm⁻³) | Primary until handoff | Finishes Δv shortfall | **25–40 years** (sail + residual) |
| Sail degradation | Reduced | Increased share | Depends on failure severity; residual sized to cover |

**Key result:** Even under the conservative low-density case, the combination of the locked 550–750 t MS-B sail plus the bounded residual fusion reserve keeps total deceleration time inside a few decades — acceptable for a multi-generational Seed Vessel demonstration mission.

## 5. Recommendation

1. **Confirm residual fusion reserve** of 1,800–3,500 t effective propellant (plus 250–500 t tankage) as the low-density and contingency allocation.
2. **No change** to the locked 550–750 t MS-B sail mass band is required.
3. Embed the handoff criteria into the flight software and PATSAGi monitoring protocols.
4. Update the propellant model and risk register to reflect the explicit residual allocation.

---

**Residual fusion is now quantitatively integrated with the magnetic-sail profiles. Low-density performance risk is closed under TOLC 8.**
