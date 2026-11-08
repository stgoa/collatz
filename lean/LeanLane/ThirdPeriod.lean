import LeanLane.RationalCycle
import LeanLane.CycleInequality

/-!
# Balanced unaligned third-period words

The word is `A[+d] B A B[-d] A B`, with both altered terminal
exponents positive.  All intercepts use the shared `Words.C` convention.
-/

namespace LeanLane.CycleEquation

lemma small_step {a : ℕ} {y : ℤ} (hy : 0 < y) (_ho : Odd y)
    {n : ℤ} (hn : n ≤ 52) (hs : 2 ^ a * y = n) : a ≤ 5 := by
  by_contra h
  have h6 : 6 ≤ a := by omega
  have hp : (64 : ℤ) ≤ 2 ^ a := by
    simpa using (pow_le_pow_right₀ (by norm_num : (1 : ℤ) ≤ 2) h6)
  have hp0 : (0 : ℤ) < 2 ^ a := by positivity
  have hmul : 2 ^ a ≤ 2 ^ a * y := by nlinarith
  omega

lemma step_one {a : ℕ} {y : ℤ} (hy : 0 < y) (ho : Odd y)
    (hs : 2 ^ a * y = 4) : y = 1 ∧ a = 2 := by
  have ha := small_step hy ho (by norm_num : (4 : ℤ) ≤ 52) hs
  rcases ho with ⟨k, hk⟩
  interval_cases a <;> norm_num at hs ⊢ <;> omega

lemma step_three {a : ℕ} {y : ℤ} (hy : 0 < y) (ho : Odd y)
    (hs : 2 ^ a * y = 10) : y = 5 := by
  have ha := small_step hy ho (by norm_num : (10 : ℤ) ≤ 52) hs
  rcases ho with ⟨k, hk⟩
  interval_cases a <;> norm_num at hs ⊢ <;> omega

lemma step_five {a : ℕ} {y : ℤ} (hy : 0 < y) (ho : Odd y)
    (hs : 2 ^ a * y = 16) : y = 1 := by
  have ha := small_step hy ho (by norm_num : (16 : ℤ) ≤ 52) hs
  rcases ho with ⟨k, hk⟩
  interval_cases a <;> norm_num at hs ⊢ <;> omega

lemma step_seven {a : ℕ} {y : ℤ} (hy : 0 < y) (ho : Odd y)
    (hs : 2 ^ a * y = 22) : y = 11 := by
  have ha := small_step hy ho (by norm_num : (22 : ℤ) ≤ 52) hs
  rcases ho with ⟨k, hk⟩
  interval_cases a <;> norm_num at hs ⊢ <;> omega

lemma step_eleven {a : ℕ} {y : ℤ} (hy : 0 < y) (ho : Odd y)
    (hs : 2 ^ a * y = 34) : y = 17 := by
  have ha := small_step hy ho (by norm_num : (34 : ℤ) ≤ 52) hs
  rcases ho with ⟨k, hk⟩
  interval_cases a <;> norm_num at hs ⊢ <;> omega

lemma step_seventeen {a : ℕ} {y : ℤ} (hy : 0 < y) (ho : Odd y)
    (hs : 2 ^ a * y = 52) : y = 13 := by
  have ha := small_step hy ho (by norm_num : (52 : ℤ) ≤ 52) hs
  rcases ho with ⟨k, hk⟩
  interval_cases a <;> norm_num at hs ⊢ <;> omega

lemma step_thirteen {a : ℕ} {y : ℤ} (hy : 0 < y) (ho : Odd y)
    (hs : 2 ^ a * y = 40) : y = 5 := by
  have ha := small_step hy ho (by norm_num : (40 : ℤ) ≤ 52) hs
  rcases ho with ⟨k, hk⟩
  interval_cases a <;> norm_num at hs ⊢ <;> omega

lemma periodic_multiple {w : List ℕ} {x : ℕ → ℤ} (hc : IsCycle 1 w x)
    (j n : ℕ) : x (j + n * w.length) = x j := by
  induction n with
  | zero => simp
  | succ n ih =>
    rw [Nat.succ_mul, ← Nat.add_assoc, hc.periodic]
    exact ih

lemma one_forces_all_twos {w : List ℕ} {x : ℕ → ℤ}
    (hw : w ≠ []) (hc : IsCycle 1 w x)
    (hpos : ∀ i, 0 < x i) (hodd : ∀ i, Odd (x i))
    {i : ℕ} (hi : x i = 1) : ∀ a ∈ w, a = 2 := by
  have future : ∀ k, x (i + k) = 1 := by
    intro k
    induction k with
    | zero => simpa using hi
    | succ k ih =>
      have hs := hc.step (i+k)
      rw [ih] at hs
      have hout := step_one (hpos (i+k+1)) (hodd (i+k+1)) (by simpa using hs)
      simpa [Nat.add_assoc] using hout.1
  have hlen : 1 ≤ w.length := by cases w <;> simp_all
  have allone : ∀ j, x j = 1 := by
    intro j
    have hmul : i ≤ i*w.length := by simpa using Nat.mul_le_mul_left i hlen
    have hle : i ≤ j+i*w.length := by omega
    have hh := future (j+i*w.length-i)
    rw [Nat.add_sub_of_le hle] at hh
    rw [periodic_multiple hc] at hh
    exact hh
  intro a ha
  obtain ⟨j, hj, hja⟩ := List.mem_iff_getElem.mp ha
  have hs := hc.step j
  rw [allone j, allone (j+1), Nat.mod_eq_of_lt hj, List.getD_eq_getElem _ _ hj, hja] at hs
  exact (step_one (y := 1) (by norm_num) (by decide) (by simpa using hs)).2

lemma minimum_nine {w : List ℕ} {x : ℕ → ℤ}
    (hw : w ≠ []) (hc : IsCycle 1 w x)
    (hpos : ∀ i, 0 < x i) (hodd : ∀ i, Odd (x i))
    (hnontrivial : ¬ ∀ a ∈ w, a = 2) : ∀ i, 9 ≤ x i := by
  have no_one : ∀ i, x i ≠ 1 := by
    intro i hi
    exact hnontrivial (one_forces_all_twos hw hc hpos hodd hi)
  have no_five : ∀ i, x i ≠ 5 := by
    intro i hi
    have hs := hc.step i
    rw [hi] at hs
    exact no_one (i+1) (step_five (hpos (i+1)) (hodd (i+1)) (by simpa using hs))
  have no_three : ∀ i, x i ≠ 3 := by
    intro i hi
    have hs := hc.step i
    rw [hi] at hs
    exact no_five (i+1) (step_three (hpos (i+1)) (hodd (i+1)) (by simpa using hs))
  have no_seven : ∀ i, x i ≠ 7 := by
    intro i hi
    have hs := hc.step i
    rw [hi] at hs
    have h11 : x (i+1) = 11 := step_seven (hpos (i+1)) (hodd (i+1)) (by simpa using hs)
    have hs := hc.step (i+1)
    rw [h11] at hs
    have h17 : x (i+1+1) = 17 := step_eleven (hpos (i+1+1)) (hodd (i+1+1)) (by simpa using hs)
    have hs := hc.step (i+1+1)
    rw [h17] at hs
    have h13 : x (i+1+1+1) = 13 := step_seventeen (hpos (i+1+1+1)) (hodd (i+1+1+1)) (by simpa using hs)
    have hs := hc.step (i+1+1+1)
    rw [h13] at hs
    exact no_five (i+1+1+1+1)
      (step_thirteen (hpos (i+1+1+1+1)) (hodd (i+1+1+1+1)) (by simpa using hs))
  intro i
  have hp := hpos i
  obtain ⟨k, hk⟩ := hodd i
  have h1 := no_one i
  have h3 := no_three i
  have h5 := no_five i
  have h7 := no_seven i
  omega

end LeanLane.CycleEquation

namespace LeanLane.ThirdPeriodPowers

theorem first_exponent_bound (l g : ℕ) (hg : 0 < g)
    (h : (2 : ℤ) ^ (l + g) < 3 ^ g) : 17 * l < 10 * g := by
  have hp := pow_lt_pow_left₀ h (by positivity) (by decide : 17 ≠ 0)
  have hc : ((3 : ℤ) ^ 17) ^ g < ((2 : ℤ) ^ 27) ^ g :=
    pow_lt_pow_left₀ (by norm_num) (by positivity) (Nat.ne_of_gt hg)
  have hp' : (2 : ℤ) ^ ((l + g) * 17) < 3 ^ (g * 17) := by
    simpa only [← pow_mul] using hp
  have hc' : (3 : ℤ) ^ (g * 17) < 2 ^ (g * 27) := by
    simpa only [← pow_mul, Nat.mul_comm] using hc
  have he := (pow_lt_pow_iff_right₀ (by norm_num : (1 : ℤ) < 2)).mp
    (lt_trans hp' hc')
  omega

theorem second_exponent_bound (n g T : ℕ)
    (h : (3 : ℤ) ^ n * 2 ^ g < 2 ^ T) : 19 * n + 12 * g < 12 * T := by
  have hp := pow_lt_pow_left₀ h (by positivity) (by decide : 12 ≠ 0)
  have hc : ((2 : ℤ) ^ 19) ^ n ≤ ((3 : ℤ) ^ 12) ^ n :=
    pow_le_pow_left₀ (by positivity) (by norm_num) n
  have hlower : (2 : ℤ) ^ (19 * n + g * 12) ≤ ((3 : ℤ) ^ n * 2 ^ g) ^ 12 := by
    calc
      _ = ((2 : ℤ) ^ 19) ^ n * ((2 : ℤ) ^ g) ^ 12 := by
        simp only [pow_add, pow_mul]
      _ ≤ ((3 : ℤ) ^ 12) ^ n * ((2 : ℤ) ^ g) ^ 12 :=
        mul_le_mul_of_nonneg_right hc (by positivity)
      _ = ((3 : ℤ) ^ n * 2 ^ g) ^ 12 := by
        simp only [mul_pow, ← pow_mul, Nat.mul_comm]
  have hwhole : (2 : ℤ) ^ (19 * n + g * 12) < 2 ^ (T * 12) := by
    exact lt_of_le_of_lt hlower (by simpa only [← pow_mul] using hp)
  have he := (pow_lt_pow_iff_right₀ (by norm_num : (1 : ℤ) < 2)).mp hwhole
  omega

theorem product_exponent_bound (T g : ℕ) (hg : 0 < g)
    (h : (2 : ℤ) ^ (3 * T) * 9 ^ (3 * g) ≤ 28 ^ (3 * g)) :
    25 * T < 41 * g := by
  have hp := pow_le_pow_left₀ (by positivity) h 25
  have hc : ((28 : ℤ) ^ 25) ^ (3 * g) <
      ((2 : ℤ) ^ 41 * 9 ^ 25) ^ (3 * g) :=
    pow_lt_pow_left₀ (by norm_num) (by positivity) (by omega)
  have hc' : ((28 : ℤ) ^ (3 * g)) ^ 25 <
      ((2 : ℤ) ^ 41 * 9 ^ 25) ^ (3 * g) := by
    simpa only [← pow_mul, Nat.mul_comm] using hc
  have hchain := lt_of_le_of_lt hp hc'
  simp only [mul_pow, ← pow_mul] at hchain
  have e1 : 3 * T * 25 = 75 * T := by omega
  have e2 : 3 * g * 25 = 75 * g := by omega
  have e3 : 41 * (3 * g) = 123 * g := by omega
  have e4 : 25 * (3 * g) = 75 * g := by omega
  rw [e1, e2, e3, e4] at hchain
  have hpower : (2 : ℤ) ^ (75 * T) < 2 ^ (123 * g) := by
    by_contra hnot
    have hreverse := mul_le_mul_of_nonneg_right (le_of_not_gt hnot)
      (by positivity : (0 : ℤ) ≤ 9 ^ (75 * g))
    exact (not_lt_of_ge hreverse) hchain
  have he := (pow_lt_pow_iff_right₀ (by norm_num : (1 : ℤ) < 2)).mp hpower
  omega

theorem integer_power_contradiction (l n T g : ℕ) (hgn : g = l + n) (hg : 0 < g)
    (hfirst : (2 : ℤ) ^ (l + g) < 3 ^ g)
    (hsecond : (3 : ℤ) ^ n * 2 ^ g < 2 ^ T)
    (hproduct : (2 : ℤ) ^ (3 * T) * 9 ^ (3 * g) ≤ 28 ^ (3 * g)) : False := by
  have h1 := first_exponent_bound l g hg hfirst
  have h2 := second_exponent_bound n g T hsecond
  have h3 := product_exponent_bound T g hg hproduct
  have hlower : 337 * g < 204 * T := by omega
  omega

end LeanLane.ThirdPeriodPowers

namespace LeanLane.RationalCycle

open LeanLane.Words LeanLane.CycleEquation

lemma odd_C_of_positive {w : List ℕ} (hw : w ≠ [])
    (ha : ∀ a ∈ w, 0 < a) : Odd (C w) := by
  obtain ⟨a, tail, rfl⟩ := List.exists_cons_of_ne_nil hw
  have ha0 : 0 < a := ha a (by simp)
  have hp : Even ((2 : ℤ)^a) := Int.even_pow.mpr ⟨even_two, ha0.ne'⟩
  have ht : Odd ((3 : ℤ)^tail.length) := Odd.pow (by decide)
  exact ht.add_even (hp.mul_right (C tail))

lemma integral_cycle_of_dvd {w : List ℕ} (hw : w ≠ [])
    (ha : ∀ a ∈ w, 0 < a) (hD : 0 < D w) (hdiv : D w ∣ C w) :
    ∃ x : ℕ → ℤ, IsCycle 1 w x ∧ (∀ i, 0 < x i) ∧ (∀ i, Odd (x i)) := by
  have hS : 0 < w.sum := by
    obtain ⟨a, tail, rfl⟩ := List.exists_cons_of_ne_nil hw
    have ha0 := ha a (by simp)
    simp only [List.sum_cons]
    omega
  have hDodd : Odd (D w) := odd_D hS
  have hall : ∀ i, D w ∣ C (w.rotate i) := dvd_C_rotate hw hDodd hdiv (dvd_refl _)
  let x : ℕ → ℤ := fun i => C (w.rotate i) / D w
  have hexact : ∀ i, D w * x i = C (w.rotate i) := fun i => Int.mul_ediv_cancel' (hall i)
  have hrot : ∀ i, w.rotate i ≠ [] := by
    intro i hi
    apply hw
    simpa using congrArg List.length hi
  have hc : IsCycle 1 w x := by
    constructor
    · intro i
      have hid := rotation_identity' (w.rotate i) (hrot i)
      rw [List.rotate_rotate, D_rotate] at hid
      have hget : (w.rotate i).getD 0 0 = w.getD (i % w.length) 0 := by
        rw [getD_rotate w i 0 (List.length_pos_of_ne_nil hw)]
        simp
      rw [hget] at hid
      apply mul_left_cancel₀ hD.ne'
      rw [show i + 1 = 1 + i from add_comm _ _] at hid
      calc D w * (2 ^ (w.getD (i % w.length) 0) * x (i+1))
          = 2 ^ (w.getD (i % w.length) 0) * (D w * x (i+1)) := by ring
        _ = 2 ^ (w.getD (i % w.length) 0) * C (w.rotate (1+i)) := by rw [hexact, add_comm]
        _ = 3 * C (w.rotate i) + D w := hid
        _ = D w * (3*x i+1) := by rw [← hexact i]; ring
    · intro i
      show C (w.rotate (i+w.length)) / D w = C (w.rotate i) / D w
      rw [add_comm, ← List.rotate_rotate, List.rotate_length]
  refine ⟨x, hc, ?_, ?_⟩
  · intro i
    have hp := C_pos (w.rotate i) (hrot i)
    have he := hexact i
    nlinarith
  · intro i
    have hrpos : ∀ a ∈ w.rotate i, 0 < a := by
      intro a hmem
      exact ha a (List.mem_rotate.mp hmem)
    have hoddC := odd_C_of_positive (hrot i) hrpos
    have hprod : Odd (D w * x i) := by rw [hexact]; exact hoddC
    exact (Int.odd_mul.mp hprod).2

end LeanLane.RationalCycle

namespace LeanLane.ThirdPeriod

open Words CycleEquation RationalCycle

def Positive (w : List ℕ) : Prop := ∀ a ∈ w, 0 < a

theorem length_le_sum {w : List ℕ} (hw : Positive w) : w.length ≤ w.sum := by
  induction w with
  | nil => simp
  | cons a w ih =>
    have ha := hw a (by simp)
    have ht : Positive w := fun b hb => hw b (by simp [hb])
    have := ih ht
    simp only [List.length_cons, List.sum_cons]
    omega

theorem intercept_bound {w : List ℕ} (hw : Positive w) :
    (2 : ℤ) ^ w.length * C w < 2 ^ w.sum * 3 ^ w.length := by
  induction w with
  | nil => simp [C]
  | cons a w ih =>
    have ha := hw a (by simp)
    have ht : Positive w := fun b hb => hw b (by simp [hb])
    have hi := ih ht
    have hl := length_le_sum ht
    have he : w.length + 1 ≤ a + w.sum := by omega
    have hp : (2 : ℤ) ^ (w.length + 1) ≤ 2 ^ (a + w.sum) :=
      pow_le_pow_right₀ (by norm_num) he
    have hp' := mul_le_mul_of_nonneg_right hp (show (0 : ℤ) ≤ 3 ^ w.length by positivity)
    have hi' := mul_lt_mul_of_pos_left hi (show (0 : ℤ) < 2 ^ a * 2 by positivity)
    simp only [List.length_cons, List.sum_cons, C]
    simp only [pow_add, pow_succ] at hp' hi' ⊢
    nlinarith

theorem intercept_last (u : List ℕ) (a : ℕ) :
    C (u ++ [a]) = 3 * C u + 2 ^ u.sum := by
  simp [C_append, C]

def block (u : List ℕ) (a : ℕ) : List ℕ := u ++ [a]

theorem block_positive {u : List ℕ} {a : ℕ} (hu : Positive u) (ha : 0 < a) :
    Positive (block u a) := by
  intro x hx
  simp only [block, List.mem_append, List.mem_singleton] at hx
  rcases hx with hx | rfl
  · exact hu x hx
  · exact ha

theorem positive_append {u v : List ℕ} (hu : Positive u) (hv : Positive v) :
    Positive (u ++ v) := by
  intro a ha
  rcases List.mem_append.mp ha with ha | ha
  · exact hu a ha
  · exact hv a ha

def word (u v : List ℕ) (a b d : ℕ) : List ℕ :=
  block u (a + d) ++ block v (b + d) ++ block u a ++
    block v b ++ block u a ++ block v (b + d)

theorem word_length (u v : List ℕ) (a b d : ℕ) :
    (word u v a b d).length = 3 * ((block u a).length + (block v (b + d)).length) := by
  simp [word, block]
  omega

theorem word_sum (u v : List ℕ) (a b d : ℕ) :
    (word u v a b d).sum = 3 * ((block u a).sum + (block v (b + d)).sum) := by
  simp [word, block]
  omega

theorem word_positive {u v : List ℕ} {a b d : ℕ}
    (hu : Positive u) (hv : Positive v) (ha : 0 < a) (hb : 0 < b) :
    Positive (word u v a b d) := by
  intro x hx
  simp only [word, block, List.mem_append, List.mem_singleton] at hx
  rcases hx with (((((h | h) | h) | h) | h) | h)
  all_goals rcases h with h | h
  all_goals first | exact hu x h | exact hv x h | omega

theorem six_block_intercept (u v : List ℕ) (a b d : ℕ) :
    let α : ℤ := 3 ^ (block u a).length
    let β : ℤ := 3 ^ (block v (b + d)).length
    let Q : ℤ := 2 ^ (block u a).sum
    let S : ℤ := 2 ^ (block v (b + d)).sum
    let X := β * C (block u a)
    let Y := Q * C (block v (b + d))
    C (word u v a b d) =
      X * (α * β) ^ 2 + 2 ^ d * Y * (α * β) ^ 2 +
      2 ^ d * X * (α * β) * (Q * S) + 2 ^ d * Y * (α * β) * (Q * S) +
      X * (Q * S) ^ 2 + Y * (Q * S) ^ 2 := by
  dsimp
  simp only [word, block, C_append, List.length_append, List.length_singleton,
    List.sum_append, List.sum_singleton, C, List.length_nil,
    pow_zero, mul_zero, add_zero, pow_add, pow_succ]
  ring

theorem shortened_intercept_bound {u v : List ℕ} {a b d : ℕ}
    (hu : Positive u) (hv : Positive v) (ha : 0 < a) (hb : 0 < b) :
    (2 : ℤ) ^ d * 2 ^ ((block u a).length + (block v (b + d)).length) *
      (3 ^ (block v (b + d)).length * C (block u a) +
        2 ^ (block u a).sum * C (block v (b + d))) <
      (2 ^ (block u a).sum * 2 ^ (block v (b + d)).sum) *
        (3 ^ (block u a).length * 3 ^ (block v (b + d)).length) := by
  have h := intercept_bound
    (positive_append (block_positive hu ha) (block_positive hv hb))
  have h' := mul_lt_mul_of_pos_left h (show (0 : ℤ) < 2 ^ d by positivity)
  convert h' using 1 <;>
    simp only [C_append, block, C, List.length_nil, pow_zero, mul_zero, add_zero,
      List.length_append, List.length_singleton, List.sum_append, List.sum_singleton,
      pow_add, pow_succ] <;> ring

theorem coprime_cyclotomic {P Z : ℤ} (h : IsCoprime P Z) :
    IsCoprime (P ^ 2 + P * Z + Z ^ 2) Z := by
  obtain ⟨f, g, hfg⟩ := h.mul_left h
  refine ⟨f, g - f * (P + Z), ?_⟩
  linear_combination hfg

theorem retained_lattice {α β Q S C E k : ℤ}
    (hα : 0 < α) (hβ : 0 < β) (hQ : 0 < Q) (hS : 0 < S)
    (hC : 0 < C) (hE : 0 < E) (hk : 1 < k)
    (hcop : IsCoprime (α * β) (Q * S))
    (hcopC : IsCoprime (Q * S) (α * β ^ 2))
    (hcopE : IsCoprime (α * β) (Q ^ 2 * S))
    (hdiv : (α * β) ^ 2 + (α * β) * (Q * S) + (Q * S) ^ 2 ∣
      (k - 1) * (Q * S) * ((α * β) * (β * C) - (Q * S) * (Q * E))) :
    ∃ d t s : ℤ, 0 < d ∧ d < k ∧ 0 < t ∧ 0 < s ∧
      d * (β * C + Q * E) = β * (α * β) * t + Q * (Q * S) * s := by
  let P := α * β
  let Z := Q * S
  let Φ := P ^ 2 + P * Z + Z ^ 2
  let R := P * (β * C) - Z * (Q * E)
  have hΦ : IsCoprime Φ Z := coprime_cyclotomic hcop
  have hdiv' : Φ ∣ (k - 1) * R := by
    apply hΦ.dvd_of_dvd_mul_right
    convert hdiv using 1
    dsimp [Φ, P, Z, R]
    ring
  let d : ℤ := Int.gcd (k - 1) Φ
  have hd : 0 < d := by
    dsimp [d]
    exact_mod_cast Int.gcd_pos_of_ne_zero_left Φ (show k - 1 ≠ 0 by omega)
  have hdk : d < k := by
    have hle : d ≤ k - 1 := Int.le_of_dvd (by omega) (Int.gcd_dvd_left (k - 1) Φ)
    omega
  have hR : Φ ∣ d * R := by
    rw [show d = (k - 1) * Int.gcdA (k - 1) Φ + Φ * Int.gcdB (k - 1) Φ from
      Int.gcd_eq_gcd_ab (k - 1) Φ]
    have h1 := hdiv'.mul_right (Int.gcdA (k - 1) Φ)
    have h2 : Φ ∣ Φ * (Int.gcdB (k - 1) Φ * R) := dvd_mul_right _ _
    convert dvd_add h1 h2 using 1
    ring
  obtain ⟨h, hh⟩ := hR
  have hCt : Z ∣ d * C - h * α := by
    apply hcopC.dvd_of_dvd_mul_left
    refine ⟨d * Q * E + h * (P + Z), ?_⟩
    dsimp [Φ, P, Z, R] at hh ⊢
    linear_combination hh
  have hEs : P ∣ d * E + h * S := by
    apply hcopE.dvd_of_dvd_mul_left
    refine ⟨d * β * C - h * (P + Z), ?_⟩
    dsimp [Φ, P, Z, R] at hh ⊢
    linear_combination -hh
  obtain ⟨t, ht⟩ := hCt
  obtain ⟨s, hs⟩ := hEs
  have hrel : β * t - Q * s = h := by
    have hprod : P * Z * (β * t - Q * s - h) = 0 := by
      dsimp [Φ, P, Z, R] at hh ht hs ⊢
      linear_combination hh - α * β ^ 2 * ht + Q ^ 2 * S * hs
    have hPZ : P * Z ≠ 0 := by dsimp [P, Z]; positivity
    have := (mul_eq_zero.mp hprod).resolve_left hPZ
    omega
  have htpos : 0 < t := by
    by_cases hhpos : 0 ≤ h
    · have hspos : 0 < s := by
        have : 0 < d * E + h * S := by positivity
        rw [hs] at this
        exact (mul_pos_iff_of_pos_left (show 0 < P by dsimp [P]; positivity)).mp this
      have : 0 < Q * s + h := by positivity
      have : 0 < β * t := by linarith [hrel]
      exact (mul_pos_iff_of_pos_left hβ).mp this
    · have : 0 < d * C - h * α := by nlinarith [mul_pos hd hC, mul_pos hα (show 0 < -h by omega)]
      rw [ht] at this
      exact (mul_pos_iff_of_pos_left (show 0 < Z by dsimp [Z]; positivity)).mp this
  have hspos : 0 < s := by
    by_cases hhpos : 0 ≤ h
    · have : 0 < d * E + h * S := by positivity
      rw [hs] at this
      exact (mul_pos_iff_of_pos_left (show 0 < P by dsimp [P]; positivity)).mp this
    · have : 0 < β * t - h := by nlinarith [mul_pos hβ htpos]
      have : 0 < Q * s := by linarith [hrel]
      exact (mul_pos_iff_of_pos_left hQ).mp this
  refine ⟨d, t, s, hd, hdk, htpos, hspos, ?_⟩
  dsimp [P, Z] at ht hs
  linear_combination β * ht + Q * hs + (Q * S - α * β) * hrel



theorem retained_word_constraints {u v : List ℕ} {a b d : ℕ}
    (hu : Positive u) (hv : Positive v) (ha : 0 < a) (hb : 0 < b) (hd : 0 < d)
    (hdiv : D (word u v a b d) ∣ C (word u v a b d)) :
    (2 : ℤ) ^ ((block u a).length + ((block u a).length + (block v (b + d)).length)) <
      3 ^ ((block u a).length + (block v (b + d)).length) ∧
    (3 : ℤ) ^ (block v (b + d)).length *
        2 ^ ((block u a).length + (block v (b + d)).length) <
      2 ^ ((block u a).sum + (block v (b + d)).sum) := by
  let A := block u a
  let B := block v (b + d)
  let α : ℤ := 3 ^ A.length
  let β : ℤ := 3 ^ B.length
  let Q : ℤ := 2 ^ A.sum
  let S : ℤ := 2 ^ B.sum
  let P := α * β
  let Z := Q * S
  let Φ := P ^ 2 + P * Z + Z ^ 2
  let k : ℤ := 2 ^ d
  let X := β * C A
  let Y := Q * C B
  have hα : 0 < α := by dsimp [α]; positivity
  have hβ : 0 < β := by dsimp [β]; positivity
  have hQ : 0 < Q := by dsimp [Q]; positivity
  have hS : 0 < S := by dsimp [S]; positivity
  have hP : 0 < P := mul_pos hα hβ
  have hZ : 0 < Z := mul_pos hQ hS
  have hC : 0 < C A := C_pos A (by simp [A, block])
  have hE : 0 < C B := C_pos B (by simp [B, block])
  have hk : 1 < k := by
    have := (pow_lt_pow_iff_right₀ (by norm_num : (1 : ℤ) < 2)).mpr hd
    simpa [k] using this
  have hc : IsCoprime (3 : ℤ) 2 := ⟨1, -1, by norm_num⟩
  have hcα : IsCoprime α Z := by
    simpa only [α, Z, Q, S, ← pow_add] using
      (hc.pow : IsCoprime ((3 : ℤ) ^ A.length) (2 ^ (A.sum + B.sum)))
  have hcβ : IsCoprime β Z := by
    simpa only [β, Z, Q, S, ← pow_add] using
      (hc.pow : IsCoprime ((3 : ℤ) ^ B.length) (2 ^ (A.sum + B.sum)))
  have hcQ : IsCoprime P Q := by
    simpa only [P, α, β, Q, ← pow_add] using
      (hc.pow : IsCoprime ((3 : ℤ) ^ (A.length + B.length)) (2 ^ A.sum))
  have hcS : IsCoprime P S := by
    simpa only [P, α, β, S, ← pow_add] using
      (hc.pow : IsCoprime ((3 : ℤ) ^ (A.length + B.length)) (2 ^ B.sum))
  have hfactor : D (word u v a b d) = (Z - P) * Φ := by
    unfold D
    rw [word_sum, word_length]
    dsimp [Z, P, Q, S, α, β, Φ, A, B]
    rw [Nat.mul_comm 3 ((block u a).sum + (block v (b + d)).sum),
      Nat.mul_comm 3 ((block u a).length + (block v (b + d)).length),
      pow_mul, pow_mul, pow_add, pow_add]
    ring
  have hΦC : Φ ∣ C (word u v a b d) :=
    dvd_trans ⟨Z - P, by rw [hfactor]; ring⟩ hdiv
  have hpoly : C (word u v a b d) =
      (X + k * Y) * Φ + (k - 1) * Z * (P * X - Z * Y) := by
    rw [six_block_intercept]
    dsimp [X, Y, k, Φ, P, Z, α, β, Q, S, A, B]
    ring
  have hR : Φ ∣ (k - 1) * Z * (P * X - Z * Y) := by
    have hsub := dvd_sub hΦC (dvd_mul_left Φ (X + k * Y))
    rw [hpoly] at hsub
    simpa using hsub
  obtain ⟨d₁, t, s, hd₁, hdk, ht, hs, heq⟩ :=
    retained_lattice hα hβ hQ hS hC hE hk (hcα.mul_left hcβ)
      (by simpa only [pow_two] using (hcα.mul_left (hcβ.mul_left hcβ)).symm)
      (by simpa only [pow_two] using (hcQ.mul_right hcQ).mul_right hcS) hR
  let U : ℤ := 2 ^ (A.length + B.length)
  have hU : 0 < U := by dsimp [U]; positivity
  have hCAB : 0 < β * C A + Q * C B := by positivity
  have hshort : k * U * (β * C A + Q * C B) < Z * P :=
    shortened_intercept_bound hu hv ha hb
  have hlower : β * P + Q * Z ≤ d₁ * (β * C A + Q * C B) := by
    rw [heq]
    have ht1 : 1 ≤ t := by omega
    have hs1 : 1 ≤ s := by omega
    have h1 := mul_le_mul_of_nonneg_left ht1 (show 0 ≤ β * P by positivity)
    have h2 := mul_le_mul_of_nonneg_left hs1 (show 0 ≤ Q * Z by positivity)
    dsimp [P, Z] at h1 h2 ⊢
    nlinarith
  have hupper : U * (β * P + Q * Z) < Z * P := by
    have h1 := mul_le_mul_of_nonneg_left hlower hU.le
    have h2 := mul_lt_mul_of_pos_right hdk hCAB
    have h3 := mul_lt_mul_of_pos_left h2 hU
    nlinarith
  have hfirst : Q * U < P := by
    have hterm : 0 < U * (β * P) := by positivity
    have hmul : (Q * U) * Z < P * Z := by nlinarith
    exact (mul_lt_mul_iff_of_pos_right hZ).mp hmul
  have hsecond : β * U < Z := by
    have hterm : 0 < U * (Q * Z) := by positivity
    have hmul : (β * U) * P < Z * P := by nlinarith
    exact (mul_lt_mul_iff_of_pos_right hP).mp hmul
  have hlen : A.length ≤ A.sum := length_le_sum (block_positive hu ha)
  have hpow : (2 : ℤ) ^ A.length ≤ Q := pow_le_pow_right₀ (by norm_num) hlen
  have hfirst' := lt_of_le_of_lt (mul_le_mul_of_nonneg_right hpow hU.le) hfirst
  constructor
  · simpa only [U, P, α, β, A, B, pow_add] using hfirst'
  · simpa only [U, Z, Q, S, β, A, B, pow_add] using hsecond

theorem word_not_all_twos (u v : List ℕ) (a b d : ℕ) (hd : 0 < d) :
    ¬ ∀ e ∈ word u v a b d, e = 2 := by
  intro h
  have ha := h a (by simp [word, block])
  have had := h (a + d) (by simp [word, block])
  omega

/-- The full six-block word cannot support a positive odd integer cycle of `3x+1`. -/
theorem no_positive_odd_cycle {u v : List ℕ} {a b d : ℕ} {x : ℕ → ℤ}
    (hu : Positive u) (hv : Positive v) (ha : 0 < a) (hb : 0 < b) (hd : 0 < d)
    (hc : IsCycle 1 (word u v a b d) x)
    (hpos : ∀ i, 0 < x i) (hodd : ∀ i, Odd (x i)) : False := by
  have hw : word u v a b d ≠ [] := by simp [word, block]
  have hm : 0 < (word u v a b d).length := List.length_pos_iff.mpr hw
  have hdiv : D (word u v a b d) ∣ C (word u v a b d) := by
    refine ⟨x 0, ?_⟩
    simpa only [one_mul, mul_comm] using hc.cycle_eq.symm
  obtain ⟨hfirst, hsecond⟩ := retained_word_constraints hu hv ha hb hd hdiv
  have hmin := minimum_nine hw hc hpos hodd (word_not_all_twos u v a b d hd)
  have hproduct := CycleInequality.pow_le_bound hc hm 9 (by norm_num) hmin
  rw [word_sum, word_length] at hproduct
  norm_num only at hproduct
  exact ThirdPeriodPowers.integer_power_contradiction
    (block u a).length (block v (b + d)).length
    ((block u a).sum + (block v (b + d)).sum)
    ((block u a).length + (block v (b + d)).length) rfl
    (by simp [block]) hfirst hsecond hproduct

/-- Exact word-level exclusion: the positive discriminant cannot divide the intercept. -/
theorem discriminant_not_dvd_intercept {u v : List ℕ} {a b d : ℕ}
    (hu : Positive u) (hv : Positive v) (ha : 0 < a) (hb : 0 < b) (hd : 0 < d)
    (hD : 0 < D (word u v a b d)) :
    ¬ D (word u v a b d) ∣ C (word u v a b d) := by
  intro hdiv
  obtain ⟨x, hc, hpos, hodd⟩ := integral_cycle_of_dvd
    (by simp [word, block]) (word_positive hu hv ha hb) hD hdiv
  exact no_positive_odd_cycle hu hv ha hb hd hc hpos hodd

/-- A genuine positive-addend control in the six-block family. -/
theorem positive_addend_control :
    ∃ x : ℕ → ℤ, IsCycle 32039 (word [] [] 2 2 1) x ∧ (∀ i, 0 < x i) := by
  have hnonempty : word [] [] 2 2 1 ≠ [] := by decide
  have hD : 0 < D (word [] [] 2 2 1) := by norm_num [word, block, D]
  obtain ⟨hc, _, _, hp, _, _⟩ := reduced_cycle (word [] [] 2 2 1) hnonempty hD
  refine ⟨_, ?_, hp⟩
  convert hc using 1
  norm_num [word, block, D, C]

theorem control_intercepts :
    C (word [] [] 2 2 1) = 12091 ∧ D (word [] [] 2 2 1) = 32039 ∧
    (List.range 6).map (fun i => C ((word [] [] 2 2 1).rotate i)) =
      [12091, 8539, 7207, 13415, 18071, 21563] := by
  norm_num [word, block, C, D, List.range_succ, List.rotate]

end LeanLane.ThirdPeriod

#print axioms LeanLane.CycleEquation.small_step
#print axioms LeanLane.CycleEquation.step_one
#print axioms LeanLane.CycleEquation.step_three
#print axioms LeanLane.CycleEquation.step_five
#print axioms LeanLane.CycleEquation.step_seven
#print axioms LeanLane.CycleEquation.step_eleven
#print axioms LeanLane.CycleEquation.step_seventeen
#print axioms LeanLane.CycleEquation.step_thirteen
#print axioms LeanLane.CycleEquation.periodic_multiple
#print axioms LeanLane.CycleEquation.one_forces_all_twos
#print axioms LeanLane.CycleEquation.minimum_nine
#print axioms LeanLane.ThirdPeriodPowers.first_exponent_bound
#print axioms LeanLane.ThirdPeriodPowers.second_exponent_bound
#print axioms LeanLane.ThirdPeriodPowers.product_exponent_bound
#print axioms LeanLane.ThirdPeriodPowers.integer_power_contradiction
#print axioms LeanLane.RationalCycle.odd_C_of_positive
#print axioms LeanLane.RationalCycle.integral_cycle_of_dvd
#print axioms LeanLane.ThirdPeriod.length_le_sum
#print axioms LeanLane.ThirdPeriod.intercept_bound
#print axioms LeanLane.ThirdPeriod.intercept_last
#print axioms LeanLane.ThirdPeriod.block_positive
#print axioms LeanLane.ThirdPeriod.positive_append
#print axioms LeanLane.ThirdPeriod.word_length
#print axioms LeanLane.ThirdPeriod.word_sum
#print axioms LeanLane.ThirdPeriod.word_positive
#print axioms LeanLane.ThirdPeriod.six_block_intercept
#print axioms LeanLane.ThirdPeriod.shortened_intercept_bound
#print axioms LeanLane.ThirdPeriod.coprime_cyclotomic
#print axioms LeanLane.ThirdPeriod.retained_lattice
#print axioms LeanLane.ThirdPeriod.retained_word_constraints
#print axioms LeanLane.ThirdPeriod.word_not_all_twos
#print axioms LeanLane.ThirdPeriod.no_positive_odd_cycle
#print axioms LeanLane.ThirdPeriod.discriminant_not_dvd_intercept
#print axioms LeanLane.ThirdPeriod.positive_addend_control
#print axioms LeanLane.ThirdPeriod.control_intercepts
