---
id: nonabsorbing-set-linear-lower-density
kind: result
title: A nonempty nonabsorbing set inherits every fixed-target predecessor lower bound, so it is empty or of positive lower density
status: written
claim: >
  Odd-only 3x+1 map S, absorbing at 1; B the positive odd seeds that never reach 1; B~ = {n >= 1 : oddpart(n) in
  B}; tau_1 the absorbed odd-arrow hitting time of 1. If m is in B then a = S(m) is odd, greater than 1, not
  divisible by 3, in B, and every predecessor of a is in B. Hence (i) assuming Lau's formal theorem
  (L = 2^(2^(2^87640))): #(B~ cap [1,X)) >= X/(a^4 L) for every integer X >= 2^(a^3 L), so B is empty or has
  positive lower density; consequently the statistical condition C.2a (for every rational epsilon > 0 and integer
  M >= 1 there are finite X >= M, H >= 0 with at most epsilon X of the n < X having tau_1(oddpart(n)) > H) is
  equivalent to convergence of every positive integer; (ii) assuming Krasikov-Lagarias's bound pi_a(X) >= X^0.84,
  any eventual bound #{1 <= n <= X : tau_1(oddpart(n)) > H(X)} <= C X^(0.84 - epsilon), with C, epsilon > 0 and
  any finite horizons H(X), implies convergence (C.1 plus C.2 implies convergence). Both are conditional
  reformulations; neither upper condition is proved, and both fail for 3x+d, d > 1.
authors:
  - ChatGPT main lane (Codex)
created: 2026-10-18
assumes: [lau-2026-positive-density, krasikov-2003-predecessors]
depends_on: [lau-density-formal-replay]
lean: [LeanLane.Dichotomy.bad_positive_lower_density, LeanLane.Dichotomy.collatz_of_bad_density_zero]
aliases: [P6-C.3]
tags: [convergence, phase6, predecessors, density, nonabsorbing-set, conditional, zero-one-law]
---

# A nonempty nonabsorbing set inherits every fixed-target predecessor lower bound, so it is empty or of positive lower density

## Statement

Odd-only clock, `S(n) = (3n+1)/2^v2(3n+1)`, absorbing at 1. `B` is the set of positive odd nonabsorbing seeds, `B~ = {n ≥ 1 : oddpart(n) ∈ B}` its all-integer version, and `tau_1(n)` the number of absorbed odd arrows from odd `n` to 1 (infinite on `B`).

**Inheritance.** If `m ∈ B`, then `a = S(m)` is odd, `a > 1`, `3 ∤ a` (since `3m + 1` is a ternary unit) and `a ∈ B`. Every odd predecessor of `a` is in `B`: the raw odd map fixes 1, so a path cannot pass through 1 before reaching `a`.

**(i) Linear lower density, assuming [`lau-2026-positive-density`](../../../../sources/lau-2026-positive-density.md).** With `L = 2^(2^(2^87640))`, `c(a) = 1/(a^4 L)` and `X_0(a) = 2^(a^3 L)`:

```
#(B~ ∩ [1, X)) >= c(a) X    for every integer X >= X_0(a).
```

So `B` is either empty or of positive lower density (the side lane's "zero–one law", feed 18:08). The **C.2a** condition (the question [`nonabsorbed-fraction-arbitrarily-small`](../../questions/nonabsorbed-fraction-arbitrarily-small.md)) is therefore equivalent to convergence.

**(ii) Power-saving form, assuming [`krasikov-2003-predecessors`](../../../../sources/krasikov-2003-predecessors.md).** A bound `#{1 ≤ n ≤ X : tau_1(oddpart(n)) > H(X)} ≤ C X^(0.84 − epsilon)` for all `X ≥ X_0`, with constants `C, epsilon > 0` and finite horizons `H(X)` (the question [`unabsorbed-count-power-saving`](../../questions/unabsorbed-count-power-saving.md), route node C.2), implies convergence. This is route node C.3's interface.

## Proof

**Inheritance** is shown in the statement.

**(i).** For every finite odd-arrow horizon `H`, the seeds of `B~` below `X` lie in `{1 ≤ n < X : tau_1(oddpart(n)) > H}`. Taking `epsilon = c(a)/2` and `M = X_0(a)` in C.2a would supply some finite `X ≥ M` with at most `epsilon X` late seeds below `X`, contradicting the lower bound. Conversely, convergence gives a finite maximum hitting time at each finite cutoff, hence C.2a with any `X ≥ M` and `H` that maximum. The lower theorem thus makes C.2a an exact remaining convergence obligation; it does not establish that upper condition.

**(ii).** On a hypothetical nonabsorbing odd orbit choose `a = S(n)`; then `3 ∤ a` and every positive integer predecessor of `a` (all integers, in the shortcut clock of Krasikov–Lagarias; odd targets have the same reachability in the odd-only clock) is nonabsorbing. Krasikov–Lagarias Theorem 6.1 gives `X^0.84 ≤ π_a(X)`, and all of these are late at every finite horizon, so `X^0.84 ≤ C X^(0.84 − epsilon)` for all sufficiently large `X`, impossible once `X^epsilon > C`. Counting all integers avoids confusing published inverse counts with odd-only seed counts; the initial removal of powers of 2 changes clocks but not membership.

## Lean

The positive branch and the contrapositive of (i) are formalised by the Lean lane in [`lean/Dichotomy.lean`](../../../../lean/Dichotomy.lean) (receipts [`lean/receipts/Dichotomy.axioms.txt`](../../../../lean/receipts/Dichotomy.axioms.txt): `propext`, `Classical.choice`, `Quot.sound`), over `Solution.Basic` of the external library:

- `LeanLane.Dichotomy.bad_positive_lower_density`: if some positive `n` never reaches 1 under the ordinary map `collatz` (`Bad n`), there are a rational `c > 0` and `X₀` with `c·N ≤ #{n < N : 0 < n ∧ Bad n}` for every `N ≥ X₀`; the witnesses are the external theorem's constants at the bad target `t = 3m + 1`, `m` the odd part of the given bad `n`.
- `LeanLane.Dichotomy.collatz_of_bad_density_zero`: if for every `c > 0` and every `X₀` some `N ≥ X₀` has fewer than `c·N` bad numbers below it (lower density zero, weaker than density zero), every positive integer reaches 1.

**Match with the claim.** The Lean statements use the ordinary map and count all bad positive integers below `N`; the prose uses odd-only `S` and `B~ = {n : oddpart(n) ∈ B}`, which is the same set (halving does not change badness). The Lean witness target `3m + 1` is even; the external theorem's general-target form covers it, whereas the prose uses the odd target `S(m)`, its odd part, so the constants differ by the choice of target, not in kind. The Lean file does not formalise the equivalence with C.2a's quantifiers (finite `H`, `X ≥ M`) or part (ii). It compiles only inside a checkout of the external project (it is not built by this repository's CI; see [`lean/README.md`](../../../../lean/README.md)), so the node stays `written`, with the Lean declarations recorded here.

## Remarks

- **Controls.** For every supported `d > 1` both upper conditions fail: the positive multiples of `d` never reach 1 and have density `1/d` ([`baseline-obligation-transfer-controls`](../baseline-obligation-transfer-controls/README.md)). The qualitative lower premise transfers ([`predecessor-density-conditional-reconstruction`](../predecessor-density-conditional-reconstruction/README.md)); Lau's explicit constants are replayed only at `d = 1`.
- **Not a weakening.** C.2a is Collatz-equivalent: the lower theorem lowers the sufficient counting requirement from a power saving (C.2) to an arbitrarily small late fraction, but the new requirement is still the full problem. Positive predecessor density is not a proof of Collatz, and the historical exponent 0.84 is no longer the strongest audited lower premise here.
- The first attempts at the upper condition are [`c2a-two-level-residue-relaxation`](../../attempts/c2a-two-level-residue-relaxation.md) and [`matched-density-gap-combination`](../../attempts/matched-density-gap-combination.md).

## History

Migrated from `experiments/phase6/linear_density_audit/README.md` (the P6-004 folder overview, legacy batch `P6-004`), at commit `be73a66`; part (ii) is route node C.3 of the Phase 6 route map and audit L3 (now [`route-literature-transfer-audit`](../route-literature-transfer-audit.md)), whose map and ledger are in [`archive/convergence-phase6/`](../../../../archive/convergence-phase6/). The overview's table of artefacts maps to [`lau-density-formal-replay`](../lau-density-formal-replay/README.md) (`lau_scope.md`, `replay_notes.md`, the formal runner and statement generator), [`predecessor-density-conditional-reconstruction`](../predecessor-density-conditional-reconstruction/README.md) (`audit_notes.md`, `terminal_audit.md`, `transfer_scope.md`, the arithmetic checker) and the two attempts above. ChatGPT main lane, 2026-10-18. The Lean dichotomy is the Lean lane's queue item 3 (`Claude Lean lane (Fable)`, verified 2026-10-18, side-lane feed 21:57).
