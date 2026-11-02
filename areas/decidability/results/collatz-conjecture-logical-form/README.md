---
id: collatz-conjecture-logical-form
kind: result
title: "The logical form of the Collatz conjecture: the cycle half is Π⁰₁, the whole is Π⁰₂, and a halting reduction into 3x+1 orbits would refute it"
status: written
claim: >
  For the Collatz map T on the positive integers: (1) for each n, "n reaches 1" is a Σ⁰₁ statement, and every true
  instance is provable in Peano arithmetic (PA); the set R of integers reaching 1 is recursively enumerable. (2) For
  each m, "the odd-only map has no cycle of period m other than {1}" is decided by a finite search, because a cycle
  word of length m has total A with 3^m < 2^A ≤ 4^m; hence "no nontrivial cycle" (NC) is a Π⁰₁ sentence. (3) The
  conjecture C, "every n reaches 1", is Π⁰₂, and C is equivalent to NC together with "no orbit is unbounded".
  Consequences: (a) if NC is false, PA proves it false; so if NC is independent of PA (or of any Σ⁰₁-sound
  extension), NC is true; (b) if C is independent of PA, then C can fail only through an unbounded orbit; (c) the
  problem "given n, does n reach 1?" is decidable if C is true (the answer is always yes), so it can be undecidable
  only if C is false; (d) there is no computable map from Turing machines M to integers n_M with "n_M reaches 1 iff
  M halts" unless C is false, and any such map would hand out an explicit counterexample n_M for any machine M that
  provably never halts. A single sentence such as C is never "undecidable" as an algorithmic problem; the meaningful
  notions are independence of a theory, and undecidability of a family of instances in which something varies.
authors:
  - Claude cycles lane (Opus 5.5; directed by Santiago Armstrong)
created: 2026-11-01
depends_on: []
certificates: [check_cycle_decision.py]
evidence:
  - "cycle_decision.json: the receipt; the finite cycle search of part (2) run for 3x+1 to period 12, and for the controls 3x+5, 3x+7, 3x+13 to period 7, cross-checked against direct iteration"
tags: [decidability, logic, arithmetic-hierarchy, independence, cycles]
---

# The logical form of the Collatz conjecture

## Statement

`T` is the Collatz map on `Z_(>0)` (`n/2` for even `n`, `3n + 1` for odd `n`), and `S` the odd-only map `n ↦ (3n + 1)/2^(v₂(3n+1))` on odd `n`. Write `R = {n : T^k(n) = 1 for some k}`.

1. **Each instance is Σ⁰₁.** "`n ∈ R`" is `∃k T^k(n) = 1`, a Σ⁰₁ formula (bounded computation inside). Every true Σ⁰₁ sentence is provable in PA (even in Robinson arithmetic), so for every `n ∈ R` PA proves `n ∈ R`. The set `R` is recursively enumerable: run the orbit and wait.
2. **The cycle half is Π⁰₁.** For each `m`, the statement `P(m)`: "the odd-only map has no cycle of period exactly `m` other than `{1}`" is decided by a finite search. Hence `NC := ∀m P(m)` ("no nontrivial cycle") is a Π⁰₁ sentence.
3. **The whole conjecture is Π⁰₂.** `C := ∀n ∃k T^k(n) = 1`, and `C ⟺ NC ∧ NU`, where `NU` says every orbit is bounded.

**Consequences.**

- (a) If `NC` is false, a nontrivial cycle is a finite witness, and PA proves `¬NC`. Contrapositively, if `NC` is independent of PA (or of any theory containing Robinson arithmetic that proves no false Σ⁰₁ sentence), then `NC` is **true**.
- (b) If `C` is independent of PA, then by (a) applied to its cycle half, either `NC` is provable or it is independent and true; either way `NC` holds, so `C` can only fail through an unbounded orbit. Independence of a Π⁰₂ sentence does not by itself make it true.
- (c) The decision problem "given `n`, is `n ∈ R`?" is solved by the program that always answers *yes* if `C` holds. So it can be undecidable only if `C` is false (and then only if `R` is not co-r.e.).
- (d) Suppose `M ↦ n_M` is computable with `n_M ∈ R ⟺ M halts`. Then `R` would be undecidable, so `C` is false by (c). More directly: for any machine `M` that provably never halts (say, a one-line infinite loop), `n_M` is an explicit integer not in `R`. **Encoding arbitrary machines into the orbits of the fixed `3x+1` map, with "reaches 1" as the halting signal, is therefore at least as hard as disproving the conjecture.**
- (e) **Single sentences versus families.** A decision problem has infinitely many instances. A single sentence such as `C` has one answer, so one of the two constant programs "print yes" and "print no" decides it; we just do not know which. "Undecidable" applies to families in which something varies (the map in [Conway](../../../../sources/conway-1972-unpredictable-iterations.md) and [Kurtz–Simon](../../../../sources/kurtz-simon-2007-generalized-collatz.md), the starting value, a word list as in [`synchronised-coding-pcp-reduction`](../synchronised-coding-pcp-reduction/README.md)). For a single sentence the meaningful notion is independence of a theory.

## Proof

(1) is the definition plus Σ⁰₁-completeness of PA (a true existential statement about a terminating computation is proved by exhibiting the computation).

(2) A cycle of the odd-only map with states `n_1, …, n_m` and valuations `a_i` satisfies `2^(a_i) n_(i+1) = 3n_i + 1` cyclically; multiplying, `2^A·Π n_i = Π(3n_i + 1)`, so `3^m < 2^A ≤ 4^m` with `A = Σ a_i`, and equality on the right only for `n_i = 1` (this is Theorem 1 of [`cycle-length-lower-bound-from-convergents`](../../../cycles/results/cycle-length-lower-bound-from-convergents/README.md) with `L ≥ 1`). So `A` ranges over a finite set and the word `w = (a_1, …, a_m)` over finitely many compositions of `A`. For each candidate the cycle equation `x_0·D_w = C_w` (with `D_w = 2^A − 3^m`, `C_w` the intercept; [`conventions/NOTATION.md`](../../../../conventions/NOTATION.md) §2) gives the only possible starting state `x_0 = C_w/D_w`, and `w` is a cycle word iff `x_0` is a positive odd integer whose orbit follows `w` for `m` steps. This is a finite computation, so `P(m)` is decidable and `NC = ∀m P(m)` is Π⁰₁. A cycle of `T` contains odd states and is a cycle of `S`, so `NC` for `S` is `NC` for `T`.

(3) `C` has the displayed form. If every orbit reaches 1, there is no nontrivial cycle and every orbit is bounded. Conversely, a bounded orbit is eventually periodic, so it enters a cycle; under `NC` that cycle is `{1, 4, 2}`.

(a)–(e) follow as stated: (a) from (2) and Σ⁰₁-completeness; (b) from (a) and (3); (c) and (d) from the definitions and the undecidability of the halting problem; (e) is the definition of a decision problem. ∎

## Certificates

[`check_cycle_decision.py`](check_cycle_decision.py) (standard library, about 15 s) implements the decision procedure of (2) for the odd-only `3x+d` map (bound `3^m < 2^A ≤ (3+d)^m`, cycle states coprime to `d`): **V1** for `3x+1` and every period `m ≤ 12` it finds only the trivial cycle `{1}`; **V2** for `3x+5`, `3x+7`, `3x+13` and periods `≤ 7` it finds exactly the cycles reached by direct iteration from odd seeds below 20,000 (3, 1 and 8 cycles, including the fixed point 1 of `3x+5` and `3x+13`); **V3** the receipt [`cycle_decision.json`](cycle_decision.json). The certificate illustrates the procedure; the periods it covers are far below the known period bounds and add nothing to them.

## Remarks

- **Why this node exists.** The decidability area must not overclaim. Every undecidability statement in it concerns a family with a varying input, and (d) shows why the obvious route (simulate a machine inside the orbits of `3x+1`) cannot be taken without first disproving the conjecture. Constructions that embed computation must put the hardness elsewhere, as the PCP reduction does: there every encoded orbit reaches 1 and the hardness is in synchronising two codings.
- **Controls.** Parts (1)–(3) hold for every `3x+d`. They are consistent with the controls, whose nontrivial cycles are finite witnesses of `¬NC` for those maps, as (a) predicts.
- **Novelty.** None; these are standard observations of logic applied to the problem, recorded here with exact scope. The Π⁰₁ form of the cycle statement and the Π⁰₂ form of the conjecture are folklore (see [`lagarias-1985-survey`](../../../../sources/lagarias-1985-survey.md) for the problem's literature; the specific framing here was not checked against it).

## History

- Written 2026-11-01 by the Claude cycles lane (Opus 5.5), directed by Santiago Armstrong, as the scoping node of the new decidability area.
