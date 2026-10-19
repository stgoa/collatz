# Cycle spectrum programme log

## C002 — Two growing blocks and a uniform exclusion, 2026-10-19

**Progress; headline active and open.** C001 was delivered at
`14441c0864ba67e73d32b24dc67afb4cd832921e`. This batch tests its next
mechanism, with both repetition counts free. [The report](../experiments/cycle_spectrum/C002/REPORT.md)
links the full arguments, primary source, independent review and exact
receipts. Historical mathematics and C001 evidence are preserved.

The strongest elementary result is uniform over changing blocks:
different words u,v with equal totals (A,m), `2^A>3^m`, and k+ell>=3
have `den(u^k v^ell)>2^(A+m)/3^m>2^m`. This bounds the totals and
words in each bounded denominator layer; the explicit proportional-slope
bound then bounds both repetitions. It excludes this whole structural
class without assuming a finite catalogue. Arbitrary cycle words need
not admit the required decomposition.

The general elimination identity retains a shared geometric gcd.
Proportional slopes admit an elementary strong-divisibility proof and
an explicit exponential bound. Unequal slopes retain the full leading
exponential denominator rate, using Corvaja–Zannier's Corollary 1 and
Proposition 1; the local terms and exceptional-grid intersections are
audited. This covers an expanding block but supplies no effective
threshold. K=0 retains repetitions of a common primitive cycle.

The former constant bound is false: `(1,1,3)^t(1,2,2)^t` has cancellation
`(32^t-27^t)/5`, already greater than K=20 at t=2. All thirteen failures
found among actual cycle decompositions are saved. A separate exact
family shows the proportional half-exponent is sharp.

The rotated-mechanical family has every rational state>m/12, with no
extra exponent separation, and is primitive and nonbalanced. Its
odd-only and shortcut minimum counts are retained separately. The
literature comparison is scoped to the hypotheses audited in C001;
general record improvement and novelty are unclaimed.

The checker replays 2,459 actual cycles over 333 parameters, 37,271
canonical power decompositions and all eleven fixtures. It generates
451,584 word/exponent cases, including 433,074 positive realizations
and over 10.6 million exact odd arrows. Separate checks exercise the
uniform theorem and the rotating family. Finite checks do not verify
the imported asymptotic theorem. The final receipts distinguish proof
review, local replay and the historical finite gate.

The reviewed side pin is `f82781197b1b2792e7b3394a142754f383b4555d`.
Its new V006 Lean report and V009 reading are external evidence; C002
does not independently replay those builds or use them as new premises.
The [side review](../experiments/cycle_spectrum/C002/SIDE_REVIEW.md) records
the D1–D8 assessment. No side branch was modified.

**Next:** seek a uniform structural restriction when block totals differ.
The user's high-level concern about accumulating small lemmas is addressed
by keeping that uniformity requirement explicit. Extending only fixed
catalogues would leave the main gap untouched. The accepted goal remains
cycle exclusion through the generalized family, with divergence separate.

## C001 — Fixed perturbations and bounded cancellation, 2026-10-18

**Progress; headline active and open.** The user replaced the quantitative
goal after V009 at `4be9bae23a2d06dc7c31c2237299273cb9c5a1f2`.
The [new brief](CYCLE_SPECTRUM_BRIEF.md) studies the entire positive
3x+d family through rational-cycle denominators. The old ratio target
remains open historical work; it is not marked solved.

[C001](../experiments/cycle_spectrum/C001/REPORT.md) selects one mechanism:
a fixed block inserted after arbitrarily many repetitions of another.
A nonzero affine determinant K bounds every cancellation divisor, and the
cancellation sequence is periodic. K=0 is retained as the common-cycle
case. A stronger equality requires coprime block denominators; the
exact d485 cycle 49,79,361 refutes dropping that premise.

The application `u_m^k 2`, with u_m the mechanical word at
`A=ceil(m log_2 3)`, m>=13,k>=2, has denominator greater than 1.
It is primitive and nonbalanced. Under an explicit extra exponent
condition its rational minimum exceeds m/10, and its shortcut minimum
count is k(A-m)+1. This simultaneously escapes fixed height/count
cutoffs and the mechanical class. The result's scope and novelty are
kept separate from improvements to a general published cycle record.

An independent raw scan supplies 2,459 cycles over 333 values of d from
832,500 seeds, all eleven fixtures rediscovered, with no caps reached.
It verifies 34,453 canonical splits and 2,371 repeated-prefix cases.
The separate word-family check supplies 239,345 positive cycles and
over 6.2 million exact arrows. Written proof, finite receipts and
independent review are linked in the report. Historical mathematics
and the open LaTeX source are unchanged.

The reviewed side pin is `a15cd429747e43997ce94aa84264fb8e32b6848d`.
Its V009 confirmation and new Lean report are retained as external
input, not instructions. Detailed assessments of D1–D8 and the current
cycle literature are in the batch's side review and literature audit.

**Next mechanism:** two growing repeated blocks. Common geometric
divisors must be retained; proportional slopes give a real cancellation
obstruction. Examine the published S-unit gcd input for unequal slopes
and test both regimes on actual cycle data before claiming a new law.
