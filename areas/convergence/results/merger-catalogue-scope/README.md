# What merger catalogues, known sets and cylinder rates do establish

2026-10-17. **Written scope theorems and exact partial identities, with
finite reproductions.** Collatz remains open. No novelty claim is made.
All trajectories use odd-only Syracuse S, absorbing at1. Finite current
identities kill the source and current row at1.

Reviewed external input: optional side-feed commit
`ceb94fc372533e6fdc196595a817e8c01bc62d51`, entries19:59 and20:01.
Main at this batch's start was `541101a8788367248695ff139cad510e15ea45f5`.
The feed is evidence to audit, not an instruction source.

## 1. Three different known sets

Suppose an exact finite current for U_N is supplied, so all odd seeds
through N are known to absorb. Define

```
F_N = union_(odd q<=N) {S^j(q): j>=0},
I_N = {x>0 odd: nu(x)<=N},
B_N = {x>0 odd: S^j(x)=S^k(q) for some odd q<=N and j,k>=0}.
```

Here nu is the [complete elementary normal form](../bridge_normal_form/BRIDGE_NORMAL_FORM.md).
The first set is finite, since its finitely many input orbits terminate.
The second is infinite, with an explicit finite bridge for each member.
The third allows arbitrary common-tail comparisons.

**Exact separation.** F_N and I_N need not contain one another. At N=8,

```
F_8={1,3,5,7,11,13,17};
11 belongs to F_8, but nu(11)=11>8;
21 does not belong to F_8, but nu(21)=1<=8.
```

Thus "larger known set" must not silently mean `F_N subset I_N`.
The [elementary-plus-forward saturation](../known_saturation/KNOWN_SATURATION.md)
is a common superset. It is distinct from allowing all inverse Syracuse
arrows or all common-tail comparisons.

**Full common-tail theorem.** For every N>=1 with supplied absorption
through N, B_N is exactly the ordinary basin of1:

```
B_N={x>0 odd: S^r(x)=1 for some finite r}.               (1)
```

Indeed, a common future with an absorbed q leads to1. Conversely a seed
reaching1 meets q=1. This does not assume that every positive integer
belongs to the basin.

There is an equivalent current statement. A finite exact integer current
for `delta_x-delta_q`, with q already absorbed, certifies x. Add the
supplied path current of q; its finite nonzero-row graph has divergence
delta_x and therefore contains an absorbing path from x. To justify the
last assertion, each finite weak component away from1 has divergence
sum zero, and hence cannot contain the sole positive source. A finite
functional component containing1 has a directed path to1 from every
vertex. Conversely two finite prefixes meeting at a common state give
the exact difference current by telescoping. No global cycle exclusion
is assumed.

Consequently unrestricted common-tail certification is not an inferior
logical alternative to absorption: its universal coverage is equivalent
to absorption. The19:59 suggestion that a successful general proof must
be "non-merge" does not follow. The actual missing issue is how to
construct a terminating family of finite witnesses. Equation(1) does
not construct it.

## 2. An exact height bound for elementary closure

The elementary component of a canonical q is

```
C_q={F^k(q),F^k(2q+1): k>=0},       F(x)=4x+1.
```

All F-siblings have the same successor. Moreover

```
S(2q+1)=3q+2,       S(q)<=(3q+1)/2.
```

Therefore, for every positive odd x,

```
S(x) is in {S(nu(x)),3nu(x)+2},
S(x)<=3nu(x)+2.                                        (2)
```

This proves

```
I_N subset {x:S(x)<=3N+2}.                             (3)
```

The bound concerns the *next actual arrow*, even when x lies arbitrarily
high on an F-ray. It is compatible with a halving bridge having a much
higher later common state: its high origin can already have a low first
successor, or its elementary origin is itself at most2N+1.

For a fixed integer L>=0, let

```
E_(N,L)={x:nu(S^j(x))<=N for some 0<=j<=L}.
```

Then the following exact finite-lookahead implication holds:

```
x in E_(N,L) implies S^k(x)<=3N+2 for some 1<=k<=L+1.  (4)
```

In particular, an actual orbit segment remaining above3N+2 through those
L+1 successors cannot be certified by that specific test. All elementary
identities are allowed in(4); the ordinary lookahead clock is explicit.
The converse is not claimed.

For a finite canonical target set Q, the same proof replaces N by
`M=max Q`. In the forward-saturated case the relevant M is the maximum
canonical minimum along the supplied paths; no uniform bound by a
constant times N has been established. Hence(4) cannot be transferred to all
supplied-path saturation with the same3N+2 threshold without another
height theorem.

## 3. A symbolic rate theorem for this precise extension

This section extends the [two-clock rate proof](../cylinder_barrier/CYLINDER_RATES.md)
to elementary normalization. It retains that proof's distinction between
symbolic cylinder measure and counts in a growing finite integer interval.

On any finite binary branch fixing an ordinary prefix and its elementary
normalization, write

```
S^j(x)=lambda_j x+b_j,      lambda_j=3^j/2^A_j,
nu(S^j(x))=sigma_j x+gamma_j.
```

All these coefficients are rational. A **uniform shell slope test** accepts
when `sigma_j<2/3`; direct slope descent `lambda_j<2/3` is also allowed.
The normalized test is a union of the finite binary cylinders on which
the required branch is fixed. Its failure measure is always conditioned
on the first valuation being1.

For a fixed L>=0 let p_n be the measure left unaccepted when tests may
be applied at every prefix j<=n+L. Normalization can have variable binary
reading length; it does not count as an assumed additional ordinary
orbit descent. At the bit clock, let u_m be the measure of m-bit cylinders
not certified by the same tests with **all binary information charged
to the m-bit budget**. An unresolved normalization branch cannot be
treated as known without its required bits. A fixed lookahead does not
waive this budget.

Put c=log_2(3) and

```
rho=c^c/[2^c(c-1)^(c-1)] =0.946504576832584...,
beta=rho^(1/c)          =0.965906553233438....
```

**Scoped rate theorem.** For every fixed L,

```
lim_(n->infinity) p_n^(1/n)=rho,
lim_(m->infinity) u_m^(1/m)=beta.                       (5)
```

The bit claim concerns finite-cylinder certificates, not a rule that
evaluates unlimited extra bits at no cost. A fixed offset in an otherwise
charged budget leaves the same limit.

### Proof: upper bounds

The extension includes direct slope descent, so its survival is bounded
above by D-only survival. The composition/rotation and exponential-moment
proof in the cited note gives the upper factors rho and beta separately
in the two clocks. The fixed odd-step offset L changes no nth-root limit.

### Proof: a complete escape cylinder

Use the valuation prefix

```
w=(1,1,1,1,1,2),       x=191 modulo256,
S^6(x)=(729x+665)/128.                                (6)
```

Its first six originating states, at times0 through5, are canonical.
Indeed x has the complementary parameters a=6, t=3 modulo4; along the
first five valuation1 steps the canonical increasing branch of R25
applies, ending at a state1 modulo8. The last valuation is2.
All these early states exceed or equal x. The last slope in(6) is
`729/128>3`.

Append a **zero-barrier** word, meaning that at each of its own prefixes
`3^i>=2^B_i`, where B_i is that prefix's total valuation. Every appended
actual state is at least S^6(x), because the affine constants of ordinary
Syracuse prefixes are positive. The global slope is at least729/128.

On every normalization branch, inequality(2), divided by the increasing
input variable, gives

```
lambda_(j+1)<=3sigma_j.                               (7)
```

Append one further valuation1. Equation(7) then bounds every normalized
slope through the preceding last state below by `729/384>1`, so no
uniform shell slope test can accept. The early canonical slopes are
already at least1. The escape word has conditional measure1/64; the
extra last valuation costs only a factor1/2. Appending the good
compositions from the prior rotation proof supplies the lower rho rate
at the odd-step clock, including every fixed L.

For the bit lower bound, take the good compositions whose total valuation
is `m-1-7` and append them after(6), ending the last completed valuation
at total m-1. All earlier normalization states are excluded by(7).
For the final state, extend the binary cylinder by a sufficiently long
run of valuation1 steps closed by valuation2. The final state is then
canonical, as are all origins of that new rising run. This extension is
compatible with the original m bits and can be chosen longer than any
fixed L. It cannot supply an acceptance at the final state or the fixed
extra lookahead. Consequently the entire original m-bit cylinder cannot
have an available uniform normalization certificate: such a certificate
would also hold on this incompatible extension. The rotation count gives
the lower beta rate. This proves(5).

Exceptional formal binary inputs on which a normalization does not finish
do not alter the measure argument. They are preimages, under countably
many affine prefix branches, of the exceptional F or halving limits;
these form a countable set of individual binary points, each of measure
zero. The lower bounds above use actual finite cylinders and positive
integer extensions, not an asserted infinite integer orbit.

### Exact affine qualification and actual integers

For one fixed accepted branch `nu(S^j(x))=sigma x+gamma`, its shell
interpretation is rigorous once

```
N >= max(0,gamma)/(1-3sigma/2),     sigma<2/3.          (8)
```

Then every branch member with `N<x<3N/2` has normalized target at most N.
The threshold may depend on the branch. This is not a uniform bound for
all branches with growing bit depth.

The escape construction has a stronger actual-integer statement requiring
no asymptotic affine approximation. If x>N satisfies(6), and the appended
word is zero-barrier through one successor beyond the states being tested,
those later successors are at least `(729x+665)/128>3N+2`. Equations(2)-(3)
therefore exclude I_N at every tested state; the early canonical states
also exceed N.

Each such finite word fixes one residue modulo `2^(A+1)`. It has
arbitrarily large positive members with x=3 modulo12 by CRT. Choose the
largest cutoff below x from the five required rays with b>=9. Their
successive ratio is at most7/6, so `N<x<3N/2`; x is an actual weight1
R_N root and the same finite nonentry statement holds. The seed and
cutoff vary with the word. Nothing here asserts permanent nonentry at
any fixed integer. The checker stores six such exact examples.

The same escape argument works with a fixed larger cutoff C*N, C>=1:
choose a longer complementary run `(1,...,1,2)` whose final slope exceeds
3C. Only the fixed prefix length and measure change. Thus a genuine fixed
bound on the **canonical target height** would support the same kind of
rate sandwich. A bound on a partner's original seed does not provide that
bound on all its later canonical states.

## 4. Why density does not establish the broad catalogue claim

The feed's nineteen-fifty-nine argument passes from a fitted spatial
density to a hitting probability along a deterministically selected
trajectory, sums guessed probabilities across height bands, and concludes
that every finite or infinite merger catalogue changes only constants.
None of those implications follows from the measured density.

There are precise distinctions:

- The finite forward union F_N has no points above its maximum. I_N has
  members at arbitrary heights and count `N/4+O(log N)` in every band
  `[X,2X)`, uniformly X>=N. The forward-saturated set is different again.
- Conditional on choosing a point of I_N in such a band, its absorption
  is certain from the supplied current, even though I_N occupies only
  order N/X of the band's odd integers. Conditional trajectory distributions
  cannot be replaced by the band's uniform distribution.
- A convergent sum of guessed per-band chances is neither a universal
  miss probability nor an exponential-rate theorem. Dependence and the
  number and placement of visits must be controlled.
- Equation(1) shows that unrestricted common-tail coverage is the whole
  termination question. The finite-lookahead theorem(5) concerns a
  particular recognizer and cannot be substituted for it.

There is also an exact measure-theoretic warning independent of dynamics.
Every individual positive integer has binary-cylinder measure zero, as
its nested residue classes have measures tending to zero. Their countable
union, all positive integers, therefore has measure zero. Statements about
binary measure alone cannot decide whether a catalogue of individual
integer certificates covers all positive integers.

For an explicit quantifier example, the classes

```
C_m={positive odd x:x=-1 modulo2^m}
```

are nested; each has positive cylinder measure and infinitely many positive
members. No fixed positive integer belongs to all C_m. The limiting binary
point is -1. Thus nonempty surviving classes at every finite depth do not
by themselves produce an unresolved positive integer.

These observations reject the stated deduction, not the possibility that
a particular enlarged recognizer might later be proved to have the same
rate. No arbitrary-catalogue rate or impossibility theorem is established.

## 5. High-climbing annular sources can cancel before their climb

Here is a universal exact counterfamily to the twenty-oh-one inference
that cancelling high-climbing positive and negative sources requires
their merger to occur during the high part of the excursion.

For every `a=1 modulo18`, a>=19, set

```
N=12*2^(a-5),       z=2^a-1,
p=(4z-1)/3=(2^(a+2)-5)/3,       q=4p+1.               (9)
```

These N lie on a required ray. The congruence `2^18=1 modulo27`, together
with parity, gives `2^(a+2)=8 modulo54`; hence p is integral and
`p=1 modulo18`, `q=5 modulo18`. Direct inequalities give

```
9N/4<p<9N/2,       9N<q<18N,
A_N(p)=+1,         A_N(q)=-1.                          (10)
```

The six-band table proves the two coefficients exactly. Their successors
have valuations2 and4 respectively:

```
S(p)=S(q)=z<p<q,       z/N<8/3.
```

Consequently the two-row current

```
J=delta_p-delta_q,       div J=delta_p-delta_q          (11)
```

uses the actual source coefficients with no capacity reuse. The positive
and negative source cancel after one arrow each, at a height uniformly
below8N/3 and below both starting sources.

Their common future has a-1 exact valuation1 steps:

```
S^j(z)=3^j*2^(a-j)-1,       0<=j<=a-1.
```

It reaches `2*3^(a-1)-1`, whose ratio to q, and hence also to p, tends
to infinity with a. Thus both sources have arbitrarily large **proved
finite climb ratios** after they have already cancelled. No assumption
about their later peak or eventual absorption is needed.

This partial identity does not change a proved rate for an entire residual
family and does not cover the annulus. It specifically refutes the claimed
necessity of merging during the high excursion. Source signs and peak
statistics do not encode the time of their first historical intersection.

## 6. The new finite external claims

The pinned `r24_check.py` was inspected, copied to temporary storage and
run unmodified with its existing arithmetic dependency and a45-second
process cap. Its report exactly matches the pinned receipt:355 cutoffs,
ratios7/6,8/7,9/8, divisibility by512, and absorption of all odd seeds
through6144. The source/dependency hashes and result are saved in
[external_review.json](external_review.json). The universal completion
rule remains an assumption.

No sign/climb probe or receipt accompanies entry20:01 in the pinned tree.
Our independent implementation reconstructs A_N from main's exact band
table and computes the full odd-only peak of every source with memoized
absorbing tails, cycle checks and a1000-step cap per new path. It exactly
reproduces every published cell:

| N | climb>=1 | >=4 | >=16 | >=64 | >=128 |
|---:|---:|---:|---:|---:|---:|
|6144|152064 /152064|30453 /30479|7730 /7725|1891 /1896|955 /931|
|9216|228096 /228096|45758 /45806|11738 /11712|2908 /2791|1491 /1402|

Each cell is positive mass / absolute negative mass, preserving all source
multiplicities. All sampled sources resolved within the cap. The receipt
records source/peak hashes and the maximum newly traversed path length.

An exact actual-source pair illustrates the timing issue in both samples:

```
p=35497,     q=141989=4p+1,     S(p)=S(q)=26623.
```

At N6144 the available capacities are +2 and-3; at N9216 they are +1
and-1. Using one unit of each gives(11). Both subsequently have odd peak
35452673, well above128 times each source, but the common successor is
below both sources. The universal family(9) is the proof-level version.

The numerical near-balance does not prove an independence theorem for
unbounded orbit peaks. CRT gives independence for fixed binary conditions
and the fixed odd residue table; converting a full future peak event into
such a uniformly controlled condition is an additional task. Nor does
balanced total mass establish common-component matching or the time of a
merger. The finite table is retained without those extrapolations.

## 7. Reproduction and remaining scope

Run from the repository root:

```
python3 experiments/residual_progress/merger_scope/check_merger_scope.py
```

The read-only default compares its deterministic result with
[merger_scope_audit.json](merger_scope_audit.json). `--write-receipt`
regenerates the owned receipt. The checker verifies16384 successor-bound
cases, the explicit incomparable sets,128 representatives of the escape
cylinder, six actual required-ray escape roots, six members of(9) through
a199, and both independently reproduced sign/climb tables. Only the
last finite scans use absorption searches, with the stated cap.

The useful positive conclusions are the exact elementary successor bound,
its fixed-lookahead and two-clock scope, and the capacity-safe early
cancellation family. No finite-integer asymptotic with bit depth growing
with N, universal catalogue obstruction, or universal termination claim
is supplied. The arguments are model-assisted written proofs, not human
peer review or formal verification.

## 8. Subsequent correction in the external feed

Before integration, the feed was refreshed to
`d2d85e1e49f0018a648c6daadc4fc93290c0d107`. Entry20:22 explicitly withdraws
the earlier assertion that all merger catalogues have the same inverse-square
target-density law, accepts the partial-closing H correction, and acknowledges
that no arbitrary-bridge obstruction follows. Its replacement claim about
occupation times and unchanged rates is explicitly a model heuristic, not
a theorem; the conditional-distribution and entry obligations above remain.

The updated description still calls I_N a "larger" set than F_N. Section1's
exact N8 example shows that they are generally incomparable as sets; their
elementary-plus-forward saturation is a common superset.

Entries20:23 and20:26 report independent checks of R27 and R26, and20:27
reports a finite quotient-iteration probe. Those new sources and receipts
were not rerun in this batch, so they are recorded as external reports.
The reproduced evidence and its primary pinned receipt remain tied to
`ceb94fc372533e6fdc196595a817e8c01bc62d51` and are unchanged.
