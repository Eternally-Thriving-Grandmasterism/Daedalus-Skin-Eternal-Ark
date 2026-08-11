# DSA-Ref-A FMEA — Propulsion & Power (First Population)

**Status:** First populated tables  
**Reference Design:** DSA-Ref-A  
**Owner:** Autonomicity Games Inc.  
**Authority:** PATSAGi Councils under TOLC 8  
**Last Updated:** 2026-08-11

Severity / Occurrence / Detection scale: 1 (lowest) – 10 (highest). RPN = S × O × D.

## Critical Propulsion & Power Failure Modes

| ID | Function | Failure Mode | Cause | Effect on Crew / Mission | S | O | D | RPN | Current Controls | Recommended Actions |
|----|----------|--------------|-------|---------------------------|---|---|---|-----|------------------|---------------------|
| P-01 | Fusion burn sustainment | Inability to maintain required gain / pulse rate | Driver degradation, pellet quality, nozzle erosion | Loss of primary thrust; mission timeline impact | 9 | 4 | 5 | 180 | Multiple drivers, monitoring, ground test program | Accelerated endurance testing of driver + nozzle |
| P-02 | Magnetic nozzle | Thermal or structural failure mid-burn | Heat load, material fatigue | Thrust vector loss or reduced performance | 9 | 3 | 4 | 108 | Thermal design margin, sensors | High-fidelity thermal cycling tests |
| P-03 | Power reactors | Cascading loss of multiple reactors | Common-cause failure, thermal runaway | Threat to life support & control power | 10 | 2 | 4 | 80 | Independent clusters, isolation | Formal common-cause analysis + isolation testing |
| P-04 | Propellant feed | Major tank or feed line rupture | Impact, fatigue, valve failure | Loss of propellant, possible contamination | 8 | 2 | 5 | 80 | Redundant isolation, shielding | Impact and fatigue testing of critical lines |
| P-05 | Attitude during burn | Uncontrolled torque from nozzle or imbalance | Control system fault, structural shift | High structural loads, possible spin coupling | 9 | 2 | 4 | 72 | Independent attitude control, abort thrust | Coupled dynamics simulation + abort procedures |

## Immediate Safety Actions

- All RPN > 100 items require active mitigation plans in the technology maturation program.
- P-01 and P-02 are currently the highest propulsion risks and drive ground test priorities.
- Power isolation and common-cause failure analysis are mandatory before final design freeze.

## Next FMEA Populations

1. Rotating habitat bearings, seals, and transfer systems
2. Life support biological and physicochemical loops
3. Magnetic sail deployment and operation

---

**This is the first living FMEA population. It will be expanded and re-scored as test data arrives.**
