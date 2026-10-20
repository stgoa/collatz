---
id: universal-w5-quotient-stopping
kind: question
title: Does the quotient orbit of rho(w) fall below (8 rho(w) - 5)/9 for every W5 input?
status: open
claim: >
  Odd-only 3x+1 map S, absorbing at 1; nu, T = nu S and rho(w) = nu(3w) as in elementary-bridge-quotient-normal-form
  and critical-image-rank-composition; W5 = {w > 0 : w = 5 mod 8}, where q = rho(w) >= 7. Prove or refute: for every
  w in W5 there is a finite k >= 0 with 9 T^k(q) + 5 < 8q (no uniform bound on k is required), or supply an
  alternative universal finite-current construction with a proved termination argument. By
  quotient-prefix-plans-rho-decreasing the universal statement is equivalent to Collatz convergence; it is Phase 6
  route node S.2 (with R.2 its frozen interface), not a weakening.
created: 2026-10-18
aliases: [P6-S.2, P6-R.2]
tags: [convergence, phase6, stopping-time, quotient, w5, collatz-equivalent]
---

# Does the quotient orbit of rho(w) fall below (8 rho(w) - 5)/9 for every W5 input?

## Question

For every `w ∈ W5`, put `q = ρ(w) = ν(3w)`; then `q ≥ 7` ([`critical-image-rank-composition`](../results/critical-image-rank-composition/README.md)). Is there always a finite quotient time `k ≥ 0` with

```
9 T^k(q) + 5 < 8q ?
```

Root 1 is excluded from the quantified domain. An alternative universal finite-current supply with a proved termination argument would also answer the route node; any replacement interface must be stated before it is relied on.

## Why it matters

By [`quotient-prefix-plans-rho-decreasing`](../results/quotient-prefix-plans-rho-decreasing/README.md) (reviewed), any such prefix is a strict-ρ plan, so universal hitting supplies every W5 tripling current by strong induction on ρ, which is [`universal-w5-tripling-currents`](universal-w5-tripling-currents.md) and hence convergence; conversely convergence sends every quotient orbit to 1, which passes the threshold. So this is a Collatz-equivalent stopping-time form, alongside [`normalised-quotient-termination`](normalised-quotient-termination.md). It is not a necessary local test for every possible current construction, nor an equivalence between finite search algorithms. In Phase 6 it was the open node of the stopping route S (route map in [`archive/convergence-phase6/`](../../../archive/convergence-phase6/)).

**Transfer.** The ordinary universal-descent analogue "every odd `n > 1` has some `S_d^k(n) < n`" fails at the nonprincipal cycle minima of [`baseline-obligation-transfer-controls`](../results/baseline-obligation-transfer-controls/README.md), including `19 → 31 → 49 → 19` for `d = 5`. The exact quotient statement is untested for `d ≠ 1`: no `ν_d`, `T_d` or `ρ_d` is defined.

## Known progress

- **Density one, with explicit constants (calibration S.1):** [`fixed-factor-stopping-explicit-constants`](../results/fixed-factor-stopping-explicit-constants/README.md) proves that the threshold is reached within `K_W(epsilon)` steps for all but an `epsilon`-fraction of W5 inputs below `X`, for all large `X`. The exceptional set is not removed, and letting `epsilon → 0` varies the horizon.
- **Scoped barriers (P6-002, P6-003):** iterating first-half descent by a constant-cardinality transport bound into arbitrary targets fails for every finite constant ([`arbitrary-target-linear-transport-barrier`](../results/arbitrary-target-linear-transport-barrier/README.md)), and so does contraction of any power-growth norm `0 < alpha < 1` on arbitrary targets ([`growth-norm-transport-barrier`](../results/growth-norm-transport-barrier/README.md)). Both leave estimates for the actual nonabsorbing set open: [`bad-set-half-descent-transport`](bad-set-half-descent-transport.md), with its conditional consequences and the `3x+d` negative control in [`bad-set-transport-bootstrap`](../results/bad-set-transport-bootstrap.md).
- **Two redundant preparations, graded none.** (P6-001) A proof that finitely many bounded-prefix stopping tests cannot cover W5 was correct but already follows from the frozen R25/R31 results ([`elementary-bridge-quotient-normal-form`](../results/elementary-bridge-quotient-normal-form/README.md), [`bounded-runs-exclude-finite-label-potentials`](../results/bounded-runs-exclude-finite-label-potentials/README.md)); its positive-density cylinder does not change that mechanism. (P6-002) Full backward components meet every finite binary or ternary residue cylinder, so a congruence-closure separation supplies nothing beyond the frozen Monks sufficient-sets audit ([`five-ray-profile-completion-suffices`](../results/five-ray-profile-completion-suffices/README.md)). Both were confirmed none by the side lane.
- **Published benchmarks** (Terras, Everett, Korec, Borovkov–Pfeifer, Lagarias's stopping-tail counts, Tao) each keep an exceptional set; see [`route-literature-transfer-audit`](../results/route-literature-transfer-audit.md) L1, L1a, L2.

## Suggested attacks

From the Phase 6 ledger: allow input-dependent unbounded histories (another finite dispatcher catalogue would not address the missing obligation); do not add exponent variants of the power-norm barrier; use properties of the actual nonabsorbing set `B = E ⊔ L^(−1)(B)`, another specified norm, or signed cancellation, and state exactly how `B`-invariance changes the estimate and why the claimed step fails on a certified `d`-cycle. The side lane observed that a target `y` has about `log2(X/y)/2` one-arrow first-half preimages below `X`, so logarithmically weighted transport (Tao's setting) is the natural untested weight (speculation).
