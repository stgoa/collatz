import LeanLane.Words

/-!
# Exact powers of two at the two Mersenne boundaries

The hypotheses are the ordinary signed block endpoint equations and the
corresponding changed-final-valuation equations for cleared integer states.
The two difference identities are derived, rather than assumed. No cycle
exclusion, logarithmic estimate, or sign restriction is used here.
-/

namespace LeanLane.MersenneBoundaries

open LeanLane.Words

/-- The integer is divisible by exactly this power of two. -/
def ExactTwoPower (k : ℕ) (x : ℤ) : Prop :=
  (2 : ℤ) ^ k ∣ x ∧ ¬ (2 : ℤ) ^ (k + 1) ∣ x

theorem ExactTwoPower.ne_zero {k : ℕ} {x : ℤ} (hx : ExactTwoPower k x) :
    x ≠ 0 := by
  intro h
  exact hx.2 (h ▸ dvd_zero _)

theorem ExactTwoPower.le_abs {k : ℕ} {x : ℤ} (hx : ExactTwoPower k x) :
    (2 : ℤ) ^ k ≤ |x| :=
  Int.le_abs_of_dvd hx.ne_zero hx.1

/-- Cancelling an odd ternary multiplier preserves an exact binary power. -/
theorem exact_two_power_of_ternary_eq {a k : ℕ} {x t : ℤ}
    (ht : Odd t) (he : (3 : ℤ) ^ a * x = 2 ^ k * t) : ExactTwoPower k x := by
  have hcop : IsCoprime (2 : ℤ) 3 := ⟨-1, 1, by norm_num⟩
  have hd : (2 : ℤ) ^ k ∣ 3 ^ a * x := ⟨t, he⟩
  refine ⟨(hcop.pow (m := k) (n := a)).dvd_of_dvd_mul_left hd, ?_⟩
  rintro ⟨v, hv⟩
  have hp : (2 : ℤ) ^ k ≠ 0 := by positivity
  have hc : (2 : ℤ) ^ k * (3 ^ a * (2 * v)) = 2 ^ k * t := by
    rw [hv, pow_succ] at he
    linear_combination he
  have hc' := mul_left_cancel₀ hp hc
  have hev : Even t := ⟨3 ^ a * v, by rw [← hc']; ring⟩
  exact (Int.not_even_iff_odd.mpr ht) hev

theorem even_two_power {k : ℕ} (hk : 0 < k) : Even ((2 : ℤ) ^ k) :=
  even_two.pow_of_ne_zero hk.ne'

theorem odd_mersenne {k : ℕ} (hk : 0 < k) : Odd ((2 : ℤ) ^ k - 1) :=
  (even_two_power hk).sub_odd odd_one

/-- High-to-low boundary equations, expressed with actual word intercepts.
`X,Y` are cleared integer states; `q` is their odd additive parameter. -/
theorem high_low_boundaries (A B : List ℕ) (J r : ℕ)
    (q h z X Y : ℤ) (hr : 0 < r) (hJ : r < J)
    (hP : J - r ≤ A.sum) (hT : r ≤ B.sum)
    (hq : Odd q) (hh : Odd h) (hY : Odd Y)
    (hA : (2 : ℤ) ^ A.sum * z =
      3 ^ A.length * (-h) + (2 ^ J - 1) * C A)
    (hAm : (2 : ℤ) ^ (A.sum - (J - r)) * Y = 3 ^ A.length * X + q * C A)
    (hB : (2 : ℤ) ^ B.sum * h =
      3 ^ B.length * z + (2 ^ r - 1) * C B)
    (hBm : (2 : ℤ) ^ (B.sum - r) * (2 ^ J * X + q * h) =
      3 ^ B.length * Y + q * C B) :
    (3 ^ A.length * ((2 ^ J - 1) * X + q * h) =
      (2 : ℤ) ^ (A.sum - (J - r)) * ((2 ^ J - 1) * Y - 2 ^ (J - r) * q * z)) ∧
    ExactTwoPower (A.sum - (J - r)) ((2 ^ J - 1) * X + q * h) ∧
    (3 ^ B.length * ((2 ^ r - 1) * Y - q * z) =
      (2 : ℤ) ^ (B.sum - r) * (2 ^ J * (2 ^ r - 1) * X - q * h)) ∧
    ExactTwoPower (B.sum - r) ((2 ^ r - 1) * Y - q * z) := by
  have hp : 0 < J - r := by omega
  have hJpos : 0 < J := by omega
  have hpowP : (2 : ℤ) ^ A.sum = 2 ^ (A.sum - (J - r)) * 2 ^ (J - r) := by
    rw [← pow_add, Nat.sub_add_cancel hP]
  have hpowT : (2 : ℤ) ^ B.sum = 2 ^ (B.sum - r) * 2 ^ r := by
    rw [← pow_add, Nat.sub_add_cancel hT]
  have first : 3 ^ A.length * ((2 ^ J - 1) * X + q * h) =
      (2 : ℤ) ^ (A.sum - (J - r)) * ((2 ^ J - 1) * Y - 2 ^ (J - r) * q * z) := by
    rw [hpowP] at hA
    linear_combination q * hA - ((2 : ℤ) ^ J - 1) * hAm
  have first_odd : Odd (((2 : ℤ) ^ J - 1) * Y - 2 ^ (J - r) * q * z) :=
    ((odd_mersenne hJpos).mul hY).sub_even (((even_two_power hp).mul_right q).mul_right z)
  have second : 3 ^ B.length * ((2 ^ r - 1) * Y - q * z) =
      (2 : ℤ) ^ (B.sum - r) * (2 ^ J * (2 ^ r - 1) * X - q * h) := by
    rw [hpowT] at hB
    linear_combination q * hB - ((2 : ℤ) ^ r - 1) * hBm
  have second_odd : Odd ((2 : ℤ) ^ J * (2 ^ r - 1) * X - q * h) :=
    (((even_two_power hJpos).mul_right (2 ^ r - 1)).mul_right X).sub_odd (hq.mul hh)
  exact ⟨first, exact_two_power_of_ternary_eq first_odd first,
    second, exact_two_power_of_ternary_eq second_odd second⟩

/-- Low-to-high boundary equations. No positivity or denominator-one
hypothesis is needed, and the two start differences can have either sign. -/
theorem low_high_boundaries (A B : List ℕ) (J r : ℕ)
    (q h z X Y : ℤ) (hr : 0 < r) (hJ : r < J) (hT : J ≤ B.sum)
    (hq : Odd q) (hh : Odd h) (hz : Odd z)
    (hA : (2 : ℤ) ^ A.sum * z =
      3 ^ A.length * (-h) + (2 ^ r - 1) * C A)
    (hAm : (2 : ℤ) ^ (A.sum + (J - r)) * Y = 3 ^ A.length * X + q * C A)
    (hB : (2 : ℤ) ^ B.sum * h =
      3 ^ B.length * z + (2 ^ J - 1) * C B)
    (hBm : (2 : ℤ) ^ (B.sum - J) * (2 ^ r * X + q * h) =
      3 ^ B.length * Y + q * C B) :
    (3 ^ A.length * ((2 ^ r - 1) * X + q * h) =
      (2 : ℤ) ^ A.sum * ((2 ^ r - 1) * 2 ^ (J - r) * Y - q * z)) ∧
    ExactTwoPower A.sum ((2 ^ r - 1) * X + q * h) ∧
    (3 ^ B.length * ((2 ^ J - 1) * Y - q * z) =
      (2 : ℤ) ^ (B.sum - J) * (2 ^ r * (2 ^ J - 1) * X - q * h)) ∧
    ExactTwoPower (B.sum - J) ((2 ^ J - 1) * Y - q * z) := by
  have hp : 0 < J - r := by omega
  have hpowT : (2 : ℤ) ^ B.sum = 2 ^ (B.sum - J) * 2 ^ J := by
    rw [← pow_add, Nat.sub_add_cancel hT]
  have first : 3 ^ A.length * ((2 ^ r - 1) * X + q * h) =
      (2 : ℤ) ^ A.sum * ((2 ^ r - 1) * 2 ^ (J - r) * Y - q * z) := by
    rw [pow_add] at hAm
    linear_combination q * hA - ((2 : ℤ) ^ r - 1) * hAm
  have first_odd : Odd (((2 : ℤ) ^ r - 1) * 2 ^ (J - r) * Y - q * z) :=
    (((even_two_power hp).mul_left (2 ^ r - 1)).mul_right Y).sub_odd (hq.mul hz)
  have second : 3 ^ B.length * ((2 ^ J - 1) * Y - q * z) =
      (2 : ℤ) ^ (B.sum - J) * (2 ^ r * (2 ^ J - 1) * X - q * h) := by
    rw [hpowT] at hB
    linear_combination q * hB - ((2 : ℤ) ^ J - 1) * hBm
  have second_odd : Odd ((2 : ℤ) ^ r * (2 ^ J - 1) * X - q * h) :=
    (((even_two_power hr).mul_right (2 ^ J - 1)).mul_right X).sub_odd (hq.mul hh)
  exact ⟨first, exact_two_power_of_ternary_eq first_odd first,
    second, exact_two_power_of_ternary_eq second_odd second⟩

/-- A genuine reduced `3x+361` control has a negative second difference. -/
theorem negative_difference_control :
    ExactTwoPower 5 (480 : ℤ) ∧ ExactTwoPower 3 (-600 : ℤ) := by
  have hc := high_low_boundaries [2, 1, 1, 3] [4] 3 1 361 1 5 17 1205
    (by norm_num) (by norm_num) (by norm_num) (by norm_num)
    (by norm_num) (by norm_num) (by norm_num)
    (by norm_num [C]) (by norm_num [C]) (by norm_num [C]) (by norm_num [C])
  exact ⟨by simpa using hc.2.1, by simpa using hc.2.2.2⟩

end LeanLane.MersenneBoundaries

#print axioms LeanLane.MersenneBoundaries.ExactTwoPower.ne_zero
#print axioms LeanLane.MersenneBoundaries.ExactTwoPower.le_abs
#print axioms LeanLane.MersenneBoundaries.exact_two_power_of_ternary_eq
#print axioms LeanLane.MersenneBoundaries.even_two_power
#print axioms LeanLane.MersenneBoundaries.odd_mersenne
#print axioms LeanLane.MersenneBoundaries.high_low_boundaries
#print axioms LeanLane.MersenneBoundaries.low_high_boundaries
#print axioms LeanLane.MersenneBoundaries.negative_difference_control
