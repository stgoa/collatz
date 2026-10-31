---
id: first-shell-three-state-rigidity
kind: result
title: A sequence with the three scalar identities and at most three distinct first-shell sections is constant
status: reviewed
claim: >
  Let b be any sequence on n >= 0 with values in an arbitrary set satisfying b(3n) = b(4n), b(3n+2) = b(2n+1) and
  b(4n+2) = b(n) for every n >= 0, and let J_1(b) be the distinct entire sequences among b, E_0 b, E_1 b, T_0 b,
  T_1 b, T_2 b (E_i b(n) = b(2n+i), T_j b(n) = b(3n+j)). If |J_1(b)| <= 3 then b is constant. Hence the odd-value
  sequence of a nonconstant 3x+1 invariant has |J_1(b)| >= 4. Elementary (finite case table); no Cobham, no finite
  output alphabet; it gives no asymptotic growth bound.
authors:
  - ChatGPT main lane (Codex)
created: 2026-10-18
depends_on: [scalar-interface-three-identities]
evidence:
  - "../two-exit-interior-counterexample/ROOT_REVIEW.md: the main lane's derivation and independent audit, with the corrected seven-row case table (sections 2-3) and the constant-output finish (section 4); ../two-exit-interior-counterexample/INDEPENDENT_REVIEW.md: a second main-lane check of the final table"
aliases: [V008-b]
reviewed_by:
  - by: Claude review lane (Fable 5.1; directed by Santiago Armstrong)
    date: 2026-10-31
    link: REVIEW-2026-10-31-claude-review-lane.md
    scope: "Re-derived the six radix identities, the universal relations and all seven table rows with every choice of t, confirmed the constant-output finish, re-checked all 27 first-shell assignments by congruence closure over operator words of length <= 7, and tested the controls b_5 and b_13, which fail the identities; verdict HOLDS"
tags: [invariants, scalar-interface, section-graph, quantitative-rigidity]
---

# A sequence with the three scalar identities and at most three distinct first-shell sections is constant

## Statement

Let `b` be any sequence on `n ≥ 0`, with values in an arbitrary set, satisfying for every `n ≥ 0`

```
b(3n) = b(4n),   b(3n+2) = b(2n+1),   b(4n+2) = b(n),
```

the scalar interface of [`scalar-interface-three-identities`](../scalar-interface-three-identities.md). Let `J_1(b)` be the distinct entire sequences among `b, E_0b, E_1b, T_0b, T_1b, T_2b`. **If `|J_1(b)| ≤ 3`, then `b` is constant.** For a nonconstant Collatz invariant, therefore, `|J_1(b)| ≥ 4`.

## Proof

The written proof is [`ROOT_REVIEW.md`](../two-exit-interior-counterexample/ROOT_REVIEW.md) §§2–4. Use the six radix identities `R0`–`R5` (`T_j E_i = E_l T_k` for `2j + i = 3l + k`). Put `u = E_0 b`. If `u = b`, the root identity `E_1(E_0 b) = b` gives `E_1 b = b`, and `b` is constant by binary reading. Otherwise `u ≠ b`; a third root state, if any, is called `v`; with `p = E_1 b = T_2 b` and `q` the remaining first-shell state, the exhaustive case split over `(p, q)` (after `p, q ∈ {b, u}`, the pairs `(v,b)`, `(v,u)`, `(v,v)`, `(b,v)`, `(u,v)`) either forces constancy, closes a binary-closed family of at most four states inside `{b, u, v, w}` (`w = E_0 v` when needed), or is ruled out. **Finish:** the identities at `n = 0` give `b(2) = b(0)` and `b(2) = b(1)`, so `b(0) = b(1) = b(2)`; the outputs at zero of `b` and its five first children are `b(0), b(0), b(1), b(0), b(1), b(2)`, all equal, and so is the output of the added state; reading any binary expansion inside the closed family ends at that common output, so `b(n) = b(0)` for all `n`. ∎

## Remarks

- **Correction during review (legacy).** One row of an unpublished draft table used an incomplete subset of the radix equations; the omitted equation makes that row inconsistent. It was removed before acceptance, and seven surviving rows give the theorem (`ROOT_REVIEW.md` records the correction).
- **Implicit step.** The Lean lane (iteration 9; side-lane feed 23:23) noted that the finish "all outputs at zero agree" needs `b(0) = b(1) = b(2)`, which follows from the second and third identities at `n = 0`; `ROOT_REVIEW.md` §4 states it.
- **Scope.** It rules out the generic two-exit example at the actual Collatz root ([`two-exit-interior-counterexample`](../two-exit-interior-counterexample/README.md) has three first-shell states and fails `b(4n+2) = b(n)` at `n = 1`), and confirms that the extra equations matter. It does not move the root equations to arbitrary boundary states, does not exclude later two-exit interiors, repeated bounded layers or any larger linear coefficient, and gives no asymptotic gain. The `d = 5` and `d = 61` periodic controls fail the named `d = 1` root relations.
- **Review status.** Both reviews on record are main-lane agents. The Lean lane re-derived the setup, the universal relations and row 3.1 only (iteration 9), and the side lane read the theorem without replaying it (feed 23:01), so the node stays `written`. The Lean lane queued it as unit V008-a (finite case table, no Cobham), not done.

## History

- New node by the B16 migration (Claude, Opus 5.5) from `experiments/viewpoints/V008/ROOT_REVIEW.md` and the V008 report §2 (legacy ID V008) at commit `be73a66`; the notes stay in [`two-exit-interior-counterexample`](../two-exit-interior-counterexample/README.md)'s folder.
- Main lane (ChatGPT/Codex), 2026-10-18, main commit `9d66b69`.
- 2026-10-31: reviewed by the Claude review lane (Fable 5.1; directed by Santiago Armstrong); status raised to reviewed. The node was moved from `first-shell-three-state-rigidity.md` to this folder (`README.md`); each relative link and the two `evidence` paths gained one `../`; no text changed. Finding in [`REVIEW-2026-10-31-claude-review-lane.md`](REVIEW-2026-10-31-claude-review-lane.md): four of the seven rows of the table in `ROOT_REVIEW.md` are themselves inconsistent with `b, u, v` distinct (vacuous cases; the theorem is unaffected).
