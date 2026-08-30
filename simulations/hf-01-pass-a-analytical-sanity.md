# HF-01 Pass A — Analytical Sanity (Not FEA)

**Status:** Surmise with arithmetic. Does **not** close Pass A. Does **not** move 5,850 t.  
**Date:** 2026-08-30  
**Owner:** Autonomicity Games Inc.  
**Authority:** Ra-Thor + Permanent PATSAGi Councils under TOLC 8  
**Contact:** info@Rathor.ai  
**Proof Ladder:** Design / systems-engineering. Surmise labeled as measurement is forbidden.

## 1. Why this note exists

A partner FEA has not been run. PATSAGi still owes one quantitative question: is 5,850 t even in the same decade as a 140 m-radius, 100 m-long pressurized cylinder at 101.3 kPa?

## 2. Allowable used (CFRP lower bound, ADR deck)

From the frozen TOML: Ftu long = 1,800 MPa, ultimate factor 2.0, aging 1.25.

$$\sigma_\mathrm{allow} = 1800 / 2.0 / 1.25 = 720\ \mathrm{MPa}$$

Density $\rho = 1550\ \mathrm{kg/m^3}$. This ignores matrix-dominated allowables, joints, and buckling. It is an *optimistic* membrane floor, not a design allowable set.

## 3. Pressure membrane thickness

Thin-wall hoop: $t = PR / \sigma_\mathrm{allow}$.

$$t = (101300 \times 140) / 720\times10^6 = 0.0197\ \mathrm{m} \approx 20\ \mathrm{mm}$$

## 4. Two geometries

### Case S — cylinder wall only (no end caps)

$$m_\mathrm{wall} = 2\pi R L t \rho = 2\pi(140)(100)(0.0197)(1550) \approx 2.69\ \mathrm{kt}$$

### Case E — Case S plus two flat end disks at the same $t$

$$m_\mathrm{ends} = 2 \pi R^2 t \rho = 2\pi(140)^2(0.0197)(1550) \approx 3.76\ \mathrm{kt}$$

$$m_\mathrm{S+E} \approx 6.45\ \mathrm{kt}$$

Already above 5,850 t *before* decks, frames, penetrations, knockdown 0.50, or live load. Flat 280 m end caps dominate.

### Case T — short torus / no full-diameter pressure heads

If the rotating section does not fly two 280 m pressure disks — torus, ring, or pressure-bulkhead at a much smaller radius — Case E is the wrong model. Case S (~2.7 kt membrane wall) plus decks could still land near 5.85 kt. That is a *geometry* question, not a material question.

## 5. Spin (order of magnitude)

$\omega = 0.251\ \mathrm{rad/s}$, $a = 8.83\ \mathrm{m/s^2}$ at 140 m. Membrane pressure is the sizing driver for the wall; spin matters for decks and attachments. This note does not size decks. ADR-0005 occupied floor is the live-load side.

## 6. What PATSAGi will accept as Pass A output

A real FEA report must split mass at least as:

| Bucket | Why |
|--------|-----|
| Cylindrical shell | Compare to Case S ~2.7 kt |
| End caps / spin-interface bulkheads | Compare to Case E; say if heads are full-diameter or not |
| Decks + stiffening | Occupied-floor map |
| Joints / penetrations / contingency | |

If the model uses full-diameter flat heads and still prints 5,850 t without showing how the heads disappeared, reject the run.

## 7. Decision

- 5,850 t remains the planning lock.
- Change rule remains 6,727.5 t.
- **Pass A stays OPEN.**
- First FEA question is now explicit: *are the pressure heads full-diameter disks or not?*

Negative result dignity: Case E overshoot is a live risk, not a secret.
