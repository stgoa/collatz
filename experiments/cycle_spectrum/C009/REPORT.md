# C009 — Excursion compression does not supply the missing obstruction

**Status: the proposed automatic compression mechanism is rejected by
written arithmetic and exact actual-cycle counterexamples. No new
denominator-one cycle exclusion is obtained. The full cycle-spectrum
goal remains active.** The previous C008 turn was progress: its published
results and counterexamples selected the present bounded test.

## Mechanism tested

Cut an ordered primitive positive odd cycle at each visit to its minimum
dyadic band `[L,2L)`. Try to use exact excursion congruences and a simpler
ordered return map to force descent or an additional denominator
restriction. Keep the original complement closing every excursion;
all statements use the raw odd-only clock without an absorber.

Three parts of this proposed mechanism fail in precisely different ways.

### Exact cuts preserve the lattice but add no congruence

For a positive valuation block with length ell, total A and exact
intercept C, positive odd endpoints satisfying

```text
2^A y = 3^ell x + q C
```

already force every intermediate state to be an odd integer with the
prescribed exact valuation. The [written proof](EXCURSION_ARITHMETIC.md)
uses each prefix of the true intercept. Its exact cylinder has modulus
`2^(A+1)`; the odd endpoint is essential.

Closing any number of such blocks has a cyclic integer matrix with
Smith form `diag(1,...,1,D)`, where `D=2^A_total-3^m`. Its integrality
condition at q1 is the original `D|C_full`. This is the block form of
C004's single-obstruction calculation. It supplies no independent
filter. Replacing the true weighted intercept by the unweighted
mechanical one *does* lose the lattice: in the q13 control below it
sends431 to1985/4 instead of493.

### Circular order is not inherited

The exact ordered q13 cycle

```text
283 -> 431 -> 653 -> 493 -> 373 -> 283
```

has one state above its minimum band. Its full normalized successor is
a shift by3 on five sorted ranks. Delete653 and retain first returns:
the sorted core `(283,373,431,493)` has successor ranks `(2,0,3,1)`,
which is not a circular shift.

The [one-point deletion theorem](FIRST_RETURN_ORDER.md) proves the
general obstruction: inducing a coprime shift s on m ranks after
deleting one rank preserves a circular shift exactly when s=1 or s=m-1.
Interior shifts produce two different regular rank displacements.
This holds at all periods under its hypotheses; it does not assert
actual Collatz cycles at every period or exclude q1 cycles.

### Excursions have no automatic descent sign

In the q13 cycle, `431 -> 653 -> 493` rises and has slope9/8. A
contracting slope is also insufficient: the ordered q83 cycle with
minimum157 has excursion `277 -> 457 -> 727 -> 283`, satisfying
`32*283=27*277+83*19`. Its slope27/32 is below1, yet it rises by6.

Even at q1, open positive odd paths can have either sign while their
sorted normalized images increase locally: `7 -> 11 -> 17 -> 13`
has a rising excursion, and `19 -> 29 -> 11` a falling one. These
are explicitly **open paths**, not counterexamples to cycle exclusion.
They show why local excursion shape and local order alone cannot
supply a signed drift assertion.

## Exact finite evidence

[The excursion checker](check_excursions.py) retains all 2,459 original
source cycles across333 parameters, all11 fixtures, scaling data, and
the C007 addition, giving1,185 distinct normalized cycles. It checks
2,593 first returns and28,831 prefix cylinders with complementary
closure. The ordered domain contains51 nonfixed cycles and the q1
fixed point:

| Ordered-domain observation | Count |
| --- | ---: |
| Height-zero first returns | 177 |
| Returns traversing positive height | 60 |
| Positive excursions that descend / rise | 48 / 12 |
| Positive excursions with contracting / expanding slope | 50 / 10 |
| Contracting positive excursions that rise | 2 |
| Cycles whose induced core loses circular order | 12 |

The [independent checker](check_return_order.py) verifies the deletion
formula on105,388 finite permutations through m80, totaling6,250,510
arrows. It also reconstructs16,368 positive odd endpoint pairs across
q1/5/7/13 and76,464 exact arrows. These constructed paths are not counted
as cycles. Two actual controls are replayed independently.

The [independent argument](INDEPENDENT_EXCURSION.md),
[arithmetic review](ARITHMETIC_REVIEW.md), [checker review](CHECKER_REVIEW.md)
and [root review](ROOT_REVIEW.md) separate proofs, author runs,
independent runs and preservation. The historical gate is separately
recorded. No novelty, formal verification or cycle-record improvement
is claimed; see [literature scope](LITERATURE.md).

## Decision and next mechanism

The bounded excursion pass reached its pivot criterion. Exact algebra
returns the old divisibility condition, and the proposed ordered
induction class is not closed under the compression. Reject that
automatic recursion and a local drift proof. Do not enlarge an
excursion catalogue or a fixed-band ladder as a substitute.

The next bounded mechanism should use **global integer rounding in
the complete sorted-gap system**, retaining every height, odd-state
condition and the dyadic seam. A useful cut must distinguish the
integer lattice from the rationally rescaled q5/q13 controls and yield
an inequality beyond `D|C_h`. Pure real inequalities are already
insufficient by C007; identifying the same congruence again is not
progress. No such new rounding inequality is asserted here.

The intermediate all-height ordered q1 exclusion and the headline
exclusion of all nontrivial cycles remain open. Unordered cycles and
possible divergent orbits are separate unresolved questions. The
[side review](SIDE_REVIEW.md) records reported Lean progress without
importing an unverified formal premise.

## High-level recommendation after the user's question

The next substantial milestone should be a complete exclusion of
nontrivial integer cycles whose dyadically normalized successor preserves
circular order, without any bound on period, height or height changes.
This is the existing intermediate target under the all-cycle headline;
this recommendation does not activate a replacement goal.

The payoff is explicit. C005 proves that any hypothetical primitive q1
cycle with H<8L has that order. Completing the proposed exclusion would
therefore imply H>8L for every nontrivial integer cycle (H=8L is impossible
for positive odd endpoints), and would also exclude ordered cycles with
arbitrarily large height range. This is an implication within our ledger,
not a claim of novelty or an improvement over a published numerical record.
Unordered cycles and divergence would remain open.

Order is a working hypothesis, not an established explanation of Collatz.
C007's candidate also survives unordered controls, and C009 refutes the
automatic recursion. The next bounded discrimination is the complete
integer-gap rounding mechanism above. If it supplies only the old
divisibility identity, needs an unproved complexity bound or fails an
exact control, retire that mechanism and reassess the role of order.
Further fixed-band lemmas do not complete the all-size milestone.

Fable's Lean lane is useful for validating stable statements and exposing
hidden premises. Its reported V004 assembly retains Cobham as an explicit
hypothesis; its cycle work formalizes specific algebraic and order results.
Neither substitutes for the missing global argument. The latest branch
pins and scopes are recorded in the side review.
