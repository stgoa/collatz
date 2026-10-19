import Mathlib

/-!
# The scalar interface of invariant colourings (main's V005 §2)

Lane: `claude/lean-lane`. Prose source: `experiments/viewpoints/V005/scalar_interface.md`
on main ("Three scalar identities retain the complete Collatz guard").

Setting. A *colouring* `h : ℕ → α` is *invariant* when `h(2n) = h(n)` for all `n`
and `h(3n+1) = h(n)` for odd `n > 1`. Its *scalar* (odd-value) sequence is
`b(n) = h(2n+1)`. Conversely, from any sequence `b` main defines the odd-part
extension `h(x) = b((oddpart x − 1)/2)`, here `ext b`.

Verified in this file (all with the standard axioms):

* `ext_two_mul`, `ext_two_mul_add_one`, `ext_zero`, `ext_one`: for every `b`,
  `h = ext b` satisfies `h(2n) = h(n)`, `h(2n+1) = b(n)` and `h(0) = h(1) = b(0)`;
* `ext_tri_iff` (**main's equivalence**): `ext b` satisfies the remaining rule
  `h(3n+1) = h(n)` for odd `n > 1` **iff** `b` satisfies the three identities
  `b(3n) = b(4n)`, `b(3n+2) = b(2n+1)`, `b(4n+2) = b(n)` for all `n ≥ 0`.
  The converse goes through `ext_three_mul_add_two` (`h(3m+2) = b(m)`, main's
  `E(m)`, by strong induction on `m` with the split `m` odd / `4l` / `4l+2`);
  the rule then even holds for every odd `n`, including `n = 1` (`ext_tri`);
* `scalar_interface_iff`: `b` satisfies the three identities iff it is the
  scalar sequence of some invariant colouring;
* `ext_odd_values`: for an invariant colouring `h` (only `h(2n) = h(n)` is
  used), `ext (n ↦ h(2n+1)) x = h x` for every `x > 0` — so, together with
  `ext_two_mul_add_one`, the two passages are mutually inverse on the positive
  integers;
* `v004_relation`: the additional V004 relation `b(3n+1) = b(16n+8)` follows
  from the colouring rules, as the prose notes.

Nothing here concerns orbits, kernels, growth or convergence; Collatz remains
open.
-/

namespace LeanLane
namespace Scalar

variable {α : Type*}

/-! ### The odd part -/

/-- The odd part of `n`: `n / 2^{v₂(n)}`, with `oddPart 0 = 0`. -/
def oddPart (n : ℕ) : ℕ := n / 2 ^ padicValNat 2 n

theorem oddPart_zero : oddPart 0 = 0 := by simp [oddPart]

theorem oddPart_two_mul (n : ℕ) : oddPart (2 * n) = oddPart n := by
  rcases Nat.eq_zero_or_pos n with rfl | hn
  · simp [oddPart]
  · unfold oddPart
    rw [padicValNat.mul (by norm_num) hn.ne', padicValNat.self (by norm_num), pow_add, pow_one,
      Nat.mul_div_mul_left _ _ (by norm_num : 0 < 2)]

theorem oddPart_odd {n : ℕ} (hn : Odd n) : oddPart n = n := by
  unfold oddPart
  have h2 : ¬ 2 ∣ n := by obtain ⟨k, hk⟩ := hn; omega
  rw [padicValNat.eq_zero_of_not_dvd h2, pow_zero, Nat.div_one]

theorem oddPart_odd_of_pos : ∀ x, 0 < x → Odd (oddPart x) := by
  intro x
  induction x using Nat.strong_induction_on with
  | _ x ih =>
    intro hx
    rcases Nat.even_or_odd x with ⟨y, hy⟩ | hodd
    · have hx2 : x = 2 * y := by omega
      subst hx2
      rw [oddPart_two_mul]
      exact ih y (by omega) (by omega)
    · rw [oddPart_odd hodd]
      exact hodd

/-- A colouring with `h(2n) = h(n)` is determined by its values at odd arguments. -/
theorem colouring_oddPart (h : ℕ → α) (hdbl : ∀ n, h (2 * n) = h n) :
    ∀ x, 0 < x → h (oddPart x) = h x := by
  intro x
  induction x using Nat.strong_induction_on with
  | _ x ih =>
    intro hx
    rcases Nat.even_or_odd x with ⟨y, hy⟩ | hodd
    · have hx2 : x = 2 * y := by omega
      subst hx2
      rw [oddPart_two_mul, hdbl]
      exact ih y (by omega) (by omega)
    · rw [oddPart_odd hodd]

/-! ### The odd-part extension of a sequence -/

/-- Main's extension: `h(x) = b((oddpart x − 1)/2)`; in particular `h(2n+1) = b(n)`. -/
def ext (b : ℕ → α) (x : ℕ) : α := b ((oddPart x - 1) / 2)

theorem ext_zero (b : ℕ → α) : ext b 0 = b 0 := by simp [ext, oddPart]

theorem ext_one (b : ℕ → α) : ext b 1 = b 0 := by simp [ext, oddPart_odd odd_one]

theorem ext_two_mul (b : ℕ → α) (n : ℕ) : ext b (2 * n) = ext b n := by
  unfold ext
  rw [oddPart_two_mul]

theorem ext_two_mul_add_one (b : ℕ → α) (n : ℕ) : ext b (2 * n + 1) = b n := by
  unfold ext
  rw [oddPart_odd ⟨n, rfl⟩]
  congr 1
  omega

/-- Main's `E(m)`: under the three identities, `h(3m+2) = b(m)` for every `m`. -/
theorem ext_three_mul_add_two (b : ℕ → α)
    (h1 : ∀ n, b (3 * n) = b (4 * n))
    (h2 : ∀ n, b (3 * n + 2) = b (2 * n + 1))
    (h3 : ∀ n, b (4 * n + 2) = b n) :
    ∀ m, ext b (3 * m + 2) = b m := by
  intro m
  induction m using Nat.strong_induction_on with
  | _ m ih =>
    rcases Nat.even_or_odd m with ⟨k, hk⟩ | ⟨k, hk⟩
    · rcases Nat.even_or_odd k with ⟨l, hl⟩ | ⟨l, hl⟩
      · -- `m = 4l`: `h(12l+2) = h(6l+1) = b(3l) = b(4l)` by the first identity
        have hm : m = 4 * l := by omega
        subst hm
        rw [show 3 * (4 * l) + 2 = 2 * (2 * (3 * l) + 1) by ring, ext_two_mul,
          ext_two_mul_add_one]
        exact h1 l
      · -- `m = 4l+2`: `h(12l+8) = h(3l+2) = b(l) = b(4l+2)` by induction and the third
        have hm : m = 4 * l + 2 := by omega
        subst hm
        rw [show 3 * (4 * l + 2) + 2 = 2 * (2 * (3 * l + 2)) by ring, ext_two_mul, ext_two_mul,
          ih l (by omega)]
        exact (h3 l).symm
    · -- `m = 2k+1`: `h(6k+5) = b(3k+2) = b(2k+1)` by the second identity
      have hm : m = 2 * k + 1 := by omega
      subst hm
      rw [show 3 * (2 * k + 1) + 2 = 2 * (3 * k + 2) + 1 by ring, ext_two_mul_add_one]
      exact h2 k

/-- Under the three identities the extension satisfies the odd rule at **every** odd
`n`, including `n = 1`. -/
theorem ext_tri (b : ℕ → α)
    (h1 : ∀ n, b (3 * n) = b (4 * n))
    (h2 : ∀ n, b (3 * n + 2) = b (2 * n + 1))
    (h3 : ∀ n, b (4 * n + 2) = b n) :
    ∀ n, Odd n → ext b (3 * n + 1) = ext b n := by
  rintro n ⟨m, rfl⟩
  rw [show 3 * (2 * m + 1) + 1 = 2 * (3 * m + 2) by ring, ext_two_mul,
    ext_three_mul_add_two b h1 h2 h3 m, ext_two_mul_add_one]

/-! ### The three identities from the colouring rules (V004 algebra) -/

theorem odd_rule_two_mul_add_one (h : ℕ → α) (hdbl : ∀ n, h (2 * n) = h n)
    (htri : ∀ n, Odd n → 1 < n → h (3 * n + 1) = h n) (n : ℕ) :
    h (2 * n + 1) = h (3 * n + 2) := by
  rcases Nat.eq_zero_or_pos n with rfl | hn
  · have h21 : h 2 = h 1 := by simpa using hdbl 1
    simpa using h21.symm
  · have := htri (2 * n + 1) ⟨n, rfl⟩ (by omega)
    rw [show 3 * (2 * n + 1) + 1 = 2 * (3 * n + 2) by ring, hdbl] at this
    exact this.symm

/-- `b(3n) = b(4n)`, i.e. `h(6n+1) = h(8n+1)`. -/
theorem id1_of_colouring (h : ℕ → α) (hdbl : ∀ n, h (2 * n) = h n)
    (htri : ∀ n, Odd n → 1 < n → h (3 * n + 1) = h n) (n : ℕ) :
    h (2 * (3 * n) + 1) = h (2 * (4 * n) + 1) := by
  rcases Nat.eq_zero_or_pos n with rfl | hn
  · simp
  · have := htri (8 * n + 1) ⟨4 * n, by ring⟩ (by omega)
    rw [show 3 * (8 * n + 1) + 1 = 2 * (2 * (6 * n + 1)) by ring, hdbl, hdbl] at this
    rw [show 2 * (3 * n) + 1 = 6 * n + 1 by ring, show 2 * (4 * n) + 1 = 8 * n + 1 by ring]
    exact this

/-- `b(3n+2) = b(2n+1)`, i.e. `h(6n+5) = h(4n+3)`. -/
theorem id2_of_colouring (h : ℕ → α) (hdbl : ∀ n, h (2 * n) = h n)
    (htri : ∀ n, Odd n → 1 < n → h (3 * n + 1) = h n) (n : ℕ) :
    h (2 * (3 * n + 2) + 1) = h (2 * (2 * n + 1) + 1) := by
  have := htri (4 * n + 3) ⟨2 * n + 1, by ring⟩ (by omega)
  rw [show 3 * (4 * n + 3) + 1 = 2 * (6 * n + 5) by ring, hdbl] at this
  rw [show 2 * (3 * n + 2) + 1 = 6 * n + 5 by ring, show 2 * (2 * n + 1) + 1 = 4 * n + 3 by ring]
  exact this

/-- `b(4n+2) = b(n)`, i.e. `h(8n+5) = h(2n+1)`. -/
theorem id3_of_colouring (h : ℕ → α) (hdbl : ∀ n, h (2 * n) = h n)
    (htri : ∀ n, Odd n → 1 < n → h (3 * n + 1) = h n) (n : ℕ) :
    h (2 * (4 * n + 2) + 1) = h (2 * n + 1) := by
  have := htri (8 * n + 5) ⟨4 * n + 2, by ring⟩ (by omega)
  rw [show 3 * (8 * n + 5) + 1 = 2 * (2 * (2 * (3 * n + 2))) by ring, hdbl, hdbl, hdbl] at this
  rw [show 2 * (4 * n + 2) + 1 = 8 * n + 5 by ring]
  exact this.symm.trans (odd_rule_two_mul_add_one h hdbl htri n).symm

/-- The additional V004 relation `b(3n+1) = b(16n+8)` follows from the colouring rules. -/
theorem v004_relation (h : ℕ → α) (hdbl : ∀ n, h (2 * n) = h n)
    (htri : ∀ n, Odd n → 1 < n → h (3 * n + 1) = h n) (n : ℕ) :
    h (2 * (3 * n + 1) + 1) = h (2 * (16 * n + 8) + 1) := by
  have hA := htri (32 * n + 17) ⟨16 * n + 8, by ring⟩ (by omega)
  rw [show 3 * (32 * n + 17) + 1 = 2 * (2 * (24 * n + 13)) by ring, hdbl, hdbl] at hA
  have hB := htri (24 * n + 13) ⟨12 * n + 6, by ring⟩ (by omega)
  rw [show 3 * (24 * n + 13) + 1 = 2 * (2 * (2 * (9 * n + 5))) by ring, hdbl, hdbl, hdbl] at hB
  have hC := htri (6 * n + 3) ⟨3 * n + 1, by ring⟩ (by omega)
  rw [show 3 * (6 * n + 3) + 1 = 2 * (9 * n + 5) by ring, hdbl] at hC
  rw [show 2 * (3 * n + 1) + 1 = 6 * n + 3 by ring,
    show 2 * (16 * n + 8) + 1 = 32 * n + 17 by ring]
  exact hC.symm.trans (hB.trans hA)

/-! ### The equivalence -/

/-- **Main's V005 §2 equivalence.** For any sequence `b`, the odd-part extension
`h = ext b` (which always has `h(2n) = h(n)`, `h(2n+1) = b(n)`, `h(0) = h(1)`)
satisfies the remaining invariant rule `h(3n+1) = h(n)` at every odd `n > 1` iff
`b` satisfies the three scalar identities for all `n ≥ 0`. -/
theorem ext_tri_iff (b : ℕ → α) :
    (∀ n, Odd n → 1 < n → ext b (3 * n + 1) = ext b n) ↔
      (∀ n, b (3 * n) = b (4 * n)) ∧ (∀ n, b (3 * n + 2) = b (2 * n + 1)) ∧
        (∀ n, b (4 * n + 2) = b n) := by
  constructor
  · intro htri
    refine ⟨fun n => ?_, fun n => ?_, fun n => ?_⟩
    · have := id1_of_colouring (ext b) (ext_two_mul b) htri n
      rwa [ext_two_mul_add_one, ext_two_mul_add_one] at this
    · have := id2_of_colouring (ext b) (ext_two_mul b) htri n
      rwa [ext_two_mul_add_one, ext_two_mul_add_one] at this
    · have := id3_of_colouring (ext b) (ext_two_mul b) htri n
      rwa [ext_two_mul_add_one, ext_two_mul_add_one] at this
  · rintro ⟨h1, h2, h3⟩ n hn _
    exact ext_tri b h1 h2 h3 n hn

/-- **The scalar interface.** A sequence `b` satisfies the three identities iff it
is the odd-value sequence `n ↦ h(2n+1)` of some invariant colouring `h`. -/
theorem scalar_interface_iff (b : ℕ → α) :
    ((∀ n, b (3 * n) = b (4 * n)) ∧ (∀ n, b (3 * n + 2) = b (2 * n + 1)) ∧
        (∀ n, b (4 * n + 2) = b n)) ↔
      ∃ h : ℕ → α, (∀ n, h (2 * n) = h n) ∧ (∀ n, Odd n → 1 < n → h (3 * n + 1) = h n) ∧
        ∀ n, h (2 * n + 1) = b n := by
  constructor
  · intro hb
    exact ⟨ext b, ext_two_mul b, (ext_tri_iff b).mpr hb, ext_two_mul_add_one b⟩
  · rintro ⟨h, hdbl, htri, hb⟩
    refine ⟨fun n => ?_, fun n => ?_, fun n => ?_⟩
    · have := id1_of_colouring h hdbl htri n
      rwa [hb, hb] at this
    · have := id2_of_colouring h hdbl htri n
      rwa [hb, hb] at this
    · have := id3_of_colouring h hdbl htri n
      rwa [hb, hb] at this

/-- The passage `h ↦ (n ↦ h(2n+1)) ↦ ext` recovers `h` on the positive integers (only
`h(2n) = h(n)` is used); with `ext_two_mul_add_one` the two passages are inverse. -/
theorem ext_odd_values (h : ℕ → α) (hdbl : ∀ n, h (2 * n) = h n) (x : ℕ) (hx : 0 < x) :
    ext (fun n => h (2 * n + 1)) x = h x := by
  obtain ⟨k, hk⟩ := oddPart_odd_of_pos x hx
  have e : 2 * ((oddPart x - 1) / 2) + 1 = oddPart x := by omega
  show h (2 * ((oddPart x - 1) / 2) + 1) = h x
  rw [e, colouring_oddPart h hdbl x hx]

end Scalar
end LeanLane
