# Magnetic Sail Integration for Deceleration

**Status:** Accepted baseline (WP-07 complete)  
**Owner:** Autonomicity Games Inc.  
**Related:** ADR-0001, propulsion performance model  
**Last Updated:** 2026-08-11

## 1. Purpose

Provide propellantless or low-propellant deceleration from interstellar cruise velocities (0.05–0.12 c) by interacting with the interstellar medium and, later, stellar winds.

Pure propulsive reverse thrust at high cruise speed is extremely expensive in mass ratio. A magnetic sail (magsail) is therefore the baseline primary deceleration method for early Eternal Ark vessels.

## 2. Operating Principle

A large superconducting loop (or array of loops) generates a magnetic field that deflects charged particles in the interstellar medium (and later the solar/stellar wind). The resulting momentum transfer produces drag opposite to the velocity vector, decelerating the ship.

## 3. Design Implications

- Sail “size” (effective magnetic moment / field volume) must be large for useful deceleration times from 0.1 c class speeds.
- Deployment and structural support of very large lightweight superconducting structures is a major engineering challenge.
- Power is required to maintain the superconducting currents and for attitude control, but no propellant is consumed for the primary drag force.
- Performance depends on local plasma density; interstellar medium density is low, so deceleration times are long (years to decades depending on sail scale and initial velocity).

## 4. Integration with Fusion Propulsion

Baseline strategy:
1. Main fusion boost to cruise velocity.
2. Long coast.
3. Deploy / activate magnetic sail for primary deceleration.
4. Use residual fusion propellant for final matching, orbit insertion, or emergency thrust.

This hybrid approach keeps total propellant mass within more realistic bounds than pure rocket deceleration.

## 5. Risks & Open Work

- Achieving and maintaining large-scale space-qualified superconducting loops
- Dynamic stability and attitude control of the sail-ship system
- Performance uncertainty due to variations in interstellar plasma density
- Combined structural loads during simultaneous residual thrust and magnetic drag
- Stowing, deployment, and possible reconfiguration for different mission phases

## 6. Next Analyses Required

- Parametric sizing: required magnetic moment vs. desired deceleration time from 0.05 / 0.08 / 0.10 / 0.12 c
- Structural and thermal design concepts for the sail
- Interaction with the forward particle shield
- Failure modes and recovery

---

**PATSAGi note:** Magnetic sail is selected as the highest-valence realistic deceleration method that preserves mass budget under known physics.
