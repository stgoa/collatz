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
