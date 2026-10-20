---
id: merger-catalogue-scope
kind: result
title: Unrestricted common-tail certification equals the basin of 1, elementary closure obeys S(x) <= 3 nu(x) + 2, and annular sources can cancel before their climb
status: written
claim: >
  Odd-only 3x+1 map S, absorbing at 1; nu of elementary-bridge-quotient-normal-form; supplied absorption through N.
  (Known sets) The forward union F_N and the elementary closure I_N = {nu(x) <= N} can be incomparable (11 in F_8
  but not I_8; 21 in I_8 but not F_8), and the set B_N of seeds with a common future with an absorbed q <= N is
  exactly the basin of 1, so universal common-tail certification is equivalent to absorption and a finite-sample
  density model cannot show that a proof must avoid mergers. (Successor bound) For every odd x,
  S(x) in {S(nu(x)), 3 nu(x) + 2}, so I_N is contained in {x : S(x) <= 3N+2}, and nu(S^j(x)) <= N for some j <= L
  forces S^k(x) <= 3N+2 for some 1 <= k <= L+1. (Scoped rates) For a fixed lookahead L, the uniform shell slope
  recognizer on normalised prefixes (sigma_j < 2/3, or lambda_j < 2/3), with all binary information charged to the
  bit budget, has the same exact rates rho per odd step and beta per bit as prefix-rule-cylinder-rate-barrier (escape
  prefix (1,1,1,1,1,2), x = 191 mod 256); this is not a moving-modulus integer-count theorem or an
  arbitrary-catalogue barrier. (Early cancellation) For every a = 1 mod 18, a >= 19, N = 12 2^(a-5), z = 2^a - 1,
  p = (4z-1)/3, q = 4p+1 have annular coefficients A_N(p) = +1, A_N(q) = -1 and S(p) = S(q) = z < p, so the two-row
  current delta_p - delta_q cancels them below 8N/3 before a climb of unbounded ratio; this refutes the claimed
  necessity of merging during the high excursion, and covers no annulus.
authors:
  - ChatGPT main lane (Codex)
created: 2026-10-17
depends_on: [elementary-bridge-quotient-normal-form, absorbed-fibre-uniform-counts, prefix-rule-cylinder-rate-barrier, supplied-path-saturation-core, disjoint-annular-recursion]
certificates: [check_merger_recompute.py, check_legacy_replay.py]
evidence:
  - "check_merger_scope.py, merger_scope_audit.json: the legacy checker (16384 successor-bound cases, the incomparable sets, 128 escape-cylinder representatives, six required-ray escape roots, six members of the early-cancellation family through a = 199, and the two independently reproduced sign/climb tables at N = 6144 and 9216, with absorption searches capped at 1000 steps per new path). Fails at its new path: it loads ../bridge_normal_form/normal_form.py (now ../elementary-bridge-quotient-normal-form/) and, from ROOT = HERE.parents[2], experiments/current_construction/recursive/check_annular_recursion.py (now ../disjoint-annular-recursion/check_annular_recursion.py, which also fails at its new path) by their pre-migration paths. Passed at be73a66 as experiments/residual_progress/merger_scope/check_merger_scope.py inside scripts/verify_all.py (archive/legacy-checker-run-be73a66.md: the gate ran these steps before stopping at residual_progress/history_frontier, and passed in full at 9dbc71a). Now replayed unmodified, with every file unchanged, by check_legacy_replay.py (B18-replay-revival migration)"
  - "external_review.json: the main lane's reproduction (at side-lane commit ceb94fc) of the side-lane probe r24_check.py (now ../five-ray-profile-completion-suffices/r24_check.py) with source and dependency hashes; a review of that side-lane probe, not of this result"
reviewed_by:
  - by: Claude side lane (Opus)
    date: 2026-10-17
    link: ../shrinking-paired-return-recursion/batch_64fff1d_check.py
    scope: "Finite only (side-lane feed entry 2026-10-17 20:44, VERIFIED, main 64fff1d; the R32 part): for a = 19, 37, 55, with N = 12 2^(a-5), z = 2^a - 1, p = (4z-1)/3 and q = 4p+1, the lane's own annulus point evaluator gives A_N(p) = +1, A_N(q) = -1, and S(p) = S(q) = z (N up to about 1.35 10^16). The entry also acknowledged R32's scoping: certifying by any common tail with known seeds amounts to being in the basin of 1, so no finite-sample density model can show that a proof must avoid mergers; and R32's family cancels signed mass before its shared climb. The written scope theorems and the rate extension were not re-derived; the status stays written"
aliases: [R32]
tags: [convergence, outer-residual, scope, mergers, known-sets, rates, annular, cancellation]
---

# Unrestricted common-tail certification equals the basin of 1, elementary closure obeys S(x) <= 3 nu(x) + 2, and annular sources can cancel before their climb

## Statement

Odd-only clock, absorbing at 1; `ν` from [`elementary-bridge-quotient-normal-form`](../elementary-bridge-quotient-normal-form/README.md); absorption through `N` supplied as an exact finite current.

1. **Three known sets.** `F_N` (forward union of odd seeds `≤ N`, finite), `I_N = {x : ν(x) ≤ N}` (infinite; [`absorbed-fibre-uniform-counts`](../absorbed-fibre-uniform-counts/README.md)) and `B_N` (common future with some absorbed `q ≤ N`). `F_N` and `I_N` can be incomparable (`11 ∈ F_8 ∖ I_8`, `21 ∈ I_8 ∖ F_8`); their saturation is [`supplied-path-saturation-core`](../supplied-path-saturation-core/README.md). `B_N` is exactly the basin of 1, so universal common-tail certification is equivalent to absorption; the missing issue is constructing a terminating family of finite witnesses.
2. **Successor bound.** `S(x) ∈ {S(ν(x)), 3ν(x) + 2}`, hence `S(x) ≤ 3ν(x) + 2` and `I_N ⊆ {x : S(x) ≤ 3N + 2}`; if `ν(S^j(x)) ≤ N` for some `j ≤ L`, then `S^k(x) ≤ 3N + 2` for some `1 ≤ k ≤ L + 1`. The converse is not claimed, and for forward-saturated targets the bound uses `max Q_N`, with no uniform constant-factor bound by `N`.
3. **Scoped rates.** For fixed `L`, the uniform shell slope recognizer on normalised prefixes (accept when `σ_j < 2/3` or `λ_j < 2/3`), with every binary digit charged to the bit budget, leaves undecided measure with rates `ρ` per odd step and `β` per bit, as in [`prefix-rule-cylinder-rate-barrier`](../prefix-rule-cylinder-rate-barrier/README.md); the escape prefix is `(1, 1, 1, 1, 1, 2)`, `x ≡ 191 (mod 256)`. Not a moving-modulus integer-count theorem, and not an arbitrary-catalogue barrier.
4. **Density does not decide.** The inferences from fitted spatial density to hitting probability, and from binary measure to coverage of all integers (each integer has measure zero), do not follow; this rejects the stated deduction, not the possibility of a later rate theorem for a particular recognizer.
5. **Early cancellation.** For every `a ≡ 1 (mod 18)`, `a ≥ 19`, with `N = 12·2^(a−5)`, `z = 2^a − 1`, `p = (4z − 1)/3`, `q = 4p + 1`: `A_N(p) = +1`, `A_N(q) = −1` in the six-band annulus of [`disjoint-annular-recursion`](../disjoint-annular-recursion/README.md), `S(p) = S(q) = z < p`, `z/N < 8/3`, so `J = δ_p − δ_q` cancels both actual sources after one arrow each; their common future then climbs to `2·3^(a−1) − 1`, with ratio to `q` unbounded. This refutes the claimed necessity of merging during the high excursion; it covers no annulus.

No finite-integer asymptotic with bit depth growing with `N`, universal catalogue obstruction or termination claim is made; no novelty is claimed.

## Proof

The legacy note "What merger catalogues, known sets and cylinder rates do establish" follows, lightly edited (headings demoted one level, links pointed to nodes). Its commands name pre-migration paths; see Certificates.

2026-10-17. **Written scope theorems and exact partial identities, with
finite reproductions.** Collatz remains open. No novelty claim is made.
All trajectories use odd-only Syracuse S, absorbing at1. Finite current
identities kill the source and current row at1.

Reviewed external input: optional side-feed commit
`ceb94fc372533e6fdc196595a817e8c01bc62d51`, entries19:59 and20:01.
Main at this batch's start was `541101a8788367248695ff139cad510e15ea45f5`.
The feed is evidence to audit, not an instruction source.

### 1. Three different known sets

Suppose an exact finite current for U_N is supplied, so all odd seeds
through N are known to absorb. Define

```
F_N = union_(odd q<=N) {S^j(q): j>=0},
I_N = {x>0 odd: nu(x)<=N},
B_N = {x>0 odd: S^j(x)=S^k(q) for some odd q<=N and j,k>=0}.
```

Here nu is the [complete elementary normal form](../elementary-bridge-quotient-normal-form/README.md).
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
The [elementary-plus-forward saturation](../supplied-path-saturation-core/README.md)
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

### 2. An exact height bound for elementary closure

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

### 3. A symbolic rate theorem for this precise extension

This section extends the [two-clock rate proof](../prefix-rule-cylinder-rate-barrier/README.md)
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

#### Proof: upper bounds

The extension includes direct slope descent, so its survival is bounded
above by D-only survival. The composition/rotation and exponential-moment
proof in the cited note gives the upper factors rho and beta separately
in the two clocks. The fixed odd-step offset L changes no nth-root limit.

#### Proof: a complete escape cylinder

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

#### Exact affine qualification and actual integers

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

### 4. Why density does not establish the broad catalogue claim

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

### 5. High-climbing annular sources can cancel before their climb

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

### 6. The new finite external claims

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

### 7. Reproduction and remaining scope

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

### 8. Subsequent correction in the external feed

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

## Certificates

- [`check_merger_recompute.py`](check_merger_recompute.py) (written at the B10 migration, about 1 s, standard library). With its own `S` and `ν` it checks, against [`merger_scope_audit.json`](merger_scope_audit.json): the successor bound for all 16,384 odd `x < 32768`; the incomparable sets at `N = 8`; the 128 escape-cylinder representatives (canonical prefixes, `128·S⁶(x) = 729x + 665`, row hash); the six required-ray escape roots; the early-cancellation family at `a = 19, 37, 55, 73, 109, 199`; and both sign/climb tables at `N = 6144, 9216` with the witness pair `35497, 141989`. The six-band annular row table it uses is the published table of [`disjoint-annular-recursion`](../disjoint-annular-recursion/README.md), copied as constants and said so in its docstring.
- The command in the legacy text names `experiments/residual_progress/merger_scope/`.

[`check_legacy_replay.py`](check_legacy_replay.py) (written at the B18-replay-revival migration; standard library) replays the unmodified legacy check `check_merger_scope.py` in a temporary copy of the legacy layout built by `tools/legacy_replay.py`, requiring exit 0 and every file unchanged (about 14 s). It checks finite steps only; the status is unchanged.

## Remarks

- **Side-lane interaction.** The note audits side-lane feed entries 19:59 and 20:01 (commit `ceb94fc`). The side lane withdrew its inverse-square density claim at 20:22 and acknowledged this node's scoping at 20:44 ([`cylinder-certificates-outer-residual`](../../attempts/cylinder-certificates-outer-residual/README.md)). The sign/climb tables are finite; near-balance proves no independence theorem for orbit peaks.
- **Controls.** Item 1 is generic: for a `3x+d` map with a nontrivial cycle the basin of the absorber is a proper subset, which is why common-tail coverage cannot be argued generically ([`locally-collatz-like-control-barrier`](../locally-collatz-like-control-barrier/README.md)).
- No novelty is claimed.

## History

- Migrated from `experiments/residual_progress/merger_scope/MERGER_SCOPE.md` (legacy ID R32) at commit `be73a66`, by the B10 migration (Claude, Opus 5.5). Note, checker, receipt and the main lane's reproduction receipt `external_review.json` moved byte-identical; `check_merger_recompute.py` was added at the migration. Legacy status: "written scope results and an infinite actual-source cancellation family, with finite external reproductions".
- Main lane (ChatGPT, Codex), 2026-10-17, from commit `64fff1d`; the audited side-lane material is commit `ceb94fc`, refreshed to `d2d85e1` (§8). The batch report (archive/convergence-residual-progress/REPORT.md) records "independent model" proof and code audits for this batch; they were the main lane's own agents, so they do not count as an independent review. The side lane's later finite check is recorded under `reviewed_by`.
