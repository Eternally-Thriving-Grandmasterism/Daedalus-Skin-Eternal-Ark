# Radiation Scoping — WP-DE-02 Parallel Track

**Status:** Scoping complete — ready for quantitative transport runs  
**Owner:** Autonomicity Games Inc.  
**Authority:** Ra-Thor + Permanent PATSAGi Councils under TOLC 8  
**Last Updated:** 2026-08-11  
**Linked:** WP-DE-02, dsa-ref-a-dose-trade.md

---

## 1. Purpose

Define the precise inputs required to begin quantitative radiation transport calculations so that shielding mass can be tightened in parallel with the structural FE work.

## 2. Mission Dose Targets (Provisional — for first runs)

| Metric | Provisional Target | Notes |
|--------|--------------------|-------|
| Annual effective dose (GCR-dominated) | ≤ 150–200 mSv/year | Conservative long-duration planning band |
| Career effective dose (10–25 year mission) | ≤ 1.0–1.5 Sv | To be confirmed under TOLC 8 crew-safety valence |
| Storm shelter residual dose (design-basis SPE) | ≤ 50–100 mSv event | Short-term limit |

These targets are deliberately conservative. Final values will be locked by PATSAGi after the first transport results are available.

## 3. Geometry Configurations to Analyse

1. **Baseline dual-use water** — Life-support water inventory placed as an annular or segmented shield around primary living volumes.
2. **Optimised water placement** — Water concentrated over sleep quarters and high-occupancy zones; thinner coverage elsewhere.
3. **Storm shelter high-areal-density core** — Local 40–60 g/cm² hydrogen-rich region.
4. **Sensitivity cases** — ±20 % water mass; pure polyethylene equivalent; minimal dedicated shielding.

## 4. Radiation Environments

- GCR solar-minimum spectrum (worst-case continuous)
- GCR solar-maximum spectrum
- Design-basis SPE (historical extreme event scaled)
- Secondary neutron and charged-particle production in the shield materials

## 5. Analysis Outputs Required

- Annual and career effective dose for each geometry
- Organ-specific doses (where code capability exists)
- Required additional dedicated shielding mass to meet targets after dual-use water is applied
- Mass vs dose curves for the active-shielding trade (if active systems are still under consideration)

## 6. Parallel Execution Note

Radiation geometry (especially water-tank placement) shall be coordinated with the structural FE models so that the same water mass and location are used in both the dose calculations and the structural load paths.

---

**This scoping enables immediate quantitative transport work under WP-DE-02 while structural models are built.**
