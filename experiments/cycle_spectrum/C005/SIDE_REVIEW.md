# C005 — External input and scope review

Reviewed local remote-tracking commit
`67c691b93ddd3d07748f557c8a26f9883e37389b` of `origin/claude/sidekick`.
Read `archive/side_lane/DIRECTIONS.md` and the new `archive/side_lane/FEED.md` entries with
`git show`. A fresh fetch was attempted, but automatic approval review
could not execute because its selected model was at capacity. This is
a tooling failure, not evidence that the branch is current or the action
unsafe. Independent mathematics can continue. No side branch was edited.

## New evidence and proposals

- The C004 referee reports a different finite word grid and an exact
  match of the narrow spectrum with the stored census. This agrees with
  the written main theorem. Its finite checks remain reported external
  checks; main's C005 checker separately exercises its declared domain.
- The C003 referee reports the effective contracting bound and an
  algebraic derivation of the same inequality. It does not extend the
  theorem to arbitrary words or supply an effective threshold for the
  separate asymptotic statement.
- The Lean report now states that `uniform_two_block_strong` at
  `325130a` proves C002's full bound, including the factor `2^A/3^m`.
  The earlier mismatch concerned the earlier declaration, and is no
  longer the lane's reported scope. Main has not independently built or
  replayed that commit. Its reports do not formally verify C005.
- The proposed test of cycles spanning more than one dyadic range is
  aligned with C005's mechanism. A fixed ratio restriction is a proper
  subclass. Proving exclusion for every finite ratio bound would cover
  every finite cycle, and is not a smaller completion criterion.

## Discrepancy qualification

Do not identify `H<2L` with discrepancy less than one when discrepancy
is centered on `log_2(3)` over a full period. The primitive raw word
`(2,3)` gives the parameter-23 cycle `7 -> 11 -> 7`: its ratio is
`11/7<2`, while the full-period discrepancy is
`5-2*log_2(3)>1` (equivalently `32>18`). The C004 equivalence is with
mechanical coding using its actual rational slope `A/m`. Changing the
center or dropping the accumulated additive error needs a separate
argument. The earlier `m/L` qualification remains necessary.

## Directions and research scope

D1/D2 remain evidence and controls; D3 remains rejected as stated;
D4 is deferred; D5 is standing; D6 is historical; D7 remains the useful
formal-input audit standard; D8 belongs to the replaced quantitative
goal. None of these external proposals changes the active goal.

The preceding chat proposed bounded-denominator finiteness as a possible
major milestone. That recommendation did not activate a replacement
goal. C005 continues the original cycle-exclusion objective.

The primary-source search on dyadic normalization and cycle order did
not supply a theorem that licenses the proposed extension. The
[C004 proof](../C004/ROTATION_LATTICE.md) and
[mechanical denominator argument](../../residual_progress/lattice_cycles/BALANCED_DENOMINATORS.md)
are the exact local inputs. Related source material includes
[Halbeisen–Hungerbuehler](https://people.math.ethz.ch/~halorenz/publications/pdf/collatz.pdf)
and [Knight's publisher preview](https://www.sciencedirect.com/science/article/pii/S0012365X25004200),
with the limitations already recorded in C004. No novelty claim or new
external mathematical premise is adopted here.
