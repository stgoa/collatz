import Mathlib

/-!
# Periodic rigidity of Collatz-invariant colourings (d = 1), with the 3x+5 control

Lane: `claude/lean-lane`. Prose source: main's
`experiments/viewpoints/V002/invariant_colors.md`, §4 and Appendix
("every periodic or eventually periodic d=1 invariant coloring is constant").

Conventions. A colouring is any function `h : ℕ → α`. It is `M`-periodic if
`h (n + M) = h n` for all `n`, and Collatz-invariant if `h (2 * n) = h n` for
all `n` and `h (3 * n + 1) = h n` for all odd `n > 1`. The main theorem
`periodic_invariant_const` shows that for `M > 0` such an `h` is constant on
the positive integers. No statement about convergence of orbits is involved.

Proof structure (all elementary):
* `period_odd_part`: doubling invariance lets the period drop to its odd part;
* `period_div_three`: for an invariant colouring a period `3K` yields the
  period `K` (strong induction on `n`, splitting on parity);
* `succ_eq`: for an odd period `M` coprime to `3`, the two identities
  `h (6x+1) = h x = h (6x+2)` (obtained through odd representatives
  `2x+M` and `x+M`) and the invertibility of `6` modulo `M` give
  `h (n+1) = h n`;
* `const_of_odd_period`: strong induction on an odd period, stripping factors
  of `3` until the period is coprime to `6`.

`control_three_x_plus_five` shows the additive constant matters: the
indicator of `5 ∣ n` is 5-periodic, doubling-invariant and invariant under
`n ↦ 3n + 5` at odd `n`, but not constant.
-/

namespace LeanLane

variable {α : Type*} (h : ℕ → α)

/-- Doubling invariance iterated. -/
theorem pow_two_mul (hdbl : ∀ n, h (2 * n) = h n) (a n : ℕ) : h (2 ^ a * n) = h n := by
  induction a with
  | zero => simp
  | succ a ih => rw [pow_succ, mul_comm (2 ^ a) 2, mul_assoc, hdbl, ih]

/-- Periodicity iterated. -/
theorem add_mul_period {M : ℕ} (hper : ∀ n, h (n + M) = h n) (n k : ℕ) :
    h (n + M * k) = h n := by
  induction k with
  | zero => simp
  | succ k ih => rw [Nat.mul_succ, ← add_assoc, hper, ih]

/-- Equal residues modulo the period give equal colours. -/
theorem eq_of_mod_eq {M : ℕ} (hper : ∀ n, h (n + M) = h n) {a b : ℕ}
    (hab : a % M = b % M) : h a = h b := by
  have key : ∀ x, h x = h (x % M) := fun x => by
    rw [← add_mul_period h hper (x % M) (x / M), Nat.mod_add_div]
  rw [key a, key b, hab]

/-- Periodicity descends to the odd part of the period. -/
theorem period_odd_part {a M' : ℕ} (hper : ∀ n, h (n + 2 ^ a * M') = h n)
    (hdbl : ∀ n, h (2 * n) = h n) : ∀ n, h (n + M') = h n := by
  intro n
  rw [← pow_two_mul h hdbl a (n + M'), mul_add, hper, pow_two_mul h hdbl]

/-- For an invariant colouring, a period `3K` yields the period `K`. -/
theorem period_div_three {K : ℕ} (hper : ∀ n, h (n + 3 * K) = h n)
    (hdbl : ∀ n, h (2 * n) = h n) (htri : ∀ n, Odd n → h (3 * n + 1) = h n) :
    ∀ n, h (n + K) = h n := by
  have odd_step : ∀ n, Odd n → h (n + K) = h n := by
    intro n hn
    have h1 : h (n + K) = h (n + 4 * K) := by
      rw [show n + 4 * K = (n + K) + 3 * K by ring, hper]
    have hodd' : Odd (n + 4 * K) := hn.add_even ⟨2 * K, by ring⟩
    have h2 : h (n + 4 * K) = h (3 * (n + 4 * K) + 1) := (htri _ hodd').symm
    have h3 : h (3 * (n + 4 * K) + 1) = h (3 * n + 1) := by
      rw [show 3 * (n + 4 * K) + 1 = (3 * n + 1) + 3 * K * 4 by ring]
      exact add_mul_period h hper _ _
    rw [h1, h2, h3, htri n hn]
  have pair : ∀ n, 0 < n → h (n + K) = h n ∧ h (n + 2 * K) = h n := by
    intro n
    induction n using Nat.strong_induction_on with
    | _ n ih =>
      intro hn
      rcases Nat.even_or_odd n with ⟨m, hm⟩ | hodd
      · have hm0 : 0 < m := by omega
        have hmn : m < n := by omega
        obtain ⟨ih1, ih2⟩ := ih m hmn hm0
        subst hm
        constructor
        · calc h (m + m + K) = h (m + m + K + 3 * K) := (hper _).symm
            _ = h (2 * (m + 2 * K)) := by congr 1; ring
            _ = h (m + 2 * K) := hdbl _
            _ = h m := ih2
            _ = h (2 * m) := (hdbl m).symm
            _ = h (m + m) := by congr 1; ring
        · calc h (m + m + 2 * K) = h (2 * (m + K)) := by congr 1; ring
            _ = h (m + K) := hdbl _
            _ = h m := ih1
            _ = h (2 * m) := (hdbl m).symm
            _ = h (m + m) := by congr 1; ring
      · refine ⟨odd_step n hodd, ?_⟩
        have hodd2 : Odd (n + 2 * K) := hodd.add_even (even_two_mul K)
        have := odd_step (n + 2 * K) hodd2
        rw [show n + 2 * K + K = n + 3 * K by ring, hper] at this
        exact this.symm
  intro n
  rcases Nat.eq_zero_or_pos n with rfl | hn
  · rcases Nat.eq_zero_or_pos K with rfl | hK0
    · simp
    · have := (pair (2 * K) (by omega)).1
      calc h (0 + K) = h K := by rw [zero_add]
        _ = h (2 * K) := (hdbl K).symm
        _ = h (2 * K + K) := this.symm
        _ = h (0 + 3 * K) := by congr 1; ring
        _ = h 0 := hper 0
  · exact (pair n hn).1

/-- With an odd period `M > 1` coprime to `3`, neighbours have equal colours. -/
theorem succ_eq {M : ℕ} (hM : 1 < M) (hModd : Odd M) (hcop : Nat.Coprime 6 M)
    (hper : ∀ n, h (n + M) = h n) (hdbl : ∀ n, h (2 * n) = h n)
    (htri : ∀ n, Odd n → h (3 * n + 1) = h n) :
    ∀ n, 0 < n → h (n + 1) = h n := by
  intro n hn
  obtain ⟨y, -, hy⟩ := Nat.exists_mul_mod_eq_one_of_coprime hcop hM
  have h6 : 6 * y ≡ 1 [MOD M] := by
    unfold Nat.ModEq; rw [hy, Nat.mod_eq_of_lt hM]
  set x := y * (n - 1) with hx
  have hmod1 : 6 * x + 1 ≡ n [MOD M] := by
    have e : 6 * x + 1 = 6 * y * (n - 1) + 1 := by rw [hx]; ring
    rw [e]
    have := (h6.mul_right (n - 1)).add_right 1
    rwa [one_mul, Nat.sub_add_cancel hn] at this
  have hmod2 : 6 * x + 2 ≡ n + 1 [MOD M] := by
    have e : 6 * x + 2 = 6 * y * (n - 1) + 2 := by rw [hx]; ring
    rw [e]
    have := (h6.mul_right (n - 1)).add_right 2
    rwa [one_mul, show n - 1 + 2 = n + 1 by omega] at this
  have hA : h (6 * x + 1) = h x := by
    have hodd : Odd (2 * x + M) := (even_two_mul x).add_odd hModd
    calc h (6 * x + 1) = h (6 * x + 1 + M * 3) := (add_mul_period h hper _ _).symm
      _ = h (3 * (2 * x + M) + 1) := by congr 1; ring
      _ = h (2 * x + M) := htri _ hodd
      _ = h (2 * x) := hper _
      _ = h x := hdbl _
  have hB : h (6 * x + 2) = h x := by
    rcases Nat.even_or_odd x with hev | hodd
    · have hodd' : Odd (x + M) := hev.add_odd hModd
      calc h (6 * x + 2) = h (6 * x + 2 + M * 6) := (add_mul_period h hper _ _).symm
        _ = h (2 * (3 * (x + M) + 1)) := by congr 1; ring
        _ = h (3 * (x + M) + 1) := hdbl _
        _ = h (x + M) := htri _ hodd'
        _ = h x := hper _
    · calc h (6 * x + 2) = h (2 * (3 * x + 1)) := by congr 1; ring
        _ = h (3 * x + 1) := hdbl _
        _ = h x := htri _ hodd
  calc h (n + 1) = h (6 * x + 2) := (eq_of_mod_eq h hper hmod2).symm
    _ = h x := hB
    _ = h (6 * x + 1) := hA.symm
    _ = h n := eq_of_mod_eq h hper hmod1

/-- Neighbour equality on the positive integers gives constancy there. -/
theorem const_of_succ (hsucc : ∀ n, 0 < n → h (n + 1) = h n) : ∀ n, 0 < n → h n = h 1 := by
  intro n hn
  induction n with
  | zero => omega
  | succ k ih =>
    rcases Nat.eq_zero_or_pos k with rfl | hk
    · rfl
    · rw [hsucc k hk, ih hk]

/-- An invariant colouring with an odd period is constant on the positive integers. -/
theorem const_of_odd_period (hdbl : ∀ n, h (2 * n) = h n)
    (htri : ∀ n, Odd n → h (3 * n + 1) = h n) :
    ∀ M, Odd M → (∀ n, h (n + M) = h n) → ∀ n, 0 < n → h n = h 1 := by
  intro M
  induction M using Nat.strong_induction_on with
  | _ M ih =>
    intro hModd hper
    by_cases h3 : 3 ∣ M
    · obtain ⟨K, hK⟩ := h3
      have hKodd : Odd K := by
        rw [hK] at hModd; exact (Nat.odd_mul.mp hModd).2
      have hKpos : 0 < K := hKodd.pos
      have hKlt : K < M := by omega
      have hper3 : ∀ n, h (n + 3 * K) = h n := fun n => by rw [← hK]; exact hper n
      exact ih K hKlt hKodd (period_div_three h hper3 hdbl htri)
    · have h2 : Nat.Coprime 2 M := (Nat.Prime.coprime_iff_not_dvd Nat.prime_two).2 (by
        intro hd
        exact (Nat.not_even_iff_odd.mpr hModd) (even_iff_two_dvd.mpr hd))
      have h3' : Nat.Coprime 3 M := (Nat.Prime.coprime_iff_not_dvd Nat.prime_three).2 h3
      have hcop : Nat.Coprime 6 M := by
        have := Nat.Coprime.mul_left h2 h3'
        norm_num at this
        exact this
      rcases Nat.lt_or_ge 1 M with hM1 | hM1
      · exact const_of_succ h (succ_eq h hM1 hModd hcop hper hdbl htri)
      · have hM : M = 1 := by
          have := hModd.pos
          omega
        subst hM
        exact const_of_succ h (fun n _ => hper n)

/-- **Periodic rigidity (d = 1).** Every `M`-periodic colouring (`M > 0`) with
`h (2n) = h n` for all `n` and `h (3n+1) = h n` for all odd `n > 1` is constant
on the positive integers. -/
theorem periodic_invariant_const {M : ℕ} (hM : 0 < M)
    (hper : ∀ n, h (n + M) = h n) (hdbl : ∀ n, h (2 * n) = h n)
    (htri : ∀ n, Odd n → 1 < n → h (3 * n + 1) = h n) :
    ∀ n, 0 < n → h n = h 1 := by
  have htri' : ∀ n, Odd n → h (3 * n + 1) = h n := by
    intro n hn
    rcases Nat.lt_or_ge 1 n with h1 | h1
    · exact htri n hn h1
    · have hn1 : n = 1 := by
        obtain ⟨k, hk⟩ := hn
        omega
      subst hn1
      calc h (3 * 1 + 1) = h (2 * 2) := by norm_num
        _ = h 2 := hdbl 2
        _ = h (2 * 1) := by norm_num
        _ = h 1 := hdbl 1
  obtain ⟨a, M', hM'not, hMeq⟩ := Nat.exists_eq_pow_mul_and_not_dvd hM.ne' 2 (by norm_num)
  have hM'odd : Odd M' := Nat.not_even_iff_odd.mp (fun he => hM'not (even_iff_two_dvd.mp he))
  subst hMeq
  exact const_of_odd_period h hdbl htri' M' hM'odd (period_odd_part h hper hdbl)

/-- **The `3x+5` control.** The indicator of `5 ∣ n` is 5-periodic, invariant under
doubling and under `n ↦ 3n+5` at odd `n`, and not constant. -/
theorem control_three_x_plus_five :
    ∃ g : ℕ → Bool, (∀ n, g (n + 5) = g n) ∧ (∀ n, g (2 * n) = g n) ∧
      (∀ n, Odd n → g (3 * n + 5) = g n) ∧ g 1 ≠ g 5 := by
  refine ⟨fun n => decide (5 ∣ n), ?_, ?_, ?_, ?_⟩
  · intro n; simp only [decide_eq_decide]; omega
  · intro n; simp only [decide_eq_decide]; omega
  · intro n _; simp only [decide_eq_decide]; omega
  · decide

end LeanLane
