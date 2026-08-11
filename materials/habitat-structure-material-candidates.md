# Habitat Structure — Material Candidate Matrix (DSA-Ref-A)

**Status:** Working short-list for WP-DE-01  
**Owner:** Autonomicity Games Inc.  
**Linked Work Package:** WP-DE-01 Structural Analysis  
**Last Updated:** 2026-08-11

---

## 1. Purpose

Provide a traceable short-list of material systems that can be used for the first finite-element cycle of the 140 m class rotating habitat. The matrix records density, specific strength indicators, and known space-relevant limitations so that selection can be deliberated under PATSAGi.

## 2. Evaluation Criteria

- Specific strength (strength / density) and specific stiffness
- Fracture toughness and damage tolerance for multi-decade service
- Vacuum stability, outgassing, and radiation degradation resistance
- Thermal expansion and thermal cycling performance
- Manufacturability of large-diameter (≈280 m) sections or joinable modules
- Inspectability and repairability
- Cost and industrial readiness (relative)

## 3. Candidate Classes

### 3.1 Carbon-Fibre Reinforced Polymer (CFRP) — Highest Priority for First Cycle

| Attribute | Notes |
|-----------|-------|
| Density | ~1.5–1.8 g/cm³ |
| Strength / Stiffness | Excellent specific properties; can be tailored |
| Damage tolerance | Requires careful design (delamination risk); toughened resins preferred |
| Space heritage | Growing (satellites, some pressure vessels); long-duration habitat data limited |
| Manufacturing | Large sections possible via automated fibre placement or filament winding of modules |
| Key risks | Micrometeoroid damage progression, radiation-induced matrix degradation, joint design |

**Recommendation:** Primary candidate for pressure shell and primary stiffening. Requires explicit damage-tolerance and radiation-aging substantiation plan.

### 3.2 Aluminium-Lithium Alloys (e.g., 2195, 2099 family)

| Attribute | Notes |
|-----------|-------|
| Density | ~2.6–2.7 g/cm³ |
| Strength | High specific strength relative to conventional aluminium |
| Fracture toughness | Generally good |
| Space heritage | Strong (cryogenic tanks, aerospace structures) |
| Manufacturing | Conventional aerospace fabrication and welding / friction-stir methods |
| Key risks | Still higher mass than optimised composites; lithium handling and corrosion considerations |

**Recommendation:** Strong metallic baseline / hybrid option. Useful as reference and for hybrid metal-composite concepts.

### 3.3 Titanium Alloys (Ti-6Al-4V and selected beta alloys)

| Attribute | Notes |
|-----------|-------|
| Density | ~4.4–4.5 g/cm³ |
| Strength / Toughness | Excellent strength and corrosion resistance; high specific strength in some alloys |
| Space heritage | Extensive |
| Manufacturing | More difficult and expensive than aluminium; welding and forming challenges at large scale |
| Key risks | Cost, density penalty relative to Al-Li or CFRP, manufacturing of very large sections |

**Recommendation:** Reserved for high-load interfaces, spin-bearing regions, and critical penetrations rather than the bulk pressure shell.

### 3.4 Hybrid Metal-Lined Composite Pressure Vessel

| Attribute | Notes |
|-----------|-------|
| Concept | Thin metallic liner (leak-tight) + composite overwrap |
| Advantages | Combines leak-tightness of metal with mass efficiency of composite |
| Risks | Thermal expansion mismatch, liner buckling, interface integrity over decades |

**Recommendation:** High-value concept for detailed trade after pure-CFRP and Al-Li baselines are established.

## 4. First-Cycle Decision Rule

For the initial global FE model:
1. Run a pure high-modulus CFRP configuration as the primary mass-minimising case.
2. Run an Al-Li configuration as the metallic reference case.
3. Compare mass, margins, and critical failure modes.
4. Present both results to PATSAGi for selection of the baseline material system (or hybrid path).

## 5. Open Items for Material Substantiation

- Published or proprietary long-duration radiation aging data for candidate resins/fibres
- Large-scale join methods and their allowables
- Damage-tolerance substantiation approach for a multi-decade rotating habitat
- Integration of Daedalus-Skin outer layers with the primary structural material

---

**This matrix is the material input required to begin WP-DE-01 finite-element work.**
