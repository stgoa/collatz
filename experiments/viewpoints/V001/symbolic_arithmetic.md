# V001 — Symbolic and arithmetic languages: bounded first pass

**Status: exploratory comparison, not a proof programme or a new result.**
The user's breadth-first viewpoint search supersedes the former Phase 6 priority.
No theorem, novelty, formal-verification or convergence claim is made here.
The examples below are elementary exact calculations; proposed tests remain unperformed.

Read before comparison: current `README.md`, `docs/RESULTS.md`, and the source notes for
[R25](../../residual_progress/bridge_normal_form/BRIDGE_NORMAL_FORM.md),
[R31](../../residual_progress/bounded_run_cycles/BOUNDED_RUN_GROWTH.md),
[R49](../../residual_progress/inverse_scope/INVERSE_SCOPE.md),
[integer prefixes](../../residual_progress/integer_prefix/INTEGER_PREFIXES.md),
[itinerary complexity](../../residual_progress/itinerary_complexity/ITINERARY_COMPLEXITY.md),
and [P6-003](../../phase6/growth_norm_transport/GROWTH_NORM_TRANSPORT.md).
The cached independent feed was read at
`54bb81b89e8eb2d8bfc25aa263147669d28e5c19`; no finding from it is used as a premise.

Default dynamics are positive odd Syracuse
`S_d(n)=(3n+d)/2^v2(3n+d)`, stopped at 1, with fixed positive odd d.
Where needed, `C_d` explicitly denotes the **shortcut** clock: even `n -> n/2`,
odd `n -> (3n+d)/2`. Coding on the 2-adics uses its unabsorbed extension.
Neither this shortcut clock nor a symbolic return count is the repository's quotient clock.

## V1. Parity coding: a shift with a difficult arithmetic subset

**1. Objects.** Replace a starting value by its shortcut parity itinerary
`Q_d(x)=sum_(j>=0) (C_d^j(x) mod2) 2^j` in `Z_2`. For odd d this is the
standard shift-conjugacy setting; positive integers are a special countable
subset of that space, not typical 2-adic points. The primary construction is
[Bernstein–Lagarias, equations (1.3), (1.5), (1.6), and §4](https://websites.umich.edu/~lagarias/doc/bernstein.pdf).
For d=1, `Q_1 C_1 = shift Q_1`. The conjecture concerns which coded points come
from positive integers, and whether their tails reach the code of the 1–2 cycle.

**2. Structural gain.** Dynamics becomes a left shift; exact finite prefixes,
branch cylinders and periodic words can be handled without repeatedly tracing
integer paths. This cleanly separates *symbolic availability* from *integer
realization*. It does not transfer Haar-almost-everywhere facts to all positive
integers: that countable set has Haar measure zero.

**3. Translated gap.** Exclude positive integer points from the coded survivor
set. The repository already realizes every finite mixed return word and excludes
eventually periodic survivors in one growing subsystem. Its remaining aperiodic
integer intersection is precisely the missing issue. R25 already provides another
exact quotient; simply drawing a new symbolic graph supplies no progress.

**4. Exact small example.** The shortcut path
`3 -> 5 -> 8 -> 4 -> 2 -> 1 -> 2 -> 1 ...` gives
`Q_1(3)=3+32(1+4+4^2+...)=-23/3` in `Z_2`, whereas
`Q_1(1)=-1/3`. These are codes, not real starting values. The same trajectory
has two odd arrows, with valuation word `(1,4)`. Its exact integer cylinder is
`n=3 mod64`: `S(n)=5+96t`, `S^2(n)=1+18t` for `n=3+64t`.
The shorter five-parity-bit prefix only fixes `n=3 mod32`; the extra bit matters.

**5. `3x+d` control.** For d=5, `19 -> 31 -> 49 -> 19` has odd valuations
`(1,1,3)`. Its shortcut parity word is the periodic `11100`, so
`Q_5(19)=7/(1-32)=-7/31`. Shift coding therefore accommodates a genuine
nonabsorbing positive cycle; it cannot itself distinguish convergence.

**6. Cheapest next test.** Translate one already stored *aperiodic* survivor
language into prefix residues. Ask whether a proposed language restriction
excludes any positive integer beyond the existing integer-complexity bounds.
Stop if it only repeats finite-cylinder counting or periodic-word exclusion.

**7. Genuinely partial milestone.** A proved arithmetic exclusion for one
explicit aperiodic survivor sublanguage, allowing unbounded word lengths and
not already covered by the frozen results. This would shrink a specified
exceptional set without asserting all positive orbits terminate.

**Assessment:** keep as a precision tool; recoding alone is not a new direction.

## V2. A mixed real/2-adic/3-adic affine cocycle

**1. Objects.** Retain each odd valuation word as an affine matrix product,
`x -> (3^k x+d b)/2^A`, with exact integer b and `A=sum a_j`.
View the same rational coefficients at the real, 2-adic and 3-adic places.
The real coordinate records size, binary conditions record exact branch legality,
and ternary conditions record which endpoints have integer predecessors.
This is a proposed arithmetic ledger, not an asserted adelic conjugacy.
[Tao, corrected v7, §1.2, equations (1.3)–(1.8)](https://arxiv.org/html/1909.03562v7#S1.SS2)
provides the exact affine-word framework and retains its offset.

**2. Structural gain.** A word's real slope no longer stands in for its
arithmetic effect. The full offset and both residue constraints remain visible
through composition. For the slope `lambda=3^k/2^A`, the exact product
`|lambda|_infinity |lambda|_2 |lambda|_3=1` displays compensation between
places. It supplies no global contraction. Nor does the same three-place
identity hold automatically for states: additive offsets introduce other primes.

**3. Translated gap.** Obtain a quantitative restriction on the *diagonal
positive-integer states* that can follow an infinite admissible cocycle.
Real contraction, 2-adic precision and ternary congruences separately are
insufficient. The frozen itinerary note already gives different real and
2-adic limits for the same rational sequence. R31 rules out a large class of
finite-label height ranks; P6-003 prevents replacing this gap with contraction
on arbitrary sparse targets. A useful new inequality must genuinely couple
height with evolving arithmetic data.

**4. Exact small example.** For d=1 and word `(1,4)`,
`y=(9x+5)/32`. Its legal positive integer family is
`x=3+64t`, `y=1+18t`, `t>=0`. Inverse integrality requires
`32y-5=0 mod9`, while oddness makes the endpoint class `1 mod18`.
The slope has norms `9/32`, `32`, `1/9`; their product is 1.
The offset `5/32` cannot be discarded. These are two odd arrows, equivalently
five shortcut arrows; the calculation concerns actual integer states.

**5. `3x+d` control.** Word `(1,1,3)` gives
`F_d(x)=(27x+19d)/32`. Its fixed point is `19d/5`.
For d=1 this is a nonintegral rational; for d=5 it is the actual integer
cycle `19 -> 31 -> 49 -> 19`. The same slopes and local norm balance occur
in both. Integer divisibility distinguishes this word, but excluding periodic
words does not settle aperiodic histories.

**6. Cheapest next test.** On one frozen growing family, compare any proposed
mixed-place quantity at the exact entry and exit, retaining the offset and
all valuation guards; repeat on the displayed d=5 cycle. Reject a claim
that is merely a weighted slope sum or a finite-residue height rank.

**7. Genuinely partial milestone.** A uniform integer-realization restriction
for one specified unbounded family of nonperiodic words, stronger than its
separate binary-cylinder and real-slope bounds. Its conclusion should be a
stated exclusion or counting improvement, not a universal termination claim.

**Assessment:** the most useful of these three for locating missing arithmetic
information; no effective coupled estimate has yet been identified.

## V3. Multiplicative semigroup completion versus legal path lifting

**1. Objects.** Use the multiplicative semigroup generated by
`2` and `r_k=(2k+1)/(3k+2)`, `k>=0`. These are inverse-arrow ratios for the
shortcut map `C_1`. Unlike the previous two viewpoints, this deliberately
forgets the ordering and intermediate states of an itinerary.
[Applegate–Lagarias, Theorem 1.1](https://arxiv.org/html/math/0411140v2#S1)
proves the semigroup equals all positive rationals whose reduced denominator
is not divisible by 3. In particular, every positive integer already has an
abstract multiplicative certificate.

**2. Structural gain.** A substantial arithmetic relaxation is completely
solved. Factorization and multiplicative induction become available even when
a Collatz orbit cannot be controlled. This identifies a concrete possible
interface: understand the additional information needed to lift an abstract
certificate to a legal path, rather than proving semigroup membership again.

**3. Translated gap.** A factor `r_k` is a genuine inverse odd shortcut arrow
only when the current state is exactly `3k+2`; multiplying another state by
that same rational is generally not a Collatz move, even if the result is an
integer. Need a legality/order criterion, not just cancellation of rational
factors. R49 rules out universal smaller-ancestor search; changing the name
of that search to semigroup geometry does not avoid its examples. R25's
already complete elementary bridge classes also remain an explicit boundary.

**4. Exact small example.** The factorization
`3=2^3*(5/8)*(3/5)` lifts, in the displayed order, to
`1 -> 2 -> 4 -> 8 -> 5 -> 3` under inverse shortcut arrows.
Read forward, it is five shortcut steps, or two odd Syracuse steps.
Commuting `3/5` to the beginning leaves the product unchanged but sends
`1 -> 3/5`, outside the positive integer lattice. This refutes automatic
lifting of an arbitrary factor ordering, not existence of another legal order.

**5. `3x+d` control.** The corresponding odd ratios are
`(2k+1)/(3k+(3+d)/2)`. For d=5 the identity
`2^2*(49/76)*(31/49)*(19/31)=1` lifts starting at 19 to
`19 -> 38 -> 76 -> 49 -> 31 -> 19` in inverse shortcut time.
It is the same nonabsorbing three-odd-arrow cycle. A unit product may encode
a cycle away from 1. No extension of the published semigroup classification
to all d is assumed.

**6. Cheapest next test.** Inspect one actual multiplication step in the
published semigroup induction. Write its state-dependent legality obligations
and compare them with existing supplied-current interfaces. If the multiplier
merely requests an unproved tripling/doubling certificate, record that circularity
and stop; do not start a large factor search.

**7. Genuinely partial milestone.** A proved lifting criterion for a restricted
class of certificates of unbounded length, with every intermediate state and
clock explicit. A useful success must supply a stated infinite family of
actual paths or identify a provable obstruction to lifting that class.
Membership in the full semigroup is already known and is not a milestone.

**Assessment:** reject unrestricted semigroup completion as a proof route;
retain the legality-of-lifting question for one small diagnostic pass. It is
more distinct than another inverse-tree description, but currently has less
specific promise than V2.

## First-pass comparison

| Viewpoint | Information made easier | Information still missing | First-pass decision |
|---|---|---|---|
| V1: shift coding | Prefixes, tails, periodicity | Positive-integer intersection of aperiodic survivors | Diagnostic language; avoid repeating frozen prefix work |
| V2: mixed-place cocycle | Joint slope, offset and congruence bookkeeping | A genuinely coupled integer-realization bound | Keep for comparison with other proposed viewpoints |
| V3: multiplicative semigroup | Abstract arithmetic factorization | Legal, ordered state-by-state realization | Reject membership-only route; permit one lifting diagnostic |

All three are established mathematical languages. None presently supplies a
new inequality, infinite-family certificate or convergence theorem here.
