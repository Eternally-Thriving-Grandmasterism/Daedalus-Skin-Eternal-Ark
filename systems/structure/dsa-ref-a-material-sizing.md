# DSA-Ref-A — Material-Specific Structural Sizing & Early FE Direction

**Status:** Material selection & sizing guidance  
**Reference Design:** DSA-Ref-A (~140 m spin radius)  
**Owner:** Autonomicity Games Inc.  
**Last Updated:** 2026-08-11

## 1. Purpose

Move the first-order structural mass estimate toward material-specific sizing and define the direction for early finite-element (FE) confirmation.

## 2. Candidate Material Systems

| Material Family | Advantages | Concerns for Seed Vessel |
|-----------------|------------|---------------------------|
| Advanced carbon-fiber / polymer composites | Very high specific strength & stiffness | Long-term radiation + vacuum aging, joining, inspectability |
| High-strength aluminum-lithium or titanium alloys | Mature space heritage, better inspectability | Higher mass for same performance |
| Hybrid metal-composite construction | Balance of mass and inspectability | Interface complexity |

**Current planning preference:**  
Primary rotating habitat shell and stiffening biased toward high-specific-strength composites, with metallic solutions retained for the spin interface, bearings, and highly loaded joints where inspectability and replaceability are paramount.

## 3. Sizing Rules for First Material-Specific Pass

- Use conservative allowables that include radiation, vacuum, and long-duration knockdowns.
- Design for internal pressure + full centrifugal load at 1.0 g + reasonable safety factors.
- Explicitly size for buckling under combined loads.
- Treat the spin interface (bearings, seals, load transfer) as a separate, high-reliability metallic or hybrid subsystem.

## 4. Early Finite-Element Direction

First FE models should focus on:

1. Global rotating cylinder (or torus segment) under spin + pressure
2. Local stress concentrations at deck attachments and penetrations
3. Spin-interface load path into the non-rotating spine
4. Modal / dynamic behavior relevant to balancing and control

Goal of the first FE campaign: confirm or revise the 4,700–12,200 t analytical range with a narrower, material-specific estimate.

## 5. Integration Rule

Any FE or material-specific result that moves the rotating habitat structural mass by more than ~15% must update the reconciled top-level mass budget and the risk register.

---

**This document sets the material and FE path for closing the largest remaining structural uncertainty.**
