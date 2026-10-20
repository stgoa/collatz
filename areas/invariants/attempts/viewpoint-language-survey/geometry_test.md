# V002 — What an inverse-conductance tail bound controls

**Decision: demote geometry to an approximation tool pending a new global
estimate.** This bounded test proves an elementary local bound and compares
two tiny domains. It does not establish a growing-domain absorption average,
and does not justify a deeper potential-theory investigation. No novelty is
claimed. It continues the exact convention in
[the V001 probe](potential_probe.md); the frozen R7 component criterion
and R10 boundary-flux warning remain applicable.

## 1. Domain, absorber and exact inverse tails

Fix a positive odd integer d with 3 not dividing d. Vertices are positive
odd integers. Each actual odd-only arrow

\[
 n\longrightarrow S_d(n)=\frac{3n+d}{2^{v_2(3n+d)}},\qquad n>1,
\]

supplies an undirected edge of conductance 1/n. Parallel edges add, self-loops
are omitted, and 1 has no outgoing arrow. The associated reversible walk has
an auxiliary clock, not the deterministic odd-step clock. For finite F
containing 1, write u_F for its probability of hitting 1 before leaving F;
every omitted edge leads to the zero escape boundary.

An inverse source of an odd target y has the form

\[
 n_a=\frac{2^a y-d}{3},\qquad a\ge1.                 \tag{1}
\]

It is retained only when integral and n_a>1, and when it is not a self-loop.
Integrality makes n_a odd; the identity 3n_a+d=2^a y gives the **exact**
valuation a. If 3 divides y, there are no inverse sources. Otherwise,
integrality selects exactly one parity of a. Before any loop or absorber
deletion, successive positive candidates therefore obey

\[
 n_{a+2}=4n_a+d.
\]

Suppose a nonempty omitted set of inverse sources has least member n_0>1.
All its members belong to the ray

\[
 n_j=4^j n_0+\frac{d(4^j-1)}3,\qquad j\ge0.
\]

Thus its total conductance T obeys the uniform bound

\[
 \frac1{n_0}\le T\le
 J_d(n_0):=\sum_{j\ge0}\frac1{4^j n_0+d(4^j-1)/3}
 \le\frac4{3n_0}.                                    \tag{2}
\]

The middle inequality allows an arbitrary omitted subset, not just a full
tail. Deleting the absorber or a self-loop can only reduce its sum. An empty
omitted set has T=0. Equation (2) also establishes finiteness of the incident
conductance at every vertex. J_d is an exact convergent-series specification;
no truncated rational sum is being called the exact conductance.

For the height domain F_R consisting of all odd vertices at most an integer
R, every omitted inverse source is greater than R. At each y in F_R,

\[
 T^{\rm in}_{R}(y)\le\frac4{3(R+1)}.                 \tag{3}
\]

This concerns incoming edges only. If S_d(y)>R, the actual outgoing edge
contributes another escape conductance **1/y**. It cannot be discarded or
bounded by (3). At the absorber no harmonic equation is required.

For an exponent cutoff one may instead choose the first admissible a_0 at
or above that cutoff with 2^{a_0}y>d+3. Equation (2) gives
T <= 4/(2^{a_0}y-d) for its full tail, with any deleted loops removed. This
explicit threshold matters when y is small compared with d.

## 2. Height cutoff versus a supplied path

For d=1 the actual path

\[
7\longrightarrow11\longrightarrow17\longrightarrow13
 \longrightarrow5\longrightarrow1                         \tag{4}
\]

uses five odd arrows. In F_13={1,3,5,7,9,11,13}, the interior component
{7,9,11} has no path to 1: 9 maps to 7, 7 to 11, and 11 escapes to 17 with
conductance 1/11. Consequently u_{F_13}(7)=0, despite its actual absorption.
The small incoming tails do not repair that missing outgoing connection.

Now take the supplied-path domain F_path={1,5,7,11,13,17}. The five internal
edge weights along (4) are exactly 1/7, 1/11, 1/17, 1/13 and 1/5. All its
omitted inverse conductances are specified by the following table:

| Vertex | Exact escape conductance | Rational upper bound |
|---|---:|---:|
| 7 | J_1(9) | 4/27 |
| 11 | J_1(29) | 4/87 |
| 17 | J_1(45) | 4/135 |
| 13 | J_1(69) | 4/207 |
| 5 | 1/3 + J_1(53) | 19/53 |

The absorber's incident edges need not enter its fixed boundary equation.
Every other forward edge is internal. Replacing these escape totals by
their upper bounds gives a finite rational lower-comparison problem; it
does not silently omit an infinite family of edges.

A simple bound already proves positivity without solving that system. For
d=1 and y>=3, each inverse contribution is at most
18/(5*2^a*y), since 2^a*y>=6. Summing over its one admissible exponent parity
gives total incoming conductance at most 12/(5y). The forward-edge
probability of the auxiliary walk is therefore at least 5/17. The event of
following (4) exactly gives

\[
 u_{F_{\rm path}}(7)\ge (5/17)^5>0.                   \tag{5}
\]

The two displayed domains are not nested, so this is not a general domain
monotonicity comparison. The larger height domain F_17 does contain F_path
and hence has at least its voltage. All three statements concern finite
sets with exact boundary conditions. Supplying path (4) is a valid input;
it has already supplied the absorption fact before the voltage is computed.

## 3. Why the estimate does not yet control an average

For this functional graph, u_F(n)>0 exactly when the actual forward path
from n to 1 is contained in F. This follows from the unique simple path to
the root in its undirected component; it is the finite-component criterion,
not a new method of identifying that component. On a supplied path union,
all positive-voltage membership was already proved by the supplied paths.
On a height domain, membership additionally depends on the unknown future
excursion height, as (4) demonstrates.

Let h_o(X)=sum_{odd n<=X}1/n. A proposed quantitative improvement needs, for
example, explicitly specified growing finite domains F_X and

\[
 \frac1{h_o(X)}\sum_{\substack{n\le X\\n\ {
m odd}}}
          \frac{u_{F_X}(n)}n\ge\frac12
 \quad\hbox{for every integer }X\ge X_0.             \tag{6}
\]

This would imply a logarithmic absorption lower bound, allowing exceptions.
No such estimate is derived here. Every fixed finite domain has normalized
average tending to zero. Equation (3) bounds each local leak; it gives no
bound on the effect of repeatedly revisiting a leaking vertex, no control
of outgoing escapes, and no lower bound on how much of the input ensemble
connects to 1. A resolvent/occupation estimate or a valid subharmonic
comparison is still needed. Even summing O(1/R) leaks over O(R) vertices
does not make the total leakage vanish, and that sum alone is not the
weighted voltage error.

Low Dirichlet energy without the required boundary and comparison
inequalities is insufficient. Wiring unknown exits to 1 would replace the
missing absorption premise by an assumption. The frozen R10 example makes
the analogous boundary-flux error explicit for currents; its particular
counterexample is not a theorem against all potential-theoretic estimates.

## 4. Controls and transfer scope

The entire inverse-tail argument transfers unchanged to d=5 and d=61.
For d=5, the arrows 19→31→49→19 have exact valuations (1,1,3) and
conductances 1/19, 1/31, 1/49. Their component cannot contain 1. Hence all
three voltages are zero for **every** finite domain, despite the same local
tail bound. The escape arrows 11→19, 81→31 and 129→49 from the V001 probe
still retain their conductances 1/11, 1/81 and 1/129.

For d=61, the simplest direct control is S_61(61)=61. Removing this
self-loop does not connect its component to 1 or assign it positive
voltage. The separately certified 41-cycle with minimum 235 in the
[frozen negative-control record](../../../convergence/results/locally-collatz-like-control-barrier/NOTE.md)
is a nonprincipal control with the same conclusion. These are statements
for the designated absorber **1**, without enlarging it to include cycles.

More generally S_d(dm)=d*S_1(m) for odd m. When d>1 its multiple-of-d
sector never reaches 1 and has relative odd logarithmic density 1/d.
Thus the local bound supplies no distinction between absorbing and
nonabsorbing sectors. This observation does not refute a 50% theorem for
these maps: the displayed sectors alone are too small to do so. Any future
claim must state whether it is fractional or pointwise before applying the
controls.

## 5. What would earn another test

The proved tail bound is useful for rigorous finite voltage approximation.
The domain comparison recovers supplied membership and exposes the
uncontrolled excursion. **It earns no further geometry-only slot now.**

A further bounded test would need a concrete new arithmetic estimate on an
explicit unbounded domain family, chosen independently of unknown
absorption: either a subsolution with all escape terms checked, or an
occupation/error bound that links (3) to a nonvanishing weighted average.
It must address the outgoing boundary and explain its effect on the cycle
controls. Merely computing more finite voltages, using domains built from
already enumerated histories, or restating component connectivity would
not meet that condition. This demotion concerns the present proposed test;
it is not an impossibility theorem for graph geometry.

**Verification scope:** the inverse-ray identities, tail comparison, five
arrows in (4), exact escape series and geometric probability bound are
direct arithmetic derivations. No large computation, extrapolation,
new external analytic theorem or change to the frozen mathematics was used.
