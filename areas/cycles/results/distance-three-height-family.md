---
id: distance-three-height-family
kind: result
title: Rotation distance three, q ≤ L and vanishing drift do not bound the height of a cycle
status: reviewed
claim: >
  Raw odd-only clock. For integer pairs (a, b) with δ_0 = a·log 2 − b·log 3 > 0, δ_0 → 0, b → ∞, put
  u = 2b + 2 − a, v = a − b − 3 (eventually positive), U = 1^u 2^v and w = (3, U, 4, U, 5, U), so m = 3b,
  A = 3a. Each w is primitive with minimum nonidentity rotation distance exactly 3 and gives a
  primitive positive 3x+q cycle at its reduced q, with δ_0·(L/q) → 5/6, (H/L)/(3/2)^u → 2 and
  B/m → (2 − log₂3)·log₂(3/2)/3 > 0. Choosing the pairs from upper convergents of log₂3 suitably
  gives L/q = Θ(m), q ≤ L eventually, and B = Θ(m) at ρ = 3. Hence no bound B = O(s + log m),
  B = O(s + log(L/q)) or H ≤ q·poly(m) follows from overlap, exact arrows, q ≤ L and small positive
  drift at bounded rotation distance. In this family q → ∞ (liminf (log q)/b > 0), so it is no
  counterexample at fixed q or at q = 1.
authors:
  - ChatGPT main lane (Codex)
created: 2026-10-19
depends_on: [paired-state-run-law]
evidence:
  - "shared-background-denominator-law/OVERLAP_THEORY.md, sections 3-6: the written proof and the finite controls (a, b) = (27, 17), (65, 41), (485, 306)"
  - "shared-background-denominator-law/overlap_audit.json: exact checks of (11), (15), (16) on the three controls (historical receipt; its checker no longer runs at the new path)"
reviewed_by:
  - by: Claude Lean lane (Fable)
    date: 2026-10-19
    scope: "Feed 2026-10-19 05:03: OVERLAP_THEORY.md sections 1-3 read in full, no error; the run law and the ρ = 3 height family re-derived by hand"
tags: [cycles, rotation-distance, height, counterexample]
---

# Rotation distance three, q ≤ L and vanishing drift do not bound the height of a cycle

## Statement

Let `(a, b)` range over integer pairs with `δ_0 = a·log 2 − b·log 3 > 0`, `δ_0 → 0`, `b → ∞`, `a/b → log₂3`. Eventually `u = 2b + 2 − a` and `v = a − b − 3` are positive. Define

```
U = 1^u 2^v,     w = (3, U, 4, U, 5, U),     m = 3b,     A = 3a.          (8)
```

1. The markers 3, 4, 5 occur once each, so `w` is primitive and every nonidentity rotation mismatches at all three marker positions; rotation by `b` has exactly those three. So `ρ(w) = 3` (9). Since `2^A > 3^m`, `w` gives a positive rational cycle at additive parameter 1, and dividing the rotated intercepts by their gcd with `D` gives a primitive positive odd `3x+q` cycle (an actual-cycle construction, not a fractional state read as an integer).
2. With `r = 3^b/2^a = e^(−δ_0)`, exact affine composition gives the states `X0, X1, X2` before the markers 3, 4, 5 in closed form (11), and

```
δ_0·(L/q) → 5/6,    (H/L)/(3/2)^u → 2,                                     (13)
B/m → ((2 − log₂3)·log₂(3/2))/3 > 0.                                       (14)
```

3. Finite exact bounds (for `r ≥ 1/2`, `u, v ≥ 1`): `L/q > 27/[256(1 − r^3)]` (15) and `H/L > (3/2)^u` (16); in integers, with `P = 3^b`, `Q = 2^a`: `256·L·(Q^3 − P^3) > 27·q·Q^3` and `H·2^u > L·3^u`. The pairs `(27, 17)`, `(65, 41)`, `(485, 306)` are in the domain.
4. **Linear minimum with linear height.** From upper convergents `(a_0, b_0)` of `log₂3` with error `δ_00 < (log 2)/b_0`, take `k = ceil((b_0·δ_00)^(−1/2))`, `a = k·a_0`, `b = k·b_0`; then `1 ≤ b·δ_0 < (1 + √(log 2))² < 4`, and (13)–(14) give `L/q = Θ(m)`, `ρ(w) = 3`, `B = Θ(m)` (17). (`a, b` need not be coprime; unique markers give primitivity.)
5. **Denominators grow.** The run law at rotation `b` gives `q·((H − L)/q) ≥ 2·3^(b−1)`, and with (13), `δ_0 = Θ(1/b)`, `u = (2 − log₂3)·b + o(b)`: `liminf (log q)/b ≥ log 3 − (2 − log₂3)·log(3/2) > 0`.

## Proof

[`OVERLAP_THEORY.md`](shared-background-denominator-law/OVERLAP_THEORY.md) §§3–5. With `f_k(x) = (3x+1)/2^k`: `f_1^u(x) = (3/2)^u·(x + 1) − 1` and `f_2^v(y) = (3/4)^v·(y − 1) + 1`, so `U` acts by `F_U(x) = λx + β` with `τ = (3/4)^v`, `λ = (16/3)·r`, `β = λ + 1 − 2τ`. With `b_k = β + λ/2^k`, marker `k` followed by `U` acts by `2r·x + b_3`, `r·x + b_4`, `(r/2)·x + b_5` (10), so `X1 = 2r·X0 + b_3`, `X2 = r·X1 + b_4`, `X0 = (r/2)·X2 + b_5`, `X0 = T/(1 − r^3)` with `T = (r²/2)·b_3 + (r/2)·b_4 + b_5` (11), exactly. For `r ≥ 1/2`, `λ > 1`, every marker step strictly reduces its input, the one-run increases and the two-run moves monotonically toward 1, so the block minimum is the state right after the marker: `L/q = min((3X0 + 1)/8, (3X1 + 1)/16, (3X2 + 1)/32)` (12). In the limit `λ → 16/3`, `β → 19/3`, `(b_3, b_4, b_5) → (7, 20/3, 13/2)`, `T → 40/3`, `X1/X0 → 2`, `X2/X0 → 2`; the third entry of (12) is eventually the minimum, and the maximum sits at the end of a one-run of length `u`, which gives (13)–(14). The bounds (15)–(16) use `β ≥ 13/6`, `b_5 ≥ 9/4`, `T ≥ 9/4`, `X1 ≥ X0`, `X2 ≥ X0/2`.

## Remarks

- **What it refutes.** A uniform polynomial conversion from normalised minimum to height (e.g. `B = O(s + log m)` or `H ≤ q·poly(m)`) based only on actual overlap, positive exact arrows, `q ≤ L` and small positive drift at bounded rotation distance. So the height term of [`paired-state-run-law`](paired-state-run-law.md) cannot be dropped.
- **What it does not refute.** A height bound that also uses arithmetic at fixed `q` or at `q = 1`; here `q → ∞`. It is not presented as a new fixed-family exclusion.
- **Correction recorded in the side feed.** The side lane's S05 entry ([`mismatch-height-tradeoff`](mismatch-height-tradeoff/README.md)) first called its general-`q` chain "sharp in the exponent" on this family, using `log₂ q ≳ 0.447m`; corrected at 13:29 the same day (a correction first raised by the Lean lane): `0.447m` is the lower bound of part 5, while the family's actual denominators are about `D`.
- **Novelty.** None claimed.

## History

- Split from `experiments/cycle_spectrum/C013/` (legacy ID `C013`; `OVERLAP_THEORY.md` §§3–6) at commit `be73a66`, by the B04 migration (Claude, Opus 5.5). Main lane (ChatGPT/Codex), 2026-10-19.
