# DSA-Ref-A — Expanded FMEA Outline & Critical Failure Modes

**Status:** Expanded safety analysis  
**Reference Design:** DSA-Ref-A  
**Owner:** Autonomicity Games Inc.  
**Authority:** PATSAGi Councils under TOLC 8  
**Last Updated:** 2026-08-11

## 1. Purpose

Expand the high-level safety case into a structured Failure Modes and Effects Analysis (FMEA) framework that both humans and AI systems can populate and maintain.

## 2. FMEA Structure (to be applied to each major subsystem)

For every significant component or function record:

- Function
- Potential failure mode
- Possible causes
- Local effects
- System / crew effects
- Detection method
- Current controls / mitigations
- Severity (1–10)
- Occurrence (1–10)
- Detection difficulty (1–10)
- Risk Priority Number (RPN = S × O × D)
- Recommended actions
- Responsibility and status

## 3. Highest-Priority Failure Modes (Seed Vessel Focus)

### Propulsion & Power
- Inability to initiate or sustain fusion burn
- Magnetic nozzle degradation or failure mid-burn
- Cascading power loss affecting life support

### Rotating Habitat
- Primary bearing or seal failure
- Uncontrolled despin or imbalance
- Loss of transfer capability between rotating and non-rotating sections

### Life Support
- Progressive biological loop instability
- Contamination event that disables major growth zones
- Long-term trace contaminant build-up

### Shielding & Environment
- Inadequate storm shelter capacity during extreme SPE
- Forward shield compromise at cruise speed
- Higher-than-modeled GCR dose over multi-year exposure

### Governance & Human Factors
- Loss of primary control lattice with inadequate fallback
- Social / psychological cascade in small closed population
- Conflicting authority during emergency

## 4. Governing Safety Rules (Reinforced)

- No single failure shall lead to loss of the entire crew.
- Critical functions require independent redundant paths or demonstrated graceful degradation.
- All life-critical mode changes require logged decision + TOLC 8 valence check.
- Sectional isolation must be possible without total loss of life support.

## 5. Next Steps

- Populate full FMEA tables for propulsion, habitat spin system, and life support first
- Link each high-RPN item to a specific mitigation activity in the development roadmap
- Update the living risk register as RPNs are quantified

---

**This outline turns the safety case into a living, actionable engineering tool under PATSAGi oversight.**
