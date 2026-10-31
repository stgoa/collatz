---
id: annular-root-collapse-contraction
kind: result
title: Collapsing 4x+1 chains to their roots contracts every annulus to 19/22 of its norm in one pass, but cannot be iterated
status: reviewed
claim: >
  Odd-only 3x+1 map, absorbing at 1. Let R send each odd state to the root of its F-chain, F(x) = 4x + 1
  (replace x by (x−1)/4 while x ≡ 5 mod 8), discarding root 1. For every finite measure μ, PRμ = Pμ, so
  μ = (I − P)(μ − Rμ) + Rμ is an explicit finite partial current, and ‖Rμ‖₁ = ‖Pμ‖₁. For the annulus A_N of
  disjoint-annular-recursion, for every N divisible by 8: ‖R A_N‖₁ = ‖P A_N‖₁ = 171N/4 − |c_N| ≤ (19/22)·‖A_N‖₁,
  where c_N is the signed annular mass of the chain rooted at 1 and |c_N| ≤ 3 (c_80000 = 0). R is idempotent and
  (R A_N)(p) = 2 at the 2N states 32Q < p < 64Q, p ≡ −1 mod 36, so the residual keeps positive mass at least
  4N: one pass, no iterated contraction theorem.
authors:
  - ChatGPT main lane (Codex)
created: 2026-10-17
depends_on: [disjoint-annular-recursion]
evidence:
  - "../exposure-potential-boundary-flux/check_duality.py (a certificate of that node; exits 0 at its new path): independently checks the 19/22 collapse formula at nine cutoffs by grouping actual F-chains and separately pushing the source, including absorption of the root-1 class and the 2N surviving positive outer atoms"
  - "../universal-annular-partial-current/check_arithmetic_reductions.py, arithmetic_audit.json: the legacy checker of the norm formula at 66 cutoffs and of c_80000 = 0. Fails at its new path (it loads experiments/current_construction/recursive/check_annular_recursion.py by its legacy path); passed at be73a66 inside scripts/verify_all.py (archive/legacy-checker-run-be73a66.md)"
  - "../locally-collatz-like-control-barrier/progress_measures_audit.py, progress_measures_audit.json: the PR1 lane's independent check (a certificate of that node)"
reviewed_by:
  - by: Claude PR1 lane (Opus)
    date: 2026-10-17
    link: ../progress-measures-control-3x-61.md
    scope: "Finite only (ledger C1/C4, NOTE §11): with independent code, ‖P A_N‖₁ = ‖R A_N‖₁ = 171N/4 − |c_N| at 68 cutoffs N ≤ 4096, (R A_N)(p) = 2 at the 2N survivors p ≡ −1 mod 36 in (32Q, 64Q), and c_80000 = 0 by an independent point evaluator. The written entry-profile proof was not re-derived, so the status stays written"
  - by: Claude review lane (Fable 5.1; directed by Santiago Armstrong)
    date: 2026-10-31
    link: REVIEW-2026-10-31-claude-review-lane.md
    scope: "Full re-derivation of the algebra (PR = P, the root-successor bijection), the entry-profile table, the period sums and 171N/4, |c_N| <= 3 and the 2N survivors, with independent code at 131 cutoffs (8 | N <= 1024, 2048, 4096, 6144) and c_80000 = 0; evidence scripts re-run (check_duality.py, progress_measures_audit.py, the legacy check_arithmetic_reductions.py replay; all exit 0); the algebra checked d-uniform on 3x+5 and 3x+13; verdict HOLDS"
aliases: [R9]
tags: [convergence, packet-currents, annular, compression, norm-contraction]
---

# Collapsing 4x+1 chains to their roots contracts every annulus to 19/22 of its norm in one pass, but cannot be iterated

## Statement

Odd-only clock, absorbing at 1; `A_N`, `Q = 9N/4` and the six bands as in [`disjoint-annular-recursion`](../disjoint-annular-recursion/README.md). Define `F(x) = 4x + 1`. Then `S(F(x)) = S(x)` on positive odd states. Every odd state belongs to a unique `F`-chain rooted at a state `ρ(x)` with first valuation 1 or 2: repeatedly replace `x` by `(x − 1)/4` while `x ≡ 5 (mod 8)`. Let `Rμ` sum the coefficients of `μ` at these roots, discarding root 1.

**Theorem.** For every finite measure `μ`, `PRμ = Pμ` and

```
J_F = μ − Rμ,     μ = (I − P)J_F + Rμ,     ‖Rμ‖₁ = ‖Pμ‖₁.
```

For every `N` divisible by 8,

```
‖R A_N‖₁ = ‖P A_N‖₁ = 171N/4 − |c_N| ≤ (19/22)·‖A_N‖₁,     |c_N| ≤ 3,
```

where `c_N` is the signed mass of the unique `F`-chain rooted at 1, before absorption. The correction can vanish: `c_80000 = 0`.

**Where positive mass remains.** For every `32Q < p < 64Q` with `p ≡ −1 (mod 36)`, `ρ(p) = p`, the annular coefficient is 2, and `F(p) > 64Q`; thus `(R A_N)(p) = 2`. There are `2N` such states, so the residual `R A_N` has positive mass at least `4N`.

## Proof

From §2 of the legacy note `ARITHMETIC_RESULTS.md` (now [`universal-annular-partial-current`](../universal-annular-partial-current/README.md)), kept as written.

Each replacement `x → (x − 1)/4` decreases the positive integer, so the root procedure terminates. Because `PRμ = Pμ`, the identity `μ = (I − P)(μ − Rμ) + Rμ` is an exact finite partial current. Different roots have different successors: a successor `y ≡ 2 (mod 3)` has root `(2y − 1)/3`, and one with `y ≡ 1 (mod 3)` has root `(4y − 1)/3`. Hence `‖Rμ‖₁ = ‖Pμ‖₁`.

**Finite residue profiles.** Write `f_j(r)` for annular row `j`, with zero coefficients on odd multiples of 3. The first annular point in each `F`-chain is its entry. Entries in bands 0 and 1 are all odd states in those bands. Entries in bands 2 through 5 are exactly the states not `≡ 5 (mod 8)`; otherwise the previous `F`-point would still be in the annulus. If an entry is in band `j`, its successive annular points are in bands `j, j+2, …, 5`. The sum along this chain is

```
g_j(x) = Σ_(0 ≤ k ≤ (5−j)/2) f_(j+2k)(F^k(x) mod 18).
```

The resulting period-18 table, including the odd multiples of 3:

| j / r | 1 | 3 | 5 | 7 | 9 | 11 | 13 | 15 | 17 |
|---|--:|--:|--:|--:|--:|---:|---:|---:|---:|
| 0 | 0 | 1 | 2 | 3 | 1 | -1 | -3 | -2 | -1 |
| 1 | -1 | 3 | 1 | 2 | 0 | 1 | -1 | -3 | -2 |
| 2 | 1 | 2 | -1 | -2 | -1 | 2 | 1 | -1 | -1 |
| 3 | 0 | 0 | -3 | -3 | 0 | 3 | 3 | 0 | 0 |
| 4 | -1 | 0 | -2 | -1 | 0 | 1 | 2 | 0 | 1 |
| 5 | 0 | 0 | -1 | 0 | 0 | -1 | 0 | 0 | 2 |

The absolute sums in one period are 14 and 14 for bands 0 and 1. In bands 2 through 5 the entry condition introduces modulus 8; in each complete period of length 72 the absolute sums are 36, 36, 24, 12. Those four band lengths and boundaries are multiples of 72. Since band `j` has length `2^j·Q`, the six exact norm contributions are `N·(7/4, 7/2, 9/2, 9, 12, 12)`, which sum to `171N/4`. Killing the class rooted at 1 subtracts `|c_N|`. This class has an entry in band 0 or 1 and three annular points, so the first two rows of the table prove `|c_N| ≤ 3`. To compute it, start at 1, iterate `F` until first exceeding `Q`, and add its three annular coefficients; the arithmetic formula gives `c_80000 = 0`. Finally `(171N/4)/(99N/2) = 19/22`.

**Survivors.** The legacy note states these facts without further argument; they are direct: `p ≡ −1 (mod 36)` gives `p ≡ 17 (mod 18)`, where the top-band coefficient is 2, and `p ≡ 3 (mod 4)`, so `p ≢ 5 (mod 8)` is its own root and no smaller chain point is annular; `F(p) = 4p + 1 > 64Q` leaves the annulus. The interval `(32Q, 64Q)` has length `32Q = 72N`, a multiple of 36, so it holds exactly `2N` such states. ∎

## Remarks

- **One pass only.** `R` is idempotent, so a second pass does nothing, and its residual is not another annulus. The contraction cannot be applied repeatedly as stated. The `4N` survivors rule out completing the construction with `F`-coalescence diamonds alone: such diamonds preserve `Pμ`, whereas a nonpositive residual would have nonpositive pushforward, and `P A_N` has the corresponding positive atoms. The obstruction allows combinations with further forward transport, larger affine identities, or cross-time intersections. Literal forward transport has its own closure obstruction: [`outer-profile-closure-obstruction`](../outer-profile-closure-obstruction/README.md).
- **Not evidence of progress.** On the false analogue `3x+61`, whose packet obligation fails, the same one-pass ratio is 0.849–0.863 ([`progress-measures-control-3x-61`](../progress-measures-control-3x-61.md)). A one-pass contraction near `19/22` therefore says nothing about whether every positive plateau of `3x+1` ends.
- The root-transport normal form [`root-transport-normal-form`](../root-transport-normal-form/README.md) (legacy R12) builds on `R`: `R² = R`, `PR = P`, explicit top-band atoms survive any bounded number of transports, and at `N = 96` the contraction fails on the next step (`3533 → 3124`).
- Novelty undetermined.

## History

- Migrated from `experiments/annular_construction/arithmetic/ARITHMETIC_RESULTS.md` §2 (legacy ID R9) at commit `be73a66`, by the B08 migration (Claude, Opus 5.5). Legacy status: "written identity and finite arithmetic checks. No iterated contraction theorem".
- Main lane (ChatGPT, Codex), 2026-10-17, commit `ce56699`. The round report records "independent model reviews" of the norm proof by the main lane's own agents (not counted as independent). Cross-checked on finite ranges by the PR1 lane the same day.
- 2026-10-31: reviewed by the Claude review lane (Fable 5.1; directed by Santiago Armstrong); status raised to reviewed. No corrections. For the review the node was moved from the single file `annular-root-collapse-contraction.md` into this folder; every relative link in it gained one `../`, and the incoming links in `disjoint-annular-recursion`, `universal-annular-partial-current`, `exposure-potential-boundary-flux`, `root-transport-normal-form`, `outer-profile-closure-obstruction`, `progress-measures-control-3x-61`, `right-aligned-reduction-independent-checks`, the questions `packet-current-supply` and `five-ray-annular-current-supply`, the area `OVERVIEW.md` and `papers/right-aligned-reduction/README.md` were repointed; `MAP.md` is regenerated. Review: [`REVIEW-2026-10-31-claude-review-lane.md`](REVIEW-2026-10-31-claude-review-lane.md).
