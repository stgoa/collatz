---
id: saturated-sets-residue-classes-finite-automaton
kind: result
title: "A finite automaton decides the residue-class question for all moduli 2^k·3^b·M′ at once; it is strongly connected for every M′ ≤ 1000"
status: written
claim: >
  Let T be the Collatz map on the positive integers and B a nonempty saturated set (x ∈ B iff T(x) ∈ B). Fix M′
  coprime to 6, let o₄ = ord_(M′)(4), v = v₃(o₄), v* = max(1, v), m₃ = 3^(v*+1). For odd z put W = 3z + 1 and
  σ(z) = (W mod M′, W mod m₃). Define the finite directed graph A(M′) on the M′·3^(v*) pairs (x, y) with y ≡ 1 (mod 3)
  by the arrows (x, y) → (4^s x, 4^s y) for s ≥ 1 and, when (y − 1)/3 ≢ 0 (mod 3), (x, y) → (2^j (x − 1)/3, 2^j z′ mod m₃)
  for every j ≥ 1 with 2^j·((y−1)/3) ≡ 1 (mod 3) and every lift z′ of (y − 1)/3 (mod 3^(v*)) to a class modulo 3^(v*+1).
  Theorem: if A(M′) is strongly connected, then for all k, b ≥ 0 every nonempty saturated B meets every residue class
  modulo 2^k·3^b·M′. The proof realises each arrow by legal moves (scalings σ_s(z) = 4^s z + (4^s − 1)/3 and inverse
  steps ι_j(z) = (2^j z − 1)/3, with the 3-adic digits of W beyond m₃ set freely by scalings with 4^s ≡ 1 (mod M′)),
  reaches the state (1 + 3ρ, 1 + 3ε) and then steers W modulo 3^(b+1) at no cost modulo M′; the 2-adic lift of the
  six-smooth node finishes. Certificate: A(M′) is strongly connected for all 333 moduli M′ ≤ 1000 coprime to 6
  (largest automaton 118,341 states, at M′ = 487 with v* = 5; 163 of the moduli have 3 | ord_(M′)(2), where the
  theorem of saturated-sets-residue-classes-order-of-two-prime-to-three does not apply). Hence every nonempty
  saturated set meets every residue class modulo every M whose part prime to 6 is at most 1000, in particular
  modulo every M ≤ 1000. Control: for the map 3x+5 the automaton modulo 5 has two components (the multiples of 5
  are saturated for 3x+5) while modulo 7 it is strongly connected, as it must be.
authors:
  - Claude cycles lane (Fable 5.1; directed by Santiago Armstrong)
created: 2026-10-31
depends_on: [saturated-sets-meet-residue-classes-six-smooth-moduli, saturated-sets-residue-classes-order-of-two-prime-to-three]
lean:
  - LeanLane.SaturatedAutomaton.saturated_dense_of_automaton
  - LeanLane.SaturatedAutomaton.exists_step
  - LeanLane.SaturatedAutomaton.exists_free_exponent'
certificates: [check_automaton.py]
evidence:
  - "../../../../lean/receipts/SaturatedAutomaton.build.txt, SaturatedAutomaton.axioms.txt, SaturatedAutomaton.sha256.txt: the Lean receipts for Theorem 1 (standard axioms only)"
  - "automaton.json: the receipt; for each M′ ≤ 1000 coprime to 6 the connectivity, the number of states, v*, and the orders of 2 and 4; the 3x+5 controls modulo 5 and 7"
tags: [invariants, residues, saturated-sets, orbit-components, density, profinite, finite-automaton]
---

# A finite automaton decides the residue-class question for all moduli `2^k·3^b·M′` at once; it is strongly connected for every `M′ ≤ 1000`

## Statement

`T` is the Collatz map on `Z_(>0)`; `B ⊆ Z_(>0)` is **saturated** if `x ∈ B ⟺ T(x) ∈ B` (the unions of orbit components of the question [`invariant-sets-meet-every-residue-class`](../../questions/invariant-sets-meet-every-residue-class.md)). Fix `M′` coprime to 6 and write

```
o₄ = ord_(M′)(4),   v = v₃(o₄),   v* = max(1, v),   m₃ = 3^(v*+1).
```

For an odd integer `z` let `W = 3z + 1` (so `W ≡ 1 (mod 3)`) and let its **state** be `σ(z) = (W mod M′, W mod m₃)`. The two moves of [`saturated-sets-residue-classes-order-of-two-prime-to-three`](../saturated-sets-residue-classes-order-of-two-prime-to-three/README.md) act on `W`: the scaling `σ_s` multiplies `W` by `4^s`, and the inverse step `ι_j` (legal iff `2^j z ≡ 1 (mod 3)`) sends `W` to `2^j z`.

**The automaton `A(M′)`.** Vertices: the pairs `(x, y)` with `x ∈ Z/M′`, `y ∈ Z/m₃`, `y ≡ 1 (mod 3)` (there are `M′·3^(v*)` of them). Arrows:

```
(S)  (x, y) → (4^s·x, 4^s·y)                                           for s ≥ 1;
(I)  (x, y) → (2^j·(x − 1)/3 mod M′,  2^j·z′ mod m₃)                   if z₃ := (y − 1)/3 mod 3 ≠ 0, for every j ≥ 1 with
                                                                        2^j·z₃ ≡ 1 (mod 3) and every z′ ≡ (y − 1)/3 (mod 3^(v*)).
```

(The three lifts `z′` of `(y − 1)/3` modulo `3^(v*)` to classes modulo `3^(v*+1)` give up to three arrows per `j`; the pairs `(2^j mod M′, 2^j mod m₃)` repeat with period `lcm(ord_(M′)(2), 2·3^(v*))`, so finitely many `j` suffice, and likewise `s` modulo `lcm(o₄, 3^(v*))`.)

**Theorem 1 (reduction).** If `A(M′)` is strongly connected, then for every nonempty saturated `B`, all `k, b ≥ 0` and every residue `r` modulo `2^k·3^b·M′`, `B` contains an element `≡ r`.

**Theorem 2 (computation).** `A(M′)` is strongly connected for every `M′ ≤ 1000` coprime to 6 (333 moduli; the largest automaton has 118,341 states, at `M′ = 487`, `v* = 5`). Consequently every nonempty saturated set meets every residue class modulo every `M` whose part prime to 6 is at most 1000; in particular modulo every `M ≤ 1000`.

| `v*` | 1 | 2 | 3 | 4 | 5 |
|---|---|---|---|---|---|
| number of `M′ ≤ 1000` | 278 | 47 | 5 | 2 | 1 |

Of the 333 moduli, 163 have `3 | ord_(M′)(2)` and are not covered by the uniform theorem of the order-prime-to-three node; the automaton settles them (for example `M′ = 7`: 21 states; `13`: 39; `19`: 171; `73`: 657; `163`: 13,203).

## Proof

Notation and Lemmas 1–2 (legality of `σ_s` and `ι_j`, `3σ_s(z) + 1 = 4^s(3z + 1)`, `3ι_j(z) + 1 = 2^j z`) are those of the order-prime-to-three node; Lemma 2 of the six-smooth node (4 generates the units `≡ 1 (mod 3)` modulo `3^(B+1)`, of order `3^B`) is used throughout.

**Lemma F (free steering beyond `m₃`).** Let `z ∈ B` be odd, `W = 3z + 1`, `B ≥ v*`, and `τ ≡ W (mod m₃)`. Then there is `s ≥ 1` with `4^s ≡ 1 (mod M′)` and `4^s W ≡ τ (mod 3^(B+1))`; so `z′ = σ_s(z) ∈ B` is odd, `z′ ≡ z (mod M′)`, `σ(z′) = σ(z)`, and `3z′ + 1 ≡ τ (mod 3^(B+1))`.

*Proof.* `τ/W ≡ 1 (mod 3^(v*+1))`, so `τ/W` lies in the subgroup of the cyclic group `U = ⟨4⟩` (units `≡ 1 (mod 3)` modulo `3^(B+1)`, order `3^B`) consisting of the elements `≡ 1 (mod 3^(v*+1))`, which has order `3^(B−v*)` and equals `⟨4^(3^(v*))⟩`. So `τ/W ≡ 4^(3^(v*)·t) (mod 3^(B+1))` for some `t`. Write `o₄ = 3^v·u` with `3 ∤ u`; since `v* ≥ v`, the condition `o₄ | 3^(v*)·t′` is `u | t′`. Choose `t′ ≥ 1` with `t′ ≡ t (mod 3^(B−v*))` and `t′ ≡ 0 (mod u)` (Chinese remainder theorem) and put `s = 3^(v*)·t′`. Then `4^s ≡ 4^(3^(v*)·t) ≡ τ/W (mod 3^(B+1))` because `4^(3^(v*))` has order `3^(B−v*)` there, and `4^s ≡ 1 (mod M′)` because `o₄ | s`. The rest is Lemma 1 (`3σ_s(z) + 1 = 4^s W`). ∎

**Lemma A (every arrow is realised).** Let `z ∈ B` be odd with `σ(z) = (x, y)`. For every arrow `(x, y) → (x′, y′)` of `A(M′)` there is an odd `z′ ∈ B` with `σ(z′) = (x′, y′)`.

*Proof.* (S): `z′ = σ_s(z)`; `W′ = 4^s W` gives the state `(4^s x, 4^s y)`. (I): the arrow has data `j` and a lift `z′₀` of `(y − 1)/3` modulo `3^(v*)`. The class of `z` modulo `3^(v*+1)` is determined by `W` modulo `3^(v*+2)`; by Lemma F with `B = v* + 1` and `τ ≡ W (mod m₃)` chosen as the lift corresponding to `z′₀`, replace `z` by an odd `z₁ ∈ B` with the same state and `z₁ ≡ z′₀ (mod 3^(v*+1))`. Now `z₁ ≡ (y − 1)/3 ≡ z₃ (mod 3)` and `2^j z₃ ≡ 1 (mod 3)`, so `ι_j(z₁) = (2^j z₁ − 1)/3 ∈ B` is odd (Lemma 2) with `W′ = 2^j z₁`: modulo `M′`, `z₁ ≡ (x − 1)/3`, so `W′ ≡ 2^j (x − 1)/3`; modulo `m₃`, `W′ ≡ 2^j z′₀`. ∎

**Proof of Theorem 1.** Let `B` be saturated and nonempty, and let the target be `r` modulo `2^k·3^b·M′`; by the 2-adic lift of the six-smooth node (its Lemma 4 with the odd modulus `3^b·M′` in place of `3^b`, exactly as in the order-prime-to-three node) it suffices to find, for every `b` and every pair `(ε mod 3^b, ρ mod M′)`, an odd element of `B` in that joint class; and it suffices to do so for `b ≥ v*`. Take an odd `x₀ ∈ B` (Lemma 1 of the six-smooth node) with state `σ(x₀)`, and the target state `(x*, y*) = (1 + 3ρ mod M′, 1 + 3ε mod m₃)`, a vertex of `A(M′)` since `y* ≡ 1 (mod 3)`. Strong connectivity gives a directed path from `σ(x₀)` to `(x*, y*)`; by Lemma A, induction along the path gives an odd `z ∈ B` with `σ(z) = (x*, y*)`. Finally Lemma F with `B = b` and `τ = 1 + 3ε` (indeed `τ ≡ W (mod m₃)`) gives an odd `z′ ∈ B` with `z′ ≡ z (mod M′)` and `3z′ + 1 ≡ 1 + 3ε (mod 3^(b+1))`, i.e. `z′ ≡ ε (mod 3^b)`; and `3z ≡ 3ρ (mod M′)` gives `z′ ≡ z ≡ ρ (mod M′)`. ∎

**Proof of Theorem 2.** The certificate builds `A(M′)` for each `M′ ≤ 1000` coprime to 6 with the finitely many multipliers above and computes its strongly connected components (Kosaraju's algorithm); each has exactly one. The consequence for `M = 2^k·3^b·M′` with `M′ ≤ 1000` is Theorem 1. ∎

## Lean

[`lean/LeanLane/SaturatedAutomaton.lean`](../../../../lean/LeanLane/SaturatedAutomaton.lean), namespace `LeanLane.SaturatedAutomaton`, built by `lake build LeanLane` (receipts [`SaturatedAutomaton.build.txt`](../../../../lean/receipts/SaturatedAutomaton.build.txt), [`SaturatedAutomaton.axioms.txt`](../../../../lean/receipts/SaturatedAutomaton.axioms.txt): only `propext`, `Classical.choice`, `Quot.sound`). **Theorem 1 is formal; Theorem 2 is the certificate's computation**, so the status stays `written`.

- States are pairs in `ZMod M' × ZMod (3 ^ v)` and `state M' v z = ((z : ZMod M'), (z : ZMod (3^v)))`: the Lean automaton uses the coordinates `(z mod M′, z mod 3^v)`, equivalent to `(W mod M′, W mod 3^(v+1))` of the text through `W = 3z + 1`.
- `Step M' v` is the inductive relation with the two kinds of arrows: `scale s hs x η : Step (x, η) (4^s x + cst s, 4^s η + cst s)` with `cst s = (4^s − 1)/3`, and `inv j hj x x' η zc hzc hleg hx' : Step (x, η) (x', ((2^j zc − 1)/3 : ℕ))` where `zc` is a natural number with `(zc : ZMod (3^v)) = η` (a lift of the class `η`), `2^j zc % 3 = 1` (legality), and `3 x' = 2^j x − 1` in `ZMod M'`.
- `exists_free_exponent' M' v u hu h3u hper z Bexp τ hB hτ hτv` is Lemma F: for `4 ^ (3^v u) ≡ 1 [MOD M']` with `3 ∤ u`, `v ≤ Bexp`, `τ ≡ 1 (mod 3)` and `τ ≡ 3z + 1 [MOD 3^(v+1)]`, some `s ≥ 1` has `4^s ≡ 1 [MOD M']` and `4^s (3z+1) ≡ τ [MOD 3^(Bexp+1)]`. Its new ingredient is `three_pow_dvd_of_four_pow_modEq`: `4^s ≡ 1 [MOD 3^(v+1)] → 3^v ∣ s`.
- `exists_step` is Lemma A: every arrow from the state of an odd element of `B` is realised by an odd element of `B`.
- `saturated_dense_of_automaton (hB : Saturated B) (hne : B.Nonempty) (M' v u : ℕ) (hM' : 0 < M') (hM6 : Nat.Coprime M' 6) (hv : 1 ≤ v) (hu : 0 < u) (h3u : ¬ 3 ∣ u) (hper : 4 ^ (3 ^ v * u) ≡ 1 [MOD M']) (hconn : ∀ σ σ', Relation.ReflTransGen (Step M' v) σ σ') (k b r : ℕ) : ∃ x ∈ B, x ≡ r [MOD 2 ^ k * 3 ^ b * M']` is Theorem 1. The hypotheses on `(v, u)` say that `3^v·u` is a period of 4 modulo `M′` with `3 ∤ u`; for `v = v*` of the text such a `u` exists (`u = o₄/3^(v₃(o₄))`, or `u = o₄` when `v₃(o₄) = 0`), and the strong-connectivity hypothesis is exactly what the certificate checks for each `M′ ≤ 1000`.
- Not formalised: Theorem 2 (the connectivity of the 333 automata), the equivalence between the two coordinate systems (a change of variables), and the `3x+d` remark.

## Certificates

[`check_automaton.py`](check_automaton.py) (standard library, about 4.5 minutes): **V1** for every `M′ ≤ 1000` coprime to 6, builds `A(M′)` (arrows (S) for `s` up to `lcm(o₄, 3^(v*))`, arrows (I) for `j` up to `lcm(ord_(M′)(2), 2·3^(v*))` of each parity and the three lifts) and checks that Kosaraju's algorithm finds one strongly connected component; the receipt records for each modulus the number of states, `v*`, `ord_(M′)(2)` and `o₄`; **V2** controls for the map `3x+5` (`W = 3z + 5`, inverse step legal iff `2^j z ≡ 5 ≡ 2 (mod 3)`, scaling `(4^s(3z + 5) − 5)/3`): the automaton modulo 5 has two components (the class `W ≡ 0`, i.e. the multiples of 5, is closed) and the automaton modulo 7 is strongly connected; **V3** the receipt [`automaton.json`](automaton.json) (`--write-receipt` regenerates it). Finite statements only; Theorem 1 is the text above.

## Remarks

- **What this adds.** The two earlier theorems prove the statement uniformly for `M′ = 1` and for `3 ∤ ord_(M′)(2)`; the finite search of [`saturated-sets-meet-residue-classes-small-moduli`](../saturated-sets-meet-residue-classes-small-moduli/README.md) proves it for individual `M ≤ 100`, one modulus at a time, with a state space growing with `k` and `b`. Theorem 1 removes `k` and `b` from the computation: a single graph with `M′·3^(v*)` vertices decides the statement for all `2^k·3^b·M′` simultaneously, because the 2-adic lift handles `k` and Lemma F makes all 3-adic digits beyond `m₃` free. The automaton is tiny even for the "bad" primes (`7`: 21 states) and was strongly connected in every case tried, including the 163 moduli with `3 | ord_(M′)(2)` up to 1000. The remaining content of the question is a proof that `A(M′)` is strongly connected for every `M′`, or a replacement of that finite check by an argument; the computation suggests this is true, and any failure would be a counterexample to the question (a congruence obstruction for some orbit component).
- **Why the state is `W mod 3^(v*+1)`.** A scaling that steers the 3-adic class of `W` by `4^s` acts modulo `M′` by `4^s`, and `s` modulo `3^v` is visible modulo `M′` (as `3^v ∥ o₄`); so only the digits of `W` beyond `3^(v*+1)` can be steered for free, and the coupled part of the 3-adic information is exactly `W mod 3^(v*+1)`. For good `M′` (`v = 0`) the state space is `3M′` and the automaton's connectivity is what the order-prime-to-three node proves by hand.
- **Controls.** For `3x+d` the same construction gives an automaton whose arrows are the `d`-versions of (S) and (I); it is disconnected modulo every prime dividing `d` (the class `W ≡ 0` is closed, i.e. `dZ_(>0)` is saturated) and connected modulo 7 for `d = 5`, as checked. Novelty undetermined.
- **Formalisation.** Theorem 1 is a finite reduction whose ingredients are already formal (the moves, the free-steering lemma, the lift); the strong-connectivity hypothesis for a specific `M′` is a decidable statement about a small graph. Not formalised here.

## History

- Written 2026-10-31 by the Claude cycles lane (Fable 5.1), directed by Santiago Armstrong, after the order-prime-to-three proof showed that the only obstacle to a uniform argument was the finite coupled part of the 3-adic information.
- 2026-10-31, later: Theorem 1 formalised in Lean (`LeanLane.SaturatedAutomaton`, standard axioms only); the status stays `written` because Theorem 2 is the certificate's computation (Claude cycles lane, Fable 5.1).
