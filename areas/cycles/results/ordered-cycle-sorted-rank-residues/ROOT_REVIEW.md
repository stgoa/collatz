# C008 root review

## Written mathematics

The normalized chronological recurrence is valid modulo every divisor
Q of reduced q. Unit residues require gcd(Q,6)=1 and reduced
numerators; primitive period alone would not supply numerator reduction.
With coprime totals, Bezout gives a generator t with `t^m=2,t^A=3`.
Substituting the mechanical prefix `floor(iA/m)` leaves the least
nonnegative rank `Ai-m floor(iA/m)`, giving the sorted progression.
This is stronger placement information than cyclicity alone; cyclicity
already follows from coprime totals without circular order.

I checked the lattice basis `(ord_d2,0),(a,b)` from the quotient group
`<2,3>/<2>`. Its first Smith factor divides both coordinates of every
relation. The stated factors35/65/91 therefore cannot divide a reduced
ordered denominator. The premise `q<=L` and circular order is essential
to obtaining coprime totals here. The stored corpus includes114
unordered q<=L cycles with noncoprime totals, and actual cycles at
the excluded factors survive outside the theorem domain.

For normalized Hall through B2, the minimum arrow gives two distinct
height-zero residues; adjacent height bands cannot share one singleton;
the full normalized orbit has at least three values. These exhaust the
subsets of at most three height levels. The separate sorted proof gives
at least four values when B2, and agrees. Raw Hall through B1 uses only
the minimum arrow. None of these proofs applies at q1, where all
residues coincide. Full Hall and the target exclusion remain open.

## Corrections and exact failures

1. The prior top ledger said C007 rejected residue injection. Its
   actual counterexample rejects disjoint residue sets; matching remains
   possible. The ledger is corrected, with old batch files preserved.
2. A draft raw B2 extension to arbitrary divisor Q was withdrawn after
   an exact q5077565 cycle failed Hall modulo5. Normalized B2 survives.
3. In a larger height graph, a minimal Hall failure can be a pair of
   nonadjacent bands; the next-test row was corrected to retain that case.
4. Distinct normalized residues do not by themselves prove raw matching.
   The independent note now gives separate verified assignments for both
   graphs at the full q of each projected counterexample.

The proper-divisor controls are exact primitive positive cycles,
with the indicated reduced q, odd valuations, heights and order.
They do not refute matching modulo full q. The primewise proof route
is rejected, not the full-denominator candidate.

## Independent verification

- The author matcher and separate root full replay both PASS at script
  SHA256 `f8d63a71dc57206386c35cfcadba62a29969f1405aa8be665fa39158e99d1f39`.
  Receipt SHA256 is
  `8be1fb6414481b333f36cd007e4542a2c9e009d6339afd7fb3771b6e79b7361a`.
  They retain all11 fixtures,2459 source cycles,1185 normalized cycles,
  946001 screened profiles, both matching conventions and the exact
  projected failures. All13 retained small-q construction cases are
  already known. No added evidentiary weight is assigned to that grid.
- The independently implemented spectrum checker passes author write,
  root replay and a separate agent replay:332 moduli,477552 relation
  cells,1185 cycles,51 ordered nonfixed cases. It validates exact sorted
  normalized and raw residues and preserves noncoprime controls.
- The seven-state difference between the side's modular count and C007
  is exactly the q>1 fixed points; both counts are reproduced.
- [ARITHMETIC_REVIEW.md](ARITHMETIC_REVIEW.md) and
  [CHECKER_REVIEW.md](CHECKER_REVIEW.md) record separate proof inspection
  and exact replays. No review is a claim of human peer review, novelty
  or independent Lean kernel verification.
- The required historical gate completed with exit0 and all119 report
  fields checked; C++ and transfer controls passed. Its receipt and the
  preservation/link checks are saved
  in [historical_gate.json](historical_gate.json) and
  [delivery_checks.json](delivery_checks.json). Publication requires
  their completed PASS receipts, not a running process. The delivery
  checker was corrected to read the matching receipt's descriptive
  status field as scope text, rather than expecting a literal PASS;
  the already successful mathematical replay and its receipt did not change.

The all-cycle objective remains active. All-height ordered q1 exclusion
is an intermediate recommendation, and q>1 small-band gains are not its
completion. The open LaTeX document and frozen historical mathematics
are preserved.
