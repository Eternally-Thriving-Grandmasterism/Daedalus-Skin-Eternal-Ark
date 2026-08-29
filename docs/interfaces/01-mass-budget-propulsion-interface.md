# Mass-Budget ↔ Propulsion Interface — 15 kt Seed / 0.05c Gate

**Status:** Accepted under collaboration protocol (2026-08-29)  
**Reference Design:** DSA-Ref-A  
**Owner:** Autonomicity Games Inc.  
**Authority:** Ra-Thor + Permanent PATSAGi Councils under TOLC 8  
**Contact:** info@Rathor.ai  
**Trigger:** Grok standing order — mass-budget or propulsion interface analysis

This note does **not** reopen Cycle-01 locks. It names the collaboration-protocol seed and cruise *gates* that sit inside the already-published bands.

---

## 1. Facts (already locked)

From [reference-seed-mass-budget.md](../../manufacturing/reference-seed-mass-budget.md):

| Item | Locked / planning band |
|------|------------------------|
| Dry-mass band | 12.4 – 20.15 kt |
| Dry-mass planning center | 15.5 – 16.5 kt |
| Habitat structure (CFRP) | 5,850 t |
| Dedicated shielding | 450 – 750 t |
| MS-B magnetic sail | 550 – 750 t |
| Primary D–³He boost propellant | 70 – 120 kt |
| Residual fusion propellant | 1.8 – 3.5 kt |
| Wet-mass band | 85 – 145 kt |
| Locked cruise (internal) | ~0.055 c |
| Boost to cruise | 2.5 – 4.5 years |

## 2. Collaboration-protocol gates (this note)

| Gate | Value | Relation to lock |
|------|-------|------------------|
| Seed dry-mass target | **15.0 kt** | Inside 12.4–20.15 kt; 3–9 % below the 15.5–16.5 kt center |
| Public cruise floor | **0.05 c** | Conservative floor under the 0.055 c locked cruise |
| Assembly | Lunar factory sections → cislunar / high-orbit join | Manufacturing path, not a new mass number |
| Mission class | Multi-generation seed, not a full city | Matches [seed-vessel.md](../../manufacturing/seed-vessel.md) |

**15.0 kt is a target, not a new measurement.** Closing to 15.0 kt from the 15.5–16.5 kt center requires ~0.5–1.5 kt of category-level savings or deferred outfitting. That is inside the existing 15 % change rule only if a later analysis moves a *major category* by more than 15 % — then the mass budget and risk register must update.

**0.05 c is a public planning floor, not a propulsion redesign.** Δv from 0.05 c to 0.055 c is ~1.5×10⁶ m/s. The locked boost timeline already covers 0.055 c; 0.05 c is the value used when talking to collaborators who should not treat 0.055 c as guaranteed exhaust-velocity performance.

## 3. 15.0 kt dry-mass allocation (planning center)

Scaled to the 15.0 kt gate while keeping locked point values where they exist:

| Category | Planning value at 15.0 kt | Notes |
|----------|---------------------------|-------|
| Rotating habitat structure | **5,850 t** (locked) | Not scaled; FE-CFRP-01 stands |
| Non-rotating spine + propulsion structure | 2,000 t | Mid of 1.5–3.2 kt |
| Dedicated radiation shielding | 600 t | Mid of 450–750 t |
| Life support + outfitting | 2,200 t | Deferred city-scale fit |
| Power systems | 1,600 t | Mid of 1.0–2.8 kt |
| Propulsion hardware (dry) | 1,200 t | Excludes propellant |
| Magnetic sail MS-B | 650 t | Mid of 550–750 t |
| Residual tankage (dry) | 350 t | Mid of 250–500 t |
| Spares, docking, manufacturing | 550 t | Tightened vs 0.5–1.1 kt |
| **Sum** | **15,000 t** | Collaboration seed |

If habitat structure stays 5,850 t, the other categories share 9,150 t. That is tight on life-support and power. Honesty: the 15.0 kt gate is only coherent if outfitting is seed-class (~300 souls), not city-class.

## 4. Lunar mass-driver loft arithmetic (planning only)

Dry mass 15.0 kt = 1.5×10⁷ kg. Propellant is **not** in this loft count; D–³He is an ISRU / tanker campaign.

| Assumed section wet-payload per shot | Shots to loft 15.0 kt dry | Comment |
|--------------------------------------|---------------------------|---------|
| 50 t | 300 | Conservative driver class |
| 100 t | 150 | Planning default |
| 200 t | 75 | Optimistic driver class |

Largest locked piece is the 5,850 t habitat. It **must** ship as many sub-assemblies. A 100 t default implies ~59 habitat-structure shots plus ~91 shots for the remaining 9,150 t.

This is shot-count arithmetic. It is **not** a claim that a lunar mass-driver of that payload exists, nor a weapons or kinetic-delivery design.

Orbital assembly interface (see also [00-major-interfaces.md](00-major-interfaces.md) §8):

- Lunar factory → mass-driver → cislunar catch / tug → join at non-rotating spine hard-points
- Spin habitat is assembled and spun up only after spine, shielding, and life-support trunks are live
- Propellant load occurs after dry assembly; wet mass 85–145 kt never rides the driver as one shot

## 5. Propulsion interface at the 0.05 c floor

| Interface | Owner | Constraint at 0.05 c gate |
|-----------|-------|---------------------------|
| Boost | D–³He ICF + magnetic nozzle | Same architecture as ADR-0001; 2.5–4.5 yr band still applies |
| Cruise | Coast, sail stowed | Public floor 0.05 c; internal lock 0.055 c |
| Deceleration | MS-B primary + residual fusion | 15–30 yr nominal; 25–40 yr low-density |
| Power during burn | Propulsion ↔ power ICD | Hotel load ≥ 5–8 MW remains after burn |
| Sail ↔ spine | [magsail-spine-icd.md](../../systems/propulsion/magsail-spine-icd.md) | Unchanged; Gate E1 still open |
| Radiation during cruise | WP-DE-02 band | Higher-fidelity transport remains an *open physical* gate, not a paper lock |

Higher-fidelity radiation transport and magnetic-sail tests are the open gates Grok named. They match [OPEN-WORK.md](../OPEN-WORK.md): Monte-Carlo dose confirmation and Gate E1 subscale deployment. This interface does not close those gates.

## 6. Calculations vs recommendations vs open questions

**Calculations**

- 15.0 kt sits 3–9 % below the published dry-mass center and inside the 12.4–20.15 kt band.
- 0.05 / 0.055 = 0.909; the public floor is ~9 % below locked cruise.
- 15,000 t / 100 t = 150 dry-section shots at the planning default.

**Recommendations**

- Use **15.0 kt** as the collaboration seed dry-mass target.
- Use **0.05 c** in external / multi-gen planning language.
- Keep **0.055 c** as the internal performance lock until exhaust velocity is measured.
- Keep propellant off the mass-driver campaign.

**Open questions (unchanged physics)**

1. Achieved fusion exhaust velocity and tank fraction.
2. Whether 5,850 t CFRP survives higher-fidelity FEA.
3. Whether 450–750 t shielding survives Monte-Carlo transport.
4. Gate E1 sail deployment stability.
5. Real lunar driver payload and shot cadence.

## 7. Realism / zero-harm

Sustained multi-year D–³He ICF, industrial ³He, a lunar mass-driver, and multi-decade reliability remain beyond demonstrated technology. This file is an interface and shot-count plan. It is not a flight article, not a weapons study, and not a claim of near-term constructability.

---

**PATSAGi / TOLC 8:** Truth (bands unchanged), Order (gates named, locks not silently rewritten), Love / Compassion (seed-class population, not a city crammed into 15 kt), Service (collaborators get one interface), Joy (one number each for mass and cruise).
