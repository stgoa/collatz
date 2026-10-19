import Solution.Basic

/-!
# The dichotomy corollary over the audited positive-density theorem (queue item 3)

Lane: `claude/lean-lane`. Imports `Solution.Basic` of
`AxiomMath/CollatzPositiveDensity` @ `3a38bfbb` (audited in
`experiments/lean_audit`), whose theorem
`positive_density_collatz_and_collatzAccel_reaches_of_not_three_dvd` states: for
every target `t` with `¬ 3 ∣ t` and every `N ≥ collatzDensityThresholdDep t`,
at least `collatzDensityDep t · N` of the `n < N` are odd and reach `t` under
the ordinary map `collatz` within `⌊10.46 log(n/t)⌋` steps (and the odd part
of `t` under the accelerated map).

Here `Bad n` means that `n` never reaches `1` under the ordinary map
`collatz`, in any number of steps. The results:

* `bad_positive_lower_density`: if some positive `n` is bad, there are an
  explicit rational `c > 0` and an explicit threshold `X₀` with
  `c · N ≤ #{n < N : 0 < n ∧ Bad n}` for every `N ≥ X₀`, i.e. the bad set
  has positive lower natural density. The witnesses are
  `collatzDensityDep t` and `collatzDensityThresholdDep t` for the bad target
  `t = 3m + 1`, `m` the odd part of the given bad `n`.
* `collatz_of_bad_density_zero`: if the bad set has *lower* natural density
  zero (for every `c > 0` and every `X₀` some `N ≥ X₀` has fewer than `c · N`
  bad numbers below it; this is weaker than natural density zero), then every
  positive integer reaches `1`.

Clock and map: iterates of `collatz`, exactly as in the imported theorem.
Nothing here proves that any `n` is bad or that none is; Collatz remains open.
-/

namespace LeanLane
namespace Dichotomy

open Finset
open scoped Classical

/-- `n` never reaches `1` under the ordinary Collatz map. -/
def Bad (n : ℕ) : Prop := ∀ k, collatz^[k] n ≠ 1

theorem collatz_two_mul (x : ℕ) : collatz (2 * x) = x := by
  unfold collatz
  split <;> omega

theorem collatz_odd {m : ℕ} (hm : Odd m) : collatz m = 3 * m + 1 := by
  unfold collatz
  have := Nat.odd_iff.mp hm
  split <;> omega

theorem iterate_two_pow (v m : ℕ) : collatz^[v] (2 ^ v * m) = m := by
  induction v with
  | zero => simp
  | succ v ih =>
    rw [Function.iterate_succ_apply, show 2 ^ (v + 1) * m = 2 * (2 ^ v * m) by ring,
      collatz_two_mul, ih]

theorem bad_iterate {n : ℕ} (hn : Bad n) (k : ℕ) : Bad (collatz^[k] n) := by
  intro j
  rw [← Function.iterate_add_apply]
  exact hn (j + k)

theorem three_iterate_one : collatz^[3] 1 = 1 := by decide

theorem iterate_three_mul_one (j : ℕ) : (collatz^[3])^[j] 1 = 1 := by
  induction j with
  | zero => rfl
  | succ j ih => rw [Function.iterate_succ_apply, three_iterate_one, ih]

theorem not_bad_iterate_one (j : ℕ) : ¬ Bad (collatz^[j] 1) := by
  intro hb
  apply hb (2 * j)
  rw [← Function.iterate_add_apply, show 2 * j + j = 3 * j by ring, Function.iterate_mul]
  exact iterate_three_mul_one j

/-- Anything that reaches a bad number is bad. -/
theorem bad_of_reach {t n r : ℕ} (ht : Bad t) (hr : collatz^[r] n = t) : Bad n := by
  intro k hk
  rcases Nat.lt_or_ge k r with hkr | hkr
  · have h1 : t = collatz^[r - k] 1 := by
      rw [← hk, ← Function.iterate_add_apply, Nat.sub_add_cancel hkr.le, hr]
    exact not_bad_iterate_one (r - k) (h1 ▸ ht)
  · apply ht (k - r)
    rw [← hr, ← Function.iterate_add_apply, Nat.sub_add_cancel hkr, hk]

/-- A positive bad number has a bad iterate not divisible by `3`: `3m + 1` for its
odd part `m`. -/
theorem exists_bad_target {n : ℕ} (hn0 : 0 < n) (hn : Bad n) :
    ∃ t, 0 < t ∧ ¬ 3 ∣ t ∧ Bad t := by
  obtain ⟨v, m, hm2, hnm⟩ := Nat.exists_eq_pow_mul_and_not_dvd hn0.ne' 2 (by norm_num)
  have hmodd : Odd m := Nat.not_even_iff_odd.mp (fun he => hm2 (even_iff_two_dvd.mp he))
  refine ⟨3 * m + 1, by omega, by omega, ?_⟩
  have h1 : collatz^[v + 1] n = 3 * m + 1 := by
    rw [Function.iterate_succ_apply', hnm, iterate_two_pow, collatz_odd hmodd]
  rw [← h1]
  exact bad_iterate hn (v + 1)

/-- **Dichotomy, positive branch.** If some positive integer never reaches `1`, the
set of positive integers that never reach `1` has positive lower natural density,
with the explicit constants of the audited theorem at the bad target. -/
theorem bad_positive_lower_density (hex : ∃ n, 0 < n ∧ Bad n) :
    ∃ (c : ℚ) (X₀ : ℕ), 0 < c ∧ ∀ N, X₀ ≤ N →
      c * N ≤ #{n ∈ range N | 0 < n ∧ Bad n} := by
  obtain ⟨n₀, hn₀, hbad⟩ := hex
  obtain ⟨t, ht0, ht3, htbad⟩ := exists_bad_target hn₀ hbad
  refine ⟨collatzDensityDep t, collatzDensityThresholdDep t, ?_, fun N hN => ?_⟩
  · have htq : (0 : ℚ) < t := by exact_mod_cast ht0
    -- `unfold`, `positivity` and a bare `rw` try to normalise the tower `2^2^2^87640`
    -- and overflow the recursion limit; stating the positivity for a general `q` and
    -- closing by definitional unfolding never evaluates it.
    have key : ∀ q : ℚ, 0 < q → 0 < 1 / (q ^ 4 * 2 ^ 2 ^ 2 ^ 87640) :=
      fun q hq => one_div_pos.mpr (mul_pos (pow_pos hq 4) (pow_pos two_pos _))
    exact key _ htq
  · have hmain := positive_density_collatz_and_collatzAccel_reaches_of_not_three_dvd ht3 hN
    refine le_trans hmain (Nat.cast_le.mpr (card_le_card ?_))
    intro n hn
    rw [mem_filter] at hn ⊢
    obtain ⟨hnr, hodd, ⟨r, -, hr⟩, -⟩ := hn
    refine ⟨hnr, ?_, bad_of_reach htbad hr⟩
    obtain ⟨k, hk⟩ := hodd
    omega

/-- **Dichotomy, contrapositive.** If the bad set has *lower* natural density zero
(for every `c > 0` and every `X₀`, some `N ≥ X₀` has fewer than `c · N` bad numbers
below it — the negation of the positive branch's conclusion, weaker than density
zero), every positive integer reaches `1` under the ordinary Collatz map. -/
theorem collatz_of_bad_density_zero
    (hzero : ∀ c : ℚ, 0 < c → ∀ X₀ : ℕ, ∃ N, X₀ ≤ N ∧
      (#{n ∈ range N | 0 < n ∧ Bad n} : ℚ) < c * N) :
    ∀ n, 0 < n → ∃ k, collatz^[k] n = 1 := by
  intro n hn
  by_contra hcon
  have hbad : Bad n := fun k hk => hcon ⟨k, hk⟩
  obtain ⟨c, X₀, hc, hge⟩ := bad_positive_lower_density ⟨n, hn, hbad⟩
  obtain ⟨N, hN, hlt⟩ := hzero c hc X₀
  exact absurd (hge N hN) (not_le.mpr hlt)

end Dichotomy
end LeanLane
