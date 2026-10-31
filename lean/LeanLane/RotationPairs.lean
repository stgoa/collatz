import LeanLane.Doubled

/-!
# The cancellation of a doubled word from a common factor of the half-intercepts

Formal companion of `areas/cycles/results/doubled-word-cancellation-formula/README.md`.

For `w = u ++ v` with `|u| = |v| = n`, `S = S_u + j`, `Φ₁ = 2^S − 3^n`, `Φ₂ = 2^S + 3^n`: if `Φ₁ = L·K`,
`C_u = A·K` and `C_v = B·K` (for instance `K = Φ₁/d` when both half-words have periodic points with
denominator `d`, `A`, `B` their numerators and `L = d`), then

* `gcd (C_w) Φ₁ = |K| · gcd (2^j A + B) L`,
* `gcd (C_w) Φ₂ = gcd (2^j A − B) Φ₂`,
* `gcd (C_w) (D_w) = |K| · gcd (2^j A + B) L · gcd (2^j A − B) Φ₂`, and
  `D_w = gcd (C_w) (D_w) · (L / gcd (2^j A + B) L) · (Φ₂ / gcd (2^j A − B) Φ₂)` when `K > 0`.

The rotation pairs `(R_r u, R_s u)` of an actual `3x+d` cycle are the case `K = gcd(C_u, D_u)`, `L = d`,
`A = n_r`, `B = n_s` (the states), `j = 0`: their cancellation is `K · gcd(n_r + n_s, d) · gcd(n_r − n_s, Φ₂)`.
-/

namespace LeanLane
namespace RotationPairs

open LeanLane.Words LeanLane.Doubled

theorem gcd_K_Phi2 (S n : ℕ) (hS : 0 < S) (hn : 0 < n) (K L : ℤ) (hK : Phi1 S n = L * K) :
    Int.gcd K (Phi2 S n) = 1 := by
  have h1 : Int.gcd K (Phi2 S n) ∣ Int.gcd (Phi1 S n) (Phi2 S n) :=
    Int.gcd_dvd_gcd_of_dvd_left _ ⟨L, by rw [hK]; ring⟩
  rw [gcd_Phi1_Phi2 S n hS hn] at h1
  exact Nat.dvd_one.mp h1

/-- `gcd (C_w) Φ₁ = |K| · gcd (2^j A + B) L`. -/
theorem gcd_Phi1_of_common_factor (u v : List ℕ) (j : ℕ) (K L A B : ℤ) (hlen : v.length = u.length)
    (hS : 0 < u.sum + j) (hK : Phi1 (u.sum + j) u.length = L * K) (hu : C u = A * K) (hv : C v = B * K) :
    (Int.gcd (C (u ++ v)) (Phi1 (u.sum + j) u.length) : ℤ) = |K| * Int.gcd (2 ^ j * A + B) L := by
  rw [gcd_Phi1 u v j hlen hS, hu, hv, hK]
  have h : 2 ^ j * (A * K) + B * K = K * (2 ^ j * A + B) := by ring
  rw [h, mul_comm L K, Int.gcd_mul_left]
  push_cast
  ring

/-- `gcd (C_w) Φ₂ = gcd (2^j A − B) Φ₂`. -/
theorem gcd_Phi2_of_common_factor (u v : List ℕ) (j : ℕ) (K L A B : ℤ) (hlen : v.length = u.length)
    (hS : 0 < u.sum + j) (hn : 0 < u.length) (hK : Phi1 (u.sum + j) u.length = L * K)
    (hu : C u = A * K) (hv : C v = B * K) :
    Int.gcd (C (u ++ v)) (Phi2 (u.sum + j) u.length) = Int.gcd (2 ^ j * A - B) (Phi2 (u.sum + j) u.length) := by
  rw [gcd_Phi2 u v j hlen hS, hu, hv]
  have h : 2 ^ j * (A * K) - B * K = K * (2 ^ j * A - B) := by ring
  rw [h, Int.gcd_mul_right_left_of_gcd_eq_one (gcd_K_Phi2 _ _ hS hn K L hK)]

/-- **The cancellation formula.** -/
theorem gcd_D_of_common_factor (u v : List ℕ) (j : ℕ) (K L A B : ℤ) (hlen : v.length = u.length)
    (hv2 : v.sum = u.sum + 2 * j) (hS : 0 < u.sum + j) (hn : 0 < u.length)
    (hK : Phi1 (u.sum + j) u.length = L * K) (hu : C u = A * K) (hv : C v = B * K) :
    (Int.gcd (C (u ++ v)) (D (u ++ v)) : ℤ)
      = |K| * Int.gcd (2 ^ j * A + B) L * Int.gcd (2 ^ j * A - B) (Phi2 (u.sum + j) u.length) := by
  rw [gcd_D_eq_mul u v j hlen hv2 hS hn]
  push_cast
  rw [gcd_Phi1_of_common_factor u v j K L A B hlen hS hK hu hv,
    gcd_Phi2_of_common_factor u v j K L A B hlen hS hn hK hu hv]

/-- **The reduced denominator.** For `K > 0`: `D_w = G · (L / g₁) · (Φ₂ / g₂)`, with `g₁ = gcd (2^j A + B) L`
and `g₂ = gcd (2^j A − B) Φ₂` dividing `L` and `Φ₂`. -/
theorem D_eq_gcd_mul (u v : List ℕ) (j : ℕ) (K L A B : ℤ) (hlen : v.length = u.length)
    (hv2 : v.sum = u.sum + 2 * j) (hS : 0 < u.sum + j) (hn : 0 < u.length) (hKpos : 0 < K)
    (hK : Phi1 (u.sum + j) u.length = L * K) (hu : C u = A * K) (hv : C v = B * K) :
    D (u ++ v) = (Int.gcd (C (u ++ v)) (D (u ++ v)) : ℤ)
      * (L / Int.gcd (2 ^ j * A + B) L) * (Phi2 (u.sum + j) u.length / Int.gcd (2 ^ j * A - B) (Phi2 (u.sum + j) u.length)) := by
  rw [gcd_D_of_common_factor u v j K L A B hlen hv2 hS hn hK hu hv, D_eq_Phi1_mul_Phi2 u v (u.sum + j) hlen (by omega), hK,
    abs_of_pos hKpos]
  have h1 : (Int.gcd (2 ^ j * A + B) L : ℤ) * (L / Int.gcd (2 ^ j * A + B) L) = L :=
    Int.mul_ediv_cancel' (Int.gcd_dvd_right _ _)
  have h2 : (Int.gcd (2 ^ j * A - B) (Phi2 (u.sum + j) u.length) : ℤ)
      * (Phi2 (u.sum + j) u.length / Int.gcd (2 ^ j * A - B) (Phi2 (u.sum + j) u.length)) = Phi2 (u.sum + j) u.length :=
    Int.mul_ediv_cancel' (Int.gcd_dvd_right _ _)
  calc L * K * Phi2 (u.sum + j) u.length
      = K * ((Int.gcd (2 ^ j * A + B) L : ℤ) * (L / Int.gcd (2 ^ j * A + B) L))
          * ((Int.gcd (2 ^ j * A - B) (Phi2 (u.sum + j) u.length) : ℤ)
            * (Phi2 (u.sum + j) u.length / Int.gcd (2 ^ j * A - B) (Phi2 (u.sum + j) u.length))) := by
        rw [h1, h2]; ring
    _ = _ := by ring

end RotationPairs
end LeanLane

#print axioms LeanLane.RotationPairs.gcd_Phi1_of_common_factor
#print axioms LeanLane.RotationPairs.gcd_Phi2_of_common_factor
#print axioms LeanLane.RotationPairs.gcd_D_of_common_factor
#print axioms LeanLane.RotationPairs.D_eq_gcd_mul
