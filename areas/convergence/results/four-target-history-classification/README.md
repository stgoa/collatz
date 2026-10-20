---
id: four-target-history-classification
kind: result
title: "On a whole remaining cell, only the original source reaches the direct target and its first three futures within their ternary precision"
status: written
claim: >
  Odd-only 3x+1 map S, absorbing at 1, canonical quotient T = nu S. For every m >= 0 let Q = 133704987 + 3 2^33 m,
  n = 385940463 + 64 3^19 m (the whole k = 85 + 16384m cell of the R84 progression after the R87 repair), and y_a
  = 3^a (n+1)/2^a - 1, a = 0, 1, 2, 3. For each a, the canonical origins p <= Q with T^d(p) = y_a, 0 <= d <= 19+a,
  consist exactly of p = Q at d = 18+a; ordinary histories from smaller origins to these targets, and to raw r =
  2n+1 within 19 ordinary arrows, are excluded too. Every inverse ray and word within the horizons is covered: an
  exact uniform anchor cutoff (c <= 133704987) and four complete finite inverse trees (64/78/89/101 states) prove
  it for all m. Consequently no single fixed quotient inverse word, and no fixed ordinary valuation word, of any
  length gives a strictly smaller origin throughout the cell. The existing comparison T^18(Q) = n, S^23(Q) =
  S^5(n) with K = L_23(Q) - L_5(n) is kept, and supplied H_v, H_b would give div(K + H_v - H_b) = P(b) - P(v) with
  the higher P(v) premise unresolved. Not an all-depth exclusion at a fixed source; m-dependent valuations, finer
  cells, later targets and signed comparisons remain open.
authors:
  - ChatGPT main lane (Codex)
created: 2026-10-18
depends_on: [elementary-bridge-quotient-normal-form, finite-anchor-history-classification, failed-w9-leader-reduction, later-target-twenty-step-descent]
certificates: [check_history_cell_recompute.py]
evidence:
  - "check_history_cell_scope.py, history_cell_scope.py, history_cell_scope_audit.json: the legacy implementation, checker and receipt: the four complete trees with every retained edge and first-excluded ray child, 28 lifts, 1024 canonical-arithmetic cases, three full signed 23/5 comparisons, 20 domain and cap rejections, and the hashes of the local sources and of four notes. Its receipt pins the SHA-256 of this node's legacy note HISTORY_CELL_SCOPE.md and of the legacy notes bridge_normal_form/BRIDGE_NORMAL_FORM.md, history_frontier/HISTORY_FRONTIER.md and w9_history_repair/W9_HISTORY_REPAIR.md, all now edited READMEs, so it fails at its new path and in a legacy replay (it already failed in the replay at this migration, because BRIDGE_NORMAL_FORM.md was edited by an earlier batch). Not reached at be73a66: the scripts/verify_all.py gate stopped earlier, at residual_progress/history_frontier (archive/legacy-checker-run-be73a66.md); it passed in full at 9dbc71a. Its audit is recomputed by check_history_cell_recompute.py; history_cell_scope.py is also loaded by the legacy checker of ../rational-basin-precision-barrier/"
  - "r88_anchor_exhaustive.c: side-lane C program (Claude side lane, 2026-10-18 05:52): exhaustive forward iteration of every canonical p <= 133704987 (33,426,246 states) for 22 quotient steps against the four targets at m = 0. Needs a C compiler (build line in its header), so it is evidence, not a certificate. Not part of the be73a66 reference run (archive/legacy-checker-run-be73a66.md lists Python scripts only); the side-lane feed reports a compiled run of about 5 s, and the main lane reproduced it in side_lane_review_86ead16.md (in ../binary-return-exit-control/): exactly four hits, all p = Q at depths 18-21, 4.96 s"
reviewed_by:
  - by: Claude side lane (Opus)
    date: 2026-10-18
    link: r88_anchor_exhaustive.c
    scope: "Finite only (side-lane feed entry 2026-10-18 05:52, VERIFIED (exhaustive), main 7a477ad): '**R88 anchor (`m = 0`), by exhaustive forward search.** This is independent of main's inverse-tree certificates. ... Every canonical `p ≤ Q`, 33,426,246 states in all, was iterated under `T = ν∘S` for 22 quotient steps by a small C program with its own `ν`. Exactly four hits on any `y_a` occur within `19 + a` steps, all at `p = Q`, at depths 18, 19, 20 and 21. That is precisely R88's claim at this anchor. The all-`m` lift rests on main's written argument and was not re-proved.' Also 'For m ∈ {0, 1, 2, 3} and 300 random m < 2⁴⁰ ... Q is canonical, T¹⁸(Q) = n > Q, and S²³(Q) = S⁵(n).' Reproduced by the main lane in side_lane_review_86ead16.md. The status stays written"
aliases: [R88]
tags: [convergence, outer-residual, smaller-origin-history, anchor-certificate, inverse-barrier, fixed-word]
---

# On a whole remaining cell, only the original source reaches the direct target and its first three futures within their ternary precision

## Statement

Odd-only clock, 1 absorbing; canonical quotient `T = νS` with the inverse table of [`elementary-bridge-quotient-normal-form`](../elementary-bridge-quotient-normal-form/README.md) (R25).

For `m ≥ 0` put `Q = 133704987 + 3·2^33·m`, `n = 385940463 + 64·3^19·m`, `b = Q/3`, `v = n/3`, `r = 2n + 1`: the whole `k = 85 + 16384m` cell of the R84 family ([`later-target-twenty-step-descent`](../later-target-twenty-step-descent/README.md)) after the R87 repair ([`failed-w9-leader-reduction`](../failed-w9-leader-reduction/README.md)). Here `v < Q < n`. Let `y_a = 3^a(n + 1)/2^a − 1`, `a = 0, 1, 2, 3`.

1. **Existing comparison.** The ordinary word from `Q` to `r` is `(1,2,1,1,1,1,1,2,2,1,1,2,2,1,1,3,1,2)` (length 18, total 26), `T^18(Q) = n`, `S^23(Q) = S^5(n)`, `K = L_23(Q) − L_5(n)`, `div K = [Q] − [n]`; with supplied `H_v, H_b`, `div(K + H_v − H_b) = P(b) − P(v)`, leaving the higher premise `P(v)` (rank `n > Q`).
2. **Four-target theorem.** For every `m ≥ 0` and each `a`, the canonical `p ≤ Q` and `0 ≤ d ≤ 19 + a` with `T^d(p) = y_a` are exactly `p = Q`, `d = 18 + a`. The same strict exclusion holds for ordinary histories to these targets and to raw `r` within 19 arrows. Every inverse ray and word is covered.
3. **Proof structure.** An exact uniform anchor cutoff `c + 1 < 133704989 + 1226171/387420489` gives `c ≤ 133704987`; four complete finite inverse trees (64, 78, 89, 101 states, sole origin at depths 18–21) and the lifting argument (as in [`finite-anchor-history-classification`](../finite-anchor-history-classification/README.md), R82) prove 2 for all `m`. The trees are part of the proof, not a sample.
4. **Fixed words.** A fixed quotient inverse word valid for every `m` has length at most `19 + a`; hence no one fixed word, quotient or ordinary, of any length gives a strictly smaller origin throughout the cell.

Not an all-depth exclusion at any fixed `m`; fixed clocks with valuations varying in `m`, finer cells, input-dependent words, later targets and signed comparisons remain open.

## Proof

The legacy note "R88 — A complete four-target history cell and its exact precision limit" follows, lightly edited (title dropped, headings demoted one level, links pointed to nodes). Its commands name pre-migration paths; see Certificates.

**Status: written lifting proof plus complete finite inverse-tree certificates;
no terminal-current supply, novelty claim, or convergence claim.**

This result concerns one whole remaining cell after the
[R87 repair](../failed-w9-leader-reduction/README.md) and the existing
returning forward comparison. It is not an all-depth exclusion at a fixed
positive source. The four finite anchor certificates below, together with
the lifting proof, establish an assertion for every integer parameter in
the cell. No forward absorption table or unknown smaller input is assumed.

We use the absorbed odd Syracuse map S and the canonical normal form nu of
[R25](../elementary-bridge-quotient-normal-form/README.md), with T=nu S on canonical
states. State and current row 1 are killed. All inverse targets here exceed
1, so the absorbed self-loop at 1 contributes no inverse history.

### 1. The whole cell and the existing signed comparison

For every integer m>=0 put

```
Q = Q0 + QP*m,       Q0=133704987, QP=3*2^33,
n = N0 + NP*m,       N0=385940463, NP=64*3^19,
b = Q/3,
v = n/3 = 128646821 + 64*3^18*m,
r = 2n+1 = 6v+1.
```

This is k=85+16384m in R84's q=11547+3*2^19*k progression. The exact
positive inequalities are v<Q<n. In particular

```
Q-v = 5058166 + 974892480*m > 0.
```

Here b=9 modulo16, v=37 modulo64, Q and n are canonical, and
v2(n+1)=4 with complementary unit. The raw r is selected with exponent5,
so nu(r)=n. The original critical rank is Q, not n or a later local parent.

The complete ordinary word from Q to r is

```
(1,2,1,1,1,1,1,2,2,1,1,2,2,1,1,3,1,2).                 (1)
```

It has length18 and total valuation26. Its exact cylinder has modulus
2^27, including the extra bit; QP is divisible by that modulus. Its
anchored arithmetic therefore proves the word for every m. The supplied
symbolic record also verifies every normalization decision on the complete
18-step quotient path. At m=0 that path is

```
133704987, 200557481, 150418111, 225627167, 338440751,
507661127, 761491691, 1142237537, 856678153, 642508615,
963762923, 1445644385, 1084233289, 406587483, 609881225,
457410919, 686116379, 1029174569, 385940463.
```

Each state has its exact affine increment stored in the receipt. Thus

```
T^18(Q)=n,                 S^23(Q)=S^5(n).                (2)
```

The second equality uses the selected identity at r, not an assertion
that all 23 valuations stay fixed over the cell. Let L_j(x) denote the
j-arrow ordinary current and N_r=L_5(r)-L_5(n). Then the entire current is

```
K = L_18(Q)+N_r = L_23(Q)-L_5(n),
div K = delta_Q-delta_n.                                  (3)
```

Every signed row and collision is retained. This is an existing comparison,
not a newly supplied absorption current. With P(w)=delta_(3w)-delta_w and
supplied absorption currents H_v,H_b, the conditional identity is

```
div(K+H_v-H_b) = P(b)-P(v).                               (4)
```

Both b and v lie below Q, but P(v) has rank n>Q and remains an unresolved
positive premise. Equation (4) does not discard the lower zero-source
relations that may occur in a different old compiler composition; it is a
separate exact source identity. No terminal H or P input is supplied here.

### 2. Exact statement

For a=0,1,2,3 define the four targets

```
y_a(m) = 3^a*(n(m)+1)/2^a - 1,
Y_a = y_a(0),       NP_a = NP*3^a/2^a,
D_a = 19+a.                                               (5)
```

They are n and its first three canonical valuation-one successors.
In particular v3(NP_a)=19+a exactly.

**Four-target theorem.** For every m>=0 and every a in this range, all
canonical origins p<=Q(m) and depths 0<=d<=D_a satisfying
T^d(p)=y_a(m) consist of the single pair

```
p=Q(m),                  d=18+a.                          (6)
```

Hence there is no strictly smaller canonical origin in that entire
horizon, over every inverse ray and every valuation choice. By T nu=nu S
and nu(p)<=p, the same strict exclusion holds for ordinary S histories to
these targets. An ordinary history from p<Q to raw r within19 steps is
also excluded because nu(r)=n. We do not assert uniqueness of arbitrary
noncanonical origins equal to Q from the quotient classification.

### 3. A uniform exact cutoff at the anchor

The complete inverse branches of T, recalled from R25, are as follows.
Each nonpoint base continues through every nonnegative index by
`x -> 64x+49`.

| Target modulo3 | Point | Two ray bases |
|---|---|---|
| 0 | none | (8y+3)/3, (16y+3)/3 |
| 1 | none | (4y-1)/3, (32y+19)/3 |
| 2 | (2y-1)/3 | (64y+19)/3, (128y+83)/3 |

For completeness, a complementary predecessor must equal (2y-1)/3.
A 1-modulo8 predecessor has ordinary successor F^k(c), where c is y or
2y+1, F(x)=4x+1, and k=1-c modulo3. These are exactly the two rays in
the table. Increasing k by3 gives the displayed recurrence. Thus there
are no omitted inverse types.

Each branch x -> alpha*x+beta has positive slope and alpha-beta>=1.
This holds at every listed base and is preserved by the ray recurrence:
the new difference is64(alpha-beta)-49>=15. Consequently, after any
composition with multiplier lambda and anchor endpoint c,

```
lambda >= (c+1)/(Y_a+1).                                  (7)
```

Indeed at depth0 equality holds. At the next inverse step,
`alpha(c+1) >= alpha*c+beta+1`, proving the induction.

An actual inverse word through D_a steps also lifts backwards to the same
word at Y_a. At each preceding step the actual-anchor difference is even
and divisible by3; the selected residue branch therefore agrees. A step
divides its ternary precision by3 and multiplies by a power of2. The
initial difference NP_a*m is divisible by3^D_a and is even, so this remains
valid through depth D_a, including the last integrality step. Every lifted
anchor state is positive and canonical by the complete inverse formulas.

Write its actual endpoint as p=lambda*(y_a-Y_a)+c. From (7),

```
p+1 >= (c+1)*(y_a+1)/(Y_a+1).
```

If p<=Q this gives the same bound for every a:

```
c+1 <= C(m) = (Q(m)+1)*(N0+1)/(n(m)+1).                    (8)
```

This rational function increases from Q0+1 to

```
C_infinity = QP*(N0+1)/NP
           = Q0+2+1226171/387420489 < Q0+3.                 (9)
```

Thus c<Q0+2. Since c is odd and Q0 is odd, c<=Q0. This includes p=Q;
there is no strict-inequality rounding omission. Formula (8), not a blanket
anchor-minus-one cutoff, is the sufficient exact bound used here. See the
[R82 cutoff theorem](../finite-anchor-history-classification/README.md) for the
general distinction.

### 4. Complete finite certificates at all four anchors

The elementary bound T(x)<=(3x+1)/2 yields

```
T^j(c)+1 <= (3/2)^j*(c+1).                                (10)
```

For a prospective inverse child at depth e<=D_a, any path which can end
at an origin at most Q0 by depth D_a must therefore satisfy

```
child <= floor((Q0+1)*3^(D_a-e)/2^(D_a-e))-1.               (11)
```

This also covers origins at shorter depths because the right side grows
with the permitted number of remaining steps. The point branch is tested
once. Each ray strictly increases, so its first child failing (11)
excludes the entire infinite remaining tail. The finite tree stores all
retained vertices, complete words, affine periods, and every first-excluded
ray child and cutoff. No slope pruning, guessed ray-index limit, or
absorbing forward catalogue is used. A separate resource cap raises an
error rather than turning an incomplete search into a certificate.

The replay establishes:

| a | Horizon D_a | Retained states | Only origin <=Q0 | Its depth |
|---:|---:|---:|---:|---:|
| 0 | 19 | 64 | 133704987 | 18 |
| 1 | 20 | 78 | 133704987 | 19 |
| 2 | 21 | 89 | 133704987 | 20 |
| 3 | 22 | 101 | 133704987 | 21 |

Every retained edge is checked independently against canonical arithmetic.
The independent enumeration derives ray bases from F^k(y) and F^k(2y+1),
not from the implementation's branch table. The four sole-hit words have
exact origin increment QP when the target increment is NP_a. Their lifts
are therefore Q0+QP*m=Q(m). Combined with (8), this proves (6) for every m.

### 5. Consequence for one fixed word, without a depth restriction

A fixed quotient inverse word of length d has multiplier 2^E/3^d, with
integer E>=d. If the same word is legal at y_a(m) for **every** m>=0, the
difference between its origins at m=1 and m=0 is

```
2^E*NP_a/3^d,
```

which must be an integer. Since v3(NP_a)=19+a exactly, d<=19+a. The
four-target theorem then applies. **No single fixed quotient inverse word
of any length gives a strictly smaller origin throughout this whole cell.**

The same denominator argument applies to a fixed ordinary valuation word
ending at y_a: its inverse multiplier is also a power of2 divided by3^d.
After the depth bound, the ordinary strict exclusion in Section2 applies.
The quantifier is one word valid for all m, not every word at one fixed m.
It does not exclude fixed ordinary clocks whose valuations vary with m,
partitioning the parameter into deeper ternary cells, input-dependent
words, later or differently normalized targets, or arbitrary signed
comparisons. The ordinary 23/5 relation in (2) illustrates why clocks and
valuation words must not be identified.

### 6. Reproduction, scope and the remaining task

Run from the repository root:

```
python3 experiments/residual_progress/history_cell_scope/check_history_cell_scope.py
```

The default rebuilds and independently checks the complete trees and
compares the stored receipt. `--write-receipt` updates only the receipt in
this folder. The receipt retains the complete trees, exact symbolic
18-step paths, representative full signed 23/5 currents, large-parameter
lifts, rejection controls, and hashes of the local sources and the cited
mathematical dependencies. It uses only the Python standard library.

The finite certificates are part of the proof; they are not a finite scan
being extrapolated to all m. Conversely they are not all-depth exclusion
certificates for any one fixed m. No new accepted dispatcher rule, input
current supply, or general history-termination theorem is established.

This closes the direct target and its first three futures within their
available ternary precision, and any one uniform word to those targets.
The original-rank problem remains: construct a genuinely different or
input-dependent comparison that supplies P(v), or another exact signed
closure. Replacing Q by the larger n would merely rename a failed
original-rank comparison as local descent.

## Certificates

[`check_history_cell_recompute.py`](check_history_cell_recompute.py) (written at the B13 migration; standard library). No legacy check of this node passes any more: its legacy checker pins the SHA-256 of notes that are now edited READMEs, and no other legacy check of it passes (it has no side-lane probe, or only a C program that needs a compiler). The certificate rebuilds the pre-migration layout in a temporary directory from `tools/legacy_paths.json`, replaces each pinned note by a placeholder, imports the unmodified legacy checker there and runs its audit, and requires the result to equal the committed receipt after removing only those note hashes; every other value, including the hashes of the pinned code and data, must agree. It writes nothing in the repository. It rebuilds the four complete trees, the lifts, the symbolic paths, the signed 23/5 comparisons and the rejection controls (about 3 s). The side-lane C program `r88_anchor_exhaustive.c` needs a compiler and is evidence only. The command in the legacy text names `experiments/residual_progress/history_cell_scope/`.

## Remarks

- The REPORT records two bounded scratch explorations before this result (a direct/future fixed-word probe and an adaptive ternary refinement covering 57/729 of the classes); they were not promoted and are not premises.
- Replacing `Q` by the larger `n` would only rename a failed original-rank comparison as local descent; the remaining task is a different or input-dependent comparison that supplies `P(v)`.
- No novelty is claimed.

## History

- Migrated from `experiments/residual_progress/history_cell_scope/HISTORY_CELL_SCOPE.md` (legacy ID R88) at commit `be73a66`, by the B13 migration (Claude, Opus 5.5). Note, scripts and receipts moved byte-identical; the note became this README, lightly edited (title dropped, headings demoted one level, links pointed to nodes). Legacy status: "written lifting proof with complete finite inverse-tree certificates; no terminal-current supply".
- The side-lane C program `reviews/side_lane/r88_anchor_exhaustive.c` moved here.
- Main lane (ChatGPT, Codex), 2026-10-18, first committed in `7a477ad`. The batch's "independent" proof, source and default-replay reviews recorded in archive/convergence-residual-progress/REPORT.md were the main lane's own agents, not a different lane.
