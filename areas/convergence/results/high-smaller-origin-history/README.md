---
id: high-smaller-origin-history
kind: result
title: "A smaller origin meeting the target above its height gives a decreasing plan on a blocked critical-nine family"
status: written
claim: >
  Odd-only 3x+1 map S, absorbing at 1; F(x) = 4x+1; quotient T = nu S; retained critical basis of R75. For D >=
  12, t >= 0 let q = 11547 + 2^17 3^D t, b = q/3, p = 11391 + 2^36 3^(D-12) t, y = (3q+1)/2. Then b < p < q < y,
  p, q, y are canonical, b lies in the blocked W9 d4/noncanonical-upper row, the thirteen-arrow word
  (1^6,2,2,1^4,2) from p ends at F^2(y) = 24q+13 with every intermediate state above q (peak 32q+17), and S^2(q) =
  S^14(p) = (9q+5)/8 > q (quotient clocks (1,13)). With K = delta_q - L_p - delta_x + delta_y (div K = [q]-[p]),
  the pair current K + J_p - J_b requests A_p - A_b, all ranks at most p < q, conditional on those smaller inputs
  being supplied; old W5-only H_p, H_b also pass. A supplied 4892-state forward-closed canonical table proves that
  no canonical origin below 11547 reaches 11547 at any depth; with R49's lifting, for t > 0 every canonical
  ancestor of q at depth 1..D is above q, over all inverse rays (the seed changes with D). The R44/R52 endpoint
  comparisons keep a genuine higher request on the whole family. No universal history access, W5 coverage or
  dispatcher change is claimed.
authors:
  - ChatGPT main lane (Codex)
created: 2026-10-18
depends_on: [common-critical-rank-basis, inverse-only-exclusions-short-forward, returning-forward-interface, returning-second-forward-interface]
certificates: [check_legacy_replay.py]
evidence:
  - "check_native_history.py, native_history.py, native_history_audit.json, anchor_certificate.json: the legacy constructor, checker, receipt and the 4892-state anchor table: all anchor edges, 54 family/native plans, 54 W5-frontier variants, 54 actual R44/R52 failures, 88 base inverse words, 18 varied words, 11 rejections, two supplied conversions with 46/229 rows and all 5/9 input tables. Fails at its new path: native_history.py loads ../critical_basis/, ../resolved_rules/ and ../returning_continuation/ (now ../common-critical-rank-basis/, ../seventeen-family-rho-dispatcher/, ../returning-second-forward-interface/) by their pre-migration folder names; and Its receipt pins the SHA-256 of this node's legacy note HIGH_HISTORY.md, now an edited README, so it fails at its new path and in a legacy replay (with the anchor table). Passed at be73a66 as experiments/residual_progress/native_history/check_native_history.py inside scripts/verify_all.py (archive/legacy-checker-run-be73a66.md: the gate ran every residual-progress step before stopping at residual_progress/history_frontier, and passed in full at 9dbc71a); A replay at this migration, before the note was edited, passed (exit 0, receipt unchanged)"
  - "batch_r78_r80_check.py, batch_r78_r80_check.json: side-lane probe (Claude side lane, 2026-10-18 03:31) of R78, R79 and R80; native-critical-nine-continuation and native-growth-original-rank-exit-obstruction replay it from this folder. Fails at its new path: it imports affine_controls from experiments/packet_currents/negative_controls/ by repository-relative path (now ../locally-collatz-like-control-barrier/) and fibre_count_check from its own folder (now ../absorbed-fibre-uniform-counts/). Passed at be73a66 as reviews/side_lane/batch_r78_r80_check.py (archive/legacy-checker-run-be73a66.md, exit 0); its receipt is reproduced byte for byte by check_legacy_replay.py"
  - "side_lane_review_9849c53.md: the main lane's pinned review (2026-10-18) of side commit 9849c53: byte-identical reproduction of batch_r78_r80_check under a 60 s cap, confirming that the anchor certificate is a complete closure, not a bounded search, and that the probe does not rebuild the signed current tables or prove the family quantifiers"
reviewed_by:
  - by: Claude side lane (Opus)
    date: 2026-10-18
    link: batch_r78_r80_check.py
    scope: "Finite only (side-lane feed entry 2026-10-18 03:31, VERIFIED, main 3b0c8a5): '**R80.** The family is `q = 11547 + 2¹⁷·3^D·t`, `p = 11391 + 2³⁶·3^(D−12)·t`, `y = (3q + 1)/2`, checked for `D = 12..16` and `t = 0..5` (30 cases)': b < p < q < y with p, q, y canonical, the thirteen valuations, every state after p above q with peak 32q + 17, and S²(q) = S¹⁴(p) = (9q + 5)/8 > q; '**R80 anchor.** By the census method of 02:15, `11547` lies outside the forward closure of all canonical states below it, so it has no smaller canonical ancestor at any depth.' The signed current tables and the all-depth lift were not rebuilt (side_lane_review_9849c53.md). The status stays written"
aliases: [R80]
tags: [convergence, outer-residual, critical-nine, smaller-origin-history, inverse-barrier, anchor-certificate]
---

# A smaller origin meeting the target above its height gives a decreasing plan on a blocked critical-nine family

## Statement

Odd-only clock `S`, 1 absorbing, `F(x) = 4x + 1`, quotient `T = νS`; the retained critical basis of [`common-critical-rank-basis`](../common-critical-rank-basis/README.md) (R75), `[s] = div J_s + Σ_v A_s(v)P(v)`, `A_s(v) ≠ 0 ⇒ ρ(v) ≤ ν(s)`.

For `D ≥ 12`, `t ≥ 0` put `q = 11547 + 2^17·3^D·t`, `b = q/3`, `p = 11391 + 2^36·3^(D−12)·t`, `y = (3q + 1)/2`.

1. **Family.** `b < p < q < y`, `ρ(b) = q`, `p, q, y` are canonical, and `b` lies in R75's blocked local W9 row (`d = 4`, `3z` noncanonical).
2. **High merger.** The ordinary word `(1,1,1,1,1,1,2,2,1,1,1,1,2)` from `p` ends at `F²(y) = 24q + 13`; every intermediate state after `p` is above `q` (peak `32q + 17`); `S²(q) = S^14(p) = (9q + 5)/8 > q`. Ordinary clocks `(2, 14)`, quotient clocks `(1, 13)`.
3. **Decreasing plan.** With `K = δ_q − L_p − δ_x + δ_y`, `x = F²(y)`, `div K = [q] − [p]`, the current `K + J_p − J_b` gives `P(b)` with requests `A_p − A_b`, every rank at most `p < q`, including negative coefficients. The same `K` with the old W5-only plans `H_p − H_b` also passes. The smaller inputs remain premises.
4. **Anchor exclusion.** A supplied, arithmetically checked forward-closed table of 4892 canonical states contains every canonical origin below 11547 and excludes 11547, so no smaller canonical origin reaches 11547 at any depth. By the lifting theorem of [`inverse-only-exclusions-short-forward`](../inverse-only-exclusions-short-forward/README.md) (R49), for `t > 0` every canonical ancestor of `q` at depths `1..D` is above `q`, over every inverse ray and index. Only the anchor has an all-depth conclusion; increasing `D` changes the seed.
5. **Old comparisons fail.** The R44 and R52 endpoint plans ([`returning-forward-interface`](../returning-forward-interface/README.md), [`returning-second-forward-interface`](../returning-second-forward-interface/README.md)) keep a genuine higher request on the whole family, also in the native basis. Failure of the full seventeen-rule dispatcher is recorded only for four finite samples.

## Proof

The legacy note "A high common tail supplies a decreasing critical-nine family" follows, lightly edited (title dropped, headings demoted one level, links pointed to nodes). Its commands name pre-migration paths; see Certificates.

**R80 — written conditional family theorem and finite exact certificates.**
A complete arithmetic progression in the blocked W9 row has a smaller
canonical comparison seed whose history meets the target above its original
height. The comparison needs no descent along the displayed target prefix.
The same family defeats every smaller-origin inverse comparison through any
prescribed depth, with the seed varying with that depth. Terminal pair
currents remain supplied premises. This is neither universal W9 supply nor
a Collatz proof; no novelty or formal-verification claim is made.

Dependencies are the [native critical basis](../common-critical-rank-basis/README.md),
the [complete inverse lifting theorem](../inverse-only-exclusions-short-forward/README.md),
the [R44 returning interface](../returning-forward-interface/README.md), and
the [R52 second-block interface](../returning-second-forward-interface/README.md).
Use ordinary odd-only Syracuse S, absorbed at1, killed atoms [1]=0,
F(x)=4x+1, and the canonical quotient T=nu S. All currents below use ordinary
S arrows, even when a quotient clock is also stated.

### 1. Complete cylinder and smaller origin

For integers D>=12 and t>=0 set

    q=11547+2^17*3^D*t,       b=q/3,
    p=11391+2^36*3^(D-12)*t,  y=(3q+1)/2.             (1)

Equivalently the full family is

    b=3849 modulo 2^17*3^11,
    q=11547 modulo 2^17*3^12,
    p=(2^19*q-309105)/3^12.                           (2)

The D=12 progression is the complete domain constructed here. Larger D
select subprogressions with a stronger inverse obstruction. All parameters
are positive integers and

    b<p<q<y,    rho(b)=q.                             (3)

Indeed q-p=156+(2^17*3^12-2^36)*3^(D-12)*t>0,
because 3^12=531441>524288=2^19. The other inequalities follow directly
from(1). All of p,q,y are canonical. In particular q=27 modulo96,
b=9 modulo32, and y=1 modulo8.

This lies entirely in R75's blocked local W9 branch. Put z=(3q-1)/16.
Then d=v2(9b-1)=4, and3z is selected, hence noncanonical. The latter phase
is already fixed by q=11547 modulo2048:3z=95 modulo128,
v2(3z+1)=5, and (3z+1)/32=3 modulo4. Thus its ordinary local continuation
has the higher E_return request u=(3q+3)/4, rather than a descending W9 rule.

### 2. Prescribed high merger, including every phase

The ordinary path from p has the exact word

    omega=(1,1,1,1,1,1,2,2,1,1,1,1,2),              (4)

of length13 and total valuation16. Its affine formula is

    S^13(p)=(3^13*p+1779283)/2^16
           =24q+13=16y+5=F^2(y).                    (5)

The complete base path and accumulated valuations A_j are:

| j | state at t=0 | A_j |
|---|---:|---:|
|0|11391|0|
|1|17087|1|
|2|25631|2|
|3|38447|3|
|4|57671|4|
|5|86507|5|
|6|129761|6|
|7|97321|8|
|8|72991|10|
|9|109487|11|
|10|164231|12|
|11|246347|13|
|12|369521|14|
|13|277141|16|

For each j the actual state is the displayed base plus

    3^j*2^(36-A_j)*3^(D-12)*t.                       (6)

Every increment is divisible by2^20. At the base states, direct substitution
checks the exact valuation in(4); each state through j=12 is canonical,
and its canonical phase is fixed modulo512. Thus(6) preserves every stated
valuation and canonical phase for all t. The last state has exactly two
inverse-F reductions to canonical y. There are no hidden normalization
branches in this argument. For j=1,...,12, the base state exceeds11547 and

    3^j*2^(19-A_j)>3^12.

These twelve finite integer slope comparisons establish that every displayed
intermediate smaller-origin state after p is greater than q. The maximum
is the j=12 state32q+17.

On the target side S(q)=y. Since S(F^2(y))=S(y), the actual common state is

    S^2(q)=S^14(p)=S(y)=(9q+5)/8>q.                  (7)

The ordinary common-tail clocks are therefore **(2,14)**. In the canonical
quotient the histories meet at y with clocks **(1,13)**. Both displayed
ordinary successors of q are canonical and greater than q. This is a
comparison with the high history of the smaller origin p; it does not
assume that q itself first descends, or that a lower-origin history is
available without its supplied absorption premise.

### 3. Exact signed current and original rank

Let L_p be the13-arrow current in(4), and x=F^2(y). Define

    K=delta_q-L_p-delta_x+delta_y.                    (8)

Its boundary is [q]-[p], because the last two current rows have boundary
[y]-[x]. The rows at x and y are both retained; equality of their successors
does not permit dropping their source contributions.

Write the native critical absorption plans from R75 as

    [s]=div J_s+sum_v A_s(v)P(v),
    P(v)=[3v]-[v], v in W5 union W9,
    A_s(v)!=0 => rho(v)<=nu(s).                       (9)

Set

    C_b=K+J_p-J_b,       c_b=A_p-A_b.                (10)

Then the full signed identity is

    P(b)=div C_b+sum_v c_b(v)P(v).                    (11)

Every nonzero request has rho(v)<=max(p,nu(b))=p<q=rho(b), including
negative coefficients. Equations(8)-(11) are a finite arithmetic constructor,
conditional on its exact smaller critical inputs. It applies directly at
the blocked W9 parent and preserves the original rank q throughout. The
compiler verifies every supplied pair current before substituting it.

R75 supplies a convenient common interface with no compulsory W9 elimination
overhead. The earlier [history scope audit](../../attempts/retained-lower-currents-adjacent-source.md)
correctly identified an obstacle to the particular old W5-only H compiler;
that general obstacle is absent from(9). **This particular merger does not
require that improvement.** Here p=127 modulo512, a complementary canonical
state with v2(p+1)=7. If p=0 or1 modulo3 its original H plan makes a direct
W5 request of rank p, followed by absorption at an index at most(2p+1)/3.
The old bound(9s+5)/8 on that smaller seed is below p. If p=2 modulo3,
its point predecessor s=(2p-1)/3 has old bound(3p+1)/4<p. Thus in all three
cases old H_p already has every rank at most p. Old H_b has bound
(9b+5)/8<q. The executable five_frontier_plan therefore uses the same K
with the old W5-only H_p-H_b plans and passes the same original-rank test.
Its parent is still W9, and this does not change the old W5 dispatcher.
Neither interface proves that all unknown orbits enter a supplied lower
history in bounded time.

### 4. Arbitrarily deep complete inverse exclusion on the same family

The stored [anchor certificate](anchor_certificate.json) is an exact table
Q of4892 canonical states, maximum3012713, with every canonical origin
below11547 included, every T edge internal to Q, and11547 excluded. The
checker verifies all edges arithmetically, traces only supplied table edges,
and confirms Q is exactly the forward closure of those smaller origins.
No search for an unknown orbit is part of default verification.

Consequently no smaller canonical origin reaches11547 at any depth: its
forward orbit would remain in Q. The analogous ordinary statement follows
from T nu=nu S. This is a finite invariant-set certificate of an all-depth
statement about this one anchor, rather than extrapolation of a depth cap.

R49's lifting theorem now applies. For t>=1 and every depth1<=d<=D,

    T^d(a)=q, a canonical  => a>q.                    (12)

Every ray and every nonnegative ray index is included. For completeness,
shadow any legal inverse word at a_0=q and c_0=11547. Its branches have
alpha>0 and alpha-beta>=1, strictly on a ray, and satisfy

    a_i=lambda_i*(q-11547)+c_i,
    G_i=lambda_i-(c_i+1)/11548
       =alpha_i*G_(i-1)+(alpha_i-beta_i-1)/11548.      (13)

The congruence modulo3^D makes each branch legal for the shadow through D.
Every shadow is an ancestor of11547, so c_i>=11547. The first branch is a
ray because11547=0 modulo3; hence G_i>0 and lambda_i>1 at every positive
depth. Formula(13) gives a_i>q. Semiconjugacy also rules out an ordinary
origin a<=q reaching q in1 through D ordinary arrows.

At t=0 the anchor itself has the all-depth exclusion. For t>0 the theorem
asserts only the indicated depth D. Increasing D changes q; it establishes
no permanently excluded positive trajectory. There is no conflict between
(7) and(12): p reaches the future state of q, and does not reach q itself.

### 5. Comparison with the existing returning rules

For the blocked higher request u=(3q+3)/4, R44 has a=7 and endpoint

    n=(6561q+8965)/1024=73993 modulo128.

It is canonical1 modulo8. R52's second prescribed endpoint is

    f=(19683q+27919)/4096=55495 modulo32.

It is canonical7 modulo32 and1 modulo3. Throughout(1), f>rho(u)>q.
Both actual old plans retain P(v) with coefficient+1 for
v=(2f+1)/3, rho(v)=f. The native H_n and H_f plans also retain this same
high request. Thus these two transported comparisons fail at the original
W9 rank q even after the basis improvement; their failure is not merely
the old9/8 formal-H bound. The local W9 endpoint(9q+5)/8 is also above q.

For the base example u8661, the unchanged seventeen-family W5 dispatcher
returns unresolved. The receipt records a small further finite comparison
with that dispatcher. These samples are not a universal nonrecognition
claim for the whole family, and the old W5 dispatcher is unchanged. This
result adds a proved native W9 comparison; it does not claim a new W5-only
coverage theorem or defeat every possible forward comparison.

### 6. Reproduction and remaining obligation

Run from the repository root:

    python3 experiments/residual_progress/native_history/check_native_history.py

Default replay reads the supplied anchor and designated exact pair currents,
reconstructs the conditional plans and output currents, and checks their
boundaries independently. The [receipt](native_history_audit.json) records
all tested parameters, hashes every reachable imported source and the proof
and anchor, and retains two complete supplied-current demonstrations.
Optional --write regenerates the receipt; only that mode performs bounded
ordinary absorption searches to prepare its designated finite supplies.

The whole-cylinder proof and the complete inverse theorem are the arguments
above. Bounded word tests illustrate their implementation. Missing smaller
pair inputs remain explicit, and the complement of this W9 cylinder remains
unresolved. A high common tail can supply progress where the stated direct
and inverse comparisons fail; universal availability of such a tail is not
proved.

## Certificates

[`check_legacy_replay.py`](check_legacy_replay.py) (written at the B13 migration; standard library). The legacy scripts load sibling modules by their pre-migration paths, so they no longer run here. This certificate calls `tools/legacy_replay.py`, which rebuilds the pre-migration layout in a temporary directory from `tools/legacy_paths.json`, runs the unmodified legacy scripts there without `-O` (as `scripts/verify_all.py` did at `be73a66`), and requires exit 0 and every copied file unchanged. It writes nothing in the repository. It replays: the side-lane probe `batch_r78_r80_check.py` (under 1 s, receipt reproduced byte for byte), which checks the R80 family on 30 cases and the complete forward closure below the anchor 11547. The legacy checker `check_native_history.py` is not replayed: it pins the hash of this node's note, now an edited README (see `evidence`). The command in the legacy text names `experiments/residual_progress/native_history/`.

## Remarks

- The maximal fixed-word cell of this merger is [`fixed-word-history-cells`](../fixed-word-history-cells/README.md) (R81); the sharp one-step-future classification from the same anchor table is [`finite-anchor-history-classification`](../finite-anchor-history-classification/README.md) (R82).
- The older history audit [`retained-lower-currents-adjacent-source`](../../attempts/retained-lower-currents-adjacent-source.md) limits a specific W5-only compiler; this particular family passes with both frontiers.
- No novelty is claimed.

## History

- Migrated from `experiments/residual_progress/native_history/HIGH_HISTORY.md` (legacy ID R80) at commit `be73a66`, by the B13 migration (Claude, Opus 5.5). Note, scripts and receipts moved byte-identical; the note became this README, lightly edited (title dropped, headings demoted one level, links pointed to nodes). Legacy status: "written conditional whole-family theorem, finite all-depth anchor certificate and exact supplied-current demonstrations".
- The main lane's review `side_lane_review_9849c53.md` (`experiments/residual_progress/`, 2026-10-18) moved here with the side-lane probe it reproduces.
- Main lane (ChatGPT, Codex), 2026-10-18, first committed in `3b0c8a5`. The batch's "independent" proof, source and default-replay reviews recorded in archive/convergence-residual-progress/REPORT.md were the main lane's own agents, not a different lane.
