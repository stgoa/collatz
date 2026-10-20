# C011 — Root review and completed verification

**Outcome: the scoped written theorem and its declared inputs are
supported. The full cycle objective remains open.** This is model-assisted
research and review, with exact finite execution. It is not a human
review, formal proof, exhaustive literature search or external-computation
replay.

## Proof and source checks

The root read the complete two-arc and obstruction notes, checked the
repeated-word exception, last-letter independence, complementary cut,
strict intercept envelope, amplitude removal, and the three-stage
bounded-q finiteness argument. The separate reviewers explicitly
re-derived these steps. An arc's pure denominator need not be positive;
only the whole word's D is required positive. The optional sharper
factor involving the lower mismatch letter is supported by the proof,
while the finite checker tests its weaker a>=1 corollary.

The root assembled the explicit exclusion and numerical checker. A
separate reviewer read both and independently replayed the checker.
The Matveev statement was inspected in the primary paper containing its
rational formulation. The exact Hercher corollary, its clocks, the
Barina verification interval and the corrigendum were inspected. The
q1 argument uses A<2m from the actual integer cycle. No generalized
cycle inherits the q1-specific published period input.

The marker family's direct denominator bound, unbounded rational
minimum, shortcut minimum count and unique-marker/coprime-total scope
comparisons were checked. They support the stated comparison with fixed
record hypotheses and old repository classes. They do not establish
novelty against all cycle literature.

The root wrote the arbitrary-defect control checker. A separate agent
reviewed and replayed it. That review caught an omitted plateau factor
in the draft GENERAL_DEFECTS prose. The correction is explicitly
recorded there; no theorem, checker or historical result lost that factor.

## Executed evidence

- Root replay of `check_rotation_defects.py` completed with exit0 and
  PASS, comparing the full saved JSON. It covers all2,459 raw cycles,
  1,185 normalized cycles, eleven fixtures,27,646 rotations,192
  two-defect quadratic checks and the separately stated generated cases.
  Separate agents also replayed that unchanged script successfully.
- Root author execution and replay of `check_exclusion_constants.py`
  passed. A separate agent independently replayed it. The exact
  coefficient, boundary and derivative are checked; external theorems
  and computations are not.
- Root author execution of `check_coupled_defects.py` passed. Its final
  source explicitly checks every quotient is exact. The independent
  reviewer replayed this final version and verified source word/state
  correspondence. The three actual controls refute termwise
  divisibility only.
- The pre-existing live historical process, session66447, was polled
  rather than restarted. It completed with exit0. The saved JSON has
  all119 expected fields and every nonmetadata field reports PASS.
  The command was `python3 scripts/verify_all.py --cpp --transfer-controls`.
  This gate verifies preserved infrastructure; it is not a formal proof
  of the new all-size statement.

The final preservation and link audit is recorded in
[delivery_checks.json](delivery_checks.json). It compares all127 earlier
cycle files to the C010 baseline and the frozen R-series ledger and
named infrastructure to9190ccf2519acc56446dd027c6cbf8d45dcceeb6.
The open LaTeX source is unchanged.

## Completion assessment

This batch produces a denominator law, effective bounded-q finiteness
and an all-size q1 exclusion for one intrinsic class. The actual control
set was exercised on the claimed formulas, rather than merely replayed
as a baseline. The source and literature scopes support a genuine
intermediate result under the original success ladder.

The headline is not achieved: no theorem puts every primitive word in
the two-defect class, and no growing lower bound for arbitrary rotation
differences is proved. The next coupled-sum test addresses that gap;
it is not evidence of its solution. Divergence remains outside this
cycle-only claim. Leave the original goal active.
