import Mathlib

/-!
# Quadratic separation of digit-count states (main's V006 `overlap.md` §2)

Lane: `claude/lean-lane`. Prose source: `experiments/viewpoints/V006/overlap.md` §2
(theorem (3)–(4), formulas (5)–(7)) and `QUADRATIC_REVIEW.md` on main.

Setting. `s2 n` is the binary digit count of `n`. For `F : ℕ → α` (any type `α`)
and `t₀`, the states are `Q F t₀ a t = fun n => F (t₀ + t + s2 (3^a * n))`, `a, t ≥ 0`.
`F` is *eventually periodic* when `∃ N M, 0 < M ∧ ∀ n ≥ N, F (n + M) = F n`.

Verified in this file (all with the standard axioms):

* digit-count identities: `s2_add_pow_mul` (block additivity, `n < 2^k`),
  `s2_compl` (the complement identity `s2 (2^k − 1 − x) + s2 x = k`),
  `s2_mul_pow_sub` (main's (5) in additive form:
  `s2 (m(2^k − c)) + s2 (mc − 1) = k + s2 (m − 1)` for `0 < m, c`, `mc < 2^k`),
  `s2_mul_pow_sub_one` (main's (6)), `three_pow_dvd` (`3^(r+1) ∣ 2^(3^r) + 1`),
  `s2_balanced_block` and `s2_balanced` (main's (7): the balanced quotient
  `(2^(2·3^r·j) − 1)/3^(r+1)` has exactly `3^r j` ones);
* `Q_injective`: if `F` is not eventually periodic, `(a, t) ↦ Q F t₀ a t` is
  injective — main's "pairwise distinct" theorem, with the same two steps
  (`t = u` at `n = 2^k − 1`; then `a = b` at `n = 2^k − c` with the balanced
  quotient `c`);
* `Q_mem_Reach`: `Q F t₀ a t` is reached from `g = Q F t₀ 0 0 = F (t₀ + s2 ·)` by
  `t` binary digit-1 sections and `a` ternary digit-0 sections, so it lies in the
  joint section family through depth `a + t` (`Reach g (a + t)`);
* `triangle_encard_le`: hence the joint family through depth `D` has at least as
  many members as the triangle `{(a,t) : a + t ≤ D}` — main's `(D+1)(D+2)/2`
  (the numeric value of the triangle's cardinality is not computed here).

Finite-valuedness of `F` is never used. Nothing here concerns Collatz orbits;
main's Collatz corollary (a digit-count section forces quadratic growth) is not
formalised, and its reduction to this theorem runs through V005/V004 (Cobham).
-/

namespace LeanLane
namespace Quad

variable {α : Type*}

/-! ### Binary digit count -/

/-- Binary digit count. -/
def s2 (n : ℕ) : ℕ := (Nat.digits 2 n).sum

theorem s2_zero : s2 0 = 0 := by simp [s2]

theorem s2_eq (n : ℕ) (hn : 0 < n) : s2 n = s2 (n / 2) + n % 2 := by
  unfold s2
  rw [Nat.digits_def' (by norm_num) hn, List.sum_cons, add_comm]

theorem s2_two_mul (n : ℕ) : s2 (2 * n) = s2 n := by
  rcases Nat.eq_zero_or_pos n with rfl | hn
  · simp [s2]
  · rw [s2_eq (2 * n) (by omega), Nat.mul_div_cancel_left _ (by norm_num), Nat.mul_mod_right,
      add_zero]

theorem s2_two_mul_add_one (n : ℕ) : s2 (2 * n + 1) = s2 n + 1 := by
  rw [s2_eq (2 * n + 1) (by omega), show (2 * n + 1) / 2 = n by omega,
    show (2 * n + 1) % 2 = 1 by omega]

/-- Block additivity: for `n < 2^k`, `s2 (n + 2^k m) = s2 n + s2 m`. -/
theorem s2_add_pow_mul : ∀ k n m, n < 2 ^ k → s2 (n + 2 ^ k * m) = s2 n + s2 m := by
  intro k
  induction k with
  | zero =>
    intro n m hn
    have : n = 0 := by rw [pow_zero] at hn; omega
    subst this
    simp [s2_zero]
  | succ k ih =>
    intro n m hn
    rcases Nat.even_or_odd n with ⟨n', rfl⟩ | ⟨n', rfl⟩
    · have hn' : n' < 2 ^ k := by rw [pow_succ] at hn; omega
      rw [show n' + n' + 2 ^ (k + 1) * m = 2 * (n' + 2 ^ k * m) by ring, s2_two_mul, ih n' m hn',
        show n' + n' = 2 * n' by ring, s2_two_mul]
    · have hn' : n' < 2 ^ k := by rw [pow_succ] at hn; omega
      rw [show 2 * n' + 1 + 2 ^ (k + 1) * m = 2 * (n' + 2 ^ k * m) + 1 by ring,
        s2_two_mul_add_one, ih n' m hn', s2_two_mul_add_one]
      ring

/-- The complement identity: for `x < 2^k`, `s2 (2^k − 1 − x) + s2 x = k`. -/
theorem s2_compl : ∀ k x, x < 2 ^ k → s2 (2 ^ k - 1 - x) + s2 x = k := by
  intro k
  induction k with
  | zero =>
    intro x hx
    have : x = 0 := by rw [pow_zero] at hx; omega
    subst this
    simp [s2_zero]
  | succ k ih =>
    intro x hx
    rcases Nat.even_or_odd x with ⟨x', rfl⟩ | ⟨x', rfl⟩
    · have hx' : x' < 2 ^ k := by rw [pow_succ] at hx; omega
      have e : 2 ^ (k + 1) - 1 - (x' + x') = 2 * (2 ^ k - 1 - x') + 1 := by
        rw [pow_succ]; omega
      rw [e, s2_two_mul_add_one, show x' + x' = 2 * x' by ring, s2_two_mul]
      have := ih x' hx'
      omega
    · have hx' : x' < 2 ^ k := by rw [pow_succ] at hx; omega
      have e : 2 ^ (k + 1) - 1 - (2 * x' + 1) = 2 * (2 ^ k - 1 - x') := by
        rw [pow_succ]; omega
      rw [e, s2_two_mul, s2_two_mul_add_one]
      have := ih x' hx'
      omega

/-- **Main's (5), additive form.** For `0 < m`, `0 < c` and `mc < 2^k`:
`s2 (m (2^k − c)) + s2 (mc − 1) = k + s2 (m − 1)`. -/
theorem s2_mul_pow_sub {m c k : ℕ} (hm : 0 < m) (hc : 0 < c) (hk : m * c < 2 ^ k) :
    s2 (m * (2 ^ k - c)) + s2 (m * c - 1) = k + s2 (m - 1) := by
  have hmc : 0 < m * c := Nat.mul_pos hm hc
  have hAQ : 2 ^ k ≤ 2 ^ k * m := Nat.le_mul_of_pos_right _ hm
  have h1 : m * (2 ^ k - c) = (2 ^ k - m * c) + 2 ^ k * (m - 1) := by
    rw [mul_tsub, Nat.mul_sub_one, mul_comm m (2 ^ k)]
    omega
  have hlt : 2 ^ k - m * c < 2 ^ k := by omega
  have hcompl := s2_compl k (m * c - 1) (by omega)
  rw [show 2 ^ k - 1 - (m * c - 1) = 2 ^ k - m * c by omega] at hcompl
  rw [h1, s2_add_pow_mul k _ _ hlt]
  omega

/-- **Main's (6).** For `0 < m < 2^k`, `s2 (m (2^k − 1)) = k`. -/
theorem s2_mul_pow_sub_one {m k : ℕ} (hm : 0 < m) (hk : m < 2 ^ k) :
    s2 (m * (2 ^ k - 1)) = k := by
  have := s2_mul_pow_sub hm one_pos (by rw [mul_one]; exact hk)
  rw [mul_one] at this
  omega

/-! ### The balanced quotient -/

/-- `3^(r+1) ∣ 2^(3^r) + 1`, by `x³ + 1 = (x + 1)(x² − x + 1)` with `3 ∣ x² − x + 1`. -/
theorem three_pow_dvd (r : ℕ) : 3 ^ (r + 1) ∣ 2 ^ (3 ^ r) + 1 := by
  induction r with
  | zero => norm_num
  | succ r ih =>
    obtain ⟨q, hq⟩ := ih
    have hx3 : 2 ^ (3 ^ (r + 1)) = (2 ^ (3 ^ r)) ^ 3 := by rw [← pow_mul, pow_succ]
    rw [hx3]
    have hz : (2 : ℤ) ^ (3 ^ r) = 3 ^ (r + 1) * (q : ℤ) - 1 := by
      have : ((2 ^ (3 ^ r) + 1 : ℕ) : ℤ) = ((3 ^ (r + 1) * q : ℕ) : ℤ) := by rw [hq]
      push_cast at this
      linarith
    have key : ((3 : ℤ) ^ (r + 1 + 1)) ∣ ((2 : ℤ) ^ (3 ^ r)) ^ 3 + 1 := by
      refine ⟨q * (3 ^ (2 * r + 1) * q ^ 2 - 3 ^ (r + 1) * q + 1), ?_⟩
      rw [hz]
      ring
    exact_mod_cast key

theorem two_pow_double_sub_one (n : ℕ) : 2 ^ (2 * n) - 1 = (2 ^ n + 1) * (2 ^ n - 1) := by
  have h1 : 1 ≤ 2 ^ (2 * n) := Nat.one_le_two_pow
  have h2 : 1 ≤ 2 ^ n := Nat.one_le_two_pow
  zify [h1, h2]
  ring

theorem three_pow_dvd_two_pow_sub_one (r : ℕ) : 3 ^ (r + 1) ∣ 2 ^ (2 * 3 ^ r) - 1 := by
  rw [two_pow_double_sub_one]
  exact (three_pow_dvd r).mul_right _

theorem three_pow_dvd_two_pow_mul_sub_one (r j : ℕ) : 3 ^ (r + 1) ∣ 2 ^ (2 * 3 ^ r * j) - 1 := by
  induction j with
  | zero => simp
  | succ j ih =>
    have e : 2 ^ (2 * 3 ^ r * (j + 1)) - 1
        = (2 ^ (2 * 3 ^ r * j) - 1) * 2 ^ (2 * 3 ^ r) + (2 ^ (2 * 3 ^ r) - 1) := by
      have h1 : 1 ≤ 2 ^ (2 * 3 ^ r * j) := Nat.one_le_two_pow
      have h2 : 1 ≤ 2 ^ (2 * 3 ^ r) := Nat.one_le_two_pow
      have h3 : 1 ≤ 2 ^ (2 * 3 ^ r * (j + 1)) := Nat.one_le_two_pow
      zify [h1, h2, h3]
      ring
    rw [e]
    exact dvd_add (ih.mul_right _) (three_pow_dvd_two_pow_sub_one r)

/-- One balanced block: `(2^(2·3^r) − 1)/3^(r+1) = w (2^(3^r) − 1)` with `w < 2^(3^r)`,
so it has exactly `3^r` ones (by (6)). -/
theorem s2_balanced_block (r : ℕ) : s2 ((2 ^ (2 * 3 ^ r) - 1) / 3 ^ (r + 1)) = 3 ^ r := by
  obtain ⟨w, hw⟩ := three_pow_dvd r
  have hw0 : 0 < w := by
    rcases Nat.eq_zero_or_pos w with rfl | h
    · simp at hw
    · exact h
  have h3 : 3 ≤ 3 ^ (r + 1) := by
    calc 3 = 3 ^ 1 := by norm_num
      _ ≤ 3 ^ (r + 1) := Nat.pow_le_pow_right (by norm_num) (by omega)
  have hA2 : 2 ≤ 2 ^ (3 ^ r) := by
    calc 2 = 2 ^ 1 := by norm_num
      _ ≤ 2 ^ (3 ^ r) := Nat.pow_le_pow_right (by norm_num) (Nat.one_le_pow _ _ (by norm_num))
  have hwA : w < 2 ^ (3 ^ r) := by
    have : 3 * w ≤ 3 ^ (r + 1) * w := Nat.mul_le_mul_right w h3
    omega
  have hq : (2 ^ (2 * 3 ^ r) - 1) / 3 ^ (r + 1) = w * (2 ^ (3 ^ r) - 1) := by
    rw [two_pow_double_sub_one, hw, mul_assoc, Nat.mul_div_cancel_left _ (by positivity)]
  rw [hq]
  exact s2_mul_pow_sub_one hw0 hwA

/-- **Main's (7).** For `K = 2·3^r·j`, the quotient `(2^K − 1)/3^(r+1)` has exactly
`K/2 = 3^r j` ones: it consists of `j` non-overlapping copies of the balanced block. -/
theorem s2_balanced (r : ℕ) :
    ∀ j, s2 ((2 ^ (2 * 3 ^ r * j) - 1) / 3 ^ (r + 1)) = 3 ^ r * j := by
  intro j
  induction j with
  | zero => simp [s2_zero]
  | succ j ih =>
    have hsplit : (2 ^ (2 * 3 ^ r * (j + 1)) - 1) / 3 ^ (r + 1)
        = (2 ^ (2 * 3 ^ r * j) - 1) / 3 ^ (r + 1)
          + 2 ^ (2 * 3 ^ r * j) * ((2 ^ (2 * 3 ^ r) - 1) / 3 ^ (r + 1)) := by
      apply Nat.eq_of_mul_eq_mul_left (show 0 < 3 ^ (r + 1) by positivity)
      rw [Nat.mul_div_cancel' (three_pow_dvd_two_pow_mul_sub_one r (j + 1)),
        mul_add (3 ^ (r + 1)),
        Nat.mul_div_cancel' (three_pow_dvd_two_pow_mul_sub_one r j),
        mul_left_comm (3 ^ (r + 1)) (2 ^ (2 * 3 ^ r * j)),
        Nat.mul_div_cancel' (three_pow_dvd_two_pow_sub_one r)]
      have h1 : 1 ≤ 2 ^ (2 * 3 ^ r * j) := Nat.one_le_two_pow
      have h2 : 1 ≤ 2 ^ (2 * 3 ^ r) := Nat.one_le_two_pow
      have h3 : 1 ≤ 2 ^ (2 * 3 ^ r * (j + 1)) := Nat.one_le_two_pow
      zify [h1, h2, h3]
      ring
    have hlt : (2 ^ (2 * 3 ^ r * j) - 1) / 3 ^ (r + 1) < 2 ^ (2 * 3 ^ r * j) := by
      have := Nat.one_le_two_pow (n := 2 * 3 ^ r * j)
      calc (2 ^ (2 * 3 ^ r * j) - 1) / 3 ^ (r + 1) ≤ 2 ^ (2 * 3 ^ r * j) - 1 :=
            Nat.div_le_self _ _
        _ < 2 ^ (2 * 3 ^ r * j) := by omega
    rw [hsplit, s2_add_pow_mul _ _ _ hlt, ih, s2_balanced_block]
    ring

theorem s2_odd_sub_one {q : ℕ} (hq : Odd q) : s2 (q - 1) + 1 = s2 q := by
  obtain ⟨m, rfl⟩ := hq
  rw [show 2 * m + 1 - 1 = 2 * m by omega, s2_two_mul, s2_two_mul_add_one]

/-! ### Eventual periodicity and the states -/

/-- `F` is eventually periodic. -/
def EventuallyPeriodic (F : ℕ → α) : Prop :=
  ∃ N M : ℕ, 0 < M ∧ ∀ n, N ≤ n → F (n + M) = F n

/-- Two tails of `F` that agree after different shifts give an eventual period. -/
theorem eventuallyPeriodic_of_tails (F : ℕ → α) {c₁ c₂ N : ℕ} (hc : c₁ < c₂)
    (h : ∀ k, N ≤ k → F (c₁ + k) = F (c₂ + k)) : EventuallyPeriodic F := by
  refine ⟨c₁ + N, c₂ - c₁, by omega, fun n hn => ?_⟩
  have := h (n - c₁) (by omega)
  rw [show c₁ + (n - c₁) = n by omega, show c₂ + (n - c₁) = n + (c₂ - c₁) by omega] at this
  exact this.symm

/-- Main's states `Q_(a,t)(n) = F(t₀ + t + s₂(3^a n))`. -/
def Q (F : ℕ → α) (t₀ a t : ℕ) : ℕ → α := fun n => F (t₀ + t + s2 (3 ^ a * n))

/-- Evaluation at `n = 2^k − 1`: equal states have equal shifted tails. -/
theorem shift_eq_of_Q_eq (F : ℕ → α) (t₀ : ℕ) {a b t u : ℕ}
    (h : Q F t₀ a t = Q F t₀ b u) :
    ∀ k, 3 ^ a + 3 ^ b ≤ k → F (t₀ + t + k) = F (t₀ + u + k) := by
  intro k hk
  have hk2 : 3 ^ a + 3 ^ b < 2 ^ k := lt_of_le_of_lt hk Nat.lt_two_pow_self
  have ha : 3 ^ a < 2 ^ k := lt_of_le_of_lt (Nat.le_add_right _ _) hk2
  have hb : 3 ^ b < 2 ^ k := lt_of_le_of_lt (Nat.le_add_left _ _) hk2
  have := congrFun h (2 ^ k - 1)
  simp only [Q] at this
  rwa [s2_mul_pow_sub_one (by positivity) ha, s2_mul_pow_sub_one (by positivity) hb] at this

/-- **Step 1.** Equal states have the same shift `t`. -/
theorem t_eq_of_Q_eq (F : ℕ → α) (hF : ¬ EventuallyPeriodic F) (t₀ : ℕ) {a b t u : ℕ}
    (h : Q F t₀ a t = Q F t₀ b u) : t = u := by
  by_contra hne
  have htail := shift_eq_of_Q_eq F t₀ h
  rcases Nat.lt_or_gt_of_ne hne with hlt | hgt
  · exact hF (eventuallyPeriodic_of_tails F (c₁ := t₀ + t) (c₂ := t₀ + u) (by omega) htail)
  · exact hF (eventuallyPeriodic_of_tails F (c₁ := t₀ + u) (c₂ := t₀ + t) (by omega)
      (fun k hk => (htail k hk).symm))

/-- **Step 2.** With equal shifts, a smaller ternary exponent is impossible: evaluate at
`n = 2^k − c` for the balanced quotient `c = (2^K − 1)/3^b`, `K = 2·3^(b−1)·J`,
`J = s2(3^b − 1) + 1`, and use (5) and (7). -/
theorem not_lt_of_Q_eq (F : ℕ → α) (hF : ¬ EventuallyPeriodic F) (t₀ : ℕ) {a b t : ℕ}
    (hab : a < b) (h : Q F t₀ a t = Q F t₀ b t) : False := by
  obtain ⟨s, rfl⟩ : ∃ s, b = a + s + 1 := ⟨b - a - 1, by omega⟩
  obtain ⟨J, hJ⟩ : ∃ J, J = s2 (3 ^ (a + s + 1) - 1) + 1 := ⟨_, rfl⟩
  obtain ⟨c, hc⟩ := three_pow_dvd_two_pow_mul_sub_one (a + s) J
  obtain ⟨K, hK⟩ : ∃ K, K = 2 * 3 ^ (a + s) * J := ⟨_, rfl⟩
  rw [← hK] at hc
  -- hc : 2 ^ K - 1 = 3 ^ (a + s + 1) * c
  obtain ⟨X, hX⟩ : ∃ X, X = 3 ^ (a + s) * J := ⟨_, rfl⟩
  have hK2 : K = 2 * X := by rw [hK, hX]; ring
  have hXJ : J ≤ X := by
    rw [hX]
    exact Nat.le_mul_of_pos_left J (by positivity)
  have hJpos : 0 < J := by omega
  have hKge : 2 ≤ K := by omega
  -- `c` is odd and positive
  have hodd : Odd (2 ^ K - 1) := by
    obtain ⟨K', hK'⟩ : ∃ K', K = K' + 1 := ⟨K - 1, by omega⟩
    refine ⟨2 ^ K' - 1, ?_⟩
    rw [hK', pow_succ]
    have := Nat.one_le_two_pow (n := K')
    omega
  have hcodd : Odd c := by
    rw [hc] at hodd
    exact (Nat.odd_mul.mp hodd).2
  have hc0 : 0 < c := hcodd.pos
  -- `P_l = s2 (3^(a+s+1) c − 1) = K − 1`
  have hPl : s2 (3 ^ (a + s + 1) * c - 1) + 1 = K := by
    obtain ⟨K', hK'⟩ : ∃ K', K = K' + 1 := ⟨K - 1, by omega⟩
    have h1 : 1 < 2 ^ K' := by
      calc 1 < 2 ^ 1 := by norm_num
        _ ≤ 2 ^ K' := Nat.pow_le_pow_right (by norm_num) (by omega)
    have e : 3 ^ (a + s + 1) * c - 1 = 2 * (1 * (2 ^ K' - 1)) := by
      rw [← hc, hK', pow_succ, one_mul]
      have := Nat.one_le_two_pow (n := K')
      omega
    rw [e, s2_two_mul, s2_mul_pow_sub_one one_pos h1]
    omega
  -- `3^a c` is the balanced quotient at `r = s`, `j = 3^a J`
  have hX' : 2 * 3 ^ s * (3 ^ a * J) = K := by rw [hK]; ring
  have hmc : (2 ^ (2 * 3 ^ s * (3 ^ a * J)) - 1) / 3 ^ (s + 1) = 3 ^ a * c := by
    apply Nat.div_eq_of_eq_mul_left (by positivity)
    rw [hX', hc]
    ring
  have hXeq : 3 ^ s * (3 ^ a * J) = X := by rw [hX]; ring
  have hs2mc : s2 (3 ^ a * c) = X := by
    rw [← hmc, s2_balanced s (3 ^ a * J), hXeq]
  have hmcodd : Odd (3 ^ a * c) := Nat.odd_mul.mpr ⟨Odd.pow ⟨1, by norm_num⟩, hcodd⟩
  -- `P_m = s2 (3^a c − 1) = X − 1`
  have hPm : s2 (3 ^ a * c - 1) + 1 = X := by
    rw [s2_odd_sub_one hmcodd, hs2mc]
  -- the gap `Δ = (R_m + P_l) − (R_l + P_m)` is positive
  have hΔ : s2 (3 ^ (a + s + 1) - 1) + s2 (3 ^ a * c - 1)
      < s2 (3 ^ a - 1) + s2 (3 ^ (a + s + 1) * c - 1) := by
    omega
  -- bounds for the evaluation points `2^k − c`, `k > K`
  have hlc_lt : ∀ k, K < k → 3 ^ (a + s + 1) * c < 2 ^ k := by
    intro k hk
    rw [← hc]
    have h1 := Nat.pow_lt_pow_right (by norm_num : 1 < 2) hk
    have h2 := Nat.one_le_two_pow (n := K)
    omega
  have hmc_lt : ∀ k, K < k → 3 ^ a * c < 2 ^ k := by
    intro k hk
    have h1 := hlc_lt k hk
    have h2 : 3 ^ a * c ≤ 3 ^ (a + s + 1) * c :=
      Nat.mul_le_mul_right c (Nat.pow_le_pow_right (by norm_num) (by omega))
    omega
  -- evaluation of the state equality at `n = 2^k − c`
  have heval : ∀ k, K < k →
      F (t₀ + t + s2 (3 ^ (a + s + 1) * (2 ^ k - c))
          + ((s2 (3 ^ a - 1) + s2 (3 ^ (a + s + 1) * c - 1))
            - (s2 (3 ^ (a + s + 1) - 1) + s2 (3 ^ a * c - 1))))
        = F (t₀ + t + s2 (3 ^ (a + s + 1) * (2 ^ k - c))) := by
    intro k hk
    have e1 := s2_mul_pow_sub (m := 3 ^ a) (c := c) (k := k) (by positivity) hc0 (hmc_lt k hk)
    have e2 := s2_mul_pow_sub (m := 3 ^ (a + s + 1)) (c := c) (k := k) (by positivity) hc0
      (hlc_lt k hk)
    have hQ := congrFun h (2 ^ k - c)
    simp only [Q] at hQ
    have hS : t₀ + t + s2 (3 ^ a * (2 ^ k - c)) =
        t₀ + t + s2 (3 ^ (a + s + 1) * (2 ^ k - c))
          + ((s2 (3 ^ a - 1) + s2 (3 ^ (a + s + 1) * c - 1))
            - (s2 (3 ^ (a + s + 1) - 1) + s2 (3 ^ a * c - 1))) := by
      omega
    rw [hS] at hQ
    exact hQ
  -- the resulting eventual period
  apply hF
  refine ⟨t₀ + t + s2 (3 ^ (a + s + 1) - 1) + 2,
    (s2 (3 ^ a - 1) + s2 (3 ^ (a + s + 1) * c - 1))
      - (s2 (3 ^ (a + s + 1) - 1) + s2 (3 ^ a * c - 1)),
    by omega, fun x hx => ?_⟩
  obtain ⟨k, hk, hxk⟩ : ∃ k, K < k ∧ t₀ + t + s2 (3 ^ (a + s + 1) * (2 ^ k - c)) = x := by
    refine ⟨x - (t₀ + t) - s2 (3 ^ (a + s + 1) - 1) + s2 (3 ^ (a + s + 1) * c - 1),
      by omega, ?_⟩
    have e2 := s2_mul_pow_sub (m := 3 ^ (a + s + 1)) (c := c)
      (k := x - (t₀ + t) - s2 (3 ^ (a + s + 1) - 1) + s2 (3 ^ (a + s + 1) * c - 1))
      (by positivity) hc0 (hlc_lt _ (by omega))
    omega
  rw [← hxk]
  exact heval k hk

/-- **Main's theorem (V006 `overlap.md` §2).** If `F` is not eventually periodic, the
states `Q_(a,t)` are pairwise distinct. -/
theorem Q_injective (F : ℕ → α) (hF : ¬ EventuallyPeriodic F) (t₀ : ℕ) :
    Function.Injective (fun p : ℕ × ℕ => Q F t₀ p.1 p.2) := by
  rintro ⟨a, t⟩ ⟨b, u⟩ h
  change Q F t₀ a t = Q F t₀ b u at h
  have htu : t = u := t_eq_of_Q_eq F hF t₀ h
  subst htu
  rcases lt_trichotomy a b with hab | hab | hab
  · exact (not_lt_of_Q_eq F hF t₀ hab h).elim
  · rw [hab]
  · exact (not_lt_of_Q_eq F hF t₀ hab h.symm).elim

/-! ### The joint section family -/

/-- One binary or ternary section operation. -/
def Step (s s' : ℕ → α) : Prop :=
  (∃ i, i < 2 ∧ s' = fun n => s (2 * n + i)) ∨ (∃ j, j < 3 ∧ s' = fun n => s (3 * n + j))

/-- Sequences reachable from `g` by at most `D` section operations (main's `J_D(g)`). -/
def Reach (g : ℕ → α) : ℕ → Set (ℕ → α)
  | 0 => {g}
  | D + 1 => Reach g D ∪ {s' | ∃ s ∈ Reach g D, Step s s'}

theorem Reach_succ_left (g : ℕ → α) (D : ℕ) {s : ℕ → α} (hs : s ∈ Reach g D) :
    s ∈ Reach g (D + 1) :=
  Set.mem_union_left _ hs

theorem Reach_step (g : ℕ → α) (D : ℕ) {s s' : ℕ → α} (hs : s ∈ Reach g D) (h : Step s s') :
    s' ∈ Reach g (D + 1) :=
  Set.mem_union_right _ ⟨s, hs, h⟩

theorem Reach_mono (g : ℕ → α) {k D : ℕ} (h : k ≤ D) : Reach g k ⊆ Reach g D := by
  induction h with
  | refl => exact subset_rfl
  | step _ ih => exact ih.trans (fun s hs => Reach_succ_left g _ hs)

/-- `Q_(a,t)` is reached from `g = Q_(0,0)` by `t` binary digit-1 sections followed by `a`
ternary digit-0 sections. -/
theorem Q_mem_Reach (F : ℕ → α) (t₀ a t : ℕ) : Q F t₀ a t ∈ Reach (Q F t₀ 0 0) (a + t) := by
  have hbin : ∀ t, Q F t₀ 0 t ∈ Reach (Q F t₀ 0 0) t := by
    intro t
    induction t with
    | zero => simp [Reach]
    | succ t ih =>
      refine Reach_step _ _ ih (Or.inl ⟨1, by norm_num, ?_⟩)
      funext n
      simp only [Q, pow_zero, one_mul]
      rw [s2_two_mul_add_one]
      congr 1
      ring
  have hter : ∀ a, Q F t₀ a t ∈ Reach (Q F t₀ 0 0) (a + t) := by
    intro a
    induction a with
    | zero => simpa using hbin t
    | succ a ih =>
      rw [show a + 1 + t = (a + t) + 1 by ring]
      refine Reach_step _ _ ih (Or.inr ⟨0, by norm_num, ?_⟩)
      funext n
      simp only [Q]
      rw [show 3 ^ (a + 1) * n = 3 ^ a * (3 * n + 0) by ring]
  exact hter a

/-- **Main's (4) in set form.** The joint family through depth `D` is at least as large
as the triangle `{(a,t) : a + t ≤ D}`, which has `(D+1)(D+2)/2` elements. -/
theorem triangle_encard_le (F : ℕ → α) (hF : ¬ EventuallyPeriodic F) (t₀ D : ℕ) :
    ({p : ℕ × ℕ | p.1 + p.2 ≤ D} : Set (ℕ × ℕ)).encard ≤ (Reach (Q F t₀ 0 0) D).encard := by
  have hinj := (Q_injective F hF t₀).injOn (s := {p : ℕ × ℕ | p.1 + p.2 ≤ D})
  rw [← hinj.encard_image]
  apply Set.encard_le_encard
  rintro _ ⟨⟨a, t⟩, hp, rfl⟩
  exact Reach_mono _ hp (Q_mem_Reach F t₀ a t)

end Quad
end LeanLane
