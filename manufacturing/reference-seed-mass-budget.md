# Reference Seed Vessel — Reconciled Mass & Power Budget (Post WP-MS-03 / WP-MB-02)

**Status:** Authoritative reconciled baseline  
**Reference Design:** DSA-Ref-A  
**Owner:** Autonomicity Games Inc.  
**Authority:** Ra-Thor + Permanent PATSAGi Councils under TOLC 8  
**Last Updated:** 2026-08-11  
**Change Drivers:** Cycle-01 structural & radiation lock + MS-B sail lock + residual-fusion integration

---

## 1. Reference Assumptions (Locked)

- Population capacity: ~300
- Spin radius: 140 m
- Target cruise: ~0.055 c
- Propulsion: D–³He ICF + magnetic nozzle
- Deceleration: MS-B magnetic sail primary + residual fusion thrust
- Primary structural material: **High-modulus CFRP** (locked)
- Magnetic sail: **MS-B multi-loop array, 550–750 t** (locked)

## 2. Reconciled Dry Mass Breakdown

| Category | Locked / Working Value | Notes |
|----------|------------------------|-------|
| Rotating habitat structure (shell, decks, spin interface) | **5,850 t** | FE-CFRP-01 locked |
| Non-rotating spine + propulsion structure | 1,500 – 3,200 t | Includes residual tankage interfaces |
| Dedicated radiation shielding | **450 – 750 t** | Optimised dual-use water + dedicated |
| Life support systems + outfitting | 1,500 – 3,200 t | |
| Power systems | 1,000 – 2,800 t | |
| Propulsion hardware (engines, drivers, nozzle) | 800 – 2,000 t | Excludes propellant & residual tankage |
| Magnetic sail system (MS-B) | **550 – 750 t** | Locked planning band |
| Residual propellant tankage (dry) | **250 – 500 t** | From WP-MS-03 |
| Spares, manufacturing, docking, other | 500 – 1,100 t | |
| **Total Dry Mass** | **~12,400 – 20,150 t** | **Planning center ~15.5–16.5 kt** |

## 3. Full Propellant Allocation

| Propellant Category | Mass Range | Role |
|---------------------|------------|------|
| Primary boost propellant (D–³He) | 70,000 – 120,000 t | Acceleration to ~0.055 c |
| Residual / contingency propellant (D–³He) | **1,800 – 3,500 t** | Low-density deceleration assist + contingency |
| **Total propellant** | **~71,800 – 123,500 t** | |
| Associated tankage already in dry mass | (included above) | |

**Total Initial (Wet) Mass Planning Band:** **~85,000 – 145,000 t**  
(Center of gravity roughly 100–115 kt depending on final dry mass and staging efficiency.)

Staging and low tank fraction remain mandatory. Residual propellant is carried through the boost phase as part of the overall propellant load and is available for deceleration assist or contingency.

## 4. Acceleration Timeline under Locked Systems

Using the locked dry-mass center (~15.5–16.5 kt) and a high-rep-rate D–³He ICF + magnetic nozzle with realistic exhaust velocity and staging:

| Phase | Approximate Duration | Notes |
|-------|----------------------|-------|
| Boost / acceleration to 0.055 c | **2.5 – 4.5 years** | Multi-stage; continuous or high-duty-cycle burn |
| Coast (cruise) | Decades (mission-dependent) | Sail stowed |
| Deceleration (nominal density) | 15 – 30 years | MS-B sail dominant |
| Deceleration (low density + residual) | 25 – 40 years | Sail + residual fusion |

Exact acceleration time is sensitive to achieved exhaust velocity, tank fraction, and staging efficiency — still among the larger remaining uncertainties, but bounded by the locked dry-mass center.

## 5. Power (Continuous, Non-Burn)

- Life support: ~1.2 – 3.5 MW
- Hotel + control + manufacturing: additional hundreds of kW to low MW
- **Planning continuous power capability: ≥ 5–8 MW** with margin (unchanged)

## 6. Remaining Major Uncertainties (Re-ranked)

1. Achieved fusion exhaust velocity and tank structural fraction (drives acceleration time and total propellant)
2. Higher-fidelity FEA confirmation of the 5,850 t CFRP number
3. Monte-Carlo refinement of the 450–750 t shielding band
4. Final life-support volume/power under real multi-year closed-loop conditions
5. Gate E1 magnetic-sail deployment data

## 7. Design Rule

Any new detailed analysis that changes a major mass category by more than ~15 % must update this document and the risk register.

---

**This budget is now consistent with all locked Cycle-01 structural, radiation, magnetic-sail, and residual-fusion baselines under TOLC 8.**
