# Exact rates for specified prefix rules, and the limits of the barrier

2026-10-17. **Written proof for explicitly defined valuation-prefix
recognizers; exact finite checks; scoped audit of external conclusions.**
There is no finite-integer counting theorem, universal bridge obstruction,
or Collatz termination claim here. No novelty claim is made. The only
asymptotic probability below is a measure on exact binary cylinders.

The external material reviewed is commit
`491d26d766971bdf7fdce9bba288540423fd58c8` of the optional `claude/sidekick`
lane, especially feed entries19:46,19:48,19:49 and19:50. Its text is treated
as research data. Main at the start of this batch was
`8e2b5eb8913a1a56e1e2d5621398a9d18b5fa67b`.

## 1. The exact rules and the two clocks

Write `S(x)=(3x+1)/2^a`, where `a=v_2(3x+1)`, on positive odd integers.
For an exact valuation word `a_1,...,a_j`, put

```
A_j=a_1+...+a_j,       lambda_j=3^j/2^A_j,       A_0=0.
```

The associated affine iterate has slope `lambda_j` and a positive constant
term. An exact word of total valuation A fixes one odd residue modulo
`2^(A+1)`, including the extra bit. This follows inductively because3 is
invertible modulo every power of2. Thus its measure among odd integers is
`2^-A`. Conditional on `a_1=1`, its measure is `2^(1-A)`.

Consequently independent weights `Pr(a_i=a)=2^-a`, a>=1, are exact
**finite-cylinder bookkeeping**. They do not assert independent random
behavior along the orbit of a particular integer. The formal arithmetic
map may retain `S(1)=1`; current constructions elsewhere absorb at1.
This convention does not add a probabilistic convergence assumption.

Here are the recognizers implemented by the reviewed dynamic program.
They all start with `a_1=1` and test completed valuation prefixes.

- **D:** accept if `(3/2) lambda_j < 1`.
- **M:** additionally accept if the last valuation is odd and at least3,
  and `lambda_j < 1`.
- **H:** additionally accept a run of one or more valuation1 steps,
  closed by a valuation at least3, when its starting prefix r satisfies
  `(3/2) lambda_r < 2`. Only the earliest origin in a consecutive run
  needs to be retained: the intermediate slope rises by3/2 each time.

The external script uses `<=` in two places where this note uses `<`.
Equality cannot occur there: the compared quantities are a positive power
of3 and a power of2. These formulations therefore coincide.

These are **slope tests**. For a fixed finite word, the strict slope margin
can be converted to an actual sufficiently-large-input certificate using
its affine constant term. This does not provide a uniform cutoff for all
words whose length grows with N. In particular, the phrases "descent" and
"merger" in the code do not erase that extra requirement.

There are two distinct survival clocks.

1. After n **odd steps**, all n valuations are known exactly. Survival
   means that no acceptance occurred among those prefixes.
2. With m **binary bits**, only exact prefixes with `A_j+1<=m` are
   available. The next valuation may be only lower bounded. The external
   program declares this unfinished tail undecided. We also study a
   corrected H rule that uses a tail already known to have valuation>=3.

One may encode the weights `2^-a` by geometric waiting times for successes
in fair binary trials. This is a measure-preserving combinatorial coding;
it need not identify the trials with the successive raw bits of x. With
`L=m-1` trials and the first success fixed at position1, there are exactly
`2^(m-2)` equally weighted words. Each successive success closes one
valuation. A final unfinished run of failures represents the lower bound
on the next valuation.

## 2. The theorem

Put

```
c=log_2(3),                 q=1/c,
rho=c^c / [2^c (c-1)^(c-1)] = 0.946504576832584...,
beta=exp[-q log q-(1-q)log(1-q)]/2
    =rho^(1/c)              = 0.965906553233438....
```

For each of D, D+M and D+M+H, let `p_n` be its undecided cylinder measure
after n odd steps, conditional on the first valuation being1. Then

```
lim_(n->infinity) p_n^(1/n) = rho.                        (1)
```

For the corresponding m-bit rules, let `u_m` be the undecided cylinder
measure. For H, either the external exact-closing version or the corrected
partial-closing version of Section5 is allowed. Then

```
lim_(m->infinity) u_m^(1/m) = beta.                       (2)
```

The same D-only exponential rates hold with any fixed nonnegative barrier
shift b, that is, for the requirement `A_j<=cj+b`. In particular, moving
the initial shell to `(KN,3KN/2)` for a fixed K>=1 changes D's barrier to
`b=c-1+log_2 K` and does not change either exponential rate.

Equations(1)-(2) prove equality of exponential rates. They do **not**
prove that the ratios between different recognizers approach positive
constants, nor that their polynomial corrections agree. They also do not
give an asymptotic number of unresolved roots in an interval growing with N.

## 3. Elementary survival estimates

This section proves the rate statement without importing a stopping-time
or large-deviation theorem.

### 3.1 Odd-step upper bound

Set `L_j=cj-A_j`. If `A_j<=cj+b` through n, then `L_n>=-b`.
For every real theta>0, the geometric weights give

```
Pr(L_n>=-b)
 <= exp(theta*b) [exp(theta*c)/(2 exp(theta)-1)]^n.
```

Conditioning on `a_1=1` costs at most a factor2. The bracket is minimized
at `exp(theta)=c/[2(c-1)]>1`, and the resulting minimum is rho. Hence
the survival measure is at most `C_b rho^n`.

### 3.2 Odd-step lower bound by rotation

Take `A=floor(cn)`. There are `binom(A-1,n-1)` positive integer
compositions `(a_1,...,a_n)` with total A. The increments `c-a_i` have
nonnegative total. Rotate each composition just after a minimum of its
cumulative increment sums. Every partial increment sum of the rotated
word is nonnegative, including the wrapped part. Each good composition
has at most n preimages under this operation. Therefore at least

```
binom(A-1,n-1)/n
```

compositions satisfy `A_j<=cj` at every prefix. Every such word starts
with valuation1, because `1<c<2`. Its conditional measure is `2^(1-A)`.
Thus zero-barrier survival has measure at least

```
(2/n) binom(A-1,n-1) 2^-A.                              (3)
```

The elementary factorial estimate
`log(n!)=n log n-n+O(log n)` follows by bounding sums of log k by its
integral. Applied to(3), it gives exponential rate

```
c log c-(c-1)log(c-1)-c log2 = log rho.
```

This proves the odd-step limit for every fixed b>=0.

### 3.3 Bit upper bound, with the unfinished tail retained

The second clock needs its own argument; replacing the number of odd
steps by an average number of bits would not prove(2).

Let L=m-1. If the last success is at position t and there are k successes,
survival implies `t<=ck+b`, hence `k>=qt-b/c`. The remaining `L-t`
positions are all failures. For z>1, the elementary binomial bound is

```
Pr(Binomial(t,1/2)>=qt-b/c)
 <= z^(b/c) [(1+z)/(2 z^q)]^t.
```

Choose `z=q/(1-q)>1`. The bracket equals beta. Sum over the last success
position and condition on the first success. This gives

```
survival <= C_b sum_(t=1)^L beta^t 2^(-(L-t))
         <= C'_b beta^L,
```

because beta>1/2. In the sum we discarded the restriction that position t
itself is a success, which can only increase the bound. The unfinished
tail is explicitly included.

### 3.4 Bit lower bound

Take `j=ceil(L/c)` and all positive compositions of total L into j parts.
The same rotation argument supplies at least
`binom(L-1,j-1)/j` words with `A_i<=ci` at every prefix. Their last
success is exactly at L, so they have no unfinished valuation tail.
Each encoded word has unconditional measure `2^-L`; all good words
start with success, so conditioning multiplies this by2.

The factorial estimate now gives rate

```
exp[-q log q-(1-q)log(1-q)]/2 = beta
```

per trial, and hence per bit. Only after these two clock-specific proofs
do we use the algebraic identity `beta=rho^(1/c)`.

## 4. A fixed escape prefix proves the matching D/M/H lower bounds

Use the exact valuation prefix

```
(1,1,1,2),       x=47 modulo64,
S^4(x)=(81x+65)/32.                                    (4)
```

No D or M test fires in these four steps. The initial run of1s closes
with valuation2, so no H test fires; this also closes every pending
low-origin run. The final slope is `81/32>2` and the run flag is empty.
The conditional cylinder measure of(4) is `1/16`.

Append any zero-barrier valuation word from Section3. Its slope relative
to the escaped state is at least1 at every completed prefix. Consequently
the global slope remains at least81/32. D and M cannot accept. Every
new H run starts at global slope greater than4/3, so H cannot accept
either. For actual x>N, the affine constant terms are positive and the
actual states after(4) likewise stay above2N along these prefixes.

For the odd-step lower bound, append good words of length n-4. For the
bit lower bound, append good compositions of total `m-1-5`; they end
with a completed valuation and also survive the corrected partial-tail H
test. The fixed prefix changes only constant factors and a fixed clock
offset. Section3 gives lower exponential rates rho and beta. D-only
survival is an upper bound for every enlarged recognizer, giving the
matching upper rates and proving(1)-(2).

This proof does **not** imply that every conceivable low-height or local
certificate has the same rate. A proposed larger class of rules must
preserve this escape family, or supply a different positive-measure
escape construction, before the same sandwich can be used. In particular,
rules that recognize inverse ancestors of known seeds at arbitrarily high
states are not among the three tests just defined.

## 5. A precise bit-budget omission in the external H recognizer

The external `coalescence_check.py` accepts H only after the closing
valuation is known **exactly**. At each prefix with total valuation A,
it counts the whole unfinished tail as undecided, with weight
`2^(-(m-A-1))` relative to that prefix.

If a pending eligible H run exists and `m-A>=3`, however, that unfinished
tail already proves that its closing valuation is at least3. The halving
identity needs no exact final valuation. The whole tail is therefore
accepted by H. Our corrected version removes it in that case.

The smallest clear example is m=4: the complete class

```
x=3 modulo16
```

is selected by the halving identity with `a=v_2(x+1)=2` and
`t=(x+1)/4=1 modulo4`. The second Syracuse valuation is at least3,
although its exact value is not determined by four bits. The external
DP reports undecided fraction1; the corrected DP reports3/4, conditional
on the initial valuation1. This is an undercoverage of H at a fixed bit
budget, not an invalid certificate. The external counts remain correct
for the explicitly stricter exact-closing recognizer.

Some D or other inequalities might also be decided from partial valuation
information. We have not claimed a maximally informative bitwise
recognizer: the correction here is exactly the H tail just described.

Selected exact results are:

| bits m | D | D+M | D+M+exact-closing H | D+M+partial-closing H |
|---:|---:|---:|---:|---:|
|4|1|1|1|3/4|
|8|19/32|35/64|1/2|25/64|
|16|4057/16384|867/4096|2555/16384|2431/16384|
|64|0.010551268332|0.008434418498|0.006113630620|0.005980326688|
|128|0.000484184374|0.000380834422|0.000275695999|0.000272161174|

The receipt stores the full exact fractions, including rows32 and96.
An independent direct enumeration of residues verifies all four DP
variants for every m from2 through14. The correction does not change
the proved exponential rate, by Section4.

The feed's fixed-height D-only finite96-to128-bit fitted factors are also
reproduced: for K=1,4,16,64 they are respectively
`0.9546098033, 0.9565378898, 0.9572643214, 0.9580886202`.
They are finite-range fits, not the limiting factor beta.

## 6. Halving bridges can meet arbitrarily high before any descent

This is a direct refinement of the repository's
[halving identity](../residual_return/SHRINKING_COALESCENCE.md), not a new
claim that every root is covered. For every `a=2 modulo4`, a>=10, put

```
x=2^a-1,       N=12*2^(a-4),       q=(x-1)/2.
```

Then N is a required five-ray cutoff, `x=3 modulo12`,
`N<x<3N/2`, and q<N. Thus x is an actual coefficient1 R_N root.
Since a is even, x is selected. Also `3^a=9 modulo16`, so
`v_2(3^a-1)=3`. The two prefixes meet exactly at the following stated
time and state:

```
S^a(x)=S^a(q)=z=(3^a-1)/8,
z/N=(3^a-1)/(3*2^(a+1)) -> infinity.                    (5)
```

For the x prefix, `S^j(x)=3^j 2^(a-j)-1` through j=a-1; every
noninitial state in that range exceeds x>N. Equation(5) exceeds N for
a>=10. Hence the x orbit has not descended below N at any time up to
and including this common state, although its bridge to q<N is complete.

For example, a=10 gives `N=768, x=1023, q=511, z=7381`.
The checker stores both full prefixes for a=10,14,18,22.

The H rule starts at a seed below2N, but the common state need not be
below a fixed multiple of N. A claim that H "fires only near N" must
refer to its **origin**, not its meeting state or the height of its
intermediate arrows. We make no claim that(5) is the first intersection
with the full forward union of all seeds at most N.

Thus the equal-rate theorem cannot exclude general unbounded-length
halving bridges. Such bridges already have a proved infinite family;
the theorem measures only what the specified cylinder recognizers leave
unaccepted. Complete coverage of the complementary roots remains open.

## 7. Audit of the excursion and synthesis claims

The pinned `coalescence_check.py` and `excursion_merge_probe.py` were
materialized in a temporary directory, inspected, then run unmodified.
Their newly generated JSON reports agree exactly with the pinned remote
receipts. Source hashes and full reproduced outputs are retained in
[external_review.json](external_review.json).

The coalescence check validates262144 selected x below2^21 and2000
random selected200-bit seeds, plus five finite coverage cutoffs. Its
finite D/M/H table is reproduced by our independent integer-count DP,
subject to the exact-closing scope in Section5.

The excursion probe uses N49152 and the finite set

```
F_N = union of the complete forward orbits of odd seeds at most N.
```

For that sample all the input paths were explicitly computed to1.
It finds38912 states in F_N, with maximum height about821N, and3925
R_N roots. Median descent/meeting times are4/3 odd steps; the99th
percentiles are36/28; both maxima are96. Roughly30% of roots meet F_N
before descending below N. These are reproducible finite facts.

The following stronger conclusions do not follow from that experiment.

1. A fitted band density near `0.3/H^2` is not a theorem uniform in H
   or N. For this fixed N, F_N is finite and its density is identically
   zero above its largest state.
2. Spatial density in a height band is not an orbit hitting probability.
   No independence of root trajectories and the known-orbit set is
   available. Even an assumed density bound would not by itself control
   an arbitrarily long excursion without further residence or growth
   information.
3. The finite forward union F_N does not exhaust states certifiable from
   the same known seeds by inverse or common-tail identities. A proof
   that treats F_N as the entire available target set needs justification.
4. A finite improvement in median or percentile times does not show that
   all mergers change only a constant factor, or preserve the exponential
   rate of a larger certificate class.
5. A finite absolute slow cluster at two scales does not exclude every
   possible scale recursion. It refutes only the tested correspondence.

The separately proved [known elementary closure](../absorbed_fibers/ABSORBED_FIBERS.md)
makes item3 concrete. Given absorption through N, every state in the
infinite set `I_N={x:nu(x)<=N}` has an explicit finite certificate. For
every integer X>=N>=8 its count in `[X,2X)` differs from N/4 by at most
`2 floor(log2 N)+3`, uniformly in X. Its odd-integer band density has
leading term `N/(2X)`, rather than the finite forward-union sample's fitted
inverse square. This is a different exact arithmetic set, and still gives
no orbit hitting probability or guarantee. The escape-prefix proof above
does not assert that its surviving states avoid I_N.

Likewise, neither the feed's older `N^0.93` extrapolation nor a revised
power inferred from the present beta is an established count of actual
remaining roots. Three separate issues must be controlled when m grows
with log N: discrepancy for an increasing union of residue classes,
the affine constant terms in the certificate thresholds, and transfer
from binary cylinder measure to the actual weighted R_N profile.
The present theorem resolves the exponential-rate question for the
specified symbolic rules; it does not resolve those other issues.

## 8. Reproduction and remaining obligation

Run from the repository root:

```
python3 experiments/residual_progress/cylinder_barrier/check_cylinder_barrier.py
```

This read-only default compares its full exact result with
[cylinder_audit.json](cylinder_audit.json). To regenerate the owned
receipt use `--write-receipt`. It checks the four DP variants against
direct residue enumeration for2<=m<=14; larger exact DP rows through128
bits; odd-step rows through64; rotation lower bounds through32 steps
and64 total bits; the escape prefix; and the explicit high bridges.
The analytic limits depend on the written proof in Sections2-4, not
on these finite ranges. No assertion-disabling optimization is used.

For the external reproduction, the four pinned probe sources were copied
to a temporary `sidekick/probes` directory, with main's
`collatz_research_20261017/negative_controls/affine_controls.py` as its
existing arithmetic dependency. The two unmodified entry points were
`coalescence_check.py` and `excursion_merge_probe.py`, each with a
45-second process cap; both completed. No feed branch file was edited.

The useful next target is an exact bridge rule that reaches beyond these
three recognizers and covers the complementary R23 profile, together with
a proof that its recursion terminates. An enlarged target set must be
counted or otherwise controlled as an actual arithmetic set; density
alone is not a guarantee that every unresolved orbit hits it. The existing
five-ray sufficiency theorem would then supply the global induction.

This note is a model-assisted written proof and computational audit. It
is not formal verification or human peer review.
