---
id: universal-w5-tripling-currents
kind: question
title: Does every W5 tripling pair have a finite exact current?
status: open
claim: >
  Odd-only 3x+1 map S on positive odd integers, absorbing at 1, killed atom [1] = 0; P(w) = [3w] - [w]; W5 = {w
  = 5 mod 8}. Prove or refute: for every w in W5 there is a finite integer current J_w with div J_w = P(w), with
  no uniform cost, height, clock or computability assumption. By critical-nine-elimination this is equivalent to
  every positive odd integer reaching 1, so it is a full-strength convergence target, not a helper lemma. By
  critical-image-rank-composition it suffices to supply the currents on W5 minus the accepted domain of any
  finite union of rules that strictly decrease rho(w) = nu(3w).
created: 2026-10-17
---

# Does every W5 tripling pair have a finite exact current?

## Question

Odd-only clock, `S(x) = (3x+1)/2^v2(3x+1)`, 1 absorbing, `[1] = 0`, `P(w) = [3w] − [w]`, `W5 = {w ≡ 5 (mod 8)}`, `ν` the elementary normal form of [`elementary-bridge-quotient-normal-form`](../results/elementary-bridge-quotient-normal-form/README.md) and `ρ(w) = ν(3w)`.

**Target.** For every `w ∈ W5`, construct (or refute the existence of) a finite integer current `J_w` with `div J_w = P(w)`. No uniform cost, height, clock or computability is required.

The form other nodes use: the "missing premise" of every critical-pair rule from R40 onwards is a supplied exact current for each request `P(u)`, `u ∈ W5`, that the rule leaves unresolved. A rule whose requests all have `ρ(u) < ρ(w)` removes its accepted domain from the premise ([`critical-image-rank-composition`](../results/critical-image-rank-composition/README.md)).

## Why it matters

- It is **equivalent to Collatz convergence** of every positive odd integer: [`critical-nine-elimination`](../results/critical-nine-elimination/README.md) supplies every `W9` pair from `W5` pairs, and [`critical-tripling-domain-equivalence`](../results/critical-tripling-domain-equivalence/README.md) turns universal pair currents on `W5 ∪ W9` into convergence; conversely absorption currents of `3w` and `w` give their difference. An answer is therefore exactly as hard as the convergence half of the conjecture; proving it would prove that half, and the equivalence itself is not progress towards it.
- Every conditional constructor of the R41–R60 rounds (below) is a reduction of this premise to a smaller explicit residual set.

## Known progress

All of the following are conditional reductions; none supplies a current for an unresolved request.

- **Sufficient sets.** [`decreasing-w5-phase-inverse-barrier`](../results/decreasing-w5-phase-inverse-barrier/README.md) (R41) removes `E_good = {w ∈ W5 : 3 | w, 3w selected, w ≢ 3 (mod 9)}`; the returning row `w ≡ 3 (mod 9)` is an exact self-request. [`critical-image-rank-composition`](../results/critical-image-rank-composition/README.md) (R43) composes any strict-`ρ` rules and removes their union.
- **Strict-`ρ` rules on further domains:** [`returning-forward-interface`](../results/returning-forward-interface/README.md) (R44), [`base-inverse-phases-increasing-pairs`](../results/base-inverse-phases-increasing-pairs/README.md) (R45), [`variable-depth-inverse-escape-barrier`](../results/variable-depth-inverse-escape-barrier/README.md) (R46), [`nonselected-multiples-inverse-interface`](../results/nonselected-multiples-inverse-interface/README.md) (R47), [`forward-blocks-low-exponent-tests`](../results/forward-blocks-low-exponent-tests/README.md) (R48), [`two-inverse-phases-intermediate-increase`](../results/two-inverse-phases-intermediate-increase/README.md) (R50), [`returning-second-forward-interface`](../results/returning-second-forward-interface/README.md) (R52), [`low-block-continuation-prescribed-growth`](../results/low-block-continuation-prescribed-growth/README.md) (R53), [`selected-critical-five-forward-tables`](../results/selected-critical-five-forward-tables/README.md) (R55), [`two-selected-inverse-choices`](../results/two-selected-inverse-choices/README.md) (R56), [`guarded-cycle-exit-phases`](../results/guarded-cycle-exit-phases/README.md) (R57), [`rank-excess-absorption-classification`](../results/rank-excess-absorption-classification/README.md) (R58), [`deferred-original-rank-testing`](../results/deferred-original-rank-testing/README.md) (R59) and [`maximal-inverse-cycle-continuation`](../results/maximal-inverse-cycle-continuation/README.md) (R60); the fixed union of the first twelve families is [`twelve-family-rho-dispatcher`](../results/twelve-family-rho-dispatcher/README.md). A separate rank `σ` is [`sigma-rank-removes-absorption-overhead`](../results/sigma-rank-removes-absorption-overhead/README.md) (R51); the two ranks cannot be mixed automatically ([`rho-sigma-rank-mixing`](../attempts/rho-sigma-rank-mixing/README.md)).
- **Scoped obstructions to named procedures:** bounded-depth inverse descent fails ([`decreasing-w5-phase-inverse-barrier`](../results/decreasing-w5-phase-inverse-barrier/README.md), [`variable-depth-inverse-escape-barrier`](../results/variable-depth-inverse-escape-barrier/README.md)); inverse-only search cannot enlarge a forward-closed history ([`inverse-only-exclusions-short-forward`](../results/inverse-only-exclusions-short-forward/README.md)); a fixed lookahead with the seven direct rules leaves an unhandled leading input ([`growing-prefix-unhandled-leading-input`](../results/growing-prefix-unhandled-leading-input/README.md)); the joint-source block of R39 keeps an unbounded positive frontier ([`joint-source-unbounded-frontier`](../results/joint-source-unbounded-frontier/README.md)).
- **Measurements, not theorems.** The side lane's samplers (in the folders of [`critical-image-rank-composition`](../results/critical-image-rank-composition/README.md), [`two-inverse-phases-intermediate-increase`](../results/two-inverse-phases-intermediate-increase/README.md) and [`twelve-family-rho-dispatcher`](../results/twelve-family-rho-dispatcher/README.md)) report size-stable acceptance shares of about 18%, 43% and 70% of `W5` for the four-, seven- and twelve-family dispatchers. They give no asymptotic or universal coverage statement.
- The later legacy rounds R61–R94 (`experiments/residual_progress/`, batches B12–B13, not yet migrated) continue this line.

## Suggested attacks

- The side lane's quotient stopping-time reformulation (feed 2026-10-18 00:53, migrating with R62 in a later batch): a strict-`ρ` recursion for all of `W5` is the same as every `q = ν(3w)` reaching a quotient state below `(8q − 5)/9`. It turns rule recognition into a stopping-time statement; it does not make that statement easier.
- Eliminate every retained high or original request by a compatible further comparison, or prove a different well-founded recursion covering them (the main lane's own decision, `side_lane_review_767af32.md` in [`two-selected-inverse-choices`](../results/two-selected-inverse-choices/README.md)). Any argument must use arithmetic that fails for the `3x+d` controls of `conventions/NOTATION.md` §3: the generic pair statement fails on `W` for `3x−1`, `3x+13` and `3x+61` ([`critical-tripling-domain-equivalence`](../results/critical-tripling-domain-equivalence/README.md), Remarks).
