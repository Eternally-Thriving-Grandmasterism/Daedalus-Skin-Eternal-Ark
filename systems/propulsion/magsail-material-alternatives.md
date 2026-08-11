# Magnetic Sail — Material & Architecture Alternatives

**Status:** Alternatives analysis  
**Reference Design:** DSA-Ref-A  
**Owner:** Autonomicity Games Inc.  
**Last Updated:** 2026-08-11

## 1. Purpose

Explore realistic material and architectural options for the magnetic sail so that mass, deployment, thermal, and reliability trades can be made explicitly.

## 2. Functional Requirements Recap

- Generate a large effective magnetic moment / magnetosphere
- Survive deployment, dynamic loads, thermal cycling, and long-duration radiation
- Remain controllable in attitude and (ideally) reconfigurable or stowable
- Fit within or near the current 200–800 t planning allocation if possible

## 3. Architecture Options

| Architecture | Description | Primary Advantages | Primary Concerns |
|--------------|-------------|--------------------|------------------|
| Single large superconducting loop | One primary current loop of very large radius | Conceptual simplicity, maximum moment per conductor amp | Structural dynamics, single-point failure, deployment scale |
| Distributed multi-loop array | Multiple smaller loops or a grid | Redundancy, staged deployment, graceful degradation | Complexity of current distribution and control |
| Boom-supported or tensegrity structure | Lightweight structural support for conductor | Potentially lower structural mass | Deployment reliability, dynamic modes |
| Hybrid plasma / magnetic systems | Augment pure magnetic sail with plasma injection or other effects | Possible performance gain | Added complexity, power, and propellant |

**Current baseline preference:** Distributed multi-loop or segmented array for redundancy and staged deployment, pending higher-fidelity mass and dynamics work.

## 4. Conductor & Material Options

| Material / System | Advantages | Concerns for Multi-Year Interstellar Use |
|-------------------|------------|------------------------------------------|
| High-temperature superconductors (HTS) | Higher operating temperature, reduced cryogenic burden | Radiation tolerance, joint reliability, long-term stability still maturing |
| Low-temperature superconductors (LTS) | Mature performance in some applications | Heavy cryogenic system, vulnerability to thermal excursions |
| Advanced normal conductors (high-purity Al or Cu) with active cooling | No superconducting quench risk | Much higher power dissipation and radiator mass for same moment |
| Hybrid superconducting + structural composites | Integrated load-bearing and current-carrying function | Complex manufacturing and inspection |

**Planning preference:** HTS or advanced LTS with robust thermal control and radiation shielding of critical joints, pending radiation and aging data.

## 5. Key Trades Still Open

- Moment (performance) vs. conductor + structure mass
- Redundancy vs. total mass and complexity
- Operating temperature vs. cryogenic system mass and reliability
- Stowed volume and deployment reliability vs. on-orbit complexity

## 6. Decision Rule

No final material or architecture down-select occurs until:
1. Drag vs. moment curves exist across realistic densities
2. At least Gate E1 (subscale deployment + stability) data are in hand
3. Radiation and thermal aging data support multi-year operation claims

Until then the sail remains a high-uncertainty, high-leverage system with residual fusion propellant as the mandatory operational backup.

---

**This alternatives analysis keeps the sail design space open while preventing premature lock-in.**
