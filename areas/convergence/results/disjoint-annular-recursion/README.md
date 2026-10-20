---
id: disjoint-annular-recursion
kind: result
title: Multiplying the cutoff by 64 adds a disjoint six-band annulus A_N to the right-aligned packets
status: written
claim: >
  Odd-only clock, absorbing at 1; Π^R_N and η_N as in right-aligned-fixed-core-remainder. For every positive
  integer N divisible by 8, with Q = 9N/4: Π^R_(64N) = Π^R_N + A_N and η_(64N) = η_N, with
  supp Π^R_N ⊂ (1, Q) and supp A_N ⊂ (Q, 64Q). On each band 2^j·Q < y < 2^(j+1)·Q (j = 0, …, 5), A_N(y)
  depends only on y mod 18, by an explicit 6 × 6 table; every band has signed total 0, Σ_y y·A_N(y) = 63Q,
  ‖A_N‖₁ = 99N/2, ‖A_N⁺‖₁ = 99N/4 and |supp A_N| = 267N/8. Also A_N = P·V_N with V_N = ν_(64N) − ν_N an
  explicit three-interval measure. Corollary (with five-ray-current-criterion): currents with nonpositive
  residual for every increment A_N on the 30 sequences N = a·2^r·64^k suffice for Collatz. The identity is a
  recurrence for measures; it constructs no current for A_N.
authors:
  - ChatGPT main lane (Codex)
created: 2026-10-17
depends_on: [right-aligned-fixed-core-remainder, five-ray-current-criterion, finite-current-certificate-identity]
evidence:
  - "check_annular_recursion.py, annular_audit.json: derives the residue table from inverse source arithmetic and compares the whole annular measure with the packet constructor at every multiple of 8 through 512 and at 1000 and 4096 (66 cases, expanded cutoffs up to 262144), with bands, both source components, the core identity and the first moment; no trajectory search. Fails at its new path: it loads experiments/packet_currents/right_aligned_packets.py relative to the repository root (now right-aligned-fixed-core-remainder/right_aligned_packets.py). Passed at be73a66 as experiments/current_construction/recursive/check_annular_recursion.py inside scripts/verify_all.py, which compared its output with the receipt (archive/legacy-checker-run-be73a66.md: the gate ran these steps before stopping at residual_progress/history_frontier, and passed in full at 9dbc71a). The file name is kept because 16 residual-progress receipts pin its hash"
  - "../locally-collatz-like-control-barrier/main_claims_audit.py, main_claims_audit.json: the PR1 lane's independent check of the identity at 68 cutoffs (a certificate of that node)"
reviewed_by:
  - by: Claude PR1 lane (Opus)
    date: 2026-10-17
    link: ../locally-collatz-like-control-barrier/NOTE.md
    scope: "Finite only (NOTE §10, ledger C1): independent code checks Π_(64N) − Π_N against the six-band table mod 18 at every odd endpoint of (Q, 64Q), η_(64N) = η_N, supp Π_N ⊂ (1, Q), zero band totals, Σ A_N = 0, Σ y·A_N(y) = 63Q, ‖A_N‖₁ = 99N/2, ‖A_N⁺‖₁ = 99N/4 and |supp A_N| = 267N/8 at 68 cutoffs N ∈ {8, 16, …, 512, 768, 1024, 2048, 4096}. The written proof was not re-derived, so the status stays written"
aliases: [R6]
tags: [convergence, packet-currents, right-aligned, annular, recursion]
---

# Multiplying the cutoff by 64 adds a disjoint six-band annulus A_N to the right-aligned packets

## Statement

All clocks and measures are those of [`right-aligned-fixed-core-remainder`](../right-aligned-fixed-core-remainder/README.md) and the main proof note ([`papers/right-aligned-reduction`](../../../../papers/right-aligned-reduction/README.md)): odd-only Syracuse, absorption at 1, exact integer source cutoffs, and the revised right-aligned depth-one packets `Π^R_N` with core remainder `η_N`.

**Theorem.** Let `N` be any positive integer divisible by 8 and put `Q = 9N/4`, a positive even multiple of 18. Then

```
Π^R_(64N) = Π^R_N + A_N,     η_(64N) = η_N,
supp Π^R_N ⊂ (1, Q),         supp A_N ⊂ (Q, 64Q).
```

For `j = 0, …, 5`, on the integer band `2^j·Q < y < 2^(j+1)·Q`, `A_N(y)` depends only on `y mod 18`. It vanishes on multiples of 3 and has this table on the remaining odd residues:

| j | 1 | 5 | 7 | 11 | 13 | 17 |
|---|--:|--:|--:|---:|---:|---:|
| 0 | 1 | 0 | 1 | 0 | -2 | 0 |
| 1 | 2 | 1 | -1 | 1 | -1 | -2 |
| 2 | 3 | -1 | -3 | 2 | 0 | -1 |
| 3 | 1 | -3 | -2 | 3 | 1 | 0 |
| 4 | -1 | -2 | -1 | 1 | 2 | 1 |
| 5 | 0 | -1 | 0 | -1 | 0 | 2 |

Every band has signed total zero, and

```
Σ_y A_N(y) = 0,   Σ_y y·A_N(y) = 63Q,   ‖A_N‖₁ = 99N/2,   ‖A_N⁺‖₁ = 99N/4,   |supp A_N| = 267N/8.
```

**Lower-source representative.** With `V_N = ν_(64N) − ν_N` and `w_r(x) = 3·1[x ≡ r mod 3] − 1`, `A_N = P·V_N = V_N − (I − P)V_N`, where `V_N` is exactly `w_1(x)` on `3N/4 < x ≤ 3N/2`, `w_1(x) + w_2(x) = 1 − 3·1[3 | x]` on `3N/2 < x ≤ 48N`, `w_2(x)` on `48N < x ≤ 96N`, and zero elsewhere.

**Corollary (thirty sequences).** By [`five-ray-current-criterion`](../five-ray-current-criterion/README.md), the five rays split into 30 sequences `N_k = a·2^r·64^k` (`a ∈ {12, 14, 16, 18, 21}`, `r = 3, …, 8`) whose initial packets have exact finite currents. Hence finite currents with nonpositive residual for **all increments `A_(N_k)` on these 30 sequences** suffice for Collatz: summing them with the initial current gives a current with nonpositive residual at every five-ray cutoff. This universal obligation is open ([`five-ray-annular-current-supply`](../../questions/five-ray-annular-current-supply.md)).

## Proof

From the legacy note `annular_recursion.md`, kept as written.

**The recursion.** For `8 | N`, both source cutoffs are even integers, `n_1(N) = 3N/2` and `n_2(N) = 3N/4`, and `n_i(64N) = 64·n_i(N)`. Recall the exact valuation representatives `q_a`, periods `M_a = 2^(a+1)`, endpoint progressions `e_a + 6t` and first lift indices of [`right-aligned-fixed-core-remainder`](../right-aligned-fixed-core-remainder/README.md). Their exact shift identities are

```
q_(a+6) = 64·q_a + 21,    M_(a+6) = 64·M_a,    e_(a+6) = e_a.
```

The source cutoff difference `n_i(N) − q_a` is odd. Its fractional quotient by the even integer `M_a` is at least `1/M_a`; consequently subtracting `21/(64·M_a)` cannot change its floor. This includes negative quotients. Therefore

```
floor((64·n_i(N) − q_(a+6)) / M_(a+6)) = floor((n_i(N) − q_a) / M_a).
```

The first lift index is unchanged, so the entire lift interval, its length modulo 3, and its right-aligned triple partition are unchanged. Corresponding sources satisfy `x' = 64x + 21`, hence `x' ≡ x (mod 3)`; their coefficients agree in each of the two components. Thus valuations `a + 6` at cutoff `64N` reproduce exactly valuation `a` at cutoff `N`. The valuation budget also shifts by exactly 6.

Only valuations `a = 1, …, 6` remain. At cutoff `64N` both source cutoffs are divisible by `3·M_a` for these six valuations. If `a` is odd, its lift count is divisible by 3 and there is no leftover. If `a` is even, its lift count is 2 modulo 3, and its two leftovers have endpoints 7 and 13. Summing both components, the leftover coefficient pairs for `a = 2, 4, 6` are `(−2, 1)`, `(1, −2)` and `(1, 1)`. They sum to zero. This proves `η_(64N) = η_N`, and `A_N` is exactly the total one-step pushforward supplied by valuations 1 through 6 at cutoff `64N`.

**The bands.** For an odd endpoint `y` not divisible by 3, valuation `a` contributes only when `x_a = (2^a·y − 1)/3` is an integer; equivalently `a` is odd for `y ≡ 5 (mod 6)` and even for `y ≡ 1 (mod 6)`. Its two cutoff conditions, on odd integer endpoints, are

```
y < 2^(7−a)·Q   (outer component),        y < 2^(6−a)·Q   (inner component).
```

The possible fractional `1/2^a` in solving the source inequality makes no difference: every displayed threshold is even and every endpoint is odd. Endpoints equal to 1 are discarded throughout.

For `1 < y < Q`, all three compatible valuations in `1, …, 6` occur in both components. Passing from `a` to `a + 2` replaces `x_a` by `4x_a + 1`, so the three source residues modulo 3 run through all three classes, and each component's coefficient sum is zero. For `y > 64Q` no valuation occurs. The new contribution is therefore confined to `(Q, 64Q)`.

In band `j`, put `k = 6 − j`. The outer component includes exactly the compatible valuations `a ≤ k`, and the inner component those `a ≤ k − 1`. Consequently

```
A_N(y) = Σ_(1 ≤ a ≤ k, 2^a·y ≡ 1 (3)) (3·1[x_a ≡ 2 (3)] − 1) + Σ_(1 ≤ a < k, 2^a·y ≡ 1 (3)) (3·1[x_a ≡ 1 (3)] − 1).
```

This depends only on `y mod 18` and evaluates to the table above. Every row has coefficient sum zero. Every band boundary is a multiple of 18, so each row's residues occur equally often; this proves zero mass for each band. The weighted residue sums are `(−18, −36, −18, 18, 36, 18)`; multiplying by the number `2^j·Q/18` of full 18-blocks proves the first-moment identity `63Q`. The row absolute sums are `(4, 8, 10, 10, 8, 4)` and the row support sizes `(3, 6, 5, 5, 6, 3)`. Since band `j` contains `2^j·N/8` complete blocks, their weighted sums give `99N/2` and `267N/8`. Zero signed mass makes the positive mass exactly half the absolute mass.

Finally a packet endpoint at cutoff `N` is at most `(3·n_1(N) + 1)/2 = Q + 1/2`. It is odd, while `Q` is even, so it is at most `Q − 1`. This proves disjointness. ∎

**The representative `V_N`.** The equality of the core remainders gives `A_N = P·V_N`; the three intervals follow from the definition of `ν_N` at `N` and `64N`. ∎

## Remarks

- **What the identity does not construct.** It gives the exact measure recursion `Π^R_(64^h·N) = Π^R_N + Σ_(r=0)^(h−1) A_(64^r·N)` (`h ≥ 1`), with pairwise disjoint annular supports. A certificate `J_N` and an exact annular certificate `K_N` with `A_N = (I − P)K_N` would give `J_(64N) = J_N + K_N`. The table does **not** supply `K_N`. Zero signed mass in each band does not control its unknown future ([`orbit-component-current-criterion`](../orbit-component-current-criterion/README.md)).
- **Norm and atom recursions.** Disjointness gives `‖Π^R_(64^h·N)‖₁ = ‖Π^R_N‖₁ + (11N/14)(64^h − 1)` and `|supp Π^R_(64^h·N)| = |supp Π^R_N| + (267N/(8·63))(64^h − 1)`, so the normalized limits along any such ray are `11/14` and `89/168`. These count the source measure; they are not bounds on the size or positive cost of a current.
- **No terminating induction.** The change of representative `A_N ↔ V_N` is reversible, but the new measure is not a smaller member of the same six-band family. In the finite-current quotient, with `U_t` the counting measure on odd states `1 < x ≤ t` and `F_t = U_(64t) − U_t`, the exact source transport identity gives `[A_N] = 3[F_N] − 3[F_(N/4)] − [F_(3N/2)] − [F_(3N/4)]` (brackets: equality modulo a finite signed divergence). This is the same expanding source-scale operator as the original problem: the term `F_(3N/2)` exceeds the source scale `N`. No contraction or finite termination follows from the recursion alone. The exact finite representative of this quotient, with its boundary flux, is in [`exposure-potential-boundary-flux`](../exposure-potential-boundary-flux/README.md).
- **Specific to `d = 1`.** The shift `q_(a+6) = 64·q_a + 21` uses the `3x+1` offsets; the PR1 lane notes that `T_61` has no exact `×64` recursion ([`locally-collatz-like-control-barrier`](../locally-collatz-like-control-barrier/README.md), NOTE §12.3).
- **Later work on `A_N`.** Partial currents: [`universal-annular-partial-current`](../universal-annular-partial-current/README.md), [`affine-common-tail-tree-lifting`](../affine-common-tail-tree-lifting/README.md); one-pass compression [`annular-root-collapse-contraction`](../annular-root-collapse-contraction.md); progress potential [`exposure-potential-boundary-flux`](../exposure-potential-boundary-flux/README.md).
- Novelty undetermined.

## History

- Migrated from `experiments/current_construction/recursive/annular_recursion.md` (legacy ID R6) at commit `be73a66`, by the B08 migration (Claude, Opus 5.5); the checker and receipt moved byte-identical with it. The corollary on the 30 sequences is from the legacy ledger entry R6 (`archive/docs/RESULTS.md`, legacy path) and the round report (now [`archive/convergence-current-construction/REPORT.md`](../../../../archive/convergence-current-construction/REPORT.md)). Legacy status: "written identity and finite arithmetic checks; no universal current constructor".
- Main lane (ChatGPT, Codex), 2026-10-17, commit `8d62dcc`. The round report records "independent model reviews" of the annular recursion; these were run by the main lane's own agents and are not counted as an independent review. Cross-checked on finite ranges by the PR1 lane the same day (ledger C1).
