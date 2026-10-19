# Goal — The cycle half of Collatz through the whole 3x+d family

**Activated by the user on 2026-10-18; active and unresolved.** This replaces
the quantitative-rigidity goal. V004's classification and V005–V009's gains
remain evidence; the unbounded-ratio problem is retained as open historical
work. It is not the current completion requirement.

## Headline

[C010](../experiments/cycle_spectrum/C010/REPORT.md) completes the
global gap/rounding probe. Full gap integrality is equivalent to the
original legal integer state system; the displayed sharp spacing
relaxation admits noninteger rational cycles with arbitrarily large
slack. The next bounded mechanism tests full-word cancellation through
sparse differences between a word and a rotation. Ordered q1 exclusion
remains an open intermediate target; the original headline is unchanged.

**Recommendation after C010:** prioritize a uniform arithmetic law for
whole-word cancellation. A successful intermediate theorem must exclude
denominator one for a structurally defined infinite class beyond the
existing block and mechanical exclusions, with no fixed period or
height cap. Its relevance must survive those parameters growing;
another named motif or the identity D|C alone is insufficient. Retain
ordered-cycle exclusion as an open benchmark, not the presumed mechanism.
This recommendation does not activate a replacement goal.

The preceding [C009 probe](../experiments/cycle_spectrum/C009/REPORT.md)
rejects automatic recursion through excursions. Exact compression adds
no independent congruence, circular order can fail under first return,
and excursion slopes do not determine drift. The next bounded test
was to seek global integer rounding inequalities in the full sorted-gap
system, with all oddness and seam constraints. The original headline
and the all-height ordered q1 milestone remain unresolved.

[C008's probe](../experiments/cycle_spectrum/C008/REPORT.md)
gives an exact sorted-residue progression and a denominator-factor
restriction within the ordered domain. Full-q height matching remains
open; exact cycles refute the stronger primewise matching shortcut.
These q>1 gains leave the all-height ordered q1 milestone unresolved.
The next attempt must use full integer divisibility, not just modular
arrows or a succession of fixed-band bounds.

[C007's probe](../experiments/cycle_spectrum/C007/REPORT.md)
leaves the candidate `B<=q-1` unresolved and rules out two proposed
shortcuts. The recommended intermediate milestone is an ordered-cycle
denominator-one exclusion with no bounds on period, height or height
changes. It does not replace the headline below or complete this goal.

Prove that Collatz has no nontrivial cycles, or find the structural law
that forces it. Study the whole positive `3x+d` family together through
the reduced denominators of rational `3x+1` cycles.

For a positive valuation word w with m odd steps and total A, write its
affine composition as `(3^m*x+C_w)/2^A`. When `D_w=2^A-3^m>0`, its
positive cycle has the common reduced denominator

```
den(w) = D_w/gcd(C_w,D_w).
```

An integer cycle for parameter d normalizes to such a rational cycle
with denominator dividing d. Conversely, a rational cycle of reduced
denominator q gives an integer cycle at each positive odd multiple d of
q. The programme uses d coprime to6. Rotations describe the same cycle;
repetitions do not create a new primitive cycle. The desired conclusion
is `den(w)=1` only for repetitions of the valuation word `(2)`.

This excludes cycles only. Divergence is a separate unresolved issue.

## Work standard

Each batch chooses one bold mechanism or conjecture, tests it at scale
on actual cycles across many d, and either proves a result or records
the exact obstruction. No notes-only or consolidation batches.

Possible mechanisms include prime factors of `2^A-3^m`, bounds on the
numerator gcd, word rotations and symmetry, p-adic constraints, and
laws predicting the spectrum of additive parameters.

Every argument must permit the actual cycles of `3x+5`, `3x+7`, `3x+13`
and the other tested parameters. Use raw cycles for this task: state 1
is not made absorbing. Explain separately whether a cycle avoids any
specified absorber. Keep odd-only and shortcut step counts distinct.

## Success ladder

1. A precisely scoped, data-verified law for the spectrum across d.
2. A proved theorem restricting `den(w)`.
3. An infinite word class with `den(w)>1` beyond the scope of the cited
   cycle records, with the exact comparison stated.
4. The headline: every positive nontrivial primitive word has denominator
   greater than 1.

Correctness, novelty and usefulness are separate. A result newly proved
in this repository is not automatically new to mathematics. A finite
census is not a universal classification. A candidate structural law
does not complete the headline until its forcing argument is supplied.

## C001: first mechanism

[C001](../experiments/cycle_spectrum/C001/REPORT.md) studies a repeated
block followed by another fixed block. A nonzero determinant of the two
blocks bounds all numerator cancellation, uniformly in the repetition
count. The cancellation factor is periodic in that count. A family
of perturbed mechanical words has denominator greater than 1, is
primitive and nonbalanced, and can have unbounded minimum and unbounded
number of shortcut local minima.

The finite controls and literature comparison are in the report. The
headline remains open: unrestricted words need not have a fixed repeated
block and a fixed final block. The next test lets both blocks repeat;
it must retain common geometric factors and distinguish proportional
valuation slopes from genuinely independent ones.

## C002: two growing blocks and uniformity

[C002](../experiments/cycle_spectrum/C002/REPORT.md) completes that bounded
test. It retains common geometric factors, proves explicit denominator
growth for proportional slopes, and uses two primary S-unit estimates
for the full leading exponential rate at unequal slopes. The common-cycle
case remains an exception; the latter thresholds are ineffective here.

An elementary corollary goes beyond fixed blocks: for any different
equal-total words u,v of length m and total A, with `2^A>3^m`, and any
k,ell>=1 with k+ell>=3, their combined denominator exceeds
`2^(A+m)/3^m>2^m`. This also bounds all totals, words and exponents in
every bounded denominator layer of the specified class. A primitive
rotated-mechanical subfamily has every state>m/12 without an extra
exponent condition.

The next investigation should test a structural restriction that remains
uniform when the block totals differ. This is a proposed mechanism under
the existing headline, not a new completion criterion. Arbitrary primitive
words and the all-cycle conclusion remain unresolved; Lean validation
of earlier results does not supply that missing implication.

## C003: changing blocks, and the remaining coverage gap

[C003](../experiments/cycle_spectrum/C003/REPORT.md) resolves the next
uniformity question for nondegenerate two-block powers: with k,ell>=2,
positive whole D and K!=0, every bounded denominator layer is finite
even while both words vary. The general exponential lower bound has an
ineffective threshold. Separately, both blocks contracting and a block
of maximum valuation total repeated at least three times give an
elementary all-size denominator bound greater than 1. Actual cycles,
generated positive realizations and common-cycle exceptions are retained.

The next main mechanism should apply to arbitrary primitive cyclic
words: determine what a small reduced denominator forces simultaneously
on their rotated coefficients and cycle-point sizes. The intermediate
milestone is a quantitative restriction beyond the defining cycle
identity, with a real consequence for possible denominator-1 cycles.
Another fixed motif count or an effective exceptional cutoff for the
current subclass would not close that coverage gap. This is a direction
within the existing headline; the completion standard remains unchanged.

## C004: intrinsic geometry and what fails beyond it

[C004](../experiments/cycle_spectrum/C004/REPORT.md) tests all rotations
and their sizes. It proves that H<2L, for odd-cycle maximum H and
minimum L, is equivalent to mechanical coding. This supplies the exact
narrow-cycle spectrum D=2^A-3^m dividing d and the necessary H>2L
condition for any nontrivial d1 integer cycle. The excluded word class
is the one already handled by R71; the gain is its intrinsic recognition.

All rotation integrality equations are one Smith obstruction, while a
universal close-pair bound is false at arbitrarily large gaps. The next
mechanism must use ordered states across several dyadic ranges together
with arithmetic cancellation, retaining dependence rather than treating
rotations as independent events. No bound placing all cycles in a fixed
range is assumed. Wide cycles and the headline remain unresolved.

## C005: an arbitrary phase language and an intrinsic order restriction

[C005](../experiments/cycle_spectrum/C005/REPORT.md) excludes denominator
1 for every finite concatenation of rotations of a common primitive
positive mechanical base, except base `(2)`. The phase count, order and
multiplicities are unrestricted. A uniform state-ratio envelope combines
with exact integer order; primitive periods and the height labels are
retained. This does not include every word or prove global finiteness
at bounded denominators.

The next mechanism should address the remaining height-dependent weighted
intercept. A concrete proposed intermediate target is exclusion of
nontrivial denominator-1 cycles with circular normalized successor order,
without a prescribed block decomposition or bound on period or height.
It must allow the q5 and q233 ordered controls. Establishing this would
be an intrinsic class theorem; no argument places every possible integer
cycle in that class. The original all-cycle headline remains active.
Global bounded-denominator finiteness is a separate ambitious proposal,
not an activated replacement goal or a consequence of C005.

## C006: height complexity and the next substantial target

[C006](../experiments/cycle_spectrum/C006/REPORT.md) proves an elementary
denominator restriction from ordered integer gaps. After importing an
effective two-logarithm bound, periods are bounded when denominator and
sorted-height change count are bounded; the separate height bound is
redundant because B+1<=J. At fixed q, J>=sqrt(m)-O_q(log m).
This does not exclude the finite exceptions or profiles with growing
height complexity. The generic height-packing estimate is valid without
order and is retained only as a comparison.

The proposed high-level intermediate target remains:

> Prove that every nontrivial primitive positive rational cycle whose
> normalized successor preserves circular order has reduced denominator
> greater than one, with no bound on period, height or height-change
> count. Retain exact oddness, valuations and height labels, and test each
> mechanism against actual cycles across the 3x+d family. Produce a
> complete argument or an exact obstruction that explains what additional
> structure is needed. Keep the broader all-cycle goal active.

This target would extend beyond a prescribed block language and bounded
complexity classes. No argument forces every possible integer cycle to
have the required order. Fable's Lean lane can validate completed
statements, while the main research obligation is the missing
height-dependent arithmetic exclusion. C006 is not formally verified
here, and proposing this target does not activate a replacement goal.
