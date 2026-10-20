---
id: sparse-indicator-linear-growth-in-both-bases
kind: result
title: A non-eventually-periodic indicator with linear section growth in both bases 2 and 3
status: reviewed
claim: >
  Let E = {2^j : j >= 0}, A = {6^e : e in E} and f = 1_A on n >= 0. With G_k(f; D) the number of distinct entire
  sections n -> f(k^a n + r), 0 <= a <= D, 0 <= r < k^a: G_2(f; D) <= 5D + 3 and G_3(f; D) <= 3D + 3 for every D >= 0,
  yet f is not eventually periodic; its joint 2/3 section family through depth D has at least (D+1)(D+2)/2 members.
  So separately linear growth in two multiplicatively independent bases does not force eventual periodicity,
  contradicting Conjecture 3.4 of Bell's 2009 survey "Cobham's theorem and its extensions" as printed. f is not a
  Collatz invariant (f(6) = 1, f(3) = 0).
authors:
  - ChatGPT main lane (Codex)
created: 2026-10-18
certificates: [v005_sparse_growth_check.py]
evidence:
  - "../automatic-section-forces-constancy/literature.md section 2: the written proposition and proof, and the joint-section count"
  - "../automatic-section-forces-constancy/verify_examples.py: V005's bounded replay includes the sparse control (59,823 sparse-cell evaluations, 45 mixed sections distinguished with 990 comparisons)"
reviewed_by:
  - by: Claude side lane (Opus)
    date: 2026-10-18
    link: v005_sparse_growth_check.py
    scope: "Feed 22:10 (REFEREE V005): Bell's Definitions 4-5 and Conjecture 3.4 read from the CIRM PDF; G_2 and G_3 computed exactly (not from prefixes) from v_p(6^e) = e, inside 5D+3 and 3D+3 for D up to 1000; both dimensions 1 and f not eventually periodic; counterexample to the printed conjecture confirmed. The joint-section bound was not separately rechecked"
aliases: [V005-b]
tags: [invariants, automatic, section-growth, counterexample, cobham]
---

# A non-eventually-periodic indicator with linear section growth in both bases 2 and 3

## Statement

Put `E = {2^j : j ≥ 0}`, `A = {6^e : e ∈ E}` and `f(n) = 1_A(n)` for `n ≥ 0`. For a sequence `f` let

```
G_k(f; D) = #{ n ↦ f(k^a n + r) : 0 ≤ a ≤ D, 0 ≤ r < k^a },
```

with equality meaning equality on **all** `n ≥ 0`; this is the `k`-growth of Definition 4 in J. P. Bell, [*Cobham's theorem and its extensions*](https://numdam.org/item/10.5802/acirm.3.pdf), Actes des rencontres du CIRM 1 (2009), 11–16. Then `f` is not eventually periodic, but for every `D ≥ 0`

```
G_2(f; D) ≤ 5D + 3,     G_3(f; D) ≤ 3D + 3,
```

while the joint sections `F_(a,b)(n) = f(2^a 3^b n)`, `a + b ≤ D`, are pairwise distinct, so the joint family has at least `(D+1)(D+2)/2` members.

## Proof

From [`literature.md`](../automatic-section-forces-constancy/literature.md) §2 (V005). Fix `p ∈ {2, 3}` and a depth `a`. The support points `6^e` have `p`-adic valuation exactly `e`; those with `e ≥ a` lie in the zero class mod `p^a`, and those with `e < a` have nonzero residues with distinct valuations, so no two share a nonzero class. Hence every section with `r > 0` is the zero sequence or a singleton `δ_q`, `q = ⌊6^e/p^a⌋`, `e < a`. Over depths `0..D` the zero-offset sections give at most `D + 1` sequences, the zero sequence and `δ_0` at most two more. For `p = 2`, `6^e < 2^(3e)` means `q > 0` needs `a < 3e`, fewer than `2e` eligible depths per `e < D`, so `G_2 ≤ D + 3 + 2Σ_(e∈E, e<D) e < 5D + 3` (`D ≥ 1`), using `Σ_(2^j<D) 2^j < 2D`; for `p = 3`, `6^e < 3^(2e)` gives fewer than `e` depths and `G_3 < 3D + 3`. The non-strict bounds include `D = 0`. The support is infinite with gaps tending to infinity, so `f` is not eventually periodic. For the joint count, the supports of `F_(a,b)` are `{2^(e−a) 3^(e−b) : e ∈ E, e ≥ max(a, b)}`; equal supports force `a' − a = b' − b = c` with the tails of `E` invariant under translation by `c`, impossible for `c ≠ 0` since large powers of 2 cannot differ by `c`. ∎

## Certificates

- [`v005_sparse_growth_check.py`](v005_sparse_growth_check.py) (under a second; side lane, independent code): computes `G_2(f; D)` and `G_3(f; D)` **exactly** (no prefix truncation; it counts the zero-offset sections and the distinct singletons `⌊6^e/p^a⌋` from `v_p(6^e) = e`) for `D ≤ 1000` and requires `G_2 ≤ 5D + 3`, `G_3 ≤ 3D + 3`; at `D = 1000` it finds `G_2 = 2273`, `G_3 = 1631`. It rewrites [`v005_sparse_growth_check.json`](v005_sparse_growth_check.json) identically.

## Remarks

- **Not a Collatz counterexample.** `f` fails doubling invariance already at 3 (`f(6) = 1`, `f(3) = 0`); its support is even and divisible by 3. It does not refute the quantitative goal [`section-count-depth-ratio-unbounded`](../../questions/section-count-depth-ratio-unbounded/README.md).
- **What it rules out.** "Linear growth in both bases separately forces periodicity", so a linear-complexity Cobham theorem in that form is false; any route of that kind has to use the **joint** family `b(2^i 3^j n + r)` (as [`automatic-section-forces-constancy`](../automatic-section-forces-constancy/README.md) does) or the scalar identities. This supersedes the side lane's earlier remark (feed 21:26) that excluding linear growth "in both bases" would be a linear-complexity Cobham theorem.
- **Why the count is linear.** A single-point section `⌊6^e/2^a⌋` becomes `δ_0` once `a > e·log₂6`, so each `e` contributes about `1.6e` functions; the Lean lane flagged that a naive count gives `D log D` (iteration 6).
- **Literature.** Bell's Conjecture 3.4 asserts eventual periodicity for a finite-valued sequence with finite dimensions (`limsup log G_k / log D`) in two independent bases; both dimensions of `f` are 1. Neither lane found a published correction in a bounded search; that establishes neither novelty nor the absence of a later correction. Novelty undetermined.

## History

- New node by the B16 migration (Claude, Opus 5.5) from `experiments/viewpoints/V005/literature.md` §2 and the V005 report §3 (legacy ID V005) at commit `be73a66`; the note stays in [`automatic-section-forces-constancy`](../automatic-section-forces-constancy/README.md)'s folder. The side-lane check `reviews/side_lane/v005_sparse_growth_check.*` moved here.
- Main lane (ChatGPT/Codex), 2026-10-18, main commit `85a07c2`; side-lane confirmation, feed 22:10.
