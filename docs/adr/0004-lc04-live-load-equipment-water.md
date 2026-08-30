# ADR-0004 — LC-04 Live Load, Equipment Mass, Dual-Use Water

**Status:** Accepted (planning freeze)  
**Date:** 2026-08-30  
**Owner:** Autonomicity Games Inc.  
**Authority:** Ra-Thor + Permanent PATSAGi Councils under TOLC 8  
**Contact:** info@Rathor.ai

## Context

HF-01 Pass A input deck could not run LC-04 while deck live load, equipment mass, and water-tank mass were TBD. Unified command is Pass A first. These values must be frozen as *planning loads*, not as measurements.

## Decision

| Load | Planning freeze | Provenance |
|------|-----------------|------------|
| Occupied-deck live load | **2.4 kPa** | Terrestrial-habitat analog (office-class). Not a flight measurement. |
| Technical / grow-deck live load | **3.0 kPa** | Higher for plant facilities and workshops. |
| First-cycle uniform live load | **2.4 kPa** on all rotating decks | Use until a deck-by-deck map exists. |
| Equipment + outfitting on decks | **1,800 t** | Seed LS+outfitting 2,200 t from the 15.0 kt allocation minus 400 t water. |
| Dual-use water inventory | **400 t** | 300-person throughput 1.2–1.8 t/day; 400 t is ~7–11 months of throughput and a shieldable annulus. |
| Dedicated shielding (not water) | **600 t** | Mid of locked 450–750 t band. Pass B owns the dose check. |
| Water placement | Segmented annulus outboard of sleep decks | Same geometry for Pass A mass and Pass B transport. |

## Consequences

- LC-04 is now numerically specified on the input deck.
- Pass B must use the same 400 t water geometry.
- If a later human-factors or shielding study moves water or equipment by more than ~15 %, update this ADR and the deck together.
- None of these numbers confirm 5,850 t. That still requires an FEA run.

## Alternatives rejected

- Metabolic-only water (~36–54 t for 30 days): too small for dual-use shielding.
- City-scale 10k-person LS masses: wrong class for the seed.
- Leaving TBDs in place: blocks the unified next vector.
