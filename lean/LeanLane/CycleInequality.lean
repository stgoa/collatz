import LeanLane.CycleEquation

/-!
# `LeanLane.CycleInequality`: the cycle inequality and the lattice lemma of the period bound

Formal companion of Theorems 1 and 2 of
`areas/cycles/results/cycle-length-lower-bound-from-convergents/README.md`.

* `prod_identity`: for a cycle of the odd-only `3x+q` map following `w` (length `m`),
  `2^(Σw) · Π x_i = Π (3 x_i + q)` over one period.
* `three_pow_lt` and `pow_le_bound`: for `q = 1` and positive states with minimum at least `L`,
  `3^m < 2^A` and `2^A · L^m ≤ (3L + 1)^m` (strict when some state exceeds `L`).
* `lattice_lemma`: for reals `θ` and integers `p, q, p', q'` with `p'q − pq' = ±1`, `0 < q < q'`, errors
  `e = qθ − p`, `e' = q'θ − p'` of opposite signs, and an integer pair `(m, A)` with `q ≤ m < q'` and
  `A − mθ > 0`: writing `m = xq + yq'`, `A = xp + yp'`, one has `A − mθ = |x||e| + |y||e'|`, with `y ≥ 1, x ≤ −1`
  when `e > 0` and `x ≥ 1, y ≤ 0` when `e < 0`.
-/

namespace LeanLane
namespace CycleInequality

open LeanLane.Words LeanLane.CycleEquation Finset

/-- `Σ_{i<|w|} w_i = Σ w`. -/
theorem sum_getD (w : List ℕ) : ∑ i ∈ range w.length, w.getD i 0 = w.sum := by
  induction w with
  | nil => simp
  | cons a w ih =>
    rw [List.length_cons, sum_range_succ', List.sum_cons, ← ih]
    simp [add_comm]

/-- The product identity of a cycle: `2^(Σw) Π x_i = Π (3 x_i + q)` over one period. -/
theorem prod_identity {q : ℤ} {w : List ℕ} {x : ℕ → ℤ} (h : IsCycle q w x) (hm : 0 < w.length) :
    2 ^ w.sum * ∏ i ∈ range w.length, x i = ∏ i ∈ range w.length, (3 * x i + q) := by
  set m := w.length with hm_def
  have hstep : ∀ i ∈ range m, 2 ^ (w.getD i 0) * x (i + 1) = 3 * x i + q := by
    intro i hi
    have := h.step i
    rwa [Nat.mod_eq_of_lt (mem_range.mp hi)] at this
  have hprod : ∏ i ∈ range m, (2 ^ (w.getD i 0) * x (i + 1)) = ∏ i ∈ range m, (3 * x i + q) :=
    prod_congr rfl hstep
  rw [prod_mul_distrib, prod_pow_eq_pow_sum, sum_getD] at hprod
  -- the shifted product equals the unshifted one, by periodicity
  have hshift : ∏ i ∈ range m, x (i + 1) = ∏ i ∈ range m, x i := by
    obtain ⟨n, hn⟩ : ∃ n, m = n + 1 := ⟨m - 1, by omega⟩
    rw [hn, prod_range_succ, prod_range_succ']
    have hper : x (n + 1) = x 0 := by
      have := h.periodic 0
      rw [zero_add, ← hm_def, hn] at this
      exact this
    rw [hper, mul_comm]
  rw [hshift] at hprod
  exact hprod

/-- `3^m < 2^A` for a cycle of `3x+1` with positive states, unless every factor `3x_i + 1 = 3x_i`, which is
impossible; so the product of the `3x_i + 1` exceeds `3^m Π x_i` strictly. -/
theorem three_pow_lt {w : List ℕ} {x : ℕ → ℤ} (h : IsCycle 1 w x) (hm : 0 < w.length)
    (hpos : ∀ i, 0 < x i) : (3 : ℤ) ^ w.length < 2 ^ w.sum := by
  have hid := prod_identity h hm
  have hP : 0 < ∏ i ∈ range w.length, x i := prod_pos fun i _ => hpos i
  have h3 : (3 : ℤ) ^ w.length * ∏ i ∈ range w.length, x i = ∏ i ∈ range w.length, (3 * x i) := by
    rw [prod_mul_distrib, prod_const, card_range]
  have hlt : 3 ^ w.length * ∏ i ∈ range w.length, x i < ∏ i ∈ range w.length, (3 * x i + 1) := by
    rw [h3]
    exact Finset.prod_lt_prod_of_nonempty₀ (fun i _ => mul_pos (by norm_num) (hpos i)) (fun i _ => by linarith)
      (nonempty_range_iff.mpr (by omega))
  rw [← hid] at hlt
  exact lt_of_mul_lt_mul_right hlt hP.le

/-- `2^A · L^m ≤ (3L + 1)^m` when every state is at least `L ≥ 1`. -/
theorem pow_le_bound {w : List ℕ} {x : ℕ → ℤ} (h : IsCycle 1 w x) (hm : 0 < w.length)
    (L : ℤ) (hL : 0 < L) (hmin : ∀ i, L ≤ x i) :
    2 ^ w.sum * L ^ w.length ≤ (3 * L + 1) ^ w.length := by
  have hid := prod_identity h hm
  have hpos : ∀ i, 0 < x i := fun i => lt_of_lt_of_le hL (hmin i)
  have hP : 0 < ∏ i ∈ range w.length, x i := prod_pos fun i _ => hpos i
  -- termwise: (3 x_i + 1) L ≤ x_i (3L + 1)  ⟺  L ≤ x_i
  have hterm : ∏ i ∈ range w.length, ((3 * x i + 1) * L) ≤ ∏ i ∈ range w.length, (x i * (3 * L + 1)) :=
    Finset.prod_le_prod₀ (fun i _ => mul_nonneg (by linarith [hpos i]) hL.le) (fun i _ => by nlinarith [hmin i])
  rw [prod_mul_distrib, prod_const, card_range, prod_mul_distrib, prod_const, card_range, ← hid] at hterm
  -- hterm : 2^A Π x · L^m ≤ Π x · (3L+1)^m
  have : (∏ i ∈ range w.length, x i) * (2 ^ w.sum * L ^ w.length) ≤
      (∏ i ∈ range w.length, x i) * (3 * L + 1) ^ w.length := by
    calc (∏ i ∈ range w.length, x i) * (2 ^ w.sum * L ^ w.length)
        = 2 ^ w.sum * (∏ i ∈ range w.length, x i) * L ^ w.length := by ring
      _ ≤ (∏ i ∈ range w.length, x i) * (3 * L + 1) ^ w.length := hterm
  exact le_of_mul_le_mul_left this hP

/-- The lattice lemma behind Theorem 2 of the period-bound node. -/
theorem lattice_lemma (θ : ℝ) (p q p' q' : ℤ) (hdet : p' * q - p * q' = 1 ∨ p' * q - p * q' = -1)
    (hq : 0 < q) (hqq : q < q') (hsign : (q * θ - p) * (q' * θ - p') < 0)
    (m A : ℤ) (hm1 : q ≤ m) (hm2 : m < q') (hA : 0 < A - m * θ) :
    let d : ℤ := p' * q - p * q'
    let x : ℤ := d * (m * p' - A * q')
    let y : ℤ := d * (A * q - m * p)
    m = x * q + y * q' ∧ A = x * p + y * p' ∧
    (0 < q * θ - p → 1 ≤ y ∧ x ≤ -1) ∧ (q * θ - p < 0 → 1 ≤ x ∧ y ≤ 0) ∧
    A - m * θ = |(x : ℝ)| * |q * θ - p| + |(y : ℝ)| * |q' * θ - p'| := by
  intro d x y
  have hd2 : d * d = 1 := by rcases hdet with h | h <;> simp [d, h]
  have hxq : m = x * q + y * q' := by
    have : x * q + y * q' = d * d * m := by simp only [x, y, d]; ring
    rw [this, hd2, one_mul]
  have hxp : A = x * p + y * p' := by
    have : x * p + y * p' = d * d * A := by simp only [x, y, d]; ring
    rw [this, hd2, one_mul]
  refine ⟨hxq, hxp, ?_, ?_, ?_⟩
  -- the real identity A - mθ = -(x e + y e')
  all_goals
    have hreal : (A : ℝ) - m * θ = -((x : ℝ) * (q * θ - p) + (y : ℝ) * (q' * θ - p')) := by
      have h1 : (m : ℝ) = x * q + y * q' := by exact_mod_cast hxq
      have h2 : (A : ℝ) = x * p + y * p' := by exact_mod_cast hxp
      rw [h1, h2]; ring
  · intro he
    have he' : q' * θ - p' < 0 := by
      by_contra hcon; push_neg at hcon
      have := mul_nonneg he.le hcon; linarith
    -- y ≥ 1: otherwise x < 0 and m < 0
    have hy : 1 ≤ y := by
      by_contra hcon; push_neg at hcon
      have hy0 : (y : ℝ) ≤ 0 := by exact_mod_cast (Int.lt_add_one_iff.mp hcon)
      have hye : 0 ≤ (y : ℝ) * (q' * θ - p') := mul_nonneg_of_nonpos_of_nonpos hy0 he'.le
      have hxe : (x : ℝ) * (q * θ - p) < 0 := by linarith
      have hx0 : (x : ℝ) < 0 := by
        by_contra hx; push_neg at hx
        have := mul_nonneg hx he.le; linarith
      have hxi : x ≤ -1 := by
        have : x < 0 := by exact_mod_cast hx0
        omega
      have : m < 0 := by
        have hq'pos : 0 < q' := by omega
        nlinarith [hxq, hxi, hcon, hq'pos]
      omega
    refine ⟨hy, ?_⟩
    have hq'pos : 0 < q' := by omega
    -- x ≤ -1 from m < q' and y ≥ 1
    by_contra hcon; push_neg at hcon
    have : m ≥ q' := by nlinarith [hxq, hy, hcon, hq]
    omega
  · intro he
    have he' : 0 < q' * θ - p' := by
      by_contra hcon; push_neg at hcon
      have := mul_nonneg_of_nonpos_of_nonpos he.le hcon; linarith
    have hx : 1 ≤ x := by
      by_contra hcon; push_neg at hcon
      have hx0 : (x : ℝ) ≤ 0 := by exact_mod_cast (Int.lt_add_one_iff.mp hcon)
      have hxe : 0 ≤ (x : ℝ) * (q * θ - p) := mul_nonneg_of_nonpos_of_nonpos hx0 he.le
      have hye : (y : ℝ) * (q' * θ - p') < 0 := by linarith
      have hy0 : (y : ℝ) < 0 := by
        by_contra hy; push_neg at hy
        have := mul_nonneg hy he'.le; linarith
      have hyi : y ≤ -1 := by
        have : y < 0 := by exact_mod_cast hy0
        omega
      have : m < 0 := by
        have hq'pos : 0 < q' := by omega
        nlinarith [hxq, hyi, hcon, hq'pos, hq]
      omega
    refine ⟨hx, ?_⟩
    by_contra hcon; push_neg at hcon
    have : m ≥ q' := by nlinarith [hxq, hx, hcon, hq]
    omega
  · -- the absolute-value form, by the sign cases
    rcases lt_or_gt_of_ne (show q * θ - p ≠ 0 from fun h0 => by rw [h0, zero_mul] at hsign; exact lt_irrefl _ hsign)
      with he | he
    · have he' : 0 < q' * θ - p' := by
        by_contra hcon; push_neg at hcon
        have := mul_nonneg_of_nonpos_of_nonpos he.le hcon; linarith
      have hx : 1 ≤ x := by
        by_contra hcon; push_neg at hcon
        have hx0 : (x : ℝ) ≤ 0 := by exact_mod_cast (Int.lt_add_one_iff.mp hcon)
        have hxe : 0 ≤ (x : ℝ) * (q * θ - p) := mul_nonneg_of_nonpos_of_nonpos hx0 he.le
        have hye : (y : ℝ) * (q' * θ - p') < 0 := by linarith
        have hy0 : (y : ℝ) < 0 := by
          by_contra hy; push_neg at hy
          have := mul_nonneg hy he'.le; linarith
        have hyi : y ≤ -1 := by
          have : y < 0 := by exact_mod_cast hy0
          omega
        have : m < 0 := by
          have hq'pos : 0 < q' := by omega
          nlinarith [hxq, hyi, hcon, hq'pos, hq]
        omega
      have hy : y ≤ 0 := by
        by_contra hcon; push_neg at hcon
        have : m ≥ q' := by nlinarith [hxq, hx, hcon, hq]
        omega
      have hxr : (0 : ℝ) ≤ x := by exact_mod_cast (by omega : (0 : ℤ) ≤ x)
      have hyr : (y : ℝ) ≤ 0 := by exact_mod_cast hy
      rw [hreal, abs_of_nonneg hxr, abs_of_neg he, abs_of_nonpos hyr, abs_of_pos he']
      ring
    · have he' : q' * θ - p' < 0 := by
        by_contra hcon; push_neg at hcon
        have := mul_nonneg he.le hcon; linarith
      have hy : 1 ≤ y := by
        by_contra hcon; push_neg at hcon
        have hy0 : (y : ℝ) ≤ 0 := by exact_mod_cast (Int.lt_add_one_iff.mp hcon)
        have hye : 0 ≤ (y : ℝ) * (q' * θ - p') := mul_nonneg_of_nonpos_of_nonpos hy0 he'.le
        have hxe : (x : ℝ) * (q * θ - p) < 0 := by linarith
        have hx0 : (x : ℝ) < 0 := by
          by_contra hx; push_neg at hx
          have := mul_nonneg hx he.le; linarith
        have hxi : x ≤ -1 := by
          have : x < 0 := by exact_mod_cast hx0
          omega
        have : m < 0 := by
          have hq'pos : 0 < q' := by omega
          nlinarith [hxq, hxi, hcon, hq'pos]
        omega
      have hx : x ≤ -1 := by
        by_contra hcon; push_neg at hcon
        have hq'pos : 0 < q' := by omega
        have : m ≥ q' := by nlinarith [hxq, hy, hcon, hq]
        omega
      have hxr : (x : ℝ) ≤ 0 := by exact_mod_cast (by omega : x ≤ 0)
      have hyr : (0 : ℝ) ≤ y := by exact_mod_cast (by omega : (0 : ℤ) ≤ y)
      rw [hreal, abs_of_nonpos hxr, abs_of_pos he, abs_of_nonneg hyr, abs_of_neg he']
      ring

end CycleInequality
end LeanLane

#print axioms LeanLane.CycleInequality.prod_identity
#print axioms LeanLane.CycleInequality.three_pow_lt
#print axioms LeanLane.CycleInequality.pow_le_bound
#print axioms LeanLane.CycleInequality.lattice_lemma
