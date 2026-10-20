---
id: depth-32-aggregate-exposure-obstruction
kind: result
title: An exact inverse oracle finds a complete positive depth-32 exposed component of a required annulus
status: written
claim: >
  Odd-only 3x+1 map, absorbing at 1; A_N the six-band annulus (8 | N); G_D(N) the first D arrows exposed from
  every nonzero source of A_N. (Oracle) A capped inverse-reachability recursion under the exact height bounds
  B_r = floor(3^r 144N / 2^r) - 1 decides membership in G_D(N) exactly and saturates one complete component,
  including every incoming arrow, without enumerating the O(N) source support; exceeding a cap returns
  unresolved. (Finite obstruction) At N* = 96 2^24 = 12 2^27 and D = 32 the component of 144N* - 1 in the
  entire G_32(N*) is the 35-vertex chain x_j = 3^j 64N*/2^j - 1 (0 <= j <= 34), whose only sources are
  (64N* - 1, -2), (96N* - 1, +2), (144N* - 1, +2); its mass is 2 and it does not contain 1, so no current
  supported on G_32(N*) represents A_(N*) with nonpositive residual, and no packed source cover by
  common-tail trees of source-to-anchor depth <= 32 exists at that cutoff. (Naive chain fails) At N = 10368,
  depth 2, the complete top component has 27 sources of total mass 0 (+22, -22) and is not linked to 1.
  Deeper or different currents are not excluded.
authors:
  - ChatGPT main lane (Codex)
created: 2026-10-17
depends_on: [disjoint-annular-recursion, orbit-component-current-criterion]
evidence:
  - "unbounded-exposure-depth-necessary/check_inverse_exposure.py, unbounded-exposure-depth-necessary/inverse_exposure_probe.py, unbounded-exposure-depth-necessary/inverse_exposure_audit.json: the legacy oracle (inverse_exposure_probe.py: coefficient, predecessors, component) and its checker (48 comparisons with independent forward graphs at N = 8, 16, 96, 288, depths 1, 2, 4, 8; brute-force predecessors through 2047; both cap exits; the two full components above, stored vertex by vertex). The checker fails at its new path: it loads experiments/current_construction/recursive/check_annular_recursion.py relative to the repository root (now ../disjoint-annular-recursion/, which itself no longer runs). Passed at be73a66 as experiments/residual_progress/templates/check_inverse_exposure.py inside scripts/verify_all.py (archive/legacy-checker-run-be73a66.md: the gate ran these steps before stopping at residual_progress/history_frontier, and passed in full at 9dbc71a). The scripts sit in the folder of unbounded-exposure-depth-necessary because the other template checkers import the oracle from their own folder"
  - "unbounded-exposure-depth-necessary/check_symbolic_lift.py: a certificate of unbounded-exposure-depth-necessary that, among other things, reruns the integer oracle at q = 1, that is at N* and depth 32, and checks that the complete component is exactly the 35-vertex chain with sources (-2, +2, +2); it passes at its new path"
aliases: [R13-b]
tags: [convergence, packet-currents, annular, exposure-depth, inverse-oracle, obstruction, finite-certificate]
---

# An exact inverse oracle finds a complete positive depth-32 exposed component of a required annulus

## Statement

`A_N`, `8 | N`, is the six-band annulus of [`disjoint-annular-recursion`](disjoint-annular-recursion/README.md), `Q = 9N/4`, support in `(Q, 64Q)`; the map is odd-only Syracuse with absorption at 1. For `D ≥ 1`, `G_D(N)` contains the arrow `x → S(x)` exactly when `x ≠ 1` and some nonzero annular source reaches `x` in at most `D − 1` steps; this does not bound the length of an undirected component.

1. **Dual test.** If a component `C` of `G_D(N)` does not contain 1 and `A_N(C) > 0`, no finite current supported on the whole `G_D(N)` gives `A_N = (I − P)J + ζ` with `ζ ≤ 0` (the component indicator is an exact dual witness, as in [`orbit-component-current-criterion`](orbit-component-current-criterion/README.md)). A finite packed catalogue of common-tail trees with maximal source-to-anchor depth `D` has all its arrows in `G_D(N)`, so a positive component excludes a complete packing (also fractional combinations) at that cutoff. The implication is one-way: recursive rewrites can leave `G_D(N)`.
2. **Exact inverse oracle.** With `B_r = ⌊3^r·144N/2^r⌋ − 1`, the recursion `Reach(y, r)` over all predecessors `p = (2^a y − 1)/3 ≤ B_(r−1)` decides exactly whether a nonzero source reaches `y` within `r` steps; saturating outgoing and incoming exposed arrows from a source returns its entire component. Explicit vertex and query caps return `unresolved_cap`, never an obstruction.
3. **Depth-32 obstruction.** At `N* = 96·2^24 = 1 610 612 736` and `D = 32`, the component of `144N* − 1` in the entire `G_32(N*)` is the increasing chain `x_j = 3^j·64N*/2^j − 1`, `0 ≤ j ≤ 34` (35 vertices, 34 arrows, all valuations 1), with source table `103079215103 → −2`, `154618822655 → +2`, `231928233983 → +2`; mass 2, not linked to 1; 9171 memoized decisions, below the caps.
4. **Why the bare chain is not enough.** At `N = 10368`, depth 2, the complete component of the top source `1492991` has 34 vertices, 27 sources, positive and negative masses `22` and `−22`, and is not linked to 1.

No obstruction at every depth, universal construction, Collatz proof or novelty claim is made here; the every-depth theorem is [`unbounded-exposure-depth-necessary`](unbounded-exposure-depth-necessary/README.md).

## Proof

The legacy note "Complete aggregate exposure components and a depth-32 obstruction" follows, lightly edited (headings demoted one level, links pointed to nodes). Its commands name pre-migration paths; see Certificates.

Date: 2026-10-17. Status: written algorithm-correctness argument and finite
exact enumeration. No obstruction at every depth, universal construction,
Collatz proof, or novelty claim is supplied.

The measure is the actual six-band annulus `A_N`, for positive `8|N`, with
`Q=9N/4` and support in `Q<x<64Q`. All nonzero source coefficients are
retained. The map is odd-only Syracuse with absorption at 1. In particular,
the earlier obstruction for individual raw packets is not used here.

### 1. The exposure depth of a template is a necessary test

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

### 2. Exact inverse enumeration of one complete component

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

### 3. A complete depth-32 obstruction on a required ray

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

### 4. Why the naive increasing-chain argument fails in general

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

### 5. Reproduction and remaining obligation

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

#### Subsequent status

The separate [infinite-family lift](depth-32-obstruction-infinite-family.md) preserves
the **whole** depth-32 component over an infinite congruence family. The
later [unbounded-depth theorem](unbounded-exposure-depth-necessary/README.md) answers the
historical open question above: for every fixed `D`, there are infinitely
many required-ray annuli with a complete positive component in `G_D(N)`.
That proof exhausts all competing inverse histories with a preserved
arithmetic inequality; it does not extrapolate the finite scans here.
Unbounded-depth recursive current constructions remain open.

## Certificates

This node has no folder of its own. The depth-32 component is rechecked by [`check_symbolic_lift.py`](unbounded-exposure-depth-necessary/check_symbolic_lift.py), a certificate of [`unbounded-exposure-depth-necessary`](unbounded-exposure-depth-necessary/README.md), which reruns the integer oracle at `N*`, depth 32, and compares the full node, arrow and source sets. The 48 forward-graph comparisons and the `N = 10368` component are in the legacy checker and receipt `check_inverse_exposure.py`, `inverse_exposure_audit.json` (same folder), evidence only. The commands in the legacy text name `experiments/residual_progress/templates/`.

## Remarks

- The open question in §5 of the legacy text ("does every fixed `D` admit a required-ray annulus with a positive component?") is answered by [`unbounded-exposure-depth-necessary`](unbounded-exposure-depth-necessary/README.md), as the legacy "Subsequent status" paragraph says. The intermediate infinite family is [`depth-32-obstruction-infinite-family`](depth-32-obstruction-infinite-family.md).
- The annulus has `267N*/8 = 53 754 200 064` nonzero source atoms; the oracle does not enumerate them but uses the exact coefficient function at every potential inverse source.
- Novelty undetermined.

## History

- Migrated from `experiments/residual_progress/templates/AGGREGATE_EXPOSURE.md` (legacy ID R13, its first part; alias R13-b here) at commit `be73a66`, by the B09 migration (Claude, Opus 5.5). The note moved byte-identical before editing; the folder's scripts went to [`unbounded-exposure-depth-necessary`](unbounded-exposure-depth-necessary/README.md). Legacy status: "written algorithm-correctness argument and finite exact enumeration".
- Main lane (ChatGPT, Codex), 2026-10-17.
