# Magnetic Sail Mass Envelope — Cycle 01 (Reference Flux)

**Status:** First quantitative architecture comparison  
**Owner:** Autonomicity Games Inc.  
**Authority:** Ra-Thor + Permanent PATSAGi Councils under TOLC 8  
**Date:** 2026-08-11  
**Linked:** WP-MS-01, dsa-ref-a-magsail-sizing.md, magsail-material-alternatives.md

---

## 1. Reference Assumptions

- DSA-Ref-A dry mass center: ~15–17 kt
- Cruise velocity: ~0.055 c
- Target deceleration time: years to low tens of years (not centuries)
- Interstellar plasma density: reference low-density range (variable; design must tolerate lower than average)
- Residual fusion propellant retained as mandatory performance backup

## 2. Three Architecture Options — Mass Breakdown

| Component | MS-A Single Loop (t) | MS-B Multi-Loop Array (t) | MS-C Boom / Tensegrity (t) |
|-----------|----------------------|---------------------------|----------------------------|
| Superconducting conductor + leads | 120–220 | 140–260 | 110–210 |
| Cryogenics & thermal control | 60–100 | 60–120 | 50–90 |
| Primary structure / support | 120–250 | 150–280 | 80–180 |
| Deployment mechanisms & actuators | 25–50 | 40–80 | 35–70 |
| Attitude control & current management | 15–30 | 20–40 | 15–30 |
| Contingency & joints | 50–100 | 60–120 | 50–100 |
| **Total System Mass** | **390–750** | **470–900** | **340–680** |

## 3. Comparative Assessment

| Criterion | MS-A Single Loop | MS-B Multi-Loop Array | MS-C Boom / Tensegrity |
|-----------|------------------|-----------------------|------------------------|
| Mass potential | Medium | Higher | Lowest potential |
| Redundancy | Low (single-point) | High | Medium |
| Deployment risk | High (scale) | Medium (staged) | High (dynamics) |
| Control complexity | Low | Higher | Medium–High |
| Graceful degradation | Poor | Excellent | Moderate |
| Preferred for | Maximum simplicity | Baseline reliability | Mass-critical designs |

## 4. Working Recommendation (Provisional)

**Preferred baseline for DSA-Ref-A:** **MS-B (Distributed multi-loop / segmented array)**  
Rationale: Best balance of redundancy, staged deployment, and graceful degradation under TOLC 8 zero-harm and long-duration reliability priorities. Mass penalty relative to MS-C is acceptable given the criticality of the deceleration system.

**MS-C** remains the mass-minimising alternative if higher-fidelity dynamics work later demonstrates acceptable deployment reliability.  
**MS-A** is retained only as a conceptual reference or for very large single-loop technology demonstration articles.

## 5. Packaging Implications

- All options are designed for stowage along or around the non-rotating central spine during boost and coast phases.
- Deployment occurs after the boost phase is complete and the ship is oriented for deceleration.
- Forward particle shield and residual nozzle plume interaction zones must be kept clear of the deployed sail volume.
- Stowed volume target: compatible with spine diameter and available axial length without major dry-mass growth.

## 6. Impact on Mass Budget

- Previous allocation: 200–700 t  
- Cycle-01 quantified envelope: **340–900 t** across the three options  
- Recommended planning value for next budget revision (MS-B centered): **550–750 t**

This raises the upper end of the sail allocation modestly while converting an open uncertainty into a bounded, architecture-specific range.

## 7. Open Items for Higher Fidelity

- Drag vs. magnetic moment curves across realistic density distributions
- Structural dynamics and deployment simulation for each architecture
- Radiation and thermal aging of HTS joints and current leads
- Gate E1 subscale deployment and stability data

---

**Magnetic sail mass is now quantified by architecture under reference flux. The primary open uncertainty has been reduced to a bounded envelope.**
