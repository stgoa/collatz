# C011 — A complete two-rotation-defect exclusion

**Status: written structural exclusion and bounded-denominator
finiteness, supported by independent agent reviews and exact finite
checks. The all-cycle goal remains active and unresolved.** Published
analytic and computational inputs are explicit; no novelty or formal
verification is claimed.

## Main result

If a positive valuation word differs from one of its nonidentity cyclic
rotations in exactly two positions, its reduced rational-cycle denominator
is greater than one. There is no bound on its period, state height,
valuation alphabet, mismatch amplitude or shift gcd.

Thus no hypothetical nontrivial integer Collatz cycle can have such a
rotation. This applies to the full word, including arbitrary intervening
blocks. It leaves all primitive words whose rotations differ in at
least three positions. Divergence is separate.

## Why the estimate works

The two mismatches are swapped valuations a,a+k. Cutting at each of
them produces complementary arcs u,v. With `g=gcd(C_w,2^A-3^m)`,

```
g divides (2^k-1) gcd(C_u,C_v).
```

Keeping each arc's unused terminal valuation is decisive. The
[elementary proof](ROTATION_DEFECTS.md) gives

```
g^2 < (2^k-1)^2 2^(A-m-k) 3^m,
q > (1-3^m/2^A)(2/sqrt(3))^m.
```

The second inequality uses only positivity and k<=A-m, so it has no
amplitude cap. A published effective logarithm estimate makes this
exponential denominator growth up to a polynomial loss. At bounded q,
the proof first bounds m, then A-k, then A. Consequently every bounded
denominator layer of the entire two-defect class is finite, effectively
in principle. No complete enumeration or practical cutoff is supplied.

The [explicit q1 argument](EXCLUSION.md) combines the estimate with
Matveev's explicit constant and a published odd-period lower bound
obtained from Hercher and Barina. Its rational boundary margin is
2,450,000,000 and the derivative lower bound is 373/2750. The cited
computational inputs were not rerun here; the local checker verifies
only their endpoint compatibility and the displayed numerical deductions.

## A concrete infinite class beyond fixed record hypotheses

For n=2^r-1, take a lower mechanical block b_n of length n and total
ceil(n log_2 3), and the word `(3,b_n,4,b_n)`. Its half-period rotation
has two unit mismatches. Every rational state exceeds n/128, while the
shortcut local-minimum count tends to infinity. A direct elementary
bound gives q>1, without the imported period or logarithm inputs.

Unique markers and coprime totals separate it from the stated previous
block classes. Its growing minimum and local-minimum count exceed any
fixed cutoffs in the compared published records. The
[literature audit](LITERATURE.md) explains why this is a scope gain,
not a universal numerical record or a novelty claim.

## The failed simpler mechanism is also preserved

The primitive family `1^t 2^(2t)` has two unit mismatches, but

```
g_t=gcd(4^t-1,3^t-2^t)
```

can contain every prescribed modulus coprime to6. The
[counterfamily proof](DEFECT_OBSTRUCTIONS.md) is elementary and gives
exact growing powers of5. Counting mismatches or amplitudes alone cannot
bound the absolute cancellation. The successful theorem retains period
and arc arithmetic and bounds cancellation relative to the denominator.

Extra reduced-denominator factors in rotation gcds are retained. Actual
q35 and q505 controls refute identifying the two-arc bound with g.
All generalized-cycle controls survive at their actual reduced q.

## Evidence

The [rotation receipt](rotation_defect_audit.json) retains all2,459
raw source instances across333 parameters, all1,185 normalized cycles,
and all11 fixtures. It checks27,646 rotations and1,481,154 word
positions. The192 two-defect rotations supply384 oriented arc identities
and192 checks of each quadratic bound. The108 eligible actual cycles
include22 with unit-amplitude two-defect rotations.

Separate generated checks cover51 cancellation-family examples, twelve
prescribed moduli, nineteen repetition controls, and eight marker cases.
The marker cases check1,020 exact raw arrows and1,012 rotations.
Finite checks support the formulas; they do not establish the all-size
claims or replay external analytic or computational proofs.

[Arithmetic review](ARITHMETIC_REVIEW.md),
[independent exclusion review](INDEPENDENT_REVIEW.md),
[checker review](EXACT_CHECKER_REVIEW.md), and
[root review](ROOT_REVIEW.md) identify their authorship, hashes and
verification scopes. The [constant receipt](exclusion_constants.json),
[historical gate](historical_gate.json), and
[delivery checks](delivery_checks.json) have separate purposes.

## Next mechanism: coupled differences at arbitrary complexity

[GENERAL_DEFECTS.md](GENERAL_DEFECTS.md) shows exactly why the proof
cannot be extended term by term. The actual q97 cycle has three
mismatches, and its difference is `100=36+64`: g=5 divides the total
but neither contribution. Actual q233 and q359 examples give the same
failure with four and six mismatches. Their
[exact receipt](coupled_defect_controls.json) verifies stored membership
and actual arrows.

The next bounded test combines all cyclic cuts while retaining this
coupling. Seek one denominator estimate valid for an arbitrary mismatch
count, with a consequence for every possible q1 cycle. A lower bound
on rotation mismatch count growing with period would be a meaningful
intermediate theorem; C011 supplies only the constant bound3.
Another sequence of fixed-count exclusions is not the programme.

C010 was completed progress; the intervening strategic answer did not
complete any further cycle objective. This continuation resumed the
existing C011 work and polled its confirmed live historical gate rather
than restarting it. The original goal was neither replaced nor completed.
The [side review](SIDE_REVIEW.md) records external reports and the
unchanged distinction between discovery and formal verification.
