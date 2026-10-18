# What the paired relation covers, and what remains

2026-10-17. **Written exact identities and operation-set classification;
bounded executable checks.** Universal pair existence remains open. The
classification below grants a hypothetical pair relation solely to measure
the reach of that named identity catalogue. It does not claim that the pair
hypothesis is logically insufficient for Collatz when other arguments are
allowed. No novelty, human review, or formal verification is claimed.

Use the odd-only Syracuse map S, with S(1)=1 for path algebra and the state1
killed in measures and currents. All pair coefficients below are signed
integer coefficients. Write `[u]` for the killed point mass at u and
`div=I-P`. References are the [elementary normal form](../bridge_normal_form/BRIDGE_NORMAL_FORM.md),
the [complete complementary run](../complementary_bridge/RUN_BLOCK_BRIDGES.md),
and the [partial shrinking pair construction](../second_return/SHRINKING_PAIRS.md).

## 1. The exact smaller-half comparison for every complementary root

Let

```
x=2^a t-1,  a>=2,  t>0 odd,  t=-3^a modulo4,
q=(x-1)/2=2^(a-1)t-1,
3^(a-1)t-1=2^d w,  d>=2,  w>0 odd.
```

The smaller path has the complete prescribed prefix

```
S^(a-1)(q)=w.                                           (1)
```

Its first a-2 valuations are1; its closing valuation is exactly d+1.
Indeed the last numerator is `2(3^(a-1)t-1)=2^(d+1)w`.
The statement includes a=2, when the initial run is empty.

The larger path has a-1 valuations1 followed by valuation2, giving

```
S^a(x)=3*2^(d-1)w+1.                                   (2)
```

Apply the exact valuation2 identity
`S(1+2^e c)=1+3*2^(e-2)c` for odd c and e>=3.
Writing k=floor(d/2), the complete return comparison is

```
d=2k+1: S^(a+k-1)(x)=4(3^k w)+1,   f=3^k w;
d=2k:   S^(a+k-1)(x)=2*3^k w+1,     f=2*3^k w+1.        (3)
```

In the odd case the sibling identity `S(4f+1)=S(f)` supplies a finite
signed current from x to f; in the even case the displayed path does so.
Call this explicit current D_x, with `div D_x=[x]-[f]`, and let H_q be the
path current in (1). The exact local comparison current is

```
C_x=D_x-H_q,
div C_x=[x]-[q]-[f]+[w].                               (4)
```

Thus the remaining comparison is precisely `[f]-[w]`. Adding any finite
current for it to (4) gives a bridge from x to its smaller half q. If q is
already absorbed by a supplied current, this certifies x. Every coefficient
may be multiplied by the actual source weight; no weight2 source is lost.
Independent root certificates can reuse a known lower-seed proof. This is
not a simultaneous source-capacity assertion for an annular submeasure.

The parameters are constrained: `2^d w+1` is divisible by `3^(a-1)`.
In particular w is1 modulo3 for odd d and2 modulo3 for even d. The checker
retains that integrality condition rather than sampling arbitrary triples.

## 2. Two formal pair types, without a universal construction

Define the two signed source types

```
T(u)=[3u]-[u],      D(u)=[2u+1]-[u],      u>0 odd.
```

Telescoping (3) gives the exact finite decomposition

```
d=2k+1: [f]-[w] = sum_(j=0)^(k-1) T(3^j w);
d=2k:   [f]-[w] = D(3^k w)+sum_(j=0)^(k-1) T(3^j w).   (5)
```

This is a reduction to two *formal types*, with unbounded parameters and
unbounded k. It is not a finite collection of already proved currents.
The R30 proposed universal relation covers only T(u) with u=3 modulo8.
Multiplication by3 cycles the base residues `(1,3)` and `(5,7)` modulo8;
successive summands in (5) therefore cannot all be assigned that relation
when k>=2. Known elementary doubling bridges cover D(u) when u is
canonical, but cannot simply be assumed on every remaining u.

**Equivalence warning.** Finite-current existence for D(u) for every
positive odd u is equivalent to Collatz absorption for every positive odd
integer. It remains equivalent if requested only at the noncanonical u,
because the canonical cases are already proved elementary identities.

Proof: assuming the D currents, use strong induction on odd x. If x=1 the
claim is settled. For x=1 modulo4 and x>1, `S(x)<x`, so one arrow and the
smaller input suffice. For x=3 modulo4, q=(x-1)/2 is positive odd and
smaller, and the D(q) current plus its already proved input suffices.
A finite exact signed current for the nonnegative source `[x]` forces its
finite functional-graph component to meet the absorber: otherwise summing
divergence on that component gives the contradiction1=0. Its existing
arrows consequently contain an actual path to1. Conversely, if all seeds
absorb, subtract the two finite path currents to obtain every D current.

Nor are the helper parameters automatically smaller than x. For
`a=5 modulo8`, a>=13, take x=2^a-1. Then d=4 and
`U=3^2 w=9(3^(a-1)-1)/16` in the D summand of (5). Here U/x tends to
infinity. Inducting on the original source height cannot assume this D(U)
merely because only two pair types occur.

## 3. Complete scope of adjoining every restricted tripling relation

Let B and nu be R25's canonical set and elementary normal form. Consider
the undirected graph generated by exactly:

- all elementary sibling and selected-halving identities, in both directions;
- the formal additional edge `3w -- w` for every positive w=3 modulo8.

No arbitrary forward S edge or inverse-S operation is included in this
identity graph. If the additional relations are later proved, its paths
become valid composed bridges, but they do not exhaust every possible bridge.

Quotient first by the complete elementary components. For w=3 modulo8,
the upper endpoint `3w` is1 modulo8 and hence canonical. The other endpoint
has exactly these two cases:

| w | q=3w | nu(w) | new quotient edge |
|---|---|---|---|
|3 modulo16|9 modulo48|(w-1)/2|q -- (q-3)/6|
|11 modulo16|33 modulo48|w|q -- q/3|

The first w is selected with a=2; the second is complementary with a=2.
Both lower endpoints are canonical. These are *all* added quotient edges,
not just selected examples.

Define the augmented label chi(x) by first taking nu(x), then repeatedly
applying

```
q -> (q-3)/6,  q=9 modulo48;
q -> q/3,      q=33 modulo48;                           (6)
```

until q is not9 modulo24. Every step strictly decreases a positive integer.
The label chi classifies the complete enlarged identity components.

To prove completeness, every possible added edge is in the table and joins
a canonical vertex to its unique smaller parent. Every elementary edge
has already been collapsed by nu. Following parents terminates; the two
ends of each edge have the same terminal label. Conversely every vertex
has its finite parent path to that label. Thus equality of labels is both
necessary and sufficient for connection, including paths through arbitrarily
large intermediate states.

In particular every complementary canonical vertex with a>=3 is7 modulo8
and is incident to **no** new quotient edge: upper endpoints are1 modulo8,
and lower endpoints are1 modulo8 or11 modulo16. Such a vertex is an isolated
quotient vertex in this enlarged graph. This statement concerns the named
static identity catalogue only. Advancing an actual Syracuse path may
reach another component and is a separate operation.

## 4. Infinite actual roots remain unresolved after the full first run

The preceding limitation persists after the R26 first run on an explicit
family. For every

```
a=3 modulo16, a>=19,
x=2^a-1, q=2^(a-1)-1, N=12*2^(a-4),
w=(3^(a-1)-1)/8, f=3w,                               (7)
```

x is an actual coefficient1 complementary R'_N root: N is a required
ray cutoff, q<N<x, `9N/8<x<3N/2`, x=7 modulo12, and a is odd.
Since `a-1=2 modulo16`, `3^(a-1)=9 modulo64`, so d=3 and w=1 modulo8.
Also w=1 modulo3; hence w=1 modulo24, already a terminal label for (6).

If w=1 modulo16, 3w is selected with a=2 and

```
nu(3w)=(3w-1)/2=1 modulo8 and1 modulo3.
```

This is another terminal label1 modulo24, strictly larger than w since
w>1. If w=9 modulo16, 3w=11 modulo16 is complementary canonical and is
again terminal for (6), distinct from w. Therefore in all cases

```
chi(f) != chi(w).                                    (8)
```

Granting *every* restricted relation T(v), v=3 modulo8, thus does not
complete the exact residual comparison (4) for this infinite family using
only the enlarged identity graph. This is an exact operation-set
counterfamily, not a failed capped merger search. Neither (8) nor the
checker asserts nonconvergence. Further forward/inverse arguments or
new pair relations remain available. No logical impossibility statement
about proving Collatz from an augmented theory follows from (8).

The new [missing-domain pair construction](../pair_one/MISSING_PAIR_DOMAIN.md)
illustrates this boundary concretely. It uses additional ordinary forward
arrows and reduces some w=1 modulo8 pairs to smaller parameters in the
3-modulo8 domain. In particular the exponent classes a=659 and1699
modulo4096 lie inside (7) and now have explicit smaller-seed mergers.
Their success is consistent with (8): the construction goes beyond the
static identity graph classified in Section3.

## 5. Executable evidence and remaining obligation

```
python3 experiments/residual_progress/pair_scope/check_pair_scope.py
```

The default checker is read-only and compares against
[pair_scope_audit.json](pair_scope_audit.json). `--write-receipt` regenerates
that receipt. It checks the exact current boundary (4) and decomposition
(5) on every complementary root through32767;741 integrality-preserving
parameter cases a2..20,d2..40;4096 hypothetical edges; the complete bounded
quotient graph through32767; eight members of (7); and seven growing
even-return helper cases. All loops have fixed bounds or a proved decreasing
integer. No orbit absorption or unknown merger is searched.

[pair_scope.py](pair_scope.py) exposes the local current with its unresolved
pair boundary. Its augmented normal form returns a *formal graph label*,
never a certificate asserting the hypothetical tripling relations.
The isolated graph and pair-type equivalence proofs do not rely on scans.

The constructive obligation is to prove valid currents for the unresolved
pair sources with a well-founded recursion that covers every branch.
R30 supplies such a recursion on selected branches. Formula (5) preserves
the exact remaining targets but supplies neither universal termination nor
a smaller parameter for every rewrite.
