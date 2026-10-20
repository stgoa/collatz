---
id: normalised-quotient-termination
kind: question
title: Does the normalised quotient map T(q) = nu(S(q)) reach 1 from every canonical minimum?
status: open
claim: >
  Odd-only 3x+1 map S, absorbing at 1; nu the elementary-bridge normal form and B its canonical minima
  (q = 1 mod 8, or a complementary climber q = 2^a t - 1, a >= 2, t = -3^a mod 4) of
  elementary-bridge-quotient-normal-form. Prove or refute: for every q in B there is n with T^n(q) = 1, where
  T(q) = nu(S(q)). By that node's (9) (T^n(nu(x)) = 1 implies S^(n+2)(x) = 1, and S^n(x) = 1 implies
  T^n(nu(x)) = 1) this is equivalent to the Collatz convergence statement, so it is a reformulation, not a
  weakening; the quotient supplies closure of the state space, not a decreasing global parameter.
created: 2026-10-17
tags: [convergence, outer-residual, quotient, normal-form, frontier, collatz-equivalent]
---

# Does the normalised quotient map T(q) = nu(S(q)) reach 1 from every canonical minimum?

## Question

On the canonical minima `B` of [`elementary-bridge-quotient-normal-form`](../results/elementary-bridge-quotient-normal-form/README.md), the induced map `T(q) = ν(S(q))` increases on complementary climbers (`T(q) = (3q + 1)/2`) and decreases on `q ≡ 1 (mod 8)`, `q > 1`. Does every `q ∈ B` reach 1 under iteration of `T`? A proof needs a decreasing global parameter (or another argument) that the quotient does not supply by itself; any proposed parameter must also survive the ascent family `T^j(2^a − 1) = 3^j·2^(a−j) − 1` and the non-return `T(27) = 41`, `T²(27) = 31 > 27`.

## Why it matters

The legacy R25 note proves that termination of `T` is equivalent to ordinary Collatz convergence. It is the quotient form of the outer-residual target [`five-ray-complementary-profile-completion`](five-ray-complementary-profile-completion.md): the normalised run bridges of [`complementary-run-bridges`](../results/complementary-run-bridges/README.md) certify a root exactly when its normalised return `ν(f(x))` is already absorbed, and iterating that return is iterating `T`.

## Known progress

- The quotient, its exact current lift, all inverse branches and exact counts: [`elementary-bridge-quotient-normal-form`](../results/elementary-bridge-quotient-normal-form/README.md). Greedy inverse minimisation is not optimal at depth 2 (`y = 57 + 72j`).
- One normalised return certifies about 55.28% of the leading complementary mass and leaves `(25/576 − β)N + O(log⁴ N)` roots, `25/576 − β ≈ 0.019410`, with normalised returns at unbounded relative height: [`complementary-run-bridges`](../results/complementary-run-bridges/README.md). The side lane's `quotient_iteration_probe` there found (finite data and 2-adic model estimates; heuristic) that iterating `ν∘S` raises the mean drift about 3.5-fold but leaves the decay rate of staying high unchanged, and that the slowest actual roots are the same under `S` and under the quotient.
- No finite-label potential decreases on every return: [`bounded-runs-exclude-finite-label-potentials`](../results/bounded-runs-exclude-finite-label-potentials/README.md).
- The legacy rounds R40–R94 (`experiments/residual_progress/`, not yet migrated) pursued rank functions on critical domains instead.

## Suggested attacks

- Look for a parameter on `B` that strictly decreases along every complete run block of `T` (increasing complementary steps followed by one decreasing step), with intermediate increases allowed; [`bounded-runs-exclude-finite-label-potentials`](../results/bounded-runs-exclude-finite-label-potentials/README.md) shows what it cannot be.
- Any argument must use arithmetic of `3x+1` absent from the `3x+d` controls ([`locally-collatz-like-control-barrier`](../results/locally-collatz-like-control-barrier/README.md)).
