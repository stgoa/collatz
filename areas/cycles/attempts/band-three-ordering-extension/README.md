---
id: band-three-ordering-extension
kind: attempt
title: Extending the dyadic ordering of q = 1 cycles from H < 8L to H < 16L by excluding the (n, 8n+1) pair
status: written
claim: >
  Tried, toward ordering every q = 1 cycle of the raw odd-only 3x+1 map with H < 16L: exclude directly the
  only possible inversion, a pair (n, 8n+1) at heights (0, 3). Verdict: the direct route is blocked. The pair's
  forced orbit 8n+1 → 6n+1 → 9n+2 → … adds only 2-adic congruences, so no finite-step contradiction exists; the
  general pair relation is a defect recursion of the rotation-overlap type, not easier than the general
  problem; and the same pair type occurs in actual 3x+q cycles (37 pairs at height gap exactly 3 among 719
  cycles, odd q < 400), so the inversion lemma alone cannot exclude it. No cycle is excluded.
authors:
  - Claude side lane (Opus)
created: 2026-10-19
depends_on: [q-one-inversion-pair-reduction, dyadic-order-lemma]
evidence:
  - "s3_inversion_pairs.py, s3_inversion_pairs.json: side-lane exploration probe (about 37-47 s): every odd q < 400 with 3 ∤ q, cycles from odd starts ≤ 6001, all actual inversions with height gap k ≤ 11 (counts by k) and the 37 pairs (n, 8n+1) at gap exactly 3. Fails at its new path: it imports the side-lane helper s1a_integer_cycle_check from its own folder (now in ../../results/ordered-gap-closed-form/). Passed at be73a66 as reviews/side_lane/s3_inversion_pairs.py (archive/legacy-checker-run-be73a66.md)"
aliases: [S03]
tags: [cycles, dyadic-order, inversion, rejected-mechanism]
---

# Extending the dyadic ordering of q = 1 cycles from H < 8L to H < 16L by excluding the (n, 8n+1) pair

## Idea

At `q = 1`, every cycle with `H < 8L` is ordered ([`three-band-collatz-cycles-are-ordered`](../../results/three-band-collatz-cycles-are-ordered.md)), and ordered cycles carry the sparse-forcing and `J` machinery. Extending the ordering to band 3 (`H < 16L`) needs only one inversion type excluded. S3 asked whether that pair can be excluded directly.

## What happened

**1. What blocks ordering at band 3** (exact; formal as [`q-one-inversion-pair-reduction`](../../results/q-one-inversion-pair-reduction/README.md)). C005's inversion lemma applies to `z_i < z_j` with `h_j = h_i + k`, where `r = n_j − 2^k·n_i` is positive and odd. The sorted images invert exactly when `3r < q(2^k − 1)`. At `q = 1`: `k = 1` would need `3r < 1` and `k = 2` would need `3r < 3`, which never happen (equality is excluded by primitivity); `k = 3` needs `3r < 7`, so `r = 1`. So a `q = 1` cycle with `H < 16L` (`B ≤ 3`) is ordered unless it contains a pair `(n, 8n+1)` with `h(n) = 0` and `h(8n+1) = 3`. The two points are then automatically sorted-adjacent: `z = n` and `n + 1/8`, and no `2^(−h)·odd` lies strictly between them when `h ≤ 3`. If no such pair exists, the ordered results (C005-b's `three_band`, C006-f and the formal `J` bound of 09:43) extend from `H < 8L` to `H < 16L`. *(Lean lane's precision: the extension would go through C006-f's any-`q` ordered form, not `three_band`, which is the `B ≤ 2` statement.)*

**2. The pair's orbit at `q = 1` is forced, but only 2-adically.**

- `3(8n+1) + 1 = 4(6n+1)` with `6n+1` odd, so the next state is `6n+1`.
- `3(6n+1) + 1 = 2(9n+2)` with `9n+2` odd, so the next state is `9n+2`.
- After that comes `(27n+7)/2^v`.

The constraint `H < 16L ≤ 16n` forces `n < 16L/9` and further range conditions. Each step only adds a 2-adic congruence on `n`. A positive density of `n` survives any finite number of steps, so no finite-step contradiction exists.

**3. The general relation is a defect recursion.** Write the pair as `n_(t+h) = 2^(K_t)·n_t − c_t`, starting from `K_0 = 3`, `c_0 = −1`. The pair's two orbits are two rotations of the same cycle. Then

```
K_(t+1) = K_t + a_t − a_(t+h),     c_(t+1) = (2^(K_t) + 3c_t − 1)/2^(a_(t+h)),
```

and closing the cycle requires `(K_m, c_m) = (3, −1)`. This is a rotation-mismatch / overlap problem of C013's type (see [`shared-background-denominator-law`](../../results/shared-background-denominator-law/README.md) and [`paired-state-run-law`](../../results/paired-state-run-law.md)), with a dyadic scale `2^(K_t)`. It is not easier than the general one.

**4. Data: the `q = 1` inversion type occurs at other `q`.** `s3_inversion_pairs.py` scans odd `q < 400` with `3 ∤ q`: 719 cycles with `m ≥ 2`. It finds actual inversions at every height gap `k = 1…11`, and **37 pairs `(n, 8n+1)` at height gap exactly 3**. Examples, as `(q, n, m)`: `(121, 35, 46)`, `(175, 29, 12)`, `(181, 23, 10)`, `(191, 47, 24)`. *(Lean lane's precision: these show only that the pair type is arithmetically possible; they are not controls for the `q = 1`, `H < 16L` target. For example, the `3x+121` cycle through 35 and 281 has `H > 16L`.)*

## Why it fails

The inversion lemma alone cannot exclude the pair, since it occurs at other `q`. Excluding it at `q = 1` needs `q = 1`-specific global arithmetic; the `q`-dependence enters only through the forced orbit `8n + 1 → (24n + 3 + q)/2^v → …`, which constrains `n` only 2-adically step by step, and the closing condition is the general overlap problem.

## What survives

- The exact reduction (§1): [`q-one-inversion-pair-reduction`](../../results/q-one-inversion-pair-reduction/README.md) (formal).
- The defect recursion (§3), as a reformulation.
- With [`ordered-cycle-run-renormalisation`](../ordered-cycle-run-renormalisation/README.md) (S02) and [`band-one-gcd-law-search`](../band-one-gcd-law-search/README.md) (S04), one of three shortcuts on the low-band ordered class, each reducing to the coupled `J`-term divisibility. The side lane switched to S4.

## History

- Migrated from `experiments/cycle_spectrum/S03/INVERSION_PAIRS.md` (legacy ID `S03`; side-lane producer batch S3, "a quick negative; no exclusion") at commit `be73a66`, by the B05 migration (Claude, Opus 5.5). The side-lane probe `reviews/side_lane/s3_inversion_pairs.{py,json}` moved here; §1 also became [`q-one-inversion-pair-reduction`](../../results/q-one-inversion-pair-reduction/README.md).
- Side lane (Claude, Opus), feed 2026-10-19 10:58. The Lean lane checked §1 by hand (feed update 11:11: correct) and added the two precisions quoted above; it did not issue a verdict on §§2–4, so this attempt stays `written`.
