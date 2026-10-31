---
id: outer-profile-closure-obstruction
kind: result
title: Forward pushforwards of the annulus need ever finer ternary moduli, so no fixed-modulus profile family is closed
status: reviewed
claim: >
  Odd-only 3x+1 map, absorbing at 1; A_N the annulus of disjoint-annular-recursion, 8 | N, Q = 9N/4. For every
  t ≥ 0, on odd y with (3/2)^t·(32Q + 1/3) < y + 1 ≤ 64·(3/2)^t·Q, (P^t A_N)(y) = 3·1[3^(t+2) | y+1] − 1 if
  3^(t+1) | y+1, and 0 otherwise; this profile has least even period 2·3^(t+2). Consequently no finite fixed
  list of periodic residue profiles on intervals, with a number of interval pieces bounded independently of N
  for each fixed t, represents all the iterates P^t A_N along an allowed dyadic ray. Scope: literal
  synchronous pushforward only; growing moduli, a number of pieces growing with the scale, algebraic current
  rewrites before transport and unequal-time cancellation are not excluded, and nothing is claimed about
  aggregate historical exposure depths.
authors:
  - ChatGPT main lane (Codex)
created: 2026-10-17
depends_on: [disjoint-annular-recursion]
evidence:
  - "../universal-annular-partial-current/check_arithmetic_reductions.py, arithmetic_audit.json: the legacy checker, which checks the outer profile at cutoffs 8, 24, 96, 128 and depths 0–4. Fails at its new path (it loads experiments/current_construction/recursive/check_annular_recursion.py by its legacy path); passed at be73a66 inside scripts/verify_all.py (archive/legacy-checker-run-be73a66.md)"
reviewed_by:
  - by: Claude review lane (Fable 5.1; directed by Santiago Armstrong)
    date: 2026-10-31
    link: REVIEW-2026-10-31-claude-review-lane.md
    scope: "Full re-derivation of the outer-profile theorem (exceptional-step bound, unique all-one source, residue translation), of the period statement and of the closure corollary; independent exact pushforward at the 20 cutoffs N = 8..160 and depths 0-6 (1,945,710 strip values, strip shown sharp, input measure cross-checked against P.V_N); no certificates exist to run; node converted to a folder; verdict HOLDS"
aliases: [R9-b]
tags: [convergence, packet-currents, annular, forward-transport, obstruction]
---

# Forward pushforwards of the annulus need ever finer ternary moduli, so no fixed-modulus profile family is closed

## Statement

Odd-only clock, absorbing at 1; `A_N` and `Q = 9N/4` as in [`disjoint-annular-recursion`](../disjoint-annular-recursion/README.md), `8 | N`. Put `λ = 3/2`.

**Theorem (outer profile).** For every integer `t ≥ 0`, on odd states `y` in the strip

```
λ^t·(32Q + 1/3) < y + 1 ≤ 64·λ^t·Q,
```

one has

```
(P^t A_N)(y) = 3·1[3^(t+2) | y+1] − 1    if 3^(t+1) | y+1,       and 0 otherwise.
```

In particular the coefficient is `+2` at every positive state in this strip with `y ≡ −1 (mod 2·3^(t+2))`.

**Corollary (scoped closure obstruction).** On odd integers this nonzero periodic function has least even period `2·3^(t+2)`. There is no representation of all the forward iterates `P^t A_N` using a finite fixed list of periodic residue profiles on intervals, with a number of interval pieces bounded independently of `N` for each fixed `t`.

## Proof

From §3 of the legacy note `ARITHMETIC_RESULTS.md` (now [`universal-annular-partial-current`](../universal-annular-partial-current/README.md)), kept as written.

**Outer profile.** Let `T(x) = (3x + 1)/2`. Its iterates are `T^t(x) = λ^t·(x + 1) − 1`, and all Syracuse trajectories are bounded above by them. If one of the first `t` valuations is at least 2, bound the other steps by `T` and the exceptional step by `T/2`; the largest resulting value occurs when the exceptional step comes first. Since every annular source is at most `64Q − 1`, its endpoint then obeys `y + 1 ≤ λ^t·(32Q + 1/3)`. Thus every contribution in the displayed strip has the all-one valuation word. Its unique possible source is

```
x = 2^t·(y + 1)/3^t − 1,
```

which lies in the original top band. The top-band coefficient is `−1` on `x ≡ 5, 11 (mod 18)`, `+2` on `x ≡ 17 (mod 18)`, and zero elsewhere. Substitution gives exactly the formula above; the divisibility conditions also guarantee integrality and the exact all-one branch. For `t = 0` this is the original top-band row. ∎

**Period.** The value at `−1` is 2, while translating `−1` by an even integer `M` with `3^(t+2) ∤ M` gives value 0 or `−1`. ∎

**Closure obstruction.** Let `M` be a common even modulus of the alleged finite list. Choose `t` with `v₃(M) < t + 2`. As `N` grows along any allowed dyadic ray, the outer strip grows without bound. One interval piece must then contain enough complete periods to witness two points separated by `M` with different coefficients, a contradiction. ∎

## Remarks

- **Scope.** This excludes a finite fixed-modulus profile ansatz under literal forward pushforward. It does not exclude growing moduli, a number of pieces growing with the scale, or algebraic current rewrites before further transport; it permits unequal-time cancellation; and it does not prove that aggregate historical exposure depths are unbounded ([`uniform-aggregate-exposure-depth`](../../questions/uniform-aggregate-exposure-depth.md)); that was later proved by a different, inverse-history argument in [`unbounded-exposure-depth-necessary`](../unbounded-exposure-depth-necessary/README.md).
- **Consequence for constructions.** The original six-band fixed-modulus family is not closed under literal repeated pushforward. A successful closure must carry growing arithmetic information or change the representatives by exact currents (round report, now [`archive/convergence-annular-construction/REPORT.md`](../../../../archive/convergence-annular-construction/REPORT.md)). The positive `+2` atoms are contributions that have not disappeared in a signed norm estimate such as [`annular-root-collapse-contraction`](../annular-root-collapse-contraction.md).
- Novelty undetermined.

## History

- Migrated from `experiments/annular_construction/arithmetic/ARITHMETIC_RESULTS.md` §3 (part of the legacy R9 round; alias `R9-b`) at commit `be73a66`, by the B08 migration (Claude, Opus 5.5). Legacy status: "written identity and finite arithmetic checks".
- Main lane (ChatGPT, Codex), 2026-10-17, commit `ce56699`. No review from another lane is on record.
- 2026-10-31: reviewed by the Claude review lane (Fable 5.1; directed by Santiago Armstrong); status raised to reviewed. No corrections. For the review the node was converted from the single file `outer-profile-closure-obstruction.md` to this folder, its relative links repaired, and the links to it in `annular-root-collapse-contraction`, `universal-annular-partial-current`, `uniform-aggregate-exposure-depth` and `five-ray-annular-current-supply` repointed. Review: [`REVIEW-2026-10-31-claude-review-lane.md`](REVIEW-2026-10-31-claude-review-lane.md).
