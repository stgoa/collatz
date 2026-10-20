---
id: orbit-component-current-criterion
kind: result
title: A finite current exists exactly when every nonabsorbing orbit component has the right total mass
status: written
claim: >
  Any set X with a deterministic map S and an absorbing state o; finite measures on X \ {o}, P pushes along S
  and discards mass at o; two states are in the same orbit component if S^a(x) = S^b(y) for some a, b ≥ 0.
  For a finite measure μ with component masses m_C: (1) a finite exact current μ = (I − P)J exists iff m_C = 0
  for every nonabsorbing component C; (2) finite J and ζ ≤ 0 with μ = (I − P)J + ζ exist iff m_C ≤ 0 for every
  nonabsorbing C; (3) sup_L H_L(μ) < ∞ iff the sum of the nonabsorbing masses is ≤ 0, which is weaker. Exposing
  d forward arrows from every source while retaining historical intersections, for d = 0, 1, 2, …, is a
  semidecision procedure complete for current existence: it succeeds at some finite depth iff a certificate of
  the required type exists; a depth cap returns "unresolved", never nonexistence. Applied to the odd-only 3x+1
  map absorbing at 1, it characterises what the packet certificates detect; it proves no termination.
authors:
  - ChatGPT main lane (Codex)
created: 2026-10-17
depends_on: []
certificates: [verify_obstructions.py]
evidence:
  - "audit.json: the legacy receipt of verify_obstructions.py (the script prints its report and writes no file; scripts/verify_all.py compared the two at be73a66)"
aliases: [R7]
tags: [convergence, packet-currents, currents, orbit-components, duality, semidecision]
---

# A finite current exists exactly when every nonabsorbing orbit component has the right total mass

## Statement

Let `X` be a set with a deterministic map `S` and an absorbing state `o`. Measures have finite support in `X \ {o}`, and `P` pushes along `S` while discarding mass at `o`. Currents are finite signed measures `J` with divergence `(I − P)J`. Coefficients may be real; integer source coefficients admit integer constructions below.

Two states belong to the same **orbit component** if `S^a(x) = S^b(y)` for some nonnegative integers `a, b`. This is an equivalence relation: transitivity follows by advancing both identified orbit segments until their shared middle orbit has reached both meeting times. Equivalently, these are the connected components after ignoring arrow directions. There is one absorbing component, the states that reach `o`; the others are nonabsorbing. Every finite subset of one component has a common forward descendant, with possibly different arrival times. For a finite measure `μ` write `m_C = Σ_(x ∈ C) μ(x)`.

**Theorem 1.**

1. A finite exact current `μ = (I − P)J` exists if and only if `m_C = 0` for every nonabsorbing orbit component `C`.
2. A finite signed current and nonpositive finite residual, `μ = (I − P)J + ζ` with `ζ ≤ 0`, exist if and only if `m_C ≤ 0` for every nonabsorbing orbit component `C`.

**Work.** Let `τ` be the hitting time of `o`, `h_L = min(L, τ)` and `H_L(μ) = Σ_x μ(x)·h_L(x)`. For all `L` beyond the largest finite hitting time among the finitely many sources,

```
H_L(μ) = L·Σ_(C nonabsorbing) m_C + Σ_(τ(x) < ∞) μ(x)·τ(x).
```

So `sup_L H_L(μ) < ∞` holds if and only if the **sum** of nonabsorbing component masses is nonpositive, which is weaker than each individual mass being nonpositive.

**Theorem (complete semidecision search).** For `d = 0, 1, 2, …`, expose the first `d` forward arrows from every source, retaining previously visited states, and compute the connected components of this finite graph with arrow directions ignored. If every component not containing `o` has source mass zero, an exact certificate can be formed; if all those masses are nonpositive, a one-sided certificate can be formed. If a certificate of either type exists, the search of that type succeeds at some finite depth. A depth cap returns unresolved, never nonexistence.

## Proof

From §§1–2 of the legacy note `functional_graph_currents.md`, kept as written.

**Theorem 1.** The component indicator `1_C` is invariant under `S` for every nonabsorbing component. Pairing a finite divergence with this indicator gives zero; pairing the residual gives a nonpositive number. These are the necessary conditions.

For sufficiency, only finitely many components meet the support of `μ`. In an absorbing component, follow each source to `o`. In each other component, choose a common descendant `z_C` and finite paths from every source to it. A source of weight `c` contributes current `c` along its path, whose divergence is `c·(δ_x − δ_(z_C))`. Summing gives

```
μ = (I − P)J + Σ_C m_C·δ_(z_C),
```

the sum over the finitely many nonabsorbing source components. It vanishes under condition 1 and is nonpositive under condition 2. All paths are finite, so the current is finite. The argument is an existence proof; it does not provide a decidable component-membership oracle. ∎

The work formula follows by splitting the sources into those with finite and infinite hitting time.

**Search.** To construct the certificate at a successful depth, choose one anchor per finite component (`o` when available), choose an undirected spanning tree, and route each source's coefficient to that anchor. Traversing an original arrow backwards gives a negative current on that arrow. The divergence of a routed source is exactly its source mass minus its anchor mass; the residual is the component mass at its anchor. Every reported success is a finite, checkable certificate. If a certificate of either type exists, Theorem 1 supplies finitely many paths that connect each required source component, or connect it to `o`. At a sufficiently large finite depth those paths have been exposed, so the corresponding search succeeds. ∎

## Certificates

[`verify_obstructions.py`](verify_obstructions.py) (main lane, under 1 s, standard library; checks by `assert`, so run it without `-O`; prints its report). For this node it checks the finite-graph constructor on every deterministic map on three nonabsorbing vertices and every source measure with coefficients in `{−1, 0, 1}` (1,728 cases, both certificate modes), and the negative-cycle and unequal-time examples below. The same run checks the delayed-separation formulas and the local coalescence identity of [`bounded-packet-certificate-obstruction`](../bounded-packet-certificate-obstruction.md). Its output matches the legacy receipt [`audit.json`](audit.json).

## Remarks

- **A separation example outside the positive integers.** Extend the odd Syracuse formula to negative odd integers, retaining absorption only at positive 1. The cycles are `−1 → −1` and `−5 → −7 → −5`. For `μ = δ_(−1) − δ_(−5)`, `H_L(μ) = 0` at every horizon, but the `{−1}` component has mass `+1`; hence neither type of current exists. This is a negative-integer example, not a claimed counterexample on positive Collatz states. A fully certified annular version is [`reflected-negative-annulus-control`](../reflected-negative-annulus-control.md).
- **Bounded work for one measure versus the equivalence.** The fixed-measure implications must not be confused with [`qualitative-current-criterion`](../qualitative-current-criterion.md), which quantifies over **every** packet cutoff.
- **Synchronous transport is incomplete.** On the nonabsorbing ray `S(n) = n + 1`, `δ_2 − δ_3 = (I − P)δ_2`, but `P^d(δ_2 − δ_3)` is nonzero at every depth. Recording historical intersections finds the unequal-time cancellation.
- **What completeness does not give.** For the entire right-aligned family, proving that this search always terminates remains equivalent to the universal current criterion ([`packet-current-supply`](../../questions/packet-current-supply.md)). Completeness removes an algorithmic deficiency; it does not prove the missing universal existence hypothesis. Finite runs on whole packets are [`whole-packet-historical-certificates`](../whole-packet-historical-certificates/README.md); the restricted, exposed-graph form of Theorem 1 and its potential `Φ` are in [`exposure-potential-boundary-flux`](../exposure-potential-boundary-flux/README.md).
- **Controls.** The PR1 lane's `d = −1` control overlaps the negative-integer example; its locally Collatz-like controls `d = 13, 61`, the induction barrier and the minimality lemma are not in this note ([`locally-collatz-like-control-barrier`](../locally-collatz-like-control-barrier/README.md), [`exact-current-minimality`](../exact-current-minimality.md)).
- The theorem is elementary graph duality. Novelty undetermined.

## History

- Migrated from `experiments/current_construction/obstructions/functional_graph_currents.md` §§1–2 (legacy ID R7) at commit `be73a66`, by the B08 migration (Claude, Opus 5.5); its §§3–4 became [`bounded-packet-certificate-obstruction`](../bounded-packet-certificate-obstruction.md). The checker and receipt moved byte-identical. Legacy status: "written graph theorem, complete semidecision algorithm, and finite checks"; the note says "These elementary arguments have not been human-reviewed or formally verified".
- Main lane (ChatGPT, Codex), 2026-10-17. The round report records "independent model reviews" of the component criterion by the main lane's own agents; no review from another lane is on record.
