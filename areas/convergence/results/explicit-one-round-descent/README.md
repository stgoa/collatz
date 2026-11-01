---
id: explicit-one-round-descent
kind: result
title: One round of explicit Syracuse descent outside an explicitly counted exceptional set
status: reviewed
claim: >
  Odd-only clock; any positive odd d, S_d(N) = (3N+d)/2^v2(3N+d); odd N, n >= 1, w = (a_1, ..., a_n) the word of N, A = a_1 +
  ... + a_n. Then S_d^n(N) = 3^n N/2^A + d C_w/2^A with 0 < C_w/2^A <= (3/2)^n - 1, C_w = sum_(j<n)
  3^(n-1-j) 2^(a_1+...+a_j). Hence, for 1 < theta < 2 and every integer X >= 1, every odd N <= X outside the
  exceptional set {A_n(N) <= theta n}, whose size is at most (X/2) exp(-n I(theta)) + C(floor(theta n), n) by
  explicit-valuation-large-deviations, satisfies S_d^n(N) < N (3/2^theta)^n + d (3/2)^n; the factor 3/2^theta is
  below 1 exactly when theta > log2 3. One round only: the statement does not iterate. No novelty claim, no
  convergence claim.
authors:
  - Claude explicit-Tao lane (Opus)
created: 2026-10-18
depends_on: [explicit-valuation-large-deviations]
evidence:
  - "../explicit-valuation-large-deviations/check_L2.py (a certificate of that node) checks this node too: its check 3 verifies the affine formula and 0 < C_w/2^A <= (3/2)^n - 1 exactly for 20,000 random odd N < 2^64, n <= 40, and the falsity of the discarded multiplicative form (counterexample word (10, 1), C_w = 1027 > 9); its check 4 counts descent violations off the exceptional set at X = 2^20, n in {6, 8, 10}, theta in {1.6, 1.7, 1.8}, d in {1, 5} (none); its check 5 writes the trade-off table quoted below, in receipts/L2_receipt.json"
  - "../explicit-valuation-large-deviations/fable_L2_check.py: the side lane's independent probe, which re-checks the affine identity with the d C_w term, the bound on C_w/2^A and the descent inequality on 4,000 random odd N < 2^64, n <= 40, d in {1, 5} (feed 2026-10-18 19:36; a finite re-check)"
reviewed_by:
  - by: Claude review lane (Fable 5.1; directed by Santiago Armstrong)
    date: 2026-10-31
    link: REVIEW-2026-10-31-claude-review-lane.md
    scope: "Re-derived (5) and (6) with the sharpness case, recomputed the exceptional-set counts at X = 2^20 three ways (brute force, exact cylinder formula, receipt) and the trade-off numbers, tested (6) on 3x+5, 3x+7, 3x+13, 3x+61 and all eleven raw cycles of the fixtures; check_L2.py and fable_L2_check.py re-run (exit 0, receipts identical); verdict HOLDS WITH CORRECTIONS (scope narrowed to positive odd d, which the proof uses)"
aliases: [TAO-L3]
tags: [convergence, explicit-tao, descent, stopping-time, calibration, explicit-constants]
---

# One round of explicit Syracuse descent outside an explicitly counted exceptional set

## Statement

Notation of [`explicit-valuation-large-deviations`](../explicit-valuation-large-deviations/README.md): odd-only clock, `S = S_1`, `A_j = a_1+…+a_j`, `A = A_n`, `C_w = Σ_(j=0)^(n−1) 3^(n−1−j) 2^(A_j)`, `A_0 = 0`, and `I(θ)` the rate function (3) there.

**Lemma L3.** For odd `N`, `n >= 1` and the word `w` of `N`,

```
S^n(N) = 3^n N / 2^A + C_w / 2^A,     0 < C_w / 2^A <= (3/2)^n − 1.      (5)
```

Hence, for `1 < θ < 2`, every odd `N <= X` outside the exceptional set counted in (4) of [`explicit-valuation-large-deviations`](../explicit-valuation-large-deviations/README.md) with `t = θn` satisfies

```
S^n(N) < N (3/2^θ)^n + (3/2)^n,                                       (6)
```

a decrease by the factor `(3/2^θ)^n` up to an additive term that is of lower order whenever `(3/2)^n << N (3/2^θ)^n`, i.e. `2^((θ−1)n) << N`; with `n = κ log_2 N` this holds as soon as `(θ−1)κ < 1 + κ log_2(3/2^θ)`, which is the case throughout the trade-off table below. The factor is a genuine contraction once `2^θ > 3`, i.e. `θ > log_2 3 = 1.58496…`.

**For `3x+d`.** For `S_d` with positive odd `d` the affine formula reads `S_d^n(N) = (3^n N + d C_w)/2^A`, so (5)–(6) hold with the additive term multiplied by `d`: `S_d^n(N) < N (3/2^θ)^n + d (3/2)^n`.

## Proof

In the affine formula, every later valuation is at least 1, so `A − A_j >= n − j` for `j <= n−1`, hence `2^(A_j − A) <= 2^(−(n−j))` and `C_w/2^A <= Σ_(j=0)^(n−1) 3^(n−1−j) 2^(−(n−j)) = (1/2) Σ_(i=0)^(n−1) (3/2)^i = (3/2)^n − 1`. For (6), `A > θn` gives `3^n/2^A < (3/2^θ)^n`. ∎

## Certificates

None in this folder. The finite checks of (5) and (6) are run by the certificate `check_L2.py` of [`explicit-valuation-large-deviations`](../explicit-valuation-large-deviations/README.md) (checks 3–5; see `evidence`), and re-checked independently by the side-lane probe beside it.

## Remarks

- **The trade-off.** With `θ` between `log_2 3` and 2 there is a trade-off between the descent factor `3/2^θ` per step and the rate `I(θ)`; the receipt tabulates it. One round from scale `X` with `n = ⌊κ log_2 X⌋` leaves an exceptional fraction `<= X^(−κ I(θ)/ln 2) + 2C(⌊θn⌋,n)/X` and lands below `X (3/2^θ)^n + (3/2)^n`. For example (receipt `trade-off table`, at the largest `κ` allowed by the boundary term): `θ = 1.6` gives factor `0.9896` per step, `κ_max = 0.655`, exceptional exponent `0.048` and landing exponent `0.990`; `θ = 1.8` gives factor `0.8615`, `κ_max = 0.561`, exceptional exponent `0.0090` and landing exponent `0.879`. These are Terras/Everett/Korec-type statements with every constant explicit.
- **It does not iterate.** The landing points of one round are not uniformly distributed in residue classes, and the repository's own barriers ([`arbitrary-target-linear-transport-barrier`](../arbitrary-target-linear-transport-barrier/README.md), [`growth-norm-transport-barrier`](../growth-norm-transport-barrier/README.md); legacy P6-002/P6-003) show that arbitrary-target iteration fails. Tao's mixing of the Syracuse random variables (legacy L4) is what licenses iteration; its constants were the open problem of the explicit-Tao programme ([`explicit-tao-almost-all-constants`](../../attempts/explicit-tao-almost-all-constants.md)), which stopped at [`tao-printed-window-vacuity`](../tao-printed-window-vacuity/README.md).
- **d-control.** The statement holds for every positive odd `d` with the additive term scaled by `d`; the checker repeats the integer counts and the descent test for `d = 5` with that factor. The `d`-specific input of the explicit-Tao programme is the verified range alone (legacy L7).
- No novelty claim; no convergence claim.

## History

- Migrated from the L3 part of `experiments/explicit_tao/lemmas/L2_valuation_tail.md` (legacy ID `L3`, alias `TAO-L3`) at commit `be73a66`; the L2 part is [`explicit-valuation-large-deviations`](../explicit-valuation-large-deviations/README.md), which keeps the shared checker.
- Written by the Claude explicit-Tao lane (branch `claude/explicit-tao`), iteration 1, 2026-10-18.
- *Correction record (before any commit).* The first draft of this lemma claimed the multiplicative form `S^n(N) <= 3^n (N+1)/2^A`, i.e. `C_w <= 3^n`. That is false: the word `(10, 1)` has `C_w = 3 + 2^10 = 1027 > 9`. The checker's exact test rejected it before anything was committed; the additive form (5) is the correct Terras-type statement.
- 2026-10-31: reviewed by the Claude review lane (Fable 5.1; directed by Santiago Armstrong); status raised to reviewed. Corrections: "any odd `d`" became "any positive odd `d`" in the claim, in the Statement paragraph "For `3x+d`" and in the Remark "d-control": the `3x+d` step scales `0 < C_w/2^A ≤ (3/2)^n − 1` by `d` and needs `d > 0`; for `d < 0` the inequality (6) as written fails (`d = −1`, `N = 3`, `n = 3`, `θ = 1.6`), while the count (4) is unaffected. For the review the node was moved from the single file `explicit-one-round-descent.md` into this folder; every relative link in it gained one `../`, and the incoming links in `explicit-valuation-large-deviations`, the attempt `explicit-tao-almost-all-constants`, the question `explicit-almost-all-descent-threshold`, the source `terras-1976-stopping-time` and the area `OVERVIEW.md` were repointed; `MAP.md` is regenerated. Review: [`REVIEW-2026-10-31-claude-review-lane.md`](REVIEW-2026-10-31-claude-review-lane.md).
