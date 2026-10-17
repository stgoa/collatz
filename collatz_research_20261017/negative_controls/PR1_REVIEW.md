# Review of PR1: useful controls, with a narrower minimality conclusion

Date: 2026-10-17. Reviewed merged commit `ba6b337`, especially Sections 5
and 12 of `NOTE.md` and `HANDOFF_FOR_MAIN.md`. This review does not edit the
original claims or re-run every independent-lane experiment. The adjacent
checker reproduces the two concrete certificate counterexamples below.
The subsequent integration applies the scope corrections to the note,
handoff, README and ledger. The combined repository verifier also reproduces
all five independent-lane receipts; see the research log for that validation.

**Conclusion.** The negative controls and independent arithmetic checks
are useful. Lemma 4 is sound with its stated cycle hypothesis. Several
subsequent prose conclusions are stronger than that lemma or the finite
evidence supports. In particular, cheapest one-sided certificates need not
be unique. The merged material supports stricter tests for new arguments;
it does not establish that searching for alternative constructions is
mathematically pointless.

## 1. What survives the review

- **C1, independent checks.** The independent implementation and negative
  controls are valuable verification evidence. They remain finite checks;
  the general reductions rest on their written proofs. This focused review
  did not independently repeat the entire reported C1 range.
- **C2, false analogue.** A claimed universal argument cannot rely solely
  on hypotheses also satisfied by a certified counterexample such as
  `T_61`. An inductive step must identify the additional arithmetic it uses.
  This is a scoped logical barrier, not a prohibition on induction itself.
- **C3, Lemma 4.** If `J_0` is finite and exact, `zeta<=0`, and the finite
  difference support contains no nonabsorbing cycle, then `J>=J_0`.
  Following negative predecessors gives exactly the contradiction stated
  in the proof. Applying it to both signs gives uniqueness of an exact
  current within that comparison class. The cycle condition must stay
  attached to the uniqueness statement.
- **C4, progress controls.** A one-pass norm decrease and a large early
  reduction of positive component mass also occur on the false analogue.
  Those statistics alone do not prove finite progress of every remaining
  positive component. This agrees with the programme's explicit open
  termination obligation.
- **C5, class-wise corollary.** The stated equivalence for an invariant set
  avoiding the verified finite base follows from the annular telescoping
  identity and the five-ray maximum principle. It does not provide the
  missing universal certificate construction. Equivalence to the original
  problem is not itself a theorem that the new formulation has no use.

## 2. Minimum positive cost does not imply a unique cheapest certificate

The pointwise inequality `J>=J_0` permits changes at negative entries of
`J_0` without changing `||J^+||_1`. Such changes can also preserve the
required sign of the residual. Therefore the following claims in the
merged prose do not follow:

- "the cheapest valid certificate is forced";
- "Searching for cheaper or alternative currents cannot succeed";
- a universal constructor must describe only the single exact forward sum.

The conditional lower bound on positive cost is valid. The assertion that
there are no alternative valid certificates is false, including at the
same minimum positive cost and on actual annular sources.

### Small exact counterexample using positive Syracuse states

Let

\[
\mu=\delta_{21}-\delta_3.
\]

This is a balanced signed source on two positive odd integers. The relevant
arrows are `21 -> 1`, `3 -> 5`, and `5 -> 1`. With absorption at 1,

\[
J_0=\delta_{21}-\delta_3-\delta_5,
\qquad (I-P)J_0=\mu.
\]

But the different certificate

\[
J=\delta_{21}-\delta_3,
\qquad \zeta=-\delta_5\le0
\]

also satisfies `mu=(I-P)J+zeta`. Both positive costs are 1, and the alternative
has fewer current rows. Their difference is `delta_5`, so the comparison
support is acyclic and the example respects Lemma 4's hypothesis. It does
not refute the lemma: `J>=J_0` exactly as required.

Both costs are minimal even without a global assumption about unknown
cycles. Let `h(x)` indicate that the forward orbit hits 21. Since `21 -> 1`,
`h(x)-h(Sx)=1[x=21]` with the killed convention at 1. For any admissible
certificate `mu=(I-P)K+zeta`, pairing gives

\[
1=\langle h,\mu\rangle=K(21)+\langle h,\zeta\rangle\le K(21).
\]

Thus every such certificate has positive cost at least 1.

### Actual annular example at a required cutoff

For `N=768=12*2^6`, the bounded checker reconstructs `A_768`, verifies raw
source absorption, and computes the full exact current `J_0`. It finds

\[
J_0(5)=-55,\qquad \|J_0^+\|_1=53758,
\qquad |\operatorname{supp}J_0|=40106.
\]

Because `P delta_5=0`, for each integer `0<=c<=55`,

\[
J_c=J_0+c\delta_5,\qquad \zeta_c=-c\delta_5
\]

is a valid certificate of the same positive cost 53758. At `c=55`, row 5 is
absent and the current has 40105 rows. These are 56 distinct integer
certificates, all with the same minimum positive cost.

For completeness, minimality here does not require excluding hypothetical
cycles elsewhere in the Syracuse graph. Every state in `supp J_0` belongs
to the verified absorbing basin. For each such state `z`, the indicator
of hitting `z` has defect `delta_z`. Pairing it with any one-sided
certificate gives `J(z)>=J_0(z)`. Summing over the positive entries of
`J_0` proves the minimum cost 53758. Possible unrelated cycles cannot
decrease those required positive entries.

## 3. Why exact uniqueness does not prescribe the construction method

When all source atoms are known to terminate, the finite sum
`sum_j P^j mu` gives the exact current. Its exactness and minimality are
useful. They do not imply that a successful proof must first expose all
of those orbits, use synchronous transport, or abandon finite-tree search.

For every state `x`, the source `delta_x-P delta_x` has the one-row exact
current `delta_x`. This identity requires no assertion about the future of
`Sx`. The repository's balanced common-tail templates generalize the same
principle. A universal family of such constructions would still need a
coverage or termination theorem; uniqueness does not supply or prohibit it.

For the complete five-ray programme, universal certificates are already
known to imply Collatz. Under that conclusion all forward sums terminate.
This logical equivalence does not establish that every useful constructor
must produce the exact minimum-cost table directly. One-sided certificates,
algebraic descriptions, modular lemmas, and finite searches can supply
different routes to the sufficient hypothesis.

## 4. Bottom traffic: finite facts and their limits

Section 12.1 reports six sampled annuli whose exact forward currents reach
state5 and other entries to 1. The displayed traffic at `N=3072`, and the
estimate `||J_N^+||_1 approximately75N`, are finite observations. Six
samples do not establish a universal law of bottom traffic or a universal
linear cost bound.

Within a sampled absorbing basin, a positive exact-current row is forced
in every one-sided certificate by the hitting-indicator argument above.
A negative exact-current row need not be present: `A_768` explicitly
allows removal of row 5. Thus the universal one-sided statement "the only
candidate is the forced current" cannot support the bottom-traffic claim.

Even a forced positive bottom row does not imply that all source trajectories
must be exposed individually to 1. Nor does residual bottom traffic imply
that there is no cancellation above it. Large partial cancellations and
a nonzero remaining bottom contribution can coexist; the stored current
constructions already exhibit that distinction.

The appropriate conclusions are:

1. the tested exact currents do not annihilate entirely above the bottom;
2. some positive bottom rows are compulsory for those tested sources;
3. the finite evidence does not rule out a different universal proof that
   handles the remaining contribution structurally.

The class-wise equivalence in Section 12.2 is a valid reduction. Phrases
such as "no separate leverage", "three facts together leave no room",
and "there is therefore no cancellation above the bottom to exploit"
are assessments of a research approach, not proved consequences of that
equivalence or these six experiments.

## 5. Implication for the research direction

Keep the negative controls as regression tests for claims intended to be
generic, and identify the exact `d=1` arithmetic in every proposed progress
lemma. Keep the cycle hypothesis on the exact uniqueness claim. Preserve
the distinction between an exact current and the one-sided certificates
allowed by the five-ray criterion.

The remaining task is still a noncircular finite-progress or residual-closure
argument. A pivot based solely on "there are no alternative certificates"
would use a false premise. Whether to pursue a different mathematical
approach is a strategic choice; PR1 supplies useful tests and limitations,
not a proof that the constructor programme is exhausted.

## Reproduce the bounded counterexamples

```sh
python3 collatz_research_20261017/negative_controls/check_review_scope.py
```

This standard-library check uses a hard transport/absorption cap 256 for
`A_768`, verifies the complete divergence of both annular currents, and
compares with `review_scope_audit.json`. The small example is checked by
its three exact arrows. The current tables are reconstructed rather than
duplicated in another stored CSV. `--write-receipt` intentionally refreshes
the compact receipt. No universal Collatz claim is made.

## 7. Reassessment after the delayed-release results

The user requested a fresh opinion on the merged parallel work. A remote
refresh on17 October2026 identifies this same PR1 as the only merged PR;
main already contains both it and the scope corrections. The concrete
counterexample checker above was rerun and passed.

**Decision: a tactical pivot toward recursive descent, while retaining the
current formulation.** C2/C4 make numerical compression an inadequate
progress test. C3 does not prohibit alternative constructions. The useful
next question is whether an exact cancellation supplies an explicit path
from a remaining outer seed to an already absorbed smaller seed, with all
input dependencies accounted for.

The latest optional side feed, reviewed at
`f12da944dc68cfaff0884d874e11bc6c2cb98d34`, independently reproduces the
delayed-release identities and reports sparse negative-source attachment
in a depth16 search. Both new receipts were reproduced in temporary
storage; exact integer height bounds give the same results. See the
[review receipt](../../experiments/residual_progress/side_lane_review_20261017_2005.json).
These observations motivate testing coverage. They do not prove that
later zero-cost attachment is impossible: a bounded search can miss a
deeper backward source. Insufficient negative capacity also does not mean
there are no source attachments at all.

The next batch's [annular-to-complement transfer](../../experiments/residual_progress/complement_recursion/ANNULAR_COMPLEMENT_TRANSFER.md)
makes the proposed progress test precise. Its positive annular atoms are
already certified by smaller ancestors; a capacity-checked cancellation
then certifies selected negative atoms and their outer predecessors.
The delayed family provides actual shrinking branches after unbounded
excursions. Their scope is partial: covering every residual root remains
the main open obligation. This is a concrete reason to redirect the
construction work; it does not claim that the merged PR or the new
transfer solves Collatz.

## 8. Reassessment after the half-size coalescence construction

A further remote refresh again identifies the same merged PR1. The
newer work is on `claude/sidekick`, reviewed at `9a0c28d`; it is not a
second merged PR. The merged control and scope conclusions above stand.

**Decision: focus the constructive work on the explicit complementary
outer family.** The new
[halving identity](../../experiments/residual_progress/residual_return/SHRINKING_COALESCENCE.md)
connects every selected root `x=2^a*t-1`, `t=3^a mod4`, to the smaller
seed `(x-1)/2`. It reduces the leading residual mass by half and works
through unbounded climbs. The opposite binary class remains unresolved.
The [sparse induction](../../experiments/residual_progress/sufficient_sets/SUFFICIENT_SETS_AUDIT.md)
shows exactly why a universal completion of that class would suffice.

The [fixed-h obstruction](../../experiments/residual_progress/phase_depth/FIXED_H_DEPTH.md)
rules out every depth bound depending only on the earlier ternary order,
already when that order is2. This is a reason to change the proposed
recursive state, not a reason to abandon exact currents.

Claude's new feed makes a useful diagnosis: the original R17 support is
the shell's climbing seeds after one- and two-step predecessor lookback.
That relates it directly to the familiar smaller-seed induction problem.
Its finite-bit scans are reproducible, but only test the stated prefix
rules, including a limited merger with one-step images of known seeds.
They do not exhaust arbitrary common-tail bridges to supplied paths.
The measured N^0.93 extrapolation is not a proved integer-count law.
The [durable review](../../experiments/residual_progress/side_lane_review_20261017_latest.md)
records reproduced receipts, the additional direct-prefix checks, and
these scope limits.

Thus the parallel work usefully changes our progress tests. It does not
show that all structural construction methods are exhausted, and the
current batch does not complete Collatz. A successful next step must
close the complementary family or supply a decreasing parameter that
survives every one of its branches.
