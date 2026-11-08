import LeanLane.WeightedCrossing

namespace LeanLane.OddOrderObstruction

/-- An odd common exponent makes every mixed plus factor coprime to the modulus. -/
theorem coprime_plus_factor {Q R : ℕ} (hQ : Odd Q) (hR : Odd R)
    (h2 : Nat.ModEq Q (2 ^ R) 1) (h3 : Nat.ModEq Q (3 ^ R) 1)
    (S n : ℕ) : Nat.Coprime Q (2 ^ S + 3 ^ n) := by
  let g := Nat.gcd Q (2 ^ S + 3 ^ n)
  have hgQ : g ∣ Q := Nat.gcd_dvd_left _ _
  have hgSum : g ∣ 2 ^ S + 3 ^ n := Nat.gcd_dvd_right _ _
  have hgPow : g ∣ (2 ^ S) ^ R + (3 ^ n) ^ R :=
    hgSum.trans (hR.nat_add_dvd_pow_add_pow (2 ^ S) (3 ^ n))
  have hp2 : Nat.ModEq Q ((2 ^ S) ^ R) 1 := by
    simpa only [← pow_mul, Nat.mul_comm S R, one_pow] using h2.pow S
  have hp3 : Nat.ModEq Q ((3 ^ n) ^ R) 1 := by
    simpa only [← pow_mul, Nat.mul_comm n R, one_pow] using h3.pow n
  have hp : Nat.ModEq g ((2 ^ S) ^ R + (3 ^ n) ^ R) 2 := by
    simpa using (hp2.add hp3).of_dvd hgQ
  have hgTwo : g ∣ 2 := (hp.dvd_iff (dvd_refl g)).mp hgPow
  have hgOne : g ∣ 1 := by
    have hh := Nat.dvd_gcd hgQ hgTwo
    simpa only [hQ.coprime_two_right.gcd_eq_one] using hh
  exact Nat.dvd_one.mp hgOne

/-- The corresponding natural-number endpoint factor can be cancelled. -/
theorem dvd_nat_endpoint {Q R : ℕ} (hQ : Odd Q) (hR : Odd R)
    (h2 : Nat.ModEq Q (2 ^ R) 1) (h3 : Nat.ModEq Q (3 ^ R) 1)
    (S n h : ℕ) (hd : Q ∣ (2 ^ S + 3 ^ n) * h) : Q ∣ h :=
  (coprime_plus_factor hQ hR h2 h3 S n).dvd_of_dvd_mul_left hd

/-- Signed integer endpoints obey the same divisibility obstruction. -/
theorem dvd_int_endpoint {Q R : ℕ} (hQ : Odd Q) (hR : Odd R)
    (h2 : Nat.ModEq Q (2 ^ R) 1) (h3 : Nat.ModEq Q (3 ^ R) 1)
    (S n : ℕ) (h : ℤ)
    (hd : (Q : ℤ) ∣ ((2 : ℤ) ^ S + 3 ^ n) * h) : (Q : ℤ) ∣ h := by
  have hc := (coprime_plus_factor hQ hR h2 h3 S n).isCoprime
  have hc' : IsCoprime (Q : ℤ) ((2 : ℤ) ^ S + 3 ^ n) := by
    simpa only [Nat.cast_add, Nat.cast_pow, Nat.cast_ofNat] using hc
  exact hc'.dvd_of_dvd_mul_left hd

open WeightedCrossing

/-- A common divisor of all additive coefficients divides the weighted intercept. -/
theorem dvd_intercept (Q : ℕ) (w : List Letter)
    (hd : ∀ ac ∈ w, (Q : ℤ) ∣ ac.2) : (Q : ℤ) ∣ intercept w := by
  induction w with
  | nil => exact dvd_zero _
  | cons ac w ih =>
    obtain ⟨a, c⟩ := ac
    change (Q : ℤ) ∣ 3 ^ w.length * c + 2 ^ a * intercept w
    exact dvd_add (dvd_mul_of_dvd_right (hd (a, c) (by simp)) _)
      (dvd_mul_of_dvd_right (ih (fun ac hac => hd ac (by simp [hac]))) _)

/-- Exact integer arrows imply the weighted endpoint equation. -/
theorem endpoint_of_trace (w : List Letter) {x y : ℤ} (ht : Trace w x y) :
    Endpoint w x y := by
  induction w generalizing x with
  | nil => simpa [Trace, Endpoint, total, intercept] using ht.symm
  | cons ac w ih =>
    obtain ⟨a, c⟩ := ac
    obtain ⟨z, hz, hw⟩ := ht
    have he : 2 ^ total w * y = 3 ^ w.length * z + intercept w := ih hw
    change 2 ^ (a + total w) * y =
      3 ^ (w.length + 1) * x + (3 ^ w.length * c + 2 ^ a * intercept w)
    rw [pow_add, pow_succ]
    linear_combination 2 ^ a * he + 3 ^ w.length * hz

/-- A weighted signed return with addends divisible by an odd-order modulus
has its endpoint divisible by that whole modulus. -/
theorem dvd_of_signed_endpoint {Q R : ℕ} (hQ : Odd Q) (hR : Odd R)
    (h2 : Nat.ModEq Q (2 ^ R) 1) (h3 : Nat.ModEq Q (3 ^ R) 1)
    (w : List Letter) (h : ℤ) (hd : ∀ ac ∈ w, (Q : ℤ) ∣ ac.2)
    (he : Endpoint w (-h) h) : (Q : ℤ) ∣ h := by
  apply dvd_int_endpoint hQ hR h2 h3 (total w) w.length h
  have hc := dvd_intercept Q w hd
  have hid : ((2 : ℤ) ^ total w + 3 ^ w.length) * h = intercept w := by
    unfold Endpoint at he
    linear_combination he
  rwa [hid]

/-- The same obstruction directly for arbitrary exact integer arrows. -/
theorem dvd_of_signed_trace {Q R : ℕ} (hQ : Odd Q) (hR : Odd R)
    (h2 : Nat.ModEq Q (2 ^ R) 1) (h3 : Nat.ModEq Q (3 ^ R) 1)
    (w : List Letter) (h : ℤ) (hd : ∀ ac ∈ w, (Q : ℤ) ∣ ac.2)
    (ht : Trace w (-h) h) : (Q : ℤ) ∣ h :=
  dvd_of_signed_endpoint hQ hR h2 h3 w h hd (endpoint_of_trace w ht)

end LeanLane.OddOrderObstruction

#print axioms LeanLane.OddOrderObstruction.coprime_plus_factor
#print axioms LeanLane.OddOrderObstruction.dvd_nat_endpoint
#print axioms LeanLane.OddOrderObstruction.dvd_int_endpoint
#print axioms LeanLane.OddOrderObstruction.dvd_intercept
#print axioms LeanLane.OddOrderObstruction.endpoint_of_trace
#print axioms LeanLane.OddOrderObstruction.dvd_of_signed_endpoint
#print axioms LeanLane.OddOrderObstruction.dvd_of_signed_trace
