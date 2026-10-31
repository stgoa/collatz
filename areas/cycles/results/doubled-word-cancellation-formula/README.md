---
id: doubled-word-cancellation-formula
kind: result
title: "The cancellation of a doubled word from a common factor of the half-intercepts, machine-checked"
status: formal
claim: >
  Raw odd-only clock, any 3x+q. Let w = (u, v) with |u| = |v| = n ≥ 1, S_v = S_u + 2j (j ≥ 0), S = S_u + j ≥ 1,
  Φ₁ = 2^S − 3^n, Φ₂ = 2^S + 3^n, and suppose Φ₁ = L·K, C_u = A·K and C_v = B·K for integers K, L, A, B. Then
  gcd(C_w, Φ₁) = |K|·gcd(2^j·A + B, L) (this needs neither S_v = S_u + 2j nor n ≥ 1),
  gcd(C_w, Φ₂) = gcd(2^j·A − B, Φ₂), and
  gcd(C_w, D_w) = |K|·gcd(2^j·A + B, L)·gcd(2^j·A − B, Φ₂); for K > 0,
  D_w = gcd(C_w, D_w)·(L/gcd(2^j·A + B, L))·(Φ₂/gcd(2^j·A − B, Φ₂)), i.e. the reduced denominator of w is
  (L/gcd(2^j·A + B, L))·(Φ₂/gcd(2^j·A − B, Φ₂)). Instance: if integers x_0, x_1, … follow w under the odd-only
  3x+q map (2^(a_i)·x_(i+1) = 3·x_i + q, letters read cyclically) with period |w|, q > 0, gcd(x_0, q) = 1,
  |w| ≥ 1 and Σw ≥ 1, then x_0·D_w = q·C_w, q | D_w, C_(R_r w) = x_r·(D_w/q), and for the rotation pair
  w' = (R_r w, R_s w): gcd(C_(w'), D_(w')) = (D_w/q)·gcd(x_r + x_s, q)·gcd(x_r − x_s, 2^(Σw) + 3^|w|).
  Proved in Lean (lean/LeanLane/RotationPairs.lean, lean/LeanLane/CycleEquation.lean) with the standard axioms
  only, for words with letters in ℕ.
authors:
  - Claude cycles lane (Fable 5.1; directed by Santiago Armstrong)
created: 2026-10-31
depends_on: [doubled-word-factor-gcd-identities]
lean:
  - LeanLane.RotationPairs.gcd_Phi1_of_common_factor
  - LeanLane.RotationPairs.gcd_Phi2_of_common_factor
  - LeanLane.RotationPairs.gcd_D_of_common_factor
  - LeanLane.RotationPairs.D_eq_gcd_mul
  - LeanLane.CycleEquation.follow_word
  - LeanLane.CycleEquation.IsCycle.cycle_eq
  - LeanLane.CycleEquation.IsCycle.cycle_eq_rotate
  - LeanLane.CycleEquation.IsCycle.q_dvd_D
  - LeanLane.CycleEquation.IsCycle.C_rotate_eq
  - LeanLane.CycleEquation.rotation_pair_gcd
evidence:
  - "../../../../lean/receipts/RotationPairs.build.txt, RotationPairs.axioms.txt, RotationPairs.sha256.txt and the same three CycleEquation.* files: build status, the #print axioms lines (standard axioms only) and the source hashes, produced on the pinned toolchain"
tags: [cycles, denominators, cancellation, doubled-words, lean]
---

# The cancellation of a doubled word from a common factor of the half-intercepts, machine-checked

## Statement

Notation of [`conventions/NOTATION.md`](../../../../conventions/NOTATION.md) §2 and of [`doubled-word-factor-gcd-identities`](../doubled-word-factor-gcd-identities/README.md): `w = (u, v)`, `|u| = |v| = n`, `S = S_u + j`, `Φ₁ = 2^S − 3^n`, `Φ₂ = 2^S + 3^n`. The gcd identities of that node say that `gcd(C_w, Φ₁)` and `gcd(C_w, Φ₂)` depend on `u`, `v` only through `2^j·C_u ± C_v`. When the half-intercepts share a factor `K` that divides `Φ₁`, the formulas close up:

**Theorem.** Suppose `Φ₁ = L·K`, `C_u = A·K`, `C_v = B·K` with `K, L, A, B ∈ Z`. Then

```
gcd(C_w, Φ₁) = |K| · gcd(2^j·A + B, L),                       (S ≥ 1)
gcd(C_w, Φ₂) = gcd(2^j·A − B, Φ₂),                            (S ≥ 1, n ≥ 1)
gcd(C_w, D_w) = |K| · gcd(2^j·A + B, L) · gcd(2^j·A − B, Φ₂),    (S_v = S_u + 2j, S ≥ 1, n ≥ 1)
```

and for `K > 0` the reduced denominator is `D_w / gcd(C_w, D_w) = (L / g₁) · (Φ₂ / g₂)` with `g₁ = gcd(2^j·A + B, L)`, `g₂ = gcd(2^j·A − B, Φ₂)`.

**The cycle equation and the rotation-pair instance.** Let `x : ℕ → Z` follow `w` under the odd-only `3x+q` map, `2^(a_i)·x_(i+1) = 3·x_i + q` with the letters read cyclically, and be `|w|`-periodic (an actual cycle of `3x+q` when the `x_i` are positive). Then `x_0·D_w = q·C_w`; the same holds for every rotation, `x_r·D_w = q·C_(R_r w)`; if `gcd(x_0, q) = 1` then `q | D_w` and `C_(R_r w) = x_r·(D_w/q)`; and for `q > 0`, `|w| ≥ 1`, `Σw ≥ 1`, the rotation pair `w' = (R_r w, R_s w)` has

```
gcd(C_(w'), D_(w')) = (D_w/q) · gcd(x_r + x_s, q) · gcd(x_r − x_s, 2^(Σw) + 3^|w|),
```

the theorem above with `K = D_w/q`, `L = q`, `A = x_r`, `B = x_s`, `j = 0`.

**Reading.** `C_u/Φ₁ = A/L` and `C_v/Φ₁ = B/L` are the periodic points `x_u`, `x_v` of the half-words written over the common denominator `L`; `K = Φ₁/L`. The sharpest choice is `K = gcd(C_u, C_v, Φ₁)`. The case that produced the counterexample to the half-cancellation conjecture is the rotation pair of an actual `3x+d` cycle: `K = gcd(C_u, D_u) = Φ₁/d`, `L = d`, `A = n_r`, `B = n_s` the two states, `j = 0`; see [`rotation-pair-words-exact-cancellation`](../rotation-pair-words-exact-cancellation/README.md).

## Proof

From [`doubled-word-factor-gcd-identities`](../doubled-word-factor-gcd-identities/README.md), `gcd(C_w, Φ₁) = gcd(2^j·C_u + C_v, Φ₁) = gcd(K·(2^j·A + B), K·L) = |K|·gcd(2^j·A + B, L)`, and `gcd(C_w, Φ₂) = gcd(2^j·C_u − C_v, Φ₂) = gcd(K·(2^j·A − B), Φ₂) = gcd(2^j·A − B, Φ₂)`, because `K | Φ₁` and `gcd(Φ₁, Φ₂) = 1` make `K` a unit modulo `Φ₂`. The product formula `gcd(C_w, D_w) = gcd(C_w, Φ₁)·gcd(C_w, Φ₂)` is the same node's. For the denominator, `D_w = Φ₁·Φ₂ = L·K·Φ₂`, and `g₁ | L`, `g₂ | Φ₂` give `L·K·Φ₂ = K·g₁·g₂·(L/g₁)·(Φ₂/g₂)`. For the cycle equation, induction on the word: if `2^a·x_1 = 3·x_0 + q` and `2^(Σw')·x_(|w'|+1) = 3^|w'|·x_1 + q·C_(w')` then `2^(a+Σw')·x_(|w|) = 3^|w'|·(3·x_0 + q) + q·2^a·C_(w') = 3^|w|·x_0 + q·C_w`; periodicity gives `x_|w| = x_0`. The shifted states follow the rotated word (the letter at position `i` of `R_r w` is the letter at `i + r` of `w`), and `D` is rotation invariant, so the equation holds for every rotation; `gcd(x_0, q) = 1` and `x_0·D_w = q·C_w` give `q | D_w`, then `C_(R_r w) = x_r·(D_w/q)` by cancelling `q`. The rotation-pair formula is the theorem applied to `(R_r w, R_s w)`. All of this is the two Lean files.

## Lean

[`lean/LeanLane/RotationPairs.lean`](../../../../lean/LeanLane/RotationPairs.lean), namespace `LeanLane.RotationPairs`, a module of the `LeanLane` library importing `LeanLane.Doubled`; standard axioms only (receipts `RotationPairs.*` in [`lean/receipts/`](../../../../lean/receipts/)). Words are `List ℕ`, intercepts in `ℤ`, `Int.gcd` the nonnegative gcd, `/` the integer division of `ℤ` (exact here).

| Claim | Declaration | Hypotheses |
|---|---|---|
| `gcd(C_w, Φ₁) = |K|·gcd(2^j A + B, L)` | `gcd_Phi1_of_common_factor` | `v.length = u.length`, `0 < u.sum + j`, `Phi1 (u.sum + j) u.length = L * K`, `C u = A * K`, `C v = B * K` |
| `gcd(C_w, Φ₂) = gcd(2^j A − B, Φ₂)` | `gcd_Phi2_of_common_factor` | the same and `0 < u.length` |
| `gcd(C_w, D_w) = |K|·g₁·g₂` | `gcd_D_of_common_factor` | the same and `v.sum = u.sum + 2 * j` |
| `D_w = gcd(C_w, D_w)·(L/g₁)·(Φ₂/g₂)` | `D_eq_gcd_mul` | the same and `0 < K` |

Helper: `gcd_K_Phi2` (`K | Φ₁ ⟹ gcd(K, Φ₂) = 1`).

[`lean/LeanLane/CycleEquation.lean`](../../../../lean/LeanLane/CycleEquation.lean), namespace `LeanLane.CycleEquation` (imports `LeanLane.RotationPairs`), the instance. `IsCycle q w x` is the structure with fields `step : ∀ i, 2 ^ (w.getD (i % w.length) 0) * x (i + 1) = 3 * x i + q` and `periodic : ∀ i, x (i + w.length) = x i`.

| Claim | Declaration | Statement |
|---|---|---|
| following a word | `follow_word` | `(∀ i < w.length, 2^(w.getD i 0) * x (i+1) = 3 * x i + q) → 2^w.sum * x w.length = 3^w.length * x 0 + q * C w` |
| `x_0·D_w = q·C_w` | `IsCycle.cycle_eq` | `IsCycle q w x → x 0 * D w = q * C w` |
| every rotation | `IsCycle.rotate`, `D_rotate`, `IsCycle.cycle_eq_rotate` | the shifted states follow `w.rotate r`; `D (w.rotate r) = D w`; `x r * D w = q * C (w.rotate r)` |
| `q | D_w`, `C_(R_r w) = x_r·(D_w/q)` | `IsCycle.q_dvd_D`, `IsCycle.C_rotate_eq` | with `Int.gcd (x 0) q = 1` (and `q ≠ 0` for the second) |
| the rotation pair | `rotation_pair_gcd` | `IsCycle q w x → 0 < q → Int.gcd (x 0) q = 1 → 0 < w.sum → 0 < w.length → (Int.gcd (C (w.rotate r ++ w.rotate s)) (D (w.rotate r ++ w.rotate s)) : ℤ) = |D w / q| * Int.gcd (x r + x s) q * Int.gcd (x r - x s) (Phi2 w.sum w.length)` |

`|D w / q|` is `D_w/q` itself when the states are positive (`D_w = q·C_w/x_0 > 0`); the Lean statement does not assume positivity of the states, hence the absolute value. Everything in the claim is formalised.

## Certificates

None: the content is the Lean module; `python3 tools/check_lean_receipts.py` checks the receipts' hashes against the source and the axiom lines.

## Remarks

- **Use.** With `K = gcd(C_u, C_v, Φ₁)` the formula computes `gcd(C_w, D_w)` from three gcds of numbers of the size of `Φ₁`; for the rotation pairs of actual cycles it expresses the cancellation through the cycle's states ([`rotation-pair-words-exact-cancellation`](../rotation-pair-words-exact-cancellation/README.md)). Nothing is said about `q = 1` cycles; the factor `gcd(2^j·A − B, Φ₂)` is the primitive part of [`primitive-cancellation-below-half`](../../questions/primitive-cancellation-below-half.md) when `gcd(A_w, m_w) = 2`.
- **Novelty.** Undetermined; the derivation is elementary.

## History

- Written and formalised 2026-10-31 by the Claude cycles lane (Fable 5.1), directed by Santiago Armstrong, while explaining the counterexample of [`half-cancellation-counterexample-rotation-pair`](../half-cancellation-counterexample-rotation-pair/README.md) through the two states that build it.
