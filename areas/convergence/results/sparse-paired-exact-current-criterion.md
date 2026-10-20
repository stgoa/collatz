---
id: sparse-paired-exact-current-criterion
kind: result
title: Exact currents at arbitrarily sparse pairs of cutoffs N_j, N_j − 1 imply Collatz convergence
status: written
claim: >
  Odd-only clock, absorbing at 1; Π^R_N the right-aligned packets. Fix an integer d ≥ 1 and put
  N_j = 2·3^(d−1)·(2j+1) for j ≥ 0. If finite exact currents exist for Π^R_(N_j) and Π^R_(N_j − 1) whenever both
  cutoffs are at least 8, then every positive integer reaches 1. The selected pairs have density
  1/(2·3^(d−1)) among cutoffs. The argument needs exact currents: it does not hold as stated for currents with
  nonpositive residual. It supplies no current.
authors:
  - ChatGPT main lane (Codex)
created: 2026-10-17
depends_on: [right-aligned-fixed-core-remainder, qualitative-current-criterion]
evidence:
  - "../five-ray-current-criterion/check_sparse_criteria.py, sparse_criteria_audit.json (a certificate of that node): the source difference (8) at the 249 cutoffs N = 10, 14, …, 1002, and 1665 inverse lifts for d = 1, …, 5 and odd y ≤ 999 coprime to 3"
aliases: [R5-c]
tags: [convergence, packet-currents, right-aligned, exact-currents, sparse-cutoffs]
---

# Exact currents at arbitrarily sparse pairs of cutoffs N_j, N_j − 1 imply Collatz convergence

## Statement

Odd-only Syracuse map `S`, absorbing at 1; `ν_N`, `Π_N = Π^R_N` as in [`right-aligned-fixed-core-remainder`](right-aligned-fixed-core-remainder/README.md), `e` the nontermination indicator. Fix any integer `d ≥ 1` and, for every integer `j ≥ 0`, set `N_j = 2·3^(d−1)·(2j+1)`.

**Theorem.** Suppose exact finite currents exist at both `N_j` and `N_j − 1` whenever both cutoffs are at least 8. Then Collatz follows. These selected pairs have asymptotic density `1/(2·3^(d−1))` among the integer cutoffs.

## Proof

From §7 of the legacy sparse-criteria note, kept as written.

Each `N_j` is `2 mod 4`. For any `N = 4k + 2`, the second source cutoff is unchanged from `N − 1`, while the first adds only the odd state `r = 3N/2 = 6k + 3`, with coefficient `−1`. Thus the exact source identity is

```
ν_N − ν_(N−1) = −δ_(3N/2).                                                             (8)
```

Finite divergences pair to zero with `e`, and the core remainder also pairs to zero. Subtracting the two exact-current identities therefore gives `e(3N/2) = 0`. Hence every odd multiple of `3^d` terminates. The only possible omitted small multiples are 3 and 9, already verified to terminate.

Every odd `y` coprime to 3 has an odd inverse Syracuse lift divisible by `3^d`. To see this, 2 has order `2·3^d` modulo `3^(d+1)`. An elementary proof is the identity `v₃(2^(2·3^k) − 1) = k + 1`: it holds at `k = 0`, and if `z = 1 + 3^r·u` with `3 ∤ u`, then `v₃(z^3 − 1) = r + 1` by expansion, for `r ≥ 1`. Euler's theorem and the even order modulo 3 then show that the order is exactly `2·3^d`, the number of units of the modulus. Consequently there is an exponent `1 ≤ a ≤ 2·3^d` with `2^a·y ≡ 1 (mod 3^(d+1))`. The number

```
x = (2^a·y − 1)/3
```

is positive, odd, divisible by `3^d`, and satisfies `S(x) = y` with exact valuation `a`. Its convergence forces convergence of `y`. An odd multiple of 3 has a successor coprime to 3, completing the argument. ∎

## Remarks

- **Exact currents only.** Subtracting two upper bounds, or two current identities with nonpositive residuals, does not retain a nonpositive residual. Equation (8) therefore does not justify this sparse criterion for one-sided currents. Compare [`five-ray-current-criterion`](five-ray-current-criterion/README.md), which allows nonpositive residuals.
- **What it shows.** Exact paired certificates already encode convergence of an arithmetic progression of individual seeds; the sparsification alone supplies no constructor. A related exact-current thinning (cutoffs `N ≡ 2, 5 mod 8`) is [`exact-current-prefix-criterion`](exact-current-prefix-criterion.md).
- The general claims rest on the written argument; the script checks the source identity and the inverse lifts on finite ranges. Novelty undetermined.

## History

- Migrated from `experiments/current_construction/frontier/sparse_current_criteria.md` §7 (part of the legacy R5 round) at commit `be73a66`, by the B08 migration (Claude, Opus 5.5). Legacy status: "written conditional proofs with exact finite checks".
- Main lane (ChatGPT, Codex), 2026-10-17. No review from another lane is on record.
