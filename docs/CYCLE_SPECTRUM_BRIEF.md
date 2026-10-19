# Goal — The cycle half of Collatz through the whole 3x+d family

**Activated by the user on 2026-10-18; active and unresolved.** This replaces
the quantitative-rigidity goal. V004's classification and V005–V009's gains
remain evidence; the unbounded-ratio problem is retained as open historical
work. It is not the current completion requirement.

## Headline

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
