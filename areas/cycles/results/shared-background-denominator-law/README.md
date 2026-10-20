# C013 — Denominator growth from an arbitrary shared background

**Status: written quantitative theorem, explicit analytic input, exact
finite checks and a scoped infinite obstruction.** The all-cycle goal
remains active. Neither unrestricted rotation-distance growth nor full
cycle exclusion is proved. The clock is raw positive odd-only, without
an absorber; divergence is a separate question.

## The high-level aim and the actual gain

The recommended intermediate target remains an explicit lower bound
`rho(w)>=F(m)`, with F tending to infinity, for every hypothetical
nontrivial integer cycle of primitive period m. Here rho is the minimum
number of mismatches between the valuation word and any nonidentity
rotation. C011 proves only the constant bound rho>=3. The active
headline remains exclusion of all nontrivial cycles.

This batch tests the missing overlap information. It obtains a
quantitative law for any word built from one arbitrary background U
separated by any nonconstant marker pattern. At fixed marker count and
total, every bounded-denominator layer of the whole varying-background
class is finite, effectively in principle. A hypothetical integer
cycle in this class must have growing representation complexity.

That is a genuine restriction with unbounded word length and height.
Its limitation is equally explicit: the representation count r below
is not the rotation mismatch count s. Arbitrary sparse rotations may
contain different compatible shared arcs. The desired universal
mismatch theorem remains open.

## Exact factor extraction before estimating cancellation

Write

```text
w=(U,a_0,U,a_1,...,U,a_(r-1)),
n=length(U),  T=sum a_i,  m=r(n+1),  A=r A_U+T,
u=2^A_U,  alpha=3^(n+1),  E=3 C_U+u,
P(X)=sum_(j=0)^(r-1) 2^(a_0+...+a_(j-1)) X^(r-1-j),
Q(X)=X^r-2^T.
```

All letters are positive; r>=2, markers are nonconstant, and
`D=2^A-3^m>0`. U may expand. Empty U is allowed as a boundary control.
Let G be the monic polynomial gcd of P,Q, with degree d, and put
e=r-d. After homogeneous evaluation at alpha/u, the exact reduced
denominator is

```text
q=|Qbar_h|/gcd(Qbar_h,E Pbar_h),
Pbar=P/G,  Qbar=Q/G.
```

The numerical gcd `h=gcd(Qbar_h,Pbar_h)` divides the nonzero integer
resultant `R=Res(Pbar,Qbar)`. The separate numerical gcd with E is retained.
No independence of these cancellation mechanisms is assumed.

## A uniform denominator law

The normalized positive marker-prefix sequence has exactly e nonzero
Fourier coefficients. If a selected marker rotation has s>0 letter
mismatches, the elementary support uncertainty inequality gives

```text
s * binom(e,2) >= r.
```

In particular e>=2 for every nonconstant marker pattern. Root separation
for Q and positivity of the background intercept give, with
`eta=D/2^A`,

```text
|R| <= r^[e(d+1)] * 2^(2Te),
q > eta * 2^[n(e-1)-d] / |R|
  >= eta * 2^[n(e-1)-d] / (r^[e(d+1)] * 2^(2Te)).
```

The [complete proof](OVERLAP_CONTROLS.md) includes the sharper
intermediate estimate and effective bounded-q finiteness at fixed r,T.
Its only analytic input is the explicitly sourced Matveev estimate
already used in C011. Bounding n is followed by a separate bound on
A_U; a period bound alone is not silently promoted to word finiteness.

For a hypothetical nontrivial q1 cycle, `A<2m`. With natural logarithms
and K=600,000,000 the law implies

```text
n < r + 4T + 2(r-1)log_2 r + (K/log 2)(1+log(2m)).
```

Consequently, if `T<=H_mark*r` for a fixed marker-average ceiling,
then `r=Omega_(H_mark)(sqrt(m/log m))`. The constants are effective
but large; no practical cutoff is claimed. This constrains the stated
representations and leaves finite q1 exceptions at fixed r,T. Constant
markers, including repetitions of the trivial word `(2)`, remain
outside the finiteness assertion.

## Two cancellation controls

The primitive marker word `(3,1,3,3,1,1)` has `G=X+4`. Polynomial
cancellation therefore is not merely a symptom of repetition.

Conversely, the actual q5 cycle of period17 and minimum347 has G=1
but `gcd(C,D)=1015513`. Polynomial coprimality does not prevent large
numerical cancellation at evaluation. The resultant and background
intercept cannot be discarded. The proof and checker retain actual
q5/7/13 cycles and every existing fixture.

## Why a height shortcut fails

Subtract states at two phases of an actual primitive cycle. Along an
agreeing run of t arrows and total valuation E, exact even differences
satisfy

```text
z_start=2^(E+1)k,  z_end=2*3^t*k,  k a nonzero integer.
```

This gives a denominator bound involving the actual dyadic height B.
It does not eliminate B. The [obstruction proof](OVERLAP_THEORY.md)
constructs primitive actual generalized cycles with minimum rotation
distance3, vanishing logarithmic drift, `L/q=Theta(m)` and
`B=Theta(m)`. Thus the proposed polynomial conversion from normalized
minimum to height fails even with q<=L. These examples have growing
denominators; they do not refute a restriction at fixed q or at q1.

## Verification and research decision

The exact checker, independent reviews, primary-source audit and
preservation receipt are separate evidence layers. The finite check
scope is recorded in [EXACT_REVIEW](EXACT_REVIEW.md); written proofs
carry the universal and asymptotic claims. The historical finite gate
passes all119 fields. Published analytic inputs are not independently
formally verified, and Fable's latest reported Lean build was not
kernel-replayed on main in this batch.

The candidate unrestricted bound
`q>eta*(4/3)^(m/s)` remains unproved and unrefuted. Stored successes
and the bounded structured probe are already implied by their observed
parameters and supply no discriminating support. That search was
stopped rather than enlarged.

**Next bounded mechanism:** use polynomial factor extraction for
distinct but compatible overlapping arcs, and charge every numerical
gcd/resultant term. Seek a consequence uniform in the number of
mismatches and in height. If compatibility adds no useful quantitative
gain, record that obstruction and compare another mechanism. Do not
substitute a succession of fixed marker catalogues for the growing
rotation-distance milestone.

See [the independent positive-theorem review](THEORY_REVIEW.md),
[the obstruction review](OBSTRUCTION_REVIEW.md), [root review](ROOT_REVIEW.md),
[sources and record comparison](LITERATURE.md), [side review](SIDE_REVIEW.md)
and [delivery receipt](delivery_checks.json). No novelty, unrestricted
q1 exclusion, improved universal cycle record or goal completion is
claimed. This batch is progress under the unchanged headline.
