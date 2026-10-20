---
id: bounded-source-cluster-local-bound
kind: result
title: All annular sources on one E0 path lie within a sharp span of 63 arrows, but forbidden exits can lead into source-empty components
status: written
claim: >
  Odd-only 3x+1 map, absorbing at 1; A_N the six-band annulus (8 | N, Q = 9N/4); E0 the restricted path graph
  of signed-path-collapse-capacity. (Span) With the adjusted height h(x) = x for x = 1 mod 3 and x/2 for
  x = 2 mod 3, every nonzero source has Q < h(x) < 32Q, and two nonzero sources on one E0 path have even
  separation at most 58 or odd separation at most 63; the bound 63 is attained, for every t >= 1, by
  x = 3 2^95 t - 5 with the word (1,2)^31,1 (exact cylinder modulus 2^95), Q = 18 floor(x/18). (Local
  constructor) At most 63 predecessor and 63 successor queries from a source recover all sources of its
  complete E0 component; prefix sums give an exact current placing the cluster mass at its last source, with
  rows below 192N and ||J+||_1 <= 63 ||A_N+||_1 = 6237N/4 (a bound for this preprocessing only); a finite
  arithmetic guard scheme with sufficient period 2^96 3^65 describes it. (Exits) A forbidden E0 edge x -> y of
  valuation 2 lands on a smaller inactive root, and one of valuation >= 3 lands in a component whose root is
  below x/4 (compared with the exit vertex x, not the last source). For N = 96 64^k with k odd, the first exit
  of the Mersenne component enters an E0 component with no original annular source, so the rule that every
  positive cluster's first forbidden exit joins negative source mass is false. Plateau termination is not
  claimed.
authors:
  - ChatGPT main lane (Codex)
created: 2026-10-17
depends_on: [signed-path-collapse-capacity, disjoint-annular-recursion]
evidence:
  - "check_window_components.py, window_components_audit.json: the legacy constructors (cluster_at_source, collapse_annulus, compile_guard, sharp_component) and checker (complete clusters against full-root grouping at N = 8, 16, 24, 96, 160, 168, 384, 768; all current identities and limits; sharp-span examples at t = 1, 2, 3, 9 with all 64 coefficients and slope checks; 14 affine-guard translations; forbidden edges through 8193; source-empty exit targets at k = 1, 3, 5, 31). Fails at its new path: it loads experiments/residual_progress/alternating/check_alternating_paths.py relative to the repository root (now ../signed-path-collapse-capacity/, which itself no longer runs). Passed at be73a66 as experiments/residual_progress/window_components/check_window_components.py inside scripts/verify_all.py (archive/legacy-checker-run-be73a66.md: the gate ran these steps before stopping at residual_progress/history_frontier, and passed in full at 9dbc71a)"
  - "../auxiliary-normalisation-remainder/batch_r15_r18_r21_r29_check.py: side-lane probe, a certificate of that node, which also checks the adjusted-height arithmetic below (passes at its new path)"
reviewed_by:
  - by: Claude side lane (Opus)
    date: 2026-10-18
    link: ../auxiliary-normalisation-remainder/batch_r15_r18_r21_r29_check.py
    scope: "Finite arithmetic only (side-lane feed entry 2026-10-18 11:32, VERIFIED, main 9190ccf): for all odd x < 2 10^5 the adjusted-height factors (> 3/4 from type 1, > 3/2 from type 2, a shrinking step lands on type 2) and the numeric bounds behind 58 and 63; the sharp path for t = 1..5 (word (1,2)^31,1, cost 94, in E0, ends in (Q, 32Q)); each of the 16,666 valuation-2 forbidden edges lands on a smaller inactive root and each of the 25,000 with valuation >= 3 in a component rooted below x/4. Source and cluster masses (which need A_N) were not checked. The status stays written"
aliases: [R21]
tags: [convergence, packet-currents, annular, path-graph, local-bound, obstruction]
---

# All annular sources on one E0 path lie within a sharp span of 63 arrows, but forbidden exits can lead into source-empty components

## Statement

`A_N` is the six-band annulus, `8 | N`, `Q = 9N/4`; odd-only clock, absorbing at 1. `E0` is the restricted graph of [`signed-path-collapse-capacity`](../signed-path-collapse-capacity/README.md) (its components are paths with a unique finite backward root). A *source cluster* is the set of all nonzero `A_N` atoms in one complete `E0` component, with the zeros between them; it is not a complete exposed component of the unrestricted graph.

1. **Span theorem.** With `h(x) = x` (`x ≡ 1 mod 3`) and `h(x) = x/2` (`x ≡ 2 mod 3`), every nonzero source has `Q < h(x) < 32Q` (the coefficient table vanishes on the relevant half-bands). Type-1 steps multiply `h` by more than `3/4`, type-2 steps by more than `3/2`, shrinking steps are never consecutive, and `(9/8)^29 < 32 < (9/8)^30`, `(3/4)(9/8)^31 < 32 < (3/4)(9/8)^32`. Hence two nonzero sources on one `E0` path have even separation `≤ 58` or odd separation `≤ 63`; a cluster occupies at most 64 consecutive positions.
2. **Sharpness.** For `t ≥ 1`, `x = 3·2^95·t − 5`, `Q = 18⌊x/18⌋`, `N = 8⌊x/18⌋`, the word `(1,2)^31,1` (total valuation 94, cylinder modulus `2^95`) is realized exactly, with nonzero sources at both ends; it is the entire cluster, of mass 38 if `3 ∤ t` and 35 if `3 | t`.
3. **Bounded constructor.** At most 63 predecessor and 63 successor `E0` queries from a source find every source of its component; the prefix-sum current places the cluster mass at its last source. All rows lie below `192N`; `‖J⁺‖₁ ≤ 63‖A_N⁺‖₁ = 6237N/4` (a partial-construction bound, not a cost bound for certificates). The guard period `M = 2^96·3^65` gives a finite arithmetic template description (sufficient, not minimal, and not closed under continuation).
4. **Forbidden exits.** For a forbidden `E0` edge `x → y`: valuation 2 from `x ≡ 1 (mod 3)` or `0 (mod 3)` lands on an inactive root `y < x`; valuation `≥ 3` lands in a component with root `b(y) < x/4`. The comparison is with the exit vertex `x`, which may lie far above the last source; no cycle exclusion is assumed.
5. **Source-empty exits.** For `N = 96·64^k`, `k` odd, the Mersenne cluster `(−2, +2, +2)` exits to `w = (3^L − 1)/8 ≡ 1 (mod 18)`, `w > 144N`, already a root; the whole target component has zero original source mass, so the transported mass 2 becomes an auxiliary source. This refutes the rule that a positive cluster's first forbidden exit always joins a negative source cluster.

Universal local statements and a finite description; universal plateau termination and complete annular certificates remain open. No novelty is claimed.

## Proof

The legacy note "Complete annular source clusters have sharp span63" follows, lightly edited (headings demoted one level, links pointed to nodes). Its commands name pre-migration paths; see Certificates.

Date: 2026-10-17. **Status: written elementary proofs, executable finite
preprocessing, and bounded checks.** This is a local description and
partial current construction. It does not prove that positive components
eventually resolve. No novelty is claimed.

Use the odd Syracuse map S, absorbed at1. Let `8|N`, `Q=9N/4`, and use the
six-band annulus `A_N`. The restricted graph `E0` consists of valuation1
arrows and valuation2 arrows whose source is2 modulo3. Its components are
paths with a unique finite backward root, as proved in
[the path note](../signed-path-collapse-capacity/README.md). A *source cluster*
means **all nonzero A_N atoms in one complete E0 component**, including
zeros between them in its retained path. It is not a complete exposed
component of the unrestricted Syracuse graph.

### 1. An adjusted height gives a sharp uniform bound

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

### 2. Sharpness, including the exact cylinder's extra bit

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

### 3. A bounded constructor that finds every source in a component

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

### 4. An exact finite arithmetic description

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

### 5. What a forbidden edge actually tells us

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

#### The first forbidden exit need not find negative annular source mass

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

### 6. Reproduction and scope

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

## Certificates

No certificate runs in this folder: the legacy checker loads the `E0` constructors of [`signed-path-collapse-capacity`](../signed-path-collapse-capacity/README.md) by their pre-migration path and is evidence only. The adjusted-height arithmetic, the sharp path for `t = 1..5` and the forbidden-edge classification below `2·10⁵` are certified by the side-lane script [`batch_r15_r18_r21_r29_check.py`](../auxiliary-normalisation-remainder/batch_r15_r18_r21_r29_check.py), a certificate of [`auxiliary-normalisation-remainder`](../auxiliary-normalisation-remainder/README.md). The command in the legacy text names `experiments/residual_progress/window_components/`.

## Remarks

- **What a complete construction needs.** A rule for the auxiliary source-empty components and a proof of eventual progress ([`annular-component-progress-lemma`](../../questions/annular-component-progress-lemma.md)); additional local templates are useful only with an account of which unresolved roots they cover.
- The sufficient-sets audit in [`five-ray-profile-completion-suffices`](../five-ray-profile-completion-suffices/README.md) found no primary theorem with the six-band window and the sharp 63-arrow span among the sources it read; that is not a proof of novelty. Novelty undetermined.

## History

- Migrated from `experiments/residual_progress/window_components/WINDOW_COMPONENTS.md` (legacy ID R21) at commit `be73a66`, by the B09 migration (Claude, Opus 5.5). Note, checker and receipt moved byte-identical. Legacy status: "written universal local bound and finite preprocessing constructor; no universal exit or plateau termination claim".
- Main lane (ChatGPT, Codex), 2026-10-17, from commit `65093c4`. Its "independent model review" of the source-cluster proof was the main lane's own agents; integration review clarified the cutoff domain and the convention root(1) = 1. The side lane's finite check is recorded under `reviewed_by`.
