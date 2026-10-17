# Complete aggregate exposure components and a depth-32 obstruction

Date: 2026-10-17. Status: written algorithm-correctness argument and finite
exact enumeration. No obstruction at every depth, universal construction,
Collatz proof, or novelty claim is supplied.

The measure is the actual six-band annulus `A_N`, for positive `8|N`, with
`Q=9N/4` and support in `Q<x<64Q`. All nonzero source coefficients are
retained. The map is odd-only Syracuse with absorption at 1. In particular,
the earlier obstruction for individual raw packets is not used here.

## 1. The exposure depth of a template is a necessary test

For an integer `D>=1`, define the historical exposure graph `G_D(N)` by
starting at **every nonzero source of A_N** and including its first `D`
arrows, stopping at 1. Thus an arrow `x -> S(x)` is present exactly when
`x!=1` and some annular source reaches `x` in at most `D-1` steps. This
does not bound the length of an undirected component or of a directed
path assembled using histories from different sources.

If a component `C` of this graph does not contain 1, then every current
supported on its exposed arrows satisfies

\[
\sum_{x\in C}(I-P)J(x)=0.
\]

Consequently, if `A_N(C)>0`, there is no finite current supported on the
**whole** graph `G_D(N)` with `A_N=(I-P)J+zeta`, `zeta<=0`.
The indicator of `C` is an exact dual witness. This permits arbitrary
signed current coefficients and cancellations among every annular source.

A finite catalogue of common-tail tree templates has a maximal depth `D`
from a nonzero source to its anchor, after deleting branches with no
source. If copies are packed using actual annular source coefficients,
all their current arrows lie in `G_D(N)`. A positive component therefore
excludes a complete packing of such a catalogue at that cutoff. It also
excludes fractional combinations of these currents.

This implication is deliberately one-way. Recursive rewrites can introduce
new residual sources and reach arrows outside the original `G_D(N)`;
unbounded recursive depth is allowed by the research programme. A finite
obstruction at one `D` does not exclude a larger fixed depth, much less
all finite catalogues.

## 2. Exact inverse enumeration of one complete component

Materializing the whole annulus is unnecessary when a component is small.
The following oracle tests membership in the exposure graph and saturates
one component, including all incoming arrows.

Write `M=144N`. Since every annular source is at most `M-1` and
`S(x)<=(3x+1)/2`, every state reached in at most `r` steps is at most

\[
B_r=\left\lfloor\frac{3^rM}{2^r}\right\rfloor-1.
\]

The bound is valid for all intermediate states, including 1. Its proof is
the identity `T^r(x)+1=(3/2)^r(x+1)` for `T(x)=(3x+1)/2`, together with
monotonicity of `T`. All arithmetic in the implementation is integral.

For positive odd `y`, its nonabsorbing positive odd predecessors at most
`B` are exactly

\[
p=\frac{2^a y-1}{3},\qquad a\ge1,\quad 1<p\le B,
\]

with `a` odd if `y=2 modulo 3`, even if `y=1 modulo 3`, and none if
`3|y`. The parity condition enforces divisibility by 3; the resulting
integer is odd, and `3p+1=2^a y` has exact valuation `a` because `y` is
odd. The predecessor 1 is excluded because its outgoing arrow is killed.

Let `Reach(y,r)` mean that a nonzero annular source reaches `y` in at most
`r` steps. The complete recursion is:

1. If `A_N(y)!=0`, return true.
2. If `r=0` or `y>B_r`, return false.
3. Otherwise return the disjunction of `Reach(p,r-1)` over **all** the
   predecessors above with `p<=B_(r-1)`.

Induction on `r` proves exactness in both directions. The recursion loses
no route: the final predecessor on any qualifying route obeys the height
bound. It invents no route: each predecessor arrow has the exact valuation
and each recursive witness begins at an actual source. Memoization only
avoids repeating these finite decisions.

Starting at a nonzero source `s`, repeatedly add:

- its outgoing arrow if `x!=1` and `Reach(x,D-1)`;
- every incoming arrow `p -> x` with `p<=B_(D-1)` and
  `Reach(p,D-1)`.

When this queue is empty, every incident arrow of every visited vertex in
`G_D(N)` has been considered. The result is exactly the entire component
of `s`. Summing the coefficient table over its vertices therefore includes
**all** annular atoms in that component, including atoms on branches that
were not part of the originally selected chain.

Both vertex and memoized-query caps are explicit. Exceeding either returns
`unresolved_cap`, with no component mass or obstruction assertion. A cap
is never interpreted as failure of current existence. This is a finite
graph oracle, not a universal termination argument for current search.

## 3. A complete depth-32 obstruction on a required ray

Set

\[
N_*=96\cdot2^{24}=1\,610\,612\,736=12\cdot2^{27},\qquad D=32.
\]

The component of `144N_*-1` in the **entire** `G_32(N_*)` has 35 vertices
and 34 arrows. It is precisely the increasing chain

\[
x_j=\frac{3^j\,64N_*}{2^j}-1,\qquad 0\le j\le34,
\]

with arrows `x_j -> x_(j+1)` for `j<34`. All 34 valuations are exactly 1.
Its only annular sources are:

| State | Position | Actual coefficient |
|---:|---|---:|
|103079215103|`64N_*-1 = x_0`|-2|
|154618822655|`96N_*-1 = x_1`|2|
|231928233983|`144N_*-1 = x_2`|2|

The last vertex is `100063090197999413`. The component does not contain
1 and has signed source mass **2**. The oracle completes after 9171
memoized reachability decisions, below the explicit caps of 10000 vertices
and 20000 decisions. The receipt stores every vertex and arrow.

The finite arithmetic certificate therefore rules out a complete
one-sided current supported on the first 32 steps from every actual
source, at this particular required cutoff. It rules out complete packed
catalogues of source-to-anchor depth at most 32. Merely tracing the
displayed increasing chain would not prove this: exclusion of every
additional incoming exposure edge is the essential closure check.

The annulus has `267N_*/8 = 53,754,200,064` nonzero source atoms. The oracle
does not enumerate them all. It uses the exact coefficient function at
every potential inverse source, together with exhaustive bounded inverse
reachability. A current that uses deeper or different edges remains
possible; no assertion about its nonexistence is made.

## 4. Why the naive increasing-chain argument fails in general

For `N=10368`, the component of the top source `1492991` at exposure depth
2 has 34 vertices, 33 arrows, and 27 annular sources. Its positive and
negative masses are respectively **22 and -22**, and it is not linked to
1. Its signed mass is therefore **zero**. The full source list and graph
are stored in the receipt.

At depth 1, the top component has positive mass 6; extending the exposure
to depth 2 brings in enough other annular mass to balance it. For example,
the negative source `174761` has the two-step path

\[
174761\longrightarrow131071\longrightarrow196607.
\]

The intermediate state has annular coefficient zero. The positive source
`196607` then connects by another two-step history to `442367`, and the
source chain continues through `663551`, `995327`, and `1492991`.
Other incoming branches account for the rest of the exact balance. Each
arrow is in depth-2 exposure, even though the assembled chain from
`174761` to the top source is longer than two steps.

Thus an increasing top trajectory and a positive mass calculation on a
selected chain do not prove an aggregate obstruction. All source branches
and all historical intersections must be included. In particular, the
simple family `N=8*6^k` does not have an always-positive top component:
the example above is `k=4`.

## 5. Reproduction and remaining obligation

Run from the repository root:

```sh
python3 experiments/residual_progress/templates/check_inverse_exposure.py
```

The default run finishes in about one second on the development machine.
It compares inverse components against independently materialized forward
graphs at `N=8,16,96,288`, depths `1,2,4,8`, and three actual sources at
each cutoff: **48 exact graph comparisons**. It separately brute-forces
all odd predecessor candidates through 2047, checks both cap exits, and
reproduces the two full components above. The independently generated
small annuli are compared against the oracle's coefficient function.

`inverse_exposure_audit.json` contains the graphs, masses, and check
receipts. `--write-receipt` intentionally regenerates it. No data is
rewritten by the ordinary check.

**Open.** Does every fixed `D` admit a required-ray annulus with a positive
component in `G_D(N)`? The finite depth-32 example does not answer this.
A possible next step is to lift a *complete component closure*, including
every exclusion of an additional inverse edge, across a parameter family.
Lifting the positive chain alone is insufficient. No family of residuals
closed under recursive template packing has been proved here.
