# HF-01 CI Capability Card — What This Repository Can Actually Compute

**Status:** Paper card + executable stub. **No pass of WP-HF-01 has been run.**
**Package:** [WP-HF-01](../docs/work-packages/WP-HF-01-higher-fidelity-pass.md)
**Results card:** [hf-01-run-card.md](hf-01-run-card.md) — still blank, and this card does not add a row to it
**Owner:** Autonomicity Games Inc.
**Authority:** Ra-Thor + Permanent PATSAGi Councils under TOLC 8
**Contact:** info@Rathor.ai
**Proof Ladder:** Design / systems-engineering posture. Surmise is allowed; surmise labeled as measurement is forbidden.

---

## 1. Why this card exists

WP-HF-01 asks for finite element analysis, Monte-Carlo radiation transport, and a subscale
sail deployment. A reader — human or AI — can reasonably ask what of that this repository
can execute on its own. The honest answer needs to be written down and, where possible,
machine-checked, so that "not run" is a verified state rather than a promise.

**Short answer: none of it.** Continuous integration here is a GitHub Actions `ubuntu-latest`
runner with CPython and no third-party packages. It can run closed-form arithmetic. It cannot
run a solver, and it has no test article.

## 2. Solver inventory

`tools/solver_probe.py` checks PATH for the codes that could in principle do this work:

| Role | Codes probed | Present in CI |
|------|--------------|---------------|
| FEA | CalculiX (`ccx`), Code_Aster (`as_run`), Elmer (`ElmerSolver`), SfePy (`sfepy-run`) | none |
| Radiation transport | OpenMC (`openmc`), Geant4 (`geant4-config`), PHITS (`phits`) | none |

```bash
python3 -m tools.solver_probe
```

Export-controlled codes are deliberately not in the probe list. This repository does not seek,
vendor, or wrap them. Note also that finding a binary on PATH would establish that a solver
exists, not that a qualified run has been performed by a named operator against frozen inputs.

## 3. Pass A — habitat FEA

| Field | Value |
|-------|-------|
| **Question** | Does the 5,850 t high-modulus CFRP habitat structure survive higher-fidelity analysis? |
| **Inputs** | [hf-01-pass-a-input-deck.toml](hf-01-pass-a-input-deck.toml) (frozen, revision ADR-0004); allowables from [allowables-and-safety-factors-wp-de-01.md](../materials/allowables-and-safety-factors-wp-de-01.md); load cases LC-01…LC-08 |
| **Tool required** | A shell/solid FEA solver with linear buckling eigenvalue extraction and orthotropic composite allowables |
| **Tool available in CI** | None |
| **What CI does run** | `tools/hf01_pass_a_toy.py` — thin-wall hoop thickness and membrane mass, closed form |
| **Pass criteria** | Positive margin on all eight load cases under stated factors; recommended mass within ±15 % of 5,850 t (that is, ≤ 6,727.5 t) or an explicit change-rule trigger; water tanks identical in mass and location to Pass B; mesh, allowables, and knockdowns all cited |
| **Fail criteria** | Any load case with negative margin; recommended mass > 6,727.5 t without a change-rule row in the risk register; a run that cannot cite its mesh convergence |
| **Result** | **NOT RUN** |

### What the toy computes, and what it deliberately ignores

The stub executes the arithmetic already published in
[hf-01-pass-a-analytical-sanity.md](hf-01-pass-a-analytical-sanity.md), reading the frozen deck
so the two cannot drift. `tests/test_hf01_pass_a_toy.py` pins the outputs to the figures in that note.

```bash
python3 -m tools.hf01_pass_a_toy
```

| Quantity | Value |
|----------|-------|
| Membrane allowable (Ftu 1,800 MPa / 2.0 / 1.25) | 720 MPa |
| Thin-wall hoop thickness at 101.3 kPa, R = 140 m | 19.7 mm |
| Case S — cylinder wall membrane only | 2.69 kt |
| Case E — two full-diameter flat heads | 3.76 kt |
| Case S+E | 6.45 kt |

Ignored: buckling and the 0.50 knockdown, matrix-dominated and shear allowables, decks, frames,
stiffening, joints, penetrations, the spin interface, every spin/transient/docking/thermal load
case, and the LC-04 live load, equipment, and water inventory. That list is why this is a toy,
and the code carries it in `ToyResult.ignored`.

`ToyResult.recommended_habitat_mass_t()` raises `PassANotRun` by design. There is no code path in
this repository that yields a Pass A habitat mass, and a test asserts it stays that way.

**What the toy is nonetheless good for:** it keeps the note's open geometry question in front of
anyone who runs CI. With full-diameter flat heads, the bare membrane is already over 5,850 t before
a single deck. Without them, Case S at 2.69 kt leaves room. The first question for a real FEA is
therefore a geometry question, not a material question.

## 4. Pass B — Monte-Carlo dose

| Field | Value |
|-------|-------|
| **Question** | Do the dose targets hold inside the 450–750 t dedicated shielding band? |
| **Inputs** | Four geometries from [radiation-scoping-wp-de-02.md](../systems/shielding/radiation-scoping-wp-de-02.md); GCR solar-min and solar-max spectra; design-basis SPE; secondary production; the same water mass and placement as Pass A LC-04 |
| **Tool required** | A coupled hadron/lepton Monte-Carlo transport code with a nuclear data library and secondary particle production |
| **Tool available in CI** | None |
| **What CI does run** | **Nothing.** No toy is offered for this pass — see below |
| **Pass criteria** | ≤ 150–200 mSv/year effective, ≤ 1.0–1.5 Sv career over 10–25 years, ≤ 50–100 mSv per design-basis SPE in the storm shelter, all achieved inside 450–750 t dedicated |
| **Fail criteria** | Targets require > 750 t dedicated, which fires the 15 % change rule and a risk-register row |
| **Result** | **NOT RUN** |

**Why there is no Pass B toy.** A one-line exponential attenuation estimate is easy to write and
would be worse than nothing. GCR dose behind hydrogen-rich shielding is governed by secondary
particle production, and a slab attenuation model omits exactly the physics that makes the answer
non-obvious — it can report a reassuring number while the real transport goes the other way.
Publishing that figure, even labelled, would put a plausible wrong number where collaborators
could quote it. Pass B stays empty until a real transport code runs.

## 5. Pass C — Gate E1 sail subscale

| Field | Value |
|-------|-------|
| **Question** | Does MS-B deploy and damp on a subscale article? |
| **Inputs** | [gate-e1-magsail-deployment-plan.md](../manufacturing/gate-e1-magsail-deployment-plan.md) |
| **Tool required** | A physical test article, ground kinematics rig, then thermal-vacuum |
| **Tool available in CI** | None, and none is possible. This is hardware |
| **Pass criteria** | ≥ 90 % deployment success across the defined series; residual dynamics damped without structural damage; attitude trim after deploy; no unrecoverable single-point failures on the article |
| **Fail criteria** | Anything less. A failed E1 keeps residual-fusion margins; it does not relax the 1.8–3.5 kt residual propellant |
| **Result** | **NOT RUN — no test article exists** |

MS-B 550–750 t is a planning band, not an E1 deliverable. E1 tests packaging and dynamics. It does
not weigh the flight sail.

## 6. Summary

| Pass | Tool needed | In CI | Result |
|------|-------------|-------|--------|
| A — habitat FEA | FEA solver with buckling | absent (closed-form toy only) | **NOT RUN** |
| B — Monte-Carlo dose | transport code + nuclear data | absent (no toy offered, on purpose) | **NOT RUN** |
| C — Gate E1 sail | physical article | not applicable | **NOT RUN** |

A green CI check on this repository means the locked numbers are mutually consistent and the
published arithmetic reproduces. It does not mean any pass of WP-HF-01 has been executed. No CI
result may be entered as a row on [hf-01-run-card.md](hf-01-run-card.md); that card records runs
by named operators against frozen inputs, and negative results with equal dignity.

---

**This card describes capability, not results. WP-HF-01 remains open on all three passes.**
