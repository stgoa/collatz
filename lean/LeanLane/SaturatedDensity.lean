import LeanLane.Words

/-!
# `LeanLane.SaturatedDensity`: saturated sets of the Collatz map meet every class modulo `2^k 3^b`

`T` is the Collatz map on `ℕ`; a set `B` of positive integers is *saturated* when `x ∈ B ↔ T x ∈ B` for every
positive `x`. Theorem `saturated_dense`: a nonempty saturated set contains an element in every residue class modulo
`2^k * 3^b`. Prose: `areas/invariants/results/saturated-sets-meet-residue-classes-six-smooth-moduli`.
-/

namespace LeanLane
namespace SaturatedDensity

/-- The Collatz map. -/
def T (n : ℕ) : ℕ := if n % 2 = 0 then n / 2 else 3 * n + 1

/-- `B ⊆ ℕ` is saturated: it consists of positive integers and membership is invariant under one step of `T`. -/
structure Saturated (B : Set ℕ) : Prop where
  pos : ∀ x ∈ B, 0 < x
  step : ∀ x, 0 < x → (x ∈ B ↔ T x ∈ B)

variable {B : Set ℕ} (hB : Saturated B)
include hB

theorem mem_double {x : ℕ} (hx : x ∈ B) : 2 * x ∈ B := by
  have hpos := hB.pos x hx
  have hT : T (2 * x) = x := by
    unfold T
    have h0 : 2 * x % 2 = 0 := by omega
    rw [ite_eq_left h0]; omega
  exact (hB.step (2 * x) (by omega)).2 (by rw [hT]; exact hx)

theorem mem_pow_double {x : ℕ} (hx : x ∈ B) (j : ℕ) : 2 ^ j * x ∈ B := by
  induction j with
  | zero => simpa using hx
  | succ j ih =>
    have := mem_double hB ih
    rw [pow_succ]; convert this using 1; ring

theorem mem_forward {x : ℕ} (hx : x ∈ B) (hodd : x % 2 = 1) : 3 * x + 1 ∈ B := by
  have hpos := hB.pos x hx
  have hT : T x = 3 * x + 1 := by
    unfold T; rw [ite_eq_right (by omega)]
  have h := (hB.step x hpos).1 hx
  rw [hT] at h
  exact h

theorem mem_inverse {x : ℕ} (hx : x ∈ B) (h4 : x % 6 = 4) : (x - 1) / 3 ∈ B := by
  have hT : T ((x - 1) / 3) = x := by
    unfold T; rw [ite_eq_right (by omega)]; omega
  exact (hB.step ((x - 1) / 3) (by omega)).2 (by rw [hT]; exact hx)

theorem exists_odd (hne : B.Nonempty) : ∃ x ∈ B, x % 2 = 1 := by
  obtain ⟨x, hx⟩ := hne
  induction x using Nat.strong_induction_on with
  | _ x ih =>
    by_cases hodd : x % 2 = 1
    · exact ⟨x, hx, hodd⟩
    · have hpos := hB.pos x hx
      have hT : T x = x / 2 := by unfold T; rw [ite_eq_left (by omega)]
      have hx2 : x / 2 ∈ B := by have := (hB.step x hpos).1 hx; rwa [hT] at this
      exact ih (x / 2) (by omega) hx2

theorem exists_not_three_dvd (hne : B.Nonempty) : ∃ y ∈ B, ¬ 3 ∣ y := by
  obtain ⟨x, hx, hodd⟩ := exists_odd hB hne
  by_cases h3 : 3 ∣ x
  · exact ⟨3 * x + 1, mem_forward hB hx hodd, by omega⟩
  · exact ⟨x, hx, h3⟩

omit hB

/-- `4^(3^n) = 1 + 3^(n+1)` modulo `3^(n+2)`. -/
theorem four_pow_three_pow (n : ℕ) : ∃ m : ℤ, (4 : ℤ) ^ (3 ^ n) = 1 + 3 ^ (n + 1) + m * 3 ^ (n + 2) := by
  induction n with
  | zero => exact ⟨0, by norm_num⟩
  | succ n ih =>
    obtain ⟨m, hm⟩ := ih
    refine ⟨m + 3 ^ n * (1 + 3 * m) ^ 2 + 3 ^ (2 * n) * (1 + 3 * m) ^ 3, ?_⟩
    rw [pow_succ, pow_mul, hm]; ring

/-- `4^(3^n s) = 1 + s 3^(n+1)` modulo `3^(n+2)`. -/
theorem four_pow_three_pow_mul (n s : ℕ) :
    ∃ m : ℤ, (4 : ℤ) ^ (3 ^ n * s) = 1 + s * 3 ^ (n + 1) + m * 3 ^ (n + 2) := by
  induction s with
  | zero => exact ⟨0, by simp⟩
  | succ s ih =>
    obtain ⟨ms, hs⟩ := ih
    obtain ⟨m, hm⟩ := four_pow_three_pow n
    refine ⟨m + ms + s * 3 ^ n + s * 3 ^ (n + 1) * m + ms * 3 ^ (n + 1) + ms * m * 3 ^ (n + 2), ?_⟩
    rw [Nat.mul_succ, pow_add, hs, hm]; push_cast; ring

/-- 2 is a primitive root modulo every power of 3: the powers `2^j y`, `j ≥ 1`, of an integer `y` prime to 3 meet
every class prime to 3 modulo `3^(n+1)`. -/
theorem two_pow_mul_surj (y η : ℤ) (hy : ¬ (3 : ℤ) ∣ y) (hη : ¬ (3 : ℤ) ∣ η) (n : ℕ) :
    ∃ j : ℕ, 1 ≤ j ∧ (3 : ℤ) ^ (n + 1) ∣ 2 ^ j * y - η := by
  induction n with
  | zero =>
    have hyz : ((y : ℤ) : ZMod 3) ≠ 0 := fun h => hy ((ZMod.intCast_zmod_eq_zero_iff_dvd y 3).1 h)
    have hηz : ((η : ℤ) : ZMod 3) ≠ 0 := fun h => hη ((ZMod.intCast_zmod_eq_zero_iff_dvd η 3).1 h)
    have key : ∀ a b : ZMod 3, a ≠ 0 → b ≠ 0 → 2 ^ 2 * a - b = 0 ∨ 2 ^ 1 * a - b = 0 := by decide
    rcases key _ _ hyz hηz with h | h
    · refine ⟨2, by norm_num, ?_⟩
      rw [zero_add, pow_one]
      exact (ZMod.intCast_zmod_eq_zero_iff_dvd _ 3).1 (by push_cast; exact h)
    · refine ⟨1, by norm_num, ?_⟩
      rw [zero_add, pow_one]
      exact (ZMod.intCast_zmod_eq_zero_iff_dvd _ 3).1 (by push_cast; exact h)
  | succ n ih =>
    obtain ⟨j, hj, t, ht⟩ := ih
    -- choose s ∈ {0, 1, 2} with 3 ∣ t + s η
    have hηz : ((η : ℤ) : ZMod 3) ≠ 0 := fun h => hη ((ZMod.intCast_zmod_eq_zero_iff_dvd η 3).1 h)
    have key3 : ∀ a b : ZMod 3, b ≠ 0 → a + 0 * b = 0 ∨ a + 1 * b = 0 ∨ a + 2 * b = 0 := by decide
    have hs : (3 : ℤ) ∣ t + 0 * η ∨ (3 : ℤ) ∣ t + 1 * η ∨ (3 : ℤ) ∣ t + 2 * η := by
      rcases key3 (t : ZMod 3) (η : ZMod 3) hηz with h | h | h
      · exact Or.inl ((ZMod.intCast_zmod_eq_zero_iff_dvd _ 3).1 (by push_cast; exact h))
      · exact Or.inr (Or.inl ((ZMod.intCast_zmod_eq_zero_iff_dvd _ 3).1 (by push_cast; exact h)))
      · exact Or.inr (Or.inr ((ZMod.intCast_zmod_eq_zero_iff_dvd _ 3).1 (by push_cast; exact h)))
    have key : ∀ s : ℕ, (3 : ℤ) ∣ t + s * η →
        (3 : ℤ) ^ (n + 2) ∣ 2 ^ (j + 2 * 3 ^ n * s) * y - η := by
      intro s hsη
      obtain ⟨w, hw⟩ := hsη
      obtain ⟨m, hm⟩ := four_pow_three_pow_mul n s
      have h2 : (2 : ℤ) ^ (j + 2 * 3 ^ n * s) * y = 4 ^ (3 ^ n * s) * (2 ^ j * y) := by
        rw [pow_add, show (4 : ℤ) = 2 ^ 2 by norm_num, ← pow_mul]
        rw [show 2 * (3 ^ n * s) = 2 * 3 ^ n * s by ring]; ring
      have hy' : (2 : ℤ) ^ j * y = η + t * 3 ^ (n + 1) := by linarith
      refine ⟨w + s * t * 3 ^ n + m * η + m * t * 3 ^ (n + 1), ?_⟩
      rw [h2, hy', hm]
      have h3 : (t : ℤ) = 3 * w - s * η := by linarith
      rw [h3]; ring
    rcases hs with h | h | h
    · exact ⟨j + 2 * 3 ^ n * 0, by omega, by simpa using key 0 (by simpa using h)⟩
    · exact ⟨j + 2 * 3 ^ n * 1, by omega, key 1 (by simpa using h)⟩
    · exact ⟨j + 2 * 3 ^ n * 2, by omega, key 2 (by simpa using h)⟩

include hB

/-- Base case: an element of `B` in every class modulo `3^b`. -/
theorem exists_modEq_three_pow (hne : B.Nonempty) (b ε : ℕ) : ∃ x ∈ B, x ≡ ε [MOD 3 ^ b] := by
  obtain ⟨y, hy, hy3⟩ := exists_not_three_dvd hB hne
  have hy3' : ¬ (3 : ℤ) ∣ (y : ℤ) := by exact_mod_cast hy3
  have hη : ¬ (3 : ℤ) ∣ ((1 + 3 * ε : ℕ) : ℤ) := by push_cast; omega
  obtain ⟨j, hj, hdvd⟩ := two_pow_mul_surj (y : ℤ) ((1 + 3 * ε : ℕ) : ℤ) hy3' hη b
  set X := 2 ^ j * y with hXdef
  have hX : X ∈ B := mem_pow_double hB hy j
  have hmod : 1 + 3 * ε ≡ X [MOD 3 ^ (b + 1)] := by
    rw [Nat.modEq_iff_dvd]; push_cast at hdvd ⊢; exact hdvd
  have hmod3 : 1 + 3 * ε ≡ X [MOD 3] := Nat.ModEq.of_dvd (dvd_pow_self 3 (Nat.succ_ne_zero b)) hmod
  have hX3 : X % 3 = 1 := by
    have := hmod3; unfold Nat.ModEq at this; omega
  have hX2 : X % 2 = 0 := by
    obtain ⟨j', rfl⟩ : ∃ j', j = j' + 1 := ⟨j - 1, by omega⟩
    have hX' : X = 2 * (2 ^ j' * y) := by rw [hXdef]; ring
    rw [hX']; exact Nat.mul_mod_right 2 _
  have hX6 : X % 6 = 4 := by omega
  refine ⟨(X - 1) / 3, mem_inverse hB hX hX6, ?_⟩
  have h3x : 3 * ((X - 1) / 3) + 1 = X := by omega
  have h1 : 3 * ε + 1 ≡ 3 * ((X - 1) / 3) + 1 [MOD 3 ^ (b + 1)] := by
    rw [h3x]; convert hmod using 1; ring
  have h2 : 3 * ε ≡ 3 * ((X - 1) / 3) [MOD 3 * 3 ^ b] := by
    rw [← pow_succ']; exact Nat.ModEq.add_right_cancel' 1 h1
  exact (Nat.ModEq.mul_left_cancel' (by norm_num) h2).symm

/-- The induction: an element of `B` with prescribed classes modulo `2^k` and `3^b`. -/
theorem exists_modEq_pow (hne : B.Nonempty) :
    ∀ k b r ε : ℕ, ∃ x ∈ B, x ≡ r [MOD 2 ^ k] ∧ x ≡ ε [MOD 3 ^ b] := by
  intro k
  induction k with
  | zero =>
    intro b r ε
    obtain ⟨x, hx, hmod⟩ := exists_modEq_three_pow hB hne b ε
    exact ⟨x, hx, by simp [Nat.modEq_one], hmod⟩
  | succ k ih =>
    intro b r ε
    have hodd3 : (3 ^ b) % 2 = 1 := Nat.odd_iff.mp (Odd.pow (by decide))
    have hodd3' : (3 ^ (b + 1)) % 2 = 1 := Nat.odd_iff.mp (Odd.pow (by decide))
    by_cases hr : r % 2 = 0
    · -- even target: double an element of the smaller class
      obtain ⟨y, hy, hy2, hy3⟩ := ih b (r / 2) (ε * ((3 ^ b + 1) / 2))
      refine ⟨2 * y, mem_double hB hy, ?_, ?_⟩
      · have := Nat.ModEq.mul_left' 2 hy2
        rw [pow_succ']; convert this using 2; omega
      · have := Nat.ModEq.mul_left 2 hy3
        refine this.trans ?_
        have h2 : 2 * (ε * ((3 ^ b + 1) / 2)) = ε + ε * 3 ^ b := by
          generalize 3 ^ b = M at hodd3 ⊢
          have : 2 * ((M + 1) / 2) = M + 1 := by omega
          calc 2 * (ε * ((M + 1) / 2)) = ε * (2 * ((M + 1) / 2)) := by ring
            _ = ε * (M + 1) := by rw [this]
            _ = ε + ε * M := by ring
        rw [h2]; exact Nat.add_mul_mod_self_right ε ε (3 ^ b)
    · -- odd target: lift through one inverse step
      obtain ⟨y, hy, hy2, hy3⟩ := ih (b + 1) ((3 * r + 1) / 2) ((1 + 3 * ε) * ((3 ^ (b + 1) + 1) / 2))
      set X := 2 * y with hXdef
      have hX : X ∈ B := mem_double hB hy
      have hX2 : X ≡ 3 * r + 1 [MOD 2 ^ (k + 1)] := by
        have := Nat.ModEq.mul_left' 2 hy2
        rw [pow_succ']; convert this using 2; omega
      have hX3 : X ≡ 1 + 3 * ε [MOD 3 ^ (b + 1)] := by
        have := Nat.ModEq.mul_left 2 hy3
        refine this.trans ?_
        have h2 : 2 * ((1 + 3 * ε) * ((3 ^ (b + 1) + 1) / 2)) = (1 + 3 * ε) + (1 + 3 * ε) * 3 ^ (b + 1) := by
          generalize 3 ^ (b + 1) = M at hodd3' ⊢
          have : 2 * ((M + 1) / 2) = M + 1 := by omega
          calc 2 * ((1 + 3 * ε) * ((M + 1) / 2)) = (1 + 3 * ε) * (2 * ((M + 1) / 2)) := by ring
            _ = (1 + 3 * ε) * (M + 1) := by rw [this]
            _ = (1 + 3 * ε) + (1 + 3 * ε) * M := by ring
        rw [h2]; exact Nat.add_mul_mod_self_right _ _ _
      have hmod3 : X ≡ 1 + 3 * ε [MOD 3] := Nat.ModEq.of_dvd (dvd_pow_self 3 (Nat.succ_ne_zero b)) hX3
      have hX3' : X % 3 = 1 := by unfold Nat.ModEq at hmod3; omega
      have hXeven : X % 2 = 0 := by omega
      have hX6 : X % 6 = 4 := by omega
      refine ⟨(X - 1) / 3, mem_inverse hB hX hX6, ?_, ?_⟩
      · have h3x : 3 * ((X - 1) / 3) + 1 = X := by omega
        have h1 : 3 * ((X - 1) / 3) + 1 ≡ 3 * r + 1 [MOD 2 ^ (k + 1)] := by rw [h3x]; exact hX2
        have h2 : 3 * ((X - 1) / 3) ≡ 3 * r [MOD 2 ^ (k + 1)] := Nat.ModEq.add_right_cancel' 1 h1
        exact Nat.ModEq.cancel_left_of_coprime (by
          have : Nat.Coprime (2 ^ (k + 1)) 3 := Nat.Coprime.pow_left _ (by decide)
          exact this) h2
      · have h3x : 3 * ((X - 1) / 3) + 1 = X := by omega
        have h1 : 3 * ((X - 1) / 3) + 1 ≡ 3 * ε + 1 [MOD 3 ^ (b + 1)] := by
          rw [h3x]; convert hX3 using 1; ring
        have h2 : 3 * ((X - 1) / 3) ≡ 3 * ε [MOD 3 * 3 ^ b] := by
          rw [← pow_succ']; exact Nat.ModEq.add_right_cancel' 1 h1
        exact Nat.ModEq.mul_left_cancel' (by norm_num) h2

/-- **Theorem.** A nonempty saturated set of the Collatz map meets every residue class modulo `2^k * 3^b`. -/
theorem saturated_dense (hne : B.Nonempty) (k b r : ℕ) : ∃ x ∈ B, x ≡ r [MOD 2 ^ k * 3 ^ b] := by
  obtain ⟨x, hx, h2, h3⟩ := exists_modEq_pow hB hne k b r r
  refine ⟨x, hx, ?_⟩
  have hcop : Nat.Coprime (2 ^ k) (3 ^ b) := Nat.Coprime.pow _ _ (by decide)
  exact (Nat.modEq_and_modEq_iff_modEq_mul hcop).1 ⟨h2, h3⟩

end SaturatedDensity
end LeanLane

#print axioms LeanLane.SaturatedDensity.two_pow_mul_surj
#print axioms LeanLane.SaturatedDensity.exists_modEq_pow
#print axioms LeanLane.SaturatedDensity.saturated_dense
