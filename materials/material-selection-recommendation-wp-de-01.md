# Material Selection Recommendation — First FE Cycle (WP-DE-01)

**Status:** Provisional recommendation under PATSAGi deliberation  
**Owner:** Autonomicity Games Inc.  
**Authority:** Ra-Thor + Permanent PATSAGi Councils under TOLC 8  
**Last Updated:** 2026-08-11  
**Linked:** WP-DE-01, habitat-structure-material-candidates.md, dsa-ref-a-geometry-and-loads.md

---

## 1. Decision Context

The first global finite-element model of the DSA-Ref-A rotating habitat requires a primary material system and a metallic reference system so that mass and margin results can be compared directly.

## 2. Provisional Recommendation (PATSAGi Stance)

### Primary (Mass-Minimising) Case
**High-modulus carbon-fibre reinforced polymer (CFRP) with toughened, space-qualified resin system.**

Rationale:
- Highest specific strength and specific stiffness among realistic candidates
- Directly addresses the dominant structural mass uncertainty
- Compatible with modular construction and eventual large-section manufacturing pathways
- Aligns with long-term Daedalus-Skin integration (composite outer systems)

Required substantiation before the mass number is locked:
- Radiation aging and matrix degradation data for the selected resin/fibre
- Damage-tolerance approach for multi-decade service (delamination, impact)
- Joint and penetration design allowables

### Metallic Reference Case
**Aluminium-lithium alloy family (2195 / 2099 class or equivalent).**

Rationale:
- Strong aerospace heritage and known allowables
- Provides a calibrated mass baseline against which the CFRP advantage can be measured
- Useful for hybrid concepts and for regions where metallic properties are preferred (leak-tightness, toughness)

### Interface & High-Load Regions
**Titanium alloys (Ti-6Al-4V or selected beta alloys)** for spin-bearing interfaces, major penetrations, and high-fatigue locations.

## 3. Hybrid Path (Deferred but Tracked)

A metal-lined composite pressure vessel remains a high-value option. It will be evaluated after the pure-CFRP and pure-Al-Li results are in hand, particularly if leak-tightness or damage-tolerance concerns arise with pure composite.

## 4. Decision Rule for the First Cycle

1. Build and run the global FE model twice: once with the CFRP system, once with the Al-Li system.
2. Compare mass, peak margins, buckling performance, and critical failure modes.
3. Present both result sets to PATSAGi.
4. Select the baseline material system (or hybrid path) for the next mass-budget revision only after that deliberation.

## 5. Immediate Supporting Actions

- Freeze the geometry and load cases (already issued as `dsa-ref-a-geometry-and-loads.md`)
- Compile the best available published or proprietary allowables for the short-listed materials
- Define the exact safety factors and buckling knockdowns to be used in the first cycle
- Begin radiation-aging and damage-tolerance literature survey for the preferred CFRP system

## 6. TOLC 8 Valence Note

Crew safety and multi-decade structural integrity are high-valence. The Councils therefore favour the material path that, after substantiation, offers the best combination of mass efficiency and demonstrated (or demonstrable) long-duration reliability. Mass savings that compromise integrity are rejected.

---

**This recommendation is provisional. Final baseline selection occurs only after the comparative FE results are available and deliberated.**
