# V006 — Independent verifier review

**Status: PASS for the bounded checks after a receipt-serialization fix,
2026-10-18.** This review is separate from the written universal proofs
and does not establish the active all-invariant quantitative goal.

## Material and replay

The reviewer read the complete [verifier](verify_examples.py), its
[receipt](verification.json), the [quadratic proof and pattern control](overlap.md),
and the [abstract-action control](joint_literature.md).

The final independent command was

```
python3 -B experiments/viewpoints/V006/verify_examples.py
```

It passed under Python 3.9.6 and matched the unchanged receipt. The checked
source SHA-256 is

```
9da809e0997850c136ba52be587d68ae7a68815ab068d9efd5ae06fa9f212608
```

and agrees with the receipt's `verifier_sha256` field. The digit-weight
helper uses `bin(n).count("1")`, which was exercised successfully by that
Python version.

### Draft correction found during independent replay

The first replay completed all arithmetic checks but failed the final
receipt comparison. `reachable_parameter_counts` contained Python tuples,
while reading the JSON receipt produced lists. The reviewer compared all
receipt fields and found this to be the only difference; no arithmetic
value or witness hash differed.

The author changed the parameter-count rows to lists and regenerated the
receipt. The reviewer then replayed the saved source independently with
the default, non-writing mode. This was a verification-tool correction;
no mathematical statement or proof was corrected.

## Quadratic mixed-section witnesses — PASS

The verifier checks 18 balanced blocks: r=1,...,6 and one through three
repetitions of the order-length block. It verifies divisibility by 3^r,
the odd endpoint, the half-weight formula and the subtract-one formula.

At total mixed depth 6 there are 28 parameter states. For each of two
offsets, 0 and 3, it constructs a distinguishing integer for every pair,
giving 756 comparisons. The different-shift branch uses `n=2^k-1`;
the different-dilation branch uses `n=2^k-c` with the exact rational-block
choice of c. The checker verifies both digit-weight identities and their
integer endpoint conditions before comparing colors.

These explicit comparisons use F equal to the indicator of positive
powers of 2. They supplement the general proof for arbitrary
non-eventually-periodic F. They do not provide finite witnesses uniform
over all such F or prove the universal theorem by enumeration.

## Adjacent-11 control — PASS

The identity `N_11(n)=s_2(n & (n>>1))` counts every adjacent pair,
including overlapping pairs in a longer run of ones. The replay checks
65,280 section evaluations, through depth 8, against the exact formula

```
F(t+N_11(n)+epsilon*(n mod2)).
```

The receipt reports counts of reachable **parameter pairs**. The verifier
uses only their upper bound `<=2D`; it does not infer equality of unknown
whole functions from these counts. The all-depth upper bound rests on
the displayed formula in the proof note.

The doubling and positive-return identities are checked for 4,096 inputs.
For each of the 15 reached parameter pairs the checker finds two even
integers with equal binary digit count but different colors. This
exercises the stated obstruction to being a digit-count function on
those parameters. The universal no-digit-count-section statement and
infinitude of every descendant kernel remain written arguments. The
actual full-guard failure at 3->10 is explicitly checked.

## Abstract action and dynamical controls — PASS

The root-orbit check for T,U runs through depth 32 and checks the linear
interval bound and the lower bound supplied by repeated T. For words of
lengths 1 through 7, the verifier checks 10,795 pairwise distinguishing
inputs. The first differing letter is placed at a power of 2 beyond 4D;
later iterates lie strictly between that power and the next, so the
one-unit difference persists. The receipt correctly identifies these as
abstract maps, without claiming that they realize affine sections.

For d=5 and d=61, the verifier checks divisibility colors, their odd fixed
cycles d->d away from absorber 1, doubling invariance and the guarded odd
equations on the declared finite ranges. It skips the outgoing odd
equation at source 1. A final scoped addition directly exercises failure
of the d1 graph-root identity b(3n)=b(4n): n=3 for d=5 gives colors (0,1),
and n=10 for d=61 gives colors (1,0). The reviewer inspected this addition
and independently replayed the final saved verifier and regenerated
receipt; both matched. These are controls for the stated maps and domains,
not tests of hypothetical divergence.

## Execution and claim boundaries

All computations use exact integers. The program rejects Python
optimization mode, so its assertions cannot silently disappear under
`-O`. A failed assertion or exhausted finite witness search stops the
program; no unresolved case is counted as a pass. The default invocation
only reads its source and receipt. Writing requires the explicit
`--write-receipt` option. There are no network requests or subprocesses.

The source hash and full receipt comparison identify the concrete replay.
The receipt explicitly separates finite checks from universal proofs and
the unresolved quantitative target. With these boundaries, it is suitable
evidence for this new bounded batch. The historical Phase6 gate was not
needed or run by this reviewer.
