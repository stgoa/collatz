---
id: saturated-residue-automata-uniform-connectivity
kind: result
title: "Two families of arrows make every saturated residue automaton strongly connected"
status: written
claim: >
  Let M >= 1 be coprime to 6, v >= 1, d >= 1 be coprime to 6, and Q = M*3^v.
  On Z/QZ put sigma(z) = 4z+d and F(z) = (3z+d)/4, with division by 4 taken modulo Q.
  The directed graph with arrows z -> sigma(z) and F(z) -> z for every z is strongly connected
  if and only if gcd(d,M) = 1. At d = 1 this graph, in the coordinates W = 3z+1,
  is the subgraph consisting of s = 1 scaling arrows and j = 2 inverse arrows of the
  saturated residue automaton A(M) at v = max(1,v_3(ord_M(4))). Consequently A(M) is
  strongly connected for every M coprime to 6. By the existing automaton realisation and
  lifting theorem, every nonempty union of positive 3x+1 orbit components meets every
  residue class modulo every positive integer. The corollary concerns the ordinary map
  (equivalently its shortcut map or the odd-only map extended by doubling); no orbit-length
  or convergence conclusion is asserted.
authors:
  - Codex research lane (GPT-6 Astra; directed by Santiago Armstrong)
created: 2026-11-08
depends_on: [saturated-sets-residue-classes-finite-automaton]
certificates: [check_connectivity.py]
evidence:
  - "check_connectivity.json: generated receipt for the sparse graphs, coordinate embeddings, and 3x+d controls"
tags: [invariants, residues, saturated-sets, finite-automaton, connectivity, controls]
---

# Two families of arrows make every saturated residue automaton strongly connected

## Statement

Fix positive integers `M, v, d` with `gcd(M,6) = gcd(d,6) = 1` and `v >= 1`.
Write `Q = M*3^v` and `R = Z/QZ`. Division by 4 below means multiplication
by its inverse in `R`. Define

```
sigma(z) = 4z+d,             F(z) = (3z+d)/4.
```

Let `G(M,v,d)` be the finite directed graph on `R` whose arrows are

```
z -> sigma(z),               F(z) -> z                    for every z in R.
```

Equivalently, the second family consists of all `x -> z` such that
`3z = 4x-d` in `R`. Such an arrow exists exactly when `x = d (mod 3)`;
then it has three possible targets. A path length in this graph counts
composite residue moves, not ordinary, shortcut, or odd-only Collatz steps.

**Theorem.** `G(M,v,d)` is strongly connected if and only if `gcd(d,M) = 1`.

**Corollary for `3x+1`.** Every automaton `A(M)` of
[`saturated-sets-residue-classes-finite-automaton`](../saturated-sets-residue-classes-finite-automaton/README.md)
is strongly connected, for every positive `M` coprime to 6. Therefore every
nonempty saturated subset of the positive integers meets every residue class
modulo every positive integer. Here saturated means a union of components
of the ordinary `3x+1` graph, including all forward and inverse arrows;
the equivalent odd-only description extends membership to even integers by
doubling. The convention that 1 is absorbing does not change these components.

The graph theorem is proved below without any literature input. The corollary
uses the existing automaton realisation and lifting theorem. The underlying
all-modulus density statement is already a consequence of Monks's progression
sufficiency theorem; the contribution here is a uniform proof for this
particular finite automaton and its sparse subgraph.

## Proof

### 1. Forward-closed sets are balanced modulo 3

Let `C` be a nonempty set of vertices closed under the arrows of `G(M,v,d)`.
Since `sigma` is a permutation of the finite set `R`, the inclusion
`sigma(C) subset C` implies `sigma(C) = C`.

Modulo 3, `sigma(z) = z+d`. As `3` does not divide `d`, this permutes the
three residue classes cyclically. Its restriction gives bijections between
the three parts of `C`, so

```
|C intersect {z = 0 mod 3}| = |C intersect {z = 1 mod 3}|
                          = |C intersect {z = 2 mod 3}| = |C|/3.       (1)
```

### 2. Counting supplies the reverse membership implication

The image of `F` is exactly the class `d (mod 3)`: the equation `F(z)=x`
is `3z=4x-d` modulo `Q`, which has three solutions when `x=d (mod 3)`
and none otherwise. Thus (1) gives

```
|F^(-1)(C)| = 3*|C intersect {x = d mod 3}| = |C|.                    (2)
```

Every `z` with `F(z) in C` also lies in `C`, by the arrow `F(z) -> z`.
Hence `F^(-1)(C) subset C`; (2) upgrades this inclusion to equality.
If `h` is the indicator of `C`, then for every `z in R`

```
h(sigma(z)) = h(z),                 h(F(z)) = h(z).                  (3)
```

This is the essential counting step: forward closure alone has become
membership invariance under the noninvertible map `F`.

### 3. Iterating F removes the power of 3

For `z,z' in R`, the affine formula gives

```
F^v(z) - F^v(z') = 3^v*4^(-v)*(z-z') in R.
```

If `z = z' (mod M)`, the right-hand side is zero modulo `Q=M*3^v`.
By (3),

```
h(z) = h(F^v(z)) = h(F^v(z')) = h(z').
```

Therefore `h` factors through `Z/MZ`; write the induced function as
`hbar`. It inherits both identities in (3), with `sigma` and `F` now
interpreted modulo `M`.

### 4. The two affine compositions force translation by d

Modulo `M` one has the exact identities

```
F(sigma(z)) = 3z+d,                 sigma(F(z)) = 3z+2d.
```

Equation (3) therefore implies

```
hbar(3z+d) = hbar(z) = hbar(3z+2d).
```

Since 3 is invertible modulo `M`, `3z+d` runs through every residue.
Consequently `hbar(t) = hbar(t+d)` for every `t`. If `gcd(d,M)=1`,
repeated addition of `d` reaches every residue modulo `M`, so `hbar`
is constant. Nonemptiness of `C` makes that constant 1, whence `C=R`.

For any vertex `a`, the set of vertices reachable from `a` is a nonempty
forward-closed set. We have proved that this set is `R`; because `a`
was arbitrary, the graph is strongly connected.

### 5. A shared prime factor gives the precise obstruction

If `gcd(d,M)>1`, choose a prime `p` dividing both `d` and `M`. Then
`p>=5`. The set

```
C_p = {z in R : z = 0 mod p}
```

is nonempty, proper, and forward closed. Indeed `sigma(z)=4z+d` is
zero modulo `p` when `z` is. For an arrow `F(z) -> z`, if the source
is zero modulo `p`, then `3z+d=0 (mod p)`, so the target `z` is zero
modulo `p` as well. This proper closed set prevents strong connectivity.
Together with Step 4, this proves the theorem.

### 6. Embedding the sparse graph in the existing automaton

Now set `d=1`, fix `M` coprime to 6, and take

```
v = max(1,v_3(ord_M(4))).
```

For `M=1` take `ord_1(4)=1`. A class `z modulo M*3^v` corresponds
bijectively to the existing automaton state

```
(x,y) = (3z+1 modulo M, 3z+1 modulo 3^(v+1)).
```

The first coordinate determines `z modulo M` because 3 is invertible
there; the second determines `z modulo 3^v` because `y=1 (mod 3)`.
The Chinese remainder theorem proves bijectivity.

The edge `z -> 4z+1` becomes `(x,y) -> (4x,4y)`, precisely a scaling
arrow with `s=1`.

For the second family, suppose `3t=4z-1 (mod M*3^v)`. Reducing modulo
3 gives `z=1 (mod 3)`, the legality condition for the `j=2` inverse
arrow. Modulo `M`,

```
3t+1 = 4z = 4*(x-1)/3.
```

Choose a lift `z_tilde` of `z modulo 3^v` to a residue modulo
`3^(v+1)` such that

```
4*z_tilde = 3t+1 (mod 3^(v+1)).
```

Such a lift exists: the desired congruence already holds modulo `3^v`,
and among the three lifts of `z`, multiplication by the unit 4 gives
all three lifts of `4z`. The `j=2` arrow with this lift has target
`(3t+1 modulo M, 3t+1 modulo 3^(v+1))`, as required. Thus every
edge of `G(M,v,1)` is an arrow of `A(M)` under this bijection.

By the theorem the subgraph is already strongly connected; adding the
other automaton arrows preserves this property. Theorem 1 of the
existing automaton node now gives every residue class modulo
`2^k*3^b*M` for every nonempty saturated set and all `k,b>=0`.
Every positive modulus has this factorisation, proving the corollary.

## Certificates

[`check_connectivity.py`](check_connectivity.py), using only the standard
library, constructs and checks 167 sparse graphs, comprising 197,391
vertices and 394,782 arrow instances. It checks connectivity by reachability
from zero in both the graph and its reversal, independently checks the
defining inverse congruence and the coordinate embedding for each arrow,
and checks closed divisible classes in the disconnected controls.

The tested parameters are every `M<=101` coprime to 6 with `v in {1,2,3}`
at `d=1`, plus `(M,v,d)=(487,5,1)`; and each
`d in {5,7,13,61}`, `M in {1,5,7,13,25,35,61,91}`, `v in {1,2}`.
The generated receipt [`check_connectivity.json`](check_connectivity.json)
records each instance. By default the script compares the computation
with that receipt; `--write-receipt` regenerates it. A failed check raises
an exception, including under `python3 -O`.

The uniform theorem is the written proof above; it does not follow from
the finite census. No computation of a positive orbit is used to infer
convergence.

## Remarks

**Relation to the frontier.** The preceding automaton node established
strong connectivity computationally for every `M<=1000` coprime to 6.
This proof removes that bound and the need to enumerate all powers in
the arrow definitions. It resolves the remaining automaton condition
in [`invariant-sets-meet-every-residue-class`](../../questions/invariant-sets-meet-every-residue-class.md).

**Prior work and novelty.** The density consequence is known: Theorem 1.1
of [`monks-2006-sufficiency`](../../../../sources/monks-2006-sufficiency.md)
says that every positive orbit merges with an orbit starting in any
prescribed infinite arithmetic progression. For a saturated set, such
a merger puts that progression's witness in the same set. Monks's
theorem is cited here for attribution; it is not used by the graph
proof or the corollary's dependency chain. Novelty of the sparse
automaton argument is undetermined.

**Controls and scope.** For each `d in {5,7,13,61}`, the choice `M=d`
has the proper closed set of residues divisible by `d`, exactly as
the graph theorem requires. The associated positive multiples of `d`
are saturated for `3x+d`. At moduli coprime to `d`, the theorem allows
full connectivity; that has no implication excluding the actual
cycles of those maps. Likewise, density of every component for
`3x+1` gives neither a unique component nor a bound putting a witness
below a verified convergence threshold.

**Verification status.** The proof is written and accompanied by finite
checks. Same-session agent scrutiny does not constitute an independent
review under the repository rules. No Lean formalisation is claimed.

## History

- 2026-11-08: Written by the Codex research lane (GPT-6 Astra; directed
  by Santiago Armstrong). A balanced-fibre counting argument closes
  the all-modulus connectivity gap left by the existing automaton
  construction. The literature check identified Monks's theorem as
  prior work for the density consequence.
