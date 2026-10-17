# Finite currents: exact component criteria and a bounded-template obstruction

Written proof, 17 October 2026. These elementary arguments have not been
human-reviewed or formally verified. No novelty claim is made. No universal
Collatz constructor is proved.

## 1. The distinction between current existence and bounded work

Let `X` be a set with deterministic map `S` and an absorbing state `o`.
Measures have finite support in `X \ {o}`, and `P` pushes along `S` while
discarding mass at `o`. Currents are finite signed measures with divergence
`(I-P)J`. Coefficients may be real; integer source coefficients admit integer
constructions below.

Two states belong to the same **orbit component** if
`S^a(x)=S^b(y)` for some nonnegative integers `a,b`. This is an equivalence
relation: transitivity follows by advancing both identified orbit segments
until their shared middle orbit has reached both meeting times. Equivalently,
these are the connected components after ignoring arrow directions. There is
one absorbing component, consisting of states that reach `o`; the others
are nonabsorbing components. Every finite subset of one component has a
common forward descendant, with possibly different arrival times.

For a finite measure `mu`, write `m_C = sum_(x in C) mu(x)`.

**Theorem 1.**

1. A finite exact current `mu=(I-P)J` exists if and only if `m_C=0` for
   every nonabsorbing orbit component `C`.
2. A finite signed current and nonpositive finite residual
   `mu=(I-P)J+zeta`, `zeta<=0`, exist if and only if `m_C<=0` for every
   nonabsorbing orbit component `C`.

**Proof.** The component indicator `1_C` is invariant under `S` for every
nonabsorbing component. Pairing a finite divergence with this indicator gives
zero. Pairing the residual gives a nonpositive number. These are the necessary
conditions.

For sufficiency, only finitely many components meet the support of `mu`.
In an absorbing component, follow each source to `o`. In each other component,
choose a common descendant `z_C` and finite paths from every source to it.
A source of weight `c` contributes current `c` along its path, whose divergence
is `c(delta_x-delta_(z_C))`. Summing gives

`mu = (I-P)J + sum_C m_C delta_(z_C)`.

The sum is over the finitely many nonabsorbing source components. It vanishes
under condition 1 and is nonpositive under condition 2. All paths are finite,
so the resulting current is finite. The argument is an existence proof;
it does not provide a decidable component-membership oracle. QED.

Let `tau` be the hitting time of `o`, `h_L=min(L,tau)`, and
`H_L(mu)=sum_x mu(x)h_L(x)`. For all `L` beyond the largest finite hitting
time among the finitely many sources,

`H_L(mu) = L sum_(C nonabsorbing) m_C + sum_(tau(x)<infinity) mu(x)tau(x)`.

Consequently `sup_L H_L(mu)<infinity` holds if and only if the **sum** of
nonabsorbing component masses is nonpositive. That is weaker than requiring
each individual mass to be nonpositive. The fixed-measure implications must
not be confused with the repository's equivalence after quantifying over
**every** right-packet cutoff.

There is a concrete arithmetic example outside the positive-integer domain.
Extend the odd Syracuse formula to negative odd integers, retaining absorption
only at positive `1`. The cycles are `-1 -> -1` and `-5 -> -7 -> -5`.
For `mu=delta_(-1)-delta_(-5)`, `H_L(mu)=0` at every horizon, but the
`{-1}` component has mass `+1`. Hence neither type of current exists.
This is a negative-integer example, not a claimed counterexample on positive
Collatz states.

## 2. A complete search when a certificate exists

For each depth `d=0,1,2,...`, expose the first `d` forward arrows from every
source, retaining previously visited states. Compute connected components of
this finite graph with arrow directions ignored. If every component that
does not contain `o` has source mass zero, an exact certificate can be formed.
If all those masses are nonpositive, a one-sided certificate can be formed.

To construct it, choose one anchor per finite component (`o` when available),
choose an undirected spanning tree, and route each source's coefficient to
that anchor. Traversing an original arrow backwards gives a negative current
on that arrow. The divergence of a routed source is exactly its source mass
minus its anchor mass. The residual is the component mass at its anchor.

Every reported success is a finite, checkable certificate. If a certificate
of either type exists, Theorem 1 supplies finitely many paths that connect
each required source component, or connect it to `o`. At a sufficiently large
finite depth those paths have been exposed, so the corresponding search
succeeds. Thus the search is a **semidecision procedure complete for current
existence**. A depth cap returns unresolved, never nonexistence.

This also explains why synchronous transport alone is incomplete for this
purpose. On the nonabsorbing ray `S(n)=n+1`,
`delta_2-delta_3=(I-P)delta_2`, but `P^d(delta_2-delta_3)` is nonzero at every
depth. Recording historical intersections finds the unequal-time cancellation.

For the entire right-aligned family, proving that this complete semidecision
search always terminates remains equivalent to proving the repository's
universal current criterion. Completeness removes an algorithmic deficiency;
it does not prove the missing universal existence hypothesis.

## 3. No bounded-size current catalogue for individual actual packets

The conclusion here concerns **individual triples**, even though those triples
occur in the actual right-aligned family. It does not exclude cancellations
across different triples in the aggregated measure `Pi_right_N`.

**Theorem 2.** For every integer `H>=0`, let

`K=2H+7`, `y=9*2^K-1`, and `N=4*2^K+5`.

The measure

`mu_y=2 delta_y-delta_(y+6)-delta_(y+12)`

is the last valuation-1 triple in source component 1 at cutoff `N`, under
the repository's right-aligned construction. Any finite exact current for
`mu_y`, or any finite current with everywhere nonpositive residual for it,
has strictly more than `H` nonzero rows.

**Proof of packet membership.** For valuation `a=1`, source and endpoint
lifts are `x_t=3+4t`, `y_t=5+6t`, with `t>=0`. Put
`t=3*2^(K-1)-1`, so `y_t=y` and `t=2 mod 3`. The component-1 cutoff is

`n1=floor((3N+1)/2)=6*2^K+8`.

Its final lift is `t+2`, since its source is `6*2^K+7`, while the next
source exceeds `n1`. There are `t+3=3*2^(K-1)+2` lifts. Right alignment
therefore leaves the first two and groups the rest into triples beginning at
indices `2 mod 3`. The three source residues modulo 3 are `2,0,1`, giving
the coefficients `2,-1,-1` claimed.

**Proof of delayed separation.** Consider first the integer base orbits
starting at `-1`, `5`, and `11`. Their exact valuations and states are

```
-1 -> -1 -> -1 -> ...      valuations 1,1,1,...
 5 ->  1 ->  1 -> ...      valuations 4,2,2,...
11 -> 17 -> 13 -> 5 -> 1   valuations 1,2,3,4, then 2,2,...
```

The last display uses the ordinary formula at 1, which fixes 1; the actual
positive perturbations below never equal 1 within the window. For each base
orbit let `z_j` be its state and `A_j` its accumulated valuation. For
`0<=j<=H`, each `A_j<=2H+2`. Exact branch arithmetic therefore gives

`S^j(z_0+9*2^K)=z_j+9*3^j*2^(K-A_j)`.

This follows by induction: before each division the perturbation is divisible
by at least one more power of 2 than the base numerator's exact valuation.
The displayed bound in fact leaves at least five bits at every state.

All the first `H+1` states of `y` are thus `-1=31 mod 32`. The states
from `y+6` and `y+12` have residues in `{1,5,11,13,17}` modulo 32. There
is no equality between these orbit segments, and the segment from `y` does
not reach the absorber 1.

**Proof that separation bounds certificate size.** Suppose `J` had at most
`H` nonzero rows. Form the finite undirected graph consisting of its nonzero
arrows, including their endpoints and the absorber if reached. Let `D` be
the component containing `y`. If `D` contains neither of the two negative
sources nor the absorber, summing the identity over `D` gives

`2=sum_D mu_y=sum_D zeta<=0`,

an impossibility (with `zeta=0` for the exact case). Consequently `D` has
an undirected path from `y` to a negative source or to the absorber. The path
has at most `H` edges. In a deterministic graph, any undirected simple path
has its arrows directed toward a single meeting vertex: two arrows pointing
away from an interior vertex would violate outdegree at most one. Its two
endpoints therefore meet under forward iteration with each arrival time at
most `H`; when one endpoint is the absorber, the other reaches it within
`H` steps. This contradicts the separation just established. QED.

In particular, a finite catalogue of per-triple current templates whose
expansions each have a uniformly bounded number of rows cannot certify every
actual right packet. Recursive templates with unbounded expansion, templates
using cancellations across packets, and constructions with unrestricted
certificate size are not excluded. The logarithmic lower bound here is small
relative to the arbitrary per-cutoff cost permitted by the qualitative
criterion; its purpose is to rule out an overly narrow local search strategy.

## 4. A useful local identity remains valid

For every integer `t>=0`, set `x=69+256t`. The first two Syracuse iterates are

`S^2(x)=5+18t`, and `S^2(x+6)=85+288t=16 S^2(x)+5`.

Because `3(16u+5)+1=16(3u+1)`, their odd parts agree, so
`S^3(x)=S^3(x+6)`. This yields an exact current for
`delta_x-delta_(x+6)` using at most six rows. The valuation of the third
step need not be bounded or fixed on the whole cylinder. This example and
Theorem 2 are compatible: the single residue cylinder is useful, but a
bounded-size per-packet catalogue cannot cover all packets.

## Reproducibility

Run:

```sh
python3 experiments/current_construction/obstructions/verify_obstructions.py
```

The script checks the finite-graph constructor on every deterministic map
on three nonabsorbing vertices and every source measure with coefficients
in `{-1,0,1}`; verifies the negative-cycle and unequal-time examples; checks
the delayed-separation formulas at selected depths; verifies actual packet
membership arithmetically without materializing the huge cutoff; and checks
the local coalescence identity on a finite range. Finite checks support the
implementations. The universal statements above rely on the written proofs.

Actual checks on 17 October 2026: the command above passed all 1,728 finite
map/measure cases in both certificate modes, the 10,000 coalescence parameters
`0..9999`, and obstruction depths `0,1,2,4,8,16,32,64,128`. The persisted
receipt is `audit.json` in this directory. The repository command
`python3 scripts/verify_all.py --cpp` also passed: archive and 31 manifest
entries, both stored Python certificates, the unchanged right-aligned receipt,
and independent C++ checks at cutoffs 4096 and 262144.
