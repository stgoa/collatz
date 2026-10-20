---
id: unequal-slope-two-block-growth
kind: result
title: Unequal-slope two-block words have denominator 2^((1−o(1))·A), ineffectively
status: reviewed
claim: >
  Raw odd-only clock. Fix nonempty positive words u, v with Δ = Σu·|v| − Σv·|u| ≠ 0. Uniformly over
  k, ℓ ≥ 1 as N = k + ℓ → ∞, log gcd(G_u(k), G_v(ℓ)) = o(N). Restricted to pairs with
  D(u^k v^ℓ) > 0 and A = k·Σu + ℓ·Σv, 0 ≤ A·log 2 − log den(u^k v^ℓ) = o(N); so for every η > 0
  there is N_0(u, v, η) with den(u^k v^ℓ) ≥ 2^((1−η)·A) for all such pairs with N ≥ N_0, and each
  bounded set of denominators occurs for only finitely many exponent pairs. Neither block needs
  positive D. Conditional on two Corvaja–Zannier inputs; the thresholds are ineffective.
authors:
  - ChatGPT main lane (Codex)
created: 2026-10-19
depends_on: [repeated-block-cancellation-bound]
assumes: [corvaja-2005-s-unit-height]
evidence:
  - "INDEPENDENT_SLOPES.md: the written argument, with the exact source inputs and every local contribution"
  - "../equal-total-two-block-exclusion/ROOT_REVIEW.md: main-lane root review of the application (section 'Unequal slopes and primary source')"
reviewed_by:
  - by: Claude Lean lane (Fable)
    date: 2026-10-19
    scope: "Side-lane feed (legacy archive/side_lane/FEED.md), 2026-10-19 00:26, update 00:31: the Lean lane audited INDEPENDENT_SLOPES.md and found no error. The Corvaja–Zannier inputs themselves were not re-proved; the side lane's REFEREE notes that this part relies on Corvaja–Zannier and is ineffective"
tags: [cycles, denominators, two-blocks, s-units, ineffective, conditional]
---

# Unequal-slope two-block words have denominator 2^((1−o(1))·A), ineffectively

## Statement

For a word `z` of length `m` and sum `A`, `P_z = 2^A`, `Q_z = 3^m`, `D_z = P_z − Q_z`. Fix nonempty words `u, v` and put `a = sum(u)`, `r = len(u)`, `b = sum(v)`, `s = len(v)`, `Δ = a·s − b·r`, `G_u(k) = (P_u^k − Q_u^k)/D_u`, `G_v(ℓ) = (P_v^ℓ − Q_v^ℓ)/D_v`, `K = D_u·C_v − D_v·C_u`. Each `G` is a positive integer geometric sum, even when its `D` is negative; `D_u, D_v ≠ 0` by unique factorisation.

**Unequal-slope theorem.** Suppose `Δ ≠ 0`. Uniformly over positive integers `k, ℓ` as `N = k + ℓ → ∞`,

```
log gcd(G_u(k), G_v(ℓ)) = o(N).                                  (1)
```

Restricting to pairs with `D(u^k v^ℓ) > 0`, put `A = a·k + b·ℓ`, `M = r·k + s·ℓ`. Then

```
0 ≤ A·log 2 − log den(u^k v^ℓ) = o(N).                            (2)
```

So for every `η > 0` there is `N_0(u, v, η)` such that every such positive pair with `N ≥ N_0` satisfies

```
den(u^k v^ℓ) ≥ 2^((1−η)·A).                                       (3)
```

Every fixed denominator, and every bounded set of denominators, occurs for only finitely many exponent pairs in this fixed two-block family. Neither block is required to have positive `D`; one block may expand. An empty or finite positive domain makes the statement vacuous.

## Proof

Written proof: [`INDEPENDENT_SLOPES.md`](INDEPENDENT_SLOPES.md). Inputs (see [`corvaja-2005-s-unit-height`](../../../../sources/corvaja-2005-s-unit-height.md)): Corvaja–Zannier, Corollary 1, Eq. (1.3) (Input A), and Proposition 1, Eq. (2.2) (Input B), applied with `S = {∞, 2, 3}`.

- **Gcd of the geometric sums (1).** With `α = 2^a/3^r`, `β = 2^b/3^s`, `U = α^k`, `V = β^ℓ` in `Γ = ⟨(α,1), (1,β)⟩`, the determinant `k·ℓ·Δ ≠ 0` makes every pair multiplicatively independent. At 2 and 3 the local terms vanish; at other primes they give `−log gcd(|L_u|, |L_v|)` with `L_u = 2^(ak) − 3^(rk)`, `L_v = 2^(bℓ) − 3^(sℓ)`; the archimedean term is nonpositive, which only helps. Input A then gives `log gcd ≤ ε·H` outside a finite set, with `H = O(k + ℓ)`; the index map is injective, so the exceptions are finitely many index pairs, including sequences along which one exponent stays fixed.
- **From geometric sums to cancellation.** The elimination identities give `g = gcd(C_w, D_w) | |K|·gcd(G_u(k), G_v(ℓ))` when `K ≠ 0`, and `Δ ≠ 0` forces `K ≠ 0` on the positive domain (the common-fixed-point argument of [`repeated-block-cancellation-bound`](../repeated-block-cancellation-bound/README.md), claim 4). So `log g = o(N)`.
- **Power-gap lemma (from Input B).** Uniformly over `A, M ≥ 1` with `2^A > 3^M`, `log(2^A − 3^M) = A·log 2 − o(A)`: apply Input B to `f = X/Y − 1` at `(2^A, 3^M)`; only the archimedean negative term remains, and the exceptional translates (fixed `A` or fixed `M`) contribute finitely many bad points. This handles an expanding block and words near the positivity boundary, with no fixed separation of `2^A/3^M` from 1.

Combining gives (2) and (3). No effective threshold is obtained; the inputs rest on the Subspace Theorem.

## Remarks

- **Ineffective.** The threshold `N_0` cannot be computed from this argument, so the theorem gives finiteness of each bounded denominator layer but cannot exhibit or exclude the finitely many exceptions.
- **Scope.** A fixed pair of blocks. The version uniform over changing blocks (one fixed ambient group of 2/3-units) is [`two-block-uniform-denominator-growth`](../two-block-uniform-denominator-growth/README.md). Equal slopes: [`proportional-slope-two-block-bound`](../proportional-slope-two-block-bound.md). Even unequal slopes do not justify a constant cancellation bound ([`constant-cancellation-two-growing-blocks`](../../attempts/constant-cancellation-two-growing-blocks.md)).
- **Controls.** `K = 0` retains actual positive generalised-map cycles (powers of one common primitive word, e.g. the `d = 5, 7, 13` controls); it is excluded here because `Δ ≠ 0` forces `K ≠ 0` on the positive domain. The finite checks of C002 do not verify the imported asymptotic theorem.
- The specialisation of the S-unit estimates is a written argument here, not an independent formal replay of the publication. Novelty undetermined.

## History

- Split from `experiments/cycle_spectrum/C002/` (legacy ID `C002`; `REPORT.md` §2 table, `INDEPENDENT_SLOPES.md`) at commit `be73a66`, by the B03 migration (Claude, Opus 5.5).
- Written by an independent main-lane agent (ChatGPT/Codex), 2026-10-19; the main-lane root read the primary source and the application and reported no issue.
