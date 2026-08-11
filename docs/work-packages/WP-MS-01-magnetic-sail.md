# WP-MS-01 — Magnetic Sail Mass Envelope, Architecture Options & Packaging

**Phase:** Detailed Engineering, Simulation & Technology Maturation  
**Priority:** Primary open technical uncertainty (post Cycle-01)  
**Owner:** Autonomicity Games Inc.  
**Authority:** Ra-Thor + Permanent PATSAGi Councils under TOLC 8  
**Status:** Open  
**Created:** 2026-08-11  
**Linked:** systems/propulsion/dsa-ref-a-magsail-sizing.md, magsail-material-alternatives.md, reference-seed-mass-budget.md

---

## 1. Objective

Quantify the magnetic-sail mass envelope under reference interstellar flux assumptions, baseline three distinct architecture options, and produce mass + packaging deliverables that can be folded into the reconciled mass budget and risk picture.

## 2. Reference Performance Target

- Decelerate DSA-Ref-A from ~0.055 c to interplanetary speeds in an acceptable time (target: years to low tens of years).
- Residual fusion propellant remains the mandatory operational backup.
- Interstellar plasma density is low and variable; design must remain useful across a realistic density range.

## 3. Three Baseline Architecture Options

| Option | Architecture | Primary Conductor Approach | Key Characteristics |
|--------|--------------|----------------------------|---------------------|
| **MS-A** | Single large superconducting loop | HTS or advanced LTS primary loop | Maximum moment per amp; simplest current path; single-point structural risk |
| **MS-B** | Distributed multi-loop / segmented array | Multiple smaller HTS loops with current sharing | Redundancy, staged deployment, graceful degradation; higher control complexity |
| **MS-C** | Boom-supported / tensegrity hybrid | Lightweight structural booms + superconducting elements | Potentially lowest structural mass fraction; deployment dynamics critical |

## 4. Mass Envelope Quantification (First-Order)

All values are planning estimates under reference flux assumptions for a Seed Vessel of ~15–17 kt dry mass. They will be refined by higher-fidelity plasma and structural models.

| Option | Conductor + Cryogenics (t) | Structure / Support (t) | Deployment & Control (t) | Contingency (t) | **Total System Mass (t)** | Notes |
|--------|----------------------------|-------------------------|--------------------------|-----------------|---------------------------|-------|
| **MS-A** Single loop | 180–320 | 120–250 | 40–80 | 50–100 | **390–750** | Highest single-point risk |
| **MS-B** Multi-loop array | 200–380 | 150–280 | 60–120 | 60–120 | **470–900** | Preferred for redundancy |
| **MS-C** Boom / tensegrity | 160–300 | 80–180 | 50–100 | 50–100 | **340–680** | Lowest mass potential; highest dynamics risk |

**Working planning band for DSA-Ref-A (all options):** **350–900 t**  
Previous mass-budget allocation (200–700 t) remains compatible with the lower-to-mid portion of this envelope; the upper end requires explicit acceptance of higher sail mass or reduced performance margin.

## 5. Packaging & Stowage Deliverables

- Stowed volume and location along the non-rotating spine (or dedicated sail bay)
- Deployment sequence and time
- Failure modes and recovery (especially for single-loop vs multi-loop)
- Interaction constraints with forward particle shield and residual thrust plumes
- Thermal and radiation protection for superconducting joints and current leads

## 6. Required Outputs of This Work Package

1. Updated mass envelope table (this document is the seed)
2. Side-by-side comparison of MS-A / MS-B / MS-C on mass, redundancy, deployment risk, and performance sensitivity
3. Recommended baseline architecture for the next mass-budget revision (or explicit retention of a range)
4. Packaging concept sketches / descriptions sufficient for interface definition with the spine
5. Updated risk register entries for sail mass, deployment, and performance shortfall

## 7. Success Criteria

- Magnetic-sail mass is no longer an open-ended range; it is bounded by architecture option
- At least one architecture is identified as the preferred baseline (or a dual-path is deliberately retained)
- Packaging interfaces are defined well enough for spine structural design
- Residual fusion propellant remains explicitly sized as the performance backup

## 8. Governance

No architecture is locked until higher-fidelity drag models and at least Gate E1 (subscale deployment + stability) data exist. Residual fusion propellant is non-negotiable under TOLC 8.

---

**Magnetic sail mass is now quantified by architecture. WP-MS-01 is the living vehicle for closing this uncertainty.**
