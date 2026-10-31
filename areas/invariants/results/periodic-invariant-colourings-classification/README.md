---
id: periodic-invariant-colourings-classification
kind: result
title: Periodic invariant colourings of 3x+d factor through gcd(M, d), so for 3x+1 they are constant
status: formal
claim: >
  Fix a positive odd d with 3 not dividing d, and let h be a colouring of the positive integers (any colour set)
  with h(2n) = h(n) for n >= 1 and h(3n+d) = h(n) for odd n > 1 (ordinary-arrow invariance; 1 is the absorber and
  no identity is imposed at n = 1). If h has a period M >= 1, then h factors through g = gcd(M, d) and is constant
  on the orbits of multiplication by 2 and by 3 in Z/gZ; conversely every such function is an M-periodic solution.
  An eventual period is already a global period. In particular every periodic or eventually periodic invariant
  colouring of 3x+1 (d = 1) is constant. For d = 5 and d = 61 the indicator of d | n is a nonconstant periodic
  invariant.
authors:
  - ChatGPT main lane (Codex)
created: 2026-10-18
lean:
  - LeanLane.periodic_invariant_const
  - LeanLane.control_three_x_plus_five
  - LeanLane.GenPer.invariant_classification
  - LeanLane.GenPer.factors_through_zmod
  - LeanLane.GenPer.invariant_of_class_function
  - LeanLane.GenPer.period_gcd_six_free
  - LeanLane.GenPer.eventually_periodic_invariant
  - LeanLane.GenPer.control_indicator
  - LeanLane.GenPer.control_five
  - LeanLane.GenPer.control_sixty_one
certificates: [verify_examples.py, check_legacy_replay.py]
evidence:
  - "verify_examples.py, verification.json: main-lane bounded replay of V002's examples (480 finite quotient partitions, plus the exact history, ensemble, geometry and transducer examples of the survey notes in ../../attempts/viewpoint-language-survey/ and ../../attempts/binary-ternary-carry-frontier/); not the all-modulus proof"
  - "v13_coloring_check.py, v13_coloring_check.json: side-lane check of the classification on residue graphs (2,400 cases: M <= 400, d in {1, 5, 7, 11, 13, 61}) and of the controls; it has no failure exit of its own, so check_legacy_replay.py replays it and requires its receipt byte for byte"
reviewed_by:
  - by: Claude side lane (Opus)
    date: 2026-10-18
    link: v13_coloring_check.py
    scope: "Feed 18:24 (REFEREE V002): components of the residue graph mod M equal the <x2, x3>-orbits on Z/gcd(M, d)Z in all 2,400 cases; controls 1_(5|n), 1_(61|n) invariant. Feed 22:42: Lean item 1b read from source and receipts, statement match confirmed"
  - by: Claude Lean lane (Fable)
    date: 2026-10-18
    scope: "Lean units 1 (iteration 1) and 1b (iteration 8): the periodic theorem, the gcd(M, d) classification for every odd d, its converse, eventual periods and the d | n controls, machine-checked"
aliases: [V002]
tags: [invariants, colourings, periodic, rigidity, controls, formal]
---

# Periodic invariant colourings of 3x+d factor through gcd(M, d), so for 3x+1 they are constant

## Statement

Let `h` assign a colour to every positive integer and be constant on each orbit component. Extend an odd-state colouring by `h(n) = h(oddpart(n))`. For fixed positive odd `d` with `3 ∤ d`, invariance means

```
h(2n) = h(n)                     for n >= 1,
h(3n+d) = h(n)                   for odd n > 1.                 (1)
```

The target 1 is absorbing; no second identity is imposed at `n = 1`. These equations express ordinary-arrow invariance, not a change of the default odd-only clock; the shortcut form of the second equation is equivalent by the first. A nonabsorbing-set indicator is one such two-colour function.

**Theorem.** For every `M ≥ 1`, every `M`-periodic solution of (1) factors through `g = gcd(M, d)` and is constant on the orbits of multiplication by 2 and by 3 in `Z/gZ`. The converse also holds. An eventual period is a global period. In particular, **every periodic or eventually periodic `d = 1` invariant colouring is constant**.

**Controls.** For `d = 5`, `h(n) = 1_{5|n}` is a nonconstant invariant colouring of period 5: multiplication by 2 or 3 preserves zero versus nonzero modulo 5, and the `+5` term preserves that distinction. Likewise `h(n) = 1_{61|n}` works at `d = 61`. The fixed odd states 5 and 61 lie outside the absorber 1. The commutator below gives a shift by `d`, not by 1, so it cannot erase these colours: this names exactly where the `d = 1` rigidity stops. These colours do not classify all components: the `d = 5` cycle `19 → 31 → 49` and the `d = 61` nonprincipal cycle at 235 lie outside their divisible strata.

## Proof

Assume `h` has period `M` and satisfies (1); its colour set may be arbitrary. Write `M = 2^a 3^b m` with `(m, 6) = 1`.

**Remove the factor 2.** If `n ≡ n' (mod 3^b m)`, then `2^a n ≡ 2^a n' (mod M)`. Iterating the first identity gives `h(n) = h(n')`. Thus `h` factors through the odd modulus `M0 = 3^b m`.

**Extend the affine identity to every residue.** Every class modulo `M0` has a sufficiently large positive odd representative greater than 1. The second identity therefore gives invariance of the induced colouring under `B(r) = 3r + d` on every residue of `Z/M0Z`. In particular the missing ordinary arrow at the absorber causes no exception in this finite quotient.

**Remove the factor 3.** The `b`-th iterate is `B^b(r) = 3^b r + d(3^b − 1)/2`. Residues `r, r'` equal modulo `m` have the same image under this iterate modulo `M0`. Hence `h` factors through `m`. This also works at `b = 0`.

**Use the affine commutator.** On `Z/mZ`, both `A(r) = 2r` and `B(r) = 3r + d` preserve `h`. Thus `h(6r + 2d) = h(6r + d)`. Since multiplication by 6 permutes these residues, `h` is invariant under translation by `d`. The subgroup generated by `d` consists of the multiples of `gcd(m, d)`, so `h` factors through `gcd(m, d) = gcd(M, d) = g`. At this modulus `B` is multiplication by 3 and `A` multiplication by 2. Colours are exactly unions of their joint orbits. For example, at `d = 1`: `h(6n+2) = h(A(B(n))) = h(n) = h(B(A(n))) = h(6n+1)`, and 6 is invertible modulo the remaining period, so neighbouring residues have the same colour.

**Converse.** If `h` factors through `g` and is invariant under those two multiplications, then (1) holds because `g` divides `d`. Since `g` divides `M`, the function is `M`-periodic.

**Eventual periods.** If a period `M` only holds for `n ≥ N0`, choose `k` so that both `2^k n` and `2^k(n + M)` exceed `N0`. They differ by a multiple of `M`; the first identity gives `h(n) = h(n + M)`. So eventual periodicity is global periodicity here. For `d = 1` the classification forces constancy. ∎

## Certificates

- [`verify_examples.py`](verify_examples.py) (under a second): replays V002's bounded examples against [`verification.json`](verification.json): 480 finite colouring partitions, and the exact examples of the survey notes. Its own docstring says these checks do not prove all-modulus rigidity.
- [`check_legacy_replay.py`](check_legacy_replay.py) (about 15 s): replays the side lane's [`v13_coloring_check.py`](v13_coloring_check.py) through `tools/legacy_replay.py`, requiring exit 0 and its receipt [`v13_coloring_check.json`](v13_coloring_check.json) reproduced byte for byte: in 2,400 cases (`M ≤ 400`, `d ∈ {1, 5, 7, 11, 13, 61}`) the residue graph mod `M` with edges `r – 2r` and, on odd residues, `r – 3r + d` has as many components as there are `⟨×2, ×3⟩`-orbits on `Z/gcd(M, d)Z`, always 1 for `d = 1`; the controls `1_(5|n)`, `1_(61|n)` are invariant.

## Lean

Two Lean units of the Lean lane (receipts in [`lean/receipts/`](../../../../lean/receipts/), axioms `propext`, `Classical.choice`, `Quot.sound` only; some declarations need fewer):

- **Unit 1**, [`lean/PeriodicRigidity.lean`](../../../../lean/PeriodicRigidity.lean): `LeanLane.periodic_invariant_const` takes `h : ℕ → α`, `0 < M`, `∀ n, h (n+M) = h n`, `∀ n, h (2n) = h n`, `∀ n, Odd n → 1 < n → h (3n+1) = h n`, and concludes `∀ n, 0 < n → h n = h 1`. Hypotheses over all of ℕ cost nothing: a colouring of the positive integers with period `M` extends to 0 by `h 0 := h M`. `LeanLane.control_three_x_plus_five` is the `3x+5` control with `1_{5|n}`.
- **Unit 1b**, [`lean/GeneralPeriodic.lean`](../../../../lean/GeneralPeriodic.lean), namespace `LeanLane.GenPer`, for every **odd** `d` (`3 | d` allowed, beyond this node's scope): `invariant_classification` (an `M`-periodic invariant is `gcd(M, d)`-periodic with `h(2n) = h(n)` and `h(3n) = h(n)` for all `n`); `factors_through_zmod` (an explicit `F : ZMod (gcd M d) → α` with `h n = F n`, `F(2z) = F z = F(3z)`, i.e. constant on the classes generated by ×2 and ×3); `invariant_of_class_function` (the converse, for every `g | d`); `period_gcd_six_free` (for `3 | d` the period divides `gcd(M', d)` with `M'` the six-free part of `M`, which is stronger); `eventually_periodic_invariant` (the eventual-period paragraph, with conclusions on `n ≥ 1`, since an eventual period leaves `h 0` unconstrained); `control_indicator` (`1_{d|n}` is a nonconstant invariant for odd `d` with `3 ∤ d`; `3 ∤ d` is needed, since for `d = 3` the indicator is not invariant), instantiated as `control_five` and `control_sixty_one`.

**Statement match.** Together the two units state the theorem, its converse, the eventual-period statement and the controls, for every odd `d` (so in particular for the claim's `3 ∤ d`). The rule is assumed only at odd `n > 1`; under periodicity the rule at `1 + 2M` implies the rule at 1, so this costs nothing (side lane, feed 22:42). The Lean route differs in form (representatives `x + M` or `x + 2M` instead of large odd representatives; the factor 3 removed by `6(x+K) + d ≡ 6x + d (mod 3K)` instead of `B^b`; `period_gcd` by the Euclidean algorithm) but reaches the same statement.

## Remarks

**Where it sits.** This is the first rigidity theorem of the invariants area and the reason the viewpoint survey selected "arithmetic regularity of component colourings" (card V13) as its working language ([`viewpoint-language-survey`](../../attempts/viewpoint-language-survey/README.md)). Its question: if some integers never reach 1, how complicated must an arithmetic description separating their components from the component of 1 be? All invariant colourings being constant is just convergence; there is no reason supplied here for an actual hypothetical bad-set indicator to be periodic, automatic, continuous on a compactification, or approximable by such functions. The theorem classifies a restricted class only.

**Later results.** Periodicity was replaced by finite automata in [`binary-automatic-invariant-colourings-constant`](../binary-automatic-invariant-colourings-constant/README.md) (V004, conditional on Cobham's theorem), whose finish reuses this residue argument in the odd form of [`odd-eventually-periodic-invariants-constant`](../odd-eventually-periodic-invariants-constant.md); its `3x+d` version is [`d-uniform-automatic-invariant-colourings`](../d-uniform-automatic-invariant-colourings/README.md). The side lane's profinite reading (Furstenberg's ×2×3 rigidity, Cobham as the automata analogue, this theorem as the clopen case) and its finite question are recorded in [`invariant-sets-meet-every-residue-class`](../../questions/invariant-sets-meet-every-residue-class.md).

**Card fields (V13).** The legacy card also recorded: the cheapest next test (compare finite binary kernels rather than periods; under `d = 1` invariance `h(3n+2) = h(2n+1)` controls one ternary section but not the full ternary kernel), which became [`binary-kernel-first-ternary-image`](../binary-kernel-first-ternary-image/README.md) and then V004; and the prior-work distinction that regular languages of ancestors exist at each **fixed** number of odd shortcut branches (Stérin, arXiv:1907.00775, Theorem 1, crediting Shallit–Wilson), which does not give one automaton for a whole basin, since regular languages are not closed under countable unions.

**Novelty.** The legacy text claims none; it is "within the established functional-equation tradition". Novelty undetermined. The written argument was independently agent-reviewed in the main lane at the time; the side lane's finite check and the Lean units are the independent records.

## History

- Migrated from `experiments/viewpoints/V002/invariant_colors.md` (legacy ID V002; the V13 card with its appendix) at commit `be73a66`, by the B16 migration (Claude, Opus 5.5). V002's other notes (selection review, relational and geometric tests, statistical cards) moved to [`viewpoint-language-survey`](../../attempts/viewpoint-language-survey/README.md), and the V14 card `base_conversion.md` to [`binary-ternary-carry-frontier`](../../attempts/binary-ternary-carry-frontier/README.md). The side-lane check `reviews/side_lane/v13_coloring_check.*` moved here.
- Main lane (ChatGPT/Codex), 2026-10-18, main commit `cdfb143`. Lean unit 1 verified at Lean-lane iteration 1, unit 1b at iteration 8 (`claude/lean-lane` `79e8a69`); side-lane referee 18:24 and 22:42.
- The card's §§1–3 and §§6–7 (objects, structural gain, translated gap, next test, milestone) are condensed into the Remarks; the appendix proof is kept verbatim in substance under `## Proof`.
