import Mathlib

/-!
# Cycle denominators of repeated valuation words (main's C001 `REPETITION_SPECTRUM.md` §§1–2)

Lane: `claude/lean-lane`. Prose source: `experiments/cycle_spectrum/C001/REPETITION_SPECTRUM.md`
on main (the first batch of the cycle-spectrum goal, `docs/CYCLE_SPECTRUM_BRIEF.md`).

Setting. A valuation word is a list `z = [a₀, …, a_{m−1}]` of exponents; its affine
composition is `F_z(x) = (3^m x + C_z)/2^{Σz}` with `F_a(x) = (3x+1)/2^a` applied left to
right, so `C_(a :: z) = 3^|z| + 2^a C_z` and `D_z = 2^{Σz} − 3^{|z|}`. For blocks `u, v` and
`w_k = u^k v`, with `Q = 2^{Σu}`, `P = 3^{|u|}`, `S = 2^{Σv}`, `R = 3^{|v|}`,
`G_k = Σ_{i<k} Q^{k−1−i} P^i` and `K = D_u C_v − D_v C_u`.

Verified in this file (all with the standard axioms; everything is in `ℤ`, so negative
`D` is allowed — the prose's positivity `D_k > 0` is only needed to read `C/D` as a cycle):

* `C_append`, `C_rep`, `G_mul`: concatenation and repetition formulas
  (`C_{uv} = R C_u + Q C_v`, `C_{u^k} = C_u G_k`, `(Q − P) G_k = Q^k − P^k`);
* `C_w`, `D_w`: main's (1), (2);
* `commutator`: main's (3), `D_u C_k − C_u D_k = Q^k K`;
* `gcd_dvd_K`: main's (4), `gcd(C_k, D_k) ∣ K` for every `k` (no coprimality premise);
  `gcd_le_natAbs_K`: hence `gcd(C_k, D_k) ≤ |K|` when `K ≠ 0`, main's (5);
* `gcd_eq_gcd_K`: main's (6), `gcd(C_k, D_k) = gcd(D_k, K)` when `D_u`, `D_v` are coprime;
* `D_odd`, `D_not_three_dvd`: `D_z` is odd and prime to `3` for nonempty positive words;
* the worked examples: `(1,1,3)`, `(2)` with `K = −14`; the `d = 485` word `(3,1,5)` with
  `gcd(C,D) = 1 ≠ 5 = gcd(D,K)` (the counterexample to dropping the coprimality premise);
  and the exact law `7 ∣ D((1,1,3)^k 2) ↔ k ≡ 3 (mod 6)` behind main's spectrum formula
  `den((1,1,3)^k 2) = (4·32^k − 3·27^k)/(7 if k ≡ 3 mod 6 else 1)`.

Not formalised: the periodicity statement (9), the two-sided bound (7), the `K = 0`
characterisation, and the perturbed mechanical family of §3. Nothing here concerns
convergence; Collatz remains open.
-/

namespace LeanLane
namespace Cyc

/-- `C_z`: `C_[] = 0`, `C_(a :: z) = 3^|z| + 2^a C_z`. -/
def C : List ℕ → ℤ
  | [] => 0
  | a :: z => 3 ^ z.length + 2 ^ a * C z

/-- `D_z = 2^{Σz} − 3^{|z|}`. -/
def D (z : List ℕ) : ℤ := 2 ^ z.sum - 3 ^ z.length

/-- `u^k`. -/
def rep (u : List ℕ) : ℕ → List ℕ
  | 0 => []
  | k + 1 => u ++ rep u k

/-- `G_k`, as the recurrence `G_0 = 0`, `G_{k+1} = Q G_k + P^k`. -/
def G (Q P : ℤ) : ℕ → ℤ
  | 0 => 0
  | k + 1 => Q * G Q P k + P ^ k

/-! ### Concatenation and repetition -/

theorem C_append (u v : List ℕ) : C (u ++ v) = 3 ^ v.length * C u + 2 ^ u.sum * C v := by
  induction u with
  | nil => simp [C]
  | cons a u ih =>
    simp only [List.cons_append, C, List.length_append, List.sum_cons, ih]
    ring

theorem rep_length (u : List ℕ) (k : ℕ) : (rep u k).length = k * u.length := by
  induction k with
  | zero => simp [rep]
  | succ k ih =>
    simp only [rep, List.length_append, ih]
    ring

theorem rep_sum (u : List ℕ) (k : ℕ) : (rep u k).sum = k * u.sum := by
  induction k with
  | zero => simp [rep]
  | succ k ih =>
    simp only [rep, List.sum_append, ih]
    ring

theorem G_mul (Q P : ℤ) (k : ℕ) : (Q - P) * G Q P k = Q ^ k - P ^ k := by
  induction k with
  | zero => simp [G]
  | succ k ih =>
    simp only [G]
    linear_combination Q * ih

theorem C_rep (u : List ℕ) (k : ℕ) : C (rep u k) = C u * G (2 ^ u.sum) (3 ^ u.length) k := by
  induction k with
  | zero => simp [rep, C, G]
  | succ k ih =>
    rw [rep, C_append, ih, rep_length, G, pow_mul']
    ring

/-! ### The word `u^k v` -/

section
variable (u v : List ℕ) (k : ℕ)

/-- Main's (1): `C_k = R C_u G_k + Q^k C_v`. -/
theorem C_w : C (rep u k ++ v) =
    3 ^ v.length * (C u * G (2 ^ u.sum) (3 ^ u.length) k) + (2 ^ u.sum) ^ k * C v := by
  rw [C_append, C_rep, rep_sum, pow_mul']

/-- Main's (2): `D_k = S Q^k − R P^k`. -/
theorem D_w : D (rep u k ++ v) =
    2 ^ v.sum * (2 ^ u.sum) ^ k - 3 ^ v.length * (3 ^ u.length) ^ k := by
  rw [D, List.sum_append, List.length_append, rep_sum, rep_length, pow_add, pow_add, pow_mul',
    pow_mul']
  ring

/-- Main's (3): `D_u C_k − C_u D_k = Q^k K`. -/
theorem commutator :
    D u * C (rep u k ++ v) - C u * D (rep u k ++ v)
      = (2 ^ u.sum) ^ k * (D u * C v - D v * C u) := by
  rw [C_w, D_w]
  have hG := G_mul (2 ^ u.sum) (3 ^ u.length) k
  simp only [D] at hG ⊢
  linear_combination (3 ^ v.length * C u) * hG

end

/-! ### Parity and the gcd bound -/

theorem one_le_sum_of_ne_nil {v : List ℕ} (hv0 : v ≠ []) (hv : ∀ a ∈ v, 1 ≤ a) : 1 ≤ v.sum := by
  cases v with
  | nil => exact absurd rfl hv0
  | cons a v =>
    have := hv a (List.mem_cons_self ..)
    simp only [List.sum_cons]
    omega

theorem D_odd {z : List ℕ} (hz : 1 ≤ z.sum) : ¬ (2 : ℤ) ∣ D z := by
  intro h
  have h2 : (2 : ℤ) ∣ 2 ^ z.sum := dvd_pow_self 2 (by omega)
  have h3 : (2 : ℤ) ∣ 3 ^ z.length := (dvd_sub_right h2).mp h
  exact (by decide : ¬ (2 : ℤ) ∣ 3) (Int.prime_two.dvd_of_dvd_pow h3)

theorem D_not_three_dvd {z : List ℕ} (hz : 1 ≤ z.length) : ¬ (3 : ℤ) ∣ D z := by
  intro h
  have h3 : (3 : ℤ) ∣ 3 ^ z.length := dvd_pow_self 3 (by omega)
  have h2 : (3 : ℤ) ∣ 2 ^ z.sum := (dvd_sub_left h3).mp h
  exact (by decide : ¬ (3 : ℤ) ∣ 2) (Int.prime_three.dvd_of_dvd_pow h2)

/-- **Main's (4).** For every `k`, `gcd(C_k, D_k)` divides `K = D_u C_v − D_v C_u`
(no coprimality premise). -/
theorem gcd_dvd_K (u v : List ℕ) (k : ℕ) (hv : ∀ a ∈ v, 1 ≤ a) (hv0 : v ≠ []) :
    ((Int.gcd (C (rep u k ++ v)) (D (rep u k ++ v)) : ℕ) : ℤ) ∣ D u * C v - D v * C u := by
  have hgC : ((Int.gcd (C (rep u k ++ v)) (D (rep u k ++ v)) : ℕ) : ℤ) ∣ C (rep u k ++ v) :=
    Int.gcd_dvd_left _ _
  have hgD : ((Int.gcd (C (rep u k ++ v)) (D (rep u k ++ v)) : ℕ) : ℤ) ∣ D (rep u k ++ v) :=
    Int.gcd_dvd_right _ _
  set g : ℕ := Int.gcd (C (rep u k ++ v)) (D (rep u k ++ v)) with hg
  have hdvd : (g : ℤ) ∣ (2 ^ u.sum) ^ k * (D u * C v - D v * C u) := by
    rw [← commutator]
    exact dvd_sub (dvd_mul_of_dvd_right hgC _) (dvd_mul_of_dvd_right hgD _)
  have hsum : 1 ≤ (rep u k ++ v).sum := by
    rw [List.sum_append]
    have := one_le_sum_of_ne_nil hv0 hv
    omega
  have hodd : ¬ (2 : ℤ) ∣ (g : ℤ) := fun h2 => D_odd hsum (h2.trans hgD)
  have hodd' : ¬ 2 ∣ g := fun h2 => hodd (by exact_mod_cast h2)
  have hcopN : Nat.Coprime g ((2 ^ u.sum) ^ k) :=
    Nat.Coprime.pow_right _ (Nat.Coprime.pow_right _
      ((Nat.Prime.coprime_iff_not_dvd Nat.prime_two).mpr hodd').symm)
  have hcop : IsCoprime (g : ℤ) (((2 : ℤ) ^ u.sum) ^ k) := by
    have := Nat.isCoprime_iff_coprime.mpr hcopN
    exact_mod_cast this
  exact hcop.dvd_of_dvd_mul_left hdvd

/-- **Main's (5).** When `K ≠ 0`, the cancellation is at most `|K|`, uniformly in `k`. -/
theorem gcd_le_natAbs_K (u v : List ℕ) (k : ℕ) (hv : ∀ a ∈ v, 1 ≤ a) (hv0 : v ≠ [])
    (hK : D u * C v - D v * C u ≠ 0) :
    Int.gcd (C (rep u k ++ v)) (D (rep u k ++ v)) ≤ (D u * C v - D v * C u).natAbs :=
  Nat.le_of_dvd (Int.natAbs_pos.mpr hK) (Int.natAbs_dvd_natAbs.mpr (gcd_dvd_K u v k hv hv0))

/-- **Main's (6).** If `D_u` and `D_v` are coprime, `gcd(C_k, D_k) = gcd(D_k, K)`. -/
theorem gcd_eq_gcd_K (u v : List ℕ) (k : ℕ) (hv : ∀ a ∈ v, 1 ≤ a) (hv0 : v ≠ [])
    (hcop : IsCoprime (D u) (D v)) :
    Int.gcd (C (rep u k ++ v)) (D (rep u k ++ v))
      = Int.gcd (D (rep u k ++ v)) (D u * C v - D v * C u) := by
  have hgD : ((Int.gcd (C (rep u k ++ v)) (D (rep u k ++ v)) : ℕ) : ℤ) ∣ D (rep u k ++ v) :=
    Int.gcd_dvd_right _ _
  have hHD : ((Int.gcd (D (rep u k ++ v)) (D u * C v - D v * C u) : ℕ) : ℤ) ∣
      D (rep u k ++ v) := Int.gcd_dvd_left _ _
  have hHK : ((Int.gcd (D (rep u k ++ v)) (D u * C v - D v * C u) : ℕ) : ℤ) ∣
      D u * C v - D v * C u := Int.gcd_dvd_right _ _
  set g : ℕ := Int.gcd (C (rep u k ++ v)) (D (rep u k ++ v)) with hg
  set H : ℕ := Int.gcd (D (rep u k ++ v)) (D u * C v - D v * C u) with hH
  -- `g ∣ H`
  have hgH : g ∣ H := Int.dvd_gcd hgD (gcd_dvd_K u v k hv hv0)
  -- `H` is coprime to `D_u`
  have hlen : 1 ≤ (rep u k ++ v).length := by
    rw [List.length_append]
    have : 1 ≤ v.length := List.length_pos_of_ne_nil hv0
    omega
  have hcopH : IsCoprime (H : ℤ) (D u) := by
    rw [Int.isCoprime_iff_gcd_eq_one]
    have h1 : ((Int.gcd (H : ℤ) (D u) : ℕ) : ℤ) ∣ (H : ℤ) := Int.gcd_dvd_left _ _
    have h2 : ((Int.gcd (H : ℤ) (D u) : ℕ) : ℤ) ∣ D u := Int.gcd_dvd_right _ _
    set h : ℕ := Int.gcd (H : ℤ) (D u) with hh
    have hQP : (3 : ℤ) ^ u.length ≡ 2 ^ u.sum [ZMOD h] := Int.modEq_iff_dvd.mpr h2
    have hDw : D (rep u k ++ v) ≡ D v * (3 ^ u.length) ^ k [ZMOD h] := by
      rw [D_w]
      have e1 := ((hQP.pow k).mul_left ((2 : ℤ) ^ v.sum)).symm
      have e2 := e1.sub_right ((3 : ℤ) ^ v.length * (3 ^ u.length) ^ k)
      calc 2 ^ v.sum * (2 ^ u.sum) ^ k - 3 ^ v.length * (3 ^ u.length) ^ k
          ≡ 2 ^ v.sum * (3 ^ u.length) ^ k - 3 ^ v.length * (3 ^ u.length) ^ k [ZMOD h] := e2
        _ = D v * (3 ^ u.length) ^ k := by simp only [D]; ring
    have hDw' : (h : ℤ) ∣ D (rep u k ++ v) := h1.trans hHD
    have h3 : (h : ℤ) ∣ D v * (3 ^ u.length) ^ k := (dvd_sub_left hDw').mp hDw.dvd
    have hnot3 : ¬ 3 ∣ h := fun h3' =>
      D_not_three_dvd hlen ((by exact_mod_cast h3' : (3 : ℤ) ∣ (h : ℤ)).trans hDw')
    have hcop3N : Nat.Coprime h ((3 ^ u.length) ^ k) :=
      Nat.Coprime.pow_right _ (Nat.Coprime.pow_right _
        ((Nat.Prime.coprime_iff_not_dvd Nat.prime_three).mpr hnot3).symm)
    have hcop3 : IsCoprime (h : ℤ) (((3 : ℤ) ^ u.length) ^ k) := by
      have := Nat.isCoprime_iff_coprime.mpr hcop3N
      exact_mod_cast this
    have hDv : (h : ℤ) ∣ D v := hcop3.dvd_of_dvd_mul_right h3
    have hunit : IsUnit (h : ℤ) := hcop.isUnit_of_dvd' h2 hDv
    rcases Int.isUnit_iff.mp hunit with h1' | h1'
    · exact_mod_cast h1'
    · omega
  -- `H ∣ C_k`, hence `H ∣ g`
  have hHC : (H : ℤ) ∣ C (rep u k ++ v) := by
    have e : D u * C (rep u k ++ v)
        = C u * D (rep u k ++ v) + (2 ^ u.sum) ^ k * (D u * C v - D v * C u) := by
      have := commutator u v k
      linear_combination this
    have hdvd : (H : ℤ) ∣ D u * C (rep u k ++ v) := by
      rw [e]
      exact dvd_add (dvd_mul_of_dvd_right hHD _) (dvd_mul_of_dvd_right hHK _)
    exact hcopH.dvd_of_dvd_mul_left hdvd
  have hHg : H ∣ g := Int.dvd_gcd hHC hHD
  exact Nat.dvd_antisymm hgH hHg

/-! ### Worked examples -/

example : C [1, 1, 3] = 19 ∧ D [1, 1, 3] = 5 := by norm_num [C, D]

example : C [2] = 1 ∧ D [2] = 1 := by norm_num [C, D]

/-- `K = −14` for `u = (1,1,3)`, `v = (2)`. -/
example : D [1, 1, 3] * C [2] - D [2] * C [1, 1, 3] = -14 := by norm_num [C, D]

example : C [3, 1, 5] = 49 ∧ D [3, 1, 5] = 485 := by norm_num [C, D]

/-- The `d = 485` counterexample to dropping `gcd(D_u, D_v) = 1`: for `u = (3)`, `v = (1,5)`
(`K = −30`), `gcd(C_w, D_w) = 1` while `gcd(D_w, K) = 5`. -/
example : Int.gcd (C [3, 1, 5]) (D [3, 1, 5]) = 1 ∧
    Int.gcd (D [3, 1, 5]) (D [3] * C [1, 5] - D [1, 5] * C [3]) = 5 := by
  norm_num [C, D]

theorem D_example (k : ℕ) : D (rep [1, 1, 3] k ++ [2]) = 4 * 32 ^ k - 3 * 27 ^ k := by
  rw [D_w]
  norm_num

/-- The exact residue law behind main's spectrum formula for `(1,1,3)^k (2)`:
`7 ∣ D_k ↔ k ≡ 3 (mod 6)`. -/
theorem seven_dvd_D_example (k : ℕ) :
    (7 : ℤ) ∣ D (rep [1, 1, 3] k ++ [2]) ↔ k % 6 = 3 := by
  rw [D_example]
  have hk : k = 6 * (k / 6) + k % 6 := (Nat.div_add_mod k 6).symm
  have h32 : (32 : ℤ) ^ k ≡ 32 ^ (k % 6) [ZMOD 7] := by
    conv_lhs => rw [hk]
    rw [pow_add, pow_mul]
    have : (32 : ℤ) ^ 6 ≡ 1 [ZMOD 7] := by decide
    calc ((32 : ℤ) ^ 6) ^ (k / 6) * 32 ^ (k % 6)
        ≡ 1 ^ (k / 6) * 32 ^ (k % 6) [ZMOD 7] := (this.pow _).mul_right _
      _ = 32 ^ (k % 6) := by ring
  have h27 : (27 : ℤ) ^ k ≡ 27 ^ (k % 6) [ZMOD 7] := by
    conv_lhs => rw [hk]
    rw [pow_add, pow_mul]
    have : (27 : ℤ) ^ 6 ≡ 1 [ZMOD 7] := by decide
    calc ((27 : ℤ) ^ 6) ^ (k / 6) * 27 ^ (k % 6)
        ≡ 1 ^ (k / 6) * 27 ^ (k % 6) [ZMOD 7] := (this.pow _).mul_right _
      _ = 27 ^ (k % 6) := by ring
  have hmod : 4 * (32 : ℤ) ^ k - 3 * 27 ^ k ≡ 4 * 32 ^ (k % 6) - 3 * 27 ^ (k % 6) [ZMOD 7] :=
    (h32.mul_left 4).sub (h27.mul_left 3)
  rw [Int.dvd_iff_emod_eq_zero, hmod]
  have hr : k % 6 < 6 := Nat.mod_lt _ (by norm_num)
  generalize k % 6 = r at hr ⊢
  interval_cases r <;> decide

/-- Main's (6) applies to this example (`gcd(D_u, D_v) = gcd(5, 1) = 1`):
`gcd(C_k, D_k) = gcd(D_k, −14)` for every `k`. -/
theorem gcd_example (k : ℕ) :
    Int.gcd (C (rep [1, 1, 3] k ++ [2])) (D (rep [1, 1, 3] k ++ [2]))
      = Int.gcd (D (rep [1, 1, 3] k ++ [2])) (-14) := by
  have h := gcd_eq_gcd_K [1, 1, 3] [2] k (by decide) (by decide)
    (by norm_num [D, Int.isCoprime_iff_gcd_eq_one])
  rwa [show D [1, 1, 3] * C [2] - D [2] * C [1, 1, 3] = -14 by norm_num [C, D]] at h

end Cyc
end LeanLane
