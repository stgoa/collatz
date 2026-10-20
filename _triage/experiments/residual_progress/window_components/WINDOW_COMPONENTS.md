# Complete annular source clusters have sharp span63

Date: 2026-10-17. **Status: written elementary proofs, executable finite
preprocessing, and bounded checks.** This is a local description and
partial current construction. It does not prove that positive components
eventually resolve. No novelty is claimed.

Use the odd Syracuse map S, absorbed at1. Let `8|N`, `Q=9N/4`, and use the
six-band annulus `A_N`. The restricted graph `E0` consists of valuation1
arrows and valuation2 arrows whose source is2 modulo3. Its components are
paths with a unique finite backward root, as proved in
[the path note](../alternating/ALTERNATING_PATHS.md). A *source cluster*
means **all nonzero A_N atoms in one complete E0 component**, including
zeros between them in its retained path. It is not a complete exposed
component of the unrestricted Syracuse graph.

## 1. An adjusted height gives a sharp uniform bound

No annular source is divisible by3. Define, for the other states,

\[
h(x)=\begin{cases}x,&x\equiv1\pmod3,\\x/2,&x\equiv2\pmod3.\end{cases}
\]

The coefficient table vanishes on residue2 modulo3 in the lowest band and
on residue1 modulo3 in the highest band. Consequently **every nonzero
annular source** satisfies

\[
Q<h(x)<32Q.
\]

An E0 successor is never divisible by3. From a type1 state the only
allowed outgoing edge has valuation1, and

`h(Sx)=(3h(x)+1)/4 > (3/4)h(x)`.

From a type2 state, either allowed valuation gives

`h(Sx)=(6h(x)+1)/4 > (3/2)h(x)`.

Call the former step a shrinking step. Shrinking steps cannot be
consecutive, because their targets have type2. Thus a length `2m` E0
segment multiplies h by more than `(9/8)^m`; a length `2m+1` segment
multiplies it by more than `(3/4)(9/8)^m`.

For two nonzero source endpoints the ratio of adjusted heights is below32.
Exact integer comparisons give

\[
(9/8)^{29}<32<(9/8)^{30},\qquad
\tfrac34(9/8)^{31}<32<\tfrac34(9/8)^{32}.
\]

**Theorem.** Two nonzero annular sources on one E0 path have even
separation at most58 or odd separation at most63. Hence the whole source
cluster lies in at most64 consecutive path positions.

This argument allows single-step dips, excursions through zero source
coefficients, and re-entry into a band. It does not assume ordinary or
adjusted height is monotone at every step. Roots and future exits can be
arbitrarily farther away than this source segment.

Without the coefficient table's empty half-bands, a raw window
`Q<x<64Q` would give only an even bound70 and odd bound75. The sharper
bound genuinely uses the signed annular source's support.

## 2. Sharpness, including the exact cylinder's extra bit

For each integer `t>=1`, set

\[
x=3\,2^{95}t-5,\quad Q=18\lfloor x/18\rfloor,\quad
N=8\lfloor x/18\rfloor.
\]

Follow the length63 word `(1,2)^31,1`. Its exact total valuation is94,
so its cylinder has modulus `2^95`, **not** `2^94`. More generally the
whole word is realized exactly by `x=2^95 u-5`, u positive; taking `u=3t`
also makes every valuation2 source have residue2 modulo3.

The states are

\[
x_{2j}=3\,2^{95-3j}9^j t-5\quad(0\le j\le31),
\]
\[
x_{2j+1}=9\,2^{94-3j}9^j t-7\quad(0\le j\le31).
\]

At every even index before the last arrow the state is3 modulo4, and at
every odd index before the last state it is1 modulo8. Thus all valuations
are exact. The final state is `y=2*3^64*t-7`. Direct integer inequalities
give `Q<x<2Q` and `32Q<y<64Q`; their residue classes have nonzero annular
coefficients. The span is therefore63. The bound just proved excludes any
additional nonzero source before x or after y, so this is the entire
source cluster.

The first residue is1,7,13 modulo18 as t is1,2,0 modulo3. All subsequent
even-index residues are13, and all odd-index residues are11. Its total
source mass is38 for `3∤t` and35 for `3|t`. These statements are finite
arithmetic identities, not asymptotics: in each phase

`Q=3*2^95*t-epsilon`, with `epsilon=6,12,18` respectively.

Each band-gap inequality is affine in t. Checking it at the first phase
value `t=1,2,3`, and checking that its slope is nonnegative, proves it for
all later t in that phase. The checker retains all64 coefficients and
performs those exact slope checks. The sharp cluster remains positive;
its finite local description does not settle its future.

## 3. A bounded constructor that finds every source in a component

Starting from any nonzero source x, inspect at most63 E0 predecessor edges
and63 E0 successor edges, stopping early at a missing edge. The theorem
guarantees that every nonzero source in its complete E0 component is found.
Discard only leading and trailing zero source positions; retain every
intermediate position between the first and last nonzero source.

For the resulting path `x_0,...,x_d`, `d<=63`, let `a_i=A_N(x_i)` and
`m=sum_i a_i`. The exact current and residual are

\[
J(x_i)=\sum_{j=0}^{i}a_j\quad(0\le i<d),\qquad
\mu_{cluster}=(I-P)J+m\delta_{x_d}.
\]

Process each source cluster once. The result is the same frontier
aggregation as in the earlier path note, obtained with a constant local
query bound per cluster instead of walking all the way to its backward
root. No forward exit search is involved.

All current rows are below192N. Indeed, relative to the final source z,
an earlier vertex at even distance is below z, and one at odd distance is
below `4z/3`; this follows from ordinary two-step growth and the lower
one-step factor3/4. Since `z<144N`, the claim follows.

The current also has the explicit partial-construction bound

\[
\|J^+\|_1\le63\,\|A_N^+\|_1=\frac{6237N}{4}.
\]

Each original positive unit contributes to at most63 prefix rows; negative
source units can only lower those rows. Every positive frontier mass is
retained. This bound is **not** a cost bound for complete certificates.

## 4. An exact finite arithmetic description

The bounded constructor gives a finite description even though an explicit
list of all patterns would be very large.

For a forward word `a_0,...,a_(d-1)`, write

`A_0=b_0=0`, `A_(j+1)=A_j+a_j`, `b_(j+1)=3b_j+2^A_j`.

Then

\[
x_j=(3^j x+b_j)/2^{A_j}.
\]

Words use only1 and2, with no consecutive2. They also retain the residue2
source condition for an initial valuation2. Exact valuation constraints
use modulus `2^(A_d+1)`. On each residue class modulo
`9*2^(A_d+1)`, all word states have fixed residues modulo18; the source
weights are determined by their six linear band inequalities.

To include complete-cluster boundary guards, a single sufficient universal
period is

\[
M=2^{96}3^{65}.
\]

Fix the anchor's residue class modulo M. A length63 allowed forward word
has total valuation at most95. The binary factor in M preserves every
queried exact branch, including its extra bit, and the residues modulo18
of all forward states. In a length r inverse segment, a change of anchor
by M changes the state by `2^A*M/3^r`. For `r<=63`, this remains an integer
multiple of18. Thus every predecessor decision and every residue in the
63-step inverse guard is fixed as well.

Consequently each guard state has an exact formula `u_i+v_i*t` for an
anchor `r+M*t`. The coefficients v_i are positive integers. A band is
selected by the linear inequalities

\[
2^b(9N/4)<u_i+v_i t<2^{b+1}(9N/4).
\]

The exterior intervals and the six band alternatives partition the domain;
odd states and the even band boundaries prevent equality ambiguities.
The anchor is required to be a nonzero source. On each resulting cell,
the complete source list, all weights, the prefix-current coefficients,
the total mass, and the chosen frontier formula are fixed. There are at
most127 guard positions and at most64 positions from first to last source.

This is a finite arithmetic template scheme with unbounded integer
parameters. It is not claimed to be a practical enumerated catalogue or
to be closed under future transitions. In particular, M is a sufficient
guard period, not an asserted minimal one.

## 5. What a forbidden edge actually tells us

Let `x -> y=S(x)` be a forbidden E0 edge and let b(y) be the root of the
target E0 component, with `b(1)=1`.

- **Valuation2, source1 modulo3:** `x=1 modulo24` and `y=1 modulo18`.
  The successor is already an inactive root and `y<x`.
- **Valuation2, source0 modulo3:** `x=9 modulo24` and `y=7 modulo18`.
  Again the successor is an inactive root and `y<x`. A component carrying
  original nonzero annular sources cannot end at a multiple of3, but this
  case completes the general classification.
- **Valuation a>=3:** the target root satisfies `b(y)<x/4`.

For the last assertion, if a is odd, y has residue2 modulo3 and has the
allowed valuation1 predecessor `q=(2y-1)/3`. Set `a-1=2s`, s>=1; then

`x=4^s q+(4^s-1)/3`, so `b(y)<=q<x/4`.

If a is even, then a>=4 and y has residue1 modulo3. If y is13 modulo18,
its allowed valuation2 predecessor `q=(4y-1)/3` gives the same identity
with `a-2=2s`, again s>=1. Otherwise y is already inactive, and
`b(y)=y=(3x+1)/2^a<x/4`.

The quarter bound compares with **the originating exit vertex x**, not
with its successor y, nor with the last annular source. A long E0 segment
can grow arbitrarily far before reaching x. The target component also need
not be different from the starting component without an additional cycle
exclusion; no such exclusion is assumed here.

### The first forbidden exit need not find negative annular source mass

Use the already proved Mersenne family

`N=96*64^k`, `L=12+6k`, with k positive and odd.

Its entire original E0 source cluster has weights `(−2,+2,+2)` and total2.
The first forbidden edge leads to

\[
w=(3^L-1)/8\equiv1\pmod{18},\qquad w>144N.
\]

Thus w is already the target component's root. Every E0 vertex is at
least its component root (equivalently, the old unit-atom normalizer only
decreases height). Therefore the **entire target E0 component has zero
original A_N source mass**. The transported positive mass2 is an auxiliary
source there, not a cancellation with original negative mass.

This refutes the proposed universal rule that a positive source cluster's
first forbidden exit always joins a negative source cluster. It also
pinpoints why the finite annular template scheme is not closed under the
required continuation: positive mass can enter components containing no
annular source at all. A complete construction needs a rule for these
auxiliary components and a proof of eventual progress.

## 6. Reproduction and scope

`check_window_components.py` provides `cluster_at_source`,
`collapse_annulus`, `compile_guard`, and `sharp_component`. Every current
is returned with its exact residual. The local constructor has fixed
63-step limits; the checker's independent comparison uses the earlier
proved finite full-ancestry routine.

```sh
python3 experiments/residual_progress/window_components/check_window_components.py
```

The receipt checks complete clusters against independent full-root
grouping at N8,16,24,96,160,168,384,768; all current identities and limits;
four sharp-span examples at t1,2,3,9; all three sharpness band phases and
their nonnegative slopes;14 affine-guard translations; forbidden edges
through8193; and source-empty exit targets at k1,3,5,31. No enormous
annulus is materialized for the sharp or delayed families.

The source-span bound and finite arithmetic description are universal
local statements. Universal plateau termination and complete annular
certificates remain open.
