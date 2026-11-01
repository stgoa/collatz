# Review of four-target-history-classification

Independent review of [`README.md`](README.md) (authors: ChatGPT main lane, Codex). Scope as in the node: odd-only `3x+1`, absorbing at 1, `T = νS` with the inverse table of [`elementary-bridge-quotient-normal-form`](../elementary-bridge-quotient-normal-form/README.md). Own scripts (own `ν`, `T`, canonical test and inverse table, validated by brute force as described in my review of [`high-smaller-origin-history`](../high-smaller-origin-history/README.md)) live outside the repository; every number below comes from them or from the certificates.

## What I checked

- **Certificates.** `python3 tools/run_certificates.py --node four-target-history-classification`: `check_history_cell_recompute.py` PASS (7 s) and `check_legacy_replay.py` PASS (5 s), exit 0, 13 s wall in all (concurrent with other nodes). The receipt holds trees of 64/78/89/101 states, 28 lifts, 3 full comparisons, 1024 canonical checks and 20 rejections, as `evidence` says.
- **Cell arithmetic (§1)** for twelve `m` (0, 1, 2, 7, 26, `3^19`, `2^64`, five random below `2^90`): `Q = 11547 + 3·2^19(85 + 16384m)`; `v < Q < n` with `Q − v = 5058166 + 974892480m`; `b ≡ 9 (mod 16)`, `v ≡ 37 (mod 64)`; `Q`, `n` canonical, `n` a complementary climber with `v2(n+1) = 4`, `r = 2n + 1` selected with exponent 5 and `ν(r) = n`.
- **Word (1) and the quotient path.** The word is exact for every tested `m`, total 26, `2^27 | QP`, and each ordinary state equals its `m = 0` value plus `3^(j+1)·2^(33−A_j) m`. For the quotient path I ran my own affine normalisation over the whole cell, carrying `(base, period)` and requiring every exact valuation, F-root and selected/complementary decision to be fixed by the period: it reaches `(N0, NP)` after 18 steps, so `T^18(Q(m)) = n(m)` for all `m`, and its `m = 0` states are the listed path. Normalisations occur at step 13 (`813174967 → 406587483`, a selected halving) and step 18 (`r → n`).
- **(2)-(3).** `S^23(Q) = S^5(n) = S^5(r)` (halving identity with `a = 5`); the rows `L_23(Q) − L_5(n)` have divergence `[Q] − [n]`, `N_r = L_5(r) − L_5(n)` has `[r] − [n]`, and `L_18(Q) + N_r = L_23(Q) − L_5(n)` row for row.
- **Targets (5).** `y_a = T^a(n) = 3^a(n+1)/2^a − 1`, canonical for `a ≤ 3` (`y_0, y_1, y_2` complementary with valuation-one steps, `y_3 ≡ 1 (mod 8)`); `NP_a = 2^(6−a) 3^(19+a)`, `v3 = 19 + a` exactly.
- **Cutoff (7)-(9), re-derived.** `λ ≥ (c+1)/(Y+1)` by induction: `α(c+1) ≥ αc + β + 1` is `α − β ≥ 1`, preserved along rays since `64(α − β) − 49 ≥ 15`. `C(m)` increases (`QP(N0+1) − (Q0+1)NP > 0`), `C(0) = Q0 + 1`, `C_∞ = Q0 + 2 + 1226171/387420489 < Q0 + 3`; `c` odd gives `c ≤ Q0`. The lift to the anchor is legal because `3^(19+a) | NP_a m` (only divisibility by 3 matters).
- **Trees (§4).** My own enumeration with bound (11) retains 64, 78, 89, 101 nodes for `a = 0..3`, each with the single origin `Q0` at depth `18 + a`, multiplier `2^(27+a)/3^(18+a)`, and `λ·NP_a = QP`, so the lifted origin is `Q(m)`. Independently of the lifting argument, the same search run directly at `m ∈ {1, 2, 10, 12345, 2^40 + 1}` with threshold `Q(m)` finds only `Q(m)` at depth `18 + a` (same node counts).
- **Exhaustive forward sweep** (own C program, own `ν`): all 33,426,247 canonical `p ≤ Q0` iterated 22 quotient steps; exactly four hits on the `y_a` within `19 + a` steps, all `p = Q0` at depths 18-21; 6.9 s. (The side lane's 33,426,246 starts at `p = 3`.)
- **§5.** A word legal at every `m` has `3^d | 2^E·NP_a`, so `d ≤ 19 + a`; the ordinary exclusions follow from `Tν = νS`, `ν(p) ≤ p` and `ν(r) = n`.
- **Controls** ([`NOTATION.md`](../../../../conventions/NOTATION.md) §3). The finite trees are `3x+1` computations; the lifting is `d`-uniform arithmetic of exact words (checked on the actual `3x+d` cycles in my review of [`fixed-word-history-cells`](../fixed-word-history-cells/README.md)); the absorbing hypothesis behind "unique path" is what `3x+d` cycles break (my review of [`finite-anchor-history-classification`](../finite-anchor-history-classification/README.md)). No `3x+d` cycle is excluded.

## What I did not check

- The conditional identity (4) beyond its divergence bookkeeping (no `H_v`, `H_b` are supplied); the receipt's third full comparison (`m = 2^64`) and the 20 rejection controls; `history_cell_scope.py` line by line.
- [`later-target-twenty-step-descent`](../later-target-twenty-step-descent/README.md) and [`failed-w9-leader-reduction`](../failed-w9-leader-reduction/README.md), used only to name the cell.

## Findings

1. **§1 (imprecision).** The displayed 19 states are the quotient path, but they follow the sentence about the 18-arrow ordinary word as if both visited the same states. They do not: `S^13(Q) = 813174967` is selected and `T^13(Q) = 406587483`; the ordinary states at steps 13-15 differ from the quotient states and re-merge at step 16 by `S³(813174967) = S³(406587483)`. Both clocks in (2) are right; the equal lengths 18 and 18 are a coincidence of the identities, not an identity of paths.
2. **§3 (imprecision).** "the actual-anchor difference is even and divisible by 3": only divisibility by 3 is used (branch legality depends on the residue modulo 3); evenness is irrelevant.
3. **`evidence` (typo).** `33,426,246` counts canonical states from `p = 3`; with `p = 1` the count is 33,426,247.

## Verdict

HOLDS.

Claude review lane (Fable 5.1; directed by Santiago Armstrong), 2026-10-31
