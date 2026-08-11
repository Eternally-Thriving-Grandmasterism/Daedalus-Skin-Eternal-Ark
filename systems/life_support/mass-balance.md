# Closed-Loop Life Support — Mass & Power Budget

**Status:** Accepted baseline framework (WP-02 complete)  
**Owner:** Autonomicity Games Inc.  
**Reference Population:** 10,000 – 25,000 (scalable)  
**Last Updated:** 2026-08-11

## 1. Design Goals

- Near-closed loop for multi-decade to multi-century operation.
- High recovery of water and nutrients.
- Adequate food variety and nutrition for long-term health and morale.
- Dual biological + physicochemical pathways for robustness.

## 2. Metabolic Baselines (per person per day)

| Flow | Approximate Value | Notes |
|------|-------------------|-------|
| O₂ consumption | 0.84 kg | |
| CO₂ production | 1.00 kg | |
| Water (total throughput) | 3–5+ kg | Drinking + hygiene + food prep |
| Food (dry mass equivalent) | ~0.6–0.8 kg | Highly dependent on diet |
| Metabolic waste | Corresponds to intake | Must be fully processed |

## 3. Reference Population Scaling (10,000 people)

### Atmosphere
- Daily CO₂ load ≈ 10,000 kg
- Daily O₂ demand ≈ 8,400 kg
- Primary solution: High-density algal photobioreactors + higher plants
- Backup: Physicochemical CO₂ removal + O₂ generation (Sabatier / electrolysis etc.)

### Water
- Target recovery > 98–99%
- Daily system throughput is large; storage and processing capacity must be sized with margin for peak loads and failure recovery.

### Food Production
- Mix of:
  - Fast-cycle microalgae / cyanobacteria (high productivity, O₂ generation)
  - Leafy greens and vegetables (variety, vitamins)
  - Higher-calorie crops (potatoes, wheat, soy, etc.)
- Exact cultivated area depends on lighting efficiency, crop selection, and desired diet diversity. Conservative planning uses significant volume and power allocation.

## 4. Power Implications (Order-of-Magnitude)

Life support is one of the largest continuous power consumers after propulsion/power systems themselves:

- Lighting for plants and photobioreactors is dominant.
- Pumps, fans, thermal control, and processing equipment add further load.
- Design must assume multi-megawatt continuous allocation for a 10k–25k population, scaling roughly linearly with population (with some economies of scale).

Precise numbers will be refined as crop models and lighting technology assumptions are locked.

## 5. Mass Implications

Major mass contributors:
- Photobioreactor volume and structure
- Plant growth facilities and soil/hydroponic systems
- Water storage and processing equipment
- Nutrient recovery and waste processing systems
- Buffer stocks for contingency

Life support wet mass is significant but benefits from dual-use (water tanks also serve as radiation shielding).

## 6. Robustness Rules

- No single biological or physicochemical pathway may be a single point of failure.
- Minimum contingency stores sized for multi-month recovery from major disruption.
- Quarantine and contamination control are mandatory.
- Continuous monitoring and PATSAGi-assisted anomaly response.

## 7. Open Refinements

- Detailed crop-by-crop area and power tables
- Exact photobioreactor volumetric productivity assumptions
- Lighting efficiency (µmol/J) targets
- Full mass breakdown for 10k and 25k reference cases
- Integration with habitat volume and radiation shielding

---

**PATSAGi note:** Life support is a zero-harm critical system. All designs must maintain multiple independent paths to keep the crew alive and healthy under TOLC 8.
