# DSA-Ref-A Life Support — Area & Power Tables (~300 persons)

**Status:** Detailed planning baseline  
**Reference Population:** 300  
**Owner:** Autonomicity Games Inc.  
**Last Updated:** 2026-08-11

## 1. Metabolic Loads (300 people)

| Flow | Per Person | For 300 people |
|------|------------|----------------|
| O₂ consumption | 0.84 kg/day | 252 kg/day |
| CO₂ production | 1.00 kg/day | 300 kg/day |
| Drinking + food prep water | ~2.5–3.5 kg/day | ~750–1,050 kg/day |
| Total water throughput (incl. hygiene) | ~4–6 kg/day | ~1,200–1,800 kg/day |

## 2. Food Production Strategy

Mixed system:
- High-productivity microalgae / cyanobacteria for O₂ and partial calories
- Higher plants for nutrition, variety, and psychological benefit

### Planning Area Estimates (approximate)

| Crop / System | Area Guidance | Notes |
|---------------|---------------|-------|
| Microalgae photobioreactors | 150–400 m² | High volumetric productivity; exact volume depends on density |
| Leafy greens & vegetables | 400–800 m² | Fast cycle, high value for morale |
| Calorie crops (potato, wheat, soy, etc.) | 1,200–2,500 m² | Dominant area driver |
| **Total cultivated area (planning)** | **~2,000 – 3,500 m²** | Includes access and infrastructure |

These figures assume efficient LED lighting and optimized cultivars. Real closed-loop performance will refine them.

## 3. Power Estimate (Life Support Dominant)

Lighting is the largest continuous electrical load.

- Target lighting efficiency: 2.5–3.0 µmol/J (advanced LEDs)
- Typical plant lighting power density: 150–300 W/m² depending on crop and photoperiod

**Order-of-magnitude continuous power for 300 people:**

| Load | Power Range |
|------|-------------|
| Crop & algae lighting | 0.8 – 2.5 MW |
| Pumps, fans, thermal, processing | 0.3 – 0.8 MW |
| **Total life support continuous** | **~1.2 – 3.5 MW** |

Significant margin above the upper end is recommended for the reference design.

## 4. Water & Buffer Mass

- Working water inventory sized for several days to weeks of throughput
- Dual-use as radiation shielding wherever possible
- Contingency stores for multi-month recovery from major disruption

## 5. Design Rules for DSA-Ref-A

- Multiple independent growth zones (no single point of failure)
- Physicochemical backup path for atmosphere and water
- Continuous monitoring + PATSAGi-assisted anomaly response
- Ability to isolate sections without total loss of life support

---

**These tables are now the working life-support baseline for the 300-person Reference Seed Vessel.**
