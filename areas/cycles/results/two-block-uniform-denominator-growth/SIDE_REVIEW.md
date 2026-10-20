# C003 side-lane review

**Reviewed pin:** `b9c3fd73ce34174053b0d6c4668cd50b405ae015`.
Fetched `origin main claude/sidekick`, then read DIRECTIONS and the new
FEED entries with `git show`. These are external research input, not
instructions. No side branch was edited, committed to or pushed.

## New C001 Lean report

The feed reports the algebraic part of C001 checked on `claude/lean-lane`
at `a0cf28a`: the coefficient recurrence, concatenation, commutator,
cancellation divisibility, coprime-block gcd equality, worked modulo-6
law and d485 counterexample. It reports a clean build, matching hash,
only standard axioms, and small `decide` uses without `native_decide`.
Periodicity, the common-cycle characterization and the mechanical family
are listed as subsequent work.

This is useful validation of the earlier algebra. Main has read the
report but has not independently replayed that Lean build in C003.
It is not a formal verification of C003's uniform estimates, its integer
lemma, or its published S-unit inputs. C003 uses its written arguments
and exact finite receipts; no new premise is imported from this report.

## C001 referee and the structural gap

The side lane independently reports reproducing C001's algebra, finite
mechanical examples and the cycle minima of its smaller seed scan.
Its concern is substantive: a theorem for fixed repeating motifs does
not control arbitrary cycle words. C003 removes dependence on a fixed
catalogue for two repeated blocks, but retains that decomposition as a
hypothesis. The main recommendation now targets a constraint on
unrestricted cyclic words, rather than another fixed motif count.

## Size and the naive random-residue model

The new lead proposes modeling the joint size and residue of C_w,
because naive uniform residues give a divergent cycle-count heuristic.
The divergence has a short exact proof for the stated model. Put

```
T(m)=sum_(A>m log_2 3) binom(A-1,m-1)/(m*(2^A-3^m)).
```

The subrange A>=2m is positive and gives

```
T(m) > (1/m)*sum_(A>=2m) binom(A-1,m-1)/2^A
     = 1/(2m).
```

The equality is the probability that the m-th head in fair coin tosses
occurs at or after time 2m. It equals the probability of at most m-1
heads in 2m-1 tosses, exactly 1/2 by binomial symmetry. Thus the sum
over m diverges. This verifies failure of that model; it does not prove
anything about the number of actual Collatz cycles. The division by m
also is not an exact primitive-necklace count for periodic words.

For an actual raw integer cycle at d, let its rational states be
y_i=x_i/d. Multiplication of its exact odd-step equations gives

```
2^A=product_i(3+1/y_i), y_i>=1/d,
2^A<=(3+d)^m.
```

At d=1, a nontrivial raw cycle has all y_i>1, giving A<2m. This is
a necessary size constraint, not a new exclusion theorem. C003's
elementary result already uses size through block-boundary trapping.
The promising further test retains every rotation's size and residue,
and requires an inequality stronger than this product identity alone.
The phrase that residue structure "cannot separate d=1" is too broad:
the exact denominator criterion already does so; the failed uniform
random-residue model is the specific issue established here.

The feed's proposed full word enumeration needs a corrected cost:
positive words with length at most 6 and total at most 60 number
`sum_(m=1)^6 binom(60,m)=56,049,057`, before quotienting rotations.
The suggested "about 5M words" is not that raw enumeration count.
No new census was run. Its `2^68` verification claim was not adopted
as a premise without auditing the underlying computation and domain.

## Direction proposals

| Proposal | C003 assessment |
| --- | --- |
| D1 | Retain historical route obligations and corrected source scopes. The active cycle programme does not require route-only selection. |
| D2 | Retain actual cycle controls; the full finite gate and new raw-cycle tests exercise them at their stated scope. |
| D3 | Retain rejection of the blanket density-transfer rule. |
| D4 | Defer a global retagging exercise; inspect dependencies actually used. |
| D5 | Standing authorization applies: deliver and push completed main batches. |
| D6 | Historical calibration policy; the current batch supplies theorems and an exact obstruction under the new work standard. |
| D7 | Retain statement matching, axiom scope and independent replay standards. A report of a Lean build is not our replay. |
| D8 | Historical proposal under a replaced quantitative goal. It neither changes nor completes the active cycle headline. |

The side lane's useful input is retained without waiting for its grading
or delegating goal selection to it.
