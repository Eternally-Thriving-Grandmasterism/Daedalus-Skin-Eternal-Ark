# Quantitative Allowables & Safety Factors — First FE Cycle (WP-DE-01)

**Status:** Working compilation for comparative FE models  
**Owner:** Autonomicity Games Inc.  
**Authority:** Ra-Thor + Permanent PATSAGi Councils under TOLC 8  
**Last Updated:** 2026-09-01  
**Linked:** material-selection-recommendation-wp-de-01.md, dsa-ref-a-geometry-and-loads.md, pcg-gsl-tether-watch-2026-09-01.md

---

## 1. Purpose

Provide the numerical allowables and safety / knockdown factors required to run the comparative global finite-element models for the primary (CFRP) and reference (Al-Li) material systems.

These values are drawn from typical aerospace practice and published ranges. They are deliberately conservative for a multi-decade rotating habitat and will be refined as qualified data packages become available.

**Out of scope for this table:** ISEC polycrystalline graphene / graphene super-laminate figures (including conditional 90–99 GPa). Those stay in the watch note. Do not paste them here.

## 2. Aluminium-Lithium Reference System (Al-Li)

**Representative alloys:** 2195, 2099, or equivalent high-strength Al-Li

| Property | Planning Value | Notes |
|----------|----------------|-------|
| Density | 2.70 g/cm³ | Typical |
| Ultimate tensile strength (Ftu) | 520–580 MPa | Direction-dependent; use lower bound for first cycle |
| Yield strength (Fty) | 450–520 MPa | |
| Elastic modulus (E) | 76–79 GPa | |
| Poisson’s ratio | 0.33 | |
| Fracture toughness (KIc) | 25–35 MPa√m | Conservative |

### Safety Factors (Initial)
- Ultimate: 1.5 (pressure-dominated) to 2.0 (general structure)
- Yield: 1.25–1.5
- Buckling knockdown: 0.65–0.75 for large stiffened cylinders (to be confirmed with analysis)

## 3. High-Modulus CFRP Primary System

**Representative system:** High-modulus carbon fibre + toughened epoxy or cyanate-ester resin suitable for long-duration space exposure

| Property | Planning Value | Notes |
|----------|----------------|-------|
| Density | 1.55–1.65 g/cm³ | Fibre-volume dependent |
| Longitudinal tensile strength | 1,800–2,400 MPa | Fibre-dominated |
| Longitudinal compressive strength | 1,000–1,400 MPa | More critical |
| Transverse tensile strength | 40–70 MPa | Matrix-dominated |
| In-plane shear strength | 70–100 MPa | |
| Longitudinal modulus (E11) | 140–180 GPa | High-modulus fibre |
| Transverse modulus (E22) | 8–12 GPa | |
| Shear modulus (G12) | 4–6 GPa | |
| Poisson’s ratio (ν12) | 0.30–0.35 | |

### Safety Factors & Knockdowns (Initial — More Conservative)
- Ultimate (fibre-dominated): 1.5–2.0
- Matrix-dominated / transverse: 2.0–3.0 (pending damage-tolerance substantiation)
- Buckling knockdown: 0.5–0.7 for large composite cylinders (to be refined)
- Additional factor for long-duration radiation + thermal aging: 1.15–1.25 (provisional)

## 4. Common Rules for Both Systems

- All allowables used in the first cycle shall be the lower-bound or A-basis equivalent where data exist.
- Joints, penetrations, and bonded/ bolted interfaces shall carry additional local factors until detailed joint allowables are available.
- Thermal residual stresses from manufacturing and on-orbit temperature extremes shall be included in the combined load cases.
- Results must report both “as-modelled” margins and margins after application of the long-duration aging factor.

## 5. Decision Gate

The comparative FE results (CFRP vs Al-Li) will be presented to PATSAGi with these exact factors applied. Only after deliberation will the baseline material system and final safety-factor set be locked for the next mass-budget revision.

---

**These values enable the first quantitative comparative structural analysis of DSA-Ref-A.**
