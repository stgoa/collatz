---
id: two-arc-word-rotation-structure
kind: result
title: "Two-arc words: their rotation spectrum, and the Sturmian case is exactly the adjacent-defect case"
status: written
claim: >
  Let w be a positive word of length m whose letters, read along the track of a rotation h with
  gcd(h, m) = 1 (t_k = a_(kh mod m)), form two arcs of constant letters a ≠ b, of lengths t_1 and t_2 =
  m − t_1; equivalently, w is the coding of the circle rotation x ↦ x + α (mod m), α = h^(−1), with respect
  to the partition of Z/m into [0, t_1) and [t_1, m). Then: (i) every rotation r of w has exactly
  s(r) = 2·min(‖rα‖_m, t_1, t_2) mismatches, ‖·‖_m the cyclic distance to 0; so ρ(w) = 2 and s(rh) = 2r for
  1 ≤ r ≤ min(t_1, t_2); (ii) the two mismatches of h sit at the natural positions (t_1 − 1)h and −h, at
  natural distance ℓ ≡ t_1·h (mod m), and for r ≤ min(t_1, t_2) the mismatches of rh are the 2r positions
  (t_1 − j)h and −jh, 1 ≤ j ≤ r; (iii) if min(t_1, t_2) ≥ 2, the following are equivalent: the two
  mismatches of h are adjacent (ℓ ≡ ±1); t_1 ≡ ±h^(−1) (mod m), i.e. an arc has the length of the track
  step; the binary mask of w is a mechanical word; and then gcd(C_w, D) | 2^|b−a| − 1 by
  two-defect-cancellation-bound part 5; (iv) if min(t_1, t_2) = 1, every rotation has exactly two
  mismatches and the mask is mechanical. Pure combinatorics; raw odd-only clock, any 3x+q, no size input.
authors:
  - Claude cycles lane (Fable 5.1; directed by Santiago Armstrong)
created: 2026-10-28
depends_on: [two-defect-cancellation-bound]
certificates: [check_two_arc_structure.py]
tags: [cycles, rotation-distance, rotation-codings, sturmian, combinatorics]
---

# Two-arc words: their rotation spectrum, and the Sturmian case is exactly the adjacent-defect case

## Statement

Fix `m ≥ 3`, a rotation `h` with `gcd(h, m) = 1`, and `α = h^(−1) mod m`. A **two-arc word** is `w_j = a` if `jα mod m ∈ [0, t_1)` and `w_j = b` otherwise, with `a ≠ b` and `1 ≤ t_1 ≤ m − 1`, `t_2 = m − t_1`: the letters read along the `h`-track (`t_k = w_(kh)`) are `a^(t_1) b^(t_2)`. By [`few-arc-codings-denominator-census`](../few-arc-codings-denominator-census/README.md) these are exactly the words with a rotation of coprime shift and two mismatches. Write `s(r) = #{i : w_i ≠ w_(i+r)}` and `‖x‖_m = min(x mod m, m − x mod m)`.

1. **Spectrum.** `s(r) = 2·min(‖rα‖_m, t_1, t_2)` for every `0 < r < m`. In particular `ρ(w) = 2`, the rotations with two mismatches are exactly `±h` when `min(t_1, t_2) ≥ 2`, and `s(rh) = 2r` for `1 ≤ r ≤ min(t_1, t_2)`.
2. **Positions.** The mismatches of `h` are the natural positions `e_1 = (t_1 − 1)h` and `e_2 = −h` (mod `m`), at natural distance `ℓ ≡ e_1 − e_2 ≡ t_1 h (mod m)`. For `1 ≤ r ≤ min(t_1, t_2)` the mismatches of `rh` are `(t_1 − j)h` and `−jh` for `1 ≤ j ≤ r`: the arc ends and their `r − 1` track predecessors.
3. **Dichotomy** (`min(t_1, t_2) ≥ 2`). The following are equivalent: (a) the two mismatches of `h` are adjacent, `ℓ ≡ ±1`; (b) `t_1 ≡ ±α (mod m)`, an arc has the length of the track step or its complement; (c) the mask `b_j = [w_j = b]` is a mechanical word `floor(((j+1)t + φ)/m) − floor((jt + φ)/m)`. When they hold, `gcd(C_w, D) | 2^|b−a| − 1` whenever `D = 2^A − 3^m > 0`.
4. **Single distinguished letter** (`min(t_1, t_2) = 1`). Every rotation has exactly two mismatches, and the mask is mechanical.

So a two-arc word is either **Sturmian** (case 3, cancellation at most `2^|b−a| − 1`) or **non-Sturmian**, with its two mismatches at natural distance `2 ≤ ℓ ≤ m − 2` and both arcs `u`, `v` of [`two-defect-cancellation-bound`](../two-defect-cancellation-bound.md) nonempty, where only `gcd(C_w, D) | (2^|b−a| − 1)·gcd(C_u, C_v)` is known.

## Proof

Everything happens on the track. Position `j` has track index `x = jα`; position `j + r` has track index `x + rα`. Let `I = [t_1, m)` be the arc of the letter `b`, `|I| = t_2`, and `δ = rα mod m`.

- **(1)** `w_j ≠ w_(j+r)` iff exactly one of `x`, `x + δ` lies in `I`, i.e. iff `x ∈ I Δ (I − δ)`. For an arc `I` of a cyclic group of order `m` and a shift `δ`, `|I Δ (I − δ)| = 2·min(‖δ‖_m, |I|, m − |I|)`: if `‖δ‖_m ≤ min(|I|, m − |I|)` the symmetric difference consists of two stretches of length `‖δ‖_m`; otherwise the shifted arc either lies in the complement or covers it, and the symmetric difference has size `2·min(|I|, m − |I|)`. Since `x ↦ jα` is a bijection, `s(r)` is this size. For `r = r'h`, `δ = r'`, so `s(r'h) = 2r'` as long as `r' ≤ min(t_1, t_2)`. The minimum over `r` is `2`, attained exactly at `‖rα‖_m = 1` (`r ≡ ±h`) or, when `min(t_1, t_2) = 1`, at every `r`.
- **(2)** For `δ = 1` the symmetric difference `I Δ (I − 1)` is `{t_1 − 1, m − 1}` (the last track index before `I` and the last index of `I`), whose natural positions are `(t_1 − 1)h` and `(m − 1)h ≡ −h`. Their difference is `t_1 h`. For `δ = r ≤ min(t_1, t_2)` the symmetric difference is `{t_1 − r, …, t_1 − 1} ∪ {m − r, …, m − 1}`, giving the stated positions.
- **(3)** (a) ⇔ (b): `ℓ ≡ t_1 h ≡ ±1` iff `t_1 ≡ ±h^(−1) = ±α`. (b) ⇒ (c): if `t_1 ≡ α` then, in track terms, `w_j = a` iff `jα mod m < α`, i.e. iff `(j+1)α mod m < jα mod m` (the rotation wraps), which is the mechanical word of slope `α/m` with letters swapped; `t_1 ≡ −α` is the complementary mask. (c) ⇒ (a): a primitive mechanical mask of slope `t/m` (`gcd(t, m) = 1`, which holds since the word is primitive) has the rotation `r` with `rt ≡ 1 (mod m)` shifting its phase by one, and that changes exactly two adjacent letters ([`mechanical-word-exact-denominator`](../mechanical-word-exact-denominator/README.md), primitive case, or [`two-defect-cancellation-bound`](../two-defect-cancellation-bound.md) part 5); since `min(t_1, t_2) ≥ 2` the only two-mismatch rotations are `±h`, so `r ≡ ±h` and the mismatches of `h` are adjacent. The divisibility is part 5 of the two-defect node (adjacent defects: `C_u = 1`, so `g | 2^k − 1` with `k = |b − a|`).
- **(4)** With one `a` (say), any rotation moves it to a position holding `b`: two mismatches. A word with a single `1` in its mask is `floor(((j+1) + φ)/m) − floor((j + φ)/m)`, mechanical of slope `1/m`.

## Certificates

[`check_two_arc_structure.py`](check_two_arc_structure.py) (standard library, about 2 s) builds every two-arc word with `m ≤ 30`, every `h` coprime to `m`, every `t_1`, and six letter pairs (31,932 words), and checks (1)–(4) directly: the spectrum formula for every rotation, the mismatch positions, `s(rh) = 2r`, the three-way equivalence (2,640 Sturmian words with `min(t_1, t_2) ≥ 2`, where the divisibility is also checked when `D > 0`), and the single-letter case (3,312 words).

## Remarks

- **What it adds.** Part 5 of [`two-defect-cancellation-bound`](../two-defect-cancellation-bound.md) handles "adjacent defects". This node says which two-mismatch words those are: exactly the Sturmian codings, where the arc length equals the track step. R71's one-step descent ([`mechanical-word-exact-denominator`](../mechanical-word-exact-denominator/README.md)) therefore settles the Sturmian case of the cancellation question completely (`G ≤ 2^|b−a| − 1`), and the open two-arc case of [`half-cancellation-for-few-mismatch-words`](../../questions/half-cancellation-for-few-mismatch-words.md) is the non-Sturmian one: two-interval codings whose interval length differs from the step. These are the words with large `gcd(C_u, C_v)` in the census (the half-swap `(1,3)` words have `t_1 = m/2`, far from `±α`).
- **Multiples of `h`.** Part 2 is the exact form of the "chain shift by `k`" picture that [`multi-rotation-four-mismatch-exclusion`](../../attempts/multi-rotation-four-mismatch-exclusion/README.md) used as a model for the rotations `h, 2h, …`: for a two-arc word the rotation by `rh` has exactly `2r` mismatches, at the arc ends and their `r − 1` track predecessors, as long as `r` does not exceed the shorter arc. For `s`-arc words the same argument gives `s(rh) = rs` for `r ≤ min_i t_i`, with mismatches at the `s` arc ends and their predecessors; beyond that, letters shared by non-consecutive arcs can cancel mismatches.
- **Controls.** The `3x+5` cycle `(1,1,3)` (`m = 3`, `t_1 = 1`) is case 4; its mask is mechanical and every rotation has two mismatches. Nothing is excluded; the result is combinatorial.
- Novelty undetermined; the symmetric-difference count is elementary.

## History

- Written 2026-10-28 by the Claude cycles lane (Fable 5.1), directed by Santiago Armstrong, as the first step of the "Euclidean descent" attack on the half-cancellation question: it showed that the descent is already done for the Sturmian case and isolated the non-Sturmian case as the open one.
