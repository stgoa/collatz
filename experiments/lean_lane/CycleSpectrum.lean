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

/-! ### Main's (7): the two-sided bound without a coprimality premise -/

/-- The cancellation factor is coprime to `6`. -/
theorem gcd_coprime_six (u v : List ℕ) (k : ℕ) (hv : ∀ a ∈ v, 1 ≤ a) (hv0 : v ≠ []) :
    Nat.Coprime (Int.gcd (C (rep u k ++ v)) (D (rep u k ++ v))) 6 := by
  have hgD : ((Int.gcd (C (rep u k ++ v)) (D (rep u k ++ v)) : ℕ) : ℤ) ∣ D (rep u k ++ v) :=
    Int.gcd_dvd_right _ _
  set g : ℕ := Int.gcd (C (rep u k ++ v)) (D (rep u k ++ v)) with hg
  have hsum : 1 ≤ (rep u k ++ v).sum := by
    rw [List.sum_append]
    have := one_le_sum_of_ne_nil hv0 hv
    omega
  have hlen : 1 ≤ (rep u k ++ v).length := by
    rw [List.length_append]
    have : 1 ≤ v.length := List.length_pos_of_ne_nil hv0
    omega
  have h2 : ¬ 2 ∣ g := fun h =>
    D_odd hsum ((by exact_mod_cast h : (2 : ℤ) ∣ (g : ℤ)).trans hgD)
  have h3 : ¬ 3 ∣ g := fun h =>
    D_not_three_dvd hlen ((by exact_mod_cast h : (3 : ℤ) ∣ (g : ℤ)).trans hgD)
  show Nat.Coprime g (2 * 3)
  exact Nat.Coprime.mul_right ((Nat.Prime.coprime_iff_not_dvd Nat.prime_two).mpr h2).symm
    ((Nat.Prime.coprime_iff_not_dvd Nat.prime_three).mpr h3).symm

/-- **Main's (7).** With `H = gcd(D_k, K)` and `e = gcd(H, |D_u|)`:
`H/e ∣ gcd(C_k, D_k) ∣ H`, with no coprimality premise. -/
theorem gcd_two_sided (u v : List ℕ) (k : ℕ) (hv : ∀ a ∈ v, 1 ≤ a) (hv0 : v ≠ []) :
    Int.gcd (D (rep u k ++ v)) (D u * C v - D v * C u)
        / Nat.gcd (Int.gcd (D (rep u k ++ v)) (D u * C v - D v * C u)) (D u).natAbs
      ∣ Int.gcd (C (rep u k ++ v)) (D (rep u k ++ v)) ∧
    Int.gcd (C (rep u k ++ v)) (D (rep u k ++ v))
      ∣ Int.gcd (D (rep u k ++ v)) (D u * C v - D v * C u) := by
  have hHD : ((Int.gcd (D (rep u k ++ v)) (D u * C v - D v * C u) : ℕ) : ℤ) ∣
      D (rep u k ++ v) := Int.gcd_dvd_left _ _
  have hHK : ((Int.gcd (D (rep u k ++ v)) (D u * C v - D v * C u) : ℕ) : ℤ) ∣
      D u * C v - D v * C u := Int.gcd_dvd_right _ _
  set H : ℕ := Int.gcd (D (rep u k ++ v)) (D u * C v - D v * C u) with hH
  refine ⟨?_, Int.dvd_gcd (Int.gcd_dvd_right _ _) (gcd_dvd_K u v k hv hv0)⟩
  have hdvd : (H : ℤ) ∣ D u * C (rep u k ++ v) := by
    have e : D u * C (rep u k ++ v)
        = C u * D (rep u k ++ v) + (2 ^ u.sum) ^ k * (D u * C v - D v * C u) := by
      have := commutator u v k
      linear_combination this
    rw [e]
    exact dvd_add (dvd_mul_of_dvd_right hHD _) (dvd_mul_of_dvd_right hHK _)
  have hdvdN : H ∣ (D u).natAbs * (C (rep u k ++ v)).natAbs := by
    rw [← Int.natAbs_mul]
    exact Int.natCast_dvd.mp hdvd
  set e : ℕ := Nat.gcd H (D u).natAbs with he
  have hsum : 1 ≤ (rep u k ++ v).sum := by
    rw [List.sum_append]
    have := one_le_sum_of_ne_nil hv0 hv
    omega
  have hDw0 : D (rep u k ++ v) ≠ 0 := fun h0 => D_odd hsum (h0 ▸ dvd_zero 2)
  have hH0 : 0 < H := Int.gcd_pos_of_ne_zero_left _ hDw0
  have he0 : 0 < e := Nat.gcd_pos_of_pos_left _ hH0
  have heH : e ∣ H := Nat.gcd_dvd_left _ _
  have heD : e ∣ (D u).natAbs := Nat.gcd_dvd_right _ _
  have hcop : Nat.Coprime (H / e) ((D u).natAbs / e) := Nat.coprime_div_gcd_div_gcd he0
  have hdiv : H / e ∣ (D u).natAbs / e * (C (rep u k ++ v)).natAbs := by
    apply Nat.dvd_of_mul_dvd_mul_left he0
    rw [Nat.mul_div_cancel' heH, ← mul_assoc, Nat.mul_div_cancel' heD]
    exact hdvdN
  have h1 : H / e ∣ (C (rep u k ++ v)).natAbs := hcop.dvd_of_dvd_mul_left hdiv
  have h2 : H / e ∣ (D (rep u k ++ v)).natAbs :=
    (Nat.div_dvd_of_dvd heH).trans (Int.natCast_dvd.mp hHD)
  exact Nat.dvd_gcd h1 h2

/-! ### Main's (9): the cancellation factor is periodic in `k` -/

/-- Cancelling a nonzero factor `a` presented through `|a|`. -/
theorem dvd_of_mul_natAbs_dvd {n : ℕ} {a X : ℤ} (ha : a ≠ 0)
    (h : ((n * a.natAbs : ℕ) : ℤ) ∣ a * X) : (n : ℤ) ∣ X := by
  have h' : n * a.natAbs ∣ a.natAbs * X.natAbs := by
    rw [← Int.natAbs_mul]
    exact Int.natCast_dvd.mp h
  rw [mul_comm] at h'
  exact Int.natCast_dvd.mpr (Nat.dvd_of_mul_dvd_mul_left (Int.natAbs_pos.mpr ha) h')

/-- **Main's (9).** Write `|K| = 2^a 3^b K₀`. If `Q^T ≡ P^T ≡ 1 (mod K₀|D_u|)`, then the
cancellation factor has period `T`: `gcd(C_{k+T}, D_{k+T}) = gcd(C_k, D_k)` for every `k`. -/
theorem gcd_periodic (u v : List ℕ) (hu : ∀ a ∈ u, 1 ≤ a) (hu0 : u ≠ [])
    (hv : ∀ a ∈ v, 1 ≤ a) (hv0 : v ≠ []) (a b K₀ : ℕ)
    (hK : (D u * C v - D v * C u).natAbs = 2 ^ a * 3 ^ b * K₀) (T : ℕ)
    (hQ : (2 ^ u.sum) ^ T ≡ 1 [MOD K₀ * (D u).natAbs])
    (hP : (3 ^ u.length) ^ T ≡ 1 [MOD K₀ * (D u).natAbs]) (k : ℕ) :
    Int.gcd (C (rep u (k + T) ++ v)) (D (rep u (k + T) ++ v))
      = Int.gcd (C (rep u k ++ v)) (D (rep u k ++ v)) := by
  have hDu : D u ≠ 0 := fun h0 => D_odd (one_le_sum_of_ne_nil hu0 hu) (h0 ▸ dvd_zero 2)
  -- the two congruences, in `ℤ`
  have hQZ : ((K₀ * (D u).natAbs : ℕ) : ℤ) ∣ ((2 : ℤ) ^ u.sum) ^ T - 1 := by
    have := hQ.symm.dvd
    exact_mod_cast this
  have hPZ : ((K₀ * (D u).natAbs : ℕ) : ℤ) ∣ ((3 : ℤ) ^ u.length) ^ T - 1 := by
    have := hP.symm.dvd
    exact_mod_cast this
  have hK₀L : (K₀ : ℤ) ∣ ((K₀ * (D u).natAbs : ℕ) : ℤ) := by
    push_cast
    exact dvd_mul_right _ _
  have hK₀Q : (K₀ : ℤ) ∣ ((2 : ℤ) ^ u.sum) ^ T - 1 := hK₀L.trans hQZ
  have hK₀P : (K₀ : ℤ) ∣ ((3 : ℤ) ^ u.length) ^ T - 1 := hK₀L.trans hPZ
  -- `K₀ ∣ G_{k+T} − G_k`
  have hGdiff : D u * (G (2 ^ u.sum) (3 ^ u.length) (k + T) - G (2 ^ u.sum) (3 ^ u.length) k)
      = (2 ^ u.sum) ^ k * (((2 : ℤ) ^ u.sum) ^ T - 1)
        - (3 ^ u.length) ^ k * (((3 : ℤ) ^ u.length) ^ T - 1) := by
    have h1 := G_mul (2 ^ u.sum) (3 ^ u.length) (k + T)
    have h2 := G_mul (2 ^ u.sum) (3 ^ u.length) k
    simp only [D]
    linear_combination h1 - h2
  have hK₀G : (K₀ : ℤ) ∣ G (2 ^ u.sum) (3 ^ u.length) (k + T) - G (2 ^ u.sum) (3 ^ u.length) k := by
    apply dvd_of_mul_natAbs_dvd hDu
    rw [hGdiff]
    exact dvd_sub (dvd_mul_of_dvd_right hQZ _) (dvd_mul_of_dvd_right hPZ _)
  -- `C` and `D` are periodic modulo `K₀`
  have hC : (K₀ : ℤ) ∣ C (rep u (k + T) ++ v) - C (rep u k ++ v) := by
    rw [C_w, C_w]
    have e : (3 ^ v.length * (C u * G (2 ^ u.sum) (3 ^ u.length) (k + T))
          + (2 ^ u.sum) ^ (k + T) * C v)
        - (3 ^ v.length * (C u * G (2 ^ u.sum) (3 ^ u.length) k) + (2 ^ u.sum) ^ k * C v)
        = 3 ^ v.length * C u
            * (G (2 ^ u.sum) (3 ^ u.length) (k + T) - G (2 ^ u.sum) (3 ^ u.length) k)
          + (2 ^ u.sum) ^ k * (((2 : ℤ) ^ u.sum) ^ T - 1) * C v := by ring
    rw [e]
    exact dvd_add (dvd_mul_of_dvd_right hK₀G _)
      (dvd_mul_of_dvd_left (dvd_mul_of_dvd_right hK₀Q _) _)
  have hD : (K₀ : ℤ) ∣ D (rep u (k + T) ++ v) - D (rep u k ++ v) := by
    rw [D_w, D_w]
    have e : (2 ^ v.sum * (2 ^ u.sum) ^ (k + T) - 3 ^ v.length * (3 ^ u.length) ^ (k + T))
        - (2 ^ v.sum * (2 ^ u.sum) ^ k - 3 ^ v.length * (3 ^ u.length) ^ k)
        = 2 ^ v.sum * (2 ^ u.sum) ^ k * (((2 : ℤ) ^ u.sum) ^ T - 1)
          - 3 ^ v.length * (3 ^ u.length) ^ k * (((3 : ℤ) ^ u.length) ^ T - 1) := by ring
    rw [e]
    exact dvd_sub (dvd_mul_of_dvd_right hK₀Q _) (dvd_mul_of_dvd_right hK₀P _)
  -- both cancellation factors divide `K₀`
  have hg_dvd : ∀ j, Int.gcd (C (rep u j ++ v)) (D (rep u j ++ v)) ∣ K₀ := by
    intro j
    have h1 : Int.gcd (C (rep u j ++ v)) (D (rep u j ++ v)) ∣ 2 ^ a * 3 ^ b * K₀ := by
      rw [← hK]
      exact Int.natCast_dvd.mp (gcd_dvd_K u v j hv hv0)
    have h6 := gcd_coprime_six u v j hv hv0
    have hcop : Nat.Coprime (Int.gcd (C (rep u j ++ v)) (D (rep u j ++ v))) (2 ^ a * 3 ^ b) :=
      Nat.Coprime.mul_right (Nat.Coprime.pow_right _ (h6.coprime_dvd_right (by norm_num)))
        (Nat.Coprime.pow_right _ (h6.coprime_dvd_right (by norm_num)))
    exact hcop.dvd_of_dvd_mul_left h1
  have hgT := hg_dvd (k + T)
  have hgk := hg_dvd k
  apply Nat.dvd_antisymm
  · apply Int.dvd_gcd
    · have h1 : ((Int.gcd (C (rep u (k + T) ++ v)) (D (rep u (k + T) ++ v)) : ℕ) : ℤ) ∣
          C (rep u (k + T) ++ v) := Int.gcd_dvd_left _ _
      have h2 := (Int.natCast_dvd_natCast.mpr hgT).trans hC
      exact (dvd_sub_right h1).mp h2
    · have h1 : ((Int.gcd (C (rep u (k + T) ++ v)) (D (rep u (k + T) ++ v)) : ℕ) : ℤ) ∣
          D (rep u (k + T) ++ v) := Int.gcd_dvd_right _ _
      have h2 := (Int.natCast_dvd_natCast.mpr hgT).trans hD
      exact (dvd_sub_right h1).mp h2
  · apply Int.dvd_gcd
    · have h1 : ((Int.gcd (C (rep u k ++ v)) (D (rep u k ++ v)) : ℕ) : ℤ) ∣
          C (rep u k ++ v) := Int.gcd_dvd_left _ _
      have h2 := (Int.natCast_dvd_natCast.mpr hgk).trans hC
      exact (dvd_sub_left h1).mp h2
    · have h1 : ((Int.gcd (C (rep u k ++ v)) (D (rep u k ++ v)) : ℕ) : ℤ) ∣
          D (rep u k ++ v) := Int.gcd_dvd_right _ _
      have h2 := (Int.natCast_dvd_natCast.mpr hgk).trans hD
      exact (dvd_sub_left h1).mp h2

/-- **Main's (9) with the explicit period `φ(K₀|D_u|)`**, for `K₀` coprime to `6`. -/
theorem gcd_periodic_totient (u v : List ℕ) (hu : ∀ a ∈ u, 1 ≤ a) (hu0 : u ≠ [])
    (hv : ∀ a ∈ v, 1 ≤ a) (hv0 : v ≠ []) (a b K₀ : ℕ)
    (hK : (D u * C v - D v * C u).natAbs = 2 ^ a * 3 ^ b * K₀) (hK₀ : Nat.Coprime K₀ 6)
    (k : ℕ) :
    Int.gcd (C (rep u (k + Nat.totient (K₀ * (D u).natAbs)) ++ v))
        (D (rep u (k + Nat.totient (K₀ * (D u).natAbs)) ++ v))
      = Int.gcd (C (rep u k ++ v)) (D (rep u k ++ v)) := by
  have hodd := D_odd (one_le_sum_of_ne_nil hu0 hu)
  have hnot3 := D_not_three_dvd (List.length_pos_of_ne_nil hu0)
  have h2 : ¬ 2 ∣ (D u).natAbs := fun h => hodd (by exact_mod_cast Int.natCast_dvd.mpr h)
  have h3 : ¬ 3 ∣ (D u).natAbs := fun h => hnot3 (by exact_mod_cast Int.natCast_dvd.mpr h)
  apply gcd_periodic u v hu hu0 hv hv0 a b K₀ hK
  · apply Nat.ModEq.pow_totient
    apply Nat.Coprime.pow_left
    exact Nat.Coprime.mul_right (hK₀.coprime_dvd_right (by norm_num)).symm
      ((Nat.Prime.coprime_iff_not_dvd Nat.prime_two).mpr h2)
  · apply Nat.ModEq.pow_totient
    apply Nat.Coprime.pow_left
    exact Nat.Coprime.mul_right (hK₀.coprime_dvd_right (by norm_num)).symm
      ((Nat.Prime.coprime_iff_not_dvd Nat.prime_three).mpr h3)

/-! ### Two growing blocks `u^k v^ℓ` (main's C002 `PROPORTIONAL.md` §§1–2) -/

/-- The cancellation factor of any word with positive sum and length is coprime to `6`. -/
theorem gcd_coprime_six' (w : List ℕ) (hsum : 1 ≤ w.sum) (hlen : 1 ≤ w.length) :
    Nat.Coprime (Int.gcd (C w) (D w)) 6 := by
  have hgD : ((Int.gcd (C w) (D w) : ℕ) : ℤ) ∣ D w := Int.gcd_dvd_right _ _
  have h2 : ¬ 2 ∣ Int.gcd (C w) (D w) := fun h =>
    D_odd hsum ((by exact_mod_cast h : (2 : ℤ) ∣ ((Int.gcd (C w) (D w) : ℕ) : ℤ)).trans hgD)
  have h3 : ¬ 3 ∣ Int.gcd (C w) (D w) := fun h =>
    D_not_three_dvd hlen
      ((by exact_mod_cast h : (3 : ℤ) ∣ ((Int.gcd (C w) (D w) : ℕ) : ℤ)).trans hgD)
  show Nat.Coprime _ (2 * 3)
  exact Nat.Coprime.mul_right ((Nat.Prime.coprime_iff_not_dvd Nat.prime_two).mpr h2).symm
    ((Nat.Prime.coprime_iff_not_dvd Nat.prime_three).mpr h3).symm

section TwoBlocks
variable (u v : List ℕ) (k l : ℕ)

/-- C002's (1). -/
theorem C_two : C (rep u k ++ rep v l) =
    (3 ^ v.length) ^ l * (C u * G (2 ^ u.sum) (3 ^ u.length) k)
      + (2 ^ u.sum) ^ k * (C v * G (2 ^ v.sum) (3 ^ v.length) l) := by
  rw [C_append, C_rep, C_rep, rep_length, rep_sum, pow_mul', pow_mul']

/-- C002's (2). -/
theorem D_two : D (rep u k ++ rep v l) =
    (2 ^ v.sum) ^ l * (2 ^ u.sum) ^ k - (3 ^ v.length) ^ l * (3 ^ u.length) ^ k := by
  rw [D, List.sum_append, List.length_append, rep_sum, rep_sum, rep_length, rep_length,
    pow_add, pow_add, pow_mul', pow_mul', pow_mul', pow_mul']
  ring

/-- C002's (3): `D_u C − C_u D = Q^k G_v(ℓ) K`. -/
theorem commutator_two_u :
    D u * C (rep u k ++ rep v l) - C u * D (rep u k ++ rep v l)
      = (2 ^ u.sum) ^ k * G (2 ^ v.sum) (3 ^ v.length) l * (D u * C v - D v * C u) := by
  rw [C_two, D_two]
  have h1 := G_mul (2 ^ u.sum) (3 ^ u.length) k
  have h2 := G_mul (2 ^ v.sum) (3 ^ v.length) l
  simp only [D] at h1 h2 ⊢
  linear_combination ((3 ^ v.length) ^ l * C u) * h1 + ((2 ^ u.sum) ^ k * C u) * h2

/-- C002's (4): `D_v C − C_v D = −R^ℓ G_u(k) K`. -/
theorem commutator_two_v :
    D v * C (rep u k ++ rep v l) - C v * D (rep u k ++ rep v l)
      = -((3 ^ v.length) ^ l * G (2 ^ u.sum) (3 ^ u.length) k * (D u * C v - D v * C u)) := by
  rw [C_two, D_two]
  have h1 := G_mul (2 ^ u.sum) (3 ^ u.length) k
  have h2 := G_mul (2 ^ v.sum) (3 ^ v.length) l
  simp only [D] at h1 h2 ⊢
  linear_combination ((2 ^ u.sum) ^ k * C v) * h2 + ((3 ^ v.length) ^ l * C v) * h1

end TwoBlocks

/-- **C002's (5).** `gcd(C, D) ∣ |K| · gcd(G_u(k), G_v(ℓ))`, with no coprimality premise on
the blocks (both blocks nonempty and positive, `k, ℓ ≥ 1`). -/
theorem gcd_dvd_K_mul_gcd (u v : List ℕ) (k l : ℕ) (_hu : ∀ a ∈ u, 1 ≤ a) (_hu0 : u ≠ [])
    (hv : ∀ a ∈ v, 1 ≤ a) (hv0 : v ≠ []) (_hk : 1 ≤ k) (hl : 1 ≤ l) :
    Int.gcd (C (rep u k ++ rep v l)) (D (rep u k ++ rep v l))
      ∣ (D u * C v - D v * C u).natAbs
          * Int.gcd (G (2 ^ u.sum) (3 ^ u.length) k) (G (2 ^ v.sum) (3 ^ v.length) l) := by
  have hgC : ((Int.gcd (C (rep u k ++ rep v l)) (D (rep u k ++ rep v l)) : ℕ) : ℤ) ∣
      C (rep u k ++ rep v l) := Int.gcd_dvd_left _ _
  have hgD : ((Int.gcd (C (rep u k ++ rep v l)) (D (rep u k ++ rep v l)) : ℕ) : ℤ) ∣
      D (rep u k ++ rep v l) := Int.gcd_dvd_right _ _
  set g : ℕ := Int.gcd (C (rep u k ++ rep v l)) (D (rep u k ++ rep v l)) with hg
  have hsum : 1 ≤ (rep u k ++ rep v l).sum := by
    rw [List.sum_append, rep_sum, rep_sum]
    have := Nat.mul_le_mul hl (one_le_sum_of_ne_nil hv0 hv)
    omega
  have hlen : 1 ≤ (rep u k ++ rep v l).length := by
    rw [List.length_append, rep_length, rep_length]
    have := Nat.mul_le_mul hl (List.length_pos_of_ne_nil hv0)
    omega
  have h6 := gcd_coprime_six' _ hsum hlen
  have hcopQ : IsCoprime (g : ℤ) (((2 : ℤ) ^ u.sum) ^ k) := by
    have := Nat.isCoprime_iff_coprime.mpr
      (Nat.Coprime.pow_right k (Nat.Coprime.pow_right u.sum
        (h6.coprime_dvd_right (by norm_num : 2 ∣ 6))))
    exact_mod_cast this
  have hcopR : IsCoprime (g : ℤ) (((3 : ℤ) ^ v.length) ^ l) := by
    have := Nat.isCoprime_iff_coprime.mpr
      (Nat.Coprime.pow_right l (Nat.Coprime.pow_right v.length
        (h6.coprime_dvd_right (by norm_num : 3 ∣ 6))))
    exact_mod_cast this
  -- `g ∣ K G_v` and `g ∣ K G_u`
  have h1 : (g : ℤ) ∣ (2 ^ u.sum) ^ k * (G (2 ^ v.sum) (3 ^ v.length) l * (D u * C v - D v * C u)) := by
    rw [← mul_assoc, ← commutator_two_u]
    exact dvd_sub (dvd_mul_of_dvd_right hgC _) (dvd_mul_of_dvd_right hgD _)
  have h2 : (g : ℤ) ∣ (3 ^ v.length) ^ l * (G (2 ^ u.sum) (3 ^ u.length) k * (D u * C v - D v * C u)) := by
    have := dvd_sub (dvd_mul_of_dvd_right hgC (D v)) (dvd_mul_of_dvd_right hgD (C v))
    rw [commutator_two_v, dvd_neg, mul_assoc] at this
    exact this
  have h1' : (g : ℤ) ∣ (D u * C v - D v * C u) * G (2 ^ v.sum) (3 ^ v.length) l := by
    rw [mul_comm]; exact hcopQ.dvd_of_dvd_mul_left h1
  have h2' : (g : ℤ) ∣ (D u * C v - D v * C u) * G (2 ^ u.sum) (3 ^ u.length) k := by
    rw [mul_comm]; exact hcopR.dvd_of_dvd_mul_left h2
  have := Int.dvd_gcd h2' h1'
  rwa [Int.gcd_mul_left] at this

/-! ### Strong divisibility of `U^i − V^i` -/

/-- For coprime `U, V`, `gcd(U^i − V^i, U^j − V^j) = |U^gcd(i,j) − V^gcd(i,j)|`. -/
theorem gcd_pow_sub_pow (U V : ℤ) (hUV : IsCoprime U V) (i j : ℕ) :
    Int.gcd (U ^ i - V ^ i) (U ^ j - V ^ j)
      = (U ^ Nat.gcd i j - V ^ Nat.gcd i j).natAbs := by
  induction i, j using Nat.gcd.induction with
  | H0 j => simp
  | H1 i j hi ih =>
    rw [Nat.gcd_rec, ← ih]
    have hj : j = i * (j / i) + j % i := (Nat.div_add_mod j i).symm
    have hsplit : U ^ j - V ^ j
        = U ^ (i * (j / i)) * (U ^ (j % i) - V ^ (j % i))
          + V ^ (j % i) * ((U ^ i) ^ (j / i) - (V ^ i) ^ (j / i)) := by
      conv_lhs => rw [hj]
      ring
    have hdvd : U ^ i - V ^ i ∣ (U ^ i) ^ (j / i) - (V ^ i) ^ (j / i) := sub_dvd_pow_sub_pow _ _ _
    have hcopU : IsCoprime U (U ^ i - V ^ i) := by
      have h1 : IsCoprime U (-(V ^ i)) := (hUV.pow_right (n := i)).neg_right
      have h2 := h1.add_mul_left_right (U ^ (i - 1))
      have e : U * U ^ (i - 1) = U ^ i := by rw [← pow_succ', Nat.sub_add_cancel hi]
      rwa [e, show -(V ^ i) + U ^ i = U ^ i - V ^ i by ring] at h2
    have hcop : IsCoprime (U ^ (i * (j / i))) (U ^ i - V ^ i) := hcopU.pow_left
    apply Nat.dvd_antisymm
    · apply Int.dvd_gcd
      · have hA : ((Int.gcd (U ^ i - V ^ i) (U ^ j - V ^ j) : ℕ) : ℤ) ∣
            U ^ (i * (j / i)) * (U ^ (j % i) - V ^ (j % i))
              + V ^ (j % i) * ((U ^ i) ^ (j / i) - (V ^ i) ^ (j / i)) := by
          rw [← hsplit]
          exact Int.gcd_dvd_right _ _
        have hB : ((Int.gcd (U ^ i - V ^ i) (U ^ j - V ^ j) : ℕ) : ℤ) ∣
            V ^ (j % i) * ((U ^ i) ^ (j / i) - (V ^ i) ^ (j / i)) :=
          dvd_mul_of_dvd_right ((Int.gcd_dvd_left _ _).trans hdvd) _
        have hC := (dvd_add_left hB).mp hA
        have hcop' : IsCoprime ((Int.gcd (U ^ i - V ^ i) (U ^ j - V ^ j) : ℕ) : ℤ)
            (U ^ (i * (j / i))) :=
          (hcop.of_isCoprime_of_dvd_right (Int.gcd_dvd_left _ _)).symm
        exact hcop'.dvd_of_dvd_mul_left hC
      · exact Int.gcd_dvd_left _ _
    · apply Int.dvd_gcd
      · exact Int.gcd_dvd_right _ _
      · rw [hsplit]
        exact dvd_add (dvd_mul_of_dvd_right (Int.gcd_dvd_left _ _) _)
          (dvd_mul_of_dvd_right ((Int.gcd_dvd_right _ _).trans hdvd) _)

/-! ### Intercepts of equal-total words: positivity, parity, injectivity, the bound (U2) -/

theorem C_nonneg : ∀ z : List ℕ, 0 ≤ C z
  | [] => le_rfl
  | a :: z => by
    simp only [C]
    exact add_nonneg (by positivity) (mul_nonneg (by positivity) (C_nonneg z))

theorem C_pos {z : List ℕ} (hz : z ≠ []) : 0 < C z := by
  cases z with
  | nil => exact absurd rfl hz
  | cons a z =>
    simp only [C]
    have := C_nonneg z
    positivity

theorem C_odd {z : List ℕ} (hz : z ≠ []) (hpos : ∀ a ∈ z, 1 ≤ a) : Odd (C z) := by
  cases z with
  | nil => exact absurd rfl hz
  | cons a z =>
    simp only [C]
    have ha : 1 ≤ a := hpos a (List.mem_cons_self ..)
    exact Odd.add_even (Odd.pow ⟨1, by norm_num⟩)
      ((even_two.pow_of_ne_zero (by omega)).mul_right _)

theorem length_le_sum : ∀ z : List ℕ, (∀ a ∈ z, 1 ≤ a) → z.length ≤ z.sum
  | [], _ => le_rfl
  | a :: z, hpos => by
    have ha : 1 ≤ a := hpos a (List.mem_cons_self ..)
    have := length_le_sum z (fun x hx => hpos x (List.mem_cons_of_mem _ hx))
    simp only [List.length_cons, List.sum_cons]
    omega

/-- Distinct positive words of equal length and equal total have distinct intercepts
(`v₂(C − 3^{m−1}) = a₀` recovers the first letter; the last letter is fixed by the total). -/
theorem C_injective : ∀ (u v : List ℕ), (∀ a ∈ u, 1 ≤ a) → (∀ a ∈ v, 1 ≤ a) →
    u.length = v.length → u.sum = v.sum → C u = C v → u = v
  | [], v, _, _, hl, _, _ => (List.length_eq_zero_iff.mp hl.symm).symm
  | a :: u, [], _, _, hl, _, _ => absurd hl (by simp)
  | a :: u, b :: v, hu, hv, hl, hs, hC => by
    have hu' : ∀ x ∈ u, 1 ≤ x := fun x hx => hu x (List.mem_cons_of_mem _ hx)
    have hv' : ∀ x ∈ v, 1 ≤ x := fun x hx => hv x (List.mem_cons_of_mem _ hx)
    simp only [List.length_cons, List.sum_cons] at hl hs
    have hlen : u.length = v.length := by omega
    simp only [C] at hC
    rw [← hlen] at hC
    have hC' : (2 : ℤ) ^ a * C u = 2 ^ b * C v := add_left_cancel hC
    rcases eq_or_ne u [] with rfl | hu0
    · have hv0 : v = [] := List.length_eq_zero_iff.mp hlen.symm
      subst hv0
      simp only [List.sum_nil, add_zero] at hs
      rw [hs]
    · have hv0 : v ≠ [] := fun h => hu0 (List.length_eq_zero_iff.mp (hlen.trans (by simp [h])))
      have hou := C_odd hu0 hu'
      have hov := C_odd hv0 hv'
      have hab : a = b := by
        by_contra hne
        rcases Nat.lt_or_gt_of_ne hne with hlt | hgt
        · have e : (2 : ℤ) ^ b = 2 ^ a * 2 ^ (b - a) := by
            rw [← pow_add, Nat.add_sub_cancel' hlt.le]
          rw [e, mul_assoc] at hC'
          have h := mul_left_cancel₀ (by positivity : (2 : ℤ) ^ a ≠ 0) hC'
          have heven : Even (C u) := by
            rw [h]
            exact (even_two.pow_of_ne_zero (by omega)).mul_right _
          exact (Int.not_even_iff_odd.mpr hou) heven
        · have e : (2 : ℤ) ^ a = 2 ^ b * 2 ^ (a - b) := by
            rw [← pow_add, Nat.add_sub_cancel' hgt.le]
          rw [e, mul_assoc] at hC'
          have h := mul_left_cancel₀ (by positivity : (2 : ℤ) ^ b ≠ 0) hC'.symm
          have heven : Even (C v) := by
            rw [h]
            exact (even_two.pow_of_ne_zero (by omega)).mul_right _
          exact (Int.not_even_iff_odd.mpr hov) heven
      subst hab
      have hCuv : C u = C v := mul_left_cancel₀ (by positivity : (2 : ℤ) ^ a ≠ 0) hC'
      have := C_injective u v hu' hv' hlen (by omega) hCuv
      rw [this]

/-- **C002's (U2).** For a positive word of length `m` and total `A`,
`2^m C_z ≤ 2^A (3^m − 2^m)`. -/
theorem two_pow_mul_C_le : ∀ z : List ℕ, (∀ a ∈ z, 1 ≤ a) →
    (2 : ℤ) ^ z.length * C z ≤ 2 ^ z.sum * (3 ^ z.length - 2 ^ z.length)
  | [], _ => by simp [C]
  | a :: z, hpos => by
    have hpos' : ∀ x ∈ z, 1 ≤ x := fun x hx => hpos x (List.mem_cons_of_mem _ hx)
    have ih := two_pow_mul_C_le z hpos'
    have ha : 1 ≤ a := hpos a (List.mem_cons_self ..)
    have hlen : z.length ≤ z.sum := length_le_sum z hpos'
    simp only [C, List.length_cons, List.sum_cons]
    have h2 : (2 : ℤ) ^ (z.length + 1) ≤ 2 ^ (a + z.sum) :=
      pow_le_pow_right₀ (by norm_num) (by omega)
    have h3 : (0 : ℤ) < 3 ^ z.length := by positivity
    have hT : (0 : ℤ) ≤ 2 ^ a := by positivity
    have p1 := mul_le_mul_of_nonneg_left ih (by positivity : (0 : ℤ) ≤ 2 * 2 ^ a)
    have p2 := mul_le_mul_of_nonneg_left h2 h3.le
    simp only [pow_succ, pow_add] at h2 p2 ⊢
    nlinarith [p1, p2]

/-! ### C002's uniform equal-total exclusion (U1) -/

/-- The Euclid step `U^n − V^n = U^{n−h}(U^h − V^h) + V^h(U^{n−h} − V^{n−h})` gives
`U^{n−h}(U^h − V^h) < U^n − V^n` when `0 ≤ V < U` and `h < n`. -/
theorem pow_sub_pow_lower (U V : ℤ) (hV : 0 < V) (hUV : V < U) {h n : ℕ} (hhn : h < n) :
    U ^ (n - h) * (U ^ h - V ^ h) < U ^ n - V ^ n := by
  have e : U ^ n - V ^ n = U ^ (n - h) * (U ^ h - V ^ h) + V ^ h * (U ^ (n - h) - V ^ (n - h)) := by
    have : n = (n - h) + h := by omega
    conv_lhs => rw [this]
    ring
  rw [e]
  have hpos : 0 < V ^ h * (U ^ (n - h) - V ^ (n - h)) :=
    mul_pos (pow_pos hV h) (sub_pos.mpr (pow_lt_pow_left₀ hUV hV.le (by omega)))
  linarith

/-- **C002's (U1), full form.** Two distinct positive words `u ≠ v` of the same length `m`
and total `A`, with `U = 2^A > V = 3^m`, and `k, ℓ ≥ 1`, `k + ℓ ≥ 3`: the reduced
denominator of `u^k v^ℓ` exceeds `2^m · U/V`, i.e. `U · 2^m · gcd(C, D) < V · D`. -/
theorem uniform_two_block_strong (u v : List ℕ) (hu : ∀ a ∈ u, 1 ≤ a) (hv : ∀ a ∈ v, 1 ≤ a)
    (hu0 : u ≠ []) (huv : u ≠ v) (hlen : u.length = v.length) (hsum : u.sum = v.sum)
    (hUV : (3 : ℤ) ^ u.length < 2 ^ u.sum) (k l : ℕ) (hk : 1 ≤ k) (hl : 1 ≤ l)
    (hn : 3 ≤ k + l) :
    (2 : ℤ) ^ u.sum
        * (2 ^ u.length * (Int.gcd (C (rep u k ++ rep v l)) (D (rep u k ++ rep v l)) : ℤ))
      < 3 ^ u.length * D (rep u k ++ rep v l) := by
  have hv0 : v ≠ [] := fun h => hu0 (List.length_eq_zero_iff.mp (hlen.trans (by simp [h])))
  -- the common block data
  have hDv : D v = D u := by simp [D, hlen, hsum]
  have hE : D u = 2 ^ u.sum - 3 ^ u.length := rfl
  -- the gcd divides `|J| · |U^h − V^h|`
  have h5 := gcd_dvd_K_mul_gcd u v k l hu hu0 hv hv0 hk hl
  rw [hDv, ← hsum, ← hlen] at h5
  have hK : (D u * C v - D u * C u).natAbs = (D u).natAbs * (C v - C u).natAbs := by
    rw [← Int.natAbs_mul]; congr 1; ring
  have hcop23 : IsCoprime ((2 : ℤ) ^ u.sum) (3 ^ u.length) :=
    (Int.isCoprime_iff_gcd_eq_one.mpr (by decide)).pow
  have hsd := gcd_pow_sub_pow (2 ^ u.sum) (3 ^ u.length) hcop23 k l
  rw [← G_mul (2 ^ u.sum) (3 ^ u.length) k, ← G_mul (2 ^ u.sum) (3 ^ u.length) l, ← hE,
    Int.gcd_mul_left] at hsd
  have h5' : Int.gcd (C (rep u k ++ rep v l)) (D (rep u k ++ rep v l))
      ∣ (C v - C u).natAbs
        * (((2 : ℤ) ^ u.sum) ^ Nat.gcd k l - (3 ^ u.length) ^ Nat.gcd k l).natAbs := by
    rw [hK] at h5
    have e : (D u).natAbs * (C v - C u).natAbs
        * Int.gcd (G (2 ^ u.sum) (3 ^ u.length) k) (G (2 ^ u.sum) (3 ^ u.length) l)
        = (C v - C u).natAbs * ((D u).natAbs
          * Int.gcd (G (2 ^ u.sum) (3 ^ u.length) k) (G (2 ^ u.sum) (3 ^ u.length) l)) := by ring
    rw [e, hsd] at h5
    exact h5
  -- numeric data
  have hh1 : 1 ≤ Nat.gcd k l := Nat.gcd_pos_of_pos_left _ hk
  have hhk : Nat.gcd k l ≤ k := Nat.gcd_le_left _ hk
  have hhl : Nat.gcd k l ≤ l := Nat.gcd_le_right _ hl
  have hHh : (0 : ℤ) < ((2 : ℤ) ^ u.sum) ^ Nat.gcd k l - (3 ^ u.length) ^ Nat.gcd k l :=
    sub_pos.mpr (pow_lt_pow_left₀ hUV (by positivity) (by omega))
  have hJ : (0 : ℤ) < |C v - C u| := by
    rw [abs_pos, sub_ne_zero]
    intro hCeq
    exact huv (C_injective u v hu hv hlen hsum hCeq.symm)
  -- `|J| 2^m < 2^A 3^m` from (U2) for both words
  have hJbound : (2 : ℤ) ^ u.length * |C v - C u| < 2 ^ u.sum * 3 ^ u.length := by
    have bu := two_pow_mul_C_le u hu
    have bv := two_pow_mul_C_le v hv
    rw [← hlen, ← hsum] at bv
    have hCu := C_pos hu0
    have hCv := C_pos hv0
    have h2m : (0 : ℤ) < 2 ^ u.length := by positivity
    have h2A : (0 : ℤ) < 2 ^ u.sum := by positivity
    have q1 := mul_pos h2A h2m
    have q2 := mul_pos h2m hCu
    have q3 := mul_pos h2m hCv
    rcases le_or_gt (C u) (C v) with hle | hgt
    · rw [abs_of_nonneg (by linarith)]
      nlinarith [bv, q1, q2]
    · rw [abs_of_neg (by linarith)]
      nlinarith [bu, q1, q3]
  -- `D w = U^n − V^n`
  have hDw : D (rep u k ++ rep v l)
      = ((2 : ℤ) ^ u.sum) ^ (k + l) - (3 ^ u.length) ^ (k + l) := by
    rw [D_two, ← hlen, ← hsum]
    ring
  -- assemble
  have hg_le : ((Int.gcd (C (rep u k ++ rep v l)) (D (rep u k ++ rep v l)) : ℕ) : ℤ)
      ≤ |C v - C u| * (((2 : ℤ) ^ u.sum) ^ Nat.gcd k l - (3 ^ u.length) ^ Nat.gcd k l) := by
    have hpos := mul_pos hJ hHh
    have hdvd : ((Int.gcd (C (rep u k ++ rep v l)) (D (rep u k ++ rep v l)) : ℕ) : ℤ)
        ∣ |C v - C u| * (((2 : ℤ) ^ u.sum) ^ Nat.gcd k l - (3 ^ u.length) ^ Nat.gcd k l) := by
      have := Int.natCast_dvd_natCast.mpr h5'
      rw [Nat.cast_mul, Int.natCast_natAbs, Int.natCast_natAbs, abs_of_pos hHh] at this
      exact this
    exact Int.le_of_dvd hpos hdvd
  have hlow := pow_sub_pow_lower ((2 : ℤ) ^ u.sum) (3 ^ u.length) (by positivity) hUV
    (show Nat.gcd k l < k + l by omega)
  have h2m : (0 : ℤ) < 2 ^ u.length := by positivity
  have h2A : (0 : ℤ) < 2 ^ u.sum := by positivity
  have h3m : (0 : ℤ) < 3 ^ u.length := by positivity
  have hU2 : (2 : ℤ) ^ u.sum * 2 ^ u.sum ≤ ((2 : ℤ) ^ u.sum) ^ (k + l - Nat.gcd k l) := by
    rw [← pow_two]
    exact pow_le_pow_right₀ (one_le_pow₀ (by norm_num)) (by omega)
  calc (2 : ℤ) ^ u.sum
        * (2 ^ u.length * ((Int.gcd (C (rep u k ++ rep v l)) (D (rep u k ++ rep v l)) : ℕ) : ℤ))
      ≤ 2 ^ u.sum * (2 ^ u.length * (|C v - C u|
          * (((2 : ℤ) ^ u.sum) ^ Nat.gcd k l - (3 ^ u.length) ^ Nat.gcd k l))) :=
        mul_le_mul_of_nonneg_left (mul_le_mul_of_nonneg_left hg_le h2m.le) h2A.le
    _ = 2 ^ u.sum * ((2 ^ u.length * |C v - C u|)
          * (((2 : ℤ) ^ u.sum) ^ Nat.gcd k l - (3 ^ u.length) ^ Nat.gcd k l)) := by ring
    _ < 2 ^ u.sum * ((2 ^ u.sum * 3 ^ u.length)
          * (((2 : ℤ) ^ u.sum) ^ Nat.gcd k l - (3 ^ u.length) ^ Nat.gcd k l)) :=
        mul_lt_mul_of_pos_left (mul_lt_mul_of_pos_right hJbound hHh) h2A
    _ = 3 ^ u.length * ((2 ^ u.sum * 2 ^ u.sum)
          * (((2 : ℤ) ^ u.sum) ^ Nat.gcd k l - (3 ^ u.length) ^ Nat.gcd k l)) := by ring
    _ ≤ 3 ^ u.length * (((2 : ℤ) ^ u.sum) ^ (k + l - Nat.gcd k l)
          * (((2 : ℤ) ^ u.sum) ^ Nat.gcd k l - (3 ^ u.length) ^ Nat.gcd k l)) :=
        mul_le_mul_of_nonneg_left (mul_le_mul_of_nonneg_right hU2 hHh.le) h3m.le
    _ < 3 ^ u.length * (((2 : ℤ) ^ u.sum) ^ (k + l) - (3 ^ u.length) ^ (k + l)) :=
        mul_lt_mul_of_pos_left hlow h3m
    _ = 3 ^ u.length * D (rep u k ++ rep v l) := by rw [hDw]

/-- **C002's (U1), weaker form.** Under the same hypotheses the reduced denominator exceeds
`2^m`, i.e. `2^m · gcd(C, D) < D`. -/
theorem uniform_two_block (u v : List ℕ) (hu : ∀ a ∈ u, 1 ≤ a) (hv : ∀ a ∈ v, 1 ≤ a)
    (hu0 : u ≠ []) (huv : u ≠ v) (hlen : u.length = v.length) (hsum : u.sum = v.sum)
    (hUV : (3 : ℤ) ^ u.length < 2 ^ u.sum) (k l : ℕ) (hk : 1 ≤ k) (hl : 1 ≤ l)
    (hn : 3 ≤ k + l) :
    (2 : ℤ) ^ u.length * (Int.gcd (C (rep u k ++ rep v l)) (D (rep u k ++ rep v l)) : ℤ)
      < D (rep u k ++ rep v l) := by
  have hstrong := uniform_two_block_strong u v hu hv hu0 huv hlen hsum hUV k l hk hl hn
  have hv0 : v ≠ [] := fun h => hu0 (List.length_eq_zero_iff.mp (hlen.trans (by simp [h])))
  have hsumw : 1 ≤ (rep u k ++ rep v l).sum := by
    rw [List.sum_append, rep_sum, rep_sum]
    have := Nat.mul_le_mul hl (one_le_sum_of_ne_nil hv0 hv)
    omega
  have hDw0 : D (rep u k ++ rep v l) ≠ 0 := fun h0 => D_odd hsumw (h0 ▸ dvd_zero 2)
  have hgpos : (0 : ℤ) < (Int.gcd (C (rep u k ++ rep v l)) (D (rep u k ++ rep v l)) : ℤ) := by
    exact_mod_cast Int.gcd_pos_of_ne_zero_right _ hDw0
  have h2m : (0 : ℤ) < 2 ^ u.length := by positivity
  have h3m : (0 : ℤ) < 3 ^ u.length := by positivity
  rcases lt_or_ge ((2 : ℤ) ^ u.length
      * (Int.gcd (C (rep u k ++ rep v l)) (D (rep u k ++ rep v l)) : ℤ)) (D (rep u k ++ rep v l))
    with h | h
  · exact h
  · exfalso
    have p1 := mul_le_mul_of_nonneg_left h h3m.le
    have p2 := mul_lt_mul_of_pos_right hUV (mul_pos h2m hgpos)
    linarith

/-! ### Main's C003 (`PROPORTIONAL_UNIFORM.md`): the fixed-pair bounds (5) and the uniform
effective bound (6), proved algebraically from the commutator identities -/

theorem G_pos (Q P : ℤ) (hQ : 0 < Q) (hP : 0 < P) : ∀ k, 1 ≤ k → 0 < G Q P k
  | 0, h => absurd h (by norm_num)
  | k + 1, _ => by
    simp only [G]
    have hG : 0 ≤ G Q P k := by
      rcases Nat.eq_zero_or_pos k with rfl | hk
      · simp [G]
      · exact (G_pos Q P hQ hP k hk).le
    exact add_pos_of_nonneg_of_pos (mul_nonneg hQ.le hG) (pow_pos hP k)

/-- The intermediate step of C002's (5): `gcd(C, D) ∣ K · G_v(ℓ)`. -/
theorem gcd_dvd_K_mul_Gv (u v : List ℕ) (k l : ℕ) (hv : ∀ a ∈ v, 1 ≤ a) (hv0 : v ≠ [])
    (hl : 1 ≤ l) :
    ((Int.gcd (C (rep u k ++ rep v l)) (D (rep u k ++ rep v l)) : ℕ) : ℤ)
      ∣ (D u * C v - D v * C u) * G (2 ^ v.sum) (3 ^ v.length) l := by
  have hgC : ((Int.gcd (C (rep u k ++ rep v l)) (D (rep u k ++ rep v l)) : ℕ) : ℤ) ∣
      C (rep u k ++ rep v l) := Int.gcd_dvd_left _ _
  have hgD : ((Int.gcd (C (rep u k ++ rep v l)) (D (rep u k ++ rep v l)) : ℕ) : ℤ) ∣
      D (rep u k ++ rep v l) := Int.gcd_dvd_right _ _
  set g : ℕ := Int.gcd (C (rep u k ++ rep v l)) (D (rep u k ++ rep v l)) with hg
  have hsum : 1 ≤ (rep u k ++ rep v l).sum := by
    rw [List.sum_append, rep_sum, rep_sum]
    have := Nat.mul_le_mul hl (one_le_sum_of_ne_nil hv0 hv)
    omega
  have hlen : 1 ≤ (rep u k ++ rep v l).length := by
    rw [List.length_append, rep_length, rep_length]
    have := Nat.mul_le_mul hl (List.length_pos_of_ne_nil hv0)
    omega
  have h6 := gcd_coprime_six' _ hsum hlen
  have hcopQ : IsCoprime (g : ℤ) (((2 : ℤ) ^ u.sum) ^ k) := by
    have := Nat.isCoprime_iff_coprime.mpr
      (Nat.Coprime.pow_right k (Nat.Coprime.pow_right u.sum
        (h6.coprime_dvd_right (by norm_num : 2 ∣ 6))))
    exact_mod_cast this
  have h1 : (g : ℤ) ∣ (2 ^ u.sum) ^ k
      * (G (2 ^ v.sum) (3 ^ v.length) l * (D u * C v - D v * C u)) := by
    rw [← mul_assoc, ← commutator_two_u]
    exact dvd_sub (dvd_mul_of_dvd_right hgC _) (dvd_mul_of_dvd_right hgD _)
  rw [mul_comm]
  exact hcopQ.dvd_of_dvd_mul_left h1

/-- The other intermediate step of C002's (5): `gcd(C, D) ∣ K · G_u(k)`. -/
theorem gcd_dvd_K_mul_Gu (u v : List ℕ) (k l : ℕ) (hv : ∀ a ∈ v, 1 ≤ a) (hv0 : v ≠ [])
    (hl : 1 ≤ l) :
    ((Int.gcd (C (rep u k ++ rep v l)) (D (rep u k ++ rep v l)) : ℕ) : ℤ)
      ∣ (D u * C v - D v * C u) * G (2 ^ u.sum) (3 ^ u.length) k := by
  have hgC : ((Int.gcd (C (rep u k ++ rep v l)) (D (rep u k ++ rep v l)) : ℕ) : ℤ) ∣
      C (rep u k ++ rep v l) := Int.gcd_dvd_left _ _
  have hgD : ((Int.gcd (C (rep u k ++ rep v l)) (D (rep u k ++ rep v l)) : ℕ) : ℤ) ∣
      D (rep u k ++ rep v l) := Int.gcd_dvd_right _ _
  set g : ℕ := Int.gcd (C (rep u k ++ rep v l)) (D (rep u k ++ rep v l)) with hg
  have hsum : 1 ≤ (rep u k ++ rep v l).sum := by
    rw [List.sum_append, rep_sum, rep_sum]
    have := Nat.mul_le_mul hl (one_le_sum_of_ne_nil hv0 hv)
    omega
  have hlen : 1 ≤ (rep u k ++ rep v l).length := by
    rw [List.length_append, rep_length, rep_length]
    have := Nat.mul_le_mul hl (List.length_pos_of_ne_nil hv0)
    omega
  have h6 := gcd_coprime_six' _ hsum hlen
  have hcopR : IsCoprime (g : ℤ) (((3 : ℤ) ^ v.length) ^ l) := by
    have := Nat.isCoprime_iff_coprime.mpr
      (Nat.Coprime.pow_right l (Nat.Coprime.pow_right v.length
        (h6.coprime_dvd_right (by norm_num : 3 ∣ 6))))
    exact_mod_cast this
  have h2 : (g : ℤ) ∣ (3 ^ v.length) ^ l
      * (G (2 ^ u.sum) (3 ^ u.length) k * (D u * C v - D v * C u)) := by
    have := dvd_sub (dvd_mul_of_dvd_right hgC (D v)) (dvd_mul_of_dvd_right hgD (C v))
    rw [commutator_two_v, dvd_neg, mul_assoc] at this
    exact this
  rw [mul_comm]
  exact hcopR.dvd_of_dvd_mul_left h2

/-- Positivity of `D(u^k v^ℓ)` for contracting blocks. -/
theorem D_two_pos (u v : List ℕ) (k l : ℕ) (hk : 1 ≤ k) (hl : 1 ≤ l) (hDu : 0 < D u)
    (hDv : 0 < D v) : 0 < D (rep u k ++ rep v l) := by
  have hPQ : (3 : ℤ) ^ u.length < 2 ^ u.sum := by simp only [D] at hDu; linarith
  have hRS : (3 : ℤ) ^ v.length < 2 ^ v.sum := by simp only [D] at hDv; linarith
  have hPQk : ((3 : ℤ) ^ u.length) ^ k < ((2 : ℤ) ^ u.sum) ^ k :=
    pow_lt_pow_left₀ hPQ (by positivity) (by omega)
  have hRSl : ((3 : ℤ) ^ v.length) ^ l < ((2 : ℤ) ^ v.sum) ^ l :=
    pow_lt_pow_left₀ hRS (by positivity) (by omega)
  rw [D_two]
  have := mul_lt_mul'' hRSl hPQk (by positivity) (by positivity)
  linarith

/-- **C003's (5), first form.** For contracting blocks with `K ≠ 0`:
`Q^k D_v · gcd(C, D) < |K| · D`, i.e. `den(u^k v^ℓ) > Q^k D_v/|K|`. -/
theorem fixed_pair_bound_u (u v : List ℕ) (k l : ℕ) (hv : ∀ a ∈ v, 1 ≤ a) (hv0 : v ≠ [])
    (hk : 1 ≤ k) (hl : 1 ≤ l) (hDu : 0 < D u) (hDv : 0 < D v)
    (hK : D u * C v - D v * C u ≠ 0) :
    ((2 : ℤ) ^ u.sum) ^ k * D v
        * (Int.gcd (C (rep u k ++ rep v l)) (D (rep u k ++ rep v l)) : ℤ)
      < |D u * C v - D v * C u| * D (rep u k ++ rep v l) := by
  have hGv : 0 < G (2 ^ v.sum) (3 ^ v.length) l := G_pos _ _ (by positivity) (by positivity) l hl
  have hdvd := gcd_dvd_K_mul_Gv u v k l hv hv0 hl
  have hg_le : ((Int.gcd (C (rep u k ++ rep v l)) (D (rep u k ++ rep v l)) : ℕ) : ℤ)
      ≤ |D u * C v - D v * C u| * G (2 ^ v.sum) (3 ^ v.length) l := by
    have h1 : ((Int.gcd (C (rep u k ++ rep v l)) (D (rep u k ++ rep v l)) : ℕ) : ℤ)
        ∣ |D u * C v - D v * C u| * G (2 ^ v.sum) (3 ^ v.length) l := by
      rw [← abs_of_pos hGv, ← abs_mul]
      exact (dvd_abs _ _).mpr hdvd
    exact Int.le_of_dvd (mul_pos (abs_pos.mpr hK) hGv) h1
  have hPQ : (3 : ℤ) ^ u.length < 2 ^ u.sum := by simp only [D] at hDu; linarith
  have hPQk : ((3 : ℤ) ^ u.length) ^ k < ((2 : ℤ) ^ u.sum) ^ k :=
    pow_lt_pow_left₀ hPQ (by positivity) (by omega)
  have hDvG : D v * G (2 ^ v.sum) (3 ^ v.length) l
      = ((2 : ℤ) ^ v.sum) ^ l - ((3 : ℤ) ^ v.length) ^ l := by
    unfold D; exact G_mul _ _ _
  have hR : (0 : ℤ) < ((3 : ℤ) ^ v.length) ^ l := by positivity
  calc ((2 : ℤ) ^ u.sum) ^ k * D v
          * ((Int.gcd (C (rep u k ++ rep v l)) (D (rep u k ++ rep v l)) : ℕ) : ℤ)
      ≤ ((2 : ℤ) ^ u.sum) ^ k * D v
          * (|D u * C v - D v * C u| * G (2 ^ v.sum) (3 ^ v.length) l) :=
        mul_le_mul_of_nonneg_left hg_le (mul_pos (by positivity) hDv).le
    _ = |D u * C v - D v * C u|
          * (((2 : ℤ) ^ u.sum) ^ k * (D v * G (2 ^ v.sum) (3 ^ v.length) l)) := by ring
    _ = |D u * C v - D v * C u|
          * (((2 : ℤ) ^ u.sum) ^ k * (((2 : ℤ) ^ v.sum) ^ l - ((3 : ℤ) ^ v.length) ^ l)) := by
        rw [hDvG]
    _ < |D u * C v - D v * C u|
          * (((2 : ℤ) ^ v.sum) ^ l * ((2 : ℤ) ^ u.sum) ^ k
            - ((3 : ℤ) ^ v.length) ^ l * ((3 : ℤ) ^ u.length) ^ k) := by
        apply mul_lt_mul_of_pos_left _ (abs_pos.mpr hK)
        nlinarith [mul_lt_mul_of_pos_left hPQk hR]
    _ = |D u * C v - D v * C u| * D (rep u k ++ rep v l) := by rw [D_two]

/-- **C003's (5), second form.** `S^ℓ D_u · gcd(C, D) < |K| · D`, i.e.
`den(u^k v^ℓ) > S^ℓ D_u/|K|`. -/
theorem fixed_pair_bound_v (u v : List ℕ) (k l : ℕ) (hv : ∀ a ∈ v, 1 ≤ a) (hv0 : v ≠ [])
    (hk : 1 ≤ k) (hl : 1 ≤ l) (hDu : 0 < D u) (hDv : 0 < D v)
    (hK : D u * C v - D v * C u ≠ 0) :
    ((2 : ℤ) ^ v.sum) ^ l * D u
        * (Int.gcd (C (rep u k ++ rep v l)) (D (rep u k ++ rep v l)) : ℤ)
      < |D u * C v - D v * C u| * D (rep u k ++ rep v l) := by
  have hGu : 0 < G (2 ^ u.sum) (3 ^ u.length) k := G_pos _ _ (by positivity) (by positivity) k hk
  have hdvd := gcd_dvd_K_mul_Gu u v k l hv hv0 hl
  have hg_le : ((Int.gcd (C (rep u k ++ rep v l)) (D (rep u k ++ rep v l)) : ℕ) : ℤ)
      ≤ |D u * C v - D v * C u| * G (2 ^ u.sum) (3 ^ u.length) k := by
    have h1 : ((Int.gcd (C (rep u k ++ rep v l)) (D (rep u k ++ rep v l)) : ℕ) : ℤ)
        ∣ |D u * C v - D v * C u| * G (2 ^ u.sum) (3 ^ u.length) k := by
      rw [← abs_of_pos hGu, ← abs_mul]
      exact (dvd_abs _ _).mpr hdvd
    exact Int.le_of_dvd (mul_pos (abs_pos.mpr hK) hGu) h1
  have hRS : (3 : ℤ) ^ v.length < 2 ^ v.sum := by simp only [D] at hDv; linarith
  have hRSl : ((3 : ℤ) ^ v.length) ^ l < ((2 : ℤ) ^ v.sum) ^ l :=
    pow_lt_pow_left₀ hRS (by positivity) (by omega)
  have hDuG : D u * G (2 ^ u.sum) (3 ^ u.length) k
      = ((2 : ℤ) ^ u.sum) ^ k - ((3 : ℤ) ^ u.length) ^ k := by
    unfold D; exact G_mul _ _ _
  have hP : (0 : ℤ) < ((3 : ℤ) ^ u.length) ^ k := by positivity
  calc ((2 : ℤ) ^ v.sum) ^ l * D u
          * ((Int.gcd (C (rep u k ++ rep v l)) (D (rep u k ++ rep v l)) : ℕ) : ℤ)
      ≤ ((2 : ℤ) ^ v.sum) ^ l * D u
          * (|D u * C v - D v * C u| * G (2 ^ u.sum) (3 ^ u.length) k) :=
        mul_le_mul_of_nonneg_left hg_le (mul_pos (by positivity) hDu).le
    _ = |D u * C v - D v * C u|
          * (((2 : ℤ) ^ v.sum) ^ l * (D u * G (2 ^ u.sum) (3 ^ u.length) k)) := by ring
    _ = |D u * C v - D v * C u|
          * (((2 : ℤ) ^ v.sum) ^ l * (((2 : ℤ) ^ u.sum) ^ k - ((3 : ℤ) ^ u.length) ^ k)) := by
        rw [hDuG]
    _ < |D u * C v - D v * C u|
          * (((2 : ℤ) ^ v.sum) ^ l * ((2 : ℤ) ^ u.sum) ^ k
            - ((3 : ℤ) ^ v.length) ^ l * ((3 : ℤ) ^ u.length) ^ k) := by
        apply mul_lt_mul_of_pos_left _ (abs_pos.mpr hK)
        nlinarith [mul_lt_mul_of_pos_right hRSl hP]
    _ = |D u * C v - D v * C u| * D (rep u k ++ rep v l) := by rw [D_two]

/-! #### The intercept and fixed-point bounds (7)–(9) -/

/-- C003's (7)+(8): for a contracting positive word, `2^m C_z < D_z (3^m + 1) 3^m`
(the fixed point is below `F(m) = (3^m + 1) 3^m / 2^m`). -/
theorem two_pow_mul_C_lt (z : List ℕ) (hpos : ∀ a ∈ z, 1 ≤ a) (hD : 0 < D z) :
    (2 : ℤ) ^ z.length * C z < D z * ((3 ^ z.length + 1) * 3 ^ z.length) := by
  have h7 := two_pow_mul_C_le z hpos
  have hQ : (2 : ℤ) ^ z.sum = D z + 3 ^ z.length := by simp [D]
  have h2m : (0 : ℤ) < 2 ^ z.length := by positivity
  have h3m : (0 : ℤ) < 3 ^ z.length := by positivity
  have h2A : (0 : ℤ) < 2 ^ z.sum := by positivity
  have hD1 : (1 : ℤ) ≤ D z := hD
  have hQ3 : (2 : ℤ) ^ z.sum * 3 ^ z.length = D z * 3 ^ z.length + 3 ^ z.length * 3 ^ z.length := by
    rw [hQ]; ring
  nlinarith [h7, hQ3, mul_pos h2A h2m, mul_le_mul_of_nonneg_left hD1 (mul_pos h3m h3m).le]

/-- `F(m) = (3^m + 1) 3^m / 2^m` is increasing, in cleared form. -/
theorem F_mono {m M : ℕ} (h : m ≤ M) :
    ((3 : ℤ) ^ m + 1) * 3 ^ m * 2 ^ M ≤ (3 ^ M + 1) * 3 ^ M * 2 ^ m := by
  obtain ⟨d, rfl⟩ := Nat.exists_eq_add_of_le h
  simp only [pow_add]
  have h3 : (3 : ℤ) ^ m + 1 ≤ 3 ^ m * 3 ^ d + 1 := by
    have h1 : (1 : ℤ) ≤ 3 ^ d := one_le_pow₀ (by norm_num)
    nlinarith [pow_pos (by norm_num : (0 : ℤ) < 3) m]
  have h23 : (2 : ℤ) ^ d ≤ 3 ^ d := pow_le_pow_left₀ (by norm_num) (by norm_num) d
  have hpos : (0 : ℤ) ≤ 3 ^ m * 2 ^ m := by positivity
  calc ((3 : ℤ) ^ m + 1) * 3 ^ m * (2 ^ m * 2 ^ d)
      = ((3 ^ m + 1) * 2 ^ d) * (3 ^ m * 2 ^ m) := by ring
    _ ≤ ((3 ^ m * 3 ^ d + 1) * 3 ^ d) * (3 ^ m * 2 ^ m) := by
        apply mul_le_mul_of_nonneg_right _ hpos
        exact mul_le_mul h3 h23 (by positivity) (by positivity)
    _ = (3 ^ m * 3 ^ d + 1) * (3 ^ m * 3 ^ d) * 2 ^ m := by ring

/-- C003's (9), one block: for `m_z ≤ M`, `2^M C_z < D_z (3^M + 1) 3^M`. -/
theorem two_pow_mul_C_lt_M (z : List ℕ) (hpos : ∀ a ∈ z, 1 ≤ a) (hD : 0 < D z) {M : ℕ}
    (hM : z.length ≤ M) :
    (2 : ℤ) ^ M * C z < D z * ((3 ^ M + 1) * 3 ^ M) := by
  have h1 := two_pow_mul_C_lt z hpos hD
  have h2 := F_mono hM
  have h2m : (0 : ℤ) < 2 ^ z.length := by positivity
  have h3 : (2 : ℤ) ^ z.length * (2 ^ M * C z) < 2 ^ z.length * (D z * ((3 ^ M + 1) * 3 ^ M)) := by
    calc (2 : ℤ) ^ z.length * (2 ^ M * C z) = 2 ^ M * (2 ^ z.length * C z) := by ring
      _ < 2 ^ M * (D z * ((3 ^ z.length + 1) * 3 ^ z.length)) :=
          mul_lt_mul_of_pos_left h1 (by positivity)
      _ = D z * ((3 ^ z.length + 1) * 3 ^ z.length * 2 ^ M) := by ring
      _ ≤ D z * ((3 ^ M + 1) * 3 ^ M * 2 ^ z.length) := mul_le_mul_of_nonneg_left h2 hD.le
      _ = 2 ^ z.length * (D z * ((3 ^ M + 1) * 3 ^ M)) := by ring
  exact lt_of_mul_lt_mul_left h3 h2m.le

/-- C003's (9), the determinant: `2^M |K| < D_u D_v (3^M + 1) 3^M` for contracting blocks of
lengths at most `M`. -/
theorem K_bound (u v : List ℕ) (hu : ∀ a ∈ u, 1 ≤ a) (hv : ∀ a ∈ v, 1 ≤ a) (hDu : 0 < D u)
    (hDv : 0 < D v) {M : ℕ} (hMu : u.length ≤ M) (hMv : v.length ≤ M) :
    |D u * C v - D v * C u| * 2 ^ M < D u * D v * ((3 ^ M + 1) * 3 ^ M) := by
  have hu0 : u ≠ [] := by
    rintro rfl
    simp [D] at hDu
  have hv0 : v ≠ [] := by
    rintro rfl
    simp [D] at hDv
  have hCu := two_pow_mul_C_lt_M u hu hDu hMu
  have hCv := two_pow_mul_C_lt_M v hv hDv hMv
  have hCu0 := C_pos hu0
  have hCv0 := C_pos hv0
  have h2M : (0 : ℤ) < 2 ^ M := by positivity
  rw [← abs_of_pos h2M, ← abs_mul, abs_lt]
  constructor
  · nlinarith [mul_lt_mul_of_pos_left hCu hDv, mul_pos (mul_pos hDu h2M) hCv0]
  · nlinarith [mul_lt_mul_of_pos_left hCv hDu, mul_pos (mul_pos hDv h2M) hCu0]

/-- **C003's (6), `u`-block form.** Both blocks contracting, `K ≠ 0`, `Q = 2^Σu ≥ S = 2^Σv`,
`k ≥ 3`, `ℓ ≥ 1`, `M ≥` both lengths with `3^M < Q`: then
`2^M Q^{k−3} · gcd(C, D) < D`, i.e. `den(u^k v^ℓ) > 2^M Q^{k−3}`. -/
theorem uniform_bound_u (u v : List ℕ) (k l : ℕ) (hu : ∀ a ∈ u, 1 ≤ a) (hv : ∀ a ∈ v, 1 ≤ a)
    (hv0 : v ≠ []) (hk : 3 ≤ k) (hl : 1 ≤ l) (hDu : 0 < D u) (hDv : 0 < D v)
    (hK : D u * C v - D v * C u ≠ 0) {M : ℕ} (hMu : u.length ≤ M) (hMv : v.length ≤ M)
    (h3M : (3 : ℤ) ^ M < 2 ^ u.sum) :
    (2 : ℤ) ^ M * ((2 : ℤ) ^ u.sum) ^ (k - 3)
        * (Int.gcd (C (rep u k ++ rep v l)) (D (rep u k ++ rep v l)) : ℤ)
      < D (rep u k ++ rep v l) := by
  have h5 := fixed_pair_bound_u u v k l hv hv0 (by omega) hl hDu hDv hK
  have hKb := K_bound u v hu hv hDu hDv hMu hMv
  have hDw := D_two_pos u v k l (by omega) hl hDu hDv
  have h2M : (0 : ℤ) < 2 ^ M := by positivity
  have hQ : (0 : ℤ) < 2 ^ u.sum := by positivity
  have hQ3 : (3 : ℤ) ^ M + 1 ≤ 2 ^ u.sum := by linarith
  have h3Mpos : (0 : ℤ) < 3 ^ M := by positivity
  have hF : ((3 : ℤ) ^ M + 1) * 3 ^ M < 2 ^ u.sum * 2 ^ u.sum := by
    nlinarith [mul_le_mul_of_nonneg_right hQ3 h3Mpos.le, mul_lt_mul_of_pos_left h3M hQ]
  have hDuQ : D u < 2 ^ u.sum := by
    simp only [D]
    linarith [pow_pos (by norm_num : (0 : ℤ) < 3) u.length]
  set g : ℤ := (Int.gcd (C (rep u k ++ rep v l)) (D (rep u k ++ rep v l)) : ℤ) with hg
  set W : ℤ := D (rep u k ++ rep v l) with hW
  have step1 : 2 ^ M * (((2 : ℤ) ^ u.sum) ^ k * D v * g) < 2 ^ M * (|D u * C v - D v * C u| * W) :=
    mul_lt_mul_of_pos_left h5 h2M
  have step2 : |D u * C v - D v * C u| * 2 ^ M * W
      < D u * D v * ((3 ^ M + 1) * 3 ^ M) * W := mul_lt_mul_of_pos_right hKb hDw
  have step3 : D u * D v * ((3 ^ M + 1) * 3 ^ M) * W ≤ D u * D v * (2 ^ u.sum * 2 ^ u.sum) * W := by
    apply mul_le_mul_of_nonneg_right _ hDw.le
    exact mul_le_mul_of_nonneg_left hF.le (mul_pos hDu hDv).le
  have step4 : D v * (2 ^ M * ((2 : ℤ) ^ u.sum) ^ k * g)
      < D v * (D u * (2 ^ u.sum * 2 ^ u.sum) * W) := by nlinarith [step1, step2, step3]
  have step5 : 2 ^ M * ((2 : ℤ) ^ u.sum) ^ k * g < D u * (2 ^ u.sum * 2 ^ u.sum) * W :=
    lt_of_mul_lt_mul_left step4 hDv.le
  have step6 : D u * (2 ^ u.sum * 2 ^ u.sum) * W < 2 ^ u.sum * (2 ^ u.sum * 2 ^ u.sum) * W := by
    apply mul_lt_mul_of_pos_right _ hDw
    exact mul_lt_mul_of_pos_right hDuQ (by positivity)
  have hk3 : ((2 : ℤ) ^ u.sum) ^ k = ((2 : ℤ) ^ u.sum) ^ (k - 3) * ((2 : ℤ) ^ u.sum) ^ 3 := by
    rw [← pow_add, Nat.sub_add_cancel hk]
  have step7 : ((2 : ℤ) ^ u.sum) ^ 3 * (2 ^ M * ((2 : ℤ) ^ u.sum) ^ (k - 3) * g)
      < ((2 : ℤ) ^ u.sum) ^ 3 * W := by
    calc ((2 : ℤ) ^ u.sum) ^ 3 * (2 ^ M * ((2 : ℤ) ^ u.sum) ^ (k - 3) * g)
        = 2 ^ M * (((2 : ℤ) ^ u.sum) ^ (k - 3) * ((2 : ℤ) ^ u.sum) ^ 3) * g := by ring
      _ = 2 ^ M * ((2 : ℤ) ^ u.sum) ^ k * g := by rw [← hk3]
      _ < 2 ^ u.sum * (2 ^ u.sum * 2 ^ u.sum) * W := lt_trans step5 step6
      _ = ((2 : ℤ) ^ u.sum) ^ 3 * W := by ring
  exact lt_of_mul_lt_mul_left step7 (by positivity)

/-- **C003's (6), `v`-block form.** As above with the roles of the blocks exchanged:
`S ≥ Q`, `ℓ ≥ 3`, `k ≥ 1`, `3^M < S`; then `2^M S^{ℓ−3} · gcd(C, D) < D`. -/
theorem uniform_bound_v (u v : List ℕ) (k l : ℕ) (hu : ∀ a ∈ u, 1 ≤ a) (hv : ∀ a ∈ v, 1 ≤ a)
    (hv0 : v ≠ []) (hk : 1 ≤ k) (hl : 3 ≤ l) (hDu : 0 < D u) (hDv : 0 < D v)
    (hK : D u * C v - D v * C u ≠ 0) {M : ℕ} (hMu : u.length ≤ M) (hMv : v.length ≤ M)
    (h3M : (3 : ℤ) ^ M < 2 ^ v.sum) :
    (2 : ℤ) ^ M * ((2 : ℤ) ^ v.sum) ^ (l - 3)
        * (Int.gcd (C (rep u k ++ rep v l)) (D (rep u k ++ rep v l)) : ℤ)
      < D (rep u k ++ rep v l) := by
  have h5 := fixed_pair_bound_v u v k l hv hv0 hk (by omega) hDu hDv hK
  have hKb := K_bound u v hu hv hDu hDv hMu hMv
  have hDw := D_two_pos u v k l hk (by omega) hDu hDv
  have h2M : (0 : ℤ) < 2 ^ M := by positivity
  have hS : (0 : ℤ) < 2 ^ v.sum := by positivity
  have hS3 : (3 : ℤ) ^ M + 1 ≤ 2 ^ v.sum := by linarith
  have h3Mpos : (0 : ℤ) < 3 ^ M := by positivity
  have hF : ((3 : ℤ) ^ M + 1) * 3 ^ M < 2 ^ v.sum * 2 ^ v.sum := by
    nlinarith [mul_le_mul_of_nonneg_right hS3 h3Mpos.le, mul_lt_mul_of_pos_left h3M hS]
  have hDvS : D v < 2 ^ v.sum := by
    simp only [D]
    linarith [pow_pos (by norm_num : (0 : ℤ) < 3) v.length]
  set g : ℤ := (Int.gcd (C (rep u k ++ rep v l)) (D (rep u k ++ rep v l)) : ℤ) with hg
  set W : ℤ := D (rep u k ++ rep v l) with hW
  have step1 : 2 ^ M * (((2 : ℤ) ^ v.sum) ^ l * D u * g) < 2 ^ M * (|D u * C v - D v * C u| * W) :=
    mul_lt_mul_of_pos_left h5 h2M
  have step2 : |D u * C v - D v * C u| * 2 ^ M * W
      < D u * D v * ((3 ^ M + 1) * 3 ^ M) * W := mul_lt_mul_of_pos_right hKb hDw
  have step3 : D u * D v * ((3 ^ M + 1) * 3 ^ M) * W ≤ D u * D v * (2 ^ v.sum * 2 ^ v.sum) * W := by
    apply mul_le_mul_of_nonneg_right _ hDw.le
    exact mul_le_mul_of_nonneg_left hF.le (mul_pos hDu hDv).le
  have step4 : D u * (2 ^ M * ((2 : ℤ) ^ v.sum) ^ l * g)
      < D u * (D v * (2 ^ v.sum * 2 ^ v.sum) * W) := by nlinarith [step1, step2, step3]
  have step5 : 2 ^ M * ((2 : ℤ) ^ v.sum) ^ l * g < D v * (2 ^ v.sum * 2 ^ v.sum) * W :=
    lt_of_mul_lt_mul_left step4 hDu.le
  have step6 : D v * (2 ^ v.sum * 2 ^ v.sum) * W < 2 ^ v.sum * (2 ^ v.sum * 2 ^ v.sum) * W := by
    apply mul_lt_mul_of_pos_right _ hDw
    exact mul_lt_mul_of_pos_right hDvS (by positivity)
  have hl3 : ((2 : ℤ) ^ v.sum) ^ l = ((2 : ℤ) ^ v.sum) ^ (l - 3) * ((2 : ℤ) ^ v.sum) ^ 3 := by
    rw [← pow_add, Nat.sub_add_cancel hl]
  have step7 : ((2 : ℤ) ^ v.sum) ^ 3 * (2 ^ M * ((2 : ℤ) ^ v.sum) ^ (l - 3) * g)
      < ((2 : ℤ) ^ v.sum) ^ 3 * W := by
    calc ((2 : ℤ) ^ v.sum) ^ 3 * (2 ^ M * ((2 : ℤ) ^ v.sum) ^ (l - 3) * g)
        = 2 ^ M * (((2 : ℤ) ^ v.sum) ^ (l - 3) * ((2 : ℤ) ^ v.sum) ^ 3) * g := by ring
      _ = 2 ^ M * ((2 : ℤ) ^ v.sum) ^ l * g := by rw [← hl3]
      _ < 2 ^ v.sum * (2 ^ v.sum * 2 ^ v.sum) * W := lt_trans step5 step6
      _ = ((2 : ℤ) ^ v.sum) ^ 3 * W := by ring
  exact lt_of_mul_lt_mul_left step7 (by positivity)

/-- **C003's (6) with `M = max(m_u, m_v)` and `Q_* = Q`.** If the `u`-block has the larger
binary power and is repeated `k ≥ 3` times, `den(u^k v^ℓ) > 2^M Q^{k−3} ≥ 2^M`. -/
theorem uniform_bound_max_u (u v : List ℕ) (k l : ℕ) (hu : ∀ a ∈ u, 1 ≤ a)
    (hv : ∀ a ∈ v, 1 ≤ a) (hv0 : v ≠ []) (hk : 3 ≤ k) (hl : 1 ≤ l) (hDu : 0 < D u)
    (hDv : 0 < D v) (hK : D u * C v - D v * C u ≠ 0) (hQS : (2 : ℤ) ^ v.sum ≤ 2 ^ u.sum) :
    (2 : ℤ) ^ max u.length v.length * ((2 : ℤ) ^ u.sum) ^ (k - 3)
        * (Int.gcd (C (rep u k ++ rep v l)) (D (rep u k ++ rep v l)) : ℤ)
      < D (rep u k ++ rep v l) := by
  apply uniform_bound_u u v k l hu hv hv0 hk hl hDu hDv hK (le_max_left _ _) (le_max_right _ _)
  have hPQ : (3 : ℤ) ^ u.length < 2 ^ u.sum := by simp only [D] at hDu; linarith
  have hRS : (3 : ℤ) ^ v.length < 2 ^ v.sum := by simp only [D] at hDv; linarith
  rcases le_total v.length u.length with h | h
  · rw [max_eq_left h]; exact hPQ
  · rw [max_eq_right h]; exact lt_of_lt_of_le hRS hQS

/-- The worked example `(1,2,2)^3 (2)` of C003: `C = 213341`, `D = 72023`, coprime. -/
example : C (rep [1, 2, 2] 3 ++ rep [2] 1) = 213341 ∧ D (rep [1, 2, 2] 3 ++ rep [2] 1) = 72023 ∧
    Int.gcd (C (rep [1, 2, 2] 3 ++ rep [2] 1)) (D (rep [1, 2, 2] 3 ++ rep [2] 1)) = 1 := by
  norm_num [rep, C, D]

/-! ### One-letter cuts (main's C004 `ROTATION_LATTICE.md` §2, (6)–(7)) -/

/-- C004's (6): cut the first letter `a` off `w = a :: v`, so `u = (a)`, `C_u = 1`,
`D_u = 2^a − 3` and `K = D_u C_v − D_v C_u`; then `2^a K = (2^a − 3) C_w − D_w`. This is
the `k = 1` case of `commutator`. -/
theorem cut_identity (a : ℕ) (v : List ℕ) :
    (2 : ℤ) ^ a * ((2 ^ a - 3) * C v - D v) = (2 ^ a - 3) * C (a :: v) - D (a :: v) := by
  simp only [C, D, List.sum_cons, List.length_cons, pow_succ, pow_add]
  ring

/-- `gcd(a, b − a) = gcd(a, b)` for integers. -/
theorem gcd_sub_self_right (a b : ℤ) : Int.gcd a (b - a) = Int.gcd a b := by
  apply Nat.dvd_antisymm
  · refine Int.dvd_gcd (Int.gcd_dvd_left _ _) ?_
    have h := dvd_add (Int.gcd_dvd_right a (b - a)) (Int.gcd_dvd_left a (b - a))
    rwa [sub_add_cancel] at h
  · exact Int.dvd_gcd (Int.gcd_dvd_left _ _)
      (dvd_sub (Int.gcd_dvd_right _ _) (Int.gcd_dvd_left _ _))

/-- C004's (7): for `w = a :: v` with `a ≥ 1`, `g = gcd(C_w, D_w)` and `d₀ = D_w/g`,
`gcd(D_w, K) = g · gcd(d₀, 2^a − 3)`, where `K = (2^a − 3) C_v − D_v` is the one-letter cut
commutator. -/
theorem cut_gcd (a : ℕ) (v : List ℕ) (ha : 1 ≤ a) :
    Int.gcd (D (a :: v)) ((2 ^ a - 3) * C v - D v)
      = Int.gcd (C (a :: v)) (D (a :: v))
        * Int.gcd (D (a :: v) / (Int.gcd (C (a :: v)) (D (a :: v)) : ℤ)) (2 ^ a - 3) := by
  have hsum : 1 ≤ (a :: v).sum := by
    simp only [List.sum_cons]; omega
  have hDodd : ¬ (2 : ℤ) ∣ D (a :: v) := D_odd hsum
  have hD0 : D (a :: v) ≠ 0 := fun h => hDodd (by rw [h]; exact dvd_zero 2)
  set g : ℕ := Int.gcd (C (a :: v)) (D (a :: v)) with hg
  have hgpos : 0 < g := Int.gcd_pos_of_ne_zero_right _ hD0
  have hgC : (g : ℤ) ∣ C (a :: v) := Int.gcd_dvd_left _ _
  have hgD : (g : ℤ) ∣ D (a :: v) := Int.gcd_dvd_right _ _
  have hcop : Int.gcd (C (a :: v) / g) (D (a :: v) / g) = 1 := Int.gcd_div_gcd_div_gcd hgpos
  set n : ℤ := C (a :: v) / g with hn
  set d₀ : ℤ := D (a :: v) / g with hd₀
  have hCw : C (a :: v) = g * n := (Int.mul_ediv_cancel' hgC).symm
  have hDw : D (a :: v) = g * d₀ := (Int.mul_ediv_cancel' hgD).symm
  -- Step 1: `2^a` is a unit modulo the odd `D_w`.
  have step1 : Int.gcd (D (a :: v)) ((2 ^ a - 3) * C v - D v)
      = Int.gcd (D (a :: v)) (2 ^ a * ((2 ^ a - 3) * C v - D v)) := by
    apply Nat.dvd_antisymm
    · exact Int.dvd_gcd (Int.gcd_dvd_left _ _)
        (dvd_mul_of_dvd_right (Int.gcd_dvd_right _ _) _)
    · have hD : ((Int.gcd (D (a :: v)) (2 ^ a * ((2 ^ a - 3) * C v - D v)) : ℕ) : ℤ)
          ∣ D (a :: v) := Int.gcd_dvd_left _ _
      have hK : ((Int.gcd (D (a :: v)) (2 ^ a * ((2 ^ a - 3) * C v - D v)) : ℕ) : ℤ)
          ∣ 2 ^ a * ((2 ^ a - 3) * C v - D v) := Int.gcd_dvd_right _ _
      have h2 : ¬ 2 ∣ Int.gcd (D (a :: v)) (2 ^ a * ((2 ^ a - 3) * C v - D v)) := fun h2 =>
        hDodd ((by exact_mod_cast h2 : (2 : ℤ) ∣
          ((Int.gcd (D (a :: v)) (2 ^ a * ((2 ^ a - 3) * C v - D v)) : ℕ) : ℤ)).trans hD)
      have hcop2 : IsCoprime
          ((Int.gcd (D (a :: v)) (2 ^ a * ((2 ^ a - 3) * C v - D v)) : ℕ) : ℤ) ((2 : ℤ) ^ a) := by
        have := Nat.isCoprime_iff_coprime.mpr (Nat.Coprime.pow_right a
          ((Nat.Prime.coprime_iff_not_dvd Nat.prime_two).mpr h2).symm)
        exact_mod_cast this
      exact Int.dvd_gcd hD (hcop2.dvd_of_dvd_mul_left hK)
  -- Step 2: the cut identity, then `gcd(D, X − D) = gcd(D, X)`.
  have step2 : Int.gcd (D (a :: v)) (2 ^ a * ((2 ^ a - 3) * C v - D v))
      = Int.gcd (D (a :: v)) ((2 ^ a - 3) * C (a :: v)) := by
    rw [cut_identity, gcd_sub_self_right]
  -- Step 3: factor out `g`.
  have step3 : Int.gcd (D (a :: v)) ((2 ^ a - 3) * C (a :: v))
      = g * Int.gcd d₀ ((2 ^ a - 3) * n) := by
    rw [hDw, hCw, show (2 ^ a - 3 : ℤ) * (g * n) = g * ((2 ^ a - 3) * n) by ring,
      Int.gcd_mul_left, Int.natAbs_natCast]
  -- Step 4: cancel `n`, which is coprime to `d₀`.
  have step4 : Int.gcd d₀ ((2 ^ a - 3) * n) = Int.gcd d₀ (2 ^ a - 3) := by
    apply Nat.dvd_antisymm
    · have hcopn : IsCoprime ((Int.gcd d₀ ((2 ^ a - 3) * n) : ℕ) : ℤ) n :=
        (Int.isCoprime_iff_gcd_eq_one.mpr hcop).symm.of_isCoprime_of_dvd_left
          (Int.gcd_dvd_left _ _)
      exact Int.dvd_gcd (Int.gcd_dvd_left _ _)
        (hcopn.dvd_of_dvd_mul_right (Int.gcd_dvd_right _ _))
    · exact Int.dvd_gcd (Int.gcd_dvd_left _ _)
        (dvd_mul_of_dvd_left (Int.gcd_dvd_right _ _) _)
  rw [step1, step2, step3, step4]

/-- The `d = 5` control `(1,2,2)`: `K = −14`, (6) reads `−28 = −28`, and both sides of (7)
are `1`. -/
example : (2 : ℤ) ^ 1 * ((2 ^ 1 - 3) * C [2, 2] - D [2, 2]) = -28 ∧
    (2 ^ 1 - 3 : ℤ) * C [1, 2, 2] - D [1, 2, 2] = -28 ∧
    Int.gcd (D [1, 2, 2]) ((2 ^ 1 - 3) * C [2, 2] - D [2, 2]) = 1 ∧
    Int.gcd (C [1, 2, 2]) (D [1, 2, 2]) = 1 := by
  norm_num [C, D]

/-! ### Mechanical words and their phases (C004 `ROTATION_LATTICE.md` §3, reverse direction) -/

/-- The word of successive differences `F(j+1) − F(j)`, `j < m`. -/
def diffWord (F : ℕ → ℕ) (m : ℕ) : List ℕ := (List.range m).map fun j => F (j + 1) - F j

/-- The phase-`l` mechanical word of total `A` and length `m`,
`a_j = ⌊((j+1)A + l)/m⌋ − ⌊(jA + l)/m⌋`; phase `0` is R71's mechanical word. -/
def mech (A m l : ℕ) : List ℕ := diffWord (fun j => (j * A + l) / m) m

theorem diffWord_zero (F : ℕ → ℕ) : diffWord F 0 = [] := rfl

theorem diffWord_succ (F : ℕ → ℕ) (m : ℕ) :
    diffWord F (m + 1) = (F 1 - F 0) :: diffWord (fun j => F (j + 1)) m := by
  simp [diffWord, List.range_succ_eq_map, List.map_map, Function.comp_def]

theorem length_diffWord (F : ℕ → ℕ) (m : ℕ) : (diffWord F m).length = m := by
  simp [diffWord]

theorem sum_map_range (f : ℕ → ℕ) :
    ∀ m, ((List.range m).map f).sum = ∑ j ∈ Finset.range m, f j
  | 0 => by simp
  | m + 1 => by
    rw [List.range_succ, List.map_append, List.sum_append, Finset.sum_range_succ,
      sum_map_range f m]
    simp

theorem sum_diffWord (F : ℕ → ℕ) (hF : Monotone F) (m : ℕ) :
    (diffWord F m).sum = F m - F 0 := by
  rw [diffWord, sum_map_range, Finset.sum_range_tsub hF]

/-- The closed form of the intercept: `2^{F 0} · C(diffWord F m) = ∑_{j<m} 3^{m−1−j} 2^{F j}`
(R71's sum, with `F j` the prefix sums). -/
theorem C_diffWord (F : ℕ → ℕ) (hF : Monotone F) :
    ∀ m, (2 : ℤ) ^ F 0 * C (diffWord F m)
      = ∑ j ∈ Finset.range m, (3 : ℤ) ^ (m - (j + 1)) * 2 ^ F j
  | 0 => by simp [diffWord_zero, C]
  | m + 1 => by
    have ih : (2 : ℤ) ^ F 1 * C (diffWord (fun j => F (j + 1)) m)
        = ∑ j ∈ Finset.range m, (3 : ℤ) ^ (m - (j + 1)) * 2 ^ F (j + 1) :=
      C_diffWord (fun j => F (j + 1)) (fun _ _ h => hF (Nat.add_le_add_right h 1)) m
    have h01 : F 0 ≤ F 1 := hF (Nat.zero_le 1)
    have hpow : (2 : ℤ) ^ F 0 * 2 ^ (F 1 - F 0) = 2 ^ F 1 := by
      rw [← pow_add, Nat.add_sub_of_le h01]
    rw [diffWord_succ, Finset.sum_range_succ']
    simp only [C, length_diffWord, Nat.add_sub_add_right, zero_add, Nat.add_sub_cancel]
    rw [← ih, ← hpow]
    ring

theorem mech_monotone (A m l : ℕ) : Monotone fun j : ℕ => (j * A + l) / m :=
  fun _ _ h => Nat.div_le_div_right (Nat.add_le_add_right (Nat.mul_le_mul_right A h) l)

theorem mech_length (A m l : ℕ) : (mech A m l).length = m := by
  simp [mech, diffWord]

theorem mech_sum {m : ℕ} (hm : 0 < m) (A l : ℕ) (hl : l < m) : (mech A m l).sum = A := by
  rw [mech, sum_diffWord _ (mech_monotone A m l)]
  simp only [zero_mul, zero_add]
  rw [show m * A + l = l + m * A by ring, Nat.add_mul_div_left _ _ hm, Nat.div_eq_of_lt hl]
  simp

/-- Every phase word has `D = 2^A − 3^m`. -/
theorem D_mech {m : ℕ} (hm : 0 < m) (A l : ℕ) (hl : l < m) : D (mech A m l) = 2 ^ A - 3 ^ m := by
  rw [D, mech_sum hm A l hl, mech_length]

/-- For `A ≥ m` the mechanical words are positive valuation words. -/
theorem mech_pos {m : ℕ} (hm : 0 < m) (A l : ℕ) (hAm : m ≤ A) : ∀ x ∈ mech A m l, 1 ≤ x := by
  intro x hx
  simp only [mech, diffWord, List.mem_map, List.mem_range] at hx
  obtain ⟨j, -, rfl⟩ := hx
  have h1 : (j * A + l + m) / m ≤ ((j + 1) * A + l) / m :=
    Nat.div_le_div_right (by nlinarith)
  rw [Nat.add_div_right _ hm] at h1
  omega

/-- The intercept of the phase-`l` word, `l < m`, as R71's sum. -/
theorem C_mech {m : ℕ} (A l : ℕ) (hl : l < m) :
    C (mech A m l) = ∑ j ∈ Finset.range m, (3 : ℤ) ^ (m - (j + 1)) * 2 ^ ((j * A + l) / m) := by
  have h := C_diffWord (fun j => (j * A + l) / m) (mech_monotone A m l) m
  simp only [zero_mul, zero_add, Nat.div_eq_of_lt hl, pow_zero, one_mul] at h
  exact h

theorem phase_floor_le (m A l j : ℕ) : j * A / m ≤ (j * A + l) / m :=
  Nat.div_le_div_right (Nat.le_add_right _ _)

theorem phase_floor_le_succ {m : ℕ} (hm : 0 < m) (A l j : ℕ) (hl : l < m) :
    (j * A + l) / m ≤ j * A / m + 1 := by
  rw [← Nat.add_div_right _ hm]
  exact Nat.div_le_div_right (by omega)

/-- `C_0 ≤ C_l`: each summand of phase `l` is at least the matching summand of phase `0`. -/
theorem C_mech_zero_le {m : ℕ} (hm : 0 < m) (A l : ℕ) (hl : l < m) :
    C (mech A m 0) ≤ C (mech A m l) := by
  rw [C_mech A 0 hm, C_mech A l hl]
  apply Finset.sum_le_sum
  intro j _
  simp only [add_zero]
  exact mul_le_mul_of_nonneg_left (pow_le_pow_right₀ (by norm_num) (phase_floor_le m A l j))
    (by positivity)

/-- `C_l < 2 C_0`: each summand of phase `l` is at most twice the matching summand of phase
`0`, and the `j = 0` summand `3^{m−1}` is the same in both. -/
theorem C_mech_lt_two {m : ℕ} (hm : 0 < m) (A l : ℕ) (hl : l < m) :
    C (mech A m l) < 2 * C (mech A m 0) := by
  rw [C_mech A 0 hm, C_mech A l hl, Finset.mul_sum]
  apply Finset.sum_lt_sum
  · intro j _
    have h := phase_floor_le_succ hm A l j hl
    simp only [add_zero]
    calc (3 : ℤ) ^ (m - (j + 1)) * 2 ^ ((j * A + l) / m)
        ≤ 3 ^ (m - (j + 1)) * 2 ^ (j * A / m + 1) :=
          mul_le_mul_of_nonneg_left (pow_le_pow_right₀ (by norm_num) h) (by positivity)
      _ = 2 * (3 ^ (m - (j + 1)) * 2 ^ (j * A / m)) := by ring
  · refine ⟨0, Finset.mem_range.mpr hm, ?_⟩
    simp only [zero_mul, zero_add, Nat.div_eq_of_lt hl, Nat.zero_div, pow_zero, mul_one]
    have : (0 : ℤ) < 3 ^ (m - 1) := by positivity
    linarith

/-! #### Rotations of a phase word are phase words -/

theorem step_add_mul {m : ℕ} (hm : 0 < m) (A r q : ℕ) :
    (r + m * q + A) / m - (r + m * q) / m = (r + A) / m - r / m := by
  rw [show r + m * q + A = r + A + m * q by ring, Nat.add_mul_div_left _ _ hm,
    Nat.add_mul_div_left _ _ hm, Nat.add_sub_add_right]

theorem step_mod {m : ℕ} (hm : 0 < m) (A N : ℕ) :
    (N + A) / m - N / m = (N % m + A) / m - N % m / m := by
  have h := step_add_mul hm A (N % m) (N / m)
  rwa [Nat.mod_add_div] at h

theorem step_congr {m : ℕ} (hm : 0 < m) (A : ℕ) {N₁ N₂ : ℕ} (h : N₁ % m = N₂ % m) :
    (N₁ + A) / m - N₁ / m = (N₂ + A) / m - N₂ / m := by
  rw [step_mod hm A N₁, step_mod hm A N₂, h]

/-- Rotating the phase-`l` word by `i` letters gives the phase `(l + iA) mod m`; in particular
every rotation of the mechanical word `mech A m 0` is the phase word of `iA mod m`. -/
theorem mech_rotate {m : ℕ} (hm : 0 < m) (A l i : ℕ) :
    (mech A m l).rotate i = mech A m ((l + i * A) % m) := by
  apply List.ext_getElem
  · simp [mech_length]
  · intro k hk₁ hk₂
    rw [List.getElem_rotate]
    simp only [mech, diffWord, List.getElem_map, List.getElem_range, List.length_map,
      List.length_range]
    have e1 : ((k + i) % m + 1) * A + l = (k + i) % m * A + l + A := by ring
    have e2 : (k + 1) * A + (l + i * A) % m = k * A + (l + i * A) % m + A := by ring
    rw [e1, e2]
    apply step_congr hm
    have h1 : (k + i) % m * A + l ≡ (k + i) * A + l [MOD m] :=
      ((Nat.mod_modEq (k + i) m).mul_right A).add_right l
    have h2 : k * A + (l + i * A) % m ≡ k * A + (l + i * A) [MOD m] :=
      (Nat.mod_modEq (l + i * A) m).add_left (k * A)
    have e3 : (k + i) * A + l = k * A + (l + i * A) := by ring
    have h2' : (k + i) * A + l ≡ k * A + (l + i * A) % m [MOD m] := by
      rw [e3]; exact h2.symm
    exact h1.trans h2'

/-- **C004 §3, reverse direction.** Every rotation of the mechanical word has its intercept in
`[C_0, 2 C_0)` and the common `D = 2^A − 3^m`; so, when `D > 0`, all states `C_i/D` of the
mechanical cycle lie in `[L, 2L)` with `L = C_0/D`: a mechanical cycle is narrow, `H < 2L`.
No coprimality of `A` and `m` is needed for the inequalities. -/
theorem narrow_mech {m : ℕ} (hm : 0 < m) (A i : ℕ) :
    C (mech A m 0) ≤ C ((mech A m 0).rotate i)
      ∧ C ((mech A m 0).rotate i) < 2 * C (mech A m 0)
      ∧ D ((mech A m 0).rotate i) = 2 ^ A - 3 ^ m := by
  rw [mech_rotate hm A 0 i]
  have hl : (0 + i * A) % m < m := Nat.mod_lt _ hm
  exact ⟨C_mech_zero_le hm A _ hl, C_mech_lt_two hm A _ hl, D_mech hm A _ hl⟩

/-- The `d = 5` control: `mech 5 3 0 = (1,2,2)`, rotations `(2,2,1)`, `(2,1,2)`, intercepts
`23, 37, 29` (C004's table), `37 < 2 · 23`. -/
example : mech 5 3 0 = [1, 2, 2] ∧ (mech 5 3 0).rotate 1 = [2, 2, 1] ∧
    (mech 5 3 0).rotate 2 = [2, 1, 2] := by decide

example : C [1, 2, 2] = 23 ∧ C [2, 2, 1] = 37 ∧ C [2, 1, 2] = 29 ∧ D [1, 2, 2] = 5 := by
  norm_num [C, D]

/-! ### Toward C004's forward direction (narrow ⇒ mechanical), part 1: the cyclic recursion
(1) on rotations, abstract narrow cycles, the exponent dichotomy, successor order and the
rank-shift lemmas of `ROTATION_LATTICE.md` §3 -/

/-- C004's (1) in cons form: `2^a C(v ++ [a]) = 3 C(a :: v) + D(a :: v)`. -/
theorem C_cons_rotate (a : ℕ) (v : List ℕ) :
    (2 : ℤ) ^ a * C (v ++ [a]) = 3 * C (a :: v) + D (a :: v) := by
  rw [C_append]
  simp only [C, D, List.sum_cons, List.length_cons, List.length_nil, pow_succ, pow_add, pow_zero,
    one_mul, mul_zero, add_zero]
  ring

theorem D_rotate (w : List ℕ) (i : ℕ) : D (w.rotate i) = D w := by
  simp only [D, (List.rotate_perm w i).sum_eq, List.length_rotate]

/-- C004's (1) on rotations: if `w.rotate i = a :: v` then `2^a C_{i+1} = 3 C_i + D_w`. -/
theorem C_rotate_succ {w : List ℕ} {i a : ℕ} {v : List ℕ} (h : w.rotate i = a :: v) :
    (2 : ℤ) ^ a * C (w.rotate (i + 1)) = 3 * C (w.rotate i) + D w := by
  have h1 : w.rotate (i + 1) = v ++ [a] := by
    rw [← List.rotate_rotate, h, List.rotate_cons_succ, List.rotate_zero]
  rw [h1, h, ← D_rotate w i, h]
  exact C_cons_rotate a v

/-! ### C009: exact excursion cuts and the elimination `D x = q C`

C009 (`EXCURSION_ARITHMETIC.md` §§1–2) takes a positive valuation word `w` of length `ℓ`, total
`a = Σ w`, prefix totals `P_j = Σ (take j w)` and prefix intercepts `C_j = C (take j w)`, and
positive odd integers `q, x, y` with the exact endpoint relation `2^a y = 3^ℓ x + q C_w`. The
cut states `u_j = (3^j x + q C_j)/2^{P_j}` are then positive odd integers with `u_0 = x`,
`u_ℓ = y` and the exact arrows `2^{a_j} u_{j+1} = 3 u_j + q`: no internal odd-only cylinder is
lost by passing to the endpoint relation. Oddness of `x` is a consequence, not a hypothesis. -/

/-- `C_w = 3^{ℓ−j} C_j + 2^{P_j} C_tail` (composition of the prefix and the tail). -/
theorem C_take_drop (w : List ℕ) (j : ℕ) :
    C w = 3 ^ (w.drop j).length * C (w.take j) + 2 ^ (w.take j).sum * C (w.drop j) := by
  rw [← C_append, List.take_append_drop]

/-- `Σ w = P_j + Σ tail`. -/
theorem sum_take_drop (w : List ℕ) (j : ℕ) : w.sum = (w.take j).sum + (w.drop j).sum := by
  rw [← List.sum_append, List.take_append_drop]

/-- The integrality step of C009's cut lemma: reducing the endpoint relation modulo `2^{P_j}`
and cancelling the unit `3^{ℓ−j}` gives `2^{P_j} ∣ 3^j x + q C_j`. -/
theorem cut_dvd (w : List ℕ) {q x y : ℤ} (h : 2 ^ w.sum * y = 3 ^ w.length * x + q * C w)
    {j : ℕ} (hj : j ≤ w.length) :
    (2 : ℤ) ^ (w.take j).sum ∣ 3 ^ j * x + q * C (w.take j) := by
  have hsplit := C_take_drop w j
  have hsum := sum_take_drop w j
  have hlen : w.length = j + (w.drop j).length := by rw [List.length_drop]; omega
  have hcop : IsCoprime ((2 : ℤ) ^ (w.take j).sum) (3 ^ (w.drop j).length) :=
    (Int.isCoprime_iff_gcd_eq_one.mpr (by norm_num)).pow
  apply hcop.dvd_of_dvd_mul_left
  refine ⟨2 ^ (w.drop j).sum * y - q * C (w.drop j), ?_⟩
  rw [hlen, hsum, hsplit] at h
  linear_combination (-1 : ℤ) * h

/-- The cut states `u_j = (3^j x + q C_j)/2^{P_j}` of C009's lemma. -/
def cutState (w : List ℕ) (q x : ℤ) (j : ℕ) : ℤ :=
  (3 ^ j * x + q * C (w.take j)) / 2 ^ (w.take j).sum

/-- `2^{P_j} u_j = 3^j x + q C_j`: the cut state is an integer. -/
theorem cutState_spec (w : List ℕ) {q x y : ℤ}
    (h : 2 ^ w.sum * y = 3 ^ w.length * x + q * C w) {j : ℕ} (hj : j ≤ w.length) :
    2 ^ (w.take j).sum * cutState w q x j = 3 ^ j * x + q * C (w.take j) :=
  Int.mul_ediv_cancel' (cut_dvd w h hj)

theorem cutState_zero (w : List ℕ) (q x : ℤ) : cutState w q x 0 = x := by
  simp [cutState, C]

theorem cutState_last (w : List ℕ) {q x y : ℤ}
    (h : 2 ^ w.sum * y = 3 ^ w.length * x + q * C w) : cutState w q x w.length = y := by
  have hs := cutState_spec w h (le_refl w.length)
  rw [List.take_length] at hs
  exact mul_left_cancel₀ (pow_ne_zero _ two_ne_zero) (hs.trans h.symm)

/-- The exact arrow `2^{a_j} u_{j+1} = 3 u_j + q` between consecutive cut states. -/
theorem cutState_arrow (w : List ℕ) {q x y : ℤ}
    (h : 2 ^ w.sum * y = 3 ^ w.length * x + q * C w) {j : ℕ} (hj : j < w.length) :
    2 ^ w[j] * cutState w q x (j + 1) = 3 * cutState w q x j + q := by
  have h1 := cutState_spec w h hj.le
  have h2 := cutState_spec w h (show j + 1 ≤ w.length from hj)
  rw [List.take_succ_eq_append_getElem hj, List.sum_append, C_append] at h2
  simp only [List.sum_cons, List.sum_nil, add_zero, List.length_singleton, List.length_nil,
    pow_one, pow_zero, C, mul_zero, mul_one] at h2
  apply mul_left_cancel₀ (pow_ne_zero (w.take j).sum (two_ne_zero : (2 : ℤ) ≠ 0))
  linear_combination h2 - 3 * h1

/-- Positivity of the cut states (`q, x > 0`). -/
theorem cutState_pos (w : List ℕ) {q x y : ℤ} (hq : 0 < q) (hx : 0 < x)
    (h : 2 ^ w.sum * y = 3 ^ w.length * x + q * C w) {j : ℕ} (hj : j ≤ w.length) :
    0 < cutState w q x j := by
  have hs := cutState_spec w h hj
  have hC := C_nonneg (w.take j)
  have h3 : (0 : ℤ) < 3 ^ j * x := mul_pos (by positivity) hx
  have hqC : 0 ≤ q * C (w.take j) := mul_nonneg hq.le hC
  have h2 : (0 : ℤ) < 2 ^ (w.take j).sum := by positivity
  have hpos : 0 < 2 ^ (w.take j).sum * cutState w q x j := by rw [hs]; linarith
  exact (mul_pos_iff_of_pos_left h2).mp hpos

/-- Oddness of the cut states: `u_ℓ = y` is odd, and for `j < ℓ` the arrow
`2^{a_j} u_{j+1} = 3 u_j + q` has an even left side (`a_j ≥ 1`) and odd `q`, so `u_j` is odd. -/
theorem cutState_odd (w : List ℕ) (hw : ∀ a ∈ w, 1 ≤ a) {q x y : ℤ} (hq : Odd q) (hy : Odd y)
    (h : 2 ^ w.sum * y = 3 ^ w.length * x + q * C w) {j : ℕ} (hj : j ≤ w.length) :
    Odd (cutState w q x j) := by
  rcases Nat.lt_or_ge j w.length with hlt | hge
  · have harrow := cutState_arrow w h hlt
    have ha : 1 ≤ w[j] := hw _ (List.getElem_mem hlt)
    have heven : Even (2 ^ w[j] * cutState w q x (j + 1)) :=
      even_iff_two_dvd.mpr (dvd_mul_of_dvd_left (dvd_pow_self 2 (by omega)) _)
    rw [harrow] at heven
    have hq' : ¬ Even q := Int.not_even_iff_odd.mpr hq
    have h3 : Odd (3 * cutState w q x j) :=
      Int.not_even_iff_odd.mp (fun he => hq' ((Int.even_add.mp heven).mp he))
    exact (Int.odd_mul.mp h3).2
  · rw [le_antisymm hj hge, cutState_last w h]
    exact hy

/-- **C009's cut lemma** (`EXCURSION_ARITHMETIC.md` §1). For a positive word `w` of length `ℓ`,
total `a` and intercept `C_w`, and integers `q > 0` odd, `x > 0`, `y` odd with
`2^a y = 3^ℓ x + q C_w`, the cut states `u_j` (`j ≤ ℓ`) satisfy `u_0 = x`, `u_ℓ = y`,
`2^{P_j} u_j = 3^j x + q C_j`, are positive odd integers, and obey the exact arrows
`2^{a_j} u_{j+1} = 3 u_j + q`. (Oddness of the next state is the exactness of the valuation.) -/
theorem cut_lemma (w : List ℕ) (hw : ∀ a ∈ w, 1 ≤ a) {q x y : ℤ} (hq0 : 0 < q) (hq : Odd q)
    (hx0 : 0 < x) (hy : Odd y) (h : 2 ^ w.sum * y = 3 ^ w.length * x + q * C w) :
    cutState w q x 0 = x ∧ cutState w q x w.length = y ∧
    (∀ j, j ≤ w.length →
      2 ^ (w.take j).sum * cutState w q x j = 3 ^ j * x + q * C (w.take j)) ∧
    (∀ j, j ≤ w.length → 0 < cutState w q x j ∧ Odd (cutState w q x j)) ∧
    (∀ j, (hj : j < w.length) →
      2 ^ w[j] * cutState w q x (j + 1) = 3 * cutState w q x j + q) :=
  ⟨cutState_zero w q x, cutState_last w h, fun _ hj => cutState_spec w h hj,
    fun _ hj => ⟨cutState_pos w hq0 hx0 h hj, cutState_odd w hw hq hy h hj⟩,
    fun _ hj => cutState_arrow w h hj⟩

/-- C009's (3): eliminating `y` from the endpoint equations of an excursion `E` and its
complement `P` gives `D x = q C` with `D = D_{EP} = 2^{a+b} − 3^{ℓ+r}` and
`C = C_{EP} = 3^r C_E + 2^a C_P`, the intercept of the full word based at `x`. -/
theorem elimination (E P : List ℕ) {q x y : ℤ}
    (hE : 2 ^ E.sum * y = 3 ^ E.length * x + q * C E)
    (hP : 2 ^ P.sum * x = 3 ^ P.length * y + q * C P) :
    D (E ++ P) * x = q * C (E ++ P) ∧
      C (E ++ P) = 3 ^ P.length * C E + 2 ^ E.sum * C P := by
  refine ⟨?_, C_append E P⟩
  rw [D, List.sum_append, List.length_append, C_append]
  linear_combination 2 ^ E.sum * hP + 3 ^ P.length * hE

/-- At `q = 1` an integer solution of the cycle equation forces `D_w ∣ C_w` (C009 §2,
necessity). -/
theorem D_dvd_C_of_cycle {w : List ℕ} {x : ℤ}
    (h : 2 ^ w.sum * x = 3 ^ w.length * x + C w) : D w ∣ C w :=
  ⟨x, by rw [D]; linear_combination (-1 : ℤ) * h⟩

/-- `D_w` is coprime to `2` (it is odd). -/
theorem isCoprime_two_D {w : List ℕ} (hw : 1 ≤ w.sum) : IsCoprime (2 : ℤ) (D w) := by
  rw [Int.isCoprime_iff_gcd_eq_one]
  have h1 : Int.gcd 2 (D w) ∣ 2 := by
    have := Int.gcd_dvd_left (2 : ℤ) (D w)
    exact_mod_cast this
  rcases (Nat.dvd_prime Nat.prime_two).mp h1 with h | h
  · exact h
  · exfalso
    apply D_odd hw
    have := Int.gcd_dvd_right (2 : ℤ) (D w)
    rw [h] at this
    exact_mod_cast this

/-- The rotation recurrence `2^{a_i} C_{(i+1)} = 3 C_{(i)} + D` propagates `D ∣ C_{(i)}` to
every phase (C009 §2; `D` is odd). -/
theorem dvd_C_rotate {w : List ℕ} (hw0 : w ≠ []) (hw : ∀ a ∈ w, 1 ≤ a) (hdvd : D w ∣ C w) :
    ∀ i, D w ∣ C (w.rotate i) := by
  intro i
  induction i with
  | zero => simpa using hdvd
  | succ i ih =>
    obtain ⟨a, v, hav⟩ : ∃ a v, w.rotate i = a :: v := by
      cases hrot : w.rotate i with
      | nil => exact absurd (List.rotate_eq_nil_iff.mp hrot) hw0
      | cons a v => exact ⟨a, v, rfl⟩
    have hrec := C_rotate_succ hav
    have h2 : D w ∣ 2 ^ a * C (w.rotate (i + 1)) := by
      rw [hrec]
      exact dvd_add (dvd_mul_of_dvd_right ih 3) dvd_rfl
    have hcop : IsCoprime (D w) (2 ^ a) :=
      (isCoprime_two_D (one_le_sum_of_ne_nil hw0 hw)).symm.pow_right
    exact hcop.dvd_of_dvd_mul_left h2

/-- Every phase quotient `C_{(i)}/D` is odd when `D ∣ C` (C009 §2). -/
theorem odd_quot_rotate {w : List ℕ} (hw0 : w ≠ []) (hw : ∀ a ∈ w, 1 ≤ a) (hdvd : D w ∣ C w)
    (i : ℕ) : Odd (C (w.rotate i) / D w) := by
  have hd := dvd_C_rotate hw0 hw hdvd i
  have hrot0 : w.rotate i ≠ [] := fun h => hw0 (List.rotate_eq_nil_iff.mp h)
  have hrotpos : ∀ a ∈ w.rotate i, 1 ≤ a := fun a ha => hw a (List.mem_rotate.mp ha)
  have hodd := C_odd hrot0 hrotpos
  rw [← Int.mul_ediv_cancel' hd] at hodd
  exact (Int.odd_mul.mp hodd).2

/-- C009 §2 at `q = 1`, sufficiency: if `D_w > 0` and `D_w x = C_w` for a positive word `w`,
then `x` is a positive odd integer closing the cycle equation `2^A x = 3^m x + 1 · C_w`. -/
theorem integer_cycle_of_dvd (w : List ℕ) (hw0 : w ≠ []) (hw : ∀ a ∈ w, 1 ≤ a) (hD : 0 < D w)
    {x : ℤ} (hx : D w * x = C w) :
    0 < x ∧ Odd x ∧ 2 ^ w.sum * x = 3 ^ w.length * x + 1 * C w := by
  have hC := C_pos hw0
  have hCodd := C_odd hw0 hw
  refine ⟨?_, ?_, ?_⟩
  · have hDx : 0 < D w * x := by rw [hx]; exact hC
    exact (mul_pos_iff_of_pos_left hD).mp hDx
  · rw [← hx] at hCodd
    exact (Int.odd_mul.mp hCodd).2
  · rw [D] at hx
    linear_combination hx

/-- C009 §2 at `q = 1`: `D_w ∣ C_w` (with `D_w > 0`, positive `w`) yields the odd integer cycle
through `x = C_w/D_w`, with every cut state a positive odd integer and every arrow exact —
the cut lemma recovers all the internal cylinders. -/
theorem cylinders_of_dvd (w : List ℕ) (hw0 : w ≠ []) (hw : ∀ a ∈ w, 1 ≤ a) (hD : 0 < D w)
    {x : ℤ} (hx : D w * x = C w) :
    cutState w 1 x 0 = x ∧ cutState w 1 x w.length = x ∧
    (∀ j, j ≤ w.length → 0 < cutState w 1 x j ∧ Odd (cutState w 1 x j)) ∧
    (∀ j, (hj : j < w.length) →
      2 ^ w[j] * cutState w 1 x (j + 1) = 3 * cutState w 1 x j + 1) := by
  obtain ⟨hx0, hxodd, hcyc⟩ := integer_cycle_of_dvd w hw0 hw hD hx
  obtain ⟨h0, hl, -, hpo, harr⟩ := cut_lemma w hw one_pos odd_one hx0 hxodd hcyc
  exact ⟨h0, hl, hpo, harr⟩

/-- The exponent `q` of C004 §3 exists: `2^q lo ≤ 3 lo + d < 2^{q+1} lo`. -/
theorem exists_exponent {lo d : ℤ} (hlo : 0 < lo) (hd : 0 < d) :
    ∃ q : ℕ, (2 : ℤ) ^ q * lo ≤ 3 * lo + d ∧ 3 * lo + d < 2 ^ (q + 1) * lo := by
  classical
  have hex : ∃ n : ℕ, 3 * lo + d < 2 ^ (n + 1) * lo := by
    obtain ⟨n, hn⟩ := pow_unbounded_of_one_lt (3 * lo + d) (by norm_num : (1 : ℤ) < 2)
    refine ⟨n, ?_⟩
    have h1 : (2 : ℤ) ^ n ≤ 2 ^ (n + 1) := pow_le_pow_right₀ (by norm_num) (Nat.le_succ n)
    have h2 : (2 : ℤ) ^ (n + 1) ≤ 2 ^ (n + 1) * lo :=
      le_mul_of_one_le_right (by positivity) (by linarith)
    linarith
  refine ⟨Nat.find hex, ?_, Nat.find_spec hex⟩
  rcases Nat.eq_zero_or_pos (Nat.find hex) with h0 | hpos
  · rw [h0, pow_zero, one_mul]; linarith
  · have hmin := Nat.find_min hex (Nat.sub_lt hpos Nat.one_pos)
    rw [Nat.sub_add_cancel hpos] at hmin
    exact not_lt.mp hmin

/-- The exponent dichotomy of C004 §3: if the states `x, y` of an arrow `2^a y = 3x + d` lie in
`[lo, 2 lo)` and `2^q lo ≤ 3 lo + d < 2^{q+1} lo`, then `a = q` exactly when
`3x + d < 2^{q+1} lo`, and `a = q + 1` exactly when `2^{q+1} lo ≤ 3x + d`. -/
theorem exponent_dichotomy {lo d x y : ℤ} {a q : ℕ} (hd : 0 < d) (hx : lo ≤ x) (hx2 : x < 2 * lo)
    (hy : lo ≤ y) (hy2 : y < 2 * lo) (harrow : (2 : ℤ) ^ a * y = 3 * x + d)
    (hq1 : (2 : ℤ) ^ q * lo ≤ 3 * lo + d) (hq2 : 3 * lo + d < 2 ^ (q + 1) * lo) :
    (a = q ∧ 3 * x + d < 2 ^ (q + 1) * lo) ∨ (a = q + 1 ∧ 2 ^ (q + 1) * lo ≤ 3 * x + d) := by
  have hlo : 0 < lo := by linarith
  have h2a : (0 : ℤ) < 2 ^ a := by positivity
  rcases lt_trichotomy a q with hlt | heq | hgt
  · exfalso
    have h1 : (2 : ℤ) ^ (a + 1) ≤ 2 ^ q := pow_le_pow_right₀ (by norm_num) hlt
    rw [pow_succ] at h1
    nlinarith [mul_lt_mul_of_pos_left hy2 h2a, mul_le_mul_of_nonneg_right h1 hlo.le]
  · subst heq
    left
    refine ⟨rfl, ?_⟩
    rw [pow_succ]
    nlinarith [mul_lt_mul_of_pos_left hy2 h2a]
  · rcases Nat.lt_or_ge (q + 1) a with hgt2 | hle
    · exfalso
      have h1 : (2 : ℤ) ^ (q + 2) ≤ 2 ^ a := pow_le_pow_right₀ (by norm_num) hgt2
      rw [pow_add] at h1
      rw [pow_succ] at hq2
      nlinarith [mul_le_mul_of_nonneg_left hy h2a.le, mul_le_mul_of_nonneg_right h1 hlo.le]
    · have ha : a = q + 1 := le_antisymm hle hgt
      subst ha
      right
      refine ⟨rfl, ?_⟩
      nlinarith [mul_le_mul_of_nonneg_left hy h2a.le]

/-- Successors of two states with the same exponent compare as the states. -/
theorem succ_order_same {d x x' y y' : ℤ} {a : ℕ} (harrow : (2 : ℤ) ^ a * y = 3 * x + d)
    (harrow' : (2 : ℤ) ^ a * y' = 3 * x' + d) : y < y' ↔ x < x' := by
  have h2a : (0 : ℤ) < 2 ^ a := by positivity
  constructor
  · intro h; nlinarith [mul_lt_mul_of_pos_left h h2a]
  · intro h; exact lt_of_mul_lt_mul_left (by linarith) h2a.le

/-- A high-exponent successor lies below every low-exponent successor (narrow states). -/
theorem succ_order_high_low {lo d x x' y y' : ℤ} {q : ℕ} (hd : 0 < d) (hx2 : x < 2 * lo)
    (hx' : lo ≤ x') (harrow : (2 : ℤ) ^ (q + 1) * y = 3 * x + d)
    (harrow' : (2 : ℤ) ^ q * y' = 3 * x' + d) : y < y' := by
  have h2q : (0 : ℤ) < 2 ^ q := by positivity
  rw [pow_succ] at harrow
  have h : (2 : ℤ) ^ q * 2 * y < 2 ^ q * 2 * y' := by linarith
  exact lt_of_mul_lt_mul_left h (by positivity)

/-- The exponent dichotomy in image form: if `y ∈ [lo, 2 lo)`, `2^a y = F` and
`2^q lo ≤ F < 2^{q+2} lo`, then `a = q` exactly when `F < 2^{q+1} lo`, and `a = q + 1` exactly
when `2^{q+1} lo ≤ F`. -/
theorem exponent_dichotomy_F {lo F y : ℤ} {a q : ℕ} (hy : lo ≤ y) (hy2 : y < 2 * lo)
    (harrow : (2 : ℤ) ^ a * y = F) (hq1 : (2 : ℤ) ^ q * lo ≤ F) (hq2 : F < 2 ^ (q + 2) * lo) :
    (a = q ∧ F < 2 ^ (q + 1) * lo) ∨ (a = q + 1 ∧ 2 ^ (q + 1) * lo ≤ F) := by
  have hlo : 0 < lo := by linarith
  have h2a : (0 : ℤ) < 2 ^ a := by positivity
  rcases lt_trichotomy a q with hlt | heq | hgt
  · exfalso
    have h1 : (2 : ℤ) ^ (a + 1) ≤ 2 ^ q := pow_le_pow_right₀ (by norm_num) hlt
    rw [pow_succ] at h1
    nlinarith [mul_lt_mul_of_pos_left hy2 h2a, mul_le_mul_of_nonneg_right h1 hlo.le]
  · subst heq
    left
    refine ⟨rfl, ?_⟩
    rw [pow_succ]
    nlinarith [mul_lt_mul_of_pos_left hy2 h2a]
  · rcases Nat.lt_or_ge (q + 1) a with hgt2 | hle
    · exfalso
      have h1 : (2 : ℤ) ^ (q + 2) ≤ 2 ^ a := pow_le_pow_right₀ (by norm_num) hgt2
      nlinarith [mul_le_mul_of_nonneg_left hy h2a.le, mul_le_mul_of_nonneg_right h1 hlo.le]
    · have ha : a = q + 1 := le_antisymm hle hgt
      subst ha
      right
      refine ⟨rfl, ?_⟩
      nlinarith [mul_le_mul_of_nonneg_left hy h2a.le]

/-- Abstract data of an ordered, dyadically normalised cycle of period `m` (C004 §3 with a
constant offset; C005's order lemma in general): states `x i`, periodic mod `m`, all in
`[lo, 2 lo)`; exponents `a i` with the arrows `2^{a i} x(i+1) = F i`, where the images `F i`
are strictly increasing in the states (`x i < x j ↔ F i < F j`) and lie in a factor-two window
(`F i < 2 F j`); and an exponent `q` with `2^q lo ≤ F i < 2^{q+2} lo`. For C004,
`F i = 3 x i + d`; for C005, `F i = 3 z_i + q/2^{h_i}` after scaling to integers. -/
structure NarrowCycle (m : ℕ) where
  x : ℕ → ℤ
  a : ℕ → ℕ
  F : ℕ → ℤ
  lo : ℤ
  q : ℕ
  hm : 0 < m
  periodic : ∀ i, x (i + m) = x i
  arrow : ∀ i, (2 : ℤ) ^ a i * x (i + 1) = F i
  lower : ∀ i, lo ≤ x i
  upper : ∀ i, x i < 2 * lo
  order : ∀ i j, x i < x j ↔ F i < F j
  window : ∀ i j, F i < 2 * F j
  hq1 : ∀ i, (2 : ℤ) ^ q * lo ≤ F i
  hq2 : ∀ i, F i < 2 ^ (q + 2) * lo

namespace NarrowCycle

variable {m : ℕ} (N : NarrowCycle m)

theorem lo_pos : 0 < N.lo := by
  have h1 := N.lower 0
  have h2 := N.upper 0
  linarith

theorem F_eq_of_x_eq {i j : ℕ} (h : N.x i = N.x j) : N.F i = N.F j := by
  have h1 : ¬ N.F i < N.F j := fun hlt => by
    have := (N.order i j).mpr hlt
    rw [h] at this
    exact lt_irrefl _ this
  have h2 : ¬ N.F j < N.F i := fun hlt => by
    have := (N.order j i).mpr hlt
    rw [h] at this
    exact lt_irrefl _ this
  exact le_antisymm (not_lt.mp h2) (not_lt.mp h1)

/-- Index `i` is *high* when its arrow has exponent `q + 1`. -/
def high (i : ℕ) : Prop := 2 ^ (N.q + 1) * N.lo ≤ N.F i

instance decHigh (i : ℕ) : Decidable (N.high i) :=
  inferInstanceAs (Decidable (2 ^ (N.q + 1) * N.lo ≤ N.F i))

/-- The exponent dichotomy on the cycle. -/
theorem a_eq (i : ℕ) : N.a i = if N.high i then N.q + 1 else N.q := by
  have hdi := exponent_dichotomy_F (N.lower (i + 1)) (N.upper (i + 1)) (N.arrow i) (N.hq1 i)
    (N.hq2 i)
  split_ifs with hc
  · rcases hdi with ⟨_, h2⟩ | ⟨h1, _⟩
    · exact absurd hc (not_le.mpr h2)
    · exact h1
  · rcases hdi with ⟨h1, _⟩ | ⟨_, h2⟩
    · exact h1
    · exact absurd h2 hc

theorem a_of_low {i : ℕ} (hi : ¬ N.high i) : N.a i = N.q := by rw [N.a_eq, ite_eq_right hi]

theorem a_of_high {i : ℕ} (hi : N.high i) : N.a i = N.q + 1 := by rw [N.a_eq, ite_eq_left hi]

/-- Low states lie below high states. -/
theorem x_lt_of_low_high {i j : ℕ} (hi : ¬ N.high i) (hj : N.high j) : N.x i < N.x j := by
  have hi' : N.F i < 2 ^ (N.q + 1) * N.lo := by simpa [high, not_le] using hi
  have hj' : 2 ^ (N.q + 1) * N.lo ≤ N.F j := hj
  exact (N.order i j).mpr (lt_of_lt_of_le hi' hj')

/-- Successors of two states with the same exponent compare as the states. -/
theorem succ_lt_iff_of_a_eq {i j : ℕ} (h : N.a i = N.a j) :
    N.x (i + 1) < N.x (j + 1) ↔ N.x i < N.x j := by
  have h1 := N.arrow i
  have h2 := N.arrow j
  rw [h] at h1
  have h2a : (0 : ℤ) < 2 ^ N.a j := by positivity
  rw [N.order i j, ← h1, ← h2]
  exact ⟨fun hlt => mul_lt_mul_of_pos_left hlt h2a, fun hlt => lt_of_mul_lt_mul_left hlt h2a.le⟩

theorem succ_lt_iff_low {i j : ℕ} (hi : ¬ N.high i) (hj : ¬ N.high j) :
    N.x (i + 1) < N.x (j + 1) ↔ N.x i < N.x j :=
  N.succ_lt_iff_of_a_eq (by rw [N.a_of_low hi, N.a_of_low hj])

theorem succ_lt_iff_high {i j : ℕ} (hi : N.high i) (hj : N.high j) :
    N.x (i + 1) < N.x (j + 1) ↔ N.x i < N.x j :=
  N.succ_lt_iff_of_a_eq (by rw [N.a_of_high hi, N.a_of_high hj])

/-- A high-exponent successor lies below every low-exponent successor (the factor-two window). -/
theorem succ_lt_of_high_low {i j : ℕ} (hi : N.high i) (hj : ¬ N.high j) :
    N.x (i + 1) < N.x (j + 1) := by
  have h1 := N.arrow i
  have h2 := N.arrow j
  rw [N.a_of_high hi, pow_succ] at h1
  rw [N.a_of_low hj] at h2
  have hw := N.window i j
  have h2q : (0 : ℤ) < 2 ^ N.q := by positivity
  have h : (2 : ℤ) ^ N.q * 2 * N.x (i + 1) < 2 ^ N.q * 2 * N.x (j + 1) := by linarith
  exact lt_of_mul_lt_mul_left h (by positivity)

/-- Shifting the summation index once around the cycle. -/
theorem sum_range_shift (f : ℕ → ℕ) (hf : f m = f 0) :
    ∑ j ∈ Finset.range m, f (j + 1) = ∑ j ∈ Finset.range m, f j := by
  have h1 := Finset.sum_range_succ f m
  have h2 := Finset.sum_range_succ' f m
  omega

theorem x_add_mul (n k : ℕ) : N.x (n + m * k) = N.x n := by
  induction k with
  | zero => simp
  | succ k ih => rw [Nat.mul_succ, ← Nat.add_assoc, N.periodic, ih]

theorem x_mod (i : ℕ) : N.x (i % m) = N.x i := by
  conv_rhs => rw [← Nat.mod_add_div i m]
  exact (N.x_add_mul _ _).symm

theorem x_m : N.x m = N.x 0 := by simpa using N.periodic 0

/-- The rank of index `i`: the number of indices `j < m` whose state lies below `x i`. -/
def rank (i : ℕ) : ℕ := ∑ j ∈ Finset.range m, if N.x j < N.x i then 1 else 0

/-- The number of high indices among `0, …, m − 1` (C004's `h`). -/
def numHigh : ℕ := ∑ j ∈ Finset.range m, if N.high j then 1 else 0

theorem numHigh_add_low :
    N.numHigh + (∑ j ∈ Finset.range m, if N.high j then 0 else 1) = m := by
  unfold numHigh
  rw [← Finset.sum_add_distrib]
  calc (∑ j ∈ Finset.range m, ((if N.high j then 1 else 0) + if N.high j then 0 else 1))
      = ∑ j ∈ Finset.range m, 1 := Finset.sum_congr rfl (fun j _ => by split_ifs <;> omega)
    _ = m := by simp

theorem numHigh_le : N.numHigh ≤ m := by
  have := N.numHigh_add_low
  omega

theorem sum_low : (∑ j ∈ Finset.range m, if N.high j then 0 else 1) = m - N.numHigh := by
  have := N.numHigh_add_low
  omega

theorem rank_succ (i : ℕ) :
    N.rank (i + 1) = ∑ j ∈ Finset.range m, if N.x (j + 1) < N.x (i + 1) then 1 else 0 := by
  unfold rank
  exact (sum_range_shift (fun j => if N.x j < N.x (i + 1) then 1 else 0) (by simp [N.x_m])).symm

/-- **C004 §3, rank shift at a low index:** `rank(i+1) = rank(i) + h`. -/
theorem rank_succ_of_low {i : ℕ} (hi : ¬ N.high i) : N.rank (i + 1) = N.rank i + N.numHigh := by
  rw [N.rank_succ, rank, numHigh, ← Finset.sum_add_distrib]
  apply Finset.sum_congr rfl
  intro j _
  by_cases hj : N.high j
  · simp only [ite_eq_left (N.succ_lt_of_high_low hj hi),
      ite_eq_right (not_lt.mpr (N.x_lt_of_low_high hi hj).le), ite_eq_left hj, zero_add]
  · simp only [ite_eq_right hj, add_zero]
    by_cases hx : N.x j < N.x i
    · simp only [ite_eq_left hx, ite_eq_left ((N.succ_lt_iff_low hj hi).mpr hx)]
    · simp only [ite_eq_right hx, ite_eq_right ((fun h => hx ((N.succ_lt_iff_low hj hi).mp h)) :
        ¬ N.x (j + 1) < N.x (i + 1))]

/-- **C004 §3, rank shift at a high index:** `rank(i) = rank(i+1) + (m − h)`. -/
theorem rank_of_high {i : ℕ} (hi : N.high i) : N.rank i = N.rank (i + 1) + (m - N.numHigh) := by
  rw [← N.sum_low, N.rank_succ, rank, ← Finset.sum_add_distrib]
  apply Finset.sum_congr rfl
  intro j _
  by_cases hj : N.high j
  · simp only [ite_eq_left hj, add_zero]
    by_cases hx : N.x j < N.x i
    · simp only [ite_eq_left hx, ite_eq_left ((N.succ_lt_iff_high hj hi).mpr hx)]
    · simp only [ite_eq_right hx, ite_eq_right ((fun h => hx ((N.succ_lt_iff_high hj hi).mp h)) :
        ¬ N.x (j + 1) < N.x (i + 1))]
  · simp only [ite_eq_left (N.x_lt_of_low_high hj hi),
      ite_eq_right (not_lt.mpr (N.succ_lt_of_high_low hi hj).le), ite_eq_right hj, zero_add]

/-- A high index has rank at least `m − h`. -/
theorem rank_ge_of_high {i : ℕ} (hi : N.high i) : m - N.numHigh ≤ N.rank i := by
  rw [← N.sum_low, rank]
  apply Finset.sum_le_sum
  intro j _
  by_cases hj : N.high j
  · simp only [ite_eq_left hj]
    exact Nat.zero_le _
  · simp only [ite_eq_right hj, ite_eq_left (N.x_lt_of_low_high hj hi), le_refl]

/-- A low index `i < m` has rank below `m − h`. -/
theorem rank_lt_of_low {i : ℕ} (hi : i < m) (hlow : ¬ N.high i) : N.rank i < m - N.numHigh := by
  rw [← N.sum_low, rank]
  apply Finset.sum_lt_sum
  · intro j _
    by_cases hj : N.high j
    · have h : ¬ N.x j < N.x i := not_lt.mpr (N.x_lt_of_low_high hlow hj).le
      simp only [ite_eq_right h, ite_eq_left hj, le_refl]
    · simp only [ite_eq_right hj]
      split_ifs <;> omega
  · exact ⟨i, Finset.mem_range.mpr hi, by simp [hlow]⟩

/-- The high indices are exactly the `h` largest ranks. -/
theorem high_iff_rank {i : ℕ} (hi : i < m) : N.high i ↔ m - N.numHigh ≤ N.rank i :=
  ⟨N.rank_ge_of_high, fun h => by
    by_contra hlow
    exact absurd h (not_le.mpr (N.rank_lt_of_low hi hlow))⟩

/-! #### Part 2: the rank formula, `gcd(h, m) = 1` and the letter formula -/

theorem rank_mod (i : ℕ) : N.rank (i % m) = N.rank i := by
  unfold rank
  rw [N.x_mod]

theorem F_mod (i : ℕ) : N.F (i % m) = N.F i := N.F_eq_of_x_eq (N.x_mod i)

theorem high_mod (i : ℕ) : N.high (i % m) ↔ N.high i := by
  unfold high
  rw [N.F_mod]

/-- `rank i < m`: the index `i` itself (reduced mod `m`) is never counted. -/
theorem rank_lt (i : ℕ) : N.rank i < m := by
  unfold rank
  calc (∑ j ∈ Finset.range m, if N.x j < N.x i then 1 else 0)
      < ∑ j ∈ Finset.range m, 1 := by
        apply Finset.sum_lt_sum
        · intro j _
          split_ifs <;> omega
        · refine ⟨i % m, Finset.mem_range.mpr (Nat.mod_lt _ N.hm), ?_⟩
          rw [N.x_mod]
          simp
    _ = m := by simp

/-- Ranks are strictly monotone in the states (for a counted index `i < m`). -/
theorem rank_lt_of_lt {i j : ℕ} (hi : i < m) (h : N.x i < N.x j) : N.rank i < N.rank j := by
  unfold rank
  apply Finset.sum_lt_sum
  · intro k _
    split_ifs <;> omega
  · refine ⟨i, Finset.mem_range.mpr hi, ?_⟩
    simp [h]

theorem x_eq_of_rank_eq {i j : ℕ} (hi : i < m) (hj : j < m) (h : N.rank i = N.rank j) :
    N.x i = N.x j := by
  rcases lt_trichotomy (N.x i) (N.x j) with hlt | heq | hgt
  · exact absurd h (ne_of_lt (N.rank_lt_of_lt hi hlt))
  · exact heq
  · exact absurd h.symm (ne_of_lt (N.rank_lt_of_lt hj hgt))

/-- Primitivity (the prose's "primitive state period"): the `m` states are distinct. -/
def Primitive : Prop := ∀ i j, i < m → j < m → N.x i = N.x j → i = j

theorem rank_inj (hp : N.Primitive) {i j : ℕ} (hi : i < m) (hj : j < m)
    (h : N.rank i = N.rank j) : i = j :=
  hp i j hi hj (N.x_eq_of_rank_eq hi hj h)

theorem all_low_of_numHigh_zero (h0 : N.numHigh = 0) (j : ℕ) : ¬ N.high j := by
  intro hj
  have h1 : m - N.numHigh ≤ N.rank j := N.rank_ge_of_high hj
  rw [h0, Nat.sub_zero] at h1
  exact absurd (N.rank_lt j) (not_lt.mpr h1)

theorem all_high_of_numHigh_eq (hm0 : N.numHigh = m) (j : ℕ) : N.high j := by
  by_contra hj
  have h1 := N.rank_lt_of_low (Nat.mod_lt j N.hm) ((not_congr (N.high_mod j)).mpr hj)
  rw [hm0, Nat.sub_self] at h1
  exact Nat.not_lt_zero _ h1

/-- A primitive narrow cycle with `m ≥ 2` has a high index: `h ≥ 1`. -/
theorem numHigh_pos (hp : N.Primitive) (hm2 : 2 ≤ m) : 0 < N.numHigh := by
  rcases Nat.eq_zero_or_pos N.numHigh with h0 | hpos
  · exfalso
    have h01 : N.rank 1 = N.rank 0 + N.numHigh :=
      N.rank_succ_of_low (N.all_low_of_numHigh_zero h0 0)
    rw [h0, Nat.add_zero] at h01
    have := N.rank_inj hp (by omega) (by omega) h01
    omega
  · exact hpos

/-- A primitive narrow cycle with `m ≥ 2` has a low index: `h ≤ m − 1`. -/
theorem numHigh_lt (hp : N.Primitive) (hm2 : 2 ≤ m) : N.numHigh < m := by
  rcases Nat.lt_or_ge N.numHigh m with h | h
  · exact h
  · exfalso
    have hm0 : N.numHigh = m := le_antisymm N.numHigh_le h
    have h01 : N.rank 0 = N.rank 1 + (m - N.numHigh) :=
      N.rank_of_high (N.all_high_of_numHigh_eq hm0 0)
    rw [hm0, Nat.sub_self, Nat.add_zero] at h01
    have := N.rank_inj hp (by omega) (by omega) h01
    omega

/-- The rank shift in one formula: `rank(i+1) = (rank i + h) mod m`. -/
theorem rank_succ_eq (hh : N.numHigh < m) (i : ℕ) :
    N.rank (i + 1) = (N.rank i + N.numHigh) % m := by
  by_cases hi : N.high i
  · have h1 := N.rank_of_high hi
    have h2 : m - N.numHigh ≤ N.rank i := N.rank_ge_of_high hi
    have h3 := N.rank_lt (i + 1)
    rw [Nat.mod_eq_sub_mod (show m ≤ N.rank i + N.numHigh by omega),
      Nat.mod_eq_of_lt (show N.rank i + N.numHigh - m < m by omega)]
    omega
  · rw [N.rank_succ_of_low hi]
    have h1 : N.rank i < m - N.numHigh := by
      have := N.rank_lt_of_low (Nat.mod_lt i N.hm) ((not_congr (N.high_mod i)).mpr hi)
      rwa [N.rank_mod] at this
    rw [Nat.mod_eq_of_lt (show N.rank i + N.numHigh < m by omega)]

/-- **C004 §3:** time `i` has rank `rank 0 + i h mod m`. -/
theorem rank_formula (hh : N.numHigh < m) (i : ℕ) :
    N.rank i = (N.rank 0 + i * N.numHigh) % m := by
  induction i with
  | zero => simp [Nat.mod_eq_of_lt (N.rank_lt 0)]
  | succ i ih =>
    rw [N.rank_succ_eq hh, ih, Nat.mod_add_mod, Nat.add_mul, Nat.one_mul, Nat.add_assoc]

/-- **C004 §3, the letters:** starting at the minimum (`rank 0 = 0`),
`a_i = q + ⌊(i+1)h/m⌋ − ⌊ih/m⌋`. -/
theorem a_formula (hh : N.numHigh < m) (h0 : N.rank 0 = 0) (i : ℕ) :
    N.a i = N.q + (((i + 1) * N.numHigh) / m - (i * N.numHigh) / m) := by
  have hr : N.rank i = (i * N.numHigh) % m := by
    rw [N.rank_formula hh i, h0, Nat.zero_add]
  have hlt : (i * N.numHigh) % m < m := Nat.mod_lt _ N.hm
  have hdiv : ((i + 1) * N.numHigh) / m - (i * N.numHigh) / m
      = ((i * N.numHigh) % m + N.numHigh) / m := by
    rw [Nat.add_mul, Nat.one_mul, step_mod N.hm, Nat.div_eq_of_lt hlt, Nat.sub_zero]
  rw [hdiv, N.a_eq]
  have hiff : N.high i ↔ m - N.numHigh ≤ N.rank i := by
    rw [← N.high_mod, ← N.rank_mod]
    exact N.high_iff_rank (Nat.mod_lt _ N.hm)
  split_ifs with hc
  · have h1 : m ≤ (i * N.numHigh) % m + N.numHigh := by
      have := hiff.mp hc
      omega
    rw [Nat.div_eq_of_lt_le (show 1 * m ≤ (i * N.numHigh) % m + N.numHigh by omega)
      (show (i * N.numHigh) % m + N.numHigh < Nat.succ 1 * m by omega)]
  · have h1 : (i * N.numHigh) % m + N.numHigh < m := by
      have := (not_congr hiff).mp hc
      omega
    rw [Nat.div_eq_of_lt h1, Nat.add_zero]

/-- **C004 §3:** `gcd(h, m) = 1` for a primitive narrow cycle with `m ≥ 2`. -/
theorem coprime_numHigh (hp : N.Primitive) (hm2 : 2 ≤ m) : Nat.Coprime N.numHigh m := by
  have hh := N.numHigh_lt hp hm2
  by_contra hne
  have hg1 : Nat.gcd N.numHigh m ≠ 1 := hne
  have hgpos : 0 < Nat.gcd N.numHigh m := Nat.gcd_pos_of_pos_right _ N.hm
  obtain ⟨m', hm'⟩ := Nat.gcd_dvd_right N.numHigh m
  obtain ⟨h', hh'⟩ := Nat.gcd_dvd_left N.numHigh m
  set g := Nat.gcd N.numHigh m with hg
  have hg2 : 2 ≤ g := by omega
  have hm'pos : 0 < m' := by
    rcases Nat.eq_zero_or_pos m' with h0 | h0
    · rw [h0, Nat.mul_zero] at hm'
      omega
    · exact h0
  have hm'lt : m' < m := by
    rw [hm']
    nlinarith
  have hmul : m' * N.numHigh = m * h' := by
    rw [hh', hm']
    ring
  have hr : N.rank m' = N.rank 0 := by
    rw [N.rank_formula hh m', hmul, Nat.add_mul_mod_self_left, Nat.mod_eq_of_lt (N.rank_lt 0)]
  have := N.rank_inj hp hm'lt N.hm hr
  omega

/-- The total over one period: `A = mq + h`. -/
theorem sum_a : ∑ i ∈ Finset.range m, N.a i = m * N.q + N.numHigh := by
  have h : ∀ i, N.a i = N.q + if N.high i then 1 else 0 := fun i => by
    rw [N.a_eq]
    split_ifs <;> omega
  simp_rw [h]
  rw [Finset.sum_add_distrib, Finset.sum_const, Finset.card_range, smul_eq_mul]
  rfl

/-! #### Part 3: the instance on words and C004 §3's forward direction -/

theorem rotate_ne_nil {w : List ℕ} (hw : w ≠ []) (i : ℕ) : w.rotate i ≠ [] :=
  fun h => hw (List.rotate_eq_nil_iff.mp h)

/-- The first letter of `w.rotate i`, for `i < w.length`, is `w[i]`. -/
theorem headD_rotate (w : List ℕ) {i : ℕ} (hi : i < w.length) :
    (w.rotate i).headD 0 = w[i] := by
  rw [List.rotate_eq_drop_append_take_mod, Nat.mod_eq_of_lt hi, List.drop_eq_getElem_cons hi,
    List.cons_append, List.headD_cons]

/-- The narrow-cycle data of a word `w` with `D_w > 0` that starts at its minimum and is narrow
(`H < 2L`): states `C(w.rotate i)`, letters the first letters of the rotations, images
`3 C(w.rotate i) + D_w` (constant offset), `lo = C_w`, and an exponent `q` with
`2^q C_w ≤ 3 C_w + D_w < 2^{q+1} C_w`. -/
def ofWord (w : List ℕ) (hm : 0 < w.length) (hD : 0 < D w)
    (hmin : ∀ i, C w ≤ C (w.rotate i)) (hnarrow : ∀ i, C (w.rotate i) < 2 * C w) (q : ℕ)
    (hq1 : (2 : ℤ) ^ q * C w ≤ 3 * C w + D w) (hq2 : 3 * C w + D w < 2 ^ (q + 1) * C w) :
    NarrowCycle w.length where
  x i := C (w.rotate i)
  a i := (w.rotate i).headD 0
  F i := 3 * C (w.rotate i) + D w
  lo := C w
  q := q
  hm := hm
  periodic i := by
    show C (w.rotate (i + w.length)) = C (w.rotate i)
    rw [← List.rotate_mod w (i + w.length), Nat.add_mod_right, List.rotate_mod]
  arrow i := by
    show (2 : ℤ) ^ (w.rotate i).headD 0 * C (w.rotate (i + 1)) = 3 * C (w.rotate i) + D w
    obtain ⟨a, v, h⟩ :=
      List.exists_cons_of_ne_nil (rotate_ne_nil (List.ne_nil_of_length_pos hm) i)
    have ha : (w.rotate i).headD 0 = a := by rw [h, List.headD_cons]
    rw [ha]
    exact C_rotate_succ h
  lower := hmin
  upper := hnarrow
  order i j := by
    show C (w.rotate i) < C (w.rotate j) ↔ 3 * C (w.rotate i) + D w < 3 * C (w.rotate j) + D w
    constructor <;> intro h <;> linarith
  window i j := by
    show 3 * C (w.rotate i) + D w < 2 * (3 * C (w.rotate j) + D w)
    have h1 := hnarrow i
    have h2 := hmin j
    linarith
  hq1 i := by
    show (2 : ℤ) ^ q * C w ≤ 3 * C (w.rotate i) + D w
    have := hmin i
    linarith
  hq2 i := by
    show 3 * C (w.rotate i) + D w < 2 ^ (q + 2) * C w
    have h1 := hnarrow i
    have h3 : (2 : ℤ) ^ (q + 2) * C w = 2 * (2 ^ (q + 1) * C w) := by ring
    rw [h3]
    linarith

/-- **C004 §3, forward direction, for a word starting at its minimum.** A word `w` of length
`m ≥ 2` with `D_w > 0` whose `m` rotations have distinct intercepts, all in `[C_w, 2 C_w)`, is
the mechanical word of its own total: `w = mech w.sum m 0`, and `gcd(w.sum, m) = 1`. -/
theorem eq_mech_of_narrow (w : List ℕ) (hm2 : 2 ≤ w.length) (hD : 0 < D w)
    (hmin : ∀ i, C w ≤ C (w.rotate i)) (hnarrow : ∀ i, C (w.rotate i) < 2 * C w)
    (hdist : ∀ i j, i < w.length → j < w.length → C (w.rotate i) = C (w.rotate j) → i = j) :
    w = mech w.sum w.length 0 ∧ Nat.Coprime w.sum w.length := by
  have hm0 : 0 < w.length := by omega
  have hne : w ≠ [] := List.ne_nil_of_length_pos hm0
  obtain ⟨q, hq1, hq2⟩ := exists_exponent (C_pos hne) hD
  set N : NarrowCycle w.length := ofWord w hm0 hD hmin hnarrow q hq1 hq2 with hN
  have hx : ∀ i, N.x i = C (w.rotate i) := fun _ => rfl
  have ha : ∀ i, N.a i = (w.rotate i).headD 0 := fun _ => rfl
  have hq : N.q = q := rfl
  have hp : N.Primitive := by
    unfold NarrowCycle.Primitive
    intro i j hi hj h
    exact hdist i j hi hj h
  have hh := N.numHigh_lt hp hm2
  have h0 : N.rank 0 = 0 := by
    unfold NarrowCycle.rank
    apply Finset.sum_eq_zero
    intro j _
    rw [hx, hx, List.rotate_zero]
    exact ite_eq_right (not_lt.mpr (hmin j))
  have hlet : ∀ i, (hi : i < w.length) →
      w[i] = q + (((i + 1) * N.numHigh) / w.length - (i * N.numHigh) / w.length) := by
    intro i hi
    rw [← headD_rotate w hi, ← ha, N.a_formula hh h0 i, hq]
  have hw : w = mech (w.length * q + N.numHigh) w.length 0 := by
    apply List.ext_getElem
    · simp [mech_length]
    · intro i hi _
      rw [hlet i hi]
      simp only [mech, diffWord, List.getElem_map, List.getElem_range, add_zero]
      have e1 : (i + 1) * (w.length * q + N.numHigh)
          = (i + 1) * N.numHigh + w.length * (q * (i + 1)) := by ring
      have e2 : i * (w.length * q + N.numHigh) = i * N.numHigh + w.length * (q * i) := by ring
      rw [e1, e2, Nat.add_mul_div_left _ _ hm0, Nat.add_mul_div_left _ _ hm0]
      have hmono : (i * N.numHigh) / w.length ≤ ((i + 1) * N.numHigh) / w.length :=
        Nat.div_le_div_right (Nat.mul_le_mul_right _ (Nat.le_succ i))
      rw [Nat.mul_add, Nat.mul_one]
      omega
  have hsum : w.sum = w.length * q + N.numHigh := by
    conv_lhs => rw [hw]
    exact mech_sum hm0 _ _ hm0
  refine ⟨?_, ?_⟩
  · rw [hsum]
    exact hw
  · rw [hsum]
    exact (Nat.coprime_mul_left_add_left N.numHigh w.length q).mpr (N.coprime_numHigh hp hm2)

/-- **C004 §3, forward direction (narrow ⇒ mechanical).** A word `w` of length `m ≥ 2` with
`D_w > 0`, whose `m` rotations have distinct intercepts (a primitive cycle) and which is narrow —
every rotated intercept is below twice every other, i.e. `H < 2L` — is a phase of the
mechanical word of its total: `w = mech w.sum m l` for some `l < m`, and `gcd(w.sum, m) = 1`.
Together with `narrow_mech` this is C004's narrow-cycle equivalence. -/
theorem is_mech_of_narrow (w : List ℕ) (hm2 : 2 ≤ w.length) (hD : 0 < D w)
    (hnarrow : ∀ i j, C (w.rotate i) < 2 * C (w.rotate j))
    (hdist : ∀ i j, i < w.length → j < w.length → C (w.rotate i) = C (w.rotate j) → i = j) :
    ∃ l < w.length, w = mech w.sum w.length l ∧ Nat.Coprime w.sum w.length := by
  have hm0 : 0 < w.length := by omega
  obtain ⟨i₀, hi₀, hmin₀⟩ := Finset.exists_min_image (Finset.range w.length)
    (fun i => C (w.rotate i)) ⟨0, Finset.mem_range.mpr hm0⟩
  rw [Finset.mem_range] at hi₀
  set w' := w.rotate i₀ with hw'
  have hlen : w'.length = w.length := List.length_rotate w i₀
  have hrot : ∀ j, w'.rotate j = w.rotate (i₀ + j) := fun j => List.rotate_rotate w i₀ j
  have hmin : ∀ j, C w' ≤ C (w'.rotate j) := by
    intro j
    rw [hrot, ← List.rotate_mod w (i₀ + j)]
    exact hmin₀ _ (Finset.mem_range.mpr (Nat.mod_lt _ hm0))
  have hnar : ∀ j, C (w'.rotate j) < 2 * C w' := fun j => by
    rw [hrot]
    exact hnarrow _ _
  have hdist' : ∀ i j, i < w'.length → j < w'.length →
      C (w'.rotate i) = C (w'.rotate j) → i = j := by
    intro i j hi hj h
    rw [hlen] at hi hj
    rw [hrot, hrot, ← List.rotate_mod w (i₀ + i), ← List.rotate_mod w (i₀ + j)] at h
    have h1 := hdist _ _ (Nat.mod_lt _ hm0) (Nat.mod_lt _ hm0) h
    have h2 : i % w.length = j % w.length := Nat.ModEq.add_left_cancel' i₀ h1
    rwa [Nat.mod_eq_of_lt hi, Nat.mod_eq_of_lt hj] at h2
  have hD' : 0 < D w' := by
    rw [hw', D_rotate]
    exact hD
  have hm2' : 2 ≤ w'.length := by
    rw [hlen]
    exact hm2
  obtain ⟨hmech, hcop⟩ := eq_mech_of_narrow w' hm2' hD' hmin hnar hdist'
  have hsum : w'.sum = w.sum := (List.rotate_perm w i₀).sum_eq
  rw [hlen, hsum] at hmech hcop
  have hback : w = w'.rotate (w.length - i₀) := by
    rw [hrot, Nat.add_sub_of_le hi₀.le, List.rotate_length]
  refine ⟨(0 + (w.length - i₀) * w.sum) % w.length, Nat.mod_lt _ hm0, ?_, hcop⟩
  conv_lhs => rw [hback]
  rw [hmech, mech_rotate hm0]

/-! #### Part 4: states indexed by rank (C006 §3's sorted order `z_[r]`, its extension
`z_[r+m] = 2 z_[r]` and the sorted gaps) -/

theorem rank_congr {i j : ℕ} (h : N.x i = N.x j) : N.rank i = N.rank j := by
  unfold rank
  simp only [h]

/-- On a primitive cycle the rank is onto `{0, …, m−1}`. -/
theorem exists_rank_eq (hp : N.Primitive) {r : ℕ} (hr : r < m) :
    ∃ i, i < m ∧ N.rank i = r := by
  have hsurj := Finset.surj_on_of_inj_on_of_card_le (s := Finset.range m)
    (t := Finset.range m) (fun i _ => N.rank i)
    (fun i _ => Finset.mem_range.mpr (N.rank_lt i))
    (fun i j hi hj h => N.rank_inj hp (Finset.mem_range.mp hi) (Finset.mem_range.mp hj) h)
    le_rfl
  obtain ⟨i, hi, hri⟩ := hsurj r (Finset.mem_range.mpr hr)
  exact ⟨i, Finset.mem_range.mp hi, hri.symm⟩

open Classical in
/-- The index below `m` of the state of rank `r` (on a primitive cycle). -/
noncomputable def idx (r : ℕ) : ℕ :=
  if h : ∃ i, i < m ∧ N.rank i = r then Classical.choose h else 0

theorem idx_spec (hp : N.Primitive) {r : ℕ} (hr : r < m) :
    N.idx r < m ∧ N.rank (N.idx r) = r := by
  have h := N.exists_rank_eq hp hr
  unfold idx
  rw [dite_eq_left h]
  exact Classical.choose_spec h

/-- The state of rank `r`: C006's sorted `z_[r]`. -/
noncomputable def y (r : ℕ) : ℤ := N.x (N.idx r)

/-- The sorted states increase strictly with the rank. -/
theorem y_lt_y (hp : N.Primitive) {r r' : ℕ} (hrr : r < r') (hr' : r' < m) : N.y r < N.y r' := by
  have h1 := N.idx_spec hp (lt_trans hrr hr')
  have h2 := N.idx_spec hp hr'
  unfold y
  rcases lt_trichotomy (N.x (N.idx r)) (N.x (N.idx r')) with h | h | h
  · exact h
  · exfalso
    have := N.rank_congr h
    rw [h1.2, h2.2] at this
    omega
  · exfalso
    have := N.rank_lt_of_lt h2.1 h
    rw [h1.2, h2.2] at this
    omega

theorem idx_zero (hp : N.Primitive) (h0 : N.rank 0 = 0) : N.idx 0 = 0 := by
  have h := N.idx_spec hp N.hm
  exact N.rank_inj hp h.1 N.hm (h.2.trans h0.symm)

theorem y_zero (hp : N.Primitive) (h0 : N.rank 0 = 0) : N.y 0 = N.x 0 := by
  unfold y
  rw [N.idx_zero hp h0]

/-- The extension over one more period: `yext r = y r` for `r < m` and `2 y (r − m)` beyond,
so `yext m = 2 y 0` (C006's seam). -/
noncomputable def yext (r : ℕ) : ℤ := if r < m then N.y r else 2 * N.y (r - m)

/-- The sorted gaps `Δ_r = z_[r+1] − z_[r]`, with the seam gap `2 z_[0] − z_[m−1]` at `r = m−1`. -/
noncomputable def gap (r : ℕ) : ℤ := N.yext (r + 1) - N.yext r

theorem yext_of_lt {r : ℕ} (hr : r < m) : N.yext r = N.y r := by
  unfold yext
  rw [ite_eq_left hr]

theorem yext_m : N.yext m = 2 * N.y 0 := by
  unfold yext
  rw [ite_eq_right (lt_irrefl m), Nat.sub_self]

/-- Every gap is positive (the states are distinct and below `2 lo ≤ 2 z_[0]`). -/
theorem gap_pos (hp : N.Primitive) (h0 : N.rank 0 = 0) {r : ℕ} (hr : r < m) : 0 < N.gap r := by
  unfold gap
  rcases Nat.lt_or_ge (r + 1) m with hlt | hge
  · rw [N.yext_of_lt hlt, N.yext_of_lt hr]
    linarith [N.y_lt_y hp (Nat.lt_succ_self r) hlt]
  · have hr1 : r + 1 = m := le_antisymm hr hge
    rw [hr1, N.yext_m, N.yext_of_lt hr]
    have h1 : N.y r < 2 * N.lo := N.upper _
    have h2 : N.lo ≤ N.x 0 := N.lower 0
    rw [N.y_zero hp h0]
    linarith

/-- The gaps over one period sum to `z_[m] − z_[0] = z_[0]`, the minimum. -/
theorem sum_gap (hp : N.Primitive) (h0 : N.rank 0 = 0) :
    ∑ r ∈ Finset.range m, N.gap r = N.x 0 := by
  unfold gap
  rw [Finset.sum_range_sub N.yext m, N.yext_m, N.yext_of_lt N.hm, N.y_zero hp h0]
  ring

/-- Hence each gap is below the minimum when `m ≥ 2` (C006's `G_start < 2^B L` after scaling). -/
theorem gap_lt (hp : N.Primitive) (h0 : N.rank 0 = 0) (hm2 : 2 ≤ m) {r : ℕ} (hr : r < m) :
    N.gap r < N.x 0 := by
  rw [← N.sum_gap hp h0]
  have hmem : r ∈ Finset.range m := Finset.mem_range.mpr hr
  rw [← Finset.add_sum_erase _ _ hmem]
  have hpos : 0 < ∑ j ∈ (Finset.range m).erase r, N.gap j := by
    apply Finset.sum_pos
    · intro j hj
      exact N.gap_pos hp h0 (Finset.mem_range.mp (Finset.mem_of_mem_erase hj))
    · obtain ⟨j, hj, hjr⟩ : ∃ j, j < m ∧ j ≠ r := by
        rcases Nat.eq_zero_or_pos r with h | h
        · exact ⟨1, by omega, by omega⟩
        · exact ⟨0, by omega, by omega⟩
      exact ⟨j, Finset.mem_erase.mpr ⟨hjr, Finset.mem_range.mpr hj⟩⟩
  linarith

/-- The successor of the state of rank `r` is the state of rank `(r + h) mod m`. -/
theorem x_idx_succ (hp : N.Primitive) (hh : N.numHigh < m) {r : ℕ} (hr : r < m) :
    N.x (N.idx r + 1) = N.y ((r + N.numHigh) % m) := by
  have h1 := N.idx_spec hp hr
  have h2 := N.idx_spec hp (Nat.mod_lt (r + N.numHigh) N.hm)
  have hrk : N.rank (N.idx r + 1) = (r + N.numHigh) % m := by
    rw [N.rank_succ_eq hh, h1.2]
  unfold y
  rw [← N.x_mod (N.idx r + 1)]
  congr 1
  apply N.rank_inj hp (Nat.mod_lt _ N.hm) h2.1
  rw [N.rank_mod, hrk, h2.2]

/-- The state of rank `r` is high exactly when `r ≥ m − h` (the final block of ranks). -/
theorem high_idx_iff (hp : N.Primitive) {r : ℕ} (hr : r < m) :
    N.high (N.idx r) ↔ m - N.numHigh ≤ r := by
  have h := N.idx_spec hp hr
  rw [N.high_iff_rank h.1, h.2]

/-- Prefix sums of the mechanical word: `Σ_{j<i} c_j = ⌊iA/m⌋` with `A = mq + h` (started at
the minimum). -/
theorem sum_a_range (hh : N.numHigh < m) (h0 : N.rank 0 = 0) (i : ℕ) :
    ∑ j ∈ Finset.range i, N.a j = (i * (m * N.q + N.numHigh)) / m := by
  have hf : ∀ j, N.a j = N.q + (((j + 1) * N.numHigh) / m - (j * N.numHigh) / m) :=
    N.a_formula hh h0
  simp_rw [hf]
  rw [Finset.sum_add_distrib, Finset.sum_const, Finset.card_range, smul_eq_mul]
  have hmono : Monotone fun j : ℕ => (j * N.numHigh) / m :=
    fun a b hab => Nat.div_le_div_right (Nat.mul_le_mul_right _ hab)
  rw [Finset.sum_range_tsub hmono i]
  simp only [zero_mul, Nat.zero_div, Nat.sub_zero]
  rw [show i * (m * N.q + N.numHigh) = i * N.numHigh + m * (i * N.q) by ring,
    Nat.add_mul_div_left _ _ N.hm]
  ring

/-! #### Part 5: the gap recurrence in rank coordinates (C006 (7)/(G3)) -/

/-- The image of the state of rank `r`. -/
noncomputable def Fr (r : ℕ) : ℤ := N.F (N.idx r)

/-- Its extension over one more period, `Fext m = 2 Fr 0` (C006's seam `ε_[m] = 2ε_[0]`
together with `z_[m] = 2z_[0]`). -/
noncomputable def Fext (r : ℕ) : ℤ := if r < m then N.Fr r else 2 * N.Fr (r - m)

/-- The exponent at rank `r`: `q` on the low ranks `r < m − h`, `q + 1` on the final `h` ranks
(C006's `1 + 1_{j ≥ m−s}` when `q = 1`). -/
def e (r : ℕ) : ℕ := if m - N.numHigh ≤ r then N.q + 1 else N.q

theorem Fext_of_lt {r : ℕ} (hr : r < m) : N.Fext r = N.Fr r := by
  unfold Fext
  rw [ite_eq_left hr]

theorem Fext_m : N.Fext m = 2 * N.Fr 0 := by
  unfold Fext
  rw [ite_eq_right (lt_irrefl m), Nat.sub_self]

theorem e_eq (hp : N.Primitive) {r : ℕ} (hr : r < m) : N.e r = N.a (N.idx r) := by
  unfold e
  rw [N.a_eq (N.idx r)]
  by_cases h2 : m - N.numHigh ≤ r
  · rw [ite_eq_left h2, ite_eq_left ((N.high_idx_iff hp hr).mpr h2)]
  · rw [ite_eq_right h2, ite_eq_right (fun h3 => h2 ((N.high_idx_iff hp hr).mp h3))]

/-- The arrow at the state of rank `r`: `2^{e_r} z_[(r+h) mod m] = F_[r]`. -/
theorem arrow_rank (hp : N.Primitive) (hh : N.numHigh < m) {r : ℕ} (hr : r < m) :
    (2 : ℤ) ^ N.e r * N.y ((r + N.numHigh) % m) = N.Fr r := by
  rw [N.e_eq hp hr]
  have h1 := N.arrow (N.idx r)
  rw [N.x_idx_succ hp hh hr] at h1
  exact h1

/-- **C006's gap recurrence (G3)** in rank coordinates: `2^{e_r} Δ_{(r+h) mod m} = F_[r+1] − F_[r]`
for every rank `r < m`, the seam `r = m − 1` using the extension `F_[m] = 2F_[0]`,
`z_[m] = 2z_[0]`. -/
theorem gap_recurrence (hp : N.Primitive) (hm2 : 2 ≤ m) {r : ℕ} (hr : r < m) :
    (2 : ℤ) ^ N.e r * N.gap ((r + N.numHigh) % m) = N.Fext (r + 1) - N.Fext r := by
  have hh := N.numHigh_lt hp hm2
  have hpos := N.numHigh_pos hp hm2
  have hA := N.arrow_rank hp hh hr
  rw [N.Fext_of_lt hr]
  rcases Nat.lt_or_ge (r + 1) m with hr1 | hr1
  · have hA' := N.arrow_rank hp hh hr1
    rw [N.Fext_of_lt hr1]
    by_cases hlow : m - N.numHigh ≤ r
    · -- both ranks high: exponents `q + 1`, successor ranks `r + h − m`, `r + h − m + 1`
      have hlow' : m - N.numHigh ≤ r + 1 := le_trans hlow (Nat.le_succ r)
      have he : N.e r = N.q + 1 := by
        unfold e
        rw [ite_eq_left hlow]
      have he' : N.e (r + 1) = N.q + 1 := by
        unfold e
        rw [ite_eq_left hlow']
      have hm1 : (r + N.numHigh) % m = r + N.numHigh - m := by
        rw [Nat.mod_eq_sub_mod (by omega), Nat.mod_eq_of_lt (by omega)]
      have hm2' : (r + 1 + N.numHigh) % m = r + N.numHigh - m + 1 := by
        rw [Nat.mod_eq_sub_mod (by omega), Nat.mod_eq_of_lt (by omega)]
        omega
      rw [he, hm1] at hA
      rw [he', hm2'] at hA'
      rw [hm1, he]
      unfold gap
      rw [N.yext_of_lt (by omega : r + N.numHigh - m + 1 < m),
        N.yext_of_lt (by omega : r + N.numHigh - m < m)]
      linarith
    · rw [not_le] at hlow
      have he : N.e r = N.q := by
        unfold e
        rw [ite_eq_right (not_le.mpr hlow)]
      by_cases hlow' : m - N.numHigh ≤ r + 1
      · -- `r` low, `r + 1` high: successor ranks `m − 1` and `0`, the seam gap
        have he' : N.e (r + 1) = N.q + 1 := by
          unfold e
          rw [ite_eq_left hlow']
        have hm1 : (r + N.numHigh) % m = m - 1 := by
          rw [show r + N.numHigh = m - 1 by omega]
          exact Nat.mod_eq_of_lt (by omega)
        have hm2' : (r + 1 + N.numHigh) % m = 0 := by
          rw [show r + 1 + N.numHigh = m by omega]
          exact Nat.mod_self m
        rw [he, hm1] at hA
        rw [he', hm2', pow_succ] at hA'
        rw [hm1, he]
        unfold gap
        rw [show m - 1 + 1 = m by omega, N.yext_m, N.yext_of_lt (by omega : m - 1 < m)]
        linarith
      · -- both ranks low: exponents `q`, successor ranks `r + h`, `r + h + 1`
        have he' : N.e (r + 1) = N.q := by
          unfold e
          rw [ite_eq_right hlow']
        have hm1 : (r + N.numHigh) % m = r + N.numHigh := Nat.mod_eq_of_lt (by omega)
        have hm2' : (r + 1 + N.numHigh) % m = r + N.numHigh + 1 := by
          rw [show r + 1 + N.numHigh = r + N.numHigh + 1 by ring]
          exact Nat.mod_eq_of_lt (by omega)
        rw [he, hm1] at hA
        rw [he', hm2'] at hA'
        rw [hm1, he]
        unfold gap
        rw [N.yext_of_lt (by omega : r + N.numHigh + 1 < m),
          N.yext_of_lt (by omega : r + N.numHigh < m)]
        linarith
  · -- the seam `r = m − 1` (high): successor rank `h − 1`; the next image is `2F_[0]`
    have hlow : m - N.numHigh ≤ r := by omega
    have he : N.e r = N.q + 1 := by
      unfold e
      rw [ite_eq_left hlow]
    have hA0 := N.arrow_rank hp hh N.hm
    have he0 : N.e 0 = N.q := by
      unfold e
      rw [ite_eq_right (by omega)]
    have hm0 : (0 + N.numHigh) % m = N.numHigh := by
      rw [Nat.zero_add]
      exact Nat.mod_eq_of_lt hh
    rw [he0, hm0] at hA0
    have hm1 : (r + N.numHigh) % m = N.numHigh - 1 := by
      rw [show r + N.numHigh = (N.numHigh - 1) + m by omega, Nat.add_mod_right]
      exact Nat.mod_eq_of_lt (by omega)
    rw [he, pow_succ, hm1] at hA
    rw [show r + 1 = m by omega, N.Fext_m, hm1, he, pow_succ]
    unfold gap
    rw [N.yext_of_lt (by omega : N.numHigh - 1 + 1 < m),
      N.yext_of_lt (by omega : N.numHigh - 1 < m), show N.numHigh - 1 + 1 = N.numHigh by omega]
    linarith

end NarrowCycle

/-! ### C005 `ORDER_THEORY.md` §2: the inversion formula (2) and the three-band observation -/

/-- C005's (2): with normalised states `z_i = n_i/2^h`, `z_j = n_j/2^{h+k}` and offsets `q/2^h`,
`q/2^{h+k}`, the difference of the images `F = 3z + q/2^{height}` is
`(3r − q(2^k − 1))/2^{h+k}` with `r = n_j − 2^k n_i`. -/
theorem inversion_formula (n_i n_j q : ℚ) (h k : ℕ) :
    (3 * (n_j / 2 ^ (h + k)) + q / 2 ^ (h + k)) - (3 * (n_i / 2 ^ h) + q / 2 ^ h)
      = (3 * (n_j - 2 ^ k * n_i) - q * (2 ^ k - 1)) / 2 ^ (h + k) := by
  rw [pow_add]
  field_simp
  ring

/-- C005's three-band observation at `q = 1`: a height gap `k ≤ 2` cannot invert, because
`3r − (2^k − 1) ≥ 0` for `r ≥ 1`, with equality only for `k = 2`, `r = 1`. -/
theorem no_inversion_of_le_two {r : ℤ} {k : ℕ} (hr : 1 ≤ r) (hk : k ≤ 2) :
    0 ≤ 3 * r - (2 ^ k - 1) ∧ (3 * r - (2 ^ k - 1) = 0 → k = 2 ∧ r = 1) := by
  interval_cases k <;> norm_num <;> omega

/-! ### C005 §§1–2 on actual cycles: dyadic heights, scaled normalised states, and the
three-band order at `q = 1` -/

/-- Heights exist: for `0 < L ≤ n` there is `h` with `2^h L ≤ n < 2^{h+1} L`. -/
theorem exists_height {L n : ℤ} (hL : 0 < L) (hn : L ≤ n) :
    ∃ h : ℕ, 2 ^ h * L ≤ n ∧ n < 2 ^ (h + 1) * L := by
  classical
  have hex : ∃ k : ℕ, n < 2 ^ (k + 1) * L := by
    obtain ⟨k, hk⟩ := pow_unbounded_of_one_lt n (by norm_num : (1 : ℤ) < 2)
    refine ⟨k, ?_⟩
    have h1 : (2 : ℤ) ^ k ≤ 2 ^ (k + 1) := pow_le_pow_right₀ (by norm_num) (Nat.le_succ k)
    have h2 : (2 : ℤ) ^ (k + 1) ≤ 2 ^ (k + 1) * L :=
      le_mul_of_one_le_right (by positivity) (by linarith)
    linarith
  refine ⟨Nat.find hex, ?_, Nat.find_spec hex⟩
  rcases Nat.eq_zero_or_pos (Nat.find hex) with h0 | hpos
  · rw [h0, pow_zero, one_mul]; exact hn
  · have hmin := Nat.find_min hex (Nat.sub_lt hpos Nat.one_pos)
    rw [Nat.sub_add_cancel hpos] at hmin
    exact not_lt.mp hmin

/-- `H < 8L` means heights at most `2`. -/
theorem height_le_two {L n : ℤ} {h : ℕ} (hL : 0 < L) (h1 : 2 ^ h * L ≤ n) (h8 : n < 8 * L) :
    h ≤ 2 := by
  by_contra hgt
  rw [not_le] at hgt
  have : (2 : ℤ) ^ 3 ≤ 2 ^ h := pow_le_pow_right₀ (by norm_num) hgt
  nlinarith [mul_le_mul_of_nonneg_right this hL.le]

/-- A power of two times an odd number determines both factors. -/
theorem pow_mul_eq_of_odd {x y : ℤ} {s t : ℕ} (hx : Odd x) (hy : Odd y)
    (h : (2 : ℤ) ^ s * x = 2 ^ t * y) : s = t ∧ x = y := by
  rcases lt_trichotomy s t with hlt | heq | hgt
  · exfalso
    have e : (2 : ℤ) ^ t = 2 ^ s * (2 * 2 ^ (t - s - 1)) := by
      rw [← pow_succ', ← pow_add]
      congr 1
      omega
    rw [e, mul_assoc] at h
    have hx' : x = 2 * 2 ^ (t - s - 1) * y := mul_left_cancel₀ (by positivity) h
    exact (Int.not_even_iff_odd.mpr hx) ⟨2 ^ (t - s - 1) * y, by rw [hx']; ring⟩
  · subst heq
    exact ⟨rfl, mul_left_cancel₀ (by positivity) h⟩
  · exfalso
    have e : (2 : ℤ) ^ s = 2 ^ t * (2 * 2 ^ (s - t - 1)) := by
      rw [← pow_succ', ← pow_add]
      congr 1
      omega
    rw [e, mul_assoc] at h
    have hy' : y = 2 * 2 ^ (s - t - 1) * x := mul_left_cancel₀ (by positivity) h.symm
    exact (Int.not_even_iff_odd.mpr hy) ⟨2 ^ (s - t - 1) * x, by rw [hy']; ring⟩

/-- Two numbers of `[lo, 2 lo)` whose quotient is a power of two are equal. -/
theorem eq_of_pow_mul_eq_in_window {lo x y : ℤ} {s t : ℕ} (hx : lo ≤ x) (hx2 : x < 2 * lo)
    (hy : lo ≤ y) (hy2 : y < 2 * lo) (h : (2 : ℤ) ^ s * x = 2 ^ t * y) : x = y := by
  have hlo : 0 < lo := by linarith
  rcases lt_trichotomy s t with hlt | heq | hgt
  · exfalso
    have e : (2 : ℤ) ^ (s + 1) ≤ 2 ^ t := pow_le_pow_right₀ (by norm_num) hlt
    rw [pow_succ] at e
    have h2s : (0 : ℤ) < 2 ^ s := by positivity
    have h3 : (2 : ℤ) ^ s * (2 * y) ≤ 2 ^ s * x := by
      have := mul_le_mul_of_nonneg_right e (by linarith : (0 : ℤ) ≤ y)
      linarith
    have h4 : 2 * y ≤ x := le_of_mul_le_mul_left h3 h2s
    linarith
  · subst heq
    exact mul_left_cancel₀ (by positivity) h
  · exfalso
    have e : (2 : ℤ) ^ (t + 1) ≤ 2 ^ s := pow_le_pow_right₀ (by norm_num) hgt
    rw [pow_succ] at e
    have h2t : (0 : ℤ) < 2 ^ t := by positivity
    have h3 : (2 : ℤ) ^ t * (2 * x) ≤ 2 ^ t * y := by
      have := mul_le_mul_of_nonneg_right e (by linarith : (0 : ℤ) ≤ x)
      linarith
    have h4 : 2 * x ≤ y := le_of_mul_le_mul_left h3 h2t
    linarith

/-! ### C006 `ORDER_RIGIDITY.md` §3, elementary parts: the zero-forcing run lemma behind (G1)
and the discrete intermediate-value step behind (H1) -/

/-- Binary divisibility along a zero-forcing run: if `2^{e_k} G_{k+1} = 3 G_k` for `k < t`,
then `2^{E_t} G_t = 3^t G_0` with `E_t = Σ_{k<t} e_k`. -/
theorem run_pow_mul (G : ℕ → ℤ) (e : ℕ → ℕ) (t : ℕ)
    (hrun : ∀ k, k < t → (2 : ℤ) ^ e k * G (k + 1) = 3 * G k) :
    (2 : ℤ) ^ (∑ k ∈ Finset.range t, e k) * G t = 3 ^ t * G 0 := by
  induction t with
  | zero => simp
  | succ t ih =>
    have ih' := ih (fun k hk => hrun k (Nat.lt_succ_of_lt hk))
    rw [Finset.sum_range_succ, pow_add, pow_succ]
    calc (2 : ℤ) ^ (∑ k ∈ Finset.range t, e k) * 2 ^ e t * G (t + 1)
        = 2 ^ (∑ k ∈ Finset.range t, e k) * (2 ^ e t * G (t + 1)) := by ring
      _ = 2 ^ (∑ k ∈ Finset.range t, e k) * (3 * G t) := by rw [hrun t (Nat.lt_succ_self t)]
      _ = 3 * (2 ^ (∑ k ∈ Finset.range t, e k) * G t) := by ring
      _ = 3 * (3 ^ t * G 0) := by rw [ih']
      _ = 3 ^ t * 3 * G 0 := by ring

/-- Hence `2^{E_t} ∣ G_0`: "since `G_start` is a positive integer and 2 and 3 are coprime". -/
theorem run_dvd (G : ℕ → ℤ) (e : ℕ → ℕ) (t : ℕ)
    (hrun : ∀ k, k < t → (2 : ℤ) ^ e k * G (k + 1) = 3 * G k) :
    (2 : ℤ) ^ (∑ k ∈ Finset.range t, e k) ∣ G 0 := by
  have h := run_pow_mul G e t hrun
  have h1 : (2 : ℤ) ^ (∑ k ∈ Finset.range t, e k) ∣ 3 ^ t * G 0 := ⟨G t, h.symm⟩
  have hcop : IsCoprime ((2 : ℤ) ^ (∑ k ∈ Finset.range t, e k)) (3 ^ t) :=
    IsCoprime.pow (Int.isCoprime_iff_gcd_eq_one.mpr (by norm_num))
  exact hcop.dvd_of_dvd_mul_left h1

/-- A positive run start is at least `2^{E_t} ≥ 2^t` when every run exponent is positive
(C006's `G_start ≥ 2^{e_run} ≥ 2^t`). -/
theorem run_lower (G : ℕ → ℤ) (e : ℕ → ℕ) (t : ℕ) (hG : 0 < G 0) (he : ∀ k, k < t → 1 ≤ e k)
    (hrun : ∀ k, k < t → (2 : ℤ) ^ e k * G (k + 1) = 3 * G k) :
    (2 : ℤ) ^ t ≤ G 0 := by
  have h1 := Int.le_of_dvd hG (run_dvd G e t hrun)
  have h2 : t ≤ ∑ k ∈ Finset.range t, e k := by
    calc t = ∑ _k ∈ Finset.range t, 1 := by simp
      _ ≤ ∑ k ∈ Finset.range t, e k :=
          Finset.sum_le_sum (fun k hk => he k (Finset.mem_range.mp hk))
  exact le_trans (pow_le_pow_right₀ (by norm_num) h2) h1

/-- A sequence of naturals starting at `0` that rises by at most one per step attains every
value up to any value it attains (C006 (H1): reaching height `B` from `0` visits all heights). -/
theorem exists_eq_of_step_le (f : ℕ → ℕ) (h0 : f 0 = 0) (hstep : ∀ i, f (i + 1) ≤ f i + 1)
    {j b : ℕ} (hb : b ≤ f j) : ∃ i, i ≤ j ∧ f i = b := by
  induction j with
  | zero => exact ⟨0, le_refl 0, by omega⟩
  | succ j ih =>
    rcases Nat.lt_or_ge b (f (j + 1)) with hlt | hge
    · obtain ⟨i, hi, hfi⟩ := ih (by have := hstep j; omega)
      exact ⟨i, Nat.le_succ_of_le hi, hfi⟩
    · exact ⟨j + 1, le_refl _, by omega⟩

/-! ### C008 `INDEPENDENT_MATCHING.md` §1: the cyclicity of `⟨2, 3⟩` -/

/-- C008's cyclicity, abstractly: in a commutative group, if `x^A = y^m` with `gcd(A, m) = 1`,
then `x` and `y` are powers of one element `t` with `t^m = x` and `t^A = y`, so `⟨x, y⟩ = ⟨t⟩`
is cyclic. -/
theorem exists_common_root {G : Type*} [CommGroup G] (x y : G) {A m : ℕ} (hAm : Nat.Coprime A m)
    (h : x ^ A = y ^ m) : ∃ t : G, t ^ m = x ∧ t ^ A = y := by
  obtain ⟨u, v, huv⟩ : ∃ u v : ℤ, u * (m : ℤ) + v * (A : ℤ) = 1 := by
    obtain ⟨u, v, huv⟩ := Nat.isCoprime_iff_coprime.mpr hAm.symm
    exact ⟨u, v, huv⟩
  have hx : x ^ (A : ℤ) = y ^ (m : ℤ) := by
    rw [zpow_natCast, zpow_natCast]
    exact h
  refine ⟨x ^ u * y ^ v, ?_, ?_⟩
  · calc (x ^ u * y ^ v) ^ m = (x ^ u * y ^ v) ^ (m : ℤ) := (zpow_natCast _ _).symm
      _ = x ^ (u * (m : ℤ)) * y ^ (v * (m : ℤ)) := by rw [mul_zpow, ← zpow_mul, ← zpow_mul]
      _ = x ^ (u * (m : ℤ)) * (y ^ (m : ℤ)) ^ v := by rw [mul_comm v, zpow_mul y]
      _ = x ^ (u * (m : ℤ)) * (x ^ (A : ℤ)) ^ v := by rw [hx]
      _ = x ^ (u * (m : ℤ) + v * (A : ℤ)) := by rw [← zpow_mul, ← zpow_add, mul_comm (A : ℤ)]
      _ = x := by rw [huv, zpow_one]
  · calc (x ^ u * y ^ v) ^ A = (x ^ u * y ^ v) ^ (A : ℤ) := (zpow_natCast _ _).symm
      _ = x ^ (u * (A : ℤ)) * y ^ (v * (A : ℤ)) := by rw [mul_zpow, ← zpow_mul, ← zpow_mul]
      _ = (x ^ (A : ℤ)) ^ u * y ^ (v * (A : ℤ)) := by rw [mul_comm u, zpow_mul x]
      _ = (y ^ (m : ℤ)) ^ u * y ^ (v * (A : ℤ)) := by rw [hx]
      _ = y ^ (u * (m : ℤ) + v * (A : ℤ)) := by rw [← zpow_mul, ← zpow_add, mul_comm (m : ℤ)]
      _ = y := by rw [huv, zpow_one]

/-- C008's cyclicity of `⟨2, 3⟩` modulo `N`: if `N ∣ 2^A − 3^m` with `gcd(A, m) = 1` and `N`
coprime to `2` and `3`, the units `2` and `3` of `ZMod N` are powers of one unit `t` with
`t^m = 2`, `t^A = 3`. -/
theorem zmod_common_root {N A m : ℕ} (hN2 : Nat.Coprime 2 N) (hN3 : Nat.Coprime 3 N)
    (hAm : Nat.Coprime A m) (hdvd : (N : ℤ) ∣ (2 : ℤ) ^ A - 3 ^ m) :
    ∃ t : (ZMod N)ˣ, t ^ m = ZMod.unitOfCoprime 2 hN2 ∧ t ^ A = ZMod.unitOfCoprime 3 hN3 := by
  have : NeZero N := ⟨fun h => by subst h; simp at hN2⟩
  apply exists_common_root _ _ hAm
  apply Units.ext
  simp only [Units.val_pow_eq_pow_val, ZMod.coe_unitOfCoprime]
  have h := (ZMod.intCast_zmod_eq_zero_iff_dvd ((2 : ℤ) ^ A - 3 ^ m) N).mpr hdvd
  push_cast at h ⊢
  linear_combination h

/-- An actual odd cycle of the raw `3x+q` map, listed from its minimum `n 0`, with dyadic
heights `h i` (`2^{h_i} n_0 ≤ n_i < 2^{h_i+1} n_0`) bounded by `B`: C005 §1's data. -/
structure OddCycle (m : ℕ) where
  n : ℕ → ℤ
  a : ℕ → ℕ
  h : ℕ → ℕ
  q : ℤ
  B : ℕ
  hm : 0 < m
  hq : 0 < q
  nper : ∀ i, n (i + m) = n i
  nodd : ∀ i, Odd (n i)
  nmin : ∀ i, n 0 ≤ n i
  npos : 0 < n 0
  arrow : ∀ i, (2 : ℤ) ^ a i * n (i + 1) = 3 * n i + q
  hlo : ∀ i, 2 ^ h i * n 0 ≤ n i
  hhi : ∀ i, n i < 2 ^ (h i + 1) * n 0
  hB : ∀ i, h i ≤ B

namespace OddCycle

variable {m : ℕ} (Γ : OddCycle m)

/-- The scaled normalised state `2^{B−h_i} n_i = 2^B z_i`. -/
def Z (i : ℕ) : ℤ := 2 ^ (Γ.B - Γ.h i) * Γ.n i

/-- The scaled image `2^B F_i = 3 Z_i + 2^{B−h_i} q`. -/
def F (i : ℕ) : ℤ := 3 * Γ.Z i + 2 ^ (Γ.B - Γ.h i) * Γ.q

/-- The normalised exponent `c_i = a_i + h_{i+1} − h_i` (C005 (1)). -/
def c (i : ℕ) : ℕ := Γ.a i + Γ.h (i + 1) - Γ.h i

/-- The scaled lower endpoint `2^B L`. -/
def lo : ℤ := 2 ^ Γ.B * Γ.n 0

theorem h_unique {L n : ℤ} {h h' : ℕ} (hL : 0 < L) (h1 : 2 ^ h * L ≤ n)
    (h2 : n < 2 ^ (h + 1) * L) (h1' : 2 ^ h' * L ≤ n) (h2' : n < 2 ^ (h' + 1) * L) : h = h' := by
  by_contra hne
  rcases Nat.lt_or_gt_of_ne hne with hlt | hgt
  · have : (2 : ℤ) ^ (h + 1) ≤ 2 ^ h' := pow_le_pow_right₀ (by norm_num) hlt
    nlinarith [mul_le_mul_of_nonneg_right this hL.le]
  · have : (2 : ℤ) ^ (h' + 1) ≤ 2 ^ h := pow_le_pow_right₀ (by norm_num) hgt
    nlinarith [mul_le_mul_of_nonneg_right this hL.le]

theorem h_zero : Γ.h 0 = 0 := by
  have h1 := Γ.hlo 0
  have hp := Γ.npos
  by_contra hne
  have h2 : (2 : ℤ) ^ 1 ≤ 2 ^ Γ.h 0 :=
    pow_le_pow_right₀ (by norm_num) (Nat.one_le_iff_ne_zero.mpr hne)
  nlinarith [mul_le_mul_of_nonneg_right h2 hp.le]

theorem h_per (i : ℕ) : Γ.h (i + m) = Γ.h i := by
  have h1 := Γ.hlo (i + m)
  have h2 := Γ.hhi (i + m)
  rw [Γ.nper i] at h1 h2
  exact h_unique Γ.npos h1 h2 (Γ.hlo i) (Γ.hhi i)

theorem n_add_mul (k t : ℕ) : Γ.n (k + m * t) = Γ.n k := by
  induction t with
  | zero => simp
  | succ t ih => rw [Nat.mul_succ, ← Nat.add_assoc, Γ.nper, ih]

theorem n_mod (k : ℕ) : Γ.n (k % m) = Γ.n k := by
  conv_rhs => rw [← Nat.mod_add_div k m]
  exact (Γ.n_add_mul _ _).symm

theorem h_mod (k : ℕ) : Γ.h (k % m) = Γ.h k := by
  have h1 := Γ.hlo k
  have h2 := Γ.hhi k
  rw [← Γ.n_mod k] at h1 h2
  exact h_unique Γ.npos (Γ.hlo (k % m)) (Γ.hhi (k % m)) h1 h2

theorem Z_per (i : ℕ) : Γ.Z (i + m) = Γ.Z i := by
  unfold Z
  rw [Γ.h_per, Γ.nper]

theorem Z_mod (k : ℕ) : Γ.Z (k % m) = Γ.Z k := by
  unfold Z
  rw [Γ.h_mod, Γ.n_mod]

theorem pow_sub_mul {B h : ℕ} (hh : h ≤ B) : (2 : ℤ) ^ (B - h) * 2 ^ h = 2 ^ B := by
  rw [← pow_add, Nat.sub_add_cancel hh]

theorem Z_lower (i : ℕ) : Γ.lo ≤ Γ.Z i := by
  unfold Z lo
  have h1 := Γ.hlo i
  have h2 : (0 : ℤ) < 2 ^ (Γ.B - Γ.h i) := by positivity
  calc (2 : ℤ) ^ Γ.B * Γ.n 0 = 2 ^ (Γ.B - Γ.h i) * (2 ^ Γ.h i * Γ.n 0) := by
        rw [← mul_assoc, pow_sub_mul (Γ.hB i)]
    _ ≤ 2 ^ (Γ.B - Γ.h i) * Γ.n i := mul_le_mul_of_nonneg_left h1 h2.le

theorem Z_upper (i : ℕ) : Γ.Z i < 2 * Γ.lo := by
  unfold Z lo
  have h2 := Γ.hhi i
  have hp : (0 : ℤ) < 2 ^ (Γ.B - Γ.h i) := by positivity
  have e := pow_sub_mul (Γ.hB i)
  calc (2 : ℤ) ^ (Γ.B - Γ.h i) * Γ.n i < 2 ^ (Γ.B - Γ.h i) * (2 ^ (Γ.h i + 1) * Γ.n 0) :=
        mul_lt_mul_of_pos_left h2 hp
    _ = 2 * (2 ^ Γ.B * Γ.n 0) := by
        rw [pow_succ]
        linear_combination (2 * Γ.n 0) * e

theorem Z_zero : Γ.Z 0 = Γ.lo := by
  unfold Z lo
  rw [Γ.h_zero, Nat.sub_zero]

theorem h_le_a_add (i : ℕ) : Γ.h i ≤ Γ.a i + Γ.h (i + 1) := by
  by_contra hlt
  rw [not_le] at hlt
  have h1 := Γ.arrow i
  have h2 := Γ.hhi (i + 1)
  have h3 := Γ.hlo i
  have hp := Γ.npos
  have hq := Γ.hq
  have hpow : (2 : ℤ) ^ (Γ.a i + Γ.h (i + 1) + 1) ≤ 2 ^ Γ.h i :=
    pow_le_pow_right₀ (by norm_num) hlt
  have h4 : (2 : ℤ) ^ Γ.a i * Γ.n (i + 1) < 2 ^ Γ.a i * (2 ^ (Γ.h (i + 1) + 1) * Γ.n 0) :=
    mul_lt_mul_of_pos_left h2 (by positivity)
  have h5 : (2 : ℤ) ^ Γ.a i * (2 ^ (Γ.h (i + 1) + 1) * Γ.n 0)
      = 2 ^ (Γ.a i + Γ.h (i + 1) + 1) * Γ.n 0 := by
    rw [← mul_assoc, ← pow_add, Nat.add_assoc]
  have h6 : (2 : ℤ) ^ (Γ.a i + Γ.h (i + 1) + 1) * Γ.n 0 ≤ 2 ^ Γ.h i * Γ.n 0 :=
    mul_le_mul_of_nonneg_right hpow hp.le
  have h7 : 0 < Γ.n i := lt_of_lt_of_le hp (Γ.nmin i)
  linarith

/-- C005 (1): `2^{c_i} Z_{i+1} = F_i`. -/
theorem c_arrow (i : ℕ) : (2 : ℤ) ^ Γ.c i * Γ.Z (i + 1) = Γ.F i := by
  unfold c F Z
  have h1 := Γ.arrow i
  have hle := Γ.h_le_a_add i
  have hB := Γ.hB (i + 1)
  have hBi := Γ.hB i
  have e : (2 : ℤ) ^ (Γ.a i + Γ.h (i + 1) - Γ.h i) * 2 ^ (Γ.B - Γ.h (i + 1))
      = 2 ^ (Γ.B - Γ.h i) * 2 ^ Γ.a i := by
    rw [← pow_add, ← pow_add]
    congr 1
    omega
  calc (2 : ℤ) ^ (Γ.a i + Γ.h (i + 1) - Γ.h i) * (2 ^ (Γ.B - Γ.h (i + 1)) * Γ.n (i + 1))
      = (2 ^ (Γ.a i + Γ.h (i + 1) - Γ.h i) * 2 ^ (Γ.B - Γ.h (i + 1))) * Γ.n (i + 1) := by ring
    _ = 2 ^ (Γ.B - Γ.h i) * (2 ^ Γ.a i * Γ.n (i + 1)) := by rw [e]; ring
    _ = 2 ^ (Γ.B - Γ.h i) * (3 * Γ.n i + Γ.q) := by rw [h1]
    _ = 3 * (2 ^ (Γ.B - Γ.h i) * Γ.n i) + 2 ^ (Γ.B - Γ.h i) * Γ.q := by ring

/-- Distinct odd numerators give distinct normalised states. -/
theorem Z_inj {i j : ℕ} (h : Γ.Z i = Γ.Z j) : Γ.h i = Γ.h j ∧ Γ.n i = Γ.n j := by
  unfold Z at h
  obtain ⟨h1, h2⟩ := pow_mul_eq_of_odd (Γ.nodd i) (Γ.nodd j) h
  refine ⟨?_, h2⟩
  have := Γ.hB i
  have := Γ.hB j
  omega

/-- C005 (2) in scaled form, for `h_i ≤ h_j`, `k = h_j − h_i`, `r = n_j − 2^k n_i`:
`F_j − F_i = 2^{B−h_j} (3r − q(2^k − 1))`. -/
theorem F_sub_of_le {i j : ℕ} (hij : Γ.h i ≤ Γ.h j) :
    Γ.F j - Γ.F i = 2 ^ (Γ.B - Γ.h j)
      * (3 * (Γ.n j - 2 ^ (Γ.h j - Γ.h i) * Γ.n i) - Γ.q * (2 ^ (Γ.h j - Γ.h i) - 1)) := by
  unfold F Z
  have e : (2 : ℤ) ^ (Γ.B - Γ.h i) = 2 ^ (Γ.B - Γ.h j) * 2 ^ (Γ.h j - Γ.h i) := by
    rw [← pow_add]
    congr 1
    have := Γ.hB j
    omega
  rw [e]
  ring

theorem Z_sub_of_le {i j : ℕ} (hij : Γ.h i ≤ Γ.h j) :
    Γ.Z j - Γ.Z i = 2 ^ (Γ.B - Γ.h j) * (Γ.n j - 2 ^ (Γ.h j - Γ.h i) * Γ.n i) := by
  unfold Z
  have e : (2 : ℤ) ^ (Γ.B - Γ.h i) = 2 ^ (Γ.B - Γ.h j) * 2 ^ (Γ.h j - Γ.h i) := by
    rw [← pow_add]
    congr 1
    have := Γ.hB j
    omega
  rw [e]
  ring

/-- The equality case of (2) is excluded in a primitive cycle: equal images give equal
normalised successors, hence equal states. -/
theorem Z_eq_of_F_eq (hprim : ∀ i j, i < m → j < m → Γ.n i = Γ.n j → i = j) {i j : ℕ}
    (h : Γ.F i = Γ.F j) : Γ.Z i = Γ.Z j := by
  rw [← Γ.c_arrow i, ← Γ.c_arrow j] at h
  have hZ : Γ.Z (i + 1) = Γ.Z (j + 1) :=
    eq_of_pow_mul_eq_in_window (Γ.Z_lower _) (Γ.Z_upper _) (Γ.Z_lower _) (Γ.Z_upper _) h
  have hn : Γ.n ((i + 1) % m) = Γ.n ((j + 1) % m) := by
    rw [Γ.n_mod, Γ.n_mod]
    exact (Γ.Z_inj hZ).2
  have hij := hprim _ _ (Nat.mod_lt _ Γ.hm) (Nat.mod_lt _ Γ.hm) hn
  have hmod : i % m = j % m := Nat.ModEq.add_right_cancel' 1 hij
  rw [← Γ.Z_mod i, ← Γ.Z_mod j, hmod]

/-- **C005 §2, the three-band order at `q = 1`:** with all heights at most `2` (`H < 8L`), the
images increase with the normalised states. -/
theorem F_lt_of_Z_lt (hq1 : Γ.q = 1) (hB2 : Γ.B ≤ 2)
    (hprim : ∀ i j, i < m → j < m → Γ.n i = Γ.n j → i = j) {i j : ℕ} (hZ : Γ.Z i < Γ.Z j) :
    Γ.F i < Γ.F j := by
  rcases Nat.lt_or_ge (Γ.h i) (Γ.h j) with hlt | hle
  · have hk : Γ.h j - Γ.h i ≤ 2 := by
      have := Γ.hB j
      omega
    have hsub := Γ.F_sub_of_le hlt.le
    have hZs := Γ.Z_sub_of_le hlt.le
    set r := Γ.n j - 2 ^ (Γ.h j - Γ.h i) * Γ.n i with hr
    have hpos : (0 : ℤ) < 2 ^ (Γ.B - Γ.h j) := by positivity
    have hr0 : 0 < r := by
      have hprod : 0 < 2 ^ (Γ.B - Γ.h j) * r := by
        rw [← hZs]
        linarith
      by_contra hneg
      rw [not_lt] at hneg
      nlinarith
    have hr1 : 1 ≤ r := by linarith
    obtain ⟨hnn, _⟩ := no_inversion_of_le_two hr1 hk
    rw [hq1] at hsub
    rcases lt_or_eq_of_le hnn with hgt | heq0
    · have hin : (0 : ℤ) < 3 * r - 1 * (2 ^ (Γ.h j - Γ.h i) - 1) := by linarith
      have := mul_pos hpos hin
      linarith
    · exfalso
      have hFeq : Γ.F i = Γ.F j := by
        have hz : (3 : ℤ) * r - 1 * (2 ^ (Γ.h j - Γ.h i) - 1) = 0 := by linarith
        rw [hz, mul_zero] at hsub
        linarith
      have := Γ.Z_eq_of_F_eq hprim hFeq
      linarith
  · have e1 : (2 : ℤ) ^ (Γ.B - Γ.h i) ≤ 2 ^ (Γ.B - Γ.h j) :=
      pow_le_pow_right₀ (by norm_num) (by have := Γ.hB i; have := Γ.hB j; omega)
    have hq := Γ.hq
    unfold F
    nlinarith [mul_le_mul_of_nonneg_right e1 hq.le]

theorem order_of_three_band (hq1 : Γ.q = 1) (hB2 : Γ.B ≤ 2)
    (hprim : ∀ i j, i < m → j < m → Γ.n i = Γ.n j → i = j) (i j : ℕ) :
    Γ.Z i < Γ.Z j ↔ Γ.F i < Γ.F j := by
  constructor
  · exact Γ.F_lt_of_Z_lt hq1 hB2 hprim
  · intro hF
    rcases lt_trichotomy (Γ.Z i) (Γ.Z j) with h | h | h
    · exact h
    · exfalso
      obtain ⟨hh, hn⟩ := Γ.Z_inj h
      have : Γ.F i = Γ.F j := by
        unfold F Z
        rw [hh, hn]
      linarith
    · exfalso
      have := Γ.F_lt_of_Z_lt hq1 hB2 hprim h
      linarith

theorem F_zero : Γ.F 0 = 3 * Γ.lo + 2 ^ Γ.B * Γ.q := by
  unfold F
  rw [Γ.Z_zero, Γ.h_zero, Nat.sub_zero]

theorem F_lt_two_F_zero (i : ℕ) : Γ.F i < 2 * Γ.F 0 := by
  rw [Γ.F_zero]
  unfold F
  have h1 := Γ.Z_upper i
  have h2 : (2 : ℤ) ^ (Γ.B - Γ.h i) ≤ 2 ^ Γ.B :=
    pow_le_pow_right₀ (by norm_num) (Nat.sub_le _ _)
  have hq := Γ.hq
  have hB : (0 : ℤ) < 2 ^ Γ.B := by positivity
  nlinarith [mul_le_mul_of_nonneg_right h2 hq.le]

theorem F_zero_le (hord : ∀ i j, Γ.Z i < Γ.Z j ↔ Γ.F i < Γ.F j) (j : ℕ) : Γ.F 0 ≤ Γ.F j := by
  by_contra hlt
  rw [not_le] at hlt
  have := (hord j 0).mpr hlt
  rw [Γ.Z_zero] at this
  linarith [Γ.Z_lower j]

/-- An ordered actual cycle gives a `NarrowCycle` on its scaled normalised states, with
exponents `c_i`, images `2^B F_i` and `lo = 2^B L` (C005 §§1–2). -/
def toNarrow (hord : ∀ i j, Γ.Z i < Γ.Z j ↔ Γ.F i < Γ.F j) (q' : ℕ)
    (hq1 : (2 : ℤ) ^ q' * Γ.lo ≤ Γ.F 0) (hq2 : Γ.F 0 < 2 ^ (q' + 1) * Γ.lo) : NarrowCycle m where
  x := Γ.Z
  a := Γ.c
  F := Γ.F
  lo := Γ.lo
  q := q'
  hm := Γ.hm
  periodic := Γ.Z_per
  arrow := Γ.c_arrow
  lower := Γ.Z_lower
  upper := Γ.Z_upper
  order := hord
  window i j := by
    have h1 := Γ.F_lt_two_F_zero i
    have h2 := Γ.F_zero_le hord j
    linarith
  hq1 i := le_trans hq1 (Γ.F_zero_le hord i)
  hq2 i := by
    have h1 := Γ.F_lt_two_F_zero i
    have h3 : (2 : ℤ) ^ (q' + 2) * Γ.lo = 2 * (2 ^ (q' + 1) * Γ.lo) := by ring
    rw [h3]
    linarith

/-- The normalised and original totals agree over a period: `Σ c_i = Σ a_i` (the height
coboundary telescopes). -/
theorem sum_c : ∑ i ∈ Finset.range m, Γ.c i = ∑ i ∈ Finset.range m, Γ.a i := by
  have hshift : ∑ i ∈ Finset.range m, Γ.h (i + 1) = ∑ i ∈ Finset.range m, Γ.h i :=
    NarrowCycle.sum_range_shift Γ.h (by simpa using Γ.h_per 0)
  have hc : ∀ i ∈ Finset.range m, Γ.c i + Γ.h i = Γ.a i + Γ.h (i + 1) := fun i _ => by
    unfold c
    have := Γ.h_le_a_add i
    omega
  have := Finset.sum_congr rfl hc
  rw [Finset.sum_add_distrib, Finset.sum_add_distrib, hshift] at this
  omega

/-- **C005 §2, the three-band restriction at `q = 1`.** A primitive odd cycle of the `3x+1`
map with `m ≥ 2` and all dyadic heights at most `2` (`H < 8L`) has mechanical normalised
exponents: there are `q'` and `h'` coprime to `m` with `c_i = q' + ⌊(i+1)h'/m⌋ − ⌊ih'/m⌋`,
and the total `A = Σ a_i = Σ c_i = mq' + h'` is coprime to `m`. -/
theorem three_band (hq1 : Γ.q = 1) (hB2 : Γ.B ≤ 2) (hm2 : 2 ≤ m)
    (hprim : ∀ i j, i < m → j < m → Γ.n i = Γ.n j → i = j) :
    ∃ q' h' : ℕ, Nat.Coprime h' m ∧ (∀ i, Γ.c i = q' + (((i + 1) * h') / m - (i * h') / m)) ∧
      ∑ i ∈ Finset.range m, Γ.a i = m * q' + h' ∧
      Nat.Coprime (∑ i ∈ Finset.range m, Γ.a i) m := by
  have hord := Γ.order_of_three_band hq1 hB2 hprim
  have hlo : 0 < Γ.lo := by
    unfold lo
    exact mul_pos (by positivity) Γ.npos
  have hd : (0 : ℤ) < 2 ^ Γ.B * Γ.q := mul_pos (by positivity) Γ.hq
  obtain ⟨q', hq1', hq2'⟩ := exists_exponent hlo hd
  rw [← Γ.F_zero] at hq1' hq2'
  set N : NarrowCycle m := Γ.toNarrow hord q' hq1' hq2' with hN
  have hx : ∀ i, N.x i = Γ.Z i := fun _ => rfl
  have ha : ∀ i, N.a i = Γ.c i := fun _ => rfl
  have hq : N.q = q' := rfl
  have hp : N.Primitive := by
    unfold NarrowCycle.Primitive
    intro i j hi hj h
    exact hprim i j hi hj (Γ.Z_inj h).2
  have hh := N.numHigh_lt hp hm2
  have h0 : N.rank 0 = 0 := by
    unfold NarrowCycle.rank
    apply Finset.sum_eq_zero
    intro j _
    rw [hx, hx, Γ.Z_zero]
    exact ite_eq_right (not_lt.mpr (Γ.Z_lower j))
  have hsum : ∑ i ∈ Finset.range m, Γ.a i = m * q' + N.numHigh := by
    rw [← Γ.sum_c]
    have := N.sum_a
    rw [hq] at this
    exact this
  refine ⟨q', N.numHigh, N.coprime_numHigh hp hm2, ?_, hsum, ?_⟩
  · intro i
    rw [← ha, N.a_formula hh h0 i, hq]
  · rw [hsum]
    exact (Nat.coprime_mul_left_add_left _ _ _).mpr (N.coprime_numHigh hp hm2)

/-- **C005's denominator corollary**, contrapositive form: a primitive odd cycle with `m ≥ 2`,
heights at most `2` and `gcd(A, m) > 1` is not a `3x+1` cycle (`q ≠ 1`). -/
theorem q_ne_one_of_not_coprime (hB2 : Γ.B ≤ 2) (hm2 : 2 ≤ m)
    (hprim : ∀ i j, i < m → j < m → Γ.n i = Γ.n j → i = j)
    (hg : ¬ Nat.Coprime (∑ i ∈ Finset.range m, Γ.a i) m) : Γ.q ≠ 1 := by
  intro hq1
  obtain ⟨_, _, _, _, _, hcop⟩ := Γ.three_band hq1 hB2 hm2 hprim
  exact hg hcop

/-! #### C007 `HEIGHT_DENOMINATOR.md` §§2–3: the modular lemma and the min–top inequality -/

/-- The prefix sums `P_i = Σ_{j<i} c_j` of the normalised word. -/
def P (i : ℕ) : ℕ := ∑ j ∈ Finset.range i, Γ.c j

/-- C007's modular lemma (2) in integer form: `2^{P_i} Z_i ≡ 3^i Z_0 (mod q)`, i.e.
`z_i ≡ L 3^i 2^{−P_i}` once the powers of two are inverted modulo `q`; the height profile does
not appear. -/
theorem residue_law (i : ℕ) : (2 : ℤ) ^ Γ.P i * Γ.Z i ≡ 3 ^ i * Γ.Z 0 [ZMOD Γ.q] := by
  induction i with
  | zero => simp [P]
  | succ i ih =>
    have harrow := Γ.c_arrow i
    have hP : Γ.P (i + 1) = Γ.P i + Γ.c i := by
      unfold P
      rw [Finset.sum_range_succ]
    rw [hP, pow_add, mul_assoc, harrow]
    unfold F
    have e : (2 : ℤ) ^ Γ.P i * (3 * Γ.Z i + 2 ^ (Γ.B - Γ.h i) * Γ.q)
        = 3 * (2 ^ Γ.P i * Γ.Z i) + Γ.q * (2 ^ Γ.P i * 2 ^ (Γ.B - Γ.h i)) := by ring
    rw [e, pow_succ]
    calc 3 * (2 ^ Γ.P i * Γ.Z i) + Γ.q * (2 ^ Γ.P i * 2 ^ (Γ.B - Γ.h i))
        ≡ 3 * (3 ^ i * Γ.Z 0) + 0 [ZMOD Γ.q] :=
          Int.ModEq.add (Int.ModEq.mul_left 3 ih)
            (Int.modEq_zero_iff_dvd.mpr (dvd_mul_right _ _))
      _ = 3 ^ i * 3 * Γ.Z 0 := by ring

/-- C007's modular lemma: when `3 ∤ q`, no numerator is divisible by `3`. -/
theorem three_not_dvd (hq3 : ¬ (3 : ℤ) ∣ Γ.q) (i : ℕ) : ¬ (3 : ℤ) ∣ Γ.n i := by
  intro h3
  have harrow := Γ.arrow (i + m - 1)
  have hidx : i + m - 1 + 1 = i + m := by
    have := Γ.hm
    omega
  rw [hidx, Γ.nper] at harrow
  have h1 : (3 : ℤ) ∣ 3 * Γ.n (i + m - 1) + Γ.q := by
    rw [← harrow]
    exact dvd_mul_of_dvd_right h3 _
  have h2 := dvd_sub h1 (dvd_mul_right 3 (Γ.n (i + m - 1)))
  rw [add_sub_cancel_left] at h2
  exact hq3 h2

/-- A divisor of `q` coprime to `2` that divides one numerator divides the next. -/
theorem dvd_succ_of_dvd {p : ℤ} (hp : p ∣ Γ.q) (hp2 : IsCoprime p 2) {i : ℕ} (hi : p ∣ Γ.n i) :
    p ∣ Γ.n (i + 1) := by
  have harrow := Γ.arrow i
  have h1 : p ∣ (2 : ℤ) ^ Γ.a i * Γ.n (i + 1) := by
    rw [harrow]
    exact dvd_add (dvd_mul_of_dvd_right hi 3) hp
  exact hp2.pow_right.dvd_of_dvd_mul_left h1

/-- Hence such a divisor divides every numerator: a reduced cycle (numerators with no common
factor) has all numerators coprime to `q` — C007's "every numerator is a unit modulo `6q`",
together with `three_not_dvd` and oddness. -/
theorem dvd_all_of_dvd {p : ℤ} (hp : p ∣ Γ.q) (hp2 : IsCoprime p 2) {i : ℕ} (hi : p ∣ Γ.n i)
    (j : ℕ) : p ∣ Γ.n j := by
  have hk : ∀ k, p ∣ Γ.n (i + k) := by
    intro k
    induction k with
    | zero => simpa using hi
    | succ k ih => exact Γ.dvd_succ_of_dvd hp hp2 ih
  have hle : i ≤ j + m * i := le_trans (Nat.le_mul_of_pos_left i Γ.hm) (Nat.le_add_left _ _)
  have := hk (j + m * i - i)
  rw [Nat.add_sub_of_le hle, Γ.n_add_mul] at this
  exact this

/-- C007's min–top inequality (3): in an ordered cycle every state above the minimum
satisfies `q(2^{h_j} − 1) < 3(n_j − 2^{h_j} n_0)`; at the top band `h_j = B` this is
`3r > q(2^B − 1)` with `r = n_j − 2^B L`. -/
theorem min_top (hord : ∀ i j, Γ.Z i < Γ.Z j ↔ Γ.F i < Γ.F j) {j : ℕ} (hj : Γ.Z 0 < Γ.Z j) :
    Γ.q * (2 ^ Γ.h j - 1) < 3 * (Γ.n j - 2 ^ Γ.h j * Γ.n 0) := by
  have hF := (hord 0 j).mp hj
  have hsub := Γ.F_sub_of_le (i := 0) (j := j) (by rw [Γ.h_zero]; exact Nat.zero_le _)
  rw [Γ.h_zero, Nat.sub_zero] at hsub
  have hpos : (0 : ℤ) < 2 ^ (Γ.B - Γ.h j) := by positivity
  have hprod : 0 < 2 ^ (Γ.B - Γ.h j)
      * (3 * (Γ.n j - 2 ^ Γ.h j * Γ.n 0) - Γ.q * (2 ^ Γ.h j - 1)) := by
    rw [← hsub]
    linarith
  by_contra hneg
  rw [not_lt] at hneg
  have hX : 3 * (Γ.n j - 2 ^ Γ.h j * Γ.n 0) - Γ.q * (2 ^ Γ.h j - 1) ≤ 0 := by linarith
  nlinarith

/-! #### C006 §§1, 3 on actual cycles: `c ≤ 2` under `q ≤ L`, chronological height steps -/

/-- Under `q ≤ L` every normalised exponent is at most `2` (C005 §1, C006 §1). -/
theorem c_le_two (hqL : Γ.q ≤ Γ.n 0) (i : ℕ) : Γ.c i ≤ 2 := by
  by_contra hgt
  rw [not_le] at hgt
  have harrow := Γ.c_arrow i
  have hZ := Γ.Z_lower (i + 1)
  have hZi := Γ.Z_upper i
  have hpow : (2 : ℤ) ^ 3 ≤ 2 ^ Γ.c i := pow_le_pow_right₀ (by norm_num) hgt
  have hlo : 0 < Γ.lo := by
    unfold lo
    exact mul_pos (by positivity) Γ.npos
  have hoff : (2 : ℤ) ^ (Γ.B - Γ.h i) * Γ.q ≤ Γ.lo := by
    unfold lo
    have h1 : (2 : ℤ) ^ (Γ.B - Γ.h i) ≤ 2 ^ Γ.B :=
      pow_le_pow_right₀ (by norm_num) (Nat.sub_le _ _)
    have h2 : (0 : ℤ) ≤ 2 ^ Γ.B := by positivity
    linarith [mul_le_mul_of_nonneg_right h1 Γ.hq.le, mul_le_mul_of_nonneg_left hqL h2]
  have hF : Γ.F i < 7 * Γ.lo := by
    unfold F
    linarith
  have h8 : (8 : ℤ) * Γ.lo ≤ 2 ^ Γ.c i * Γ.Z (i + 1) := by
    have h2c : (0 : ℤ) ≤ 2 ^ Γ.c i := by positivity
    linarith [mul_le_mul_of_nonneg_right hpow hlo.le, mul_le_mul_of_nonneg_left hZ h2c]
  linarith

/-- Chronological heights rise by at most one per odd step when `q ≤ L` and the valuation is
positive (the first half of C006's (H1)). -/
theorem h_succ_le (hqL : Γ.q ≤ Γ.n 0) (i : ℕ) (hai : 1 ≤ Γ.a i) : Γ.h (i + 1) ≤ Γ.h i + 1 := by
  have h1 := Γ.c_le_two hqL i
  have h2 := Γ.h_le_a_add i
  unfold c at h1
  omega

/-- Every height between `0` and an attained height is attained (C006 (H1)): with `q ≤ L` and
positive valuations, reaching height `h_j` from `h_0 = 0` visits all heights `0, …, h_j`. -/
theorem exists_height_eq (hqL : Γ.q ≤ Γ.n 0) (hapos : ∀ i, 1 ≤ Γ.a i) {j b : ℕ}
    (hb : b ≤ Γ.h j) : ∃ i, i ≤ j ∧ Γ.h i = b :=
  exists_eq_of_step_le Γ.h Γ.h_zero (fun i => Γ.h_succ_le hqL i (hapos i)) hb

/-! #### C008 `INDEPENDENT_MATCHING.md` §1 on actual cycles: the cycle identities and the
sorted-rank residue law -/

/-- The prefix totals `A_i = Σ_{j<i} a_j`. -/
def Apre (i : ℕ) : ℕ := ∑ j ∈ Finset.range i, Γ.a j

/-- The prefix intercepts `C_i = Σ_{j<i} 3^{i−1−j} 2^{A_j}`, by `C_{i+1} = 3 C_i + 2^{A_i}`. -/
def Cpre : ℕ → ℤ
  | 0 => 0
  | i + 1 => 3 * Cpre i + 2 ^ Γ.Apre i

theorem Apre_succ (i : ℕ) : Γ.Apre (i + 1) = Γ.Apre i + Γ.a i := by
  unfold Apre
  rw [Finset.sum_range_succ]

/-- The exact prefix identity `2^{A_i} n_i = 3^i n_0 + q C_i`. -/
theorem prefix_identity (i : ℕ) :
    (2 : ℤ) ^ Γ.Apre i * Γ.n i = 3 ^ i * Γ.n 0 + Γ.q * Γ.Cpre i := by
  induction i with
  | zero => simp [Apre, Cpre]
  | succ i ih =>
    rw [Γ.Apre_succ, pow_add]
    simp only [Cpre]
    calc (2 : ℤ) ^ Γ.Apre i * 2 ^ Γ.a i * Γ.n (i + 1)
        = 2 ^ Γ.Apre i * (2 ^ Γ.a i * Γ.n (i + 1)) := by ring
      _ = 2 ^ Γ.Apre i * (3 * Γ.n i + Γ.q) := by rw [Γ.arrow i]
      _ = 3 * (2 ^ Γ.Apre i * Γ.n i) + Γ.q * 2 ^ Γ.Apre i := by ring
      _ = 3 * (3 ^ i * Γ.n 0 + Γ.q * Γ.Cpre i) + Γ.q * 2 ^ Γ.Apre i := by rw [ih]
      _ = 3 ^ (i + 1) * Γ.n 0 + Γ.q * (3 * Γ.Cpre i + 2 ^ Γ.Apre i) := by ring

/-- The cycle identity `(2^A − 3^m) n_0 = q C_m`, `A = Σ_{j<m} a_j` (C005's (4), C006's (2)). -/
theorem cycle_identity : ((2 : ℤ) ^ Γ.Apre m - 3 ^ m) * Γ.n 0 = Γ.q * Γ.Cpre m := by
  have h := Γ.prefix_identity m
  rw [show Γ.n m = Γ.n 0 by simpa using Γ.nper 0] at h
  linarith

/-- For a reduced cycle (`q` coprime to its minimum), `q ∣ 2^A − 3^m`: C008's `Q ∣ D`. -/
theorem q_dvd_D (hcop : IsCoprime Γ.q (Γ.n 0)) : Γ.q ∣ (2 : ℤ) ^ Γ.Apre m - 3 ^ m := by
  have h : Γ.q ∣ ((2 : ℤ) ^ Γ.Apre m - 3 ^ m) * Γ.n 0 := ⟨Γ.Cpre m, Γ.cycle_identity⟩
  exact hcop.dvd_of_dvd_mul_right h

theorem Cpre_succ (i : ℕ) : Γ.Cpre (i + 1) = 3 * Γ.Cpre i + 2 ^ Γ.Apre i := rfl

/-- The prefix intercepts are positive from index `1` on. -/
theorem Cpre_pos (i : ℕ) : 0 < Γ.Cpre (i + 1) := by
  induction i with
  | zero =>
    rw [Γ.Cpre_succ]
    simp only [Cpre]
    positivity
  | succ i ih =>
    rw [Γ.Cpre_succ (i + 1)]
    have h2 : (0 : ℤ) < 2 ^ Γ.Apre (i + 1) := by positivity
    linarith

/-- `D = 2^A − 3^m` is positive for a positive cycle: `D n_0 = q C_m` with `q, C_m, n_0 > 0`. -/
theorem D_pos : 0 < (2 : ℤ) ^ Γ.Apre m - 3 ^ m := by
  have h := Γ.cycle_identity
  have hC : 0 < Γ.Cpre m := by
    have h1 := Γ.Cpre_pos (m - 1)
    have hm := Γ.hm
    rw [show m - 1 + 1 = m by omega] at h1
    exact h1
  have hqC : 0 < Γ.q * Γ.Cpre m := mul_pos Γ.hq hC
  have hn := Γ.npos
  by_contra hD
  rw [not_lt] at hD
  have : ((2 : ℤ) ^ Γ.Apre m - 3 ^ m) * Γ.n 0 ≤ 0 := mul_nonpos_of_nonpos_of_nonneg hD hn.le
  linarith

/-- With positive valuations the additive parameter is odd: `2^{a_0} n_1 = 3 n_0 + q` has an even
left side and `3 n_0` is odd. -/
theorem q_odd (hapos : ∀ i, 1 ≤ Γ.a i) : Odd Γ.q := by
  have harrow := Γ.arrow 0
  have heven : Even (2 ^ Γ.a 0 * Γ.n 1) :=
    even_iff_two_dvd.mpr (dvd_mul_of_dvd_left (dvd_pow_self 2 (by have := hapos 0; omega)) _)
  rw [harrow] at heven
  have h3 : Odd (3 * Γ.n 0) := Int.odd_mul.mpr ⟨⟨1, by norm_num⟩, Γ.nodd 0⟩
  have hne : ¬ Even (3 * Γ.n 0) := Int.not_even_iff_odd.mpr h3
  exact Int.not_even_iff_odd.mp (fun hq => hne ((Int.even_add.mp heven).mpr hq))

/-- `OVERLAP_THEORY.md` §1 (2): where the valuations of two phases agree, the state differences
`z_i = n_{i+k} − n_i` satisfy `2^{a_i} z_{i+1} = 3 z_i`. -/
theorem diff_step (i k : ℕ) (h : Γ.a (i + k) = Γ.a i) :
    (2 : ℤ) ^ Γ.a i * (Γ.n (i + k + 1) - Γ.n (i + 1)) = 3 * (Γ.n (i + k) - Γ.n i) := by
  have h1 := Γ.arrow i
  have h2 := Γ.arrow (i + k)
  rw [h] at h2
  linear_combination h2 - h1

/-- Along a run of `t` agreeing positions starting at `i`, `2^E z_{i+t} = 3^t z_i` with
`E = Σ_{j<t} a_{i+j}` (`OVERLAP_THEORY.md` §1, (3), via `run_pow_mul`). -/
theorem run_diff (i k t : ℕ) (hrun : ∀ j, j < t → Γ.a (i + j + k) = Γ.a (i + j)) :
    (2 : ℤ) ^ (∑ j ∈ Finset.range t, Γ.a (i + j)) * (Γ.n (i + t + k) - Γ.n (i + t))
      = 3 ^ t * (Γ.n (i + k) - Γ.n i) := by
  have h := run_pow_mul (fun j => Γ.n (i + j + k) - Γ.n (i + j)) (fun j => Γ.a (i + j)) t
    (fun j hj => by
      have := Γ.diff_step (i + j) k (hrun j hj)
      show (2 : ℤ) ^ Γ.a (i + j) * (Γ.n (i + (j + 1) + k) - Γ.n (i + (j + 1)))
        = 3 * (Γ.n (i + j + k) - Γ.n (i + j))
      rw [show i + (j + 1) + k = i + j + k + 1 by ring, show i + (j + 1) = i + j + 1 by ring]
      exact this)
  exact h

theorem toNarrow_primitive (hord : ∀ i j, Γ.Z i < Γ.Z j ↔ Γ.F i < Γ.F j) (q' : ℕ)
    (hq1 : (2 : ℤ) ^ q' * Γ.lo ≤ Γ.F 0) (hq2 : Γ.F 0 < 2 ^ (q' + 1) * Γ.lo)
    (hprim : ∀ i j, i < m → j < m → Γ.n i = Γ.n j → i = j) :
    (Γ.toNarrow hord q' hq1 hq2).Primitive := by
  unfold NarrowCycle.Primitive
  intro i j hi hj h
  exact hprim i j hi hj (Γ.Z_inj h).2

theorem toNarrow_rank_zero (hord : ∀ i j, Γ.Z i < Γ.Z j ↔ Γ.F i < Γ.F j) (q' : ℕ)
    (hq1 : (2 : ℤ) ^ q' * Γ.lo ≤ Γ.F 0) (hq2 : Γ.F 0 < 2 ^ (q' + 1) * Γ.lo) :
    (Γ.toNarrow hord q' hq1 hq2).rank 0 = 0 := by
  unfold NarrowCycle.rank
  apply Finset.sum_eq_zero
  intro j _
  show (if Γ.Z j < Γ.Z 0 then 1 else 0) = 0
  rw [Γ.Z_zero]
  exact ite_eq_right (not_lt.mpr (Γ.Z_lower j))

/-- C008's sorted-rank law (R1) in integer form: for an ordered primitive cycle, at time
`i < m` the state has sorted rank `(i h) mod m` and `2^{P_i} z_[rank_i] ≡ 3^i z_[0] (mod q)`,
with `P_i = Σ_{j<i} c_j = ⌊iA/m⌋` (`A = mq' + h`). Dividing by the unit `2^{P_i}` modulo `q`
and substituting `2 = t^m`, `3 = t^A` gives the prose's `z_[j] ≡ L t^j`. -/
theorem sorted_residue_law (hord : ∀ i j, Γ.Z i < Γ.Z j ↔ Γ.F i < Γ.F j) (q' : ℕ)
    (hq1 : (2 : ℤ) ^ q' * Γ.lo ≤ Γ.F 0) (hq2 : Γ.F 0 < 2 ^ (q' + 1) * Γ.lo) (hm2 : 2 ≤ m)
    (hprim : ∀ i j, i < m → j < m → Γ.n i = Γ.n j → i = j) {i : ℕ} (hi : i < m) :
    (2 : ℤ) ^ Γ.P i * (Γ.toNarrow hord q' hq1 hq2).y
        ((i * (Γ.toNarrow hord q' hq1 hq2).numHigh) % m)
      ≡ 3 ^ i * Γ.Z 0 [ZMOD Γ.q] ∧
    Γ.P i = (i * (m * q' + (Γ.toNarrow hord q' hq1 hq2).numHigh)) / m := by
  set N := Γ.toNarrow hord q' hq1 hq2 with hN
  have hp : N.Primitive := Γ.toNarrow_primitive hord q' hq1 hq2 hprim
  have h0 : N.rank 0 = 0 := Γ.toNarrow_rank_zero hord q' hq1 hq2
  have hh := N.numHigh_lt hp hm2
  have hx : ∀ j, N.x j = Γ.Z j := fun _ => rfl
  have ha : ∀ j, N.a j = Γ.c j := fun _ => rfl
  have hq : N.q = q' := rfl
  have hyi : N.y ((i * N.numHigh) % m) = Γ.Z i := by
    have hr := N.idx_spec hp (Nat.mod_lt (i * N.numHigh) N.hm)
    have hri : N.rank i = (i * N.numHigh) % m := by
      rw [N.rank_formula hh i, h0, Nat.zero_add]
    unfold NarrowCycle.y
    rw [← hx]
    exact N.x_eq_of_rank_eq hr.1 hi (hr.2.trans hri.symm)
  refine ⟨?_, ?_⟩
  · rw [hyi]
    exact Γ.residue_law i
  · have := N.sum_a_range hh h0 i
    rw [hq] at this
    unfold P
    simp_rw [← ha]
    exact this

end OddCycle

/-! ### C006 §3 on actual cycles: the height term `T_r`, the zero-forcing recurrence and the
per-run bound of the sparse-forcing law -/

/-- **The cyclic pigeonhole behind C006's (G1).** If `J ≥ 1` of the `m` positions of a cycle are
forced, some forced position is followed by `⌈m/J⌉ − 1 = ⌊(m−1)/J⌋` consecutive unforced ones.
Proof: otherwise every forced position is followed within `t = ⌊(m−1)/J⌋` steps by another, and
iterating `J` times from a forced position produces `J + 1` distinct forced positions inside an
arc of length `Jt + 1 ≤ m`. -/
theorem exists_run {m : ℕ} (hm : 0 < m) (forced : ℕ → Prop) [DecidablePred forced]
    (hJ : 0 < ((Finset.range m).filter forced).card) :
    ∃ k₀, k₀ < m ∧ forced k₀ ∧
      ∀ j, j < (m - 1) / ((Finset.range m).filter forced).card →
        ¬ forced ((k₀ + 1 + j) % m) := by
  classical
  by_cases hex : ∃ k₀, k₀ < m ∧ forced k₀ ∧
      ∀ j, j < (m - 1) / ((Finset.range m).filter forced).card →
        ¬ forced ((k₀ + 1 + j) % m)
  · exact hex
  exfalso
  have hstep : ∀ k, k < m → forced k → ∃ d, 1 ≤ d ∧
      d ≤ (m - 1) / ((Finset.range m).filter forced).card ∧ forced ((k + d) % m) := by
    intro k hk hf
    by_contra h2
    apply hex
    refine ⟨k, hk, hf, fun j hj hfj => h2 ⟨j + 1, by omega, by omega, ?_⟩⟩
    rw [show k + (j + 1) = k + 1 + j by ring]
    exact hfj
  choose! d hd using hstep
  obtain ⟨k₀, hk₀⟩ := Finset.card_pos.mp hJ
  have hk₀m : k₀ < m := Finset.mem_range.mp (Finset.mem_filter.mp hk₀).1
  have hk₀f : forced k₀ := (Finset.mem_filter.mp hk₀).2
  let pos : ℕ → ℕ := fun i => Nat.rec (motive := fun _ => ℕ) k₀ (fun _ p => (p + d p) % m) i
  have pos_zero : pos 0 = k₀ := rfl
  have pos_succ : ∀ i, pos (i + 1) = (pos i + d (pos i)) % m := fun _ => rfl
  have pos_prop : ∀ i, pos i < m ∧ forced (pos i) := by
    intro i
    induction i with
    | zero => exact ⟨hk₀m, hk₀f⟩
    | succ i ih =>
      rw [pos_succ]
      exact ⟨Nat.mod_lt _ hm, (hd (pos i) ih.1 ih.2).2.2⟩
  let s : ℕ → ℕ := fun i => ∑ j ∈ Finset.range i, d (pos j)
  have s_succ : ∀ i, s (i + 1) = s i + d (pos i) := fun i => Finset.sum_range_succ _ _
  have pos_eq : ∀ i, pos i = (k₀ + s i) % m := by
    intro i
    induction i with
    | zero =>
      rw [pos_zero]
      simp [s, Nat.mod_eq_of_lt hk₀m]
    | succ i ih =>
      rw [pos_succ, s_succ, ← Nat.add_assoc]
      have hmod : pos i ≡ k₀ + s i [MOD m] := by
        unfold Nat.ModEq
        rw [ih, Nat.mod_mod]
      exact hmod.add_right _
  have s_le : ∀ i, s i ≤ i * ((m - 1) / ((Finset.range m).filter forced).card) := by
    intro i
    induction i with
    | zero => simp [s]
    | succ i ih =>
      rw [s_succ, Nat.add_mul, Nat.one_mul]
      have := (hd (pos i) (pos_prop i).1 (pos_prop i).2).2.1
      omega
  have s_mono : StrictMono s := by
    apply strictMono_nat_of_lt_succ
    intro i
    rw [s_succ]
    have := (hd (pos i) (pos_prop i).1 (pos_prop i).2).1
    omega
  have hJt : ((Finset.range m).filter forced).card
      * ((m - 1) / ((Finset.range m).filter forced).card) ≤ m - 1 :=
    Nat.mul_div_le (m - 1) _
  have hinj : Set.InjOn pos (Finset.range (((Finset.range m).filter forced).card + 1) : Set ℕ) := by
    intro i hi i' hi' h
    simp only [Finset.coe_range, Set.mem_Iio] at hi hi'
    rw [pos_eq, pos_eq] at h
    have hsi : s i < m := by
      have h1 := s_le i
      have h2 : i * ((m - 1) / ((Finset.range m).filter forced).card)
          ≤ ((Finset.range m).filter forced).card
            * ((m - 1) / ((Finset.range m).filter forced).card) :=
        Nat.mul_le_mul_right _ (by omega)
      omega
    have hsi' : s i' < m := by
      have h1 := s_le i'
      have h2 : i' * ((m - 1) / ((Finset.range m).filter forced).card)
          ≤ ((Finset.range m).filter forced).card
            * ((m - 1) / ((Finset.range m).filter forced).card) :=
        Nat.mul_le_mul_right _ (by omega)
      omega
    have hmod : s i ≡ s i' [MOD m] := Nat.ModEq.add_left_cancel' k₀ h
    unfold Nat.ModEq at hmod
    rw [Nat.mod_eq_of_lt hsi, Nat.mod_eq_of_lt hsi'] at hmod
    exact s_mono.injective hmod
  have hmaps : ∀ i ∈ Finset.range (((Finset.range m).filter forced).card + 1),
      pos i ∈ (Finset.range m).filter forced := by
    intro i _
    exact Finset.mem_filter.mpr ⟨Finset.mem_range.mpr (pos_prop i).1, (pos_prop i).2⟩
  have hcard := Finset.card_le_card_of_injOn pos hmaps hinj
  rw [Finset.card_range] at hcard
  omega

/-- Adjacent changes bound the number of distinct values: a sequence on `{0, …, n}` takes at
most `1 + #{r < n : f(r+1) ≠ f r}` distinct values (the counting step of C006's (H1)). -/
theorem card_image_le_changes (f : ℕ → ℕ) (n : ℕ) :
    ((Finset.range (n + 1)).image f).card
      ≤ 1 + ((Finset.range n).filter (fun r => f (r + 1) ≠ f r)).card := by
  induction n with
  | zero => simp
  | succ n ih =>
    conv_lhs => rw [Finset.range_add_one, Finset.image_insert]
    conv_rhs => rw [Finset.range_add_one, Finset.filter_insert]
    by_cases h : f (n + 1) ≠ f n
    · have hn : n ∉ (Finset.range n).filter (fun r => f (r + 1) ≠ f r) := fun hmem =>
        lt_irrefl n (Finset.mem_range.mp (Finset.mem_filter.mp hmem).1)
      rw [ite_eq_left h, Finset.card_insert_of_notMem hn]
      have h1 := Finset.card_insert_le (f (n + 1)) ((Finset.range (n + 1)).image f)
      omega
    · rw [ite_eq_right h]
      have h' : f (n + 1) = f n := not_not.mp h
      have hmem : f (n + 1) ∈ (Finset.range (n + 1)).image f := by
        rw [h']
        exact Finset.mem_image_of_mem f (Finset.mem_range.mpr (Nat.lt_succ_self n))
      rw [Finset.card_insert_of_mem hmem]
      exact ih

/-! ### C009: the one-point deletion theorem for the first-return permutation

C009 (`FIRST_RETURN_ORDER.md`): for the rank shift `R(j) = (j + s) mod m` on `m ≥ 2` ranks with
`1 ≤ s < m`, delete rank `0` and take the first-return map on the retained ranks `1, …, m − 1`
(compressed to `0, …, m − 2`). The induced map is a circular rank shift if and only if `s = 1` or
`s = m − 1`. (The prose also assumes `gcd(s, m) = 1`; it is not needed for this statement. The
deleted rank is `0` without loss of generality, by rotating the circle.) -/

/-- The first-return map on the retained old ranks after deleting rank `0`: one step of
`j ↦ (j + s) mod m`, or two steps when the first lands on the deleted rank. -/
def retMap (m s j : ℕ) : ℕ := if (j + s) % m = 0 then (j + 2 * s) % m else (j + s) % m

/-- The compressed first-return permutation on `{0, …, m − 2}` (old rank `j + 1 ↦` new rank). -/
def compMap (m s j : ℕ) : ℕ := retMap m s (j + 1) - 1

/-- "The induced permutation is a circular rank shift": some `c` with
`compMap j = (j + c) mod (m − 1)` on all compressed ranks. -/
def IsRankShift (m s : ℕ) : Prop := ∃ c, ∀ j, j < m - 1 → compMap m s j = (j + c) % (m - 1)

theorem retMap_of_lt {m s j : ℕ} (h : j + s < m) (h0 : 0 < j + s) : retMap m s j = j + s := by
  unfold retMap
  rw [Nat.mod_eq_of_lt h]
  exact ite_eq_right (by omega)

theorem retMap_of_ge {m s j : ℕ} (h1 : m ≤ j + s) (h2 : j + s < 2 * m) (h0 : j + s ≠ m) :
    retMap m s j = j + s - m := by
  unfold retMap
  have hmod : (j + s) % m = j + s - m := by
    rw [Nat.mod_eq_sub_mod h1]
    exact Nat.mod_eq_of_lt (by omega)
  rw [hmod]
  exact ite_eq_right (by omega)

theorem retMap_of_eq {m s j : ℕ} (h : j + s = m) (hsm : s < m) : retMap m s j = s := by
  unfold retMap
  rw [h, Nat.mod_self, ite_eq_left rfl, show j + 2 * s = s + m by omega, Nat.add_mod_right,
    Nat.mod_eq_of_lt hsm]

/-- **C009's one-point deletion theorem.** For `m ≥ 2` and `1 ≤ s < m`, the compressed
first-return map after deleting one rank is a circular rank shift iff `s = 1` or `s = m − 1`.
For `2 ≤ s ≤ m − 2` the compressed shifts of old ranks `1` and `m − 1` are `s` and `s − 1`,
which differ modulo `m − 1`; for `s = 1` every compressed shift is `1`, for `s = m − 1` it is
`m − 2 ≡ −1`. -/
theorem one_point_deletion (m s : ℕ) (hm : 2 ≤ m) (hs1 : 1 ≤ s) (hsm : s < m) :
    IsRankShift m s ↔ (s = 1 ∨ s = m - 1) := by
  constructor
  · rintro ⟨c, hc⟩
    by_contra hne
    rw [not_or] at hne
    obtain ⟨hne1, hne2⟩ := hne
    have h0 := hc 0 (by omega)
    have h1 := hc (m - 2) (by omega)
    have hc0 : compMap m s 0 = s := by
      unfold compMap
      rw [retMap_of_lt (by omega) (by omega)]
      omega
    have hc1 : compMap m s (m - 2) = s - 2 := by
      unfold compMap
      rw [retMap_of_ge (by omega) (by omega) (by omega)]
      omega
    rw [hc0, zero_add] at h0
    rw [hc1] at h1
    have hcm : c % (m - 1) = s := h0.symm
    have hval : (m - 2 + c) % (m - 1) = s - 1 := by
      rw [Nat.add_mod, hcm, show (m - 2) % (m - 1) = m - 2 from Nat.mod_eq_of_lt (by omega),
        show m - 2 + s = (s - 1) + (m - 1) by omega, Nat.add_mod_right,
        Nat.mod_eq_of_lt (by omega)]
    omega
  · rintro (rfl | rfl)
    · refine ⟨1, fun j hj => ?_⟩
      unfold compMap
      rcases Nat.lt_or_ge (j + 2) m with hlt | hge
      · rw [retMap_of_lt (by omega) (by omega), Nat.mod_eq_of_lt (by omega)]
        omega
      · rw [retMap_of_eq (by omega) (by omega), show j + 1 = m - 1 by omega, Nat.mod_self]
    · refine ⟨m - 2, fun j hj => ?_⟩
      unfold compMap
      rcases Nat.eq_zero_or_pos j with hj0 | hjpos
      · subst hj0
        rw [retMap_of_eq (by omega) (by omega), Nat.zero_add, Nat.mod_eq_of_lt (by omega)]
        omega
      · rw [retMap_of_ge (by omega) (by omega) (by omega),
          show j + (m - 2) = (j - 1) + (m - 1) by omega, Nat.add_mod_right,
          Nat.mod_eq_of_lt (by omega)]
        omega

/-- C009's `q = 13` control in this normalisation: for `m = 5`, `s = 3` (the ordered cycle
`(283, 431, 653, 493, 373)` with the positive-height state deleted) the compressed first-return
map is `(3, 2, 0, 1)` — the prose's `(2, 0, 3, 1)` conjugated by the relabelling that puts the
deleted rank at `0` — and not a rank shift. -/
example : (List.range 4).map (compMap 5 3) = [3, 2, 0, 1] := by decide

example : ¬ IsRankShift 5 3 := by
  rw [one_point_deletion 5 3 (by norm_num) (by norm_num) (by norm_num)]
  omega

/-! ### C011: the two-arc identity and the two-defect cancellation bounds

C011 (`ROTATION_DEFECTS.md` §§2–3) compares a positive word `w` with a rotation `w'` differing from
it in exactly two positions; after cutting at the first mismatch and exchanging the roles if
necessary, `w = a :: (u₀ ++ (a + k) :: v₀)` and `w' = (a + k) :: (u₀ ++ a :: v₀)` with `k ≥ 1`.
With the complementary arcs `u = u₀ ++ [a + k]` and `v = v₀ ++ [a]`, `g = gcd(C_w, D_w)` divides
`(2^k − 1) gcd(C_u, C_v)` (its (2)), and the intercept bound `C_z ≤ 2^{S−l−(b−1)} (3^l − 2^l)`
for a word of length `l`, total `S` and last letter `b` (its (4)) gives
`g² < (2^k − 1)² 2^{A−m−k−2a+2} 3^m` (its (5)) and `g² < 2^{2A−2m} 3^m` (its (7)). Everything is
kept in cleared integer form. The combinatorial reduction of an arbitrary two-defect rotation to
this normal form, the real-analytic (6)–(8) and the imported Matveev/Hercher inputs of
`EXCLUSION.md` are not formalised. -/

/-- The intercept of a word does not depend on its last letter: `C (z ++ [b]) = 3 C_z + 2^{Σz}`. -/
theorem C_append_singleton (z : List ℕ) (b : ℕ) : C (z ++ [b]) = 3 * C z + 2 ^ z.sum := by
  rw [C_append]
  simp [C]

/-- C011's two-arc identity (1): `C_{w'} − C_w = (2^k − 1) 2^a 3^{|v₀|} C_u`, `u = u₀ ++ [a + k]`. -/
theorem two_arc_identity (a k : ℕ) (u₀ v₀ : List ℕ) :
    C ((a + k) :: (u₀ ++ a :: v₀)) - C (a :: (u₀ ++ (a + k) :: v₀))
      = (2 ^ k - 1) * 2 ^ a * 3 ^ v₀.length * C (u₀ ++ [a + k]) := by
  rw [C_append_singleton]
  simp only [C, C_append, List.length_append, List.length_cons, pow_add, pow_succ]
  ring

/-- The cut at the second mismatch is a rotation: rotating `x :: (u₀ ++ y :: v₀)` by `|u₀| + 1`
gives `y :: (v₀ ++ x :: u₀)`. -/
theorem rotate_cut (x y : ℕ) (u₀ v₀ : List ℕ) :
    (x :: (u₀ ++ y :: v₀)).rotate (u₀.length + 1) = y :: (v₀ ++ x :: u₀) := by
  have h1 : x :: (u₀ ++ y :: v₀) = (x :: u₀) ++ (y :: v₀) := by simp
  have h2 : y :: (v₀ ++ x :: u₀) = (y :: v₀) ++ (x :: u₀) := by simp
  rw [h1, h2, show u₀.length + 1 = (x :: u₀).length by simp,
    List.rotate_eq_drop_append_take (by simp), List.drop_left, List.take_left]

/-- `D_w` is coprime to `3` (`3 ∤ D_w`). -/
theorem isCoprime_three_D {w : List ℕ} (hw : 1 ≤ w.length) : IsCoprime (3 : ℤ) (D w) := by
  rw [Int.isCoprime_iff_gcd_eq_one]
  have h1 : Int.gcd 3 (D w) ∣ 3 := by
    have := Int.gcd_dvd_left (3 : ℤ) (D w)
    exact_mod_cast this
  rcases (Nat.dvd_prime Nat.prime_three).mp h1 with h | h
  · exact h
  · exfalso
    apply D_not_three_dvd hw
    have := Int.gcd_dvd_right (3 : ℤ) (D w)
    rw [h] at this
    exact_mod_cast this

/-- Every common divisor `g` of `C_w` and `D_w` that is coprime to `2` divides every rotated
intercept (the recurrence `2^{a_i} C_{(i+1)} = 3 C_{(i)} + D_w`). -/
theorem dvd_C_rotate_of_dvd {w : List ℕ} (hw0 : w ≠ []) {g : ℤ} (hg2 : IsCoprime g 2)
    (hgC : g ∣ C w) (hgD : g ∣ D w) : ∀ i, g ∣ C (w.rotate i) := by
  intro i
  induction i with
  | zero => simpa using hgC
  | succ i ih =>
    obtain ⟨a, v, hav⟩ : ∃ a v, w.rotate i = a :: v := by
      cases hrot : w.rotate i with
      | nil => exact absurd (List.rotate_eq_nil_iff.mp hrot) hw0
      | cons a v => exact ⟨a, v, rfl⟩
    have hrec := C_rotate_succ hav
    have h2 : g ∣ 2 ^ a * C (w.rotate (i + 1)) := by
      rw [hrec]
      exact dvd_add (dvd_mul_of_dvd_right ih 3) hgD
    exact (hg2.pow_right).dvd_of_dvd_mul_left h2

/-- `g = gcd(C_w, D_w)` is coprime to `2` (it divides the odd `D_w`). -/
theorem gcd_isCoprime_two {w : List ℕ} (hw : 1 ≤ w.sum) :
    IsCoprime ((Int.gcd (C w) (D w) : ℕ) : ℤ) 2 :=
  (isCoprime_two_D hw).symm.of_isCoprime_of_dvd_left (Int.gcd_dvd_right _ _)

/-- `g = gcd(C_w, D_w)` is coprime to `3`. -/
theorem gcd_isCoprime_three {w : List ℕ} (hw : 1 ≤ w.length) :
    IsCoprime ((Int.gcd (C w) (D w) : ℕ) : ℤ) 3 :=
  (isCoprime_three_D hw).symm.of_isCoprime_of_dvd_left (Int.gcd_dvd_right _ _)

/-- C011's (2): in the two-defect normal form `w = a :: (u₀ ++ (a + k) :: v₀)` with
`w' = (a + k) :: (u₀ ++ a :: v₀)` a rotation of `w` and `k ≥ 1`, `g = gcd(C_w, D_w)` divides
`(2^k − 1) gcd(C_u, C_v)` for the complementary arcs `u = u₀ ++ [a + k]`, `v = v₀ ++ [a]`. -/
theorem two_arc_dvd (a k : ℕ) (hk : 1 ≤ k) (u₀ v₀ : List ℕ)
    (hrot : ∃ r, (a :: (u₀ ++ (a + k) :: v₀)).rotate r = (a + k) :: (u₀ ++ a :: v₀)) :
    ((Int.gcd (C (a :: (u₀ ++ (a + k) :: v₀))) (D (a :: (u₀ ++ (a + k) :: v₀))) : ℕ) : ℤ)
      ∣ (2 ^ k - 1) * ((Int.gcd (C (u₀ ++ [a + k])) (C (v₀ ++ [a])) : ℕ) : ℤ) := by
  obtain ⟨r, hr⟩ := hrot
  have hw0 : a :: (u₀ ++ (a + k) :: v₀) ≠ [] := List.cons_ne_nil _ _
  have hsum : 1 ≤ (a :: (u₀ ++ (a + k) :: v₀)).sum := by
    simp only [List.sum_cons, List.sum_append]
    omega
  have hlen : 1 ≤ (a :: (u₀ ++ (a + k) :: v₀)).length := by simp
  have hg2 := gcd_isCoprime_two hsum
  have hg3 := gcd_isCoprime_three hlen
  have hgC : ((Int.gcd (C (a :: (u₀ ++ (a + k) :: v₀))) (D (a :: (u₀ ++ (a + k) :: v₀))) : ℕ) : ℤ)
      ∣ C (a :: (u₀ ++ (a + k) :: v₀)) := Int.gcd_dvd_left _ _
  have hgD : ((Int.gcd (C (a :: (u₀ ++ (a + k) :: v₀))) (D (a :: (u₀ ++ (a + k) :: v₀))) : ℕ) : ℤ)
      ∣ D (a :: (u₀ ++ (a + k) :: v₀)) := Int.gcd_dvd_right _ _
  have hrotall := dvd_C_rotate_of_dvd hw0 hg2 hgC hgD
  set g : ℤ :=
    ((Int.gcd (C (a :: (u₀ ++ (a + k) :: v₀))) (D (a :: (u₀ ++ (a + k) :: v₀))) : ℕ) : ℤ) with hg
  -- the first arc
  have hu : g ∣ (2 ^ k - 1) * C (u₀ ++ [a + k]) := by
    have hdiff : g ∣ C ((a + k) :: (u₀ ++ a :: v₀)) - C (a :: (u₀ ++ (a + k) :: v₀)) := by
      have := hrotall r
      rw [hr] at this
      exact dvd_sub this hgC
    rw [two_arc_identity, show (2 ^ k - 1) * 2 ^ a * 3 ^ v₀.length * C (u₀ ++ [a + k])
        = (2 ^ a * 3 ^ v₀.length) * ((2 ^ k - 1) * C (u₀ ++ [a + k])) by ring] at hdiff
    exact ((hg2.pow_right).mul_right (hg3.pow_right)).dvd_of_dvd_mul_left hdiff
  -- the second arc: cut at the other mismatch
  have hv : g ∣ (2 ^ k - 1) * C (v₀ ++ [a]) := by
    have hW : g ∣ C ((a + k) :: (v₀ ++ a :: u₀)) := by
      have := hrotall (u₀.length + 1)
      rwa [rotate_cut] at this
    have hW' : g ∣ C (a :: (v₀ ++ (a + k) :: u₀)) := by
      have := hrotall (r + (u₀.length + 1))
      rwa [← List.rotate_rotate, hr, rotate_cut] at this
    have hdiff := dvd_sub hW hW'
    rw [two_arc_identity, show (2 ^ k - 1) * 2 ^ a * 3 ^ u₀.length * C (v₀ ++ [a + k])
        = (2 ^ a * 3 ^ u₀.length) * ((2 ^ k - 1) * C (v₀ ++ [a + k])) by ring] at hdiff
    have := ((hg2.pow_right).mul_right (hg3.pow_right)).dvd_of_dvd_mul_left hdiff
    rwa [C_append_singleton, ← C_append_singleton v₀ a] at this
  have hX1 : (1 : ℤ) ≤ 2 ^ k := one_le_pow₀ (by norm_num)
  have hX0 : (0 : ℤ) ≤ 2 ^ k - 1 := by linarith
  have hdvd := Int.dvd_gcd hu hv
  rw [Int.gcd_mul_left] at hdvd
  have h' : ((Int.gcd (C (a :: (u₀ ++ (a + k) :: v₀))) (D (a :: (u₀ ++ (a + k) :: v₀))) : ℕ) : ℤ)
      ∣ (((2 ^ k - 1 : ℤ).natAbs * Int.gcd (C (u₀ ++ [a + k])) (C (v₀ ++ [a])) : ℕ) : ℤ) :=
    Int.natCast_dvd_natCast.mpr hdvd
  rw [Nat.cast_mul, Int.natAbs_of_nonneg hX0] at h'
  exact h'

/-- C011's (4) for a word with last letter `b`, in cleared form: `2^{l−1} C_z ≤ 2^{S−b} (3^l − 2^l)`
with `z = z₀ ++ [b]`, `l = |z₀| + 1`, `S − b = Σ z₀` (the last letter does not enter). -/
theorem intercept_bound_last (z₀ : List ℕ) (b : ℕ) (hz : ∀ x ∈ z₀, 1 ≤ x) :
    (2 : ℤ) ^ z₀.length * C (z₀ ++ [b])
      ≤ 2 ^ z₀.sum * (3 ^ (z₀.length + 1) - 2 ^ (z₀.length + 1)) := by
  rw [C_append_singleton]
  have h := two_pow_mul_C_le z₀ hz
  have h3 : (2 : ℤ) ^ z₀.length * (3 * C z₀ + 2 ^ z₀.sum)
      = 3 * (2 ^ z₀.length * C z₀) + 2 ^ z₀.length * 2 ^ z₀.sum := by ring
  rw [h3, pow_succ, pow_succ]
  linarith

/-- The arithmetic of C011's (5): from `G ≤ X H`, `H ≤ C_u, C_v`, the cleared intercept bounds
`P_u C_u ≤ B_u < T_u`, `P_v C_v ≤ B_v < T_v`, one gets `G² P_u P_v < X² T_u T_v`. -/
theorem two_defect_arith {G H X Cu Cv Pu Pv Bu Bv Tu Tv : ℤ} (hG0 : 0 ≤ G) (hX : 0 < X)
    (hH0 : 0 ≤ H) (hGXH : G ≤ X * H) (hHu : H ≤ Cu) (hHv : H ≤ Cv) (hPu : 0 ≤ Pu)
    (hPv : 0 ≤ Pv) (hbu : Pu * Cu ≤ Bu) (hbv : Pv * Cv ≤ Bv) (hBuT : Bu < Tu) (hBvT : Bv < Tv)
    (hTu : 0 < Tu) : G ^ 2 * (Pu * Pv) < X ^ 2 * (Tu * Tv) := by
  have hPuPv : 0 ≤ Pu * Pv := mul_nonneg hPu hPv
  have h1 : G ^ 2 ≤ (X * H) ^ 2 := pow_le_pow_left₀ hG0 hGXH 2
  have hPuH : Pu * H ≤ Bu := le_trans (mul_le_mul_of_nonneg_left hHu hPu) hbu
  have hPvH : Pv * H ≤ Bv := le_trans (mul_le_mul_of_nonneg_left hHv hPv) hbv
  have hPuH0 : 0 ≤ Pu * H := mul_nonneg hPu hH0
  have hPvH0 : 0 ≤ Pv * H := mul_nonneg hPv hH0
  have hBu0 : 0 ≤ Bu := le_trans hPuH0 hPuH
  have hBv0 : 0 ≤ Bv := le_trans hPvH0 hPvH
  have hX2 : 0 < X ^ 2 := pow_pos hX 2
  calc G ^ 2 * (Pu * Pv) ≤ (X * H) ^ 2 * (Pu * Pv) := mul_le_mul_of_nonneg_right h1 hPuPv
    _ = X ^ 2 * ((Pu * H) * (Pv * H)) := by ring
    _ ≤ X ^ 2 * (Bu * Bv) :=
        mul_le_mul_of_nonneg_left (mul_le_mul hPuH hPvH hPvH0 hBu0) hX2.le
    _ < X ^ 2 * (Tu * Tv) := by
        apply mul_lt_mul_of_pos_left _ hX2
        calc Bu * Bv ≤ Tu * Bv := mul_le_mul_of_nonneg_right hBuT.le hBv0
          _ < Tu * Tv := mul_lt_mul_of_pos_left hBvT hTu

/-- C011's (5) in cleared integer form: in the two-defect normal form (`k ≥ 1`, positive arcs),
`g² · 2^{|u₀| + |v₀|} < (2^k − 1)² · 2^{Σu₀ + Σv₀} · 3^m` with `m = |u₀| + |v₀| + 2`, i.e.
`g² < (2^k − 1)² 2^{A − m − k − 2a + 2} 3^m`. -/
theorem two_defect_bound_sharp (a k : ℕ) (hk : 1 ≤ k) (u₀ v₀ : List ℕ)
    (hu : ∀ x ∈ u₀, 1 ≤ x) (hv : ∀ x ∈ v₀, 1 ≤ x)
    (hrot : ∃ r, (a :: (u₀ ++ (a + k) :: v₀)).rotate r = (a + k) :: (u₀ ++ a :: v₀)) :
    ((Int.gcd (C (a :: (u₀ ++ (a + k) :: v₀))) (D (a :: (u₀ ++ (a + k) :: v₀))) : ℕ) : ℤ) ^ 2
        * 2 ^ (u₀.length + v₀.length)
      < (2 ^ k - 1) ^ 2 * 2 ^ (u₀.sum + v₀.sum) * 3 ^ (u₀.length + v₀.length + 2) := by
  have hg := two_arc_dvd a k hk u₀ v₀ hrot
  have hG0 : (0 : ℤ) ≤
      ((Int.gcd (C (a :: (u₀ ++ (a + k) :: v₀))) (D (a :: (u₀ ++ (a + k) :: v₀))) : ℕ) : ℤ) :=
    Nat.cast_nonneg _
  have hH0 : (0 : ℤ) ≤ ((Int.gcd (C (u₀ ++ [a + k])) (C (v₀ ++ [a])) : ℕ) : ℤ) :=
    Nat.cast_nonneg _
  have hCu : 0 < C (u₀ ++ [a + k]) := C_pos (by simp)
  have hCv : 0 < C (v₀ ++ [a]) := C_pos (by simp)
  have hHpos : (0 : ℤ) < ((Int.gcd (C (u₀ ++ [a + k])) (C (v₀ ++ [a])) : ℕ) : ℤ) := by
    have := Int.gcd_pos_of_ne_zero_left (C (v₀ ++ [a])) hCu.ne'
    exact_mod_cast this
  have hHu : ((Int.gcd (C (u₀ ++ [a + k])) (C (v₀ ++ [a])) : ℕ) : ℤ) ≤ C (u₀ ++ [a + k]) :=
    Int.le_of_dvd hCu (Int.gcd_dvd_left _ _)
  have hHv : ((Int.gcd (C (u₀ ++ [a + k])) (C (v₀ ++ [a])) : ℕ) : ℤ) ≤ C (v₀ ++ [a]) :=
    Int.le_of_dvd hCv (Int.gcd_dvd_right _ _)
  have hX : (0 : ℤ) < 2 ^ k - 1 := by
    have : (1 : ℤ) < 2 ^ k := one_lt_pow₀ (by norm_num) (by omega)
    linarith
  have hGXH := Int.le_of_dvd (mul_pos hX hHpos) hg
  have hbu := intercept_bound_last u₀ (a + k) hu
  have hbv := intercept_bound_last v₀ a hv
  have hBuT : (2 : ℤ) ^ u₀.sum * (3 ^ (u₀.length + 1) - 2 ^ (u₀.length + 1))
      < 2 ^ u₀.sum * 3 ^ (u₀.length + 1) :=
    mul_lt_mul_of_pos_left (sub_lt_self _ (by positivity)) (by positivity)
  have hBvT : (2 : ℤ) ^ v₀.sum * (3 ^ (v₀.length + 1) - 2 ^ (v₀.length + 1))
      < 2 ^ v₀.sum * 3 ^ (v₀.length + 1) :=
    mul_lt_mul_of_pos_left (sub_lt_self _ (by positivity)) (by positivity)
  have key := two_defect_arith hG0 hX hH0 hGXH hHu hHv (by positivity) (by positivity) hbu hbv
    hBuT hBvT (by positivity)
  calc ((Int.gcd (C (a :: (u₀ ++ (a + k) :: v₀))) (D (a :: (u₀ ++ (a + k) :: v₀))) : ℕ) : ℤ) ^ 2
        * 2 ^ (u₀.length + v₀.length)
      = ((Int.gcd (C (a :: (u₀ ++ (a + k) :: v₀))) (D (a :: (u₀ ++ (a + k) :: v₀))) : ℕ) : ℤ) ^ 2
        * (2 ^ u₀.length * 2 ^ v₀.length) := by rw [pow_add]
    _ < (2 ^ k - 1) ^ 2 * ((2 ^ u₀.sum * 3 ^ (u₀.length + 1)) * (2 ^ v₀.sum * 3 ^ (v₀.length + 1))) :=
        key
    _ = (2 ^ k - 1) ^ 2 * 2 ^ (u₀.sum + v₀.sum) * 3 ^ (u₀.length + v₀.length + 2) := by ring

/-- C011's (7) in cleared integer form: `g² · 2^{2m} < 2^{2A} · 3^m`, i.e. `g² < 2^{2A−2m} 3^m`, for
the two-defect normal form with `a, k ≥ 1` and positive arcs (`A = Σw`, `m = |w|`). -/
theorem two_defect_bound (a k : ℕ) (ha : 1 ≤ a) (hk : 1 ≤ k) (u₀ v₀ : List ℕ)
    (hu : ∀ x ∈ u₀, 1 ≤ x) (hv : ∀ x ∈ v₀, 1 ≤ x)
    (hrot : ∃ r, (a :: (u₀ ++ (a + k) :: v₀)).rotate r = (a + k) :: (u₀ ++ a :: v₀)) :
    ((Int.gcd (C (a :: (u₀ ++ (a + k) :: v₀))) (D (a :: (u₀ ++ (a + k) :: v₀))) : ℕ) : ℤ) ^ 2
        * 2 ^ (2 * (a :: (u₀ ++ (a + k) :: v₀)).length)
      < 2 ^ (2 * (a :: (u₀ ++ (a + k) :: v₀)).sum) * 3 ^ (a :: (u₀ ++ (a + k) :: v₀)).length := by
  have hsharp := two_defect_bound_sharp a k hk u₀ v₀ hu hv hrot
  have hlen : (a :: (u₀ ++ (a + k) :: v₀)).length = u₀.length + v₀.length + 2 := by
    simp only [List.length_cons, List.length_append]
    omega
  have hsum : (a :: (u₀ ++ (a + k) :: v₀)).sum = a + u₀.sum + (a + k) + v₀.sum := by
    simp only [List.sum_cons, List.sum_append]
    omega
  rw [hlen, hsum]
  set G : ℤ :=
    ((Int.gcd (C (a :: (u₀ ++ (a + k) :: v₀))) (D (a :: (u₀ ++ (a + k) :: v₀))) : ℕ) : ℤ) with hG
  have hX1 : (1 : ℤ) ≤ 2 ^ k := one_le_pow₀ (by norm_num)
  have hX0 : (0 : ℤ) ≤ 2 ^ k - 1 := by linarith
  have hX : (2 : ℤ) ^ k - 1 < 2 ^ k := sub_one_lt _
  have hX2 : ((2 : ℤ) ^ k - 1) ^ 2 ≤ (2 ^ k) ^ 2 := by
    rw [sq, sq]
    exact (mul_self_lt_mul_self hX0 hX).le
  have hlu := List.length_le_sum_of_one_le u₀ hu
  have hlv := List.length_le_sum_of_one_le v₀ hv
  have hexp : 2 * k + (u₀.sum + v₀.sum) + (u₀.length + v₀.length + 4)
      ≤ 2 * (a + u₀.sum + (a + k) + v₀.sum) := by omega
  have hpow : (2 : ℤ) ^ (2 * k + (u₀.sum + v₀.sum) + (u₀.length + v₀.length + 4))
      ≤ 2 ^ (2 * (a + u₀.sum + (a + k) + v₀.sum)) := pow_le_pow_right₀ (by norm_num) hexp
  have hQ : (0 : ℤ) < 2 ^ (u₀.length + v₀.length + 4) := by positivity
  calc G ^ 2 * 2 ^ (2 * (u₀.length + v₀.length + 2))
      = (G ^ 2 * 2 ^ (u₀.length + v₀.length)) * 2 ^ (u₀.length + v₀.length + 4) := by ring
    _ < ((2 ^ k - 1) ^ 2 * 2 ^ (u₀.sum + v₀.sum) * 3 ^ (u₀.length + v₀.length + 2))
          * 2 ^ (u₀.length + v₀.length + 4) := mul_lt_mul_of_pos_right hsharp hQ
    _ ≤ ((2 ^ k) ^ 2 * 2 ^ (u₀.sum + v₀.sum) * 3 ^ (u₀.length + v₀.length + 2))
          * 2 ^ (u₀.length + v₀.length + 4) := by
        apply mul_le_mul_of_nonneg_right _ hQ.le
        apply mul_le_mul_of_nonneg_right _ (by positivity)
        exact mul_le_mul_of_nonneg_right hX2 (by positivity)
    _ = 2 ^ (2 * k + (u₀.sum + v₀.sum) + (u₀.length + v₀.length + 4))
          * 3 ^ (u₀.length + v₀.length + 2) := by ring
    _ ≤ 2 ^ (2 * (a + u₀.sum + (a + k) + v₀.sum)) * 3 ^ (u₀.length + v₀.length + 2) :=
        mul_le_mul_of_nonneg_right hpow (by positivity)

/-- The reduced denominator form of C011's (7): with `D_w = g q`, `q > 0`,
`D_w² · 2^{2m} < q² · 2^{2A} · 3^m`, i.e. `q > (1 − 3^m/2^A) (2/√3)^m`. -/
theorem two_defect_q_bound (a k : ℕ) (ha : 1 ≤ a) (hk : 1 ≤ k) (u₀ v₀ : List ℕ)
    (hu : ∀ x ∈ u₀, 1 ≤ x) (hv : ∀ x ∈ v₀, 1 ≤ x)
    (hrot : ∃ r, (a :: (u₀ ++ (a + k) :: v₀)).rotate r = (a + k) :: (u₀ ++ a :: v₀))
    {q : ℤ} (hq0 : 0 < q)
    (hq : D (a :: (u₀ ++ (a + k) :: v₀)) =
      ((Int.gcd (C (a :: (u₀ ++ (a + k) :: v₀))) (D (a :: (u₀ ++ (a + k) :: v₀))) : ℕ) : ℤ) * q) :
    D (a :: (u₀ ++ (a + k) :: v₀)) ^ 2 * 2 ^ (2 * (a :: (u₀ ++ (a + k) :: v₀)).length)
      < q ^ 2 * 2 ^ (2 * (a :: (u₀ ++ (a + k) :: v₀)).sum)
          * 3 ^ (a :: (u₀ ++ (a + k) :: v₀)).length := by
  have h := two_defect_bound a k ha hk u₀ v₀ hu hv hrot
  rw [hq]
  calc (((Int.gcd (C (a :: (u₀ ++ (a + k) :: v₀))) (D (a :: (u₀ ++ (a + k) :: v₀))) : ℕ) : ℤ) * q)
          ^ 2 * 2 ^ (2 * (a :: (u₀ ++ (a + k) :: v₀)).length)
      = q ^ 2 * (((Int.gcd (C (a :: (u₀ ++ (a + k) :: v₀)))
          (D (a :: (u₀ ++ (a + k) :: v₀))) : ℕ) : ℤ) ^ 2
            * 2 ^ (2 * (a :: (u₀ ++ (a + k) :: v₀)).length)) := by ring
    _ < q ^ 2 * (2 ^ (2 * (a :: (u₀ ++ (a + k) :: v₀)).sum)
          * 3 ^ (a :: (u₀ ++ (a + k) :: v₀)).length) :=
        mul_lt_mul_of_pos_left h (pow_pos hq0 2)
    _ = q ^ 2 * 2 ^ (2 * (a :: (u₀ ++ (a + k) :: v₀)).sum)
          * 3 ^ (a :: (u₀ ++ (a + k) :: v₀)).length := by ring

/-! ### C013: the shared-background block identities and the run law

C013 (`OVERLAP_CONTROLS.md` §1) studies `w = (U, a_0, U, a_1, …, U, a_{r−1})`: an arbitrary
positive background `U` (length `n`, total `A_U`, intercept `C_U`) interleaved with a marker word
`a` of length `r` and total `T`. With `u = 2^{A_U}`, `α = 3^{n+1}`, `E = 3 C_U + u` and
`P_j = Σ_{i<j} a_i`, its (1) reads `C_w = E · u^{r−1} P(α/u)` and `D_w = −u^r Q(α/u)` for
`P(X) = Σ_j 2^{P_j} X^{r−1−j}`, `Q(X) = X^r − 2^T`. Here these are list identities: `Ph U a` is the
homogenised `u^{r−1} P(α/u)`, by the recursion `P_h(x :: a) = α^{|a|} + u 2^x P_h(a)`, with the
closed form `Σ_{j<r} α^{r−1−j} 2^{j A_U + P_j}`. The polynomial gcd, the resultant, the Fourier
step (5) and the Matveev input are not formalised. -/

/-- The word `(U, a_0, U, a_1, …, U, a_{r−1})` of C013: background `U`, marker word `a`. -/
def interleave (U a : List ℕ) : List ℕ := List.flatMap (fun x => U ++ [x]) a

/-- The homogenised marker polynomial `P_h = u^{r−1} P(α/u)` of C013, by the recursion
`P_h(x :: a) = α^{|a|} + u 2^x P_h(a)` with `α = 3^{|U|+1}`, `u = 2^{Σ U}`. -/
def Ph (U : List ℕ) : List ℕ → ℤ
  | [] => 0
  | x :: a => 3 ^ ((U.length + 1) * a.length) + 2 ^ (U.sum + x) * Ph U a

theorem interleave_cons (U : List ℕ) (x : ℕ) (a : List ℕ) :
    interleave U (x :: a) = (U ++ [x]) ++ interleave U a := by
  simp [interleave]

theorem interleave_length (U a : List ℕ) :
    (interleave U a).length = a.length * (U.length + 1) := by
  induction a with
  | nil => simp [interleave]
  | cons x a ih =>
    rw [interleave_cons, List.length_append, ih]
    simp only [List.length_append, List.length_cons, List.length_nil]
    ring

theorem interleave_sum (U a : List ℕ) : (interleave U a).sum = a.sum + a.length * U.sum := by
  induction a with
  | nil => simp [interleave]
  | cons x a ih =>
    rw [interleave_cons, List.sum_append, ih]
    simp only [List.sum_append, List.sum_cons, List.sum_nil, List.length_cons, add_zero]
    ring

/-- C013's (1), first half: `C_w = E · P_h` with `E = 3 C_U + 2^{Σ U}` the common block
intercept (`C_append_singleton`). -/
theorem C_interleave (U a : List ℕ) : C (interleave U a) = (3 * C U + 2 ^ U.sum) * Ph U a := by
  induction a with
  | nil => simp [interleave, C, Ph]
  | cons x a ih =>
    rw [interleave_cons, C_append, ih, C_append_singleton, interleave_length]
    simp only [Ph, List.sum_append, List.sum_singleton]
    ring

/-- C013's (1), second half: `D_w = 2^{T + r A_U} − 3^{r(n+1)}` (`= −u^r Q(α/u)`). -/
theorem D_interleave (U a : List ℕ) :
    D (interleave U a) = 2 ^ (a.sum + a.length * U.sum) - 3 ^ (a.length * (U.length + 1)) := by
  rw [D, interleave_sum, interleave_length]

/-- The closed form `P_h = Σ_{j<r} 3^{(n+1)(r−1−j)} 2^{j A_U + P_j}`, `P_j = Σ_{i<j} a_i`. -/
theorem Ph_eq_sum (U a : List ℕ) :
    Ph U a = ∑ j ∈ Finset.range a.length,
      (3 : ℤ) ^ ((U.length + 1) * (a.length - 1 - j)) * 2 ^ (j * U.sum + (a.take j).sum) := by
  induction a with
  | nil => simp [Ph]
  | cons x a ih =>
    have hpt : ∀ j ∈ Finset.range a.length,
        (3 : ℤ) ^ ((U.length + 1) * (a.length + 1 - 1 - (j + 1)))
            * 2 ^ ((j + 1) * U.sum + ((x :: a).take (j + 1)).sum)
          = 2 ^ (U.sum + x)
            * (3 ^ ((U.length + 1) * (a.length - 1 - j)) * 2 ^ (j * U.sum + (a.take j).sum)) := by
      intro j _
      rw [List.take_succ_cons, List.sum_cons,
        show a.length + 1 - 1 - (j + 1) = a.length - 1 - j by omega,
        show (j + 1) * U.sum + (x + (a.take j).sum) = (U.sum + x) + (j * U.sum + (a.take j).sum)
          by ring, pow_add]
      ring
    rw [List.length_cons, Finset.sum_range_succ', Finset.sum_congr rfl hpt, ← Finset.mul_sum,
      ← ih]
    simp only [Ph, Nat.sub_zero, Nat.add_sub_cancel, Nat.zero_mul, List.take_zero, List.sum_nil,
      Nat.add_zero, pow_zero, mul_one]
    ring

/-- C013's (8) in cleared form: `2^n E ≤ u (3^{n+1} − 2^{n+1})`, i.e. `E ≤ u (α/2^n − 2)`, for a
positive background (`intercept_bound_last` with the block's last letter). -/
theorem E_bound (U : List ℕ) (hU : ∀ x ∈ U, 1 ≤ x) :
    (2 : ℤ) ^ U.length * (3 * C U + 2 ^ U.sum)
      ≤ 2 ^ U.sum * (3 ^ (U.length + 1) - 2 ^ (U.length + 1)) := by
  have h := intercept_bound_last U 0 hU
  rwa [C_append_singleton] at h

/-- C013's run law (`OVERLAP_THEORY.md` §1, (3)): if `2^E z_end = 3^t z_start` and `z_end` is
even, then `z_start = 2^{E+1} k` and `z_end = 2 · 3^t k` for an integer `k`. -/
theorem run_factor {E t : ℕ} {zs ze : ℤ} (h : (2 : ℤ) ^ E * ze = 3 ^ t * zs) (he : Even ze) :
    ∃ k : ℤ, zs = 2 ^ (E + 1) * k ∧ ze = 2 * 3 ^ t * k := by
  have hcop : IsCoprime ((2 : ℤ) ^ E) (3 ^ t) :=
    (Int.isCoprime_iff_gcd_eq_one.mpr (by norm_num)).pow
  have hdvd : (2 : ℤ) ^ E ∣ zs := hcop.dvd_of_dvd_mul_left ⟨ze, h.symm⟩
  obtain ⟨k', hk'⟩ := hdvd
  have hze : ze = 3 ^ t * k' := by
    have h2 : (2 : ℤ) ^ E * ze = 2 ^ E * (3 ^ t * k') := by rw [h, hk']; ring
    exact mul_left_cancel₀ (pow_ne_zero _ two_ne_zero) h2
  have hcop2 : IsCoprime (2 : ℤ) (3 ^ t) :=
    (Int.isCoprime_iff_gcd_eq_one.mpr (by norm_num)).pow_right
  have h2k : (2 : ℤ) ∣ k' := by
    have : (2 : ℤ) ∣ 3 ^ t * k' := by rw [← hze]; exact even_iff_two_dvd.mp he
    exact hcop2.dvd_of_dvd_mul_left this
  obtain ⟨k, hk⟩ := h2k
  refine ⟨k, ?_, ?_⟩
  · rw [hk', hk]; ring
  · rw [hze, hk]; ring

/-! ### C005: the rotation-block ratio bound `H/L ≤ R³` and its gcd bookkeeping

C005 (`ORDER_THEORY.md` §2, rotation-block theorem): concatenating `r` cyclic rotations of a
primitive mechanical word `v` (coprime totals, rational states in `[l, h]`, `R = h/l < 2` by
C004 — `C_mech_lt_two`) gives a rational cycle all of whose states lie in `[l/R, R h]`, hence
`H/L ≤ R³ < 8`; and if its reduced denominator were `1`, the three-band corollary (`three_band`)
would force the primitive cycle word to have coprime totals, which by the gcd bookkeeping forces
every aligned block to be the same rotation, i.e. the base mechanical cycle (whose denominator is
`D_0` by R71, not formalised). Below: the affine comparison, the interval and fixed-point lemmas
behind `[l/R, R h]`, the ratio bound, and the bookkeeping, all stated abstractly. -/

/-- C005's prefix comparison: for `g(x) = αx + β` with `α > 0`, `β ≥ 0`, and `X/R ≤ x ≤ R X`
(`R ≥ 1`), `g(X)/R ≤ g(x) ≤ R g(X)` — the prose's `min(1, x/X) ≤ g(x)/g(X) ≤ max(1, x/X)`. -/
theorem affine_ratio {α β x X R : ℚ} (hα : 0 < α) (hβ : 0 ≤ β) (hR : 1 ≤ R)
    (hlo : X ≤ R * x) (hhi : x ≤ R * X) :
    α * X + β ≤ R * (α * x + β) ∧ α * x + β ≤ R * (α * X + β) := by
  have h1 := mul_le_mul_of_nonneg_left hlo hα.le
  have h2 := mul_le_mul_of_nonneg_left hhi hα.le
  have h3 := mul_le_mul_of_nonneg_left hR hβ
  constructor <;> nlinarith

/-- A block map `x ↦ s x + (1 − s) X` with `0 ≤ s ≤ 1` and `X ∈ [l, h]` preserves `[l, h]`. -/
theorem block_preserves {s X l h x : ℚ} (hs0 : 0 ≤ s) (hs1 : s ≤ 1) (hXl : l ≤ X) (hXh : X ≤ h)
    (hxl : l ≤ x) (hxh : x ≤ h) : l ≤ s * x + (1 - s) * X ∧ s * x + (1 - s) * X ≤ h := by
  constructor <;> nlinarith

/-- The fixed point of an affine map `x ↦ σ x + τ` with `σ < 1` that maps `[l, h]` into itself
lies in `[l, h]`. -/
theorem fixed_point_mem {σ τ l h x : ℚ} (hσ1 : σ < 1) (hl : l ≤ σ * l + τ)
    (hh : σ * h + τ ≤ h) (hx : σ * x + τ = x) : l ≤ x ∧ x ≤ h := by
  constructor <;> nlinarith

/-- The composition of block maps with common slope `s` and fixed points `t 0, t 1, …`:
`blockComp s t 0 x = x`, `blockComp s t (i+1) x = s · blockComp s t i x + (1 − s) t i`. -/
def blockComp (s : ℚ) (t : ℕ → ℚ) : ℕ → ℚ → ℚ
  | 0, x => x
  | i + 1, x => s * blockComp s t i x + (1 - s) * t i

/-- Boundary points stay in `[l, h]` when the block fixed points do. -/
theorem blockComp_mem {s l h : ℚ} {t : ℕ → ℚ} (hs0 : 0 ≤ s) (hs1 : s ≤ 1)
    (ht : ∀ i, l ≤ t i ∧ t i ≤ h) {x : ℚ} (hxl : l ≤ x) (hxh : x ≤ h) (i : ℕ) :
    l ≤ blockComp s t i x ∧ blockComp s t i x ≤ h := by
  induction i with
  | zero => exact ⟨hxl, hxh⟩
  | succ i ih =>
    simp only [blockComp]
    exact block_preserves hs0 hs1 (ht i).1 (ht i).2 ih.1 ih.2

/-- The composition is affine with slope `s^i`: `blockComp s t i x = s^i x + blockComp s t i 0`. -/
theorem blockComp_affine (s : ℚ) (t : ℕ → ℚ) (i : ℕ) (x : ℚ) :
    blockComp s t i x = s ^ i * x + blockComp s t i 0 := by
  induction i with
  | zero => simp [blockComp]
  | succ i ih =>
    simp only [blockComp]
    rw [ih]
    ring

/-- The closing point of a mixed cycle of `r ≥ 1` blocks (slope `0 < s < 1`, fixed points in
`[l, h]`) lies in `[l, h]`: C005's "the unique positive fixed point of their composition, and all
successive block boundary points, lie in `[l, h]`". -/
theorem cycle_point_mem {s l h : ℚ} {t : ℕ → ℚ} (hs0 : 0 < s) (hs1 : s < 1)
    (ht : ∀ i, l ≤ t i ∧ t i ≤ h) (hlh : l ≤ h) {r : ℕ} (hr : 1 ≤ r) {x : ℚ}
    (hx : blockComp s t r x = x) : l ≤ x ∧ x ≤ h := by
  have hσ1 : s ^ r < 1 := pow_lt_one₀ hs0.le hs1 (by omega)
  have hl := (blockComp_mem hs0.le hs1.le ht (le_refl l) hlh r).1
  have hh := (blockComp_mem hs0.le hs1.le ht hlh (le_refl h) r).2
  rw [blockComp_affine] at hl hh hx
  exact fixed_point_mem hσ1 hl hh hx

/-- Every mixed-cycle state lies in `[l/R, R h]`, `R = h/l`: a prefix map `g(x) = αx + β`
(`α > 0`, `β ≥ 0`) applied to a boundary point `x ∈ [l, h]`, when the block fixed point `X` and
the base prefix state `g(X)` lie in `[l, h]`, satisfies `l²/h ≤ g(x) ≤ h²/l` (cleared form). -/
theorem state_bound {α β x X l h : ℚ} (hα : 0 < α) (hβ : 0 ≤ β) (hl : 0 < l) (hlh : l ≤ h)
    (hxl : l ≤ x) (hxh : x ≤ h) (hXl : l ≤ X) (hXh : X ≤ h)
    (hgl : l ≤ α * X + β) (hgh : α * X + β ≤ h) :
    l * l ≤ h * (α * x + β) ∧ l * (α * x + β) ≤ h * h := by
  have hl0 : l ≠ 0 := hl.ne'
  have hR : 1 ≤ h / l := (one_le_div hl).mpr hlh
  have hR0 : 0 ≤ h / l := div_nonneg (hl.le.trans hlh) hl.le
  have hRl : h / l * l = h := by field_simp
  have hlR : l * (h / l) = h := by field_simp
  have hlo : X ≤ h / l * x := by
    have := mul_le_mul_of_nonneg_left hxl hR0
    rw [hRl] at this
    exact hXh.trans this
  have hhi : x ≤ h / l * X := by
    have := mul_le_mul_of_nonneg_left hXl hR0
    rw [hRl] at this
    exact hxh.trans this
  obtain ⟨h1, h2⟩ := affine_ratio hα hβ hR hlo hhi
  have e1 : l * (α * X + β) ≤ h * (α * x + β) := by
    calc l * (α * X + β) ≤ l * (h / l * (α * x + β)) := mul_le_mul_of_nonneg_left h1 hl.le
      _ = (l * (h / l)) * (α * x + β) := by ring
      _ = h * (α * x + β) := by rw [hlR]
  have e2 : l * (α * x + β) ≤ h * (α * X + β) := by
    calc l * (α * x + β) ≤ l * (h / l * (α * X + β)) := mul_le_mul_of_nonneg_left h2 hl.le
      _ = (l * (h / l)) * (α * X + β) := by ring
      _ = h * (α * X + β) := by rw [hlR]
  constructor
  · have := mul_le_mul_of_nonneg_left hgl hl.le
    linarith
  · have := mul_le_mul_of_nonneg_left hgh (hl.le.trans hlh)
    linarith

/-- Hence the largest-to-smallest state ratio is at most `R³ = (h/l)³`: for states `y₁, y₂` with
`y₁ ≤ h²/l` and `l²/h ≤ y₂` (cleared), `y₁ l³ ≤ y₂ h³` (C005's `H/L ≤ R³`). -/
theorem ratio_bound {y₁ y₂ l h : ℚ} (hl : 0 < l) (hlh : l ≤ h)
    (h₁ : l * y₁ ≤ h * h) (h₂ : l * l ≤ h * y₂) : y₁ * l ^ 3 ≤ y₂ * h ^ 3 := by
  have hh : 0 < h := hl.trans_le hlh
  have := mul_le_mul h₁ h₂ (by positivity) (by positivity)
  linarith

/-- Concatenating rotations of `v` (any order, repetitions allowed): the length. -/
theorem flatten_rotations_length (v : List ℕ) (blocks : List (List ℕ))
    (hb : ∀ b ∈ blocks, ∃ i, b = v.rotate i) :
    blocks.flatten.length = blocks.length * v.length := by
  induction blocks with
  | nil => simp
  | cons b bs ih =>
    obtain ⟨i, hi⟩ := hb b (List.mem_cons_self ..)
    rw [List.flatten_cons, List.length_append, ih (fun c hc => hb c (List.mem_cons_of_mem _ hc)),
      hi, List.length_rotate, List.length_cons]
    ring

/-- Concatenating rotations of `v`: the total. -/
theorem flatten_rotations_sum (v : List ℕ) (blocks : List (List ℕ))
    (hb : ∀ b ∈ blocks, ∃ i, b = v.rotate i) : blocks.flatten.sum = blocks.length * v.sum := by
  induction blocks with
  | nil => simp
  | cons b bs ih =>
    obtain ⟨i, hi⟩ := hb b (List.mem_cons_self ..)
    rw [List.flatten_cons, List.sum_append, ih (fun c hc => hb c (List.mem_cons_of_mem _ hc)),
      hi, (List.rotate_perm v i).sum_eq, List.length_cons]
    ring

/-- The gcd of the totals of a concatenation of `r` rotations of a word with coprime totals is
`r` (C005: "the displayed word has totals `(rA_0, rm_0)`, whose gcd is `r`"). -/
theorem gcd_flatten_rotations (v : List ℕ) (hcop : Nat.Coprime v.sum v.length)
    (blocks : List (List ℕ)) (hb : ∀ b ∈ blocks, ∃ i, b = v.rotate i) :
    Nat.gcd blocks.flatten.sum blocks.flatten.length = blocks.length := by
  rw [flatten_rotations_sum v blocks hb, flatten_rotations_length v blocks hb, Nat.gcd_mul_left,
    hcop.gcd_eq_one, mul_one]

/-- If that concatenation is `p` repetitions of a word `z`, then `gcd(Σz, |z|) · p = r`
(C005: "`p ∣ r` and the primitive word's total/length gcd is `r/p`"). -/
theorem gcd_rep_of_flatten (v : List ℕ) (hcop : Nat.Coprime v.sum v.length)
    (blocks : List (List ℕ)) (hb : ∀ b ∈ blocks, ∃ i, b = v.rotate i) (z : List ℕ) (p : ℕ)
    (hw : blocks.flatten = rep z p) : Nat.gcd z.sum z.length * p = blocks.length := by
  have h := gcd_flatten_rotations v hcop blocks hb
  rw [hw, rep_sum, rep_length, Nat.gcd_mul_left] at h
  rw [mul_comm]
  exact h

/-- If a concatenation of blocks of length `|z|` equals `z^r` with `r` the number of blocks, every
block is `z` (C005: "every aligned rotation block of `w` is identical"). -/
theorem blocks_eq_of_flatten_rep (z : List ℕ) : ∀ (blocks : List (List ℕ)),
    (∀ b ∈ blocks, b.length = z.length) → blocks.flatten = rep z blocks.length →
      ∀ b ∈ blocks, b = z
  | [], _, _, _, hb => nomatch hb
  | b :: bs, hlen, h, c, hc => by
    rw [List.flatten_cons, List.length_cons, rep] at h
    obtain ⟨h1, h2⟩ := List.append_inj h (hlen b (List.mem_cons_self ..))
    rcases List.mem_cons.mp hc with rfl | hc'
    · exact h1
    · exact blocks_eq_of_flatten_rep z bs (fun d hd => hlen d (List.mem_cons_of_mem _ hd)) h2
        c hc'

/-- C005's bookkeeping conclusion: if the concatenation of `r ≥ 1` rotations of `v` (coprime
totals) is `p` repetitions of a word `z` with coprime totals (the three-band output at `q = 1`),
then `p = r`, `|z| = |v|` and every block equals `z`. -/
theorem blocks_identical (v : List ℕ) (hcop : Nat.Coprime v.sum v.length)
    (blocks : List (List ℕ)) (hb : ∀ b ∈ blocks, ∃ i, b = v.rotate i) (hr : 0 < blocks.length)
    (z : List ℕ) (p : ℕ) (hw : blocks.flatten = rep z p) (hz : Nat.Coprime z.sum z.length) :
    p = blocks.length ∧ z.length = v.length ∧ ∀ b ∈ blocks, b = z := by
  have hp := gcd_rep_of_flatten v hcop blocks hb z p hw
  rw [hz.gcd_eq_one, one_mul] at hp
  have hlen : blocks.flatten.length = blocks.length * v.length :=
    flatten_rotations_length v blocks hb
  rw [hw, rep_length, hp] at hlen
  have hzl : z.length = v.length := Nat.eq_of_mul_eq_mul_left hr hlen
  refine ⟨hp, hzl, ?_⟩
  apply blocks_eq_of_flatten_rep z blocks
  · intro b hb'
    obtain ⟨i, hi⟩ := hb b hb'
    rw [hi, List.length_rotate, hzl]
  · rw [hw, hp]

/-! ### R71: the exact denominator of a primitive mechanical word

R71 (`BALANCED_DENOMINATORS.md` §2, primitive case): for `gcd(A, m) = 1`, every phase word is a
rotation of phase `0`, so all `gcd(B_l, D)` agree; passing from phase `0` to phase `1` raises
exactly one prefix floor, so `B_1 − B_0 = 3^{m−1−j} 2^{⌊jA/m⌋}` for the unique `j` with
`jA ≡ −1 (mod m)`; since `gcd(D, 6) = 1` the common gcd is `1`, and the reduced denominator is
`D = 2^A − 3^m` itself. Here `B_l = C (mech A m l)`. The modulo-`8` exclusion of denominator `1`
follows; the repeated case (`gcd(A, m) > 1` reduces to the primitive parameters) is not
formalised. -/

/-- `gcd(C_{(i)}, D)` is the same for every rotation (positive total): each divides the other
through the recurrence `2^{a} C_{(i+1)} = 3 C_{(i)} + D`. -/
theorem gcd_rotate_eq {w : List ℕ} (hw0 : w ≠ []) (hsum : 1 ≤ w.sum) (i : ℕ) :
    Int.gcd (C (w.rotate i)) (D (w.rotate i)) = Int.gcd (C w) (D w) := by
  have hlen : 0 < w.length := List.length_pos_of_ne_nil hw0
  have hinv : (w.rotate i).rotate (w.length - i % w.length) = w := by
    have hr := Nat.mod_lt i hlen
    have hd := Nat.div_add_mod i w.length
    have heq : i + (w.length - i % w.length) = w.length * (i / w.length + 1) := by
      rw [Nat.mul_succ]
      omega
    rw [List.rotate_rotate, heq, List.rotate_length_mul]
  have hsum' : 1 ≤ (w.rotate i).sum := by rwa [(List.rotate_perm w i).sum_eq]
  have hw0' : w.rotate i ≠ [] := fun h => hw0 (List.rotate_eq_nil_iff.mp h)
  apply Nat.dvd_antisymm
  · have h1 := dvd_C_rotate_of_dvd hw0' (gcd_isCoprime_two hsum') (Int.gcd_dvd_left _ _)
      (Int.gcd_dvd_right _ _) (w.length - i % w.length)
    rw [hinv] at h1
    have h2 : ((Int.gcd (C (w.rotate i)) (D (w.rotate i)) : ℕ) : ℤ) ∣ D w :=
      (Int.gcd_dvd_right (C (w.rotate i)) (D (w.rotate i))).trans (dvd_of_eq (D_rotate w i))
    exact Int.dvd_gcd h1 h2
  · have h1 := dvd_C_rotate_of_dvd hw0 (gcd_isCoprime_two hsum) (Int.gcd_dvd_left _ _)
      (Int.gcd_dvd_right _ _) i
    have h2 : ((Int.gcd (C w) (D w) : ℕ) : ℤ) ∣ D (w.rotate i) :=
      (Int.gcd_dvd_right (C w) (D w)).trans (dvd_of_eq (D_rotate w i).symm)
    exact Int.dvd_gcd h1 h2

/-- Uniqueness of the jump index: two `j, j' < m` with `m ∣ jA + 1` and `m ∣ j'A + 1` agree
when `gcd(A, m) = 1`. -/
theorem mech_jump_unique {m A j j' : ℕ} (hcop : Nat.Coprime A m) (hj : j < m) (hj' : j' < m)
    (h : m ∣ j * A + 1) (h' : m ∣ j' * A + 1) : j' = j := by
  have hcop' : Nat.Coprime m A := hcop.symm
  rcases le_total j j' with hle | hle
  · have hd : m ∣ (j' - j) * A := by
      have := Nat.dvd_sub h' h
      rwa [show j' * A + 1 - (j * A + 1) = (j' - j) * A by rw [Nat.sub_mul]; omega] at this
    have := Nat.eq_zero_of_dvd_of_lt (hcop'.dvd_of_dvd_mul_right hd) (by omega)
    omega
  · have hd : m ∣ (j - j') * A := by
      have := Nat.dvd_sub h h'
      rwa [show j * A + 1 - (j' * A + 1) = (j - j') * A by rw [Nat.sub_mul]; omega] at this
    have := Nat.eq_zero_of_dvd_of_lt (hcop'.dvd_of_dvd_mul_right hd) (by omega)
    omega

/-- Existence and uniqueness of the jump index (R71: "among `j = 0, …, k−1` there is exactly one
`j` with `jA ≡ k − 1 (mod k)`"). -/
theorem exists_unique_mech_jump {m : ℕ} (hm : 2 ≤ m) (A : ℕ) (hcop : Nat.Coprime A m) :
    ∃ j, j < m ∧ m ∣ j * A + 1 ∧ ∀ j', j' < m → m ∣ j' * A + 1 → j' = j := by
  obtain ⟨i, _, hiA⟩ := Nat.exists_mul_mod_eq_one_of_coprime hcop (by omega)
  have hiA' : A * i ≡ 1 [MOD m] := by
    show A * i % m = 1 % m
    rw [Nat.mod_eq_of_lt (by omega : 1 < m)]
    exact hiA
  have hjlt : (m - 1) * i % m < m := Nat.mod_lt _ (by omega)
  have hjd : m ∣ (m - 1) * i % m * A + 1 := by
    have h1 : (m - 1) * i % m * A ≡ (m - 1) * i * A [MOD m] := (Nat.mod_modEq _ _).mul_right A
    have h2 : (m - 1) * i * A ≡ (m - 1) * 1 [MOD m] := by
      rw [show (m - 1) * i * A = (m - 1) * (A * i) by ring]
      exact Nat.ModEq.mul_left (m - 1) hiA'
    have h3 : (m - 1) * i % m * A + 1 ≡ (m - 1) * 1 + 1 [MOD m] := (h1.trans h2).add_right 1
    rw [show (m - 1) * 1 + 1 = m by omega] at h3
    exact Nat.modEq_zero_iff_dvd.mp (h3.trans (Nat.modEq_zero_iff_dvd.mpr dvd_rfl))
  exact ⟨_, hjlt, hjd, fun j' hj' h' => mech_jump_unique hcop hjlt hj' hjd h'⟩

/-- R71's (4): `B_1 − B_0 = 3^{m−1−j} 2^{⌊jA/m⌋}` for the unique `j < m` with `m ∣ jA + 1`
("passing from `l = 0` to `l = 1` increases precisely one prefix floor"). -/
theorem C_mech_one_sub_zero {m : ℕ} (hm : 2 ≤ m) (A : ℕ) (hcop : Nat.Coprime A m) :
    ∃ j, j < m ∧ C (mech A m 1) - C (mech A m 0) = 3 ^ (m - (j + 1)) * 2 ^ (j * A / m) := by
  obtain ⟨j, hj, hjd, huniq⟩ := exists_unique_mech_jump hm A hcop
  refine ⟨j, hj, ?_⟩
  rw [C_mech A 1 (by omega), C_mech A 0 (by omega), ← Finset.sum_sub_distrib]
  have hterm : ∀ x ∈ Finset.range m,
      (3 : ℤ) ^ (m - (x + 1)) * 2 ^ ((x * A + 1) / m) - 3 ^ (m - (x + 1)) * 2 ^ ((x * A + 0) / m)
        = if x = j then (3 : ℤ) ^ (m - (x + 1)) * 2 ^ (x * A / m) else 0 := by
    intro x hx
    rw [Nat.succ_div, add_zero]
    by_cases hdx : m ∣ x * A + 1
    · rw [ite_eq_left hdx, pow_add, pow_one,
        ite_eq_left (huniq x (Finset.mem_range.mp hx) hdx)]
      ring
    · rw [ite_eq_right hdx, add_zero, ite_eq_right (fun h => hdx (by rw [h]; exact hjd))]
      ring
  rw [Finset.sum_congr rfl hterm, Finset.sum_ite_eq', ite_eq_left (Finset.mem_range.mpr hj)]

/-- **R71's exact denominator, primitive case.** For `m ≥ 2`, `A ≥ m` and `gcd(A, m) = 1`, the
phase-`0` mechanical word has `gcd(C, D) = 1`: its rational cycle has reduced denominator
exactly `D = 2^A − 3^m`. -/
theorem mech_gcd_one {m : ℕ} (hm : 2 ≤ m) (A : ℕ) (hAm : m ≤ A) (hcop : Nat.Coprime A m) :
    Int.gcd (C (mech A m 0)) (D (mech A m 0)) = 1 := by
  have hm0 : 0 < m := by omega
  have hsum : 1 ≤ (mech A m 0).sum := by rw [mech_sum hm0 A 0 hm0]; omega
  have hlen : 1 ≤ (mech A m 0).length := by rw [mech_length]; omega
  have hw0 : mech A m 0 ≠ [] := fun h => by
    have := congrArg List.length h
    rw [mech_length, List.length_nil] at this
    omega
  have hg2 := gcd_isCoprime_two hsum
  have hg3 := gcd_isCoprime_three hlen
  obtain ⟨i, _, hiA⟩ := Nat.exists_mul_mod_eq_one_of_coprime hcop (by omega)
  have hrot : (mech A m 0).rotate i = mech A m 1 := by
    rw [mech_rotate hm0 A 0 i, zero_add, mul_comm, hiA]
  have hC1 : ((Int.gcd (C (mech A m 0)) (D (mech A m 0)) : ℕ) : ℤ) ∣ C (mech A m 1) := by
    have := dvd_C_rotate_of_dvd hw0 hg2 (Int.gcd_dvd_left _ _) (Int.gcd_dvd_right _ _) i
    rwa [hrot] at this
  have hC0 : ((Int.gcd (C (mech A m 0)) (D (mech A m 0)) : ℕ) : ℤ) ∣ C (mech A m 0) :=
    Int.gcd_dvd_left _ _
  obtain ⟨j, _, hdiff⟩ := C_mech_one_sub_zero hm A hcop
  have hdvd : ((Int.gcd (C (mech A m 0)) (D (mech A m 0)) : ℕ) : ℤ)
      ∣ (3 : ℤ) ^ (m - (j + 1)) * 2 ^ (j * A / m) := by
    rw [← hdiff]
    exact dvd_sub hC1 hC0
  have hcop' : IsCoprime ((Int.gcd (C (mech A m 0)) (D (mech A m 0)) : ℕ) : ℤ)
      ((3 : ℤ) ^ (m - (j + 1)) * 2 ^ (j * A / m)) :=
    (hg3.pow_right).mul_right (hg2.pow_right)
  have h1 : ((Int.gcd (C (mech A m 0)) (D (mech A m 0)) : ℕ) : ℤ) ∣ ((1 : ℕ) : ℤ) :=
    hcop'.dvd_of_dvd_mul_left (by rw [Nat.cast_one, mul_one]; exact hdvd)
  exact Nat.dvd_one.mp (Int.natCast_dvd_natCast.mp h1)

/-- Every phase word is a rotation of phase `0`, so `gcd(C, D) = 1` for every phase `l < m` in
the primitive case. -/
theorem mech_gcd_one_phase {m : ℕ} (hm : 2 ≤ m) (A : ℕ) (hAm : m ≤ A) (hcop : Nat.Coprime A m)
    {l : ℕ} (hl : l < m) : Int.gcd (C (mech A m l)) (D (mech A m l)) = 1 := by
  have hm0 : 0 < m := by omega
  have hsum : 1 ≤ (mech A m 0).sum := by rw [mech_sum hm0 A 0 hm0]; omega
  have hw0 : mech A m 0 ≠ [] := fun h => by
    have := congrArg List.length h
    rw [mech_length, List.length_nil] at this
    omega
  obtain ⟨i, _, hiA⟩ := Nat.exists_mul_mod_eq_one_of_coprime hcop (by omega)
  have hrot : (mech A m 0).rotate (l * i) = mech A m l := by
    rw [mech_rotate hm0 A 0 (l * i), zero_add, show l * i * A = l * (A * i) by ring,
      Nat.mul_mod, hiA, mul_one, Nat.mod_mod, Nat.mod_eq_of_lt hl]
  rw [← hrot, gcd_rotate_eq hw0 hsum, mech_gcd_one hm A hAm hcop]

/-- `3^m ≡ 1` or `3 (mod 8)`. -/
theorem three_pow_mod_eight (m : ℕ) : 3 ^ m % 8 = 1 ∨ 3 ^ m % 8 = 3 := by
  induction m with
  | zero => left; rfl
  | succ m ih =>
    rw [pow_succ, Nat.mul_mod]
    rcases ih with h | h <;> rw [h] <;> decide

/-- R71's exclusion: `D = 2^A − 3^m ≠ 1` for `m ≥ 2`, `A ≥ m` (modulo `8` for `A ≥ 3`; `A = 2`
forces `m = 2` and `4 ≠ 10`). With `mech_gcd_one` this is "their only positive integer case is
the all-`2` word", whose cycle is the fixed point `1`. -/
theorem mech_D_ne_one {m : ℕ} (hm : 2 ≤ m) (A : ℕ) (hAm : m ≤ A) : (2 : ℤ) ^ A - 3 ^ m ≠ 1 := by
  intro h
  have hN : 2 ^ A = 3 ^ m + 1 := by
    have : (2 : ℤ) ^ A = 3 ^ m + 1 := by linarith
    exact_mod_cast this
  rcases Nat.lt_or_ge A 3 with hA | hA
  · have hA2 : A = 2 := by omega
    have hm2 : m = 2 := by omega
    subst hA2
    subst hm2
    norm_num at hN
  · have h8 : 8 ∣ 2 ^ A := by
      have := pow_dvd_pow 2 hA
      simpa using this
    have h3 := three_pow_mod_eight m
    omega

/-! ### C004-c: the integer corollary of the narrow-cycle theorem

C004 §3 with R71: a primitive positive odd integer cycle at `q = 1` all of whose states lie
below `2L` (every height `0`) is the fixed point `1`. Its valuation word is narrow, hence a
phase of the mechanical word of its total with coprime totals (`is_mech_of_narrow`); the
cycle identity gives `D ∣ C`, R71 gives `gcd(C, D) = 1`, so `D = 1`, which `mech_D_ne_one`
excludes for `m ≥ 2`; the one-letter case is `(2^A − 3) n_0 = 1`. -/

namespace OddCycle

variable {m : ℕ} (Γ : OddCycle m)

/-- The chronological valuation word `(a_0, …, a_{m−1})` of the cycle. -/
def word : List ℕ := (List.range m).map Γ.a

theorem word_length : Γ.word.length = m := by simp [word]

theorem word_prefix (i : ℕ) :
    ((List.range i).map Γ.a).sum = Γ.Apre i ∧ C ((List.range i).map Γ.a) = Γ.Cpre i := by
  induction i with
  | zero => simp [Apre, Cpre, C]
  | succ i ih =>
    obtain ⟨h1, h2⟩ := ih
    rw [List.range_succ, List.map_append, List.map_singleton, List.sum_append,
      List.sum_singleton, C_append_singleton, h1, h2, Γ.Apre_succ, Γ.Cpre_succ]
    exact ⟨rfl, rfl⟩

theorem word_sum : Γ.word.sum = Γ.Apre m := (Γ.word_prefix m).1

theorem C_word : C Γ.word = Γ.Cpre m := (Γ.word_prefix m).2

theorem D_word : D Γ.word = 2 ^ Γ.Apre m - 3 ^ m := by
  rw [D, Γ.word_sum, Γ.word_length]

theorem word_ne_nil : Γ.word ≠ [] :=
  List.ne_nil_of_length_pos (by rw [Γ.word_length]; exact Γ.hm)

/-- At `q = 1` the rotated intercepts are `D · n_i` (the cycle identity propagated along the
rotation recurrence `2^{a_i} C_{(i+1)} = 3 C_{(i)} + D`). -/
theorem C_word_rotate (hq : Γ.q = 1) : ∀ i, i < m → C (Γ.word.rotate i) = D Γ.word * Γ.n i
  | 0, _ => by
    rw [List.rotate_zero, Γ.C_word, Γ.D_word]
    have h := Γ.cycle_identity
    rw [hq, one_mul] at h
    exact h.symm
  | i + 1, hi => by
    have ih := C_word_rotate hq i (by omega)
    obtain ⟨x, v, hxv⟩ := List.exists_cons_of_ne_nil (NarrowCycle.rotate_ne_nil Γ.word_ne_nil i)
    have hx : x = Γ.a i := by
      have h1 := NarrowCycle.headD_rotate Γ.word (show i < Γ.word.length by rw [Γ.word_length]; omega)
      rw [hxv, List.headD_cons] at h1
      rw [h1]
      simp [word]
    subst hx
    have hrec := C_rotate_succ hxv
    have harrow := Γ.arrow i
    rw [hq] at harrow
    rw [ih] at hrec
    have h2 : (2 : ℤ) ^ Γ.a i * C (Γ.word.rotate (i + 1))
        = 2 ^ Γ.a i * (D Γ.word * Γ.n (i + 1)) := by
      linear_combination hrec - D Γ.word * harrow
    exact mul_left_cancel₀ (pow_ne_zero _ two_ne_zero) h2

theorem C_word_rotate' (hq : Γ.q = 1) (i : ℕ) : C (Γ.word.rotate i) = D Γ.word * Γ.n i := by
  rw [← List.rotate_mod, Γ.word_length, Γ.C_word_rotate hq (i % m) (Nat.mod_lt _ Γ.hm), Γ.n_mod]

/-- **C004's integer corollary.** A primitive positive odd integer cycle at `q = 1` with every
state below `2 n_0` (all heights `0`, i.e. `H < 2L`) is the fixed point `1`: `m = 1` and
`n_0 = 1`. -/
theorem narrow_integer_cycle (hq : Γ.q = 1) (hB : Γ.B = 0)
    (hprim : ∀ i j, i < m → j < m → Γ.n i = Γ.n j → i = j) : m = 1 ∧ Γ.n 0 = 1 := by
  have hm := Γ.hm
  have hh : ∀ i, Γ.h i = 0 := fun i => by have := Γ.hB i; omega
  have hlt : ∀ i, Γ.n i < 2 * Γ.n 0 := fun i => by
    have := Γ.hhi i
    rw [hh i] at this
    simpa using this
  have hCD : C Γ.word = D Γ.word * Γ.n 0 := by
    have := Γ.C_word_rotate hq 0 hm
    rwa [List.rotate_zero] at this
  have hCpos : 0 < C Γ.word := C_pos Γ.word_ne_nil
  have hn0 := Γ.npos
  have hD : 0 < D Γ.word := by
    by_contra hneg
    rw [not_lt] at hneg
    have : D Γ.word * Γ.n 0 ≤ 0 := mul_nonpos_of_nonpos_of_nonneg hneg hn0.le
    linarith
  rcases Nat.lt_or_ge m 2 with hm1 | hm2
  · have hm1' : m = 1 := by omega
    subst hm1'
    refine ⟨rfl, ?_⟩
    have hC1 : C Γ.word = 1 := by simp [word, C]
    rw [hC1] at hCD
    have hdvd : Γ.n 0 ∣ 1 := ⟨D Γ.word, by rw [mul_comm]; exact hCD⟩
    have := Int.le_of_dvd one_pos hdvd
    omega
  · exfalso
    have hrot := Γ.C_word_rotate' hq
    have hnarrow : ∀ i j, C (Γ.word.rotate i) < 2 * C (Γ.word.rotate j) := by
      intro i j
      rw [hrot i, hrot j]
      have h1 := mul_lt_mul_of_pos_left (hlt i) hD
      have h2 := mul_le_mul_of_nonneg_left (Γ.nmin j) hD.le
      linarith
    have hdist : ∀ i j, i < Γ.word.length → j < Γ.word.length →
        C (Γ.word.rotate i) = C (Γ.word.rotate j) → i = j := by
      intro i j hi hj hij
      rw [hrot i, hrot j] at hij
      rw [Γ.word_length] at hi hj
      exact hprim i j hi hj (mul_left_cancel₀ hD.ne' hij)
    obtain ⟨l, hl, hw, hcop⟩ :=
      NarrowCycle.is_mech_of_narrow Γ.word (by rw [Γ.word_length]; exact hm2) hD hnarrow hdist
    rw [Γ.word_length] at hl hw hcop
    have hAm : m ≤ Γ.word.sum := by
      by_contra hlt'
      rw [not_le] at hlt'
      have h1 : (2 : ℤ) ^ Γ.word.sum ≤ 2 ^ m := pow_le_pow_right₀ (by norm_num) hlt'.le
      have h2 : (2 : ℤ) ^ m ≤ 3 ^ m := pow_le_pow_left₀ (by norm_num) (by norm_num) m
      have h3 : D Γ.word = 2 ^ Γ.word.sum - 3 ^ Γ.word.length := rfl
      rw [Γ.word_length] at h3
      linarith
    have hgcd := mech_gcd_one_phase hm2 Γ.word.sum hAm hcop hl
    rw [← hw] at hgcd
    have hDdvd : D Γ.word ∣ C Γ.word := ⟨Γ.n 0, hCD⟩
    have h1 : (D Γ.word).natAbs ∣ 1 := by
      rw [← hgcd]
      exact Int.dvd_gcd (Int.natAbs_dvd.mpr hDdvd) (Int.natAbs_dvd.mpr dvd_rfl)
    have hD1 : D Γ.word = 1 := by
      have h2 := Int.natAbs_of_nonneg hD.le
      rw [Nat.dvd_one.mp h1] at h2
      simpa using h2.symm
    have hDne := mech_D_ne_one hm2 Γ.word.sum hAm
    rw [hw, D_mech (by omega) _ _ hl] at hD1
    exact hDne hD1

end OddCycle

/-! ### C004-d: the primitive-period reduction — every nontrivial cycle has `H > 2L`

C004 §3's sentence "every nontrivial integer Collatz cycle has `H > 2L`", as stated: a positive
odd integer cycle at `q = 1` other than the fixed point `1` has a state above `2 n_0`. The
reduction to C004-c passes to the least return time of the minimum, on which the deterministic
state sequence is a primitive `OddCycle`; the parity remark (`n_i` odd, `2 n_0` even) turns `≥`
into `>`. -/

namespace OddCycle

variable {m : ℕ} (Γ : OddCycle m)

/-- Determinism of the odd-only dynamics: equal states have equal successors and valuations. -/
theorem succ_eq_of_eq {i j : ℕ} (h : Γ.n i = Γ.n j) :
    Γ.n (i + 1) = Γ.n (j + 1) ∧ Γ.a i = Γ.a j := by
  have hi := Γ.arrow i
  have hj := Γ.arrow j
  rw [h] at hi
  have := pow_mul_eq_of_odd (Γ.nodd (i + 1)) (Γ.nodd (j + 1)) (hi.trans hj.symm)
  exact ⟨this.2, this.1⟩

/-- Equal states propagate: `n (i + t) = n (j + t)` for all `t`. -/
theorem shift_eq_of_eq {i j : ℕ} (h : Γ.n i = Γ.n j) : ∀ t, Γ.n (i + t) = Γ.n (j + t)
  | 0 => h
  | t + 1 => by
    show Γ.n (i + t + 1) = Γ.n (j + t + 1)
    exact (Γ.succ_eq_of_eq (shift_eq_of_eq h t)).1

/-- If the minimum is `1` then every state is `1` (the fixed point). -/
theorem all_one_of_min_one (hq : Γ.q = 1) (h0 : Γ.n 0 = 1) : ∀ i, Γ.n i = 1
  | 0 => h0
  | i + 1 => by
    have hi := Γ.arrow i
    rw [hq, all_one_of_min_one hq h0 i] at hi
    have : (2 : ℤ) ^ Γ.a i * Γ.n (i + 1) = 2 ^ 2 * 1 := by rw [hi]; norm_num
    exact (pow_mul_eq_of_odd (Γ.nodd (i + 1)) odd_one this).2

/-- The least positive return time of the minimum: `n p = n 0`, `0 < p`, and no smaller. -/
theorem exists_least_period :
    ∃ p, 0 < p ∧ Γ.n p = Γ.n 0 ∧ ∀ k, 0 < k → k < p → Γ.n k ≠ Γ.n 0 := by
  classical
  have hex : ∃ k, 0 < k ∧ Γ.n k = Γ.n 0 := ⟨m, Γ.hm, by simpa using Γ.nper 0⟩
  exact ⟨Nat.find hex, (Nat.find_spec hex).1, (Nat.find_spec hex).2,
    fun k hk0 hk hkeq => Nat.find_min hex hk ⟨hk0, hkeq⟩⟩

/-- A return time of the minimum is a period of the whole state sequence. -/
theorem nper_of_return {p : ℕ} (hp : Γ.n p = Γ.n 0) (i : ℕ) : Γ.n (i + p) = Γ.n i := by
  have := Γ.shift_eq_of_eq hp i
  rwa [add_comm p i, zero_add] at this

theorem n_add_mul_of_return {p : ℕ} (hp : Γ.n p = Γ.n 0) (k : ℕ) :
    ∀ c, Γ.n (k + c * p) = Γ.n k
  | 0 => by simp
  | c + 1 => by
    rw [show k + (c + 1) * p = (k + c * p) + p by ring, Γ.nper_of_return hp,
      n_add_mul_of_return hp k c]

/-- On the least period the states are pairwise distinct (primitivity). -/
theorem distinct_on_least_period {p : ℕ} (hp0 : 0 < p) (hp : Γ.n p = Γ.n 0)
    (hmin : ∀ k, 0 < k → k < p → Γ.n k ≠ Γ.n 0) :
    ∀ i j, i < p → j < p → Γ.n i = Γ.n j → i = j := by
  have key : ∀ i j, i < j → j < p → Γ.n i = Γ.n j → False := by
    intro i j hij hjp heq
    have hle : i ≤ i * p := Nat.le_mul_of_pos_right i hp0
    have h1 : Γ.n (i * p + (j - i)) = Γ.n (i * p) := by
      have := Γ.shift_eq_of_eq heq (i * p - i)
      rw [show i + (i * p - i) = i * p by omega,
        show j + (i * p - i) = i * p + (j - i) by omega] at this
      exact this.symm
    have h2 : Γ.n (i * p) = Γ.n 0 := by
      have := Γ.n_add_mul_of_return hp 0 i
      rwa [zero_add] at this
    have h3 : Γ.n (j - i) = Γ.n 0 := by
      have := Γ.n_add_mul_of_return hp (j - i) i
      rw [add_comm] at this
      rw [← this, h1, h2]
    exact hmin (j - i) (by omega) (by omega) h3
  intro i j hi hj heq
  rcases lt_trichotomy i j with h | h | h
  · exact (key i j h hj heq).elim
  · exact h
  · exact (key j i h hi heq.symm).elim

/-- The cycle on a return time `p` of its minimum, with `B = 0` when every state lies below
`2 n_0`. -/
def returnCycle {p : ℕ} (hp0 : 0 < p) (hp : Γ.n p = Γ.n 0) (hnarrow : ∀ i, Γ.n i < 2 * Γ.n 0) :
    OddCycle p where
  n := Γ.n
  a := Γ.a
  h := Γ.h
  q := Γ.q
  B := 0
  hm := hp0
  hq := Γ.hq
  nper := Γ.nper_of_return hp
  nodd := Γ.nodd
  nmin := Γ.nmin
  npos := Γ.npos
  arrow := Γ.arrow
  hlo := Γ.hlo
  hhi := Γ.hhi
  hB := fun i => by
    by_contra hne
    have h1 : 1 ≤ Γ.h i := by omega
    have h2 : (2 : ℤ) ^ 1 ≤ 2 ^ Γ.h i := pow_le_pow_right₀ (by norm_num) h1
    have h3 := Γ.hlo i
    have h4 := hnarrow i
    have h5 := Γ.npos
    have h6 := mul_le_mul_of_nonneg_right h2 h5.le
    norm_num at h6
    linarith

/-- **C004 §3's sentence as stated:** every positive odd integer cycle at `q = 1` other than the
fixed point `1` has a state above `2 n_0`, i.e. `H > 2L`. -/
theorem H_gt_two_L (hq : Γ.q = 1) (hnt : Γ.n 0 ≠ 1) : ∃ i, 2 * Γ.n 0 < Γ.n i := by
  by_contra hall
  rw [not_exists] at hall
  have hnarrow : ∀ i, Γ.n i < 2 * Γ.n 0 := fun i => by
    have h1 : ¬ (2 * Γ.n 0 < Γ.n i) := hall i
    rw [not_lt] at h1
    rcases lt_or_eq_of_le h1 with h | h
    · exact h
    · exfalso
      have hodd := Γ.nodd i
      rw [h] at hodd
      exact (Int.not_even_iff_odd.mpr hodd) (even_two_mul _)
  obtain ⟨p, hp0, hp, hmin⟩ := Γ.exists_least_period
  have hprim := Γ.distinct_on_least_period hp0 hp hmin
  have := (Γ.returnCycle hp0 hp hnarrow).narrow_integer_cycle hq rfl hprim
  exact hnt this.2

/-- The same, with "nontrivial" read as "some state is not `1`". -/
theorem H_gt_two_L' (hq : Γ.q = 1) (hnt : ∃ i, Γ.n i ≠ 1) : ∃ i, 2 * Γ.n 0 < Γ.n i := by
  apply Γ.H_gt_two_L hq
  intro h0
  obtain ⟨i, hi⟩ := hnt
  exact hi (Γ.all_one_of_min_one hq h0 i)

end OddCycle

/-! ### C005-d: the integer cycle of a positive word at its reduced parameter

R71 §1 and C004: for a positive word `w` with `D_w > 0`, the rotated intercepts `C_{(i)}` are odd,
`g = gcd(C_w, D_w)` divides all of them and `D_w`, and `n_i = C_{(i)}/g` is a positive odd
integer cycle of the `3x + q` map at the reduced parameter `q = D_w/g`:
`2^{a_i} n_{i+1} = 3 n_i + q` with `a_i` the `i`-th letter ("multiplication by `d` gives an
integer `S_d` cycle"). Packaged as an `OddCycle` for a word starting at its minimal rotated
intercept, with heights chosen from `exists_height`; its chronological word is `w` again and
`gcd(q, n_0) = 1`. -/

namespace OddCycle

/-- The height of a state `x ≥ L` relative to `L > 0` (and `0` below `L`). -/
noncomputable def heightOf (L : ℤ) (hL : 0 < L) (x : ℤ) : ℕ :=
  if hx : L ≤ x then Classical.choose (exists_height hL hx) else 0

theorem heightOf_spec (L : ℤ) (hL : 0 < L) {x : ℤ} (hx : L ≤ x) :
    2 ^ heightOf L hL x * L ≤ x ∧ x < 2 ^ (heightOf L hL x + 1) * L := by
  unfold heightOf
  rw [dite_eq_left hx]
  exact Classical.choose_spec (exists_height hL hx)

/-- `g = gcd(C_w, D_w)` as an integer. -/
def gcdCD (w : List ℕ) : ℤ := ((Int.gcd (C w) (D w) : ℕ) : ℤ)

theorem gcdCD_pos (w : List ℕ) (hw0 : w ≠ []) : 0 < gcdCD w := by
  unfold gcdCD
  have := Int.gcd_pos_of_ne_zero_left (D w) (C_pos hw0).ne'
  exact_mod_cast this

theorem gcdCD_dvd_C (w : List ℕ) : gcdCD w ∣ C w := Int.gcd_dvd_left _ _

theorem gcdCD_dvd_D (w : List ℕ) : gcdCD w ∣ D w := Int.gcd_dvd_right _ _

theorem gcdCD_dvd_rotate (w : List ℕ) (hw0 : w ≠ []) (hpos : ∀ x ∈ w, 1 ≤ x) (i : ℕ) :
    gcdCD w ∣ C (w.rotate i) :=
  dvd_C_rotate_of_dvd hw0 (gcd_isCoprime_two (one_le_sum_of_ne_nil hw0 hpos))
    (gcdCD_dvd_C w) (gcdCD_dvd_D w) i

theorem quot_pos (w : List ℕ) (hw0 : w ≠ []) (hpos : ∀ x ∈ w, 1 ≤ x) (i : ℕ) :
    0 < C (w.rotate i) / gcdCD w := by
  have hg := gcdCD_pos w hw0
  have hC := C_pos (NarrowCycle.rotate_ne_nil hw0 i)
  have hmul := Int.mul_ediv_cancel' (gcdCD_dvd_rotate w hw0 hpos i)
  by_contra hle
  rw [not_lt] at hle
  have := mul_nonneg hg.le (neg_nonneg.mpr hle)
  linarith

theorem quotD_pos (w : List ℕ) (hw0 : w ≠ []) (hD : 0 < D w) : 0 < D w / gcdCD w := by
  have hg := gcdCD_pos w hw0
  have hmul := Int.mul_ediv_cancel' (gcdCD_dvd_D w)
  by_contra hle
  rw [not_lt] at hle
  have := mul_nonneg hg.le (neg_nonneg.mpr hle)
  linarith

theorem quot_odd (w : List ℕ) (hw0 : w ≠ []) (hpos : ∀ x ∈ w, 1 ≤ x) (i : ℕ) :
    Odd (C (w.rotate i) / gcdCD w) := by
  have hodd : Odd (C (w.rotate i)) :=
    C_odd (NarrowCycle.rotate_ne_nil hw0 i) (fun x hx => hpos x (List.mem_rotate.mp hx))
  rw [← Int.mul_ediv_cancel' (gcdCD_dvd_rotate w hw0 hpos i)] at hodd
  exact (Int.odd_mul.mp hodd).2

/-- The exact arrows of the reduced integer cycle: `2^{a_i} n_{i+1} = 3 n_i + q`. -/
theorem quot_arrow (w : List ℕ) (hw0 : w ≠ []) (hpos : ∀ x ∈ w, 1 ≤ x) (i : ℕ) :
    (2 : ℤ) ^ (w.rotate i).headD 0 * (C (w.rotate (i + 1)) / gcdCD w)
      = 3 * (C (w.rotate i) / gcdCD w) + D w / gcdCD w := by
  obtain ⟨x, v, hxv⟩ := List.exists_cons_of_ne_nil (NarrowCycle.rotate_ne_nil hw0 i)
  have hhead : (w.rotate i).headD 0 = x := by rw [hxv, List.headD_cons]
  have hrec := C_rotate_succ hxv
  have hg := gcdCD_pos w hw0
  have h1 := Int.mul_ediv_cancel' (gcdCD_dvd_rotate w hw0 hpos i)
  have h2 := Int.mul_ediv_cancel' (gcdCD_dvd_rotate w hw0 hpos (i + 1))
  have h3 := Int.mul_ediv_cancel' (gcdCD_dvd_D w)
  rw [hhead]
  apply mul_left_cancel₀ hg.ne'
  linear_combination 2 ^ x * h2 - 3 * h1 - h3 + hrec

/-- **The integer cycle of a positive word at its reduced parameter.** For `w ≠ []` with
positive letters, `D_w > 0` and `C_w` minimal among the rotated intercepts: states
`n_i = C(w.rotate i)/g`, letters `a_i` = the first letter of `w.rotate i`, parameter
`q = D_w/g`, heights from `exists_height`. -/
noncomputable def ofWord (w : List ℕ) (hw0 : w ≠ []) (hpos : ∀ x ∈ w, 1 ≤ x) (hD : 0 < D w)
    (hmin : ∀ i, C w ≤ C (w.rotate i)) : OddCycle w.length :=
  let L : ℤ := C (w.rotate 0) / gcdCD w
  have hL : 0 < L := quot_pos w hw0 hpos 0
  have hle : ∀ i, L ≤ C (w.rotate i) / gcdCD w := fun i =>
    Int.ediv_le_ediv (gcdCD_pos w hw0) (by rw [List.rotate_zero]; exact hmin i)
  { n := fun i => C (w.rotate i) / gcdCD w
    a := fun i => (w.rotate i).headD 0
    h := fun i => heightOf L hL (C (w.rotate i) / gcdCD w)
    q := D w / gcdCD w
    B := (Finset.range w.length).sup fun i => heightOf L hL (C (w.rotate i) / gcdCD w)
    hm := List.length_pos_of_ne_nil hw0
    hq := quotD_pos w hw0 hD
    nper := fun i => by
      show C (w.rotate (i + w.length)) / gcdCD w = C (w.rotate i) / gcdCD w
      rw [← List.rotate_mod w (i + w.length), Nat.add_mod_right, List.rotate_mod]
    nodd := quot_odd w hw0 hpos
    nmin := hle
    npos := hL
    arrow := quot_arrow w hw0 hpos
    hlo := fun i => (heightOf_spec L hL (hle i)).1
    hhi := fun i => (heightOf_spec L hL (hle i)).2
    hB := fun i => by
      show heightOf L hL (C (w.rotate i) / gcdCD w)
        ≤ (Finset.range w.length).sup fun j => heightOf L hL (C (w.rotate j) / gcdCD w)
      have hper : C (w.rotate i) = C (w.rotate (i % w.length)) := by rw [List.rotate_mod]
      rw [hper]
      exact Finset.le_sup (f := fun j => heightOf L hL (C (w.rotate j) / gcdCD w))
        (Finset.mem_range.mpr (Nat.mod_lt _ (List.length_pos_of_ne_nil hw0))) }

section ofWordInterface

variable (w : List ℕ) (hw0 : w ≠ []) (hpos : ∀ x ∈ w, 1 ≤ x) (hD : 0 < D w)
  (hmin : ∀ i, C w ≤ C (w.rotate i))

theorem ofWord_n (i : ℕ) : (ofWord w hw0 hpos hD hmin).n i = C (w.rotate i) / gcdCD w := rfl

theorem ofWord_a (i : ℕ) : (ofWord w hw0 hpos hD hmin).a i = (w.rotate i).headD 0 := rfl

theorem ofWord_q : (ofWord w hw0 hpos hD hmin).q = D w / gcdCD w := rfl

/-- `g · n_i = C_{(i)}`. -/
theorem gcdCD_mul_ofWord_n (i : ℕ) :
    gcdCD w * (ofWord w hw0 hpos hD hmin).n i = C (w.rotate i) :=
  Int.mul_ediv_cancel' (gcdCD_dvd_rotate w hw0 hpos i)

/-- `g · q = D_w`. -/
theorem gcdCD_mul_ofWord_q : gcdCD w * (ofWord w hw0 hpos hD hmin).q = D w :=
  Int.mul_ediv_cancel' (gcdCD_dvd_D w)

/-- The cycle is reduced: `gcd(q, n_0) = 1`. -/
theorem ofWord_coprime : IsCoprime (ofWord w hw0 hpos hD hmin).q ((ofWord w hw0 hpos hD hmin).n 0) := by
  rw [Int.isCoprime_iff_gcd_eq_one]
  show Int.gcd (D w / gcdCD w) (C (w.rotate 0) / gcdCD w) = 1
  rw [List.rotate_zero, Int.gcd_comm]
  exact Int.gcd_div_gcd_div_gcd (Int.gcd_pos_of_ne_zero_left _ (C_pos hw0).ne')

/-- Distinct rotated intercepts give a primitive cycle. -/
theorem ofWord_primitive
    (hdist : ∀ i j, i < w.length → j < w.length → C (w.rotate i) = C (w.rotate j) → i = j) :
    ∀ i j, i < w.length → j < w.length →
      (ofWord w hw0 hpos hD hmin).n i = (ofWord w hw0 hpos hD hmin).n j → i = j := by
  intro i j hi hj hij
  apply hdist i j hi hj
  rw [← gcdCD_mul_ofWord_n w hw0 hpos hD hmin i, ← gcdCD_mul_ofWord_n w hw0 hpos hD hmin j, hij]

/-- The chronological word of the reduced cycle is `w` itself. -/
theorem ofWord_word : (ofWord w hw0 hpos hD hmin).word = w := by
  apply List.ext_getElem
  · simp [word]
  · intro i h1 h2
    simp only [word, List.getElem_map, List.getElem_range]
    exact NarrowCycle.headD_rotate w h2

end ofWordInterface

end OddCycle

/-! ### C005-e: repetitions and the least period

Preparations for assembling C005's rotation-block exclusion: the rational cycle of a repeated
word is the base cycle (R71 "repeated words": `C(z^k) D_z = C_z D(z^k)`), so `D(z^k) ∣ C(z^k)`
forces `D_z ∣ C_z`; the least return time of an `OddCycle`'s minimum divides its period and the
chronological word is the corresponding power of the word of one least period; and the cycle on
a return time keeping its height bound. -/

theorem D_rep (z : List ℕ) (k : ℕ) : D (rep z k) = D z * G (2 ^ z.sum) (3 ^ z.length) k := by
  unfold D
  rw [rep_sum, rep_length, pow_mul', pow_mul', ← G_mul]

/-- R71's "repeated words": the fixed point is unchanged by repetition,
`C(z^k)/D(z^k) = C_z/D_z` in cleared form. -/
theorem C_rep_mul_D (z : List ℕ) (k : ℕ) : C (rep z k) * D z = C z * D (rep z k) := by
  rw [C_rep, D_rep]
  ring

/-- If the repeated word has denominator `1` (`D(z^k) ∣ C(z^k)`), so does the base word. -/
theorem D_dvd_C_of_rep_dvd (z : List ℕ) (k : ℕ) (hD : D (rep z k) ≠ 0)
    (h : D (rep z k) ∣ C (rep z k)) : D z ∣ C z := by
  obtain ⟨t, ht⟩ := h
  refine ⟨t, ?_⟩
  have h1 := C_rep_mul_D z k
  rw [ht] at h1
  have h2 : D (rep z k) * (t * D z) = D (rep z k) * C z := by linear_combination h1
  have h3 := mul_left_cancel₀ hD h2
  linarith

theorem rep_add (u : List ℕ) (a b : ℕ) : rep u (a + b) = rep u a ++ rep u b := by
  induction a with
  | zero => simp [rep]
  | succ a ih =>
    rw [show a + 1 + b = (a + b) + 1 by ring, rep, ih, rep, List.append_assoc]

theorem rep_one (u : List ℕ) : rep u 1 = u := by simp [rep]

theorem rep_succ' (u : List ℕ) (k : ℕ) : rep u (k + 1) = rep u k ++ u := by
  rw [rep_add, rep_one]

/-- A `p`-periodic letter function on `k·p` letters is the `k`-fold repetition of its first
period. -/
theorem map_range_mul_eq_rep (f : ℕ → ℕ) (p : ℕ) (hf : ∀ i, f (i + p) = f i) :
    ∀ k, (List.range (k * p)).map f = rep ((List.range p).map f) k
  | 0 => by simp [rep]
  | k + 1 => by
    rw [rep_succ', ← map_range_mul_eq_rep f p hf k, show (k + 1) * p = k * p + p by ring,
      List.range_add, List.map_append, List.map_map]
    congr 1
    apply List.map_congr_left
    intro j _
    show f (k * p + j) = f j
    have hper : ∀ c, f (j + c * p) = f j := by
      intro c
      induction c with
      | zero => simp
      | succ c ih => rw [show j + (c + 1) * p = (j + c * p) + p by ring, hf, ih]
    rw [add_comm]
    exact hper k

namespace OddCycle

variable {m : ℕ} (Γ : OddCycle m)

/-- The cycle on a return time `p` of its minimum, keeping the height bound `B`. -/
def returnCycleB {p : ℕ} (hp0 : 0 < p) (hp : Γ.n p = Γ.n 0) : OddCycle p where
  n := Γ.n
  a := Γ.a
  h := Γ.h
  q := Γ.q
  B := Γ.B
  hm := hp0
  hq := Γ.hq
  nper := Γ.nper_of_return hp
  nodd := Γ.nodd
  nmin := Γ.nmin
  npos := Γ.npos
  arrow := Γ.arrow
  hlo := Γ.hlo
  hhi := Γ.hhi
  hB := Γ.hB

/-- The letters are periodic along any return time of the minimum (determinism). -/
theorem a_add_of_return {p : ℕ} (hp : Γ.n p = Γ.n 0) (i : ℕ) : Γ.a (i + p) = Γ.a i :=
  (Γ.succ_eq_of_eq (Γ.nper_of_return hp i)).2

/-- The least return time of the minimum divides the period. -/
theorem least_period_dvd {p : ℕ} (hp0 : 0 < p) (hp : Γ.n p = Γ.n 0)
    (hmin : ∀ k, 0 < k → k < p → Γ.n k ≠ Γ.n 0) : p ∣ m := by
  have h1 : Γ.n (m % p) = Γ.n 0 := by
    have := Γ.n_add_mul_of_return hp (m % p) (m / p)
    rw [show m % p + m / p * p = m by rw [mul_comm]; exact Nat.mod_add_div m p] at this
    rw [← this]
    simpa using Γ.nper 0
  by_contra hndvd
  have hpos : 0 < m % p := Nat.pos_of_ne_zero (fun h0 => hndvd (Nat.dvd_of_mod_eq_zero h0))
  exact hmin (m % p) hpos (Nat.mod_lt _ hp0) h1

/-- The chronological word is the `m/p`-fold repetition of the word of one return time `p ∣ m`. -/
theorem word_eq_rep {p : ℕ} (hp : Γ.n p = Γ.n 0) (hdvd : p ∣ m) :
    Γ.word = rep ((List.range p).map Γ.a) (m / p) := by
  have hm : m / p * p = m := Nat.div_mul_cancel hdvd
  have h1 : Γ.word = (List.range (m / p * p)).map Γ.a := by
    unfold word
    rw [hm]
  rw [h1]
  exact map_range_mul_eq_rep Γ.a p (Γ.a_add_of_return hp) (m / p)

end OddCycle

/-! ### C005-f: rotations of a repeated word, and the inputs of the rotation-block assembly

Remaining bookkeeping for C005's rotation-block exclusion: `(z^k).rotate u = (z.rotate u)^k`;
for the reduced cycle `ofWord w`, `q = 1` iff `D_w ∣ C_w`, and `B ≤ 2` once every rotated
intercept is below `8 C_w`; and on the least period of a `q = 1` cycle with `B ≤ 2` the word has
coprime totals (the three-band theorem, or trivially for a one-letter period). -/

theorem rep_nil : ∀ k, rep ([] : List ℕ) k = []
  | 0 => rfl
  | k + 1 => by rw [rep, rep_nil k]; rfl

/-- Rotating a repetition by one block length changes nothing. -/
theorem rep_rotate_block (z : List ℕ) (k : ℕ) : (rep z k).rotate z.length = rep z k := by
  rcases k with _ | k
  · simp [rep]
  · show (z ++ rep z k).rotate z.length = z ++ rep z k
    rw [List.rotate_eq_drop_append_take (by simp), List.drop_append_of_le_length le_rfl,
      List.take_append_of_le_length le_rfl, List.drop_length, List.take_length, List.nil_append]
    exact (rep_succ' z k).symm

theorem rep_rotate_mul (z : List ℕ) (k : ℕ) : ∀ c, (rep z k).rotate (c * z.length) = rep z k
  | 0 => by simp
  | c + 1 => by
    rw [show (c + 1) * z.length = c * z.length + z.length by ring, ← List.rotate_rotate,
      rep_rotate_mul z k c, rep_rotate_block]

/-- Rotating `z^{k+1}` by `u ≤ |z|` places: `drop u z ++ z^k ++ take u z`. -/
theorem rep_rotate_le (z : List ℕ) (k u : ℕ) (hu : u ≤ z.length) :
    (rep z (k + 1)).rotate u = z.drop u ++ rep z k ++ z.take u := by
  show (z ++ rep z k).rotate u = z.drop u ++ rep z k ++ z.take u
  rw [List.rotate_eq_drop_append_take (by rw [List.length_append]; omega),
    List.drop_append_of_le_length hu, List.take_append_of_le_length hu]

theorem rep_drop_take (z : List ℕ) (u : ℕ) :
    ∀ k, rep (z.drop u ++ z.take u) (k + 1) = z.drop u ++ rep z k ++ z.take u
  | 0 => by simp [rep]
  | k + 1 => by
    rw [rep_succ', rep_drop_take z u k, rep_succ' z k]
    simp only [List.append_assoc]
    rw [← List.append_assoc (z.take u) (z.drop u) (z.take u), List.take_append_drop]

/-- Rotating a repeated word rotates the base: `(z^k).rotate u = (z.rotate u)^k`. -/
theorem rep_rotate (z : List ℕ) (k u : ℕ) : (rep z k).rotate u = rep (z.rotate u) k := by
  rcases k with _ | k
  · simp [rep]
  rcases Nat.eq_zero_or_pos z.length with hz | hz
  · rw [List.length_eq_zero_iff.mp hz]
    simp [rep_nil]
  have hu : u % z.length ≤ z.length := (Nat.mod_lt u hz).le
  have hdecomp : u = u / z.length * z.length + u % z.length := (Nat.div_add_mod' u z.length).symm
  conv_lhs => rw [hdecomp]
  rw [← List.rotate_rotate, rep_rotate_mul, rep_rotate_le z k _ hu, ← List.rotate_mod z u,
    List.rotate_eq_drop_append_take hu, rep_drop_take]

/-- Every nonempty word has a rotation starting at its minimal rotated intercept. -/
theorem exists_min_rotation (w : List ℕ) (hw0 : w ≠ []) :
    ∃ i₀, ∀ i, C (w.rotate i₀) ≤ C ((w.rotate i₀).rotate i) := by
  have hm0 : 0 < w.length := List.length_pos_of_ne_nil hw0
  obtain ⟨i₀, -, hmin₀⟩ := Finset.exists_min_image (Finset.range w.length)
    (fun i => C (w.rotate i)) ⟨0, Finset.mem_range.mpr hm0⟩
  refine ⟨i₀, fun i => ?_⟩
  rw [List.rotate_rotate, ← List.rotate_mod w (i₀ + i)]
  exact hmin₀ _ (Finset.mem_range.mpr (Nat.mod_lt _ hm0))

namespace OddCycle

/-- `D_w ∣ C_w` (denominator `1`) makes `g = D_w`. -/
theorem gcdCD_eq_D_of_dvd (w : List ℕ) (hD : 0 < D w) (hdvd : D w ∣ C w) : gcdCD w = D w := by
  have h1 : (D w).natAbs ∣ Int.gcd (C w) (D w) :=
    Int.dvd_gcd (Int.natAbs_dvd.mpr hdvd) (Int.natAbs_dvd.mpr dvd_rfl)
  have h2 : Int.gcd (C w) (D w) ∣ (D w).natAbs := by
    have := Int.gcd_dvd_right (C w) (D w)
    rw [← Int.dvd_natAbs] at this
    exact Int.natCast_dvd_natCast.mp this
  have h3 := Nat.dvd_antisymm h1 h2
  unfold gcdCD
  rw [← h3, Int.natAbs_of_nonneg hD.le]

section ofWordCriteria

variable (w : List ℕ) (hw0 : w ≠ []) (hpos : ∀ x ∈ w, 1 ≤ x) (hD : 0 < D w)
  (hmin : ∀ i, C w ≤ C (w.rotate i))

/-- The reduced cycle of `w` has parameter `1` when `D_w ∣ C_w`. -/
theorem ofWord_q_eq_one (hdvd : D w ∣ C w) : (ofWord w hw0 hpos hD hmin).q = 1 := by
  show D w / gcdCD w = 1
  rw [gcdCD_eq_D_of_dvd w hD hdvd, Int.ediv_self hD.ne']

/-- Conversely, parameter `1` means `D_w ∣ C_w`. -/
theorem dvd_of_ofWord_q_eq_one (h1 : (ofWord w hw0 hpos hD hmin).q = 1) : D w ∣ C w := by
  have := gcdCD_mul_ofWord_q w hw0 hpos hD hmin
  rw [h1, mul_one] at this
  rw [← this]
  exact gcdCD_dvd_C w

/-- If every rotated intercept is below `8 C_w` (`H < 8L`), every height is at most `2`. -/
theorem ofWord_B_le_two (h8 : ∀ i, C (w.rotate i) < 8 * C w) :
    (ofWord w hw0 hpos hD hmin).B ≤ 2 := by
  have hg := gcdCD_pos w hw0
  have hn8 : ∀ i, (ofWord w hw0 hpos hD hmin).n i < 8 * (ofWord w hw0 hpos hD hmin).n 0 := by
    intro i
    have h1 := gcdCD_mul_ofWord_n w hw0 hpos hD hmin i
    have h0 := gcdCD_mul_ofWord_n w hw0 hpos hD hmin 0
    rw [List.rotate_zero] at h0
    have h8i := h8 i
    rw [← h1, ← h0] at h8i
    have h2 : gcdCD w * (ofWord w hw0 hpos hD hmin).n i
        < gcdCD w * (8 * (ofWord w hw0 hpos hD hmin).n 0) := by linarith
    exact lt_of_mul_lt_mul_left h2 hg.le
  show (Finset.range w.length).sup _ ≤ 2
  exact Finset.sup_le fun i _ => height_le_two (ofWord w hw0 hpos hD hmin).npos
    ((ofWord w hw0 hpos hD hmin).hlo i) (hn8 i)

end ofWordCriteria

variable {m : ℕ} (Γ : OddCycle m)

/-- On the least period of a `q = 1` cycle with `B ≤ 2`, the valuation word has coprime totals:
the three-band theorem for `p ≥ 2`, and trivially for `p = 1`. -/
theorem coprime_least_period (hq : Γ.q = 1) (hB2 : Γ.B ≤ 2) {p : ℕ} (hp0 : 0 < p)
    (hp : Γ.n p = Γ.n 0) (hmin : ∀ k, 0 < k → k < p → Γ.n k ≠ Γ.n 0) :
    Nat.Coprime ((List.range p).map Γ.a).sum p := by
  rw [sum_map_range]
  rcases Nat.lt_or_ge p 2 with hp1 | hp2
  · have hp1' : p = 1 := by omega
    subst hp1'
    exact (Nat.coprime_one_right_iff _).mpr trivial
  · obtain ⟨_, _, -, -, -, hcop⟩ := (Γ.returnCycleB hp0 hp).three_band hq hB2 hp2
      (Γ.distinct_on_least_period hp0 hp hmin)
    exact hcop

end OddCycle

/-! ### C005-g: the rotation-block exclusion, conditional on the ratio bound

C005 §2's rotation-block theorem, second half: a concatenation of rotations of a primitive
mechanical word `v = mech A₀ m₀ l₀` (`m₀ ≥ 2`) whose cycle has `H < 8L` has reduced denominator
greater than `1`. The assembly: rotate `w` to its minimal intercept, form its reduced integer
cycle (`ofWord`), which has `q = 1` and `B ≤ 2`; on the least period the word has coprime totals
(`coprime_least_period`), so `w` is a power `z^r` of a single block (`word_eq_rep`,
`rep_rotate`, `blocks_identical`), `z` a rotation of `v`; denominator `1` descends to `z`
(`D_dvd_C_of_rep_dvd`), R71-a gives `gcd(C_z, D_z) = 1`, hence `D_z = 1`, excluded by
`mech_D_ne_one`. The hypothesis `H < 8L` is the ratio bound `H/L ≤ R³ < 8` of C005-c, whose
wiring to the actual states is the remaining step. -/

/-- The rotation by `i` is undone by the rotation by `|w| − i mod |w|`. -/
theorem rotate_inv (w : List ℕ) (hw0 : w ≠ []) (i : ℕ) :
    (w.rotate i).rotate (w.length - i % w.length) = w := by
  have hlen : 0 < w.length := List.length_pos_of_ne_nil hw0
  have hr := Nat.mod_lt i hlen
  have hd := Nat.div_add_mod i w.length
  have heq : i + (w.length - i % w.length) = w.length * (i / w.length + 1) := by
    rw [Nat.mul_succ]
    omega
  rw [List.rotate_rotate, heq, List.rotate_length_mul]

namespace OddCycle

/-- **C005's rotation-block exclusion, conditional on the ratio bound.** For a primitive
mechanical word `v = mech A₀ m₀ l₀` (`m₀ ≥ 2`, `A₀ ≥ m₀`, `gcd(A₀, m₀) = 1`) and `w` a
concatenation of `r ≥ 1` rotations of `v` with `D_w > 0`: if every rotated intercept of `w` is
below `8` times every other (`H < 8L` for its cycle), then `D_w ∤ C_w`, i.e. the reduced
denominator of `w`'s cycle exceeds `1`. -/
theorem rotation_block_exclusion {m₀ A₀ l₀ : ℕ} (hm₀ : 2 ≤ m₀) (hAm : m₀ ≤ A₀)
    (hcop : Nat.Coprime A₀ m₀) (hl₀ : l₀ < m₀) (blocks : List (List ℕ))
    (hb : ∀ b ∈ blocks, ∃ i, b = (mech A₀ m₀ l₀).rotate i) (hr : 0 < blocks.length)
    (hD : 0 < D blocks.flatten)
    (h8 : ∀ i j, C (blocks.flatten.rotate i) < 8 * C (blocks.flatten.rotate j)) :
    ¬ D blocks.flatten ∣ C blocks.flatten := by
  intro hq1
  have hm0 : 0 < m₀ := by omega
  have hv_pos : ∀ x ∈ mech A₀ m₀ l₀, 1 ≤ x := mech_pos hm0 A₀ l₀ hAm
  have hv_len : (mech A₀ m₀ l₀).length = m₀ := mech_length A₀ m₀ l₀
  have hv_sum : (mech A₀ m₀ l₀).sum = A₀ := mech_sum hm0 A₀ l₀ hl₀
  have hv_cop : Nat.Coprime (mech A₀ m₀ l₀).sum (mech A₀ m₀ l₀).length := by
    rw [hv_sum, hv_len]
    exact hcop
  have hwlen : blocks.flatten.length = blocks.length * m₀ := by
    rw [flatten_rotations_length _ blocks hb, hv_len]
  have hw0 : blocks.flatten ≠ [] :=
    List.ne_nil_of_length_pos (by rw [hwlen]; exact Nat.mul_pos hr hm0)
  have hpos : ∀ x ∈ blocks.flatten, 1 ≤ x := by
    intro x hx
    obtain ⟨b, hbmem, hxb⟩ := List.mem_flatten.mp hx
    obtain ⟨i, hi⟩ := hb b hbmem
    rw [hi] at hxb
    exact hv_pos x (List.mem_rotate.mp hxb)
  have hsum : 1 ≤ blocks.flatten.sum := one_le_sum_of_ne_nil hw0 hpos
  -- rotate `w` to its minimal intercept
  obtain ⟨i₀, hmin₀⟩ := exists_min_rotation blocks.flatten hw0
  obtain ⟨w', hw'⟩ : ∃ w', w' = blocks.flatten.rotate i₀ := ⟨_, rfl⟩
  rw [← hw'] at hmin₀
  have hw0' : w' ≠ [] := by rw [hw']; exact NarrowCycle.rotate_ne_nil hw0 i₀
  have hpos' : ∀ x ∈ w', 1 ≤ x := by
    intro x hx
    rw [hw'] at hx
    exact hpos x (List.mem_rotate.mp hx)
  have hD' : 0 < D w' := by rw [hw', D_rotate]; exact hD
  have hgw' : gcdCD w' = D w' := by
    rw [hw']
    unfold gcdCD
    rw [gcd_rotate_eq hw0 hsum i₀, D_rotate]
    exact gcdCD_eq_D_of_dvd _ hD hq1
  have hq1' : D w' ∣ C w' := by rw [← hgw']; exact gcdCD_dvd_C w'
  have h8' : ∀ i, C (w'.rotate i) < 8 * C w' := by
    intro i
    rw [hw', List.rotate_rotate]
    exact h8 _ _
  -- the reduced integer cycle of `w'`: parameter `1`, heights at most `2`
  have hq : (ofWord w' hw0' hpos' hD' hmin₀).q = 1 := ofWord_q_eq_one w' hw0' hpos' hD' hmin₀ hq1'
  have hB2 : (ofWord w' hw0' hpos' hD' hmin₀).B ≤ 2 := ofWord_B_le_two w' hw0' hpos' hD' hmin₀ h8'
  obtain ⟨p, hp0, hp, hminp⟩ := (ofWord w' hw0' hpos' hD' hmin₀).exists_least_period
  have hpdvd : p ∣ w'.length := (ofWord w' hw0' hpos' hD' hmin₀).least_period_dvd hp0 hp hminp
  obtain ⟨z, hz⟩ : ∃ z, z = (List.range p).map (ofWord w' hw0' hpos' hD' hmin₀).a := ⟨_, rfl⟩
  have hz_cop : Nat.Coprime z.sum z.length := by
    rw [hz, List.length_map, List.length_range]
    exact (ofWord w' hw0' hpos' hD' hmin₀).coprime_least_period hq hB2 hp0 hp hminp
  obtain ⟨k, hk⟩ : ∃ k, w'.length / p = k := ⟨_, rfl⟩
  have hw'_rep : w' = rep z k := by
    have := (ofWord w' hw0' hpos' hD' hmin₀).word_eq_rep hp hpdvd
    rwa [ofWord_word, hk, ← hz] at this
  -- back to `w` itself: a power of one rotated block
  obtain ⟨u, hu⟩ : ∃ u, u = blocks.flatten.length - i₀ % blocks.flatten.length := ⟨_, rfl⟩
  have hinv : w'.rotate u = blocks.flatten := by
    rw [hw', hu]
    exact rotate_inv _ hw0 i₀
  have hw_rep : blocks.flatten = rep (z.rotate u) k := by
    rw [← hinv, hw'_rep, rep_rotate]
  have hz'_cop : Nat.Coprime (z.rotate u).sum (z.rotate u).length := by
    rwa [(List.rotate_perm z u).sum_eq, List.length_rotate]
  obtain ⟨hk_eq, -, hall⟩ :=
    blocks_identical (mech A₀ m₀ l₀) hv_cop blocks hb hr (z.rotate u) k hw_rep hz'_cop
  obtain ⟨b₀, hb₀⟩ := List.exists_mem_of_length_pos hr
  obtain ⟨i₁, hi₁⟩ := hb b₀ hb₀
  have hz' : z.rotate u = mech A₀ m₀ ((l₀ + i₁ * A₀) % m₀) := by
    rw [← hall b₀ hb₀, hi₁, mech_rotate hm0]
  have hl₁m : (l₀ + i₁ * A₀) % m₀ < m₀ := Nat.mod_lt _ hm0
  -- denominator `1` descends to the block, where R71 forbids it
  have hDw_ne : D (rep (z.rotate u) k) ≠ 0 := by rw [← hw_rep]; exact hD.ne'
  have hdvd_z : D (z.rotate u) ∣ C (z.rotate u) :=
    D_dvd_C_of_rep_dvd _ k hDw_ne (by rw [← hw_rep]; exact hq1)
  have hDz_pos : 0 < D (z.rotate u) := by
    have hG : 0 < G (2 ^ (z.rotate u).sum) (3 ^ (z.rotate u).length) k :=
      G_pos _ _ (by positivity) (by positivity) k (by omega)
    have hprod : 0 < D (z.rotate u) * G (2 ^ (z.rotate u).sum) (3 ^ (z.rotate u).length) k := by
      rw [← D_rep, ← hw_rep]
      exact hD
    exact (mul_pos_iff_of_pos_right hG).mp hprod
  have hgcd := mech_gcd_one_phase hm₀ A₀ hAm hcop hl₁m
  rw [← hz'] at hgcd
  have h1 : (D (z.rotate u)).natAbs ∣ 1 := by
    rw [← hgcd]
    exact Int.dvd_gcd (Int.natAbs_dvd.mpr hdvd_z) (Int.natAbs_dvd.mpr dvd_rfl)
  have hD1 : D (z.rotate u) = 1 := by
    have h2 := Int.natAbs_of_nonneg hDz_pos.le
    rw [Nat.dvd_one.mp h1] at h2
    simpa using h2.symm
  rw [hz', D_mech hm0 _ _ hl₁m] at hD1
  exact mech_D_ne_one hm₀ A₀ hAm hD1

end OddCycle

/-! ### C005-h: the state-bound wiring — the `8L` hypothesis from the ratio bound

C005 §2's rotation-block theorem, first half, on actual words. For `w` a concatenation of
rotations of a nonempty word `v` with `D_v > 0` whose rotated intercepts lie in `[lo, hi]`, the
rational states `x_i = C_{(i)}/D_w` of `w`'s cycle are controlled by the states
`C_{(t)}/D_v ∈ [l, h] = [lo/D_v, hi/D_v]` of `v`'s cycle: the one-block identity
`2^{A₀} C_{((k+1)m₀)} = 3^{m₀} C_{(km₀)} + D_w C_{b_k}` (`C_split`) says the entry states are
the `blockComp` iterates of the closing point `x_0` under the block maps `x ↦ s x + (1 − s) X_k`,
`s = 3^{m₀}/2^{A₀}`, `X_k = C_{b_k}/D_v`, and `x_0` is a fixed point of their composition
(`cycle_point_mem`); inside a block the state is the prefix map of the entry state, with the same
`(α, β)` as the base state of `v` (`state_bound`). Hence `C_{(i)} lo³ ≤ C_{(j)} hi³`
(`flatten_rotations_ratio`), and `hi < 2 lo` gives `C_{(i)} < 8 C_{(j)}`
(`flatten_rotations_lt_eight`), the hypothesis of `rotation_block_exclusion`; for the mechanical
base `C_0 ≤ C_l < 2 C_0` supplies it (`rotation_block_exclusion_mech`). The one-letter bases
`(a)`, `a ≥ 3`, are covered separately (`single_block_exclusion`). -/

/-- The split identity: for the cycle of `u ++ t`, the state after `|u|` arrows is the cycle of
`t ++ u`: `2^{Σu} C(t ++ u) = 3^{|u|} C(u ++ t) + D(u ++ t) C_u`. -/
theorem C_split (u t : List ℕ) :
    (2 : ℤ) ^ u.sum * C (t ++ u) = 3 ^ u.length * C (u ++ t) + D (u ++ t) * C u := by
  simp only [C_append, D, List.sum_append, List.length_append, pow_add]
  ring

/-- Rotating a concatenation of equal-length blocks by one block length rotates the block list. -/
theorem flatten_rotate_one {m₀ : ℕ} (bs : List (List ℕ)) (hbs : bs ≠ [])
    (hlen : ∀ b ∈ bs, b.length = m₀) : bs.flatten.rotate m₀ = (bs.rotate 1).flatten := by
  obtain ⟨b, bs', rfl⟩ := List.exists_cons_of_ne_nil hbs
  rw [List.flatten_cons, ← hlen b (List.mem_cons_self ..), List.rotate_append_length_eq,
    List.rotate_cons_succ, List.rotate_zero, List.flatten_append, List.flatten_cons,
    List.flatten_nil, List.append_nil]

/-- Rotating by `k` block lengths rotates the block list by `k`. -/
theorem flatten_rotate_blocks {m₀ : ℕ} (bs : List (List ℕ)) (hbs : bs ≠ [])
    (hlen : ∀ b ∈ bs, b.length = m₀) (k : ℕ) :
    bs.flatten.rotate (k * m₀) = (bs.rotate k).flatten := by
  induction k with
  | zero => simp
  | succ k ih =>
    rw [add_mul, one_mul, ← List.rotate_rotate bs.flatten (k * m₀) m₀, ih,
      flatten_rotate_one (bs.rotate k) (fun h => hbs (List.rotate_eq_nil_iff.mp h))
        (fun b hb => hlen b (List.mem_rotate.mp hb)),
      List.rotate_rotate]

/-- A cleared prefix identity `P Cn = Q Cx + Dd Cp` in the affine form
`(Q/P) (Cx/Dd) + Cp/P = Cn/Dd`. -/
theorem prefix_div_eq {P Q Dd Cn Cx Cp : ℚ} (hP : P ≠ 0) (hD : Dd ≠ 0)
    (h : P * Cn = Q * Cx + Dd * Cp) : Q / P * (Cx / Dd) + Cp / P = Cn / Dd := by
  rw [div_mul_div_comm, div_add_div _ _ (mul_ne_zero hP hD) hP,
    div_eq_div_iff (mul_ne_zero (mul_ne_zero hP hD) hP) hD]
  linear_combination (-(P * Dd)) * h

/-- The cleared block identity `P Cn = T Cb' + Dw Cb` with `Dv = P − T` as the block map
`x ↦ s x + (1 − s) X`, `s = T/P`, `X = Cb/Dv`. -/
theorem block_step_div_eq {P T Dw Dv Cn Cb' Cb : ℚ} (hP : P ≠ 0) (hDw : Dw ≠ 0) (hDv : Dv ≠ 0)
    (hDv' : Dv = P - T) (h : P * Cn = T * Cb' + Dw * Cb) :
    T / P * (Cb' / Dw) + (1 - T / P) * (Cb / Dv) = Cn / Dw := by
  have h1 : 1 - T / P = Dv / P := by rw [hDv', sub_div, div_self hP]
  have h2 : Dv / P * (Cb / Dv) = Cb / P := by
    rw [div_mul_div_comm, mul_comm Dv Cb, mul_div_mul_right _ _ hDv]
  rw [h1, h2]
  exact prefix_div_eq hP hDw h

/-- **C005's ratio bound on actual words.** For `w` a concatenation of `r ≥ 1` rotations of a
nonempty word `v` with `D_v > 0` whose rotated intercepts all lie in `[lo, hi]` (`lo > 0`), any
two rotated intercepts of `w` satisfy `C_{(i)} lo³ ≤ C_{(j)} hi³`: the cleared form of
`H/L ≤ (hi/lo)³ = R³`. -/
theorem flatten_rotations_ratio (v : List ℕ) (hv0 : v ≠ []) (hDv : 0 < D v) {lo hi : ℤ}
    (hlo0 : 0 < lo) (hlo : ∀ t, lo ≤ C (v.rotate t)) (hhi : ∀ t, C (v.rotate t) ≤ hi)
    (blocks : List (List ℕ)) (hb : ∀ b ∈ blocks, ∃ i, b = v.rotate i) (hr : 0 < blocks.length)
    (i j : ℕ) : C (blocks.flatten.rotate i) * lo ^ 3 ≤ C (blocks.flatten.rotate j) * hi ^ 3 := by
  obtain ⟨w, hw⟩ : ∃ w, w = blocks.flatten := ⟨_, rfl⟩
  rw [← hw]
  have hm0 : 0 < v.length := List.length_pos_of_ne_nil hv0
  have hbs0 : blocks ≠ [] := List.ne_nil_of_length_pos hr
  have hlen : ∀ b ∈ blocks, b.length = v.length := fun b hb' => by
    obtain ⟨t, ht⟩ := hb b hb'
    rw [ht, List.length_rotate]
  have hwlen : w.length = blocks.length * v.length := by
    rw [hw]; exact flatten_rotations_length v blocks hb
  have hwsum : w.sum = blocks.length * v.sum := by
    rw [hw]; exact flatten_rotations_sum v blocks hb
  have h32 : (3 : ℤ) ^ v.length < 2 ^ v.sum := by
    have := hDv
    rw [D] at this
    exact sub_pos.mp this
  have hDw : 0 < D w := by
    rw [D, hwlen, hwsum, pow_mul', pow_mul']
    exact sub_pos.mpr (pow_lt_pow_left₀ h32 (by positivity) hr.ne')
  have hDwQ : (0 : ℚ) < D w := by exact_mod_cast hDw
  have hDvQ : (0 : ℚ) < D v := by exact_mod_cast hDv
  have hDv' : (D v : ℚ) = 2 ^ v.sum - 3 ^ v.length := by simp [D]
  have hP : (2 : ℚ) ^ v.sum ≠ 0 := by positivity
  -- the blocks in rotation order: `blocks.rotate k = b :: bs`, `b` a rotation of `v`
  have hdec : ∀ k, ∃ b bs τ, blocks.rotate k = b :: bs ∧ b = v.rotate τ := by
    intro k
    obtain ⟨b, bs, hcons⟩ :=
      List.exists_cons_of_ne_nil (fun h => hbs0 (List.rotate_eq_nil_iff.mp h) : blocks.rotate k ≠ [])
    obtain ⟨τ, hτ⟩ := hb b (List.mem_rotate.mp (by rw [hcons]; exact List.mem_cons_self ..))
    exact ⟨b, bs, τ, hcons, hτ⟩
  -- the rational data: block slope, block fixed points, entry states, the band `[l, h]`
  obtain ⟨s, hs⟩ : ∃ s : ℚ, s = 3 ^ v.length / 2 ^ v.sum := ⟨_, rfl⟩
  obtain ⟨tt, htt⟩ : ∃ tt : ℕ → ℚ, ∀ k, tt k = (C ((blocks.rotate k).headD []) : ℚ) / D v :=
    ⟨_, fun _ => rfl⟩
  obtain ⟨x, hx⟩ : ∃ x : ℕ → ℚ, ∀ k, x k = (C (w.rotate (k * v.length)) : ℚ) / D w :=
    ⟨_, fun _ => rfl⟩
  have hs0 : 0 < s := by rw [hs]; positivity
  have hs1 : s < 1 := by
    rw [hs, div_lt_one (by positivity)]
    exact_mod_cast h32
  have hl : (0 : ℚ) < lo / D v := div_pos (by exact_mod_cast hlo0) hDvQ
  have hlh : (lo : ℚ) / D v ≤ hi / D v :=
    div_le_div_of_nonneg_right (by exact_mod_cast (hlo 0).trans (hhi 0)) hDvQ.le
  have hvlo : ∀ t, (lo : ℚ) / D v ≤ (C (v.rotate t) : ℚ) / D v := fun t =>
    div_le_div_of_nonneg_right (by exact_mod_cast hlo t) hDvQ.le
  have hvhi : ∀ t, (C (v.rotate t) : ℚ) / D v ≤ hi / D v := fun t =>
    div_le_div_of_nonneg_right (by exact_mod_cast hhi t) hDvQ.le
  have ht : ∀ k, (lo : ℚ) / D v ≤ tt k ∧ tt k ≤ hi / D v := by
    intro k
    obtain ⟨b, bs, τ, hcons, hτ⟩ := hdec k
    rw [htt k, hcons, List.headD_cons, hτ]
    exact ⟨hvlo τ, hvhi τ⟩
  -- the one-block step: `x (k+1) = s x k + (1 − s) X_k`
  have hstep : ∀ k, x (k + 1) = s * x k + (1 - s) * tt k := by
    intro k
    obtain ⟨b, bs, τ, hcons, hτ⟩ := hdec k
    have hkb : w.rotate (k * v.length) = b ++ bs.flatten := by
      rw [hw, flatten_rotate_blocks blocks hbs0 hlen k, hcons, List.flatten_cons]
    have hblen : b.length = v.length := by rw [hτ, List.length_rotate]
    have hbsum : b.sum = v.sum := by rw [hτ, (List.rotate_perm v τ).sum_eq]
    have hk1 : w.rotate ((k + 1) * v.length) = bs.flatten ++ b := by
      rw [add_mul, one_mul, ← List.rotate_rotate, hkb, ← hblen, List.rotate_append_length_eq]
    have hid := C_split b bs.flatten
    rw [hbsum, hblen, ← hkb, D_rotate, ← hk1] at hid
    have hidQ : (2 : ℚ) ^ v.sum * (C (w.rotate ((k + 1) * v.length)) : ℚ) =
        3 ^ v.length * (C (w.rotate (k * v.length)) : ℚ) + (D w : ℚ) * (C b : ℚ) := by
      exact_mod_cast hid
    rw [hx, hx, htt k, hcons, List.headD_cons, hs]
    exact (block_step_div_eq hP hDwQ.ne' hDvQ.ne' hDv' hidQ).symm
  -- entry states are `blockComp` iterates of the closing point, which is a fixed point
  have hcomp : ∀ k, blockComp s tt k (x 0) = x k := by
    intro k
    induction k with
    | zero => simp [blockComp]
    | succ k ih =>
      simp only [blockComp]
      rw [ih, hstep]
  have hfix : blockComp s tt blocks.length (x 0) = x 0 := by
    rw [hcomp, hx, hx, zero_mul, List.rotate_zero, ← hwlen, List.rotate_length]
  have hx0 := cycle_point_mem hs0 hs1 ht hlh hr hfix
  have hxk : ∀ k, (lo : ℚ) / D v ≤ x k ∧ x k ≤ hi / D v := fun k => by
    rw [← hcomp k]
    exact blockComp_mem hs0.le hs1.le ht hx0.1 hx0.2 k
  -- every state: a prefix map of its entry state, with the base state's `(α, β)`
  have hsb : ∀ i, (lo : ℚ) / D v * (lo / D v) ≤ hi / D v * ((C (w.rotate i) : ℚ) / D w) ∧
      (lo : ℚ) / D v * ((C (w.rotate i) : ℚ) / D w) ≤ hi / D v * (hi / D v) := by
    intro i
    obtain ⟨k, j, hj, rfl⟩ : ∃ k j, j < v.length ∧ i = k * v.length + j :=
      ⟨i / v.length, i % v.length, Nat.mod_lt _ hm0, (Nat.div_add_mod' _ _).symm⟩
    obtain ⟨b, bs, τ, hcons, hτ⟩ := hdec k
    have hkb : w.rotate (k * v.length) = b ++ bs.flatten := by
      rw [hw, flatten_rotate_blocks blocks hbs0 hlen k, hcons, List.flatten_cons]
    have hblen : b.length = v.length := by rw [hτ, List.length_rotate]
    have hjb : j < b.length := by rw [hblen]; exact hj
    have htl : (b.take j).length = j := by rw [List.length_take, min_eq_left hjb.le]
    have hrot : (b ++ bs.flatten).rotate j = (b.drop j ++ bs.flatten) ++ b.take j := by
      have := List.rotate_append_length_eq (b.take j) (b.drop j ++ bs.flatten)
      rwa [htl, ← List.append_assoc, List.take_append_drop] at this
    have hrotv : b.rotate j = b.drop j ++ b.take j := by
      have := List.rotate_append_length_eq (b.take j) (b.drop j)
      rwa [htl, List.take_append_drop] at this
    have hwi : w.rotate (k * v.length + j) = (b.drop j ++ bs.flatten) ++ b.take j := by
      rw [← List.rotate_rotate, hkb, hrot]
    have hbj : b.rotate j = v.rotate (τ + j) := by rw [hτ, List.rotate_rotate]
    have hDb : D b = D v := by rw [hτ, D_rotate]
    have hw_id : (2 : ℤ) ^ (b.take j).sum * C (w.rotate (k * v.length + j)) =
        3 ^ j * C (w.rotate (k * v.length)) + D w * C (b.take j) := by
      have := C_split (b.take j) (b.drop j ++ bs.flatten)
      rwa [htl, ← List.append_assoc, List.take_append_drop, ← hkb, D_rotate, ← hwi] at this
    have hv_id : (2 : ℤ) ^ (b.take j).sum * C (v.rotate (τ + j)) =
        3 ^ j * C b + D v * C (b.take j) := by
      have := C_split (b.take j) (b.drop j)
      rwa [htl, List.take_append_drop, ← hrotv, hbj, hDb] at this
    have hP' : (2 : ℚ) ^ (b.take j).sum ≠ 0 := by positivity
    have hw_idQ : (2 : ℚ) ^ (b.take j).sum * (C (w.rotate (k * v.length + j)) : ℚ) =
        3 ^ j * (C (w.rotate (k * v.length)) : ℚ) + (D w : ℚ) * (C (b.take j) : ℚ) := by
      exact_mod_cast hw_id
    have hv_idQ : (2 : ℚ) ^ (b.take j).sum * (C (v.rotate (τ + j)) : ℚ) =
        3 ^ j * (C b : ℚ) + (D v : ℚ) * (C (b.take j) : ℚ) := by
      exact_mod_cast hv_id
    have hgx := prefix_div_eq hP' hDwQ.ne' hw_idQ
    have hgX := prefix_div_eq hP' hDvQ.ne' hv_idQ
    have hXk : tt k = (C b : ℚ) / D v := by rw [htt k, hcons, List.headD_cons]
    rw [← hgx, ← hx]
    refine state_bound (by positivity)
      (div_nonneg (by exact_mod_cast C_nonneg _) (by positivity)) hl hlh (hxk k).1 (hxk k).2
      (ht k).1 (ht k).2 ?_ ?_
    · rw [hXk, hgX]; exact hvlo (τ + j)
    · rw [hXk, hgX]; exact hvhi (τ + j)
  have key := ratio_bound hl hlh (hsb i).2 (hsb j).1
  rw [div_pow, div_pow, div_mul_div_comm, div_mul_div_comm,
    div_le_div_iff_of_pos_right (mul_pos hDwQ (pow_pos hDvQ 3))] at key
  exact_mod_cast key

/-- The `8L` hypothesis of `rotation_block_exclusion` from the ratio bound: when the rotated
intercepts of the base lie in `[lo, 2lo)` (`R < 2`), every rotated intercept of the
concatenation is below `8` times every other (`H/L ≤ R³ < 8`). -/
theorem flatten_rotations_lt_eight (v : List ℕ) (hv0 : v ≠ []) (hDv : 0 < D v) {lo hi : ℤ}
    (hlo0 : 0 < lo) (hlo : ∀ t, lo ≤ C (v.rotate t)) (hhi : ∀ t, C (v.rotate t) ≤ hi)
    (h2 : hi < 2 * lo) (blocks : List (List ℕ)) (hb : ∀ b ∈ blocks, ∃ i, b = v.rotate i)
    (hr : 0 < blocks.length) (i j : ℕ) :
    C (blocks.flatten.rotate i) < 8 * C (blocks.flatten.rotate j) := by
  have key := flatten_rotations_ratio v hv0 hDv hlo0 hlo hhi blocks hb hr i j
  have hhi0 : 0 ≤ hi := hlo0.le.trans ((hlo 0).trans (hhi 0))
  have hcube : hi ^ 3 < 8 * lo ^ 3 := by
    have := pow_lt_pow_left₀ h2 hhi0 (by norm_num : (3 : ℕ) ≠ 0)
    rw [mul_pow] at this
    norm_num at this
    linarith
  have hw0 : blocks.flatten ≠ [] := List.ne_nil_of_length_pos (by
    rw [flatten_rotations_length v blocks hb]
    exact Nat.mul_pos hr (List.length_pos_of_ne_nil hv0))
  have hCj : 0 < C (blocks.flatten.rotate j) := C_pos (NarrowCycle.rotate_ne_nil hw0 j)
  have h1 : C (blocks.flatten.rotate j) * hi ^ 3 < C (blocks.flatten.rotate j) * (8 * lo ^ 3) :=
    mul_lt_mul_of_pos_left hcube hCj
  have h3 : C (blocks.flatten.rotate i) * lo ^ 3 < 8 * C (blocks.flatten.rotate j) * lo ^ 3 := by
    linarith
  exact lt_of_mul_lt_mul_right h3 (pow_pos hlo0 3).le

/-- The one-letter base `(a)`, `a ≥ 3` (the `m₀ = 1` mechanical words other than `(2)`): every
concatenation of its copies has `D ∤ C`, since `C_{(a)} = 1` and `D_{(a)} = 2^a − 3 ≥ 5`. -/
theorem single_block_exclusion (a : ℕ) (ha : 3 ≤ a) (blocks : List (List ℕ))
    (hb : ∀ b ∈ blocks, ∃ i, b = [a].rotate i) (hr : 0 < blocks.length) :
    ¬ D blocks.flatten ∣ C blocks.flatten := by
  have hall : ∀ b ∈ blocks, b = [a] := fun b hb' => by
    obtain ⟨i, hi⟩ := hb b hb'
    rw [hi, List.rotate_singleton]
  have hrep : blocks.flatten = rep [a] blocks.length := by
    clear hb hr
    induction blocks with
    | nil => rfl
    | cons b bs ih =>
      rw [List.flatten_cons, List.length_cons, rep, hall b (List.mem_cons_self ..),
        ih (fun c hc => hall c (List.mem_cons_of_mem _ hc))]
  have h8 : (8 : ℤ) ≤ 2 ^ a :=
    calc (8 : ℤ) = 2 ^ 3 := by norm_num
      _ ≤ 2 ^ a := pow_le_pow_right₀ (by norm_num) ha
  have hDa : D [a] = 2 ^ a - 3 := by simp [D]
  have hCa : C [a] = 1 := by simp [C]
  have hDpos : 0 < D blocks.flatten := by
    rw [hrep, D_rep, hDa]
    exact mul_pos (by omega) (G_pos _ _ (by positivity) (by positivity) _ hr)
  intro hdvd
  rw [hrep] at hdvd
  have hdiv := D_dvd_C_of_rep_dvd [a] blocks.length (by rw [← hrep]; exact hDpos.ne') hdvd
  rw [hDa, hCa] at hdiv
  have := Int.le_of_dvd one_pos hdiv
  omega

namespace OddCycle

/-- **C005's rotation-block exclusion for the mechanical base, unconditional.** For
`v = mech A₀ m₀ l₀` with `2 ≤ m₀ ≤ A₀`, `gcd(A₀, m₀) = 1` and `3^{m₀} < 2^{A₀}` (`D_v > 0`),
every concatenation of `r ≥ 1` rotations of `v` has `D_w ∤ C_w`: the reduced denominator of its
cycle exceeds `1`. The `8L` hypothesis of `rotation_block_exclusion` is supplied by
`flatten_rotations_lt_eight` from `C_0 ≤ C_l < 2 C_0` (`C_mech_zero_le`, `C_mech_lt_two`). -/
theorem rotation_block_exclusion_mech {m₀ A₀ l₀ : ℕ} (hm₀ : 2 ≤ m₀) (hAm : m₀ ≤ A₀)
    (hcop : Nat.Coprime A₀ m₀) (hl₀ : l₀ < m₀) (h32 : (3 : ℤ) ^ m₀ < 2 ^ A₀)
    (blocks : List (List ℕ)) (hb : ∀ b ∈ blocks, ∃ i, b = (mech A₀ m₀ l₀).rotate i)
    (hr : 0 < blocks.length) : ¬ D blocks.flatten ∣ C blocks.flatten := by
  have hm0 : 0 < m₀ := by omega
  have hv0 : mech A₀ m₀ l₀ ≠ [] :=
    List.ne_nil_of_length_pos (by rw [mech_length]; exact hm0)
  have hDv : 0 < D (mech A₀ m₀ l₀) := by
    rw [D_mech hm0 A₀ l₀ hl₀]
    exact sub_pos.mpr h32
  have hlo : ∀ t, C (mech A₀ m₀ 0) ≤ C ((mech A₀ m₀ l₀).rotate t) := by
    intro t
    rw [mech_rotate hm0]
    exact C_mech_zero_le hm0 A₀ _ (Nat.mod_lt _ hm0)
  have hhi : ∀ t, C ((mech A₀ m₀ l₀).rotate t) ≤ 2 * C (mech A₀ m₀ 0) - 1 := by
    intro t
    rw [mech_rotate hm0]
    have := C_mech_lt_two hm0 A₀ _ (Nat.mod_lt (l₀ + t * A₀) hm0)
    omega
  have hlo0 : 0 < C (mech A₀ m₀ 0) :=
    C_pos (List.ne_nil_of_length_pos (by rw [mech_length]; exact hm0))
  have hD : 0 < D blocks.flatten := by
    rw [D, flatten_rotations_length _ blocks hb, flatten_rotations_sum _ blocks hb, mech_length,
      mech_sum hm0 A₀ l₀ hl₀, pow_mul', pow_mul']
    exact sub_pos.mpr (pow_lt_pow_left₀ h32 (by positivity) hr.ne')
  exact rotation_block_exclusion hm₀ hAm hcop hl₀ blocks hb hr hD
    (flatten_rotations_lt_eight _ hv0 hDv hlo0 hlo hhi (by omega) blocks hb hr)

end OddCycle

/-! ### R71-b: repeated words — `den(z^k) = den(z)` and R71's (3) in full

R71 §2's repeated case: for `g = gcd(A, k) > 1` the phase-`l` mechanical word with parameters
`(A, k)` is `g` repeats of the phase-`h` word with parameters `(A/g, k/g)`, where `l = g h + r`,
`0 ≤ r < g` (the floor identity `⌊(jA + l)/k⌋ = ⌊(jA₀ + h)/k₀⌋`), and "its positive fixed point is
unchanged by repetition", so the reduced denominator is that of the primitive word:
`d = 2^{A/g} − 3^{k/g}` for every mechanical word (R71's (3)); R71-a gave the primitive case
`gcd(C, D) = 1`. Here `den w := D_w / gcd(C_w, D_w)`; `C(z^k) = C_z G_k` and `D(z^k) = D_z G_k`
scale the gcd by `G_k` (`gcdCD_rep`), so `den (z^k) = den z` (`den_rep`); `mech_rep` is the
power decomposition; `den_mech` is (3). R71's example: `(k, A) = (6, 10)` has `D = 295` but
`d = 2^5 − 3^3 = 5`. -/

/-- The reduced denominator `den(w) = D_w / gcd(C_w, D_w)` of the cycle-spectrum brief. -/
def den (w : List ℕ) : ℤ := D w / OddCycle.gcdCD w

/-- The gcd of a repeated word scales by `G_k`. -/
theorem gcdCD_rep (z : List ℕ) {k : ℕ} (hk : 1 ≤ k) :
    OddCycle.gcdCD (rep z k) = G (2 ^ z.sum) (3 ^ z.length) k * OddCycle.gcdCD z := by
  have hG : 0 < G (2 ^ z.sum) (3 ^ z.length) k :=
    G_pos _ _ (by positivity) (by positivity) k hk
  unfold OddCycle.gcdCD
  rw [C_rep, D_rep, mul_comm (C z), mul_comm (D z), Int.gcd_mul_left, Nat.cast_mul,
    Int.natAbs_of_nonneg hG.le]

/-- R71 §2: the reduced denominator is unchanged by repetition. -/
theorem den_rep (z : List ℕ) {k : ℕ} (hk : 1 ≤ k) : den (rep z k) = den z := by
  have hG : 0 < G (2 ^ z.sum) (3 ^ z.length) k :=
    G_pos _ _ (by positivity) (by positivity) k hk
  unfold den
  rw [D_rep, gcdCD_rep z hk, mul_comm (D z), Int.mul_ediv_mul_of_pos _ _ hG]

/-- `⌊(gX + r)/(g k₀)⌋ = ⌊X/k₀⌋` for `r < g`. -/
theorem div_scale {g k₀ : ℕ} (hg : 0 < g) (hk₀ : 0 < k₀) (X r : ℕ) (hr : r < g) :
    (g * X + r) / (g * k₀) = X / k₀ := by
  have hdm := Nat.div_add_mod X k₀
  have hlt : g * (X % k₀) + r < g * k₀ := by
    have h1 : X % k₀ + 1 ≤ k₀ := Nat.mod_lt X hk₀
    have h2 := Nat.mul_le_mul_left g h1
    rw [Nat.mul_add, Nat.mul_one] at h2
    omega
  have heq : g * X + r = g * k₀ * (X / k₀) + (g * (X % k₀) + r) := by
    rw [show g * X = g * (k₀ * (X / k₀) + X % k₀) by rw [hdm]]
    ring
  rw [heq, Nat.mul_add_div (Nat.mul_pos hg hk₀), Nat.div_eq_of_lt hlt, Nat.add_zero]

/-- R71 §2: the mechanical word with parameters `(gA₀, gk₀)` and phase `gh + r` (`r < g`) is `g`
repeats of the word with parameters `(A₀, k₀)` and phase `h`. -/
theorem mech_rep {g A₀ k₀ h r : ℕ} (hg : 0 < g) (hk₀ : 0 < k₀) (hr : r < g) :
    mech (g * A₀) (g * k₀) (g * h + r) = rep (mech A₀ k₀ h) g := by
  have hF : ∀ j, (j * (g * A₀) + (g * h + r)) / (g * k₀) = (j * A₀ + h) / k₀ := by
    intro j
    rw [show j * (g * A₀) + (g * h + r) = g * (j * A₀ + h) + r by ring]
    exact div_scale hg hk₀ _ r hr
  have hper : ∀ j, (j + k₀) * A₀ + h = (j * A₀ + h) + k₀ * A₀ := fun j => by ring
  unfold mech diffWord
  simp only [hF]
  have hf : ∀ i, ((i + k₀ + 1) * A₀ + h) / k₀ - ((i + k₀) * A₀ + h) / k₀ =
      ((i + 1) * A₀ + h) / k₀ - (i * A₀ + h) / k₀ := by
    intro i
    rw [show i + k₀ + 1 = (i + 1) + k₀ by ring, hper (i + 1), hper i,
      Nat.add_mul_div_left _ _ hk₀, Nat.add_mul_div_left _ _ hk₀]
    omega
  exact map_range_mul_eq_rep (fun j => ((j + 1) * A₀ + h) / k₀ - (j * A₀ + h) / k₀) k₀ hf g

/-- R71-a extended to `k₀ = 1`: every primitive mechanical word has `gcd(C, D) = 1`. -/
theorem mech_gcd_one_phase' {k₀ : ℕ} (hk₀ : 0 < k₀) (A₀ : ℕ) (hAm : k₀ ≤ A₀)
    (hcop : Nat.Coprime A₀ k₀) {h : ℕ} (hh : h < k₀) :
    Int.gcd (C (mech A₀ k₀ h)) (D (mech A₀ k₀ h)) = 1 := by
  rcases Nat.lt_or_ge k₀ 2 with h1 | h2
  · have hk1 : k₀ = 1 := by omega
    subst hk1
    have hh0 : h = 0 := by omega
    subst hh0
    have hC : C (mech A₀ 1 0) = 1 := by
      rw [C_mech A₀ 0 (show 0 < 1 by norm_num)]
      simp
    rw [hC, Int.gcd_one_left]
  · exact mech_gcd_one_phase h2 A₀ hAm hcop hh

/-- **R71's (3)**: every mechanical word with parameters `(A, k)`, `k ≤ A`, phase `l < k`, has
reduced denominator `2^{A/g} − 3^{k/g}` with `g = gcd(A, k)`. -/
theorem den_mech {A k l : ℕ} (hk : 0 < k) (hAk : k ≤ A) (hl : l < k) :
    den (mech A k l) = 2 ^ (A / Nat.gcd A k) - 3 ^ (k / Nat.gcd A k) := by
  obtain ⟨g, hg⟩ : ∃ g, g = Nat.gcd A k := ⟨_, rfl⟩
  have hgpos : 0 < g := by rw [hg]; exact Nat.gcd_pos_of_pos_right _ hk
  have hgA : g ∣ A := by rw [hg]; exact Nat.gcd_dvd_left _ _
  have hgk : g ∣ k := by rw [hg]; exact Nat.gcd_dvd_right _ _
  have hA : A = g * (A / g) := (Nat.mul_div_cancel' hgA).symm
  have hk' : k = g * (k / g) := (Nat.mul_div_cancel' hgk).symm
  have hl' : l = g * (l / g) + l % g := (Nat.div_add_mod l g).symm
  have hk₀ : 0 < k / g := Nat.div_pos (Nat.le_of_dvd hk hgk) hgpos
  have hcop : Nat.Coprime (A / g) (k / g) := by
    rw [hg]
    exact Nat.coprime_div_gcd_div_gcd (Nat.gcd_pos_of_pos_right _ hk)
  have hAm : k / g ≤ A / g := Nat.div_le_div_right hAk
  have hh : l / g < k / g := by
    apply Nat.div_lt_of_lt_mul
    rw [← hk']
    exact hl
  rw [← hg]
  conv_lhs => rw [hA, hk', hl']
  rw [mech_rep hgpos hk₀ (Nat.mod_lt l hgpos), den_rep _ hgpos]
  unfold den OddCycle.gcdCD
  rw [mech_gcd_one_phase' hk₀ (A / g) hAm hcop hh, Nat.cast_one, Int.ediv_one,
    D_mech hk₀ (A / g) (l / g) hh]

/-! ### R71-c: the state bound (5) — rational cycles arbitrarily far above the absorber

R71 §3: for `k ≥ 1` take `A = ⌈k log₂ 3⌉`, so `3^k < 2^A < 2·3^k` and `0 < D < 3^k`. Every
summand of `C` is `3^{k−1−j} 2^{⌊(jA + l)/k⌋} > (3^{k−1}/2)(2^{A/k}/3)^j ≥ 3^{k−1}/2`, so summing
`k` terms and dividing by `D < 3^k` gives every cycle state `x = C_{(l)}/D > k/6`. Here:
`mech_term_lower` (`3^j ≤ 2^{⌊(jA+l)/k⌋+1}`, from `2^A ≥ 3^k` by taking `k`-th powers),
`mech_state_bound` (`k D < 6 C` for every phase, cleared), `exists_total` (the bit length of
`3^k`), and `mech_cycle_state_bound`: the reduced integer `3x+q` cycle of the phase-`0` word
(`ofWord`) has every state above `k q/6`, `q = den` — R71's "the corresponding integer `S_d`
cycle has every state `> C d`". -/

/-- `3^j ≤ 2^{⌊(jA + l)/k⌋ + 1}` when `3^k ≤ 2^A`: compare `k`-th powers. -/
theorem mech_term_lower {A k : ℕ} (hk : 0 < k) (hA : 3 ^ k ≤ 2 ^ A) (l j : ℕ) :
    3 ^ j ≤ 2 ^ ((j * A + l) / k + 1) := by
  have h1 : j * A + l < k * ((j * A + l) / k + 1) := Nat.lt_mul_div_succ _ hk
  have h2 : (3 ^ j) ^ k ≤ (2 ^ ((j * A + l) / k + 1)) ^ k := by
    calc (3 ^ j) ^ k = (3 ^ k) ^ j := by rw [← pow_mul, ← pow_mul, Nat.mul_comm]
      _ ≤ (2 ^ A) ^ j := Nat.pow_le_pow_left hA j
      _ = 2 ^ (j * A) := by rw [← pow_mul, Nat.mul_comm]
      _ ≤ 2 ^ (k * ((j * A + l) / k + 1)) := Nat.pow_le_pow_right (by norm_num) (by omega)
      _ = (2 ^ ((j * A + l) / k + 1)) ^ k := by rw [← pow_mul, Nat.mul_comm]
  exact (Nat.pow_le_pow_iff_left hk.ne').mp h2

/-- Each summand of `C` is at least `3^{k−1}/2` (cleared). -/
theorem mech_summand_lower {A k l : ℕ} (hk : 0 < k) (hA : 3 ^ k ≤ 2 ^ A) {j : ℕ} (hj : j < k) :
    (3 : ℤ) ^ (k - 1) ≤ 2 * (3 ^ (k - (j + 1)) * 2 ^ ((j * A + l) / k)) := by
  have h' : (3 : ℤ) ^ j ≤ 2 ^ ((j * A + l) / k + 1) := by
    exact_mod_cast mech_term_lower hk hA l j
  have hsplit : k - 1 = (k - (j + 1)) + j := by omega
  rw [hsplit, pow_add]
  calc (3 : ℤ) ^ (k - (j + 1)) * 3 ^ j ≤ 3 ^ (k - (j + 1)) * 2 ^ ((j * A + l) / k + 1) :=
        mul_le_mul_of_nonneg_left h' (by positivity)
    _ = 2 * (3 ^ (k - (j + 1)) * 2 ^ ((j * A + l) / k)) := by rw [pow_succ]; ring

/-- **R71's (5), cleared**: for a mechanical word with `3^k < 2^A < 2·3^k`, every cycle state
exceeds `k/6`: `k D < 6 C` for every phase `l`. -/
theorem mech_state_bound {A k l : ℕ} (hk : 0 < k) (hl : l < k) (hpos : 3 ^ k < 2 ^ A)
    (hsmall : 2 ^ A < 2 * 3 ^ k) : (k : ℤ) * D (mech A k l) < 6 * C (mech A k l) := by
  have hsum : (k : ℤ) * 3 ^ (k - 1) ≤ 2 * C (mech A k l) := by
    rw [C_mech A l hl, Finset.mul_sum]
    have := Finset.sum_le_sum (s := Finset.range k) (f := fun _ => (3 : ℤ) ^ (k - 1))
      (g := fun j => 2 * (3 ^ (k - (j + 1)) * 2 ^ ((j * A + l) / k)))
      (fun j hj => mech_summand_lower hk hpos.le (Finset.mem_range.mp hj))
    rw [Finset.sum_const, Finset.card_range, nsmul_eq_mul] at this
    exact this
  have h3 : (3 : ℤ) ^ k = 3 * 3 ^ (k - 1) := by
    rw [← pow_succ']
    congr 1
    omega
  have hA' : (2 : ℤ) ^ A < 2 * 3 ^ k := by exact_mod_cast hsmall
  have hk' : (0 : ℤ) < k := by exact_mod_cast hk
  have h1 : (k : ℤ) * 3 ^ k ≤ 6 * C (mech A k l) := by
    calc (k : ℤ) * 3 ^ k = 3 * (k * 3 ^ (k - 1)) := by rw [h3]; ring
      _ ≤ 3 * (2 * C (mech A k l)) := by linarith
      _ = 6 * C (mech A k l) := by ring
  have h2 : (k : ℤ) * (2 ^ A - 3 ^ k) < k * 3 ^ k := by
    apply mul_lt_mul_of_pos_left _ hk'
    linarith
  rw [D_mech hk A l hl]
  linarith

/-- R71 §3: for every `k ≥ 1`, the bit length `A` of `3^k` (`A = ⌈k log₂ 3⌉`) satisfies
`3^k < 2^A < 2·3^k`. -/
theorem exists_total {k : ℕ} (hk : 0 < k) : ∃ A, 3 ^ k < 2 ^ A ∧ 2 ^ A < 2 * 3 ^ k := by
  refine ⟨Nat.log 2 (3 ^ k) + 1, Nat.lt_pow_succ_log_self (by norm_num) _, ?_⟩
  have h1 : 2 ^ Nat.log 2 (3 ^ k) ≤ 3 ^ k := Nat.pow_log_le_self 2 (by positivity)
  rw [pow_succ]
  rcases Nat.lt_or_ge (2 ^ Nat.log 2 (3 ^ k)) (3 ^ k) with hlt | hge
  · omega
  · exfalso
    have heq : 2 ^ Nat.log 2 (3 ^ k) = 3 ^ k := le_antisymm h1 hge
    have hL : Nat.log 2 (3 ^ k) ≠ 0 := by
      intro h0
      rw [h0, pow_zero] at heq
      have : 1 < 3 ^ k := Nat.one_lt_pow hk.ne' (by norm_num)
      omega
    have h2 : 2 ∣ 3 ^ k := by
      rw [← heq]
      exact dvd_pow_self 2 hL
    have h3 : Odd (3 ^ k) := Odd.pow (Nat.odd_iff.mpr (by norm_num))
    exact (Nat.not_even_iff_odd.mpr h3) (even_iff_two_dvd.mpr h2)

theorem mech_ne_nil {k : ℕ} (hk : 0 < k) (A l : ℕ) : mech A k l ≠ [] :=
  List.ne_nil_of_length_pos (by rw [mech_length]; exact hk)

theorem mech_D_pos {A k l : ℕ} (hk : 0 < k) (hl : l < k) (hpos : 3 ^ k < 2 ^ A) :
    0 < D (mech A k l) := by
  rw [D_mech hk A l hl]
  have : (3 : ℤ) ^ k < 2 ^ A := by exact_mod_cast hpos
  linarith

/-- Phase `0` is the minimal rotation (`C_mech_zero_le` through `mech_rotate`). -/
theorem mech_zero_min {k : ℕ} (hk : 0 < k) (A : ℕ) :
    ∀ i, C (mech A k 0) ≤ C ((mech A k 0).rotate i) := by
  intro i
  rw [mech_rotate hk]
  exact C_mech_zero_le hk A _ (Nat.mod_lt _ hk)

/-- **R71 §3's high control**: the reduced integer `3x+q` cycle of the phase-`0` mechanical word
with `3^k < 2^A < 2·3^k` (`ofWord`, parameter `q = den`) has every state above `k q/6`. -/
theorem mech_cycle_state_bound {A k : ℕ} (hk : 0 < k) (hpos : 3 ^ k < 2 ^ A)
    (hsmall : 2 ^ A < 2 * 3 ^ k) (hw0 : mech A k 0 ≠ []) (hpw : ∀ x ∈ mech A k 0, 1 ≤ x)
    (hD : 0 < D (mech A k 0)) (hmin : ∀ i, C (mech A k 0) ≤ C ((mech A k 0).rotate i)) (i : ℕ) :
    (k : ℤ) * (OddCycle.ofWord (mech A k 0) hw0 hpw hD hmin).q <
      6 * (OddCycle.ofWord (mech A k 0) hw0 hpw hD hmin).n i := by
  set Γ := OddCycle.ofWord (mech A k 0) hw0 hpw hD hmin with hΓ
  have hg := OddCycle.gcdCD_pos (mech A k 0) hw0
  have hq : OddCycle.gcdCD (mech A k 0) * Γ.q = D (mech A k 0) := OddCycle.gcdCD_mul_ofWord_q ..
  have hn : OddCycle.gcdCD (mech A k 0) * Γ.n i = C ((mech A k 0).rotate i) :=
    OddCycle.gcdCD_mul_ofWord_n ..
  rw [mech_rotate hk] at hn
  have hb := mech_state_bound hk (Nat.mod_lt (0 + i * A) hk) hpos hsmall
  rw [D_mech hk A _ (Nat.mod_lt _ hk), ← D_mech hk A 0 hk, ← hq, ← hn] at hb
  have h' : OddCycle.gcdCD (mech A k 0) * ((k : ℤ) * Γ.q) <
      OddCycle.gcdCD (mech A k 0) * (6 * Γ.n i) := by
    calc OddCycle.gcdCD (mech A k 0) * ((k : ℤ) * Γ.q)
        = (k : ℤ) * (OddCycle.gcdCD (mech A k 0) * Γ.q) := by ring
      _ < 6 * (OddCycle.gcdCD (mech A k 0) * Γ.n i) := hb
      _ = OddCycle.gcdCD (mech A k 0) * (6 * Γ.n i) := by ring
  exact lt_of_mul_lt_mul_left h' hg.le

/-! ### R71-d: the reduced denominator exceeds `1` once `k ≥ 3`

R71 §3's "for `k > 6`, `d > 1`", with the exact threshold: by `den_mech`, `den = 2^{A/g} − 3^{k/g}`;
`den = 1` is excluded by `mech_D_ne_one` when `k/g ≥ 2`, and when `k/g = 1` it forces `A/g = 2`,
i.e. `A = 2k`, which `2^A < 2·3^k` excludes for `k ≥ 3` (`4^k ≥ 2·3^k`). So the high-control
cycles avoid the absorber `q` from `k = 3` on; `k = 1, 2` give `den = 1`. -/

theorem two_mul_three_pow_le_four_pow {k : ℕ} (hk : 3 ≤ k) : 2 * 3 ^ k ≤ 4 ^ k := by
  induction k with
  | zero => omega
  | succ n ih =>
    rcases Nat.lt_or_ge n 3 with h | h
    · have hn : n = 2 := by omega
      subst hn
      norm_num
    · have := ih h
      calc 2 * 3 ^ (n + 1) = 3 * (2 * 3 ^ n) := by ring
        _ ≤ 3 * 4 ^ n := Nat.mul_le_mul_left 3 this
        _ ≤ 4 * 4 ^ n := Nat.mul_le_mul_right _ (by norm_num)
        _ = 4 ^ (n + 1) := by ring

/-- R71 §3's remark with the exact threshold: for `k ≥ 3` and `3^k < 2^A < 2·3^k`, the reduced
denominator of the mechanical word exceeds `1`. -/
theorem den_mech_gt_one {A k l : ℕ} (hk3 : 3 ≤ k) (hl : l < k) (hpos : 3 ^ k < 2 ^ A)
    (hsmall : 2 ^ A < 2 * 3 ^ k) : 1 < den (mech A k l) := by
  have hk : 0 < k := by omega
  have hkA : k < A := by
    have h2 : 2 ^ k ≤ 3 ^ k := Nat.pow_le_pow_left (by norm_num) k
    exact (Nat.pow_lt_pow_iff_right (by norm_num)).mp (lt_of_le_of_lt h2 hpos)
  rw [den_mech hk hkA.le hl]
  obtain ⟨g, hg⟩ : ∃ g, g = Nat.gcd A k := ⟨_, rfl⟩
  rw [← hg]
  have hgpos : 0 < g := by rw [hg]; exact Nat.gcd_pos_of_pos_right _ hk
  have hgA : g ∣ A := by rw [hg]; exact Nat.gcd_dvd_left _ _
  have hgk : g ∣ k := by rw [hg]; exact Nat.gcd_dvd_right _ _
  have hA : A = g * (A / g) := (Nat.mul_div_cancel' hgA).symm
  have hk' : k = g * (k / g) := (Nat.mul_div_cancel' hgk).symm
  have hAm : k / g ≤ A / g := Nat.div_le_div_right hkA.le
  have hpos₀ : 3 ^ (k / g) < 2 ^ (A / g) := by
    have : (3 ^ (k / g)) ^ g < (2 ^ (A / g)) ^ g := by
      rw [← pow_mul, ← pow_mul, Nat.mul_comm (k / g), Nat.mul_comm (A / g), ← hk', ← hA]
      exact hpos
    exact (Nat.pow_lt_pow_iff_left hgpos.ne').mp this
  have hpos₀' : (3 : ℤ) ^ (k / g) < 2 ^ (A / g) := by exact_mod_cast hpos₀
  rcases Nat.lt_or_ge (k / g) 2 with h1 | h2
  · have hk1 : k / g = 1 := by
      have : 0 < k / g := Nat.div_pos (Nat.le_of_dvd hk hgk) hgpos
      omega
    have hgk' : k = g := by rw [hk1, Nat.mul_one] at hk'; exact hk'
    rw [hk1, pow_one] at hpos₀'
    rw [hk1, pow_one]
    by_contra hle
    rw [not_lt] at hle
    have heq : (2 : ℤ) ^ (A / g) = 4 := by linarith
    have heqN : 2 ^ (A / g) = 4 := by exact_mod_cast heq
    have hA2 : A / g = 2 :=
      Nat.pow_right_injective (le_refl 2) (heqN.trans (by norm_num : (4 : ℕ) = 2 ^ 2))
    have hA' : A = 2 * k := by rw [hA, hA2, hgk']; ring
    rw [hA', pow_mul] at hsmall
    norm_num at hsmall
    have := two_mul_three_pow_le_four_pow hk3
    omega
  · have hne := mech_D_ne_one h2 (A / g) hAm
    omega

/-! ### C006-c: the exact logarithmic identity (G4)

C006 (ORDER_RIGIDITY.md, proof of the elementary part): "Multiplying the original odd-cycle
arrows gives the exact identity `δ = Σ_i log(1 + q/(3n_i)) ≤ mq/(3L)` (G4)", with
`δ = A log 2 − m log 3`. It is the elementary half of the side lane's small-`J` calibration
(feed 08:22), `L ≤ mq/(3δ)`. Here, for every `OddCycle` (any `q`): the product identity
`2^A Π n_i = Π (3n_i + q)` (`prod_arrow`), its logarithm (`log_identity`), the bound (`G4`, via
`log(1 + x) ≤ x` and `n_i ≥ L`), and the cleared `3 L δ ≤ m q` (`L_mul_delta_le`). -/

namespace OddCycle

variable {m : ℕ} (Γ : OddCycle m)

/-- The arrows multiplied around the cycle: `2^A Π n_i = Π (3 n_i + q)`. -/
theorem prod_arrow :
    (2 : ℤ) ^ Γ.Apre m * ∏ i ∈ Finset.range m, Γ.n i =
      ∏ i ∈ Finset.range m, (3 * Γ.n i + Γ.q) := by
  have h1 : ∏ i ∈ Finset.range m, ((2 : ℤ) ^ Γ.a i * Γ.n (i + 1)) =
      ∏ i ∈ Finset.range m, (3 * Γ.n i + Γ.q) :=
    Finset.prod_congr rfl (fun i _ => Γ.arrow i)
  rw [Finset.prod_mul_distrib, Finset.prod_pow_eq_pow_sum] at h1
  have h2 : ∏ i ∈ Finset.range m, Γ.n (i + 1) = ∏ i ∈ Finset.range m, Γ.n i := by
    have h3 := Finset.prod_range_succ' Γ.n m
    have h4 := Finset.prod_range_succ Γ.n m
    have h5 : Γ.n m = Γ.n 0 := by
      have := Γ.nper 0
      rwa [Nat.zero_add] at this
    rw [h5] at h4
    exact mul_right_cancel₀ Γ.npos.ne' (h3.symm.trans h4)
  rw [h2] at h1
  unfold Apre
  exact h1

/-- (G4), the identity: `A log 2 − m log 3 = Σ_{i<m} log(1 + q/(3 n_i))`. -/
theorem log_identity :
    (Γ.Apre m : ℝ) * Real.log 2 - m * Real.log 3 =
      ∑ i ∈ Finset.range m, Real.log (1 + (Γ.q : ℝ) / (3 * Γ.n i)) := by
  have hpos : ∀ i, (0 : ℝ) < Γ.n i := fun i => by exact_mod_cast Γ.npos.trans_le (Γ.nmin i)
  have hq : (0 : ℝ) < Γ.q := by exact_mod_cast Γ.hq
  have hprod : (2 : ℝ) ^ Γ.Apre m * ∏ i ∈ Finset.range m, (Γ.n i : ℝ) =
      ∏ i ∈ Finset.range m, (3 * (Γ.n i : ℝ) + Γ.q) := by exact_mod_cast Γ.prod_arrow
  have hP : (0 : ℝ) < ∏ i ∈ Finset.range m, (Γ.n i : ℝ) := Finset.prod_pos (fun i _ => hpos i)
  have hne1 : ∀ i ∈ Finset.range m, (Γ.n i : ℝ) ≠ 0 := fun i _ => (hpos i).ne'
  have hne2 : ∀ i ∈ Finset.range m, (3 * (Γ.n i : ℝ) + Γ.q) ≠ 0 := fun i _ => by
    have := hpos i
    exact ne_of_gt (by linarith)
  have hlog := congrArg Real.log hprod
  rw [Real.log_mul (by positivity : (2 : ℝ) ^ Γ.Apre m ≠ 0) hP.ne', Real.log_pow,
    Real.log_prod hne1, Real.log_prod hne2] at hlog
  have hterm : ∀ i ∈ Finset.range m, Real.log (1 + (Γ.q : ℝ) / (3 * Γ.n i)) =
      Real.log (3 * (Γ.n i : ℝ) + Γ.q) - Real.log (Γ.n i) - Real.log 3 := by
    intro i _
    have hn := hpos i
    have hn' : (3 * (Γ.n i : ℝ)) ≠ 0 := mul_ne_zero (by norm_num) hn.ne'
    have hx : (0 : ℝ) < 3 * Γ.n i + Γ.q := by linarith
    rw [one_add_div hn', Real.log_div (ne_of_gt hx) hn',
      Real.log_mul (by norm_num : (3 : ℝ) ≠ 0) hn.ne']
    ring
  rw [Finset.sum_congr rfl hterm, Finset.sum_sub_distrib, Finset.sum_sub_distrib,
    Finset.sum_const, Finset.card_range, nsmul_eq_mul]
  linarith

/-- **(G4)**: `A log 2 − m log 3 ≤ m q/(3 L)` with `L = n_0`, from `log(1 + x) ≤ x` and
`n_i ≥ L`. -/
theorem G4 : (Γ.Apre m : ℝ) * Real.log 2 - m * Real.log 3 ≤
    (m : ℝ) * (Γ.q : ℝ) / (3 * (Γ.n 0 : ℝ)) := by
  rw [Γ.log_identity]
  have hpos : ∀ i, (0 : ℝ) < Γ.n i := fun i => by exact_mod_cast Γ.npos.trans_le (Γ.nmin i)
  have hq : (0 : ℝ) < Γ.q := by exact_mod_cast Γ.hq
  have hn0 : (0 : ℝ) < Γ.n 0 := hpos 0
  have h30 : (0 : ℝ) < 3 * Γ.n 0 := by linarith
  have hterm : ∀ i ∈ Finset.range m,
      Real.log (1 + (Γ.q : ℝ) / (3 * Γ.n i)) ≤ (Γ.q : ℝ) / (3 * Γ.n 0) := by
    intro i _
    have hn := hpos i
    have h3n : (0 : ℝ) < 3 * Γ.n i := by linarith
    have hle : (Γ.n 0 : ℝ) ≤ Γ.n i := by exact_mod_cast Γ.nmin i
    have hx : (0 : ℝ) < 1 + Γ.q / (3 * Γ.n i) := by
      have := div_pos hq h3n
      linarith
    calc Real.log (1 + (Γ.q : ℝ) / (3 * Γ.n i)) ≤ (1 + (Γ.q : ℝ) / (3 * Γ.n i)) - 1 :=
          Real.log_le_sub_one_of_pos hx
      _ = Γ.q / (3 * Γ.n i) := by ring
      _ ≤ Γ.q / (3 * Γ.n 0) := div_le_div_of_nonneg_left hq.le h30 (by linarith)
  calc ∑ i ∈ Finset.range m, Real.log (1 + (Γ.q : ℝ) / (3 * Γ.n i))
      ≤ ∑ _i ∈ Finset.range m, (Γ.q : ℝ) / (3 * Γ.n 0) := Finset.sum_le_sum hterm
    _ = (m : ℝ) * (Γ.q : ℝ) / (3 * (Γ.n 0 : ℝ)) := by
      rw [Finset.sum_const, Finset.card_range, nsmul_eq_mul]
      ring

/-- The cleared form `3 L δ ≤ m q` (the side lane's `L ≤ mq/(3δ)` when `δ > 0`). -/
theorem L_mul_delta_le :
    3 * (Γ.n 0 : ℝ) * ((Γ.Apre m : ℝ) * Real.log 2 - m * Real.log 3) ≤ (m : ℝ) * Γ.q := by
  have h := Γ.G4
  have hn0 : (0 : ℝ) < Γ.n 0 := by exact_mod_cast Γ.npos
  have h30 : (0 : ℝ) < 3 * Γ.n 0 := by linarith
  calc 3 * (Γ.n 0 : ℝ) * ((Γ.Apre m : ℝ) * Real.log 2 - m * Real.log 3)
      ≤ 3 * (Γ.n 0 : ℝ) * ((m : ℝ) * (Γ.q : ℝ) / (3 * (Γ.n 0 : ℝ))) :=
        mul_le_mul_of_nonneg_left h h30.le
    _ = (m : ℝ) * Γ.q := by rw [← mul_div_assoc, mul_div_cancel_left₀ _ h30.ne']

end OddCycle

/-! ### C006-e: the normalised intercept `C_c` and `C_h ≤ C_c`

C006 writes (G1)'s second inequality with `C_c`, the intercept of the normalised word
`c_i = a_i + h_{i+1} − h_i`, using `D L = q C_h ≤ q C_c`, where `C_h = Σ_j M_j/2^{h_j}` is the
chronological intercept (`Cpre m`): the prefix sums of `c` are `P_j = A_j + h_j` (`Ppre_eq`), so
`C_h ≤ C_c` termwise (`Cpre_le_Cc`) and `D L ≤ q C_c` (`D_mul_n_le`). At `q = 1`, `B ≤ 2` the
normalised word is the phase-`0` mechanical word of total `A` (`three_band`; `cword_eq_mech`), so
`C_c = C(mech A m 0)` and R71-a gives `gcd(C_c, D) = 1` (`Cc_gcd_one`) — C006's "`Y_0 = C_c/D` is
the lower mechanical minimum". The `OrdCycle` consequences (`G1_second_c`, `run_bound_c`) follow
after the `OrdCycle` section. -/

namespace OddCycle

variable {m : ℕ} (Γ : OddCycle m)

/-- Prefix sums of the normalised word `c`. -/
def Ppre (i : ℕ) : ℕ := ∑ j ∈ Finset.range i, Γ.c j

theorem Ppre_succ (i : ℕ) : Γ.Ppre (i + 1) = Γ.Ppre i + Γ.c i := by
  unfold Ppre
  rw [Finset.sum_range_succ]

/-- `P_i = A_i + h_i`: the normalised prefix sums carry the height. -/
theorem Ppre_eq (i : ℕ) : Γ.Ppre i = Γ.Apre i + Γ.h i := by
  induction i with
  | zero => simp [Ppre, Apre, Γ.h_zero]
  | succ i ih =>
    rw [Γ.Ppre_succ, Γ.Apre_succ, ih]
    have := Γ.h_le_a_add i
    unfold c
    omega

/-- The intercept of the normalised word's prefixes, `C_c = Σ 3^{m−1−j} 2^{P_j}`, as a Horner
recurrence. -/
def Cc : ℕ → ℤ
  | 0 => 0
  | i + 1 => 3 * Cc i + 2 ^ Γ.Ppre i

theorem Cc_succ (i : ℕ) : Γ.Cc (i + 1) = 3 * Γ.Cc i + 2 ^ Γ.Ppre i := rfl

/-- The normalised word `(c_0, …, c_{i−1})` has total `P_i` and intercept `C_c(i)`. -/
theorem cword_prefix (i : ℕ) :
    ((List.range i).map Γ.c).sum = Γ.Ppre i ∧ C ((List.range i).map Γ.c) = Γ.Cc i := by
  induction i with
  | zero => simp [Ppre, Cc, C]
  | succ i ih =>
    obtain ⟨h1, h2⟩ := ih
    rw [List.range_succ, List.map_append, List.map_singleton, List.sum_append,
      List.sum_singleton, C_append_singleton, h1, h2, Γ.Ppre_succ, Γ.Cc_succ]
    exact ⟨rfl, rfl⟩

/-- `C_h ≤ C_c`: termwise `2^{A_j} ≤ 2^{A_j + h_j}`. -/
theorem Cpre_le_Cc (i : ℕ) : Γ.Cpre i ≤ Γ.Cc i := by
  induction i with
  | zero => simp [Cpre, Cc]
  | succ i ih =>
    rw [Γ.Cpre_succ, Γ.Cc_succ, Γ.Ppre_eq]
    have h2 : (2 : ℤ) ^ Γ.Apre i ≤ 2 ^ (Γ.Apre i + Γ.h i) :=
      pow_le_pow_right₀ (by norm_num) (Nat.le_add_right _ _)
    linarith

/-- C006's comparison `L ≤ q C_c/D`, cleared: `D L ≤ q C_c`, from the cycle identity `D L = q C_h`. -/
theorem D_mul_n_le : ((2 : ℤ) ^ Γ.Apre m - 3 ^ m) * Γ.n 0 ≤ Γ.q * Γ.Cc m := by
  rw [Γ.cycle_identity]
  exact mul_le_mul_of_nonneg_left (Γ.Cpre_le_Cc m) Γ.hq.le

/-- At `q = 1`, `B ≤ 2` (`m ≥ 2`, primitive), the normalised word is the phase-`0` mechanical word
of total `A = Σ a_i` (`three_band`). -/
theorem cword_eq_mech (hq1 : Γ.q = 1) (hB2 : Γ.B ≤ 2) (hm2 : 2 ≤ m)
    (hprim : ∀ i j, i < m → j < m → Γ.n i = Γ.n j → i = j) :
    (List.range m).map Γ.c = mech (Γ.Apre m) m 0 := by
  obtain ⟨q', h', -, hc, hsum, -⟩ := Γ.three_band hq1 hB2 hm2 hprim
  have hm : 0 < m := by omega
  have hA : Γ.Apre m = m * q' + h' := by unfold Apre; exact hsum
  unfold mech diffWord
  apply List.map_congr_left
  intro j _
  show Γ.c j = ((j + 1) * Γ.Apre m) / m - (j * Γ.Apre m) / m
  rw [hc j, hA,
    show (j + 1) * (m * q' + h') = m * ((j + 1) * q') + (j + 1) * h' by ring,
    show j * (m * q' + h') = m * (j * q') + j * h' by ring, Nat.mul_add_div hm, Nat.mul_add_div hm,
    show (j + 1) * q' = j * q' + q' by ring]
  have hmono : j * h' / m ≤ (j + 1) * h' / m :=
    Nat.div_le_div_right (Nat.mul_le_mul_right h' (Nat.le_succ j))
  rw [Nat.add_assoc (j * q'), Nat.add_sub_add_left, Nat.add_sub_assoc hmono]

/-- R71-a on the normalised word: at `q = 1`, `B ≤ 2`, with positive letters, `gcd(C_c, D) = 1`. -/
theorem Cc_gcd_one (hq1 : Γ.q = 1) (hB2 : Γ.B ≤ 2) (hm2 : 2 ≤ m)
    (hprim : ∀ i j, i < m → j < m → Γ.n i = Γ.n j → i = j) (hapos : ∀ i, 1 ≤ Γ.a i) :
    Int.gcd (Γ.Cc m) ((2 : ℤ) ^ Γ.Apre m - 3 ^ m) = 1 := by
  obtain ⟨_, _, -, -, -, hcop⟩ := Γ.three_band hq1 hB2 hm2 hprim
  have hm : 0 < m := by omega
  have hAm : m ≤ Γ.Apre m := by
    unfold Apre
    calc m = ∑ _i ∈ Finset.range m, 1 := by simp
      _ ≤ ∑ i ∈ Finset.range m, Γ.a i := Finset.sum_le_sum (fun i _ => hapos i)
  have hcop' : Nat.Coprime (Γ.Apre m) m := by unfold Apre; exact hcop
  have hC : Γ.Cc m = C (mech (Γ.Apre m) m 0) := by
    rw [← Γ.cword_eq_mech hq1 hB2 hm2 hprim]
    exact (Γ.cword_prefix m).2.symm
  rw [hC, ← D_mech hm (Γ.Apre m) 0 hm]
  exact mech_gcd_one hm2 (Γ.Apre m) hAm hcop'

end OddCycle

/-! ### C010-b: the complete dyadic gap lattice (GAP_LATTICE.md §§1–2)

C010 §1: for `Z = (Z_0, …, Z_{m−1})` the dyadic shift `(EZ)_j = Z_{j+1}` (`j < m−1`),
`(EZ)_{m−1} = 2Z_0`, and `U = E − I`; `G = UZ` are the complete gaps with the seam
`G_{m−1} = 2Z_0 − Z_{m−1}`. `U` is unimodular with inverse `I + E + ⋯ + E^{m−1}`:
`Z_0 = Σ_j G_j`, `Z_j = Σ_i G_i + Σ_{i<j} G_i` (1). Hence a vector and its complete gaps have the
same common divisors (the gcd statement), are integral together, a scalar clears the denominators
of one iff of the other (the common-denominator statement), and `G > 0` exactly on the normalised
order cone `0 < Z_0 < Z_1 < ⋯ < Z_{m−1} < 2Z_0`. §2: for a reduced cycle whose maximal height is
attained, the scaled states have gcd `1`, hence so do their complete gaps. Here `cgap Z m` is `UZ`
on indices `< m`; the matrix `E` is not formalised and (1) is proved by telescoping. -/

section GapLattice

variable {R : Type*} [CommRing R]

/-- The complete gaps `(UZ)_j = Z_{j+1} − Z_j` for `j + 1 < m`, and the seam `2Z_0 − Z_{m−1}`. -/
def cgap (Z : ℕ → R) (m j : ℕ) : R := if j + 1 < m then Z (j + 1) - Z j else 2 * Z 0 - Z j

/-- Telescoping below the seam: `Σ_{i<j} G_i = Z_j − Z_0` for `j < m`. -/
theorem sum_cgap_prefix (Z : ℕ → R) {m j : ℕ} (hj : j < m) :
    ∑ i ∈ Finset.range j, cgap Z m i = Z j - Z 0 := by
  induction j with
  | zero => simp
  | succ j ih =>
    rw [Finset.sum_range_succ, ih (by omega)]
    unfold cgap
    rw [ite_eq_left hj]
    ring

/-- `Σ_{j<m} G_j = Z_0`: the seam closes the telescope. -/
theorem sum_cgap (Z : ℕ → R) {m : ℕ} (hm : 0 < m) :
    ∑ j ∈ Finset.range m, cgap Z m j = Z 0 := by
  obtain ⟨k, rfl⟩ : ∃ k, m = k + 1 := ⟨m - 1, by omega⟩
  rw [Finset.sum_range_succ, sum_cgap_prefix Z (Nat.lt_succ_self k)]
  unfold cgap
  rw [ite_eq_right (lt_irrefl (k + 1))]
  ring

/-- C010's (1): `Z_j = Σ_i G_i + Σ_{i<j} G_i` — `U` is unimodular with inverse
`I + E + ⋯ + E^{m−1}`. -/
theorem Z_eq_sum_cgap (Z : ℕ → R) {m j : ℕ} (hj : j < m) :
    Z j = ∑ i ∈ Finset.range m, cgap Z m i + ∑ i ∈ Finset.range j, cgap Z m i := by
  rw [sum_cgap Z (by omega), sum_cgap_prefix Z hj]
  ring

end GapLattice

/-- The gcd statement: an integer vector and its complete gaps have the same common divisors. -/
theorem dvd_cgap_iff (Z : ℕ → ℤ) {m : ℕ} (hm : 0 < m) (d : ℤ) :
    (∀ j, j < m → d ∣ cgap Z m j) ↔ (∀ i, i < m → d ∣ Z i) := by
  constructor
  · intro h i hi
    rw [Z_eq_sum_cgap Z hi]
    exact dvd_add (Finset.dvd_sum (fun j hj => h j (Finset.mem_range.mp hj)))
      (Finset.dvd_sum (fun j hj => h j (by have := Finset.mem_range.mp hj; omega)))
  · intro h j hj
    unfold cgap
    split_ifs with hj1
    · exact dvd_sub (h _ hj1) (h j hj)
    · exact dvd_sub ((h 0 hm).mul_left 2) (h j hj)

/-- Integrality transfers both ways: a rational vector has integer entries iff its complete gaps
do. -/
theorem cgap_int_iff (Z : ℕ → ℚ) {m : ℕ} (hm : 0 < m) :
    (∀ i, i < m → ∃ z : ℤ, Z i = z) ↔ (∀ j, j < m → ∃ z : ℤ, cgap Z m j = z) := by
  constructor
  · intro h j hj
    unfold cgap
    split_ifs with hj1
    · obtain ⟨a, ha⟩ := h _ hj1
      obtain ⟨b, hb⟩ := h j hj
      exact ⟨a - b, by rw [ha, hb]; norm_cast⟩
    · obtain ⟨a, ha⟩ := h 0 hm
      obtain ⟨b, hb⟩ := h j hj
      exact ⟨2 * a - b, by rw [ha, hb]; norm_cast⟩
  · intro h i hi
    rw [Z_eq_sum_cgap Z hi]
    have hs : ∀ n, n ≤ m → ∃ z : ℤ, ∑ j ∈ Finset.range n, cgap Z m j = z := by
      intro n hn
      induction n with
      | zero => exact ⟨0, by simp⟩
      | succ n ih =>
        obtain ⟨a, ha⟩ := ih (by omega)
        obtain ⟨b, hb⟩ := h n (by omega)
        exact ⟨a + b, by rw [Finset.sum_range_succ, ha, hb]; norm_cast⟩
    obtain ⟨a, ha⟩ := hs m le_rfl
    obtain ⟨b, hb⟩ := hs i hi.le
    exact ⟨a + b, by rw [ha, hb]; norm_cast⟩

theorem cgap_smul (Z : ℕ → ℚ) (k : ℚ) (m j : ℕ) :
    cgap (fun i => k * Z i) m j = k * cgap Z m j := by
  unfold cgap
  split_ifs <;> ring

/-- C010 §1's last statement: a scalar clears the denominators of `Z` iff it clears those of
`UZ`, so the least positive common denominator is the same for states and complete gaps. -/
theorem clears_iff (Z : ℕ → ℚ) {m : ℕ} (hm : 0 < m) (k : ℚ) :
    (∀ i, i < m → ∃ z : ℤ, k * Z i = z) ↔ (∀ j, j < m → ∃ z : ℤ, k * cgap Z m j = z) := by
  have h := cgap_int_iff (fun i => k * Z i) hm
  simp only [cgap_smul] at h
  exact h

/-- The gap cone is the normalised order cone: all complete gaps positive iff
`0 < Z_0 < Z_1 < ⋯ < Z_{m−1} < 2Z_0`. -/
theorem cgap_pos_iff (Z : ℕ → ℤ) {m : ℕ} (hm : 0 < m) :
    (∀ j, j < m → 0 < cgap Z m j) ↔
      (0 < Z 0 ∧ (∀ j, j + 1 < m → Z j < Z (j + 1)) ∧ Z (m - 1) < 2 * Z 0) := by
  constructor
  · intro h
    refine ⟨?_, fun j hj => ?_, ?_⟩
    · rw [← sum_cgap Z hm]
      exact Finset.sum_pos (fun j hj => h j (Finset.mem_range.mp hj)) ⟨0, Finset.mem_range.mpr hm⟩
    · have := h j (by omega)
      unfold cgap at this
      rw [ite_eq_left hj] at this
      linarith
    · have := h (m - 1) (by omega)
      unfold cgap at this
      rw [ite_eq_right (by omega : ¬ (m - 1 + 1 < m))] at this
      linarith
  · rintro ⟨h0, hinc, hseam⟩ j hj
    unfold cgap
    split_ifs with hj1
    · linarith [hinc j hj1]
    · have hjm : j = m - 1 := by omega
      rw [hjm]
      linarith

/-! ### C010-c: §2 without the ordering hypothesis — gcd `1` of the scaled states of any reduced
cycle, of the complete gaps of any arrangement of one period, and the exact common denominator
`q` of the states normalised to parameter `1` -/

namespace OddCycle

variable {m : ℕ} (Γ : OddCycle m)

/-- C010 §2 for an arbitrary reduced cycle (no ordering hypothesis) whose maximal height is
attained: the scaled states `Z_i` have no common divisor but units — a common divisor is odd
(some `Z_i` is odd), divides every numerator, hence `q` by an arrow, against reduction. -/
theorem Z_dvd_isUnit (hred : IsCoprime Γ.q (Γ.n 0)) (hB : ∃ i, Γ.h i = Γ.B) {d : ℤ}
    (hd : ∀ i, d ∣ Γ.Z i) : IsUnit d := by
  obtain ⟨i₀, hi₀⟩ := hB
  have hodd : Odd (Γ.Z i₀) := by
    unfold OddCycle.Z
    rw [hi₀, Nat.sub_self, pow_zero, one_mul]
    exact Γ.nodd i₀
  have hdodd : Odd d := by
    by_contra h
    rw [Int.not_odd_iff_even] at h
    exact (Int.not_even_iff_odd.mpr hodd) (h.trans_dvd (hd i₀))
  have hd2 : IsCoprime d 2 := by
    obtain ⟨k, hk⟩ := hdodd
    exact ⟨1, -k, by rw [hk]; ring⟩
  have hn : ∀ i, d ∣ Γ.n i := fun i => hd2.pow_right.dvd_of_dvd_mul_left (hd i)
  have hq : d ∣ Γ.q := by
    have harrow := Γ.arrow 0
    have hqe : Γ.q = 2 ^ Γ.a 0 * Γ.n 1 - 3 * Γ.n 0 := by linarith
    rw [hqe]
    exact dvd_sub ((hn 1).mul_left _) ((hn 0).mul_left 3)
  exact hred.isUnit_of_dvd' hq (hn 0)

/-- The same with the divisibility assumed on one period only. -/
theorem Z_dvd_isUnit_of_lt (hred : IsCoprime Γ.q (Γ.n 0)) (hB : ∃ i, Γ.h i = Γ.B) {d : ℤ}
    (hd : ∀ i, i < m → d ∣ Γ.Z i) : IsUnit d := by
  apply Γ.Z_dvd_isUnit hred hB
  intro i
  rw [← Γ.Z_mod i]
  exact hd _ (Nat.mod_lt i Γ.hm)

/-- C010 §2 for unordered cycles: the complete gaps of any arrangement `Z ∘ σ` of the scaled
states that exhausts one period — the sorted arrangement in particular — have gcd `1`. -/
theorem cgap_dvd_isUnit (hred : IsCoprime Γ.q (Γ.n 0)) (hB : ∃ i, Γ.h i = Γ.B) {σ : ℕ → ℕ}
    (hσ : ∀ i, i < m → ∃ j, j < m ∧ σ j = i) {d : ℤ}
    (hd : ∀ j, j < m → d ∣ cgap (fun i => Γ.Z (σ i)) m j) : IsUnit d := by
  have hZ : ∀ i, i < m → d ∣ Γ.Z (σ i) := (dvd_cgap_iff (fun i => Γ.Z (σ i)) Γ.hm d).mp hd
  apply Γ.Z_dvd_isUnit_of_lt hred hB
  intro i hi
  obtain ⟨j, hj, rfl⟩ := hσ i hi
  exact hZ j hj

/-- If `q` divides every `k Z_i` then `q ∣ k` (the `Z_i` have gcd `1`). -/
theorem q_dvd_of_dvd_mul (hred : IsCoprime Γ.q (Γ.n 0)) (hB : ∃ i, Γ.h i = Γ.B) {k : ℤ}
    (hk : ∀ i, Γ.q ∣ k * Γ.Z i) : Γ.q ∣ k := by
  obtain ⟨g, hg⟩ : ∃ g : ℤ, g = Int.gcd Γ.q k := ⟨_, rfl⟩
  have hgpos : 0 < Int.gcd Γ.q k := Int.gcd_pos_of_ne_zero_left k Γ.hq.ne'
  have hg0 : g ≠ 0 := by rw [hg]; exact_mod_cast hgpos.ne'
  obtain ⟨q', hq'⟩ : g ∣ Γ.q := by rw [hg]; exact Int.gcd_dvd_left Γ.q k
  obtain ⟨k', hk'⟩ : g ∣ k := by rw [hg]; exact Int.gcd_dvd_right Γ.q k
  have hcop : IsCoprime q' k' := by
    have h := Int.gcd_div_gcd_div_gcd hgpos
    rw [← hg] at h
    have e1 : Γ.q / g = q' := by rw [hq']; exact Int.mul_ediv_cancel_left q' hg0
    have e2 : k / g = k' := by rw [hk']; exact Int.mul_ediv_cancel_left k' hg0
    rw [e1, e2] at h
    exact Int.isCoprime_iff_gcd_eq_one.mpr h
  have hq'Z : ∀ i, q' ∣ Γ.Z i := by
    intro i
    have h := hk i
    rw [hq', hk', mul_assoc] at h
    exact hcop.dvd_of_dvd_mul_left ((mul_dvd_mul_iff_left hg0).mp h)
  have hu : IsUnit q' := Γ.Z_dvd_isUnit hred hB hq'Z
  rw [hq']
  exact hu.mul_right_dvd.mpr ⟨k', hk'⟩

/-- `q` itself clears the denominators of the states normalised to parameter `1`. -/
theorem q_clears (i : ℕ) : ∃ z : ℤ, (Γ.q : ℚ) * ((Γ.Z i : ℚ) / Γ.q) = z := by
  refine ⟨Γ.Z i, ?_⟩
  have hq : (Γ.q : ℚ) ≠ 0 := by exact_mod_cast Γ.hq.ne'
  rw [mul_comm, div_mul_cancel₀ _ hq]

/-- C010 §2: after normalising the parameter to `1`, an integer `k` clears the denominators of
all scaled states `Z_i/q` iff `q ∣ k`. -/
theorem clears_q_iff (hred : IsCoprime Γ.q (Γ.n 0)) (hB : ∃ i, Γ.h i = Γ.B) (k : ℤ) :
    (∀ i, i < m → ∃ z : ℤ, (k : ℚ) * ((Γ.Z i : ℚ) / Γ.q) = z) ↔ Γ.q ∣ k := by
  have hq : (Γ.q : ℚ) ≠ 0 := by exact_mod_cast Γ.hq.ne'
  constructor
  · intro hk
    apply Γ.q_dvd_of_dvd_mul hred hB
    intro i
    obtain ⟨z, hz⟩ := hk (i % m) (Nat.mod_lt i Γ.hm)
    rw [Γ.Z_mod] at hz
    have h1 : (k : ℚ) * (Γ.Z i : ℚ) = (z : ℚ) * (Γ.q : ℚ) := by
      rw [← hz, mul_assoc, div_mul_cancel₀ _ hq]
    have h2 : k * Γ.Z i = z * Γ.q := by exact_mod_cast h1
    exact Dvd.intro z (by rw [h2, mul_comm])
  · rintro ⟨t, ht⟩ i hi
    refine ⟨t * Γ.Z i, ?_⟩
    rw [ht]
    push_cast
    rw [mul_comm (Γ.q : ℚ) (t : ℚ), mul_assoc, mul_comm (Γ.q : ℚ), div_mul_cancel₀ _ hq]

/-- The least positive common denominator of the normalised states is exactly `q`. -/
theorem q_le_of_clears (hred : IsCoprime Γ.q (Γ.n 0)) (hB : ∃ i, Γ.h i = Γ.B) {k : ℤ}
    (hk0 : 0 < k) (hk : ∀ i, i < m → ∃ z : ℤ, (k : ℚ) * ((Γ.Z i : ℚ) / Γ.q) = z) : Γ.q ≤ k :=
  Int.le_of_dvd hk0 ((Γ.clears_q_iff hred hB k).mp hk)

/-- C010 §2 for unordered cycles: for any arrangement of one period, `k` clears the denominators
of the complete gaps of the normalised scaled states iff `q ∣ k` — the common reduced
denominator of `G/q` is exactly `q`. -/
theorem clears_q_cgap_iff (hred : IsCoprime Γ.q (Γ.n 0)) (hB : ∃ i, Γ.h i = Γ.B) {σ : ℕ → ℕ}
    (hσ : ∀ i, i < m → ∃ j, j < m ∧ σ j = i) (k : ℤ) :
    (∀ j, j < m → ∃ z : ℤ, (k : ℚ) * cgap (fun i => (Γ.Z (σ i) : ℚ) / Γ.q) m j = z) ↔
      Γ.q ∣ k := by
  rw [← clears_iff (fun i => (Γ.Z (σ i) : ℚ) / Γ.q) Γ.hm (k : ℚ), ← Γ.clears_q_iff hred hB k]
  constructor
  · intro h i hi
    obtain ⟨j, hj, rfl⟩ := hσ i hi
    exact h j hj
  · intro h j hj
    obtain ⟨z, hz⟩ := h (σ j % m) (Nat.mod_lt _ Γ.hm)
    rw [Γ.Z_mod] at hz
    exact ⟨z, hz⟩

end OddCycle

/-! ### C013-b: the paired-state run law and its denominator consequences

C013 `OVERLAP_THEORY.md` §§1–2 on `OddCycle` (C013-a is the earlier list-level block-identity unit). For a rotation `h` the paired differences are
`z_i = n_{i+h} − n_i`: even (`z_even`), and nonzero for a nonidentity rotation of a primitive cycle
(`z_ne_zero`). At an agreeing position `a_i = a_{i+h}` subtraction of the two arrows gives
`2^{a_i} z_{i+1} = 3 z_i` (2, `z_step`); over `t` agreeing positions with valuation sum `E`,
`2^E z_end = 3^t z_start` (`z_run`) and, by coprimality and evenness, `z_start = 2^{E+1} k`,
`z_end = 2·3^t k` with `k ≠ 0` when the differences are (3, `z_run_factor`). Both endpoints are
bounded by the diameter, so `H − L ≥ 2 max(2^E, 3^t)` for every upper bound `H` of the states
(4, `diameter_ge`); with `n_j < 2^{B+1} L` this is `(2^{B+1} − 1) L > 2 max(2^E, 3^t)`
(5, `K_mul_L_gt`); with (G4)'s `3 L δ ≤ m q` and `δ > 0` it is the real inequality
`6 δ max(2^E, 3^t) < m q (2^{B+1} − 1)` (6, `q_bound_delta`), and `η = D/2^A ≤ δ` gives the
rational `6 D max(2^E, 3^t) < m q 2^A (2^{B+1} − 1)` (7, `q_bound_rational`). The run is given by
its start `i`, its length `t` and the agreement hypothesis; the pigeonhole choice of a long run
(`t ≥ ⌈m/s⌉ − 1`) and the orbit sums (1) are not part of this unit. -/

namespace OddCycle

variable {m : ℕ} (Γ : OddCycle m)

/-- The paired difference `z_i = n_{i+h} − n_i` for the rotation `h`. -/
def z (h i : ℕ) : ℤ := Γ.n (i + h) - Γ.n i

/-- The valuation sum `E` of the run of length `t` starting at `i`. -/
def runSum (i t : ℕ) : ℕ := ∑ j ∈ Finset.range t, Γ.a (i + j)

theorem runSum_succ (i t : ℕ) : Γ.runSum i (t + 1) = Γ.runSum i t + Γ.a (i + t) := by
  unfold runSum
  rw [Finset.sum_range_succ]

theorem z_even (h i : ℕ) : Even (Γ.z h i) := by
  unfold z
  exact (Γ.nodd _).sub_odd (Γ.nodd _)

/-- Primitivity makes every paired difference of a nonidentity rotation nonzero. -/
theorem z_ne_zero (hprim : ∀ i j, i < m → j < m → Γ.n i = Γ.n j → i = j) {h : ℕ}
    (hh : h % m ≠ 0) (i : ℕ) : Γ.z h i ≠ 0 := by
  intro hz
  have heq : Γ.n (i + h) = Γ.n i := by
    unfold z at hz
    exact sub_eq_zero.mp hz
  rw [← Γ.n_mod (i + h), ← Γ.n_mod i] at heq
  have hmod := hprim _ _ (Nat.mod_lt _ Γ.hm) (Nat.mod_lt _ Γ.hm) heq
  apply hh
  have h2 := Nat.sub_mod_eq_zero_of_mod_eq hmod
  rwa [Nat.add_sub_cancel_left] at h2

/-- (2): at an agreeing position the paired differences satisfy the homogeneous arrow. -/
theorem z_step {h i : ℕ} (ha : Γ.a i = Γ.a (i + h)) :
    (2 : ℤ) ^ Γ.a i * Γ.z h (i + 1) = 3 * Γ.z h i := by
  have h1 := Γ.arrow i
  have h2 := Γ.arrow (i + h)
  rw [← ha] at h2
  unfold z
  rw [Nat.add_right_comm i 1 h]
  linear_combination h2 - h1

/-- The run law: over `t` agreeing positions starting at `i`, `2^E z_{i+t} = 3^t z_i`. -/
theorem z_run {h i : ℕ} (t : ℕ) (hagree : ∀ j, j < t → Γ.a (i + j) = Γ.a (i + j + h)) :
    (2 : ℤ) ^ Γ.runSum i t * Γ.z h (i + t) = 3 ^ t * Γ.z h i := by
  induction t with
  | zero => simp [runSum]
  | succ t ih =>
    have ih' := ih (fun j hj => hagree j (Nat.lt_succ_of_lt hj))
    have hstep := Γ.z_step (h := h) (i := i + t) (hagree t (Nat.lt_succ_self t))
    rw [runSum_succ, pow_add, pow_succ, ← Nat.add_assoc]
    linear_combination (2 : ℤ) ^ Γ.runSum i t * hstep + 3 * ih'

/-- (3): the endpoints of an agreeing run are `z_end = 2·3^t k` and `z_start = 2^{E+1} k` for one
integer `k`, which is nonzero when `z_end` is. -/
theorem z_run_factor {h i : ℕ} (t : ℕ) (hagree : ∀ j, j < t → Γ.a (i + j) = Γ.a (i + j + h)) :
    ∃ k : ℤ, Γ.z h (i + t) = 2 * 3 ^ t * k ∧ Γ.z h i = 2 ^ (Γ.runSum i t + 1) * k ∧
      (Γ.z h (i + t) ≠ 0 → k ≠ 0) := by
  have hrun := Γ.z_run t hagree
  have hcop : IsCoprime ((3 : ℤ) ^ t) (2 ^ Γ.runSum i t) :=
    IsCoprime.pow ⟨1, -1, by norm_num⟩
  have hdvd3 : (3 : ℤ) ^ t ∣ Γ.z h (i + t) := by
    have h3 : (3 : ℤ) ^ t ∣ 2 ^ Γ.runSum i t * Γ.z h (i + t) := by
      rw [hrun]
      exact dvd_mul_right _ _
    exact hcop.dvd_of_dvd_mul_left h3
  obtain ⟨k', hk'⟩ := hdvd3
  have hk'even : Even k' := by
    have he := Γ.z_even h (i + t)
    rw [hk'] at he
    rcases Int.even_mul.mp he with h3 | h3
    · exact absurd h3 (Int.not_even_iff_odd.mpr (Odd.pow ⟨1, by norm_num⟩))
    · exact h3
  obtain ⟨k, hk⟩ := hk'even
  refine ⟨k, ?_, ?_, ?_⟩
  · rw [hk', hk]
    ring
  · have h3pos : (0 : ℤ) < 3 ^ t := by positivity
    have h4 : (3 : ℤ) ^ t * Γ.z h i = 3 ^ t * (2 ^ (Γ.runSum i t + 1) * k) := by
      rw [← hrun, hk', hk]
      ring
    exact mul_left_cancel₀ h3pos.ne' h4
  · intro hne hk0
    apply hne
    rw [hk', hk, hk0]
    ring

/-- (4): both run endpoints are bounded by the diameter, so `H − L ≥ 2 max(2^E, 3^t)` for every
upper bound `H` of the states, when the run's differences are nonzero. -/
theorem diameter_ge {h i : ℕ} (t : ℕ) (hagree : ∀ j, j < t → Γ.a (i + j) = Γ.a (i + j + h))
    (hz : Γ.z h (i + t) ≠ 0) {H : ℤ} (hH : ∀ j, Γ.n j ≤ H) :
    2 * max ((2 : ℤ) ^ Γ.runSum i t) (3 ^ t) ≤ H - Γ.n 0 := by
  obtain ⟨k, hend, hstart, hk⟩ := Γ.z_run_factor t hagree
  have hk1 : (1 : ℤ) ≤ |k| := Int.one_le_abs (hk hz)
  have hbound : ∀ j, |Γ.z h j| ≤ H - Γ.n 0 := by
    intro j
    unfold z
    rw [abs_le]
    constructor
    · linarith [hH j, Γ.nmin (j + h)]
    · linarith [hH (j + h), Γ.nmin j]
  rw [mul_max_of_nonneg _ _ (by norm_num : (0 : ℤ) ≤ 2)]
  apply max_le
  · have hb := hbound i
    rw [hstart, abs_mul, abs_of_pos (by positivity : (0 : ℤ) < 2 ^ (Γ.runSum i t + 1))] at hb
    have h3 : (2 : ℤ) ^ (Γ.runSum i t + 1) * 1 ≤ 2 ^ (Γ.runSum i t + 1) * |k| :=
      mul_le_mul_of_nonneg_left hk1 (by positivity)
    have h4 : (2 : ℤ) ^ (Γ.runSum i t + 1) = 2 * 2 ^ Γ.runSum i t := by ring
    linarith
  · have hb := hbound (i + t)
    rw [hend, abs_mul, abs_of_pos (by positivity : (0 : ℤ) < 2 * 3 ^ t)] at hb
    have h3 : (2 : ℤ) * 3 ^ t * 1 ≤ 2 * 3 ^ t * |k| :=
      mul_le_mul_of_nonneg_left hk1 (by positivity)
    linarith

/-- (5): `(2^{B+1} − 1) L > 2 max(2^E, 3^t)`, from (4) with the height bound `n_j < 2^{B+1} L`. -/
theorem K_mul_L_gt {h i : ℕ} (t : ℕ) (hagree : ∀ j, j < t → Γ.a (i + j) = Γ.a (i + j + h))
    (hz : Γ.z h (i + t) ≠ 0) :
    2 * max ((2 : ℤ) ^ Γ.runSum i t) (3 ^ t) < (2 ^ (Γ.B + 1) - 1) * Γ.n 0 := by
  have hH : ∀ j, Γ.n j ≤ 2 ^ (Γ.B + 1) * Γ.n 0 - 1 := by
    intro j
    have h1 := Γ.hhi j
    have h2 : (2 : ℤ) ^ (Γ.h j + 1) ≤ 2 ^ (Γ.B + 1) :=
      pow_le_pow_right₀ (by norm_num) (Nat.succ_le_succ (Γ.hB j))
    have h3 := mul_le_mul_of_nonneg_right h2 Γ.npos.le
    exact Int.le_sub_one_iff.mpr (lt_of_lt_of_le h1 h3)
  have h4 := Γ.diameter_ge t hagree hz hH
  have h5 : (2 ^ (Γ.B + 1) - 1) * Γ.n 0 = (2 : ℤ) ^ (Γ.B + 1) * Γ.n 0 - Γ.n 0 := by ring
  linarith

/-- `δ = A log 2 − m log 3 > 0`, from `D > 0`. -/
theorem delta_pos : 0 < (Γ.Apre m : ℝ) * Real.log 2 - m * Real.log 3 := by
  have hD := Γ.D_pos
  have h1 : (3 : ℝ) ^ m < 2 ^ Γ.Apre m := by
    have h0 : (3 : ℤ) ^ m < 2 ^ Γ.Apre m := by linarith
    exact_mod_cast h0
  have h2 := Real.log_lt_log (by positivity) h1
  rw [Real.log_pow, Real.log_pow] at h2
  linarith

/-- (6): the real denominator inequality retaining the height,
`6 δ max(2^E, 3^t) < m q (2^{B+1} − 1)`. -/
theorem q_bound_delta {h i : ℕ} (t : ℕ) (hagree : ∀ j, j < t → Γ.a (i + j) = Γ.a (i + j + h))
    (hz : Γ.z h (i + t) ≠ 0) :
    6 * ((Γ.Apre m : ℝ) * Real.log 2 - m * Real.log 3) *
        max ((2 : ℝ) ^ Γ.runSum i t) (3 ^ t) <
      (m : ℝ) * Γ.q * (2 ^ (Γ.B + 1) - 1) := by
  have hδ := Γ.delta_pos
  have hL := Γ.L_mul_delta_le
  have h5 : 2 * max ((2 : ℝ) ^ Γ.runSum i t) (3 ^ t) < (2 ^ (Γ.B + 1) - 1) * Γ.n 0 := by
    exact_mod_cast Γ.K_mul_L_gt t hagree hz
  have hK : (0 : ℝ) < 2 ^ (Γ.B + 1) - 1 := by
    have h2 : (2 : ℝ) ≤ 2 ^ (Γ.B + 1) := by
      calc (2 : ℝ) = 2 ^ 1 := by norm_num
        _ ≤ 2 ^ (Γ.B + 1) := pow_le_pow_right₀ (by norm_num) (by omega)
    linarith
  set δ := (Γ.Apre m : ℝ) * Real.log 2 - m * Real.log 3 with hδdef
  set M := max ((2 : ℝ) ^ Γ.runSum i t) (3 ^ t) with hM
  set K := (2 : ℝ) ^ (Γ.B + 1) - 1 with hKdef
  calc 6 * δ * M = 3 * δ * (2 * M) := by ring
    _ < 3 * δ * (K * Γ.n 0) := mul_lt_mul_of_pos_left h5 (by linarith)
    _ = K * (3 * Γ.n 0 * δ) := by ring
    _ ≤ K * (m * Γ.q) := mul_le_mul_of_nonneg_left hL hK.le
    _ = m * Γ.q * K := by ring

/-- (7): the rational consequence `6 D max(2^E, 3^t) < m q 2^A (2^{B+1} − 1)`, through
`η = D/2^A ≤ δ` (`log x ≤ x − 1` at `x = 3^m/2^A`). -/
theorem q_bound_rational {h i : ℕ} (t : ℕ) (hagree : ∀ j, j < t → Γ.a (i + j) = Γ.a (i + j + h))
    (hz : Γ.z h (i + t) ≠ 0) :
    6 * ((2 : ℤ) ^ Γ.Apre m - 3 ^ m) * max ((2 : ℤ) ^ Γ.runSum i t) (3 ^ t) <
      (m : ℤ) * Γ.q * 2 ^ Γ.Apre m * (2 ^ (Γ.B + 1) - 1) := by
  have h6 := Γ.q_bound_delta t hagree hz
  have hA : (0 : ℝ) < 2 ^ Γ.Apre m := by positivity
  have hx : (0 : ℝ) < 3 ^ m / 2 ^ Γ.Apre m := by positivity
  have hlog := Real.log_le_sub_one_of_pos hx
  rw [Real.log_div (by positivity) (by positivity), Real.log_pow, Real.log_pow] at hlog
  set δ := (Γ.Apre m : ℝ) * Real.log 2 - m * Real.log 3 with hδdef
  have h1 : (1 - δ) * 2 ^ Γ.Apre m ≤ 3 ^ m :=
    (le_div_iff₀ hA).mp (by linarith)
  have hD : (2 : ℝ) ^ Γ.Apre m - 3 ^ m ≤ δ * 2 ^ Γ.Apre m := by
    linear_combination h1
  have hM : (0 : ℝ) ≤ max ((2 : ℝ) ^ Γ.runSum i t) (3 ^ t) := le_max_of_le_left (by positivity)
  have hreal : 6 * ((2 : ℝ) ^ Γ.Apre m - 3 ^ m) * max ((2 : ℝ) ^ Γ.runSum i t) (3 ^ t) <
      (m : ℝ) * Γ.q * 2 ^ Γ.Apre m * (2 ^ (Γ.B + 1) - 1) := by
    calc 6 * ((2 : ℝ) ^ Γ.Apre m - 3 ^ m) * max ((2 : ℝ) ^ Γ.runSum i t) (3 ^ t)
        ≤ 6 * (δ * 2 ^ Γ.Apre m) * max ((2 : ℝ) ^ Γ.runSum i t) (3 ^ t) :=
          mul_le_mul_of_nonneg_right (mul_le_mul_of_nonneg_left hD (by norm_num)) hM
      _ = 6 * δ * max ((2 : ℝ) ^ Γ.runSum i t) (3 ^ t) * 2 ^ Γ.Apre m := by ring
      _ < (m : ℝ) * Γ.q * (2 ^ (Γ.B + 1) - 1) * 2 ^ Γ.Apre m := mul_lt_mul_of_pos_right h6 hA
      _ = (m : ℝ) * Γ.q * 2 ^ Γ.Apre m * (2 ^ (Γ.B + 1) - 1) := by ring
  exact_mod_cast hreal

/-- (7) under the prose's hypotheses: a primitive cycle and a nonidentity rotation. -/
theorem q_bound_rational_prim (hprim : ∀ i j, i < m → j < m → Γ.n i = Γ.n j → i = j) {h : ℕ}
    (hh : h % m ≠ 0) {i : ℕ} (t : ℕ) (hagree : ∀ j, j < t → Γ.a (i + j) = Γ.a (i + j + h)) :
    6 * ((2 : ℤ) ^ Γ.Apre m - 3 ^ m) * max ((2 : ℤ) ^ Γ.runSum i t) (3 ^ t) <
      (m : ℤ) * Γ.q * 2 ^ Γ.Apre m * (2 ^ (Γ.B + 1) - 1) :=
  Γ.q_bound_rational t hagree (Γ.z_ne_zero hprim hh _)

end OddCycle

/-! ### S2-b (part 1): parity of a scaled state -/

namespace OddCycle

variable {m : ℕ} (Γ : OddCycle m)

/-- A scaled state `Z_i = 2^{B−h_i} n_i` is odd iff its height is `B`. -/
theorem Z_odd_iff (i : ℕ) : Odd (Γ.Z i) ↔ Γ.h i = Γ.B := by
  unfold OddCycle.Z
  constructor
  · intro h
    by_contra hne
    have hlt : Γ.h i < Γ.B := lt_of_le_of_ne (Γ.hB i) hne
    have hpos : Γ.B - Γ.h i ≠ 0 := Nat.sub_ne_zero_of_lt hlt
    have heven : Even ((2 : ℤ) ^ (Γ.B - Γ.h i) * Γ.n i) :=
      (even_two.pow_of_ne_zero hpos).mul_right _
    exact (Int.not_even_iff_odd.mpr h) heven
  · intro h
    rw [h, Nat.sub_self, pow_zero, one_mul]
    exact Γ.nodd i

end OddCycle

/-! ### S3-a: C005's inversion lemma as a theorem (the side lane's S3 §1)

For `Z_i < Z_j` with `h_i ≤ h_j`, `k = h_j − h_i` and `r = n_j − 2^k n_i`:
`Z_j − Z_i = 2^{B−h_j} r` and `F_j − F_i = 2^{B−h_j}(3r − q(2^k − 1))` (C005-b's `Z_sub_of_le`,
`F_sub_of_le`; the tie `F_i = F_j` is excluded by primitivity, `Z_eq_of_F_eq`),
so the images invert (`F_j < F_i`) iff `h_i < h_j` and `3r < q(2^k − 1)` (`inversion_iff`; when
`h_j ≤ h_i` both terms of `F_j − F_i` are positive). At `q = 1` an inversion needs `k ≥ 3`
(`inversion_gap_ge_three`: `3 ≤ 3r < 2^k − 1`), and `k = 3` forces `r = 1`, the pair `(n, 8n+1)`
(`inversion_gap_three`: `r` is odd and `3r < 7`). With `B = 3` that pair is sorted-adjacent: no state
lies strictly between `Z_i = 8n` and `Z_j = 8n + 1` (`pair_adjacent`). -/

namespace OddCycle

variable {m : ℕ} (Γ : OddCycle m)

/-- `r = n_j − 2^k n_i` is positive when `Z_i < Z_j` and `h_i ≤ h_j`. -/
theorem r_pos {i j : ℕ} (hij : Γ.h i ≤ Γ.h j) (hZ : Γ.Z i < Γ.Z j) :
    0 < Γ.n j - 2 ^ (Γ.h j - Γ.h i) * Γ.n i := by
  have h := Γ.Z_sub_of_le hij
  have hP : (0 : ℤ) < 2 ^ (Γ.B - Γ.h j) := by positivity
  have h2 : 0 < Γ.Z j - Γ.Z i := by linarith
  rw [h] at h2
  exact (mul_pos_iff_of_pos_left hP).mp h2

/-- C005's inversion lemma (S3 §1): for `Z_i < Z_j`, the images invert iff `h_i < h_j` and
`3r < q(2^k − 1)`. -/
theorem inversion_iff {i j : ℕ} (hZ : Γ.Z i < Γ.Z j) :
    Γ.F j < Γ.F i ↔ Γ.h i < Γ.h j ∧
      3 * (Γ.n j - 2 ^ (Γ.h j - Γ.h i) * Γ.n i) < Γ.q * (2 ^ (Γ.h j - Γ.h i) - 1) := by
  rcases Nat.lt_or_ge (Γ.h i) (Γ.h j) with hlt | hge
  · have hF := Γ.F_sub_of_le hlt.le
    have hP : (0 : ℤ) < 2 ^ (Γ.B - Γ.h j) := by positivity
    constructor
    · intro h
      refine ⟨hlt, ?_⟩
      have h2 : 2 ^ (Γ.B - Γ.h j) * (3 * (Γ.n j - 2 ^ (Γ.h j - Γ.h i) * Γ.n i) -
          Γ.q * (2 ^ (Γ.h j - Γ.h i) - 1)) < 0 := by
        rw [← hF]
        linarith
      by_contra hge'
      have h3 : 0 ≤ 3 * (Γ.n j - 2 ^ (Γ.h j - Γ.h i) * Γ.n i) -
          Γ.q * (2 ^ (Γ.h j - Γ.h i) - 1) := by linarith [not_lt.mp hge']
      exact absurd h2 (not_lt.mpr (mul_nonneg hP.le h3))
    · rintro ⟨_, h⟩
      have hX : 3 * (Γ.n j - 2 ^ (Γ.h j - Γ.h i) * Γ.n i) -
          Γ.q * (2 ^ (Γ.h j - Γ.h i) - 1) < 0 := by linarith
      have h2 := mul_neg_of_pos_of_neg hP hX
      rw [← hF] at h2
      linarith
  · constructor
    · intro h
      exfalso
      have h1 : (2 : ℤ) ^ (Γ.B - Γ.h i) ≤ 2 ^ (Γ.B - Γ.h j) :=
        pow_le_pow_right₀ (by norm_num) (Nat.sub_le_sub_left hge _)
      have hq := Γ.hq
      unfold OddCycle.F at h
      linarith [mul_le_mul_of_nonneg_right h1 hq.le]
    · rintro ⟨h, _⟩
      exact absurd h (not_lt.mpr hge)

/-- At `q = 1`, an inversion needs height gap at least `3`. -/
theorem inversion_gap_ge_three (hq1 : Γ.q = 1) {i j : ℕ} (hZ : Γ.Z i < Γ.Z j)
    (hinv : Γ.F j < Γ.F i) : 3 ≤ Γ.h j - Γ.h i := by
  obtain ⟨hlt, h⟩ := (Γ.inversion_iff hZ).mp hinv
  rw [hq1, one_mul] at h
  have hr := Γ.r_pos hlt.le hZ
  rcases Nat.lt_or_ge (Γ.h j - Γ.h i) 3 with hk | hk
  · exfalso
    have h4 : (2 : ℤ) ^ (Γ.h j - Γ.h i) ≤ 2 ^ 2 := pow_le_pow_right₀ (by norm_num) (by omega)
    linarith
  · exact hk

/-- At `q = 1` and height gap exactly `3`, an inversion forces the pair `(n, 8n+1)`. -/
theorem inversion_gap_three (hq1 : Γ.q = 1) {i j : ℕ} (hZ : Γ.Z i < Γ.Z j) (hinv : Γ.F j < Γ.F i)
    (hk : Γ.h j - Γ.h i = 3) : Γ.n j = 8 * Γ.n i + 1 := by
  obtain ⟨hlt, h⟩ := (Γ.inversion_iff hZ).mp hinv
  have hr := Γ.r_pos hlt.le hZ
  rw [hq1, one_mul, hk] at h
  rw [hk] at hr
  have hodd : Odd (Γ.n j - 2 ^ 3 * Γ.n i) :=
    Int.odd_sub.mpr ⟨fun _ => ⟨4 * Γ.n i, by ring⟩, fun _ => Γ.nodd j⟩
  obtain ⟨c, hc⟩ := hodd
  rw [show (2 : ℤ) ^ 3 = 8 by norm_num] at h hr hc
  omega

/-- With `B = 3`, the pair `(n, 8n+1)` at heights `(0, 3)` is sorted-adjacent: no state lies
strictly between `Z_i = 8n` and `Z_j = 8n + 1`. -/
theorem pair_adjacent (hB3 : Γ.B = 3) {i j : ℕ} (hi : Γ.h i = 0) (hj : Γ.h j = 3)
    (hn : Γ.n j = 8 * Γ.n i + 1) (l : ℕ) : ¬ (Γ.Z i < Γ.Z l ∧ Γ.Z l < Γ.Z j) := by
  unfold OddCycle.Z
  rw [hB3, hi, hj, hn, Nat.sub_zero, Nat.sub_self, pow_zero, one_mul,
    show (2 : ℤ) ^ 3 = 8 by norm_num]
  generalize (2 : ℤ) ^ (3 - Γ.h l) * Γ.n l = w
  intro ⟨h1, h2⟩
  omega

end OddCycle

/-! ### S5-a: the mismatch–height trade-off (the side lane's S5 §2) as a two-library composition

For a primitive cycle at `q = 1`, a nonidentity rotation `h` with mismatch set
`mis h = {i < m : a_i ≠ a_{i+h}}` of size `s`, and the explicit gap `2^A ≤ 2^c m^μ D` (the shape of
mmusson/collatz's `gap_all`, EXT-1): some `t` has `m ≤ s(t+1)` and `6 · 3^t < 2^{B+1+c} m^{μ+1}`
(`mismatch_height`). Ingredients: the valuation word is `m`-periodic (`a_per`, `a_mod`); a full
period of agreement forces `z = 0` by the run law, so a nonidentity rotation of a primitive cycle
has a mismatch (`z_eq_zero_of_agree_period`, `exists_mis`); the pigeonhole `m ≤ (T+1)·s` when every
agreeing run has length `≤ T` (`pigeonhole`: the fibres of "next mismatch" inject into `{0,…,T}`);
and (I1)+(I3), C013-b's `q_bound_rational` with the gap, at any run with `z ≠ 0`
(`run_bound_of_gap`: `6 · 3^t < 2^{B+1+c} m^{μ+1}`). Taking `t` the longest run gives the theorem.
The real-logarithm form `(m − s) log₂ 3 < s (B + 1 + c + (μ+1) log₂ m − log₂ 6) + O(s)` follows
and is not restated. -/

namespace OddCycle

variable {m : ℕ} (Γ : OddCycle m)

/-- The valuation word is `m`-periodic: the arrows at `i` and `i + m` have the same source and
target. -/
theorem a_per (i : ℕ) : Γ.a (i + m) = Γ.a i := by
  have h1 := Γ.arrow (i + m)
  have h2 := Γ.arrow i
  rw [Γ.nper i, Nat.add_right_comm i m 1, Γ.nper (i + 1)] at h1
  have hn : 0 < Γ.n (i + 1) := Γ.npos.trans_le (Γ.nmin _)
  have h3 : (2 : ℤ) ^ Γ.a (i + m) * Γ.n (i + 1) = 2 ^ Γ.a i * Γ.n (i + 1) := by
    rw [h1, h2]
  have h4 : (2 : ℤ) ^ Γ.a (i + m) = 2 ^ Γ.a i := mul_right_cancel₀ hn.ne' h3
  exact Nat.pow_right_injective (le_refl 2) (by exact_mod_cast h4)

theorem a_add_mul (k t : ℕ) : Γ.a (k + m * t) = Γ.a k := by
  induction t with
  | zero => simp
  | succ t ih => rw [Nat.mul_succ, ← Nat.add_assoc, Γ.a_per, ih]

theorem a_mod (k : ℕ) : Γ.a (k % m) = Γ.a k := by
  conv_rhs => rw [← Nat.mod_add_div k m]
  rw [Γ.a_add_mul]

/-- The agreement predicate of the rotation `h` at position `i`: `a_i = a_{i+h}`. -/
abbrev agree (h i : ℕ) : Prop := Γ.a i = Γ.a (i + h)

theorem agree_mod (h i : ℕ) : Γ.agree h (i % m) ↔ Γ.agree h i := by
  unfold agree
  rw [Γ.a_mod i, ← Γ.a_mod (i % m + h), Nat.mod_add_mod, Γ.a_mod]

theorem agree_add_mul (h k t : ℕ) : Γ.agree h (k + m * t) ↔ Γ.agree h k := by
  unfold agree
  rw [Γ.a_add_mul, Nat.add_right_comm k (m * t) h, Γ.a_add_mul]

/-- The mismatch positions of the rotation `h` in one period; their number is `s`. -/
def mis (h : ℕ) : Finset ℕ := (Finset.range m).filter (fun i => ¬ Γ.agree h i)

/-- A full period of agreement forces `z = 0`: `2^E z = 3^m z` with `2^E ≠ 3^m`. -/
theorem z_eq_zero_of_agree_period {h i : ℕ} (hall : ∀ j, j < m → Γ.agree h (i + j)) :
    Γ.z h i = 0 := by
  have hrun := Γ.z_run (h := h) (i := i) m (fun j hj => hall j hj)
  have hper : Γ.z h (i + m) = Γ.z h i := by
    unfold z
    rw [Nat.add_right_comm i m h, Γ.nper, Γ.nper]
  rw [hper] at hrun
  have h2 : ((2 : ℤ) ^ Γ.runSum i m - 3 ^ m) * Γ.z h i = 0 := by linear_combination hrun
  rcases mul_eq_zero.mp h2 with h3 | h3
  · exfalso
    have h4 : (2 : ℤ) ^ Γ.runSum i m = 3 ^ m := by linarith
    have hodd : Odd ((3 : ℤ) ^ m) := Odd.pow ⟨1, by norm_num⟩
    rcases Nat.eq_zero_or_pos (Γ.runSum i m) with hE | hE
    · rw [hE, pow_zero] at h4
      have hm0 : m = 0 := by
        by_contra hm0
        have h5 : (3 : ℤ) ^ 1 ≤ 3 ^ m :=
          pow_le_pow_right₀ (by norm_num) (Nat.one_le_iff_ne_zero.mpr hm0)
        linarith
      exact absurd hm0 Γ.hm.ne'
    · have heven : Even ((2 : ℤ) ^ Γ.runSum i m) := even_two.pow_of_ne_zero hE.ne'
      rw [h4] at heven
      exact (Int.not_even_iff_odd.mpr hodd) heven
  · exact h3

/-- A nonidentity rotation of a primitive cycle has a mismatch. -/
theorem exists_mis (hprim : ∀ i j, i < m → j < m → Γ.n i = Γ.n j → i = j) {h : ℕ}
    (hh : h % m ≠ 0) : ∃ p, ¬ Γ.agree h p := by
  by_contra hno
  have hall : ∀ j, j < m → Γ.agree h (0 + j) := fun j _ => by
    by_contra hna
    exact hno ⟨_, hna⟩
  exact Γ.z_ne_zero hprim hh 0 (Γ.z_eq_zero_of_agree_period hall)

/-- A mismatch recurs at or after every position (periodicity). -/
theorem exists_mis_ge {h p : ℕ} (hp : ¬ Γ.agree h p) (x : ℕ) :
    ∃ y, x ≤ y ∧ ¬ Γ.agree h y := by
  refine ⟨p + m * x, ?_, ?_⟩
  · exact le_trans (Nat.le_mul_of_pos_left x Γ.hm) (Nat.le_add_left _ _)
  · rw [Γ.agree_add_mul]
    exact hp

/-- The pigeonhole (I2): if a mismatch exists and every agreeing run has length `≤ T`, then
`m ≤ (T + 1) · s`. -/
theorem pigeonhole {h : ℕ} (hne : ∃ p, ¬ Γ.agree h p) {T : ℕ}
    (hT : ∀ i t, (∀ j, j < t → Γ.agree h (i + j)) → t ≤ T) :
    m ≤ (T + 1) * (Γ.mis h).card := by
  obtain ⟨p, hp⟩ := hne
  have hex : ∀ x, ∃ y, x ≤ y ∧ ¬ Γ.agree h y := Γ.exists_mis_ge hp
  obtain ⟨nxt, hnxt⟩ : ∃ nxt : ℕ → ℕ, ∀ x, x ≤ nxt x ∧ ¬ Γ.agree h (nxt x) ∧
      ∀ y, x ≤ y → y < nxt x → Γ.agree h y :=
    ⟨fun x => Nat.find (hex x), fun x => ⟨(Nat.find_spec (hex x)).1, (Nat.find_spec (hex x)).2,
      fun y hxy hy => by
        by_contra hna
        exact absurd (Nat.find_min' (hex x) ⟨hxy, hna⟩) (not_le.mpr hy)⟩⟩
  have hd : ∀ x, nxt x - x ≤ T := by
    intro x
    have hge := (hnxt x).1
    apply hT x (nxt x - x)
    intro j hj
    exact (hnxt x).2.2 (x + j) (Nat.le_add_right x j) (by omega)
  have hg : ∀ x, nxt x % m ∈ Γ.mis h := by
    intro x
    unfold mis
    rw [Finset.mem_filter, Finset.mem_range, Γ.agree_mod]
    exact ⟨Nat.mod_lt _ Γ.hm, (hnxt x).2.1⟩
  have hfib : ∀ y ∈ (Finset.range m).image (fun x => nxt x % m),
      ((Finset.range m).filter (fun x => nxt x % m = y)).card ≤ T + 1 := by
    intro y _
    have hmaps : ∀ x ∈ (Finset.range m).filter (fun x => nxt x % m = y),
        nxt x - x ∈ Finset.range (T + 1) := by
      intro x _
      rw [Finset.mem_range]
      exact Nat.lt_succ_of_le (hd x)
    have hinj : Set.InjOn (fun x => nxt x - x)
        ((Finset.range m).filter (fun x => nxt x % m = y)) := by
      intro x hx x' hx' hxx'
      have hx2 := Finset.mem_filter.mp (Finset.mem_coe.mp hx)
      have hx2' := Finset.mem_filter.mp (Finset.mem_coe.mp hx')
      have hxm : x < m := Finset.mem_range.mp hx2.1
      have hxm' : x' < m := Finset.mem_range.mp hx2'.1
      have e1 : nxt x = x + (nxt x - x) := (Nat.add_sub_cancel' (hnxt x).1).symm
      have e2 : nxt x' = x' + (nxt x' - x') := (Nat.add_sub_cancel' (hnxt x').1).symm
      have hmod : nxt x % m = nxt x' % m := hx2.2.trans hx2'.2.symm
      rw [e1, e2] at hmod
      simp only at hxx'
      rw [← hxx'] at hmod
      have h3 : x % m = x' % m := Nat.ModEq.add_right_cancel' _ hmod
      rwa [Nat.mod_eq_of_lt hxm, Nat.mod_eq_of_lt hxm'] at h3
    calc ((Finset.range m).filter (fun x => nxt x % m = y)).card
        ≤ (Finset.range (T + 1)).card := Finset.card_le_card_of_injOn _ hmaps hinj
      _ = T + 1 := Finset.card_range _
  have hmain := Finset.card_le_mul_card_image (Finset.range m) (T + 1) hfib
  rw [Finset.card_range] at hmain
  have himg : (Finset.range m).image (fun x => nxt x % m) ⊆ Γ.mis h := by
    intro y hy
    rw [Finset.mem_image] at hy
    obtain ⟨x, _, rfl⟩ := hy
    exact hg x
  calc m ≤ (T + 1) * ((Finset.range m).image (fun x => nxt x % m)).card := hmain
    _ ≤ (T + 1) * (Γ.mis h).card := Nat.mul_le_mul_left _ (Finset.card_le_card himg)

/-- (I1)+(I3) at `q = 1`: with the explicit gap `2^A ≤ 2^c m^μ D`, every agreeing run of length `t`
of a rotation with `z ≠ 0` at its end has `6 · 3^t < 2^{B+1+c} m^{μ+1}`. -/
theorem run_bound_of_gap (hq1 : Γ.q = 1) {c μ : ℕ}
    (hgap : (2 : ℤ) ^ Γ.Apre m ≤ 2 ^ c * (m : ℤ) ^ μ * (2 ^ Γ.Apre m - 3 ^ m))
    {h i : ℕ} (t : ℕ) (hagree : ∀ j, j < t → Γ.a (i + j) = Γ.a (i + j + h))
    (hz : Γ.z h (i + t) ≠ 0) :
    6 * (3 : ℤ) ^ t < 2 ^ (Γ.B + 1 + c) * (m : ℤ) ^ (μ + 1) := by
  have h7 := Γ.q_bound_rational t hagree hz
  rw [hq1, mul_one] at h7
  have hD := Γ.D_pos
  have hmax : (3 : ℤ) ^ t ≤ max ((2 : ℤ) ^ Γ.runSum i t) (3 ^ t) := le_max_right _ _
  have hK : (2 : ℤ) ^ (Γ.B + 1) - 1 ≤ 2 ^ (Γ.B + 1) := by linarith
  have hm0 : (0 : ℤ) ≤ m := by positivity
  have h1 : 6 * ((2 : ℤ) ^ Γ.Apre m - 3 ^ m) * 3 ^ t <
      (m : ℤ) * 2 ^ Γ.Apre m * 2 ^ (Γ.B + 1) := by
    calc 6 * ((2 : ℤ) ^ Γ.Apre m - 3 ^ m) * 3 ^ t
        ≤ 6 * ((2 : ℤ) ^ Γ.Apre m - 3 ^ m) * max ((2 : ℤ) ^ Γ.runSum i t) (3 ^ t) :=
          mul_le_mul_of_nonneg_left hmax (mul_nonneg (by norm_num) hD.le)
      _ < (m : ℤ) * 2 ^ Γ.Apre m * (2 ^ (Γ.B + 1) - 1) := h7
      _ ≤ (m : ℤ) * 2 ^ Γ.Apre m * 2 ^ (Γ.B + 1) :=
          mul_le_mul_of_nonneg_left hK (by positivity)
  have h2 : (m : ℤ) * 2 ^ Γ.Apre m * 2 ^ (Γ.B + 1) ≤
      (m : ℤ) * (2 ^ c * (m : ℤ) ^ μ * (2 ^ Γ.Apre m - 3 ^ m)) * 2 ^ (Γ.B + 1) :=
    mul_le_mul_of_nonneg_right (mul_le_mul_of_nonneg_left hgap hm0) (by positivity)
  have h3 : ((2 : ℤ) ^ Γ.Apre m - 3 ^ m) * (6 * 3 ^ t) <
      ((2 : ℤ) ^ Γ.Apre m - 3 ^ m) * (2 ^ (Γ.B + 1 + c) * (m : ℤ) ^ (μ + 1)) := by
    calc ((2 : ℤ) ^ Γ.Apre m - 3 ^ m) * (6 * 3 ^ t)
        = 6 * ((2 : ℤ) ^ Γ.Apre m - 3 ^ m) * 3 ^ t := by ring
      _ < (m : ℤ) * 2 ^ Γ.Apre m * 2 ^ (Γ.B + 1) := h1
      _ ≤ (m : ℤ) * (2 ^ c * (m : ℤ) ^ μ * (2 ^ Γ.Apre m - 3 ^ m)) * 2 ^ (Γ.B + 1) := h2
      _ = ((2 : ℤ) ^ Γ.Apre m - 3 ^ m) * (2 ^ (Γ.B + 1 + c) * (m : ℤ) ^ (μ + 1)) := by ring
  exact lt_of_mul_lt_mul_left h3 hD.le

/-- **S5 §2 in integer form.** For a primitive cycle at `q = 1` with the explicit gap
`2^A ≤ 2^c m^μ D` and any rotation `h` with `h % m ≠ 0`, writing `s` for the number of mismatches,
some `t` has `m ≤ s (t + 1)` and `6 · 3^t < 2^{B+1+c} m^{μ+1}`. -/
theorem mismatch_height (hprim : ∀ i j, i < m → j < m → Γ.n i = Γ.n j → i = j) (hq1 : Γ.q = 1)
    {c μ : ℕ} (hgap : (2 : ℤ) ^ Γ.Apre m ≤ 2 ^ c * (m : ℤ) ^ μ * (2 ^ Γ.Apre m - 3 ^ m))
    {h : ℕ} (hh : h % m ≠ 0) :
    ∃ t, m ≤ (Γ.mis h).card * (t + 1) ∧
      6 * (3 : ℤ) ^ t < 2 ^ (Γ.B + 1 + c) * (m : ℤ) ^ (μ + 1) := by
  classical
  have hne := Γ.exists_mis hprim hh
  have hlt : ∀ i t, (∀ j, j < t → Γ.agree h (i + j)) → t < m := by
    intro i t hrun
    by_contra hge
    have hall : ∀ j, j < m → Γ.agree h (i + j) :=
      fun j hj => hrun j (lt_of_lt_of_le hj (not_lt.mp hge))
    exact Γ.z_ne_zero hprim hh i (Γ.z_eq_zero_of_agree_period hall)
  obtain ⟨P, hP⟩ : ∃ P : ℕ → Prop, ∀ t, P t ↔ ∃ i, i < m ∧ ∀ j, j < t → Γ.agree h (i + j) :=
    ⟨_, fun _ => Iff.rfl⟩
  have hP0 : P 0 := (hP 0).mpr ⟨0, Γ.hm, fun j hj => absurd hj (Nat.not_lt_zero j)⟩
  have hPT : P (Nat.findGreatest P m) := Nat.findGreatest_spec (Nat.zero_le m) hP0
  obtain ⟨i, _, hrun⟩ := (hP _).mp hPT
  refine ⟨Nat.findGreatest P m, ?_, ?_⟩
  · have hTbound : ∀ i' t, (∀ j, j < t → Γ.agree h (i' + j)) → t ≤ Nat.findGreatest P m := by
      intro i' t hrun'
      have hrun'' : ∀ j, j < t → Γ.agree h (i' % m + j) := by
        intro j hj
        rw [← Γ.agree_mod, Nat.mod_add_mod, Γ.agree_mod]
        exact hrun' j hj
      exact Nat.le_findGreatest (hlt i' t hrun').le
        ((hP t).mpr ⟨i' % m, Nat.mod_lt _ Γ.hm, hrun''⟩)
    have hpig := Γ.pigeonhole hne hTbound
    rw [Nat.mul_comm] at hpig
    exact hpig
  · exact Γ.run_bound_of_gap hq1 hgap _ (fun j hj => hrun j hj) (Γ.z_ne_zero hprim hh _)

end OddCycle

/-! ### S6-a: the height ceiling `B ≤ (log₂3 − 1)(m − 1) + (m − 1) log₂(1 + q/(3L))`

Each arrow multiplies the state by `(3 + q/n_i)/2^{a_i} ≤ (3/2)^{[a_i = 1]} (1 + q/(3L))` when
`a_i ≥ 1` (`n_succ_le`), so from the minimum `n_0 = L` one has
`n_j ≤ L (3/2)^{u_j} (1 + q/(3L))^j` with `u_j` the number of letters `1` among `a_0, …, a_{j−1}`
(`n_le_climb`), hence `h_j log 2 ≤ u_j (log 3 − log 2) + j log(1 + q/(3L))` (`h_le_climb`), and
when the band `B` is attained, `B log 2 ≤ (m − 1)(log 3 − log 2) + (m − 1) log(1 + q/(3L))`
(`B_le_ceiling`). For `q` odd the letters are automatically positive (`a_pos_of_odd`), so at
`q = 1` the ceiling needs no letter hypothesis (`B_le_ceiling_q1`); with `L > 2^71` its last term
is below `10^{−20} m`: the ceiling `B ≤ 0.585 (m − 1)` of the side lane's S5/S6. -/

namespace OddCycle

variable {m : ℕ} (Γ : OddCycle m)

theorem eps_nonneg : (0 : ℝ) ≤ Γ.q / (3 * Γ.n 0) := by
  have hq : (0 : ℝ) ≤ Γ.q := by exact_mod_cast Γ.hq.le
  have hn : (0 : ℝ) < Γ.n 0 := by exact_mod_cast Γ.npos
  exact div_nonneg hq (by linarith)

theorem one_add_eps_pos : (0 : ℝ) < 1 + Γ.q / (3 * Γ.n 0) := by
  linarith [Γ.eps_nonneg]

/-- With `q` odd every letter is positive: `3 n_i + q` is even and `n_{i+1}` is odd. -/
theorem a_pos_of_odd (hq : Odd Γ.q) (i : ℕ) : 1 ≤ Γ.a i := by
  by_contra h0
  have ha : Γ.a i = 0 := by omega
  have harrow := Γ.arrow i
  rw [ha, pow_zero, one_mul] at harrow
  have heven : Even (3 * Γ.n i + Γ.q) := (Odd.mul ⟨1, by norm_num⟩ (Γ.nodd i)).add_odd hq
  rw [← harrow] at heven
  exact (Int.not_even_iff_odd.mpr (Γ.nodd (i + 1))) heven

/-- The number of letters `1` among `a_0, …, a_{j−1}`. -/
def ones : ℕ → ℕ
  | 0 => 0
  | j + 1 => ones j + if Γ.a j = 1 then 1 else 0

theorem ones_succ (j : ℕ) : Γ.ones (j + 1) = Γ.ones j + if Γ.a j = 1 then 1 else 0 := rfl

theorem ones_le (j : ℕ) : Γ.ones j ≤ j := by
  induction j with
  | zero => simp [ones]
  | succ j ih =>
    rw [Γ.ones_succ]
    split_ifs <;> omega

/-- One arrow multiplies the state by at most `(3/2)^{[a_i = 1]} (1 + q/(3L))`. -/
theorem n_succ_le (hapos : ∀ i, 1 ≤ Γ.a i) (i : ℕ) :
    (Γ.n (i + 1) : ℝ) ≤
      (3 / 2 : ℝ) ^ (if Γ.a i = 1 then 1 else 0) * (1 + Γ.q / (3 * Γ.n 0)) * Γ.n i := by
  have hn0 : (0 : ℝ) < Γ.n 0 := by exact_mod_cast Γ.npos
  have hni : (0 : ℝ) < Γ.n i := by exact_mod_cast Γ.npos.trans_le (Γ.nmin i)
  have hq : (0 : ℝ) < Γ.q := by exact_mod_cast Γ.hq
  have hle : (Γ.n 0 : ℝ) ≤ Γ.n i := by exact_mod_cast Γ.nmin i
  have harrow : (2 : ℝ) ^ Γ.a i * Γ.n (i + 1) = 3 * Γ.n i + Γ.q := by exact_mod_cast Γ.arrow i
  have h1 : (3 * Γ.n i + Γ.q : ℝ) ≤ 3 * Γ.n i * (1 + Γ.q / (3 * Γ.n 0)) := by
    have h2 : (Γ.q : ℝ) ≤ Γ.n i * Γ.q / Γ.n 0 := by
      rw [le_div_iff₀ hn0]
      nlinarith
    have e : 3 * (Γ.n i : ℝ) * (1 + Γ.q / (3 * Γ.n 0)) = 3 * Γ.n i + Γ.n i * Γ.q / Γ.n 0 := by
      ring
    linarith
  have hA : (0 : ℝ) < 2 ^ Γ.a i := by positivity
  have hpow : (3 : ℝ) / 2 ^ Γ.a i ≤ (3 / 2 : ℝ) ^ (if Γ.a i = 1 then 1 else 0) := by
    split_ifs with h
    · rw [h, pow_one, pow_one]
    · have h2 : 2 ≤ Γ.a i := by
        have := hapos i
        omega
      have h4 : (4 : ℝ) ≤ 2 ^ Γ.a i := by
        calc (4 : ℝ) = 2 ^ 2 := by norm_num
          _ ≤ 2 ^ Γ.a i := pow_le_pow_right₀ (by norm_num) h2
      rw [pow_zero, div_le_one hA]
      linarith
  have hn1 : (Γ.n (i + 1) : ℝ) = (3 * Γ.n i + Γ.q) / 2 ^ Γ.a i := by
    rw [eq_div_iff hA.ne', mul_comm]
    exact harrow
  have hε : (0 : ℝ) ≤ 1 + Γ.q / (3 * Γ.n 0) := Γ.one_add_eps_pos.le
  rw [hn1]
  calc (3 * Γ.n i + Γ.q : ℝ) / 2 ^ Γ.a i
      ≤ 3 * Γ.n i * (1 + Γ.q / (3 * Γ.n 0)) / 2 ^ Γ.a i := div_le_div_of_nonneg_right h1 hA.le
    _ = (3 / 2 ^ Γ.a i) * (1 + Γ.q / (3 * Γ.n 0)) * Γ.n i := by ring
    _ ≤ (3 / 2 : ℝ) ^ (if Γ.a i = 1 then 1 else 0) * (1 + Γ.q / (3 * Γ.n 0)) * Γ.n i :=
        mul_le_mul_of_nonneg_right (mul_le_mul_of_nonneg_right hpow hε) hni.le

/-- The climb bound from the minimum: `n_j ≤ L (3/2)^{u_j} (1 + q/(3L))^j`. -/
theorem n_le_climb (hapos : ∀ i, 1 ≤ Γ.a i) (j : ℕ) :
    (Γ.n j : ℝ) ≤ Γ.n 0 * (3 / 2 : ℝ) ^ Γ.ones j * (1 + Γ.q / (3 * Γ.n 0)) ^ j := by
  induction j with
  | zero => simp [ones]
  | succ j ih =>
    have hstep := Γ.n_succ_le hapos j
    have hε : (0 : ℝ) ≤ 1 + Γ.q / (3 * Γ.n 0) := Γ.one_add_eps_pos.le
    have hc : (0 : ℝ) ≤ (3 / 2 : ℝ) ^ (if Γ.a j = 1 then 1 else 0) * (1 + Γ.q / (3 * Γ.n 0)) :=
      mul_nonneg (pow_nonneg (by norm_num) _) hε
    calc (Γ.n (j + 1) : ℝ)
        ≤ (3 / 2 : ℝ) ^ (if Γ.a j = 1 then 1 else 0) * (1 + Γ.q / (3 * Γ.n 0)) * Γ.n j := hstep
      _ ≤ (3 / 2 : ℝ) ^ (if Γ.a j = 1 then 1 else 0) * (1 + Γ.q / (3 * Γ.n 0)) *
          (Γ.n 0 * (3 / 2 : ℝ) ^ Γ.ones j * (1 + Γ.q / (3 * Γ.n 0)) ^ j) :=
          mul_le_mul_of_nonneg_left ih hc
      _ = Γ.n 0 * (3 / 2 : ℝ) ^ Γ.ones (j + 1) * (1 + Γ.q / (3 * Γ.n 0)) ^ (j + 1) := by
          rw [Γ.ones_succ, pow_add, pow_succ]
          ring

/-- The height bound: `h_j log 2 ≤ u_j (log 3 − log 2) + j log(1 + q/(3L))`. -/
theorem h_le_climb (hapos : ∀ i, 1 ≤ Γ.a i) (j : ℕ) :
    (Γ.h j : ℝ) * Real.log 2 ≤ (Γ.ones j : ℝ) * (Real.log 3 - Real.log 2) +
      (j : ℝ) * Real.log (1 + Γ.q / (3 * Γ.n 0)) := by
  have hn0 : (0 : ℝ) < Γ.n 0 := by exact_mod_cast Γ.npos
  have hlo : (2 : ℝ) ^ Γ.h j * Γ.n 0 ≤ Γ.n j := by exact_mod_cast Γ.hlo j
  have hclimb := Γ.n_le_climb hapos j
  have h1 : (2 : ℝ) ^ Γ.h j ≤ (3 / 2 : ℝ) ^ Γ.ones j * (1 + Γ.q / (3 * Γ.n 0)) ^ j := by
    have h2 : (2 : ℝ) ^ Γ.h j * Γ.n 0 ≤
        (3 / 2 : ℝ) ^ Γ.ones j * (1 + Γ.q / (3 * Γ.n 0)) ^ j * Γ.n 0 := by
      calc (2 : ℝ) ^ Γ.h j * Γ.n 0 ≤ Γ.n j := hlo
        _ ≤ Γ.n 0 * (3 / 2 : ℝ) ^ Γ.ones j * (1 + Γ.q / (3 * Γ.n 0)) ^ j := hclimb
        _ = (3 / 2 : ℝ) ^ Γ.ones j * (1 + Γ.q / (3 * Γ.n 0)) ^ j * Γ.n 0 := by ring
    exact le_of_mul_le_mul_right h2 hn0
  have hε := Γ.one_add_eps_pos
  have hlog := Real.log_le_log (by positivity) h1
  rw [Real.log_pow, Real.log_mul (by positivity : ((3 / 2 : ℝ) ^ Γ.ones j) ≠ 0)
    (pow_pos hε j).ne', Real.log_pow, Real.log_pow,
    Real.log_div (by norm_num : (3 : ℝ) ≠ 0) (by norm_num : (2 : ℝ) ≠ 0)] at hlog
  linarith

/-- **The height ceiling**: when the band `B` is attained,
`B log 2 ≤ (m − 1)(log 3 − log 2) + (m − 1) log(1 + q/(3L))`. -/
theorem B_le_ceiling (hapos : ∀ i, 1 ≤ Γ.a i) (hB : ∃ i, Γ.h i = Γ.B) :
    (Γ.B : ℝ) * Real.log 2 ≤ ((m : ℝ) - 1) * (Real.log 3 - Real.log 2) +
      ((m : ℝ) - 1) * Real.log (1 + Γ.q / (3 * Γ.n 0)) := by
  obtain ⟨i, hi⟩ := hB
  have hm := Γ.hm
  have hj : i % m ≤ m - 1 := by
    have := Nat.mod_lt i hm
    omega
  have hji : Γ.h (i % m) = Γ.B := by rw [Γ.h_mod, hi]
  have hcl := Γ.h_le_climb hapos (i % m)
  rw [hji] at hcl
  have hjm : ((i % m : ℕ) : ℝ) ≤ (m : ℝ) - 1 := by
    have h3 : ((i % m : ℕ) : ℝ) ≤ ((m - 1 : ℕ) : ℝ) := by exact_mod_cast hj
    rw [Nat.cast_sub (by omega), Nat.cast_one] at h3
    exact h3
  have hones : (Γ.ones (i % m) : ℝ) ≤ (m : ℝ) - 1 := by
    have h2 : (Γ.ones (i % m) : ℝ) ≤ ((i % m : ℕ) : ℝ) := by exact_mod_cast Γ.ones_le (i % m)
    linarith
  have hlog32 : 0 ≤ Real.log 3 - Real.log 2 := by
    have := Real.log_le_log (by norm_num : (0 : ℝ) < 2) (by norm_num : (2 : ℝ) ≤ 3)
    linarith
  have hlogε : 0 ≤ Real.log (1 + Γ.q / (3 * Γ.n 0)) := by
    apply Real.log_nonneg
    linarith [Γ.eps_nonneg]
  calc (Γ.B : ℝ) * Real.log 2
      ≤ (Γ.ones (i % m) : ℝ) * (Real.log 3 - Real.log 2) +
        ((i % m : ℕ) : ℝ) * Real.log (1 + Γ.q / (3 * Γ.n 0)) := hcl
    _ ≤ ((m : ℝ) - 1) * (Real.log 3 - Real.log 2) +
        ((m : ℝ) - 1) * Real.log (1 + Γ.q / (3 * Γ.n 0)) :=
        add_le_add (mul_le_mul_of_nonneg_right hones hlog32)
          (mul_le_mul_of_nonneg_right hjm hlogε)

/-- The ceiling at `q = 1`, with no letter hypothesis. -/
theorem B_le_ceiling_q1 (hq1 : Γ.q = 1) (hB : ∃ i, Γ.h i = Γ.B) :
    (Γ.B : ℝ) * Real.log 2 ≤ ((m : ℝ) - 1) * (Real.log 3 - Real.log 2) +
      ((m : ℝ) - 1) * Real.log (1 + 1 / (3 * Γ.n 0)) := by
  have hodd : Odd Γ.q := by
    rw [hq1]
    exact odd_one
  have h := Γ.B_le_ceiling (Γ.a_pos_of_odd hodd) hB
  rw [hq1] at h
  push_cast at h
  exact h

end OddCycle

/-! ### S6-b: the two-mismatch composition (the side lane's S6 §2, exact part)

S5-a at `s = 2` gives `t` with `m ≤ 2(t+1)` and `6 · 3^t < 2^{B+1+c} m^{μ+1}`; the ceiling S6-a bounds
`B log 2`. Together: `log 6 + t log 3 < (m−1)(log 3 − log 2) + (m−1) log(1 + 1/(3L)) + (1+c) log 2 +
(μ+1) log m` (`two_mismatch_bound`). Hence, whenever the numeric inequality fails for every such `t`
(the side lane's "false for all `m ≥ 24,891`, `L ≥ 2^20`" with `(c, μ) = (172, 341)`, taken here as
the explicit hypothesis `hnum`), no nonidentity rotation has exactly two mismatches
(`no_two_mismatch`): C011's conclusion by the S6 route. The numeric step itself is S6-c. -/

namespace OddCycle

variable {m : ℕ} (Γ : OddCycle m)

/-- S6 §2 steps 1–4, exact: at `q = 1` with the gap `(c, μ)`, an attained band and a rotation with
exactly two mismatches, some `t` has `m ≤ 2(t+1)` and
`log 6 + t log 3 < (m−1)(log 3 − log 2) + (m−1) log(1 + 1/(3L)) + (1+c) log 2 + (μ+1) log m`. -/
theorem two_mismatch_bound (hprim : ∀ i j, i < m → j < m → Γ.n i = Γ.n j → i = j) (hq1 : Γ.q = 1)
    {c μ : ℕ} (hgap : (2 : ℤ) ^ Γ.Apre m ≤ 2 ^ c * (m : ℤ) ^ μ * (2 ^ Γ.Apre m - 3 ^ m))
    (hB : ∃ i, Γ.h i = Γ.B) {h : ℕ} (hh : h % m ≠ 0) (hs : (Γ.mis h).card = 2) :
    ∃ t : ℕ, m ≤ 2 * (t + 1) ∧
      Real.log 6 + (t : ℝ) * Real.log 3 <
        ((m : ℝ) - 1) * (Real.log 3 - Real.log 2) +
          ((m : ℝ) - 1) * Real.log (1 + 1 / (3 * Γ.n 0)) +
          (1 + (c : ℝ)) * Real.log 2 + ((μ : ℝ) + 1) * Real.log m := by
  obtain ⟨t, hmt, hlt⟩ := Γ.mismatch_height hprim hq1 hgap hh
  rw [hs] at hmt
  refine ⟨t, hmt, ?_⟩
  have hceil := Γ.B_le_ceiling_q1 hq1 hB
  have hltR : (6 : ℝ) * 3 ^ t < 2 ^ (Γ.B + 1 + c) * (m : ℝ) ^ (μ + 1) := by exact_mod_cast hlt
  have hm0 : (0 : ℝ) < m := by exact_mod_cast Γ.hm
  have hlog := Real.log_lt_log (by positivity) hltR
  rw [Real.log_mul (by norm_num : (6 : ℝ) ≠ 0) (by positivity : (3 : ℝ) ^ t ≠ 0),
    Real.log_mul (by positivity : (2 : ℝ) ^ (Γ.B + 1 + c) ≠ 0) (pow_pos hm0 _).ne',
    Real.log_pow, Real.log_pow, Real.log_pow] at hlog
  push_cast at hlog
  have e : ((Γ.B : ℝ) + 1 + c) * Real.log 2 = Γ.B * Real.log 2 + (1 + (c : ℝ)) * Real.log 2 := by
    ring
  rw [e] at hlog
  linarith

/-- S6 §1 with the numeric step as an explicit hypothesis: if for every `t` with `m ≤ 2(t+1)` the
right side of `two_mismatch_bound` is at most `log 6 + t log 3`, then no nonidentity rotation has
exactly two mismatches. -/
theorem no_two_mismatch (hprim : ∀ i j, i < m → j < m → Γ.n i = Γ.n j → i = j) (hq1 : Γ.q = 1)
    {c μ : ℕ} (hgap : (2 : ℤ) ^ Γ.Apre m ≤ 2 ^ c * (m : ℤ) ^ μ * (2 ^ Γ.Apre m - 3 ^ m))
    (hB : ∃ i, Γ.h i = Γ.B)
    (hnum : ∀ t : ℕ, m ≤ 2 * (t + 1) →
      ((m : ℝ) - 1) * (Real.log 3 - Real.log 2) +
          ((m : ℝ) - 1) * Real.log (1 + 1 / (3 * Γ.n 0)) +
          (1 + (c : ℝ)) * Real.log 2 + ((μ : ℝ) + 1) * Real.log m ≤
        Real.log 6 + (t : ℝ) * Real.log 3)
    {h : ℕ} (hh : h % m ≠ 0) : (Γ.mis h).card ≠ 2 := by
  intro hs
  obtain ⟨t, hmt, hlt⟩ := Γ.two_mismatch_bound hprim hq1 hgap hB hh hs
  exact absurd hlt (not_lt.mpr (hnum t hmt))


/-! #### S6-c: the numeric step, for `m ≥ 2^15` and `L ≥ 2^20` with `gap_all`'s `(c, μ) = (172, 341)`

Only `log 2`'s decimal bounds (`Real.log_two_gt_d9`, `Real.log_two_lt_d9`), the integer comparisons
`3^41 < 2^65` and `2^19 < 3^12` (so `19/12 < log₂ 3 < 65/41`), the tangent bound
`log m ≤ 15 log 2 + m/2^15 − 1`, and `log(1 + x) ≤ x` are used; the rest is linear arithmetic. -/

theorem numeric_step {m : ℕ} (hm : 2 ^ 15 ≤ m) {L : ℝ} (hL : (2 : ℝ) ^ 20 ≤ L) (t : ℕ)
    (hmt : m ≤ 2 * (t + 1)) :
    ((m : ℝ) - 1) * (Real.log 3 - Real.log 2) + ((m : ℝ) - 1) * Real.log (1 + 1 / (3 * L)) +
        (1 + ((172 : ℕ) : ℝ)) * Real.log 2 + (((341 : ℕ) : ℝ) + 1) * Real.log m ≤
      Real.log 6 + (t : ℝ) * Real.log 3 := by
  have hmR : (2 : ℝ) ^ 15 ≤ m := by exact_mod_cast hm
  have hmtR : (m : ℝ) ≤ 2 * ((t : ℝ) + 1) := by exact_mod_cast hmt
  have ht0 : (0 : ℝ) ≤ t := by positivity
  have hm1 : (0 : ℝ) ≤ (m : ℝ) - 1 := by linarith
  have hm0 : (0 : ℝ) < m := by linarith
  have hl2a := Real.log_two_gt_d9
  have hl2b := Real.log_two_lt_d9
  have hL0 : (0 : ℝ) < L := by linarith
  have h3u : 41 * Real.log 3 < 65 * Real.log 2 := by
    have h := Real.log_lt_log (by norm_num : (0 : ℝ) < 3 ^ 41)
      (by norm_num : (3 : ℝ) ^ 41 < 2 ^ 65)
    rw [Real.log_pow, Real.log_pow] at h
    push_cast at h
    linarith
  have h3l : 19 * Real.log 2 < 12 * Real.log 3 := by
    have h := Real.log_lt_log (by norm_num : (0 : ℝ) < 2 ^ 19)
      (by norm_num : (2 : ℝ) ^ 19 < 3 ^ 12)
    rw [Real.log_pow, Real.log_pow] at h
    push_cast at h
    linarith
  have hlogm : Real.log m ≤ 15 * Real.log 2 + ((m : ℝ) / 2 ^ 15 - 1) := by
    have h := Real.log_le_sub_one_of_pos (by positivity : (0 : ℝ) < m / 2 ^ 15)
    rw [Real.log_div hm0.ne' (by positivity), Real.log_pow] at h
    push_cast at h
    linarith
  have hε : Real.log (1 + 1 / (3 * L)) ≤ 1 / (3 * 2 ^ 20) := by
    have h := Real.log_le_sub_one_of_pos (by positivity : (0 : ℝ) < 1 + 1 / (3 * L))
    have h2 : (1 : ℝ) / (3 * L) ≤ 1 / (3 * 2 ^ 20) :=
      div_le_div_of_nonneg_left (by norm_num) (by positivity) (by linarith)
    linarith
  have hlog6 : Real.log 6 = Real.log 2 + Real.log 3 := by
    rw [show (6 : ℝ) = 2 * 3 by norm_num, Real.log_mul (by norm_num) (by norm_num)]
  have hA : ((m : ℝ) - 1) * (Real.log 3 - Real.log 2) ≤
      ((m : ℝ) - 1) * ((24 / 41) * 0.6931471808) := by
    apply mul_le_mul_of_nonneg_left _ hm1
    linarith
  have hB : ((m : ℝ) - 1) * Real.log (1 + 1 / (3 * L)) ≤ ((m : ℝ) - 1) * (1 / (3 * 2 ^ 20)) :=
    mul_le_mul_of_nonneg_left hε hm1
  have hC : (t : ℝ) * ((19 / 12) * 0.6931471803) ≤ (t : ℝ) * Real.log 3 := by
    apply mul_le_mul_of_nonneg_left _ ht0
    linarith
  push_cast
  linarith [hA, hB, hC, hlogm, hlog6, hl2a, hl2b, h3l, hmR, hmtR]

/-- **C011's conclusion by the S6 route**, with explicit inputs: a primitive cycle at `q = 1` with
the gap `(172, 341)` (the shape of `gap_all`), attained band, `m ≥ 2^15` and `L ≥ 2^20` has no
nonidentity rotation with exactly two mismatches. -/
theorem no_two_mismatch_of_gap (hprim : ∀ i j, i < m → j < m → Γ.n i = Γ.n j → i = j)
    (hq1 : Γ.q = 1)
    (hgap : (2 : ℤ) ^ Γ.Apre m ≤ 2 ^ 172 * (m : ℤ) ^ 341 * (2 ^ Γ.Apre m - 3 ^ m))
    (hB : ∃ i, Γ.h i = Γ.B) (hm : 2 ^ 15 ≤ m) (hL : (2 : ℤ) ^ 20 ≤ Γ.n 0) {h : ℕ}
    (hh : h % m ≠ 0) : (Γ.mis h).card ≠ 2 :=
  Γ.no_two_mismatch hprim hq1 hgap hB
    (fun t hmt => numeric_step hm (by exact_mod_cast hL) t hmt) hh
end OddCycle

/-! ### S7-a: the sign lemma for the paired differences (the side lane's S7 step (1))

At an agreeing position `2^{a_i} z_{i+1} = 3 z_i`, so `z_{i+1}` and `z_i` have the same sign
(`z_pos_step`, `z_neg_step`), hence the sign is constant along an agreeing run (`z_pos_run`,
`z_neg_run`). In a primitive cycle the extremes are strict (`n_lt_of_ne`, `n_lt_max_of_ne`), so for
a nonidentity rotation `δ_0 = n_h − n_0 > 0`, `δ_{−h} = n_0 − n_{−h} < 0` (`z_min_pos`,
`z_pred_min_neg`), and at an index `j` attaining the maximum `δ_j < 0`, `δ_{j−h} > 0` (`z_max_neg`,
`z_pred_max_pos`); the position `−h` is `m − h % m`. Sign changes therefore happen only at
mismatches, and a nonidentity rotation has at least one `+→−` and one `−→+` change; the counting
of changes among the mismatches is not formalised here. -/

namespace OddCycle

variable {m : ℕ} (Γ : OddCycle m)

theorem z_pos_step {h i : ℕ} (ha : Γ.a i = Γ.a (i + h)) : 0 < Γ.z h (i + 1) ↔ 0 < Γ.z h i := by
  have hs := Γ.z_step ha
  have hp : (0 : ℤ) < 2 ^ Γ.a i := by positivity
  rw [← mul_pos_iff_of_pos_left hp, hs, mul_pos_iff_of_pos_left (by norm_num : (0 : ℤ) < 3)]

theorem z_neg_step {h i : ℕ} (ha : Γ.a i = Γ.a (i + h)) : Γ.z h (i + 1) < 0 ↔ Γ.z h i < 0 := by
  have hs := Γ.z_step ha
  have hp : (0 : ℤ) < 2 ^ Γ.a i := by positivity
  constructor
  · intro h1
    have h2 : (2 : ℤ) ^ Γ.a i * Γ.z h (i + 1) < 0 := mul_neg_of_pos_of_neg hp h1
    linarith
  · intro h1
    have h2 : (2 : ℤ) ^ Γ.a i * Γ.z h (i + 1) < 0 := by linarith
    exact neg_of_mul_neg_right h2 hp.le

theorem z_pos_run {h i : ℕ} (t : ℕ) (hagree : ∀ j, j < t → Γ.a (i + j) = Γ.a (i + j + h)) :
    0 < Γ.z h (i + t) ↔ 0 < Γ.z h i := by
  induction t with
  | zero => simp
  | succ t ih =>
    rw [← Nat.add_assoc, Γ.z_pos_step (hagree t (Nat.lt_succ_self t))]
    exact ih (fun j hj => hagree j (Nat.lt_succ_of_lt hj))

theorem z_neg_run {h i : ℕ} (t : ℕ) (hagree : ∀ j, j < t → Γ.a (i + j) = Γ.a (i + j + h)) :
    Γ.z h (i + t) < 0 ↔ Γ.z h i < 0 := by
  induction t with
  | zero => simp
  | succ t ih =>
    rw [← Nat.add_assoc, Γ.z_neg_step (hagree t (Nat.lt_succ_self t))]
    exact ih (fun j hj => hagree j (Nat.lt_succ_of_lt hj))

/-- The minimum is strict in a primitive cycle. -/
theorem n_lt_of_ne (hprim : ∀ i j, i < m → j < m → Γ.n i = Γ.n j → i = j) {i : ℕ}
    (hi : i % m ≠ 0) : Γ.n 0 < Γ.n i := by
  rcases (Γ.nmin i).lt_or_eq with hlt | heq
  · exact hlt
  · exfalso
    apply hi
    apply hprim (i % m) 0 (Nat.mod_lt _ Γ.hm) Γ.hm
    rw [Γ.n_mod]
    exact heq.symm

/-- An index attaining the maximum is a strict maximum in a primitive cycle. -/
theorem n_lt_max_of_ne (hprim : ∀ i j, i < m → j < m → Γ.n i = Γ.n j → i = j) {j : ℕ}
    (hj : ∀ i, Γ.n i ≤ Γ.n j) {i : ℕ} (hi : i % m ≠ j % m) : Γ.n i < Γ.n j := by
  rcases (hj i).lt_or_eq with hlt | heq
  · exact hlt
  · exfalso
    apply hi
    apply hprim (i % m) (j % m) (Nat.mod_lt _ Γ.hm) (Nat.mod_lt _ Γ.hm)
    rw [Γ.n_mod, Γ.n_mod]
    exact heq

/-- `δ_0 = n_h − n_0 > 0`. -/
theorem z_min_pos (hprim : ∀ i j, i < m → j < m → Γ.n i = Γ.n j → i = j) {h : ℕ}
    (hh : h % m ≠ 0) : 0 < Γ.z h 0 := by
  unfold z
  rw [Nat.zero_add]
  linarith [Γ.n_lt_of_ne hprim hh]

/-- The position `−h` is `m − h % m`, and `(m − h % m) + h ≡ 0`. -/
theorem pred_add_mod (hm : 0 < m) (h : ℕ) : (m - h % m + h) % m = 0 := by
  have h1 := Nat.div_add_mod h m
  have h2 := Nat.mod_lt h hm
  have e : m - h % m + h = m * (h / m + 1) := by
    rw [Nat.mul_succ]
    omega
  rw [e, Nat.mul_mod_right]

/-- `δ_{−h} = n_0 − n_{−h} < 0`. -/
theorem z_pred_min_neg (hprim : ∀ i j, i < m → j < m → Γ.n i = Γ.n j → i = j) {h : ℕ}
    (hh : h % m ≠ 0) : Γ.z h (m - h % m) < 0 := by
  unfold z
  have h1 : Γ.n (m - h % m + h) = Γ.n 0 := by
    rw [← Γ.n_mod, pred_add_mod Γ.hm]
  have h2 : (m - h % m) % m ≠ 0 := by
    have := Nat.mod_lt h Γ.hm
    have hpos : 0 < h % m := Nat.pos_of_ne_zero hh
    rw [Nat.mod_eq_of_lt (by omega)]
    omega
  rw [h1]
  linarith [Γ.n_lt_of_ne hprim h2]

/-- `δ_j = n_{j+h} − n_j < 0` at an index `j` attaining the maximum. -/
theorem z_max_neg (hprim : ∀ i j, i < m → j < m → Γ.n i = Γ.n j → i = j) {j : ℕ}
    (hj : ∀ i, Γ.n i ≤ Γ.n j) {h : ℕ} (hh : h % m ≠ 0) : Γ.z h j < 0 := by
  unfold z
  have hne : (j + h) % m ≠ j % m := by
    intro heq
    apply hh
    have := Nat.sub_mod_eq_zero_of_mod_eq heq
    rwa [Nat.add_sub_cancel_left] at this
  linarith [Γ.n_lt_max_of_ne hprim hj hne]

/-- `δ_{j−h} = n_j − n_{j−h} > 0` at an index `j` attaining the maximum; the position `j − h` is
`j + (m − h % m)`. -/
theorem z_pred_max_pos (hprim : ∀ i j, i < m → j < m → Γ.n i = Γ.n j → i = j) {j : ℕ}
    (hj : ∀ i, Γ.n i ≤ Γ.n j) {h : ℕ} (hh : h % m ≠ 0) : 0 < Γ.z h (j + (m - h % m)) := by
  unfold z
  have h1 : Γ.n (j + (m - h % m) + h) = Γ.n j := by
    rw [← Γ.n_mod, Nat.add_assoc, Nat.add_mod, pred_add_mod Γ.hm, Nat.add_zero, Nat.mod_mod, Γ.n_mod]
  have h2 : (j + (m - h % m)) % m ≠ j % m := by
    intro heq
    have h3 := Nat.mod_lt h Γ.hm
    have hpos : 0 < h % m := Nat.pos_of_ne_zero hh
    have h4 : (m - h % m) % m = 0 := by
      have := Nat.sub_mod_eq_zero_of_mod_eq (Nat.add_comm j (m - h % m) ▸ heq)
      rwa [Nat.add_sub_cancel] at this
    rw [Nat.mod_eq_of_lt (by omega)] at h4
    omega
  rw [h1]
  linarith [Γ.n_lt_max_of_ne hprim hj h2]

end OddCycle

/-! ### S7-b (part 1): three ingredients of the side lane's S7

`s ≠ 1`: the totals `Σ_{i<m} a_i` and `Σ_{i<m} a_{i+h}` agree (`sum_a_shift`), so exactly one mismatch
is impossible (`mis_card_ne_one`). The witness of a run (F1): at the end `e = i + t` of an agreeing
run with `z_e ≠ 0`, the larger of `n_e`, `n_{e+h}` exceeds `2·3^t` (`witness_gt`). The
excess-tracked ceiling (F3): with `X_k = Σ_{i<k}(a_i − 1)` (`excess`), `n_k 2^{X_k} ≤ L (3/2)^k
(1 + q/(3L))^k` (`n_mul_pow_excess_le`), hence `(h_k + X_k) log 2 ≤ k (log 3 − log 2) +
k log(1 + q/(3L))` (`h_add_excess_le`): the prose's `log₂(n_k/L) ≤ kκ − X_k`. -/

namespace OddCycle

variable {m : ℕ} (Γ : OddCycle m)

/-- The sum of the valuation word over one period is shift-invariant. -/
theorem sum_a_shift (k : ℕ) : ∑ i ∈ Finset.range m, Γ.a (i + k) = ∑ i ∈ Finset.range m, Γ.a i := by
  induction k with
  | zero => simp
  | succ k ih =>
    have h1 := Finset.sum_range_succ' (fun i => Γ.a (i + k)) m
    have h2 := Finset.sum_range_succ (fun i => Γ.a (i + k)) m
    simp only [Nat.zero_add] at h1 h2
    have h3 : Γ.a (m + k) = Γ.a k := by rw [Nat.add_comm, Γ.a_per]
    have h4 : ∑ i ∈ Finset.range m, Γ.a (i + (k + 1)) =
        ∑ i ∈ Finset.range m, Γ.a (i + 1 + k) := by
      apply Finset.sum_congr rfl
      intro i _
      rw [Nat.add_right_comm i 1 k, Nat.add_assoc]
    rw [h4, ← ih]
    rw [h3] at h2
    omega

/-- Exactly one mismatch is impossible: the two totals agree. -/
theorem mis_card_ne_one (h : ℕ) : (Γ.mis h).card ≠ 1 := by
  intro hcard
  obtain ⟨e, he⟩ := Finset.card_eq_one.mp hcard
  have hsum : ∑ i ∈ Finset.range m, ((Γ.a (i + h) : ℤ) - Γ.a i) = 0 := by
    rw [Finset.sum_sub_distrib]
    have := Γ.sum_a_shift h
    have hc : ((∑ i ∈ Finset.range m, Γ.a (i + h) : ℕ) : ℤ) = ((∑ i ∈ Finset.range m, Γ.a i : ℕ) : ℤ) := by
      rw [this]
    push_cast at hc
    linarith
  have hfilter : ∑ i ∈ Finset.range m, ((Γ.a (i + h) : ℤ) - Γ.a i) =
      ∑ i ∈ Γ.mis h, ((Γ.a (i + h) : ℤ) - Γ.a i) := by
    unfold mis
    symm
    apply Finset.sum_filter_of_ne
    intro i _ hne hagree
    apply hne
    unfold agree at hagree
    rw [hagree]
    ring
  rw [hfilter, he, Finset.sum_singleton] at hsum
  have hemis : e ∈ Γ.mis h := by
    rw [he]
    exact Finset.mem_singleton_self e
  unfold mis at hemis
  rw [Finset.mem_filter] at hemis
  apply hemis.2
  unfold agree
  have : (Γ.a (e + h) : ℤ) = Γ.a e := by linarith
  exact_mod_cast this.symm

/-- (F1), the witness: at the end `e = i + t` of an agreeing run with `z_e ≠ 0`, the larger of
`n_e` and `n_{e+h}` exceeds `2·3^t`. -/
theorem witness_gt {h i : ℕ} (t : ℕ) (hagree : ∀ j, j < t → Γ.a (i + j) = Γ.a (i + j + h))
    (hz : Γ.z h (i + t) ≠ 0) : 2 * (3 : ℤ) ^ t < max (Γ.n (i + t)) (Γ.n (i + t + h)) := by
  obtain ⟨k, hend, -, hk⟩ := Γ.z_run_factor t hagree
  have hk0 := hk hz
  have hpos1 : 0 < Γ.n (i + t) := Γ.npos.trans_le (Γ.nmin _)
  have hpos2 : 0 < Γ.n (i + t + h) := Γ.npos.trans_le (Γ.nmin _)
  have h3 : (0 : ℤ) < 3 ^ t := by positivity
  unfold z at hend
  rcases lt_or_gt_of_ne hk0 with hneg | hposk
  · -- k ≤ −1: n (i+t) = n (i+t+h) − 2·3^t k ≥ n (i+t+h) + 2·3^t
    have hk1 : k ≤ -1 := by omega
    have : 2 * (3 : ℤ) ^ t < Γ.n (i + t) := by nlinarith
    exact lt_of_lt_of_le this (le_max_left _ _)
  · have hk1 : 1 ≤ k := by omega
    have : 2 * (3 : ℤ) ^ t < Γ.n (i + t + h) := by nlinarith
    exact lt_of_lt_of_le this (le_max_right _ _)

/-- The excess `X_k = Σ_{i<k} (a_i − 1)`. -/
def excess : ℕ → ℕ
  | 0 => 0
  | k + 1 => excess k + (Γ.a k - 1)

theorem excess_succ (k : ℕ) : Γ.excess (k + 1) = Γ.excess k + (Γ.a k - 1) := rfl

/-- (F3), tracked: `n_k 2^{X_k} ≤ L (3/2)^k (1 + q/(3L))^k`. -/
theorem n_mul_pow_excess_le (hapos : ∀ i, 1 ≤ Γ.a i) (k : ℕ) :
    (Γ.n k : ℝ) * 2 ^ Γ.excess k ≤ Γ.n 0 * (3 / 2 : ℝ) ^ k * (1 + Γ.q / (3 * Γ.n 0)) ^ k := by
  induction k with
  | zero => simp [excess]
  | succ k ih =>
    have hn0 : (0 : ℝ) < Γ.n 0 := by exact_mod_cast Γ.npos
    have hnk : (0 : ℝ) < Γ.n k := by exact_mod_cast Γ.npos.trans_le (Γ.nmin k)
    have hq : (0 : ℝ) < Γ.q := by exact_mod_cast Γ.hq
    have hle : (Γ.n 0 : ℝ) ≤ Γ.n k := by exact_mod_cast Γ.nmin k
    have hε : (0 : ℝ) ≤ 1 + Γ.q / (3 * Γ.n 0) := Γ.one_add_eps_pos.le
    have harrow : (2 : ℝ) ^ Γ.a k * Γ.n (k + 1) = 3 * Γ.n k + Γ.q := by exact_mod_cast Γ.arrow k
    have hsplit : (2 : ℝ) ^ Γ.a k = 2 * 2 ^ (Γ.a k - 1) := by
      rw [← pow_succ']
      congr 1
      have := hapos k
      omega
    have h1 : (3 * Γ.n k + Γ.q : ℝ) ≤ 3 * Γ.n k * (1 + Γ.q / (3 * Γ.n 0)) := by
      have h2 : (Γ.q : ℝ) ≤ Γ.n k * Γ.q / Γ.n 0 := by
        rw [le_div_iff₀ hn0]
        nlinarith
      have e : 3 * (Γ.n k : ℝ) * (1 + Γ.q / (3 * Γ.n 0)) = 3 * Γ.n k + Γ.n k * Γ.q / Γ.n 0 := by
        ring
      linarith
    -- n (k+1) · 2^(a k − 1) = (3 n k + q)/2 ≤ (3/2) n k (1 + ε)
    have h3 : (Γ.n (k + 1) : ℝ) * 2 ^ (Γ.a k - 1) ≤ (3 / 2) * Γ.n k * (1 + Γ.q / (3 * Γ.n 0)) := by
      rw [hsplit] at harrow
      nlinarith
    have hP : (0 : ℝ) ≤ 2 ^ Γ.excess k := by positivity
    rw [Γ.excess_succ, pow_add, pow_succ, pow_succ]
    calc (Γ.n (k + 1) : ℝ) * (2 ^ Γ.excess k * 2 ^ (Γ.a k - 1))
        = (Γ.n (k + 1) * 2 ^ (Γ.a k - 1)) * 2 ^ Γ.excess k := by ring
      _ ≤ ((3 / 2) * Γ.n k * (1 + Γ.q / (3 * Γ.n 0))) * 2 ^ Γ.excess k :=
          mul_le_mul_of_nonneg_right h3 hP
      _ = (3 / 2) * (1 + Γ.q / (3 * Γ.n 0)) * (Γ.n k * 2 ^ Γ.excess k) := by ring
      _ ≤ (3 / 2) * (1 + Γ.q / (3 * Γ.n 0)) *
          (Γ.n 0 * (3 / 2 : ℝ) ^ k * (1 + Γ.q / (3 * Γ.n 0)) ^ k) :=
          mul_le_mul_of_nonneg_left ih (by positivity)
      _ = Γ.n 0 * ((3 / 2 : ℝ) ^ k * (3 / 2)) * ((1 + Γ.q / (3 * Γ.n 0)) ^ k *
          (1 + Γ.q / (3 * Γ.n 0))) := by ring

/-- (F3), tracked, in logarithms: `(h_k + X_k) log 2 ≤ k (log 3 − log 2) + k log(1 + q/(3L))`. -/
theorem h_add_excess_le (hapos : ∀ i, 1 ≤ Γ.a i) (k : ℕ) :
    ((Γ.h k : ℝ) + Γ.excess k) * Real.log 2 ≤
      (k : ℝ) * (Real.log 3 - Real.log 2) + (k : ℝ) * Real.log (1 + Γ.q / (3 * Γ.n 0)) := by
  have hn0 : (0 : ℝ) < Γ.n 0 := by exact_mod_cast Γ.npos
  have hlo : (2 : ℝ) ^ Γ.h k * Γ.n 0 ≤ Γ.n k := by exact_mod_cast Γ.hlo k
  have hcl := Γ.n_mul_pow_excess_le hapos k
  have hε := Γ.one_add_eps_pos
  have hP : (0 : ℝ) < 2 ^ Γ.excess k := by positivity
  have h1 : (2 : ℝ) ^ (Γ.h k + Γ.excess k) ≤ (3 / 2 : ℝ) ^ k * (1 + Γ.q / (3 * Γ.n 0)) ^ k := by
    have h2 : (2 : ℝ) ^ (Γ.h k + Γ.excess k) * Γ.n 0 ≤
        (3 / 2 : ℝ) ^ k * (1 + Γ.q / (3 * Γ.n 0)) ^ k * Γ.n 0 := by
      calc (2 : ℝ) ^ (Γ.h k + Γ.excess k) * Γ.n 0
          = (2 ^ Γ.h k * Γ.n 0) * 2 ^ Γ.excess k := by rw [pow_add]; ring
        _ ≤ Γ.n k * 2 ^ Γ.excess k := mul_le_mul_of_nonneg_right hlo hP.le
        _ ≤ Γ.n 0 * (3 / 2 : ℝ) ^ k * (1 + Γ.q / (3 * Γ.n 0)) ^ k := hcl
        _ = (3 / 2 : ℝ) ^ k * (1 + Γ.q / (3 * Γ.n 0)) ^ k * Γ.n 0 := by ring
    exact le_of_mul_le_mul_right h2 hn0
  have hlog := Real.log_le_log (by positivity) h1
  rw [Real.log_pow, Real.log_mul (by positivity : ((3 / 2 : ℝ) ^ k) ≠ 0) (pow_pos hε k).ne',
    Real.log_pow, Real.log_pow, Real.log_div (by norm_num : (3 : ℝ) ≠ 0) (by norm_num : (2 : ℝ) ≠ 0)]
    at hlog
  push_cast at hlog
  linarith

end OddCycle

/-! ### S7-b (part 2): counting the sign changes (the side lane's S7 Step 2, by telescoping)

With `σ_i = [z_i > 0]`, the telescoping sum `Σ_{i<m} (σ_{i+1} − σ_i) = 0` (periodicity) shows that
the `+→−` changes (`down`) and the `−→+` changes (`up`) in one period are equinumerous
(`card_down_eq_card_up`); a change happens only at a mismatch (`down_mem_mis`, `up_mem_mis`, from
`z_pos_step`); a discrete intermediate-value step (`exists_down`, `exists_up`) locates a `+→−` change
in the window `[j − h, m − h)` and a `−→+` change in `[j, m)` from the four strict signs of S7-a
(`exists_down_window`, `exists_up_window`). With exactly three mismatches there is exactly one
change of each kind, and the third mismatch has no change (`three_mismatch_changes`). -/

namespace OddCycle

variable {m : ℕ} (Γ : OddCycle m)

theorem z_per (h i : ℕ) : Γ.z h (i + m) = Γ.z h i := by
  unfold z
  rw [Nat.add_right_comm i m h, Γ.nper, Γ.nper]

/-- The sign indicator `σ_i = [z_i > 0]`, as an integer. -/
def sgn (h i : ℕ) : ℤ := if 0 < Γ.z h i then 1 else 0

theorem sgn_per (h i : ℕ) : Γ.sgn h (i + m) = Γ.sgn h i := by
  unfold sgn
  rw [Γ.z_per]

/-- A `+→−` change at `i`. -/
abbrev down (h i : ℕ) : Prop := 0 < Γ.z h i ∧ ¬ 0 < Γ.z h (i + 1)

/-- A `−→+` change at `i`. -/
abbrev up (h i : ℕ) : Prop := ¬ 0 < Γ.z h i ∧ 0 < Γ.z h (i + 1)

theorem down_per (h i : ℕ) : Γ.down h (i + m) ↔ Γ.down h i := by
  unfold down
  rw [Γ.z_per, Nat.add_right_comm i m 1, Γ.z_per]

theorem up_per (h i : ℕ) : Γ.up h (i + m) ↔ Γ.up h i := by
  unfold up
  rw [Γ.z_per, Nat.add_right_comm i m 1, Γ.z_per]

theorem sgn_succ_sub (h i : ℕ) :
    Γ.sgn h (i + 1) - Γ.sgn h i =
      (if Γ.up h i then (1 : ℤ) else 0) - (if Γ.down h i then (1 : ℤ) else 0) := by
  unfold sgn up down
  by_cases h1 : 0 < Γ.z h i <;> by_cases h2 : 0 < Γ.z h (i + 1) <;> simp [h1, h2]

theorem sum_sgn_tele (h : ℕ) : ∑ i ∈ Finset.range m, (Γ.sgn h (i + 1) - Γ.sgn h i) = 0 := by
  rw [Finset.sum_range_sub (fun i => Γ.sgn h i) m]
  have := Γ.sgn_per h 0
  rw [Nat.zero_add] at this
  rw [this, sub_self]

/-- The `+→−` and `−→+` changes in one period are equinumerous. -/
theorem card_down_eq_card_up (h : ℕ) :
    ((Finset.range m).filter (Γ.down h)).card = ((Finset.range m).filter (Γ.up h)).card := by
  have h1 := Γ.sum_sgn_tele h
  have h2 : ∑ i ∈ Finset.range m, (Γ.sgn h (i + 1) - Γ.sgn h i) =
      ∑ i ∈ Finset.range m,
        ((if Γ.up h i then (1 : ℤ) else 0) - (if Γ.down h i then (1 : ℤ) else 0)) :=
    Finset.sum_congr rfl (fun i _ => Γ.sgn_succ_sub h i)
  rw [h2, Finset.sum_sub_distrib, Finset.sum_boole, Finset.sum_boole] at h1
  have h3 : (((Finset.range m).filter (Γ.up h)).card : ℤ) =
      (((Finset.range m).filter (Γ.down h)).card : ℤ) := by linarith
  exact_mod_cast h3.symm

/-- A change happens only at a mismatch. -/
theorem down_mem_mis {h i : ℕ} (hi : i < m) (hd : Γ.down h i) : i ∈ Γ.mis h := by
  unfold mis
  rw [Finset.mem_filter, Finset.mem_range]
  refine ⟨hi, fun ha => ?_⟩
  exact hd.2 ((Γ.z_pos_step ha).mpr hd.1)

theorem up_mem_mis {h i : ℕ} (hi : i < m) (hu : Γ.up h i) : i ∈ Γ.mis h := by
  unfold mis
  rw [Finset.mem_filter, Finset.mem_range]
  refine ⟨hi, fun ha => ?_⟩
  exact hu.1 ((Γ.z_pos_step ha).mp hu.2)

/-- Discrete intermediate value: `z_a > 0` and `z_{a+d} ≤ 0` give a `+→−` change in `[a, a + d)`. -/
theorem exists_down {h a d : ℕ} (ha : 0 < Γ.z h a) (hb : ¬ 0 < Γ.z h (a + d)) :
    ∃ i, a ≤ i ∧ i < a + d ∧ Γ.down h i := by
  classical
  have hex : ∃ k, k ≤ d ∧ ¬ 0 < Γ.z h (a + k) := ⟨d, le_refl d, hb⟩
  obtain ⟨k, hkd, hkz, hkmin⟩ : ∃ k, k ≤ d ∧ ¬ 0 < Γ.z h (a + k) ∧
      ∀ k', k' < k → k' ≤ d → 0 < Γ.z h (a + k') :=
    ⟨Nat.find hex, (Nat.find_spec hex).1, (Nat.find_spec hex).2, fun k' hk' hk'd => by
      by_contra hneg
      exact Nat.find_min hex hk' ⟨hk'd, hneg⟩⟩
  have hk0 : k ≠ 0 := by
    intro h0
    rw [h0, Nat.add_zero] at hkz
    exact hkz ha
  obtain ⟨k', rfl⟩ := Nat.exists_eq_succ_of_ne_zero hk0
  refine ⟨a + k', Nat.le_add_right a k', by omega, hkmin k' (Nat.lt_succ_self k') (by omega), ?_⟩
  rw [Nat.add_assoc]
  exact hkz

/-- Discrete intermediate value: `z_a ≤ 0` and `z_{a+d} > 0` give a `−→+` change in `[a, a + d)`. -/
theorem exists_up {h a d : ℕ} (ha : ¬ 0 < Γ.z h a) (hb : 0 < Γ.z h (a + d)) :
    ∃ i, a ≤ i ∧ i < a + d ∧ Γ.up h i := by
  classical
  have hex : ∃ k, k ≤ d ∧ 0 < Γ.z h (a + k) := ⟨d, le_refl d, hb⟩
  obtain ⟨k, hkd, hkz, hkmin⟩ : ∃ k, k ≤ d ∧ 0 < Γ.z h (a + k) ∧
      ∀ k', k' < k → k' ≤ d → ¬ 0 < Γ.z h (a + k') :=
    ⟨Nat.find hex, (Nat.find_spec hex).1, (Nat.find_spec hex).2, fun k' hk' hk'd hpos =>
      Nat.find_min hex hk' ⟨hk'd, hpos⟩⟩
  have hk0 : k ≠ 0 := by
    intro h0
    rw [h0, Nat.add_zero] at hkz
    exact ha hkz
  obtain ⟨k', rfl⟩ := Nat.exists_eq_succ_of_ne_zero hk0
  refine ⟨a + k', Nat.le_add_right a k', by omega, hkmin k' (Nat.lt_succ_self k') (by omega), ?_⟩
  rw [Nat.add_assoc]
  exact hkz

/-- Step 2, first half: a `+→−` change in the window `[j − h, m − h)`, written as naturals as
`[j + (m − h % m), j + (m − h % m) + (m − j))`, for an index `j < m` attaining the maximum. -/
theorem exists_down_window (hprim : ∀ i j, i < m → j < m → Γ.n i = Γ.n j → i = j) {j : ℕ}
    (hj : ∀ i, Γ.n i ≤ Γ.n j) (hjm : j < m) {h : ℕ} (hh : h % m ≠ 0) :
    ∃ i, j + (m - h % m) ≤ i ∧ i < j + (m - h % m) + (m - j) ∧ Γ.down h i := by
  apply Γ.exists_down (Γ.z_pred_max_pos hprim hj hh)
  have e : j + (m - h % m) + (m - j) = (m - h % m) + m := by omega
  rw [e, Γ.z_per]
  exact not_lt.mpr (Γ.z_pred_min_neg hprim hh).le

/-- Step 2, second half: a `−→+` change in the window `[j, m)`. -/
theorem exists_up_window (hprim : ∀ i j, i < m → j < m → Γ.n i = Γ.n j → i = j) {j : ℕ}
    (hj : ∀ i, Γ.n i ≤ Γ.n j) (hjm : j < m) {h : ℕ} (hh : h % m ≠ 0) :
    ∃ i, j ≤ i ∧ i < j + (m - j) ∧ Γ.up h i := by
  apply Γ.exists_up (not_lt.mpr (Γ.z_max_neg hprim hj hh).le)
  have e : j + (m - j) = 0 + m := by omega
  rw [e, Γ.z_per]
  exact Γ.z_min_pos hprim hh

/-- Every `+→−` change position reduces modulo `m` to one in the period. -/
theorem down_mod (h i : ℕ) : Γ.down h (i % m) ↔ Γ.down h i := by
  have hm := Γ.hm
  conv_rhs => rw [← Nat.mod_add_div i m]
  induction (i / m) with
  | zero => simp
  | succ t ih => rw [Nat.mul_succ, ← Nat.add_assoc, Γ.down_per, ih]

theorem up_mod (h i : ℕ) : Γ.up h (i % m) ↔ Γ.up h i := by
  have hm := Γ.hm
  conv_rhs => rw [← Nat.mod_add_div i m]
  induction (i / m) with
  | zero => simp
  | succ t ih => rw [Nat.mul_succ, ← Nat.add_assoc, Γ.up_per, ih]

/-- Step 2, conclusion for exactly three mismatches: exactly one `+→−` change and one `−→+`
change in the period, and some mismatch has no change. -/
theorem three_mismatch_changes (hprim : ∀ i j, i < m → j < m → Γ.n i = Γ.n j → i = j) {j : ℕ}
    (hj : ∀ i, Γ.n i ≤ Γ.n j) (hjm : j < m) {h : ℕ} (hh : h % m ≠ 0)
    (hs : (Γ.mis h).card = 3) :
    ((Finset.range m).filter (Γ.down h)).card = 1 ∧
      ((Finset.range m).filter (Γ.up h)).card = 1 ∧
      ∃ e ∈ Γ.mis h, ¬ Γ.down h e ∧ ¬ Γ.up h e := by
  classical
  set D := (Finset.range m).filter (Γ.down h) with hD
  set U := (Finset.range m).filter (Γ.up h) with hU
  have hDU : D.card = U.card := Γ.card_down_eq_card_up h
  have hDm : D ⊆ Γ.mis h := by
    intro i hi
    rw [hD, Finset.mem_filter, Finset.mem_range] at hi
    exact Γ.down_mem_mis hi.1 hi.2
  have hUm : U ⊆ Γ.mis h := by
    intro i hi
    rw [hU, Finset.mem_filter, Finset.mem_range] at hi
    exact Γ.up_mem_mis hi.1 hi.2
  have hdisj : Disjoint D U := by
    rw [Finset.disjoint_left]
    intro i hiD hiU
    rw [hD, Finset.mem_filter] at hiD
    rw [hU, Finset.mem_filter] at hiU
    exact hiU.2.1 hiD.2.1
  have hsub : D ∪ U ⊆ Γ.mis h := Finset.union_subset hDm hUm
  have hcard : D.card + U.card ≤ 3 := by
    rw [← Finset.card_union_of_disjoint hdisj, ← hs]
    exact Finset.card_le_card hsub
  have hDpos : 0 < D.card := by
    obtain ⟨i, _, _, hdown⟩ := Γ.exists_down_window hprim hj hjm hh
    apply Finset.card_pos.mpr
    refine ⟨i % m, ?_⟩
    rw [hD, Finset.mem_filter, Finset.mem_range]
    exact ⟨Nat.mod_lt _ Γ.hm, (Γ.down_mod h i).mpr hdown⟩
  have hD1 : D.card = 1 := by omega
  have hU1 : U.card = 1 := by omega
  refine ⟨hD1, hU1, ?_⟩
  have hlt : (D ∪ U).card < (Γ.mis h).card := by
    rw [Finset.card_union_of_disjoint hdisj, hD1, hU1, hs]
    norm_num
  by_contra hno
  have hsub2 : Γ.mis h ⊆ D ∪ U := by
    intro e hem
    by_contra hen
    have hem' := hem
    unfold mis at hem'
    rw [Finset.mem_filter, Finset.mem_range] at hem'
    apply hno
    refine ⟨e, hem, ?_, ?_⟩
    · intro hd
      apply hen
      have heD : e ∈ D := by
        rw [hD, Finset.mem_filter, Finset.mem_range]
        exact ⟨hem'.1, hd⟩
      exact Finset.mem_union_left U heD
    · intro hu
      apply hen
      have heU : e ∈ U := by
        rw [hU, Finset.mem_filter, Finset.mem_range]
        exact ⟨hem'.1, hu⟩
      exact Finset.mem_union_right D heU
  have := Finset.card_le_card hsub2
  omega

end OddCycle

/-! ### S7-b (part 3a): the alignment lemma (S7 Step 4) under the window structure

With `d ≤ h ≤ j` (`d = m − j`), the descent window `W = [j, m)` having the single mismatch `e_b` and
the window `W − h = [j − h, m − h)` having the single mismatch `e_a`: every `i ∈ W ∖ {e_b}` agrees,
so `a_i = a_{i+h} = a_{i+h−m}` with `i + h − m ∈ [0, j)` and the shift injective, hence
`Σ_{W∖{e_b}} (a_i − 1) ≤ X_c`; if `e_b ≠ e_a + h` then `e_b − h ∈ W − h` agrees, so `a_{e_b}` is a
climb letter and `a_{e_b} − 1 ≤ X_c`; together `X_d ≤ 2 X_c` (`dexcess_le_two_excess`). Since
`X_c + X_d = A − m` (`excess_add_dexcess`), condition A, `3 X_c < A − m`, forces the alignment
`e_b = e_a + h` (`alignment`). The window structure itself (Step 3) is part 3b. -/

namespace OddCycle

variable {m : ℕ} (Γ : OddCycle m)

theorem excess_eq_sum (j : ℕ) : Γ.excess j = ∑ i ∈ Finset.range j, (Γ.a i - 1) := by
  induction j with
  | zero => simp [excess]
  | succ j ih => rw [Γ.excess_succ, ih, Finset.sum_range_succ]

/-- The descent excess `X_d = Σ_{i ∈ [j, m)} (a_i − 1)`. -/
def dexcess (j : ℕ) : ℕ := ∑ i ∈ Finset.Ico j m, (Γ.a i - 1)

/-- `X_c + X_d = A − m` (letters `≥ 1`), in additive form. -/
theorem excess_add_dexcess (hapos : ∀ i, 1 ≤ Γ.a i) {j : ℕ} (hj : j ≤ m) :
    Γ.excess j + Γ.dexcess j + m = Γ.Apre m := by
  rw [Γ.excess_eq_sum]
  unfold dexcess Apre
  rw [Finset.sum_range_add_sum_Ico _ hj]
  have h1 : ∑ i ∈ Finset.range m, (Γ.a i - 1) + ∑ _i ∈ Finset.range m, (1 : ℕ) =
      ∑ i ∈ Finset.range m, Γ.a i := by
    rw [← Finset.sum_add_distrib]
    apply Finset.sum_congr rfl
    intro i _
    have := hapos i
    omega
  rw [Finset.sum_const, Finset.card_range, smul_eq_mul, mul_one] at h1
  exact h1

/-- Step 4's excess transfer: `X_d ≤ 2 X_c` when `e_b ≠ e_a + h`. -/
theorem dexcess_le_two_excess {j h e_a e_b : ℕ} (hjm : j < m)
    (hdh : m - j ≤ h) (hhj : h ≤ j) (heb : j ≤ e_b ∧ e_b < m)
    (hW : ∀ i, j ≤ i → i < m → i ≠ e_b → Γ.agree h i)
    (hW' : ∀ k, j - h ≤ k → k < m - h → k ≠ e_a → Γ.agree h k)
    (hne : e_b ≠ e_a + h) : Γ.dexcess j ≤ 2 * Γ.excess j := by
  rw [Γ.excess_eq_sum]
  unfold dexcess
  have hmem : e_b ∈ Finset.Ico j m := Finset.mem_Ico.mpr heb
  rw [← Finset.add_sum_erase _ _ hmem]
  have hpart1 : ∑ i ∈ (Finset.Ico j m).erase e_b, (Γ.a i - 1) ≤
      ∑ k ∈ Finset.range j, (Γ.a k - 1) := by
    have hinj : ∀ x ∈ (Finset.Ico j m).erase e_b, ∀ y ∈ (Finset.Ico j m).erase e_b,
        x + h - m = y + h - m → x = y := by
      intro x hx y hy hxy
      rw [Finset.mem_erase, Finset.mem_Ico] at hx hy
      omega
    have heq : ∑ i ∈ (Finset.Ico j m).erase e_b, (Γ.a i - 1) =
        ∑ k ∈ ((Finset.Ico j m).erase e_b).image (fun i => i + h - m), (Γ.a k - 1) := by
      rw [Finset.sum_image hinj]
      apply Finset.sum_congr rfl
      intro i hi
      rw [Finset.mem_erase, Finset.mem_Ico] at hi
      have hag : Γ.agree h i := hW i hi.2.1 hi.2.2 hi.1
      unfold agree at hag
      have hper : Γ.a (i + h) = Γ.a (i + h - m) := by
        have e : i + h = (i + h - m) + m := by omega
        calc Γ.a (i + h) = Γ.a ((i + h - m) + m) := by rw [← e]
          _ = Γ.a (i + h - m) := Γ.a_per _
      rw [hag, hper]
    rw [heq]
    apply Finset.sum_le_sum_of_subset_of_nonneg
    · intro k hk
      rw [Finset.mem_image] at hk
      obtain ⟨i, hi, rfl⟩ := hk
      rw [Finset.mem_erase, Finset.mem_Ico] at hi
      rw [Finset.mem_range]
      omega
    · intro k _ _
      exact Nat.zero_le _
  have hpart2 : Γ.a e_b - 1 ≤ ∑ k ∈ Finset.range j, (Γ.a k - 1) := by
    have hk1 : j - h ≤ e_b - h := by omega
    have hk2 : e_b - h < m - h := by omega
    have hk3 : e_b - h ≠ e_a := by omega
    have hag : Γ.agree h (e_b - h) := hW' (e_b - h) hk1 hk2 hk3
    unfold agree at hag
    rw [Nat.sub_add_cancel (by omega : h ≤ e_b)] at hag
    rw [← hag]
    apply Finset.single_le_sum (fun k _ => Nat.zero_le (Γ.a k - 1))
    rw [Finset.mem_range]
    omega
  omega

/-- Step 4, the alignment: with condition A, `3 X_c < A − m`, the two located mismatches satisfy
`e_b = e_a + h`. -/
theorem alignment (hapos : ∀ i, 1 ≤ Γ.a i) {j h e_a e_b : ℕ} (hjm : j < m) (hdh : m - j ≤ h)
    (hhj : h ≤ j) (heb : j ≤ e_b ∧ e_b < m)
    (hW : ∀ i, j ≤ i → i < m → i ≠ e_b → Γ.agree h i)
    (hW' : ∀ k, j - h ≤ k → k < m - h → k ≠ e_a → Γ.agree h k)
    (hA : 3 * Γ.excess j < Γ.Apre m - m) : e_b = e_a + h := by
  by_contra hne
  have h1 := Γ.dexcess_le_two_excess hjm hdh hhj heb hW hW' hne
  have h2 := Γ.excess_add_dexcess hapos hjm.le
  omega

end OddCycle

/-! ### S7-b (part 3b): the window structure from the spacing bound (S7 Step 3), and Steps 3–4 assembled

The spacing bound is the hypothesis `hsep`: distinct mismatches `e₁ < e₂` have both arcs at least
`σ` (`σ ≤ e₂ − e₁` and `σ ≤ m + e₁ − e₂`). With `σ ≥ 2d − 1`, `d = m − j`, and the two located
mismatches (a `+→−` change in `[j − h, m − h)`, a `−→+` change in `[j, m)`), both window conditions
`d ≤ h ≤ j` hold (`window_conditions`: otherwise the two windows overlap in an arc of at most `2d − 1`
positions containing both). With `σ ≥ d`, a window of length `d` holds at most one mismatch
(`unique_in_window`), so every other position of the window agrees (`agree_of_window`). Assembled
with S7-b part 2 (the located changes) and part 3a (alignment): for a primitive cycle, an index `j`
attaining the maximum, a rotation `1 ≤ h < m`, the spacing bound and condition A, there are
mismatches `e_a ∈ [j − h, m − h)` (a `+→−` change) and `e_b ∈ [j, m)` (a `−→+` change) with
`d ≤ h ≤ j` and `e_b = e_a + h` (`three_mismatch_structure`). The spacing bound itself comes from
S7 Step 1 (`t_max`) and is supplied in S7-c/S7-d. -/

namespace OddCycle

variable {m : ℕ} (Γ : OddCycle m)

/-- Step 3: both window conditions `d ≤ h ≤ j` from the spacing bound `σ ≥ 2d − 1`. -/
theorem window_conditions {j h σ e_a' e_b : ℕ} (hjm : j < m) (hhm : h < m)
    (hsep : ∀ e₁ e₂, e₁ ∈ Γ.mis h → e₂ ∈ Γ.mis h → e₁ < e₂ → σ ≤ e₂ - e₁ ∧ σ ≤ m + e₁ - e₂)
    (hσ : 2 * (m - j) ≤ σ + 1)
    (hea1 : j + (m - h) ≤ e_a') (hea2 : e_a' < j + (m - h) + (m - j)) (hea : e_a' % m ∈ Γ.mis h)
    (heb1 : j ≤ e_b) (heb2 : e_b < m) (heb : e_b ∈ Γ.mis h) (hne : e_a' % m ≠ e_b) :
    m - j ≤ h ∧ h ≤ j := by
  have hm := Γ.hm
  have hmod := Nat.mod_add_div e_a' m
  have hlt := Nat.mod_lt e_a' hm
  have hq : e_a' / m ≤ 1 := by
    have h2 : e_a' / m < 2 := (Nat.div_lt_iff_lt_mul hm).mpr (by omega)
    omega
  generalize he : e_a' % m = e_a at hea hne hmod hlt
  have hpair : (e_a < e_b → σ ≤ e_b - e_a ∧ σ ≤ m + e_a - e_b) ∧
      (e_b < e_a → σ ≤ e_a - e_b ∧ σ ≤ m + e_b - e_a) :=
    ⟨fun hlt' => hsep e_a e_b hea heb hlt', fun hlt' => hsep e_b e_a heb hea hlt'⟩
  rcases Nat.le_one_iff_eq_zero_or_eq_one.mp hq with h0 | h1
  · rw [h0, Nat.mul_zero, Nat.add_zero] at hmod
    rcases Nat.lt_or_gt_of_ne hne with hlt' | hlt'
    · have := hpair.1 hlt'
      omega
    · have := hpair.2 hlt'
      omega
  · rw [h1, Nat.mul_one] at hmod
    rcases Nat.lt_or_gt_of_ne hne with hlt' | hlt'
    · have := hpair.1 hlt'
      omega
    · have := hpair.2 hlt'
      omega

/-- With spacing `σ ≥ d`, a window of length `d` contains at most one mismatch. -/
theorem unique_in_window {h σ lo d : ℕ}
    (hsep : ∀ e₁ e₂, e₁ ∈ Γ.mis h → e₂ ∈ Γ.mis h → e₁ < e₂ → σ ≤ e₂ - e₁ ∧ σ ≤ m + e₁ - e₂)
    (hσ : d ≤ σ) {e₁ e₂ : ℕ} (h₁ : e₁ ∈ Γ.mis h) (h₂ : e₂ ∈ Γ.mis h)
    (hlo₁ : lo ≤ e₁) (hhi₁ : e₁ < lo + d) (hlo₂ : lo ≤ e₂) (hhi₂ : e₂ < lo + d) : e₁ = e₂ := by
  by_contra hne
  rcases Nat.lt_or_gt_of_ne hne with hlt | hlt
  · have := hsep e₁ e₂ h₁ h₂ hlt
    omega
  · have := hsep e₂ e₁ h₂ h₁ hlt
    omega

/-- Every position of a window other than its unique mismatch agrees. -/
theorem agree_of_window {h σ lo d e : ℕ}
    (hsep : ∀ e₁ e₂, e₁ ∈ Γ.mis h → e₂ ∈ Γ.mis h → e₁ < e₂ → σ ≤ e₂ - e₁ ∧ σ ≤ m + e₁ - e₂)
    (hσ : d ≤ σ) (he : e ∈ Γ.mis h) (hlo : lo ≤ e) (hhi : e < lo + d) (hd : lo + d ≤ m)
    {i : ℕ} (hlo' : lo ≤ i) (hhi' : i < lo + d) (hne : i ≠ e) : Γ.agree h i := by
  by_contra hna
  have hi : i ∈ Γ.mis h := by
    unfold mis
    rw [Finset.mem_filter, Finset.mem_range]
    exact ⟨by omega, hna⟩
  exact hne (Γ.unique_in_window hsep hσ hi he hlo' hhi' hlo hhi)

/-- **S7 Steps 2–4 assembled.** For a primitive cycle, an index `j < m` attaining the maximum, a
rotation `1 ≤ h < m`, the spacing bound `σ ≥ 2d − 1` between distinct mismatches, positive letters
and condition A: there are a `+→−` mismatch `e_a ∈ [j − h, m − h)` and a `−→+` mismatch
`e_b ∈ [j, m)` with `d ≤ h ≤ j` and `e_b = e_a + h`. -/
theorem three_mismatch_structure (hprim : ∀ i j, i < m → j < m → Γ.n i = Γ.n j → i = j) {j : ℕ}
    (hj : ∀ i, Γ.n i ≤ Γ.n j) (hjm : j < m) {h : ℕ} (hh1 : 1 ≤ h) (hhm : h < m) {σ : ℕ}
    (hsep : ∀ e₁ e₂, e₁ ∈ Γ.mis h → e₂ ∈ Γ.mis h → e₁ < e₂ → σ ≤ e₂ - e₁ ∧ σ ≤ m + e₁ - e₂)
    (hσ : 2 * (m - j) ≤ σ + 1) (hapos : ∀ i, 1 ≤ Γ.a i) (hA : 3 * Γ.excess j < Γ.Apre m - m) :
    ∃ e_a e_b, e_a ∈ Γ.mis h ∧ e_b ∈ Γ.mis h ∧ j - h ≤ e_a ∧ e_a < m - h ∧ j ≤ e_b ∧ e_b < m ∧
      Γ.down h e_a ∧ Γ.up h e_b ∧ m - j ≤ h ∧ h ≤ j ∧ e_b = e_a + h := by
  have hm := Γ.hm
  have hh : h % m ≠ 0 := by
    rw [Nat.mod_eq_of_lt hhm]
    omega
  obtain ⟨e_a', hea1, hea2, hdown'⟩ := Γ.exists_down_window hprim hj hjm hh
  obtain ⟨e_b, heb1, heb2, hup⟩ := Γ.exists_up_window hprim hj hjm hh
  rw [Nat.mod_eq_of_lt hhm] at hea1 hea2
  have hdown : Γ.down h (e_a' % m) := (Γ.down_mod h e_a').mpr hdown'
  have hea : e_a' % m ∈ Γ.mis h := Γ.down_mem_mis (Nat.mod_lt _ hm) hdown
  have heb2' : e_b < m := by omega
  have heb : e_b ∈ Γ.mis h := Γ.up_mem_mis heb2' hup
  have hne : e_a' % m ≠ e_b := by
    intro heq
    rw [heq] at hdown
    exact hup.1 hdown.1
  obtain ⟨hdh, hhj⟩ := Γ.window_conditions hjm hhm hsep hσ hea1 hea2 hea heb1 heb2' heb hne
  -- under `h ≤ j`, `e_a' ≥ m`, so its residue is `e_a' − m ∈ [j − h, m − h)`
  have hea'm : m ≤ e_a' := by omega
  have hres : e_a' % m = e_a' - m := by
    have h2 : e_a' - m < m := by omega
    rw [Nat.mod_eq_sub_mod hea'm, Nat.mod_eq_of_lt h2]
  rw [hres] at hdown hea hne
  have hdpos : 1 ≤ m - j := by omega
  have hσd : m - j ≤ σ := by omega
  have hW : ∀ i, j ≤ i → i < m → i ≠ e_b → Γ.agree h i := by
    intro i hi1 hi2 hi3
    exact Γ.agree_of_window hsep hσd heb heb1 (by omega) (by omega) hi1 (by omega) hi3
  have hW' : ∀ k, j - h ≤ k → k < m - h → k ≠ e_a' - m → Γ.agree h k := by
    intro k hk1 hk2 hk3
    exact Γ.agree_of_window hsep hσd hea (by omega) (by omega) (by omega) hk1 (by omega) hk3
  have halign := Γ.alignment hapos hjm hdh hhj ⟨heb1, heb2'⟩ hW hW' hA
  exact ⟨e_a' - m, e_b, hea, heb, by omega, by omega, heb1, heb2', hdown, hup, hdh, hhj, halign⟩

end OddCycle

/-! ### S7-c (part 1): Step 1 — the uniform run bound and the spacing bound from three mismatches

Every agreeing run with `z ≠ 0` at its end has `2·3^t < H ≤ L (3/2)^{m−1} (1 + q/(3L))^{m−1}`
(`run_bound_max`: the witness is a state, hence at most the maximum, which the ceiling bounds), so
all runs are bounded by one `T`. With exactly three mismatches, the forward arc from one mismatch to
another holds at most one mismatch in its interior (`third_mismatch`, `eq_third`), so it consists of
at most two agreeing runs and two steps: its length is at most `2(T + 1)` (`arc_le`). Hence distinct
mismatches have both arcs at least `σ = m − 2(T + 1)` (`hsep_of_runs`), the spacing bound used by
S7-b part 3b. This is the only place where `s = 3` enters. -/

namespace OddCycle

variable {m : ℕ} (Γ : OddCycle m)

/-- Step 1, the uniform run bound: `2·3^t < L (3/2)^{m−1} (1 + q/(3L))^{m−1}` for every agreeing
run with `z ≠ 0` at its end. -/
theorem run_bound_max (hapos : ∀ i, 1 ≤ Γ.a i) {j : ℕ} (hj : ∀ i, Γ.n i ≤ Γ.n j) (hjm : j < m)
    {h i t : ℕ} (hagree : ∀ k, k < t → Γ.a (i + k) = Γ.a (i + k + h)) (hz : Γ.z h (i + t) ≠ 0) :
    2 * (3 : ℝ) ^ t < Γ.n 0 * (3 / 2 : ℝ) ^ (m - 1) * (1 + Γ.q / (3 * Γ.n 0)) ^ (m - 1) := by
  have hw := Γ.witness_gt t hagree hz
  have hmax : max (Γ.n (i + t)) (Γ.n (i + t + h)) ≤ Γ.n j := max_le (hj _) (hj _)
  have h1 : 2 * (3 : ℤ) ^ t < Γ.n j := lt_of_lt_of_le hw hmax
  have h1R : 2 * (3 : ℝ) ^ t < Γ.n j := by exact_mod_cast h1
  have hcl := Γ.n_le_climb hapos j
  have hones : Γ.ones j ≤ m - 1 := (Γ.ones_le j).trans (by omega)
  have hj1 : j ≤ m - 1 := by omega
  have hε := Γ.one_add_eps_pos
  have hn0 : (0 : ℝ) < Γ.n 0 := by exact_mod_cast Γ.npos
  have h2 : (3 / 2 : ℝ) ^ Γ.ones j ≤ (3 / 2 : ℝ) ^ (m - 1) :=
    pow_le_pow_right₀ (by norm_num) hones
  have h3 : (1 + (Γ.q : ℝ) / (3 * Γ.n 0)) ^ j ≤ (1 + (Γ.q : ℝ) / (3 * Γ.n 0)) ^ (m - 1) :=
    pow_le_pow_right₀ (by linarith [Γ.eps_nonneg]) hj1
  calc 2 * (3 : ℝ) ^ t < Γ.n j := h1R
    _ ≤ Γ.n 0 * (3 / 2 : ℝ) ^ Γ.ones j * (1 + Γ.q / (3 * Γ.n 0)) ^ j := hcl
    _ ≤ Γ.n 0 * (3 / 2 : ℝ) ^ (m - 1) * (1 + Γ.q / (3 * Γ.n 0)) ^ (m - 1) :=
        mul_le_mul (mul_le_mul_of_nonneg_left h2 hn0.le) h3 (pow_pos hε j).le
          (mul_nonneg hn0.le (by positivity))

/-- With exactly three mismatches, removing two leaves one. -/
theorem third_mismatch {h e₁ e₂ : ℕ} (hs : (Γ.mis h).card = 3) (h₁ : e₁ ∈ Γ.mis h)
    (h₂ : e₂ ∈ Γ.mis h) (hne : e₁ ≠ e₂) : ∃ e₃, ((Γ.mis h).erase e₁).erase e₂ = {e₃} := by
  have hc : (((Γ.mis h).erase e₁).erase e₂).card = 1 := by
    rw [Finset.card_erase_of_mem (Finset.mem_erase.mpr ⟨hne.symm, h₂⟩),
      Finset.card_erase_of_mem h₁, hs]
  exact Finset.card_eq_one.mp hc

/-- Any mismatch other than `e₁, e₂` is the third one. -/
theorem eq_third {h e₁ e₂ e₃ r : ℕ} (h3 : ((Γ.mis h).erase e₁).erase e₂ = {e₃}) (hr : r ∈ Γ.mis h)
    (hr1 : r ≠ e₁) (hr2 : r ≠ e₂) : r = e₃ := by
  have hmem : r ∈ ((Γ.mis h).erase e₁).erase e₂ :=
    Finset.mem_erase.mpr ⟨hr2, Finset.mem_erase.mpr ⟨hr1, hr⟩⟩
  rw [h3, Finset.mem_singleton] at hmem
  exact hmem

/-- The forward arc from a mismatch `e₁` to another mismatch `e₂` (`(e₁ + L) % m = e₂`, `0 < L < m`)
has length at most `2(T + 1)` when every agreeing run has length `≤ T` and there are exactly three
mismatches. -/
theorem arc_le {h T : ℕ} (hT : ∀ i t, (∀ k, k < t → Γ.agree h (i + k)) → t ≤ T)
    (hs : (Γ.mis h).card = 3) {e₁ e₂ L : ℕ} (h₁ : e₁ ∈ Γ.mis h) (h₂ : e₂ ∈ Γ.mis h) (hne : e₁ ≠ e₂)
    (hL0 : 0 < L) (hLm : L < m) (hL : (e₁ + L) % m = e₂) : L ≤ 2 * (T + 1) := by
  have hm := Γ.hm
  have he1 : e₁ < m := by
    unfold mis at h₁
    rw [Finset.mem_filter, Finset.mem_range] at h₁
    exact h₁.1
  obtain ⟨e₃, h3⟩ := Γ.third_mismatch hs h₁ h₂ hne
  have hres : ∀ k, 1 ≤ k → k < L → ¬ Γ.agree h (e₁ + k) → (e₁ + k) % m = e₃ := by
    intro k hk1 hkL hna
    have hmem : (e₁ + k) % m ∈ Γ.mis h := by
      unfold mis
      rw [Finset.mem_filter, Finset.mem_range, Γ.agree_mod]
      exact ⟨Nat.mod_lt _ hm, hna⟩
    apply Γ.eq_third h3 hmem
    · intro heq
      have h0 : (e₁ + k) % m = (e₁ + 0) % m := by
        rw [heq, Nat.add_zero, Nat.mod_eq_of_lt he1]
      have hk : k % m = 0 % m := Nat.ModEq.add_left_cancel' e₁ h0
      rw [Nat.zero_mod, Nat.mod_eq_of_lt (by omega : k < m)] at hk
      omega
    · intro heq
      rw [← hL] at heq
      have hk : k % m = L % m := Nat.ModEq.add_left_cancel' e₁ heq
      rw [Nat.mod_eq_of_lt (by omega : k < m), Nat.mod_eq_of_lt hLm] at hk
      omega
  by_cases hex : ∃ k₀, 1 ≤ k₀ ∧ k₀ < L ∧ ¬ Γ.agree h (e₁ + k₀)
  · obtain ⟨k₀, hk₀1, hk₀L, hk₀⟩ := hex
    have huniq : ∀ k, 1 ≤ k → k < L → ¬ Γ.agree h (e₁ + k) → k = k₀ := by
      intro k hk1 hkL hna
      have e1 := hres k hk1 hkL hna
      have e2 := hres k₀ hk₀1 hk₀L hk₀
      have hk : k % m = k₀ % m := Nat.ModEq.add_left_cancel' e₁ (e1.trans e2.symm)
      rwa [Nat.mod_eq_of_lt (by omega : k < m), Nat.mod_eq_of_lt (by omega : k₀ < m)] at hk
    have hrun1 : k₀ - 1 ≤ T := by
      apply hT (e₁ + 1) (k₀ - 1)
      intro k hk
      by_contra hna
      have := huniq (k + 1) (by omega) (by omega)
        (by rw [show e₁ + (k + 1) = e₁ + 1 + k by omega]; exact hna)
      omega
    have hrun2 : L - 1 - k₀ ≤ T := by
      apply hT (e₁ + k₀ + 1) (L - 1 - k₀)
      intro k hk
      by_contra hna
      have := huniq (k₀ + 1 + k) (by omega) (by omega)
        (by rw [show e₁ + (k₀ + 1 + k) = e₁ + k₀ + 1 + k by omega]; exact hna)
      omega
    omega
  · have hall : ∀ k, 1 ≤ k → k < L → Γ.agree h (e₁ + k) := by
      intro k hk1 hkL
      by_contra hna
      exact hex ⟨k, hk1, hkL, hna⟩
    have hrun : L - 1 ≤ T := by
      apply hT (e₁ + 1) (L - 1)
      intro k hk
      rw [show e₁ + 1 + k = e₁ + (k + 1) by omega]
      exact hall (k + 1) (by omega) (by omega)
    omega

/-- Step 1's spacing bound: with every agreeing run of length `≤ T` and exactly three mismatches,
distinct mismatches `e₁ < e₂` have both arcs at least `m − 2(T + 1)`. -/
theorem hsep_of_runs {h T : ℕ} (hT : ∀ i t, (∀ k, k < t → Γ.agree h (i + k)) → t ≤ T)
    (hs : (Γ.mis h).card = 3) : ∀ e₁ e₂, e₁ ∈ Γ.mis h → e₂ ∈ Γ.mis h → e₁ < e₂ →
      m - 2 * (T + 1) ≤ e₂ - e₁ ∧ m - 2 * (T + 1) ≤ m + e₁ - e₂ := by
  intro e₁ e₂ h₁ h₂ hlt
  have hm := Γ.hm
  have he2 : e₂ < m := by
    unfold mis at h₂
    rw [Finset.mem_filter, Finset.mem_range] at h₂
    exact h₂.1
  have hA1 : (e₁ + (e₂ - e₁)) % m = e₂ := by
    rw [Nat.add_sub_cancel' hlt.le, Nat.mod_eq_of_lt he2]
  have hA2 : (e₂ + (m - (e₂ - e₁))) % m = e₁ := by
    rw [show e₂ + (m - (e₂ - e₁)) = e₁ + m by omega, Nat.add_mod_right,
      Nat.mod_eq_of_lt (by omega)]
  have hL1 := Γ.arc_le hT hs h₁ h₂ hlt.ne (by omega) (by omega) hA1
  have hL2 := Γ.arc_le hT hs h₂ h₁ hlt.ne' (by omega) (by omega) hA2
  omega

end OddCycle

/-! ### S7-c (part 2): Step 5 — the third run's witness, and the run sums of Step 6

With the aligned pair `e_a`, `e_b = e_a + h` and the window structure, the third mismatch `e_c` lies
either below `e_a` (order 1) or strictly between `e_a` and `e_b` (order 2), since the windows hold no
other mismatch. The three agreeing runs between consecutive mismatches have lengths summing to
`m − 3`. In order 1 the run from `e_b + 1` ends at `e_c` (mod `m`), where `δ > 0` by sign
persistence from the `−→+` change at `e_b`, so its witness is `n_{e_c + h}` with `e_c + h < e_b` —
an honest index, no wrap — and `e_c + h ≤ τ + τ′ + 1` where `τ′ = h − 1` is the run between `e_a`
and `e_b`. In order 2 the run from `e_a + 1` ends at `e_c`, where `δ < 0` from the `+→−` change at
`e_a`, so the witness is `n_{e_c}` with `e_c ≤ τ + τ′ + 1`, `τ′` the wrapping run from `e_b + 1`.
Either way `2·3^τ < L (3/2)^{τ+τ′+1} (1 + q/(3L))^{τ+τ′+1}` (`three_mismatch_witness`): S7's
`τ (1 − ε) < ℓ + (τ° + 1)κ − 1` in product form, with the three runs exhibited for Step 6. -/

namespace OddCycle

variable {m : ℕ} (Γ : OddCycle m)

/-- With exactly three mismatches `e_a, e_b, e_c`, every position whose residue is none of them
agrees. -/
theorem agree_of_ne_three {h e_a e_b e_c : ℕ} (hs : (Γ.mis h).card = 3) (ha : e_a ∈ Γ.mis h)
    (hb : e_b ∈ Γ.mis h) (hc : e_c ∈ Γ.mis h) (hab : e_a ≠ e_b) (hac : e_a ≠ e_c) (hbc : e_b ≠ e_c)
    (i : ℕ) (h1 : i % m ≠ e_a) (h2 : i % m ≠ e_b) (h3 : i % m ≠ e_c) : Γ.agree h i := by
  have hsub : ({e_a, e_b, e_c} : Finset ℕ) ⊆ Γ.mis h := by
    intro x hx
    simp only [Finset.mem_insert, Finset.mem_singleton] at hx
    rcases hx with rfl | rfl | rfl <;> assumption
  have hcard : ({e_a, e_b, e_c} : Finset ℕ).card = 3 :=
    Finset.card_eq_three.mpr ⟨e_a, e_b, e_c, hab, hac, hbc, rfl⟩
  have heq : ({e_a, e_b, e_c} : Finset ℕ) = Γ.mis h :=
    Finset.eq_of_subset_of_card_le hsub (by rw [hs, hcard])
  by_contra hna
  have hmem : i % m ∈ Γ.mis h := by
    unfold mis
    rw [Finset.mem_filter, Finset.mem_range, Γ.agree_mod]
    exact ⟨Nat.mod_lt _ Γ.hm, hna⟩
  rw [← heq] at hmem
  simp only [Finset.mem_insert, Finset.mem_singleton] at hmem
  rcases hmem with h' | h' | h'
  · exact h1 h'
  · exact h2 h'
  · exact h3 h'

/-- A position below `2m` whose two possible residues avoid the three mismatches agrees. -/
theorem agree_of_pos {h e_a e_b e_c : ℕ} (hs : (Γ.mis h).card = 3) (ha : e_a ∈ Γ.mis h)
    (hb : e_b ∈ Γ.mis h) (hc : e_c ∈ Γ.mis h) (hab : e_a ≠ e_b) (hac : e_a ≠ e_c) (hbc : e_b ≠ e_c)
    (p : ℕ) (hp : p < 2 * m) (h1 : p ≠ e_a) (h2 : p ≠ e_b) (h3 : p ≠ e_c) (h1' : p ≠ e_a + m)
    (h2' : p ≠ e_b + m) (h3' : p ≠ e_c + m) : Γ.agree h p := by
  apply Γ.agree_of_ne_three hs ha hb hc hab hac hbc p
  all_goals
    rcases Nat.lt_or_ge p m with hlt | hge
    · rwa [Nat.mod_eq_of_lt hlt]
    · rw [Nat.mod_eq_sub_mod hge, Nat.mod_eq_of_lt (by omega)]; omega

/-- **Step 5 and the runs of Step 6.** Under the structure of `three_mismatch_structure` (an aligned
pair `e_a`, `e_b = e_a + h` with `h ≤ j`, each window holding exactly its mismatch) and exactly
three mismatches: there are three agreeing runs `τ, τ′, τ″` (with their start indices) summing to
`m − 3`, the first ending at the third mismatch, with the witness bound
`2·3^τ < L (3/2)^{τ+τ′+1} (1 + q/(3L))^{τ+τ′+1}`. -/
theorem three_mismatch_witness (hprim : ∀ i j, i < m → j < m → Γ.n i = Γ.n j → i = j)
    (hapos : ∀ i, 1 ≤ Γ.a i) {j h e_a : ℕ} (hjm : j < m) (hh1 : 1 ≤ h) (hhm : h < m)
    (hs : (Γ.mis h).card = 3) (hea1 : j - h ≤ e_a) (hea2 : e_a < m - h) (hdown : Γ.down h e_a)
    (hup : Γ.up h (e_a + h)) (hhj : h ≤ j)
    (hW : ∀ i, j ≤ i → i < m → i ≠ e_a + h → Γ.agree h i)
    (hW' : ∀ k, j - h ≤ k → k < m - h → k ≠ e_a → Γ.agree h k) :
    ∃ τ τ' τ'' i₁ i₂ i₃ : ℕ, τ + τ' + τ'' = m - 3 ∧
      (∀ k, k < τ → Γ.agree h (i₁ + k)) ∧ (∀ k, k < τ' → Γ.agree h (i₂ + k)) ∧
      (∀ k, k < τ'' → Γ.agree h (i₃ + k)) ∧
      2 * (3 : ℝ) ^ τ < Γ.n 0 * (3 / 2 : ℝ) ^ (τ + τ' + 1) *
        (1 + Γ.q / (3 * Γ.n 0)) ^ (τ + τ' + 1) := by
  have hm := Γ.hm
  have hh : h % m ≠ 0 := by
    rw [Nat.mod_eq_of_lt hhm]
    omega
  have hn0 : (0 : ℝ) < Γ.n 0 := by exact_mod_cast Γ.npos
  have hε := Γ.one_add_eps_pos
  have hεR : (1 : ℝ) ≤ 1 + Γ.q / (3 * Γ.n 0) := by linarith [Γ.eps_nonneg]
  set e_b := e_a + h with heb_def
  have heb : e_b < m := by omega
  have hea_mem : e_a ∈ Γ.mis h := Γ.down_mem_mis (by omega) hdown
  have heb_mem : e_b ∈ Γ.mis h := Γ.up_mem_mis heb hup
  have hab : e_a ≠ e_b := by omega
  obtain ⟨e_c, h3⟩ := Γ.third_mismatch hs hea_mem heb_mem hab
  have hec_mem' : e_c ∈ ((Γ.mis h).erase e_a).erase e_b := by
    rw [h3]
    exact Finset.mem_singleton_self e_c
  have hec_mem : e_c ∈ Γ.mis h := Finset.mem_of_mem_erase (Finset.mem_of_mem_erase hec_mem')
  have hcb : e_c ≠ e_b := (Finset.mem_erase.mp hec_mem').1
  have hca : e_c ≠ e_a := (Finset.mem_erase.mp (Finset.mem_of_mem_erase hec_mem')).1
  have hec_lt : e_c < m := by
    unfold mis at hec_mem
    rw [Finset.mem_filter, Finset.mem_range] at hec_mem
    exact hec_mem.1
  have hec_na : ¬ Γ.agree h e_c := by
    unfold mis at hec_mem
    rw [Finset.mem_filter] at hec_mem
    exact hec_mem.2
  -- `e_c` is not in `W = [j, m)` and not in `W − h = [j − h, m − h)`
  have hec_notW : e_c < j := by
    by_contra hge
    exact hec_na (hW e_c (by omega) hec_lt hcb)
  have hec_notW' : e_c < j - h ∨ m - h ≤ e_c := by
    by_contra hno
    exact hec_na (hW' e_c (by omega) (by omega) hca)
  -- the agreement helper for positions below `2m`
  have hagr : ∀ p, p < 2 * m → p ≠ e_a → p ≠ e_b → p ≠ e_c → p ≠ e_a + m → p ≠ e_b + m →
      p ≠ e_c + m → Γ.agree h p :=
    fun p => Γ.agree_of_pos hs hea_mem heb_mem hec_mem hab hca.symm hcb.symm p
  have hzc : Γ.z h e_c ≠ 0 := Γ.z_ne_zero hprim hh e_c
  rcases Nat.lt_or_gt_of_ne hca with hc1 | hc2
  · -- Order 1: `e_c < e_a`. Runs: `(e_b, e_c + m)`, `(e_a, e_b)`, `(e_c, e_a)`.
    refine ⟨m - e_b + e_c - 1, h - 1, e_a - e_c - 1, e_b + 1, e_a + 1, e_c + 1, by omega,
      ?_, ?_, ?_, ?_⟩
    · intro k hk
      exact hagr (e_b + 1 + k) (by omega) (by omega) (by omega) (by omega) (by omega) (by omega)
        (by omega)
    · intro k hk
      exact hagr (e_a + 1 + k) (by omega) (by omega) (by omega) (by omega) (by omega) (by omega)
        (by omega)
    · intro k hk
      exact hagr (e_c + 1 + k) (by omega) (by omega) (by omega) (by omega) (by omega) (by omega)
        (by omega)
    · have hrun : ∀ k, k < m - e_b + e_c - 1 → Γ.agree h (e_b + 1 + k) := by
        intro k hk
        exact hagr (e_b + 1 + k) (by omega) (by omega) (by omega) (by omega) (by omega)
          (by omega) (by omega)
      have hend : e_b + 1 + (m - e_b + e_c - 1) = e_c + m := by omega
      have hzend : Γ.z h (e_b + 1 + (m - e_b + e_c - 1)) ≠ 0 := by
        rw [hend, Γ.z_per]
        exact hzc
      have hw := Γ.witness_gt (m - e_b + e_c - 1) hrun hzend
      have hpos : 0 < Γ.z h e_c := by
        have := (Γ.z_pos_run (m - e_b + e_c - 1) hrun).mpr hup.2
        rwa [hend, Γ.z_per] at this
      rw [hend, Γ.nper, Nat.add_right_comm e_c m h, Γ.nper] at hw
      have hle : Γ.n e_c ≤ Γ.n (e_c + h) := by
        unfold z at hpos
        linarith
      rw [max_eq_right hle] at hw
      have hwR : 2 * (3 : ℝ) ^ (m - e_b + e_c - 1) < Γ.n (e_c + h) := by exact_mod_cast hw
      have hcl := Γ.n_le_climb hapos (e_c + h)
      have hidx : e_c + h ≤ m - e_b + e_c - 1 + (h - 1) + 1 := by omega
      have hones : Γ.ones (e_c + h) ≤ m - e_b + e_c - 1 + (h - 1) + 1 :=
        (Γ.ones_le _).trans hidx
      calc 2 * (3 : ℝ) ^ (m - e_b + e_c - 1) < Γ.n (e_c + h) := hwR
        _ ≤ Γ.n 0 * (3 / 2 : ℝ) ^ Γ.ones (e_c + h) * (1 + Γ.q / (3 * Γ.n 0)) ^ (e_c + h) := hcl
        _ ≤ Γ.n 0 * (3 / 2 : ℝ) ^ (m - e_b + e_c - 1 + (h - 1) + 1) *
            (1 + Γ.q / (3 * Γ.n 0)) ^ (m - e_b + e_c - 1 + (h - 1) + 1) :=
            mul_le_mul (mul_le_mul_of_nonneg_left (pow_le_pow_right₀ (by norm_num) hones) hn0.le)
              (pow_le_pow_right₀ hεR hidx) (pow_pos hε _).le (mul_nonneg hn0.le (by positivity))
  · -- Order 2: `e_a < e_c < e_b`. Runs: `(e_a, e_c)`, `(e_b, e_a + m)`, `(e_c, e_b)`.
    have hc2b : e_c < e_b := by omega
    refine ⟨e_c - e_a - 1, m - e_b + e_a - 1, e_b - e_c - 1, e_a + 1, e_b + 1, e_c + 1, by omega,
      ?_, ?_, ?_, ?_⟩
    · intro k hk
      exact hagr (e_a + 1 + k) (by omega) (by omega) (by omega) (by omega) (by omega) (by omega)
        (by omega)
    · intro k hk
      exact hagr (e_b + 1 + k) (by omega) (by omega) (by omega) (by omega) (by omega) (by omega)
        (by omega)
    · intro k hk
      exact hagr (e_c + 1 + k) (by omega) (by omega) (by omega) (by omega) (by omega) (by omega)
        (by omega)
    · have hrun : ∀ k, k < e_c - e_a - 1 → Γ.agree h (e_a + 1 + k) := by
        intro k hk
        exact hagr (e_a + 1 + k) (by omega) (by omega) (by omega) (by omega) (by omega)
          (by omega) (by omega)
      have hend : e_a + 1 + (e_c - e_a - 1) = e_c := by omega
      have hzend : Γ.z h (e_a + 1 + (e_c - e_a - 1)) ≠ 0 := by
        rw [hend]
        exact hzc
      have hw := Γ.witness_gt (e_c - e_a - 1) hrun hzend
      have hneg1 : Γ.z h (e_a + 1) < 0 := by
        have hne : Γ.z h (e_a + 1) ≠ 0 := Γ.z_ne_zero hprim hh (e_a + 1)
        exact lt_of_le_of_ne (not_lt.mp hdown.2) hne
      have hneg : Γ.z h e_c < 0 := by
        have := (Γ.z_neg_run (e_c - e_a - 1) hrun).mpr hneg1
        rwa [hend] at this
      rw [hend] at hw
      have hle : Γ.n (e_c + h) ≤ Γ.n e_c := by
        unfold z at hneg
        linarith
      rw [max_eq_left hle] at hw
      have hwR : 2 * (3 : ℝ) ^ (e_c - e_a - 1) < Γ.n e_c := by exact_mod_cast hw
      have hcl := Γ.n_le_climb hapos e_c
      have hidx : e_c ≤ e_c - e_a - 1 + (m - e_b + e_a - 1) + 1 := by omega
      have hones : Γ.ones e_c ≤ e_c - e_a - 1 + (m - e_b + e_a - 1) + 1 :=
        (Γ.ones_le _).trans hidx
      calc 2 * (3 : ℝ) ^ (e_c - e_a - 1) < Γ.n e_c := hwR
        _ ≤ Γ.n 0 * (3 / 2 : ℝ) ^ Γ.ones e_c * (1 + Γ.q / (3 * Γ.n 0)) ^ e_c := hcl
        _ ≤ Γ.n 0 * (3 / 2 : ℝ) ^ (e_c - e_a - 1 + (m - e_b + e_a - 1) + 1) *
            (1 + Γ.q / (3 * Γ.n 0)) ^ (e_c - e_a - 1 + (m - e_b + e_a - 1) + 1) :=
            mul_le_mul (mul_le_mul_of_nonneg_left (pow_le_pow_right₀ (by norm_num) hones) hn0.le)
              (pow_le_pow_right₀ hεR hidx) (pow_pos hε _).le (mul_nonneg hn0.le (by positivity))

end OddCycle

/-! ### S7-d (part 1): the numeric conditions of S7 at `m ≥ 2^19`, over the reals

Pure real arithmetic, with natural logarithms. Inputs: `log 2`'s decimal bounds, the rational bounds
`1054/665 < log₂ 3 < 485/306` (from `2^1054 < 3^665` and `3^306 < 2^485`), and the hypotheses that
the assembly (part 2) will supply: the uniform run bound `T log 3 ≤ log(L/2) + (m−1)κ` with
`κ = log(3/2) + e`, `e = log(1 + 1/(3L)) ≤ 1/(3·2^20)`; the longest run `3 t* ≥ m − 3`; the witness
of the longest run against the excess ceiling at the maximum, `log 2 + t* log 3 + X_c log 2 <
log L + jκ`; `D > 0` as `m log 3 < A log 2`; and the `L`-bound `log L ≤ 172 log 2 + 342 log m − log 3`
with the tangent bound `log m ≤ 19 log 2 + m/2^19 − 1`. `numeric_WA` gives condition W
(`2(m − j) + 2(T+1) ≤ m + 1`) and condition A (`3 X_c + 1 ≤ A − m`); `numeric_F` derives `False` from
the Step 5–6 data `m − 3 ≤ τ + 2T` and `τ log 3 < log(L/2) + (τ + T + 1)κ`. -/

namespace OddCycle

set_option exponentiation.threshold 1100 in
theorem log_three_bounds :
    1054 * Real.log 2 < 665 * Real.log 3 ∧ 306 * Real.log 3 < 485 * Real.log 2 := by
  have hn1 : (2 : ℕ) ^ 1054 < 3 ^ 665 := by norm_num
  have hn2 : (3 : ℕ) ^ 306 < 2 ^ 485 := by norm_num
  have hr1 : (2 : ℝ) ^ 1054 < 3 ^ 665 := by exact_mod_cast hn1
  have hr2 : (3 : ℝ) ^ 306 < 2 ^ 485 := by exact_mod_cast hn2
  constructor
  · have h := Real.log_lt_log (by positivity) hr1
    rw [Real.log_pow, Real.log_pow] at h
    push_cast at h
    linarith
  · have h := Real.log_lt_log (by positivity) hr2
    rw [Real.log_pow, Real.log_pow] at h
    push_cast at h
    linarith

/-- Conditions W and A of S7 at `m ≥ 2^19`. -/
theorem numeric_WA (m j T ts Xc A lL e : ℝ) (hm : 2 ^ 19 ≤ m) (hj0 : 0 ≤ j) (hj : j + 1 ≤ m)
    (hT0 : 0 ≤ T)
    (hT : T * Real.log 3 ≤ lL - Real.log 2 + (m - 1) * (Real.log 3 - Real.log 2 + e))
    (hts0 : 0 ≤ ts) (hts : m - 3 ≤ 3 * ts) (hXc0 : 0 ≤ Xc)
    (hjlow : Real.log 2 + ts * Real.log 3 + Xc * Real.log 2 <
      lL + j * (Real.log 3 - Real.log 2 + e))
    (hA0 : 0 ≤ A) (hA : m * Real.log 3 < A * Real.log 2)
    (hlL : lL ≤ 172 * Real.log 2 + 342 * (19 * Real.log 2 + (m / 2 ^ 19 - 1)) - Real.log 3)
    (he : e ≤ 1 / (3 * 2 ^ 20)) :
    2 * (m - j) + 2 * (T + 1) ≤ m + 1 ∧ 3 * Xc + 1 ≤ A - m := by
  have hl2a := Real.log_two_gt_d9
  have hl2b := Real.log_two_lt_d9
  obtain ⟨hl3a, hl3b⟩ := log_three_bounds
  have hκup : Real.log 3 - Real.log 2 + e ≤
      (179 / 306) * 0.6931471808 + 1 / (3 * 2 ^ 20) := by linarith
  have hl3lo : (1054 / 665) * 0.6931471803 ≤ Real.log 3 := by linarith
  have p1 : j * (Real.log 3 - Real.log 2 + e) ≤
      j * ((179 / 306) * 0.6931471808 + 1 / (3 * 2 ^ 20)) := mul_le_mul_of_nonneg_left hκup hj0
  have p2 : ts * ((1054 / 665) * 0.6931471803) ≤ ts * Real.log 3 :=
    mul_le_mul_of_nonneg_left hl3lo hts0
  have p3 : T * ((1054 / 665) * 0.6931471803) ≤ T * Real.log 3 :=
    mul_le_mul_of_nonneg_left hl3lo hT0
  have p4 : (m - 1) * (Real.log 3 - Real.log 2 + e) ≤
      (m - 1) * ((179 / 306) * 0.6931471808 + 1 / (3 * 2 ^ 20)) :=
    mul_le_mul_of_nonneg_left hκup (by linarith)
  have p5 : m * ((1054 / 665) * 0.6931471803) ≤ m * Real.log 3 :=
    mul_le_mul_of_nonneg_left hl3lo (by linarith)
  have p6 : A * Real.log 2 ≤ A * 0.6931471808 := mul_le_mul_of_nonneg_left hl2b.le hA0
  have p7 : Xc * 0.6931471803 ≤ Xc * Real.log 2 := mul_le_mul_of_nonneg_left hl2a.le hXc0
  constructor
  · linarith
  · linarith

/-- Condition F of S7 at `m ≥ 2^19`: the Step 5–6 data are contradictory. -/
theorem numeric_F (m T τ lL e : ℝ) (hm : 2 ^ 19 ≤ m) (hT0 : 0 ≤ T)
    (hT : T * Real.log 3 ≤ lL - Real.log 2 + (m - 1) * (Real.log 3 - Real.log 2 + e))
    (hτ0 : 0 ≤ τ) (hτ : m - 3 ≤ τ + 2 * T)
    (hwit : τ * Real.log 3 < lL - Real.log 2 + (τ + T + 1) * (Real.log 3 - Real.log 2 + e))
    (hlL : lL ≤ 172 * Real.log 2 + 342 * (19 * Real.log 2 + (m / 2 ^ 19 - 1)) - Real.log 3)
    (he : e ≤ 1 / (3 * 2 ^ 20)) : False := by
  have hl2a := Real.log_two_gt_d9
  have hl2b := Real.log_two_lt_d9
  obtain ⟨hl3a, hl3b⟩ := log_three_bounds
  have hκup : Real.log 3 - Real.log 2 + e ≤
      (179 / 306) * 0.6931471808 + 1 / (3 * 2 ^ 20) := by linarith
  have hl3lo : (1054 / 665) * 0.6931471803 ≤ Real.log 3 := by linarith
  have p1 : τ * ((1054 / 665) * 0.6931471803) ≤ τ * Real.log 3 :=
    mul_le_mul_of_nonneg_left hl3lo hτ0
  have p2 : (τ + T + 1) * (Real.log 3 - Real.log 2 + e) ≤
      (τ + T + 1) * ((179 / 306) * 0.6931471808 + 1 / (3 * 2 ^ 20)) :=
    mul_le_mul_of_nonneg_left hκup (by linarith)
  have p3 : T * ((1054 / 665) * 0.6931471803) ≤ T * Real.log 3 :=
    mul_le_mul_of_nonneg_left hl3lo hT0
  have p4 : (m - 1) * (Real.log 3 - Real.log 2 + e) ≤
      (m - 1) * ((179 / 306) * 0.6931471808 + 1 / (3 * 2 ^ 20)) :=
    mul_le_mul_of_nonneg_left hκup (by linarith)
  linarith

end OddCycle

/-! ### S7-d (part 2): the three-mismatch exclusion assembled (S7; with S6, `ρ ≥ 4` given the gap)

The assembly of S7 for a primitive cycle with `q = 1`, the linear-form gap
`2^A ≤ 2^172 m^341 (2^A − 3^m)`, `m ≥ 2^19`, `L ≥ 2^20` and a rotation `1 ≤ h < m`. Let `T` be the
length of a longest agreeing run (runs are shorter than `m`, so it exists). Step 1: `T` bounds every
run, so the mismatches are spaced by `σ = m − 2(T + 1)` (`hsep_of_runs`), and the witness of the
longest run gives the run bound in log form; the pigeonhole gives `3T ≥ m − 3`, and the same witness
against the maximum `n_j` (`witness_gt`, `n_mul_pow_excess_le`) gives the climb inequality.
`D > 0` gives `m log 3 < A log 2`; the gap with `L_mul_delta_le` gives `3L ≤ 2^172 m^342`, hence
the `L`-bound with the tangent bound on `log m`; `L ≥ 2^20` gives `log(1 + 1/(3L)) ≤ 1/(3·2^20)`.
`numeric_WA` then yields conditions W and A, `three_mismatch_structure` the aligned pair with its
windows, `three_mismatch_witness` the three runs with the witness of the first, and `numeric_F`
the contradiction (`no_three_mismatch_of_gap`). With `exists_mis`, `mis_card_ne_one` and S6's
`no_two_mismatch_of_gap`, every rotation then has at least four mismatches
(`four_le_mis_card_of_gap`). -/

namespace OddCycle

variable {m : ℕ} (Γ : OddCycle m)

/-- Logarithmic form of a bound `2·3^t·2^x < L (3/2)^k (1 + ε)^k`. -/
theorem log_of_bound {t x k : ℕ}
    (hb : 2 * (3 : ℝ) ^ t * 2 ^ x < Γ.n 0 * (3 / 2 : ℝ) ^ k * (1 + Γ.q / (3 * Γ.n 0)) ^ k) :
    Real.log 2 + t * Real.log 3 + x * Real.log 2 <
      Real.log (Γ.n 0) + k * (Real.log 3 - Real.log 2 + Real.log (1 + Γ.q / (3 * Γ.n 0))) := by
  have hn0 : (0 : ℝ) < Γ.n 0 := by exact_mod_cast Γ.npos
  have hε := Γ.one_add_eps_pos
  have h3t : (3 : ℝ) ^ t ≠ 0 := by positivity
  have h2x : (2 : ℝ) ^ x ≠ 0 := by positivity
  have h23 : 2 * (3 : ℝ) ^ t ≠ 0 := by positivity
  have h32 : (3 / 2 : ℝ) ^ k ≠ 0 := by positivity
  have hεk : ((1 : ℝ) + Γ.q / (3 * Γ.n 0)) ^ k ≠ 0 := (pow_pos hε k).ne'
  have hn32 : Γ.n 0 * (3 / 2 : ℝ) ^ k ≠ 0 := mul_ne_zero hn0.ne' h32
  have hl := Real.log_lt_log (by positivity) hb
  rw [Real.log_mul h23 h2x, Real.log_mul (by norm_num : (2 : ℝ) ≠ 0) h3t, Real.log_pow,
    Real.log_pow, Real.log_mul hn32 hεk, Real.log_mul hn0.ne' h32, Real.log_pow, Real.log_pow,
    Real.log_div (by norm_num : (3 : ℝ) ≠ 0) (by norm_num : (2 : ℝ) ≠ 0)] at hl
  linarith

/-- Logarithmic form of a bound `2·3^t < L (3/2)^k (1 + ε)^k`. -/
theorem log_of_bound' {t k : ℕ}
    (hb : 2 * (3 : ℝ) ^ t < Γ.n 0 * (3 / 2 : ℝ) ^ k * (1 + Γ.q / (3 * Γ.n 0)) ^ k) :
    Real.log 2 + t * Real.log 3 <
      Real.log (Γ.n 0) + k * (Real.log 3 - Real.log 2 + Real.log (1 + Γ.q / (3 * Γ.n 0))) := by
  have hb0 : 2 * (3 : ℝ) ^ t * 2 ^ (0 : ℕ) <
      Γ.n 0 * (3 / 2 : ℝ) ^ k * (1 + Γ.q / (3 * Γ.n 0)) ^ k := by
    rw [pow_zero, mul_one]
    exact hb
  have h := Γ.log_of_bound hb0
  rw [Nat.cast_zero, zero_mul, add_zero] at h
  exact h

/-- **S7 assembled (three-mismatch exclusion).** For a primitive cycle with `q = 1`, the
linear-form gap `2^A ≤ 2^172 m^341 (2^A − 3^m)`, `m ≥ 2^19`, `L ≥ 2^20` and a rotation
`1 ≤ h < m`, the rotation does not have exactly three mismatches. -/
theorem no_three_mismatch_of_gap (hprim : ∀ i j, i < m → j < m → Γ.n i = Γ.n j → i = j)
    (hq1 : Γ.q = 1)
    (hgap : (2 : ℤ) ^ Γ.Apre m ≤ 2 ^ 172 * (m : ℤ) ^ 341 * (2 ^ Γ.Apre m - 3 ^ m))
    (hm : 2 ^ 19 ≤ m) (hL : (2 : ℤ) ^ 20 ≤ Γ.n 0) {h : ℕ} (hh1 : 1 ≤ h) (hhm : h < m) :
    (Γ.mis h).card ≠ 3 := by
  classical
  intro hs
  have hmpos := Γ.hm
  have hh : h % m ≠ 0 := by
    rw [Nat.mod_eq_of_lt hhm]
    omega
  have hapos : ∀ i, 1 ≤ Γ.a i := Γ.a_pos_of_odd (by rw [hq1]; exact odd_one)
  -- the maximum
  obtain ⟨j, hjm', hjmax⟩ :=
    Finset.exists_max_image (Finset.range m) Γ.n ⟨0, Finset.mem_range.mpr hmpos⟩
  have hjm : j < m := Finset.mem_range.mp hjm'
  have hj : ∀ i, Γ.n i ≤ Γ.n j := fun i => by
    rw [← Γ.n_mod i]
    exact hjmax (i % m) (Finset.mem_range.mpr (Nat.mod_lt _ hmpos))
  -- a longest agreeing run `T`, realised at `i`
  have hne := Γ.exists_mis hprim hh
  have hlt : ∀ i t, (∀ k, k < t → Γ.agree h (i + k)) → t < m := by
    intro i t hrun
    by_contra hge
    have hall : ∀ k, k < m → Γ.agree h (i + k) :=
      fun k hk => hrun k (lt_of_lt_of_le hk (not_lt.mp hge))
    exact Γ.z_ne_zero hprim hh i (Γ.z_eq_zero_of_agree_period hall)
  obtain ⟨P, hP⟩ : ∃ P : ℕ → Prop, ∀ t, P t ↔ ∃ i, i < m ∧ ∀ k, k < t → Γ.agree h (i + k) :=
    ⟨_, fun _ => Iff.rfl⟩
  have hP0 : P 0 := (hP 0).mpr ⟨0, hmpos, fun k hk => absurd hk (Nat.not_lt_zero k)⟩
  have hPT : P (Nat.findGreatest P m) := Nat.findGreatest_spec (Nat.zero_le m) hP0
  have hTbound : ∀ i' t, (∀ k, k < t → Γ.agree h (i' + k)) → t ≤ Nat.findGreatest P m := by
    intro i' t hrun'
    have hrun'' : ∀ k, k < t → Γ.agree h (i' % m + k) := by
      intro k hk
      rw [← Γ.agree_mod, Nat.mod_add_mod, Γ.agree_mod]
      exact hrun' k hk
    exact Nat.le_findGreatest (hlt i' t hrun').le
      ((hP t).mpr ⟨i' % m, Nat.mod_lt _ hmpos, hrun''⟩)
  generalize Nat.findGreatest P m = T at hPT hTbound
  obtain ⟨i, _, hrun⟩ := (hP T).mp hPT
  have hzT : Γ.z h (i + T) ≠ 0 := Γ.z_ne_zero hprim hh (i + T)
  -- Step 1: the spacing bound and `3T ≥ m − 3`
  have hsep := Γ.hsep_of_runs hTbound hs
  have hpig := Γ.pigeonhole hne hTbound
  rw [hs] at hpig
  -- the real quantities
  have hn0 : (0 : ℝ) < Γ.n 0 := by exact_mod_cast Γ.npos
  have hmR : (2 : ℝ) ^ 19 ≤ m := by exact_mod_cast hm
  have hm0 : (0 : ℝ) < m := by exact_mod_cast hmpos
  have hqR : (Γ.q : ℝ) = 1 := by
    rw [hq1]
    exact Int.cast_one
  have hLR : (2 : ℝ) ^ 20 ≤ Γ.n 0 := by exact_mod_cast hL
  have hε := Γ.one_add_eps_pos
  have hlog32 : 0 ≤ Real.log 3 - Real.log 2 := by
    have := Real.log_le_log (by norm_num : (0 : ℝ) < 2) (by norm_num : (2 : ℝ) ≤ 3)
    linarith
  have he0 : 0 ≤ Real.log (1 + Γ.q / (3 * Γ.n 0)) :=
    Real.log_nonneg (by linarith [Γ.eps_nonneg])
  have hκ0 : 0 ≤ Real.log 3 - Real.log 2 + Real.log (1 + Γ.q / (3 * Γ.n 0)) := by linarith
  have he : Real.log (1 + Γ.q / (3 * Γ.n 0)) ≤ 1 / (3 * 2 ^ 20) := by
    have h1 := Real.log_le_sub_one_of_pos hε
    have h2 : (Γ.q : ℝ) / (3 * Γ.n 0) ≤ 1 / (3 * 2 ^ 20) := by
      rw [hqR]
      apply one_div_le_one_div_of_le (by positivity)
      linarith
    linarith
  -- the run bound in log form (hypothesis `hT` of the numeric lemmas)
  have hb := Γ.run_bound_max hapos hj hjm (fun k hk => hrun k hk) hzT
  have hTlog := Γ.log_of_bound' hb
  rw [Nat.cast_sub (by omega : 1 ≤ m), Nat.cast_one] at hTlog
  have hT : (T : ℝ) * Real.log 3 ≤ Real.log (Γ.n 0) - Real.log 2 +
      ((m : ℝ) - 1) * (Real.log 3 - Real.log 2 + Real.log (1 + Γ.q / (3 * Γ.n 0))) := by
    linarith
  -- the longest run against the maximum (hypothesis `hjlow`)
  have hw := Γ.witness_gt T (fun k hk => hrun k hk) hzT
  have hwj : 2 * (3 : ℤ) ^ T < Γ.n j := lt_of_lt_of_le hw (max_le (hj _) (hj _))
  have hwjR : 2 * (3 : ℝ) ^ T < Γ.n j := by exact_mod_cast hwj
  have hcl := Γ.n_mul_pow_excess_le hapos j
  have hprod : 2 * (3 : ℝ) ^ T * 2 ^ Γ.excess j <
      Γ.n 0 * (3 / 2 : ℝ) ^ j * (1 + Γ.q / (3 * Γ.n 0)) ^ j :=
    lt_of_lt_of_le (mul_lt_mul_of_pos_right hwjR (by positivity)) hcl
  have hjlow := Γ.log_of_bound hprod
  -- `3T ≥ m − 3` (hypothesis `hts`)
  have hts : (m : ℝ) - 3 ≤ 3 * (T : ℝ) := by
    have h' : (m : ℝ) ≤ ((T : ℝ) + 1) * 3 := by exact_mod_cast hpig
    linarith
  -- `D > 0` (hypothesis `hA`)
  have hA : (m : ℝ) * Real.log 3 < (Γ.Apre m : ℝ) * Real.log 2 := by
    have hD := Γ.D_pos
    have hDR : (3 : ℝ) ^ m < 2 ^ Γ.Apre m := by
      have : (3 : ℤ) ^ m < 2 ^ Γ.Apre m := by linarith
      exact_mod_cast this
    have := Real.log_lt_log (by positivity) hDR
    rwa [Real.log_pow, Real.log_pow] at this
  -- the `L`-bound (hypothesis `hlL`)
  have hlL : Real.log (Γ.n 0) ≤
      172 * Real.log 2 + 342 * (19 * Real.log 2 + ((m : ℝ) / 2 ^ 19 - 1)) - Real.log 3 := by
    have hA2 : (0 : ℝ) < 2 ^ Γ.Apre m := by positivity
    have h3m : (0 : ℝ) < 3 ^ m := by positivity
    have hgapR : (2 : ℝ) ^ Γ.Apre m ≤ 2 ^ 172 * (m : ℝ) ^ 341 * (2 ^ Γ.Apre m - 3 ^ m) := by
      exact_mod_cast hgap
    have hδ : ((2 : ℝ) ^ Γ.Apre m - 3 ^ m) / 2 ^ Γ.Apre m ≤
        (Γ.Apre m : ℝ) * Real.log 2 - m * Real.log 3 := by
      have hx : (0 : ℝ) < 2 ^ Γ.Apre m / 3 ^ m := div_pos hA2 h3m
      have hlog := Real.one_sub_inv_le_log_of_pos hx
      rw [Real.log_div hA2.ne' h3m.ne', Real.log_pow, Real.log_pow, inv_div] at hlog
      have heq : ((2 : ℝ) ^ Γ.Apre m - 3 ^ m) / 2 ^ Γ.Apre m = 1 - 3 ^ m / 2 ^ Γ.Apre m := by
        rw [sub_div, div_self hA2.ne']
      rw [heq]
      exact hlog
    have hkey : (1 : ℝ) ≤
        2 ^ 172 * (m : ℝ) ^ 341 * ((Γ.Apre m : ℝ) * Real.log 2 - m * Real.log 3) := by
      have h1 : (1 : ℝ) ≤
          2 ^ 172 * (m : ℝ) ^ 341 * ((2 ^ Γ.Apre m - 3 ^ m) / 2 ^ Γ.Apre m) := by
        rw [← mul_div_assoc]
        exact (one_le_div hA2).mpr hgapR
      exact h1.trans (mul_le_mul_of_nonneg_left hδ (by positivity))
    have hLδ := Γ.L_mul_delta_le
    rw [hqR, mul_one] at hLδ
    have h3n : (0 : ℝ) ≤ 3 * (Γ.n 0 : ℝ) := by linarith
    have h3L : 3 * (Γ.n 0 : ℝ) ≤ 2 ^ 172 * (m : ℝ) ^ 342 := by
      calc 3 * (Γ.n 0 : ℝ) = 3 * (Γ.n 0 : ℝ) * 1 := by ring
        _ ≤ 3 * (Γ.n 0 : ℝ) *
            (2 ^ 172 * (m : ℝ) ^ 341 * ((Γ.Apre m : ℝ) * Real.log 2 - m * Real.log 3)) :=
          mul_le_mul_of_nonneg_left hkey h3n
        _ = 2 ^ 172 * (m : ℝ) ^ 341 *
            (3 * (Γ.n 0 : ℝ) * ((Γ.Apre m : ℝ) * Real.log 2 - m * Real.log 3)) := by ring
        _ ≤ 2 ^ 172 * (m : ℝ) ^ 341 * m := mul_le_mul_of_nonneg_left hLδ (by positivity)
        _ = 2 ^ 172 * (m : ℝ) ^ 342 := by ring
    have hlogL : Real.log 3 + Real.log (Γ.n 0) ≤ 172 * Real.log 2 + 342 * Real.log m := by
      have hm342 : (m : ℝ) ^ 342 ≠ 0 := pow_ne_zero _ hm0.ne'
      have h2172 : (2 : ℝ) ^ 172 ≠ 0 := by positivity
      have h := Real.log_le_log (by linarith) h3L
      rw [Real.log_mul (by norm_num : (3 : ℝ) ≠ 0) hn0.ne', Real.log_mul h2172 hm342,
        Real.log_pow, Real.log_pow] at h
      push_cast at h
      linarith
    have htan : Real.log m ≤ 19 * Real.log 2 + ((m : ℝ) / 2 ^ 19 - 1) := by
      have h219 : (0 : ℝ) < 2 ^ 19 := by positivity
      have hx : (0 : ℝ) < (m : ℝ) / 2 ^ 19 := div_pos hm0 h219
      have h := Real.log_le_sub_one_of_pos hx
      rw [Real.log_div hm0.ne' h219.ne', Real.log_pow] at h
      push_cast at h
      linarith
    linarith
  -- conditions W and A
  have hj0 : (0 : ℝ) ≤ j := Nat.cast_nonneg j
  have hjR : (j : ℝ) + 1 ≤ m := by
    have : j + 1 ≤ m := hjm
    exact_mod_cast this
  have hT0 : (0 : ℝ) ≤ T := Nat.cast_nonneg T
  have hXc0 : (0 : ℝ) ≤ Γ.excess j := Nat.cast_nonneg _
  have hA0 : (0 : ℝ) ≤ Γ.Apre m := Nat.cast_nonneg _
  obtain ⟨hWr, hAr⟩ := numeric_WA (m : ℝ) j T T (Γ.excess j) (Γ.Apre m) (Real.log (Γ.n 0))
    (Real.log (1 + Γ.q / (3 * Γ.n 0))) hmR hj0 hjR hT0 hT hT0 hts hXc0 hjlow hA0 hA hlL he
  have hWnat : 2 * (m - j) + 2 * (T + 1) ≤ m + 1 := by
    have h' : ((2 * (m - j) + 2 * (T + 1) : ℕ) : ℝ) ≤ ((m + 1 : ℕ) : ℝ) := by
      push_cast [Nat.cast_sub hjm.le]
      linarith
    exact_mod_cast h'
  have hσ : 2 * (m - j) ≤ m - 2 * (T + 1) + 1 := by omega
  have hσd : m - j ≤ m - 2 * (T + 1) := by omega
  have hmA : m ≤ Γ.Apre m := by
    have := Γ.excess_add_dexcess hapos hjm.le
    omega
  have hAnat : 3 * Γ.excess j < Γ.Apre m - m := by
    have h' : ((3 * Γ.excess j + 1 : ℕ) : ℝ) ≤ ((Γ.Apre m - m : ℕ) : ℝ) := by
      push_cast [Nat.cast_sub hmA]
      linarith
    have h'' : 3 * Γ.excess j + 1 ≤ Γ.Apre m - m := by exact_mod_cast h'
    omega
  -- Steps 2–4: the aligned pair and its windows
  obtain ⟨e_a, e_b, hea, heb, hea1, hea2, heb1, heb2, hdown, hup, _, hhj, halign⟩ :=
    Γ.three_mismatch_structure hprim hj hjm hh1 hhm hsep hσ hapos hAnat
  subst halign
  have hW : ∀ i, j ≤ i → i < m → i ≠ e_a + h → Γ.agree h i := by
    intro i hi1 hi2 hi3
    exact Γ.agree_of_window hsep hσd heb heb1 (by omega) (by omega) hi1 (by omega) hi3
  have hW' : ∀ k, j - h ≤ k → k < m - h → k ≠ e_a → Γ.agree h k := by
    intro k hk1 hk2 hk3
    exact Γ.agree_of_window hsep hσd hea hea1 (by omega) (by omega) hk1 (by omega) hk3
  -- Step 5: the three runs and the witness of the first
  obtain ⟨τ, τ', τ'', _, i₂, i₃, hsum, _, hr2, hr3, hwitR⟩ :=
    Γ.three_mismatch_witness hprim hapos hjm hh1 hhm hs hea1 hea2 hdown hup hhj hW hW'
  have hτ'T : τ' ≤ T := hTbound i₂ τ' hr2
  have hτ''T : τ'' ≤ T := hTbound i₃ τ'' hr3
  have hwlog := Γ.log_of_bound' hwitR
  push_cast at hwlog
  have hτ'R : (τ' : ℝ) ≤ T := by exact_mod_cast hτ'T
  have hwit : (τ : ℝ) * Real.log 3 < Real.log (Γ.n 0) - Real.log 2 +
      ((τ : ℝ) + T + 1) * (Real.log 3 - Real.log 2 + Real.log (1 + Γ.q / (3 * Γ.n 0))) := by
    have := mul_le_mul_of_nonneg_right hτ'R hκ0
    linarith
  have hmτ : m ≤ τ + 2 * T + 3 := by omega
  have hτR : (m : ℝ) - 3 ≤ (τ : ℝ) + 2 * T := by
    have : (m : ℝ) ≤ (τ : ℝ) + 2 * T + 3 := by exact_mod_cast hmτ
    linarith
  -- Step 6
  exact numeric_F (m : ℝ) T τ (Real.log (Γ.n 0)) (Real.log (1 + Γ.q / (3 * Γ.n 0))) hmR hT0 hT
    (Nat.cast_nonneg τ) hτR hwit hlL he

/-- **`ρ ≥ 4` given the gap (S6 and S7 assembled).** Under the hypotheses of
`no_three_mismatch_of_gap`, with the height exponent attained (`hB`), every rotation `1 ≤ h < m`
has at least four mismatches. -/
theorem four_le_mis_card_of_gap (hprim : ∀ i j, i < m → j < m → Γ.n i = Γ.n j → i = j)
    (hq1 : Γ.q = 1)
    (hgap : (2 : ℤ) ^ Γ.Apre m ≤ 2 ^ 172 * (m : ℤ) ^ 341 * (2 ^ Γ.Apre m - 3 ^ m))
    (hB : ∃ i, Γ.h i = Γ.B) (hm : 2 ^ 19 ≤ m) (hL : (2 : ℤ) ^ 20 ≤ Γ.n 0) {h : ℕ} (hh1 : 1 ≤ h)
    (hhm : h < m) : 4 ≤ (Γ.mis h).card := by
  have hh : h % m ≠ 0 := by
    rw [Nat.mod_eq_of_lt hhm]
    omega
  have h0 : 0 < (Γ.mis h).card := by
    obtain ⟨p, hp⟩ := Γ.exists_mis hprim hh
    apply Finset.card_pos.mpr
    refine ⟨p % m, ?_⟩
    unfold mis
    rw [Finset.mem_filter, Finset.mem_range, Γ.agree_mod]
    exact ⟨Nat.mod_lt _ Γ.hm, hp⟩
  have h1 := Γ.mis_card_ne_one h
  have h2 := Γ.no_two_mismatch_of_gap hprim hq1 hgap hB (le_trans (by norm_num) hm) hL hh
  have h3 := Γ.no_three_mismatch_of_gap hprim hq1 hgap hm hL hh1 hhm
  omega

end OddCycle

/-! ### S10-a: the four-mismatch dichotomy and the cyclic alternation of the sign changes

For a rotation `h` of a cycle, the mismatches split into the `+→−` changes `D`, the `−→+` changes
`U` and the non-changes `N`: `|mis h| = |D| + |U| + |N|` (`mis_card_partition`), with `|D| = |U|`
(`card_down_eq_card_up`). Between two `+→−` changes there is a `−→+` change and conversely
(`up_between_downs`, `down_between_ups`: the sign of `z` changes only at a change), also across the
period (`down_add_period`, `up_add_period`). With exactly four mismatches (and a primitive cycle, so
that a change exists): either one change of each kind and two non-changes, or two of each kind and
no non-change (`four_mismatch_dichotomy`). In the second case the four mismatches alternate in
cyclic order — in increasing order they read `down, up, down, up` or `up, down, up, down`
(`four_mismatch_alternation`, via `alternation_core`). The side lane's single-drop model is the
first case; the alternation is the geometry of the second. -/

namespace OddCycle

variable {m : ℕ} (Γ : OddCycle m)

theorem mis_lt_m {h i : ℕ} (hi : i ∈ Γ.mis h) : i < m := by
  unfold mis at hi
  rw [Finset.mem_filter, Finset.mem_range] at hi
  exact hi.1

theorem down_add_period (h i : ℕ) : Γ.down h (i + m) ↔ Γ.down h i := by
  have h1 : Γ.z h (i + m) = Γ.z h i := Γ.z_per h i
  have h2 : Γ.z h (i + m + 1) = Γ.z h (i + 1) := by
    rw [Nat.add_right_comm i m 1]
    exact Γ.z_per h (i + 1)
  show (0 < Γ.z h (i + m) ∧ ¬ 0 < Γ.z h (i + m + 1)) ↔ (0 < Γ.z h i ∧ ¬ 0 < Γ.z h (i + 1))
  rw [h1, h2]

theorem up_add_period (h i : ℕ) : Γ.up h (i + m) ↔ Γ.up h i := by
  have h1 : Γ.z h (i + m) = Γ.z h i := Γ.z_per h i
  have h2 : Γ.z h (i + m + 1) = Γ.z h (i + 1) := by
    rw [Nat.add_right_comm i m 1]
    exact Γ.z_per h (i + 1)
  show (¬ 0 < Γ.z h (i + m) ∧ 0 < Γ.z h (i + m + 1)) ↔ (¬ 0 < Γ.z h i ∧ 0 < Γ.z h (i + 1))
  rw [h1, h2]

/-- Between two `+→−` changes `e₁ < e₂` there is a `−→+` change. -/
theorem up_between_downs {h e₁ e₂ : ℕ} (h₁ : Γ.down h e₁) (h₂ : Γ.down h e₂) (hlt : e₁ < e₂) :
    ∃ u, e₁ < u ∧ u < e₂ ∧ Γ.up h u := by
  have hd : e₁ + 1 + (e₂ - e₁ - 1) = e₂ := by omega
  have hb : 0 < Γ.z h (e₁ + 1 + (e₂ - e₁ - 1)) := by
    rw [hd]
    exact h₂.1
  obtain ⟨u, hu1, hu2, hu⟩ := Γ.exists_up h₁.2 hb
  exact ⟨u, by omega, by omega, hu⟩

/-- Between two `−→+` changes `e₁ < e₂` there is a `+→−` change. -/
theorem down_between_ups {h e₁ e₂ : ℕ} (h₁ : Γ.up h e₁) (h₂ : Γ.up h e₂) (hlt : e₁ < e₂) :
    ∃ d, e₁ < d ∧ d < e₂ ∧ Γ.down h d := by
  have hd : e₁ + 1 + (e₂ - e₁ - 1) = e₂ := by omega
  have hb : ¬ 0 < Γ.z h (e₁ + 1 + (e₂ - e₁ - 1)) := by
    rw [hd]
    exact h₂.1
  obtain ⟨d, hd1, hd2, hdown⟩ := Γ.exists_down h₁.2 hb
  exact ⟨d, by omega, by omega, hdown⟩

/-- The mismatches split into the `+→−` changes, the `−→+` changes and the non-changes. -/
theorem mis_card_partition (h : ℕ) :
    (Γ.mis h).card = ((Finset.range m).filter (Γ.down h)).card +
      ((Finset.range m).filter (Γ.up h)).card +
      ((Γ.mis h).filter (fun i => ¬ Γ.down h i ∧ ¬ Γ.up h i)).card := by
  have h1 := Finset.card_filter_add_card_filter_not (s := Γ.mis h) (Γ.down h)
  have h2 := Finset.card_filter_add_card_filter_not
    (s := (Γ.mis h).filter (fun i => ¬ Γ.down h i)) (Γ.up h)
  have hD : (Γ.mis h).filter (Γ.down h) = (Finset.range m).filter (Γ.down h) := by
    ext i
    rw [Finset.mem_filter, Finset.mem_filter, Finset.mem_range]
    constructor
    · rintro ⟨hi, hd⟩
      exact ⟨Γ.mis_lt_m hi, hd⟩
    · rintro ⟨hi, hd⟩
      exact ⟨Γ.down_mem_mis hi hd, hd⟩
  have hU : ((Γ.mis h).filter (fun i => ¬ Γ.down h i)).filter (Γ.up h) =
      (Finset.range m).filter (Γ.up h) := by
    ext i
    rw [Finset.mem_filter, Finset.mem_filter, Finset.mem_filter, Finset.mem_range]
    constructor
    · rintro ⟨⟨hi, _⟩, hu⟩
      exact ⟨Γ.mis_lt_m hi, hu⟩
    · rintro ⟨hi, hu⟩
      exact ⟨⟨Γ.up_mem_mis hi hu, fun hd => hd.2 hu.2⟩, hu⟩
  have hN : ((Γ.mis h).filter (fun i => ¬ Γ.down h i)).filter (fun i => ¬ Γ.up h i) =
      (Γ.mis h).filter (fun i => ¬ Γ.down h i ∧ ¬ Γ.up h i) := by
    rw [Finset.filter_filter]
  rw [hD] at h1
  rw [hU, hN] at h2
  omega

/-- **The four-mismatch dichotomy.** With exactly four mismatches: one change of each kind and two
non-changes, or two changes of each kind and no non-change. -/
theorem four_mismatch_dichotomy (hprim : ∀ i j, i < m → j < m → Γ.n i = Γ.n j → i = j) {j : ℕ}
    (hj : ∀ i, Γ.n i ≤ Γ.n j) (hjm : j < m) {h : ℕ} (hh : h % m ≠ 0)
    (hs : (Γ.mis h).card = 4) :
    (((Finset.range m).filter (Γ.down h)).card = 1 ∧
        ((Finset.range m).filter (Γ.up h)).card = 1 ∧
        ((Γ.mis h).filter (fun i => ¬ Γ.down h i ∧ ¬ Γ.up h i)).card = 2) ∨
      (((Finset.range m).filter (Γ.down h)).card = 2 ∧
        ((Finset.range m).filter (Γ.up h)).card = 2 ∧
        ((Γ.mis h).filter (fun i => ¬ Γ.down h i ∧ ¬ Γ.up h i)).card = 0) := by
  have hpart := Γ.mis_card_partition h
  have hDU := Γ.card_down_eq_card_up h
  have hDpos : 0 < ((Finset.range m).filter (Γ.down h)).card := by
    obtain ⟨i, _, _, hdown⟩ := Γ.exists_down_window hprim hj hjm hh
    apply Finset.card_pos.mpr
    refine ⟨i % m, ?_⟩
    rw [Finset.mem_filter, Finset.mem_range]
    exact ⟨Nat.mod_lt _ Γ.hm, (Γ.down_mod h i).mpr hdown⟩
  omega

/-- Two `+→−` changes `x < y` and two `−→+` changes `p < q`, the latter being all the `−→+` changes
below `m`: in increasing order the four positions read `x, p, y, q` or `p, x, q, y`. -/
theorem alternation_core {h x y p q : ℕ} (hx : x < m ∧ Γ.down h x) (hy : y < m ∧ Γ.down h y)
    (hxy : x < y) (hp : p < m ∧ Γ.up h p) (hq : q < m ∧ Γ.up h q) (hpq : p < q)
    (hU : ∀ i, i < m → Γ.up h i → i = p ∨ i = q) :
    (x < p ∧ p < y ∧ y < q) ∨ (p < x ∧ x < q ∧ q < y) := by
  have hm := Γ.hm
  have hpx : p ≠ x := fun e => by
    rw [e] at hp
    exact hp.2.1 hx.2.1
  have hpy : p ≠ y := fun e => by
    rw [e] at hp
    exact hp.2.1 hy.2.1
  have hqx : q ≠ x := fun e => by
    rw [e] at hq
    exact hq.2.1 hx.2.1
  have hqy : q ≠ y := fun e => by
    rw [e] at hq
    exact hq.2.1 hy.2.1
  obtain ⟨u, hu1, hu2, hu⟩ := Γ.up_between_downs hx.2 hy.2 hxy
  have hu' := hU u (by omega) hu
  have hxm : Γ.down h (x + m) := (Γ.down_add_period h x).mpr hx.2
  obtain ⟨v, hv1, hv2, hv⟩ := Γ.up_between_downs hy.2 hxm (by omega)
  have hvm : Γ.up h (v % m) := (Γ.up_mod h v).mpr hv
  have hv' := hU (v % m) (Nat.mod_lt _ hm) hvm
  have hvres : (v < m ∧ v % m = v) ∨ (m ≤ v ∧ v % m = v - m) := by
    rcases Nat.lt_or_ge v m with hlt | hge
    · exact Or.inl ⟨hlt, Nat.mod_eq_of_lt hlt⟩
    · right
      refine ⟨hge, ?_⟩
      rw [Nat.mod_eq_sub_mod hge, Nat.mod_eq_of_lt (by omega)]
  omega

/-- A four-element set of naturals in increasing order has cardinality four. -/
theorem card_four {a b c d : ℕ} (hab : a < b) (hbc : b < c) (hcd : c < d) :
    ({a, b, c, d} : Finset ℕ).card = 4 := by
  have hc : c ∉ ({d} : Finset ℕ) := by
    rw [Finset.mem_singleton]
    omega
  have hb : b ∉ ({c, d} : Finset ℕ) := by
    rw [Finset.mem_insert, Finset.mem_singleton]
    omega
  have ha : a ∉ ({b, c, d} : Finset ℕ) := by
    rw [Finset.mem_insert, Finset.mem_insert, Finset.mem_singleton]
    omega
  have e1 := Finset.card_insert_of_notMem ha
  have e2 := Finset.card_insert_of_notMem hb
  have e3 := Finset.card_insert_of_notMem hc
  have e4 : ({d} : Finset ℕ).card = 1 := Finset.card_singleton d
  omega

/-- **Cyclic alternation in the two-and-two case.** With exactly four mismatches and two `+→−`
changes, the mismatch set is `{a, b, c, d}` with `a < b < c < d < m`, alternating:
`down, up, down, up` or `up, down, up, down`. -/
theorem four_mismatch_alternation {h : ℕ} (hs : (Γ.mis h).card = 4)
    (hD2 : ((Finset.range m).filter (Γ.down h)).card = 2) :
    ∃ a b c d, a < b ∧ b < c ∧ c < d ∧ d < m ∧ Γ.mis h = {a, b, c, d} ∧
      ((Γ.down h a ∧ Γ.up h b ∧ Γ.down h c ∧ Γ.up h d) ∨
        (Γ.up h a ∧ Γ.down h b ∧ Γ.up h c ∧ Γ.down h d)) := by
  have hpart := Γ.mis_card_partition h
  have hDU := Γ.card_down_eq_card_up h
  have hU2 : ((Finset.range m).filter (Γ.up h)).card = 2 := by omega
  obtain ⟨x₀, y₀, hxy₀, hDeq⟩ := Finset.card_eq_two.mp hD2
  obtain ⟨p₀, q₀, hpq₀, hUeq⟩ := Finset.card_eq_two.mp hU2
  have hUmem : ∀ i, i < m → Γ.up h i → i = p₀ ∨ i = q₀ := by
    intro i hi hu
    have : i ∈ (Finset.range m).filter (Γ.up h) := by
      rw [Finset.mem_filter, Finset.mem_range]
      exact ⟨hi, hu⟩
    rw [hUeq, Finset.mem_insert, Finset.mem_singleton] at this
    exact this
  have hx₀ : x₀ < m ∧ Γ.down h x₀ := by
    have : x₀ ∈ (Finset.range m).filter (Γ.down h) := by
      rw [hDeq]
      exact Finset.mem_insert_self _ _
    rwa [Finset.mem_filter, Finset.mem_range] at this
  have hy₀ : y₀ < m ∧ Γ.down h y₀ := by
    have : y₀ ∈ (Finset.range m).filter (Γ.down h) := by
      rw [hDeq]
      exact Finset.mem_insert_of_mem (Finset.mem_singleton_self _)
    rwa [Finset.mem_filter, Finset.mem_range] at this
  have hp₀ : p₀ < m ∧ Γ.up h p₀ := by
    have : p₀ ∈ (Finset.range m).filter (Γ.up h) := by
      rw [hUeq]
      exact Finset.mem_insert_self _ _
    rwa [Finset.mem_filter, Finset.mem_range] at this
  have hq₀ : q₀ < m ∧ Γ.up h q₀ := by
    have : q₀ ∈ (Finset.range m).filter (Γ.up h) := by
      rw [hUeq]
      exact Finset.mem_insert_of_mem (Finset.mem_singleton_self _)
    rwa [Finset.mem_filter, Finset.mem_range] at this
  -- sort the two pairs
  obtain ⟨x, y, hx, hy, hxy⟩ : ∃ x y, (x < m ∧ Γ.down h x) ∧ (y < m ∧ Γ.down h y) ∧ x < y := by
    rcases Nat.lt_or_gt_of_ne hxy₀ with hlt | hlt
    · exact ⟨x₀, y₀, hx₀, hy₀, hlt⟩
    · exact ⟨y₀, x₀, hy₀, hx₀, hlt⟩
  obtain ⟨p, q, hp, hq, hpq, hUmem'⟩ : ∃ p q, (p < m ∧ Γ.up h p) ∧ (q < m ∧ Γ.up h q) ∧
      p < q ∧ ∀ i, i < m → Γ.up h i → i = p ∨ i = q := by
    rcases Nat.lt_or_gt_of_ne hpq₀ with hlt | hlt
    · exact ⟨p₀, q₀, hp₀, hq₀, hlt, hUmem⟩
    · exact ⟨q₀, p₀, hq₀, hp₀, hlt, fun i hi hu => (hUmem i hi hu).symm⟩
  -- the set equality from four distinct members and the cardinality
  have hset : ∀ a b c d, a < b → b < c → c < d → a ∈ Γ.mis h → b ∈ Γ.mis h → c ∈ Γ.mis h →
      d ∈ Γ.mis h → Γ.mis h = {a, b, c, d} := by
    intro a b c d hab hbc hcd ha hb hc hd
    symm
    apply Finset.eq_of_subset_of_card_le
    · intro e he
      rw [Finset.mem_insert, Finset.mem_insert, Finset.mem_insert, Finset.mem_singleton] at he
      rcases he with rfl | rfl | rfl | rfl
      · exact ha
      · exact hb
      · exact hc
      · exact hd
    · have := card_four hab hbc hcd
      omega
  rcases Γ.alternation_core hx hy hxy hp hq hpq hUmem' with ⟨h1, h2, h3⟩ | ⟨h1, h2, h3⟩
  · exact ⟨x, p, y, q, h1, h2, h3, hq.1,
      hset x p y q h1 h2 h3 (Γ.down_mem_mis hx.1 hx.2) (Γ.up_mem_mis hp.1 hp.2)
        (Γ.down_mem_mis hy.1 hy.2) (Γ.up_mem_mis hq.1 hq.2),
      Or.inl ⟨hx.2, hp.2, hy.2, hq.2⟩⟩
  · exact ⟨p, x, q, y, h1, h2, h3, hy.1,
      hset p x q y h1 h2 h3 (Γ.up_mem_mis hp.1 hp.2) (Γ.down_mem_mis hx.1 hx.2)
        (Γ.up_mem_mis hq.1 hq.2) (Γ.down_mem_mis hy.1 hy.2),
      Or.inr ⟨hp.2, hx.2, hq.2, hy.2⟩⟩

end OddCycle

/-! ### S9-a: the global-drift ceiling

The exact prefix identity `2^{A_k} n_k = 3^k n_0 + q C_k` and the closing identity
`(2^A − 3^m) n_0 = q C_m` give, for `k ≤ m`, the ceiling `n_k 2^{A_k} 3^m ≤ n_0 3^k 2^A`
(`global_drift`), because the intercepts satisfy `3^{m−k} C_k ≤ C_m` (`Cpre_mul_pow_le`: `C_k/3^k`
is nondecreasing). In the language of S9 §1, with the drift `δ = A log 2 − m log 3 = log(2^A/3^m)`:
`log n_k + X_k log 2 ≤ log L + k log(3/2) + δ` (`global_drift_log`, natural logarithms), with no
hypothesis on `L/q`. The per-step ceiling `n_mul_pow_excess_le` has `k log(1 + q/(3L))` in place of
`δ`; both hold, so their minimum does. For the height exponents, `h_k log 2 ≤ k log(3/2) + δ`
(`h_le_drift`) and, with the height attained, `B log 2 ≤ (m − 1) log(3/2) + δ` (`B_le_drift`): S9's
elimination of the height through the drift. -/

namespace OddCycle

variable {m : ℕ} (Γ : OddCycle m)

/-- `3^j C_k ≤ C_{k+j}`: the intercepts grow at least by the factor `3` per step. -/
theorem Cpre_mul_pow_le (k j : ℕ) : 3 ^ j * Γ.Cpre k ≤ Γ.Cpre (k + j) := by
  induction j with
  | zero => simp
  | succ j ih =>
    rw [← Nat.add_assoc, Γ.Cpre_succ, pow_succ]
    have h2 : (0 : ℤ) ≤ 2 ^ Γ.Apre (k + j) := by positivity
    linarith

/-- **The global-drift ceiling** (S9 §1, integer form): for `k ≤ m`,
`n_k 2^{A_k} 3^m ≤ n_0 3^k 2^A`. No hypothesis on `L/q`. -/
theorem global_drift {k : ℕ} (hk : k ≤ m) :
    Γ.n k * 2 ^ Γ.Apre k * 3 ^ m ≤ Γ.n 0 * 3 ^ k * 2 ^ Γ.Apre m := by
  have hpre := Γ.prefix_identity k
  have hcyc := Γ.cycle_identity
  have hC := Γ.Cpre_mul_pow_le k (m - k)
  rw [Nat.add_sub_cancel' hk] at hC
  have hq := Γ.hq
  have h3k : (0 : ℤ) < 3 ^ k := by positivity
  have hqC : Γ.q * (3 ^ (m - k) * Γ.Cpre k) ≤ Γ.q * Γ.Cpre m :=
    mul_le_mul_of_nonneg_left hC hq.le
  have h3m : (3 : ℤ) ^ m = 3 ^ k * 3 ^ (m - k) := by
    rw [← pow_add, Nat.add_sub_cancel' hk]
  calc Γ.n k * 2 ^ Γ.Apre k * 3 ^ m = (2 ^ Γ.Apre k * Γ.n k) * 3 ^ m := by ring
    _ = (3 ^ k * Γ.n 0 + Γ.q * Γ.Cpre k) * 3 ^ m := by rw [hpre]
    _ = 3 ^ k * (3 ^ m * Γ.n 0) + 3 ^ k * (Γ.q * (3 ^ (m - k) * Γ.Cpre k)) := by
        rw [h3m]
        ring
    _ ≤ 3 ^ k * (3 ^ m * Γ.n 0) + 3 ^ k * (Γ.q * Γ.Cpre m) := by
        linarith [mul_le_mul_of_nonneg_left hqC h3k.le]
    _ = 3 ^ k * (3 ^ m * Γ.n 0 + ((2 : ℤ) ^ Γ.Apre m - 3 ^ m) * Γ.n 0) := by
        rw [hcyc]
        ring
    _ = Γ.n 0 * 3 ^ k * 2 ^ Γ.Apre m := by ring

/-- `A_k = X_k + k` for letters `≥ 1`. -/
theorem Apre_eq_excess_add (hapos : ∀ i, 1 ≤ Γ.a i) (k : ℕ) : Γ.Apre k = Γ.excess k + k := by
  induction k with
  | zero => simp [Apre, excess]
  | succ k ih =>
    rw [Γ.Apre_succ, Γ.excess_succ, ih]
    have := hapos k
    omega

/-- The global-drift ceiling in the form of S9 §1 (natural logarithms): for `k ≤ m`,
`log n_k + X_k log 2 ≤ log L + k log(3/2) + δ`, `δ = A log 2 − m log 3`. -/
theorem global_drift_log (hapos : ∀ i, 1 ≤ Γ.a i) {k : ℕ} (hk : k ≤ m) :
    Real.log (Γ.n k) + Γ.excess k * Real.log 2 ≤
      Real.log (Γ.n 0) + k * (Real.log 3 - Real.log 2) +
        ((Γ.Apre m : ℝ) * Real.log 2 - m * Real.log 3) := by
  have hnk : (0 : ℝ) < Γ.n k := by exact_mod_cast lt_of_lt_of_le Γ.npos (Γ.nmin k)
  have hn0 : (0 : ℝ) < Γ.n 0 := by exact_mod_cast Γ.npos
  have hAk := Γ.Apre_eq_excess_add hapos k
  have hR : (Γ.n k : ℝ) * 2 ^ Γ.Apre k * 3 ^ m ≤ Γ.n 0 * 3 ^ k * 2 ^ Γ.Apre m := by
    exact_mod_cast Γ.global_drift hk
  have h2k : (2 : ℝ) ^ Γ.Apre k ≠ 0 := by positivity
  have h3m : (3 : ℝ) ^ m ≠ 0 := by positivity
  have h3k : (3 : ℝ) ^ k ≠ 0 := by positivity
  have h2A : (2 : ℝ) ^ Γ.Apre m ≠ 0 := by positivity
  have hnk2 : (Γ.n k : ℝ) * 2 ^ Γ.Apre k ≠ 0 := mul_ne_zero hnk.ne' h2k
  have hn03 : (Γ.n 0 : ℝ) * 3 ^ k ≠ 0 := mul_ne_zero hn0.ne' h3k
  have hpos : (0 : ℝ) < Γ.n k * 2 ^ Γ.Apre k * 3 ^ m :=
    mul_pos (mul_pos hnk (by positivity)) (by positivity)
  have hl := Real.log_le_log hpos hR
  rw [Real.log_mul hnk2 h3m, Real.log_mul hnk.ne' h2k, Real.log_mul hn03 h2A,
    Real.log_mul hn0.ne' h3k, Real.log_pow, Real.log_pow, Real.log_pow, Real.log_pow, hAk] at hl
  push_cast at hl
  linarith

/-- The height exponents under the drift ceiling: `h_k log 2 ≤ k log(3/2) + δ` for `k ≤ m`. -/
theorem h_le_drift (hapos : ∀ i, 1 ≤ Γ.a i) {k : ℕ} (hk : k ≤ m) :
    (Γ.h k : ℝ) * Real.log 2 ≤ k * (Real.log 3 - Real.log 2) +
      ((Γ.Apre m : ℝ) * Real.log 2 - m * Real.log 3) := by
  have hn0 : (0 : ℝ) < Γ.n 0 := by exact_mod_cast Γ.npos
  have hlo : (2 : ℝ) ^ Γ.h k * Γ.n 0 ≤ Γ.n k := by exact_mod_cast Γ.hlo k
  have h2h : (2 : ℝ) ^ Γ.h k ≠ 0 := by positivity
  have hl := Real.log_le_log (mul_pos (by positivity) hn0) hlo
  rw [Real.log_mul h2h hn0.ne', Real.log_pow] at hl
  have hlog2 : 0 < Real.log 2 := Real.log_pos (by norm_num)
  have hX : (0 : ℝ) ≤ Γ.excess k * Real.log 2 := mul_nonneg (Nat.cast_nonneg _) hlog2.le
  have hg := Γ.global_drift_log hapos hk
  linarith

/-- S9's elimination of the height: with the height attained, `B log 2 ≤ (m − 1) log(3/2) + δ`. -/
theorem B_le_drift (hapos : ∀ i, 1 ≤ Γ.a i) (hB : ∃ i, Γ.h i = Γ.B) :
    (Γ.B : ℝ) * Real.log 2 ≤ ((m : ℝ) - 1) * (Real.log 3 - Real.log 2) +
      ((Γ.Apre m : ℝ) * Real.log 2 - m * Real.log 3) := by
  obtain ⟨i, hi⟩ := hB
  have hm := Γ.hm
  have hj : i % m ≤ m - 1 := by
    have := Nat.mod_lt i hm
    omega
  have hji : Γ.h (i % m) = Γ.B := by rw [Γ.h_mod, hi]
  have hd := Γ.h_le_drift hapos (Nat.mod_lt i hm).le
  rw [hji] at hd
  have hjm : ((i % m : ℕ) : ℝ) ≤ (m : ℝ) - 1 := by
    have h3 : ((i % m : ℕ) : ℝ) ≤ ((m - 1 : ℕ) : ℝ) := by exact_mod_cast hj
    rw [Nat.cast_sub (by omega), Nat.cast_one] at h3
    exact h3
  have hlog32 : 0 ≤ Real.log 3 - Real.log 2 := by
    have := Real.log_le_log (by norm_num : (0 : ℝ) < 2) (by norm_num : (2 : ℝ) ≤ 3)
    linarith
  have := mul_le_mul_of_nonneg_right hjm hlog32
  linarith

end OddCycle

/-! ### S9-b: the two-mismatch denominator law at general `q` (S9 §2 (i))

S6's chain with the global-drift ceiling, for an arbitrary `OddCycle` (any `q > 0`, letters `≥ 1`;
for odd `q` the letters are automatically `≥ 1`). A rotation with exactly two mismatches has a
longest agreeing run `T` with `m ≤ 2(T + 1)` (`exists_longest_run`, `pigeonhole`); its witness
exceeds `2·3^T` and is at most the maximum `n_j`, which the drift ceiling bounds through
`log n_j ≤ log L + (m − 1) log(3/2) + δ`; and `3 L D ≤ m q 2^A` (`three_L_D_le`, S7's (F4), from
`L_mul_delta_le` and `D/2^A ≤ δ`). Hence
`log 2 + T log 3 < log q + (m − 1) log(3/2) + δ + λ`, with `δ = A log 2 − m log 3` and
`λ = log m + A log 2 − log 3 − log D`, `D = 2^A − 3^m` (`two_mismatch_denominator_law`); with
`T ≥ ⌈(m − 2)/2⌉ = (m − 1)/2` this is S9 (i) (`two_mismatch_denominator_law'`), and
`two_mismatch_denominator_law_odd` is the `3x+q` reading for odd `q`. Dividing by `log 2` gives S9's
`log₂ den(w) > Φ₂(m) − δ(w) − λ(w)` once `q = den(w)`; the identification of a reduced cycle's `q`
with `den(w)` is the programme's (C008/C009) and is not re-proved here. -/

namespace OddCycle

variable {m : ℕ} (Γ : OddCycle m)

/-- A longest agreeing run of a rotation with a mismatch: realised at some `i`, and bounding every
run. -/
theorem exists_longest_run (hprim : ∀ i j, i < m → j < m → Γ.n i = Γ.n j → i = j) {h : ℕ}
    (hh : h % m ≠ 0) :
    ∃ i T, (∀ k, k < T → Γ.agree h (i + k)) ∧
      ∀ i' t, (∀ k, k < t → Γ.agree h (i' + k)) → t ≤ T := by
  classical
  have hmpos := Γ.hm
  have hlt : ∀ i t, (∀ k, k < t → Γ.agree h (i + k)) → t < m := by
    intro i t hrun
    by_contra hge
    have hall : ∀ k, k < m → Γ.agree h (i + k) :=
      fun k hk => hrun k (lt_of_lt_of_le hk (not_lt.mp hge))
    exact Γ.z_ne_zero hprim hh i (Γ.z_eq_zero_of_agree_period hall)
  obtain ⟨P, hP⟩ : ∃ P : ℕ → Prop, ∀ t, P t ↔ ∃ i, i < m ∧ ∀ k, k < t → Γ.agree h (i + k) :=
    ⟨_, fun _ => Iff.rfl⟩
  have hP0 : P 0 := (hP 0).mpr ⟨0, hmpos, fun k hk => absurd hk (Nat.not_lt_zero k)⟩
  have hPT : P (Nat.findGreatest P m) := Nat.findGreatest_spec (Nat.zero_le m) hP0
  obtain ⟨i, _, hrun⟩ := (hP _).mp hPT
  refine ⟨i, Nat.findGreatest P m, hrun, ?_⟩
  intro i' t hrun'
  have hrun'' : ∀ k, k < t → Γ.agree h (i' % m + k) := by
    intro k hk
    rw [← Γ.agree_mod, Nat.mod_add_mod, Γ.agree_mod]
    exact hrun' k hk
  exact Nat.le_findGreatest (hlt i' t hrun').le
    ((hP t).mpr ⟨i' % m, Nat.mod_lt _ hmpos, hrun''⟩)

/-- `D/2^A ≤ δ = A log 2 − m log 3` (the `OddCycle` form of `OrdCycle.delta_ge_gap`). -/
theorem D_div_le_delta :
    ((2 : ℝ) ^ Γ.Apre m - 3 ^ m) / 2 ^ Γ.Apre m ≤
      (Γ.Apre m : ℝ) * Real.log 2 - m * Real.log 3 := by
  have hA2 : (0 : ℝ) < 2 ^ Γ.Apre m := by positivity
  have h3m : (0 : ℝ) < 3 ^ m := by positivity
  have hx : (0 : ℝ) < 2 ^ Γ.Apre m / 3 ^ m := div_pos hA2 h3m
  have hlog := Real.one_sub_inv_le_log_of_pos hx
  rw [Real.log_div hA2.ne' h3m.ne', Real.log_pow, Real.log_pow, inv_div] at hlog
  have heq : ((2 : ℝ) ^ Γ.Apre m - 3 ^ m) / 2 ^ Γ.Apre m = 1 - 3 ^ m / 2 ^ Γ.Apre m := by
    rw [sub_div, div_self hA2.ne']
  rw [heq]
  exact hlog

/-- S7's (F4): `3 L D ≤ m q 2^A`, i.e. `L ≤ m q 2^A/(3D)`. -/
theorem three_L_D_le :
    3 * (Γ.n 0 : ℝ) * ((2 : ℝ) ^ Γ.Apre m - 3 ^ m) ≤ m * Γ.q * 2 ^ Γ.Apre m := by
  have hn0 : (0 : ℝ) < Γ.n 0 := by exact_mod_cast Γ.npos
  have hA2 : (0 : ℝ) < 2 ^ Γ.Apre m := by positivity
  have hδ := Γ.D_div_le_delta
  have hL := Γ.L_mul_delta_le
  have h3n : (0 : ℝ) ≤ 3 * (Γ.n 0 : ℝ) := by linarith
  have h1 : 3 * (Γ.n 0 : ℝ) * (((2 : ℝ) ^ Γ.Apre m - 3 ^ m) / 2 ^ Γ.Apre m) ≤ m * Γ.q :=
    le_trans (mul_le_mul_of_nonneg_left hδ h3n) hL
  have h2 : 3 * (Γ.n 0 : ℝ) * (((2 : ℝ) ^ Γ.Apre m - 3 ^ m) / 2 ^ Γ.Apre m) * 2 ^ Γ.Apre m =
      3 * (Γ.n 0 : ℝ) * ((2 : ℝ) ^ Γ.Apre m - 3 ^ m) := by
    rw [mul_assoc, div_mul_cancel₀ _ hA2.ne']
  calc 3 * (Γ.n 0 : ℝ) * ((2 : ℝ) ^ Γ.Apre m - 3 ^ m)
      = 3 * (Γ.n 0 : ℝ) * (((2 : ℝ) ^ Γ.Apre m - 3 ^ m) / 2 ^ Γ.Apre m) * 2 ^ Γ.Apre m := h2.symm
    _ ≤ m * Γ.q * 2 ^ Γ.Apre m := mul_le_mul_of_nonneg_right h1 hA2.le

/-- **S9 (i), the two-mismatch denominator law** (natural logarithms). For a primitive cycle with
letters `≥ 1` and a rotation with exactly two mismatches, some run `T` with `m ≤ 2(T + 1)` has
`log 2 + T log 3 < log q + (m − 1) log(3/2) + δ + λ`, where `δ = A log 2 − m log 3` and
`λ = log m + A log 2 − log 3 − log D`, `D = 2^A − 3^m`. -/
theorem two_mismatch_denominator_law (hprim : ∀ i j, i < m → j < m → Γ.n i = Γ.n j → i = j)
    (hapos : ∀ i, 1 ≤ Γ.a i) {h : ℕ} (hh : h % m ≠ 0) (hs : (Γ.mis h).card = 2) :
    ∃ T, m ≤ 2 * (T + 1) ∧
      Real.log 2 + T * Real.log 3 < Real.log (Γ.q) + ((m : ℝ) - 1) * (Real.log 3 - Real.log 2) +
        ((Γ.Apre m : ℝ) * Real.log 2 - m * Real.log 3) +
        (Real.log m + (Γ.Apre m : ℝ) * Real.log 2 - Real.log 3 -
          Real.log ((2 : ℝ) ^ Γ.Apre m - 3 ^ m)) := by
  have hmpos := Γ.hm
  obtain ⟨i, T, hrun, hTbound⟩ := Γ.exists_longest_run hprim hh
  have hne := Γ.exists_mis hprim hh
  have hpig := Γ.pigeonhole hne hTbound
  rw [hs] at hpig
  refine ⟨T, by omega, ?_⟩
  -- the maximum
  obtain ⟨j, hjm', hjmax⟩ :=
    Finset.exists_max_image (Finset.range m) Γ.n ⟨0, Finset.mem_range.mpr hmpos⟩
  have hjm : j < m := Finset.mem_range.mp hjm'
  have hj : ∀ i, Γ.n i ≤ Γ.n j := fun i => by
    rw [← Γ.n_mod i]
    exact hjmax (i % m) (Finset.mem_range.mpr (Nat.mod_lt _ hmpos))
  -- the witness of the longest run, below the maximum
  have hw := Γ.witness_gt T (fun k hk => hrun k hk) (Γ.z_ne_zero hprim hh (i + T))
  have hwj : 2 * (3 : ℤ) ^ T < Γ.n j := lt_of_lt_of_le hw (max_le (hj _) (hj _))
  have hwjR : 2 * (3 : ℝ) ^ T < Γ.n j := by exact_mod_cast hwj
  have h3T : (3 : ℝ) ^ T ≠ 0 := by positivity
  have hlw := Real.log_lt_log (by positivity) hwjR
  rw [Real.log_mul (by norm_num : (2 : ℝ) ≠ 0) h3T, Real.log_pow] at hlw
  -- the drift ceiling at the maximum
  have hg := Γ.global_drift_log hapos hjm.le
  have hlog32 : 0 ≤ Real.log 3 - Real.log 2 := by
    have := Real.log_le_log (by norm_num : (0 : ℝ) < 2) (by norm_num : (2 : ℝ) ≤ 3)
    linarith
  have hlog2 : 0 < Real.log 2 := Real.log_pos (by norm_num)
  have hX : (0 : ℝ) ≤ Γ.excess j * Real.log 2 := mul_nonneg (Nat.cast_nonneg _) hlog2.le
  have hjR : (j : ℝ) ≤ (m : ℝ) - 1 := by
    have h' : ((j + 1 : ℕ) : ℝ) ≤ m := by exact_mod_cast (hjm : j + 1 ≤ m)
    push_cast at h'
    linarith
  have hjκ := mul_le_mul_of_nonneg_right hjR hlog32
  -- `3 L D ≤ m q 2^A` in logarithms
  have hn0 : (0 : ℝ) < Γ.n 0 := by exact_mod_cast Γ.npos
  have hD : (0 : ℝ) < (2 : ℝ) ^ Γ.Apre m - 3 ^ m := by exact_mod_cast Γ.D_pos
  have hq : (0 : ℝ) < Γ.q := by exact_mod_cast Γ.hq
  have hm0 : (0 : ℝ) < m := by exact_mod_cast hmpos
  have hA2 : (0 : ℝ) < 2 ^ Γ.Apre m := by positivity
  have h3n0 : (0 : ℝ) < 3 * Γ.n 0 := mul_pos (by norm_num) hn0
  have hmq : (0 : ℝ) < m * Γ.q := mul_pos hm0 hq
  have hl3 := Real.log_le_log (mul_pos h3n0 hD) Γ.three_L_D_le
  rw [Real.log_mul h3n0.ne' hD.ne', Real.log_mul (by norm_num : (3 : ℝ) ≠ 0) hn0.ne',
    Real.log_mul hmq.ne' hA2.ne', Real.log_mul hm0.ne' hq.ne', Real.log_pow] at hl3
  linarith

/-- S9 (i) in its stated form, with `⌈(m − 2)/2⌉ = (m − 1)/2` (natural division):
`log 2 + ⌈(m − 2)/2⌉ log 3 < log q + (m − 1) log(3/2) + δ + λ`. -/
theorem two_mismatch_denominator_law' (hprim : ∀ i j, i < m → j < m → Γ.n i = Γ.n j → i = j)
    (hapos : ∀ i, 1 ≤ Γ.a i) {h : ℕ} (hh : h % m ≠ 0) (hs : (Γ.mis h).card = 2) :
    Real.log 2 + (((m - 1) / 2 : ℕ) : ℝ) * Real.log 3 <
      Real.log (Γ.q) + ((m : ℝ) - 1) * (Real.log 3 - Real.log 2) +
        ((Γ.Apre m : ℝ) * Real.log 2 - m * Real.log 3) +
        (Real.log m + (Γ.Apre m : ℝ) * Real.log 2 - Real.log 3 -
          Real.log ((2 : ℝ) ^ Γ.Apre m - 3 ^ m)) := by
  obtain ⟨T, hT, hlt⟩ := Γ.two_mismatch_denominator_law hprim hapos hh hs
  have h1 : (m - 1) / 2 ≤ T := by omega
  have h2 : (((m - 1) / 2 : ℕ) : ℝ) ≤ T := by exact_mod_cast h1
  have hlog3 : 0 < Real.log 3 := Real.log_pos (by norm_num)
  have := mul_le_mul_of_nonneg_right h2 hlog3.le
  linarith

/-- The `3x+q` reading: for odd `q` the letters are `≥ 1` automatically. -/
theorem two_mismatch_denominator_law_odd (hprim : ∀ i j, i < m → j < m → Γ.n i = Γ.n j → i = j)
    (hq : Odd Γ.q) {h : ℕ} (hh : h % m ≠ 0) (hs : (Γ.mis h).card = 2) :
    Real.log 2 + (((m - 1) / 2 : ℕ) : ℝ) * Real.log 3 <
      Real.log (Γ.q) + ((m : ℝ) - 1) * (Real.log 3 - Real.log 2) +
        ((Γ.Apre m : ℝ) * Real.log 2 - m * Real.log 3) +
        (Real.log m + (Γ.Apre m : ℝ) * Real.log 2 - Real.log 3 -
          Real.log ((2 : ℝ) ^ Γ.Apre m - 3 ^ m)) :=
  Γ.two_mismatch_denominator_law' hprim (Γ.a_pos_of_odd hq) hh hs

end OddCycle

/-! ### S8-a: the by-products of S8 — runs of ones and the 1-cycle identity

S8's headline is withdrawn; its §1 constraint (5) and §4 1-cycle remain valid and are recorded here.
On a one-letter the arrow reads `2 (n_{i+1} + q) = 3 (n_i + q)` (`one_step_add_q`), so a run of `r`
ones from `i₀` gives `2^r (n_{i₀+r} + q) = 3^r (n_{i₀} + q)` (`ones_run_identity`); for odd `q` this
yields `2^r ∣ n_{i₀} + q` and `2·3^r ∣ n_{i₀+r} + q` (`ones_run_dvd`: the factor `2` because the states
are odd), hence `2·3^r ≤ n_{i₀+r} + q` (`ones_run_le`). The inequality is NOT strict in general: the
one-step `3 → 5` at `q = 1` has `r = 1` and `5 + 1 = 2·3`. The 1-cycle: with `q = 1` and the word
`1^{m−1} V` read from the minimum (letters `a_k = 1` for `k < m − 1`), the intercepts are
`C_j = 3^j − 2^j` (`Cpre_ones`), so the closing identity gives `D n_0 = 3^m − 2^m`, and with
`3^m ≡ 2^A (mod D)` and `D` odd, `D ∣ 2^{A−m} − 1` (`one_cycle_D_dvd`), hence `D ≤ 2^{A−m} − 1`
(`one_cycle_D_le`). With the gap `2^A ≤ 2^172 m^341 D` this forces `2^m < 2^172 m^341`
(`one_cycle_pow_lt`), impossible for `m ≥ 2^13` (`no_one_cycle_of_gap`; the exact threshold is
`m ≥ 4287`, computed outside Lean). All of this is conditional on the gap and far weaker than
Steiner's unconditional theorem on 1-cycles; it is recorded as a by-product. -/

namespace OddCycle

variable {m : ℕ} (Γ : OddCycle m)

/-- On a one-letter, `2 (n_{i+1} + q) = 3 (n_i + q)`. -/
theorem one_step_add_q {i : ℕ} (hi : Γ.a i = 1) :
    2 * (Γ.n (i + 1) + Γ.q) = 3 * (Γ.n i + Γ.q) := by
  have h := Γ.arrow i
  rw [hi, pow_one] at h
  linarith

/-- A run of `r` ones from `i₀`: `2^r (n_{i₀+r} + q) = 3^r (n_{i₀} + q)`. -/
theorem ones_run_identity (i₀ : ℕ) : ∀ r, (∀ k, k < r → Γ.a (i₀ + k) = 1) →
    2 ^ r * (Γ.n (i₀ + r) + Γ.q) = 3 ^ r * (Γ.n i₀ + Γ.q) := by
  intro r
  induction r with
  | zero =>
    intro _
    simp
  | succ r ih =>
    intro hr
    have h1 := ih (fun k hk => hr k (Nat.lt_succ_of_lt hk))
    have h2 := Γ.one_step_add_q (hr r (Nat.lt_succ_self r))
    rw [pow_succ, pow_succ, ← Nat.add_assoc]
    linear_combination 2 ^ r * h2 + 3 * h1

/-- **S8 §1 (5), the divisibility form, at general odd `q`.** A run of `r` ones from `i₀` gives
`2^r ∣ n_{i₀} + q` and `2·3^r ∣ n_{i₀+r} + q`. -/
theorem ones_run_dvd (hq : Odd Γ.q) {i₀ r : ℕ} (hr : ∀ k, k < r → Γ.a (i₀ + k) = 1) :
    (2 : ℤ) ^ r ∣ Γ.n i₀ + Γ.q ∧ 2 * (3 : ℤ) ^ r ∣ Γ.n (i₀ + r) + Γ.q := by
  have hid := Γ.ones_run_identity i₀ r hr
  have h23 : IsCoprime (2 : ℤ) 3 := Int.isCoprime_iff_gcd_eq_one.mpr (by norm_num)
  have hcop : IsCoprime ((2 : ℤ) ^ r) (3 ^ r) := h23.pow
  constructor
  · have h : (2 : ℤ) ^ r ∣ 3 ^ r * (Γ.n i₀ + Γ.q) := ⟨Γ.n (i₀ + r) + Γ.q, hid.symm⟩
    exact hcop.dvd_of_dvd_mul_left h
  · have h : (3 : ℤ) ^ r ∣ 2 ^ r * (Γ.n (i₀ + r) + Γ.q) := ⟨Γ.n i₀ + Γ.q, hid⟩
    have h3 : (3 : ℤ) ^ r ∣ Γ.n (i₀ + r) + Γ.q := hcop.symm.dvd_of_dvd_mul_left h
    have heven : (2 : ℤ) ∣ Γ.n (i₀ + r) + Γ.q :=
      even_iff_two_dvd.mp ((Γ.nodd (i₀ + r)).add_odd hq)
    exact IsCoprime.mul_dvd h23.pow_right heven h3

/-- The size form of (5): `2·3^r ≤ n_{i₀+r} + q` (not strict in general: `3 → 5`, `r = 1`, `q = 1`). -/
theorem ones_run_le (hq : Odd Γ.q) {i₀ r : ℕ} (hr : ∀ k, k < r → Γ.a (i₀ + k) = 1) :
    2 * (3 : ℤ) ^ r ≤ Γ.n (i₀ + r) + Γ.q := by
  have hpos : 0 < Γ.n (i₀ + r) + Γ.q := by
    have := lt_of_lt_of_le Γ.npos (Γ.nmin (i₀ + r))
    have := Γ.hq
    linarith
  exact Int.le_of_dvd hpos (Γ.ones_run_dvd hq hr).2

/-- Letters `≥ 1` give `m ≤ A`. -/
theorem m_le_Apre (hapos : ∀ i, 1 ≤ Γ.a i) : m ≤ Γ.Apre m := by
  rw [Γ.Apre_eq_excess_add hapos m]
  omega

/-- With the first `m − 1` letters equal to `1`, `A_j = j` for `j ≤ m − 1`. -/
theorem Apre_ones (hones : ∀ k, k < m - 1 → Γ.a k = 1) : ∀ j, j ≤ m - 1 → Γ.Apre j = j := by
  intro j
  induction j with
  | zero =>
    intro _
    simp [Apre]
  | succ j ih =>
    intro hj
    rw [Γ.Apre_succ, ih (by omega), hones j (by omega)]

/-- With the first `m − 1` letters equal to `1`, `C_j = 3^j − 2^j` for `j ≤ m`. -/
theorem Cpre_ones (hones : ∀ k, k < m - 1 → Γ.a k = 1) :
    ∀ j, j ≤ m → Γ.Cpre j = 3 ^ j - 2 ^ j := by
  intro j
  induction j with
  | zero =>
    intro _
    simp [Cpre]
  | succ j ih =>
    intro hj
    rw [Γ.Cpre_succ, ih (by omega), Γ.Apre_ones hones j (by omega), pow_succ, pow_succ]
    ring

/-- **S8 §4, the 1-cycle identity**: with `q = 1` and the word `1^{m−1} V` from the minimum,
`D ∣ 2^{A−m} − 1`. -/
theorem one_cycle_D_dvd (hq1 : Γ.q = 1) (hones : ∀ k, k < m - 1 → Γ.a k = 1) :
    (2 : ℤ) ^ Γ.Apre m - 3 ^ m ∣ 2 ^ (Γ.Apre m - m) - 1 := by
  have hapos : ∀ i, 1 ≤ Γ.a i := Γ.a_pos_of_odd (by rw [hq1]; exact odd_one)
  have hAm := Γ.m_le_Apre hapos
  have hcyc := Γ.cycle_identity
  rw [hq1, one_mul, Γ.Cpre_ones hones m le_rfl] at hcyc
  have hD : (2 : ℤ) ^ Γ.Apre m - 3 ^ m ∣ 3 ^ m - 2 ^ m := ⟨Γ.n 0, hcyc.symm⟩
  have h1 : (2 : ℤ) ^ Γ.Apre m - 3 ^ m ∣ 2 ^ Γ.Apre m - 2 ^ m := by
    have e : (2 : ℤ) ^ Γ.Apre m - 2 ^ m = (3 ^ m - 2 ^ m) + (2 ^ Γ.Apre m - 3 ^ m) := by ring
    rw [e]
    exact dvd_add hD (dvd_refl _)
  have h2 : (2 : ℤ) ^ Γ.Apre m - 2 ^ m = 2 ^ m * (2 ^ (Γ.Apre m - m) - 1) := by
    rw [mul_sub, mul_one, ← pow_add, Nat.add_sub_cancel' hAm]
  rw [h2] at h1
  have hA0 : Γ.Apre m ≠ 0 := by
    have := Γ.hm
    omega
  have hDodd : Odd ((2 : ℤ) ^ Γ.Apre m - 3 ^ m) :=
    (even_two.pow_of_ne_zero hA0).sub_odd (Odd.pow ⟨1, by norm_num⟩)
  obtain ⟨k, hk⟩ := hDodd
  have hcop2 : IsCoprime ((2 : ℤ) ^ Γ.Apre m - 3 ^ m) 2 := ⟨1, -k, by rw [hk]; ring⟩
  exact (hcop2.pow_right).dvd_of_dvd_mul_left h1

/-- `D ≤ 2^{A−m} − 1`, i.e. `2^A − 3^m ≤ 2^{A−m} − 1`. -/
theorem one_cycle_D_le (hq1 : Γ.q = 1) (hones : ∀ k, k < m - 1 → Γ.a k = 1) :
    (2 : ℤ) ^ Γ.Apre m - 3 ^ m ≤ 2 ^ (Γ.Apre m - m) - 1 := by
  have hdvd := Γ.one_cycle_D_dvd hq1 hones
  have hD := Γ.D_pos
  have hm := Γ.hm
  have h32 : (2 : ℤ) ^ m ≤ 3 ^ m := by
    gcongr
    norm_num
  have hAm : m < Γ.Apre m := by
    by_contra hle
    have hle' : Γ.Apre m ≤ m := not_lt.mp hle
    have : (2 : ℤ) ^ Γ.Apre m ≤ 2 ^ m := pow_le_pow_right₀ (by norm_num) hle'
    linarith
  have h1 : (2 : ℤ) ^ 1 ≤ 2 ^ (Γ.Apre m - m) := pow_le_pow_right₀ (by norm_num) (by omega)
  have hpos : (0 : ℤ) < 2 ^ (Γ.Apre m - m) - 1 := by
    rw [pow_one] at h1
    linarith
  exact Int.le_of_dvd hpos hdvd

/-- With the gap `2^A ≤ 2^172 m^341 D`, a 1-cycle forces `2^m < 2^172 m^341`. -/
theorem one_cycle_pow_lt (hq1 : Γ.q = 1)
    (hgap : (2 : ℤ) ^ Γ.Apre m ≤ 2 ^ 172 * (m : ℤ) ^ 341 * (2 ^ Γ.Apre m - 3 ^ m))
    (hones : ∀ k, k < m - 1 → Γ.a k = 1) : (2 : ℤ) ^ m < 2 ^ 172 * (m : ℤ) ^ 341 := by
  have hapos : ∀ i, 1 ≤ Γ.a i := Γ.a_pos_of_odd (by rw [hq1]; exact odd_one)
  have hAm := Γ.m_le_Apre hapos
  have hle := Γ.one_cycle_D_le hq1 hones
  have hmZ : (0 : ℤ) < m := by exact_mod_cast Γ.hm
  have hc : (0 : ℤ) < 2 ^ 172 * (m : ℤ) ^ 341 := mul_pos (by positivity) (pow_pos hmZ _)
  have h3 : (2 : ℤ) ^ Γ.Apre m ≤ 2 ^ 172 * (m : ℤ) ^ 341 * (2 ^ (Γ.Apre m - m) - 1) :=
    le_trans hgap (mul_le_mul_of_nonneg_left hle hc.le)
  have h4 : (2 : ℤ) ^ Γ.Apre m < 2 ^ 172 * (m : ℤ) ^ 341 * 2 ^ (Γ.Apre m - m) := by
    linarith
  have h2 : (2 : ℤ) ^ Γ.Apre m = 2 ^ m * 2 ^ (Γ.Apre m - m) := by
    rw [← pow_add, Nat.add_sub_cancel' hAm]
  rw [h2] at h4
  exact lt_of_mul_lt_mul_right h4 (by positivity)

/-- **No 1-cycle with the gap for `m ≥ 2^13`** (exact threshold `m ≥ 4287`, computed outside Lean):
`2^m < 2^172 m^341` is impossible there. -/
theorem no_one_cycle_of_gap (hq1 : Γ.q = 1)
    (hgap : (2 : ℤ) ^ Γ.Apre m ≤ 2 ^ 172 * (m : ℤ) ^ 341 * (2 ^ Γ.Apre m - 3 ^ m))
    (hones : ∀ k, k < m - 1 → Γ.a k = 1) (hm : 2 ^ 13 ≤ m) : False := by
  have h := Γ.one_cycle_pow_lt hq1 hgap hones
  have hR : (2 : ℝ) ^ m < 2 ^ 172 * (m : ℝ) ^ 341 := by exact_mod_cast h
  have hm' : 8192 ≤ m := by
    norm_num at hm
    exact hm
  have hmR : (8192 : ℝ) ≤ m := by exact_mod_cast hm'
  have hm0 : (0 : ℝ) < m := by linarith
  have hm341 : (m : ℝ) ^ 341 ≠ 0 := pow_ne_zero _ hm0.ne'
  have hl := Real.log_lt_log (by positivity) hR
  rw [Real.log_pow, Real.log_mul (by positivity : (2 : ℝ) ^ 172 ≠ 0) hm341, Real.log_pow,
    Real.log_pow] at hl
  push_cast at hl
  have hx : (0 : ℝ) < (m : ℝ) / 8192 := by positivity
  have ht := Real.log_le_sub_one_of_pos hx
  rw [Real.log_div hm0.ne' (by norm_num), show (8192 : ℝ) = 2 ^ 13 by norm_num, Real.log_pow] at ht
  push_cast at ht
  have hl2a := Real.log_two_gt_d9
  have hl2b := Real.log_two_lt_d9
  have hp : (m : ℝ) * 0.6931471803 ≤ m * Real.log 2 := mul_le_mul_of_nonneg_left hl2a.le hm0.le
  linarith

end OddCycle

/-! ### S9-c: the three-mismatch denominator law at general `q` (S9 §2 (ii), linear form)

S7's chain with the global-drift ceiling in place of the per-step ceiling, for an arbitrary
`OddCycle` with letters `≥ 1`: no gap hypothesis and no hypothesis on `L/q`. The single size variable
is `Λ = log L + δ`, `δ = A log 2 − m log 3`. The drift ceiling gives `log n_k ≤ log L + k log(3/2) + δ`
(`n_le_drift`, `log_of_drift_bound`); the witness of the first run in S7 Step 5 becomes
`2·3^τ < L (3/2)^{τ+τ′+1} 2^A/3^m` (`three_mismatch_witness_drift`, the two ceiling calls of
`three_mismatch_witness` replaced). The numeric conditions W, A and F hold for `m ≥ 2^19` whenever
`Λ ≤ (m/70) log 2` (`numeric_WA_drift`, `numeric_F_drift`; the supremum of the admissible ratio is
`Λ₃(m)/m = 0.014570…` for every `m ≥ 2^19`, `1/70 = 0.0142857…`, with W binding: margins at `2^19`
of about `348`, `195,000` and `4,395` positions). Hence a rotation `1 ≤ h < m` with exactly three
mismatches forces `Λ > (m/70) log 2` (`no_three_mismatch_of_small_drift`), and with
`log L ≤ log q + λ`, `λ = log(m 2^A/(3D))` (`three_L_D_le`):
`(m/70) log 2 < log q + δ + λ` (`three_mismatch_denominator_law`). In bits: `log₂ q > m/70 − δ(w) −
λ(w)`, S9 (ii) with the explicit constant `1/70` in place of `Λ₃(m)`. The identification `q = den(w)`
is the programme's (C008/C009), not re-proved here. -/

namespace OddCycle

variable {m : ℕ} (Γ : OddCycle m)

/-- The drift ceiling without the excess: `n_k ≤ L (3/2)^k · 2^A/3^m` for `k ≤ m`. -/
theorem n_le_drift (hapos : ∀ i, 1 ≤ Γ.a i) {k : ℕ} (hk : k ≤ m) :
    (Γ.n k : ℝ) ≤ Γ.n 0 * (3 / 2 : ℝ) ^ k * ((2 : ℝ) ^ Γ.Apre m / 3 ^ m) := by
  have hR : (Γ.n k : ℝ) * 2 ^ Γ.Apre k * 3 ^ m ≤ Γ.n 0 * 3 ^ k * 2 ^ Γ.Apre m := by
    exact_mod_cast Γ.global_drift hk
  have hAk := Γ.Apre_eq_excess_add hapos k
  have hnk : (0 : ℝ) ≤ Γ.n k := by exact_mod_cast (lt_of_lt_of_le Γ.npos (Γ.nmin k)).le
  have h3m : (0 : ℝ) < 3 ^ m := by positivity
  have h2k : (0 : ℝ) < 2 ^ k := by positivity
  have hkA : k ≤ Γ.Apre k := by
    rw [hAk]
    omega
  have h2 : (2 : ℝ) ^ k ≤ 2 ^ Γ.Apre k := pow_le_pow_right₀ (by norm_num) hkA
  have h1 : (Γ.n k : ℝ) * (2 ^ k * 3 ^ m) ≤ Γ.n 0 * 3 ^ k * 2 ^ Γ.Apre m := by
    calc (Γ.n k : ℝ) * (2 ^ k * 3 ^ m) = Γ.n k * 2 ^ k * 3 ^ m := by ring
      _ ≤ Γ.n k * 2 ^ Γ.Apre k * 3 ^ m :=
          mul_le_mul_of_nonneg_right (mul_le_mul_of_nonneg_left h2 hnk) h3m.le
      _ ≤ Γ.n 0 * 3 ^ k * 2 ^ Γ.Apre m := hR
  have e : Γ.n 0 * (3 / 2 : ℝ) ^ k * ((2 : ℝ) ^ Γ.Apre m / 3 ^ m) =
      Γ.n 0 * 3 ^ k * 2 ^ Γ.Apre m / (2 ^ k * 3 ^ m) := by
    rw [div_pow]
    field_simp
  rw [e, le_div_iff₀ (mul_pos h2k h3m)]
  exact h1

/-- Logarithmic form of a drift bound `2·3^t < L (3/2)^k 2^A/3^m`. -/
theorem log_of_drift_bound {t k : ℕ}
    (hb : 2 * (3 : ℝ) ^ t < Γ.n 0 * (3 / 2 : ℝ) ^ k * ((2 : ℝ) ^ Γ.Apre m / 3 ^ m)) :
    Real.log 2 + t * Real.log 3 <
      Real.log (Γ.n 0) + k * (Real.log 3 - Real.log 2) +
        ((Γ.Apre m : ℝ) * Real.log 2 - m * Real.log 3) := by
  have hn0 : (0 : ℝ) < Γ.n 0 := by exact_mod_cast Γ.npos
  have h3t : (3 : ℝ) ^ t ≠ 0 := by positivity
  have h32 : (3 / 2 : ℝ) ^ k ≠ 0 := by positivity
  have h2A : (2 : ℝ) ^ Γ.Apre m ≠ 0 := by positivity
  have h3m : (3 : ℝ) ^ m ≠ 0 := by positivity
  have hq : (2 : ℝ) ^ Γ.Apre m / 3 ^ m ≠ 0 := div_ne_zero h2A h3m
  have hn32 : Γ.n 0 * (3 / 2 : ℝ) ^ k ≠ 0 := mul_ne_zero hn0.ne' h32
  have hl := Real.log_lt_log (by positivity) hb
  rw [Real.log_mul (by norm_num : (2 : ℝ) ≠ 0) h3t, Real.log_pow, Real.log_mul hn32 hq,
    Real.log_mul hn0.ne' h32, Real.log_pow, Real.log_div h2A h3m, Real.log_pow, Real.log_pow,
    Real.log_div (by norm_num : (3 : ℝ) ≠ 0) (by norm_num : (2 : ℝ) ≠ 0)] at hl
  linarith

/-- S7 Step 5 with the drift ceiling: the three runs and the witness of the first,
`2·3^τ < L (3/2)^{τ+τ′+1} 2^A/3^m`. -/
theorem three_mismatch_witness_drift (hprim : ∀ i j, i < m → j < m → Γ.n i = Γ.n j → i = j)
    (hapos : ∀ i, 1 ≤ Γ.a i) {j h e_a : ℕ} (hjm : j < m) (hh1 : 1 ≤ h) (hhm : h < m)
    (hs : (Γ.mis h).card = 3) (hea1 : j - h ≤ e_a) (hea2 : e_a < m - h) (hdown : Γ.down h e_a)
    (hup : Γ.up h (e_a + h)) (hhj : h ≤ j)
    (hW : ∀ i, j ≤ i → i < m → i ≠ e_a + h → Γ.agree h i)
    (hW' : ∀ k, j - h ≤ k → k < m - h → k ≠ e_a → Γ.agree h k) :
    ∃ τ τ' τ'' i₁ i₂ i₃ : ℕ, τ + τ' + τ'' = m - 3 ∧
      (∀ k, k < τ → Γ.agree h (i₁ + k)) ∧ (∀ k, k < τ' → Γ.agree h (i₂ + k)) ∧
      (∀ k, k < τ'' → Γ.agree h (i₃ + k)) ∧
      2 * (3 : ℝ) ^ τ < Γ.n 0 * (3 / 2 : ℝ) ^ (τ + τ' + 1) *
        ((2 : ℝ) ^ Γ.Apre m / 3 ^ m) := by
  have hm := Γ.hm
  have hh : h % m ≠ 0 := by
    rw [Nat.mod_eq_of_lt hhm]
    omega
  have hn0 : (0 : ℝ) < Γ.n 0 := by exact_mod_cast Γ.npos
  have hA3 : (0 : ℝ) ≤ (2 : ℝ) ^ Γ.Apre m / 3 ^ m := by positivity
  set e_b := e_a + h with heb_def
  have heb : e_b < m := by omega
  have hea_mem : e_a ∈ Γ.mis h := Γ.down_mem_mis (by omega) hdown
  have heb_mem : e_b ∈ Γ.mis h := Γ.up_mem_mis heb hup
  have hab : e_a ≠ e_b := by omega
  obtain ⟨e_c, h3⟩ := Γ.third_mismatch hs hea_mem heb_mem hab
  have hec_mem' : e_c ∈ ((Γ.mis h).erase e_a).erase e_b := by
    rw [h3]
    exact Finset.mem_singleton_self e_c
  have hec_mem : e_c ∈ Γ.mis h := Finset.mem_of_mem_erase (Finset.mem_of_mem_erase hec_mem')
  have hcb : e_c ≠ e_b := (Finset.mem_erase.mp hec_mem').1
  have hca : e_c ≠ e_a := (Finset.mem_erase.mp (Finset.mem_of_mem_erase hec_mem')).1
  have hec_lt : e_c < m := Γ.mis_lt_m hec_mem
  have hec_na : ¬ Γ.agree h e_c := by
    unfold mis at hec_mem
    rw [Finset.mem_filter] at hec_mem
    exact hec_mem.2
  -- `e_c` is not in `W = [j, m)` and not in `W − h = [j − h, m − h)`
  have hec_notW : e_c < j := by
    by_contra hge
    exact hec_na (hW e_c (by omega) hec_lt hcb)
  have hec_notW' : e_c < j - h ∨ m - h ≤ e_c := by
    by_contra hno
    exact hec_na (hW' e_c (by omega) (by omega) hca)
  -- the agreement helper for positions below `2m`
  have hagr : ∀ p, p < 2 * m → p ≠ e_a → p ≠ e_b → p ≠ e_c → p ≠ e_a + m → p ≠ e_b + m →
      p ≠ e_c + m → Γ.agree h p :=
    fun p => Γ.agree_of_pos hs hea_mem heb_mem hec_mem hab hca.symm hcb.symm p
  have hzc : Γ.z h e_c ≠ 0 := Γ.z_ne_zero hprim hh e_c
  rcases Nat.lt_or_gt_of_ne hca with hc1 | hc2
  · -- Order 1: `e_c < e_a`. Runs: `(e_b, e_c + m)`, `(e_a, e_b)`, `(e_c, e_a)`.
    refine ⟨m - e_b + e_c - 1, h - 1, e_a - e_c - 1, e_b + 1, e_a + 1, e_c + 1, by omega,
      ?_, ?_, ?_, ?_⟩
    · intro k hk
      exact hagr (e_b + 1 + k) (by omega) (by omega) (by omega) (by omega) (by omega) (by omega)
        (by omega)
    · intro k hk
      exact hagr (e_a + 1 + k) (by omega) (by omega) (by omega) (by omega) (by omega) (by omega)
        (by omega)
    · intro k hk
      exact hagr (e_c + 1 + k) (by omega) (by omega) (by omega) (by omega) (by omega) (by omega)
        (by omega)
    · have hrun : ∀ k, k < m - e_b + e_c - 1 → Γ.agree h (e_b + 1 + k) := by
        intro k hk
        exact hagr (e_b + 1 + k) (by omega) (by omega) (by omega) (by omega) (by omega)
          (by omega) (by omega)
      have hend : e_b + 1 + (m - e_b + e_c - 1) = e_c + m := by omega
      have hzend : Γ.z h (e_b + 1 + (m - e_b + e_c - 1)) ≠ 0 := by
        rw [hend, Γ.z_per]
        exact hzc
      have hw := Γ.witness_gt (m - e_b + e_c - 1) hrun hzend
      have hpos : 0 < Γ.z h e_c := by
        have := (Γ.z_pos_run (m - e_b + e_c - 1) hrun).mpr hup.2
        rwa [hend, Γ.z_per] at this
      rw [hend, Γ.nper, Nat.add_right_comm e_c m h, Γ.nper] at hw
      have hle : Γ.n e_c ≤ Γ.n (e_c + h) := by
        unfold z at hpos
        linarith
      rw [max_eq_right hle] at hw
      have hwR : 2 * (3 : ℝ) ^ (m - e_b + e_c - 1) < Γ.n (e_c + h) := by exact_mod_cast hw
      have hkm : e_c + h ≤ m := by omega
      have hcl := Γ.n_le_drift hapos hkm
      have hidx : e_c + h ≤ m - e_b + e_c - 1 + (h - 1) + 1 := by omega
      calc 2 * (3 : ℝ) ^ (m - e_b + e_c - 1) < Γ.n (e_c + h) := hwR
        _ ≤ Γ.n 0 * (3 / 2 : ℝ) ^ (e_c + h) * ((2 : ℝ) ^ Γ.Apre m / 3 ^ m) := hcl
        _ ≤ Γ.n 0 * (3 / 2 : ℝ) ^ (m - e_b + e_c - 1 + (h - 1) + 1) *
            ((2 : ℝ) ^ Γ.Apre m / 3 ^ m) :=
            mul_le_mul_of_nonneg_right
              (mul_le_mul_of_nonneg_left (pow_le_pow_right₀ (by norm_num) hidx) hn0.le) hA3
  · -- Order 2: `e_a < e_c < e_b`. Runs: `(e_a, e_c)`, `(e_b, e_a + m)`, `(e_c, e_b)`.
    have hc2b : e_c < e_b := by omega
    refine ⟨e_c - e_a - 1, m - e_b + e_a - 1, e_b - e_c - 1, e_a + 1, e_b + 1, e_c + 1, by omega,
      ?_, ?_, ?_, ?_⟩
    · intro k hk
      exact hagr (e_a + 1 + k) (by omega) (by omega) (by omega) (by omega) (by omega) (by omega)
        (by omega)
    · intro k hk
      exact hagr (e_b + 1 + k) (by omega) (by omega) (by omega) (by omega) (by omega) (by omega)
        (by omega)
    · intro k hk
      exact hagr (e_c + 1 + k) (by omega) (by omega) (by omega) (by omega) (by omega) (by omega)
        (by omega)
    · have hrun : ∀ k, k < e_c - e_a - 1 → Γ.agree h (e_a + 1 + k) := by
        intro k hk
        exact hagr (e_a + 1 + k) (by omega) (by omega) (by omega) (by omega) (by omega)
          (by omega) (by omega)
      have hend : e_a + 1 + (e_c - e_a - 1) = e_c := by omega
      have hzend : Γ.z h (e_a + 1 + (e_c - e_a - 1)) ≠ 0 := by
        rw [hend]
        exact hzc
      have hw := Γ.witness_gt (e_c - e_a - 1) hrun hzend
      have hneg1 : Γ.z h (e_a + 1) < 0 := by
        have hne : Γ.z h (e_a + 1) ≠ 0 := Γ.z_ne_zero hprim hh (e_a + 1)
        exact lt_of_le_of_ne (not_lt.mp hdown.2) hne
      have hneg : Γ.z h e_c < 0 := by
        have := (Γ.z_neg_run (e_c - e_a - 1) hrun).mpr hneg1
        rwa [hend] at this
      rw [hend] at hw
      have hle : Γ.n (e_c + h) ≤ Γ.n e_c := by
        unfold z at hneg
        linarith
      rw [max_eq_left hle] at hw
      have hwR : 2 * (3 : ℝ) ^ (e_c - e_a - 1) < Γ.n e_c := by exact_mod_cast hw
      have hcl := Γ.n_le_drift hapos hec_lt.le
      have hidx : e_c ≤ e_c - e_a - 1 + (m - e_b + e_a - 1) + 1 := by omega
      calc 2 * (3 : ℝ) ^ (e_c - e_a - 1) < Γ.n e_c := hwR
        _ ≤ Γ.n 0 * (3 / 2 : ℝ) ^ e_c * ((2 : ℝ) ^ Γ.Apre m / 3 ^ m) := hcl
        _ ≤ Γ.n 0 * (3 / 2 : ℝ) ^ (e_c - e_a - 1 + (m - e_b + e_a - 1) + 1) *
            ((2 : ℝ) ^ Γ.Apre m / 3 ^ m) :=
            mul_le_mul_of_nonneg_right
              (mul_le_mul_of_nonneg_left (pow_le_pow_right₀ (by norm_num) hidx) hn0.le) hA3

/-- Conditions W and A of S7 in the drift formulation, for `m ≥ 2^19` and `Λ ≤ (m/70) log 2`. -/
theorem numeric_WA_drift (m j T ts Xc A Λ : ℝ) (hm : 2 ^ 19 ≤ m) (hj0 : 0 ≤ j) (hj : j + 1 ≤ m)
    (hT0 : 0 ≤ T) (hT : T * Real.log 3 ≤ Λ - Real.log 2 + (m - 1) * (Real.log 3 - Real.log 2))
    (hts0 : 0 ≤ ts) (hts : m - 3 ≤ 3 * ts) (hXc0 : 0 ≤ Xc)
    (hjlow : Real.log 2 + ts * Real.log 3 + Xc * Real.log 2 < Λ + j * (Real.log 3 - Real.log 2))
    (hA0 : 0 ≤ A) (hA : m * Real.log 3 < A * Real.log 2) (hΛ : Λ ≤ m / 70 * Real.log 2) :
    2 * (m - j) + 2 * (T + 1) ≤ m + 1 ∧ 3 * Xc + 1 ≤ A - m := by
  have hl2a := Real.log_two_gt_d9
  have hl2b := Real.log_two_lt_d9
  obtain ⟨hl3a, hl3b⟩ := log_three_bounds
  have hκup : Real.log 3 - Real.log 2 ≤ (179 / 306) * 0.6931471808 := by linarith
  have hl3lo : (1054 / 665) * 0.6931471803 ≤ Real.log 3 := by linarith
  have p1 : j * (Real.log 3 - Real.log 2) ≤ j * ((179 / 306) * 0.6931471808) :=
    mul_le_mul_of_nonneg_left hκup hj0
  have p2 : ts * ((1054 / 665) * 0.6931471803) ≤ ts * Real.log 3 :=
    mul_le_mul_of_nonneg_left hl3lo hts0
  have p3 : T * ((1054 / 665) * 0.6931471803) ≤ T * Real.log 3 :=
    mul_le_mul_of_nonneg_left hl3lo hT0
  have p4 : (m - 1) * (Real.log 3 - Real.log 2) ≤ (m - 1) * ((179 / 306) * 0.6931471808) :=
    mul_le_mul_of_nonneg_left hκup (by linarith)
  have p5 : m * ((1054 / 665) * 0.6931471803) ≤ m * Real.log 3 :=
    mul_le_mul_of_nonneg_left hl3lo (by linarith)
  have p6 : A * Real.log 2 ≤ A * 0.6931471808 := mul_le_mul_of_nonneg_left hl2b.le hA0
  have p7 : Xc * 0.6931471803 ≤ Xc * Real.log 2 := mul_le_mul_of_nonneg_left hl2a.le hXc0
  have p8 : m / 70 * Real.log 2 ≤ m / 70 * 0.6931471808 :=
    mul_le_mul_of_nonneg_left hl2b.le (by linarith)
  constructor
  · linarith
  · linarith

/-- Condition F of S7 in the drift formulation: the Step 5–6 data are contradictory for `m ≥ 2^19`
and `Λ ≤ (m/70) log 2`. -/
theorem numeric_F_drift (m T τ Λ : ℝ) (hm : 2 ^ 19 ≤ m) (hT0 : 0 ≤ T)
    (hT : T * Real.log 3 ≤ Λ - Real.log 2 + (m - 1) * (Real.log 3 - Real.log 2))
    (hτ0 : 0 ≤ τ) (hτ : m - 3 ≤ τ + 2 * T)
    (hwit : τ * Real.log 3 < Λ - Real.log 2 + (τ + T + 1) * (Real.log 3 - Real.log 2))
    (hΛ : Λ ≤ m / 70 * Real.log 2) : False := by
  have hl2a := Real.log_two_gt_d9
  have hl2b := Real.log_two_lt_d9
  obtain ⟨hl3a, hl3b⟩ := log_three_bounds
  have hκup : Real.log 3 - Real.log 2 ≤ (179 / 306) * 0.6931471808 := by linarith
  have hl3lo : (1054 / 665) * 0.6931471803 ≤ Real.log 3 := by linarith
  have p1 : τ * ((1054 / 665) * 0.6931471803) ≤ τ * Real.log 3 :=
    mul_le_mul_of_nonneg_left hl3lo hτ0
  have p2 : (τ + T + 1) * (Real.log 3 - Real.log 2) ≤
      (τ + T + 1) * ((179 / 306) * 0.6931471808) :=
    mul_le_mul_of_nonneg_left hκup (by linarith)
  have p3 : T * ((1054 / 665) * 0.6931471803) ≤ T * Real.log 3 :=
    mul_le_mul_of_nonneg_left hl3lo hT0
  have p4 : (m - 1) * (Real.log 3 - Real.log 2) ≤ (m - 1) * ((179 / 306) * 0.6931471808) :=
    mul_le_mul_of_nonneg_left hκup (by linarith)
  have p8 : m / 70 * Real.log 2 ≤ m / 70 * 0.6931471808 :=
    mul_le_mul_of_nonneg_left hl2b.le (by linarith)
  linarith

/-- **S7 in the drift formulation.** For a primitive cycle with letters `≥ 1`, `m ≥ 2^19` and
`Λ = log L + δ ≤ (m/70) log 2`, no rotation `1 ≤ h < m` has exactly three mismatches. No gap
hypothesis and no hypothesis on `L/q`. -/
theorem no_three_mismatch_of_small_drift (hprim : ∀ i j, i < m → j < m → Γ.n i = Γ.n j → i = j)
    (hapos : ∀ i, 1 ≤ Γ.a i) (hm : 2 ^ 19 ≤ m)
    (hΛ : Real.log (Γ.n 0) + ((Γ.Apre m : ℝ) * Real.log 2 - m * Real.log 3) ≤
      (m : ℝ) / 70 * Real.log 2)
    {h : ℕ} (hh1 : 1 ≤ h) (hhm : h < m) : (Γ.mis h).card ≠ 3 := by
  intro hs
  have hmpos := Γ.hm
  have hh : h % m ≠ 0 := by
    rw [Nat.mod_eq_of_lt hhm]
    omega
  -- the maximum
  obtain ⟨j, hjm', hjmax⟩ :=
    Finset.exists_max_image (Finset.range m) Γ.n ⟨0, Finset.mem_range.mpr hmpos⟩
  have hjm : j < m := Finset.mem_range.mp hjm'
  have hj : ∀ i, Γ.n i ≤ Γ.n j := fun i => by
    rw [← Γ.n_mod i]
    exact hjmax (i % m) (Finset.mem_range.mpr (Nat.mod_lt _ hmpos))
  -- a longest agreeing run `T`, realised at `i`
  obtain ⟨i, T, hrun, hTbound⟩ := Γ.exists_longest_run hprim hh
  have hzT : Γ.z h (i + T) ≠ 0 := Γ.z_ne_zero hprim hh (i + T)
  -- Step 1: the spacing bound and `3T ≥ m − 3`
  have hsep := Γ.hsep_of_runs hTbound hs
  have hpig := Γ.pigeonhole (Γ.exists_mis hprim hh) hTbound
  rw [hs] at hpig
  -- the witness of the longest run, below the maximum, against the drift ceiling
  have hw := Γ.witness_gt T (fun k hk => hrun k hk) hzT
  have hwj : 2 * (3 : ℤ) ^ T < Γ.n j := lt_of_lt_of_le hw (max_le (hj _) (hj _))
  have hwjR : 2 * (3 : ℝ) ^ T < Γ.n j := by exact_mod_cast hwj
  have hnj : (0 : ℝ) < Γ.n j := by exact_mod_cast lt_of_lt_of_le Γ.npos (Γ.nmin j)
  have h3T : (3 : ℝ) ^ T ≠ 0 := by positivity
  have hlw := Real.log_lt_log (by positivity) hwjR
  rw [Real.log_mul (by norm_num : (2 : ℝ) ≠ 0) h3T, Real.log_pow] at hlw
  have hg := Γ.global_drift_log hapos hjm.le
  have hlog32 : 0 ≤ Real.log 3 - Real.log 2 := by
    have := Real.log_le_log (by norm_num : (0 : ℝ) < 2) (by norm_num : (2 : ℝ) ≤ 3)
    linarith
  have hlog2 : 0 < Real.log 2 := Real.log_pos (by norm_num)
  have hX : (0 : ℝ) ≤ Γ.excess j * Real.log 2 := mul_nonneg (Nat.cast_nonneg _) hlog2.le
  have hjR : (j : ℝ) + 1 ≤ m := by exact_mod_cast (hjm : j + 1 ≤ m)
  have hjκ := mul_le_mul_of_nonneg_right (by linarith : (j : ℝ) ≤ (m : ℝ) - 1) hlog32
  have hmR : (2 : ℝ) ^ 19 ≤ m := by exact_mod_cast hm
  -- hypotheses of the numeric lemmas
  have hT : (T : ℝ) * Real.log 3 ≤
      (Real.log (Γ.n 0) + ((Γ.Apre m : ℝ) * Real.log 2 - m * Real.log 3)) - Real.log 2 +
        ((m : ℝ) - 1) * (Real.log 3 - Real.log 2) := by
    linarith
  have hjlow : Real.log 2 + (T : ℝ) * Real.log 3 + (Γ.excess j : ℝ) * Real.log 2 <
      (Real.log (Γ.n 0) + ((Γ.Apre m : ℝ) * Real.log 2 - m * Real.log 3)) +
        (j : ℝ) * (Real.log 3 - Real.log 2) := by
    linarith
  have hts : (m : ℝ) - 3 ≤ 3 * (T : ℝ) := by
    have h' : (m : ℝ) ≤ ((T : ℝ) + 1) * 3 := by exact_mod_cast hpig
    linarith
  have hA : (m : ℝ) * Real.log 3 < (Γ.Apre m : ℝ) * Real.log 2 := by
    have hD := Γ.D_pos
    have hDR : (3 : ℝ) ^ m < 2 ^ Γ.Apre m := by
      have : (3 : ℤ) ^ m < 2 ^ Γ.Apre m := by linarith
      exact_mod_cast this
    have := Real.log_lt_log (by positivity) hDR
    rwa [Real.log_pow, Real.log_pow] at this
  obtain ⟨hWr, hAr⟩ := numeric_WA_drift (m : ℝ) j T T (Γ.excess j) (Γ.Apre m)
    (Real.log (Γ.n 0) + ((Γ.Apre m : ℝ) * Real.log 2 - m * Real.log 3)) hmR (Nat.cast_nonneg j)
    hjR (Nat.cast_nonneg T) hT (Nat.cast_nonneg T) hts (Nat.cast_nonneg _) hjlow
    (Nat.cast_nonneg _) hA hΛ
  have hWnat : 2 * (m - j) + 2 * (T + 1) ≤ m + 1 := by
    have h' : ((2 * (m - j) + 2 * (T + 1) : ℕ) : ℝ) ≤ ((m + 1 : ℕ) : ℝ) := by
      push_cast [Nat.cast_sub hjm.le]
      linarith
    exact_mod_cast h'
  have hσ : 2 * (m - j) ≤ m - 2 * (T + 1) + 1 := by omega
  have hσd : m - j ≤ m - 2 * (T + 1) := by omega
  have hmA : m ≤ Γ.Apre m := Γ.m_le_Apre hapos
  have hAnat : 3 * Γ.excess j < Γ.Apre m - m := by
    have h' : ((3 * Γ.excess j + 1 : ℕ) : ℝ) ≤ ((Γ.Apre m - m : ℕ) : ℝ) := by
      push_cast [Nat.cast_sub hmA]
      linarith
    have h'' : 3 * Γ.excess j + 1 ≤ Γ.Apre m - m := by exact_mod_cast h'
    omega
  -- Steps 2–4: the aligned pair and its windows
  obtain ⟨e_a, e_b, hea, heb, hea1, hea2, heb1, heb2, hdown, hup, _, hhj, halign⟩ :=
    Γ.three_mismatch_structure hprim hj hjm hh1 hhm hsep hσ hapos hAnat
  subst halign
  have hW : ∀ i, j ≤ i → i < m → i ≠ e_a + h → Γ.agree h i := by
    intro i hi1 hi2 hi3
    exact Γ.agree_of_window hsep hσd heb heb1 (by omega) (by omega) hi1 (by omega) hi3
  have hW' : ∀ k, j - h ≤ k → k < m - h → k ≠ e_a → Γ.agree h k := by
    intro k hk1 hk2 hk3
    exact Γ.agree_of_window hsep hσd hea hea1 (by omega) (by omega) hk1 (by omega) hk3
  -- Step 5: the three runs and the witness of the first, with the drift ceiling
  obtain ⟨τ, τ', τ'', _, i₂, i₃, hsum, _, hr2, hr3, hwitR⟩ :=
    Γ.three_mismatch_witness_drift hprim hapos hjm hh1 hhm hs hea1 hea2 hdown hup hhj hW hW'
  have hτ'T : τ' ≤ T := hTbound i₂ τ' hr2
  have hτ''T : τ'' ≤ T := hTbound i₃ τ'' hr3
  have hwlog := Γ.log_of_drift_bound hwitR
  push_cast at hwlog
  have hτ'R : (τ' : ℝ) ≤ T := by exact_mod_cast hτ'T
  have hwit : (τ : ℝ) * Real.log 3 <
      (Real.log (Γ.n 0) + ((Γ.Apre m : ℝ) * Real.log 2 - m * Real.log 3)) - Real.log 2 +
        ((τ : ℝ) + T + 1) * (Real.log 3 - Real.log 2) := by
    have := mul_le_mul_of_nonneg_right hτ'R hlog32
    linarith
  have hmτ : m ≤ τ + 2 * T + 3 := by omega
  have hτR : (m : ℝ) - 3 ≤ (τ : ℝ) + 2 * T := by
    have : (m : ℝ) ≤ (τ : ℝ) + 2 * T + 3 := by exact_mod_cast hmτ
    linarith
  -- Step 6
  exact numeric_F_drift (m : ℝ) T τ
    (Real.log (Γ.n 0) + ((Γ.Apre m : ℝ) * Real.log 2 - m * Real.log 3)) hmR (Nat.cast_nonneg T)
    hT (Nat.cast_nonneg τ) hτR hwit hΛ

/-- **S9 (ii), the three-mismatch denominator law** (natural logarithms, explicit constant). For a
primitive cycle with odd `q`, `m ≥ 2^19`, and a rotation `1 ≤ h < m` with exactly three mismatches,
`(m/70) log 2 < log q + δ + λ`, where `δ = A log 2 − m log 3` and
`λ = log m + A log 2 − log 3 − log D`, `D = 2^A − 3^m`. In bits: `log₂ q > m/70 − δ(w) − λ(w)`. -/
theorem three_mismatch_denominator_law (hprim : ∀ i j, i < m → j < m → Γ.n i = Γ.n j → i = j)
    (hq : Odd Γ.q) (hm : 2 ^ 19 ≤ m) {h : ℕ} (hh1 : 1 ≤ h) (hhm : h < m)
    (hs : (Γ.mis h).card = 3) :
    (m : ℝ) / 70 * Real.log 2 <
      Real.log (Γ.q) + ((Γ.Apre m : ℝ) * Real.log 2 - m * Real.log 3) +
        (Real.log m + (Γ.Apre m : ℝ) * Real.log 2 - Real.log 3 -
          Real.log ((2 : ℝ) ^ Γ.Apre m - 3 ^ m)) := by
  have hapos : ∀ i, 1 ≤ Γ.a i := Γ.a_pos_of_odd hq
  by_contra hle
  have hle' := not_lt.mp hle
  -- `log L ≤ log q + λ`
  have hn0 : (0 : ℝ) < Γ.n 0 := by exact_mod_cast Γ.npos
  have hD : (0 : ℝ) < (2 : ℝ) ^ Γ.Apre m - 3 ^ m := by exact_mod_cast Γ.D_pos
  have hqR : (0 : ℝ) < Γ.q := by exact_mod_cast Γ.hq
  have hm0 : (0 : ℝ) < m := by exact_mod_cast Γ.hm
  have hA2 : (0 : ℝ) < 2 ^ Γ.Apre m := by positivity
  have h3n0 : (0 : ℝ) < 3 * Γ.n 0 := mul_pos (by norm_num) hn0
  have hmq : (0 : ℝ) < m * Γ.q := mul_pos hm0 hqR
  have hl3 := Real.log_le_log (mul_pos h3n0 hD) Γ.three_L_D_le
  rw [Real.log_mul h3n0.ne' hD.ne', Real.log_mul (by norm_num : (3 : ℝ) ≠ 0) hn0.ne',
    Real.log_mul hmq.ne' hA2.ne', Real.log_mul hm0.ne' hqR.ne', Real.log_pow] at hl3
  have hΛ : Real.log (Γ.n 0) + ((Γ.Apre m : ℝ) * Real.log 2 - m * Real.log 3) ≤
      (m : ℝ) / 70 * Real.log 2 := by
    linarith
  exact Γ.no_three_mismatch_of_small_drift hprim hapos hm hΛ hh1 hhm hs

end OddCycle

/-! ### S12-a: the discrete Denjoy–Koksma inequality at a single convergent

For an `m`-periodic `f : ℕ → ℝ` of zero mean over a period and a rotation `h` with a rational
approximation `p/q`: `q h = p m + r`, `0 ≤ r`, `q r < m` (that is `0 ≤ h/m − p/q < 1/q²`), `gcd(p, q)
= 1`: `|Σ_{k<q} f(x + k h)| ≤ Σ_{t<m} |f(t+1) − f(t)|` for every start `x` (`dk_core` for `x = 0`,
`dk_discrete` in general). The proof is the one-point-per-cell argument in coordinates scaled by `q`:
position `t` occupies the block `[qt, qt+q)` and cell `j < q` the interval `[jm, jm+m)`, both tiling
`[0, qm)`; the chain point `k` lies in the cell `J k ≡ k p (mod q)` (`J_spec`), a bijection of
`[0, q)` (`J_lt`, injectivity by coprimality); with the integer weights `w j t = #(block t ∩ cell j)`
(`sum_w_t`, `sum_w_j`), `m Σ_k f(c_k) = Σ_k Σ_t w (J k) t (f c_k − f t)`, each cell's contribution
is bounded by the variation of `f` over the positions touching the cell (`w_pos_bounds`,
`abs_sub_le_var_window`), and those windows are disjoint across cells (`windows_disjoint`,
`sum_windows_le`). Applied to the height profile `μ_h(t) = log n_{t+h} − log n_t` of a cycle, whose
chain sums telescope, this is the side lane's S12 (1): `|log n_{x+qh} − log n_x| ≤ Var(μ_h)`
(`OddCycle.dk_log`). Every convergent `p/q` of `h/m` with `q < m` satisfies the hypotheses (with
`h` replaced by `m − h` when `qh < pm`); nothing else about the cycle is used. -/

namespace DK

theorem card_filter_div {N d j : ℕ} (hd : 0 < d) (hj : (j + 1) * d ≤ N) :
    ((Finset.range N).filter (fun u => u / d = j)).card = d := by
  have he : (Finset.range N).filter (fun u => u / d = j) = Finset.Ico (j * d) (j * d + d) := by
    ext u
    rw [Finset.mem_filter, Finset.mem_range, Finset.mem_Ico]
    constructor
    · rintro ⟨_, hu⟩
      have h1 := Nat.div_add_mod' u d
      have h2 := Nat.mod_lt u hd
      rw [hu] at h1
      omega
    · rintro ⟨h1, h2⟩
      refine ⟨?_, ?_⟩
      · calc u < j * d + d := h2
          _ = (j + 1) * d := by ring
          _ ≤ N := hj
      · exact Nat.div_eq_of_lt_le h1 (by rw [add_mul, one_mul]; exact h2)
  rw [he, Nat.card_Ico, Nat.add_sub_cancel_left]

/-- The weight of position `t` in cell `j`, in coordinates scaled by `q`. -/
def w (m q j t : ℕ) : ℕ :=
  ((Finset.range (q * m)).filter (fun u => u / m = j ∧ u / q = t)).card

/-- Each cell has total weight `m`. -/
theorem sum_w_t {m q j : ℕ} (hm : 0 < m) (hq : 0 < q) (hj : j < q) :
    ∑ t ∈ Finset.range m, w m q j t = m := by
  have hcard := card_filter_div (N := q * m) (d := m) (j := j) hm (Nat.mul_le_mul_right m hj)
  have hmaps : Set.MapsTo (fun u => u / q)
      (↑((Finset.range (q * m)).filter (fun u => u / m = j)) : Set ℕ)
      (↑(Finset.range m) : Set ℕ) := by
    intro u hu
    rw [Finset.mem_coe, Finset.mem_filter, Finset.mem_range] at hu
    rw [Finset.mem_coe, Finset.mem_range]
    exact (Nat.div_lt_iff_lt_mul hq).mpr (by rw [Nat.mul_comm]; exact hu.1)
  have hfib := Finset.card_eq_sum_card_fiberwise hmaps
  calc ∑ t ∈ Finset.range m, w m q j t
      = ∑ t ∈ Finset.range m,
          (((Finset.range (q * m)).filter (fun u => u / m = j)).filter (fun u => u / q = t)).card := by
        apply Finset.sum_congr rfl
        intro t _
        unfold w
        rw [Finset.filter_filter]
    _ = ((Finset.range (q * m)).filter (fun u => u / m = j)).card := hfib.symm
    _ = m := hcard

/-- Each position has total weight `q`. -/
theorem sum_w_j {m q t : ℕ} (hm : 0 < m) (hq : 0 < q) (ht : t < m) :
    ∑ j ∈ Finset.range q, w m q j t = q := by
  have hcard := card_filter_div (N := q * m) (d := q) (j := t) hq
    (by rw [Nat.mul_comm q m]; exact Nat.mul_le_mul_right q ht)
  have hmaps : Set.MapsTo (fun u => u / m)
      (↑((Finset.range (q * m)).filter (fun u => u / q = t)) : Set ℕ)
      (↑(Finset.range q) : Set ℕ) := by
    intro u hu
    rw [Finset.mem_coe, Finset.mem_filter, Finset.mem_range] at hu
    rw [Finset.mem_coe, Finset.mem_range]
    exact (Nat.div_lt_iff_lt_mul hm).mpr hu.1
  have hfib := Finset.card_eq_sum_card_fiberwise hmaps
  calc ∑ j ∈ Finset.range q, w m q j t
      = ∑ j ∈ Finset.range q,
          (((Finset.range (q * m)).filter (fun u => u / q = t)).filter (fun u => u / m = j)).card := by
        apply Finset.sum_congr rfl
        intro j _
        unfold w
        rw [Finset.filter_filter]
        congr 1
        exact Finset.filter_congr (fun u _ => and_comm)
    _ = ((Finset.range (q * m)).filter (fun u => u / q = t)).card := hfib.symm
    _ = q := hcard

/-- A position of positive weight in cell `j` lies in the window `[jm/q, (jm+m−1)/q]`. -/
theorem w_pos_bounds {m q j t : ℕ} (hm : 0 < m) (hq : 0 < q) (hw : 0 < w m q j t) :
    j * m / q ≤ t ∧ t ≤ (j * m + m - 1) / q := by
  unfold w at hw
  rw [Finset.card_pos] at hw
  obtain ⟨u, hu⟩ := hw
  rw [Finset.mem_filter, Finset.mem_range] at hu
  obtain ⟨_, huj, hut⟩ := hu
  have h1 := Nat.div_add_mod' u m
  have h2 := Nat.mod_lt u hm
  have h3 := Nat.div_add_mod' u q
  have h4 := Nat.mod_lt u hq
  rw [huj] at h1
  rw [hut] at h3
  constructor
  · have h5 : j * m < (t + 1) * q := by
      rw [add_mul, one_mul]
      omega
    exact Nat.le_of_lt_succ ((Nat.div_lt_iff_lt_mul hq).mpr h5)
  · apply (Nat.le_div_iff_mul_le hq).mpr
    omega

/-- Telescoping: `|f b − f a| ≤ Σ_{a ≤ s < b} |f(s+1) − f(s)|`. -/
theorem abs_sub_le_sum_jumps (f : ℕ → ℝ) {a b : ℕ} (hab : a ≤ b) :
    |f b - f a| ≤ ∑ s ∈ Finset.Ico a b, |f (s + 1) - f s| := by
  induction b, hab using Nat.le_induction with
  | base => simp
  | succ b hab ih =>
    rw [Finset.sum_Ico_succ_top hab]
    calc |f (b + 1) - f a| ≤ |f (b + 1) - f b| + |f b - f a| := abs_sub_le _ _ _
      _ ≤ |f (b + 1) - f b| + ∑ s ∈ Finset.Ico a b, |f (s + 1) - f s| := by linarith
      _ = ∑ s ∈ Finset.Ico a b, |f (s + 1) - f s| + |f (b + 1) - f b| := by ring

/-- Two positions in the window `[lo, hi]` differ by at most the variation over the window. -/
theorem abs_sub_le_var_window (f : ℕ → ℝ) {lo hi a b : ℕ} (ha1 : lo ≤ a) (ha2 : a ≤ hi)
    (hb1 : lo ≤ b) (hb2 : b ≤ hi) :
    |f b - f a| ≤ ∑ s ∈ Finset.Ico lo hi, |f (s + 1) - f s| := by
  rcases le_total a b with hab | hba
  · calc |f b - f a| ≤ ∑ s ∈ Finset.Ico a b, |f (s + 1) - f s| := abs_sub_le_sum_jumps f hab
      _ ≤ ∑ s ∈ Finset.Ico lo hi, |f (s + 1) - f s| :=
          Finset.sum_le_sum_of_subset_of_nonneg (Finset.Ico_subset_Ico ha1 hb2)
            (fun _ _ _ => abs_nonneg _)
  · rw [abs_sub_comm]
    calc |f a - f b| ≤ ∑ s ∈ Finset.Ico b a, |f (s + 1) - f s| := abs_sub_le_sum_jumps f hba
      _ ≤ ∑ s ∈ Finset.Ico lo hi, |f (s + 1) - f s| :=
          Finset.sum_le_sum_of_subset_of_nonneg (Finset.Ico_subset_Ico hb1 ha2)
            (fun _ _ _ => abs_nonneg _)

/-- The windows of distinct cells are disjoint. -/
theorem windows_disjoint {m q : ℕ} :
    (↑(Finset.range q) : Set ℕ).PairwiseDisjoint
      (fun j => Finset.Ico (j * m / q) ((j * m + m - 1) / q)) := by
  intro j _ j' _ hne
  have key : ∀ a b : ℕ, a < b →
      Disjoint (Finset.Ico (a * m / q) ((a * m + m - 1) / q))
        (Finset.Ico (b * m / q) ((b * m + m - 1) / q)) := by
    intro a b hab
    have h1 : (a + 1) * m ≤ b * m := Nat.mul_le_mul_right m hab
    rw [add_mul, one_mul] at h1
    have h2 : (a * m + m - 1) / q ≤ b * m / q := Nat.div_le_div_right (by omega)
    rw [Finset.disjoint_left]
    intro s hs hs'
    rw [Finset.mem_Ico] at hs hs'
    omega
  rcases Nat.lt_or_gt_of_ne hne with hlt | hlt
  · exact key j j' hlt
  · exact (key j' j hlt).symm

/-- The sum over all windows of a nonnegative function is at most the sum over a period. -/
theorem sum_windows_le {m q : ℕ} (hm : 0 < m) (hq : 0 < q) (g : ℕ → ℝ) (hg : ∀ s, 0 ≤ g s) :
    ∑ j ∈ Finset.range q, ∑ s ∈ Finset.Ico (j * m / q) ((j * m + m - 1) / q), g s ≤
      ∑ s ∈ Finset.range m, g s := by
  rw [← Finset.sum_biUnion windows_disjoint]
  apply Finset.sum_le_sum_of_subset_of_nonneg
  · intro s hs
    rw [Finset.mem_biUnion] at hs
    obtain ⟨j, hj, hs⟩ := hs
    rw [Finset.mem_range] at hj ⊢
    rw [Finset.mem_Ico] at hs
    have h1 : (j * m + m - 1) / q ≤ (q * m - 1) / q := by
      apply Nat.div_le_div_right
      have h1' : (j + 1) * m ≤ q * m := Nat.mul_le_mul_right m hj
      rw [add_mul, one_mul] at h1'
      omega
    have h2 : (q * m - 1) / q < m := by
      rw [Nat.div_lt_iff_lt_mul hq, Nat.mul_comm m q]
      have : 0 < q * m := Nat.mul_pos hq hm
      omega
    omega
  · intro s _ _
    exact hg s

/-- The cell of the chain point `k`: `J k = k p − q ⌊k h / m⌋`. -/
def J (m q p h k : ℕ) : ℕ := k * p - q * (k * h / m)

theorem J_add {m q p h r k : ℕ} (hr : q * h = p * m + r) (hqr : q * r < m) (hk : k < q) :
    J m q p h k + q * (k * h / m) = k * p := by
  unfold J
  apply Nat.sub_add_cancel
  by_contra hlt
  have hlt' : k * p + 1 ≤ q * (k * h / m) := not_le.mp hlt
  have h1 : (k * p + 1) * m ≤ q * (k * h / m) * m := Nat.mul_le_mul_right m hlt'
  have h2 : k * h / m * m ≤ k * h := Nat.div_mul_le_self (k * h) m
  have h3 : q * (k * h / m) * m ≤ q * (k * h) := by
    rw [Nat.mul_assoc]
    exact Nat.mul_le_mul_left q h2
  have h4 : q * (k * h) = k * (p * m) + k * r := by
    calc q * (k * h) = k * (q * h) := by ring
      _ = k * (p * m + r) := by rw [hr]
      _ = k * (p * m) + k * r := by ring
  have h5 : k * r < m := by
    calc k * r ≤ q * r := Nat.mul_le_mul_right r hk.le
      _ < m := hqr
  have h6 : (k * p + 1) * m ≤ k * (p * m) + k * r := le_trans h1 (le_trans h3 h4.le)
  have e1 : (k * p + 1) * m = k * (p * m) + m := by ring
  omega

theorem J_spec {m q p h r k : ℕ} (hr : q * h = p * m + r) (hqr : q * r < m) (hk : k < q) :
    m * J m q p h k + k * r = q * (k * h % m) := by
  have hJ := J_add hr hqr hk
  have hdm := Nat.div_add_mod (k * h) m
  zify at hJ hdm hr ⊢
  linear_combination (m : ℤ) * hJ - (q : ℤ) * hdm - (k : ℤ) * hr

theorem J_lt {m q p h r k : ℕ} (hm : 0 < m) (hq : 0 < q) (hr : q * h = p * m + r)
    (hqr : q * r < m) (hk : k < q) : J m q p h k < q := by
  have hs := J_spec hr hqr hk
  have hmod : k * h % m < m := Nat.mod_lt (k * h) hm
  have h1 : q * (k * h % m) < q * m := Nat.mul_lt_mul_of_pos_left hmod hq
  have h2 : m * J m q p h k < m * q := by
    calc m * J m q p h k ≤ m * J m q p h k + k * r := Nat.le_add_right _ _
      _ = q * (k * h % m) := hs
      _ < q * m := h1
      _ = m * q := Nat.mul_comm q m
  exact Nat.lt_of_mul_lt_mul_left h2

theorem J_mod {m q p h r k : ℕ} (hr : q * h = p * m + r) (hqr : q * r < m) (hk : k < q) :
    J m q p h k % q = k * p % q := by
  have hJ := J_add hr hqr hk
  rw [← hJ, Nat.add_mul_mod_self_left]

theorem J_injOn {m q p h r : ℕ} (hr : q * h = p * m + r) (hqr : q * r < m)
    (hcop : Nat.Coprime p q) : Set.InjOn (J m q p h) (↑(Finset.range q) : Set ℕ) := by
  intro k hk k' hk' heq
  rw [Finset.mem_coe, Finset.mem_range] at hk hk'
  have h1 := J_mod hr hqr hk
  have h2 := J_mod hr hqr hk'
  have h3 : k * p ≡ k' * p [MOD q] := by
    unfold Nat.ModEq
    rw [← h1, ← h2, heq]
  have h4 : k ≡ k' [MOD q] := Nat.ModEq.cancel_right_of_coprime hcop.symm.gcd_eq_one h3
  unfold Nat.ModEq at h4
  rwa [Nat.mod_eq_of_lt hk, Nat.mod_eq_of_lt hk'] at h4

theorem J_image {m q p h r : ℕ} (hm : 0 < m) (hq : 0 < q) (hr : q * h = p * m + r)
    (hqr : q * r < m) (hcop : Nat.Coprime p q) :
    (Finset.range q).image (J m q p h) = Finset.range q := by
  apply Finset.eq_of_subset_of_card_le
  · intro j hj
    rw [Finset.mem_image] at hj
    obtain ⟨k, hk, rfl⟩ := hj
    rw [Finset.mem_range] at hk ⊢
    exact J_lt hm hq hr hqr hk
  · rw [Finset.card_image_of_injOn (J_injOn hr hqr hcop)]

/-- The chain point `k` has positive weight in its cell `J k`. -/
theorem w_J_pos {m q p h r k : ℕ} (hm : 0 < m) (hq : 0 < q) (hr : q * h = p * m + r)
    (hqr : q * r < m) (hk : k < q) : 0 < w m q (J m q p h k) (k * h % m) := by
  have hs := J_spec hr hqr hk
  have hkr : k * r < m := by
    calc k * r ≤ q * r := Nat.mul_le_mul_right r hk.le
      _ < m := hqr
  unfold w
  apply Finset.card_pos.mpr
  refine ⟨q * (k * h % m), ?_⟩
  rw [Finset.mem_filter, Finset.mem_range]
  refine ⟨?_, ?_, ?_⟩
  · exact Nat.mul_lt_mul_of_pos_left (Nat.mod_lt (k * h) hm) hq
  · have e : J m q p h k * m = m * J m q p h k := Nat.mul_comm _ _
    apply Nat.div_eq_of_lt_le
    · omega
    · rw [add_mul, one_mul]
      omega
  · exact Nat.mul_div_cancel_left _ hq

/-- Shift invariance of a periodic sum over a period. -/
theorem sum_range_shift {m : ℕ} (f : ℕ → ℝ) (hper : ∀ t, f (t + m) = f t) (x : ℕ) :
    ∑ t ∈ Finset.range m, f (x + t) = ∑ t ∈ Finset.range m, f t := by
  induction x with
  | zero => simp
  | succ x ih =>
    rw [← ih]
    rcases Nat.eq_zero_or_pos m with hm0 | hmpos
    · subst hm0
      simp
    · obtain ⟨n, rfl⟩ := Nat.exists_eq_succ_of_ne_zero hmpos.ne'
      rw [Finset.sum_range_succ, Finset.sum_range_succ' (fun t => f (x + t))]
      have h1 : f (x + 1 + n) = f (x + 0) := by
        rw [Nat.add_zero, show x + 1 + n = x + (n + 1) by omega]
        exact hper x
      rw [h1]
      congr 1
      apply Finset.sum_congr rfl
      intro t _
      congr 1
      omega

/-- **The discrete Denjoy–Koksma inequality**, chain starting at `0`. -/
theorem dk_core {m q p h r : ℕ} (f : ℕ → ℝ) (hper : ∀ t, f (t + m) = f t)
    (hmean : ∑ t ∈ Finset.range m, f t = 0) (hm : 0 < m) (hq : 0 < q)
    (hr : q * h = p * m + r) (hqr : q * r < m) (hcop : Nat.Coprime p q) :
    |∑ k ∈ Finset.range q, f (k * h)| ≤ ∑ t ∈ Finset.range m, |f (t + 1) - f t| := by
  -- periodic reduction
  have fmod : ∀ t, f (t % m) = f t := by
    intro t
    have : ∀ n, f (t % m + m * n) = f (t % m) := by
      intro n
      induction n with
      | zero => simp
      | succ n ih => rw [Nat.mul_succ, ← Nat.add_assoc, hper, ih]
    conv_rhs => rw [← Nat.mod_add_div t m]
    exact (this _).symm
  have hS : ∑ k ∈ Finset.range q, f (k * h) = ∑ k ∈ Finset.range q, f (k * h % m) :=
    Finset.sum_congr rfl (fun k _ => (fmod (k * h)).symm)
  rw [hS]
  -- weights
  have hW2 : ∀ k ∈ Finset.range q, ∑ t ∈ Finset.range m, (w m q (J m q p h k) t : ℝ) = m := by
    intro k hk
    rw [Finset.mem_range] at hk
    exact_mod_cast sum_w_t hm hq (J_lt hm hq hr hqr hk)
  have hW1 : ∀ t ∈ Finset.range m, ∑ j ∈ Finset.range q, (w m q j t : ℝ) = q := by
    intro t ht
    rw [Finset.mem_range] at ht
    exact_mod_cast sum_w_j hm hq ht
  have hJinj := J_injOn hr hqr hcop
  have hJimg := J_image hm hq hr hqr hcop
  -- the weighted sum of `f` over all cells vanishes
  have hzero : ∑ k ∈ Finset.range q, ∑ t ∈ Finset.range m,
      (w m q (J m q p h k) t : ℝ) * f t = 0 := by
    have h1 : ∑ k ∈ Finset.range q, ∑ t ∈ Finset.range m, (w m q (J m q p h k) t : ℝ) * f t
        = ∑ j ∈ Finset.range q, ∑ t ∈ Finset.range m, (w m q j t : ℝ) * f t := by
      conv_rhs => rw [← hJimg]
      rw [Finset.sum_image hJinj]
    rw [h1, Finset.sum_comm]
    have h2 : ∀ t ∈ Finset.range m,
        ∑ j ∈ Finset.range q, (w m q j t : ℝ) * f t = (q : ℝ) * f t := by
      intro t ht
      rw [← Finset.sum_mul, hW1 t ht]
    rw [Finset.sum_congr rfl h2, ← Finset.mul_sum, hmean, mul_zero]
  -- the key identity
  have hident : (m : ℝ) * ∑ k ∈ Finset.range q, f (k * h % m) =
      ∑ k ∈ Finset.range q, ∑ t ∈ Finset.range m,
        (w m q (J m q p h k) t : ℝ) * (f (k * h % m) - f t) := by
    have h1 : ∀ k ∈ Finset.range q, ∑ t ∈ Finset.range m,
        (w m q (J m q p h k) t : ℝ) * (f (k * h % m) - f t) =
        (m : ℝ) * f (k * h % m) - ∑ t ∈ Finset.range m, (w m q (J m q p h k) t : ℝ) * f t := by
      intro k hk
      have e : ∀ t, (w m q (J m q p h k) t : ℝ) * (f (k * h % m) - f t) =
          (w m q (J m q p h k) t : ℝ) * f (k * h % m) - (w m q (J m q p h k) t : ℝ) * f t :=
        fun t => mul_sub _ _ _
      rw [Finset.sum_congr rfl (fun t _ => e t), Finset.sum_sub_distrib, ← Finset.sum_mul,
        hW2 k hk]
    rw [Finset.sum_congr rfl h1, Finset.sum_sub_distrib, hzero, sub_zero, ← Finset.mul_sum]
  -- the pointwise bound by the window variation
  have hbound : ∀ k ∈ Finset.range q, ∀ t ∈ Finset.range m,
      (w m q (J m q p h k) t : ℝ) * |f (k * h % m) - f t| ≤
        (w m q (J m q p h k) t : ℝ) *
          ∑ s ∈ Finset.Ico (J m q p h k * m / q) ((J m q p h k * m + m - 1) / q),
            |f (s + 1) - f s| := by
    intro k hk t _
    rw [Finset.mem_range] at hk
    rcases Nat.eq_zero_or_pos (w m q (J m q p h k) t) with h0 | hpos
    · rw [h0]
      simp
    · apply mul_le_mul_of_nonneg_left _ (Nat.cast_nonneg _)
      obtain ⟨ht1, ht2⟩ := w_pos_bounds hm hq hpos
      obtain ⟨hc1, hc2⟩ := w_pos_bounds hm hq (w_J_pos hm hq hr hqr hk)
      exact abs_sub_le_var_window f ht1 ht2 hc1 hc2
  have hmpos : (0 : ℝ) < m := by exact_mod_cast hm
  have hmain : (m : ℝ) * |∑ k ∈ Finset.range q, f (k * h % m)| ≤
      (m : ℝ) * ∑ t ∈ Finset.range m, |f (t + 1) - f t| := by
    calc (m : ℝ) * |∑ k ∈ Finset.range q, f (k * h % m)|
        = |(m : ℝ) * ∑ k ∈ Finset.range q, f (k * h % m)| := by
          rw [abs_mul, abs_of_pos hmpos]
      _ = |∑ k ∈ Finset.range q, ∑ t ∈ Finset.range m,
            (w m q (J m q p h k) t : ℝ) * (f (k * h % m) - f t)| := by rw [hident]
      _ ≤ ∑ k ∈ Finset.range q, ∑ t ∈ Finset.range m,
            |(w m q (J m q p h k) t : ℝ) * (f (k * h % m) - f t)| := by
          refine (Finset.abs_sum_le_sum_abs _ _).trans ?_
          exact Finset.sum_le_sum (fun k _ => Finset.abs_sum_le_sum_abs _ _)
      _ = ∑ k ∈ Finset.range q, ∑ t ∈ Finset.range m,
            (w m q (J m q p h k) t : ℝ) * |f (k * h % m) - f t| := by
          apply Finset.sum_congr rfl
          intro k _
          apply Finset.sum_congr rfl
          intro t _
          rw [abs_mul, abs_of_nonneg (Nat.cast_nonneg _)]
      _ ≤ ∑ k ∈ Finset.range q, ∑ t ∈ Finset.range m, (w m q (J m q p h k) t : ℝ) *
            ∑ s ∈ Finset.Ico (J m q p h k * m / q) ((J m q p h k * m + m - 1) / q),
              |f (s + 1) - f s| := by
          apply Finset.sum_le_sum
          intro k hk
          apply Finset.sum_le_sum
          intro t ht
          exact hbound k hk t ht
      _ = ∑ k ∈ Finset.range q, (m : ℝ) *
            ∑ s ∈ Finset.Ico (J m q p h k * m / q) ((J m q p h k * m + m - 1) / q),
              |f (s + 1) - f s| := by
          apply Finset.sum_congr rfl
          intro k hk
          rw [← Finset.sum_mul, hW2 k hk]
      _ = (m : ℝ) * ∑ j ∈ Finset.range q,
            ∑ s ∈ Finset.Ico (j * m / q) ((j * m + m - 1) / q), |f (s + 1) - f s| := by
          rw [← Finset.mul_sum]
          congr 1
          conv_rhs => rw [← hJimg]
          rw [Finset.sum_image hJinj]
      _ ≤ (m : ℝ) * ∑ t ∈ Finset.range m, |f (t + 1) - f t| := by
          apply mul_le_mul_of_nonneg_left _ (Nat.cast_nonneg _)
          exact sum_windows_le hm hq (fun s => |f (s + 1) - f s|) (fun s => abs_nonneg _)
  exact le_of_mul_le_mul_left hmain hmpos

/-- **The discrete Denjoy–Koksma inequality**, chain starting anywhere. -/
theorem dk_discrete {m q p h r : ℕ} (f : ℕ → ℝ) (hper : ∀ t, f (t + m) = f t)
    (hmean : ∑ t ∈ Finset.range m, f t = 0) (hm : 0 < m) (hq : 0 < q)
    (hr : q * h = p * m + r) (hqr : q * r < m) (hcop : Nat.Coprime p q) (x : ℕ) :
    |∑ k ∈ Finset.range q, f (x + k * h)| ≤ ∑ t ∈ Finset.range m, |f (t + 1) - f t| := by
  have hper' : ∀ t, f (x + (t + m)) = f (x + t) := by
    intro t
    rw [← Nat.add_assoc, hper]
  have hmean' : ∑ t ∈ Finset.range m, f (x + t) = 0 := by
    rw [sum_range_shift f hper x, hmean]
  have h : |∑ k ∈ Finset.range q, f (x + k * h)| ≤
      ∑ t ∈ Finset.range m, |f (x + (t + 1)) - f (x + t)| :=
    dk_core (fun t => f (x + t)) hper' hmean' hm hq hr hqr hcop
  refine h.trans (le_of_eq ?_)
  have hg : ∀ t, |f (t + m + 1) - f (t + m)| = |f (t + 1) - f t| := by
    intro t
    rw [show t + m + 1 = t + 1 + m by omega, hper, hper]
  have hsh : ∑ t ∈ Finset.range m, |f (x + t + 1) - f (x + t)| =
      ∑ t ∈ Finset.range m, |f (t + 1) - f t| :=
    sum_range_shift (fun t => |f (t + 1) - f t|) hg x
  rw [← hsh]
  apply Finset.sum_congr rfl
  intro t _
  rw [Nat.add_assoc]

end DK

namespace OddCycle

variable {m : ℕ} (Γ : OddCycle m)

/-- **S12 (1) for a cycle.** For a rational approximation `p/q` of `h/m` with `q h = p m + r`,
`0 ≤ r`, `q r < m`, `gcd(p, q) = 1`, and every `x`: `|log n_{x+qh} − log n_x| ≤ Var(μ_h)`, with
`μ_h(t) = log n_{t+h} − log n_t` (natural logarithms; every proper convergent of `h/m` qualifies,
with `h` replaced by `m − h` when `q h < p m`). -/
theorem dk_log {q p h r : ℕ} (hq : 0 < q) (hr : q * h = p * m + r) (hqr : q * r < m)
    (hcop : Nat.Coprime p q) (x : ℕ) :
    |Real.log (Γ.n (x + q * h)) - Real.log (Γ.n x)| ≤
      ∑ t ∈ Finset.range m, |(Real.log (Γ.n (t + 1 + h)) - Real.log (Γ.n (t + 1))) -
        (Real.log (Γ.n (t + h)) - Real.log (Γ.n t))| := by
  have hper : ∀ t, Real.log (Γ.n (t + m + h)) - Real.log (Γ.n (t + m)) =
      Real.log (Γ.n (t + h)) - Real.log (Γ.n t) := by
    intro t
    rw [Nat.add_right_comm t m h, Γ.nper, Γ.nper]
  have hmean : ∑ t ∈ Finset.range m, (Real.log (Γ.n (t + h)) - Real.log (Γ.n t)) = 0 := by
    rw [Finset.sum_sub_distrib, sub_eq_zero]
    have hsh : ∑ t ∈ Finset.range m, Real.log (Γ.n (h + t)) =
        ∑ t ∈ Finset.range m, Real.log (Γ.n t) :=
      DK.sum_range_shift (fun t => Real.log (Γ.n t)) (fun t => by rw [Γ.nper]) h
    rw [← hsh]
    apply Finset.sum_congr rfl
    intro t _
    rw [Nat.add_comm]
  have hdk : |∑ k ∈ Finset.range q,
      (Real.log (Γ.n (x + k * h + h)) - Real.log (Γ.n (x + k * h)))| ≤
      ∑ t ∈ Finset.range m, |(Real.log (Γ.n (t + 1 + h)) - Real.log (Γ.n (t + 1))) -
        (Real.log (Γ.n (t + h)) - Real.log (Γ.n t))| :=
    DK.dk_discrete (fun t => Real.log (Γ.n (t + h)) - Real.log (Γ.n t)) hper hmean Γ.hm hq hr
      hqr hcop x
  have htel : ∑ k ∈ Finset.range q,
      (Real.log (Γ.n (x + k * h + h)) - Real.log (Γ.n (x + k * h))) =
      Real.log (Γ.n (x + q * h)) - Real.log (Γ.n x) := by
    have hs := Finset.sum_range_sub (fun k => Real.log (Γ.n (x + k * h))) q
    simp only [zero_mul, add_zero] at hs
    rw [← hs]
    apply Finset.sum_congr rfl
    intro k _
    rw [show x + (k + 1) * h = x + k * h + h by ring]
  rw [← htel]
  exact hdk

end OddCycle

/-! ### S12-b: Denjoy–Koksma for either sign, the greedy Ostrowski ladder, and the ladder walk

The first half of S12 (2). `varMu h` is the variation of `μ_h(t) = log n_{t+h} − log n_t` over a
period; it is invariant under `h ↦ m − h` (`varMu_neg`: `μ_{m−h}(t) = −μ_h(t − h)`), which gives
the DK step for either sign of `q h − p m` (`dk_log_either`, replacing `h` by `m − h` and reading the
chain backwards). Iterating a block `c` times gives `|log n_{x + c q h} − log n_x| ≤ c·Var`
(`dk_log_iter`), and a whole ladder `N = Σ_{i<n} b_i q_i` of admissible denominators gives
`|log n_{x + N h} − log n_x| ≤ (Σ b_i)·Var` (`dk_walk`). The arithmetic half: for a
continued-fraction denominator ladder `q 0 = 1`, `q 1 = a 1`, `q (i+2) = a (i+2) q (i+1) + q i`
with partial quotients `a i ≥ 1` (`Ladder`), every `N < q n` has a greedy decomposition
`N = Σ_{i<n} b_i q_i` with `Σ_{i<n} b_i + 1 ≤ Σ_{1 ≤ i ≤ n} a i` (`ostrowski_greedy`): the side lane's
`Σ b_i ≤ K − 1`. The DK admissibility of the convergents (`|q_i h − p_i m| < m/q_i`) is taken as a
hypothesis on the ladder, not derived from continued-fraction theory. The assembly into the height
bound `B ≤ (K − 1)·Var(μ_h)` for `gcd(h, m) = 1` is the second half (S12-c). -/

namespace DK

/-- A continued-fraction denominator ladder: `q 0 = 1`, `q 1 = a 1`,
`q (i+2) = a (i+2) q (i+1) + q i`, with all partial quotients `a i ≥ 1` for `i ≥ 1`. -/
structure Ladder (q a : ℕ → ℕ) : Prop where
  q0 : q 0 = 1
  q1 : q 1 = a 1
  step : ∀ i, q (i + 2) = a (i + 2) * q (i + 1) + q i
  apos : ∀ i, 1 ≤ i → 1 ≤ a i

theorem ladder_mono {q a : ℕ → ℕ} (L : Ladder q a) : ∀ i, q i ≤ q (i + 1) := by
  intro i
  cases i with
  | zero =>
    show q 0 ≤ q 1
    rw [L.q0, L.q1]
    exact L.apos 1 le_rfl
  | succ i =>
    show q (i + 1) ≤ q (i + 2)
    rw [L.step i]
    have ha : 0 < a (i + 2) := L.apos (i + 2) (by omega)
    have : q (i + 1) ≤ a (i + 2) * q (i + 1) := Nat.le_mul_of_pos_left _ ha
    omega

theorem ladder_pos {q a : ℕ → ℕ} (L : Ladder q a) : ∀ i, 1 ≤ q i := by
  intro i
  induction i with
  | zero => rw [L.q0]
  | succ i ih => exact le_trans ih (ladder_mono L i)

/-- **The greedy Ostrowski decomposition.** Every `N < q n` (`n ≥ 1`) is `Σ_{i<n} b i q i` with
`Σ_{i<n} b i + 1 ≤ Σ_{1 ≤ i ≤ n} a i`. -/
theorem ostrowski_greedy {q a : ℕ → ℕ} (L : Ladder q a) : ∀ n, 1 ≤ n → ∀ N, N < q n →
    ∃ b : ℕ → ℕ, N = ∑ i ∈ Finset.range n, b i * q i ∧
      ∑ i ∈ Finset.range n, b i + 1 ≤ ∑ i ∈ Finset.Icc 1 n, a i := by
  intro n hn
  induction n, hn using Nat.le_induction with
  | base =>
    intro N hN
    rw [L.q1] at hN
    refine ⟨fun _ => N, ?_, ?_⟩
    · simp [L.q0]
    · simp only [Finset.sum_range_one, Finset.Icc_self, Finset.sum_singleton]
      omega
  | succ n hn ih =>
    intro N hN
    have hqn : 1 ≤ q n := ladder_pos L n
    obtain ⟨b', hb'1, hb'2⟩ := ih (N % q n) (Nat.mod_lt N hqn)
    have hdiv : N / q n ≤ a (n + 1) := by
      obtain ⟨k, rfl⟩ := Nat.exists_eq_succ_of_ne_zero (by omega : n ≠ 0)
      have hN' : N < q (k + 2) := hN
      rw [L.step k] at hN'
      have hmono := ladder_mono L k
      have h1 : N < (a (k + 2) + 1) * q (k + 1) := by
        calc N < a (k + 2) * q (k + 1) + q k := hN'
          _ ≤ a (k + 2) * q (k + 1) + q (k + 1) := by omega
          _ = (a (k + 2) + 1) * q (k + 1) := by ring
      exact Nat.le_of_lt_succ ((Nat.div_lt_iff_lt_mul hqn).mpr h1)
    have e1 : (fun i => if i = n then N / q n else b' i) n = N / q n := by simp
    have e2 : ∀ i ∈ Finset.range n, (fun i => if i = n then N / q n else b' i) i = b' i := by
      intro i hi
      have hne : i ≠ n := (Finset.mem_range.mp hi).ne
      simp [hne]
    have e3 : ∑ i ∈ Finset.range n, (fun i => if i = n then N / q n else b' i) i * q i =
        ∑ i ∈ Finset.range n, b' i * q i :=
      Finset.sum_congr rfl (fun i hi => by rw [e2 i hi])
    refine ⟨fun i => if i = n then N / q n else b' i, ?_, ?_⟩
    · rw [Finset.sum_range_succ, e1, e3, ← hb'1]
      exact (Nat.mod_add_div' N (q n)).symm
    · have e1' : (if n = n then N / q n else b' n) = N / q n := by simp
      have e4' : (∑ x ∈ Finset.range n, if x = n then N / q n else b' x) =
          ∑ i ∈ Finset.range n, b' i :=
        Finset.sum_congr rfl (fun i hi => by
          have hne : i ≠ n := (Finset.mem_range.mp hi).ne
          simp [hne])
      rw [Finset.sum_range_succ, e1', e4', Finset.sum_Icc_succ_top (by omega : 1 ≤ n + 1)]
      omega

end DK

namespace OddCycle

variable {m : ℕ} (Γ : OddCycle m)

/-- The variation of the height profile `μ_h(t) = log n_{t+h} − log n_t` over a period. -/
noncomputable def varMu (h : ℕ) : ℝ :=
  ∑ t ∈ Finset.range m, |(Real.log (Γ.n (t + 1 + h)) - Real.log (Γ.n (t + 1))) -
    (Real.log (Γ.n (t + h)) - Real.log (Γ.n t))|

/-- `Var(μ_{m−h}) = Var(μ_h)`: `μ_{m−h}(t) = −μ_h(t − h)`, a shift of a sign change. -/
theorem varMu_neg {h : ℕ} (hhm : h ≤ m) : Γ.varMu (m - h) = Γ.varMu h := by
  unfold varMu
  have hg : ∀ s, |(Real.log (Γ.n (s + m + 1 + h)) - Real.log (Γ.n (s + m + 1))) -
      (Real.log (Γ.n (s + m + h)) - Real.log (Γ.n (s + m)))| =
      |(Real.log (Γ.n (s + 1 + h)) - Real.log (Γ.n (s + 1))) -
        (Real.log (Γ.n (s + h)) - Real.log (Γ.n s))| := by
    intro s
    rw [show s + m + 1 + h = s + 1 + h + m by omega, show s + m + 1 = s + 1 + m by omega,
      show s + m + h = s + h + m by omega, Γ.nper, Γ.nper, Γ.nper, Γ.nper]
  have hsh : ∑ t ∈ Finset.range m,
      |(Real.log (Γ.n (m - h + t + 1 + h)) - Real.log (Γ.n (m - h + t + 1))) -
        (Real.log (Γ.n (m - h + t + h)) - Real.log (Γ.n (m - h + t)))| =
      ∑ t ∈ Finset.range m, |(Real.log (Γ.n (t + 1 + h)) - Real.log (Γ.n (t + 1))) -
        (Real.log (Γ.n (t + h)) - Real.log (Γ.n t))| :=
    DK.sum_range_shift (fun s => |(Real.log (Γ.n (s + 1 + h)) - Real.log (Γ.n (s + 1))) -
      (Real.log (Γ.n (s + h)) - Real.log (Γ.n s))|) hg (m - h)
  rw [← hsh]
  apply Finset.sum_congr rfl
  intro t _
  rw [show m - h + t + 1 + h = t + 1 + m by omega, show m - h + t + h = t + m by omega, Γ.nper,
    Γ.nper, show m - h + t + 1 = t + 1 + (m - h) by omega, show m - h + t = t + (m - h) by omega,
    ← abs_neg]
  congr 1
  ring

/-- S12 (1) for either sign of `q h − p m`: `|log n_{x+qh} − log n_x| ≤ Var(μ_h)`. -/
theorem dk_log_either {q p h r : ℕ} (hq : 0 < q) (hhm : h ≤ m)
    (hr : q * h = p * m + r ∨ p * m = q * h + r) (hqr : q * r < m) (hcop : Nat.Coprime p q)
    (x : ℕ) : |Real.log (Γ.n (x + q * h)) - Real.log (Γ.n x)| ≤ Γ.varMu h := by
  rcases hr with hr | hr
  · exact Γ.dk_log hq hr hqr hcop x
  · have hrm : r < m := lt_of_le_of_lt (Nat.le_mul_of_pos_left r hq) hqr
    have hpq : p ≤ q := by
      have h1 : q * h ≤ q * m := Nat.mul_le_mul_left q hhm
      have h2 : p * m < (q + 1) * m := by
        calc p * m = q * h + r := hr
          _ < q * m + m := by omega
          _ = (q + 1) * m := by ring
      exact Nat.le_of_lt_succ (Nat.lt_of_mul_lt_mul_right h2)
    have hr' : q * (m - h) = (q - p) * m + r := by
      zify [hhm, hpq] at hr ⊢
      linear_combination hr
    have hcop' : Nat.Coprime (q - p) q := by
      have e : q = q - p + p := (Nat.sub_add_cancel hpq).symm
      have h1 : Nat.Coprime p (q - p) := by
        have h2 := hcop
        rw [e] at h2
        exact Nat.coprime_add_self_right.mp h2
      have h3 : Nat.Coprime (q - p) (q - p + p) := Nat.coprime_self_add_right.mpr h1.symm
      rwa [← e] at h3
    have hdk := Γ.dk_log hq hr' hqr hcop' (x + q * h)
    have hsum : x + q * h + q * (m - h) = x + q * m := by
      rw [Nat.add_assoc, ← Nat.mul_add, Nat.add_sub_cancel' hhm]
    have hper : Γ.n (x + q * m) = Γ.n x := by
      rw [← Γ.n_mod (x + q * m), Nat.add_mul_mod_self_right, Γ.n_mod]
    rw [hsum, hper, abs_sub_comm] at hdk
    have hvar := Γ.varMu_neg hhm
    unfold varMu at hvar
    unfold varMu
    rw [← hvar]
    exact hdk

/-- Repeating a DK block `c` times: `|log n_{x + c q h} − log n_x| ≤ c · Var(μ_h)`. -/
theorem dk_log_iter {q p h r : ℕ} (hq : 0 < q) (hhm : h ≤ m)
    (hr : q * h = p * m + r ∨ p * m = q * h + r) (hqr : q * r < m) (hcop : Nat.Coprime p q) :
    ∀ c x, |Real.log (Γ.n (x + c * (q * h))) - Real.log (Γ.n x)| ≤ (c : ℝ) * Γ.varMu h := by
  intro c
  induction c with
  | zero =>
    intro x
    simp
  | succ c ih =>
    intro x
    have h1 := ih x
    have h2 := Γ.dk_log_either hq hhm hr hqr hcop (x + c * (q * h))
    rw [show x + (c + 1) * (q * h) = x + c * (q * h) + q * h by ring]
    push_cast
    calc |Real.log (Γ.n (x + c * (q * h) + q * h)) - Real.log (Γ.n x)|
        ≤ |Real.log (Γ.n (x + c * (q * h) + q * h)) - Real.log (Γ.n (x + c * (q * h)))| +
          |Real.log (Γ.n (x + c * (q * h))) - Real.log (Γ.n x)| := abs_sub_le _ _ _
      _ ≤ Γ.varMu h + (c : ℝ) * Γ.varMu h := add_le_add h2 h1
      _ = ((c : ℝ) + 1) * Γ.varMu h := by ring

/-- Walking a ladder of admissible denominators: `|log n_{x + N h} − log n_x| ≤ (Σ b_i)·Var(μ_h)`
for `N = Σ_{i<n} b_i q_i`. -/
theorem dk_walk {h : ℕ} (hhm : h ≤ m) (q b : ℕ → ℕ) (n : ℕ)
    (hadm : ∀ i, i < n → 0 < q i ∧ ∃ p r, (q i * h = p * m + r ∨ p * m = q i * h + r) ∧
      q i * r < m ∧ Nat.Coprime p (q i)) :
    ∀ x, |Real.log (Γ.n (x + (∑ i ∈ Finset.range n, b i * q i) * h)) - Real.log (Γ.n x)| ≤
      (∑ i ∈ Finset.range n, (b i : ℝ)) * Γ.varMu h := by
  induction n with
  | zero =>
    intro x
    simp
  | succ n ih =>
    intro x
    have hadm' : ∀ i, i < n → 0 < q i ∧ ∃ p r, (q i * h = p * m + r ∨ p * m = q i * h + r) ∧
        q i * r < m ∧ Nat.Coprime p (q i) := fun i hi => hadm i (Nat.lt_succ_of_lt hi)
    have h1 := ih hadm' x
    obtain ⟨hqn, p, r, hr, hqr, hcop⟩ := hadm n (Nat.lt_succ_self n)
    set S := ∑ i ∈ Finset.range n, b i * q i with hS
    have h2 := Γ.dk_log_iter hqn hhm hr hqr hcop (b n) (x + S * h)
    rw [Finset.sum_range_succ, Finset.sum_range_succ, ← hS,
      show x + (S + b n * q n) * h = x + S * h + b n * (q n * h) by ring]
    calc |Real.log (Γ.n (x + S * h + b n * (q n * h))) - Real.log (Γ.n x)|
        ≤ |Real.log (Γ.n (x + S * h + b n * (q n * h))) - Real.log (Γ.n (x + S * h))| +
          |Real.log (Γ.n (x + S * h)) - Real.log (Γ.n x)| := abs_sub_le _ _ _
      _ ≤ (b n : ℝ) * Γ.varMu h + (∑ i ∈ Finset.range n, (b i : ℝ)) * Γ.varMu h :=
          add_le_add h2 h1
      _ = (∑ i ∈ Finset.range n, (b i : ℝ) + (b n : ℝ)) * Γ.varMu h := by ring

end OddCycle

/-! ### S12-c: the height bound `B ≤ (K − 1)·Var(μ_h)` (S12 (2) assembled)

For `gcd(h, m) = 1` every position is `x + N h (mod m)` with `N < m` (`DK.exists_chain_index`: the
map `N ↦ (x + N h) mod m` is injective on `[0, m)`, hence onto). For a continued-fraction ladder
`(q, a)` of `h/m` with `q n = m` whose denominators `q i`, `i < n`, are DK-admissible for `h`, the
greedy decomposition `N = Σ_{i<n} b_i q_i` with `Σ b_i ≤ K − 1` (`ostrowski_greedy`) and the ladder
walk (`dk_walk`) give `|log n_y − log n_x| ≤ (K − 1)·Var(μ_h)` for all positions `x, y`
(`height_le_varMu`), `K = Σ_{1 ≤ i ≤ n} a_i` the sum of the partial quotients; relative to the
minimum `n_0` this is the side lane's `B ≤ Var(μ_h)·(K − 1)` with `B = log(n_max/L)`
(`height_le_varMu'`). The admissibility of the convergents is a hypothesis on the ladder (supplied by
continued-fraction theory, not derived here); the inequality itself uses nothing about the cycle
beyond periodicity. -/

namespace DK

/-- For `gcd(h, m) = 1`, every residue is `(x + N h) mod m` for some `N < m`. -/
theorem exists_chain_index {m h : ℕ} (hm : 0 < m) (hcop : Nat.Coprime h m) (x y : ℕ) :
    ∃ N, N < m ∧ (x + N * h) % m = y % m := by
  have hinj : Set.InjOn (fun N => (x + N * h) % m) (↑(Finset.range m) : Set ℕ) := by
    intro N hN N' hN' heq
    rw [Finset.mem_coe, Finset.mem_range] at hN hN'
    have h1 : N * h ≡ N' * h [MOD m] := Nat.ModEq.add_left_cancel' x heq
    have h2 : N ≡ N' [MOD m] := Nat.ModEq.cancel_right_of_coprime hcop.symm.gcd_eq_one h1
    unfold Nat.ModEq at h2
    rwa [Nat.mod_eq_of_lt hN, Nat.mod_eq_of_lt hN'] at h2
  have himg : (Finset.range m).image (fun N => (x + N * h) % m) = Finset.range m := by
    apply Finset.eq_of_subset_of_card_le
    · intro r hr
      rw [Finset.mem_image] at hr
      obtain ⟨N, _, rfl⟩ := hr
      exact Finset.mem_range.mpr (Nat.mod_lt _ hm)
    · rw [Finset.card_image_of_injOn hinj]
  have hy : y % m ∈ (Finset.range m).image (fun N => (x + N * h) % m) := by
    rw [himg]
    exact Finset.mem_range.mpr (Nat.mod_lt _ hm)
  rw [Finset.mem_image] at hy
  obtain ⟨N, hN, hNy⟩ := hy
  exact ⟨N, Finset.mem_range.mp hN, hNy⟩

end DK

namespace OddCycle

variable {m : ℕ} (Γ : OddCycle m)

theorem varMu_nonneg (h : ℕ) : 0 ≤ Γ.varMu h := by
  unfold varMu
  exact Finset.sum_nonneg (fun _ _ => abs_nonneg _)

/-- **S12 (2), the height bound.** For a ladder `(q, a)` with `q n = m`, `n ≥ 1`, whose denominators
`q i` (`i < n`) are DK-admissible for the rotation `h`, with `gcd(h, m) = 1` and `h ≤ m`: for all
positions `x, y`, `|log n_y − log n_x| ≤ (K − 1)·Var(μ_h)`, `K = Σ_{1 ≤ i ≤ n} a i`. -/
theorem height_le_varMu {h : ℕ} (hhm : h ≤ m) (hcop : Nat.Coprime h m) {q a : ℕ → ℕ}
    (L : DK.Ladder q a) {n : ℕ} (hn : 1 ≤ n) (hqn : q n = m)
    (hadm : ∀ i, i < n → ∃ p r, (q i * h = p * m + r ∨ p * m = q i * h + r) ∧ q i * r < m ∧
      Nat.Coprime p (q i)) (x y : ℕ) :
    |Real.log (Γ.n y) - Real.log (Γ.n x)| ≤
      (((∑ i ∈ Finset.Icc 1 n, a i : ℕ) : ℝ) - 1) * Γ.varMu h := by
  obtain ⟨N, hN, hNy⟩ := DK.exists_chain_index Γ.hm hcop x y
  rw [← hqn] at hN
  obtain ⟨b, hb1, hb2⟩ := DK.ostrowski_greedy L n hn N hN
  have hadm' : ∀ i, i < n → 0 < q i ∧ ∃ p r, (q i * h = p * m + r ∨ p * m = q i * h + r) ∧
      q i * r < m ∧ Nat.Coprime p (q i) := fun i hi => ⟨DK.ladder_pos L i, hadm i hi⟩
  have hw := Γ.dk_walk hhm q b n hadm' x
  rw [← hb1] at hw
  have hny : Γ.n y = Γ.n (x + N * h) := by
    rw [← Γ.n_mod y, ← hNy, Γ.n_mod]
  rw [hny]
  refine hw.trans (mul_le_mul_of_nonneg_right ?_ (Γ.varMu_nonneg h))
  have hK : ((∑ i ∈ Finset.range n, b i : ℕ) : ℝ) + 1 ≤ ((∑ i ∈ Finset.Icc 1 n, a i : ℕ) : ℝ) := by
    exact_mod_cast hb2
  push_cast at hK ⊢
  linarith

/-- The side lane's form: relative to the minimum `n_0`, `log(n_y/L) ≤ (K − 1)·Var(μ_h)`, so the real
height `B = log(n_max/L)` satisfies `B ≤ (K − 1)·Var(μ_h)`. -/
theorem height_le_varMu' {h : ℕ} (hhm : h ≤ m) (hcop : Nat.Coprime h m) {q a : ℕ → ℕ}
    (L : DK.Ladder q a) {n : ℕ} (hn : 1 ≤ n) (hqn : q n = m)
    (hadm : ∀ i, i < n → ∃ p r, (q i * h = p * m + r ∨ p * m = q i * h + r) ∧ q i * r < m ∧
      Nat.Coprime p (q i)) (y : ℕ) :
    Real.log (Γ.n y) - Real.log (Γ.n 0) ≤
      (((∑ i ∈ Finset.Icc 1 n, a i : ℕ) : ℝ) - 1) * Γ.varMu h :=
  le_trans (le_abs_self _) (Γ.height_le_varMu hhm hcop L hn hqn hadm 0 y)

end OddCycle

/-! ### S12-d: the variation bound `Var(μ_h) ≤ V_h log 2 + 2δ` (S12 (3))

The height step of a cycle is `log n_{t+1} − log n_t = log 3 − a_t log 2 + ε_t` with the correction
`ε_t = log(1 + q/(3 n_t)) ≥ 0` (`log_step`, from the arrow `2^{a_t} n_{t+1} = 3 n_t + q`), and the
corrections sum to the drift: `Σ_{t<m} ε_t = A log 2 − m log 3 = δ` (`sum_eps`, telescoping over the
period). Hence `μ_h(t+1) − μ_h(t) = (a_t − a_{t+h}) log 2 + (ε_{t+h} − ε_t)`, and summing
`|·| ≤ |a_t − a_{t+h}| log 2 + ε_{t+h} + ε_t` over a period gives `Var(μ_h) ≤ V_h log 2 + 2δ`
(`varMu_le`, `varMu_le_Vh`), with `V_h = Σ_t |a_t − a_{t+h}|` the letter variation of the rotation
(`Vh`; only the mismatches contribute). This is the side lane's (3) in natural logarithms. With
S12-a/b/c, the height tool reads: `B ≤ (K − 1)·(V_h log 2 + 2δ)` for every rotation `h` coprime
to `m`, given the ladder of its convergents. -/

namespace OddCycle

variable {m : ℕ} (Γ : OddCycle m)

theorem n_cast_pos (t : ℕ) : (0 : ℝ) < Γ.n t := by
  exact_mod_cast lt_of_lt_of_le Γ.npos (Γ.nmin t)

/-- The per-step correction `ε_t = log(1 + q/(3 n_t))`. -/
noncomputable def eps (t : ℕ) : ℝ := Real.log (1 + (Γ.q : ℝ) / (3 * (Γ.n t : ℝ)))

theorem eps_nonneg' (t : ℕ) : 0 ≤ Γ.eps t := by
  unfold eps
  apply Real.log_nonneg
  have hq : (0 : ℝ) ≤ Γ.q := by exact_mod_cast Γ.hq.le
  have hn := Γ.n_cast_pos t
  have h1 : (0 : ℝ) ≤ (Γ.q : ℝ) / (3 * (Γ.n t : ℝ)) := div_nonneg hq (by linarith)
  linarith

theorem eps_per (t : ℕ) : Γ.eps (t + m) = Γ.eps t := by
  unfold eps
  rw [Γ.nper]

/-- The height step: `log n_{t+1} − log n_t = log 3 − a_t log 2 + ε_t`. -/
theorem log_step (t : ℕ) :
    Real.log (Γ.n (t + 1)) - Real.log (Γ.n t) =
      Real.log 3 - (Γ.a t : ℝ) * Real.log 2 + Γ.eps t := by
  have hn := Γ.n_cast_pos t
  have hn1 := Γ.n_cast_pos (t + 1)
  have hq : (0 : ℝ) < Γ.q := by exact_mod_cast Γ.hq
  have h3n : (0 : ℝ) < 3 * (Γ.n t : ℝ) := mul_pos (by norm_num) hn
  have harrow : (2 : ℝ) ^ Γ.a t * Γ.n (t + 1) = 3 * Γ.n t + Γ.q := by exact_mod_cast Γ.arrow t
  have hfac : (3 : ℝ) * Γ.n t + Γ.q = 3 * Γ.n t * (1 + (Γ.q : ℝ) / (3 * (Γ.n t : ℝ))) := by
    rw [mul_add, mul_one, mul_comm (3 * (Γ.n t : ℝ)) ((Γ.q : ℝ) / (3 * (Γ.n t : ℝ))),
      div_mul_cancel₀ _ h3n.ne']
  have h1pos : (0 : ℝ) < 1 + (Γ.q : ℝ) / (3 * (Γ.n t : ℝ)) := by
    have := div_pos hq h3n
    linarith
  have h2a : (2 : ℝ) ^ Γ.a t ≠ 0 := by positivity
  have hl := congrArg Real.log harrow
  rw [Real.log_mul h2a hn1.ne', Real.log_pow, hfac, Real.log_mul h3n.ne' h1pos.ne',
    Real.log_mul (by norm_num : (3 : ℝ) ≠ 0) hn.ne'] at hl
  unfold eps
  linarith

/-- The corrections sum to the drift: `Σ_{t<m} ε_t = A log 2 − m log 3`. -/
theorem sum_eps : ∑ t ∈ Finset.range m, Γ.eps t =
    (Γ.Apre m : ℝ) * Real.log 2 - m * Real.log 3 := by
  have htel : ∑ t ∈ Finset.range m, (Real.log (Γ.n (t + 1)) - Real.log (Γ.n t)) = 0 := by
    rw [Finset.sum_range_sub (fun t => Real.log (Γ.n t)) m]
    show Real.log (Γ.n m) - Real.log (Γ.n 0) = 0
    rw [show Γ.n m = Γ.n 0 by simpa using Γ.nper 0, sub_self]
  have h2 : ∑ t ∈ Finset.range m, (Real.log (Γ.n (t + 1)) - Real.log (Γ.n t)) =
      ∑ t ∈ Finset.range m, (Real.log 3 - (Γ.a t : ℝ) * Real.log 2 + Γ.eps t) :=
    Finset.sum_congr rfl (fun t _ => Γ.log_step t)
  rw [h2, Finset.sum_add_distrib, Finset.sum_sub_distrib, Finset.sum_const, Finset.card_range,
    nsmul_eq_mul, ← Finset.sum_mul] at htel
  have hA : ((Γ.Apre m : ℕ) : ℝ) = ∑ t ∈ Finset.range m, (Γ.a t : ℝ) := by
    unfold Apre
    exact Nat.cast_sum _ _
  rw [hA]
  linarith

/-- The shifted corrections have the same sum. -/
theorem sum_eps_shift (h : ℕ) :
    ∑ t ∈ Finset.range m, Γ.eps (t + h) = ∑ t ∈ Finset.range m, Γ.eps t := by
  have hsh : ∑ t ∈ Finset.range m, Γ.eps (h + t) = ∑ t ∈ Finset.range m, Γ.eps t :=
    DK.sum_range_shift Γ.eps Γ.eps_per h
  rw [← hsh]
  apply Finset.sum_congr rfl
  intro t _
  rw [Nat.add_comm]

/-- **S12 (3)**: `Var(μ_h) ≤ (Σ_t |a_t − a_{t+h}|) log 2 + 2δ`, `δ = A log 2 − m log 3`. -/
theorem varMu_le (h : ℕ) :
    Γ.varMu h ≤ (∑ t ∈ Finset.range m, |(Γ.a t : ℝ) - (Γ.a (t + h) : ℝ)|) * Real.log 2 +
      2 * ((Γ.Apre m : ℝ) * Real.log 2 - m * Real.log 3) := by
  have hlog2 : 0 ≤ Real.log 2 := Real.log_nonneg (by norm_num)
  have hpt : ∀ t, |(Real.log (Γ.n (t + 1 + h)) - Real.log (Γ.n (t + 1))) -
      (Real.log (Γ.n (t + h)) - Real.log (Γ.n t))| ≤
      |(Γ.a t : ℝ) - (Γ.a (t + h) : ℝ)| * Real.log 2 + (Γ.eps (t + h) + Γ.eps t) := by
    intro t
    have e1 := Γ.log_step t
    have e2 := Γ.log_step (t + h)
    rw [show t + h + 1 = t + 1 + h by omega] at e2
    have heq : (Real.log (Γ.n (t + 1 + h)) - Real.log (Γ.n (t + 1))) -
        (Real.log (Γ.n (t + h)) - Real.log (Γ.n t)) =
        ((Γ.a t : ℝ) - (Γ.a (t + h) : ℝ)) * Real.log 2 + (Γ.eps (t + h) - Γ.eps t) := by
      linarith
    rw [heq]
    have hε1 := Γ.eps_nonneg' t
    have hε2 := Γ.eps_nonneg' (t + h)
    have habs : |Γ.eps (t + h) - Γ.eps t| ≤ Γ.eps (t + h) + Γ.eps t := by
      rw [abs_le]
      constructor <;> linarith
    calc |((Γ.a t : ℝ) - (Γ.a (t + h) : ℝ)) * Real.log 2 + (Γ.eps (t + h) - Γ.eps t)|
        ≤ |((Γ.a t : ℝ) - (Γ.a (t + h) : ℝ)) * Real.log 2| + |Γ.eps (t + h) - Γ.eps t| :=
          abs_add_le _ _
      _ = |(Γ.a t : ℝ) - (Γ.a (t + h) : ℝ)| * Real.log 2 + |Γ.eps (t + h) - Γ.eps t| := by
          rw [abs_mul, abs_of_nonneg hlog2]
      _ ≤ |(Γ.a t : ℝ) - (Γ.a (t + h) : ℝ)| * Real.log 2 + (Γ.eps (t + h) + Γ.eps t) := by
          linarith
  unfold varMu
  calc ∑ t ∈ Finset.range m, |(Real.log (Γ.n (t + 1 + h)) - Real.log (Γ.n (t + 1))) -
        (Real.log (Γ.n (t + h)) - Real.log (Γ.n t))|
      ≤ ∑ t ∈ Finset.range m, (|(Γ.a t : ℝ) - (Γ.a (t + h) : ℝ)| * Real.log 2 +
          (Γ.eps (t + h) + Γ.eps t)) := Finset.sum_le_sum (fun t _ => hpt t)
    _ = (∑ t ∈ Finset.range m, |(Γ.a t : ℝ) - (Γ.a (t + h) : ℝ)|) * Real.log 2 +
          (∑ t ∈ Finset.range m, Γ.eps (t + h) + ∑ t ∈ Finset.range m, Γ.eps t) := by
        rw [Finset.sum_add_distrib, Finset.sum_add_distrib, Finset.sum_mul]
    _ = (∑ t ∈ Finset.range m, |(Γ.a t : ℝ) - (Γ.a (t + h) : ℝ)|) * Real.log 2 +
          2 * ((Γ.Apre m : ℝ) * Real.log 2 - m * Real.log 3) := by
        rw [Γ.sum_eps_shift, Γ.sum_eps]
        ring

/-- The letter variation of the rotation `h`: `V_h = Σ_t |a_t − a_{t+h}|` (only mismatches contribute). -/
def Vh (h : ℕ) : ℕ := ∑ t ∈ Finset.range m, Int.natAbs ((Γ.a t : ℤ) - (Γ.a (t + h) : ℤ))

theorem Vh_cast (h : ℕ) :
    (Γ.Vh h : ℝ) = ∑ t ∈ Finset.range m, |(Γ.a t : ℝ) - (Γ.a (t + h) : ℝ)| := by
  unfold Vh
  rw [Nat.cast_sum]
  apply Finset.sum_congr rfl
  intro t _
  rw [Nat.cast_natAbs, Int.cast_abs]
  push_cast
  rfl

/-- **S12 (3) with the integer letter variation**: `Var(μ_h) ≤ V_h log 2 + 2δ`. -/
theorem varMu_le_Vh (h : ℕ) :
    Γ.varMu h ≤ (Γ.Vh h : ℝ) * Real.log 2 +
      2 * ((Γ.Apre m : ℝ) * Real.log 2 - m * Real.log 3) := by
  rw [Γ.Vh_cast]
  exact Γ.varMu_le h

end OddCycle

/-! ### S9-d: the denominator laws for words (the `q = den(w)` glue)

`ofWord w` is the reduced integer cycle of a positive word `w` with `D_w > 0` whose first rotation
is minimal; its parameter is `q = D_w/gcd(C_w, D_w) = den(w)` (`ofWord_den`), its letters are those
of `w` (`ofWord_a`, `ofWord_word`), `A = Σ w` (`ofWord_Apre`) and `2^A − 3^m = D_w` (`ofWord_D`);
`den(w)` is odd (`den_odd`) and the mismatch set of a rotation is the letter mismatch set of `w`
(`ofWord_mis`). Hence S9 (i) and (ii) read as statements about words: for a primitive positive
word (distinct rotated intercepts) with a rotation `h` having exactly two letter mismatches,
`log 2 + ⌈(m−2)/2⌉ log 3 < log den(w) + (m − 1) log(3/2) + δ(w) + λ(w)` (`word_two_mismatch_law`),
and with exactly three and `m ≥ 2^19`, `(m/70) log 2 < log den(w) + δ(w) + λ(w)`
(`word_three_mismatch_law`), where `δ(w) = Σw · log 2 − m log 3` and
`λ(w) = log m + Σw · log 2 − log 3 − log(2^{Σw} − 3^m)`. The minimal-rotation hypothesis is a
normalisation (every word has one); no gap and no `L/q` hypothesis enter. -/

namespace OddCycle

theorem ofWord_den (w : List ℕ) (hw0 : w ≠ []) (hpos : ∀ x ∈ w, 1 ≤ x) (hD : 0 < D w)
    (hmin : ∀ i, C w ≤ C (w.rotate i)) : (ofWord w hw0 hpos hD hmin).q = den w := rfl

theorem ofWord_Apre (w : List ℕ) (hw0 : w ≠ []) (hpos : ∀ x ∈ w, 1 ≤ x) (hD : 0 < D w)
    (hmin : ∀ i, C w ≤ C (w.rotate i)) :
    (ofWord w hw0 hpos hD hmin).Apre w.length = w.sum := by
  rw [← (ofWord w hw0 hpos hD hmin).word_sum, ofWord_word]

theorem ofWord_D (w : List ℕ) (hw0 : w ≠ []) (hpos : ∀ x ∈ w, 1 ≤ x) (hD : 0 < D w)
    (hmin : ∀ i, C w ≤ C (w.rotate i)) :
    (2 : ℤ) ^ (ofWord w hw0 hpos hD hmin).Apre w.length - 3 ^ w.length = D w := by
  rw [← (ofWord w hw0 hpos hD hmin).D_word, ofWord_word]

theorem gcdCD_mul_den (w : List ℕ) : gcdCD w * den w = D w :=
  Int.mul_ediv_cancel' (gcdCD_dvd_D w)

theorem den_odd (w : List ℕ) (hz : 1 ≤ w.sum) : Odd (den w) := by
  rw [← Int.not_even_iff_odd]
  intro he
  have h2 : (2 : ℤ) ∣ den w := even_iff_two_dvd.mp he
  have h3 : (2 : ℤ) ∣ D w := by
    rw [← gcdCD_mul_den w]
    exact Dvd.dvd.mul_left h2 _
  exact D_odd hz h3

theorem sum_pos_of_pos (w : List ℕ) (hw0 : w ≠ []) (hpos : ∀ x ∈ w, 1 ≤ x) : 1 ≤ w.sum := by
  obtain ⟨x, v, hxv⟩ := List.exists_cons_of_ne_nil hw0
  have hx : 1 ≤ x := hpos x (by rw [hxv]; simp)
  rw [hxv, List.sum_cons]
  omega

/-- The mismatch set of the reduced cycle is the letter mismatch set of the word. -/
theorem ofWord_mis (w : List ℕ) (hw0 : w ≠ []) (hpos : ∀ x ∈ w, 1 ≤ x) (hD : 0 < D w)
    (hmin : ∀ i, C w ≤ C (w.rotate i)) (h : ℕ) : (ofWord w hw0 hpos hD hmin).mis h =
    (Finset.range w.length).filter
      (fun i => (w.rotate i).headD 0 ≠ (w.rotate (i + h)).headD 0) := by
  ext i
  unfold mis
  rw [Finset.mem_filter, Finset.mem_filter]
  exact Iff.rfl

/-- **S9 (i) for words.** -/
theorem word_two_mismatch_law (w : List ℕ) (hw0 : w ≠ []) (hpos : ∀ x ∈ w, 1 ≤ x)
    (hD : 0 < D w) (hmin : ∀ i, C w ≤ C (w.rotate i))
    (hdist : ∀ i j, i < w.length → j < w.length → C (w.rotate i) = C (w.rotate j) → i = j)
    {h : ℕ} (hh : h % w.length ≠ 0)
    (hs : ((Finset.range w.length).filter
      (fun i => (w.rotate i).headD 0 ≠ (w.rotate (i + h)).headD 0)).card = 2) :
    Real.log 2 + (((w.length - 1) / 2 : ℕ) : ℝ) * Real.log 3 <
      Real.log (den w) + ((w.length : ℝ) - 1) * (Real.log 3 - Real.log 2) +
        ((w.sum : ℝ) * Real.log 2 - w.length * Real.log 3) +
        (Real.log w.length + (w.sum : ℝ) * Real.log 2 - Real.log 3 -
          Real.log ((2 : ℝ) ^ w.sum - 3 ^ w.length)) := by
  have hq : Odd (ofWord w hw0 hpos hD hmin).q := by
    rw [ofWord_den]
    exact den_odd w (sum_pos_of_pos w hw0 hpos)
  have hprim := ofWord_primitive w hw0 hpos hD hmin hdist
  have hs' : ((ofWord w hw0 hpos hD hmin).mis h).card = 2 := by
    rw [ofWord_mis]
    exact hs
  have key := (ofWord w hw0 hpos hD hmin).two_mismatch_denominator_law_odd hprim hq hh hs'
  rw [ofWord_Apre, ofWord_den] at key
  exact key

/-- **S9 (ii) for words**, with the explicit constant `1/70` and `m ≥ 2^19`. -/
theorem word_three_mismatch_law (w : List ℕ) (hw0 : w ≠ []) (hpos : ∀ x ∈ w, 1 ≤ x)
    (hD : 0 < D w) (hmin : ∀ i, C w ≤ C (w.rotate i))
    (hdist : ∀ i j, i < w.length → j < w.length → C (w.rotate i) = C (w.rotate j) → i = j)
    (hm : 2 ^ 19 ≤ w.length) {h : ℕ} (hh1 : 1 ≤ h) (hhm : h < w.length)
    (hs : ((Finset.range w.length).filter
      (fun i => (w.rotate i).headD 0 ≠ (w.rotate (i + h)).headD 0)).card = 3) :
    (w.length : ℝ) / 70 * Real.log 2 <
      Real.log (den w) + ((w.sum : ℝ) * Real.log 2 - w.length * Real.log 3) +
        (Real.log w.length + (w.sum : ℝ) * Real.log 2 - Real.log 3 -
          Real.log ((2 : ℝ) ^ w.sum - 3 ^ w.length)) := by
  have hq : Odd (ofWord w hw0 hpos hD hmin).q := by
    rw [ofWord_den]
    exact den_odd w (sum_pos_of_pos w hw0 hpos)
  have hprim := ofWord_primitive w hw0 hpos hD hmin hdist
  have hs' : ((ofWord w hw0 hpos hD hmin).mis h).card = 3 := by
    rw [ofWord_mis]
    exact hs
  have key := (ofWord w hw0 hpos hD hmin).three_mismatch_denominator_law hprim hq hm hh1 hhm hs'
  rw [ofWord_Apre, ofWord_den] at key
  exact key

end OddCycle

/-! ### S12-e: the Denjoy–Koksma denominator law for every mismatch count

S12's denominator corollary: for a primitive cycle with letters `≥ 1`, a rotation `h` coprime to `m`
with exactly `s ≥ 1` mismatches, and a ladder `(q, a)` of `h/m` with `q n = m` whose denominators
are DK-admissible, the longest agreeing run `T` has `m ≤ s(T + 1)`, so `T ≥ ⌈(m−s)/s⌉ = (m − 1)/s`
(natural division); its witness exceeds `2·3^T` and is at most the maximum `n_j`; the height bound
gives `log n_j ≤ log L + (K − 1)·Var(μ_h)`, the variation bound `Var(μ_h) ≤ V_h log 2 + 2δ`, and
`3 L D ≤ m q 2^A` gives `log L ≤ log q + λ`. Hence
`log 2 + ((m − 1)/s) log 3 < log q + λ + (K − 1)(V_h log 2 + 2δ)` (`dk_denominator_law`), the side
lane's `log₂ den(w) > 1 + ⌈(m−s)/s⌉ log₂3 − (K − 1)(V_h + 2δ) − λ(w)` in natural logarithms, and
the same for words with `den(w)` (`word_dk_denominator_law`). Unlike S9 (i)–(ii) it holds for every
`s`, informative when `(K − 1)(V_h log 2 + 2δ)` is small (low-variation words with tame `h/m`);
the ladder is a hypothesis, as in S12-c. -/

namespace OddCycle

variable {m : ℕ} (Γ : OddCycle m)

/-- A rotation by a multiple of the period has no mismatches. -/
theorem mis_empty_of_mod_zero {h : ℕ} (hh : h % m = 0) : Γ.mis h = ∅ := by
  unfold mis
  rw [Finset.filter_eq_empty_iff]
  intro i _ hna
  apply hna
  show Γ.a i = Γ.a (i + h)
  rw [← Γ.a_mod (i + h), Nat.add_mod, hh, Nat.add_zero, Nat.mod_mod, Γ.a_mod]

/-- **S12's denominator law for every mismatch count** (natural logarithms). -/
theorem dk_denominator_law (hprim : ∀ i j, i < m → j < m → Γ.n i = Γ.n j → i = j)
    {h : ℕ} (hhm : h ≤ m) (hcop : Nat.Coprime h m) {q a : ℕ → ℕ} (L : DK.Ladder q a) {n : ℕ}
    (hn : 1 ≤ n) (hqn : q n = m)
    (hadm : ∀ i, i < n → ∃ p r, (q i * h = p * m + r ∨ p * m = q i * h + r) ∧ q i * r < m ∧
      Nat.Coprime p (q i))
    {s : ℕ} (hs1 : 1 ≤ s) (hs : (Γ.mis h).card = s) :
    Real.log 2 + (((m - 1) / s : ℕ) : ℝ) * Real.log 3 <
      Real.log (Γ.q) + (Real.log m + (Γ.Apre m : ℝ) * Real.log 2 - Real.log 3 -
          Real.log ((2 : ℝ) ^ Γ.Apre m - 3 ^ m)) +
        (((∑ i ∈ Finset.Icc 1 n, a i : ℕ) : ℝ) - 1) *
          ((Γ.Vh h : ℝ) * Real.log 2 + 2 * ((Γ.Apre m : ℝ) * Real.log 2 - m * Real.log 3)) := by
  have hmpos := Γ.hm
  have hh : h % m ≠ 0 := by
    intro h0
    have h1 := Γ.mis_empty_of_mod_zero h0
    rw [h1, Finset.card_empty] at hs
    omega
  obtain ⟨i, T, hrun, hTbound⟩ := Γ.exists_longest_run hprim hh
  have hpig := Γ.pigeonhole (Γ.exists_mis hprim hh) hTbound
  rw [hs] at hpig
  have hT : (m - 1) / s ≤ T := by
    have h1 : (m - 1) / s < T + 1 := by
      rw [Nat.div_lt_iff_lt_mul hs1]
      omega
    omega
  -- the maximum
  obtain ⟨j, hjm', hjmax⟩ :=
    Finset.exists_max_image (Finset.range m) Γ.n ⟨0, Finset.mem_range.mpr hmpos⟩
  have hj : ∀ k, Γ.n k ≤ Γ.n j := fun k => by
    rw [← Γ.n_mod k]
    exact hjmax (k % m) (Finset.mem_range.mpr (Nat.mod_lt _ hmpos))
  -- the witness of the longest run, below the maximum
  have hw := Γ.witness_gt T (fun k hk => hrun k hk) (Γ.z_ne_zero hprim hh (i + T))
  have hwj : 2 * (3 : ℤ) ^ T < Γ.n j := lt_of_lt_of_le hw (max_le (hj _) (hj _))
  have hwjR : 2 * (3 : ℝ) ^ T < Γ.n j := by exact_mod_cast hwj
  have h3T : (3 : ℝ) ^ T ≠ 0 := by positivity
  have hlw := Real.log_lt_log (by positivity) hwjR
  rw [Real.log_mul (by norm_num : (2 : ℝ) ≠ 0) h3T, Real.log_pow] at hlw
  -- the height bound at the maximum and the variation bound
  have hht := Γ.height_le_varMu' hhm hcop L hn hqn hadm j
  have hvar := Γ.varMu_le_Vh h
  have hK : (1 : ℝ) ≤ ((∑ i ∈ Finset.Icc 1 n, a i : ℕ) : ℝ) := by
    have h1 : 1 ≤ ∑ i ∈ Finset.Icc 1 n, a i := by
      calc 1 ≤ a 1 := L.apos 1 le_rfl
        _ ≤ ∑ i ∈ Finset.Icc 1 n, a i :=
          Finset.single_le_sum (fun _ _ => Nat.zero_le _) (Finset.mem_Icc.mpr ⟨le_rfl, hn⟩)
    exact_mod_cast h1
  have hprod := mul_le_mul_of_nonneg_left hvar
    (by linarith : (0 : ℝ) ≤ ((∑ i ∈ Finset.Icc 1 n, a i : ℕ) : ℝ) - 1)
  -- `3 L D ≤ m q 2^A` in logarithms
  have hn0 : (0 : ℝ) < Γ.n 0 := by exact_mod_cast Γ.npos
  have hD : (0 : ℝ) < (2 : ℝ) ^ Γ.Apre m - 3 ^ m := by exact_mod_cast Γ.D_pos
  have hq : (0 : ℝ) < Γ.q := by exact_mod_cast Γ.hq
  have hm0 : (0 : ℝ) < m := by exact_mod_cast hmpos
  have hA2 : (0 : ℝ) < 2 ^ Γ.Apre m := by positivity
  have h3n0 : (0 : ℝ) < 3 * Γ.n 0 := mul_pos (by norm_num) hn0
  have hmq : (0 : ℝ) < m * Γ.q := mul_pos hm0 hq
  have hl3 := Real.log_le_log (mul_pos h3n0 hD) Γ.three_L_D_le
  rw [Real.log_mul h3n0.ne' hD.ne', Real.log_mul (by norm_num : (3 : ℝ) ≠ 0) hn0.ne',
    Real.log_mul hmq.ne' hA2.ne', Real.log_mul hm0.ne' hq.ne', Real.log_pow] at hl3
  -- `(m − 1)/s ≤ T`
  have hTR : (((m - 1) / s : ℕ) : ℝ) ≤ T := by exact_mod_cast hT
  have hlog3 : 0 < Real.log 3 := Real.log_pos (by norm_num)
  have hTlog := mul_le_mul_of_nonneg_right hTR hlog3.le
  linarith

/-- The letter variation of the reduced cycle of a word, in word terms. -/
theorem ofWord_Vh (w : List ℕ) (hw0 : w ≠ []) (hpos : ∀ x ∈ w, 1 ≤ x) (hD : 0 < D w)
    (hmin : ∀ i, C w ≤ C (w.rotate i)) (h : ℕ) : (ofWord w hw0 hpos hD hmin).Vh h =
    ∑ t ∈ Finset.range w.length,
      Int.natAbs (((w.rotate t).headD 0 : ℤ) - ((w.rotate (t + h)).headD 0 : ℤ)) := rfl

/-- **S12's denominator law for words**, every mismatch count. -/
theorem word_dk_denominator_law (w : List ℕ) (hw0 : w ≠ []) (hpos : ∀ x ∈ w, 1 ≤ x)
    (hD : 0 < D w) (hmin : ∀ i, C w ≤ C (w.rotate i))
    (hdist : ∀ i j, i < w.length → j < w.length → C (w.rotate i) = C (w.rotate j) → i = j)
    {h : ℕ} (hhm : h ≤ w.length) (hcop : Nat.Coprime h w.length) {q a : ℕ → ℕ}
    (L : DK.Ladder q a) {n : ℕ} (hn : 1 ≤ n) (hqn : q n = w.length)
    (hadm : ∀ i, i < n → ∃ p r, (q i * h = p * w.length + r ∨ p * w.length = q i * h + r) ∧
      q i * r < w.length ∧ Nat.Coprime p (q i))
    {s : ℕ} (hs1 : 1 ≤ s)
    (hs : ((Finset.range w.length).filter
      (fun i => (w.rotate i).headD 0 ≠ (w.rotate (i + h)).headD 0)).card = s) :
    Real.log 2 + (((w.length - 1) / s : ℕ) : ℝ) * Real.log 3 <
      Real.log (den w) + (Real.log w.length + (w.sum : ℝ) * Real.log 2 - Real.log 3 -
          Real.log ((2 : ℝ) ^ w.sum - 3 ^ w.length)) +
        (((∑ i ∈ Finset.Icc 1 n, a i : ℕ) : ℝ) - 1) *
          (((∑ t ∈ Finset.range w.length,
              Int.natAbs (((w.rotate t).headD 0 : ℤ) - ((w.rotate (t + h)).headD 0 : ℤ)) : ℕ) : ℝ) *
              Real.log 2 +
            2 * ((w.sum : ℝ) * Real.log 2 - w.length * Real.log 3)) := by
  have hprim := ofWord_primitive w hw0 hpos hD hmin hdist
  have hs' : ((ofWord w hw0 hpos hD hmin).mis h).card = s := by
    rw [ofWord_mis]
    exact hs
  have key := (ofWord w hw0 hpos hD hmin).dk_denominator_law hprim hhm hcop L hn hqn hadm hs1 hs'
  rw [ofWord_Apre, ofWord_den, ofWord_Vh] at key
  exact key

end OddCycle

/-! ### S9-e: rotation invariance — the word laws without the minimal-rotation normalisation

Every nonempty word has a rotation of minimal intercept (the existing `exists_min_rotation`). `D`, `gcd(C, D)`
and hence `den` are rotation-invariant (`D_rotate`, `gcdCD_rotate`, `den_rotate`), as are the
length and the letter sum (`rotate_sum`); distinct rotated intercepts are inherited by rotations
(`hdist_rotate`); the mismatch count of a rotation `h` and the letter variation are the same for
every rotation of the word (`mismatch_card_rotate`, `Vh_sum_rotate`: periodic shifts of indicator
sums, `rotate_add_length`, `sum_range_shift_nat`). Hence the word laws S9 (i), S9 (ii) and S12's
corollary hold for every positive primitive word with `D_w > 0` — no normalisation hypothesis
(`word_two_mismatch_law'`, `word_three_mismatch_law'`, `word_dk_denominator_law'`). -/

namespace OddCycle

theorem gcdCD_rotate (w : List ℕ) (hw0 : w ≠ []) (hsum : 1 ≤ w.sum) (k : ℕ) :
    gcdCD (w.rotate k) = gcdCD w := by
  unfold gcdCD
  rw [gcd_rotate_eq hw0 hsum k]

theorem den_rotate (w : List ℕ) (hw0 : w ≠ []) (hsum : 1 ≤ w.sum) (k : ℕ) :
    den (w.rotate k) = den w := by
  unfold den
  rw [D_rotate, gcdCD_rotate w hw0 hsum k]

theorem rotate_sum (w : List ℕ) (k : ℕ) : (w.rotate k).sum = w.sum :=
  (List.rotate_perm w k).sum_eq

/-- Rotations are periodic in the rotation index. -/
theorem rotate_add_length (w : List ℕ) (i : ℕ) : w.rotate (i + w.length) = w.rotate i := by
  rw [← List.rotate_mod, Nat.add_mod_right, List.rotate_mod]

theorem hdist_rotate (w : List ℕ)
    (hdist : ∀ i j, i < w.length → j < w.length → C (w.rotate i) = C (w.rotate j) → i = j)
    (k : ℕ) : ∀ i j, i < (w.rotate k).length → j < (w.rotate k).length →
      C ((w.rotate k).rotate i) = C ((w.rotate k).rotate j) → i = j := by
  intro i j hi hj hij
  rw [List.length_rotate] at hi hj
  have hlen : 0 < w.length := by omega
  rw [List.rotate_rotate, List.rotate_rotate, ← List.rotate_mod w (k + i),
    ← List.rotate_mod w (k + j)] at hij
  have h1 := hdist _ _ (Nat.mod_lt _ hlen) (Nat.mod_lt _ hlen) hij
  have h2 : i % w.length = j % w.length := Nat.ModEq.add_left_cancel' k h1
  rwa [Nat.mod_eq_of_lt hi, Nat.mod_eq_of_lt hj] at h2

/-- Shift invariance of a periodic natural sum over a period. -/
theorem sum_range_shift_nat {m : ℕ} (f : ℕ → ℕ) (hper : ∀ t, f (t + m) = f t) (x : ℕ) :
    ∑ t ∈ Finset.range m, f (x + t) = ∑ t ∈ Finset.range m, f t := by
  induction x with
  | zero => simp
  | succ x ih =>
    rw [← ih]
    rcases Nat.eq_zero_or_pos m with hm0 | hmpos
    · subst hm0
      simp
    · obtain ⟨n, rfl⟩ := Nat.exists_eq_succ_of_ne_zero hmpos.ne'
      rw [Finset.sum_range_succ, Finset.sum_range_succ' (fun t => f (x + t))]
      have h1 : f (x + 1 + n) = f (x + 0) := by
        rw [Nat.add_zero, show x + 1 + n = x + (n + 1) by omega]
        exact hper x
      rw [h1]
      congr 1
      apply Finset.sum_congr rfl
      intro t _
      congr 1
      omega

/-- The mismatch count of the rotation `h` is the same for every rotation of the word. -/
theorem mismatch_card_rotate (w : List ℕ) (k h : ℕ) :
    ((Finset.range (w.rotate k).length).filter
      (fun i => ((w.rotate k).rotate i).headD 0 ≠ ((w.rotate k).rotate (i + h)).headD 0)).card =
    ((Finset.range w.length).filter
      (fun i => (w.rotate i).headD 0 ≠ (w.rotate (i + h)).headD 0)).card := by
  rw [List.length_rotate, Finset.card_filter, Finset.card_filter]
  have hper : ∀ t, (if (w.rotate (t + w.length)).headD 0 ≠ (w.rotate (t + w.length + h)).headD 0
      then 1 else 0) = (if (w.rotate t).headD 0 ≠ (w.rotate (t + h)).headD 0 then 1 else 0) := by
    intro t
    rw [rotate_add_length, show t + w.length + h = t + h + w.length by omega, rotate_add_length]
  have hsh := sum_range_shift_nat
    (fun t => if (w.rotate t).headD 0 ≠ (w.rotate (t + h)).headD 0 then 1 else 0) hper k
  rw [← hsh]
  apply Finset.sum_congr rfl
  intro t _
  rw [List.rotate_rotate, List.rotate_rotate, ← Nat.add_assoc]

/-- The letter variation of the rotation `h` is the same for every rotation of the word. -/
theorem Vh_sum_rotate (w : List ℕ) (k h : ℕ) :
    ∑ t ∈ Finset.range (w.rotate k).length,
        Int.natAbs ((((w.rotate k).rotate t).headD 0 : ℤ) -
          (((w.rotate k).rotate (t + h)).headD 0 : ℤ)) =
      ∑ t ∈ Finset.range w.length,
        Int.natAbs (((w.rotate t).headD 0 : ℤ) - ((w.rotate (t + h)).headD 0 : ℤ)) := by
  rw [List.length_rotate]
  have hper : ∀ t, Int.natAbs (((w.rotate (t + w.length)).headD 0 : ℤ) -
      ((w.rotate (t + w.length + h)).headD 0 : ℤ)) =
      Int.natAbs (((w.rotate t).headD 0 : ℤ) - ((w.rotate (t + h)).headD 0 : ℤ)) := by
    intro t
    rw [rotate_add_length, show t + w.length + h = t + h + w.length by omega, rotate_add_length]
  have hsh := sum_range_shift_nat
    (fun t => Int.natAbs (((w.rotate t).headD 0 : ℤ) - ((w.rotate (t + h)).headD 0 : ℤ))) hper k
  rw [← hsh]
  apply Finset.sum_congr rfl
  intro t _
  rw [List.rotate_rotate, List.rotate_rotate, ← Nat.add_assoc]

/-- **S9 (i) for every positive primitive word** (no normalisation). -/
theorem word_two_mismatch_law' (w : List ℕ) (hw0 : w ≠ []) (hpos : ∀ x ∈ w, 1 ≤ x)
    (hD : 0 < D w)
    (hdist : ∀ i j, i < w.length → j < w.length → C (w.rotate i) = C (w.rotate j) → i = j)
    {h : ℕ} (hh : h % w.length ≠ 0)
    (hs : ((Finset.range w.length).filter
      (fun i => (w.rotate i).headD 0 ≠ (w.rotate (i + h)).headD 0)).card = 2) :
    Real.log 2 + (((w.length - 1) / 2 : ℕ) : ℝ) * Real.log 3 <
      Real.log (den w) + ((w.length : ℝ) - 1) * (Real.log 3 - Real.log 2) +
        ((w.sum : ℝ) * Real.log 2 - w.length * Real.log 3) +
        (Real.log w.length + (w.sum : ℝ) * Real.log 2 - Real.log 3 -
          Real.log ((2 : ℝ) ^ w.sum - 3 ^ w.length)) := by
  obtain ⟨k, hmin⟩ := exists_min_rotation w hw0
  have hsum := sum_pos_of_pos w hw0 hpos
  have hr0 : w.rotate k ≠ [] := NarrowCycle.rotate_ne_nil hw0 k
  have hrpos : ∀ x ∈ w.rotate k, 1 ≤ x := fun x hx => hpos x (List.mem_rotate.mp hx)
  have hrD : 0 < D (w.rotate k) := by
    rw [D_rotate]
    exact hD
  have hrdist := hdist_rotate w hdist k
  have hrh : h % (w.rotate k).length ≠ 0 := by
    rw [List.length_rotate]
    exact hh
  have hrs : ((Finset.range (w.rotate k).length).filter
      (fun i => ((w.rotate k).rotate i).headD 0 ≠ ((w.rotate k).rotate (i + h)).headD 0)).card
      = 2 := by
    rw [mismatch_card_rotate]
    exact hs
  have key := word_two_mismatch_law (w.rotate k) hr0 hrpos hrD hmin hrdist hrh hrs
  rw [den_rotate w hw0 hsum k, List.length_rotate, rotate_sum] at key
  exact key

/-- **S9 (ii) for every positive primitive word** (no normalisation), `m ≥ 2^19`. -/
theorem word_three_mismatch_law' (w : List ℕ) (hw0 : w ≠ []) (hpos : ∀ x ∈ w, 1 ≤ x)
    (hD : 0 < D w)
    (hdist : ∀ i j, i < w.length → j < w.length → C (w.rotate i) = C (w.rotate j) → i = j)
    (hm : 2 ^ 19 ≤ w.length) {h : ℕ} (hh1 : 1 ≤ h) (hhm : h < w.length)
    (hs : ((Finset.range w.length).filter
      (fun i => (w.rotate i).headD 0 ≠ (w.rotate (i + h)).headD 0)).card = 3) :
    (w.length : ℝ) / 70 * Real.log 2 <
      Real.log (den w) + ((w.sum : ℝ) * Real.log 2 - w.length * Real.log 3) +
        (Real.log w.length + (w.sum : ℝ) * Real.log 2 - Real.log 3 -
          Real.log ((2 : ℝ) ^ w.sum - 3 ^ w.length)) := by
  obtain ⟨k, hmin⟩ := exists_min_rotation w hw0
  have hsum := sum_pos_of_pos w hw0 hpos
  have hr0 : w.rotate k ≠ [] := NarrowCycle.rotate_ne_nil hw0 k
  have hrpos : ∀ x ∈ w.rotate k, 1 ≤ x := fun x hx => hpos x (List.mem_rotate.mp hx)
  have hrD : 0 < D (w.rotate k) := by
    rw [D_rotate]
    exact hD
  have hrdist := hdist_rotate w hdist k
  have hrm : 2 ^ 19 ≤ (w.rotate k).length := by
    rw [List.length_rotate]
    exact hm
  have hrhm : h < (w.rotate k).length := by
    rw [List.length_rotate]
    exact hhm
  have hrs : ((Finset.range (w.rotate k).length).filter
      (fun i => ((w.rotate k).rotate i).headD 0 ≠ ((w.rotate k).rotate (i + h)).headD 0)).card
      = 3 := by
    rw [mismatch_card_rotate]
    exact hs
  have key := word_three_mismatch_law (w.rotate k) hr0 hrpos hrD hmin hrdist hrm hh1 hrhm hrs
  rw [den_rotate w hw0 hsum k, List.length_rotate, rotate_sum] at key
  exact key

/-- **S12's denominator law for every positive primitive word** (no normalisation). -/
theorem word_dk_denominator_law' (w : List ℕ) (hw0 : w ≠ []) (hpos : ∀ x ∈ w, 1 ≤ x)
    (hD : 0 < D w)
    (hdist : ∀ i j, i < w.length → j < w.length → C (w.rotate i) = C (w.rotate j) → i = j)
    {h : ℕ} (hhm : h ≤ w.length) (hcop : Nat.Coprime h w.length) {q a : ℕ → ℕ}
    (L : DK.Ladder q a) {n : ℕ} (hn : 1 ≤ n) (hqn : q n = w.length)
    (hadm : ∀ i, i < n → ∃ p r, (q i * h = p * w.length + r ∨ p * w.length = q i * h + r) ∧
      q i * r < w.length ∧ Nat.Coprime p (q i))
    {s : ℕ} (hs1 : 1 ≤ s)
    (hs : ((Finset.range w.length).filter
      (fun i => (w.rotate i).headD 0 ≠ (w.rotate (i + h)).headD 0)).card = s) :
    Real.log 2 + (((w.length - 1) / s : ℕ) : ℝ) * Real.log 3 <
      Real.log (den w) + (Real.log w.length + (w.sum : ℝ) * Real.log 2 - Real.log 3 -
          Real.log ((2 : ℝ) ^ w.sum - 3 ^ w.length)) +
        (((∑ i ∈ Finset.Icc 1 n, a i : ℕ) : ℝ) - 1) *
          (((∑ t ∈ Finset.range w.length,
              Int.natAbs (((w.rotate t).headD 0 : ℤ) - ((w.rotate (t + h)).headD 0 : ℤ)) : ℕ) : ℝ) *
              Real.log 2 +
            2 * ((w.sum : ℝ) * Real.log 2 - w.length * Real.log 3)) := by
  obtain ⟨k, hmin⟩ := exists_min_rotation w hw0
  have hsum := sum_pos_of_pos w hw0 hpos
  have hr0 : w.rotate k ≠ [] := NarrowCycle.rotate_ne_nil hw0 k
  have hrpos : ∀ x ∈ w.rotate k, 1 ≤ x := fun x hx => hpos x (List.mem_rotate.mp hx)
  have hrD : 0 < D (w.rotate k) := by
    rw [D_rotate]
    exact hD
  have hrdist := hdist_rotate w hdist k
  have hrhm : h ≤ (w.rotate k).length := by
    rw [List.length_rotate]
    exact hhm
  have hrcop : Nat.Coprime h (w.rotate k).length := by
    rw [List.length_rotate]
    exact hcop
  have hrqn : q n = (w.rotate k).length := by
    rw [List.length_rotate]
    exact hqn
  have hradm : ∀ i, i < n → ∃ p r, (q i * h = p * (w.rotate k).length + r ∨
      p * (w.rotate k).length = q i * h + r) ∧ q i * r < (w.rotate k).length ∧
      Nat.Coprime p (q i) := by
    rw [List.length_rotate]
    exact hadm
  have hrs : ((Finset.range (w.rotate k).length).filter
      (fun i => ((w.rotate k).rotate i).headD 0 ≠ ((w.rotate k).rotate (i + h)).headD 0)).card
      = s := by
    rw [mismatch_card_rotate]
    exact hs
  have key := word_dk_denominator_law (w.rotate k) hr0 hrpos hrD hmin hrdist hrhm hrcop L hn
    hrqn hradm hs1 hrs
  rw [den_rotate w hw0 hsum k, Vh_sum_rotate, List.length_rotate, rotate_sum] at key
  exact key

end OddCycle

/-! ### S12-f (part 1): convergents from Euclidean data — the ladder invariants

Abstract Euclidean data: remainders `r` and quotients `a` with exact steps
`r i = a (i+1) · r (i+1) + r (i+2)` for `i < n` (`EuclidData`). The convergent denominators and
numerators follow the ladder recursion from the quotients (`convQ`, `convP`: `q 0 = 1`, `q 1 = a 1`,
`p 0 = 0`, `p 1 = 1`). Without any hypothesis: the determinant identity
`p (i+1) q i − p i q (i+1) = (−1)^i` (`conv_det`), hence `gcd(p i, q i) = 1` (`conv_coprime`); with
quotients `≥ 1`, `convQ a` is a `Ladder` (`ladder_convQ`), positive and strictly increasing from
index `1` (`convQ_lt_succ`). With the Euclidean steps: the approximation identity
`q i · r 1 − p i · r 0 = (−1)^i r (i+1)` for `i ≤ n` (`conv_approx`), its either-sign form
(`conv_approx_either`, the hypothesis shape of `dk_log_either`), the Euclidean identity
`r 0 = q (i+1) r (i+1) + q i r (i+2)` for `i < n` (`conv_identity`), and the admissibility
`q i · r (i+1) < r 0` for `i < n` when `r 1 < r 0` and the remainders before termination are
positive (`conv_adm`). Part 2 instantiates this with the Euclidean algorithm for `h/m`; part 3
removes the ladder hypothesis from the height tool. -/

namespace DK

/-- Euclidean data: exact steps `r i = a (i+1) · r (i+1) + r (i+2)` for `i < n`. -/
structure EuclidData (r a : ℕ → ℕ) (n : ℕ) : Prop where
  step : ∀ i, i < n → r i = a (i + 1) * r (i + 1) + r (i + 2)

/-- Convergent denominators: `q 0 = 1`, `q 1 = a 1`, `q (i+2) = a (i+2) q (i+1) + q i`. -/
def convQ (a : ℕ → ℕ) : ℕ → ℕ
  | 0 => 1
  | 1 => a 1
  | i + 2 => a (i + 2) * convQ a (i + 1) + convQ a i

/-- Convergent numerators: `p 0 = 0`, `p 1 = 1`, `p (i+2) = a (i+2) p (i+1) + p i`. -/
def convP (a : ℕ → ℕ) : ℕ → ℕ
  | 0 => 0
  | 1 => 1
  | i + 2 => a (i + 2) * convP a (i + 1) + convP a i

theorem convQ_zero (a : ℕ → ℕ) : convQ a 0 = 1 := by rw [convQ]
theorem convQ_one (a : ℕ → ℕ) : convQ a 1 = a 1 := by rw [convQ]
theorem convQ_succ_succ (a : ℕ → ℕ) (i : ℕ) :
    convQ a (i + 2) = a (i + 2) * convQ a (i + 1) + convQ a i := by rw [convQ]
theorem convP_zero (a : ℕ → ℕ) : convP a 0 = 0 := by rw [convP]
theorem convP_one (a : ℕ → ℕ) : convP a 1 = 1 := by rw [convP]
theorem convP_succ_succ (a : ℕ → ℕ) (i : ℕ) :
    convP a (i + 2) = a (i + 2) * convP a (i + 1) + convP a i := by rw [convP]

/-- The convergent denominators form a ladder when the quotients are `≥ 1`. -/
theorem ladder_convQ (a : ℕ → ℕ) (ha : ∀ i, 1 ≤ i → 1 ≤ a i) : Ladder (convQ a) a :=
  ⟨convQ_zero a, convQ_one a, convQ_succ_succ a, ha⟩

theorem convQ_pos (a : ℕ → ℕ) (ha : ∀ i, 1 ≤ i → 1 ≤ a i) (i : ℕ) : 1 ≤ convQ a i :=
  ladder_pos (ladder_convQ a ha) i

/-- From index `1` on the denominators strictly increase. -/
theorem convQ_lt_succ (a : ℕ → ℕ) (ha : ∀ i, 1 ≤ i → 1 ≤ a i) (i : ℕ) :
    convQ a (i + 1) < convQ a (i + 2) := by
  rw [convQ_succ_succ]
  have h1 := convQ_pos a ha i
  have h2 : 0 < a (i + 2) := ha (i + 2) (by omega)
  have h3 : convQ a (i + 1) ≤ a (i + 2) * convQ a (i + 1) := Nat.le_mul_of_pos_left _ h2
  omega

/-- The determinant identity `p (i+1) q i − p i q (i+1) = (−1)^i`. -/
theorem conv_det (a : ℕ → ℕ) : ∀ i,
    (convP a (i + 1) : ℤ) * convQ a i - convP a i * convQ a (i + 1) = (-1) ^ i := by
  intro i
  induction i with
  | zero => simp [convQ_zero, convQ_one, convP_zero, convP_one]
  | succ i ih =>
    show (convP a (i + 2) : ℤ) * convQ a (i + 1) - convP a (i + 1) * convQ a (i + 2) =
      (-1) ^ (i + 1)
    rw [convQ_succ_succ, convP_succ_succ]
    push_cast
    linear_combination -ih

/-- `gcd(p i, q i) = 1`. -/
theorem conv_coprime (a : ℕ → ℕ) (i : ℕ) : Nat.Coprime (convP a i) (convQ a i) := by
  rw [← Nat.isCoprime_iff_coprime]
  have h := conv_det a i
  have h2 : ((-1 : ℤ) ^ i) ^ 2 = 1 := by
    rcases neg_one_pow_eq_or ℤ i with h1 | h1 <;> rw [h1] <;> norm_num
  refine ⟨(-1) ^ i * (-(convQ a (i + 1) : ℤ)), (-1) ^ i * (convP a (i + 1) : ℤ), ?_⟩
  linear_combination (-1 : ℤ) ^ i * h + h2

/-- The approximation identity `q i · r 1 − p i · r 0 = (−1)^i r (i+1)` for `i ≤ n`. -/
theorem conv_approx {r a : ℕ → ℕ} {n : ℕ} (E : EuclidData r a n) : ∀ i, i ≤ n →
    (convQ a i : ℤ) * r 1 - convP a i * r 0 = (-1) ^ i * r (i + 1) := by
  have key : ∀ i, (i ≤ n → (convQ a i : ℤ) * r 1 - convP a i * r 0 = (-1) ^ i * r (i + 1)) ∧
      (i + 1 ≤ n → (convQ a (i + 1) : ℤ) * r 1 - convP a (i + 1) * r 0 =
        (-1) ^ (i + 1) * r (i + 2)) := by
    intro i
    induction i with
    | zero =>
      constructor
      · intro _
        simp [convQ_zero, convP_zero]
      · intro h1
        have hs : (r 0 : ℤ) = a 1 * r 1 + r 2 := by exact_mod_cast E.step 0 (by omega)
        rw [convQ_one, convP_one]
        push_cast
        linear_combination -hs
    | succ i ih =>
      constructor
      · exact ih.2
      · intro h2
        have e1 := ih.1 (by omega)
        have e2 := ih.2 (by omega)
        have hs : (r (i + 1) : ℤ) = a (i + 2) * r (i + 2) + r (i + 3) := by
          exact_mod_cast E.step (i + 1) (by omega)
        show (convQ a (i + 2) : ℤ) * r 1 - convP a (i + 2) * r 0 = (-1) ^ (i + 2) * r (i + 3)
        rw [convQ_succ_succ, convP_succ_succ]
        push_cast
        linear_combination (a (i + 2) : ℤ) * e2 + e1 + (-1 : ℤ) ^ i * hs
  intro i hi
  exact (key i).1 hi

/-- The either-sign form of the approximation identity. -/
theorem conv_approx_either {r a : ℕ → ℕ} {n : ℕ} (E : EuclidData r a n) {i : ℕ} (hi : i ≤ n) :
    convQ a i * r 1 = convP a i * r 0 + r (i + 1) ∨
      convP a i * r 0 = convQ a i * r 1 + r (i + 1) := by
  have h := conv_approx E i hi
  rcases neg_one_pow_eq_or ℤ i with h1 | h1
  · left
    rw [h1, one_mul] at h
    have h' : (convQ a i : ℤ) * r 1 = convP a i * r 0 + r (i + 1) := by linarith
    exact_mod_cast h'
  · right
    rw [h1] at h
    have h' : (convP a i : ℤ) * r 0 = convQ a i * r 1 + r (i + 1) := by linarith
    exact_mod_cast h'

/-- The Euclidean identity `r 0 = q (i+1) r (i+1) + q i r (i+2)` for `i < n`. -/
theorem conv_identity {r a : ℕ → ℕ} {n : ℕ} (E : EuclidData r a n) : ∀ i, i < n →
    r 0 = convQ a (i + 1) * r (i + 1) + convQ a i * r (i + 2) := by
  intro i
  induction i with
  | zero =>
    intro h0
    rw [convQ_one, convQ_zero, one_mul]
    exact E.step 0 h0
  | succ i ih =>
    intro h1
    have e := ih (by omega)
    have hs : r (i + 1) = a (i + 2) * r (i + 2) + r (i + 3) := E.step (i + 1) h1
    show r 0 = convQ a (i + 2) * r (i + 2) + convQ a (i + 1) * r (i + 3)
    rw [convQ_succ_succ, e, hs]
    ring

/-- Admissibility of the convergent denominators: `q i · r (i+1) < r 0` for `i < n`. -/
theorem conv_adm {r a : ℕ → ℕ} {n : ℕ} (E : EuclidData r a n) (ha : ∀ i, 1 ≤ i → 1 ≤ a i)
    (h10 : r 1 < r 0) (hpos : ∀ j, j < n → 0 < r (j + 1)) :
    ∀ i, i < n → convQ a i * r (i + 1) < r 0 := by
  intro i hi
  rcases Nat.eq_zero_or_pos i with hi0 | hi0
  · subst hi0
    rw [convQ_zero, one_mul]
    exact h10
  · obtain ⟨k, rfl⟩ := Nat.exists_eq_succ_of_ne_zero hi0.ne'
    have hid : r 0 = convQ a (k + 2) * r (k + 2) + convQ a (k + 1) * r (k + 3) :=
      conv_identity E (k + 1) hi
    have hlt := convQ_lt_succ a ha k
    have hr : 0 < r (k + 2) := hpos (k + 1) hi
    have hmul : convQ a (k + 1) * r (k + 2) < convQ a (k + 2) * r (k + 2) :=
      Nat.mul_lt_mul_of_pos_right hlt hr
    show convQ a (k + 1) * r (k + 2) < r 0
    omega

end DK

/-! ### S12-f (part 2): the Euclidean algorithm for `h/m` and the ladder supply

The remainders `rem 0 = m`, `rem 1 = h`, `rem (i+2) = rem i mod rem (i+1)` and the quotients
`quot (i+1) = rem i div rem (i+1)` (floored at `1`, which only matters past termination) form
Euclidean data up to the termination index `n = termIndex m h`, the least `n` with `rem (n+1) = 0`
(`rem_exists_zero`: the remainders strictly decrease while positive). Before `n` the remainders are
positive and nonincreasing (`rem_pos_of_lt_termIndex`, `rem_succ_le`), so the steps are exact
(`euclidData_rem`); the gcd is invariant along the algorithm (`gcd_rem`), so `rem n = 1` for `h`
coprime to `m` (`rem_termIndex`), and the Euclidean identity at `n − 1` gives `q n = m`
(`convQ_termIndex`). **`ladder_of_coprime`**: for `0 < h < m` with `gcd(h, m) = 1`, the convergent
denominators of `h/m` form a `Ladder` ending at `m` whose denominators are DK-admissible — the
hypothesis of `height_le_varMu` and `dk_denominator_law`, now supplied. Part 3 states the height tool
with only `gcd(h, m) = 1`. -/

namespace DK

/-- Euclidean remainders of `(m, h)`. -/
def rem (m h : ℕ) : ℕ → ℕ
  | 0 => m
  | 1 => h
  | i + 2 => rem m h i % rem m h (i + 1)

theorem rem_zero (m h : ℕ) : rem m h 0 = m := by rw [rem]
theorem rem_one (m h : ℕ) : rem m h 1 = h := by rw [rem]
theorem rem_succ_succ (m h i : ℕ) : rem m h (i + 2) = rem m h i % rem m h (i + 1) := by rw [rem]

/-- The partial quotients, floored at `1` (irrelevant before termination). -/
def quot (m h : ℕ) (i : ℕ) : ℕ := max 1 (rem m h (i - 1) / rem m h i)

theorem one_le_quot (m h i : ℕ) : 1 ≤ quot m h i := le_max_left _ _

theorem quot_succ_eq {m h i : ℕ} (hpos : 0 < rem m h (i + 1))
    (hle : rem m h (i + 1) ≤ rem m h i) : quot m h (i + 1) = rem m h i / rem m h (i + 1) := by
  unfold quot
  rw [Nat.add_sub_cancel]
  exact max_eq_right ((Nat.le_div_iff_mul_le hpos).mpr (by rw [one_mul]; exact hle))

theorem rem_lt {m h i : ℕ} (hpos : 0 < rem m h (i + 1)) : rem m h (i + 2) < rem m h (i + 1) := by
  rw [rem_succ_succ]
  exact Nat.mod_lt _ hpos

/-- While positive, the remainders strictly decrease: `rem (i+1) + i ≤ rem 1`. -/
theorem rem_add_le (m h : ℕ) : ∀ i, (∀ j, j < i → 0 < rem m h (j + 1)) →
    rem m h (i + 1) + i ≤ rem m h 1 := by
  intro i
  induction i with
  | zero =>
    intro _
    simp
  | succ i ih =>
    intro hpos
    have h1 := ih (fun j hj => hpos j (Nat.lt_succ_of_lt hj))
    have h2 := rem_lt (hpos i (Nat.lt_succ_self i))
    show rem m h (i + 2) + (i + 1) ≤ rem m h 1
    omega

theorem rem_exists_zero (m h : ℕ) : ∃ k, rem m h (k + 1) = 0 := by
  by_contra hno
  have hpos : ∀ k, 0 < rem m h (k + 1) := fun k => Nat.pos_of_ne_zero (fun h0 => hno ⟨k, h0⟩)
  have h1 := rem_add_le m h (rem m h 1) (fun j _ => hpos j)
  have h2 := hpos (rem m h 1)
  omega

/-- The termination index: the least `n` with `rem (n+1) = 0`. -/
def termIndex (m h : ℕ) : ℕ := Nat.find (rem_exists_zero m h)

theorem rem_termIndex_succ (m h : ℕ) : rem m h (termIndex m h + 1) = 0 :=
  Nat.find_spec (rem_exists_zero m h)

theorem rem_pos_of_lt_termIndex {m h j : ℕ} (hj : j < termIndex m h) : 0 < rem m h (j + 1) :=
  Nat.pos_of_ne_zero (Nat.find_min (rem_exists_zero m h) hj)

theorem termIndex_pos {m h : ℕ} (hh : 0 < h) : 0 < termIndex m h := by
  apply Nat.pos_of_ne_zero
  intro h0
  have h1 := rem_termIndex_succ m h
  rw [h0] at h1
  simp only [Nat.zero_add, rem_one] at h1
  omega

theorem rem_succ_le {m h i : ℕ} (hi : i < termIndex m h) (hhm : h ≤ m) :
    rem m h (i + 1) ≤ rem m h i := by
  cases i with
  | zero =>
    show rem m h 1 ≤ rem m h 0
    rw [rem_one, rem_zero]
    exact hhm
  | succ k =>
    have hpos : 0 < rem m h (k + 1) := rem_pos_of_lt_termIndex (by omega)
    exact (rem_lt hpos).le

/-- The remainders and quotients are Euclidean data up to the termination index. -/
theorem euclidData_rem (m h : ℕ) (hhm : h ≤ m) :
    EuclidData (rem m h) (quot m h) (termIndex m h) := by
  constructor
  intro i hi
  have hpos : 0 < rem m h (i + 1) := rem_pos_of_lt_termIndex hi
  have hle : rem m h (i + 1) ≤ rem m h i := rem_succ_le hi hhm
  rw [quot_succ_eq hpos hle, rem_succ_succ, Nat.mul_comm]
  exact (Nat.div_add_mod (rem m h i) (rem m h (i + 1))).symm

/-- The gcd is invariant along the algorithm. -/
theorem gcd_rem (m h : ℕ) : ∀ i, Nat.gcd (rem m h i) (rem m h (i + 1)) = Nat.gcd m h := by
  intro i
  induction i with
  | zero => rw [rem_zero, rem_one]
  | succ i ih =>
    rw [← ih]
    show Nat.gcd (rem m h (i + 1)) (rem m h (i + 2)) = Nat.gcd (rem m h i) (rem m h (i + 1))
    rw [rem_succ_succ, Nat.gcd_comm (rem m h (i + 1)), ← Nat.gcd_rec, Nat.gcd_comm]

theorem rem_termIndex {m h : ℕ} (hcop : Nat.Coprime h m) : rem m h (termIndex m h) = 1 := by
  have hg := gcd_rem m h (termIndex m h)
  rw [rem_termIndex_succ, Nat.gcd_zero_right] at hg
  rw [hg, Nat.gcd_comm]
  exact hcop

/-- The last convergent denominator is `m`. -/
theorem convQ_termIndex {m h : ℕ} (hh : 0 < h) (hhm : h ≤ m) (hcop : Nat.Coprime h m) :
    convQ (quot m h) (termIndex m h) = m := by
  have E := euclidData_rem m h hhm
  have hn := termIndex_pos (m := m) hh
  obtain ⟨k, hk⟩ : ∃ k, termIndex m h = k + 1 := ⟨termIndex m h - 1, by omega⟩
  have hid := conv_identity E k (by omega)
  have h1 : rem m h (k + 1) = 1 := by
    rw [← hk]
    exact rem_termIndex hcop
  have h0 : rem m h (k + 2) = 0 := by
    rw [show k + 2 = termIndex m h + 1 by omega]
    exact rem_termIndex_succ m h
  rw [hk]
  rw [rem_zero, h1, h0] at hid
  omega

/-- **The ladder of `h/m`.** For `0 < h < m` coprime to `m`: the convergent denominators of `h/m`
form a `Ladder` ending at `m` whose denominators are DK-admissible. -/
theorem ladder_of_coprime {m h : ℕ} (hh : 0 < h) (hhm : h < m) (hcop : Nat.Coprime h m) :
    Ladder (convQ (quot m h)) (quot m h) ∧ 1 ≤ termIndex m h ∧
      convQ (quot m h) (termIndex m h) = m ∧
      ∀ i, i < termIndex m h → ∃ p r,
        (convQ (quot m h) i * h = p * m + r ∨ p * m = convQ (quot m h) i * h + r) ∧
        convQ (quot m h) i * r < m ∧ Nat.Coprime p (convQ (quot m h) i) := by
  have E := euclidData_rem m h hhm.le
  refine ⟨ladder_convQ _ (fun i _ => one_le_quot m h i), termIndex_pos hh,
    convQ_termIndex hh hhm.le hcop, ?_⟩
  intro i hi
  refine ⟨convP (quot m h) i, rem m h (i + 1), ?_, ?_, conv_coprime _ i⟩
  · have h1 := conv_approx_either E hi.le
    rw [rem_one, rem_zero] at h1
    exact h1
  · have h2 := conv_adm E (fun i _ => one_le_quot m h i)
      (by rw [rem_one, rem_zero]; exact hhm) (fun j hj => rem_pos_of_lt_termIndex hj) i hi
    rw [rem_zero] at h2
    exact h2

end DK

/-! ### S12-f (part 3): the height tool with only `gcd(h, m) = 1`

With the ladder of `h/m` supplied by `ladder_of_coprime`, the S12 statements lose their ladder
hypothesis: `K(h/m) = Σ_{1 ≤ i ≤ n} a_i` is the sum of the partial quotients (`cfK`), and for every
rotation `0 < h < m` coprime to `m`: `|log n_y − log n_x| ≤ (K − 1)·Var(μ_h)` for all positions
(`height_le_varMu_coprime`), `B ≤ (K − 1)·Var(μ_h)` relative to the minimum (`height_le_varMu_coprime'`),
`B ≤ (K − 1)(V_h log 2 + 2δ)` (`height_le_coprime`, the composed height bound), and the denominator
law for every mismatch count (`dk_denominator_law_coprime`, `word_dk_denominator_law_coprime`).
Nothing external remains: the only hypotheses are the cycle (or the positive word with `D_w > 0`
and distinct rotated intercepts), the rotation, and the mismatch count. -/

namespace DK

/-- The sum of the partial quotients of `h/m`: the side lane's `K(h/m)`. -/
def cfK (m h : ℕ) : ℕ := ∑ i ∈ Finset.Icc 1 (termIndex m h), quot m h i

/-- `K(h/m) ≥ 1` for `h > 0` (the first quotient is `≥ 1`). -/
theorem one_le_cfK {m h : ℕ} (hh : 0 < h) : 1 ≤ cfK m h := by
  unfold cfK
  calc 1 ≤ quot m h 1 := one_le_quot m h 1
    _ ≤ ∑ i ∈ Finset.Icc 1 (termIndex m h), quot m h i :=
      Finset.single_le_sum (fun _ _ => Nat.zero_le _)
        (Finset.mem_Icc.mpr ⟨le_rfl, termIndex_pos hh⟩)

end DK

namespace OddCycle

variable {m : ℕ} (Γ : OddCycle m)

/-- **The height bound for every coprime rotation**: `|log n_y − log n_x| ≤ (K − 1)·Var(μ_h)`. -/
theorem height_le_varMu_coprime {h : ℕ} (hh : 0 < h) (hhm : h < m) (hcop : Nat.Coprime h m)
    (x y : ℕ) :
    |Real.log (Γ.n y) - Real.log (Γ.n x)| ≤ ((DK.cfK m h : ℝ) - 1) * Γ.varMu h := by
  obtain ⟨L, hn, hqn, hadm⟩ := DK.ladder_of_coprime hh hhm hcop
  exact Γ.height_le_varMu hhm.le hcop L hn hqn hadm x y

/-- Relative to the minimum: `B ≤ (K − 1)·Var(μ_h)`. -/
theorem height_le_varMu_coprime' {h : ℕ} (hh : 0 < h) (hhm : h < m) (hcop : Nat.Coprime h m)
    (y : ℕ) : Real.log (Γ.n y) - Real.log (Γ.n 0) ≤ ((DK.cfK m h : ℝ) - 1) * Γ.varMu h :=
  le_trans (le_abs_self _) (Γ.height_le_varMu_coprime hh hhm hcop 0 y)

/-- **The composed height bound**: `B ≤ (K − 1)(V_h log 2 + 2δ)` for every coprime rotation. -/
theorem height_le_coprime {h : ℕ} (hh : 0 < h) (hhm : h < m) (hcop : Nat.Coprime h m) (y : ℕ) :
    Real.log (Γ.n y) - Real.log (Γ.n 0) ≤ ((DK.cfK m h : ℝ) - 1) *
      ((Γ.Vh h : ℝ) * Real.log 2 + 2 * ((Γ.Apre m : ℝ) * Real.log 2 - m * Real.log 3)) := by
  have h1 := Γ.height_le_varMu_coprime' hh hhm hcop y
  have h2 := Γ.varMu_le_Vh h
  have hK : (1 : ℝ) ≤ DK.cfK m h := by exact_mod_cast DK.one_le_cfK (m := m) hh
  exact h1.trans (mul_le_mul_of_nonneg_left h2 (by linarith))

/-- **S12's denominator law for every coprime rotation and mismatch count.** -/
theorem dk_denominator_law_coprime (hprim : ∀ i j, i < m → j < m → Γ.n i = Γ.n j → i = j)
    {h : ℕ} (hh : 0 < h) (hhm : h < m) (hcop : Nat.Coprime h m) {s : ℕ} (hs1 : 1 ≤ s)
    (hs : (Γ.mis h).card = s) :
    Real.log 2 + (((m - 1) / s : ℕ) : ℝ) * Real.log 3 <
      Real.log (Γ.q) + (Real.log m + (Γ.Apre m : ℝ) * Real.log 2 - Real.log 3 -
          Real.log ((2 : ℝ) ^ Γ.Apre m - 3 ^ m)) +
        ((DK.cfK m h : ℝ) - 1) *
          ((Γ.Vh h : ℝ) * Real.log 2 + 2 * ((Γ.Apre m : ℝ) * Real.log 2 - m * Real.log 3)) := by
  obtain ⟨L, hn, hqn, hadm⟩ := DK.ladder_of_coprime hh hhm hcop
  exact Γ.dk_denominator_law hprim hhm.le hcop L hn hqn hadm hs1 hs

end OddCycle

namespace OddCycle

/-- **S12's denominator law for words, every coprime rotation and mismatch count.** -/
theorem word_dk_denominator_law_coprime (w : List ℕ) (hw0 : w ≠ []) (hpos : ∀ x ∈ w, 1 ≤ x)
    (hD : 0 < D w)
    (hdist : ∀ i j, i < w.length → j < w.length → C (w.rotate i) = C (w.rotate j) → i = j)
    {h : ℕ} (hh : 0 < h) (hhm : h < w.length) (hcop : Nat.Coprime h w.length) {s : ℕ}
    (hs1 : 1 ≤ s)
    (hs : ((Finset.range w.length).filter
      (fun i => (w.rotate i).headD 0 ≠ (w.rotate (i + h)).headD 0)).card = s) :
    Real.log 2 + (((w.length - 1) / s : ℕ) : ℝ) * Real.log 3 <
      Real.log (den w) + (Real.log w.length + (w.sum : ℝ) * Real.log 2 - Real.log 3 -
          Real.log ((2 : ℝ) ^ w.sum - 3 ^ w.length)) +
        ((DK.cfK w.length h : ℝ) - 1) *
          (((∑ t ∈ Finset.range w.length,
              Int.natAbs (((w.rotate t).headD 0 : ℤ) - ((w.rotate (t + h)).headD 0 : ℤ)) : ℕ) : ℝ) *
              Real.log 2 +
            2 * ((w.sum : ℝ) * Real.log 2 - w.length * Real.log 3)) := by
  obtain ⟨L, hn, hqn, hadm⟩ := DK.ladder_of_coprime hh hhm hcop
  exact word_dk_denominator_law' w hw0 hpos hD hdist hhm.le hcop L hn hqn hadm hs1 hs

end OddCycle

/-! ### C002-b (part 1): the proportional-slope denominator theorem (6)–(8)

Main's C002 `PROPORTIONAL.md` §2. Blocks `u, v` whose valuation slopes have a common ratio:
`Σu = a r`, `|u| = b r`, `Σv = a s`, `|v| = b s`, with `U = 2^a`, `V = 3^b`, `H_j = U^j − V^j`, and the
word `w = u^k v^ℓ` with `M = rk`, `N = sℓ`, `L = M + N`, `h = gcd(M, N)`, `e = gcd(r, s)`, `E = H_e`.
`E ∣ K` for the commutator `K = D_u C_v − D_v C_u` (`E_dvd_commutator`). Writing `K = E J` and
`|J| = 2^α 3^β J₀` for any factorisation (the prose's `J₀`, the part of `|J|` prime to `6`, is the case
`α = v₂(J)`, `β = v₃(J)`; `J₀ = |J|` is also allowed): (6) `gcd(C_w, D_w) ∣ J₀ H_h`
(`proportional_gcd_dvd`), from the quotient identities `D_u G_u(k) = H_M`, `D_v G_v(ℓ) = H_N`, the
strong divisibility `gcd(H_M, H_N) = H_h` (`gcd_pow_sub_pow`) and C002-a's `g ∣ |K| gcd(G_u, G_v)`
(`gcd_dvd_K_mul_gcd`), the factors `2` and `3` removed because `g ∣ D_w` is prime to `6`
(`gcd_coprime_six'`); (7) for `K ≠ 0`, `den(w) J₀ > U^(L−h) ≥ U^max(M,N)` and `(den(w) J₀)² > U^L`
(`proportional_den_lower`), from `H_L > H_h U^(L−h)` (`pow_sub_pow_mul_pow_lt`: the difference is
`V^h (U^(L−h) − V^(L−h))`) and `h ≤ min(M, N)`; (8) a bound `den(w) ≤ d₀` forces
`U^max(rk, sℓ) < d₀ J₀` (`proportional_rectangle`). Hypotheses: positive letters, `U > V`, `k, ℓ ≥ 1`;
`gcd(a, b) = 1` is not needed (every representation of the common slope works, the reduced one being
the prose's). The degenerate case `K = 0` (both blocks powers of one primitive word) and §4's family
are not part of this unit. -/

section Proportional

/-- `x^e − y^e ∣ x^n − y^n` when `e ∣ n`. -/
theorem pow_sub_pow_dvd_of_dvd (x y : ℤ) {e n : ℕ} (h : e ∣ n) :
    x ^ e - y ^ e ∣ x ^ n - y ^ n := by
  obtain ⟨t, rfl⟩ := h
  rw [pow_mul, pow_mul]
  exact sub_dvd_pow_sub_pow _ _ _

/-- The strict geometric gap `H_h · U^(L−h) < H_L` for `0 < V < U` and `h < L`: the difference is
`V^h (U^(L−h) − V^(L−h))`. -/
theorem pow_sub_pow_mul_pow_lt {U V : ℤ} (hV : 0 < V) (hUV : V < U) {h L : ℕ} (hL : h < L) :
    (U ^ h - V ^ h) * U ^ (L - h) < U ^ L - V ^ L := by
  have eU : U ^ L = U ^ h * U ^ (L - h) := by rw [← pow_add, Nat.add_sub_cancel' hL.le]
  have eV : V ^ L = V ^ h * V ^ (L - h) := by rw [← pow_add, Nat.add_sub_cancel' hL.le]
  have hlt : V ^ (L - h) < U ^ (L - h) := pow_lt_pow_left₀ hUV hV.le (by omega)
  have hpos : 0 < V ^ h * (U ^ (L - h) - V ^ (L - h)) :=
    mul_pos (pow_pos hV h) (sub_pos.mpr hlt)
  have key : U ^ L - V ^ L - (U ^ h - V ^ h) * U ^ (L - h)
      = V ^ h * (U ^ (L - h) - V ^ (L - h)) := by
    rw [eU, eV]; ring
  linarith

/-- `E = H_gcd(r,s)` divides the commutator `K = D_u C_v − D_v C_u` of proportional blocks
(`Σu = a r`, `|u| = b r`, `Σv = a s`, `|v| = b s`). -/
theorem E_dvd_commutator (a b r s : ℕ) (u v : List ℕ) (hus : u.sum = a * r)
    (hul : u.length = b * r) (hvs : v.sum = a * s) (hvl : v.length = b * s) :
    ((2 : ℤ) ^ a) ^ Nat.gcd r s - ((3 : ℤ) ^ b) ^ Nat.gcd r s ∣ D u * C v - D v * C u := by
  have hDu : ((2 : ℤ) ^ a) ^ Nat.gcd r s - ((3 : ℤ) ^ b) ^ Nat.gcd r s ∣ D u := by
    rw [D, hus, hul, pow_mul, pow_mul]
    exact pow_sub_pow_dvd_of_dvd _ _ (Nat.gcd_dvd_left r s)
  have hDv : ((2 : ℤ) ^ a) ^ Nat.gcd r s - ((3 : ℤ) ^ b) ^ Nat.gcd r s ∣ D v := by
    rw [D, hvs, hvl, pow_mul, pow_mul]
    exact pow_sub_pow_dvd_of_dvd _ _ (Nat.gcd_dvd_right r s)
  exact (hDu.mul_right _).sub (hDv.mul_right _)

/-- **C002's (6).** Proportional blocks with `U = 2^a > V = 3^b`, `k, ℓ ≥ 1`, `K = E J` and any
factorisation `|J| = 2^α 3^β J₀`: `gcd(C_w, D_w) ∣ J₀ · H_h` for `w = u^k v^ℓ`, `h = gcd(rk, sℓ)`. -/
theorem proportional_gcd_dvd (a b r s : ℕ) (u v : List ℕ) (hu : ∀ x ∈ u, 1 ≤ x)
    (hv : ∀ x ∈ v, 1 ≤ x) (hu0 : u ≠ []) (hv0 : v ≠ []) (hus : u.sum = a * r)
    (hul : u.length = b * r) (hvs : v.sum = a * s) (hvl : v.length = b * s)
    (hUV : (3 : ℤ) ^ b < 2 ^ a) (k l : ℕ) (hk : 1 ≤ k) (hl : 1 ≤ l) (J : ℤ)
    (hJ : D u * C v - D v * C u
      = (((2 : ℤ) ^ a) ^ Nat.gcd r s - ((3 : ℤ) ^ b) ^ Nat.gcd r s) * J)
    (α β J0 : ℕ) (hJ0 : J.natAbs = 2 ^ α * 3 ^ β * J0) :
    (Int.gcd (C (rep u k ++ rep v l)) (D (rep u k ++ rep v l)) : ℤ)
      ∣ (J0 : ℤ) * (((2 : ℤ) ^ a) ^ Nat.gcd (r * k) (s * l)
          - ((3 : ℤ) ^ b) ^ Nat.gcd (r * k) (s * l)) := by
  -- positivity of the data
  have hr : 1 ≤ r := by
    have h1 := List.length_pos_of_ne_nil hu0
    rw [hul] at h1
    by_contra h
    rw [show r = 0 by omega, mul_zero] at h1
    exact absurd h1 (lt_irrefl 0)
  have he : 0 < Nat.gcd r s := Nat.gcd_pos_of_pos_left _ hr
  have hh : 0 < Nat.gcd (r * k) (s * l) := Nat.gcd_pos_of_pos_left _ (Nat.mul_pos hr hk)
  have hV : (0 : ℤ) < 3 ^ b := by positivity
  have hE : (0 : ℤ) < ((2 : ℤ) ^ a) ^ Nat.gcd r s - ((3 : ℤ) ^ b) ^ Nat.gcd r s :=
    sub_pos.mpr (pow_lt_pow_left₀ hUV hV.le he.ne')
  have hH : (0 : ℤ) < ((2 : ℤ) ^ a) ^ Nat.gcd (r * k) (s * l)
      - ((3 : ℤ) ^ b) ^ Nat.gcd (r * k) (s * l) :=
    sub_pos.mpr (pow_lt_pow_left₀ hUV hV.le hh.ne')
  -- the block denominators and the quotient identities `D_u G_u(k) = H_M`, `D_v G_v(ℓ) = H_N`
  have hDu : D u = ((2 : ℤ) ^ a) ^ r - ((3 : ℤ) ^ b) ^ r := by
    rw [D, hus, hul, pow_mul, pow_mul]
  have hDv : D v = ((2 : ℤ) ^ a) ^ s - ((3 : ℤ) ^ b) ^ s := by
    rw [D, hvs, hvl, pow_mul, pow_mul]
  have hGu : D u * G (2 ^ u.sum) (3 ^ u.length) k
      = ((2 : ℤ) ^ a) ^ (r * k) - ((3 : ℤ) ^ b) ^ (r * k) := by
    rw [D, G_mul, hus, hul]
    ring
  have hGv : D v * G (2 ^ v.sum) (3 ^ v.length) l
      = ((2 : ℤ) ^ a) ^ (s * l) - ((3 : ℤ) ^ b) ^ (s * l) := by
    rw [D, G_mul, hvs, hvl]
    ring
  -- `E` divides both block denominators
  have hEu : ((2 : ℤ) ^ a) ^ Nat.gcd r s - ((3 : ℤ) ^ b) ^ Nat.gcd r s ∣ D u := by
    rw [hDu]
    exact pow_sub_pow_dvd_of_dvd _ _ (Nat.gcd_dvd_left r s)
  have hEv : ((2 : ℤ) ^ a) ^ Nat.gcd r s - ((3 : ℤ) ^ b) ^ Nat.gcd r s ∣ D v := by
    rw [hDv]
    exact pow_sub_pow_dvd_of_dvd _ _ (Nat.gcd_dvd_right r s)
  obtain ⟨tu, htu⟩ := hEu
  obtain ⟨tv, htv⟩ := hEv
  -- C002-a's divisibility `g ∣ |K| gcd(G_u, G_v)`, in `ℤ`
  have hgK := gcd_dvd_K_mul_gcd u v k l hu hu0 hv hv0 hk hl
  have hgKZ : (Int.gcd (C (rep u k ++ rep v l)) (D (rep u k ++ rep v l)) : ℤ)
      ∣ ((D u * C v - D v * C u).natAbs : ℤ)
        * (Int.gcd (G (2 ^ u.sum) (3 ^ u.length) k) (G (2 ^ v.sum) (3 ^ v.length) l) : ℤ) := by
    exact_mod_cast Int.natCast_dvd_natCast.mpr hgK
  -- the words' positivity data, for the coprimality to `6`
  have hsum : 1 ≤ (rep u k ++ rep v l).sum := by
    rw [List.sum_append, rep_sum, rep_sum]
    have h1 := Nat.mul_pos hk (one_le_sum_of_ne_nil hu0 hu)
    omega
  have hlen : 1 ≤ (rep u k ++ rep v l).length := by
    rw [List.length_append, rep_length, rep_length]
    have h1 := Nat.mul_pos hk (List.length_pos_of_ne_nil hu0)
    omega
  have hc6 := gcd_coprime_six' (rep u k ++ rep v l) hsum hlen
  -- abbreviations
  set E : ℤ := ((2 : ℤ) ^ a) ^ Nat.gcd r s - ((3 : ℤ) ^ b) ^ Nat.gcd r s with hEdef
  set Gu : ℤ := G (2 ^ u.sum) (3 ^ u.length) k with hGudef
  set Gv : ℤ := G (2 ^ v.sum) (3 ^ v.length) l with hGvdef
  set HM : ℤ := ((2 : ℤ) ^ a) ^ (r * k) - ((3 : ℤ) ^ b) ^ (r * k) with hHMdef
  set HN : ℤ := ((2 : ℤ) ^ a) ^ (s * l) - ((3 : ℤ) ^ b) ^ (s * l) with hHNdef
  set Hh : ℤ := ((2 : ℤ) ^ a) ^ Nat.gcd (r * k) (s * l)
    - ((3 : ℤ) ^ b) ^ Nat.gcd (r * k) (s * l) with hHhdef
  set g : ℕ := Int.gcd (C (rep u k ++ rep v l)) (D (rep u k ++ rep v l)) with hgdef
  -- `E (t_u G_u) = H_M`, `E (t_v G_v) = H_N`
  have hX : E * (tu * Gu) = HM := by rw [← mul_assoc, ← htu, hGu]
  have hY : E * (tv * Gv) = HN := by rw [← mul_assoc, ← htv, hGv]
  -- strong divisibility: `gcd(H_M, H_N) = H_h`
  have hcop23 : IsCoprime ((2 : ℤ) ^ a) ((3 : ℤ) ^ b) :=
    (Int.isCoprime_iff_gcd_eq_one.mpr (by decide)).pow
  have hsd : Int.gcd HM HN = Hh.natAbs :=
    gcd_pow_sub_pow ((2 : ℤ) ^ a) ((3 : ℤ) ^ b) hcop23 (r * k) (s * l)
  -- `gcd(G_u, G_v) ∣ gcd(t_u G_u, t_v G_v)` and `E · gcd(t_u G_u, t_v G_v) = H_h`
  have hdiv : (Int.gcd Gu Gv : ℤ) ∣ ((Int.gcd (tu * Gu) (tv * Gv) : ℕ) : ℤ) := by
    apply Int.natCast_dvd_natCast.mpr
    apply Int.dvd_gcd
    · exact (Int.gcd_dvd_left _ _).trans (Dvd.intro_left tu rfl)
    · exact (Int.gcd_dvd_right _ _).trans (Dvd.intro_left tv rfl)
  have hEg : E * (Int.gcd (tu * Gu) (tv * Gv) : ℤ) = Hh := by
    have h1 : Int.gcd (E * (tu * Gu)) (E * (tv * Gv)) = E.natAbs * Int.gcd (tu * Gu) (tv * Gv) :=
      Int.gcd_mul_left E _ _
    rw [hX, hY, hsd] at h1
    have h2 : ((Hh.natAbs : ℕ) : ℤ) = ((E.natAbs : ℕ) : ℤ) * (Int.gcd (tu * Gu) (tv * Gv) : ℤ) := by
      exact_mod_cast h1
    rw [Int.natAbs_of_nonneg hH.le, Int.natAbs_of_nonneg hE.le] at h2
    exact h2.symm
  have hEgdvd : E * (Int.gcd Gu Gv : ℤ) ∣ Hh := by
    rw [← hEg]
    exact mul_dvd_mul_left E hdiv
  -- `|K| = E · 2^α 3^β J₀`
  have hKabs : ((D u * C v - D v * C u).natAbs : ℤ) = E * ((2 : ℤ) ^ α * 3 ^ β * J0) := by
    rw [Int.natCast_natAbs, hJ, abs_mul, abs_of_pos hE, ← Int.natCast_natAbs, hJ0]
    push_cast
    ring
  -- assemble: `g ∣ 2^α 3^β J₀ · (E gcd(G_u, G_v)) ∣ 2^α 3^β · (J₀ H_h)`
  have hg1 : (g : ℤ) ∣ ((2 : ℤ) ^ α * 3 ^ β) * ((J0 : ℤ) * Hh) := by
    have h2 : ((D u * C v - D v * C u).natAbs : ℤ) * (Int.gcd Gu Gv : ℤ)
        = ((2 : ℤ) ^ α * 3 ^ β * J0) * (E * (Int.gcd Gu Gv : ℤ)) := by
      rw [hKabs]
      ring
    rw [h2] at hgKZ
    have h3 := hgKZ.trans (mul_dvd_mul_left ((2 : ℤ) ^ α * 3 ^ β * J0) hEgdvd)
    have h4 : ((2 : ℤ) ^ α * 3 ^ β * J0) * Hh = ((2 : ℤ) ^ α * 3 ^ β) * ((J0 : ℤ) * Hh) := by
      ring
    rw [h4] at h3
    exact h3
  -- remove the factors `2` and `3`
  have hcopN : Nat.Coprime g (2 ^ α * 3 ^ β) :=
    Nat.Coprime.mul_right ((hc6.coprime_dvd_right (by norm_num : 2 ∣ 6)).pow_right α)
      ((hc6.coprime_dvd_right (by norm_num : 3 ∣ 6)).pow_right β)
  have hcopZ : IsCoprime (g : ℤ) ((2 : ℤ) ^ α * 3 ^ β) := by
    have := Nat.isCoprime_iff_coprime.mpr hcopN
    push_cast at this
    exact this
  exact hcopZ.dvd_of_dvd_mul_left hg1

/-- **C002's (7).** For `K ≠ 0`: `den(w) J₀ > U^(L−h) ≥ U^max(rk, sℓ)`, and the half-exponent
bound `(den(w) J₀)² > U^L`. -/
theorem proportional_den_lower (a b r s : ℕ) (u v : List ℕ) (hu : ∀ x ∈ u, 1 ≤ x)
    (hv : ∀ x ∈ v, 1 ≤ x) (hu0 : u ≠ []) (hv0 : v ≠ []) (hus : u.sum = a * r)
    (hul : u.length = b * r) (hvs : v.sum = a * s) (hvl : v.length = b * s)
    (hUV : (3 : ℤ) ^ b < 2 ^ a) (k l : ℕ) (hk : 1 ≤ k) (hl : 1 ≤ l) (J : ℤ)
    (hJ : D u * C v - D v * C u
      = (((2 : ℤ) ^ a) ^ Nat.gcd r s - ((3 : ℤ) ^ b) ^ Nat.gcd r s) * J)
    (hK : D u * C v - D v * C u ≠ 0)
    (α β J0 : ℕ) (hJ0 : J.natAbs = 2 ^ α * 3 ^ β * J0) :
    ((2 : ℤ) ^ a) ^ (r * k + s * l - Nat.gcd (r * k) (s * l))
        < den (rep u k ++ rep v l) * J0 ∧
      ((2 : ℤ) ^ a) ^ max (r * k) (s * l) < den (rep u k ++ rep v l) * J0 ∧
      ((2 : ℤ) ^ a) ^ (r * k + s * l) < (den (rep u k ++ rep v l) * J0) ^ 2 := by
  have hg := proportional_gcd_dvd a b r s u v hu hv hu0 hv0 hus hul hvs hvl hUV k l hk hl J hJ
    α β J0 hJ0
  -- `J₀ ≥ 1`
  have hJ0pos : (1 : ℤ) ≤ J0 := by
    have hne : J0 ≠ 0 := by
      intro h0
      rw [h0, mul_zero] at hJ0
      have hJz : J = 0 := Int.natAbs_eq_zero.mp hJ0
      rw [hJz, mul_zero] at hJ
      exact hK hJ
    exact_mod_cast Nat.one_le_iff_ne_zero.mpr hne
  -- positivity of the data
  have hr : 1 ≤ r := by
    have h1 := List.length_pos_of_ne_nil hu0
    rw [hul] at h1
    by_contra h
    rw [show r = 0 by omega, mul_zero] at h1
    exact absurd h1 (lt_irrefl 0)
  have hs : 1 ≤ s := by
    have h1 := List.length_pos_of_ne_nil hv0
    rw [hvl] at h1
    by_contra h
    rw [show s = 0 by omega, mul_zero] at h1
    exact absurd h1 (lt_irrefl 0)
  have hM : 0 < r * k := Nat.mul_pos hr hk
  have hN : 0 < s * l := Nat.mul_pos hs hl
  have hh : 0 < Nat.gcd (r * k) (s * l) := Nat.gcd_pos_of_pos_left _ hM
  have hh1 : Nat.gcd (r * k) (s * l) ≤ r * k := Nat.gcd_le_left _ hM
  have hh2 : Nat.gcd (r * k) (s * l) ≤ s * l := Nat.gcd_le_right _ hN
  have hL : Nat.gcd (r * k) (s * l) < r * k + s * l := by omega
  have hV : (0 : ℤ) < 3 ^ b := by positivity
  have hU1 : (1 : ℤ) ≤ 2 ^ a := one_le_pow₀ (by norm_num)
  have hHh : (0 : ℤ) < ((2 : ℤ) ^ a) ^ Nat.gcd (r * k) (s * l)
      - ((3 : ℤ) ^ b) ^ Nat.gcd (r * k) (s * l) :=
    sub_pos.mpr (pow_lt_pow_left₀ hUV hV.le hh.ne')
  -- `D_w = U^L − V^L > 0`, the reduced denominator and the cancellation factor
  have hDw : D (rep u k ++ rep v l)
      = ((2 : ℤ) ^ a) ^ (r * k + s * l) - ((3 : ℤ) ^ b) ^ (r * k + s * l) := by
    rw [D, List.sum_append, List.length_append, rep_sum, rep_sum, rep_length, rep_length,
      hus, hul, hvs, hvl]
    ring
  have hDpos : 0 < D (rep u k ++ rep v l) := by
    rw [hDw]
    exact sub_pos.mpr (pow_lt_pow_left₀ hUV hV.le (by omega))
  have hlen : 1 ≤ (rep u k ++ rep v l).length := by
    rw [List.length_append, rep_length, rep_length]
    have h1 := Nat.mul_pos hk (List.length_pos_of_ne_nil hu0)
    omega
  have hw0 : rep u k ++ rep v l ≠ [] := List.ne_nil_of_length_pos hlen
  have hgpos : (0 : ℤ) < OddCycle.gcdCD (rep u k ++ rep v l) := OddCycle.gcdCD_pos _ hw0
  have hden : OddCycle.gcdCD (rep u k ++ rep v l) * den (rep u k ++ rep v l)
      = D (rep u k ++ rep v l) := OddCycle.gcdCD_mul_den _
  have hdenpos : 0 < den (rep u k ++ rep v l) :=
    Int.ediv_pos_of_pos_of_dvd hDpos hgpos.le (OddCycle.gcdCD_dvd_D _)
  have hg' : OddCycle.gcdCD (rep u k ++ rep v l)
      ∣ (J0 : ℤ) * (((2 : ℤ) ^ a) ^ Nat.gcd (r * k) (s * l)
          - ((3 : ℤ) ^ b) ^ Nat.gcd (r * k) (s * l)) := hg
  have hgle : OddCycle.gcdCD (rep u k ++ rep v l)
      ≤ (J0 : ℤ) * (((2 : ℤ) ^ a) ^ Nat.gcd (r * k) (s * l)
          - ((3 : ℤ) ^ b) ^ Nat.gcd (r * k) (s * l)) :=
    Int.le_of_dvd (mul_pos (by linarith) hHh) hg'
  -- the chain `H_h U^(L−h) < H_L = D_w = den · g ≤ den · J₀ H_h`
  have hgap := pow_sub_pow_mul_pow_lt hV hUV hL
  have h7a : ((2 : ℤ) ^ a) ^ (r * k + s * l - Nat.gcd (r * k) (s * l))
      < den (rep u k ++ rep v l) * J0 := by
    have h1 : ((2 : ℤ) ^ a) ^ (r * k + s * l - Nat.gcd (r * k) (s * l))
          * (((2 : ℤ) ^ a) ^ Nat.gcd (r * k) (s * l) - ((3 : ℤ) ^ b) ^ Nat.gcd (r * k) (s * l))
        < (den (rep u k ++ rep v l) * J0)
          * (((2 : ℤ) ^ a) ^ Nat.gcd (r * k) (s * l)
            - ((3 : ℤ) ^ b) ^ Nat.gcd (r * k) (s * l)) := by
      calc ((2 : ℤ) ^ a) ^ (r * k + s * l - Nat.gcd (r * k) (s * l))
            * (((2 : ℤ) ^ a) ^ Nat.gcd (r * k) (s * l) - ((3 : ℤ) ^ b) ^ Nat.gcd (r * k) (s * l))
          = (((2 : ℤ) ^ a) ^ Nat.gcd (r * k) (s * l) - ((3 : ℤ) ^ b) ^ Nat.gcd (r * k) (s * l))
            * ((2 : ℤ) ^ a) ^ (r * k + s * l - Nat.gcd (r * k) (s * l)) := mul_comm _ _
        _ < ((2 : ℤ) ^ a) ^ (r * k + s * l) - ((3 : ℤ) ^ b) ^ (r * k + s * l) := hgap
        _ = D (rep u k ++ rep v l) := hDw.symm
        _ = den (rep u k ++ rep v l) * OddCycle.gcdCD (rep u k ++ rep v l) := by
          rw [← hden]; ring
        _ ≤ den (rep u k ++ rep v l) * ((J0 : ℤ) * (((2 : ℤ) ^ a) ^ Nat.gcd (r * k) (s * l)
              - ((3 : ℤ) ^ b) ^ Nat.gcd (r * k) (s * l))) :=
          mul_le_mul_of_nonneg_left hgle hdenpos.le
        _ = (den (rep u k ++ rep v l) * J0)
            * (((2 : ℤ) ^ a) ^ Nat.gcd (r * k) (s * l)
              - ((3 : ℤ) ^ b) ^ Nat.gcd (r * k) (s * l)) := by ring
    exact lt_of_mul_lt_mul_right h1 hHh.le
  have hmax : max (r * k) (s * l) ≤ r * k + s * l - Nat.gcd (r * k) (s * l) := by omega
  have h7b : ((2 : ℤ) ^ a) ^ max (r * k) (s * l) < den (rep u k ++ rep v l) * J0 :=
    lt_of_le_of_lt (pow_le_pow_right₀ hU1 hmax) h7a
  have h2max : r * k + s * l ≤ 2 * max (r * k) (s * l) := by omega
  have h7c : ((2 : ℤ) ^ a) ^ (r * k + s * l) < (den (rep u k ++ rep v l) * J0) ^ 2 := by
    calc ((2 : ℤ) ^ a) ^ (r * k + s * l)
        ≤ ((2 : ℤ) ^ a) ^ (2 * max (r * k) (s * l)) := pow_le_pow_right₀ hU1 h2max
      _ = ((2 : ℤ) ^ a) ^ max (r * k) (s * l) * ((2 : ℤ) ^ a) ^ max (r * k) (s * l) := by
        rw [two_mul, pow_add]
      _ < (den (rep u k ++ rep v l) * J0) * (den (rep u k ++ rep v l) * J0) :=
        mul_self_lt_mul_self (by positivity) h7b
      _ = (den (rep u k ++ rep v l) * J0) ^ 2 := (sq _).symm
  exact ⟨h7a, h7b, h7c⟩

/-- **C002's (8).** A bound `den(w) ≤ d₀` confines both repetition counts to the finite rectangle
`U^max(rk, sℓ) < d₀ J₀`. -/
theorem proportional_rectangle (a b r s : ℕ) (u v : List ℕ) (hu : ∀ x ∈ u, 1 ≤ x)
    (hv : ∀ x ∈ v, 1 ≤ x) (hu0 : u ≠ []) (hv0 : v ≠ []) (hus : u.sum = a * r)
    (hul : u.length = b * r) (hvs : v.sum = a * s) (hvl : v.length = b * s)
    (hUV : (3 : ℤ) ^ b < 2 ^ a) (k l : ℕ) (hk : 1 ≤ k) (hl : 1 ≤ l) (J : ℤ)
    (hJ : D u * C v - D v * C u
      = (((2 : ℤ) ^ a) ^ Nat.gcd r s - ((3 : ℤ) ^ b) ^ Nat.gcd r s) * J)
    (hK : D u * C v - D v * C u ≠ 0)
    (α β J0 : ℕ) (hJ0 : J.natAbs = 2 ^ α * 3 ^ β * J0) (d0 : ℤ)
    (hd : den (rep u k ++ rep v l) ≤ d0) :
    ((2 : ℤ) ^ a) ^ max (r * k) (s * l) < d0 * J0 := by
  have h := (proportional_den_lower a b r s u v hu hv hu0 hv0 hus hul hvs hvl hUV k l hk hl J hJ
    hK α β J0 hJ0).2.1
  have hJ0 : (0 : ℤ) ≤ J0 := by positivity
  exact lt_of_lt_of_le h (mul_le_mul_of_nonneg_right hd hJ0)

end Proportional

/-! ### C002-b (part 2): the degenerate case `K = 0` — exact-valuation determinism in integer form

Main's C002 §2, "Degenerate case `K = 0`": `C_u/D_u = C_v/D_v` means both words are return words of
the same positive rational point, and determinism of the exact valuation makes their infinite
valuation words identical, so `u` and `v` are powers of one primitive word in the same phase. Integer
form, with no rational dynamics: for a positive word `u = a :: z`,
`3 C_u + D_u = 2^a · C(z ++ [a])` (`three_C_add_D`), where `C(z ++ [a])` and `D_u` are odd, so `a` is
the exact power of `2` in `3 C_u + D_u` — the valuation of `3 x₀ + 1` at `x₀ = C_u/D_u` — and
`C(rot u)/D_u` is the next point. If `K = 0`, i.e. `C_u D_v = C_v D_u`, then
`(3 C_u + D_u) D_v = (3 C_v + D_v) D_u` (`D` is rotation invariant, the file's `D_rotate`); the exact
power of two of an odd multiple is unique
(`two_pow_mul_odd_inj`), so the first letters agree and `K = 0` persists for the rotated pair
(`K0_step`). By induction every rotation has equal first letters (`K0_letters`): the two infinite
periodic valuation words coincide, hence each word has the period `gcd(|u|, |v|)`
(`K0_common_period`, through the elementary two-period lemma `period_gcd`). The list-level packaging
`u = z^(|u|/g)`, `v = z^(|v|/g)` with `z = u.take g` and the invariance `den(u^k v^ℓ) = den(z)` are
the remaining part. The prose's three controls keep their denominators: `den (1,2,2) = 5`,
`den (1,3) = 7`, `den (4) = 13` (`den_122`, `den_13`, `den_4`). -/

section KZero

/-- The first-step identity `3 C_(a::z) + D_(a::z) = 2^a · C_(z ++ [a])`. -/
theorem three_C_add_D (a : ℕ) (z : List ℕ) :
    3 * C (a :: z) + D (a :: z) = 2 ^ a * C (z ++ [a]) := by
  rw [C_append]
  simp only [C, D, List.sum_cons, List.length_cons, List.length_nil, pow_zero, mul_zero, add_zero]
  ring

/-- The first-step identity in rotation form: `3 C_w + D_w = 2^(w₀) · C(rot w)`. -/
theorem three_C_add_D_rotate (w : List ℕ) (hw : w ≠ []) :
    3 * C w + D w = 2 ^ (w.headD 0) * C (w.rotate 1) := by
  obtain ⟨a, z, rfl⟩ := List.exists_cons_of_ne_nil hw
  rw [List.headD_cons, List.rotate_cons_succ, List.rotate_zero]
  exact three_C_add_D a z

/-- The exact power of `2` in an odd multiple is unique. -/
theorem two_pow_mul_odd_inj {a b : ℕ} {o o' : ℤ} (ho : Odd o) (ho' : Odd o')
    (h : 2 ^ a * o = 2 ^ b * o') : a = b := by
  by_contra hne
  rcases Nat.lt_or_gt_of_ne hne with hlt | hlt
  · have h2 : (2 : ℤ) ^ b = 2 ^ a * 2 ^ (b - a) := by
      rw [← pow_add, Nat.add_sub_cancel' hlt.le]
    rw [h2, mul_assoc] at h
    have h3 : o = 2 ^ (b - a) * o' := mul_left_cancel₀ (pow_ne_zero a two_ne_zero) h
    have h4 : Even o := by
      rw [h3]
      exact (Int.even_pow.mpr ⟨even_two, by omega⟩).mul_right _
    exact (Int.not_even_iff_odd.mpr ho) h4
  · have h2 : (2 : ℤ) ^ a = 2 ^ b * 2 ^ (a - b) := by
      rw [← pow_add, Nat.add_sub_cancel' hlt.le]
    rw [h2, mul_assoc] at h
    have h3 : 2 ^ (a - b) * o = o' := mul_left_cancel₀ (pow_ne_zero b two_ne_zero) h
    have h4 : Even o' := by
      rw [← h3]
      exact (Int.even_pow.mpr ⟨even_two, by omega⟩).mul_right _
    exact (Int.not_even_iff_odd.mpr ho') h4

/-- Positive letters survive rotation. -/
theorem pos_rotate {w : List ℕ} (hw : ∀ x ∈ w, 1 ≤ x) (i : ℕ) : ∀ x ∈ w.rotate i, 1 ≤ x :=
  fun x hx => hw x (List.mem_rotate.mp hx)

/-- `D_w` is odd for a nonempty positive word. -/
theorem D_odd' {w : List ℕ} (hw : w ≠ []) (hpos : ∀ x ∈ w, 1 ≤ x) : Odd (D w) :=
  Int.not_even_iff_odd.mp
    (fun he => D_odd (one_le_sum_of_ne_nil hw hpos) (even_iff_two_dvd.mp he))

/-- **The `K = 0` step**: equal rational points have equal first letters, and the rotated pair again
has `K = 0`. -/
theorem K0_step {u v : List ℕ} (hu : ∀ x ∈ u, 1 ≤ x) (hv : ∀ x ∈ v, 1 ≤ x) (hu0 : u ≠ [])
    (hv0 : v ≠ []) (hK : C u * D v = C v * D u) :
    u.headD 0 = v.headD 0 ∧
      C (u.rotate 1) * D (v.rotate 1) = C (v.rotate 1) * D (u.rotate 1) := by
  have h1 : (3 * C u + D u) * D v = (3 * C v + D v) * D u := by linear_combination 3 * hK
  rw [three_C_add_D_rotate u hu0, three_C_add_D_rotate v hv0] at h1
  have hou : Odd (C (u.rotate 1) * D v) :=
    (C_odd (NarrowCycle.rotate_ne_nil hu0 1) (pos_rotate hu 1)).mul (D_odd' hv0 hv)
  have hov : Odd (C (v.rotate 1) * D u) :=
    (C_odd (NarrowCycle.rotate_ne_nil hv0 1) (pos_rotate hv 1)).mul (D_odd' hu0 hu)
  have h2 : 2 ^ (u.headD 0) * (C (u.rotate 1) * D v)
      = 2 ^ (v.headD 0) * (C (v.rotate 1) * D u) := by
    rw [← mul_assoc, ← mul_assoc]
    exact h1
  have hhead : u.headD 0 = v.headD 0 := two_pow_mul_odd_inj hou hov h2
  refine ⟨hhead, ?_⟩
  rw [hhead] at h2
  have h3 := mul_left_cancel₀ (pow_ne_zero _ two_ne_zero) h2
  rw [D_rotate, D_rotate]
  exact h3

/-- `K = 0` persists along all rotations. -/
theorem K0_rotate {u v : List ℕ} (hu : ∀ x ∈ u, 1 ≤ x) (hv : ∀ x ∈ v, 1 ≤ x) (hu0 : u ≠ [])
    (hv0 : v ≠ []) (hK : C u * D v = C v * D u) :
    ∀ i, C (u.rotate i) * D (v.rotate i) = C (v.rotate i) * D (u.rotate i) := by
  intro i
  induction i with
  | zero => simpa only [List.rotate_zero] using hK
  | succ i ih =>
    have h := (K0_step (pos_rotate hu i) (pos_rotate hv i) (NarrowCycle.rotate_ne_nil hu0 i)
      (NarrowCycle.rotate_ne_nil hv0 i) ih).2
    simp only [List.rotate_rotate] at h
    exact h

/-- **`K = 0` ⇒ the two infinite valuation words coincide**: every rotation has equal first
letters. -/
theorem K0_letters {u v : List ℕ} (hu : ∀ x ∈ u, 1 ≤ x) (hv : ∀ x ∈ v, 1 ≤ x) (hu0 : u ≠ [])
    (hv0 : v ≠ []) (hK : C u * D v = C v * D u) :
    ∀ i, (u.rotate i).headD 0 = (v.rotate i).headD 0 := fun i =>
  (K0_step (pos_rotate hu i) (pos_rotate hv i) (NarrowCycle.rotate_ne_nil hu0 i)
    (NarrowCycle.rotate_ne_nil hv0 i) (K0_rotate hu hv hu0 hv0 hK i)).1

/-- Two periods of a sequence give their gcd as a period. -/
theorem period_gcd {α : Type*} (f : ℕ → α) : ∀ m n : ℕ, (∀ i, f (i + m) = f i) →
    (∀ i, f (i + n) = f i) → ∀ i, f (i + Nat.gcd m n) = f i := by
  intro m n
  induction m, n using Nat.gcd.induction with
  | H0 n =>
    intro _ hn i
    rw [Nat.gcd_zero_left]
    exact hn i
  | H1 m n _ ih =>
    intro hm hn i
    rw [Nat.gcd_rec]
    apply ih ?_ hm
    intro j
    have hmul : ∀ q j, f (j + m * q) = f j := by
      intro q
      induction q with
      | zero => intro j; simp
      | succ q ihq =>
        intro j
        rw [Nat.mul_add_one, ← Nat.add_assoc, hm, ihq]
    have h := hn j
    rw [← Nat.mod_add_div n m, ← Nat.add_assoc, hmul] at h
    exact h

/-- Shifting the rotation index by the length does nothing. -/
theorem rotate_add_len (w : List ℕ) (i : ℕ) : w.rotate (i + w.length) = w.rotate i := by
  rw [← List.rotate_mod, Nat.add_mod_right, List.rotate_mod]

/-- **`K = 0` ⇒ both valuation words have the common period `gcd(|u|, |v|)`.** -/
theorem K0_common_period {u v : List ℕ} (hu : ∀ x ∈ u, 1 ≤ x) (hv : ∀ x ∈ v, 1 ≤ x)
    (hu0 : u ≠ []) (hv0 : v ≠ []) (hK : C u * D v = C v * D u) :
    (∀ i, (u.rotate (i + Nat.gcd u.length v.length)).headD 0 = (u.rotate i).headD 0) ∧
      (∀ i, (v.rotate (i + Nat.gcd u.length v.length)).headD 0 = (v.rotate i).headD 0) := by
  have hl := K0_letters hu hv hu0 hv0 hK
  have hpu : ∀ i, (u.rotate (i + u.length)).headD 0 = (u.rotate i).headD 0 := fun i => by
    rw [rotate_add_len]
  have hpv : ∀ i, (v.rotate (i + v.length)).headD 0 = (v.rotate i).headD 0 := fun i => by
    rw [rotate_add_len]
  have hpu' : ∀ i, (u.rotate (i + v.length)).headD 0 = (u.rotate i).headD 0 := fun i => by
    rw [hl, hpv, ← hl]
  have hpv' : ∀ i, (v.rotate (i + u.length)).headD 0 = (v.rotate i).headD 0 := fun i => by
    rw [← hl, hpu, hl]
  exact ⟨period_gcd (fun i => (u.rotate i).headD 0) u.length v.length hpu hpu',
    period_gcd (fun i => (v.rotate i).headD 0) u.length v.length hpv' hpv⟩

/-- The prose's three `K = 0` controls keep their denominators. -/
theorem den_122 : den [1, 2, 2] = 5 := by norm_num [den, OddCycle.gcdCD, C, D]

theorem den_13 : den [1, 3] = 7 := by norm_num [den, OddCycle.gcdCD, C, D]

theorem den_4 : den [4] = 13 := by norm_num [den, OddCycle.gcdCD, C, D]

end KZero

/-! ### S13-a: the rise lemma — one agreeing run of a rotation multiplies the log-height by at most `κ`

Side lane's S13 (`sidekick/research/S13/RISE_LEMMA.md`, §§1–2), in natural logarithms and with a
uniform `Δ`. For a primitive cycle with letters `≥ 1`, a forward offset `d` with `d ≢ 0 (mod m)`,
`η = q/(3 n₀)`, `κ = (log 3 + η)/log 2` and the potential `Φ_p = log n_p + log 2 + Δ`, where `Δ ≥ 0`
bounds `log n_(p+d) − log n_p` on the stretch: (W) the 2-adic start witness — on an agreeing run of
letter sum `F` from `i`, `2^(F+1) ∣ n_(i+d) − n_i ≠ 0`, hence `(F + 1) log 2 ≤ log n_i + Δ`
(`witness_two_pow`, `witness_log`; the nonvanishing is `z_ne_zero`, i.e. primitivity); (P) the rise
over `t` steps is at most `t (log 3 + η) − F log 2` (`rise_bound`, from `log_step` and `ε_t ≤ η`);
one run and its following letter multiply `Φ` by at most `κ` (`run_step`); chaining over the
mismatches of `[u, v)` — induction on their number, splitting at the least one — gives
`Φ_v ≤ κ^(k+1) Φ_u` (`rise_lemma`). From the minimum `n₀`: `Φ_j ≤ κ^(s+1) Φ_0` for every position
`j ≤ m`, `s = |mis d|` (`rise_from_min`), the natural-log form of S13's Corollary 1; and
`log n_(p+d) − log n_p ≤ d (log 3 + η − log 2)` (`rise_le_mul`), the uniform `Δ` of S13's
`Δ⁺ ≤ (σ + η) d`, giving `rise_from_min_uniform`. The orientation lemma `|mis (m − h)| = |mis h|` and
the explicit `s(h) ≥ log_κ(1 + B/c) − 1` are S13-b. -/

namespace OddCycle

variable {m : ℕ} (Γ : OddCycle m)

/-- `η = q/(3 n₀)`, the uniform bound on the per-step correction `ε_t`. -/
noncomputable def eta : ℝ := (Γ.q : ℝ) / (3 * (Γ.n 0 : ℝ))

/-- `κ = (log 3 + η)/log 2`, the rise factor of one agreeing run. -/
noncomputable def kappa : ℝ := (Real.log 3 + Γ.eta) / Real.log 2

/-- The rise potential `Φ_p = log n_p + log 2 + Δ`. -/
noncomputable def Phi (Δ : ℝ) (p : ℕ) : ℝ := Real.log (Γ.n p) + Real.log 2 + Δ

theorem eta_nonneg : 0 ≤ Γ.eta := by
  unfold eta
  have hq : (0 : ℝ) ≤ Γ.q := by exact_mod_cast Γ.hq.le
  have hn := Γ.n_cast_pos 0
  exact div_nonneg hq (by linarith)

/-- `ε_t ≤ η`: `log(1 + x) ≤ x` and `n_t ≥ n₀`. -/
theorem eps_le_eta (t : ℕ) : Γ.eps t ≤ Γ.eta := by
  unfold eps eta
  have hq : (0 : ℝ) ≤ Γ.q := by exact_mod_cast Γ.hq.le
  have hn0 := Γ.n_cast_pos 0
  have hnt := Γ.n_cast_pos t
  have hle : (Γ.n 0 : ℝ) ≤ Γ.n t := by exact_mod_cast Γ.nmin t
  have h1 : (0 : ℝ) < 1 + (Γ.q : ℝ) / (3 * (Γ.n t : ℝ)) := by
    have := div_nonneg hq (by linarith : (0 : ℝ) ≤ 3 * (Γ.n t : ℝ))
    linarith
  calc Real.log (1 + (Γ.q : ℝ) / (3 * (Γ.n t : ℝ)))
      ≤ 1 + (Γ.q : ℝ) / (3 * (Γ.n t : ℝ)) - 1 := Real.log_le_sub_one_of_pos h1
    _ = (Γ.q : ℝ) / (3 * (Γ.n t : ℝ)) := by ring
    _ ≤ (Γ.q : ℝ) / (3 * (Γ.n 0 : ℝ)) :=
      div_le_div_of_nonneg_left hq (by linarith) (by linarith)

theorem kappa_mul_log2 : Γ.kappa * Real.log 2 = Real.log 3 + Γ.eta := by
  unfold kappa
  have h2 : Real.log 2 ≠ 0 := (Real.log_pos (by norm_num)).ne'
  exact div_mul_cancel₀ _ h2

theorem one_le_kappa : 1 ≤ Γ.kappa := by
  unfold kappa
  have h2 : (0 : ℝ) < Real.log 2 := Real.log_pos (by norm_num)
  rw [le_div_iff₀ h2, one_mul]
  have := Γ.eta_nonneg
  have := Real.log_lt_log (by norm_num : (0 : ℝ) < 2) (by norm_num : (2 : ℝ) < 3)
  linarith

theorem Phi_nonneg {Δ : ℝ} (hΔ0 : 0 ≤ Δ) (p : ℕ) : 0 ≤ Γ.Phi Δ p := by
  unfold Phi
  have h1 : (1 : ℤ) ≤ Γ.n p := by
    have := Γ.npos.trans_le (Γ.nmin p)
    omega
  have h1R : (1 : ℝ) ≤ Γ.n p := by exact_mod_cast h1
  have := Real.log_nonneg h1R
  have := Real.log_pos (by norm_num : (1 : ℝ) < 2)
  linarith

/-- Letters `≥ 1`: a run of `s` letters has sum `≥ s`. -/
theorem le_runSum (hapos : ∀ i, 1 ≤ Γ.a i) (i s : ℕ) : s ≤ Γ.runSum i s := by
  unfold runSum
  calc s = ∑ _j ∈ Finset.range s, 1 := by simp
    _ ≤ ∑ j ∈ Finset.range s, Γ.a (i + j) := Finset.sum_le_sum (fun j _ => hapos _)

theorem runSum_mono (i : ℕ) {s t : ℕ} (hst : s ≤ t) : Γ.runSum i s ≤ Γ.runSum i t := by
  unfold runSum
  exact Finset.sum_le_sum_of_subset (Finset.range_mono hst)

/-- (P): the rise over `t` steps is at most `t (log 3 + η) − F log 2`. -/
theorem rise_bound (i : ℕ) : ∀ t : ℕ,
    Real.log (Γ.n (i + t)) - Real.log (Γ.n i)
      ≤ (t : ℝ) * (Real.log 3 + Γ.eta) - (Γ.runSum i t : ℝ) * Real.log 2 := by
  intro t
  induction t with
  | zero => simp [runSum]
  | succ t ih =>
    have hstep := Γ.log_step (i + t)
    have heps := Γ.eps_le_eta (i + t)
    rw [runSum_succ]
    push_cast
    show Real.log (Γ.n (i + t + 1)) - Real.log (Γ.n i) ≤ _
    linarith

/-- The uniform `Δ`: `log n_(p+d) − log n_p ≤ d (log 3 + η − log 2)`. -/
theorem rise_le_mul (hapos : ∀ i, 1 ≤ Γ.a i) (p d : ℕ) :
    Real.log (Γ.n (p + d)) - Real.log (Γ.n p)
      ≤ (d : ℝ) * (Real.log 3 + Γ.eta - Real.log 2) := by
  have h1 := Γ.rise_bound p d
  have h2 : (d : ℝ) ≤ Γ.runSum p d := by exact_mod_cast Γ.le_runSum hapos p d
  have h3 : (0 : ℝ) < Real.log 2 := Real.log_pos (by norm_num)
  have h4 : (d : ℝ) * Real.log 2 ≤ (Γ.runSum p d : ℝ) * Real.log 2 :=
    mul_le_mul_of_nonneg_right h2 h3.le
  linarith

/-- (W), 2-adic form: on an agreeing run of letter sum `F` from `i`, `2^(F+1) ∣ n_(i+d) − n_i`. -/
theorem witness_two_pow {d i : ℕ} (t : ℕ) (hrun : ∀ j, j < t → Γ.agree d (i + j)) :
    (2 : ℤ) ^ (Γ.runSum i t + 1) ∣ Γ.z d i := by
  obtain ⟨k, -, hk, -⟩ := Γ.z_run_factor t hrun
  exact Dvd.intro k hk.symm

/-- (W), logarithmic form: `(F + 1) log 2 ≤ log n_i + Δ` whenever `log n_(i+d) − log n_i ≤ Δ`. -/
theorem witness_log (hprim : ∀ i j, i < m → j < m → Γ.n i = Γ.n j → i = j) {d : ℕ}
    (hh : d % m ≠ 0) {Δ : ℝ} (hΔ0 : 0 ≤ Δ) {i : ℕ}
    (hΔ : Real.log (Γ.n (i + d)) - Real.log (Γ.n i) ≤ Δ) {t : ℕ}
    (hrun : ∀ j, j < t → Γ.agree d (i + j)) :
    ((Γ.runSum i t : ℝ) + 1) * Real.log 2 ≤ Real.log (Γ.n i) + Δ := by
  have hdvd := Γ.witness_two_pow t hrun
  have hz := Γ.z_ne_zero hprim hh i
  have hpos1 : 0 < Γ.n i := Γ.npos.trans_le (Γ.nmin _)
  have hpos2 : 0 < Γ.n (i + d) := Γ.npos.trans_le (Γ.nmin _)
  have hle : (2 : ℤ) ^ (Γ.runSum i t + 1) ≤ |Γ.z d i| :=
    Int.le_of_dvd (abs_pos.mpr hz) ((dvd_abs _ _).mpr hdvd)
  have hcase : (2 : ℤ) ^ (Γ.runSum i t + 1) ≤ Γ.n (i + d) ∨
      (2 : ℤ) ^ (Γ.runSum i t + 1) ≤ Γ.n i := by
    unfold z at hle
    rcases le_or_gt (Γ.n i) (Γ.n (i + d)) with h1 | h1
    · left
      rw [abs_of_nonneg (by linarith)] at hle
      linarith
    · right
      rw [abs_of_neg (by linarith)] at hle
      linarith
  have hlog2 : Real.log ((2 : ℝ) ^ (Γ.runSum i t + 1))
      = ((Γ.runSum i t : ℝ) + 1) * Real.log 2 := by
    rw [Real.log_pow, Nat.cast_add, Nat.cast_one]
  have hn1 := Γ.n_cast_pos i
  have hn2 := Γ.n_cast_pos (i + d)
  rcases hcase with h1 | h1
  · have h1R : (2 : ℝ) ^ (Γ.runSum i t + 1) ≤ Γ.n (i + d) := by exact_mod_cast h1
    have := Real.log_le_log (by positivity) h1R
    rw [hlog2] at this
    linarith
  · have h1R : (2 : ℝ) ^ (Γ.runSum i t + 1) ≤ Γ.n i := by exact_mod_cast h1
    have := Real.log_le_log (by positivity) h1R
    rw [hlog2] at this
    linarith

/-- **One run step.** If `[u, u + t)` agrees and `s ≤ t + 1`, then `Φ_(u+s) ≤ κ Φ_u`. -/
theorem run_step (hprim : ∀ i j, i < m → j < m → Γ.n i = Γ.n j → i = j)
    (hapos : ∀ i, 1 ≤ Γ.a i) {d : ℕ} (hh : d % m ≠ 0) {Δ : ℝ} (hΔ0 : 0 ≤ Δ) {u : ℕ}
    (hΔ : Real.log (Γ.n (u + d)) - Real.log (Γ.n u) ≤ Δ) {t : ℕ}
    (hrun : ∀ j, j < t → Γ.agree d (u + j)) {s : ℕ} (hs : s ≤ t + 1) :
    Γ.Phi Δ (u + s) ≤ Γ.kappa * Γ.Phi Δ u := by
  have hW := Γ.witness_log hprim hh hΔ0 hΔ hrun
  have hR := Γ.rise_bound u s
  have h2 : (0 : ℝ) < Real.log 2 := Real.log_pos (by norm_num)
  have h3 := Real.log_lt_log (by norm_num : (0 : ℝ) < 2) (by norm_num : (2 : ℝ) < 3)
  have heta := Γ.eta_nonneg
  have hpos3 : 0 ≤ Real.log 3 + Γ.eta := by linarith
  set F := Γ.runSum u t with hF
  set X := Real.log 3 + Γ.eta - Real.log 2 with hX
  have hXpos : 0 < X := by rw [hX]; linarith
  -- the rise is at most `(F + 1) X`
  have hrise : Real.log (Γ.n (u + s)) - Real.log (Γ.n u) ≤ ((F : ℝ) + 1) * X := by
    rcases Nat.lt_or_ge s (t + 1) with hlt | hge
    · have hst : s ≤ t := by omega
      have hRs : Γ.runSum u s ≤ F := Γ.runSum_mono u hst
      have hsR : s ≤ Γ.runSum u s := Γ.le_runSum hapos u s
      have hRsR : (Γ.runSum u s : ℝ) ≤ F := by exact_mod_cast hRs
      have hsRR : (s : ℝ) ≤ Γ.runSum u s := by exact_mod_cast hsR
      calc Real.log (Γ.n (u + s)) - Real.log (Γ.n u)
          ≤ (s : ℝ) * (Real.log 3 + Γ.eta) - (Γ.runSum u s : ℝ) * Real.log 2 := hR
        _ ≤ (Γ.runSum u s : ℝ) * (Real.log 3 + Γ.eta) - (Γ.runSum u s : ℝ) * Real.log 2 := by
          have := mul_le_mul_of_nonneg_right hsRR hpos3
          linarith
        _ = (Γ.runSum u s : ℝ) * X := by rw [hX]; ring
        _ ≤ (F : ℝ) * X := mul_le_mul_of_nonneg_right hRsR hXpos.le
        _ ≤ ((F : ℝ) + 1) * X := by linarith
    · have hst : s = t + 1 := by omega
      subst hst
      have hRs : Γ.runSum u (t + 1) = F + Γ.a (u + t) := Γ.runSum_succ u t
      have ha : 1 ≤ Γ.a (u + t) := hapos _
      have htF : t ≤ F := Γ.le_runSum hapos u t
      have htFR : (t : ℝ) ≤ F := by exact_mod_cast htF
      have haR : (1 : ℝ) ≤ Γ.a (u + t) := by exact_mod_cast ha
      rw [hRs] at hR
      push_cast at hR
      calc Real.log (Γ.n (u + (t + 1))) - Real.log (Γ.n u)
          ≤ ((t : ℝ) + 1) * (Real.log 3 + Γ.eta) - ((F : ℝ) + Γ.a (u + t)) * Real.log 2 := hR
        _ ≤ ((F : ℝ) + 1) * (Real.log 3 + Γ.eta) - ((F : ℝ) + 1) * Real.log 2 := by
          have e1 := mul_le_mul_of_nonneg_right (show (t : ℝ) + 1 ≤ F + 1 by linarith) hpos3
          have e2 := mul_le_mul_of_nonneg_right
            (show (F : ℝ) + 1 ≤ F + Γ.a (u + t) by linarith) h2.le
          linarith
        _ = ((F : ℝ) + 1) * X := by rw [hX]; ring
  -- `(F + 1) X ≤ (κ − 1) Φ_u`
  have hkX : (Γ.kappa - 1) * Real.log 2 = X := by
    rw [hX]
    have := Γ.kappa_mul_log2
    linarith
  have hk0 : 0 ≤ Γ.kappa - 1 := by
    have := Γ.one_le_kappa
    linarith
  have hΦ : ((F : ℝ) + 1) * Real.log 2 ≤ Γ.Phi Δ u := by
    unfold Phi
    linarith
  have hkey : ((F : ℝ) + 1) * X ≤ (Γ.kappa - 1) * Γ.Phi Δ u := by
    calc ((F : ℝ) + 1) * X = ((F : ℝ) + 1) * Real.log 2 * (Γ.kappa - 1) := by
          rw [← hkX]
          ring
      _ ≤ Γ.Phi Δ u * (Γ.kappa - 1) := mul_le_mul_of_nonneg_right hΦ hk0
      _ = (Γ.kappa - 1) * Γ.Phi Δ u := mul_comm _ _
  have hΦs : Γ.Phi Δ (u + s) = Real.log (Γ.n (u + s)) - Real.log (Γ.n u) + Γ.Phi Δ u := by
    unfold Phi
    ring
  rw [hΦs]
  linarith

/-- The chain, by induction on the number of mismatches of `[u, v)`. -/
theorem rise_lemma_aux (hprim : ∀ i j, i < m → j < m → Γ.n i = Γ.n j → i = j)
    (hapos : ∀ i, 1 ≤ Γ.a i) {d : ℕ} (hh : d % m ≠ 0) {Δ : ℝ} (hΔ0 : 0 ≤ Δ) (v : ℕ) :
    ∀ k u, u ≤ v → (∀ p, u ≤ p → p ≤ v → Real.log (Γ.n (p + d)) - Real.log (Γ.n p) ≤ Δ) →
      ((Finset.Ico u v).filter (fun p => ¬ Γ.agree d p)).card = k →
      Γ.Phi Δ v ≤ Γ.kappa ^ (k + 1) * Γ.Phi Δ u := by
  intro k
  induction k with
  | zero =>
    intro u huv hΔ hcard
    have hrun : ∀ j, j < v - u → Γ.agree d (u + j) := by
      intro j hj
      by_contra hna
      have hmem : u + j ∈ (Finset.Ico u v).filter (fun p => ¬ Γ.agree d p) :=
        Finset.mem_filter.mpr ⟨Finset.mem_Ico.mpr ⟨by omega, by omega⟩, hna⟩
      have := Finset.card_pos.mpr ⟨_, hmem⟩
      omega
    have h := Γ.run_step hprim hapos hh hΔ0 (hΔ u le_rfl huv) hrun (s := v - u) (by omega)
    rw [show u + (v - u) = v by omega] at h
    rw [zero_add, pow_one]
    exact h
  | succ k ih =>
    intro u huv hΔ hcard
    set M := (Finset.Ico u v).filter (fun p => ¬ Γ.agree d p) with hM
    have hne : M.Nonempty := by
      rw [← Finset.card_pos, hcard]
      omega
    set e := M.min' hne with he
    have heM : e ∈ M := Finset.min'_mem M hne
    obtain ⟨heIco, hea⟩ := Finset.mem_filter.mp heM
    obtain ⟨hue, hev⟩ := Finset.mem_Ico.mp heIco
    -- `[u, e)` agrees
    have hrun : ∀ j, j < e - u → Γ.agree d (u + j) := by
      intro j hj
      by_contra hna
      have hmem : u + j ∈ M :=
        Finset.mem_filter.mpr ⟨Finset.mem_Ico.mpr ⟨by omega, by omega⟩, hna⟩
      have h' : e ≤ u + j := Finset.min'_le M _ hmem
      omega
    -- the step to `e + 1`
    have hstep := Γ.run_step hprim hapos hh hΔ0 (hΔ u le_rfl huv) hrun (s := e - u + 1) (by omega)
    rw [show u + (e - u + 1) = e + 1 by omega] at hstep
    -- `[e + 1, v)` has `k` mismatches
    have hcard' : ((Finset.Ico (e + 1) v).filter (fun p => ¬ Γ.agree d p)).card = k := by
      have hsplit : M = (Finset.Ico u (e + 1)).filter (fun p => ¬ Γ.agree d p) ∪
          (Finset.Ico (e + 1) v).filter (fun p => ¬ Γ.agree d p) := by
        rw [hM, ← Finset.filter_union, Finset.Ico_union_Ico_eq_Ico (by omega) (by omega)]
      have hsing : (Finset.Ico u (e + 1)).filter (fun p => ¬ Γ.agree d p) = {e} := by
        apply Finset.eq_singleton_iff_unique_mem.mpr
        refine ⟨Finset.mem_filter.mpr ⟨Finset.mem_Ico.mpr ⟨hue, by omega⟩, hea⟩, ?_⟩
        intro p hp
        obtain ⟨hpI, hpa⟩ := Finset.mem_filter.mp hp
        obtain ⟨hup, hpe⟩ := Finset.mem_Ico.mp hpI
        have hpM : p ∈ M :=
          Finset.mem_filter.mpr ⟨Finset.mem_Ico.mpr ⟨hup, by omega⟩, hpa⟩
        have h' : e ≤ p := Finset.min'_le M _ hpM
        omega
      have hdisj : Disjoint ((Finset.Ico u (e + 1)).filter (fun p => ¬ Γ.agree d p))
          ((Finset.Ico (e + 1) v).filter (fun p => ¬ Γ.agree d p)) :=
        Finset.disjoint_filter_filter (Finset.Ico_disjoint_Ico_consecutive u (e + 1) v)
      have h1 := hcard
      rw [hsplit, Finset.card_union_of_disjoint hdisj, hsing, Finset.card_singleton] at h1
      omega
    have hΔ' : ∀ p, e + 1 ≤ p → p ≤ v → Real.log (Γ.n (p + d)) - Real.log (Γ.n p) ≤ Δ :=
      fun p hp1 hp2 => hΔ p (by omega) hp2
    have hih := ih (e + 1) (by omega) hΔ' hcard'
    have hκ : 0 ≤ Γ.kappa := by
      have := Γ.one_le_kappa
      linarith
    calc Γ.Phi Δ v ≤ Γ.kappa ^ (k + 1) * Γ.Phi Δ (e + 1) := hih
      _ ≤ Γ.kappa ^ (k + 1) * (Γ.kappa * Γ.Phi Δ u) :=
        mul_le_mul_of_nonneg_left hstep (pow_nonneg hκ _)
      _ = Γ.kappa ^ (k + 1 + 1) * Γ.Phi Δ u := by ring

/-- **S13's rise lemma** (natural logs, uniform `Δ`): for a primitive cycle with letters `≥ 1`, a
forward offset `d ≢ 0 (mod m)`, a stretch `u ≤ v` on which `log n_(p+d) − log n_p ≤ Δ`, and `k`
the number of mismatches in `[u, v)`: `Φ_v ≤ κ^(k+1) Φ_u`. -/
theorem rise_lemma (hprim : ∀ i j, i < m → j < m → Γ.n i = Γ.n j → i = j)
    (hapos : ∀ i, 1 ≤ Γ.a i) {d : ℕ} (hh : d % m ≠ 0) {Δ : ℝ} (hΔ0 : 0 ≤ Δ) {u v : ℕ}
    (huv : u ≤ v) (hΔ : ∀ p, u ≤ p → p ≤ v → Real.log (Γ.n (p + d)) - Real.log (Γ.n p) ≤ Δ) :
    Γ.Phi Δ v ≤
      Γ.kappa ^ (((Finset.Ico u v).filter (fun p => ¬ Γ.agree d p)).card + 1) * Γ.Phi Δ u :=
  Γ.rise_lemma_aux hprim hapos hh hΔ0 v _ u huv hΔ rfl

/-- **S13's Corollary 1, natural-log form.** From the minimum `n₀` to any position `j ≤ m`:
`Φ_j ≤ κ^(s+1) Φ_0` with `s = |mis d|`, for any uniform `Δ ≥ 0`. -/
theorem rise_from_min (hprim : ∀ i j, i < m → j < m → Γ.n i = Γ.n j → i = j)
    (hapos : ∀ i, 1 ≤ Γ.a i) {d : ℕ} (hh : d % m ≠ 0) {Δ : ℝ} (hΔ0 : 0 ≤ Δ)
    (hΔ : ∀ p, Real.log (Γ.n (p + d)) - Real.log (Γ.n p) ≤ Δ) {j : ℕ} (hj : j ≤ m) :
    Γ.Phi Δ j ≤ Γ.kappa ^ ((Γ.mis d).card + 1) * Γ.Phi Δ 0 := by
  have h := Γ.rise_lemma hprim hapos hh hΔ0 (u := 0) (v := j) (Nat.zero_le _)
    (fun p _ _ => hΔ p)
  have hsub : (Finset.Ico 0 j).filter (fun p => ¬ Γ.agree d p) ⊆ Γ.mis d := by
    unfold mis
    apply Finset.filter_subset_filter
    intro p hp
    rw [Finset.mem_Ico] at hp
    exact Finset.mem_range.mpr (by omega)
  have hcard := Finset.card_le_card hsub
  calc Γ.Phi Δ j
      ≤ Γ.kappa ^ (((Finset.Ico 0 j).filter (fun p => ¬ Γ.agree d p)).card + 1) * Γ.Phi Δ 0 := h
    _ ≤ Γ.kappa ^ ((Γ.mis d).card + 1) * Γ.Phi Δ 0 :=
      mul_le_mul_of_nonneg_right (pow_le_pow_right₀ Γ.one_le_kappa (by omega))
        (Γ.Phi_nonneg hΔ0 0)

/-- Corollary 1 with the uniform `Δ = d (log 3 + η − log 2)` (S13's `Δ⁺ ≤ (σ + η) d`):
`log n_j + log 2 + d(log 3 + η − log 2) ≤ κ^(s+1) (log n₀ + log 2 + d(log 3 + η − log 2))`. -/
theorem rise_from_min_uniform (hprim : ∀ i j, i < m → j < m → Γ.n i = Γ.n j → i = j)
    (hapos : ∀ i, 1 ≤ Γ.a i) {d : ℕ} (hh : d % m ≠ 0) {j : ℕ} (hj : j ≤ m) :
    Real.log (Γ.n j) + Real.log 2 + (d : ℝ) * (Real.log 3 + Γ.eta - Real.log 2) ≤
      Γ.kappa ^ ((Γ.mis d).card + 1) *
        (Real.log (Γ.n 0) + Real.log 2 + (d : ℝ) * (Real.log 3 + Γ.eta - Real.log 2)) := by
  have hX : 0 ≤ (d : ℝ) * (Real.log 3 + Γ.eta - Real.log 2) := by
    have := Γ.eta_nonneg
    have := Real.log_lt_log (by norm_num : (0 : ℝ) < 2) (by norm_num : (2 : ℝ) < 3)
    have hd : (0 : ℝ) ≤ d := by positivity
    nlinarith
  exact Γ.rise_from_min hprim hapos hh hX (fun p => Γ.rise_le_mul hapos p d) hj

end OddCycle

/-! ### S13-c: subadditivity of the mismatch count, the orientation lemma, and the mean-zero partner bound

Side lane's S13 §1, Corollaries 5–6 (`55cf217`, `1d87059`), and the orientation remark. (i) The
shift `i ↦ (i + h) mod m` carries `mis h` into `mis k` whenever `h + k ≡ 0 (mod m)`, injectively on
`[0, m)`, so `|mis h| ≤ |mis k|` (`mis_card_le_of_add_mod`) and `|mis (m − h)| = |mis h|`
(`mis_card_neg`): both orientations of a rotation have the same mismatch count. (ii) If
`a_i = a_(i+h₁)` and `a_(i+h₁) = a_(i+h₁+h₂)` then `a_i = a_(i+h₁+h₂)`; so the shift by `h₁` carries
`mis (h₁ + h₂) \ mis h₁` into `mis h₂`, and `|mis (h₁ + h₂)| ≤ |mis h₁| + |mis h₂|` (`mis_card_add`),
with the difference form `|mis (h₁ + (m − h₂))| ≤ |mis h₁| + |mis h₂|` (`mis_card_sub`): Corollary
5's subadditivity. (iii) The partner offset `μ_h(t) = log n_(t+h) − log n_t` has mean zero over a
period (`sum_mu_eq_zero`), so some `μ_h(t₁) ≤ 0` (`exists_mu_nonpos`); the two arcs from `x` to `y`
and from `y` around to `x + m` each have variation at least `|μ_h(y) − μ_h(x)|` and together exhaust
the period (`two_abs_sub_le_varMu`), whence `μ_h(t₀) ≤ Var(μ_h)/2` for every `t₀`
(`mu_le_half_varMu`): Corollary 6's `Δ⁺ ≤ max μ ≤ Var/2`. (iv) With `Δ = Var(μ_d)/2` the rise lemma
from the minimum gives `log n_j − log n₀ ≤ (κ^(s+1) − 1)(log n₀ + log 2 + Var(μ_d)/2)`
(`forced_variation`), and S12-d's `Var(μ_d) ≤ V_d log 2 + 2δ` turns it into
`log n_j − log n₀ ≤ (κ^(s+1) − 1)(log n₀ + log 2 + (V_d log 2 + 2δ)/2)` (`forced_letter_variation`),
Corollary 6's inequality in natural logs. The step "some letter is at least `V_d/s`" is left for
S13-d. -/

namespace OddCycle

variable {m : ℕ} (Γ : OddCycle m)

/-- The shift by `h` carries `mis h` into `mis k` when `h + k ≡ 0 (mod m)`: `|mis h| ≤ |mis k|`. -/
theorem mis_card_le_of_add_mod {h k : ℕ} (hk : (h + k) % m = 0) :
    (Γ.mis h).card ≤ (Γ.mis k).card := by
  have hm := Γ.hm
  apply Finset.card_le_card_of_injOn (fun i => (i + h) % m)
  · intro i hi
    obtain ⟨hi1, hi2⟩ := Finset.mem_filter.mp hi
    refine Finset.mem_filter.mpr ⟨Finset.mem_range.mpr (Nat.mod_lt _ hm), ?_⟩
    intro hag
    apply hi2
    have e1 : Γ.a ((i + h) % m) = Γ.a (i + h) := Γ.a_mod _
    have e2 : Γ.a ((i + h) % m + k) = Γ.a i := by
      rw [← Γ.a_mod ((i + h) % m + k), Nat.mod_add_mod, Nat.add_assoc, Nat.add_mod, hk,
        Nat.add_zero, Nat.mod_mod, Γ.a_mod]
    have hag' : Γ.a ((i + h) % m) = Γ.a ((i + h) % m + k) := hag
    rw [e1, e2] at hag'
    exact hag'.symm
  · intro i hi j hj hij
    have hi' : i < m := Finset.mem_range.mp (Finset.mem_filter.mp (Finset.mem_coe.mp hi)).1
    have hj' : j < m := Finset.mem_range.mp (Finset.mem_filter.mp (Finset.mem_coe.mp hj)).1
    have h1 : i ≡ j [MOD m] := Nat.ModEq.add_right_cancel' h hij
    rw [Nat.ModEq, Nat.mod_eq_of_lt hi', Nat.mod_eq_of_lt hj'] at h1
    exact h1

/-- **The orientation lemma**: `|mis (m − h)| = |mis h|` for `h ≤ m`. -/
theorem mis_card_neg {h : ℕ} (hh : h ≤ m) : (Γ.mis (m - h)).card = (Γ.mis h).card := by
  apply le_antisymm
  · exact Γ.mis_card_le_of_add_mod (by rw [Nat.sub_add_cancel hh, Nat.mod_self])
  · exact Γ.mis_card_le_of_add_mod (by rw [Nat.add_sub_cancel' hh, Nat.mod_self])

/-- **Subadditivity of the mismatch count**: `|mis (h₁ + h₂)| ≤ |mis h₁| + |mis h₂|`. -/
theorem mis_card_add (h₁ h₂ : ℕ) :
    (Γ.mis (h₁ + h₂)).card ≤ (Γ.mis h₁).card + (Γ.mis h₂).card := by
  have hm := Γ.hm
  have hsdiff : ((Γ.mis (h₁ + h₂)) \ (Γ.mis h₁)).card ≤ (Γ.mis h₂).card := by
    apply Finset.card_le_card_of_injOn (fun i => (i + h₁) % m)
    · intro i hi
      obtain ⟨hi1, hi2⟩ := Finset.mem_sdiff.mp hi
      obtain ⟨hr, hna⟩ := Finset.mem_filter.mp hi1
      have hag1 : Γ.a i = Γ.a (i + h₁) := by
        by_contra hno
        exact hi2 (Finset.mem_filter.mpr ⟨hr, hno⟩)
      refine Finset.mem_filter.mpr ⟨Finset.mem_range.mpr (Nat.mod_lt _ hm), ?_⟩
      intro hag2
      apply hna
      have e1 : Γ.a ((i + h₁) % m) = Γ.a (i + h₁) := Γ.a_mod _
      have e2 : Γ.a ((i + h₁) % m + h₂) = Γ.a (i + (h₁ + h₂)) := by
        rw [← Γ.a_mod ((i + h₁) % m + h₂), Nat.mod_add_mod, Nat.add_assoc, Γ.a_mod]
      have hag2' : Γ.a ((i + h₁) % m) = Γ.a ((i + h₁) % m + h₂) := hag2
      rw [e1, e2] at hag2'
      exact hag1.trans hag2'
    · intro i hi j hj hij
      have hi' : i < m :=
        Finset.mem_range.mp (Finset.mem_filter.mp (Finset.mem_sdiff.mp (Finset.mem_coe.mp hi)).1).1
      have hj' : j < m :=
        Finset.mem_range.mp (Finset.mem_filter.mp (Finset.mem_sdiff.mp (Finset.mem_coe.mp hj)).1).1
      have h1 : i ≡ j [MOD m] := Nat.ModEq.add_right_cancel' h₁ hij
      rw [Nat.ModEq, Nat.mod_eq_of_lt hi', Nat.mod_eq_of_lt hj'] at h1
      exact h1
  calc (Γ.mis (h₁ + h₂)).card
      ≤ ((Γ.mis (h₁ + h₂)) \ (Γ.mis h₁)).card + (Γ.mis h₁).card :=
        Finset.card_le_card_sdiff_add_card
    _ ≤ (Γ.mis h₂).card + (Γ.mis h₁).card := by omega
    _ = (Γ.mis h₁).card + (Γ.mis h₂).card := Nat.add_comm _ _

/-- Corollary 5's difference form: `|mis (h₁ − h₂)| ≤ |mis h₁| + |mis h₂|`, the difference taken as
`h₁ + (m − h₂)`. -/
theorem mis_card_sub (h₁ : ℕ) {h₂ : ℕ} (hh₂ : h₂ ≤ m) :
    (Γ.mis (h₁ + (m - h₂))).card ≤ (Γ.mis h₁).card + (Γ.mis h₂).card := by
  have := Γ.mis_card_add h₁ (m - h₂)
  rw [Γ.mis_card_neg hh₂] at this
  exact this

/-- The partner offset `μ_h(t) = log n_(t+h) − log n_t` has mean zero over a period. -/
theorem sum_mu_eq_zero (h : ℕ) :
    ∑ t ∈ Finset.range m, (Real.log (Γ.n (t + h)) - Real.log (Γ.n t)) = 0 := by
  rw [Finset.sum_sub_distrib]
  have hper : ∀ t, Real.log (Γ.n (t + m)) = Real.log (Γ.n t) := fun t => by rw [Γ.nper]
  have hshift : ∑ t ∈ Finset.range m, Real.log (Γ.n (h + t)) = ∑ t ∈ Finset.range m, Real.log (Γ.n t) :=
    DK.sum_range_shift (fun t => Real.log (Γ.n t)) hper h
  have e : ∑ t ∈ Finset.range m, Real.log (Γ.n (t + h))
      = ∑ t ∈ Finset.range m, Real.log (Γ.n (h + t)) := by
    apply Finset.sum_congr rfl
    intro t _
    rw [Nat.add_comm t h]
  rw [e, hshift, sub_self]

/-- Some partner offset is `≤ 0`. -/
theorem exists_mu_nonpos (h : ℕ) :
    ∃ t, t < m ∧ Real.log (Γ.n (t + h)) - Real.log (Γ.n t) ≤ 0 := by
  by_contra hno
  have hpos : ∀ t ∈ Finset.range m, 0 < Real.log (Γ.n (t + h)) - Real.log (Γ.n t) := by
    intro t ht
    by_contra hle
    exact hno ⟨t, Finset.mem_range.mp ht, not_lt.mp hle⟩
  have := Finset.sum_pos hpos ⟨0, Finset.mem_range.mpr Γ.hm⟩
  rw [Γ.sum_mu_eq_zero] at this
  exact lt_irrefl _ this

/-- The two arcs from `x` to `y` and from `y` around to `x + m` each have variation at least
`|μ_h(y) − μ_h(x)|`, and together they exhaust a period: `2|μ_h(y) − μ_h(x)| ≤ Var(μ_h)`. -/
theorem two_abs_sub_le_varMu (h : ℕ) {x y : ℕ} (hxy : x ≤ y) (hyx : y ≤ x + m) :
    2 * |(Real.log (Γ.n (y + h)) - Real.log (Γ.n y)) -
        (Real.log (Γ.n (x + h)) - Real.log (Γ.n x))| ≤ Γ.varMu h := by
  set μ : ℕ → ℝ := fun t => Real.log (Γ.n (t + h)) - Real.log (Γ.n t) with hμ
  have hμper : ∀ t, μ (t + m) = μ t := by
    intro t
    show Real.log (Γ.n (t + m + h)) - Real.log (Γ.n (t + m))
      = Real.log (Γ.n (t + h)) - Real.log (Γ.n t)
    rw [show t + m + h = t + h + m by omega, Γ.nper, Γ.nper]
  have hJper : ∀ t, |μ (t + m + 1) - μ (t + m)| = |μ (t + 1) - μ t| := by
    intro t
    rw [show t + m + 1 = t + 1 + m by omega, hμper, hμper]
  have h1 : |μ y - μ x| ≤ ∑ s ∈ Finset.Ico x y, |μ (s + 1) - μ s| :=
    DK.abs_sub_le_sum_jumps μ hxy
  have h2 : |μ (x + m) - μ y| ≤ ∑ s ∈ Finset.Ico y (x + m), |μ (s + 1) - μ s| :=
    DK.abs_sub_le_sum_jumps μ hyx
  rw [hμper, abs_sub_comm] at h2
  have hsum : ∑ s ∈ Finset.Ico x y, |μ (s + 1) - μ s|
      + ∑ s ∈ Finset.Ico y (x + m), |μ (s + 1) - μ s| = Γ.varMu h := by
    have hshift : ∑ t ∈ Finset.range m, |μ (x + t + 1) - μ (x + t)|
        = ∑ t ∈ Finset.range m, |μ (t + 1) - μ t| :=
      DK.sum_range_shift (fun s => |μ (s + 1) - μ s|) hJper x
    rw [Finset.sum_Ico_consecutive _ hxy hyx, Finset.sum_Ico_eq_sum_range,
      Nat.add_sub_cancel_left]
    calc ∑ k ∈ Finset.range m, |μ (x + k + 1) - μ (x + k)|
        = ∑ t ∈ Finset.range m, |μ (t + 1) - μ t| := hshift
      _ = Γ.varMu h := rfl
  calc 2 * |μ y - μ x| = |μ y - μ x| + |μ y - μ x| := two_mul _
    _ ≤ ∑ s ∈ Finset.Ico x y, |μ (s + 1) - μ s|
        + ∑ s ∈ Finset.Ico y (x + m), |μ (s + 1) - μ s| := add_le_add h1 h2
    _ = Γ.varMu h := hsum

/-- **Corollary 6's partner bound**: `μ_h(t₀) ≤ Var(μ_h)/2` for every position `t₀`. -/
theorem mu_le_half_varMu (h t₀ : ℕ) :
    Real.log (Γ.n (t₀ + h)) - Real.log (Γ.n t₀) ≤ Γ.varMu h / 2 := by
  have hm := Γ.hm
  obtain ⟨t₁, ht₁, hneg⟩ := Γ.exists_mu_nonpos h
  have hred : Real.log (Γ.n (t₀ + h)) - Real.log (Γ.n t₀)
      = Real.log (Γ.n (t₀ % m + h)) - Real.log (Γ.n (t₀ % m)) := by
    rw [Γ.n_mod t₀, ← Γ.n_mod (t₀ % m + h), Nat.mod_add_mod, Γ.n_mod]
  rw [hred]
  set t := t₀ % m with ht
  have htm : t < m := Nat.mod_lt _ hm
  have key : 2 * |(Real.log (Γ.n (t + h)) - Real.log (Γ.n t)) -
      (Real.log (Γ.n (t₁ + h)) - Real.log (Γ.n t₁))| ≤ Γ.varMu h := by
    rcases le_or_gt t₁ t with hle | hlt
    · exact Γ.two_abs_sub_le_varMu h hle (by omega)
    · have := Γ.two_abs_sub_le_varMu h hlt.le (by omega : t₁ ≤ t + m)
      rw [abs_sub_comm] at this
      exact this
  have habs := le_abs_self ((Real.log (Γ.n (t + h)) - Real.log (Γ.n t)) -
    (Real.log (Γ.n (t₁ + h)) - Real.log (Γ.n t₁)))
  linarith

/-- **Corollary 6's inequality, natural logs.** From the minimum, for `j ≤ m` and `s = |mis d|`:
`log n_j − log n₀ ≤ (κ^(s+1) − 1)(log n₀ + log 2 + Var(μ_d)/2)`. -/
theorem forced_variation (hprim : ∀ i j, i < m → j < m → Γ.n i = Γ.n j → i = j)
    (hapos : ∀ i, 1 ≤ Γ.a i) {d : ℕ} (hh : d % m ≠ 0) {j : ℕ} (hj : j ≤ m) :
    Real.log (Γ.n j) - Real.log (Γ.n 0) ≤
      (Γ.kappa ^ ((Γ.mis d).card + 1) - 1) *
        (Real.log (Γ.n 0) + Real.log 2 + Γ.varMu d / 2) := by
  have hΔ0 : 0 ≤ Γ.varMu d / 2 := by
    have := Γ.varMu_nonneg d
    linarith
  have h := Γ.rise_from_min hprim hapos hh hΔ0 (fun p => Γ.mu_le_half_varMu d p) hj
  unfold Phi at h
  linarith

/-- With S12-d's `Var(μ_d) ≤ V_d log 2 + 2δ`: the forced-variation law in terms of the letter
variation `V_d`, `δ = A log 2 − m log 3`. -/
theorem forced_letter_variation (hprim : ∀ i j, i < m → j < m → Γ.n i = Γ.n j → i = j)
    (hapos : ∀ i, 1 ≤ Γ.a i) {d : ℕ} (hh : d % m ≠ 0) {j : ℕ} (hj : j ≤ m) :
    Real.log (Γ.n j) - Real.log (Γ.n 0) ≤
      (Γ.kappa ^ ((Γ.mis d).card + 1) - 1) *
        (Real.log (Γ.n 0) + Real.log 2 +
          ((Γ.Vh d : ℝ) * Real.log 2 + 2 * ((Γ.Apre m : ℝ) * Real.log 2 - m * Real.log 3)) / 2) := by
  have h := Γ.forced_variation hprim hapos hh hj
  have hV := Γ.varMu_le_Vh d
  have h1 : (1 : ℝ) ≤ Γ.kappa ^ ((Γ.mis d).card + 1) := one_le_pow₀ Γ.one_le_kappa
  have hk : 0 ≤ Γ.kappa ^ ((Γ.mis d).card + 1) - 1 := by linarith
  calc Real.log (Γ.n j) - Real.log (Γ.n 0)
      ≤ (Γ.kappa ^ ((Γ.mis d).card + 1) - 1) *
          (Real.log (Γ.n 0) + Real.log 2 + Γ.varMu d / 2) := h
    _ ≤ (Γ.kappa ^ ((Γ.mis d).card + 1) - 1) *
          (Real.log (Γ.n 0) + Real.log 2 +
            ((Γ.Vh d : ℝ) * Real.log 2 + 2 * ((Γ.Apre m : ℝ) * Real.log 2 - m * Real.log 3)) / 2) :=
        mul_le_mul_of_nonneg_left (by linarith) hk

end OddCycle

/-! ### C010: sharp odd-spacing bounds on the complete dyadic circle

C010 (`ODD_ROUNDING.md` §§2–3) bounds each complete sorted gap `Δ_r` from below by a sharp
constant `b_q(a, b)` depending on the adjacent sorted heights `a = H_r`, `b = H_{r+1}`: `2/2^a`
for `b = a`, `1/2^a` for `b < a` (the seam included, with `b = −1`), and
`[q(2^k − 1) + η]/(3 · 2^b)` for `b = a + k > a`, where strict image order gives `3r > q(2^k − 1)`
for the odd numerator `r` and the residue of `q(2^k − 1)` modulo `6` supplies `η ∈ {6, 2, 4}`.
Summing over the circle, `L ≥ R_q(H) = Σ b_q(H_r, H_{r+1})`. Here everything is scaled by `2^B`
(`G_r = 2^B Δ_r`) and the upward bound is multiplied by `3` to stay in `ℤ`. -/

/-- C010's residue increment `η(q, k)`: `6` for even `k`; for odd `k`, `2` if `q ≡ 1 (mod 6)` and
`4` otherwise (`q ≡ 5 (mod 6)` in the intended domain `gcd(q, 6) = 1`). -/
def eta (q : ℤ) (k : ℕ) : ℤ := if Even k then 6 else if q % 6 = 1 then 2 else 4

/-- C010 §2's increment: for odd `r, q` and `k ≥ 1`, `q (2^k − 1) < 3 r` forces
`q (2^k − 1) + η(q, k) ≤ 3 r`, because `3 r ≡ 3 (mod 6)` while `q (2^k − 1) ≡ 3` (`k` even) or
`≡ q` (`k` odd) modulo `6`. The prose assumes `3 ∤ q`; it is not needed, since for `q ≡ 3 (mod 6)`
the true increment is `6 ≥ 4`. -/
theorem eta_refine {q r : ℤ} (k : ℕ) (hk : 1 ≤ k) (hq : Odd q) (hr : Odd r)
    (h : q * (2 ^ k - 1) < 3 * r) : q * (2 ^ k - 1) + eta q k ≤ 3 * r := by
  have hx2 : (2 : ℤ) ∣ 2 ^ k := dvd_pow_self 2 (by omega)
  have hxodd : Odd ((2 : ℤ) ^ k - 1) := by
    obtain ⟨c, hc⟩ := hx2
    exact ⟨c - 1, by omega⟩
  have hyodd : Odd (q * (2 ^ k - 1)) := Int.odd_mul.mpr ⟨hq, hxodd⟩
  have hmod : (2 : ℤ) ^ k ≡ (-1) ^ k [ZMOD 3] := (show (2 : ℤ) ≡ -1 [ZMOD 3] by decide).pow k
  obtain ⟨s, hs⟩ := hyodd
  obtain ⟨u, hu⟩ := hr
  obtain ⟨v, hv⟩ := hq
  unfold eta
  rcases Nat.even_or_odd k with hke | hko
  · rw [hke.neg_one_pow] at hmod
    have h3y : (3 : ℤ) ∣ q * (2 ^ k - 1) := Dvd.dvd.mul_left hmod.symm.dvd q
    rw [ite_eq_left hke]
    omega
  · rw [hko.neg_one_pow] at hmod
    have h3' : (3 : ℤ) ∣ 2 ^ k + 1 := by
      have := hmod.symm.dvd
      rwa [sub_neg_eq_add] at this
    have h3y : (3 : ℤ) ∣ q * (2 ^ k - 1) - q := by
      have hrew : q * (2 ^ k - 1) - q = q * (2 ^ k + 1) - 3 * q := by ring
      rw [hrew]
      exact dvd_sub (Dvd.dvd.mul_left h3' q) (dvd_mul_right 3 q)
    rw [ite_eq_right (Nat.not_even_iff_odd.mpr hko)]
    split_ifs with h6 <;> omega

/-- An ordered primitive odd cycle with `m ≥ 2`, together with its exponent window: C006's
domain (order of the normalised successor is the hypothesis `hord`). -/
structure OrdCycle (m : ℕ) where
  Γ : OddCycle m
  hord : ∀ i j, Γ.Z i < Γ.Z j ↔ Γ.F i < Γ.F j
  q' : ℕ
  hq1 : (2 : ℤ) ^ q' * Γ.lo ≤ Γ.F 0
  hq2 : Γ.F 0 < 2 ^ (q' + 1) * Γ.lo
  hm2 : 2 ≤ m
  hprim : ∀ i j, i < m → j < m → Γ.n i = Γ.n j → i = j

namespace OrdCycle

variable {m : ℕ} (Ω : OrdCycle m)

/-- The underlying ordered `NarrowCycle` on the scaled normalised states. -/
noncomputable def N : NarrowCycle m := Ω.Γ.toNarrow Ω.hord Ω.q' Ω.hq1 Ω.hq2

theorem N_prim : Ω.N.Primitive := Ω.Γ.toNarrow_primitive Ω.hord Ω.q' Ω.hq1 Ω.hq2 Ω.hprim

theorem N_rank_zero : Ω.N.rank 0 = 0 := Ω.Γ.toNarrow_rank_zero Ω.hord Ω.q' Ω.hq1 Ω.hq2

theorem N_x (i : ℕ) : Ω.N.x i = Ω.Γ.Z i := rfl

theorem N_q : Ω.N.q = Ω.q' := rfl

theorem numHigh_lt : Ω.N.numHigh < m := Ω.N.numHigh_lt Ω.N_prim Ω.hm2

theorem numHigh_pos : 0 < Ω.N.numHigh := Ω.N.numHigh_pos Ω.N_prim Ω.hm2

/-- The low exponent is at least `1` (the least image exceeds `3 lo > 2 lo`). -/
theorem q'_pos : 1 ≤ Ω.q' := by
  rcases Nat.eq_zero_or_pos Ω.q' with h | h
  · exfalso
    have h2 := Ω.hq2
    rw [h, Nat.zero_add, pow_one] at h2
    have hF := Ω.Γ.F_zero
    have hlo : 0 < Ω.Γ.lo := by
      unfold OddCycle.lo
      exact mul_pos (by positivity) Ω.Γ.npos
    have hd : (0 : ℤ) < 2 ^ Ω.Γ.B * Ω.Γ.q := mul_pos (by positivity) Ω.Γ.hq
    linarith
  · exact h

/-- The height of the state of rank `r`. -/
noncomputable def hr (r : ℕ) : ℕ := Ω.Γ.h (Ω.N.idx r)

/-- The scaled offset `2^{B−h'_r} q` of the state of rank `r`, and its seam extension. -/
noncomputable def off (r : ℕ) : ℤ := 2 ^ (Ω.Γ.B - Ω.hr r) * Ω.Γ.q

noncomputable def offext (r : ℕ) : ℤ := if r < m then Ω.off r else 2 * Ω.off (r - m)

/-- C006's `T_r = 2^B(ε_[r+1] − ε_[r])`, with the seam `ε_[m] = 2ε_[0]`. -/
noncomputable def T (r : ℕ) : ℤ := Ω.offext (r + 1) - Ω.offext r

theorem Fr_eq (r : ℕ) : Ω.N.Fr r = 3 * Ω.N.y r + Ω.off r := rfl

/-- The image difference between consecutive sorted ranks is `3Δ_r + T_r`. -/
theorem Fext_sub {r : ℕ} (hr : r < m) :
    Ω.N.Fext (r + 1) - Ω.N.Fext r = 3 * Ω.N.gap r + Ω.T r := by
  unfold NarrowCycle.gap T
  rcases Nat.lt_or_ge (r + 1) m with h1 | h1
  · rw [Ω.N.Fext_of_lt h1, Ω.N.Fext_of_lt hr, Ω.N.yext_of_lt h1, Ω.N.yext_of_lt hr]
    unfold offext
    rw [ite_eq_left h1, ite_eq_left hr, Ω.Fr_eq, Ω.Fr_eq]
    ring
  · have hm : r + 1 = m := le_antisymm hr h1
    rw [hm, Ω.N.Fext_m, Ω.N.Fext_of_lt hr, Ω.N.yext_m, Ω.N.yext_of_lt hr]
    unfold offext
    rw [ite_eq_right (lt_irrefl m), Nat.sub_self, ite_eq_left hr, Ω.Fr_eq, Ω.Fr_eq]
    ring

/-- **C006's (G3)** in its stated form: `2^{e_r} Δ_{(r+h) mod m} = 3Δ_r + T_r`. -/
theorem gap_rec {r : ℕ} (hr : r < m) :
    (2 : ℤ) ^ Ω.N.e r * Ω.N.gap ((r + Ω.N.numHigh) % m) = 3 * Ω.N.gap r + Ω.T r := by
  rw [Ω.N.gap_recurrence Ω.N_prim Ω.hm2 hr, Ω.Fext_sub hr]

theorem hr_le_B (r : ℕ) : Ω.hr r ≤ Ω.Γ.B := Ω.Γ.hB _

/-- `T_r = 0` exactly when the adjacent sorted heights agree (`r + 1 < m`). -/
theorem T_eq_zero_iff {r : ℕ} (hr1 : r + 1 < m) : Ω.T r = 0 ↔ Ω.hr (r + 1) = Ω.hr r := by
  unfold T offext off
  rw [ite_eq_left hr1, ite_eq_left (by omega : r < m)]
  constructor
  · intro h
    have hq := Ω.Γ.hq
    have h' : ((2 : ℤ) ^ (Ω.Γ.B - Ω.hr (r + 1)) - 2 ^ (Ω.Γ.B - Ω.hr r)) * Ω.Γ.q = 0 := by
      linarith
    rcases mul_eq_zero.mp h' with h'' | h''
    · have h3 : (2 : ℤ) ^ (Ω.Γ.B - Ω.hr (r + 1)) = 2 ^ (Ω.Γ.B - Ω.hr r) := by linarith
      have h4 : (2 ^ (Ω.Γ.B - Ω.hr (r + 1)) : ℕ) = 2 ^ (Ω.Γ.B - Ω.hr r) := by exact_mod_cast h3
      have h5 := Nat.pow_right_injective (le_refl 2) h4
      have := Ω.hr_le_B r
      have := Ω.hr_le_B (r + 1)
      omega
    · exact absurd h'' hq.ne'
  · intro h
    rw [h]
    ring

theorem hr_zero : Ω.hr 0 = 0 := by
  unfold hr
  rw [Ω.N.idx_zero Ω.N_prim Ω.N_rank_zero]
  exact Ω.Γ.h_zero

/-- The seam term is always positive: `T_{m−1} = 2^{B+1} q − 2^{B−h'_{m−1}} q > 0`, so the seam
is a forced position (`J ≥ 1`). -/
theorem T_seam_pos : 0 < Ω.T (m - 1) := by
  have hm := Ω.Γ.hm
  unfold T offext
  rw [show m - 1 + 1 = m by omega, ite_eq_right (lt_irrefl m), Nat.sub_self,
    ite_eq_left (by omega : m - 1 < m)]
  unfold off
  rw [Ω.hr_zero, Nat.sub_zero]
  have h1 : (2 : ℤ) ^ (Ω.Γ.B - Ω.hr (m - 1)) ≤ 2 ^ Ω.Γ.B :=
    pow_le_pow_right₀ (by norm_num) (Nat.sub_le _ _)
  have hq := Ω.Γ.hq
  have h2 : (0 : ℤ) < 2 ^ Ω.Γ.B := by positivity
  nlinarith [mul_le_mul_of_nonneg_right h1 hq.le, mul_pos h2 hq]

/-- The rank reached after `k` successor steps from rank `r₀`: `(r₀ + k h) mod m`. -/
noncomputable def orb (r₀ k : ℕ) : ℕ := (r₀ + k * Ω.N.numHigh) % m

theorem orb_lt (r₀ k : ℕ) : Ω.orb r₀ k < m := Nat.mod_lt _ Ω.Γ.hm

theorem orb_zero {r₀ : ℕ} (hr₀ : r₀ < m) : Ω.orb r₀ 0 = r₀ := by
  unfold orb
  rw [Nat.zero_mul, Nat.add_zero]
  exact Nat.mod_eq_of_lt hr₀

theorem orb_succ (r₀ k : ℕ) : Ω.orb r₀ (k + 1) = (Ω.orb r₀ k + Ω.N.numHigh) % m := by
  unfold orb
  rw [Nat.mod_add_mod, Nat.add_mul, Nat.one_mul, Nat.add_assoc]

/-- **C006's per-run bound.** Along a zero-forcing run of length `t` starting at rank `r₀`
(`T = 0` at the first `t` ranks of its successor orbit), `2^t ≤ Δ_{r₀} < 2^B L`; hence
`L > 2^{t−B}`. -/
theorem run_bound {r₀ t : ℕ} (hr₀ : r₀ < m) (hrun : ∀ k, k < t → Ω.T (Ω.orb r₀ k) = 0) :
    (2 : ℤ) ^ t ≤ Ω.N.gap r₀ ∧ Ω.N.gap r₀ < 2 ^ Ω.Γ.B * Ω.Γ.n 0 := by
  have hG : ∀ k, k < t →
      (2 : ℤ) ^ Ω.N.e (Ω.orb r₀ k) * Ω.N.gap (Ω.orb r₀ (k + 1)) = 3 * Ω.N.gap (Ω.orb r₀ k) := by
    intro k hk
    rw [Ω.orb_succ, Ω.gap_rec (Ω.orb_lt r₀ k), hrun k hk, add_zero]
  have hpos : 0 < Ω.N.gap r₀ := Ω.N.gap_pos Ω.N_prim Ω.N_rank_zero hr₀
  have hq : 1 ≤ Ω.N.q := Ω.q'_pos
  have he : ∀ k, k < t → 1 ≤ Ω.N.e (Ω.orb r₀ k) := by
    intro k _
    unfold NarrowCycle.e
    split_ifs <;> omega
  have h1 := run_lower (fun k => Ω.N.gap (Ω.orb r₀ k)) (fun k => Ω.N.e (Ω.orb r₀ k)) t
    (by show 0 < Ω.N.gap (Ω.orb r₀ 0); rw [Ω.orb_zero hr₀]; exact hpos) he hG
  have h1' : (2 : ℤ) ^ t ≤ Ω.N.gap r₀ := by
    have := h1
    rw [Ω.orb_zero hr₀] at this
    exact this
  refine ⟨h1', ?_⟩
  have h2 := Ω.N.gap_lt Ω.N_prim Ω.N_rank_zero Ω.hm2 hr₀
  rw [Ω.N_x, Ω.Γ.Z_zero] at h2
  unfold OddCycle.lo at h2
  exact h2

/-- `L > 2^{t−B}` in cleared form: `2^t < 2^B L` for every zero-forcing run of length `t`. -/
theorem run_bound_L {r₀ t : ℕ} (hr₀ : r₀ < m) (hrun : ∀ k, k < t → Ω.T (Ω.orb r₀ k) = 0) :
    (2 : ℤ) ^ t < 2 ^ Ω.Γ.B * Ω.Γ.n 0 := by
  obtain ⟨h1, h2⟩ := Ω.run_bound hr₀ hrun
  exact lt_of_le_of_lt h1 h2

/-! #### The forced positions along the orbit, `J`, and (G1)'s first inequality -/

theorem orb_zero_eq_rank (k : ℕ) : Ω.orb 0 k = Ω.N.rank k := by
  unfold orb
  rw [Ω.N.rank_formula Ω.numHigh_lt k, Ω.N_rank_zero]

theorem orb_orb (a j : ℕ) : Ω.orb (Ω.orb 0 a) j = Ω.orb 0 (a + j) := by
  unfold orb
  rw [Nat.zero_add, Nat.zero_add, Nat.mod_add_mod, Nat.add_mul]

theorem orb_mod (k : ℕ) : Ω.orb 0 (k % m) = Ω.orb 0 k := by
  unfold orb
  rw [Nat.zero_add, Nat.zero_add, Nat.mul_mod, Nat.mod_mod, ← Nat.mul_mod]

/-- The `k`-th rank of the orbit of rank `0` is a forced position: `T ≠ 0` there. -/
noncomputable def forcedAt (k : ℕ) : Prop := Ω.T (Ω.orb 0 k) ≠ 0

noncomputable instance decForcedAt (k : ℕ) : Decidable (Ω.forcedAt k) :=
  inferInstanceAs (Decidable (Ω.T (Ω.orb 0 k) ≠ 0))

/-- C006's `J`, the number of forced positions (`T_j ≠ 0`), counted along the orbit. -/
noncomputable def J : ℕ := ((Finset.range m).filter Ω.forcedAt).card

/-- `J` counts the ranks with `T_r ≠ 0`, as in the prose (the orbit visits every rank once). -/
theorem J_eq : Ω.J = ((Finset.range m).filter (fun r => Ω.T r ≠ 0)).card := by
  unfold J
  apply Finset.card_bij (fun k _ => Ω.orb 0 k)
  · intro k hk
    rw [Finset.mem_filter] at hk ⊢
    exact ⟨Finset.mem_range.mpr (Ω.orb_lt 0 k), hk.2⟩
  · intro k hk k' hk' h
    rw [Ω.orb_zero_eq_rank, Ω.orb_zero_eq_rank] at h
    exact Ω.N.rank_inj Ω.N_prim (Finset.mem_range.mp (Finset.mem_filter.mp hk).1)
      (Finset.mem_range.mp (Finset.mem_filter.mp hk').1) h
  · intro r hr
    rw [Finset.mem_filter] at hr
    obtain ⟨k, hk, hrk⟩ := Ω.N.exists_rank_eq Ω.N_prim (Finset.mem_range.mp hr.1)
    refine ⟨k, Finset.mem_filter.mpr ⟨Finset.mem_range.mpr hk, ?_⟩, ?_⟩
    · show Ω.T (Ω.orb 0 k) ≠ 0
      rw [Ω.orb_zero_eq_rank, hrk]
      exact hr.2
    · rw [Ω.orb_zero_eq_rank, hrk]

/-- The seam makes `J ≥ 1`. -/
theorem J_pos : 0 < Ω.J := by
  rw [Ω.J_eq]
  apply Finset.card_pos.mpr
  refine ⟨m - 1, Finset.mem_filter.mpr ⟨Finset.mem_range.mpr ?_, ?_⟩⟩
  · have := Ω.Γ.hm
    omega
  · exact ne_of_gt Ω.T_seam_pos

/-- Some rank `r₀` starts a zero-forcing run of length `⌊(m−1)/J⌋ = ⌈m/J⌉ − 1`. -/
theorem exists_zero_run :
    ∃ r₀, r₀ < m ∧ ∀ j, j < (m - 1) / Ω.J → Ω.T (Ω.orb r₀ j) = 0 := by
  obtain ⟨k₀, _, _, hrun⟩ := exists_run Ω.Γ.hm Ω.forcedAt Ω.J_pos
  refine ⟨Ω.orb 0 (k₀ + 1), Ω.orb_lt _ _, ?_⟩
  intro j hj
  have h := hrun j hj
  unfold forcedAt at h
  rw [Ω.orb_mod] at h
  rw [Ω.orb_orb]
  exact not_ne_iff.mp h

/-- **C006's (G1), first inequality:** `L > 2^{⌈m/J⌉ − 1 − B}`, in the cleared form
`2^{⌊(m−1)/J⌋} < 2^B L`. -/
theorem G1_first : (2 : ℤ) ^ ((m - 1) / Ω.J) < 2 ^ Ω.Γ.B * Ω.Γ.n 0 := by
  obtain ⟨r₀, hr₀, hrun⟩ := Ω.exists_zero_run
  exact Ω.run_bound_L hr₀ hrun

/-! #### C006's (H1): `J ≥ B + 1` in sorted order -/

/-- The height of the state of rank `rank i` is the height of state `i`. -/
theorem hr_rank {i : ℕ} (hi : i < m) : Ω.hr (Ω.N.rank i) = Ω.Γ.h i := by
  unfold hr
  have hr := Ω.N.idx_spec Ω.N_prim (Ω.N.rank_lt i)
  have hx : Ω.N.x (Ω.N.idx (Ω.N.rank i)) = Ω.N.x i := Ω.N.x_eq_of_rank_eq hr.1 hi hr.2
  rw [Ω.N_x, Ω.N_x] at hx
  exact (Ω.Γ.Z_inj hx).1

/-- Under `q ≤ L` and positive valuations every height up to an attained one is the height of
some ranked state. -/
theorem exists_rank_height (hqL : Ω.Γ.q ≤ Ω.Γ.n 0) (hapos : ∀ i, 1 ≤ Ω.Γ.a i) {j b : ℕ}
    (hb : b ≤ Ω.Γ.h j) : ∃ r, r < m ∧ Ω.hr r = b := by
  obtain ⟨i, _, hi⟩ := Ω.Γ.exists_height_eq hqL hapos hb
  refine ⟨Ω.N.rank (i % m), Ω.N.rank_lt _, ?_⟩
  rw [Ω.hr_rank (Nat.mod_lt _ Ω.Γ.hm), Ω.Γ.h_mod, hi]

/-- `J` is one plus the number of adjacent sorted-height changes (the seam counted once). -/
theorem J_eq_changes :
    Ω.J = 1 + ((Finset.range (m - 1)).filter (fun r => Ω.hr (r + 1) ≠ Ω.hr r)).card := by
  rw [Ω.J_eq]
  have hm := Ω.Γ.hm
  have hsplit : Finset.range m = insert (m - 1) (Finset.range (m - 1)) := by
    conv_lhs => rw [show m = (m - 1) + 1 by omega]
    exact Finset.range_add_one
  have hfeq : (Finset.range (m - 1)).filter (fun r => Ω.T r ≠ 0)
      = (Finset.range (m - 1)).filter (fun r => Ω.hr (r + 1) ≠ Ω.hr r) := by
    apply Finset.filter_congr
    intro r hr
    have hr1 : r + 1 < m := by
      have := Finset.mem_range.mp hr
      omega
    exact not_congr (Ω.T_eq_zero_iff hr1)
  have hnot : m - 1 ∉ (Finset.range (m - 1)).filter (fun r => Ω.T r ≠ 0) := fun hmem =>
    lt_irrefl (m - 1) (Finset.mem_range.mp (Finset.mem_filter.mp hmem).1)
  rw [hsplit, Finset.filter_insert, ite_eq_left (ne_of_gt Ω.T_seam_pos),
    Finset.card_insert_of_notMem hnot, hfeq, add_comm]

/-- **C006's (H1), `J ≥ B + 1`:** under `q ≤ L` and positive valuations, every attained height
`h_j` satisfies `h_j + 1 ≤ J` (all heights `0, …, h_j` occur, so the sorted height list has at
least `h_j` changes, plus the seam). -/
theorem J_ge_height (hqL : Ω.Γ.q ≤ Ω.Γ.n 0) (hapos : ∀ i, 1 ≤ Ω.Γ.a i) (j : ℕ) :
    Ω.Γ.h j + 1 ≤ Ω.J := by
  have hm := Ω.Γ.hm
  have hsub : Finset.range (Ω.Γ.h j + 1) ⊆ (Finset.range m).image Ω.hr := by
    intro b hb
    obtain ⟨r, hr, hrb⟩ :=
      Ω.exists_rank_height hqL hapos (Nat.lt_succ_iff.mp (Finset.mem_range.mp hb))
    exact Finset.mem_image.mpr ⟨r, Finset.mem_range.mpr hr, hrb⟩
  have h1 := Finset.card_le_card hsub
  rw [Finset.card_range] at h1
  have h2 := card_image_le_changes Ω.hr (m - 1)
  rw [show m - 1 + 1 = m by omega] at h2
  rw [Ω.J_eq_changes]
  omega

/-! #### (G1)'s second inequality, in the true-intercept form -/

/-- (G1)'s second inequality with the true weighted intercept `C_h = C_m` (the chronological
intercept at the minimum, `D L = q C_h`): `D · 2^{⌊(m−1)/J⌋} < 2^B q C_h`, i.e.
`q > (D/C_h) 2^{⌈m/J⌉−1−B}`. C006 states the weaker `C_c` form through `C_h ≤ C_c`, which is
not formalised here. -/
theorem G1_second :
    ((2 : ℤ) ^ Ω.Γ.Apre m - 3 ^ m) * 2 ^ ((m - 1) / Ω.J)
      < 2 ^ Ω.Γ.B * (Ω.Γ.q * Ω.Γ.Cpre m) := by
  have hD := Ω.Γ.D_pos
  have h1 := Ω.G1_first
  have hc := Ω.Γ.cycle_identity
  calc ((2 : ℤ) ^ Ω.Γ.Apre m - 3 ^ m) * 2 ^ ((m - 1) / Ω.J)
      < ((2 : ℤ) ^ Ω.Γ.Apre m - 3 ^ m) * (2 ^ Ω.Γ.B * Ω.Γ.n 0) :=
        mul_lt_mul_of_pos_left h1 hD
    _ = 2 ^ Ω.Γ.B * (((2 : ℤ) ^ Ω.Γ.Apre m - 3 ^ m) * Ω.Γ.n 0) := by ring
    _ = 2 ^ Ω.Γ.B * (Ω.Γ.q * Ω.Γ.Cpre m) := by rw [hc]

/-! #### C010's sharp odd-spacing bounds and the summed bound `L ≥ R_q(H)` -/

/-- The sorted state of rank `r` in coordinates: `y_r = 2^{B − hr_r} n_{idx r}`. -/
theorem y_eq (r : ℕ) : Ω.N.y r = 2 ^ (Ω.Γ.B - Ω.hr r) * Ω.Γ.n (Ω.N.idx r) := rfl

/-- Adjacent sorted states are strictly increasing. -/
theorem y_succ_lt {r : ℕ} (hr1 : r + 1 < m) : Ω.N.y r < Ω.N.y (r + 1) :=
  Ω.N.y_lt_y Ω.N_prim (Nat.lt_succ_self r) hr1

/-- An interior gap is the difference of adjacent sorted states. -/
theorem gap_eq {r : ℕ} (hr1 : r + 1 < m) : Ω.N.gap r = Ω.N.y (r + 1) - Ω.N.y r := by
  unfold NarrowCycle.gap
  rw [Ω.N.yext_of_lt hr1, Ω.N.yext_of_lt (by omega)]

/-- Equal adjacent heights: `G_r ≥ 2 · 2^{B − a}` (two odd numerators differ by at least `2`). -/
theorem gap_ge_of_eq {r : ℕ} (hr1 : r + 1 < m) (heq : Ω.hr (r + 1) = Ω.hr r) :
    2 * 2 ^ (Ω.Γ.B - Ω.hr r) ≤ Ω.N.gap r := by
  have hy := Ω.y_succ_lt hr1
  have hyr := Ω.y_eq r
  have hyr1 := Ω.y_eq (r + 1)
  rw [heq] at hyr1
  have hPpos : (0 : ℤ) < 2 ^ (Ω.Γ.B - Ω.hr r) := by positivity
  rw [hyr, hyr1] at hy
  have hlt := lt_of_mul_lt_mul_left hy hPpos.le
  obtain ⟨s, hs⟩ := Ω.Γ.nodd (Ω.N.idx r)
  obtain ⟨t, ht⟩ := Ω.Γ.nodd (Ω.N.idx (r + 1))
  have h2 : (2 : ℤ) ≤ Ω.Γ.n (Ω.N.idx (r + 1)) - Ω.Γ.n (Ω.N.idx r) := by omega
  rw [Ω.gap_eq hr1, hyr, hyr1]
  have h3 := mul_le_mul_of_nonneg_left h2 hPpos.le
  rw [mul_sub] at h3
  linarith

/-- Downward adjacent heights: `G_r ≥ 2^{B − a}` (the numerator `2^{a−b} n_{[r+1]} − n_{[r]}` is a
positive integer). -/
theorem gap_ge_of_lt {r : ℕ} (hr1 : r + 1 < m) (hlt : Ω.hr (r + 1) < Ω.hr r) :
    2 ^ (Ω.Γ.B - Ω.hr r) ≤ Ω.N.gap r := by
  have hy := Ω.y_succ_lt hr1
  have hyr := Ω.y_eq r
  have hB := Ω.hr_le_B r
  have hsplit : Ω.Γ.B - Ω.hr (r + 1) = (Ω.Γ.B - Ω.hr r) + (Ω.hr r - Ω.hr (r + 1)) := by omega
  have hyr1 : Ω.N.y (r + 1) = 2 ^ (Ω.Γ.B - Ω.hr r) *
      (2 ^ (Ω.hr r - Ω.hr (r + 1)) * Ω.Γ.n (Ω.N.idx (r + 1))) := by
    rw [Ω.y_eq (r + 1), hsplit, pow_add, mul_assoc]
  have hPpos : (0 : ℤ) < 2 ^ (Ω.Γ.B - Ω.hr r) := by positivity
  rw [hyr, hyr1] at hy
  have hlt' := lt_of_mul_lt_mul_left hy hPpos.le
  have h1 : (1 : ℤ) ≤ 2 ^ (Ω.hr r - Ω.hr (r + 1)) * Ω.Γ.n (Ω.N.idx (r + 1))
      - Ω.Γ.n (Ω.N.idx r) := by omega
  rw [Ω.gap_eq hr1, hyr, hyr1]
  have h3 := mul_le_mul_of_nonneg_left h1 hPpos.le
  rw [mul_sub, mul_one] at h3
  linarith

/-- The seam: `G_{m−1} ≥ 2^{B − a}` with `a = hr_{m−1}` (the numerator `2^{a+1} L − n_{[m−1]}` is a
positive integer). -/
theorem gap_seam_ge : 2 ^ (Ω.Γ.B - Ω.hr (m - 1)) ≤ Ω.N.gap (m - 1) := by
  have hm := Ω.Γ.hm
  have hgap : Ω.N.gap (m - 1) = 2 * Ω.N.y 0 - Ω.N.y (m - 1) := by
    unfold NarrowCycle.gap
    rw [show m - 1 + 1 = m by omega, Ω.N.yext_m, Ω.N.yext_of_lt (by omega)]
  have hy0 : Ω.N.y 0 = 2 ^ Ω.Γ.B * Ω.Γ.n 0 := by
    rw [Ω.N.y_zero Ω.N_prim Ω.N_rank_zero, Ω.N_x, Ω.Γ.Z_zero]
    rfl
  have hpos := Ω.N.gap_pos Ω.N_prim Ω.N_rank_zero (Nat.sub_lt hm Nat.one_pos)
  have hB := Ω.hr_le_B (m - 1)
  have hsplit : Ω.Γ.B + 1 = (Ω.Γ.B - Ω.hr (m - 1)) + (Ω.hr (m - 1) + 1) := by omega
  have hpow : (2 : ℤ) ^ Ω.Γ.B * 2 = 2 ^ (Ω.Γ.B - Ω.hr (m - 1)) * 2 ^ (Ω.hr (m - 1) + 1) := by
    rw [← pow_succ, ← pow_add, ← hsplit]
  have h2y0 : 2 * Ω.N.y 0 = 2 ^ (Ω.Γ.B - Ω.hr (m - 1)) *
      (2 ^ (Ω.hr (m - 1) + 1) * Ω.Γ.n 0) := by
    rw [hy0]
    linear_combination Ω.Γ.n 0 * hpow
  have hym := Ω.y_eq (m - 1)
  have hPpos : (0 : ℤ) < 2 ^ (Ω.Γ.B - Ω.hr (m - 1)) := by positivity
  rw [hgap, h2y0, hym] at hpos ⊢
  rw [← mul_sub] at hpos ⊢
  have h1 : (1 : ℤ) ≤ 2 ^ (Ω.hr (m - 1) + 1) * Ω.Γ.n 0 - Ω.Γ.n (Ω.N.idx (m - 1)) := by
    have := (mul_pos_iff_of_pos_left hPpos).mp hpos
    omega
  have h3 := mul_le_mul_of_nonneg_left h1 hPpos.le
  rw [mul_one] at h3
  exact h3

/-- Upward adjacent heights, the order inequality: `2^{B−b} q (2^k − 1) < 3 G_r` with `k = b − a`
(strict increase of the images `F_{[r]} < F_{[r+1]}`). -/
theorem three_gap_gt_of_gt {r : ℕ} (hr1 : r + 1 < m) (hgt : Ω.hr r < Ω.hr (r + 1)) :
    2 ^ (Ω.Γ.B - Ω.hr (r + 1)) * (Ω.Γ.q * (2 ^ (Ω.hr (r + 1) - Ω.hr r) - 1))
      < 3 * Ω.N.gap r := by
  have hy := Ω.y_succ_lt hr1
  have hZ : Ω.Γ.Z (Ω.N.idx r) < Ω.Γ.Z (Ω.N.idx (r + 1)) := hy
  have hF : Ω.Γ.F (Ω.N.idx r) < Ω.Γ.F (Ω.N.idx (r + 1)) := (Ω.hord _ _).mp hZ
  have hB := Ω.hr_le_B (r + 1)
  have hsplit : Ω.Γ.B - Ω.hr r = (Ω.Γ.B - Ω.hr (r + 1)) + (Ω.hr (r + 1) - Ω.hr r) := by omega
  have hFi : Ω.Γ.F (Ω.N.idx r) = 3 * Ω.N.y r + 2 ^ (Ω.Γ.B - Ω.hr r) * Ω.Γ.q := rfl
  have hFj : Ω.Γ.F (Ω.N.idx (r + 1)) =
      3 * Ω.N.y (r + 1) + 2 ^ (Ω.Γ.B - Ω.hr (r + 1)) * Ω.Γ.q := rfl
  rw [hFi, hFj, hsplit, pow_add] at hF
  rw [Ω.gap_eq hr1]
  linear_combination hF

/-- Upward adjacent heights, C010's sharp form: `2^{B−b} (q (2^k − 1) + η(q, k)) ≤ 3 G_r`
(`q` odd). -/
theorem three_gap_ge_of_gt (hqodd : Odd Ω.Γ.q) {r : ℕ} (hr1 : r + 1 < m)
    (hgt : Ω.hr r < Ω.hr (r + 1)) :
    2 ^ (Ω.Γ.B - Ω.hr (r + 1)) * (Ω.Γ.q * (2 ^ (Ω.hr (r + 1) - Ω.hr r) - 1)
      + eta Ω.Γ.q (Ω.hr (r + 1) - Ω.hr r)) ≤ 3 * Ω.N.gap r := by
  have hB := Ω.hr_le_B (r + 1)
  have hsplit : Ω.Γ.B - Ω.hr r = (Ω.Γ.B - Ω.hr (r + 1)) + (Ω.hr (r + 1) - Ω.hr r) := by omega
  have hyr : Ω.N.y r = 2 ^ (Ω.Γ.B - Ω.hr (r + 1)) *
      (2 ^ (Ω.hr (r + 1) - Ω.hr r) * Ω.Γ.n (Ω.N.idx r)) := by
    rw [Ω.y_eq r, hsplit, pow_add, mul_assoc]
  have hyr1 := Ω.y_eq (r + 1)
  have hPpos : (0 : ℤ) < 2 ^ (Ω.Γ.B - Ω.hr (r + 1)) := by positivity
  have hgapeq : Ω.N.gap r = 2 ^ (Ω.Γ.B - Ω.hr (r + 1)) *
      (Ω.Γ.n (Ω.N.idx (r + 1)) - 2 ^ (Ω.hr (r + 1) - Ω.hr r) * Ω.Γ.n (Ω.N.idx r)) := by
    rw [Ω.gap_eq hr1, hyr, hyr1, mul_sub]
  have hstrict := Ω.three_gap_gt_of_gt hr1 hgt
  rw [hgapeq] at hstrict
  have hr' : Ω.Γ.q * (2 ^ (Ω.hr (r + 1) - Ω.hr r) - 1)
      < 3 * (Ω.Γ.n (Ω.N.idx (r + 1)) - 2 ^ (Ω.hr (r + 1) - Ω.hr r) * Ω.Γ.n (Ω.N.idx r)) := by
    have h' : 2 ^ (Ω.Γ.B - Ω.hr (r + 1)) * (Ω.Γ.q * (2 ^ (Ω.hr (r + 1) - Ω.hr r) - 1))
        < 2 ^ (Ω.Γ.B - Ω.hr (r + 1)) * (3 * (Ω.Γ.n (Ω.N.idx (r + 1))
          - 2 ^ (Ω.hr (r + 1) - Ω.hr r) * Ω.Γ.n (Ω.N.idx r))) := by
      linear_combination hstrict
    exact lt_of_mul_lt_mul_left h' hPpos.le
  have hodd : Odd (Ω.Γ.n (Ω.N.idx (r + 1))
      - 2 ^ (Ω.hr (r + 1) - Ω.hr r) * Ω.Γ.n (Ω.N.idx r)) := by
    have he : Even (2 ^ (Ω.hr (r + 1) - Ω.hr r) * Ω.Γ.n (Ω.N.idx r)) :=
      even_iff_two_dvd.mpr (dvd_mul_of_dvd_left (dvd_pow_self 2 (by omega)) _)
    exact (Ω.Γ.nodd _).sub_even he
  have hk : 1 ≤ Ω.hr (r + 1) - Ω.hr r := by omega
  have hbound := eta_refine _ hk hqodd hodd hr'
  rw [hgapeq]
  have h3' := mul_le_mul_of_nonneg_left hbound hPpos.le
  linarith

/-- Three times C010's sharp lower bound for the complete gap `G_r` (scaled by `2^B`): the seam,
equal, downward and upward cases of `b_q(H_r, H_{r+1})`, so that `Σ_r pairBound3 r / (3 · 2^B)`
is the prose's `R_q(H)`. -/
noncomputable def pairBound3 (r : ℕ) : ℤ :=
  if r + 1 < m then
    (if Ω.hr (r + 1) = Ω.hr r then 3 * (2 * 2 ^ (Ω.Γ.B - Ω.hr r))
     else if Ω.hr (r + 1) < Ω.hr r then 3 * 2 ^ (Ω.Γ.B - Ω.hr r)
     else 2 ^ (Ω.Γ.B - Ω.hr (r + 1)) * (Ω.Γ.q * (2 ^ (Ω.hr (r + 1) - Ω.hr r) - 1)
            + eta Ω.Γ.q (Ω.hr (r + 1) - Ω.hr r)))
  else 3 * 2 ^ (Ω.Γ.B - Ω.hr r)

/-- Each complete gap dominates its sharp bound: `pairBound3 r ≤ 3 G_r`. -/
theorem pairBound3_le (hqodd : Odd Ω.Γ.q) {r : ℕ} (hr : r < m) :
    Ω.pairBound3 r ≤ 3 * Ω.N.gap r := by
  unfold pairBound3
  split_ifs with h1 h2 h4
  · exact mul_le_mul_of_nonneg_left (Ω.gap_ge_of_eq h1 h2) (by norm_num)
  · exact mul_le_mul_of_nonneg_left (Ω.gap_ge_of_lt h1 h4) (by norm_num)
  · exact Ω.three_gap_ge_of_gt hqodd h1 (lt_of_le_of_ne (not_lt.mp h4) (Ne.symm h2))
  · have hm1 : r = m - 1 := by omega
    subst hm1
    exact mul_le_mul_of_nonneg_left Ω.gap_seam_ge (by norm_num)

/-- **C010's summed bound** `L ≥ R_q(H)` (its (3)) in scaled integer form: the sharp bounds of
the `m` complete gaps sum to at most `3 · 2^B L`, because the complete gaps sum to `2^B L`. -/
theorem rounding_bound (hqodd : Odd Ω.Γ.q) :
    ∑ r ∈ Finset.range m, Ω.pairBound3 r ≤ 3 * (2 ^ Ω.Γ.B * Ω.Γ.n 0) := by
  have hsum := Ω.N.sum_gap Ω.N_prim Ω.N_rank_zero
  rw [Ω.N_x, Ω.Γ.Z_zero] at hsum
  calc ∑ r ∈ Finset.range m, Ω.pairBound3 r
      ≤ ∑ r ∈ Finset.range m, 3 * Ω.N.gap r :=
        Finset.sum_le_sum fun r hr => Ω.pairBound3_le hqodd (Finset.mem_range.mp hr)
    _ = 3 * ∑ r ∈ Finset.range m, Ω.N.gap r := by rw [Finset.mul_sum]
    _ = 3 * Ω.Γ.lo := by rw [hsum]
    _ = 3 * (2 ^ Ω.Γ.B * Ω.Γ.n 0) := rfl

/-! #### S1-a: the unrolled (G3) — every `D`-scaled sorted gap as a forcing sum

Side lane's lead (feed 06:30, index convention 06:40): unroll `gap_rec` once around the rank
orbit. With `r_i = orb r₀ i` and `E_i = e_{r_0} + ⋯ + e_{r_{i−1}}` (`E_0 = 0`),
`2^{E_n} Δ_{r_n} = 3^n Δ_{r_0} + Σ_{i<n} 3^{n−1−i} 2^{E_i} T_{r_i}` for every `n`; at `n = m` the
orbit closes (`r_m = r_0`, `E_m = A`), so `(2^A − 3^m) Δ_{r_0} = Σ_{i<m} 3^{m−1−i} 2^{E_i} T_{r_i}`,
and only the forced positions (`T ≠ 0`) contribute. The feed's `G_{r_0} = Σ 3^{m−1−i} 2^{E_i} τ_{r_i}`
is this identity divided by `q`: here `T_r = q τ_r` and `D Δ_r = q G_r`. -/

/-- The exponent sum along the orbit from rank `r₀`: `E_n = Σ_{t<n} e(r_t)`, `E_0 = 0`. -/
noncomputable def E (r₀ n : ℕ) : ℕ := ∑ t ∈ Finset.range n, Ω.N.e (Ω.orb r₀ t)

theorem E_succ (r₀ n : ℕ) : Ω.E r₀ (n + 1) = Ω.E r₀ n + Ω.N.e (Ω.orb r₀ n) := by
  unfold E
  rw [Finset.sum_range_succ]

/-- The forcing sum along the orbit, as the recurrence `S_0 = 0`,
`S_{n+1} = 3 S_n + 2^{E_n} T_{r_n}`. -/
noncomputable def jsum (r₀ : ℕ) : ℕ → ℤ
  | 0 => 0
  | n + 1 => 3 * jsum r₀ n + 2 ^ Ω.E r₀ n * Ω.T (Ω.orb r₀ n)

/-- Closed form of the forcing sum: `S_n = Σ_{i<n} 3^{n−1−i} 2^{E_i} T_{r_i}`. -/
theorem jsum_eq_sum (r₀ n : ℕ) :
    Ω.jsum r₀ n = ∑ i ∈ Finset.range n, 3 ^ (n - 1 - i) * 2 ^ Ω.E r₀ i * Ω.T (Ω.orb r₀ i) := by
  induction n with
  | zero => simp [jsum]
  | succ n ih =>
    rw [jsum, ih, Finset.sum_range_succ, Finset.mul_sum]
    congr 1
    · apply Finset.sum_congr rfl
      intro i hi
      have hi' := Finset.mem_range.mp hi
      rw [show n + 1 - 1 - i = n - 1 - i + 1 by omega, pow_succ]
      ring
    · rw [show n + 1 - 1 - n = 0 by omega, pow_zero, one_mul]

/-- **The unrolled (G3)**: `2^{E_n} Δ_{r_n} = 3^n Δ_{r_0} + S_n` for every `n`. -/
theorem gap_unroll {r₀ : ℕ} (hr₀ : r₀ < m) (n : ℕ) :
    (2 : ℤ) ^ Ω.E r₀ n * Ω.N.gap (Ω.orb r₀ n) = 3 ^ n * Ω.N.gap r₀ + Ω.jsum r₀ n := by
  induction n with
  | zero => simp [E, jsum, Ω.orb_zero hr₀]
  | succ n ih =>
    rw [Ω.E_succ, pow_add, mul_assoc, Ω.orb_succ r₀ n, Ω.gap_rec (Ω.orb_lt r₀ n), jsum]
    linear_combination 3 * ih

/-- The orbit closes after `m` steps. -/
theorem orb_m {r₀ : ℕ} (hr₀ : r₀ < m) : Ω.orb r₀ m = r₀ := by
  unfold orb
  rw [Nat.add_mul_mod_self_left]
  exact Nat.mod_eq_of_lt hr₀

/-- A sum over one period of a `p`-periodic function is shift invariant. -/
theorem sum_range_shift {g : ℕ → ℕ} {p : ℕ} (hg : ∀ t, g (t + p) = g t) (a : ℕ) :
    ∑ t ∈ Finset.range p, g (a + t) = ∑ t ∈ Finset.range p, g t := by
  induction a with
  | zero => simp
  | succ a ih =>
    have h1 : ∑ t ∈ Finset.range (p + 1), g (a + t) =
        ∑ t ∈ Finset.range p, g (a + t) + g (a + p) := Finset.sum_range_succ _ _
    have h2 : ∑ t ∈ Finset.range (p + 1), g (a + t) =
        ∑ t ∈ Finset.range p, g (a + (t + 1)) + g a := Finset.sum_range_succ' _ _
    have h3 : ∑ t ∈ Finset.range p, g (a + 1 + t) = ∑ t ∈ Finset.range p, g (a + (t + 1)) :=
      Finset.sum_congr rfl (fun t _ => by rw [show a + 1 + t = a + (t + 1) by omega])
    rw [hg a] at h1
    rw [h3, ← ih]
    exact Nat.add_right_cancel (h2.symm.trans h1)

/-- The exponent sum over one full orbit is the total `A`: every rank is visited once, `e_r` is
the letter at the index of rank `r`, and `Σ c_i = Σ a_i`. -/
theorem E_m {r₀ : ℕ} (hr₀ : r₀ < m) : Ω.E r₀ m = Ω.Γ.Apre m := by
  obtain ⟨a, ha, hra⟩ := Ω.N.exists_rank_eq Ω.N_prim hr₀
  have h1 : ∀ t, Ω.orb r₀ t = Ω.orb 0 (a + t) := fun t => by
    rw [← Ω.orb_orb, Ω.orb_zero_eq_rank, hra]
  have hper : ∀ t, Ω.N.e (Ω.orb 0 (t + m)) = Ω.N.e (Ω.orb 0 t) := fun t => by
    rw [← Ω.orb_mod (t + m), Nat.add_mod_right, Ω.orb_mod t]
  have h2 : ∀ t, t < m → Ω.N.e (Ω.orb 0 t) = Ω.N.a t := fun t ht => by
    rw [Ω.orb_zero_eq_rank t, Ω.N.e_eq Ω.N_prim (Ω.N.rank_lt t)]
    congr 1
    exact Ω.N.rank_inj Ω.N_prim (Ω.N.idx_spec Ω.N_prim (Ω.N.rank_lt t)).1 ht
      (Ω.N.idx_spec Ω.N_prim (Ω.N.rank_lt t)).2
  have h0 : ∑ t ∈ Finset.range m, Ω.N.e (Ω.orb r₀ t) =
      ∑ t ∈ Finset.range m, Ω.N.e (Ω.orb 0 (a + t)) :=
    Finset.sum_congr rfl (fun t _ => by rw [h1 t])
  have h3 : ∑ t ∈ Finset.range m, Ω.N.e (Ω.orb 0 (a + t)) =
      ∑ t ∈ Finset.range m, Ω.N.e (Ω.orb 0 t) :=
    sum_range_shift (g := fun t => Ω.N.e (Ω.orb 0 t)) hper a
  have h4 : ∑ t ∈ Finset.range m, Ω.N.e (Ω.orb 0 t) = ∑ t ∈ Finset.range m, Ω.N.a t :=
    Finset.sum_congr rfl (fun t ht => h2 t (Finset.mem_range.mp ht))
  have h5 : ∑ t ∈ Finset.range m, Ω.N.a t = Ω.Γ.Apre m := by
    show ∑ t ∈ Finset.range m, Ω.Γ.c t = Ω.Γ.Apre m
    rw [Ω.Γ.sum_c]
    rfl
  unfold E
  rw [h0, h3, h4, h5]

/-- **The `D`-scaled gap closed form** (S1-a): for every sorted rank `r₀`,
`(2^A − 3^m) Δ_{r₀} = Σ_{i<m} 3^{m−1−i} 2^{E_i} T_{r_i}`. -/
theorem gap_closed_form {r₀ : ℕ} (hr₀ : r₀ < m) :
    ((2 : ℤ) ^ Ω.Γ.Apre m - 3 ^ m) * Ω.N.gap r₀ =
      ∑ i ∈ Finset.range m, 3 ^ (m - 1 - i) * 2 ^ Ω.E r₀ i * Ω.T (Ω.orb r₀ i) := by
  have h := Ω.gap_unroll hr₀ m
  rw [Ω.orb_m hr₀, Ω.E_m hr₀, Ω.jsum_eq_sum] at h
  linear_combination h

/-- Only the forced positions (`T ≠ 0`) contribute to the closed form. -/
theorem gap_closed_form_filter {r₀ : ℕ} (hr₀ : r₀ < m) :
    ((2 : ℤ) ^ Ω.Γ.Apre m - 3 ^ m) * Ω.N.gap r₀ =
      ∑ i ∈ (Finset.range m).filter (fun i => Ω.T (Ω.orb r₀ i) ≠ 0),
        3 ^ (m - 1 - i) * 2 ^ Ω.E r₀ i * Ω.T (Ω.orb r₀ i) := by
  rw [Ω.gap_closed_form hr₀, Finset.sum_filter]
  apply Finset.sum_congr rfl
  intro i _
  split_ifs with h
  · rfl
  · rw [Ne, not_not] at h
    rw [h, mul_zero]

/-- From rank `0`, the contributing positions are exactly the `J` forced positions. -/
theorem card_forced_zero :
    ((Finset.range m).filter (fun i => Ω.T (Ω.orb 0 i) ≠ 0)).card = Ω.J := rfl

/-- `D` divides every forcing sum (the feed's "at `q = 1`, `D` must divide all `J`-term sums";
here with `T = q τ`, for every `q`). -/
theorem D_dvd_forcing_sum {r₀ : ℕ} (hr₀ : r₀ < m) :
    ((2 : ℤ) ^ Ω.Γ.Apre m - 3 ^ m) ∣
      ∑ i ∈ Finset.range m, 3 ^ (m - 1 - i) * 2 ^ Ω.E r₀ i * Ω.T (Ω.orb r₀ i) :=
  ⟨Ω.N.gap r₀, (Ω.gap_closed_form hr₀).symm⟩

/-! #### S1-b: the gcd consequence — the run-start gaps are jointly coprime to `q`

Side lane's "`gcd(C, D) = gcd(D, the J run-start gaps)`" in the integer normalisation. For a
reduced cycle (`gcd(q, n_0) = 1`, `q` odd), with `D = g q`, `Ẑ_i = g Z_i` and the feed's gaps
`G_r = g Δ_r`, the statement is `gcd(q, {Δ_r : r a run start}) = 1`: a divisor of `q` dividing
every run-start gap is a unit. Inside a run the gaps change by `3/2^e` only (`gap_rec` with
`T = 0`), so divisibility by a divisor of `q` is constant along a run (`dvd_gap_run_iff`); every
rank lies in the run of some run start (`exists_run_start`, anchored at the rank after the seam);
and a divisor of `q` dividing every gap divides `Σ_r Δ_r = Z_0 = 2^B n_0`, hence `n_0`, hence is a
unit (`dvd_all_gaps_isUnit`). -/

theorem isCoprime_q_two (hq : Odd Ω.Γ.q) : IsCoprime Ω.Γ.q 2 := by
  obtain ⟨k, hk⟩ := hq
  exact ⟨1, -k, by rw [hk]; ring⟩

theorem isCoprime_q_three (hred : IsCoprime Ω.Γ.q (Ω.Γ.n 0)) : IsCoprime Ω.Γ.q 3 := by
  have h3 : IsCoprime (3 : ℤ) (2 ^ Ω.Γ.Apre m - 3 ^ m) := by
    rw [← Ω.Γ.D_word]
    exact isCoprime_three_D (by rw [Ω.Γ.word_length]; exact Ω.Γ.hm)
  exact (h3.of_isCoprime_of_dvd_right (Ω.Γ.q_dvd_D hred)).symm

/-- Along a zero-forcing run, divisibility of the gaps by a divisor of `q` is constant. -/
theorem dvd_gap_run_iff {d : ℤ} (hd2 : IsCoprime d 2) (hd3 : IsCoprime d 3) {r₀ : ℕ}
    (hr₀ : r₀ < m) (t : ℕ) (hrun : ∀ k, k < t → Ω.T (Ω.orb r₀ k) = 0) :
    d ∣ Ω.N.gap (Ω.orb r₀ t) ↔ d ∣ Ω.N.gap r₀ := by
  induction t with
  | zero => rw [Ω.orb_zero hr₀]
  | succ t ih =>
    have hG : (2 : ℤ) ^ Ω.N.e (Ω.orb r₀ t) * Ω.N.gap (Ω.orb r₀ (t + 1)) =
        3 * Ω.N.gap (Ω.orb r₀ t) := by
      rw [Ω.orb_succ, Ω.gap_rec (Ω.orb_lt r₀ t), hrun t (Nat.lt_succ_self t), add_zero]
    rw [← ih (fun k hk => hrun k (Nat.lt_succ_of_lt hk))]
    constructor
    · intro h
      have h' : d ∣ 3 * Ω.N.gap (Ω.orb r₀ t) := by
        rw [← hG]
        exact h.mul_left _
      exact hd3.dvd_of_dvd_mul_left h'
    · intro h
      have h' : d ∣ 2 ^ Ω.N.e (Ω.orb r₀ t) * Ω.N.gap (Ω.orb r₀ (t + 1)) := by
        rw [hG]
        exact h.mul_left _
      exact hd2.pow_right.dvd_of_dvd_mul_left h'

theorem orb_add (r a b : ℕ) : Ω.orb (Ω.orb r a) b = Ω.orb r (a + b) := by
  unfold orb
  rw [Nat.mod_add_mod, Nat.add_mul, Nat.add_assoc]

/-- `orb r (m − 1)` is the orbit predecessor of `r`: it undoes one step. -/
theorem orb_pred_succ {r : ℕ} (hr : r < m) : Ω.orb (Ω.orb r 1) (m - 1) = r := by
  have hm := Ω.Γ.hm
  rw [Ω.orb_add, show 1 + (m - 1) = m by omega, Ω.orb_m hr]

/-- The orbit from any rank visits every rank within `m` steps. -/
theorem orb_surj {r₀ : ℕ} (hr₀ : r₀ < m) {r : ℕ} (hr : r < m) :
    ∃ j, j < m ∧ Ω.orb r₀ j = r := by
  obtain ⟨i, hi, hri⟩ := Ω.N.exists_rank_eq Ω.N_prim hr₀
  obtain ⟨i', hi', hri'⟩ := Ω.N.exists_rank_eq Ω.N_prim hr
  refine ⟨(i' + m - i) % m, Nat.mod_lt _ Ω.Γ.hm, ?_⟩
  rw [← hri, ← Ω.orb_zero_eq_rank, Ω.orb_orb, ← Ω.orb_mod, Nat.add_mod, Nat.mod_mod,
    ← Nat.add_mod, show i + (i' + m - i) = i' + m by omega, Nat.add_mod_right,
    Nat.mod_eq_of_lt hi', Ω.orb_zero_eq_rank, hri']

/-- Every rank is reached from a run start (a rank whose orbit predecessor is forced) along a
zero-forcing run; the run starts are found from the rank after the seam. -/
theorem exists_run_start {r : ℕ} (hr : r < m) :
    ∃ r' t, r' < m ∧ Ω.T (Ω.orb r' (m - 1)) ≠ 0 ∧ (∀ k, k < t → Ω.T (Ω.orb r' k) = 0) ∧
      Ω.orb r' t = r := by
  classical
  have hm := Ω.Γ.hm
  obtain ⟨r₁, hr₁⟩ : ∃ r₁, r₁ = Ω.orb (m - 1) 1 := ⟨_, rfl⟩
  have hr₁m : r₁ < m := by rw [hr₁]; exact Ω.orb_lt _ _
  have hpred : Ω.orb r₁ (m - 1) = m - 1 := by rw [hr₁]; exact Ω.orb_pred_succ (by omega)
  obtain ⟨j, hj, hrj⟩ := Ω.orb_surj hr₁m hr
  obtain ⟨P, hP⟩ : ∃ P : ℕ → Prop, ∀ i, P i ↔ (i = 0 ∨ Ω.T (Ω.orb r₁ (i - 1)) ≠ 0) :=
    ⟨_, fun _ => Iff.rfl⟩
  have hP0 : P 0 := (hP 0).mpr (Or.inl rfl)
  obtain ⟨j₀, hj₀⟩ : ∃ j₀, j₀ = Nat.findGreatest P j := ⟨_, rfl⟩
  have hj₀le : j₀ ≤ j := by rw [hj₀]; exact Nat.findGreatest_le j
  have hPj₀ : P j₀ := by rw [hj₀]; exact Nat.findGreatest_spec (Nat.zero_le j) hP0
  refine ⟨Ω.orb r₁ j₀, j - j₀, Ω.orb_lt _ _, ?_, ?_, ?_⟩
  · rcases Nat.eq_zero_or_pos j₀ with h0 | hpos
    · rw [h0, Ω.orb_zero hr₁m, hpred]
      exact ne_of_gt Ω.T_seam_pos
    · rcases (hP j₀).mp hPj₀ with h0 | hT
      · omega
      · rw [Ω.orb_add, show j₀ + (m - 1) = (j₀ - 1) + m by omega, ← Ω.orb_add,
          Ω.orb_m (Ω.orb_lt _ _)]
        exact hT
  · intro k hk
    have hnot : ¬ P (j₀ + k + 1) :=
      Nat.findGreatest_is_greatest (by rw [← hj₀]; omega) (by omega)
    have h2 : Ω.T (Ω.orb r₁ (j₀ + k)) = 0 := by
      by_contra hne
      exact hnot ((hP _).mpr (Or.inr (by rwa [show j₀ + k + 1 - 1 = j₀ + k by omega])))
    rw [Ω.orb_add]
    exact h2
  · rw [Ω.orb_add, show j₀ + (j - j₀) = j by omega, hrj]

/-- A divisor of `q` dividing every sorted gap of a reduced cycle (`q` odd) is a unit:
`Σ_r Δ_r = Z_0 = 2^B n_0` and `gcd(q, n_0) = 1`. -/
theorem dvd_all_gaps_isUnit (hq : Odd Ω.Γ.q) (hred : IsCoprime Ω.Γ.q (Ω.Γ.n 0)) {d : ℤ}
    (hd : d ∣ Ω.Γ.q) (hall : ∀ r, r < m → d ∣ Ω.N.gap r) : IsUnit d := by
  have hsum := Ω.N.sum_gap Ω.N_prim Ω.N_rank_zero
  rw [Ω.N_x, Ω.Γ.Z_zero] at hsum
  unfold OddCycle.lo at hsum
  have hdsum : d ∣ ∑ r ∈ Finset.range m, Ω.N.gap r :=
    Finset.dvd_sum (fun r hr => hall r (Finset.mem_range.mp hr))
  rw [hsum] at hdsum
  have hd2 : IsCoprime d 2 := (Ω.isCoprime_q_two hq).of_isCoprime_of_dvd_left hd
  have hdn : d ∣ Ω.Γ.n 0 := hd2.pow_right.dvd_of_dvd_mul_left hdsum
  exact hred.isUnit_of_dvd' hd hdn

/-- **S1-b**: for a reduced ordered cycle (`gcd(q, n_0) = 1`, `q` odd), the run-start gaps are
jointly coprime to `q`: a divisor of `q` dividing the gap at every run start (a rank whose orbit
predecessor is forced) is a unit. In the word normalisation (`D = g q`, `G_r = g Δ_r`) this is the
side lane's `gcd(C, D) = gcd(D, the J run-start gaps)`. -/
theorem run_start_gaps_coprime (hq : Odd Ω.Γ.q) (hred : IsCoprime Ω.Γ.q (Ω.Γ.n 0)) {d : ℤ}
    (hd : d ∣ Ω.Γ.q) (hstart : ∀ r, r < m → Ω.T (Ω.orb r (m - 1)) ≠ 0 → d ∣ Ω.N.gap r) :
    IsUnit d := by
  have hd2 : IsCoprime d 2 := (Ω.isCoprime_q_two hq).of_isCoprime_of_dvd_left hd
  have hd3 : IsCoprime d 3 := (Ω.isCoprime_q_three hred).of_isCoprime_of_dvd_left hd
  refine Ω.dvd_all_gaps_isUnit hq hred hd (fun r hr => ?_)
  obtain ⟨r', t, hr', hT, hrun, hrt⟩ := Ω.exists_run_start hr
  rw [← hrt, Ω.dvd_gap_run_iff hd2 hd3 hr' t hrun]
  exact hstart r' hr' hT

/-! #### S1-c/d: every gap is coprime to `q`; a single forced position forces `D = q`

Side lane (feed update 07:51), two consequences of S1-a/S1-b. (c) Every sorted gap of a reduced
ordered cycle (`q` odd) is coprime to `q`: a divisor `d` of `q` divides every `T_r`, so `gap_rec`
propagates `d ∣ Δ` along the whole orbit and `dvd_all_gaps_isUnit` finishes — C007-a's
`dvd_all_of_dvd` mechanism on gaps. (d) If `J = 1`, the seam is the only forced position, all
sorted heights equal `h_[0] = 0`, `T_{m−1} = 2^B q`, and the closed form at the run start after
the seam reads `D Δ = 2^{E} 2^B q`; with `q ∣ D` (reduced) and `D` odd this forces `D = q`: R71's
exact denominator for ordered cycles with a single forced position, from S1-a alone. -/

theorem q_dvd_off (r : ℕ) : Ω.Γ.q ∣ Ω.off r := by
  unfold off
  exact Dvd.intro_left _ rfl

theorem q_dvd_offext (r : ℕ) : Ω.Γ.q ∣ Ω.offext r := by
  unfold offext
  split_ifs
  · exact Ω.q_dvd_off r
  · exact (Ω.q_dvd_off (r - m)).mul_left 2

theorem q_dvd_T (r : ℕ) : Ω.Γ.q ∣ Ω.T r := by
  unfold T
  exact dvd_sub (Ω.q_dvd_offext (r + 1)) (Ω.q_dvd_offext r)

/-- Divisibility of the gaps by a divisor of `q` propagates along the whole orbit (`T ≡ 0`). -/
theorem dvd_gap_orb {d : ℤ} (hd : d ∣ Ω.Γ.q) (hd2 : IsCoprime d 2) {r₀ : ℕ}
    (hr₀ : r₀ < m) (hg : d ∣ Ω.N.gap r₀) (k : ℕ) : d ∣ Ω.N.gap (Ω.orb r₀ k) := by
  induction k with
  | zero => rw [Ω.orb_zero hr₀]; exact hg
  | succ k ih =>
    have hG := Ω.gap_rec (Ω.orb_lt r₀ k)
    rw [← Ω.orb_succ] at hG
    have h' : d ∣ 2 ^ Ω.N.e (Ω.orb r₀ k) * Ω.N.gap (Ω.orb r₀ (k + 1)) := by
      rw [hG]
      exact dvd_add (ih.mul_left 3) (hd.trans (Ω.q_dvd_T _))
    exact hd2.pow_right.dvd_of_dvd_mul_left h'

/-- **S1-c**: a common divisor of `q` and one sorted gap of a reduced ordered cycle (`q` odd) is a
unit: it divides every gap, hence `2^B n_0`, hence `n_0`. -/
theorem dvd_gap_isUnit (hq : Odd Ω.Γ.q) (hred : IsCoprime Ω.Γ.q (Ω.Γ.n 0)) {d : ℤ}
    (hd : d ∣ Ω.Γ.q) {r : ℕ} (hr : r < m) (hg : d ∣ Ω.N.gap r) : IsUnit d := by
  have hd2 : IsCoprime d 2 := (Ω.isCoprime_q_two hq).of_isCoprime_of_dvd_left hd
  refine Ω.dvd_all_gaps_isUnit hq hred hd (fun r' hr' => ?_)
  obtain ⟨k, -, hk⟩ := Ω.orb_surj hr hr'
  rw [← hk]
  exact Ω.dvd_gap_orb hd hd2 hr hg k

/-- Every sorted gap of a reduced ordered cycle (`q` odd) is coprime to `q`. -/
theorem gap_isCoprime_q (hq : Odd Ω.Γ.q) (hred : IsCoprime Ω.Γ.q (Ω.Γ.n 0)) {r : ℕ}
    (hr : r < m) : IsCoprime Ω.Γ.q (Ω.N.gap r) := by
  rw [Int.isCoprime_iff_gcd_eq_one]
  have hu := Ω.dvd_gap_isUnit hq hred (Int.gcd_dvd_left _ _) hr (Int.gcd_dvd_right _ _)
  rcases Int.isUnit_iff.mp hu with h | h
  · exact_mod_cast h
  · omega

theorem orb_inj_aux {r₀ i j : ℕ} (hij : i ≤ j) (hj : j < m) (h : Ω.orb r₀ i = Ω.orb r₀ j) :
    i = j := by
  have hcop : Nat.Coprime m Ω.N.numHigh :=
    Nat.coprime_comm.mp (Ω.N.coprime_numHigh Ω.N_prim Ω.hm2)
  unfold orb at h
  have h1 := Nat.sub_mod_eq_zero_of_mod_eq h.symm
  have h2 : r₀ + j * Ω.N.numHigh - (r₀ + i * Ω.N.numHigh) = (j - i) * Ω.N.numHigh := by
    rw [Nat.sub_mul]
    have := Nat.mul_le_mul_right Ω.N.numHigh hij
    omega
  rw [h2] at h1
  have h3 : m ∣ j - i := hcop.dvd_of_dvd_mul_right (Nat.dvd_of_mod_eq_zero h1)
  have h4 : j - i = 0 := Nat.eq_zero_of_dvd_of_lt h3 (by omega)
  omega

/-- The orbit visits each rank once in `m` steps. -/
theorem orb_inj {r₀ i j : ℕ} (hi : i < m) (hj : j < m) (h : Ω.orb r₀ i = Ω.orb r₀ j) : i = j := by
  rcases le_total i j with hij | hji
  · exact Ω.orb_inj_aux hij hj h
  · exact (Ω.orb_inj_aux hji hi h.symm).symm

/-- With `J = 1`, the seam is the only forced position: `T_r = 0` for `r + 1 < m`. -/
theorem T_eq_zero_of_J_one (hJ : Ω.J = 1) {r : ℕ} (hr : r + 1 < m) : Ω.T r = 0 := by
  by_contra hT
  have hm := Ω.Γ.hm
  have hsub : ({r, m - 1} : Finset ℕ) ⊆ (Finset.range m).filter (fun r => Ω.T r ≠ 0) := by
    intro x hx
    rw [Finset.mem_insert, Finset.mem_singleton] at hx
    rw [Finset.mem_filter, Finset.mem_range]
    rcases hx with rfl | rfl
    · exact ⟨by omega, hT⟩
    · exact ⟨by omega, ne_of_gt Ω.T_seam_pos⟩
  have hcard := Finset.card_le_card hsub
  rw [Finset.card_pair_eq_two_iff.mpr (by omega : r ≠ m - 1), ← Ω.J_eq, hJ] at hcard
  omega

/-- With `J = 1`, every sorted height is `hr 0 = 0`. -/
theorem hr_eq_zero_of_J_one (hJ : Ω.J = 1) {r : ℕ} (hr : r < m) : Ω.hr r = 0 := by
  induction r with
  | zero => exact Ω.hr_zero
  | succ r ih =>
    rw [(Ω.T_eq_zero_iff hr).mp (Ω.T_eq_zero_of_J_one hJ hr)]
    exact ih (by omega)

/-- With `J = 1`, the seam term is `2^B q`. -/
theorem T_seam_of_J_one (hJ : Ω.J = 1) : Ω.T (m - 1) = 2 ^ Ω.Γ.B * Ω.Γ.q := by
  have hm := Ω.Γ.hm
  unfold T offext
  rw [show m - 1 + 1 = m by omega, ite_eq_right (lt_irrefl m), Nat.sub_self,
    ite_eq_left (by omega : m - 1 < m)]
  unfold off
  rw [Ω.hr_zero, Nat.sub_zero, Ω.hr_eq_zero_of_J_one hJ (by omega : m - 1 < m), Nat.sub_zero]
  ring

/-- **S1-d**: for a reduced ordered cycle with a single forced position (`J = 1`), `D = q`: the
closed form at the run start after the seam reads `D Δ = 2^{E} 2^B q`, and `q ∣ D` with `D` odd
forces `D/q = 1`. This is R71's exact denominator (`gcd(C, D) = 1`) for such cycles, derived from
S1-a without the mechanical structure. -/
theorem D_eq_q_of_J_one (hred : IsCoprime Ω.Γ.q (Ω.Γ.n 0)) (hJ : Ω.J = 1) :
    (2 : ℤ) ^ Ω.Γ.Apre m - 3 ^ m = Ω.Γ.q := by
  have hm := Ω.Γ.hm
  have hm1 : m - 1 < m := by omega
  obtain ⟨r₁, hr₁⟩ : ∃ r₁, r₁ = Ω.orb (m - 1) 1 := ⟨_, rfl⟩
  have hr₁m : r₁ < m := by rw [hr₁]; exact Ω.orb_lt _ _
  have hpred : Ω.orb r₁ (m - 1) = m - 1 := by rw [hr₁]; exact Ω.orb_pred_succ hm1
  have hcf := Ω.gap_closed_form hr₁m
  have hsum : ∑ i ∈ Finset.range m, 3 ^ (m - 1 - i) * 2 ^ Ω.E r₁ i * Ω.T (Ω.orb r₁ i)
      = 2 ^ Ω.E r₁ (m - 1) * (2 ^ Ω.Γ.B * Ω.Γ.q) := by
    rw [Finset.sum_eq_single (m - 1)]
    · rw [hpred, Nat.sub_self, pow_zero, one_mul, Ω.T_seam_of_J_one hJ]
    · intro i hi hne
      have hT : Ω.T (Ω.orb r₁ i) = 0 := by
        apply Ω.T_eq_zero_of_J_one hJ
        have hlt := Ω.orb_lt r₁ i
        have hne' : Ω.orb r₁ i ≠ m - 1 := fun heq =>
          hne (Ω.orb_inj (Finset.mem_range.mp hi) hm1 (heq.trans hpred.symm))
        omega
      rw [hT, mul_zero]
    · intro h
      exact absurd (Finset.mem_range.mpr hm1) h
  rw [hsum] at hcf
  obtain ⟨D', hD'⟩ := Ω.Γ.q_dvd_D hred
  have hgpos : 0 < Ω.N.gap r₁ := Ω.N.gap_pos Ω.N_prim Ω.N_rank_zero hr₁m
  have hq0 : Ω.Γ.q ≠ 0 := Ω.Γ.hq.ne'
  have hkey : D' * Ω.N.gap r₁ = 2 ^ (Ω.E r₁ (m - 1) + Ω.Γ.B) := by
    rw [hD'] at hcf
    rw [pow_add]
    apply mul_left_cancel₀ hq0
    linear_combination hcf
  have hD'pos : 0 < D' := (mul_pos_iff_of_pos_right hgpos).mp (by rw [hkey]; positivity)
  have hA1 : 1 ≤ Ω.Γ.Apre m := by
    by_contra hA
    have hA0 : Ω.Γ.Apre m = 0 := by omega
    have hD := Ω.Γ.D_pos
    rw [hA0, pow_zero] at hD
    have h3 : (1 : ℤ) ≤ 3 ^ m := one_le_pow₀ (by norm_num)
    linarith
  have hDodd : IsCoprime (2 : ℤ) (2 ^ Ω.Γ.Apre m - 3 ^ m) := by
    rw [← Ω.Γ.D_word]
    exact isCoprime_two_D (by rw [Ω.Γ.word_sum]; exact hA1)
  have hD'2 : IsCoprime D' (2 ^ (Ω.E r₁ (m - 1) + Ω.Γ.B)) :=
    (hDodd.of_isCoprime_of_dvd_right (Dvd.intro_left _ hD'.symm)).symm.pow_right
  have hu : IsUnit D' := hD'2.isUnit_of_dvd' dvd_rfl (Dvd.intro _ hkey)
  have hD'1 : D' = 1 := by
    rcases Int.isUnit_iff.mp hu with h | h
    · exact h
    · omega
  rw [hD', hD'1, mul_one]

/-! #### S1-e: in band 1 with `m < A < 2m`, at least three forced positions

Side lane (feed 06:30, proved in prose): for an ordered cycle with positive letters, base exponent
`q' = 1` (equivalently `m < A < 2m`, the Collatz range) and heights in `{0, 1}` with some height
`1`, `J ≥ 3`. A non-wrapping step has `c = 1`, and `a_i = c_i + h_i − h_{i+1} ≥ 1` means the
height cannot rise on it; if `J = 2` the sorted heights were `0^k 1^{m−k}`, and the rank
`r* = max(0, k − s)` is low (`r* < m − s`), has height `0`, and its successor rank `r* + s ≥ k`
has height `1`: a zero letter. -/

/-- `hr` is constant on a stretch without adjacent changes. -/
theorem hr_eq_of_no_change (a d : ℕ) (hno : ∀ r, a ≤ r → r < a + d → Ω.hr (r + 1) = Ω.hr r) :
    Ω.hr (a + d) = Ω.hr a := by
  induction d with
  | zero => rfl
  | succ d ih =>
    rw [← Nat.add_assoc, hno (a + d) (Nat.le_add_right a d) (by omega)]
    exact ih (fun r hr1 hr2 => hno r hr1 (by omega))

/-- `q' = 1` is the Collatz range `m < A < 2m` (from `A = m q' + s`, `0 < s < m`). -/
theorem q'_eq_one_of_range (h1 : m < Ω.Γ.Apre m) (h2 : Ω.Γ.Apre m < 2 * m) : Ω.q' = 1 := by
  have hsum : ∑ i ∈ Finset.range m, Ω.N.a i = Ω.Γ.Apre m := by
    show ∑ i ∈ Finset.range m, Ω.Γ.c i = Ω.Γ.Apre m
    rw [Ω.Γ.sum_c]
    rfl
  have hA := Ω.N.sum_a
  rw [hsum, Ω.N_q] at hA
  have hs := Ω.numHigh_lt
  rcases Nat.lt_or_ge Ω.q' 1 with h0 | h0
  · have hz : Ω.q' = 0 := by omega
    rw [hz, Nat.mul_zero, Nat.zero_add] at hA
    omega
  · rcases Nat.lt_or_ge Ω.q' 2 with h1' | h2'
    · omega
    · have := Nat.mul_le_mul_left m h2'
      omega

/-- **S1-e**: an ordered cycle with positive letters, `q' = 1` and heights in `{0, 1}` with some
height `1` has at least three forced positions. -/
theorem J_ge_three (hapos : ∀ i, 1 ≤ Ω.Γ.a i) (hq' : Ω.q' = 1) (hB1 : ∀ i, Ω.Γ.h i ≤ 1)
    {j : ℕ} (hj : Ω.Γ.h j = 1) : 3 ≤ Ω.J := by
  have hm := Ω.Γ.hm
  have hs0 := Ω.numHigh_pos
  have hsm := Ω.numHigh_lt
  have hhr1 : ∀ r, Ω.hr r ≤ 1 := fun r => hB1 _
  have hj' : Ω.Γ.h (j % m) = 1 := by rw [Ω.Γ.h_mod]; exact hj
  obtain ⟨r₁, hr₁m, hr₁⟩ : ∃ r₁, r₁ < m ∧ Ω.hr r₁ = 1 :=
    ⟨Ω.N.rank (j % m), Ω.N.rank_lt _, by rw [Ω.hr_rank (Nat.mod_lt j hm)]; exact hj'⟩
  by_contra hJ
  rw [not_le] at hJ
  have hJc := Ω.J_eq_changes
  have hcard : ((Finset.range (m - 1)).filter (fun r => Ω.hr (r + 1) ≠ Ω.hr r)).card ≤ 1 := by
    omega
  have huniq := Finset.card_le_one.mp hcard
  -- a change below `r₁`
  have hex : ∃ r, r < r₁ ∧ Ω.hr (r + 1) ≠ Ω.hr r := by
    by_contra hno
    have hno' : ∀ r, r < r₁ → Ω.hr (r + 1) = Ω.hr r := fun r hr => by
      by_contra hne
      exact hno ⟨r, hr, hne⟩
    have := Ω.hr_eq_of_no_change 0 r₁ (fun r _ hr => hno' r (by omega))
    rw [Nat.zero_add, Ω.hr_zero] at this
    omega
  obtain ⟨r₀, hr₀, hch⟩ := hex
  have hr₀S : r₀ ∈ (Finset.range (m - 1)).filter (fun r => Ω.hr (r + 1) ≠ Ω.hr r) :=
    Finset.mem_filter.mpr ⟨Finset.mem_range.mpr (by omega), hch⟩
  -- the sorted heights are `0^k 1^(m−k)` with `k = r₀ + 1`
  have hlow : ∀ r, r ≤ r₀ → Ω.hr r = 0 := by
    intro r hr
    have := Ω.hr_eq_of_no_change 0 r (fun r' _ hr' => by
      by_contra hne
      have hmem : r' ∈ (Finset.range (m - 1)).filter (fun r => Ω.hr (r + 1) ≠ Ω.hr r) :=
        Finset.mem_filter.mpr ⟨Finset.mem_range.mpr (by omega), hne⟩
      have := huniq r' hmem r₀ hr₀S
      omega)
    rw [Nat.zero_add, Ω.hr_zero] at this
    exact this
  have hhigh : ∀ r, r₀ + 1 ≤ r → r < m → Ω.hr r = Ω.hr (r₀ + 1) := by
    intro r hr1 hr2
    have := Ω.hr_eq_of_no_change (r₀ + 1) (r - (r₀ + 1)) (fun r' hr' hr'' => by
      by_contra hne
      have hmem : r' ∈ (Finset.range (m - 1)).filter (fun r => Ω.hr (r + 1) ≠ Ω.hr r) :=
        Finset.mem_filter.mpr ⟨Finset.mem_range.mpr (by omega), hne⟩
      have := huniq r' hmem r₀ hr₀S
      omega)
    rw [show r₀ + 1 + (r - (r₀ + 1)) = r by omega] at this
    exact this
  have hk1 : Ω.hr (r₀ + 1) = 1 := by
    have h0 := hlow r₀ le_rfl
    have h1 := hhr1 (r₀ + 1)
    omega
  -- the low rank `r*` below `k` whose successor rank is at least `k`
  obtain ⟨r', hr'⟩ : ∃ r', r' = if Ω.N.numHigh ≤ r₀ + 1 then r₀ + 1 - Ω.N.numHigh else 0 :=
    ⟨_, rfl⟩
  have hr'k : r' < r₀ + 1 := by rw [hr']; split_ifs <;> omega
  have hr'low : r' + Ω.N.numHigh < m := by rw [hr']; split_ifs <;> omega
  have hr'succ : r₀ + 1 ≤ r' + Ω.N.numHigh := by rw [hr']; split_ifs <;> omega
  have hh0 : Ω.hr r' = 0 := hlow r' (by omega)
  have hh1 : Ω.hr (r' + Ω.N.numHigh) = 1 := by rw [hhigh _ hr'succ hr'low]; exact hk1
  -- its index, the successor index, and the zero letter
  obtain ⟨hi, hri⟩ := Ω.N.idx_spec Ω.N_prim (show r' < m by omega)
  have hrank1 : Ω.N.rank (Ω.N.idx r' + 1) = r' + Ω.N.numHigh := by
    rw [← Ω.orb_zero_eq_rank, Ω.orb_succ, Ω.orb_zero_eq_rank, hri]
    exact Nat.mod_eq_of_lt hr'low
  have hi1 : Ω.N.idx r' + 1 < m := by
    by_contra hge
    have heq : Ω.N.idx r' + 1 = m := by omega
    rw [heq, ← Ω.orb_zero_eq_rank, Ω.orb_m hm] at hrank1
    omega
  have hhi : Ω.Γ.h (Ω.N.idx r' + 1) = 1 := by
    rw [← Ω.hr_rank hi1, hrank1]
    exact hh1
  have hhi0 : Ω.Γ.h (Ω.N.idx r') = 0 := hh0
  have hc : Ω.Γ.c (Ω.N.idx r') = 1 := by
    have he := Ω.N.e_eq Ω.N_prim (show r' < m by omega)
    unfold NarrowCycle.e at he
    rw [ite_eq_right (by omega : ¬ (m - Ω.N.numHigh ≤ r')), Ω.N_q, hq'] at he
    exact he.symm
  have hca := hapos (Ω.N.idx r')
  unfold OddCycle.c at hc
  rw [hhi, hhi0] at hc
  omega

/-! #### C006-b: the `e_run` form of the run bound

C006's proof of (G1): along a zero-forcing run of length `t`, "multiplying (G3) yields
`2^{e_run} G_end = 3^t G_start`, where `e_run` is the sum of its rank exponents and
`e_run ≥ t`. Since `G_start` is a positive integer and `2` and `3` are coprime,
`G_start ≥ 2^{e_run} ≥ 2^t`", hence `L > 2^{e_run − B}` for each run. `run_bound` (C006-a) kept
only `2^t`; with S1-a's `gap_unroll` the exponent sum `e_run = E r₀ t` is exact. -/

/-- Along a zero-forcing run, `2^{e_run} ∣ Δ_{r₀}`, hence `2^{e_run} ≤ Δ_{r₀}`. -/
theorem run_bound_E {r₀ t : ℕ} (hr₀ : r₀ < m) (hrun : ∀ k, k < t → Ω.T (Ω.orb r₀ k) = 0) :
    (2 : ℤ) ^ Ω.E r₀ t ≤ Ω.N.gap r₀ := by
  have h := Ω.gap_unroll hr₀ t
  have hS : Ω.jsum r₀ t = 0 := by
    rw [Ω.jsum_eq_sum]
    apply Finset.sum_eq_zero
    intro i hi
    rw [hrun i (Finset.mem_range.mp hi), mul_zero]
  rw [hS, add_zero] at h
  have hdvd : (2 : ℤ) ^ Ω.E r₀ t ∣ 3 ^ t * Ω.N.gap r₀ := ⟨_, h.symm⟩
  have hcop : IsCoprime ((2 : ℤ) ^ Ω.E r₀ t) (3 ^ t) := by
    apply IsCoprime.pow
    exact ⟨-1, 1, by norm_num⟩
  exact Int.le_of_dvd (Ω.N.gap_pos Ω.N_prim Ω.N_rank_zero hr₀) (hcop.dvd_of_dvd_mul_left hdvd)

/-- C006's `L > 2^{e_run − B}`, cleared, for each zero-forcing run. -/
theorem run_bound_E_L {r₀ t : ℕ} (hr₀ : r₀ < m) (hrun : ∀ k, k < t → Ω.T (Ω.orb r₀ k) = 0) :
    (2 : ℤ) ^ Ω.E r₀ t < 2 ^ Ω.Γ.B * Ω.Γ.n 0 :=
  lt_of_le_of_lt (Ω.run_bound_E hr₀ hrun) (Ω.run_bound hr₀ hrun).2

/-- `e_run ≥ t`: every rank exponent is at least `1`. -/
theorem E_ge (r₀ t : ℕ) : t ≤ Ω.E r₀ t := by
  unfold E
  have hq : 1 ≤ Ω.N.q := Ω.q'_pos
  calc t = ∑ _k ∈ Finset.range t, 1 := by simp
    _ ≤ ∑ k ∈ Finset.range t, Ω.N.e (Ω.orb r₀ k) := by
      apply Finset.sum_le_sum
      intro k _
      unfold NarrowCycle.e
      split_ifs <;> omega

/-- (G1)'s first inequality in `e_run` form: some run of length `⌊(m−1)/J⌋` has
`2^{e_run} < 2^B L` with `e_run ≥ ⌊(m−1)/J⌋`. -/
theorem G1_first_E : ∃ r₀, r₀ < m ∧ (m - 1) / Ω.J ≤ Ω.E r₀ ((m - 1) / Ω.J) ∧
    (2 : ℤ) ^ Ω.E r₀ ((m - 1) / Ω.J) < 2 ^ Ω.Γ.B * Ω.Γ.n 0 := by
  obtain ⟨r₀, hr₀, hrun⟩ := Ω.exists_zero_run
  exact ⟨r₀, hr₀, Ω.E_ge r₀ _, Ω.run_bound_E_L hr₀ hrun⟩

/-! #### C006-d: (G2) conditional on an explicit linear-form gap

C006's (G2) imports `δ ≥ c₀ m^{−K₀}` from linear forms in two logarithms (Bugeaud/Matveev).
Here the import is an explicit hypothesis in the integer shape of the Collatz literature's
Böhm–Sontacchi gap bounds, `2^A ≤ 2^c m^μ (2^A − 3^m)` (the shape of mmusson/collatz's
`gap_all`, which claims `c = 172`, `μ = 341` unconditionally — read, not replayed here), and the
conclusion is (G2) cleared: `3 · 2^{⌊(m−1)/J⌋} < 2^{B+c} q m^{μ+1}`. Steps: `log x ≥ 1 − 1/x`
gives `δ ≥ (2^A − 3^m)/2^A`, so the gap gives `2^c m^μ δ ≥ 1`; (G4) gives `3Lδ ≤ mq`; (G1) gives
`2^{⌊(m−1)/J⌋} < 2^B L`. For Collatz (`q = 1`, `B ≤ 2`): `3 · 2^{⌊(m−1)/J⌋} < 2^{c+2} m^{μ+1}`,
i.e. `J > (m − 1)/(c + 3 + (μ+1) log₂ m)`. -/

/-- `δ ≥ (2^A − 3^m)/2^A`: `log x ≥ 1 − 1/x` at `x = 2^A/3^m`. -/
theorem delta_ge_gap :
    ((2 : ℝ) ^ Ω.Γ.Apre m - 3 ^ m) / 2 ^ Ω.Γ.Apre m ≤
      (Ω.Γ.Apre m : ℝ) * Real.log 2 - m * Real.log 3 := by
  have h2 : (0 : ℝ) < 2 ^ Ω.Γ.Apre m := by positivity
  have h3 : (0 : ℝ) < 3 ^ m := by positivity
  have hx : (0 : ℝ) < 2 ^ Ω.Γ.Apre m / 3 ^ m := div_pos h2 h3
  have hlog := Real.one_sub_inv_le_log_of_pos hx
  rw [Real.log_div h2.ne' h3.ne', Real.log_pow, Real.log_pow, inv_div] at hlog
  have heq : ((2 : ℝ) ^ Ω.Γ.Apre m - 3 ^ m) / 2 ^ Ω.Γ.Apre m = 1 - 3 ^ m / 2 ^ Ω.Γ.Apre m := by
    rw [sub_div, div_self h2.ne']
  rw [heq]
  exact hlog

/-- **(G2), conditional on an explicit linear-form gap**: if `2^A ≤ 2^c m^μ (2^A − 3^m)`, then
`3 · 2^{⌊(m−1)/J⌋} < 2^{B+c} q m^{μ+1}`. -/
theorem G2_of_gap {c μ : ℕ}
    (hgap : (2 : ℤ) ^ Ω.Γ.Apre m ≤ 2 ^ c * (m : ℤ) ^ μ * (2 ^ Ω.Γ.Apre m - 3 ^ m)) :
    (3 : ℤ) * 2 ^ ((m - 1) / Ω.J) < 2 ^ (Ω.Γ.B + c) * Ω.Γ.q * (m : ℤ) ^ (μ + 1) := by
  have hA : (0 : ℝ) < 2 ^ Ω.Γ.Apre m := by positivity
  have hgapR : (2 : ℝ) ^ Ω.Γ.Apre m ≤
      2 ^ c * (m : ℝ) ^ μ * (2 ^ Ω.Γ.Apre m - 3 ^ m) := by exact_mod_cast hgap
  have hδ := Ω.delta_ge_gap
  have hL := Ω.Γ.L_mul_delta_le
  have hG1R : (2 : ℝ) ^ ((m - 1) / Ω.J) < 2 ^ Ω.Γ.B * (Ω.Γ.n 0 : ℝ) := by
    exact_mod_cast Ω.G1_first
  have hn0 : (0 : ℝ) < Ω.Γ.n 0 := by exact_mod_cast Ω.Γ.npos
  have hkey : (1 : ℝ) ≤
      2 ^ c * (m : ℝ) ^ μ * ((Ω.Γ.Apre m : ℝ) * Real.log 2 - m * Real.log 3) := by
    have h1 : (1 : ℝ) ≤ 2 ^ c * (m : ℝ) ^ μ * ((2 ^ Ω.Γ.Apre m - 3 ^ m) / 2 ^ Ω.Γ.Apre m) := by
      rw [← mul_div_assoc]
      exact (one_le_div hA).mpr hgapR
    exact h1.trans (mul_le_mul_of_nonneg_left hδ (by positivity))
  have h3n : (0 : ℝ) ≤ 3 * (Ω.Γ.n 0 : ℝ) := by linarith
  have h3L : 3 * (Ω.Γ.n 0 : ℝ) ≤ 2 ^ c * Ω.Γ.q * (m : ℝ) ^ (μ + 1) := by
    calc 3 * (Ω.Γ.n 0 : ℝ) = 3 * (Ω.Γ.n 0 : ℝ) * 1 := by ring
      _ ≤ 3 * (Ω.Γ.n 0 : ℝ) *
          (2 ^ c * (m : ℝ) ^ μ * ((Ω.Γ.Apre m : ℝ) * Real.log 2 - m * Real.log 3)) :=
        mul_le_mul_of_nonneg_left hkey h3n
      _ = 2 ^ c * (m : ℝ) ^ μ *
          (3 * (Ω.Γ.n 0 : ℝ) * ((Ω.Γ.Apre m : ℝ) * Real.log 2 - m * Real.log 3)) := by ring
      _ ≤ 2 ^ c * (m : ℝ) ^ μ * ((m : ℝ) * Ω.Γ.q) := mul_le_mul_of_nonneg_left hL (by positivity)
      _ = 2 ^ c * Ω.Γ.q * (m : ℝ) ^ (μ + 1) := by ring
  have hfin : (3 : ℝ) * 2 ^ ((m - 1) / Ω.J) < 2 ^ (Ω.Γ.B + c) * Ω.Γ.q * (m : ℝ) ^ (μ + 1) := by
    calc (3 : ℝ) * 2 ^ ((m - 1) / Ω.J) < 3 * (2 ^ Ω.Γ.B * (Ω.Γ.n 0 : ℝ)) :=
          mul_lt_mul_of_pos_left hG1R (by norm_num)
      _ = 2 ^ Ω.Γ.B * (3 * (Ω.Γ.n 0 : ℝ)) := by ring
      _ ≤ 2 ^ Ω.Γ.B * (2 ^ c * Ω.Γ.q * (m : ℝ) ^ (μ + 1)) :=
          mul_le_mul_of_nonneg_left h3L (by positivity)
      _ = 2 ^ (Ω.Γ.B + c) * Ω.Γ.q * (m : ℝ) ^ (μ + 1) := by rw [pow_add]; ring
  exact_mod_cast hfin

/-- The Collatz instance (`q = 1`, `B ≤ 2`, the `H < 8L` band): `3 · 2^{⌊(m−1)/J⌋} < 2^{c+2} m^{μ+1}`. -/
theorem G2_of_gap_collatz {c μ : ℕ} (hq1 : Ω.Γ.q = 1) (hB : Ω.Γ.B ≤ 2)
    (hgap : (2 : ℤ) ^ Ω.Γ.Apre m ≤ 2 ^ c * (m : ℤ) ^ μ * (2 ^ Ω.Γ.Apre m - 3 ^ m)) :
    (3 : ℤ) * 2 ^ ((m - 1) / Ω.J) < 2 ^ (c + 2) * (m : ℤ) ^ (μ + 1) := by
  have h := Ω.G2_of_gap hgap
  rw [hq1, mul_one] at h
  have hpow : (2 : ℤ) ^ (Ω.Γ.B + c) ≤ 2 ^ (c + 2) := pow_le_pow_right₀ (by norm_num) (by omega)
  have hm : (0 : ℤ) ≤ (m : ℤ) ^ (μ + 1) := by positivity
  calc (3 : ℤ) * 2 ^ ((m - 1) / Ω.J) < 2 ^ (Ω.Γ.B + c) * (m : ℤ) ^ (μ + 1) := h
    _ ≤ 2 ^ (c + 2) * (m : ℤ) ^ (μ + 1) := mul_le_mul_of_nonneg_right hpow hm

/-! #### C006-e (continued): (G1)'s second inequality in C006's `C_c` form -/

/-- (G1)'s second inequality in C006's `C_c` form: `D · 2^{⌊(m−1)/J⌋} < 2^B q C_c`. -/
theorem G1_second_c :
    ((2 : ℤ) ^ Ω.Γ.Apre m - 3 ^ m) * 2 ^ ((m - 1) / Ω.J) < 2 ^ Ω.Γ.B * (Ω.Γ.q * Ω.Γ.Cc m) := by
  have hle : Ω.Γ.q * Ω.Γ.Cpre m ≤ Ω.Γ.q * Ω.Γ.Cc m :=
    mul_le_mul_of_nonneg_left (Ω.Γ.Cpre_le_Cc m) Ω.Γ.hq.le
  calc ((2 : ℤ) ^ Ω.Γ.Apre m - 3 ^ m) * 2 ^ ((m - 1) / Ω.J)
      < 2 ^ Ω.Γ.B * (Ω.Γ.q * Ω.Γ.Cpre m) := Ω.G1_second
    _ ≤ 2 ^ Ω.Γ.B * (Ω.Γ.q * Ω.Γ.Cc m) := mul_le_mul_of_nonneg_left hle (by positivity)

/-- C006's `q > (D/C_c) 2^{e_run − B}`, cleared: `D · 2^{e_run} < 2^B q C_c` for each
zero-forcing run. -/
theorem run_bound_c {r₀ t : ℕ} (hr₀ : r₀ < m) (hrun : ∀ k, k < t → Ω.T (Ω.orb r₀ k) = 0) :
    ((2 : ℤ) ^ Ω.Γ.Apre m - 3 ^ m) * 2 ^ Ω.E r₀ t < 2 ^ Ω.Γ.B * (Ω.Γ.q * Ω.Γ.Cc m) := by
  have hD := Ω.Γ.D_pos
  have h1 := Ω.run_bound_E_L hr₀ hrun
  have hle : Ω.Γ.q * Ω.Γ.Cpre m ≤ Ω.Γ.q * Ω.Γ.Cc m :=
    mul_le_mul_of_nonneg_left (Ω.Γ.Cpre_le_Cc m) Ω.Γ.hq.le
  calc ((2 : ℤ) ^ Ω.Γ.Apre m - 3 ^ m) * 2 ^ Ω.E r₀ t
      < ((2 : ℤ) ^ Ω.Γ.Apre m - 3 ^ m) * (2 ^ Ω.Γ.B * Ω.Γ.n 0) := mul_lt_mul_of_pos_left h1 hD
    _ = 2 ^ Ω.Γ.B * (((2 : ℤ) ^ Ω.Γ.Apre m - 3 ^ m) * Ω.Γ.n 0) := by ring
    _ = 2 ^ Ω.Γ.B * (Ω.Γ.q * Ω.Γ.Cpre m) := by rw [Ω.Γ.cycle_identity]
    _ ≤ 2 ^ Ω.Γ.B * (Ω.Γ.q * Ω.Γ.Cc m) := mul_le_mul_of_nonneg_left hle (by positivity)

/-! #### C006-f: the normalised word of every ordered cycle is the phase-`0` mechanical word

Side lane's observation on all 370 tested ordered cycles, and C005's order lemma: with the
minimum at rank `0` and ranks advancing by `s`, `c_i = q′ + ⌊(i+1)s/m⌋ − ⌊is/m⌋` (`a_formula`), so
the normalised word read from the minimum is `mech A m 0` with `A = Σ a_i = mq′ + s`, for every
ordered cycle at any `q`; `gcd(s, m) = 1` (`coprime_numHigh`) gives `gcd(A, m) = 1`, and R71-a
gives `gcd(C_c, D) = 1`. C006-e's `cword_eq_mech`/`Cc_gcd_one` needed `q = 1`, `B ≤ 2` only to
obtain the ordering through `three_band`. -/

/-- The letter formula on an ordered cycle: `c_i = q′ + ⌊(i+1)s/m⌋ − ⌊is/m⌋`. -/
theorem c_formula (i : ℕ) :
    Ω.Γ.c i = Ω.q' + (((i + 1) * Ω.N.numHigh) / m - (i * Ω.N.numHigh) / m) := by
  have h := Ω.N.a_formula Ω.numHigh_lt Ω.N_rank_zero i
  rw [Ω.N_q] at h
  exact h

/-- `A = m q′ + s` on an ordered cycle. -/
theorem Apre_eq_ord : Ω.Γ.Apre m = m * Ω.q' + Ω.N.numHigh := by
  have h := Ω.N.sum_a
  rw [Ω.N_q] at h
  have hsum : ∑ i ∈ Finset.range m, Ω.N.a i = Ω.Γ.Apre m := by
    show ∑ i ∈ Finset.range m, Ω.Γ.c i = Ω.Γ.Apre m
    rw [Ω.Γ.sum_c]
    rfl
  rw [← hsum]
  exact h

/-- **C005's order lemma, word form**: the normalised word of an ordered cycle, read from the
minimum, is the phase-`0` mechanical word of total `A`, at any `q`. -/
theorem cword_eq_mech_ord : (List.range m).map Ω.Γ.c = mech (Ω.Γ.Apre m) m 0 := by
  have hm := Ω.Γ.hm
  have hA := Ω.Apre_eq_ord
  unfold mech diffWord
  apply List.map_congr_left
  intro j _
  show Ω.Γ.c j = ((j + 1) * Ω.Γ.Apre m) / m - (j * Ω.Γ.Apre m) / m
  rw [Ω.c_formula j, hA,
    show (j + 1) * (m * Ω.q' + Ω.N.numHigh) = m * ((j + 1) * Ω.q') + (j + 1) * Ω.N.numHigh by ring,
    show j * (m * Ω.q' + Ω.N.numHigh) = m * (j * Ω.q') + j * Ω.N.numHigh by ring,
    Nat.mul_add_div hm, Nat.mul_add_div hm, show (j + 1) * Ω.q' = j * Ω.q' + Ω.q' by ring]
  have hmono : j * Ω.N.numHigh / m ≤ (j + 1) * Ω.N.numHigh / m :=
    Nat.div_le_div_right (Nat.mul_le_mul_right Ω.N.numHigh (Nat.le_succ j))
  rw [Nat.add_assoc (j * Ω.q'), Nat.add_sub_add_left, Nat.add_sub_assoc hmono]

/-- `gcd(A, m) = 1` for every ordered cycle, from `gcd(s, m) = 1`. -/
theorem coprime_Apre : Nat.Coprime (Ω.Γ.Apre m) m := by
  rw [Ω.Apre_eq_ord, Nat.add_comm, Nat.coprime_add_mul_left_left]
  exact Ω.N.coprime_numHigh Ω.N_prim Ω.hm2

/-- R71-a on every ordered cycle: `gcd(C_c, D) = 1` (positive letters give `m ≤ A`). -/
theorem Cc_gcd_one_ord (hapos : ∀ i, 1 ≤ Ω.Γ.a i) :
    Int.gcd (Ω.Γ.Cc m) ((2 : ℤ) ^ Ω.Γ.Apre m - 3 ^ m) = 1 := by
  have hm := Ω.Γ.hm
  have hAm : m ≤ Ω.Γ.Apre m := by
    unfold OddCycle.Apre
    calc m = ∑ _i ∈ Finset.range m, 1 := by simp
      _ ≤ ∑ i ∈ Finset.range m, Ω.Γ.a i := Finset.sum_le_sum (fun i _ => hapos i)
  have hC : Ω.Γ.Cc m = C (mech (Ω.Γ.Apre m) m 0) := by
    rw [← Ω.cword_eq_mech_ord]
    exact (Ω.Γ.cword_prefix m).2.symm
  rw [hC, ← D_mech hm (Ω.Γ.Apre m) 0 hm]
  exact mech_gcd_one Ω.hm2 (Ω.Γ.Apre m) hAm Ω.coprime_Apre

/-! #### C010-b (continued): the sorted scaled states and their complete gaps have gcd `1` -/

/-- The sorted gaps of C006 are the complete gaps `UZ` of the sorted scaled states. -/
theorem gap_eq_cgap {r : ℕ} (hr : r < m) : Ω.N.gap r = cgap Ω.N.y m r := by
  unfold NarrowCycle.gap NarrowCycle.yext cgap
  rcases Nat.lt_or_ge (r + 1) m with h1 | h1
  · rw [ite_eq_left h1, ite_eq_left hr, ite_eq_left h1]
  · have hr1 : r + 1 = m := by omega
    rw [ite_eq_right (by omega : ¬ (r + 1 < m)), ite_eq_left hr,
      ite_eq_right (by omega : ¬ (r + 1 < m)), hr1, Nat.sub_self]

/-- C010 §2 on an ordered cycle: the scaled states have gcd `1` (the `OddCycle` statement
`OddCycle.Z_dvd_isUnit` of C010-c needs no ordering). -/
theorem Z_dvd_isUnit (hred : IsCoprime Ω.Γ.q (Ω.Γ.n 0)) (hB : ∃ i, Ω.Γ.h i = Ω.Γ.B) {d : ℤ}
    (hd : ∀ i, d ∣ Ω.Γ.Z i) : IsUnit d :=
  Ω.Γ.Z_dvd_isUnit hred hB hd

/-- C010 §2: the complete gap vector of the sorted scaled states has gcd `1` as well. -/
theorem gap_dvd_isUnit (hred : IsCoprime Ω.Γ.q (Ω.Γ.n 0)) (hB : ∃ i, Ω.Γ.h i = Ω.Γ.B) {d : ℤ}
    (hd : ∀ r, r < m → d ∣ Ω.N.gap r) : IsUnit d := by
  have hy : ∀ i, i < m → d ∣ Ω.N.y i := by
    rw [← dvd_cgap_iff Ω.N.y Ω.Γ.hm d]
    intro j hj
    rw [← Ω.gap_eq_cgap hj]
    exact hd j hj
  apply Ω.Z_dvd_isUnit hred hB
  intro i
  have hi : i % m < m := Nat.mod_lt i Ω.Γ.hm
  have hidx : Ω.N.idx (Ω.N.rank (i % m)) = i % m :=
    Ω.N.rank_inj Ω.N_prim (Ω.N.idx_spec Ω.N_prim (Ω.N.rank_lt _)).1 hi
      (Ω.N.idx_spec Ω.N_prim (Ω.N.rank_lt _)).2
  have hZ : Ω.Γ.Z i = Ω.N.y (Ω.N.rank (i % m)) := by
    unfold NarrowCycle.y
    rw [hidx, Ω.N_x]
    unfold OddCycle.Z
    rw [Ω.Γ.h_mod, Ω.Γ.n_mod]
  rw [hZ]
  exact hy _ (Ω.N.rank_lt _)

/-! #### S2-a (pre-emptive, for the side lane's S2 "renormalisation of ordered cycles"): the exact
run-start recursion

For a run start `r₀` with `t` zero-forcing steps (`T(orb r₀ k) = 0` for `k < t`) and the forced step
at `orb r₀ t`: `2^{E_t} ∣ Δ_{r₀}` (`run_dvd`, the divisibility inside C006-b's `run_bound_E`); the
run law in quotient form `Δ_{orb r₀ t} = 3^t (Δ_{r₀}/2^{E_t})` (`run_end_eq`); the exact recursion
`2^{e_t} Δ_{orb r₀ (t+1)} = 3^{t+1} (Δ_{r₀}/2^{E_t}) + T(orb r₀ t)` (`run_start_rec`, S1's
`gap_unroll` at `n = t+1`); its two-run form `2^{e_t + E′} u′ = 3^{t+1} u + T(orb r₀ t)` with
`u = Δ_{r₀}/2^{E_t}` and `u′ = Δ_{r₁}/2^{E′}` for the next run start `r₁ = orb r₀ (t+1)` with `t′`
zero-forcing steps (`run_start_rec_two`); the oddness criterion `Odd u ↔ ¬ 2^{E_t+1} ∣ Δ_{r₀}`
(`run_quot_odd_iff`: S1 gives only `2^{E_t} ∣ Δ_{r₀}`, so "odd parts" is an extra condition); the
additivity of `E` along the orbit (`E_add`, for the product bookkeeping `Π 2^{E′} = 2^A`); the gap
sum `Σ_{r<m} Δ_r = 2^B L` (`sum_gap_eq_lo`); and the all-run-starts bound `Σ_{r ∈ R} 2^{E_r} ≤ 2^B L`
for any set `R` of run starts (`sum_run_bound`, the integer part of the side remark). -/

theorem jsum_run {r₀ t : ℕ} (hrun : ∀ k, k < t → Ω.T (Ω.orb r₀ k) = 0) : Ω.jsum r₀ t = 0 := by
  rw [Ω.jsum_eq_sum]
  apply Finset.sum_eq_zero
  intro i hi
  rw [hrun i (Finset.mem_range.mp hi), mul_zero]

/-- The run divisibility: `2^{E_t}` divides the run-start gap. -/
theorem run_dvd {r₀ t : ℕ} (hr₀ : r₀ < m) (hrun : ∀ k, k < t → Ω.T (Ω.orb r₀ k) = 0) :
    (2 : ℤ) ^ Ω.E r₀ t ∣ Ω.N.gap r₀ := by
  have h := Ω.gap_unroll hr₀ t
  rw [Ω.jsum_run hrun, add_zero] at h
  have hdvd : (2 : ℤ) ^ Ω.E r₀ t ∣ 3 ^ t * Ω.N.gap r₀ := ⟨_, h.symm⟩
  have hcop : IsCoprime ((2 : ℤ) ^ Ω.E r₀ t) (3 ^ t) := IsCoprime.pow ⟨-1, 1, by norm_num⟩
  exact hcop.dvd_of_dvd_mul_left hdvd

/-- The run law in quotient form: `Δ_{orb r₀ t} = 3^t (Δ_{r₀}/2^{E_t})`. -/
theorem run_end_eq {r₀ t : ℕ} (hr₀ : r₀ < m) (hrun : ∀ k, k < t → Ω.T (Ω.orb r₀ k) = 0) :
    Ω.N.gap (Ω.orb r₀ t) = 3 ^ t * (Ω.N.gap r₀ / 2 ^ Ω.E r₀ t) := by
  have h := Ω.gap_unroll hr₀ t
  rw [Ω.jsum_run hrun, add_zero] at h
  obtain ⟨u, hu⟩ := Ω.run_dvd hr₀ hrun
  have h2 : (0 : ℤ) < 2 ^ Ω.E r₀ t := by positivity
  rw [hu, Int.mul_ediv_cancel_left _ h2.ne']
  rw [hu] at h
  have h3 : (2 : ℤ) ^ Ω.E r₀ t * Ω.N.gap (Ω.orb r₀ t) = 2 ^ Ω.E r₀ t * (3 ^ t * u) := by
    rw [h]
    ring
  exact mul_left_cancel₀ h2.ne' h3

theorem orb_succ_eq (r₀ t : ℕ) : (Ω.orb r₀ t + Ω.N.numHigh) % m = Ω.orb r₀ (t + 1) := by
  rw [← Ω.orb_add r₀ t 1]
  unfold orb
  rw [one_mul]

/-- The exact run-start recursion (the side lane's S2 identity (a)):
`2^{e_t} Δ_{orb r₀ (t+1)} = 3^{t+1} (Δ_{r₀}/2^{E_t}) + T(orb r₀ t)`. -/
theorem run_start_rec {r₀ t : ℕ} (hr₀ : r₀ < m) (hrun : ∀ k, k < t → Ω.T (Ω.orb r₀ k) = 0) :
    (2 : ℤ) ^ Ω.N.e (Ω.orb r₀ t) * Ω.N.gap (Ω.orb r₀ (t + 1)) =
      3 ^ (t + 1) * (Ω.N.gap r₀ / 2 ^ Ω.E r₀ t) + Ω.T (Ω.orb r₀ t) := by
  have h := Ω.gap_rec (Ω.orb_lt r₀ t)
  rw [Ω.orb_succ_eq, Ω.run_end_eq hr₀ hrun] at h
  rw [h]
  ring

/-- The two-run form of S2's identity: with `u = Δ_{r₀}/2^{E_t}` and `u′ = Δ_{r₁}/2^{E′}` for the
next run start `r₁ = orb r₀ (t+1)` with `t′` zero-forcing steps,
`2^{e_t + E′} u′ = 3^{t+1} u + T(orb r₀ t)`. -/
theorem run_start_rec_two {r₀ t t' : ℕ} (hr₀ : r₀ < m)
    (hrun : ∀ k, k < t → Ω.T (Ω.orb r₀ k) = 0)
    (hrun' : ∀ k, k < t' → Ω.T (Ω.orb (Ω.orb r₀ (t + 1)) k) = 0) :
    (2 : ℤ) ^ (Ω.N.e (Ω.orb r₀ t) + Ω.E (Ω.orb r₀ (t + 1)) t') *
        (Ω.N.gap (Ω.orb r₀ (t + 1)) / 2 ^ Ω.E (Ω.orb r₀ (t + 1)) t') =
      3 ^ (t + 1) * (Ω.N.gap r₀ / 2 ^ Ω.E r₀ t) + Ω.T (Ω.orb r₀ t) := by
  have h := Ω.run_start_rec hr₀ hrun
  obtain ⟨u', hu'⟩ := Ω.run_dvd (Ω.orb_lt r₀ (t + 1)) hrun'
  have h2 : (0 : ℤ) < 2 ^ Ω.E (Ω.orb r₀ (t + 1)) t' := by positivity
  rw [hu', Int.mul_ediv_cancel_left _ h2.ne', pow_add]
  rw [hu'] at h
  rw [← h]
  ring

/-- `u = Δ_{r₀}/2^{E_t}` is odd iff the run-start gap has 2-adic valuation exactly `E_t`. -/
theorem run_quot_odd_iff {r₀ t : ℕ} (hr₀ : r₀ < m) (hrun : ∀ k, k < t → Ω.T (Ω.orb r₀ k) = 0) :
    Odd (Ω.N.gap r₀ / 2 ^ Ω.E r₀ t) ↔ ¬ (2 : ℤ) ^ (Ω.E r₀ t + 1) ∣ Ω.N.gap r₀ := by
  obtain ⟨u, hu⟩ := Ω.run_dvd hr₀ hrun
  have h2 : (0 : ℤ) < 2 ^ Ω.E r₀ t := by positivity
  rw [hu, Int.mul_ediv_cancel_left _ h2.ne', pow_succ, mul_dvd_mul_iff_left h2.ne',
    ← Int.not_even_iff_odd, even_iff_two_dvd]

/-- `E` is additive along the orbit: `E r₀ (a + b) = E r₀ a + E (orb r₀ a) b`. -/
theorem E_add (r₀ a b : ℕ) : Ω.E r₀ (a + b) = Ω.E r₀ a + Ω.E (Ω.orb r₀ a) b := by
  unfold E
  rw [Finset.sum_range_add]
  congr 1
  apply Finset.sum_congr rfl
  intro k _
  rw [Ω.orb_add]

/-- The gap sum: `Σ_{r<m} Δ_r = Z_0 = 2^B L` (C010-b's `sum_cgap` on the sorted states). -/
theorem sum_gap_eq_lo : ∑ r ∈ Finset.range m, Ω.N.gap r = Ω.Γ.lo := by
  rw [Ω.N.sum_gap Ω.N_prim Ω.N_rank_zero, Ω.N_x]
  unfold OddCycle.Z OddCycle.lo
  rw [Ω.Γ.h_zero, Nat.sub_zero]

/-- The all-run-starts bound: for any set `R` of run starts with run lengths `t r`,
`Σ_{r ∈ R} 2^{E_r} ≤ Σ_{r ∈ R} Δ_r ≤ Σ_{r<m} Δ_r = 2^B L`. -/
theorem sum_run_bound (R : Finset ℕ) (hR : ∀ r ∈ R, r < m) (t : ℕ → ℕ)
    (hrun : ∀ r ∈ R, ∀ k, k < t r → Ω.T (Ω.orb r k) = 0) :
    ∑ r ∈ R, (2 : ℤ) ^ Ω.E r (t r) ≤ Ω.Γ.lo := by
  calc ∑ r ∈ R, (2 : ℤ) ^ Ω.E r (t r) ≤ ∑ r ∈ R, Ω.N.gap r :=
        Finset.sum_le_sum (fun r hr => Ω.run_bound_E (hR r hr) (hrun r hr))
    _ ≤ ∑ r ∈ Finset.range m, Ω.N.gap r := by
        apply Finset.sum_le_sum_of_subset_of_nonneg
        · intro r hr
          exact Finset.mem_range.mpr (hR r hr)
        · intro r hr _
          exact (Ω.N.gap_pos Ω.N_prim Ω.N_rank_zero (Finset.mem_range.mp hr)).le
    _ = Ω.Γ.lo := Ω.sum_gap_eq_lo

/-! #### S2-b (part 2): the oddness rule of the side lane's S2 §2

`u = Δ_{r₀}/2^{E_t}` is odd iff the gap at the run's forced rank is odd (`run_quot_odd_iff_end`,
from the run law `Δ_{orb r₀ t} = 3^t u`); a sorted state is odd iff its height is `B` (`y_odd_iff`);
an interior gap is odd iff exactly one of its two heights equals `B` (`gap_odd_iff`); the seam gap
`2 y_0 − y_{m−1}` is odd iff the top sorted height is `B` (`gap_seam_odd_iff`); interior forcing is a
change of height (`T_ne_zero_iff`); hence in band `1` every run ending at an interior forced rank
has odd `u` (`band1_u_odd`), and a seam-ending run has odd `u` iff the top sorted height is `B`
(`seam_u_odd_iff`). -/

/-- `u = Δ_{r₀}/2^{E_t}` is odd iff the gap at the forced rank `orb r₀ t` is odd. -/
theorem run_quot_odd_iff_end {r₀ t : ℕ} (hr₀ : r₀ < m)
    (hrun : ∀ k, k < t → Ω.T (Ω.orb r₀ k) = 0) :
    Odd (Ω.N.gap r₀ / 2 ^ Ω.E r₀ t) ↔ Odd (Ω.N.gap (Ω.orb r₀ t)) := by
  rw [Ω.run_end_eq hr₀ hrun, Int.odd_mul]
  constructor
  · intro h
    exact ⟨Odd.pow ⟨1, by norm_num⟩, h⟩
  · intro h
    exact h.2

/-- The sorted state of rank `r` is odd iff its height is `B`. -/
theorem y_odd_iff (r : ℕ) : Odd (Ω.N.y r) ↔ Ω.hr r = Ω.Γ.B := by
  unfold NarrowCycle.y hr
  rw [Ω.N_x]
  exact Ω.Γ.Z_odd_iff _

/-- S2 §2: an interior gap is odd iff exactly one of its two heights equals `B`. -/
theorem gap_odd_iff {r : ℕ} (hr1 : r + 1 < m) :
    Odd (Ω.N.gap r) ↔ (Ω.hr (r + 1) = Ω.Γ.B ↔ ¬ Ω.hr r = Ω.Γ.B) := by
  unfold NarrowCycle.gap
  rw [Ω.N.yext_of_lt hr1, Ω.N.yext_of_lt (by omega), Int.odd_sub, Ω.y_odd_iff,
    ← Int.not_odd_iff_even, Ω.y_odd_iff]

/-- S2 §2: the seam gap `2 y_0 − y_{m−1}` is odd iff the top sorted height is `B`. -/
theorem gap_seam_odd_iff : Odd (Ω.N.gap (m - 1)) ↔ Ω.hr (m - 1) = Ω.Γ.B := by
  have hm := Ω.Γ.hm
  have h2 : ¬ Odd (2 * Ω.N.y 0) := Int.not_odd_iff_even.mpr (even_two_mul _)
  unfold NarrowCycle.gap
  rw [show m - 1 + 1 = m by omega, Ω.N.yext_m, Ω.N.yext_of_lt (by omega), Int.odd_sub,
    ← Ω.y_odd_iff]
  constructor
  · intro h
    by_contra hno
    exact h2 (h.mpr (Int.not_odd_iff_even.mp hno))
  · intro ho
    exact ⟨fun h => absurd h h2, fun he => absurd ho (Int.not_odd_iff_even.mpr he)⟩

/-- Interior forcing is exactly a change of height between consecutive ranks. -/
theorem T_ne_zero_iff {r : ℕ} (hr1 : r + 1 < m) : Ω.T r ≠ 0 ↔ Ω.hr r ≠ Ω.hr (r + 1) := by
  unfold T offext
  rw [ite_eq_left hr1, ite_eq_left (by omega : r < m)]
  unfold off
  constructor
  · intro h heq
    apply h
    rw [heq]
    ring
  · intro hne h0
    apply hne
    have hq := Ω.Γ.hq
    have h1 : (2 : ℤ) ^ (Ω.Γ.B - Ω.hr (r + 1)) * Ω.Γ.q = 2 ^ (Ω.Γ.B - Ω.hr r) * Ω.Γ.q := by
      linarith
    have h2 := mul_right_cancel₀ hq.ne' h1
    have h3 : Ω.Γ.B - Ω.hr (r + 1) = Ω.Γ.B - Ω.hr r :=
      Nat.pow_right_injective (le_refl 2) (by exact_mod_cast h2)
    have hb1 := Ω.hr_le_B r
    have hb2 := Ω.hr_le_B (r + 1)
    omega

/-- S2 §2, band `1`: a run ending at an interior forced rank has odd `u` (the two heights differ
and both are at most `1`, so exactly one equals `B = 1`). -/
theorem band1_u_odd (hB1 : Ω.Γ.B = 1) {r₀ t : ℕ} (hr₀ : r₀ < m)
    (hrun : ∀ k, k < t → Ω.T (Ω.orb r₀ k) = 0) (hint : Ω.orb r₀ t + 1 < m)
    (hT : Ω.T (Ω.orb r₀ t) ≠ 0) : Odd (Ω.N.gap r₀ / 2 ^ Ω.E r₀ t) := by
  rw [Ω.run_quot_odd_iff_end hr₀ hrun, Ω.gap_odd_iff hint]
  have hne := (Ω.T_ne_zero_iff hint).mp hT
  have h1 := Ω.hr_le_B (Ω.orb r₀ t)
  have h2 := Ω.hr_le_B (Ω.orb r₀ t + 1)
  rw [hB1] at h1 h2 ⊢
  constructor <;> intro h <;> omega

/-- S2 §2: a run ending at the seam has odd `u` iff the top sorted height is `B`. -/
theorem seam_u_odd_iff {r₀ t : ℕ} (hr₀ : r₀ < m) (hrun : ∀ k, k < t → Ω.T (Ω.orb r₀ k) = 0)
    (hseam : Ω.orb r₀ t = m - 1) :
    Odd (Ω.N.gap r₀ / 2 ^ Ω.E r₀ t) ↔ Ω.hr (m - 1) = Ω.Γ.B := by
  rw [Ω.run_quot_odd_iff_end hr₀ hrun, hseam, Ω.gap_seam_odd_iff]

/-! #### S2-c: the orbit exponent density `E ≥ ⌊tA/m⌋` (the side lane's corrected S2 §4)

Along the rank orbit `r ↦ (r + s) % m` (`s = numHigh`) a wrap happens exactly at a high rank
(`r ≥ m − s`), where the exponent is `q′ + 1` instead of `q′`; `t` steps from `r₀` wrap
`⌊(r₀ + ts)/m⌋ − ⌊r₀/m⌋` times (`div_succ_step`), so `E r₀ t + ⌊r₀/m⌋ = t q′ + ⌊(r₀ + ts)/m⌋`
(`E_eq_div`) and, for `r₀ < m`, `E r₀ t ≥ ⌊t·A/m⌋` with `A = m q′ + s` (`E_ge_mul_div`), a
strengthening of C006-b's `E_ge` (`t ≤ E`) by the factor `A/m`. Applied to the pigeonhole run of
length `⌊(m−1)/J⌋` it gives (G1)'s first inequality with the density (`G1_first_E_density`). -/

/-- One orbit step adds `1` to the quotient `⌊(r₀ + ks)/m⌋` exactly at a high rank. -/
theorem div_succ_step (r₀ k : ℕ) :
    (r₀ + (k + 1) * Ω.N.numHigh) / m =
      (r₀ + k * Ω.N.numHigh) / m + (if m - Ω.N.numHigh ≤ Ω.orb r₀ k then 1 else 0) := by
  have hm := Ω.Γ.hm
  have hs := Ω.numHigh_lt
  have hmd := Nat.mod_add_div (r₀ + k * Ω.N.numHigh) m
  have hX1 : r₀ + (k + 1) * Ω.N.numHigh =
      (r₀ + k * Ω.N.numHigh) % m + Ω.N.numHigh + m * ((r₀ + k * Ω.N.numHigh) / m) := by
    rw [Nat.add_mul, one_mul]
    omega
  rw [hX1, Nat.add_mul_div_left _ _ hm]
  unfold orb
  have hr : (r₀ + k * Ω.N.numHigh) % m < m := Nat.mod_lt _ hm
  split_ifs with h
  · have hpos : 0 < ((r₀ + k * Ω.N.numHigh) % m + Ω.N.numHigh) / m :=
      Nat.div_pos (by omega) hm
    have hlt : ((r₀ + k * Ω.N.numHigh) % m + Ω.N.numHigh) / m < 2 :=
      Nat.div_lt_of_lt_mul (by omega)
    omega
  · rw [Nat.div_eq_of_lt (by omega)]
    omega

/-- `E r₀ t + ⌊r₀/m⌋ = t q′ + ⌊(r₀ + ts)/m⌋`: the exponent total counts the wraps. -/
theorem E_eq_div (r₀ t : ℕ) :
    Ω.E r₀ t + r₀ / m = t * Ω.q' + (r₀ + t * Ω.N.numHigh) / m := by
  induction t with
  | zero => simp [E]
  | succ t ih =>
    rw [Ω.E_succ, Ω.div_succ_step, Nat.add_mul, one_mul]
    unfold NarrowCycle.e
    rw [Ω.N_q]
    split_ifs <;> omega

/-- S2 §4 (corrected): `E r₀ t ≥ ⌊t·A/m⌋` for every run start `r₀ < m` and length `t`. -/
theorem E_ge_mul_div {r₀ : ℕ} (hr₀ : r₀ < m) (t : ℕ) : t * Ω.Γ.Apre m / m ≤ Ω.E r₀ t := by
  have hm := Ω.Γ.hm
  have h := Ω.E_eq_div r₀ t
  rw [Nat.div_eq_of_lt hr₀, Nat.add_zero] at h
  rw [Ω.Apre_eq_ord, Nat.mul_add, ← Nat.mul_assoc, Nat.mul_comm t m, Nat.mul_assoc,
    Nat.mul_add_div hm, h]
  have hle : t * Ω.N.numHigh / m ≤ (r₀ + t * Ω.N.numHigh) / m :=
    Nat.div_le_div_right (Nat.le_add_left _ _)
  omega

/-- (G1)'s first inequality with the density: some zero-forcing run of length `⌊(m−1)/J⌋` has
`2^E < 2^B L` with `E ≥ ⌊⌊(m−1)/J⌋·A/m⌋`. -/
theorem G1_first_E_density : ∃ r₀, r₀ < m ∧
    (m - 1) / Ω.J * Ω.Γ.Apre m / m ≤ Ω.E r₀ ((m - 1) / Ω.J) ∧
    (2 : ℤ) ^ Ω.E r₀ ((m - 1) / Ω.J) < 2 ^ Ω.Γ.B * Ω.Γ.n 0 := by
  obtain ⟨r₀, hr₀, hrun⟩ := Ω.exists_zero_run
  exact ⟨r₀, hr₀, Ω.E_ge_mul_div hr₀ _, Ω.run_bound_E_L hr₀ hrun⟩

end OrdCycle

end Cyc
end LeanLane
