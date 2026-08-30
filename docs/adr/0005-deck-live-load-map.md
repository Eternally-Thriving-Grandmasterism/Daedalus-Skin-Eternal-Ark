# ADR-0005 — Deck-by-Deck Occupied Live-Load Map

**Status:** Accepted (planning freeze)  
**Date:** 2026-08-30  
**Owner:** Autonomicity Games Inc.  
**Authority:** Ra-Thor + Permanent PATSAGi Councils under TOLC 8  
**Contact:** info@Rathor.ai

## Context

ADR-0004 froze a uniform 2.4 kPa so LC-04 had a number. Applied to the full 140 m × 100 m cylinder skin (~88,000 m²) that load is ~21,000 t-equivalent and is not a seed-class case. Live load is an *occupied-floor* pressure, not a skin pressure.

## Decision

Use occupied areas from [dsa-ref-a-volume-allocation.md](../../systems/habitat/dsa-ref-a-volume-allocation.md) and the A–E layout in [dsa-ref-a-deck-layout.md](../../systems/habitat/dsa-ref-a-deck-layout.md). Midpoints of the published bands:

| Deck | Role | Occupied floor | Live load | Occupied live-load force |
|------|------|----------------|-----------|--------------------------|
| A | Residential | 3,900 m² | 2.0 kPa | 7.80 MN ≈ 795 t-eq at 1 g |
| B | Community / culture | 1,150 m² | 3.0 kPa | 3.45 MN ≈ 352 t-eq |
| C | Food production | 2,750 m² | 3.0 kPa | 8.25 MN ≈ 841 t-eq |
| D | Technical LS / utilities | 400 m² | 3.0 kPa | 1.20 MN ≈ 122 t-eq |
| E | Medical / exercise | 250 m² | 3.0 kPa | 0.75 MN ≈ 76 t-eq |
| **Sum** | | **8,450 m²** | | **21.45 MN ≈ 2,186 t-eq** |

Equipment 1,800 t and water 400 t stay as concentrated masses (ADR-0004):

- Water 400 t: annulus outboard of Deck A (sleep)
- Equipment 1,800 t: D 800 t, C 500 t, B 200 t, E 150 t, A 150 t

Unoccupied cylinder skin carries structure + pressure + spin only. No 2.4 kPa there.

## Consequences

- First-cycle uniform 2.4 kPa remains a *fallback* if a partner model cannot take a deck map.
- Preferred LC-04 is this map.
- Areas are planning midpoints, not surveyed decks.
- Does not confirm 5,850 t.

## Alternatives rejected

- Uniform 2.4 kPa on ~88,000 m² (mass-fiction).
- Zero live load (unconservative for occupied decks).
