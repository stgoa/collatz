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

/-- **C002's (U1).** Two distinct positive words `u ≠ v` of the same length `m` and total
`A`, with `2^A > 3^m`, and `k, ℓ ≥ 1`, `k + ℓ ≥ 3`: the reduced denominator of
`u^k v^ℓ` exceeds `2^m`, i.e. `2^m · gcd(C, D) < D`. -/
theorem uniform_two_block (u v : List ℕ) (hu : ∀ a ∈ u, 1 ≤ a) (hv : ∀ a ∈ v, 1 ≤ a)
    (hu0 : u ≠ []) (huv : u ≠ v) (hlen : u.length = v.length) (hsum : u.sum = v.sum)
    (hUV : (3 : ℤ) ^ u.length < 2 ^ u.sum) (k l : ℕ) (hk : 1 ≤ k) (hl : 1 ≤ l)
    (hn : 3 ≤ k + l) :
    (2 : ℤ) ^ u.length * (Int.gcd (C (rep u k ++ rep v l)) (D (rep u k ++ rep v l)) : ℤ)
      < D (rep u k ++ rep v l) := by
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
  have hU2 : (2 : ℤ) ^ u.sum * 2 ^ u.sum ≤ ((2 : ℤ) ^ u.sum) ^ (k + l - Nat.gcd k l) := by
    rw [← pow_two]
    exact pow_le_pow_right₀ (one_le_pow₀ (by norm_num)) (by omega)
  calc (2 : ℤ) ^ u.length * ((Int.gcd (C (rep u k ++ rep v l)) (D (rep u k ++ rep v l)) : ℕ) : ℤ)
      ≤ 2 ^ u.length * (|C v - C u|
          * (((2 : ℤ) ^ u.sum) ^ Nat.gcd k l - (3 ^ u.length) ^ Nat.gcd k l)) :=
        mul_le_mul_of_nonneg_left hg_le h2m.le
    _ = (2 ^ u.length * |C v - C u|)
          * (((2 : ℤ) ^ u.sum) ^ Nat.gcd k l - (3 ^ u.length) ^ Nat.gcd k l) := by ring
    _ < (2 ^ u.sum * 3 ^ u.length)
          * (((2 : ℤ) ^ u.sum) ^ Nat.gcd k l - (3 ^ u.length) ^ Nat.gcd k l) :=
        mul_lt_mul_of_pos_right hJbound hHh
    _ < (2 ^ u.sum * 2 ^ u.sum)
          * (((2 : ℤ) ^ u.sum) ^ Nat.gcd k l - (3 ^ u.length) ^ Nat.gcd k l) := by
        apply mul_lt_mul_of_pos_right _ hHh
        exact mul_lt_mul_of_pos_left hUV (by positivity)
    _ ≤ ((2 : ℤ) ^ u.sum) ^ (k + l - Nat.gcd k l)
          * (((2 : ℤ) ^ u.sum) ^ Nat.gcd k l - (3 ^ u.length) ^ Nat.gcd k l) :=
        mul_le_mul_of_nonneg_right hU2 hHh.le
    _ < ((2 : ℤ) ^ u.sum) ^ (k + l) - (3 ^ u.length) ^ (k + l) := hlow
    _ = D (rep u k ++ rep v l) := hDw.symm

end Cyc
end LeanLane
