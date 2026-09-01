# Daedalus-Skin — Material Requirements & Self-Healing Targets

**Status:** Accepted baseline (WP-08 complete)  
**Owner:** Autonomicity Games Inc.  
**Lineage:** AlphaProMega Air Foundation self-healing concepts  
**Last Updated:** 2026-09-01

## 1. Purpose

Provide a multi-layer outer skin that:
- Resists micrometeoroid and interstellar dust impacts
- Self-repairs minor and moderate damage autonomously
- Contributes to radiation and thermal protection
- Maintains integrity over multi-decade to multi-century service life with minimal crew intervention

## 2. Required Capabilities

| Capability | Target |
|------------|--------|
| Autonomous repair of punctures / cracks | Seal against vacuum loss for holes up to a defined diameter without human EVA |
| Trigger mechanisms | Mechanical damage, pressure differential, radiation, or controlled chemical trigger |
| Vacuum stability | No significant outgassing or degradation in deep space |
| Radiation tolerance | Maintain healing function after long-term GCR and solar particle exposure |
| Thermal cycling | Survive repeated temperature extremes |
| Mass efficiency | Healing function must not impose excessive areal density penalty |
| Inspectability | Damage and healing state detectable by sensors / AI inspection systems |

## 3. Material Approaches (Baseline Candidates)

- Microcapsule-based polymer systems (healing agent released on crack)
- Vitrimer / reversible covalent network polymers (can be reprocessed or healed with heat/stimulus)
- Hybrid systems incorporating limited biological or bio-inspired agents where vacuum and radiation allow
- Multi-layer construction: outer sacrificial/healing layer + structural layer + inner pressure boundary

### 3.1 Watch-class outer ply (not the healing system)

ISEC polycrystalline CVD graphene / graphene super-laminate is **watch class only**. Korean 1 km / ~2 m/min roll-to-roll is electronics-grade film. Conditional 90–99 GPa is not a skin allowable.

Allowed later use, if coupons exist: ultra-thin sacrificial, conductive, or thermal **outer** ply on top of the polymer / vitrimer healing stack. Forbidden: replacing the self-healing layer; treating CharmGraphene film as flight skin; inserting 90–99 GPa into WP-DE-01 allowables.

Packet: `pcg-gsl-tether-watch-2026-09-01.md`.

Any graphene ply stack must treat interlayer shear as first-class. Van der Waals alone is not assumed sufficient under concentrated rolling or impact loads.

## 4. Integration Rules

- Daedalus-Skin is an outer system; primary pressure vessel integrity remains independent.
- Healing is a first response; major damage still requires assessment and possible human/robotic intervention.
- Sensors and PATSAGi monitoring continuously assess skin health.
- Design must allow sectional replacement or augmentation during long missions.
- Watch-class 2D-carbon plies, if ever added, sit outside the pressure boundary and do not carry habitat hoop load.

## 5. Open Development Work

- Specific polymer / vitrimer formulations and vacuum/radiation test data
- Maximum autonomously healable defect size
- Healing time constants under space conditions
- Long-term aging and repeated-damage performance
- Sensor suite for health monitoring
- Manufacturing process for large curved sections
- Independent metre-class PCG / GSL coupon + AO + interlayer-shear data before any outer-ply FE insertion

---

**PATSAGi / TOLC 8 note:** Self-healing reduces long-term risk to life and mission. It is a high-valence investment even if it adds some initial mass and complexity. A strong 2D sheet that does not heal, or that delaminates, is not a substitute for that investment.
