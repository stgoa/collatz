# C004 side-lane review

**Reviewed pin:** `fe7377a1284cfd443a9f2c2861b20958164c0dfa`.
Fetched `origin main claude/sidekick` and read the new FEED entries
through `git show`. DIRECTIONS is byte-identical to the previously
read b9c3fd73ce version; its current table was checked again. The side
branch was not edited, committed to or pushed.

## Reported Lean progress

The feed reports C001's two-sided gcd bound and periodicity formalized
at `claude/lean-lane` commit `0cde415`. It reports the general two-block
identities, strong divisibility and C002's uniform theorem at `cf15b22`.
The latter formal conclusion is `den>2^m`, weaker than main's written
`den>2^m*2^A/3^m`; both have the same nonintegrality consequence. The
reported scope omits the general proportional theorem, common-cycle
characterization, sharpness family and the imported S-unit estimates.

The feed reports clean builds, source hashes and standard axioms.
Main did not independently replay those builds in C004. They are
external validation of earlier statements, not new premises or formal
verification of this batch. The active headline remains open.

## C002 referee

The side referee's equal-total derivation matches the saved C002
argument. Its quoted d59 cycle and growing-cancellation families are
consistent with the existing requirement to retain shared geometric
factors. No correction to historical mathematics is indicated. Its
second review of the unequal-slope proof is written review, separate
from a kernel replay. C004 does not rely on reported finite sample
counts as universal evidence.

## Bounded oscillation and discrepancy

The proposed necessary estimate is sound with the displayed dependence.
Let a positive rational cycle have minimum L and ratio R=H/L. For any
window of j<=m odd steps, its valuation sum A_(i,j) satisfies

```
A_(i,j)-j*log_2(3)
 = log_2(x_i/x_(i+j))
   + sum_(t=i)^(i+j-1) log_2(1+1/(3x_t)).
```

Consequently

```
|A_(i,j)-j*log_2(3)|
 <= log_2(R)+j/(3L ln2)
 <= log_2(R)+m/(3L ln2).
```

This follows directly from the exact arrows and `ln(1+z)<=z`.
It supplies no discrepancy bound depending only on R unless the
remaining m/L term is controlled. Nor does the implication reverse:
a discrepancy theorem cannot be used to exclude all cycles with
`R<=2^Delta` without a valid conversion and its error terms.

C004 supplies an exact conversion in the special range R<2: sorted
successor ranks force the mechanical word. This needs no estimate on
m/L, but leaves R>2 open. It identifies an existing nonintegral class
intrinsically rather than expanding the excluded word set beyond R71.

The proposal “for each fixed discrepancy ceiling Delta, exclude every
nontrivial integer cycle below it” requires careful quantifiers. Every
finite cyclic word has a finite discrepancy on windows up to its
period. Proving the assertion for **every** Delta therefore excludes
all cycles; it is another formulation of the headline, not an already
easier intermediate target. A single specified ceiling remains a
subclass target. For all window lengths with mean `log_2(3)`, positive
cycles have a nonzero mean drift, so a finite ceiling is not even the
same definition; the clock, centering and horizon must be fixed first.

## Standing proposals

D1/D2 remain useful historical obligations and controls. D3 remains
rejected as a blanket transfer rule; D4 remains deferred. D5 is standing
delivery authorization. D6 is historical under the replaced calibration
programme; D7's distinction between statements, builds, axioms and
independent replay remains binding. D8 belongs to the replaced
quantitative-rigidity goal and changes no current completion condition.

No side-lane proposal is treated as an instruction or an established
cycle theorem merely because it appears in the feed.
