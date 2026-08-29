# WP-HF-01 — Higher-Fidelity Pass (FEA / Monte-Carlo Dose / Gate E1)

**Phase:** Physical testing & higher-fidelity computation  
**Status:** Ready for execution — no results claimed  
**Date:** 2026-08-29  
**Owner:** Autonomicity Games Inc.  
**Authority:** Ra-Thor + Permanent PATSAGi Councils under TOLC 8  
**Contact:** info@Rathor.ai  
**Proof Ladder:** Design / systems-engineering posture. This package does **not** open a new ACTIVE empirical program and does **not** publish performance as fact.

**Trigger:** Grok 2026-08-29 — propulsion interface and open gates remain ready for the next higher-fidelity pass.

---

## 1. Why this pass exists

ADR-0003 locked collaboration gates:

- Seed dry-mass **target:** 15.0 kt
- Public cruise **floor:** 0.05 c
- Internal cruise **lock:** ~0.055 c

Those gates sit on three numbers that Cycle-01 *named* and that physical / high-fidelity work must still *test*:

| Open gate | Cycle-01 planning lock | What HF-01 asks |
|-----------|------------------------|-----------------|
| Habitat structure FEA | 5,850 t high-modulus CFRP | Confirm or bound the 5,850 t number |
| Monte-Carlo dose | 450–750 t dedicated shielding | Confirm the band against GCR + SPE targets |
| Gate E1 sail | MS-B 550–750 t | Subscale deploy + damp, not flight drag |

HF-01 does not rewrite the mass budget. If a gate moves a major category by more than ~15 %, then and only then update `manufacturing/reference-seed-mass-budget.md` and the risk register.

---

## 2. Pass A — Habitat FEA confirmation

**Parent:** [WP-DE-01](WP-DE-01-structural-analysis.md)  
**Geometry freeze:** 140 m spin radius, 100 m ± 20 m axial length, 101.3 kPa, 0.90 g at main deck.

### Inputs (must be configuration-controlled)

- Locked CFRP allowables and knockdowns from `materials/allowables-and-safety-factors-wp-de-01.md`
- Deck live-load and water-tank geometry shared with Pass B (same water mass in both models)
- Load cases 1–7 from WP-DE-01 §2.2

### Outputs required before PATSAGi will look at a mass change

1. Global mesh description + element type + mesh-convergence note
2. Peak stress and buckling eigenvalue per load case
3. Mass breakdown: shell, decks, spin interface, penetrations
4. A single recommended habitat-structure mass with a ± band

### Pass / fail (analysis, not hardware)

| Criterion | Pass |
|-----------|------|
| All seven load cases | Positive margin under stated factors |
| Recommended mass vs 5,850 t | Inside ±15 % **or** explicit 15 % change-rule trigger |
| Water tanks | Same mass/location as Pass B |

**Honesty:** A paper FEA that cannot cite mesh, allowables, and knockdowns does not move 5,850 t.

---

## 3. Pass B — Monte-Carlo dose confirmation

**Parent:** [WP-DE-02](WP-DE-02-radiation-dose.md), [radiation-scoping-wp-de-02.md](../../systems/shielding/radiation-scoping-wp-de-02.md)

### Inputs

- Four geometries from the scoping note (baseline water, optimised water, storm-shelter core, ±20 % sensitivity)
- GCR solar-min, GCR solar-max, design-basis SPE, secondaries
- Dedicated shielding planning band 450–750 t on top of dual-use water

### Provisional dose targets (still provisional)

| Metric | Target |
|--------|--------|
| Annual effective (GCR-dominated) | ≤ 150–200 mSv/year |
| Career (10–25 yr) | ≤ 1.0–1.5 Sv |
| Storm shelter, design-basis SPE | ≤ 50–100 mSv/event |

### Outputs

- Dose vs dedicated-mass curve for each geometry
- Recommended dedicated mass inside or outside 450–750 t
- Statement of code, physics list, and cutoff energies (or an explicit “code not yet run”)

### Pass / fail

| Criterion | Pass |
|-----------|------|
| Targets met inside 450–750 t dedicated | Band holds |
| Targets require >750 t dedicated | Trigger 15 % change-rule + risk-register row |
| No transport run performed | Gate stays **open**; do not speak as if closed |

---

## 4. Pass C — Gate E1 sail subscale

**Parent:** [gate-e1-magsail-deployment-plan.md](../../manufacturing/gate-e1-magsail-deployment-plan.md)  
**Not in scope:** plasma drag (Gate E2), flight-relevant demo (Gate E3 / FT-3).

### Minimum success (physical article)

| Criterion | Threshold |
|-----------|-----------|
| Deployment success | ≥ 90 % of the defined series |
| Residual dynamics | Damped without structural damage |
| Control authority | Attitude trim after deploy |
| Single-point failures | None unrecoverable on the test article |

Progression stays ground kinematics → thermal-vacuum → optional free-flight only after the first two succeed.

MS-B 550–750 t is a *planning band*, not an E1 deliverable. E1 tests packaging and dynamics. It does not weigh the flight sail.

---

## 5. Coupling to the 15.0 kt / 0.05 c gates

| If HF-01 finds… | Then |
|-----------------|------|
| Habitat FEA ≤ 6,730 t (5,850 + 15 %) and dose band holds | 15.0 kt seed target stays |
| Habitat FEA > 6,730 t or dedicated shield > 750 t | Reopen mass budget; 15.0 kt becomes a wish, not a target |
| E1 fails deploy / damp | Keep residual-fusion margins; do not relax 1.8–3.5 kt residual propellant |
| Exhaust velocity still unmeasured | 0.05 c public floor stays; 0.055 c stays internal lock |

Boost window 2.5–4.5 years is **not** an HF-01 output. It waits on measured exhaust velocity and tank fraction.

---

## 6. Run card (so collaborators do not invent results)

Record every attempt in `simulations/` using:

- Pass (A / B / C)
- Date, operator, code or facility
- Inputs hash or filename
- Result: pass / fail / incomplete
- Whether the 15 % change-rule fired
- Negative results published with equal dignity

A blank run card is the correct state today.

---

## 7. Governance

- Human sovereignty on any decision that would fly people.
- PATSAGi reviews Pass A/B numbers before the mass budget moves.
- PATSAGi reviews Pass C before sail scale-up or residual-propellant relief.
- Compassion gate: no dual-use / kinetic-delivery framing of the lunar loft path.
- Proof Ladder: surmise is allowed; surmise labeled as measurement is forbidden.

---

**HF-01 is the next higher-fidelity pass. It is not a claim that the pass has been run.**
