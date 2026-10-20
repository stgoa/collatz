---
id: supplied-path-saturation-core
kind: result
title: Supplied absorption paths through N saturate to an infinite target set whose first Syracuse image is a finite closed graph of 2|Q_N| states
status: written
claim: >
  Odd-only 3x+1 map, absorbing at 1; nu, B, T(q) = nu(S(q)) of elementary-bridge-quotient-normal-form. (Closure) For
  any seed set A, the smallest set closed under the elementary identities (F, selected halving, their inverses) and
  forward S arrows is nu^(-1)(Q(A)), Q(A) = union of the T-orbits of nu(A). Given a supplied finite exact current H
  with div H = U_N (signs allowed), Q_N = nu(Y_N) = union over canonical q <= N of {T^j(q)} is finite, contains 1, is
  T-closed and absorbed, and E_N = nu^(-1)(Q_N) is that closure; least origins m(z) give every smaller-cutoff table
  (least for the specified operations, not among all possible proofs). (Core) For every finite nonempty T-closed
  canonical Q, W_Q = {S(q), 3q+2 : q in Q} satisfies S(nu^(-1)(Q)) = W_Q, S(W_Q) in W_Q, |W_Q| = 2|Q|,
  max W_Q = 3 max Q + 2; so every requested x with nu(x) in Q has an absorption current of at most 2|Q| ordinary
  arrows, and any checked finite bridge into nu^(-1)(Q) (e.g. a complementary-run-bridges return with
  nu(f(x)) in Q_N, a strictly more inclusive test than nu(f(x)) <= N) compiles to an exact current. Finite examples:
  at N = 384 both units of the weight-2 root 415 are certified (complementary mass removed 11 of 17 against 9), but
  these extra roots were already on supplied history. (Counts) For finite canonical Q with maximum M and X >= M,
  |#{odd x in [X, 2X) : nu(x) in Q} - |Q|| <= floor(log2 M) + 1 (weighted version with factor max |w|), with
  persistent oscillation for Q = {1}. Saturation gives no universal target-entry theorem: a seed reaches E_N iff it
  reaches 1.
authors:
  - ChatGPT main lane (Codex)
created: 2026-10-17
depends_on: [elementary-bridge-quotient-normal-form, complementary-run-bridges, absorbed-fibre-uniform-counts]
certificates: [check_saturation_recompute.py, check_legacy_replay.py]
evidence:
  - "check_saturation.py, saturation.py, saturation_audit.json, root415_current.json: the legacy constructor (saturated quotient, least origins, finite core compiler, certify_via_bridge, high-band counts) and checker (nine supplied cutoffs 8 to 768, nested tables, 20 high bands through multipliers 2^512, four signed sparse counting cases, 224 arbitrary-height member currents, the two oscillation families, all additional R26 certificates including both units at 415; input discovery capped at 1000 steps per seed). Fails at its new path: saturation.py loads ../bridge_normal_form/normal_form.py (now ../elementary-bridge-quotient-normal-form/) and check_saturation.py loads ../complementary_bridge/run_bridge.py (now ../complementary-run-bridges/) by their pre-migration paths. Passed at be73a66 as experiments/residual_progress/known_saturation/check_saturation.py inside scripts/verify_all.py (archive/legacy-checker-run-be73a66.md: the gate ran these steps before stopping at residual_progress/history_frontier, and passed in full at 9dbc71a). The later legacy experiments/residual_progress/inverse_scope/ loads saturation.py by its old path. Now replayed unmodified, with every file unchanged, by check_legacy_replay.py (B18-replay-revival migration)"
reviewed_by:
  - by: Claude side lane (Opus)
    date: 2026-10-18
    link: ../auxiliary-normalisation-remainder/batch_r15_r18_r21_r29_check.py
    scope: "Finite only (side-lane feed entry 2026-10-18 11:32, VERIFIED, main 9190ccf; the R29 part of a probe that also checks R15, R18 and R21): with the lane's own S and nu, the T-closure Q of all canonical states below 3000 (1,269 states, maximum 252,233) has |W_Q| = 2|Q|, max W_Q = 3 max Q + 2 and S(W_Q) in W_Q; every odd x < 2 10^6 with nu(x) in Q has S(x) in W_Q (12,866 such x) and every element of W_Q is attained; sampled x reach 1 within 1 + 2|Q| arrows; S(x) <= 3 nu(x) + 2 for all odd x < 2 10^6; S^4(327) = 415 and S^9(327) = 1579. The written closure, origin and counting proofs were not re-derived; the status stays written"
aliases: [R29]
tags: [convergence, outer-residual, saturation, known-set, finite-core, conditional, counting]
---

# Supplied absorption paths through N saturate to an infinite target set whose first Syracuse image is a finite closed graph of 2|Q_N| states

## Statement

Odd-only clock, absorbing at 1; `ν`, `B`, `C_q` and `T(q) = ν(S(q))` from [`elementary-bridge-quotient-normal-form`](../elementary-bridge-quotient-normal-form/README.md).

1. **Exact closure.** For any seed set `A`, the smallest set closed under `F`, the selected halving relation, their inverses and forward `S` arrows is `E(A) = ν^(−1)(Q(A))`, `Q(A) = ⋃_(a ∈ A, j ≥ 0) {T^j(ν(a))}`. With a supplied finite exact current `H`, `div H = U_N` (signs allowed), `Q_N = ν(Y_N) = ⋃_(q ∈ B, q ≤ N, j ≥ 0) {T^j(q)}` is finite, contains 1, is `T`-closed and absorbed, and is intrinsic to the cutoff. Adding new incoming arrows or new bridges is a different inference.
2. **Least origins.** `m(z) = min{q ∈ B : T^j(q) = z}` is determined exactly on `Q_N`; `z ∈ Q_N ⇔ m(z) ≤ N`, `m(T(z)) ≤ m(z)`, and `Q_n = {z ∈ Q_N : m(z) ≤ n}` for `n ≤ N`. These are least cutoffs for the specified operations, not among all possible proofs (`113 ∉ Q_8` although `T(113) = 1`).
3. **Finite core.** For finite nonempty `T`-closed canonical `Q`, `W_Q = {S(q), 3q + 2 : q ∈ Q}` has `S(ν^(−1)(Q)) = W_Q`, `S(W_Q) ⊆ W_Q`, `|W_Q| = 2|Q|`, `max W_Q = 3·max Q + 2`; absorption of `Q` under `T` and of `W_Q` under `S` are equivalent. Every `x` with `ν(x) ∈ Q` has an absorption current of at most `2|Q|` arrows, and any checked finite bridge `div J = δ_x − δ_z` with `ν(z) ∈ Q` compiles to an exact nonnegative current.
4. **Finite examples.** At `N = 384` the weight-2 root 415 has normalised return 1579 `> N` but `m(1579) = 327`, `S^9(327) = 1579`, so both units are certified (48-row current stored); the complementary mass removed rises from 9 to 11 of 17. At `N = 96` root 111 joins via 283. These extra roots already lie on supplied history; they show reuse, not a new merger mechanism, and no coverage proportion is claimed.
5. **High-band counts.** For finite canonical `Q` with maximum `M` and integer `X ≥ M`, `|#{odd x ∈ [X, 2X) : ν(x) ∈ Q} − |Q|| ≤ ⌊log₂ M⌋ + 1`, and with integer weights the error is at most `(⌊log₂ M⌋ + 1)·max|w|`. For `Q = {1}` the count oscillates (`0` at `6·4^k`, `2` at `3·4^k`).
6. **Limits.** A seed reaches `E_N` iff it reaches 1, so saturation is no universal target-entry theorem. For odd `a ≥ 3` and `q = 2^a − 1 = N`, `Q_N` contains `2·3^(a−1) − 1`, so its height relative to `N` is unbounded.

No novelty, formal verification or human review is claimed.

## Proof

The legacy note "Saturating supplied paths: an infinite set with a finite ordinary graph" follows, lightly edited (headings demoted one level, links pointed to nodes). Its commands name pre-migration paths; see Certificates.

**Status: written characterization and finite graph construction, with bounded
certificates.** A finite exact absorption current through N is supplied.
The resulting target set is exactly closed under the stated elementary
identities and forward Syracuse arrows. Universal entry into this set remains
open. No novelty, formal verification, or human review is claimed.

Use the odd-only Syracuse map S, with absorption at1. Measures and current
rows at1 are killed. The inputs are the [R25 normal form](../elementary-bridge-quotient-normal-form/README.md),
its identity `T nu=nu S`, and the [R27 fibre construction](../absorbed-fibre-uniform-counts/README.md).
The external side-lane feed is not a premise of these results.

### 1. The exact closure under the specified operations

Let B be the canonical minima from R25. For q in B,

```
C_q={F^k(q),F^k(2q+1): k>=0},      F(x)=4x+1,
nu(x)=q exactly when x belongs to C_q,
T(q)=nu(S(q)).
```

The elementary operations are F and its inverse when available, together
with the selected R23 halving relation and its inverse. All of them preserve
nu. Add the operation of taking a forward Syracuse successor.

For any initial set A of positive odd seeds, the smallest set closed under
these operations is exactly

```
E(A)=nu^(-1)(Q(A)),
Q(A)=union_(a in A, j>=0) {T^j(nu(a))}.                 (1)
```

This is an algebraic statement even if Q(A) is infinite. To prove it, the
right side contains A and is closed under the elementary operations. It is
closed under S because `nu(S(x))=T(nu(x))`. Conversely nu(a) is reachable
from a by elementary normalization. From a canonical q, the operations S
followed by nu generate T(q); the inverse elementary identities then
generate every member of C_q. Thus every point on the right is generated.

Let `A_N={odd a:1<=a<=N}`. Suppose a finite exact integer current H with
`div H=U_N` is supplied, where U_N has weight1 at every odd3<=a<=N.
H may be signed. Its nonzero-row graph contains the complete absorbing path
from each a in A_N by the finite component argument. Write Y_N for the
union of these actual paths, including1. Then

```
Q_N=nu(Y_N)
   =union_(q in B, q<=N, j>=0) {T^j(q)},
E_N=nu^(-1)(Q_N).                                     (2)
```

In particular Q_N is finite, contains1, is T-forward-closed, and all its
vertices reach1. Initial noncanonical seeds add no further canonical starts:
their minima are at most the seed and already occur among the canonical
inputs through N.

This quotient is intrinsic to the supplied source cutoff, not to a choice
of exact comparison current: the actual Syracuse path of a seed is unique,
and every valid H must contain that path. Extra rows are not automatically
known absorption. The implementation uses only rows reached from the
positive input seeds, so unrelated zero-source components cannot enlarge
Q_N.

Once Q_N is constructed, repeating elementary rewrites and forward exposure
from E_N gives no further points. This closure result applies to the named
operations. Adding a new incoming Syracuse arrow or a new arithmetic bridge
can enlarge the set and is a different inference.

### 2. An exact minimum origin for every known canonical target

For any canonical z define

```
m(z)=min{q in B: T^j(q)=z for some finite j>=0}.        (3)
```

The set is nonempty because q=z is allowed. Thus this minimum is defined
without assuming convergence. For every z in Q_N, the supplied paths through
N determine m(z) exactly. They enumerate all canonical starts q<=N and all
their finite paths; at least one such start reaches z. Any start smaller
than the recorded minimum is also at most N and has already been checked.
A start above N cannot improve that minimum.

Consequently

```
z in Q_N  iff  m(z)<=N,
m(T(z))<=m(z),
Q_n={z in Q_N:m(z)<=n},       1<=n<=N.                 (4)
```

The first equivalence refers to the intrinsic definition in (2). The last
formula is a reusable finite interface: one supplied current through N
provides the saturated quotients for every smaller input cutoff. Each label
is accompanied by a witness `(origin, step, state)` satisfying

```
state=S^step(origin),       nu(state)=z.
```

These are exact least input cutoffs for the operation set in Section1.
They are not least cutoffs among every possible independent current proof.
For example Q_8 is `{1,7,11,17}`. The canonical seed113 is outside Q_8,
although `T(113)=nu(85)=1`; a single incoming quotient arrow certifies113
by an additional rule. This prevents interpreting (2) as all mathematically
certifiable seeds from an already known1.

### 3. The entire infinite set enters a finite ordinary-S graph in one arrow

There is a stronger construction than an abstract quotient table. For any
nonempty finite canonical set Q with T(Q) contained in Q, define

```
E_Q=nu^(-1)(Q),
W_Q={S(q),3q+2:q in Q}.                               (5)
```

Then

```
S(E_Q)=W_Q,
S(W_Q) is contained in W_Q,
|W_Q|=2|Q|,
max W_Q=3 max Q+2.                                    (6)
```

**Proof.** The two F-rays in C_q have the constant respective successors
S(q) and `S(2q+1)=3q+2`. This proves the first equality, including q=1
under the absorbed convention. Each such successor has normal form T(q),
which belongs to Q. Thus W_Q is contained in E_Q, and its successors again
belong to W_Q.

The 2|Q| bases q and2q+1 are distinct F-roots. Distinct F-roots have distinct
S successors: equality would make them one-step siblings, which lie on the
same F-ray. Hence all states listed in (5) are distinct. Finally every S(q)
is at most3q+2, and3 max Q+2 is itself listed. This proves (6).

The pointwise bound `S(x)<=3nu(x)+2`, independently identified in the
coordinated merger-scope audit, is the single-state version of this exact
finite-image theorem. High elementary representatives return immediately
to a bounded region; their height alone does not measure unknown future
exposure.

If every q in Q reaches1 under T, then every w in W_Q reaches1 under S.
Indeed (R25) `T^j(nu(w))=1` implies `S^(j+2)(w)=1`. Conversely, absorption
of W_Q absorbs Q after one arrow and therefore absorbs the quotient.
So the two finite graph conditions are equivalent. No general exclusion of
Collatz cycles is assumed: the compiler verifies that its finite quotient
table is closed and reaches1.

For a supplied Q_N, this produces an ordinary directed graph with exactly
2|Q_N| vertices. It need not be a subgraph of the original supplied paths.
At N=8,

```
Q_8={1,7,11,17},
W_Q={1,5,11,13,17,23,35,53}.
```

States23,35,53 are absent from the original forward union through8. Their
edges are nevertheless explicitly given by (5), and all their successors
remain inside the finite compiled graph.

### 4. A direct certificate compiler and a bridge interface

The finite compiler checks every T edge in Q and a finite depth ranking to1.
It constructs W_Q from (5), computes its one-step S table, checks closure,
and records exact depths to1. It never searches outside that finite table.

For any requested x with nu(x) in Q, its first successor lies in W_Q.
Append the stored absorbing path inside W_Q. This directly returns a
nonnegative integral current with divergence delta_x. With source weight c,
multiply every row by c. The path uses at most

```
2|Q| ordinary Syracuse arrows.                         (7)
```

There are at most2|Q|-1 arrows from a vertex of W_Q to1, plus the initial
arrow if needed. Thus an infinite family has a finite graph interface and
a uniform current-size bound once Q is supplied. The graph size and largest
canonical base may depend arbitrarily on the input cutoff.

More generally, suppose an independent arithmetic construction returns a
finite exact bridge J with

```
div J=delta_x-delta_z,       nu(z) in Q.               (8)
```

The compiled current for z, added to J, has divergence delta_x. Preserve all
signed rows in this sum; the finite component argument extracts a nonnegative
absorbing current from their graph. This is `certify_via_bridge`. It accepts
R26 run-block bridges or any other checked finite bridge and retains source
multiplicity throughout. There is no assumption that z or the bridge's
intermediate heights are below N.

For an R26 return, replace the test `nu(f(x))<=N` by the strictly more
inclusive finite membership test `nu(f(x)) in Q_N`. This does not introduce
a higher absorption assumption: Q_N and its core were compiled solely from
the supplied lower current.

**Stored weight2 example.** At N=384 the actual remaining root415 has
coefficient2. Its normalized R26 return is1579, above N. But

```
m(1579)=327<=384,       S^9(327)=1579.
```

Therefore (8) certifies both units at415. The complete48-row current is in
`root415_current.json`, with its exact witness and hash. For this cutoff the
R23 complementary mass is17; the original normalized rule removes9 units,
and the saturated-target rule removes11. At N=96 the additional root111
connects to canonical283 with minimum origin27. These are finite examples,
not universal coverage proportions or an asymptotic estimate.

These particular extra roots are already represented by the supplied
history: `415=S^4(327)` lies in Y_384, while
`111=nu(S^17(27))=nu(445)` lies in E_96. The same is true of every extra
root in the recorded cutoff sample. Thus these examples check exact reuse
of known history and the bridge interface, including weight2; they do not
demonstrate a new merger beyond E_N. For these roots the direct member
compiler already suffices.

### 5. Exact high-band counts for arbitrary finite base sets

No forward-closure assumption is needed for this counting theorem. Let Q be
any nonempty finite set of canonical bases, let M=max Q, and let X>=M be an
integer. Define

```
B_Q(X)=#{odd x in [X,2X):nu(x) in Q}.
```

Then

```
|B_Q(X)-|Q|| <= floor(log2 M)+1.                       (9)
```

This is the R27 telescope applied to an arbitrary canonical counting
function instead of a complete canonical prefix. For completeness set

```
K_Q(t)=#{q in Q:q<=t},
f_s(q)=2^s q+beta_s,
beta_s=(2^s-1)/3              for even s,
beta_s=(2^(s+1)-1)/3          for odd s,
A_s(t)=K_Q((t-1-beta_s)/2^s).
```

The disjoint component classification gives

```
B_Q(X)=|Q|+sum_(s>=1)[A_s(2X)-A_(s-1)(X)].           (10)
```

Each difference has arguments separated by at most1/2, and hence has
magnitude at most1. A nonzero difference requires
`2X/(M+1)<2^s<2X`. There are at most floor(log2 M)+1 such levels, proving
(9). This is uniform in the height X and uses no distribution assumption
on the sparse set Q.

For finite integer weights w(q), retain weight w(q) at every member of C_q.
Exactly the same telescope proves

```
|B_w(X)-sum_q w(q)|
    <= (floor(log2 M)+1)*max_q |w(q)|.                 (11)
```

Signed weights and their multiplicities are retained in both the exact
formula and the error bound. The implementation uses prefix sums over the
sorted finite Q and inspects only O(log M) potentially relevant levels;
bit complexity still depends on X.

For fixed sparse Q, (9) does not assert that B_Q(X) converges as X grows.
The simplest absorbing set Q={1} gives the exact persistent oscillation

```
B_{1}(6*4^k)=0,       B_{1}(3*4^k)=2,       k>=0.     (12)
```

The two F-rays verify this directly. Thus the additive error matters; a
relative leading law requires a further relation between |Q| and log M.
For Q_N, |Q_N| and M_N are computable from the supplied finite graph, but
no universal asymptotic relation between them and N is supplied here.

### 6. What the saturation does and does not advance

The construction completely reuses already supplied forward history and its
elementary identities. Its output is finite and independently checkable,
despite representing infinitely many target integers. Returning to an
already represented class gives a certificate immediately; the finite
examples in Section4 show this can improve a prescribed arithmetic rule.

The explicit prefixes prevent imposing a linear height bound on this family
of supplied-input instances. For odd a>=3, the canonical input q=2^a-1 has the explicit
initial quotient prefix

```
T^j(q)=3^j*2^(a-j)-1,        0<=j<=a-1.
```

If an absorption current through N=q is supplied, Q_N necessarily contains
the last state2*3^(a-1)-1. The ratio of that height to N is unbounded with a.
This statement uses the explicit finite prefix and is conditional only as
to finiteness of the supplied full quotient. It assumes no unproved
absorption of those inputs in order to build their prefixes.

Saturation alone provides no new universal target-entry theorem. Since E_N
contains1 and every member is absorbed, an arbitrary seed reaches E_N if
and only if it reaches1. A successful independent bounded bridge into E_N
is useful constructive information; the equivalence does not establish
such a bridge for every remaining root.

Also, allowing arbitrary incoming Syracuse arrows would change the operation
set in Section1. Repeated inverse exposure can enlarge Q_N, as the113
example already shows. Unbounded inverse/common-tail closure is not the
finite elementary-plus-forward closure characterized here. Any proposed
completion rule still needs a finite progress argument, not just a larger
known target table or its spatial count.

### 7. Reproduction

```
python3 experiments/residual_progress/known_saturation/check_saturation.py
```

The default runner is read-only and compares `saturation_audit.json` and
`root415_current.json`. `--write-receipt` regenerates both. It checks nine
supplied cutoffs8,16,24,32,64,96,168,384,768; exact least-origin labels and
all nested smaller-cutoff tables;20 high bands through multipliers2^512;
four signed sparse counting cases;224 arbitrary-height member currents;
the two persistent oscillation families; and all additional R26 certificates
at those cutoffs, including both units at415.

Finite demonstration input discovery has a1000-step cap per seed. Every
construction after that stage follows only supplied finite rows, a verified
finite graph, or a fixed arithmetic bridge. The theorem takes the lower
current as an input and claims no universal discovery algorithm.

## Certificates

- [`check_saturation_recompute.py`](check_saturation_recompute.py) (written at the B10 migration, under 1 s, standard library). With its own `S`, `ν` and `T` it rebuilds, for the nine supplied cutoffs `N = 8, …, 768` (input paths with the legacy 1000-step cap), and compares with [`saturation_audit.json`](saturation_audit.json): `Q_N` with size, maximum, hash and least-origin witnesses; `T`-closure, monotone origins and the nested smaller tables; the finite core `W_Q` (size, closure, maximum, states off the supplied paths, largest depth); the R26 extension masses with the extra roots and their witnesses; the 20 high-band counts; and the stored weight-2 current [`root415_current.json`](root415_current.json) (divergence `2δ_415`, actual path, `S⁴(327) = 415`, `S⁹(327) = 1579`). It does not rebuild the 224 member currents, the signed sparse bands or the oscillation families (legacy checker, evidence only).
- The command in the legacy text names `experiments/residual_progress/known_saturation/`.

[`check_legacy_replay.py`](check_legacy_replay.py) (written at the B18-replay-revival migration; standard library) replays the unmodified legacy check `check_saturation.py` in a temporary copy of the legacy layout built by `tools/legacy_replay.py`, requiring exit 0 and every file unchanged (about 15 s). It checks finite steps only; the status is unchanged.

## Remarks

- The pointwise bound `S(x) ≤ 3ν(x) + 2` is the single-state form of item 3; it is also proved in [`merger-catalogue-scope`](../merger-catalogue-scope/README.md).
- Arbitrary common-tail comparisons with known seeds give exactly the basin of 1 ([`merger-catalogue-scope`](../merger-catalogue-scope/README.md)); this node characterises only the elementary-plus-forward closure. Inverse ancestry beyond it is [`decreasing-inverse-ancestry`](../decreasing-inverse-ancestry/README.md).
- No novelty is claimed.

## History

- Migrated from `experiments/residual_progress/known_saturation/KNOWN_SATURATION.md` (legacy ID R29) at commit `be73a66`, by the B10 migration (Claude, Opus 5.5). Note, scripts, receipt and stored current moved byte-identical; `check_saturation_recompute.py` was added at the migration. Legacy status: "written closure theorem and finite compiler; universal entry remains open".
- Main lane (ChatGPT, Codex), 2026-10-17, from commit `64fff1d`. The batch report (archive/convergence-residual-progress/REPORT.md) records "independent model" proof and code audits for this batch; they were the main lane's own agents, so they do not count as an independent review. The side lane's later finite check (probe kept in [`auxiliary-normalisation-remainder`](../auxiliary-normalisation-remainder/README.md)) is recorded under `reviewed_by`.
