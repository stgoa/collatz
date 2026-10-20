---
id: signed-path-collapse-capacity
kind: result
title: The restricted graph E0 is a union of paths; signed collapse and intermediate capacity beat the shortcut normalizer, but naive alternation keeps mass N
status: written
claim: >
  Odd-only 3x+1 map, absorbing at 1. Let E0 contain the valuation-1 arrows and the valuation-2 arrows from
  sources = 2 mod 3. (Paths) Every vertex has in- and out-degree at most 1 in E0, no two consecutive arrows have
  valuation 2, every two backward steps contract by less than 8/9, so every E0 component is a directed path
  with a unique finite backward root (its forward path may be infinite). (Collapse) For finite integer
  sources, the linear signed collapse B gives mu = (I - P)J_B + B mu exactly, and the capacity normalizer gives
  mu = (I - P)J_cap + Z_cap with J_cap <= 0 and root residual max_j sum_(i<=j) a_i, the least possible among
  nonpositive E0 currents with nonpositive residual away from the root, and no larger than the residual of
  auxiliary-normalisation-remainder. (Alternation) Pushing normalized positive roots forward once and
  renormalizing stabilizes in finitely many rounds, but for every annulus A_N (8 | N) the fixed point keeps at
  least N positive mass. (Mersenne family) For N = 96 64^k, L = 12 + 6k, the states x_j = 3^j 2^(L-j) - 1
  form a complete E0 component of root mass 2 with sources (-2, +2, +2), carried across its first forbidden
  edge to w = (3^L - 1)/2^(2 + v2(L)) by an explicit current; for odd k, w = 1 mod 18 is a root and w/x_0 is
  unbounded, so this exit rule gives no decreasing-height recursion. Forward path termination is not proved.
authors:
  - ChatGPT main lane (Codex)
created: 2026-10-17
depends_on: [auxiliary-normalisation-remainder, disjoint-annular-recursion]
evidence:
  - "check_alternating_paths.py, alternating_paths_audit.json: the legacy constructors (ancestry, signed_path_collapse, capacity_normalize, frontier_collapse, naive_round, mersenne_component) and checker (every odd state through 4097 against the incoming-edge classification and old unit roots; 20 full annuli at N = 8..128 by 8 and 160, 168, 384, 768; all divergence identities, signs, idempotence and frontier aggregation; the exact N persistent trap atoms; finite alternation with a 32-round cap; the component family at k = 0..8, 32, 128). Fails at its new path: it loads experiments/residual_progress/auxiliary/check_auxiliary_normal_form.py relative to the repository root (now ../auxiliary-normalisation-remainder/, which itself no longer runs). Passed at be73a66 as experiments/residual_progress/alternating/check_alternating_paths.py inside scripts/verify_all.py (archive/legacy-checker-run-be73a66.md: the gate ran these steps before stopping at residual_progress/history_frontier, and passed in full at 9dbc71a). The legacy checker of bounded-source-cluster-local-bound loads it by its old path"
  - "../auxiliary-normalisation-remainder/batch_r15_r18_r21_r29_check.py: side-lane probe, a certificate of that node, which also checks the E0 arithmetic below (passes at its new path)"
reviewed_by:
  - by: Claude side lane (Opus)
    date: 2026-10-18
    link: ../auxiliary-normalisation-remainder/batch_r15_r18_r21_r29_check.py
    scope: "Finite arithmetic only (side-lane feed entry 2026-10-18 11:32, VERIFIED, main 9190ccf): on all odd y < 10^6, E0 in- and out-degree at most 1 (brute force below 3000), no two consecutive valuation-2 arrows, two-step backward contraction below 8/9, no incoming arrow exactly on 1, 3, 7, 9, 15 mod 18; the Mersenne family for k <= 12 (E0 path, exit valuation 3 + v2(L), exit w, and w = 1 mod 18 for odd k). Statements needing A_N were not checked. The status stays written"
aliases: [R18]
tags: [convergence, packet-currents, annular, path-graph, normal-form, partial-current, obstruction]
---

# The restricted graph E0 is a union of paths; signed collapse and intermediate capacity beat the shortcut normalizer, but naive alternation keeps mass N

## Statement

Odd-only Syracuse `S`, killed at 1, pushforward `P`; finite integer measures on odd states greater than 1; `A_N` the six-band annulus, `8 | N`. `E0` contains exactly the arrows of valuation 1 and the arrows of valuation 2 whose source is `2 (mod 3)`.

1. **Theorem 1 (paths).** In `E0` every vertex has at most one incoming arrow (`p(y) = (2y − 1)/3` if `y ≡ 2 (mod 3)`, `(4y − 1)/3` if `y ≡ 13 (mod 18)`) and one outgoing arrow; vertices without incoming arrow are exactly the inactive residues `{1, 3, 7, 9, 15} (mod 18)`. No two consecutive arrows have valuation 2, so `S²(x) > 9x/8`; every inverse chain terminates at a unique root within fewer than `12·bitlength(y) + 1` edges and stays below `4y/3`; `E0` has no cycles. Every component is a directed path with a unique finite backward root; its forward path may be infinite (no claim that it ends).
2. **Signed collapse.** `B μ = Σ μ(y) δ_(b(y))` (root `b`) with the finite path current `J_B` gives `μ = (I − P)J_B + B μ`; `J_B` may have positive rows. A finite current on `E0` arrows can leave a nonpositive residual iff every complete `E0` component has nonpositive total source mass.
3. **Intermediate capacity.** Processing positive arrivals edge by edge gives `μ = (I − P)J_cap + Z_cap(μ)` with `J_cap ≤ 0` and root coefficient `max_(0≤j≤m) Σ_(i≤j) a_i`, the least root residual among nonpositive `E0` currents with nonpositive residual away from the root; hence `‖Z_cap(μ)⁺‖₁ ≤ ‖Z(μ)⁺‖₁` for the normal form `Z` of [`auxiliary-normalisation-remainder`](../auxiliary-normalisation-remainder/README.md). The positive supports stay below `64N` for the annulus.
4. **Theorem 2 (naive alternation).** `T(z) = Z(z − z⁺ + P z⁺)` reaches a fixed point in finitely many rounds; at a fixed point positive atoms sit in the trap classes `{3, 7, 15, 19, 27} (mod 36)`. For every `8 | N`, the exactly `N` states `q ∈ (48N, 64N)` with `q ≡ 15 (mod 24)` or `27 (mod 48)` stay positive forever, so the fixed point keeps positive mass at least `N`.
5. **Frontier retention.** Aggregating a source segment at its furthest source gives `J_F`, `F μ` with `J_F − J_B = (Σ a_j)·Σ_(i<m) δ_(x_i)`; a next-edge constructor must retain the frontier.
6. **Mersenne component family.** For `N = 96·64^k`, `L = 12 + 6k`, `x_j = 3^j 2^(L−j) − 1` (`0 ≤ j < L`) is a complete `E0` component whose annular source is exactly `−2δ_(x_1) + 2δ_(x_2) + 2δ_(x_3)` (so `B A_N(q) = 2` at its root `q = 2^L − 1`); its first forbidden edge leads to `w = (3^L − 1)/2^(2 + v_2(L))`, and `μ_k = (I − P)(−2δ_(x_1) + 2Σ_(j=3)^(L−1) δ_(x_j)) + 2δ_w` (positive cost `2L − 6`). For odd `k`, `w ≡ 1 (mod 18)` is already a root and `w/q → ∞`.

These are partial constructions and scoped obstructions, not a complete annular constructor or a proof of Collatz; no novelty is claimed.

## Proof

The legacy note "Exact path collapse and why forward/backward alternation resets" follows, lightly edited (headings demoted one level, links pointed to nodes). Its commands name pre-migration paths; see Certificates.

Date: 2026-10-17. **Status: written elementary proofs and finite checks.**
These are partial constructions and scoped obstructions, not a complete
annular constructor or a proof of Collatz. No novelty is claimed.

Use odd Syracuse `S`, killed at1, and its pushforward `P`. Measures and
currents have finite integer support on odd states greater than1. The source
`A_N` is the six-band annulus, with `8|N`. The earlier normalizer `Z` and its
four active residues are defined in
[the auxiliary note](../auxiliary-normalisation-remainder/README.md).

### 1. A path graph behind the short backward substitutions

Define `E0` to contain precisely these Syracuse arrows `x -> S(x)`:

- exact valuation1;
- exact valuation2 with `x=2 modulo3`.

The unique incoming `E0` predecessor, when it exists, is

\[
p(y)=\begin{cases}
(2y-1)/3,&y\equiv2\pmod3,\\
(4y-1)/3,&y\equiv13\pmod{18}.
\end{cases}
\]

The cases are disjoint. In the first case the predecessor is `3 modulo4`,
so valuation1 is exact. For the second, the predecessor is `17 modulo24`,
so it has valuation2 and residue2 modulo3. Conversely, an allowed
valuation2 arrow must end at residue13 modulo18. Thus every vertex has
in-degree and out-degree at most one in `E0`. Its vertices with no incoming
arrow are exactly the inactive residues `{1,3,7,9,15}` modulo18.

There cannot be two consecutive valuation2 arrows in `E0`: any valuation2
arrow ends at residue1 modulo3, which is forbidden as the source of another
allowed valuation2 arrow. Consequently every two consecutive forward
arrows have total valuation at most3, and

\[
S^2(x)>9x/8.
\]

Equivalently, every two inverse `p` steps reduce the state by a factor
strictly below `8/9`. Twelve inverse steps more than halve it, since
`(8/9)^6<1/2`. Every inverse chain therefore terminates at a unique root,
and contains fewer than `12*bit_length(y)+1` edges when started at `y`.
Every vertex in that inverse chain is below `4y/3`: an inverse valuation2
step increases height by less than4/3, and the next inverse step brings it
below its preceding pair's start. In particular, `E0` has no cycles.

**Theorem 1.** Every `E0` component is a directed path with a unique finite
backward root. Its forward path may be finite or infinite. No assertion
that every forward path ends is made here; an infinite one would grow at
least geometrically every two steps and would be a divergent Syracuse orbit.

The old normalizer's unit-atom root is the same root. Its residue5/11 rule
uses one `p` edge, and its residue13/17 rules use two `p` edges. The two-edge
shortcut ignores any source coefficient at its intermediate vertex; this
is the information the following constructions retain.

### 2. A finite linear signed collapse, with exact current

Write `b(y)` for the root of `y` and define

\[
B\mu=\sum_y\mu(y)\delta_{b(y)}.
\]

For each source `c delta_y`, use its complete predecessor path
`q=x_0 -> ... -> x_m=y` and add current

\[
-c\sum_{i=0}^{m-1}\delta_{x_i}.
\]

Summing these finite paths gives an executable finite current `J_B` with

\[
\boxed{\mu=(I-P)J_B+B\mu.}
\]

The sign of `c` is retained. In particular, negative sources can create
positive current rows. The cost is not generally zero.

`B` is linear, idempotent, and `B(delta_x-delta_(Sx))=0` on every `E0`
arrow. To see every coefficient explicitly, take the finite ancestral
segment `x_0,...,x_m` containing a component's sources, inserting zero
coefficients as necessary, and put `a_i=mu(x_i)`. Then

\[
J_B(x_i)=-\sum_{j=i+1}^{m}a_j\quad(0\le i<m),\qquad
B\mu(x_0)=\sum_{j=0}^{m}a_j.
\]

**Corollary.** A finite current supported on `E0` arrows can leave an
everywhere nonpositive residual exactly when each complete `E0` component
has nonpositive total source mass. Necessity follows by summing the finite
divergence over that component; sufficiency is the construction above.
This applies even when the component's unexposed forward continuation is
infinite. It does not assert that the whole annulus satisfies this test.

### 3. Using intermediate negative capacity at zero positive-current cost

There is a second, nonlinear construction. Build the finite union of the
sources' complete ancestral paths. Process vertices in decreasing distance
from their roots. If a nonroot vertex has positive coefficient `c`, move it
back across its single incoming edge, adding `-c delta_(p(y))` to the
current. A negative coefficient first absorbs arriving positive mass.

This order is topological even though one inverse valuation2 step can
increase ordinary height. The finite ancestry bound in Section1 proves
termination, with no forward absorption search. The resulting current
`J_cap` is nonpositive and satisfies

\[
\mu=(I-P)J_{cap}+Z_{cap}(\mu).
\]

Every positive residual coefficient is at a root. On one path, set
`c_(m+1)=0` and, from `i=m` down to1, define

\[
c_i=\max(a_i+c_{i+1},0),\quad
J_{cap}(x_{i-1})=-c_i,\quad
Z_{cap}(x_i)=a_i+c_{i+1}-c_i.
\]

The root coefficient is

\[
\boxed{Z_{cap}(x_0)=a_0+c_1
=\max_{0\le j\le m}\sum_{i=0}^{j}a_i.}
\]

These recurrences prove uniqueness for the specified legal normalization,
independent of the order of processing available positive vertices.

They also give a restricted optimality statement. For *any* nonpositive
current on this path whose residual is nonpositive away from its root,
summing the divergence on a prefix gives

`sum_(i<=j) residual(x_i) = sum_(i<=j) a_i - J(x_j)`.

Since `J(x_j)<=0`, the root residual is at least every initial prefix sum.
The displayed construction attains that lower bound. Therefore the new
root coefficient is no larger than the root coefficient produced by the
old shortcut normalizer, component by component. In particular,

`positive_mass(Z_cap(mu)) <= positive_mass(Z(mu))`.

This improvement comes from intermediate capacities, not a termination
claim for the remaining positive roots. For example, if `u -> q` is an
allowed valuation2 arrow and the source is `2 delta_q-2 delta_u`, the new
normalizer gives exactly the current `-2 delta_u` and zero residual. The
older two-edge rule at q skipped u. The actual annular pair with
`36N<q<54N`, `q=31 modulo54`, `u=(4q-1)/3`, is one such example; its
packing and disjointness are treated in the separate release-packing note.
The smallest illustrative source used in the checker is
`2 delta13-2 delta17`: the new residual is zero with current `-2 delta17`,
whereas the old shortcut leaves `2 delta7-2 delta17`.

Also, each signed-collapse root coefficient is the total sum and hence at
most the maximum prefix sum. Therefore the positive supports of both new
residuals are contained in the positive support of the old normal form.
For the annulus they remain below64N. This inherits the old height bound;
it is not an improvement on the programme's absorption cutoff.

### 4. Why naive forward/backward alternation stops with positive mass

For a normalized source `z=Z(z)`, define one round by moving only its
positive part forward and then normalizing again:

\[
T(z)=Z\bigl(z-z^++Pz^+\bigr).
\]

For an inactive unit atom at x there are two cases.

- If `x=1 modulo4`, then `S(x)<x` or it is absorbed at1. Every subsequent
  backward endpoint is smaller still.
- If `x=3 modulo4`, then `S(x)=(3x+1)/2`. An inactive x is0 or1 modulo3,
  so this successor is5 or11 modulo18. Its first backward rule returns
  **exactly to x**. The fixed root classes are `{3,7,15,19,27}` modulo36.

Existing negative capacity at the successor may cancel positive flow
before it returns. Otherwise the forward current and its backward current
cancel row for row. No negative coefficient is ever newly created by a
round: an existing negative coefficient can only increase toward zero.

**Theorem 2.** Iterating T on any finite normalized integer source reaches
a fixed point in finitely many rounds. At that fixed point all positive
atoms are in the five trap classes above and every successor of a positive
atom has zero coefficient. The fixed point can have positive mass.

**Proof.** Label positive units before a round. During normalization,
arrivals are positive and can only be canceled by existing negative
capacity. A surviving unit from a trap returns to that same root; a unit
from another inactive state ends strictly below its starting point. Thus
the nonnegative integer `Phi(z)=sum_x x*z^+(x)` decreases strictly whenever
any unit is canceled, absorbed, or descends. If none does, every positive
unit returns to its own root and all coefficients are unchanged. Hence
every nonfixed round strictly decreases Phi. The stated fixed-point
description follows from the two cases. Conversely, that description
forces all units to return and gives zero accumulated round current.
This proves finite stabilization, not absorption. □

#### A universal positive obstruction on the actual annulus

For `8|N`, take all q in `(48N,64N)` satisfying either

`q=15 modulo24` or `q=27 modulo48`.

These classes are disjoint. The exact first-pass profile in the auxiliary
note puts at least2 positive units at each such q. They are multiples of3,
so the old backward normalization leaves `Z(A_N)(q)>=2`. They are also
`3 modulo4`. Their successors r lie in `(72N,96N)` and are5 modulo18.
The original coefficient there is exactly−1. Every positive backward
arrival from the annulus lies below64N, so `Z(A_N)(r)=-1` exactly.

In the first round, q sends at least2 units to r, spending its sole
negative unit and returning at least1 to q. Future rounds cannot create
new negative capacity at r; q therefore stays positive forever.

There are **exactly N** such q. For `N=8,16,24`, the two counts are
`(5,3)`, `(11,5)`, `(16,8)`. Increasing N by24 increases them by `(16,8)`:
both interval endpoints shift by multiples of48. These three phases cover
all multiples of8. Consequently the final fixed point of naive alternation
has positive mass at least N, for every annulus in this domain.

This obstruction concerns the specified repeated normalization. It does
not prohibit a retained-history construction, signed current cancellation,
or transporting the unresolved mass beyond the immediately undone edge.

### 5. Retain the exposed frontier, not just the root total

The same finite source segment `x_0,...,x_m` can instead be aggregated at
its *furthest supplied source*, retaining this path and the frontier x_m.
The exact current and residual are

\[
J_F(x_i)=\sum_{j=0}^{i}a_j\quad(0\le i<m),\qquad
F\mu=\left(\sum_{j=0}^{m}a_j\right)\delta_{x_m}.
\]

The two current tables differ by the component total times the path:
`J_F-J_B = (sum a_j) sum_(i<m) delta_(x_i)`. Thus the frontier can be
changed without forgetting any signed coefficient or previously exposed
arrow. The implementation returns both the exact current and records
`(root, frontier, complete path, mass)`.

If only Bmu is retained, pushing a root across an allowed edge and applying
B returns it to the same root. A next-edge constructor must therefore
retain its exposed frontier or equivalent history. It can explore beyond
that frontier and cross a forbidden E0 edge when one is reached. No proof
here guarantees that every positive component reaches such an exit, or
that the exit joins enough negative source mass.

### 6. An explicit growing-depth component current, without height descent

For every integer `k>=0`, set

\[
N=96\,64^k,\qquad L=12+6k,\qquad
x_j=3^j2^{L-j}-1\quad(0\le j<L).
\]

The root `q=x_0=2^L-1` is divisible by3 because L is even. For `j<L-1`,
the edge `x_j -> x_(j+1)` has exact valuation1. At the last vertex,

\[
v_2(3x_{L-1}+1)=1+v_2(3^L-1)=3+v_2(L)\ge4.
\]

For completeness, writing `L=2^s m`, m odd, gives
`v2(3^L-1)=v2(3^(2^s)-1)`. The s=1 value is3, and each further squaring
adds1 because `3^(2^s)=1 modulo8`. Hence it equals `s+2`.

The entire E0 component is exactly `x_0,...,x_(L-1)`: q has no predecessor,
every intermediate vertex has its unique displayed incoming and outgoing
edge, and the last edge is forbidden. Its next Syracuse state is

\[
w=\frac{3^L-1}{2^{2+v_2(L)}}.
\]

The complete annular source on this component is

\[
\mu_k=-2\delta_{x_1}+2\delta_{x_2}+2\delta_{x_3}.
\]

Indeed, `x_1=64N-1`, `x_2=96N-1`, `x_3=144N-1`; the coefficient table
gives `(−2,+2,+2)`. The root is divisible by3 and has zero coefficient,
and every later vertex exceeds144N. Consequently `B A_N(q)=2` exactly,
not just for a selected submeasure. This supplies positive complete E0
components on every member of this annular ladder.

An explicit current carries that full component mass across its first
forbidden edge:

\[
\boxed{\mu_k=(I-P)\left(-2\delta_{x_1}
+2\sum_{j=3}^{L-1}\delta_{x_j}\right)+2\delta_w.}
\]

Its positive current cost is `2L-6`; the x_0 and x_2 rows cancel exactly.
This is a family with unbounded, explicitly known depth. It uses no
assumption about the future of w and gives a reusable partial current.

It does not close a decreasing-height recursion. For odd k, `v2(L)=1`,
so `w=(3^L-1)/8=1 modulo18` is already an inactive root. Moreover

\[
\frac{w}{q}=\frac{3^L-1}{8(2^L-1)}\longrightarrow\infty
\]

along those odd k. Thus even a complete explicit E0 component exit can
increase the next root height by an unbounded factor. A successful
recursion needs another decreasing parameter or a proved cancellation
mechanism across these path components.

### 7. Executable interface, checks, and limits

`check_alternating_paths.py` provides:

- `ancestry(y)`: complete inverse E0 path with a proved logarithmic cap;
- `signed_path_collapse(mu)`: full finite current, Bmu, statistics;
- `capacity_normalize(mu)`: full nonpositive current and exact residual;
- `frontier_collapse(mu)`: full current, frontier residual, retained paths;
- `naive_round(z)`: one exact positive-forward/old-normalize round;
- `mersenne_component(k)`: the explicit full-component source, current,
  residual and parameters from Section6.

Run without Python optimization:

```sh
python3 experiments/residual_progress/alternating/check_alternating_paths.py
```

The receipt verifies every odd state through4097 against the incoming-edge
classification and old unit roots; 20 full annuli at `N=8..128` by8 and
`160,168,384,768`; all divergence identities, capacity/current signs,
idempotence and retained-frontier aggregation; the exact N persistent
trap atoms; and finite alternation with a32-round cap. It also checks the
explicit component family at `k=0..8,32,128`, using pointwise annular
coefficients without materializing those enormous annuli.

At N96, the old normalizer leaves positive mass1859, the capacity-aware
normalizer1414, and signed collapse1337. These are finite examples, not
uniform contraction constants. Every returned positive remainder is
retained. Neither the inverse-path termination proof nor the exact
growing-depth component formula supplies universal annular certificates.

## Certificates

No certificate runs in this folder: the legacy checker loads [`auxiliary-normalisation-remainder`](../auxiliary-normalisation-remainder/README.md)'s checker by its pre-migration path and is evidence only. The finite `E0` arithmetic (degrees, contraction, inactive roots, the Mersenne exits for `k ≤ 12`) is certified for odd `y < 10⁶` by the side-lane script [`batch_r15_r18_r21_r29_check.py`](../auxiliary-normalisation-remainder/batch_r15_r18_r21_r29_check.py), a certificate of that node. The command in the legacy text names `experiments/residual_progress/alternating/`. At `N = 96` the legacy receipt records positive mass 1859 (shortcut normalizer), 1414 (capacity) and 1337 (signed collapse); these are finite examples, not contraction constants.

## Remarks

- An infinite forward `E0` path would grow at least geometrically every two steps and would be a divergent Syracuse orbit; nothing here excludes it.
- The bounded source span of complete `E0` clusters and the behaviour at forbidden exits are in [`bounded-source-cluster-local-bound`](../bounded-source-cluster-local-bound/README.md). The pair of [`release-source-packing`](../release-source-packing/README.md) is an annular instance of item 3.
- The next construction must retain the exposed frontier and use additional cancellation or a different decreasing parameter ([`annular-component-progress-lemma`](../../questions/annular-component-progress-lemma.md)).

## History

- Migrated from `experiments/residual_progress/alternating/ALTERNATING_PATHS.md` (legacy ID R18) at commit `be73a66`, by the B09 migration (Claude, Opus 5.5). Note, checker and receipt moved byte-identical. Legacy status: "written finite constructors, a restricted optimality theorem, and scoped obstructions. Forward path termination remains unproved in general".
- Main lane (ChatGPT, Codex), 2026-10-17, from commit `2be37b7`. Its "independent model reviews" of the signed path arguments were the main lane's own agents; an integration review caught a missing `0 ≤ i < m` restriction on the frontier-current formula, now explicit. The side lane's finite check is recorded under `reviewed_by`.
