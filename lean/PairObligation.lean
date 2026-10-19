import Solution.Basic

/-!
# The W5 pair obligation and the `u ↔ 18u+5` reformulation (queue item 4, partial)

Lane: `claude/lean-lane`. Prose sources: `ROUTE_MAP.md` R.1 and
`docs/RESULTS.md` R40 on main.

Setting. `collatzAccel n = (3n+1) / 2^{v₂(3n+1)}` is the library's Syracuse
map `S`. `Meet f a b` says the `f`-orbits of `a` and `b` meet at possibly
different times. For `w = 4u + 1` the pair obligation `P(w) = [3w] − [w]` has a
finite exact current iff the orbits of `3w` and `w` meet (the repository's
graph-current/meeting equivalence, not restated here).

Verified in this file (all with the standard axioms):

* `collatzAccel_four_mul_add_one`: `S (4u+1) = S u` for every `u`;
* `collatzAccel_three_mul`: `S (3 (4u+1)) = 18u + 5` for every `u`;
* `pair_iff`: `Meet S (3 (4u+1)) (4u+1) ↔ Meet S (18u+5) u`, so the W5 pair
  obligation at `w = 4u+1` is exactly the meeting of `u` with `18u+5`;
* `collatz_imp_pairs_meet`: if every positive integer reaches `1` under the
  ordinary map, then for every odd `u` the Syracuse orbits of `u` and `18u+5`
  meet (the easy direction of R.1). This uses `accel_reaches_one`: an odd `n`
  that reaches `1` under `collatz` reaches `1` under `collatzAccel`.

Not formalised: the converse of R.1 (all pairs meet ⇒ Collatz). In the
repository it rests on the frozen framework (R25 normal form, R37 critical
index, R40 elimination, R43 strict-rank induction); a direct
minimal-counterexample argument does not close it (see STATE.md). No sorry is
used; the converse is simply not asserted. Collatz remains open.
-/

namespace LeanLane
namespace Pair

/-- The orbits of `a` and `b` under `f` meet, at possibly different times. -/
def Meet (f : ℕ → ℕ) (a b : ℕ) : Prop := ∃ i j, f^[i] a = f^[j] b

theorem meet_comm {f : ℕ → ℕ} {a b : ℕ} : Meet f a b ↔ Meet f b a :=
  ⟨fun ⟨i, j, h⟩ => ⟨j, i, h.symm⟩, fun ⟨i, j, h⟩ => ⟨j, i, h.symm⟩⟩

theorem meet_apply_left {f : ℕ → ℕ} {a b : ℕ} : Meet f (f a) b ↔ Meet f a b := by
  constructor
  · rintro ⟨i, j, h⟩
    exact ⟨i + 1, j, by rw [Function.iterate_succ_apply]; exact h⟩
  · rintro ⟨i, j, h⟩
    refine ⟨i, j + 1, ?_⟩
    calc f^[i] (f a) = f^[i + 1] a := (Function.iterate_succ_apply f i a).symm
      _ = f (f^[i] a) := Function.iterate_succ_apply' f i a
      _ = f (f^[j] b) := by rw [h]
      _ = f^[j + 1] b := (Function.iterate_succ_apply' f j b).symm

theorem meet_apply_right {f : ℕ → ℕ} {a b : ℕ} : Meet f a (f b) ↔ Meet f a b := by
  rw [meet_comm, meet_apply_left, meet_comm]

/-! ### The two exact identities behind the W5 pair obligation -/

theorem collatzAccel_four_mul_add_one (u : ℕ) : collatzAccel (4 * u + 1) = collatzAccel u := by
  unfold collatzAccel
  have h1 : 3 * (4 * u + 1) + 1 = 2 ^ 2 * (3 * u + 1) := by ring
  rw [h1, padicValNat.mul (by norm_num) (by omega), padicValNat.prime_pow, pow_add,
    Nat.mul_div_mul_left _ _ (by norm_num : 0 < 2 ^ 2)]

theorem collatzAccel_three_mul (u : ℕ) : collatzAccel (3 * (4 * u + 1)) = 18 * u + 5 := by
  unfold collatzAccel
  have h1 : 3 * (3 * (4 * u + 1)) + 1 = 2 * (18 * u + 5) := by ring
  have hodd : ¬ 2 ∣ 18 * u + 5 := by omega
  rw [h1, padicValNat.mul (by norm_num) (by omega), padicValNat.self (by norm_num),
    padicValNat.eq_zero_of_not_dvd hodd, add_zero, pow_one,
    Nat.mul_div_cancel_left _ (by norm_num : 0 < 2)]

/-- **The W5 pair obligation is the `u ↔ 18u+5` meeting.** -/
theorem pair_iff (u : ℕ) :
    Meet collatzAccel (3 * (4 * u + 1)) (4 * u + 1) ↔ Meet collatzAccel (18 * u + 5) u := by
  rw [← meet_apply_left, ← meet_apply_right, collatzAccel_three_mul,
    collatzAccel_four_mul_add_one, meet_apply_right]

/-! ### Ordinary orbits versus Syracuse orbits -/

theorem collatz_two_mul (x : ℕ) : collatz (2 * x) = x := by
  unfold collatz
  split <;> omega

theorem collatz_odd {m : ℕ} (hm : Odd m) : collatz m = 3 * m + 1 := by
  unfold collatz
  have := Nat.odd_iff.mp hm
  split <;> omega

theorem collatz_iterate_halve (k : ℕ) : ∀ x, 2 ^ k ∣ x → collatz^[k] x = x / 2 ^ k := by
  induction k with
  | zero => intro x _; simp
  | succ k ih =>
    intro x hx
    obtain ⟨y, hy⟩ := hx
    have hx2 : x = 2 * (2 ^ k * y) := by rw [hy, pow_succ]; ring
    rw [Function.iterate_succ_apply, hx2, collatz_two_mul, ih _ ⟨y, rfl⟩,
      Nat.mul_div_cancel_left _ (by positivity), pow_succ,
      show 2 * (2 ^ k * y) = 2 ^ k * y * 2 by ring,
      Nat.mul_div_mul_right _ _ (by norm_num : 0 < 2),
      Nat.mul_div_cancel_left _ (by positivity)]

/-- One `3n+1` step followed by the full run of halvings is one Syracuse step. -/
theorem collatz_iterate_accel {n : ℕ} (hn : Odd n) :
    collatz^[padicValNat 2 (3 * n + 1) + 1] n = collatzAccel n := by
  rw [Function.iterate_succ_apply, collatz_odd hn, collatz_iterate_halve _ _ pow_padicValNat_dvd]
  rfl

theorem collatzAccel_odd (n : ℕ) : Odd (collatzAccel n) := by
  unfold collatzAccel
  obtain ⟨e, y, hy2, hxy⟩ :=
    Nat.exists_eq_pow_mul_and_not_dvd (show 3 * n + 1 ≠ 0 by omega) 2 (by norm_num)
  have hy0 : y ≠ 0 := by
    rintro rfl
    simp at hxy
  rw [hxy, padicValNat.mul (by positivity) hy0, padicValNat.prime_pow,
    padicValNat.eq_zero_of_not_dvd hy2, add_zero, Nat.mul_div_cancel_left _ (by positivity)]
  exact Nat.not_even_iff_odd.mp (fun he => hy2 (even_iff_two_dvd.mp he))

theorem three_iterate_one : collatz^[3] 1 = 1 := by decide

theorem iterate_one_mod_three (j : ℕ) : collatz^[j] 1 = collatz^[j % 3] 1 := by
  conv_lhs => rw [← Nat.mod_add_div j 3, Function.iterate_add_apply, Function.iterate_mul]
  congr 1
  induction j / 3 with
  | zero => rfl
  | succ q ih => rw [Function.iterate_succ_apply, three_iterate_one, ih]

/-- The only odd value on the orbit of `1` is `1` itself. -/
theorem eq_one_of_odd_iterate_one {j : ℕ} (hodd : Odd (collatz^[j] 1)) : collatz^[j] 1 = 1 := by
  rw [iterate_one_mod_three] at hodd ⊢
  have h3 : j % 3 < 3 := Nat.mod_lt _ (by norm_num)
  interval_cases (j % 3)
  · rfl
  · exact absurd hodd (by decide)
  · exact absurd hodd (by decide)

/-- An odd integer that reaches `1` under the ordinary map reaches `1` under the
Syracuse map. -/
theorem accel_reaches_one {n : ℕ} (hn : Odd n) {K : ℕ} (hK : collatz^[K] n = 1) :
    ∃ k, collatzAccel^[k] n = 1 := by
  induction K using Nat.strong_induction_on generalizing n with
  | _ K ih =>
    set v := padicValNat 2 (3 * n + 1) with hv
    have hstep : collatz^[v + 1] n = collatzAccel n := collatz_iterate_accel hn
    rcases Nat.lt_or_ge K (v + 1) with hlt | hge
    · -- `1` is reached within the first Syracuse step, so that step lands on `1`
      have h1 : collatzAccel n = collatz^[v + 1 - K] 1 := by
        calc collatzAccel n = collatz^[v + 1] n := hstep.symm
          _ = collatz^[(v + 1 - K) + K] n := by rw [Nat.sub_add_cancel hlt.le]
          _ = collatz^[v + 1 - K] (collatz^[K] n) := Function.iterate_add_apply _ _ _ _
          _ = collatz^[v + 1 - K] 1 := by rw [hK]
      refine ⟨1, ?_⟩
      rw [Function.iterate_one, h1]
      exact eq_one_of_odd_iterate_one (h1 ▸ collatzAccel_odd n)
    · obtain ⟨k, hk⟩ := ih (K - (v + 1)) (by omega) (collatzAccel_odd n) (by
        rw [← hstep, ← Function.iterate_add_apply, Nat.sub_add_cancel hge, hK])
      exact ⟨k + 1, by rw [Function.iterate_succ_apply, hk]⟩

/-- **Easy direction of R.1.** If every positive integer reaches `1`, then for every
odd `u` the Syracuse orbits of `u` and `18u+5` meet. -/
theorem collatz_imp_pairs_meet (hcol : ∀ n, 0 < n → ∃ k, collatz^[k] n = 1) :
    ∀ u, Odd u → Meet collatzAccel (18 * u + 5) u := by
  intro u hu
  obtain ⟨K₁, hK₁⟩ := hcol (18 * u + 5) (by omega)
  obtain ⟨K₂, hK₂⟩ := hcol u hu.pos
  obtain ⟨i, hi⟩ := accel_reaches_one ⟨9 * u + 2, by ring⟩ hK₁
  obtain ⟨j, hj⟩ := accel_reaches_one hu hK₂
  exact ⟨i, j, by rw [hi, hj]⟩

/-- The converse of R.1, stated but not asserted here: in the repository its proof
runs through the frozen framework (R25, R37, R40, R43), which is not formalised. -/
def R1Converse : Prop :=
  (∀ u, Odd u → Meet collatzAccel (18 * u + 5) u) → ∀ n, 0 < n → ∃ k, collatz^[k] n = 1

end Pair
end LeanLane
