# From annular components to universal partial current families

Written proofs and finite certificates, 17 October 2026. No complete annular
constructor or proof of Collatz is claimed. The actual source measure here is
`A_N=Pi_right_(64N)-Pi_right_N`, for `8|N`, with the six-band table in
`experiments/current_construction/recursive/annular_recursion.md`.

## 1. Incremental graph findings

The new constructor uses multi-source breadth-first exposure and union-find.
Every original nonzero source is at depth zero; each newly discovered state
is expanded only once. The graph after layer `d` is exactly the union of the
first `d` arrows from every source. Each component keeps its total signed
source mass and its six separate band contributions. This avoids rebuilding
the whole historical graph at each depth, without changing the certificate
criterion.

All searches below had cap 128. Their final currents were checked by exact
one-step divergence arithmetic.

| N | Aggregate nonpositive residual | Each band nonpositive residual | Aggregate exact | Each band exact |
|---:|---:|---:|---:|---:|
| 96 | 28 | 33 | 45 | 45 |
| 112 | 32 | 32 | 45 | 45 |
| 128 | 44 | 44 | 45 | 45 |
| 144 | 29 | 34 | 45 | 45 |
| 168 | 34 | 44 | 41 | 44 |
| 384 | 42 | 42 | 84 | 84 |

The per-band columns use the **same exposed graph**, including arrows
discovered from all six bands. They test whether each band's mass separately
satisfies the component criterion. Hence the comparison isolates actual
cancellation across bands, rather than differing search effort.

At `N=168`, aggregate exact success at depth 41 leaves one component unlinked
to 1, with source states `(10087,15131,22697)` and coefficients `(-1,-1,2)`.
Its band-mass vector is `(0,0,0,0,-1,1)`. The individual fifth and sixth bands
cannot both be certified on this graph, while their combined measure is an
exact divergence. The other successful aggregate exact cases in this table
already link every source to 1. That distinction is retained in the receipt.

At `N=96`, nonpositive-residual success at depth 28 leaves a balanced component
on `(4591,6121,6887,10331,13775)` with coefficients `(-1,-1,1,2,-1)`.
Its band masses are again `(0,0,0,0,-1,1)`. These finite components provide
the two arithmetic templates below.

## 2. An affine compiler theorem

Consider a finite directed tree of positive odd Syracuse states with a common
sink `w`. Each non-sink edge `x -> y` has its exact valuation `a_x>=1`, so
`3x+1=2^(a_x)y`. Let `d_x` and `A_x` be the number of edges and total
valuation from `x` to `w`. Let `D=max_x d_x`. Define, for every integer `t>=0`,

`x(t)=x+2^(A_x+1)*3^(D-d_x)*t`.

Write the slope as `v_x`. For every edge, `d_x=d_y+1` and
`A_x=a_x+A_y`, whence `3v_x=2^(a_x)v_y`. Therefore

`3x(t)+1=2^(a_x)y(t)`.

Every `y(t)` is odd, so the valuation remains **exactly** `a_x`. All lifted
edges are actual Syracuse edges. At a sink originally equal to 1, the lifted
sink can exceed 1; no continuation from that sink is used.

Route finite integer source weights along this tree to `w`, producing signed
current weights `J(x)`. If the source total is `m`, then the same weights on
the lifted tree give

`mu_t=(I-P)J_t+m delta_(w(t))`,

with the sink term discarded when `w(t)=1`. Thus zero source mass gives an
exact current for every `t>=0`, and negative source mass gives a nonpositive
residual. Any coincident lifted states are combined; linearity preserves the
identity. The positive current cost is at most `sum_x max(J(x),0)`.

This theorem turns one finite tree into an infinite family of exact identities.
It does **not** assert that its lifted source coefficients occur in an actual
annular measure. That separate coverage check is essential.

## 3. A five-source template with exact annular coverage

The five sources from `A_96` have a common sink 17435. Their relevant paths are

```
6121 -> 4591 -> 6887 -> 10331 -> 15497 -> 11623 -> 17435
13775 -> 20663 -> 30995 -> 46493 -> 17435
```

The maximum path length is six. The compiler gives the following source
identity, valid for every integer `t>=0`:

```
mu_t = -delta_(4591+384t) -delta_(6121+512t)
       +delta_(6887+576t) +2delta_(10331+864t)
       -delta_(13775+1152t).
```

Its exact current consists of the following rows; a row `(x,v,c)` means
current coefficient `c` at the state `x+vt`.

| x | v | c |
|---:|---:|---:|
| 4591 | 384 | -2 |
| 6121 | 512 | -1 |
| 6887 | 576 | -1 |
| 10331 | 864 | 1 |
| 11623 | 972 | 1 |
| 13775 | 1152 | -1 |
| 15497 | 1296 | 1 |
| 20663 | 1728 | -1 |
| 30995 | 2592 | -1 |
| 46493 | 3888 | -1 |

The positive current cost is 3. This gives `H_L(mu_t)<=3` for every horizon
and every parameter, without following the common sink.

For actual annular coverage, take `t=9s+r` with `s>=0` and `r in {0,3}`.
The first three source states must lie in band 4, namely `(36N,72N)`, and
the last two in band 5, namely `(72N,144N)`. Their residues modulo 18 are

```
r=0: (1,1,11,17,5)
r=3: (1,7,11,17,5).
```

Both give exactly the required coefficients `(-1,-1,1,2,-1)` from the
annular table. All five strict band constraints reduce, for `8|N`, to

```
r=0:  96+72s <= N <= 120+96s;
r=3: 120+72s <= N <= 152+96s.
```

To verify the reduction directly, the largest lower bound on `N` comes from
the last source (and agrees after integer rounding with the third source).
The smallest upper bound comes from the first source. For `r=0` these give
`96+72s<=N<=127+96s`, and for `r=3` they give
`120+72s<=N<=159+96s`; restricting `N` to multiples of eight gives the
displayed endpoints. The other three bounds are weaker for every `s>=0`.

Equivalently, define

```
I_0(N) = {s>=0: ceil((N-120)/96) <= s <= floor((N-96)/72)};
I_3(N) = {s>=0: ceil((N-152)/96) <= s <= floor((N-120)/72)}.
```

**All admissible copies can be removed simultaneously.** There are ten source
progressions, with offsets `x_i+r v_i` and periods `9v_i`. For each pair of
different progressions, `gcd(9v_i,9v_j)` does not divide the offset difference.
The 45 exact integer checks are recorded by the checker. Consequently the
progressions have no common integer state, even if their parameters differ.
There is no use of the same annular source coefficient twice.

Let `C(N)=|I_0(N)|+|I_3(N)|`, and let `M_N` be the sum of these disjoint
five-source measures. Their summed current `K_N` is finite and satisfies

`M_N=(I-P)K_N`, `|supp M_N|=5C(N)`,
`||M_N^+||_1=3C(N)`, and `||K_N^+||_1<=3C(N)`.

The remainder `A_N-M_N` is exactly the annular measure with those source
atoms deleted. In particular, its positive mass is `99N/4-3C(N)`, and a
current with nonpositive residual for that remainder would extend to one for
the original annulus.

The count has the asymptotic `C(N)=N/144+O(1)`. Copies exist for every
multiple of eight with `96<=N<=152` or `N>=168`; `N=160` has no admissible
copy. For the eventual claim, the `r=0` intervals with `s>=2` overlap and
cover all multiples of eight from 240 onward, while the `s=1` intervals
cover 168 through 248. This is a universal partial construction for every
sufficiently large allowed cutoff, not merely the scale line `N=96(1+s)`.

Its removed positive mass is asymptotically `N/48`, about `1/1188` of the
annulus's full positive mass. The numerical fraction is small. The structural
result is that an exposed balanced component has been compiled into a valid,
capacity-checked arithmetic family for all large source cutoffs.

## 4. The two-row cross-band family

For every `8|N`, every `x` with `48N<x<64N` and `x=7 mod72` gives

`Sx=(3x+1)/2`, `S^2x=(9x+5)/4`,

and actual annular coefficients `(-1,-1,2)` at those three states. The first
state is in band 4 and the other two in band 5. Hence

`-delta_x-delta_(Sx)+2delta_(S^2x)=(I-P)(-delta_x-2delta_(Sx))`.

This current is nonpositive, so the triple's work is at most zero at every
horizon. Different admissible `x` give disjoint triples: their first states
are in a different band, and the two later source progressions have different
residues 11 and 17 modulo 18. The component `(10087,15131,22697)` at `N=168`
is one instance. The compiler independently lifts it with slopes `(8,12,18)`;
choosing `t=1008s` keeps it in `A_(168(1+s))` for all `s>=0`.

The companion symbolic-chain work extends this elementary rule to the five
families E,D,B,C,A in `arithmetic/ARITHMETIC_RESULTS.md`. Their nonzero source
supports are also disjoint from the entire two-class five-source packing
above. This additional capacity claim has its own proof:

- The first five-source atom has band-4 residue 1 and is below `48N`.
  Indeed its distance below `48N` is at least 17, using the smallest
  admissible cutoff. It misses catalogue family A's input interval.
- The second has band-4 residue 1 or 7, but its residue modulo 72 is 1
  or 25. The only catalogue inputs of these band-4 modulo-18 types require
  residue 7 or 55 modulo 72.
- The third has band-4 residue 11 and lies above `48N`. Catalogue family
  B's band-4 residue-11 images lie strictly between `36N` and `48N`.
- The fourth has band-5 residue 17 and lies in `81N<x<108N`. At the
  largest admissible cutoff it exceeds `81N` by at least 611, and at the
  smallest it is below `108N` by at least 37. This separates it from
  catalogue C's images in `(72N,81N)` and A's images in `(108N,144N)`.
- The fifth has band-5 residue 5, which is unused by the catalogue.

Each statement follows from the exact admissibility intervals in Section 3,
for both residue classes. Thus the combined removed positive mass is exactly
`D(N)+3C(N)`, where `D(N)` is the catalogue's stated floor-count formula.
Its summed current has positive cost at most `3C(N)`, since the catalogue
current is nonpositive. The remaining positive mass is therefore exactly
`99N/4-D(N)-3C(N)`. It is still positive and unhandled in general. The checker
also confirms the new cross-family claim by independently inverting each
catalogue affine map at every previously checked source point.

## 5. A failed stronger candidate and the remaining obligation

An everywhere-nonpositive current with nonpositive residual would imply
`H_L(A_N)<=0` at every horizon. This is false: exact finite witnesses are

`H_53(A_96)=699`, and `H_9(A_384)=42`.

In particular, every current with nonpositive residual for `A_96` has positive
current cost at least 699. The useful zero-cost local rules cannot by themselves
eliminate the entire positive-work obligation.

What remains is a universal construction for the residual after valid partial
families are removed, or a proof that further families cover it without
overusing source coefficients. The compiler proves each supplied tree's
identity and checks coverage; it does not prove that mining enough trees
terminates or that the unhandled positive components disappear.

## Reproducibility

`affine_template_compiler.py` checks both compiled identities at arbitrary-size
integer parameters, the linear band bounds on selected scales through `64^20`,
all 45 progression-capacity checks, and every allowed cutoff from 8 through
4096 for the summed two-class family. `affine_templates.json` is its receipt.

`annular_components.py` contains the capped incremental constructor. Its audit
driver stores the six requested annular diagnostics, finite work witnesses,
and selected actual current tables. All checks use integer arithmetic.

Actual reproduction commands, both passing on 17 October 2026:

```sh
python3 experiments/annular_construction/components/affine_template_compiler.py
python3 experiments/annular_construction/components/check_annular_components.py
```

Use `--write-receipt` only to update each script's persisted output. Default
runs compare against the existing receipts and current tables.
