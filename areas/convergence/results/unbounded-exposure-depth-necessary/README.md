---
id: unbounded-exposure-depth-necessary
kind: result
title: For every fixed exposure depth D, infinitely many required-ray annuli have a complete positive component in G_D(N)
status: written
claim: >
  Odd-only 3x+1 map, absorbing at 1; A_N the six-band annulus (8 | N); G_D(N) the first D arrows exposed from
  every nonzero source of A_N, with all historical intersections. For every integer D >= 1 and every positive
  integer X with 2^max(D+4,10) | X and X = 1 mod 3^(D+2), put N = 3X/128 and y_k = 3^k X/2^k - 1. The entire
  component of y_3 = 144N - 1 in G_D(N) is the path y_1 -> ... -> y_(D+3), whose only sources are
  (64N-1, -2), (96N-1, 2), (144N-1, 2); its mass is 2 and it does not contain 1, so no finite current supported
  on G_D(N) represents A_N with nonpositive residual. Such cutoffs are N = 96 64^(3^D t - 2), t >= 1, on the
  ladder starting at 96; hence the least sufficient exposure depth satisfies d*(96 64^k) >= v_3(k+2) + 1 for
  every k >= 0, and no finite catalogue of packed common-tail current trees of bounded source-to-anchor depth
  completes every actual annulus, even with signed, fractional and cross-packet combinations. It does not
  assert that a full current is absent at any cutoff; recursive constructions of unbounded total depth are
  not excluded.
authors:
  - ChatGPT main lane (Codex)
created: 2026-10-17
depends_on: [disjoint-annular-recursion, orbit-component-current-criterion, depth-32-aggregate-exposure-obstruction]
certificates: [check_unbounded_exposure.py, check_symbolic_lift.py]
evidence:
  - "unbounded_exposure_audit.json: receipt of check_unbounded_exposure.py, which compares its recomputation with it"
  - "symbolic_component_lift.py, symbolic_lift_audit.json: library and receipt of check_symbolic_lift.py, which certifies the companion node depth-32-obstruction-infinite-family (see Certificates)"
  - "inverse_exposure_probe.py: the inverse-reachability oracle imported by both certificates (a library; it checks nothing on its own). Legacy checkers of delayed-release-cancellation, short-delay-all-phase-obstruction and fixed-ternary-order-unbounded-depth import it from the pre-migration folder ../templates/ and no longer run"
  - "check_inverse_exposure.py, inverse_exposure_audit.json: the checker of depth-32-aggregate-exposure-obstruction (evidence there). Fails at its new path: it loads experiments/current_construction/recursive/check_annular_recursion.py relative to the repository root (now ../disjoint-annular-recursion/). Passed at be73a66 as experiments/residual_progress/templates/check_inverse_exposure.py inside scripts/verify_all.py (archive/legacy-checker-run-be73a66.md: the gate ran these steps before stopping at residual_progress/history_frontier, and passed in full at 9dbc71a)"
  - "depth_probe.py, depth_probe.json: side-lane probe (Claude side lane, 2026-10-17): builds the full forward exposure graph from every source of A_N with a separate union-find and confirms the theorem's component at the least admissible X for D = 1..4 (N = 312, 1608, 5496, 11328) and at the ray example N = 6144 (X = 2^18); it then keeps exposing until the chain's component is nonpositive or linked to 1. Fails at its new path: it imports affine_controls and progress_measures_audit from experiments/packet_currents/negative_controls/ by repository-relative path (now ../locally-collatz-like-control-barrier/). Passed at be73a66 as reviews/side_lane/depth_probe.py (archive/legacy-checker-run-be73a66.md, exit 0). Other side-lane probes (delayed_release_check, slow_cluster_probe, fixed_h_check) import its UnionFind and v3 from their own folders"
  - "q2_end_depth.py, q2_end_depth.json: side-lane probe (Claude side lane, 2026-10-18, the side lane's question Q2): for D = 1..4 and four admissible X each (13 cutoffs, N = 312..63816) it checks an exact link-depth identity for the chain's forward orbit against an independent union-find and records where the plateau ends. Finite data. Fails at its new path: it imports affine_controls and progress_measures_audit from experiments/packet_currents/negative_controls/ by repository-relative path (now ../locally-collatz-like-control-barrier/). Passed at be73a66 as reviews/side_lane/q2_end_depth.py (archive/legacy-checker-run-be73a66.md, exit 0) (about 390 s)"
reviewed_by:
  - by: Claude side lane (Opus)
    date: 2026-10-17
    link: depth_probe.py
    scope: "Finite only (side-lane feed entry 2026-10-17 19:03, VERIFIED, main 2be37b7): full forward union-find exposure graphs at the least admissible X for D = 1, 2, 3, 4 and at N = 6144 reproduce the chain y_1..y_(D+3), sources (-2, +2, +2), not linked to 1. 'These are finite checks; the theorem's quantifiers rest on its written proof.' The inverse-history argument was not re-derived, so the status stays written"
aliases: [R13]
tags: [convergence, packet-currents, annular, exposure-depth, obstruction, inverse-history]
---

# For every fixed exposure depth D, infinitely many required-ray annuli have a complete positive component in G_D(N)

## Statement

`A_N` is the six-band annulus of [`disjoint-annular-recursion`](../disjoint-annular-recursion/README.md), `8 | N`, `Q = 9N/4`, support in `Q < x < 64Q = 144N`. `G_D(N)` contains the first `D` odd-only Syracuse arrows from every nonzero source of `A_N`, absorbing at 1 ([`depth-32-aggregate-exposure-obstruction`](../depth-32-aggregate-exposure-obstruction.md)).

**Theorem.** Fix any integer `D ≥ 1` and any positive integer `X` with `2^max(D+4,10) | X` and `X ≡ 1 (mod 3^(D+2))`. Put `N = 3X/128` (an integer divisible by 8) and `y_k = 3^k X/2^k − 1`, `1 ≤ k ≤ D + 3`. The entire component of `y_3 = 144N − 1` in `G_D(N)` is the path `y_1 → y_2 → ⋯ → y_(D+3)`; its only annular sources are `(64N − 1, −2)`, `(96N − 1, 2)`, `(144N − 1, 2)`; its mass is 2 and it does not contain 1. No finite current supported on the whole `G_D(N)` represents `A_N` with a nonpositive residual.

**Required ray.** For every `D ≥ 1` and `t ≥ 1`, `X = 2^(2·3^(D+1)·t)` qualifies, giving `N = 12·2^(2·3^(D+1)·t − 9) = 96·64^(3^D·t − 2)`. Hence, with `d*(N)` the least exposure depth that supports a one-sided current (infinity allowed),

```
d*(96·64^k) ≥ v_3(k+2) + 1   for every k ≥ 0
```

(strengthened to `v_3(k+2) + 4` in [`delayed-release-cancellation`](../delayed-release-cancellation/README.md)).

**Consequence.** No finite catalogue of common-tail current trees, packed from actual annular coefficients, with bounded source-to-anchor depth, completes every actual annulus, even allowing signed coefficients, fractional combinations and cancellation across packets and bands. Recursive use with unbounded total depth, currents on larger graphs and depth depending on `N` remain allowed; the theorem does not assert that a full current is absent at any cutoff. It is a structural constraint on a constructor, not a refutation of the current criterion.

## Proof

The legacy note "Actual annular current certificates require unbounded exposure depth" follows, lightly edited (headings demoted one level, links pointed to nodes). Its commands name pre-migration paths; see Certificates.

Date: 2026-10-17. Status: written elementary proof with exact finite checks
and independent model-assisted audits. Not human peer-reviewed or formally
verified. No Collatz proof, counterexample, or novelty claim is supplied.

This theorem concerns the **whole actual annulus**, including every source
atom and every incoming historical connection. It strengthens the earlier
finite depth-32 example and its infinite fixed-depth lift. The source
family is the repository's revised six-band annulus `A_N`, `8|N`, with
`Q=9N/4` and support in `Q<x<64Q=144N`.

For `D>=1`, let `G_D(N)` include the first `D` odd-only Syracuse arrows
from every nonzero source of `A_N`, with absorption at 1. A component's
signed source mass must be nonpositive for a current supported on this
graph to have an everywhere nonpositive residual, unless that component
contains 1.

### 1. The theorem and all quantifiers

Fix an arbitrary integer `D>=1`. Let `X` be any positive integer satisfying

\[
2^{\max(D+4,10)}\mid X,\qquad X\equiv1\pmod{3^{D+2}},
\]

and put `N=3X/128`. Then `N` is an integer divisible by 8. Define

\[
y_k=\frac{3^kX}{2^k}-1,\qquad 1\le k\le D+3.
\]

**Theorem.** The entire component of the top source `y_3=144N-1` in
`G_D(N)` is precisely

\[
y_1\longrightarrow y_2\longrightarrow\cdots\longrightarrow y_{D+3}.
\]

Its only annular source atoms are

\[
(y_1,-2)=(64N-1,-2),\quad
(y_2,2)=(96N-1,2),\quad
(y_3,2)=(144N-1,2).
\]

Its signed mass is therefore **2**, and it does not contain 1. No finite
current supported on the whole graph `G_D(N)` can represent `A_N` with a
nonpositive residual.

These cutoffs exist on a required dyadic ray. For every `D>=1` and `t>=1`,
set

\[
e_D=2\cdot3^{D+1},\qquad
X=2^{e_Dt},\qquad
\boxed{\ N=12\cdot2^{e_Dt-9}.\ }
\]

The elementary congruence `2^(2*3^(D+1))=1 modulo 3^(D+2)` follows by
repeatedly cubing `4=1 modulo 3`. Also `e_Dt>=max(D+4,10)` and the ray
exponent `e_Dt-9>=3`. Thus for **every fixed exposure depth D**, infinitely
many cutoffs on the required ray with mantissa 12 fail at that depth.

Equivalently, every one of these examples lies on the single base-64
ladder starting at 96:

\[
N=96\cdot64^{3^Dt-2}.
\]

If `d_*(N)` is the least exposure depth that supports a one-sided current,
with infinity allowed, this gives the explicit lower bound

\[
d_*(96\cdot64^k)\ge v_3(k+2)+1,\qquad k\ge0.
\]

For `v_3(k+2)>=1`, use `D=v_3(k+2)` in the theorem. For valuation zero,
the bound follows because the depth-zero graph has positive source atoms
and no arrows.

#### Consequence for finite template catalogues

A finite catalogue of common-tail current trees whose sources are packed
from actual annular coefficients has a finite maximal source-to-anchor
depth `D`. Every arrow of every such copy lies in `G_D(N)`, after pruning
branches with no source. The theorem therefore rules out any such
catalogue completing every actual annulus, even allowing arbitrary signed
current coefficients, fractional combinations, and cancellation across
all packets and bands.

This allows recursive use of a finite catalogue with **unbounded total
depth**, currents using larger exposed graphs, and arbitrary finite depth
depending on `N`. It does not assert that a full current is absent at any
one of these cutoffs. Unbounded complexity is permitted by the programme's
sufficient criterion, so the theorem is a structural constraint on a
constructor, not a refutation of that criterion.

### 2. The three sources and the displayed arrows

The divisibility hypothesis makes every `y_k` an odd integer. In fact
`y_k+1` remains divisible by 2 through `k=D+3`, and through `k=D+2` it is
divisible by 4. Therefore

\[
3y_k+1=2y_{k+1},\qquad v_2(3y_k+1)=1\quad(k\le D+2).
\]

The points `y_1=64N-1`, `y_2=96N-1`, and `y_3=144N-1` are in the last
two annular bands. Since `X=1 modulo 9`, their residues modulo 18 are
respectively `5,17,17`; the six-band table gives coefficients `-2,2,2`.
All later chain states are above the source support.

Every displayed arrow is in `G_D(N)`: the first three origins are sources,
and `y_k`, `3<=k<=D+2`, is at distance `k-3<=D-1` from the top source.
The terminal state `y_(D+3)` has no outgoing arrow in this graph. Any
source's state after at most `D-1` steps is bounded above by

\[
\left(\frac32\right)^{D-1}144N-1=y_{D+2}<y_{D+3}.
\]

It remains to exclude **every extra incoming exposed arrow**. This is the
main point of the proof.

### 3. Inverse histories and their value at X=1

Consider an admissible inverse history of length `l<=D` ending at a chain
point `y_k`. If its inverse valuations are `a_1,...,a_l>=1`, write
`A=a_1+...+a_l`. Every backward state has the exact form

\[
x=uX-c,\qquad u=3^{k-l}2^{A-k},\qquad c>0.
\]

An inverse step of valuation `a` acts by

\[
u' = \frac{2^a u}{3},\qquad
c' = \frac{2^a c+1}{3}.
\]

Define the auxiliary rational number

\[
z=u-c,
\]

which is what the affine state would equal at `X=1`. Its inverse update is

\[
z'=\frac{2^a z-1}{3}.
\]

These auxiliary numbers are used only to prove an arithmetic inequality.
They are not substituted for the actual positive odd Collatz states.

Each chain point is `-1 modulo 3`, so its direct inverse valuations are
odd. Valuation 1 leads to the preceding chain point. Every other inverse
branch begins with an odd valuation at least **3**. In the rest of this
section consider any history whose first inverse step is such an extra
branch. Its cumulative excess

\[
E=A-l=\sum_{i=1}^l(a_i-1)
\]

is at least 2 and cannot decrease.

#### Before the first integer auxiliary value

Initially `c=1`. While `A<k`, the auxiliary state is not an integer and
`l<k`. The coefficient `u=3^(k-l)/2^(k-A)` is divisible by 3 in rational
arithmetic with powers of 2 as denominators. The actual state is integral
because `X` supplies all these powers of 2. Consequently the admissibility
condition for the next inverse branch is exactly

\[
3\mid 2^a c+1.
\]

Thus `c` remains a positive odd integer up to and including the first
step for which `A>=k`. That step occurs by `l<=k`, if the inverse history
is long enough to reach it. At that first step the auxiliary value is
indeed integral.

All auxiliary values through this point are positive. To see this,
compare inverse maps with `f_1(z)=(2z-1)/3`. Starting from
`z=(3/2)^k-1`, applying `l` copies of `f_1` would give
`(3/2)^(k-l)-1>=0` for `l<=k`. The first extra valuation gives a strict
increase over this comparison, and subsequent inverse maps preserve the
strict inequality while the comparison values remain nonnegative.

Before integer arrival, put `s=k-A>0` and `r=k-l`. Then
`r-s=E>=2`, so

\[
u=\frac{3^r}{2^s}=3^E\left(\frac32\right)^s\ge9.
\]

Hence every such predecessor is already above the annulus; Section 5
makes this height comparison explicit.

#### At the first integer auxiliary value

Now put `r=k-l>=0` and `s=A-k>=0`. Since `r+s=E>=2`,

\[
u=3^r2^s\ge4.
\]

At this stage `u` is an integer, `c` is a positive odd integer, and
`z=u-c` is a positive integer. If `z` is odd and equals 5, the strict
inequality `u>z` gives `u>=6`. If `z` is even, then `u` is odd, so `s=0`
and `r>=2`; in this case `u>=9`.

### 4. A preserved inequality after integer arrival

The ternary congruence makes the auxiliary integers track all subsequent
inverse admissibility decisions. At a history length `l<=D`,

\[
x-z=u(X-1),\qquad u=3^{k-l}2^{A-k}.
\]

After integer arrival the only possible denominator of `u` is a power of
3, of exponent at most `max(l-k,0)`. Since `X-1` is divisible by
`3^(D+2)`, the difference `x-z` is an integer divisible by 3 throughout
the histories under consideration. An admissible inverse branch at the
actual state therefore also has `3|(2^a z-1)`. Its new auxiliary value is
a positive integer. After one such inverse step it is odd.

For positive odd auxiliary values preserve the three conditions

\[
c>0,\qquad u\ge4,\qquad z=5\ \Longrightarrow\ u\ge6.
\tag{*}
\]

They hold at an odd first integer arrival by the preceding section. If
the first integer auxiliary value is even, `u>=9`, so its next valid
inverse has odd auxiliary value and `u'=2^a u/3>=6`. This also establishes
all three conditions.

To prove preservation, first note that `c'=(2^a c+1)/3>0`, hence `u'>z'`.

- If `a>=2`, then `u'>=4u/3>=16/3>4`.
- If `a=1`, an admissible odd `z` must be `2 modulo 3`, hence `z=5` or
  `z>=11`. At `z=5`, condition (*) gives `u'=2u/3>=4`. At `z>=11`,
  `u>z` gives `u'>22/3>4`.
- If the **new** auxiliary value is 5, then `2^a z=16`. With `z` positive
  and odd, the only possibility is `z=1`, `a=4`. Thus
  `u'=16u/3>=64/3>6`, proving the extra condition at 5.

This proves (*) by induction. Every extra-branch ancestor, before or after
integer arrival, therefore has

\[
u\ge4,\qquad z>0.
\]

The special condition at auxiliary value 5 is necessary for this
inequality proof; simply assuming `u>=4` and `u>z` would not suffice.

### 5. Excluding every extra incoming exposed edge

For any of these extra-branch predecessors,

\[
x=uX-c=u(X-1)+z>4(X-1).
\]

For `X>=8`,

\[
4(X-1)>\frac{27}{8}X-1=144N-1.
\]

Our divisibility assumptions imply `X>=1024`. Thus **no predecessor on
an extra inverse branch of length at most D is an annular source**, since
all annular sources are at most `144N-1`.

An extra incoming arrow `p -> y_k` could belong to `G_D(N)` only if some
annular source reached `p` in at most `D-1` steps. Reversing that history
would give an excluded extra-branch inverse history of length at most D.
Therefore no such incoming arrow is present.

The valuation-one predecessor at the bottom is `X-1`. It is divisible by
3, so it has annular coefficient zero and has no positive odd Syracuse
predecessor. It is not an exposed origin. All other valuation-one
predecessors are precisely the preceding displayed chain points.

Together with the terminal height bound, these facts exhaust every
incident arrow of every chain point. The chain is the **complete**
historical component. Its mass 2 proves the theorem.

### 6. Verification and exact scope

The proof above covers arbitrary integer depths and all inverse
valuations; a finite scan is not used to establish those quantifiers.
The companion checker verifies its arithmetic constants and source
formulas, then compares the complete predicted component against the
independent bounded inverse oracle at selected CRT and required-ray
cutoffs. The CRT representatives keep the numerical checks manageable;
the required-ray existence proof remains symbolic at large depths.

```sh
python3 experiments/residual_progress/templates/check_unbounded_exposure.py
```

Its receipt states every finite input and cap. A cap is always unresolved,
never an obstruction. The original finite examples and fixed-depth
symbolic lift remain available as independent evidence and provenance.

The theorem closes the earlier question of whether a uniform exposure
depth can suffice for all actual annuli: **it cannot**. It leaves the
main construction problem open. A successful universal method must allow
unbounded historical exposure, or recursive identities whose total
source-to-anchor depth grows with the cutoff.

## Certificates

- [`check_unbounded_exposure.py`](check_unbounded_exposure.py) (under 1 s). Verifies the induction constants and the source formulas, checks the bounded inverse-history (shadow) words, compares the complete predicted component with the inverse oracle at CRT cutoffs for `D = 1, 2, 4, 8, 12, 16, 24, 32` and at the required-ray cutoffs for `D = 1..4`, and checks the modular ray condition `2^(2·3^(D+1)) ≡ 1 (mod 3^(D+2))` for `D` up to 128 without materialising the powers. It compares everything with `unbounded_exposure_audit.json`. The quantifier over all `D` comes from the written proof, not from these finite checks.
- [`check_symbolic_lift.py`](check_symbolic_lift.py) (about 1 s). The certificate of the fixed-depth lift [`depth-32-obstruction-infinite-family`](../depth-32-obstruction-infinite-family.md) (and, at `q = 1`, of the depth-32 component of [`depth-32-aggregate-exposure-obstruction`](../depth-32-aggregate-exposure-obstruction.md)); it lives here because it imports the oracle from this folder.
- Both pass at their new paths with their receipts unchanged. They use `assert`; run them without `-O`. The commands in the legacy text name `experiments/residual_progress/templates/`.

## Remarks

- **Answers [`uniform-aggregate-exposure-depth`](../../questions/uniform-aggregate-exposure-depth.md)** for annuli: no uniform exposure depth suffices for all actual annuli on the required rays. A successful universal method must allow unbounded historical exposure, or recursive identities whose total source-to-anchor depth grows with the cutoff.
- **Side-lane finite data (not part of the proof).** At the five brute-forced cutoffs the protected chain stops being an obstruction at depths 11, 21, 9, 10 and 51, in four cases still with positive mass at the moment it joins the component of 1 (feed entry 2026-10-17 19:03: "the protected chains end by reaching 1, not by cancellation"). For 13 cutoffs with `D ≤ 4`, `q2_end_depth.py` finds the end depth is set by the chain orbit's excursion above the source support `144N`, not by the climb length (feed entry 2026-10-18 10:25, the side lane's Q2). The main lane reproduced the `depth_probe` receipt (`../release-source-packing/side_lane_review.json`). Finite data, no general claim.
- Later results sharpen the picture: arbitrarily long isolation followed by explicit cancellation ([`delayed-release-cancellation`](../delayed-release-cancellation/README.md)), failure of the short bound `2h + 1` in most phases ([`short-delay-all-phase-obstruction`](../short-delay-all-phase-obstruction/README.md)), and unbounded depth with the ternary order fixed at 2 ([`fixed-ternary-order-unbounded-depth`](../fixed-ternary-order-unbounded-depth/README.md)). The whole-annulus depth `d*` is studied numerically in [`exposure-absorption-giant-component`](../../questions/exposure-absorption-giant-component/README.md).
- **Controls.** The obstruction is a positive component of one specific source family; it says nothing about `3x+1` cycles and is consistent with the `3x+d` controls.
- Novelty undetermined (none claimed).

## History

- Migrated from `experiments/residual_progress/templates/UNBOUNDED_EXPOSURE_DEPTH.md` (legacy ID R13; the ledger's R13 also covers [`depth-32-aggregate-exposure-obstruction`](../depth-32-aggregate-exposure-obstruction.md), alias R13-b, and [`depth-32-obstruction-infinite-family`](../depth-32-obstruction-infinite-family.md), alias R13-c) at commit `be73a66`, by the B09 migration (Claude, Opus 5.5). All eight script and receipt files of `templates/` moved here byte-identical, with the side-lane probes `depth_probe` and `q2_end_depth` from `reviews/side_lane/`. Legacy status: "written arbitrary-depth theorem, independently model-audited, with exact finite and symbolic checks. Complete current construction remains open".
- Main lane (ChatGPT, Codex), 2026-10-17, from commit `a7b7b47`. The legacy note says "two independent model audits found no gap"; they were run by the main lane's own agents and are not counted as independent. The side lane's finite brute-force check is recorded under `reviewed_by` with its scope.
