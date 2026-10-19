# Cycle spectrum programme log

## C009 — Exact excursion obstruction and a mechanism pivot, 2026-10-19

The [batch](../experiments/cycle_spectrum/C009/REPORT.md) tests the
proposed first-return compression using true affine intercepts and full
closure. Prefix divisibility proves that odd integer endpoints already
force every internal exact valuation. The compressed block matrix has
the same Smith obstruction D, so the algebra returns D|C at q1.

Automatic geometry and descent fail on actual controls. Ordered q13
loses circular order on its four-state core, and ordered q83 has a
contracting positive-height excursion that rises. The finite-rotation
one-point-deletion theorem explains the first failure uniformly in m.
Open q1 paths realize both drift signs without being closed cycles.

All 1,185 normalized cycles give 2,593 first returns and 28,831 prefix
cylinder checks; all11 fixtures and scaling distinctions survive.
Among the52 ordered cases,12 lose induced order. Of60 positive
excursions,12 rise and2 of those have contracting slope. Separate
reconstruction and deletion checks cover16,368 endpoint pairs and
105,388 finite permutations. Proofs and independent replays are scoped
separately from formal verification and novelty.

The batch reaches its stated pivot criterion. Stop automatic excursion
recursion; test global integer rounding in the full gap system next.
No new inequality, q1 exclusion or numerical record is claimed.
Fetch and side review at2157596 retain reported Lean progress without
main kernel replay. The original all-cycle goal stays active.

## C008 — Exact rank residues and failed primewise matching, 2026-10-19

[C008](../experiments/cycle_spectrum/C008/REPORT.md) proves the sorted
law `z_[j]=L*t^j mod q` and its height-shifted raw version. The group
`<2,3>` must be cyclic under coprime totals, excluding factors35/65/91
for reduced ordered cycles with q<=L. This is an elementary consequence
of C005, not a q1 exclusion. All periods and heights are permitted.

Normalized Hall is proved for q>1,B<=2 and raw Hall for q>1,B<=1.
Actual q5077565 ordered cycles refute primewise matching, including
a proper-subset failure despite enough available units modulo5.
Both full-q variants pass all1,185 stored cycles; 946,001 screened
profiles give only13 small-q cycles, all already known. The exact
obstruction is new evidence in this batch; the grid does not improve
coverage. The separate lattice checker covers332 moduli and477,552
cells, retaining all actual-cycle controls and the q1 fixed point.

The next high-level milestone remains all-height ordered q1 exclusion.
The next mechanism must combine full weighted divisibility and all
integer rank gaps. Full-q Hall remains a candidate; fixed-band q>1
results are diagnostics. [Side review](../experiments/cycle_spectrum/C008/SIDE_REVIEW.md)
records successful fetch, pin aab73dd and reported Lean b60fd21 without
main kernel replay. Independent written reviews and finite receipts
are separate from formal verification and novelty.

## C007 — Height arithmetic and failed residue shortcuts, 2026-10-19

The [batch](../experiments/cycle_spectrum/C007/REPORT.md) tests the
candidate `B<=q-1` for ordered reduced cycles with q<=L. It remains open.
Normalized residues follow a height-free recurrence for fixed c, and
an exact q5 cycle has overlapping residue classes at different heights.
Rational rescaling of another q5 cycle preserves the real order geometry
with additive term 1 and B3. These are exact failures of specific proof
shortcuts, not counterexamples to the denominator candidate.

A bounded census processes 8,800,033 odd seeds across 33 parameters
without caps or unprocessed seeds. It adds the ordered q29 cycle with
minimum 7055, period 41 and B7, bringing combined coverage to 1,185
normalized cycles. The candidate passes every one, including unordered
cases. Proof review, separate finite replays and historical verification
are recorded in the batch; no stronger denominator exclusion is claimed.

The recommended intermediate goal remains an all-period ordered q1
exclusion, with unrestricted heights and change count. The next probe
must use full weighted divisibility together with integer order. The
unchanged headline remains exclusion of all nontrivial cycles.

Successful fetch and side review culminated at
`ecc04923e0591c3dbd1bd9658ffa19e9d6ce9a32`. It reports the completed
C004 narrow equivalence at Lean 8db3feb; main has not replayed it.
[SIDE_REVIEW.md](../experiments/cycle_spectrum/C007/SIDE_REVIEW.md)
records D1-D8 and the remaining formal scope. C005/C006 were successfully
committed and pushed as `1cb02fa`; earlier failure notes are historical.

## C006 — Order forces complexity in the height labels, 2026-10-19

**Progress; original headline active and open.** The
[batch report](../experiments/cycle_spectrum/C006/REPORT.md) proves a
gap restriction without a common-base decomposition. For primitive
ordered cycles with q<=L, maximum height B and sorted-height change
count J including the seam, a long zero-forcing run forces binary
divisibility of an integer gap. Thus
`q>(D/C_lower)2^(ceil(m/J)-1-B)`, with a sharper exponent from each
actual run. A classical effective two-logarithm bound gives finite
periods under bounds on q,J alone: chronological heights visit every
level, so B+1<=J. Fixed q force J>=sqrt(m)-O_q(log m). The proof leaves finite exceptions and
growing height complexity, so the ordered q1 target remains open.

A wide actual q233 profile gives q>=15 versus the generic packing
bound2. The generic extremal/packing estimate also holds without order;
it is not evidence of an order-specific gain. Exact q1909, q233 and q13
controls refute mechanical-normalization sufficiency, unit gcd after
one height defect and a universal small odd gap. The invalid q1 affine
loop is explicitly rejected. Every stored raw fixture is retained.

The checker covers 2,459 source cycles at 333 parameters and 360,618
generated legal profiles, separating actual heights and order from
formal labels. Proof review, source inspection, finite replay and the
historical gate have distinct scopes, recorded with the batch.

Fetch was attempted but not executed because automatic approval review
was at capacity. The shared tracking ref was read first at `2ea1c7f` and
then at `f054db41be4688dec8200208e4994e96379bc0dd`. The latter reports
Lean C004-a at `7959806` in addition to C003-a at `8388c38`. Main did not
independently replay those builds. [SIDE_REVIEW.md](../experiments/cycle_spectrum/C006/SIDE_REVIEW.md)
records D1–D8 and the exact formal scopes. No side branch was changed.

The final authorized fetch retry succeeded: main stayed at `61cf54a` and
the fetched side pin is `9ac12a8b7c960333f6ee7c2a0f39651209b486b9`.
Its added C004-b part1 report at Lean `5be60e6` covers exponent/rank lemmas,
not the full forward classification. DIRECTIONS and FEED were reread;
main did not independently replay the reported build.

**Next:** the proposed high-level intermediate target is exclusion of
every nontrivial ordered denominator-one cycle, with no bounds on its
period, height or change count. Probe the missing height-dependent
arithmetic; a bounded scan or another generic packing estimate is
insufficient. This recommendation does not replace the original goal.
Publication status is recorded separately in the batch delivery note.

## C005 — Arbitrary phase order within a mechanical base, 2026-10-19

**Progress; original headline active and open.** Baseline main is
`61cf54ad52df1caa5cc250b0d1464432ed90b162`. The preceding advisory turn
proposed a milestone but did not advance the mathematics or change the
active goal. This [batch](../experiments/cycle_spectrum/C005/REPORT.md)
tests dyadic order and arithmetic cancellation on actual cycles.

The strongest result excludes denominator1 for every finite concatenation
of rotations of one primitive positive mechanical base, with arbitrary
phase order and multiplicities; base(2) is the trivial exception. Full
block contractions and positive prefixes give odd-state ratio at most
R^3<8. A primitive integer cycle in that range has coprime totals,
forcing the mixed word to reduce to one mechanical block. A primitive
six-phase prime-base family has unbounded minimum and shortcut minimum
count. The literature comparison is scoped; novelty is unclaimed.

Under q<=L, normalized successor rank rotation is equivalent to strict
scaled-image order. The q233 two-band and q5 period17 cycles show why
mechanical normalized exponents do not retain the no-cancellation
conclusion. The exact height weights must remain in the intercept.

The order audit exercises 2,459 actual cycles at 333 parameters, all
eleven fixtures, 739,757 distinct-cycle pairs and 21,844 generated words.
The separate block checker tests arbitrary phase combinations, primitive
reduction, actual-cycle recognition and the high family. Proof review,
root replay and historical gate receipts are linked in the report.

The reviewed local side pin is
`67c691b93ddd3d07748f557c8a26f9883e37389b`. A fetch was attempted but
failed because the automatic approval service was at capacity. The
[side review](../experiments/cycle_spectrum/C005/SIDE_REVIEW.md) records
reported C002 Lean strengthening, D1–D8 scope and an exact discrepancy
correction. No side branch was edited or used as an instruction source.

The shared local ref later advanced to `2ea1c7f6e51e31b80d354b458d8fa121e4f6e8aa`.
Its new C003 Lean report is assessed in the
[addendum](../experiments/cycle_spectrum/C005/SIDE_ADDENDUM.md), with
unchanged DIRECTIONS and no independent main build.

**Next:** test denominator-1 exclusion under circular normalized successor
order, retaining the heights but dropping common-base, period and height
bounds. This is a proposed intrinsic-class milestone under the existing
headline. No argument places every hypothetical integer cycle in that
class. Global bounded-denominator finiteness remains a separate proposal;
neither it nor the all-cycle headline is proved. Historical results and
earlier C-series files remain preserved.

## C004 — Intrinsic geometry and two exact obstructions, 2026-10-19

**Progress; headline active and open.** Baseline C003 is
`7270d956e1f7037e48b92493024f4f1baefd61d8`. The selected mechanism
uses all cyclic rotations and their state sizes, with no repeated-block
hypothesis. The [report](../experiments/cycle_spectrum/C004/REPORT.md)
links proofs, controls, independent review and exact checks.

Every primitive positive rational cycle with largest odd state H<2L
is mechanical, and conversely. Its coprime totals give exact denominator
D=2^A-3^m. At odd parameter d, these cycles are exactly the mechanical
ones with positive D dividing d. Thus a hypothetical nontrivial d1
integer cycle has H>2L. This recognizes R71's existing class through
intrinsic geometry; no larger excluded word set or novelty is claimed.

The full cyclic matrix has one Smith obstruction; appending the constant
column has final factor g=gcd(C,D). All rotations give the same integer
lattice condition. The exact one-letter cut gcd includes an extra factor,
which is one at valuations1/2. Bare divisibilities cannot be multiplied
as independent filters. Meanwhile the d5 cycle19,31,49 refutes the
proposed universal pair gap<2. Coprime mechanical upper approximants
prove every pair gap can be arbitrarily large, even with H<2L.

All 2,459 source cycles, 333 parameters, 36,912 rotations and eleven
fixtures are replayed. There are 28 distinct normalized gap failures.
The 105 narrow nontrivial source instances represent eleven normalized
cycles. Separate checks cover 86,442 positive short words, 340 small
matrices and 156 mechanical examples. Independent written review and
finite replay are distinct from formal verification.

Side pin `fe7377a1284cfd443a9f2c2861b20958164c0dfa` reports C001-b and
C002-a Lean work. Main did not replay those builds. Its discrepancy
lead is retained only with the m/L error and finite-window convention;
exclusion for every finite ceiling would restate the full cycle task.
The [side review](../experiments/cycle_spectrum/C004/SIDE_REVIEW.md)
records the scope assessment. Earlier mathematics and C001–C003 stay intact.

**Next:** an order/cancellation constraint that survives several dyadic
ranges. Neither a fixed range for all cycles nor independence of the
rotated congruences is available. The headline is unchanged.

## C003 — Uniform restrictions across changing blocks, 2026-10-19

**Progress; headline active and open.** C002 was delivered at
`e14a4e361bd01d93fc48eaa4f2684300dad194e9`. This batch removes its
fixed-block limitation for nondegenerate `u^k v^ell`, k,ell>=2, with
positive whole-cycle D. The [report](../experiments/cycle_spectrum/C003/REPORT.md)
links the written proofs, reviews and exact receipts.

Every bounded denominator layer has finitely many representations in
that whole varying-word class. A fixed ambient S-unit group gives
uniform unequal-slope growth; the proportional branch retains its
shared factor and uses a sharp coprime integer inequality. The combined
positive exponent is `(5*log_3(2)-3)/14`; the general threshold remains
ineffective. K=0 retains all common-cycle powers.

An elementary theorem gives exclusion at every size when both blocks
contract and a block of maximum valuation total occurs at least three
times: `den>2^max(m_u,m_v)*Q_*^(t_*-3)`. It gives effective finite
enumeration for its bounded denominator layers. It covers unequal-total
cases but does not contain C002's equal-total counts (1,2). The actual
d499 cycle disproves extending its interval trapping to expanding blocks.

The checker replays 2,459 actual cycles at 333 parameters, every rotation
and 1,694,160 decompositions, plus 243,878 positive generated realizations
and 4,650,456 arrows. Actual data has zero cases eligible for the strong
three-copy theorem; 153,696 generated checks exercise it. The sharp
integer lemma has 78,287 bounded checks. Root replay and the historical
119-field gate pass. Finite evidence does not verify asymptotic inputs.

The reviewed side pin is `b9c3fd73ce34174053b0d6c4668cd50b405ae015`.
Its C001 Lean algebra report is external validation, not main's replay.
The [side review](../experiments/cycle_spectrum/C003/SIDE_REVIEW.md)
proves divergence of the proposed naive random-residue model and corrects
the raw word-enumeration estimate; no model is adopted as a cycle theorem.
Draft example arithmetic and two report scope issues were corrected and
documented before delivery. Historical results and C001/C002 are preserved.

**Next:** seek a restriction intrinsic to arbitrary cyclic valuation
words, coupling cancellation at all cuts with rotated cycle-point sizes.
Require a consequence beyond the cycle identity. Improving effective
mixed-block exceptions is secondary: it would still leave the word-
structure gap. No replacement goal or full-cycle proof is claimed.

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
