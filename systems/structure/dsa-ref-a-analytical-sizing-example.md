# DSA-Ref-A — Example Material-Specific Analytical Sizing

**Status:** Illustrative first-pass calculation  
**Reference Design:** DSA-Ref-A (~140 m radius)  
**Owner:** Autonomicity Games Inc.  
**Last Updated:** 2026-08-11

## 1. Purpose

Provide a transparent, reproducible example of how material allowables translate into shell mass so that future FE work has a clear analytical baseline to confirm or revise.

## 2. Reference Geometry (Example)

| Parameter | Value |
|-----------|-------|
| Spin radius (to shell mid-plane) | 140 m |
| Habitat axial length | 100 m |
| Internal pressure | 101 kPa |
| Design gravity at deck | 0.95 g |
| Shape | Cylinder (conservative for first pass) |

## 3. Example Material Assumptions

Two bounding cases are shown:

**Case C — High-performance composite**  
- Design allowable (tension, with knockdowns): ~400–600 MPa effective  
- Density: ~1,600 kg/m³

**Case M — Aerospace metallic (Al-Li class)**  
- Design allowable (tension, with knockdowns): ~250–350 MPa effective  
- Density: ~2,700 kg/m³

(Exact allowables must be replaced with qualified, radiation- and vacuum-adjusted values.)

## 4. First-Order Pressure + Spin Sizing Logic

The shell must resist:
- Internal pressure hoop and longitudinal stress
- Centrifugal body load from the rotating mass itself and attached decks
- Buckling under combined loads

A simplified thin-wall pressure-vessel starting point is augmented by a stiffening mass fraction (typically 40–80% additional for large space habitats) and by deck/interface contributions already estimated separately.

## 5. Illustrative Outcome Ranges

Using the above geometry and the previously established structural framework:

- Composite-biased designs tend toward the lower half of the 4,700–12,200 t rotating-habitat structural range.
- Metallic-biased designs push toward the upper half or beyond unless the geometry is optimized aggressively.
- Hybrid solutions (composite shell + metallic spin interface and joints) are the current preferred planning approach.

These numbers remain illustrative until qualified allowables and FE confirmation are available.

## 6. Required Next Analytical / FE Steps

1. Lock a reference material system with fully adjusted allowables.
2. Perform global FE of the cylinder under pressure + spin + deck loads.
3. Extract required thicknesses and stiffener patterns.
4. Recompute mass and update the reconciled top-level budget if the result moves >15%.

---

**This example exists to make the structural mass path transparent and falsifiable by higher-fidelity analysis.**
