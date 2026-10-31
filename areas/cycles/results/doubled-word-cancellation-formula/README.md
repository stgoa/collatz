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
  (L/gcd(2^j·A + B, L))·(Φ₂/gcd(2^j·A − B, Φ₂)). Proved in Lean (lean/LeanLane/RotationPairs.lean) with the
  standard axioms only, for words with letters in ℕ.
authors:
  - Claude cycles lane (Fable 5.1; directed by Santiago Armstrong)
created: 2026-10-31
depends_on: [doubled-word-factor-gcd-identities]
lean:
  - LeanLane.RotationPairs.gcd_Phi1_of_common_factor
  - LeanLane.RotationPairs.gcd_Phi2_of_common_factor
  - LeanLane.RotationPairs.gcd_D_of_common_factor
  - LeanLane.RotationPairs.D_eq_gcd_mul
evidence:
  - "../../../../lean/receipts/RotationPairs.build.txt, RotationPairs.axioms.txt, RotationPairs.sha256.txt: build status, the #print axioms lines (standard axioms only) and the source hash, produced on the pinned toolchain"
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

**Reading.** `C_u/Φ₁ = A/L` and `C_v/Φ₁ = B/L` are the periodic points `x_u`, `x_v` of the half-words written over the common denominator `L`; `K = Φ₁/L`. The sharpest choice is `K = gcd(C_u, C_v, Φ₁)`. The case that produced the counterexample to the half-cancellation conjecture is the rotation pair of an actual `3x+d` cycle: `K = gcd(C_u, D_u) = Φ₁/d`, `L = d`, `A = n_r`, `B = n_s` the two states, `j = 0`; see [`rotation-pair-words-exact-cancellation`](../rotation-pair-words-exact-cancellation/README.md).

## Proof

From [`doubled-word-factor-gcd-identities`](../doubled-word-factor-gcd-identities/README.md), `gcd(C_w, Φ₁) = gcd(2^j·C_u + C_v, Φ₁) = gcd(K·(2^j·A + B), K·L) = |K|·gcd(2^j·A + B, L)`, and `gcd(C_w, Φ₂) = gcd(2^j·C_u − C_v, Φ₂) = gcd(K·(2^j·A − B), Φ₂) = gcd(2^j·A − B, Φ₂)`, because `K | Φ₁` and `gcd(Φ₁, Φ₂) = 1` make `K` a unit modulo `Φ₂`. The product formula `gcd(C_w, D_w) = gcd(C_w, Φ₁)·gcd(C_w, Φ₂)` is the same node's. For the denominator, `D_w = Φ₁·Φ₂ = L·K·Φ₂`, and `g₁ | L`, `g₂ | Φ₂` give `L·K·Φ₂ = K·g₁·g₂·(L/g₁)·(Φ₂/g₂)`. All of this is the Lean file.

## Lean

[`lean/LeanLane/RotationPairs.lean`](../../../../lean/LeanLane/RotationPairs.lean), namespace `LeanLane.RotationPairs`, a module of the `LeanLane` library importing `LeanLane.Doubled`; standard axioms only (receipts `RotationPairs.*` in [`lean/receipts/`](../../../../lean/receipts/)). Words are `List ℕ`, intercepts in `ℤ`, `Int.gcd` the nonnegative gcd, `/` the integer division of `ℤ` (exact here).

| Claim | Declaration | Hypotheses |
|---|---|---|
| `gcd(C_w, Φ₁) = |K|·gcd(2^j A + B, L)` | `gcd_Phi1_of_common_factor` | `v.length = u.length`, `0 < u.sum + j`, `Phi1 (u.sum + j) u.length = L * K`, `C u = A * K`, `C v = B * K` |
| `gcd(C_w, Φ₂) = gcd(2^j A − B, Φ₂)` | `gcd_Phi2_of_common_factor` | the same and `0 < u.length` |
| `gcd(C_w, D_w) = |K|·g₁·g₂` | `gcd_D_of_common_factor` | the same and `v.sum = u.sum + 2 * j` |
| `D_w = gcd(C_w, D_w)·(L/g₁)·(Φ₂/g₂)` | `D_eq_gcd_mul` | the same and `0 < K` |

Helper: `gcd_K_Phi2` (`K | Φ₁ ⟹ gcd(K, Φ₂) = 1`). Everything in the claim is formalised.

## Certificates

None: the content is the Lean module; `python3 tools/check_lean_receipts.py` checks the receipts' hashes against the source and the axiom lines.

## Remarks

- **Use.** With `K = gcd(C_u, C_v, Φ₁)` the formula computes `gcd(C_w, D_w)` from three gcds of numbers of the size of `Φ₁`; for the rotation pairs of actual cycles it expresses the cancellation through the cycle's states ([`rotation-pair-words-exact-cancellation`](../rotation-pair-words-exact-cancellation/README.md)). Nothing is said about `q = 1` cycles; the factor `gcd(2^j·A − B, Φ₂)` is the primitive part of [`primitive-cancellation-below-half`](../../questions/primitive-cancellation-below-half.md) when `gcd(A_w, m_w) = 2`.
- **Novelty.** Undetermined; the derivation is elementary.

## History

- Written and formalised 2026-10-31 by the Claude cycles lane (Fable 5.1), directed by Santiago Armstrong, while explaining the counterexample of [`half-cancellation-counterexample-rotation-pair`](../half-cancellation-counterexample-rotation-pair/README.md) through the two states that build it.
