# HF-01 Run Card

**Status:** Blank — no runs recorded  
**Package:** [WP-HF-01](../docs/work-packages/WP-HF-01-higher-fidelity-pass.md)  
**Tooling reality:** [hf-01-ci-capability-card.md](hf-01-ci-capability-card.md) — no FEA or transport solver is available to this repository  
**Pass A inputs:** [hf-01-pass-a-input-deck.toml](hf-01-pass-a-input-deck.toml)  
**Command:** [UNIFIED-NEXT.md](../docs/UNIFIED-NEXT.md)  
**Owner:** Autonomicity Games Inc.  
**Contact:** info@Rathor.ai

| Pass | Date | Operator | Code / facility | Result | 15 % rule | Notes |
|------|------|----------|-----------------|--------|-----------|-------|
| A FEA | — | — | — | not run | — | Input deck frozen. 5,850 t still a planning lock. |
| B Monte-Carlo dose | — | — | — | queued | — | Starts after Pass A holds or fires the change rule. |
| C Gate E1 | — | — | — | queued | — | Deploy plan exists; no test article. |

Add a row per attempt. Negative results stay on this card.

A row means a named operator ran a qualified code against frozen inputs. Continuous integration
does not produce rows: it has no solver and no test article. See the capability card above.
