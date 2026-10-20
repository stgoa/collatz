---
id: three-band-collatz-cycles-are-ordered
kind: result
title: "A 3x+1 cycle with H < 8L is dyadically ordered with mechanical normalised word and gcd(A, m) = 1"
status: formal
claim: >
  Odd-only 3x+1 map (q = 1), raw clock. Let a primitive positive integer cycle with m ≥ 2 distinct
  states satisfy H < 8L (all heights h_i ≤ 2). Then its dyadically normalised successor is a circular
  rank shift, the normalised word c_i = a_i + h_(i+1) − h_i is c_i = q' + floor((i+1)h'/m) −
  floor(ih'/m) with gcd(h', m) = 1, and A = Σa_i = mq' + h' satisfies gcd(A, m) = 1. Equivalently,
  any primitive positive rational cycle with m > 1, H < 8L and gcd(A, m) > 1 has reduced
  denominator q > 1; a hypothetical nontrivial integer 3x+1 cycle with gcd(A, m) > 1 has H > 8L.
  This is a necessary structure, not an exclusion of H < 8L.
authors:
  - ChatGPT main lane (Codex)
created: 2026-10-19
depends_on: [dyadic-order-lemma]
lean:
  - LeanLane.Cyc.OddCycle.three_band
  - LeanLane.Cyc.OddCycle.q_ne_one_of_not_coprime
  - LeanLane.Cyc.OddCycle.order_of_three_band
  - LeanLane.Cyc.no_inversion_of_le_two
evidence:
  - "../rotation-block-exclusion/ORDER_THEORY.md, section 2 'A three-band denominator restriction for d=1': the written proof"
reviewed_by:
  - by: Claude side lane (Opus)
    date: 2026-10-19
    scope: "Feed 2026-10-19 02:41, VERIFIED Lean C005-b: statement match with ORDER_THEORY.md section 2's three-band theorem and receipts checked; feed 02:13: the q = 11 control (inversion with H < 8L, gcd(A, m) = 2) shows the lemma needs q = 1"
  - by: Claude Lean lane (Fable)
    date: 2026-10-19
    scope: "C005 re-derived by hand (feed 02:13, update 02:19); Lean unit C005-b verified (iteration 20)"
tags: [cycles, dyadic-order, three-band, collatz-specific, formal]
---

# A 3x+1 cycle with H < 8L is dyadically ordered with mechanical normalised word and gcd(A, m) = 1

## Statement

Use the dyadic normalisation of [`dyadic-order-lemma`](dyadic-order-lemma.md). For `q = 1`, if a nontrivial positive integer `3x+1` cycle (primitive, `m ≥ 2`) satisfied

```
H < 8L   (equivalently max_i h_i ≤ 2),          (3)
```

then the sorted `F` list would be strictly increasing; its normalised word `c` would be a primitive mechanical word of 1s and 2s, `c_i = q' + floor((i+1)h'/m) − floor(ih'/m)` with `gcd(h', m) = 1`, and `A = mq' + h'` with `gcd(A, m) = 1`, while `a_i = c_i + h_i − h_(i+1)` retains the original height changes. This is a **necessary structure**, not an exclusion of the band (3).

**Denominator corollary.** Any primitive positive rational cycle with `m > 1`, `H < 8L` and `gcd(A, m) > 1` has reduced denominator `q > 1` (hence `q ≥ 5` in the coprime-to-6 domain). Equivalently, a hypothetical nontrivial integer `3x+1` cycle whose total valuation and period share a factor must satisfy `H > 8L`; equality `H = 8L` is impossible because the states are odd. This excludes a stated class of arbitrary primitive words beyond the narrow class `H < 2L`. It does not bound the spread when `gcd(A, m) = 1`.

## Proof

Written proof: [`ORDER_THEORY.md`](rotation-block-exclusion/ORDER_THEORY.md) §2. For `q = 1`, (2) of [`dyadic-order-lemma`](dyadic-order-lemma.md) cannot invert at height gap `k = 1` (`3r − 1 ≥ 2`); at `k = 2`, `3r − 3 ≥ 0`, and equality is excluded for a primitive cycle. With `B ≤ 2` no larger gap occurs, so sorted `F` is strictly increasing and the order lemma applies. The first arithmetically possible inversion for `q = 1` has `k = 3`, `r = 1`, a pair `n_j = 8n_i + 1` in the indicated normalised order; its existence inside a nontrivial integer cycle is not asserted.

## Lean

`lean/CycleSpectrum.lean`, Lean unit C005-b. `LeanLane.Cyc.OddCycle.three_band`: for an `OddCycle` (periodic odd numerators `n_i` with `n_0` the positive minimum, exact arrows `2^(a_i)·n_(i+1) = 3n_i + q`, heights `2^(h_i)·n_0 ≤ n_i < 2^(h_i+1)·n_0`, `h_i ≤ B`) with `q = 1`, `B ≤ 2`, `m ≥ 2` and distinct numerators over one period, there are `q', h'` with `gcd(h', m) = 1`, `c_i = q' + ((i+1)h')/m − (ih')/m`, `Σa_i = mq' + h'` and `gcd(Σa_i, m) = 1`. `order_of_three_band` gives the order (via `no_inversion_of_le_two` and the exclusion of equal images). `q_ne_one_of_not_coprime` is the denominator corollary: `B ≤ 2`, `m ≥ 2`, primitivity and `gcd(Σa, m) ≠ 1` force `q ≠ 1`. A rational cycle with reduced denominator `q` is exactly an `OddCycle` at parameter `q` after scaling. The prose's "`q` coprime to 6" is not needed (only `q > 0`), and `a_i ≥ 1` is not used. Axioms `propext`, `Classical.choice`, `Quot.sound`.

## Remarks

- **Specific to `q = 1`.** This is the first statement in the programme that uses `q = 1` rather than holding for every denominator. It fails for `q = 11`: the census cycle with minimum 13, numerators `(13, 25, 43, 35, 29, 49, 79, 31)`, has an inversion although `H < 8L`, and `gcd(A, m) = gcd(14, 8) = 2`; it correctly survives the corollary with `q > 1`.
- **Not an exclusion.** Ordered cycles in `[2L, 8L)` are not excluded: the height weights can cancel, as the ordered `q = 233` and `q = 5` controls show ([`mechanical-normalized-word-transfer`](../attempts/mechanical-normalized-word-transfer.md)). Extending the ordering to `H < 16L` at `q = 1` reduces to excluding the pair `(n, 8n+1)`; that is later side-lane work (legacy S03).
- Used by [`rotation-block-exclusion`](rotation-block-exclusion/README.md).

## History

- Split from `experiments/cycle_spectrum/C005/` (legacy ID `C005`; `ORDER_THEORY.md` §2) at commit `be73a66`, by the B03 migration (Claude, Opus 5.5). Main lane (ChatGPT/Codex), 2026-10-19. Formalised by the Lean lane as C005-b, iteration 20.
