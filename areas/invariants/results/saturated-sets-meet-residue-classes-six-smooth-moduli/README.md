---
id: saturated-sets-meet-residue-classes-six-smooth-moduli
kind: result
title: "Every saturated set of the 3x+1 map meets every residue class modulo 2^k·3^b, for all k and b"
status: formal
claim: >
  Let T be the Collatz map on the positive integers (n → n/2 for even n, n → 3n+1 for odd n) and B a nonempty set
  with x ∈ B iff T(x) ∈ B (saturated: a union of orbit components). Then for all k, b ≥ 0 and every residue
  r modulo 2^k·3^b, B contains an element ≡ r (mod 2^k·3^b); equivalently, B is dense in Z_2 × Z_3. Proof: B
  contains an odd element and is closed under x → 2x, x → 3x+1 (x odd) and x → (x−1)/3 (x ≡ 4 mod 6); since 2
  is a primitive root modulo every power of 3, the doublings of one element prime to 3 followed by a single
  inverse step give odd elements in every class modulo 3^b (base case); and an odd target class u modulo 2^k with
  k ≥ 2 is reached from a target modulo 2^(k−j), j = v_2(3u+1) ≥ 1, with one more 3-adic digit prescribed, by
  j doublings and one inverse step (induction on k). The construction uses no halving, exactly one inverse step
  for the targets modulo 3^b and at most k inverse steps for the targets modulo 2^k, matching the least budgets
  found by the finite search of saturated-sets-meet-residue-classes-small-moduli (4: 2, 8: 3, …, 64: 6, 3^b: 1).
  The same proof works verbatim for the map 3x+d with gcd(d, 6) = 1 (the inverse branch is then x → (x−d)/3 on
  x even, x ≡ d mod 3), which is consistent with the controls: the saturated sets dZ_(>0) of 3x+d miss classes only
  modulo the primes dividing d, never modulo 2^k·3^b. Nothing is claimed for moduli with a prime factor ≥ 5.
authors:
  - Claude cycles lane (Fable 5.1; directed by Santiago Armstrong)
created: 2026-10-31
depends_on: []
lean:
  - LeanLane.SaturatedDensity.saturated_dense
  - LeanLane.SaturatedDensity.exists_modEq_pow
  - LeanLane.SaturatedDensity.two_pow_mul_surj
certificates: [check_six_smooth_closure.py]
evidence:
  - "../../../../lean/receipts/SaturatedDensity.build.txt, SaturatedDensity.axioms.txt, SaturatedDensity.sha256.txt: the Lean receipts (standard axioms only)"
  - "six_smooth_closure.json: the receipt; the constructive proof replayed from every odd start ≤ 99 to every class modulo 2^k·3^b, k ≤ 6, b ≤ 3 (254,000 targets), the primitive-root lemma for 3^(b+1), b ≤ 9, the 3x+d controls d ∈ {5, 7, 13, 61}, and the inverse-step counts per (k, b)"
tags: [invariants, residues, saturated-sets, orbit-components, 2-adic, 3-adic, density, primitive-root]
---

# Every saturated set of the `3x+1` map meets every residue class modulo `2^k·3^b`, for all `k` and `b`

## Statement

`T` is the Collatz map on `Z_(>0)`; `B ⊆ Z_(>0)` is **saturated** if `x ∈ B ⟺ T(x) ∈ B` (a union of connected components of the Collatz graph; the question [`invariant-sets-meet-every-residue-class`](../../questions/invariant-sets-meet-every-residue-class.md) calls these unions of orbit components).

**Theorem.** For every nonempty saturated `B`, all `k, b ≥ 0` and every residue `r` modulo `2^k·3^b`, `B` contains an element `≡ r (mod 2^k·3^b)`. Equivalently: the closure of `B` in `Z_2 × Z_3` is all of `Z_2 × Z_3`.

The finite search of [`saturated-sets-meet-residue-classes-small-moduli`](../saturated-sets-meet-residue-classes-small-moduli/README.md) proved this for the individual moduli `M ≤ 100`; this node proves it for every modulus whose prime factors are 2 and 3, by an induction that explains the budgets that search found. Moduli with a prime factor `≥ 5` are not covered (see Remarks).

## Proof

**Lemma 1 (the moves).** If `B` is saturated and `x ∈ B`, then `2x ∈ B`; if `x` is odd, `3x + 1 ∈ B`; if `x ≡ 4 (mod 6)`, then `(x − 1)/3 ∈ B`. If `B` is nonempty it contains an odd element.

*Proof.* `T(2x) = x ∈ B` gives `2x ∈ B`. For odd `x`, `T(x) = 3x + 1`. For `x ≡ 4 (mod 6)`, `z = (x − 1)/3` is a positive integer, odd because `x − 1 ≡ 3 (mod 6)`, with `T(z) = 3z + 1 = x ∈ B`, so `z ∈ B`. Halving an element of `B` (`T(x) = x/2 ∈ B` for even `x`) until it is odd gives the last claim. ∎

We call the three moves **doubling** `D`, **forward** `F` and **inverse** `I`. No halving is used below.

**Lemma 2 (2 is a primitive root modulo `3^n`).** For every `n ≥ 1`, every `y` prime to 3 and every `η ≡ y·(unit) (mod 3^n)`, i.e. every `η` prime to 3, there is `j` with `1 ≤ j ≤ 2·3^(n−1)` and `2^j·y ≡ η (mod 3^n)`.

*Proof.* The order of 2 modulo `3^n` is `2·3^(n−1) = φ(3^n)`: `4 = 1 + 3`, and by induction `4^(3^(n−1)) ≡ 1 + 3^n (mod 3^(n+1))` (cube `1 + 3^n + c·3^(n+1)`: the cross terms `3·3^(2n)` and `3·c·3^(n+1)` are `≡ 0 (mod 3^(n+2))`), so `4` has order exactly `3^(n−1)` modulo `3^n`, hence `2` has order `3^(n−1)` or `2·3^(n−1)`; and `2^(3^(n−1)) ≡ 2 ≢ 1 (mod 3)` rules out the first. So `j ↦ 2^j` is a bijection from `{1, …, 2·3^(n−1)}` onto the units modulo `3^n`, and `η·y^(−1)` is one of them. ∎

**Notation.** `P(k, b)`: for every odd class `u` modulo `2^k` (for `k = 0` the empty condition) and every class `ε` modulo `3^b`, `B` contains an **odd** element `x` with `x ≡ u (mod 2^k)` and `x ≡ ε (mod 3^b)`.

**Lemma 3 (base case: `P(1, b)` for all `b`).** Let `x_0 ∈ B` be odd (Lemma 1). Put `y = x_0` if `3 ∤ x_0`, and `y = 3x_0 + 1` otherwise (a forward move; then `y ≡ 1 (mod 3)`). Given `ε` modulo `3^b`, Lemma 2 with `n = b + 1` and `η = 1 + 3ε` (prime to 3) gives `j ≥ 1` with `2^j·y ≡ 1 + 3ε (mod 3^(b+1))`. The element `2^j·y ∈ B` is even and `≡ 1 (mod 3)`, so `≡ 4 (mod 6)`, and the inverse move gives

```
z = (2^j·y − 1)/3 ∈ B,     z odd,     z ≡ ((1 + 3ε) − 1)/3 = ε  (mod 3^b).
```

∎ (`P(0, b)` follows, and `P(1, b)` says exactly this since every `z` produced is odd.)

**Lemma 4 (the lift: `P(k − j, b + 1)` for the right `j` implies the instance of `P(k, b)`).** Let `k ≥ 2`, `u` odd modulo `2^k`, `ε` modulo `3^b`. Put `j = v_2(3u + 1) ≥ 1` (`3u + 1` is even) and

```
c = 2^(−j)·(1 + 3ε)   (mod 3^(b+1))         (2 is invertible modulo 3^(b+1)).
```

- If `j < k`: let `u′ = (3u + 1)/2^j`, odd, taken modulo `2^(k−j)`. By `P(k − j, b + 1)` there is an odd `y ∈ B` with `y ≡ u′ (mod 2^(k−j))` and `y ≡ c (mod 3^(b+1))`.
- If `j ≥ k`: by `P(1, b + 1)` there is an odd `y ∈ B` with `y ≡ c (mod 3^(b+1))` (no 2-adic condition is needed).

Then `2^j·y ≡ 2^j·c = 1 + 3ε (mod 3^(b+1))`, in particular `2^j·y ≡ 1 (mod 3)`, and `2^j·y` is even: the inverse move applies and gives `z = (2^j·y − 1)/3 ∈ B`, odd, with

```
z ≡ ε  (mod 3^b)        since 2^j·y ≡ 1 + 3ε (mod 3^(b+1)),
z ≡ u  (mod 2^k)        since 3z + 1 = 2^j·y ≡ 2^j·u′ = 3u + 1 (mod 2^k)  if j < k,  and  3z + 1 = 2^j·y ≡ 0 ≡ 3u + 1 (mod 2^k)  if j ≥ k,
```

and `3` is invertible modulo `2^k`. ∎

**Proof of the theorem.** By induction on `k`, `P(k, b)` holds for all `k ≥ 0` and all `b`: Lemma 3 gives `k ≤ 1`, and Lemma 4 reduces `(k, b)` with `k ≥ 2` to `(k − j, b + 1)` with `1 ≤ k − j < k` or to `(1, b + 1)`. For a general target `r` modulo `2^k·3^b`: if `2^k | r`, take by `P(0, b)` an element `y ≡ 2^(−k)·ε (mod 3^b)` and double it `k` times; otherwise write `r ≡ 2^v·u (mod 2^k)` with `v < k` and `u` odd, take by `P(k − v, b)` an odd `y ≡ u (mod 2^(k−v))`, `y ≡ 2^(−v)·ε (mod 3^b)`, and double it `v` times. ∎

**Budgets.** The construction uses no halving, exactly one inverse step for the targets modulo `3^b` (Lemma 3) and at most `k` inverse steps for the odd targets modulo `2^k` (each lift lowers `k` by `j ≥ 1` and the base case adds one), the worst case being the classes with `v_2(3u + 1) = 1` at every stage. These are exactly the least budgets `(0, 0), (0, 2), (0, 3), …, (0, 6)` for `M = 2, 4, …, 64` and `(1, 1)` for `M = 3^b` that the search of [`saturated-sets-meet-residue-classes-small-moduli`](../saturated-sets-meet-residue-classes-small-moduli/README.md) found (its halving budget `1` for odd `M` carries the parity that the construction here knows by other means). Each lift consumes one 3-adic digit of precision, which is why the search needed the modulus `3^(b_M + b)` with `b` up to `k`.

**The general `3x+d`, `gcd(d, 6) = 1`.** Replace `3x + 1` by `3x + d` and the inverse branch by `x → (x − d)/3` on `x` even with `x ≡ d (mod 3)`; Lemma 1 holds verbatim (`3x_0 + d` is prime to 3 because `gcd(d, 3) = 1`), Lemma 3 uses `η = d + 3ε`, Lemma 4 uses `j = v_2(3u + d)` and `c = 2^(−j)(d + 3ε)`, and the only new point is positivity of `(2^j·y − d)/3`, obtained by adding full periods `2·3^b` of doublings in the base case so that every element along the construction exceeds `d`. The certificate runs this version for `d ∈ {5, 7, 13, 61}`.

## Lean

[`lean/LeanLane/SaturatedDensity.lean`](../../../../lean/LeanLane/SaturatedDensity.lean), namespace `LeanLane.SaturatedDensity`, built by `lake build LeanLane` (receipts [`SaturatedDensity.build.txt`](../../../../lean/receipts/SaturatedDensity.build.txt), [`SaturatedDensity.axioms.txt`](../../../../lean/receipts/SaturatedDensity.axioms.txt): only `propext`, `Classical.choice`, `Quot.sound`).

- `T : ℕ → ℕ` is `if n % 2 = 0 then n / 2 else 3 * n + 1`, the Collatz map of the claim.
- `Saturated B` (for `B : Set ℕ`) is the pair of hypotheses `∀ x ∈ B, 0 < x` and `∀ x, 0 < x → (x ∈ B ↔ T x ∈ B)`: `B` consists of positive integers and is saturated in the sense of the claim. Positivity is needed because `0` is a fixed point of `T` and `{0}` would otherwise be a saturated set meeting one class only.
- `saturated_dense (hB : Saturated B) (hne : B.Nonempty) (k b r : ℕ) : ∃ x ∈ B, x ≡ r [MOD 2 ^ k * 3 ^ b]` is the theorem, with `Nat.ModEq`; `exists_modEq_pow` is the induction statement `P(k, b)` for arbitrary (not only odd) classes `r` modulo `2^k`, and `two_pow_mul_surj` is Lemma 2 in the form `∀ n, ∃ j ≥ 1, 3^(n+1) ∣ 2^j·y − η` for integers `y, η` prime to 3.
- The Lean proof follows the text with one simplification: the lift always uses `j = 1` (one doubling and one inverse step, reducing `k` by one and raising `b` by one), which is enough for the existence statement; the budget bookkeeping of the text (the choice `j = v_2(3u + 1)`) is not formalised. The moves are `mem_double`, `mem_forward`, `mem_inverse`, the odd element is `exists_odd`, and Lemma 2 rests on `four_pow_three_pow`: `4^(3^n) = 1 + 3^(n+1) + m·3^(n+2)` for some integer `m`.
- The `3x+d` generalisation of the last paragraph of the proof is not formalised; the Lean statement is for `3x+1` only.

## Certificates

[`check_six_smooth_closure.py`](check_six_smooth_closure.py) (standard library, about 3 minutes) instantiates the construction and replays every move: **V1** from every odd start `x_0 ≤ 99`, for all `k ≤ 6`, `b ≤ 3` and all `2^k·3^b` targets (254,000 paths; each doubling, forward and inverse move is checked for legality and the end point for its residues); **V2** Lemma 2 for `3^(b+1)`, `b ≤ 9`, by enumeration; **V3** the `3x+d` version for `d ∈ {5, 7, 13, 61}`, odd `x_0 ≤ 41`, `k ≤ 4`, `b ≤ 2`; **V4** the inverse-step counts: `[1, 1, 2, 3, 4, 5, 6]` for `k = 0..6` (`b = 0`) and `1` for every `b ≤ 3` (`k = 0`); **V5** the receipt [`six_smooth_closure.json`](six_smooth_closure.json) (`--write-receipt` regenerates it). The certificate checks the construction, not the theorem: the theorem's proof is the text above.

## Remarks

- **Reading.** The closure of any orbit component in `Z_2 × Z_3` is everything: no saturated set is detectable by 2-adic or 3-adic congruences, however deep. The 2-adic statement alone is probably classical for the inverse tree of an element prime to 3 (the predecessor tree of such an element is 2-adically dense); the forward move is needed only to leave the multiples of 3, whose inverse tree is `{2^j·x}` alone. Novelty undetermined.
- **What remains of the question.** For a modulus with a prime factor `p ≥ 5` the lift of Lemma 4 works unchanged (the extra condition `y ≡ 2^(−j)(1 + 3ρ) (mod p^c)` is bijective in `ρ`), so the question [`invariant-sets-meet-every-residue-class`](../../questions/invariant-sets-meet-every-residue-class.md) reduces to the base case: **odd elements of `B` in every joint class modulo `3^b·M′`, `gcd(M′, 6) = 1`.** There the doublings of one element reach only the coset `2^(j_0)·⟨4⟩` of multipliers modulo `M′`, so several inverse steps are needed, and the finite search shows two suffice for `M′ = 5` (budget `(1, 2)`) and at most four for every odd `M ≤ 100`. A uniform argument would have to show that the affine maps `ρ ↦ (cρ − 1)/3`, `c ∈ ⟨2⟩`, together with doubling, act transitively on `Z/M′` under the legality constraints; the group they generate contains all translations (the commutator of `x ↦ 2x` and `x ↦ 3x + 1` is `x ↦ x + 1`), but the constrained semigroup is what matters.
- **Controls.** For `3x+d` with `gcd(d, 6) = 1` the theorem holds with the same proof, and `d·Z_(>0)` is a saturated set of `3x+d` that misses every class `≢ 0 (mod p)` for each prime `p | d`: the obstruction lives exactly at the primes the theorem excludes. For `3 | d` the proof fails at Lemma 1 (`3x_0 + d` stays divisible by 3) and the statement is false (`3Z_(>0)` is saturated for `3x+3`). Odd-only clock not used; `3x+1` with the full map `T`.

## History

- Written 2026-10-31 by the Claude cycles lane (Fable 5.1), directed by Santiago Armstrong, generalising the finite verification of the same day after noticing that its budgets `(0, k)` for `2^k` and `(1, 1)` for `3^b` are the depths of a digit-by-digit construction.
- 2026-10-31, later: formalised in Lean (`LeanLane.SaturatedDensity`, standard axioms only); status `formal` (Claude cycles lane, Fable 5.1).
