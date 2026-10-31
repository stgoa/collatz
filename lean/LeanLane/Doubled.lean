import LeanLane.Words

/-!
# Doubled words: the two factors of `D` test the half-words

Formal companion of `areas/cycles/results/doubled-word-factor-gcd-identities/README.md`.

A positive valuation word `z` (a `List ℕ`) has intercept `C z` and discriminant `D z = 2^(Σz) − 3^|z|`,
with the definitions of `CycleSpectrum.lean`, shared through `LeanLane.Words` (this file imports only that module).
For `w = u ++ v` with `|u| = |v| = n` and `S = S_u + j`:

* `gcd_Phi1`: `gcd (C w) (2^S − 3^n) = gcd (2^j C_u + C_v) (2^S − 3^n)`;
* `gcd_Phi2`: `gcd (C w) (2^S + 3^n) = gcd (2^j C_u − C_v) (2^S + 3^n)`;
* `Phi1_dvd_iff`, `Phi2_dvd_iff`: the divisibility forms;
* `periodic_point_criterion`, `antiperiodic_point_criterion`: the same as integrality of
  `2^j x_u + x_v` and of `2^j y_u − y_v`, where `x_z = C_z/(2^S − 3^n)` and `y_z = C_z/(2^S + 3^n)`;
* `T_fixed`, `T_antifixed`: `x_z` is the fixed point and `−y_z ↦ y_z` under `T_z(x) = (3^n x + C_z)/2^S`;
* `D_eq_Phi1_mul_Phi2`, `gcd_Phi1_Phi2`, `gcd_D_eq_mul`: `D w = Φ₁Φ₂`, the factors are coprime, and
  `gcd (C w) (D w) = gcd (C w) Φ₁ · gcd (C w) Φ₂`;
* `one_letter_identity`, `one_letter_gcd_Phi1`: for `v = u` with one letter raised by `2j`,
  `2^j C_u + C_v = (2^j + 1) C_(u')` with `u'` the word with that letter raised by `j`, and
  `gcd (C w) (D u') = gcd ((2^j + 1) C_(u')) (D u')`.

Only `j ≥ 0` (`S_v ≥ S_u`) is formalised; the other case is the same statement with `u` and `v` exchanged.
-/

namespace LeanLane
namespace Doubled

open LeanLane.Words

/-- `D` of a doubled word factors as `Φ₁ Φ₂`. -/
theorem D_eq_Phi1_mul_Phi2 (u v : List ℕ) (S : ℕ) (hlen : v.length = u.length)
    (hsum : u.sum + v.sum = 2 * S) : D (u ++ v) = Phi1 S u.length * Phi2 S u.length := by
  simp only [D, Phi1, Phi2, List.sum_append, List.length_append, hlen, hsum]
  ring

/-- **The algebraic factor.** `w = u ++ v`, `|v| = |u|`, `S = S_u + j`. -/
theorem gcd_Phi1 (u v : List ℕ) (j : ℕ) (hlen : v.length = u.length) (hS : 0 < u.sum + j) :
    Int.gcd (C (u ++ v)) (Phi1 (u.sum + j) u.length)
      = Int.gcd (2 ^ j * C u + C v) (Phi1 (u.sum + j) u.length) := by
  have key : C (u ++ v)
      = 2 ^ u.sum * (2 ^ j * C u + C v) - Phi1 (u.sum + j) u.length * C u := by
    rw [C_append, hlen, Phi1, pow_add]; ring
  rw [key, Int.gcd_sub_mul_left_left, gcd_two_pow_mul_left (odd_Phi1 _ _ hS)]

/-- **The other factor.** -/
theorem gcd_Phi2 (u v : List ℕ) (j : ℕ) (hlen : v.length = u.length) (hS : 0 < u.sum + j) :
    Int.gcd (C (u ++ v)) (Phi2 (u.sum + j) u.length)
      = Int.gcd (2 ^ j * C u - C v) (Phi2 (u.sum + j) u.length) := by
  have key : C (u ++ v)
      = 2 ^ u.sum * (C v - 2 ^ j * C u) + Phi2 (u.sum + j) u.length * C u := by
    rw [C_append, hlen, Phi2, pow_add]; ring
  rw [key, Int.gcd_add_mul_left_left, gcd_two_pow_mul_left (odd_Phi2 _ _ hS),
    ← neg_sub (2 ^ j * C u) (C v), Int.neg_gcd]

theorem Phi1_dvd_iff (u v : List ℕ) (j : ℕ) (hlen : v.length = u.length) (hS : 0 < u.sum + j) :
    Phi1 (u.sum + j) u.length ∣ C (u ++ v) ↔ Phi1 (u.sum + j) u.length ∣ 2 ^ j * C u + C v := by
  rw [← Int.gcd_eq_natAbs_right_iff_dvd, ← Int.gcd_eq_natAbs_right_iff_dvd, gcd_Phi1 u v j hlen hS]

theorem Phi2_dvd_iff (u v : List ℕ) (j : ℕ) (hlen : v.length = u.length) (hS : 0 < u.sum + j) :
    Phi2 (u.sum + j) u.length ∣ C (u ++ v) ↔ Phi2 (u.sum + j) u.length ∣ 2 ^ j * C u - C v := by
  rw [← Int.gcd_eq_natAbs_right_iff_dvd, ← Int.gcd_eq_natAbs_right_iff_dvd, gcd_Phi2 u v j hlen hS]

/-! ### The two factors are coprime, and `G` is the product -/

/-- `gcd (Φ₁, Φ₂) = 1` for `S ≥ 1`, `n ≥ 1`. -/
theorem gcd_Phi1_Phi2 (S n : ℕ) (hS : 0 < S) (hn : 0 < n) : Int.gcd (Phi1 S n) (Phi2 S n) = 1 := by
  have h : Phi2 S n = 2 * 3 ^ n + Phi1 S n * 1 := by unfold Phi1 Phi2; ring
  rw [h, Int.gcd_add_mul_left_right, Int.gcd_comm,
    Int.gcd_mul_right_left_of_gcd_eq_one (gcd_two_eq_one_of_odd (odd_Phi1 S n hS))]
  simpa using gcd_pow_mul_left (gcd_three_Phi1 S n hn) n 1

/-- `G = gcd (C w) (D w)` is the product of the two partial gcds. -/
theorem gcd_D_eq_mul (u v : List ℕ) (j : ℕ) (hlen : v.length = u.length) (hv : v.sum = u.sum + 2 * j)
    (hS : 0 < u.sum + j) (hu : 0 < u.length) :
    Int.gcd (C (u ++ v)) (D (u ++ v))
      = Int.gcd (C (u ++ v)) (Phi1 (u.sum + j) u.length)
        * Int.gcd (C (u ++ v)) (Phi2 (u.sum + j) u.length) := by
  rw [D_eq_Phi1_mul_Phi2 u v (u.sum + j) hlen (by omega)]
  have hcop : Nat.Coprime (Phi1 (u.sum + j) u.length).natAbs (Phi2 (u.sum + j) u.length).natAbs :=
    gcd_Phi1_Phi2 _ _ hS hu
  simp only [Int.gcd_eq_natAbs_gcd_natAbs, Int.natAbs_mul]
  exact Nat.Coprime.gcd_mul _ hcop

/-! ### Periodic and antiperiodic points -/

/-- The affine map of a word of length `|z|` whose total is read as `S`. -/
noncomputable def T (z : List ℕ) (S : ℕ) (x : ℚ) : ℚ := (3 ^ z.length * x + C z) / 2 ^ S

/-- `x_z = C_z/Φ₁` is the fixed point of `T_z`. -/
theorem T_fixed (z : List ℕ) (S : ℕ) (h : Phi1 S z.length ≠ 0) :
    T z S ((C z : ℚ) / (Phi1 S z.length : ℚ)) = (C z : ℚ) / (Phi1 S z.length : ℚ) := by
  have h2 : (2 : ℚ) ^ S ≠ 0 := pow_ne_zero _ two_ne_zero
  have h' : ((Phi1 S z.length : ℤ) : ℚ) ≠ 0 := by exact_mod_cast h
  unfold T
  unfold Phi1 at h' ⊢
  push_cast at h' ⊢
  field_simp
  ring

/-- `y_z = C_z/Φ₂` is the antiperiodic point of `T_z`: `T_z(−y_z) = y_z`. -/
theorem T_antifixed (z : List ℕ) (S : ℕ) :
    T z S (-((C z : ℚ) / (Phi2 S z.length : ℚ))) = (C z : ℚ) / (Phi2 S z.length : ℚ) := by
  have h2 : (2 : ℚ) ^ S ≠ 0 := pow_ne_zero _ two_ne_zero
  have h' : ((Phi2 S z.length : ℤ) : ℚ) ≠ 0 := by exact_mod_cast (Phi2_pos S z.length).ne'
  unfold T
  unfold Phi2 at h' ⊢
  push_cast at h' ⊢
  field_simp
  ring

/-- `Φ₁ ∣ C w` iff `2^j x_u + x_v` is an integer. -/
theorem periodic_point_criterion (u v : List ℕ) (j : ℕ) (hlen : v.length = u.length)
    (hS : 0 < u.sum + j) :
    (∃ k : ℤ, 2 ^ j * ((C u : ℚ) / (Phi1 (u.sum + j) u.length : ℚ))
        + (C v : ℚ) / (Phi1 (u.sum + j) u.length : ℚ) = k)
      ↔ Phi1 (u.sum + j) u.length ∣ C (u ++ v) := by
  rw [Phi1_dvd_iff u v j hlen hS]
  have hne : ((Phi1 (u.sum + j) u.length : ℤ) : ℚ) ≠ 0 := Phi1_cast_ne_zero _ _ hS
  have hcomb : 2 ^ j * ((C u : ℚ) / (Phi1 (u.sum + j) u.length : ℚ))
      + (C v : ℚ) / (Phi1 (u.sum + j) u.length : ℚ)
      = ((2 ^ j * C u + C v : ℤ) : ℚ) / (Phi1 (u.sum + j) u.length : ℚ) := by
    push_cast; ring
  rw [hcomb]
  constructor
  · rintro ⟨k, hk⟩
    rw [div_eq_iff hne] at hk
    refine ⟨k, ?_⟩
    have : ((2 ^ j * C u + C v : ℤ) : ℚ) = ((Phi1 (u.sum + j) u.length * k : ℤ) : ℚ) := by
      rw [hk]; push_cast; ring
    exact_mod_cast this
  · rintro ⟨k, hk⟩
    refine ⟨k, ?_⟩
    rw [hk]
    push_cast
    exact mul_div_cancel_left₀ _ hne

/-- `Φ₂ ∣ C w` iff `2^j y_u − y_v` is an integer. -/
theorem antiperiodic_point_criterion (u v : List ℕ) (j : ℕ) (hlen : v.length = u.length)
    (hS : 0 < u.sum + j) :
    (∃ k : ℤ, 2 ^ j * ((C u : ℚ) / (Phi2 (u.sum + j) u.length : ℚ))
        - (C v : ℚ) / (Phi2 (u.sum + j) u.length : ℚ) = k)
      ↔ Phi2 (u.sum + j) u.length ∣ C (u ++ v) := by
  rw [Phi2_dvd_iff u v j hlen hS]
  have hne : ((Phi2 (u.sum + j) u.length : ℤ) : ℚ) ≠ 0 := Phi2_cast_ne_zero _ _
  have hcomb : 2 ^ j * ((C u : ℚ) / (Phi2 (u.sum + j) u.length : ℚ))
      - (C v : ℚ) / (Phi2 (u.sum + j) u.length : ℚ)
      = ((2 ^ j * C u - C v : ℤ) : ℚ) / (Phi2 (u.sum + j) u.length : ℚ) := by
    push_cast; ring
  rw [hcomb]
  constructor
  · rintro ⟨k, hk⟩
    rw [div_eq_iff hne] at hk
    refine ⟨k, ?_⟩
    have : ((2 ^ j * C u - C v : ℤ) : ℚ) = ((Phi2 (u.sum + j) u.length * k : ℤ) : ℚ) := by
      rw [hk]; push_cast; ring
    exact_mod_cast this
  · rintro ⟨k, hk⟩
    refine ⟨k, ?_⟩
    rw [hk]
    push_cast
    exact mul_div_cancel_left₀ _ hne

/-! ### One-letter changes -/

/-- `v = u` with the letter `a` raised by `2j`; `u'` has it raised by `j`. -/
theorem one_letter_identity (p s : List ℕ) (a j : ℕ) :
    2 ^ j * C (p ++ a :: s) + C (p ++ (a + 2 * j) :: s) = (2 ^ j + 1) * C (p ++ (a + j) :: s) := by
  simp only [C_append, C, List.length_cons, two_mul, pow_add]
  ring

theorem one_letter_gcd_Phi1 (p s : List ℕ) (a j : ℕ) (hS : 0 < (p ++ a :: s).sum + j) :
    Int.gcd (C ((p ++ a :: s) ++ (p ++ (a + 2 * j) :: s))) (D (p ++ (a + j) :: s))
      = Int.gcd ((2 ^ j + 1) * C (p ++ (a + j) :: s)) (D (p ++ (a + j) :: s)) := by
  have hlen : (p ++ (a + 2 * j) :: s).length = (p ++ a :: s).length := by simp
  have hD : D (p ++ (a + j) :: s) = Phi1 ((p ++ a :: s).sum + j) (p ++ a :: s).length := by
    simp only [D, Phi1, List.sum_append, List.sum_cons, List.length_append, List.length_cons]
    ring_nf
  rw [hD, gcd_Phi1 _ _ j hlen hS, one_letter_identity]

end Doubled
end LeanLane

#print axioms LeanLane.Doubled.gcd_Phi1
#print axioms LeanLane.Doubled.gcd_Phi2
#print axioms LeanLane.Doubled.Phi1_dvd_iff
#print axioms LeanLane.Doubled.Phi2_dvd_iff
#print axioms LeanLane.Doubled.D_eq_Phi1_mul_Phi2
#print axioms LeanLane.Doubled.gcd_Phi1_Phi2
#print axioms LeanLane.Doubled.gcd_D_eq_mul
#print axioms LeanLane.Doubled.T_fixed
#print axioms LeanLane.Doubled.T_antifixed
#print axioms LeanLane.Doubled.periodic_point_criterion
#print axioms LeanLane.Doubled.antiperiodic_point_criterion
#print axioms LeanLane.Doubled.one_letter_identity
#print axioms LeanLane.Doubled.one_letter_gcd_Phi1
