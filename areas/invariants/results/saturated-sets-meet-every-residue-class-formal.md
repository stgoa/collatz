---
id: saturated-sets-meet-every-residue-class-formal
kind: result
title: "Every union of 3x+1 components meets every residue class: a counting-free proof, machine-checked"
status: formal
claim: >
  Ordinary Collatz map T on the positive integers (T(n) = n/2 for even n, 3n+1 for odd n). Let B be a nonempty set
  of positive integers with x in B if and only if T(x) in B, for every positive x; that is, a nonempty union of
  components of the 3x+1 graph. Then for every M >= 1 and every r there is x in B with x = r (mod M). This is
  machine-checked in Lean with the standard axioms only (LeanLane.SaturatedConnectivity.saturated_dense_all).
  The new step is a proof, without counting, that for every M' coprime to 6 and every v the residue automaton of
  saturated-sets-residue-classes-finite-automaton is strongly connected, already through its scaling arrows with
  s = 1 and its inverse arrows with j = 2 (LeanLane.SaturatedConnectivity.step_connected). The statement is a
  consequence of Monks's theorem that every arithmetic progression is sufficient; nothing about convergence or
  about orbit lengths is asserted. For 3x+d with d > 1 the statement is false (the multiples of d).
authors:
  - Claude cycles lane (Fable 5.2; directed by Santiago Armstrong)
created: 2026-11-23
depends_on: [saturated-sets-residue-classes-finite-automaton]
lean:
  - LeanLane.SaturatedConnectivity.mem_of_map_mem
  - LeanLane.SaturatedConnectivity.closed_eq_univ
  - LeanLane.SaturatedConnectivity.step_connected
  - LeanLane.SaturatedConnectivity.saturated_dense_all
tags: [invariants, residues, saturated-sets, finite-automaton, connectivity, lean, monks]
---

# Every union of 3x+1 components meets every residue class: a counting-free proof, machine-checked

## Statement

Let `T(n) = n/2` for even `n` and `T(n) = 3n+1` for odd `n`, on the positive integers. A set `B` of positive
integers is **saturated** if `x in B` is equivalent to `T(x) in B` for every positive `x`. Saturated sets are the
unions of connected components of the `3x+1` graph.

**Theorem.** A nonempty saturated set meets every residue class modulo every positive integer.

**Connectivity.** For `M'` coprime to 6 and any `v`, consider the states `(x, eta)` in `Z/M' x Z/3^v` with the
two families of arrows

```
(x, eta) -> (4x + 1, 4 eta + 1),
(x, eta) -> (x', eta')     whenever 4x = 3x' + 1 and 4 eta = 3 eta' + 1.
```

Every set of states that is nonempty and closed under both families is the whole state space. Both families are
arrows of the automaton of
[`saturated-sets-residue-classes-finite-automaton`](saturated-sets-residue-classes-finite-automaton/README.md)
(scaling with `s = 1`, inverse with `j = 2`), so that automaton is strongly connected. Its Theorem 1 then gives
the theorem above.

**What is and is not new.** The theorem is known: it follows from Monks's sufficiency of arithmetic
progressions ([`monks-2006-sufficiency`](../../../sources/monks-2006-sufficiency.md)), and
[`saturated-residue-automata-uniform-connectivity`](saturated-residue-automata-uniform-connectivity/README.md)
proves the connectivity of the same sparse graph by a counting argument, for every addend `d` coprime to `6M`.
This node adds a second proof of the case `d = 1`, which avoids counting, and its formalisation. With it the
whole chain from the definition of the map to the theorem is machine-checked.

## Proof

Write `S = Z/M' x Z/3^v`, and let `C` be a nonempty subset of `S` closed under the two families. The numbers 4
and 3 are invertible modulo `M'`, and 4 is invertible modulo `3^v`.

### 1. Each inverse arrow frees one 3-adic digit

For `k >= 0` say that `P_k` holds at `p = (x, eta)` if `(x, eta + kappa)` is in `C` for every `kappa` with
`3^k kappa = 0`. So `P_0(p)` says `p in C`, and `P_v(p)` says that the whole fibre over `x` lies in `C`.

- **Scaling preserves `P_k`.** If `P_k(x, eta)` then `P_k(4x + 1, 4 eta + 1)`: for `3^k kappa = 0` the state
  `(x, eta + kappa/4)` is in `C`, and its image is `(4x + 1, 4 eta + 1 + kappa)`.
- **An inverse arrow turns `P_k` into `P_(k+1)`.** Let `P_k(x, eta)`, `4x = 3x' + 1` and `4 eta = 3 eta' + 1`.
  For `3^(k+1) kappa = 0` put `kappa_0 = 3 kappa/4`. Then `3^k kappa_0 = 0`, so `(x, eta + kappa_0)` is in `C`,
  and `4(eta + kappa_0) = 3(eta' + kappa) + 1`. The inverse arrow from `(x, eta + kappa_0)` ends at
  `(x', eta' + kappa)`.
- **An inverse arrow is always available after at most two scalings.** A state is the source of an inverse arrow
  exactly when `eta = 1 (mod 3)`, and scaling adds 1 to `eta` modulo 3. So one of `eta`, `4 eta + 1`,
  `4(4 eta + 1) + 1` qualifies.

By induction on `k` there is a state with `P_k`, for every `k`. At `k = v` this is a full fibre.

### 2. From one full fibre to all

Let `X` be the set of `x` in `Z/M'` whose whole fibre lies in `C`. It is nonempty by section 1.

- `X` is closed under `x -> 4x + 1`: the scaling arrow maps the fibre over `x` onto the fibre over `4x + 1`.
- `X` is closed under `x -> x'` with `4x = 3x' + 1`: every `(x', eta')` is the end of an inverse arrow from
  `(x, (3 eta' + 1)/4)`.

Both maps are injective on the finite set `Z/M'`. A subset of a finite set that an injective map sends into
itself contains every preimage of its elements. So `X` is closed under `y -> (3y + 1)/4` as well. Composing,
`X` is closed under `x -> 3x + 1` and under `x -> 3x + 2`, hence under the inverse of the first followed by the
second, which is `t -> t + 1`. Therefore `X = Z/M'` and `C = S`.

### 3. Conclusion

The set of states reachable from a given state is nonempty and closed, so it is everything: the sparse graph is
strongly connected. For a positive `M` write `M = 2^k 3^b M'` with `M'` coprime to 6, and `phi(M') = 3^e u` with
`3` not dividing `u`. Then `4^(3^(e+1) u) = 1 (mod M')`, and Theorem 1 of the automaton node applies with
`v = e + 1`.

## Lean

[`LeanLane/SaturatedConnectivity.lean`](../../../lean/LeanLane/SaturatedConnectivity.lean), built by
`lake build LeanLane` from `lean/`; receipts `lean/receipts/SaturatedConnectivity.*`.

| Lean declaration | Statement |
|---|---|
| `mem_of_map_mem` | a subset of a finite type mapped into itself by an injective map contains every preimage of its elements |
| `closed_eq_univ` | sections 1 and 2: a nonempty closed set of states is everything |
| `step_connected` | for `M'` coprime to 6 and every `v`, `Relation.ReflTransGen (Step M' v) a b` for all states `a, b` |
| `saturated_dense_all` | `Saturated B -> B.Nonempty -> 0 < M -> exists x in B, x = r [MOD M]` |

`Saturated`, `T` and `Step` are the definitions of `LeanLane.SaturatedDensity` and `LeanLane.SaturatedAutomaton`.
`saturated_dense_all` is the theorem of this node word for word: `Saturated B` requires every element of `B` to
be positive and `x in B <-> T x in B` for positive `x`. `step_connected` discharges the hypothesis `hconn` of
`LeanLane.SaturatedAutomaton.saturated_dense_of_automaton`. The Lean proof follows sections 1 to 3. The
equivalence for a general addend `d` of
[`saturated-residue-automata-uniform-connectivity`](saturated-residue-automata-uniform-connectivity/README.md)
is not formalised.

## Remarks

- **Relation to the counting proof.** The counting proof shows that the indicator of a closed set is invariant
  under the non-invertible map `z -> (3z + 1)/4` by comparing cardinalities. Here the same invariance is
  obtained digit by digit, which needs no cardinalities and is shorter to formalise.
- **Controls.** For `3x+d` with `d > 1` the multiples of `d` form a saturated set that misses residue classes.
  The proof uses the addend 1 in both families of arrows, and in section 2 it ends with the translation by 1.
  With an addend `d` it would end with the translation by `d`, which generates `Z/M'` only when `gcd(d, M') = 1`.
- **Chain strength.** The Lean proof is complete: it uses no unformalised statement. The only node it depends
  on is the automaton node, through its Theorem 1, which is machine-checked. That node as a whole is `written`,
  because its claim also contains a finite computation for `M' <= 1000` and a `3x+5` control that are not
  formalised and are not used here. This is why MAP.md shows a weaker chain strength for this node.
- **Novelty.** None is claimed for the theorem (Monks 2006). Whether a formal proof existed before is not known
  to us.

## History

- 2026-11-23: proved and formalised by the Claude cycles lane (Fable 5.2; directed by Santiago Armstrong).
