import Mathlib

/-!
# Ternary closure of the positive-offset binary kernel (V004-ii)

Lane: `claude/lean-lane`. Prose source: main's
`experiments/viewpoints/V004/GLOBAL_RIGIDITY.md`, §§2–3.

For a colouring `h : ℕ → α` with `h (2n) = h n` for all `n` and
`h (3n+1) = h n` for all odd `n > 1`, consider the sections
`n ↦ h (2^a n + r)` with `a ≥ 1` and `0 < r < 2^a` (V004's family `K₊`).
Taking a ternary section (`n ↦ 3n + j`, `j < 3`) of such a section gives
again a member of the family: `kernel_ternary_closure` produces `a' ≥ 1` and
`0 < r' < 2^a'` with `h (2^a (3n+j) + r) = h (2^a' n + r')` for every `n`.
Binary sections stay in the family trivially (`kernel_binary_closure`).

This is the elementary identity content of V004 §3. Combined with the
finiteness of the binary kernel of a binary-automatic `h` (so that `K₊` is
finite) and Cobham's theorem, it is what makes `n ↦ h (2n+1)` eventually
periodic; those two external inputs are not formalised here. Nothing in this
file concerns convergence of orbits.
-/

namespace LeanLane
namespace Kernel

variable {α : Type*} (h : ℕ → α)

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

/-- V004 (3): `h (3u) = h (16u+1)` for odd `u`. -/
theorem id3 (hdbl : ∀ n, h (2 * n) = h n)
    (htri : ∀ n, Odd n → 1 < n → h (3 * n + 1) = h n) (u : ℕ) (hu : Odd u) :
    h (3 * u) = h (16 * u + 1) := by
  have h1 := tri' h hdbl htri (3 * u) (Nat.odd_mul.mpr ⟨⟨1, rfl⟩, hu⟩)
  have h2 := id2 h hdbl htri (3 * u)
  have h3 := id2 h hdbl htri (4 * u)
  rw [← h1, h2, show 4 * (3 * u) + 1 = 3 * (4 * u) + 1 by ring, h3]
  congr 1
  ring

/-- Binary sections of the positive-offset family stay in the family. -/
theorem kernel_binary_closure {a r : ℕ} (ha : 1 ≤ a) (hr0 : 0 < r) (hr : r < 2 ^ a)
    {i : ℕ} (hi : i < 2) :
    ∃ a' r', 1 ≤ a' ∧ 0 < r' ∧ r' < 2 ^ a' ∧
      ∀ n, h (2 ^ a * (2 * n + i) + r) = h (2 ^ a' * n + r') := by
  refine ⟨a + 1, 2 ^ a * i + r, by omega, by omega, ?_, fun n => ?_⟩
  · have : 2 ^ a * i ≤ 2 ^ a * 1 := Nat.mul_le_mul_left _ (by omega)
    rw [pow_succ]
    omega
  · congr 1
    rw [pow_succ]
    ring

/-- **Ternary closure of the positive-offset family** (V004 §3). -/
theorem kernel_ternary_closure (hdbl : ∀ n, h (2 * n) = h n)
    (htri : ∀ n, Odd n → 1 < n → h (3 * n + 1) = h n)
    {a r : ℕ} (ha : 1 ≤ a) (hr0 : 0 < r) (hr : r < 2 ^ a) {j : ℕ} (hj : j < 3) :
    ∃ a' r', 1 ≤ a' ∧ 0 < r' ∧ r' < 2 ^ a' ∧
      ∀ n, h (2 ^ a * (3 * n + j) + r) = h (2 ^ a' * n + r') := by
  set c := 2 ^ a * j + r with hc
  have hc0 : 0 < c := Nat.add_pos_right _ hr0
  have hclt : c < 3 * 2 ^ a := by
    have : 2 ^ a * j ≤ 2 ^ a * 2 := Nat.mul_le_mul_left _ (by omega)
    omega
  have key : ∀ n, 2 ^ a * (3 * n + j) + r = 3 * (2 ^ a * n) + c := by
    intro n
    rw [hc]
    ring
  have hp1 : 2 ^ (a + 1) = 2 * 2 ^ a := by rw [pow_succ]; ring
  have hp2 : 2 ^ (a + 2) = 4 * 2 ^ a := by rw [pow_succ, pow_succ]; ring
  rcases (show c % 3 = 0 ∨ c % 3 = 1 ∨ c % 3 = 2 by omega) with h0 | h1 | h2
  · -- Case B: `3 ∣ c`
    obtain ⟨t, ht⟩ : ∃ t, c = 3 * t := ⟨c / 3, by omega⟩
    have ht0 : t ≠ 0 := by omega
    have htlt : t < 2 ^ a := by omega
    obtain ⟨ℓ, u, hu2, htu⟩ := Nat.exists_eq_pow_mul_and_not_dvd ht0 2 (by norm_num)
    have huodd : Odd u := Nat.not_even_iff_odd.mp (fun he => hu2 (even_iff_two_dvd.mp he))
    have hu0 : 0 < u := huodd.pos
    have hla : ℓ < a := by
      rcases Nat.lt_or_ge ℓ a with hlt | hge
      · exact hlt
      · exfalso
        have h1' : 2 ^ a ≤ 2 ^ ℓ := Nat.pow_le_pow_right (by norm_num) hge
        have h2' : 2 ^ ℓ ≤ 2 ^ ℓ * u := Nat.le_mul_of_pos_right _ hu0
        omega
    obtain ⟨s, hs⟩ := Nat.exists_eq_add_of_lt hla
    -- `a = ℓ + s + 1`; write `s1 = s + 1 ≥ 1`
    have hpa : 2 ^ a = 2 ^ ℓ * 2 ^ (s + 1) := by rw [hs]; ring
    have hu_lt : u < 2 ^ (s + 1) := by
      have hpos : 0 < 2 ^ ℓ := by positivity
      have : 2 ^ ℓ * u < 2 ^ ℓ * 2 ^ (s + 1) := by rw [← hpa, ← htu]; exact htlt
      exact Nat.lt_of_mul_lt_mul_left this
    have hp4 : 2 ^ (s + 1 + 4) = 16 * 2 ^ (s + 1) := by rw [pow_add]; ring
    refine ⟨s + 1 + 4, 16 * u + 1, by omega, by omega, by omega, fun n => ?_⟩
    have hodd' : Odd (2 ^ (s + 1) * n + u) := by
      have : Even (2 ^ (s + 1) * n) := ⟨2 ^ s * n, by rw [pow_succ]; ring⟩
      exact this.add_odd huodd
    calc h (2 ^ a * (3 * n + j) + r) = h (3 * (2 ^ a * n) + c) := by rw [key]
      _ = h (2 ^ ℓ * (3 * (2 ^ (s + 1) * n + u))) := by
          congr 1
          rw [ht, htu, hpa]
          ring
      _ = h (3 * (2 ^ (s + 1) * n + u)) := pow_two_mul h hdbl ℓ _
      _ = h (16 * (2 ^ (s + 1) * n + u) + 1) := id3 h hdbl htri _ hodd'
      _ = h (2 ^ (s + 1 + 4) * n + (16 * u + 1)) := by
          congr 1
          rw [hp4]
          ring
  · -- Case A, `c ≡ 1 (mod 3)`: `v = 2`
    obtain ⟨t, ht⟩ : ∃ t, 3 * t + 1 = 4 * c := ⟨(4 * c - 1) / 3, by omega⟩
    have htodd : Odd t := Nat.odd_iff.mpr (by omega)
    refine ⟨a + 2, t, by omega, by omega, by omega, fun n => ?_⟩
    have hodd' : Odd (2 ^ (a + 2) * n + t) := by
      have : Even (2 ^ (a + 2) * n) := ⟨2 ^ (a + 1) * n, by rw [pow_succ]; ring⟩
      exact this.add_odd htodd
    calc h (2 ^ a * (3 * n + j) + r) = h (3 * (2 ^ a * n) + c) := by rw [key]
      _ = h (2 ^ 2 * (3 * (2 ^ a * n) + c)) := (pow_two_mul h hdbl 2 _).symm
      _ = h (3 * (2 ^ (a + 2) * n + t) + 1) := by
          congr 1
          rw [show 3 * (2 ^ (a + 2) * n + t) + 1 = 3 * (2 ^ (a + 2) * n) + (3 * t + 1) by ring, ht]
          ring
      _ = h (2 ^ (a + 2) * n + t) := tri' h hdbl htri _ hodd'
  · -- Case A, `c ≡ 2 (mod 3)`: `v = 1`
    obtain ⟨t, ht⟩ : ∃ t, 3 * t + 1 = 2 * c := ⟨(2 * c - 1) / 3, by omega⟩
    have htodd : Odd t := Nat.odd_iff.mpr (by omega)
    refine ⟨a + 1, t, by omega, by omega, by omega, fun n => ?_⟩
    have hodd' : Odd (2 ^ (a + 1) * n + t) := by
      have : Even (2 ^ (a + 1) * n) := ⟨2 ^ a * n, by rw [pow_succ]; ring⟩
      exact this.add_odd htodd
    calc h (2 ^ a * (3 * n + j) + r) = h (3 * (2 ^ a * n) + c) := by rw [key]
      _ = h (2 * (3 * (2 ^ a * n) + c)) := (hdbl _).symm
      _ = h (3 * (2 ^ (a + 1) * n + t) + 1) := by
          congr 1
          rw [show 3 * (2 ^ (a + 1) * n + t) + 1 = 3 * (2 ^ (a + 1) * n) + (3 * t + 1) by ring, ht]
          ring
      _ = h (2 ^ (a + 1) * n + t) := tri' h hdbl htri _ hodd'

/-- The two worked examples of V004 §3: `h (12n+5) = h (8n+3)` and `h (12n+3) = h (64n+17)`. -/
theorem example_12n5 (hdbl : ∀ n, h (2 * n) = h n)
    (htri : ∀ n, Odd n → 1 < n → h (3 * n + 1) = h n) (n : ℕ) :
    h (12 * n + 5) = h (8 * n + 3) := by
  have := tri' h hdbl htri (8 * n + 3) ⟨4 * n + 1, by ring⟩
  rw [show 3 * (8 * n + 3) + 1 = 2 * (12 * n + 5) by ring, hdbl] at this
  exact this

theorem example_12n3 (hdbl : ∀ n, h (2 * n) = h n)
    (htri : ∀ n, Odd n → 1 < n → h (3 * n + 1) = h n) (n : ℕ) :
    h (12 * n + 3) = h (64 * n + 17) := by
  have := id3 h hdbl htri (4 * n + 1) ⟨2 * n, by ring⟩
  rw [show 3 * (4 * n + 1) = 12 * n + 3 by ring, show 16 * (4 * n + 1) + 1 = 64 * n + 17 by ring] at this
  exact this

end Kernel
end LeanLane
