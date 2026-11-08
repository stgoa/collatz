import LeanLane.Words

/-!
# Integer cuts and the two weighted coefficient blocks

The weighted signed-endpoint obstruction used by
`unequal-one-three-half-defect-exclusion`. A letter is a pair consisting
of a natural valuation and an arbitrary integer additive coefficient.
-/

namespace LeanLane.WeightedCrossing

abbrev Letter := ℕ × ℤ

def total (w : List Letter) : ℕ := (w.map Prod.fst).sum

def intercept : List Letter → ℤ
  | [] => 0
  | (a, c) :: w => 3 ^ w.length * c + 2 ^ a * intercept w

def Endpoint (w : List Letter) (x y : ℤ) : Prop :=
  2 ^ total w * y = 3 ^ w.length * x + intercept w

def Trace : List Letter → ℤ → ℤ → Prop
  | [], x, y => x = y
  | (a, c) :: w, x, y => ∃ z : ℤ, 2 ^ a * z = 3 * x + c ∧ Trace w z y

def block (c : ℤ) (w : List ℕ) : List Letter := w.map (fun a => (a, c))

/-- Integer endpoints supply every intermediate integer cut, for arbitrary
integer additive coefficients and natural valuations. -/
theorem trace_of_endpoint (w : List Letter) {x y : ℤ} (h : Endpoint w x y) :
    Trace w x y := by
  induction w generalizing x y with
  | nil => simpa [Endpoint, Trace, total, intercept] using h.symm
  | cons ac w ih =>
    obtain ⟨a, c⟩ := ac
    have hp : (0 : ℤ) < 2 ^ a := by positivity
    have hcop : IsCoprime (2 : ℤ) 3 := ⟨-1, 1, by norm_num⟩
    have he : 2 ^ a * (2 ^ total w * y - intercept w) =
        (3 : ℤ) ^ w.length * (3 * x + c) := by
      simp only [Endpoint, total, List.map_cons, List.sum_cons, List.length_cons,
        intercept, pow_add, pow_succ] at h
      unfold total
      linear_combination h
    have hd : (2 : ℤ) ^ a ∣ 3 ^ w.length * (3 * x + c) :=
      ⟨2 ^ total w * y - intercept w, he.symm⟩
    obtain ⟨z, hz⟩ := (hcop.pow (m := a) (n := w.length)).dvd_of_dvd_mul_left hd
    refine ⟨z, hz.symm, ih ?_⟩
    unfold Endpoint
    rw [hz] at he
    apply mul_left_cancel₀ (ne_of_gt hp)
    linear_combination he

theorem trace_append_iff (u v : List Letter) (x y : ℤ) :
    Trace (u ++ v) x y ↔ ∃ z, Trace u x z ∧ Trace v z y := by
  induction u generalizing x with
  | nil => simp [Trace]
  | cons ac u ih =>
    obtain ⟨a, c⟩ := ac
    simp only [List.cons_append, Trace, ih]
    constructor
    · rintro ⟨z, hz, m, hm, hy⟩
      exact ⟨m, ⟨z, hz, hm⟩, hy⟩
    · rintro ⟨m, ⟨z, hz, hm⟩, hy⟩
      exact ⟨z, hz, m, hm, hy⟩

theorem two_dvd_step {a : ℕ} (ha : 0 < a) (z : ℤ) : (2 : ℤ) ∣ 2 ^ a * z :=
  dvd_mul_of_dvd_left (dvd_pow_self 2 (by omega)) z

theorem pow_two_ge_two {a : ℕ} (ha : 0 < a) : (2 : ℤ) ≤ 2 ^ a := by
  calc
    (2 : ℤ) = 2 ^ (1 : ℕ) := by norm_num
    _ ≤ 2 ^ a := pow_le_pow_right₀ (by norm_num) ha

theorem two_step_negative {a : ℕ} {x y : ℤ} (hx : x < 0)
    (h : (2 : ℤ) ^ a * y = 3 * x + 2) : y < 0 := by
  have hp : (0 : ℤ) < 2 ^ a := by positivity
  have hn : 3 * x + 2 < 0 := by omega
  nlinarith

theorem three_step_nonpositive {a : ℕ} {x y : ℤ} (ha : 0 < a) (hx : x ≤ 0)
    (h : (2 : ℤ) ^ a * y = 3 * x + 3) : y ≤ 0 := by
  have hxneg : x < 0 := by
    by_contra hn
    have heq : x = 0 := by omega
    have hd := two_dvd_step ha y
    rw [h, heq] at hd
    norm_num at hd
  have hp : (0 : ℤ) < 2 ^ a := by positivity
  have hn : 3 * x + 3 ≤ 0 := by omega
  nlinarith

/-- Below 2, an integral positive-valuation `+2` step must start at most at 0. -/
theorem two_step_source_nonpositive {a : ℕ} {x y : ℤ} (ha : 0 < a) (hx : x ≤ 1)
    (h : (2 : ℤ) ^ a * y = 3 * x + 2) : x ≤ 0 := by
  by_contra hn
  have heq : x = 1 := by omega
  have hd := two_dvd_step ha y
  rw [h, heq] at hd
  norm_num at hd

theorem two_step_le_one {a : ℕ} {x y : ℤ} (ha : 0 < a) (hx : x ≤ 1)
    (h : (2 : ℤ) ^ a * y = 3 * x + 2) : y ≤ 1 := by
  have hx0 := two_step_source_nonpositive ha hx h
  have hp := pow_two_ge_two ha
  by_contra hn
  have hy : 2 ≤ y := by omega
  nlinarith

theorem two_step_large_nonpositive {a : ℕ} {x y : ℤ} (ha : 2 ≤ a) (hx : x ≤ 1)
    (h : (2 : ℤ) ^ a * y = 3 * x + 2) : y ≤ 0 := by
  have hx0 := two_step_source_nonpositive (by omega) hx h
  have hp : (4 : ℤ) ≤ 2 ^ a := by
    calc
      (4 : ℤ) = 2 ^ (2 : ℕ) := by norm_num
      _ ≤ 2 ^ a := pow_le_pow_right₀ (by norm_num) ha
  by_contra hn
  have hy : 1 ≤ y := by omega
  nlinarith

theorem two_block_negative (w : List ℕ) {x y : ℤ} (hx : x < 0)
    (h : Trace (block 2 w) x y) : y < 0 := by
  induction w generalizing x with
  | nil => simpa [block, Trace] using h ▸ hx
  | cons a w ih =>
    obtain ⟨z, hz, ht⟩ := h
    exact ih (two_step_negative hx hz) ht

theorem three_block_nonpositive (w : List ℕ) (hw : ∀ a ∈ w, 0 < a)
    {x y : ℤ} (hx : x ≤ 0) (h : Trace (block 3 w) x y) : y ≤ 0 := by
  induction w generalizing x with
  | nil => simpa [block, Trace] using h ▸ hx
  | cons a w ih =>
    obtain ⟨z, hz, ht⟩ := h
    exact ih (fun b hb => hw b (by simp [hb]))
      (three_step_nonpositive (hw a (by simp)) hx hz) ht

theorem two_block_le_one (w : List ℕ) (hw : ∀ a ∈ w, 0 < a)
    {x y : ℤ} (hx : x ≤ 1) (h : Trace (block 2 w) x y) : y ≤ 1 := by
  induction w generalizing x with
  | nil => simpa [block, Trace] using h ▸ hx
  | cons a w ih =>
    obtain ⟨z, hz, ht⟩ := h
    exact ih (fun b hb => hw b (by simp [hb]))
      (two_step_le_one (hw a (by simp)) hx hz) ht

/-- Coefficients 2 followed by 3 cannot take an integral segment from
a negative integer to a positive integer. -/
theorem no_crossing_two_three (u v : List ℕ) (hv : ∀ a ∈ v, 0 < a)
    {x y : ℤ} (hx : x < 0) (hy : 0 < y) :
    ¬ Endpoint (block 2 u ++ block 3 v) x y := by
  intro he
  obtain ⟨z, hu, ht⟩ := (trace_append_iff _ _ _ _).mp (trace_of_endpoint _ he)
  have hz := two_block_negative u hx hu
  have hn := three_block_nonpositive v hv (le_of_lt hz) ht
  omega

/-- Coefficients 3 followed by 2 cannot cross from negative to positive
when the final valuation is at least 2. -/
theorem no_crossing_three_two (u v : List ℕ) (a : ℕ) (ha : 2 ≤ a)
    (hu : ∀ b ∈ u, 0 < b) (hv : ∀ b ∈ v, 0 < b)
    {x y : ℤ} (hx : x < 0) (hy : 0 < y) :
    ¬ Endpoint (block 3 u ++ block 2 (v ++ [a])) x y := by
  intro he
  obtain ⟨z, h3, h2⟩ := (trace_append_iff _ _ _ _).mp (trace_of_endpoint _ he)
  have hz := three_block_nonpositive u hu (le_of_lt hx) h3
  have hsplit : block 2 (v ++ [a]) = block 2 v ++ [(a, 2)] := by simp [block]
  rw [hsplit] at h2
  obtain ⟨q, hq, hf⟩ := (trace_append_iff _ _ _ _).mp h2
  have hq1 := two_block_le_one v hv (by omega : z ≤ 1) hq
  obtain ⟨r, hr, heq⟩ := hf
  have hry : r = y := heq
  have hn := two_step_large_nonpositive ha hq1 hr
  omega

/-- The final-valuation condition is necessary: coefficients `(3, 2)`
and valuations `(1, 1)` give the integral segment `-1 → 0 → 1`. -/
theorem zero_interface_control : Trace [(1, 3), (1, 2)] (-1) 1 ∧
    Endpoint [(1, 3), (1, 2)] (-1) 1 := by
  constructor
  · exact ⟨0, by norm_num, 1, by norm_num, rfl⟩
  · norm_num [Endpoint, total, intercept]

#print axioms trace_of_endpoint
#print axioms no_crossing_two_three
#print axioms no_crossing_three_two
#print axioms zero_interface_control

end LeanLane.WeightedCrossing
