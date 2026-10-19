import Mathlib

/-!
# Odd-eventually-periodic rigidity of Collatz-invariant colourings (V004-i)

Lane: `claude/lean-lane`. Prose source: main's
`experiments/viewpoints/V004/GLOBAL_RIGIDITY.md`, §2 (identities) and §5
(the elementary finish after Cobham): if a colouring `h` satisfies

* `h (2 * n) = h n` for all `n`,
* `h (3 * n + 1) = h n` for all odd `n > 1`,

and its odd restriction `b n = h (2 * n + 1)` is eventually periodic, then
`h` is constant on the positive integers. This is the whole content of V004
except the two external inputs (Cobham's theorem and the finite-kernel
characterisation of automaticity), which produce the eventual periodicity of
`b` from binary automaticity. It strictly strengthens `PeriodicRigidity.lean`.

The proof is integer-level and uses three identities of `b`, all derived from
the two rules: `b (4n+2) = b n`, `b (3n+2) = b (2n+1)`, `b (4n) = b (3n)`.

1. `period_of_eventually`: an eventual period `M = 2^e L` of `b` is a global
   period `L` (odd), because `G n = 4n+2` preserves `b` and
   `G^[k] (n+L) = G^[k] n + 4^k L`.
2. `period_div_three`: a period `3K` of `b` yields the period `K` (strong
   induction on `n`, splitting `n` modulo 4).
3. `succ_eq`: for a period `L > 1` coprime to 6, with `c = (L+1)/2`,
   `b (3y+2) = b y = b (3 (y+c))` for all `y`; choosing `y` with
   `3 (y+c) ≡ n (mod L)` gives `b (n+c) = b n`, hence `b (n+1) = b n`.
4. `const_of_period` strips factors of 3 and concludes;
   `odd_eventually_periodic_const` transfers constancy of `b` to all positive
   integers by doubling.
-/

namespace LeanLane
namespace OddEP

variable {α : Type*} (h : ℕ → α)

/-- The odd restriction of a colouring. -/
def b (n : ℕ) : α := h (2 * n + 1)

/-- The map `n ↦ 4n+2`. -/
def G (n : ℕ) : ℕ := 4 * n + 2

/-! ### Identities derived from the two colouring rules -/

theorem pow_two_mul (hdbl : ∀ n, h (2 * n) = h n) (a n : ℕ) : h (2 ^ a * n) = h n := by
  induction a with
  | zero => simp
  | succ a ih => rw [pow_succ, mul_comm (2 ^ a) 2, mul_assoc, hdbl, ih]

/-- The odd rule, including `n = 1`. -/
theorem tri' (hdbl : ∀ n, h (2 * n) = h n)
    (htri : ∀ n, Odd n → 1 < n → h (3 * n + 1) = h n) (n : ℕ) (hn : Odd n) :
    h (3 * n + 1) = h n := by
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

/-- V004 (2), first identity: `h (3m+1) = h (4m+1)`. -/
theorem id2 (hdbl : ∀ n, h (2 * n) = h n)
    (htri : ∀ n, Odd n → 1 < n → h (3 * n + 1) = h n) (m : ℕ) :
    h (3 * m + 1) = h (4 * m + 1) := by
  have := tri' h hdbl htri (4 * m + 1) ⟨2 * m, by ring⟩
  rw [show 3 * (4 * m + 1) + 1 = 2 * (2 * (3 * m + 1)) by ring, hdbl, hdbl] at this
  exact this

/-- V004 (4): `h (4x+1) = h x` for odd `x`. -/
theorem id4 (hdbl : ∀ n, h (2 * n) = h n)
    (htri : ∀ n, Odd n → 1 < n → h (3 * n + 1) = h n) (x : ℕ) (hx : Odd x) :
    h (4 * x + 1) = h x := by
  rw [← id2 h hdbl htri x]
  exact tri' h hdbl htri x hx

/-- `b (4n+2) = b n`. -/
theorem B1 (hdbl : ∀ n, h (2 * n) = h n)
    (htri : ∀ n, Odd n → 1 < n → h (3 * n + 1) = h n) (n : ℕ) :
    b h (4 * n + 2) = b h n := by
  unfold b
  rw [show 2 * (4 * n + 2) + 1 = 4 * (2 * n + 1) + 1 by ring]
  exact id4 h hdbl htri _ ⟨n, rfl⟩

/-- `b (3n+2) = b (2n+1)`. -/
theorem B2 (hdbl : ∀ n, h (2 * n) = h n)
    (htri : ∀ n, Odd n → 1 < n → h (3 * n + 1) = h n) (n : ℕ) :
    b h (3 * n + 2) = b h (2 * n + 1) := by
  unfold b
  have := tri' h hdbl htri (4 * n + 3) ⟨2 * n + 1, by ring⟩
  rw [show 3 * (4 * n + 3) + 1 = 2 * (2 * (3 * n + 2) + 1) by ring, hdbl] at this
  rw [show 2 * (2 * n + 1) + 1 = 4 * n + 3 by ring]
  exact this

/-- `b (4n) = b (3n)`. -/
theorem B4 (hdbl : ∀ n, h (2 * n) = h n)
    (htri : ∀ n, Odd n → 1 < n → h (3 * n + 1) = h n) (n : ℕ) :
    b h (4 * n) = b h (3 * n) := by
  unfold b
  have := tri' h hdbl htri (2 * (4 * n) + 1) ⟨4 * n, rfl⟩
  rw [show 3 * (2 * (4 * n) + 1) + 1 = 2 * (2 * (2 * (3 * n) + 1)) by ring, hdbl, hdbl] at this
  exact this.symm

/-! ### Periods of `b` -/

theorem add_mul_period {P : ℕ} (hper : ∀ n, b h (n + P) = b h n) (n k : ℕ) :
    b h (n + P * k) = b h n := by
  induction k with
  | zero => simp
  | succ k ih => rw [Nat.mul_succ, ← add_assoc, hper, ih]

theorem eq_of_mod_eq {P : ℕ} (hper : ∀ n, b h (n + P) = b h n) {x y : ℕ}
    (hxy : x % P = y % P) : b h x = b h y := by
  have key : ∀ x, b h x = b h (x % P) := fun x => by
    rw [← add_mul_period h hper (x % P) (x / P), Nat.mod_add_div]
  rw [key x, key y, hxy]

theorem G_iter_add (k : ℕ) : ∀ x y, G^[k] (x + y) = G^[k] x + 4 ^ k * y := by
  induction k with
  | zero => intro x y; simp
  | succ k ih =>
    intro x y
    rw [Function.iterate_succ_apply, Function.iterate_succ_apply,
      show G (x + y) = G x + 4 * y by unfold G; ring, ih, pow_succ]
    ring

theorem le_G_iter (k n : ℕ) : 2 * k ≤ G^[k] n := by
  induction k generalizing n with
  | zero => simp
  | succ k ih =>
    rw [Function.iterate_succ_apply']
    have := ih n
    show 2 * (k + 1) ≤ 4 * G^[k] n + 2
    omega

theorem b_G_iter (hdbl : ∀ n, h (2 * n) = h n)
    (htri : ∀ n, Odd n → 1 < n → h (3 * n + 1) = h n) (k n : ℕ) :
    b h (G^[k] n) = b h n := by
  induction k generalizing n with
  | zero => simp
  | succ k ih =>
    rw [Function.iterate_succ_apply, ih]
    exact B1 h hdbl htri n

/-- An eventual period of `b` yields a global odd period. -/
theorem period_of_eventually (hdbl : ∀ n, h (2 * n) = h n)
    (htri : ∀ n, Odd n → 1 < n → h (3 * n + 1) = h n) {N M : ℕ} (hM : 0 < M)
    (hev : ∀ n, N ≤ n → b h (n + M) = b h n) :
    ∃ L, Odd L ∧ ∀ n, b h (n + L) = b h n := by
  obtain ⟨e, L, hLnot, hMeq⟩ := Nat.exists_eq_pow_mul_and_not_dvd hM.ne' 2 (by norm_num)
  have hLodd : Odd L := Nat.not_even_iff_odd.mp (fun he => hLnot (even_iff_two_dvd.mp he))
  refine ⟨L, hLodd, fun n => ?_⟩
  have hev_mul : ∀ x, N ≤ x → ∀ j, b h (x + M * j) = b h x := by
    intro x hx j
    induction j with
    | zero => simp
    | succ j ih =>
      rw [Nat.mul_succ, ← add_assoc, hev _ (le_trans hx (Nat.le_add_right _ _)), ih]
  set k := N + e with hk
  have hbig : N ≤ G^[k] n := by
    have := le_G_iter k n
    omega
  have hdvd : 2 ^ e ∣ 4 ^ k := by
    rw [show (4 : ℕ) = 2 ^ 2 by norm_num, ← pow_mul]
    exact pow_dvd_pow 2 (by omega)
  obtain ⟨j, hj⟩ := hdvd
  calc b h (n + L) = b h (G^[k] (n + L)) := (b_G_iter h hdbl htri k _).symm
    _ = b h (G^[k] n + 4 ^ k * L) := by rw [G_iter_add]
    _ = b h (G^[k] n + M * j) := by
        rw [hj, hMeq]
        congr 1
        ring
    _ = b h (G^[k] n) := hev_mul _ hbig _
    _ = b h n := b_G_iter h hdbl htri k n

/-- A period `3K` of `b` yields the period `K`. -/
theorem period_div_three (hdbl : ∀ n, h (2 * n) = h n)
    (htri : ∀ n, Odd n → 1 < n → h (3 * n + 1) = h n) {K : ℕ}
    (hper : ∀ n, b h (n + 3 * K) = b h n) :
    ∀ n, b h (n + K) = b h n := by
  have two : ∀ m, b h (m + 2 * K) = b h m := by
    intro m
    induction m using Nat.strong_induction_on with
    | _ m ih =>
      rcases Nat.even_or_odd m with ⟨t, ht⟩ | ⟨t, ht⟩
      · rcases Nat.even_or_odd t with ⟨n, hn⟩ | ⟨n, hn⟩
        · have hm : m = 4 * n := by omega
          subst hm
          calc b h (4 * n + 2 * K)
              = b h (4 * n + 2 * K + 3 * K * 2) := (add_mul_period h hper _ _).symm
            _ = b h (4 * (n + 2 * K)) := by congr 1; ring
            _ = b h (3 * (n + 2 * K)) := B4 h hdbl htri _
            _ = b h (3 * n + 3 * K * 2) := by congr 1; ring
            _ = b h (3 * n) := add_mul_period h hper _ _
            _ = b h (4 * n) := (B4 h hdbl htri n).symm
        · have hm : m = 4 * n + 2 := by omega
          have hn_lt : n < m := by omega
          have ih_n := ih n hn_lt
          subst hm
          calc b h (4 * n + 2 + 2 * K)
              = b h (4 * n + 2 + 2 * K + 3 * K * 2) := (add_mul_period h hper _ _).symm
            _ = b h (4 * (n + 2 * K) + 2) := by congr 1; ring
            _ = b h (n + 2 * K) := B1 h hdbl htri _
            _ = b h n := ih_n
            _ = b h (4 * n + 2) := (B1 h hdbl htri n).symm
      · subst ht
        calc b h (2 * t + 1 + 2 * K) = b h (2 * (t + K) + 1) := by congr 1; ring
          _ = b h (3 * (t + K) + 2) := (B2 h hdbl htri _).symm
          _ = b h (3 * t + 2 + 3 * K) := by congr 1; ring
          _ = b h (3 * t + 2) := hper _
          _ = b h (2 * t + 1) := B2 h hdbl htri t
  intro n
  calc b h (n + K) = b h (n + K + 2 * K) := (two _).symm
    _ = b h (n + 3 * K) := by congr 1; ring
    _ = b h n := hper n

/-- For a period `L > 1` coprime to 6, consecutive values of `b` agree. -/
theorem succ_eq (hdbl : ∀ n, h (2 * n) = h n)
    (htri : ∀ n, Odd n → 1 < n → h (3 * n + 1) = h n) {L : ℕ} (hL : 1 < L)
    (hLodd : Odd L) (h3 : ¬ 3 ∣ L) (hper : ∀ n, b h (n + L) = b h n) :
    ∀ n, b h (n + 1) = b h n := by
  obtain ⟨c, hc⟩ : ∃ c, 2 * c = L + 1 := by
    obtain ⟨t, ht⟩ := hLodd
    exact ⟨t + 1, by omega⟩
  have h2 : Nat.Coprime 2 L := (Nat.Prime.coprime_iff_not_dvd Nat.prime_two).2 (by
    intro hd
    exact (Nat.not_even_iff_odd.mpr hLodd) (even_iff_two_dvd.mpr hd))
  have hcop4 : Nat.Coprime 4 L := by
    have := Nat.Coprime.mul_left h2 h2
    norm_num at this
    exact this
  have hcop3 : Nat.Coprime 3 L := (Nat.Prime.coprime_iff_not_dvd Nat.prime_three).2 h3
  obtain ⟨z4, -, hz4⟩ := Nat.exists_mul_mod_eq_one_of_coprime hcop4 hL
  obtain ⟨z3, -, hz3⟩ := Nat.exists_mul_mod_eq_one_of_coprime hcop3 hL
  have h4 : 4 * z4 ≡ 1 [MOD L] := by
    unfold Nat.ModEq
    rw [hz4, Nat.mod_eq_of_lt hL]
  have h3' : 3 * z3 ≡ 1 [MOD L] := by
    unfold Nat.ModEq
    rw [hz3, Nat.mod_eq_of_lt hL]
  -- (a) `b (3y+2) = b y`
  have ha : ∀ y, b h (3 * y + 2) = b h y := by
    intro y
    set x := z4 * y with hx
    have hxy : 4 * x ≡ y [MOD L] := by
      have := h4.mul_right y
      rwa [one_mul, show 4 * z4 * y = 4 * x by rw [hx]; ring] at this
    have h12 : 3 * y + 2 ≡ 4 * (3 * x) + 2 [MOD L] := by
      have := (hxy.mul_left 3).add_right 2
      rw [show 3 * (4 * x) + 2 = 4 * (3 * x) + 2 by ring] at this
      exact this.symm
    calc b h (3 * y + 2) = b h (4 * (3 * x) + 2) := eq_of_mod_eq h hper h12
      _ = b h (3 * x) := B1 h hdbl htri _
      _ = b h (4 * x) := (B4 h hdbl htri x).symm
      _ = b h y := eq_of_mod_eq h hper hxy
  -- (b) `b (3 (y + c)) = b y`
  have hb : ∀ y, b h (3 * (y + c)) = b h y := by
    intro y
    calc b h (3 * (y + c)) = b h (4 * (y + c)) := (B4 h hdbl htri _).symm
      _ = b h (4 * y + 2 + L * 2) := by congr 1; omega
      _ = b h (4 * y + 2) := add_mul_period h hper _ _
      _ = b h y := B1 h hdbl htri y
  -- (c) `b (n + c) = b n`
  have hshift : ∀ n, b h (n + c) = b h n := by
    intro n
    have hcle : 3 * c ≤ 3 * L := by omega
    set y := z3 * (n + 3 * L - 3 * c) with hy
    have h3y : 3 * y ≡ n + 3 * L - 3 * c [MOD L] := by
      have := h3'.mul_right (n + 3 * L - 3 * c)
      rwa [one_mul, show 3 * z3 * (n + 3 * L - 3 * c) = 3 * y by rw [hy]; ring] at this
    have e1 : 3 * y + 3 * c ≡ n [MOD L] := by
      have := h3y.add_right (3 * c)
      rw [show n + 3 * L - 3 * c + 3 * c = n + L * 3 by omega] at this
      exact this.trans (Nat.add_mul_mod_self_left n L 3)
    have e2 : 3 * y + 2 ≡ n + c [MOD L] := by
      have := h3y.add_right 2
      rw [show n + 3 * L - 3 * c + 2 = n + c + L * 1 by omega] at this
      exact this.trans (Nat.add_mul_mod_self_left (n + c) L 1)
    symm
    calc b h n = b h (3 * y + 3 * c) := (eq_of_mod_eq h hper e1).symm
      _ = b h (3 * (y + c)) := by congr 1; ring
      _ = b h y := hb y
      _ = b h (3 * y + 2) := (ha y).symm
      _ = b h (n + c) := eq_of_mod_eq h hper e2
  intro n
  calc b h (n + 1) = b h (n + 1 + L) := (hper _).symm
    _ = b h (n + c + c) := by congr 1; omega
    _ = b h (n + c) := hshift _
    _ = b h n := hshift n

/-- A periodic `b` (odd period) is constant. -/
theorem const_of_period (hdbl : ∀ n, h (2 * n) = h n)
    (htri : ∀ n, Odd n → 1 < n → h (3 * n + 1) = h n) :
    ∀ L, Odd L → (∀ n, b h (n + L) = b h n) → ∀ n, b h n = b h 0 := by
  intro L
  induction L using Nat.strong_induction_on with
  | _ L ih =>
    intro hLodd hper
    by_cases h3 : 3 ∣ L
    · obtain ⟨K, hK⟩ := h3
      have hKodd : Odd K := by
        rw [hK] at hLodd
        exact (Nat.odd_mul.mp hLodd).2
      have hKlt : K < L := by
        have := hKodd.pos
        omega
      have hper3 : ∀ n, b h (n + 3 * K) = b h n := fun n => by
        rw [← hK]
        exact hper n
      exact ih K hKlt hKodd (period_div_three h hdbl htri hper3)
    · rcases Nat.lt_or_ge 1 L with hL | hL
      · have hs := succ_eq h hdbl htri hL hLodd h3 hper
        intro n
        induction n with
        | zero => rfl
        | succ k ihk => rw [hs k, ihk]
      · have hL1 : L = 1 := by
          have := hLodd.pos
          omega
        subst hL1
        intro n
        induction n with
        | zero => rfl
        | succ k ihk => rw [hper k, ihk]

/-- **Odd-eventually-periodic rigidity.** If `h (2n) = h n` for all `n`,
`h (3n+1) = h n` for all odd `n > 1`, and `n ↦ h (2n+1)` is eventually periodic
(period `M > 0` from index `N` on), then `h` is constant on the positive integers. -/
theorem odd_eventually_periodic_const (hdbl : ∀ n, h (2 * n) = h n)
    (htri : ∀ n, Odd n → 1 < n → h (3 * n + 1) = h n) {N M : ℕ} (hM : 0 < M)
    (hev : ∀ n, N ≤ n → h (2 * (n + M) + 1) = h (2 * n + 1)) :
    ∀ n, 0 < n → h n = h 1 := by
  have hev' : ∀ n, N ≤ n → b h (n + M) = b h n := hev
  obtain ⟨L, hLodd, hper⟩ := period_of_eventually h hdbl htri hM hev'
  have hconst := const_of_period h hdbl htri L hLodd hper
  intro n hn
  obtain ⟨a, m, hmnot, hmeq⟩ := Nat.exists_eq_pow_mul_and_not_dvd hn.ne' 2 (by norm_num)
  have hmodd : Odd m := Nat.not_even_iff_odd.mp (fun he => hmnot (even_iff_two_dvd.mp he))
  obtain ⟨t, ht⟩ := hmodd
  rw [hmeq, pow_two_mul h hdbl, ht]
  have := hconst t
  simp only [b] at this
  rw [this]

end OddEP
end LeanLane
