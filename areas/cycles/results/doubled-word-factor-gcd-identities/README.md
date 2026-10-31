---
id: doubled-word-factor-gcd-identities
kind: result
title: "Doubled words: gcd identities for the two factors of D, machine-checked"
status: formal
claim: >
  Raw odd-only clock, any 3x+q. Let w = (u, v) with |u| = |v| = n, S = S_u + j ≥ 1 for an integer j ≥ 0, and
  Φ₁ = 2^S − 3^n, Φ₂ = 2^S + 3^n. Then (1) gcd(C_w, Φ₁) = gcd(2^j·C_u + C_v, Φ₁) and
  gcd(C_w, Φ₂) = gcd(2^j·C_u − C_v, Φ₂); (2) Φ₁ | C_w iff 2^j·x_u + x_v is an integer and Φ₂ | C_w iff
  2^j·y_u − y_v is an integer, where x_z = C_z/Φ₁ and y_z = C_z/Φ₂; x_z is the fixed point and y_z the
  antiperiodic point (T(−y) = y) of T_z(x) = (3^n·x + C_z)/2^S; (3) if moreover S_v = S_u + 2j and n ≥ 1, then
  D_w = Φ₁·Φ₂ with gcd(Φ₁, Φ₂) = 1 and gcd(C_w, D_w) = gcd(C_w, Φ₁)·gcd(C_w, Φ₂); (4) for a one-letter change
  v = u + 2j·e_i and u' = u + j·e_i, 2^j·C_u + C_v = (2^j + 1)·C_(u') and gcd(C_w, D_(u')) = gcd((2^j + 1)·C_(u'), D_(u')).
  The case S_v < S_u is the same statement with u and v exchanged. Everything is proved in Lean
  (lean/DoubledWords.lean) with the standard axioms only, for words with letters in ℕ (zero letters allowed).
authors:
  - Claude cycles lane (Fable 5.1; directed by Santiago Armstrong)
created: 2026-10-31
depends_on: []
lean:
  - LeanLane.Doubled.gcd_Phi1
  - LeanLane.Doubled.gcd_Phi2
  - LeanLane.Doubled.Phi1_dvd_iff
  - LeanLane.Doubled.Phi2_dvd_iff
  - LeanLane.Doubled.periodic_point_criterion
  - LeanLane.Doubled.antiperiodic_point_criterion
  - LeanLane.Doubled.T_fixed
  - LeanLane.Doubled.T_antifixed
  - LeanLane.Doubled.D_eq_Phi1_mul_Phi2
  - LeanLane.Doubled.gcd_Phi1_Phi2
  - LeanLane.Doubled.gcd_D_eq_mul
  - LeanLane.Doubled.one_letter_identity
  - LeanLane.Doubled.one_letter_gcd_Phi1
evidence:
  - "../../../../lean/receipts/DoubledWords.build.txt, DoubledWords.axioms.txt, DoubledWords.sha256.txt: build status, the #print axioms lines (standard axioms only) and the source hash, produced on the pinned toolchain"
tags: [cycles, denominators, cancellation, cyclotomic-factors, doubled-words, lean]
---

# Doubled words: gcd identities for the two factors of D, machine-checked

## Statement

Notation of [`conventions/NOTATION.md`](../../../../conventions/NOTATION.md) §2, with the definitions of `lean/CycleSpectrum.lean`: for a word `z = (a_0, …, a_(k−1))`, `C_[] = 0`, `C_(a :: z) = 3^|z| + 2^a·C_z` (so `C_z = Σ_t 3^(k−1−t)·2^(s_t)`), and `D_z = 2^(Σz) − 3^|z|`.

Let `u, v` be words of the same length `n`, `j ≥ 0`, `S = S_u + j`, and

```
Φ₁ = 2^S − 3^n,     Φ₂ = 2^S + 3^n,     w = (u, v).
```

1. **The two gcd identities** (`S ≥ 1`): `gcd(C_w, Φ₁) = gcd(2^j·C_u + C_v, Φ₁)` and `gcd(C_w, Φ₂) = gcd(2^j·C_u − C_v, Φ₂)`. Hence `Φ₁ | C_w ⟺ Φ₁ | 2^j·C_u + C_v` and `Φ₂ | C_w ⟺ Φ₂ | 2^j·C_u − C_v`.
2. **Periodic and antiperiodic points** (`S ≥ 1`). Let `T_z(x) = (3^n·x + C_z)/2^S` on `ℚ`, `x_z = C_z/Φ₁`, `y_z = C_z/Φ₂`. Then `T_z(x_z) = x_z` (when `Φ₁ ≠ 0`) and `T_z(−y_z) = y_z`; and `Φ₁ | C_w` iff `2^j·x_u + x_v ∈ Z`, `Φ₂ | C_w` iff `2^j·y_u − y_v ∈ Z`.
3. **The factorisation** (`S_v = S_u + 2j`, `S ≥ 1`, `n ≥ 1`): `D_w = Φ₁·Φ₂`, `gcd(Φ₁, Φ₂) = 1`, and `gcd(C_w, D_w) = gcd(C_w, Φ₁)·gcd(C_w, Φ₂)`.
4. **One-letter changes.** For `u = p·a·s`, `v = p·(a + 2j)·s`, `u' = p·(a + j)·s`: `2^j·C_u + C_v = (2^j + 1)·C_(u')`, and (with `S_u + j ≥ 1`) `gcd(C_w, D_(u')) = gcd((2^j + 1)·C_(u'), D_(u'))`.

The prose theorem and its corollaries, with the data they produce, are in [`doubled-words-periodic-and-antiperiodic-points`](../doubled-words-periodic-and-antiperiodic-points/README.md); this node is its machine-checked core.

## Proof

By the concatenation identity `C_(u ++ v) = 3^|v|·C_u + 2^(S_u)·C_v`: modulo `Φ₁`, `3^n ≡ 2^S`, so `C_w = 2^(S_u)·(2^j·C_u + C_v) − Φ₁·C_u`; modulo `Φ₂`, `3^n ≡ −2^S`, so `C_w = 2^(S_u)·(C_v − 2^j·C_u) + Φ₂·C_u`. Subtracting a multiple of the modulus does not change the gcd, and a power of 2 can be cancelled because both moduli are odd for `S ≥ 1` (`2^S` even, `3^n` odd). The divisibility forms follow from `gcd(a, b) = |b| ⟺ b | a`; the point criteria rewrite `2^j·x_u ± x_v = (2^j·C_u ± C_v)/Φ` and use `Φ ≠ 0`. For (3), `Φ₂ = Φ₁ + 2·3^n` gives `gcd(Φ₁, Φ₂) = gcd(Φ₁, 2·3^n) = 1` (odd, and `3 ∤ Φ₁` because `3 | Φ₁` would force `3 | 2^S`); the product formula is `gcd(k, mn) = gcd(k, m)·gcd(k, n)` for coprime `m, n`. For (4), `C_(p·a·s) = 3^(|s|+1)·C_p + 2^(S_p)·(3^|s| + 2^a·C_s)`, and the identity is a direct expansion; the gcd statement is (1) with `D_(u') = Φ₁`. All of it is the Lean file; the prose argument is the same as in [`doubled-words-periodic-and-antiperiodic-points`](../doubled-words-periodic-and-antiperiodic-points/README.md).

## Lean

[`lean/DoubledWords.lean`](../../../../lean/DoubledWords.lean), namespace `LeanLane.Doubled`, standalone (`import Mathlib` only), compiled with `lake env lean DoubledWords.lean` on the pinned toolchain `leanprover/lean4:v4.35.0-rc2` with Mathlib `0653561`; receipts in [`lean/receipts/`](../../../../lean/receipts/). Axioms of every declaration: `propext`, `Classical.choice`, `Quot.sound` only. Words are `List ℕ` (letters may be 0; the claim's positive words are a special case), intercepts live in `ℤ`, `Int.gcd` is the nonnegative gcd.

| Claim | Declaration | Statement and hypotheses |
|---|---|---|
| (1), `Φ₁` | `gcd_Phi1` | `Int.gcd (C (u ++ v)) (Phi1 (u.sum + j) u.length) = Int.gcd (2^j * C u + C v) (Phi1 (u.sum + j) u.length)` for `v.length = u.length`, `0 < u.sum + j`. No hypothesis on `v.sum`: the identity holds for every `v` of the right length. |
| (1), `Φ₂` | `gcd_Phi2` | the same with `Phi2` and `2^j * C u - C v`. |
| (1), divisibility | `Phi1_dvd_iff`, `Phi2_dvd_iff` | `Phi1 … ∣ C (u ++ v) ↔ Phi1 … ∣ 2^j * C u + C v`, and the `Phi2` analogue. |
| (2), points | `T_fixed`, `T_antifixed` | `T z S (C z / Phi1 S z.length) = C z / Phi1 S z.length` for `Phi1 S z.length ≠ 0`; `T z S (−(C z / Phi2 S z.length)) = C z / Phi2 S z.length`, in `ℚ`, with `T z S x = (3^z.length * x + C z) / 2^S`. |
| (2), criteria | `periodic_point_criterion`, `antiperiodic_point_criterion` | `(∃ k : ℤ, 2^j * (C u / Φ₁) + C v / Φ₁ = k) ↔ Φ₁ ∣ C (u ++ v)` and the `Φ₂` form with a minus sign, same hypotheses as (1). |
| (3) | `D_eq_Phi1_mul_Phi2`, `gcd_Phi1_Phi2`, `gcd_D_eq_mul` | `D (u ++ v) = Phi1 S n * Phi2 S n` for `v.length = u.length`, `u.sum + v.sum = 2 * S`; `Int.gcd (Phi1 S n) (Phi2 S n) = 1` for `0 < S`, `0 < n`; `Int.gcd (C (u ++ v)) (D (u ++ v)) = Int.gcd (C (u ++ v)) Φ₁ * Int.gcd (C (u ++ v)) Φ₂` for `v.length = u.length`, `v.sum = u.sum + 2 * j`, `0 < u.sum + j`, `0 < u.length`. |
| (4) | `one_letter_identity`, `one_letter_gcd_Phi1` | `2^j * C (p ++ a :: s) + C (p ++ (a + 2 * j) :: s) = (2^j + 1) * C (p ++ (a + j) :: s)` (no hypotheses); `Int.gcd (C ((p ++ a :: s) ++ (p ++ (a + 2 * j) :: s))) (D (p ++ (a + j) :: s)) = Int.gcd ((2^j + 1) * C (p ++ (a + j) :: s)) (D (p ++ (a + j) :: s))` for `0 < (p ++ a :: s).sum + j`. |

Helper lemmas: `C_append` (the concatenation identity), `odd_Phi1`, `odd_Phi2`, `Phi2_pos`, `gcd_two_eq_one_of_odd`, `gcd_pow_mul_left`, `gcd_two_pow_mul_left`, `not_three_dvd_Phi1`, `not_three_dvd_Phi2`, `gcd_three_Phi1`, `Phi1_ne_zero`, `Phi1_cast_ne_zero`, `Phi2_cast_ne_zero`. What is **not** formalised: the case `S_v < S_u` (apply the theorems to `(v, u)`), and corollaries (ii) and (iii) of the prose node (the two-marker evaluation and the rotation pairs of actual cycles), whose data remain finite computations there.

## Certificates

None: the content is the Lean file; `python3 tools/check_lean_receipts.py` checks the receipts' hashes against the source and the axiom lines.

## Remarks

- **Why `S ≥ 1` and `n ≥ 1`.** For `S = 0` the "factors" `1 ∓ 3^n` are even, and the cancellation of powers of 2 fails; for `n = 0`, `Φ₁ = 2^S − 1` can be divisible by 3 (`S = 2`), so `gcd(Φ₁, Φ₂) = 1` needs `n ≥ 1`. Both hold for every genuine doubled word.
- **Scope.** Identities about words; nothing about `q = 1` cycles. The controls and the consequences (the two-marker family, the counterexample to the half-cancellation conjecture) are in [`doubled-words-periodic-and-antiperiodic-points`](../doubled-words-periodic-and-antiperiodic-points/README.md) and [`half-cancellation-counterexample-rotation-pair`](../half-cancellation-counterexample-rotation-pair/README.md). Novelty undetermined; the algebra is elementary.

## History

- Written and formalised 2026-10-31 by the Claude cycles lane (Fable 5.1), directed by Santiago Armstrong, as the machine-checked core of [`doubled-words-periodic-and-antiperiodic-points`](../doubled-words-periodic-and-antiperiodic-points/README.md), the same day as that node.
