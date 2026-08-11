# DSA-Ref-A FMEA — Life Support Systems

**Status:** First population  
**Reference Design:** DSA-Ref-A (~300 people)  
**Owner:** Autonomicity Games Inc.  
**Authority:** PATSAGi Councils under TOLC 8  
**Last Updated:** 2026-08-11

Severity / Occurrence / Detection: 1–10. RPN = S × O × D.

## Critical Life Support Failure Modes

| ID | Function | Failure Mode | Cause | Effect on Crew / Mission | S | O | D | RPN | Current Controls | Recommended Actions |
|----|----------|--------------|-------|---------------------------|---|---|---|-----|------------------|---------------------|
| LS-01 | Oxygen generation / CO₂ removal | Progressive failure of primary biological loop | Contamination, nutrient imbalance, lighting failure, pathogen | Rising CO₂ or falling O₂; eventual toxic atmosphere | 10 | 3 | 4 | 120 | Dual biological + physicochemical paths, continuous monitoring | Long-duration closed-loop testbeds with failure injection |
| LS-02 | Water recovery | Major loss of water processing capacity | Equipment failure, fouling, contamination | Water shortage; hygiene and food production impact | 9 | 3 | 4 | 108 | Multiple processing trains, large buffer inventory | Redundant trains + multi-month buffer demonstration |
| LS-03 | Food production | Sustained collapse of calorie/nutrition output | Crop failure, lighting loss, nutrient cascade | Progressive malnutrition over weeks–months | 9 | 3 | 5 | 135 | Multiple independent growth zones, stored contingency food | Diversified crop set + contingency food mass requirements |
| LS-04 | Trace contaminant control | Build-up of toxic or irritating compounds | Inadequate filtration, off-gassing, biological by-products | Chronic health effects, performance degradation | 8 | 4 | 5 | 160 | Continuous atmosphere monitoring, multi-stage filtration | Expanded sensor suite + long-duration contaminant studies |
| LS-05 | Section isolation | Inability to isolate a contaminated or failed zone | Valve/actuator failure, design dependency | Cascade of failure across habitat | 9 | 2 | 4 | 72 | Designed sectional isolation, independent buffers | Isolation system testing under realistic failure scenarios |

## Priority Observations

- LS-04 (trace contaminants) currently shows the highest RPN and is often underestimated in early designs.
- LS-03 (food production) and LS-01 (atmosphere) are existential over multi-month timescales and drive the need for true dual-path architecture.
- All high-RPN items must be explicitly covered in the technology maturation plan with multi-month to multi-year test objectives.

## FMEA Coverage Status

- Propulsion & Power → Complete
- Rotating Habitat & Spin → Complete
- Life Support → Complete (this document)

Next recommended: Magnetic sail deployment & operation FMEA, then integrated risk picture update.

---

**Life Support FMEA is now live under TOLC 8 governance.**
