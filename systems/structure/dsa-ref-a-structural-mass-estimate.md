# DSA-Ref-A — First Analytical Structural Mass Estimate

**Status:** First-order analytical estimate  
**Reference Design:** DSA-Ref-A (spin radius ~140 m, ~300 people)  
**Owner:** Autonomicity Games Inc.  
**Last Updated:** 2026-08-11

## 1. Scope

This is a first-order analytical estimate for the primary rotating habitat structure. It is intended to begin replacing the previous wide range with a traceable number that can be refined by finite-element work.

## 2. Reference Geometry (Planning)

| Parameter | Value | Notes |
|-----------|-------|-------|
| Spin radius to main deck | 140 m | |
| Habitat form | Cylinder (or short torus approximation) | |
| Habitat length (axial) | 80–120 m | Sized for ~300 people + systems |
| Internal design pressure | ~101 kPa | Earth-normal |
| Design gravity | 0.9–1.0 g | |

## 3. Primary Load Drivers

- Internal pressure
- Centrifugal body loads from spin
- Deck live loads and equipment
- Safety factors for long-duration space structure
- Buckling and stiffening requirements

## 4. First-Order Mass Estimate Approach

1. Size the pressure shell (thin-wall or stiffened cylinder formulas) using high-specific-strength composite or metallic allowables.
2. Apply a stiffening mass fraction (typically 30–70% of shell mass for large space habitats, depending on design).
3. Add deck and internal structural mass.
4. Add spin-interface (bearings, seals, transfer structure) mass.
5. Apply contingency (30–40% at this stage).

## 5. Current Working Estimate (Rotating Habitat Structure Only)

| Element | Estimated Mass Range (t) | Notes |
|---------|--------------------------|-------|
| Primary pressure shell + stiffening | 2,500 – 6,500 | Highly material-dependent |
| Decks & internal structure | 800 – 2,000 | |
| Spin bearings, seals, transfer | 400 – 1,200 | Critical reliability item |
| Contingency & joints | 1,000 – 2,500 | |
| **Rotating habitat structure subtotal** | **~4,700 – 12,200 t** | |

This sits inside the broader “Structure + rotating habitat” allocation of the top-level mass budget and confirms that structural mass is a dominant dry-mass term.

## 6. Key Sensitivities

- Material specific strength and allowable stress
- Chosen safety factors and buckling knockdowns
- Exact habitat length and internal layout density
- Degree of integration between structure and shielding/water tanks

## 7. Immediate Next Actions

- Select a reference material system and re-run the analytical sizing with fixed allowables
- Produce a simple finite-element or advanced analytical model of the cylinder under spin + pressure
- Reconcile the result with the top-level mass budget and update it

---

**This is the first quantitative structural anchor for DSA-Ref-A. It will be tightened as material choices and FE analysis mature.**
