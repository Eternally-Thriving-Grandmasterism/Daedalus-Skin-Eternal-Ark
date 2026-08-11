# DSA-Ref-A FMEA — Rotating Habitat & Spin System

**Status:** First population  
**Reference Design:** DSA-Ref-A  
**Owner:** Autonomicity Games Inc.  
**Authority:** PATSAGi Councils under TOLC 8  
**Last Updated:** 2026-08-11

Severity / Occurrence / Detection: 1–10. RPN = S × O × D.

## Critical Habitat Spin & Transfer Failure Modes

| ID | Function | Failure Mode | Cause | Effect on Crew / Mission | S | O | D | RPN | Current Controls | Recommended Actions |
|----|----------|--------------|-------|---------------------------|---|---|---|-----|------------------|---------------------|
| H-01 | Continuous rotation | Primary bearing seizure or catastrophic wear | Lubrication failure, fatigue, contamination | Loss of artificial gravity; major structural loads during despin | 9 | 3 | 4 | 108 | Redundant bearings where practical, monitoring, ground test articles | Accelerated vacuum bearing endurance tests |
| H-02 | Atmosphere containment | Major rotating seal failure | Seal degradation, misalignment, impact | Depressurization risk between rotating and non-rotating volumes | 10 | 2 | 4 | 80 | Multiple seal stages, rapid isolation capability | Multi-stage seal testing under thermal/vacuum cycling |
| H-03 | Utility transfer | Loss of power/data/fluid transfer across interface | Slip-ring or rotary joint failure | Loss of critical services to habitat | 9 | 3 | 5 | 135 | Redundant transfer paths, offline buffers | Dual independent transfer systems + buffer capacity |
| H-04 | Dynamic balance | Progressive imbalance | Mass shift, damage, crew movement patterns | Vibration, bearing overload, possible structural fatigue | 8 | 3 | 5 | 120 | Active balancing, continuous monitoring | Real-time balance sensing + correction procedures |
| H-05 | Emergency despin / transfer | Inability to safely stop rotation or move crew | Mechanism jam, power loss | Crew trapped in rotating section during emergency | 10 | 2 | 4 | 80 | Independent despin capability, multiple transfer routes | Dedicated emergency despin and transfer drills |

## Priority Actions

- H-03 (utility transfer) currently carries the highest RPN and requires explicit dual-path design.
- H-01 and H-04 drive the need for long-duration vacuum spin testing.
- All high-RPN items must appear in the technology maturation plan with clear test milestones.

## Next FMEA Population

Life support biological and physicochemical loops.

---

**Habitat spin system FMEA is now live and linked to the risk register and maturation plan.**
