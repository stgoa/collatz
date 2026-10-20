# R88 — A complete four-target history cell and its exact precision limit

**Status: written lifting proof plus complete finite inverse-tree certificates;
no terminal-current supply, novelty claim, or convergence claim.**

This result concerns one whole remaining cell after the
[R87 repair](../w9_history_repair/W9_HISTORY_REPAIR.md) and the existing
returning forward comparison. It is not an all-depth exclusion at a fixed
positive source. The four finite anchor certificates below, together with
the lifting proof, establish an assertion for every integer parameter in
the cell. No forward absorption table or unknown smaller input is assumed.

We use the absorbed odd Syracuse map S and the canonical normal form nu of
[R25](../bridge_normal_form/BRIDGE_NORMAL_FORM.md), with T=nu S on canonical
states. State and current row 1 are killed. All inverse targets here exceed
1, so the absorbed self-loop at 1 contributes no inverse history.

## 1. The whole cell and the existing signed comparison

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

## 2. Exact statement

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

## 3. A uniform exact cutoff at the anchor

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
[R82 cutoff theorem](../history_frontier/HISTORY_FRONTIER.md) for the
general distinction.

## 4. Complete finite certificates at all four anchors

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

## 5. Consequence for one fixed word, without a depth restriction

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

## 6. Reproduction, scope and the remaining task

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
