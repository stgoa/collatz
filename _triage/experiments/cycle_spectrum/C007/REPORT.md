# C007 — A height-denominator candidate and two exact obstructions

**Status: bounded progress on identifying failed mechanisms.** The proposed
law `B<=q-1` survives the actual-cycle tests and remains unproved. C006
remains the strongest order-dependent denominator restriction in this
programme. The all-cycle headline and the ordered denominator-one
intermediate target remain open.

## The mechanism tested

For a primitive positive rational raw odd-only cycle, write its odd
numerators and reduced common denominator as
`3n_i+q=2^a_i n_(i+1)`, with exact `a_i>=1`. There is no absorber.
Let `L=min n_i`, assume `q<=L`, and set
`h_i=floor(log_2(n_i/L))`, `B=max h_i`. As in C005/C006, require that
successors preserve circular order after dividing each state by its
height power of two. The selected candidate is

> Every such cycle satisfies `B<=q-1`.

At q1 this would force B0. The narrow classification and mechanical
denominator theorem would then leave only the trivial fixed point.
No proof puts every possible integer cycle in the ordered class.

## What the arithmetic attempt established

[HEIGHT_DENOMINATOR.md](HEIGHT_DENOMINATOR.md) proves the exact modular
identity

```
z_i = n_i/2^h_i = L 3^i 2^(-P_i) (mod q),
P_i = sum_(j<i) c_j,     c_j=a_j+h_(j+1)-h_j.
```

Every numerator is a unit modulo 6q. For fixed normalized word c and
initial residue, the modular dynamics loses the height profile entirely.
The ordered q5 cycle beginning at 187 has raw residue 2 at all four
heights 0,1,2,3. Normalized residues also overlap between height levels.
Thus the proposed injection from height levels to disjoint residue
classes is false. This is a failure of that specific mechanism; other
arguments combining congruences, order and integer constraints remain
available.

Overlap does not rule out choosing one distinct representative for each
height. Indeed the displayed raw q5 sets admit the choices
`0->2, 1->3, 2->1, 3->4`. No general matching theorem is proved here.
The scope was tightened during review before publication.

The follow-up [matching audit](RESIDUE_MATCHING.md) finds distinct
representatives for every observed height in all 1,184 tested cycles
with q>1, using either raw or normalized residues. This includes all
51 ordered cases. The denominator-one fixed point was omitted, and
no theorem extends the matching property to hypothetical q1 cycles.
This refined mechanism remains open; a finite pass is not a proof.

The [independent probe](INDEPENDENT_ARITHMETIC.md) records another exact
failure. Divide the ordered q5 cycle beginning at 347 by 5. Its rational
coordinates satisfy the additive-1 equations, with positive exponents,
correct heights, order, and B3. The first cleared gap becomes 96/5.
Real order inequalities alone therefore cannot force the integer
denominator-one conclusion. The reduced denominator stays 5; this is
not an integer Collatz cycle.

The necessary min-to-top inequality
`3(n_i-2^B L)>q(2^B-1)` also permits arbitrarily large B in its pairwise
relaxation. Actual cycles must satisfy the full weighted intercept
condition `D L=q C_h`, including oddness, exact divisions and all rank
inequalities. Neither modular cancellation nor the pairwise relaxation
is a counterexample to `B<=q-1` itself.

## Actual-cycle discrimination

The [checker](check_height_denominator.py) first replays all 2,459 C001
source cycles across 333 parameters, yielding 1,184 distinct normalized
cycles and retaining all 11 raw control fixtures. It then runs a new
deterministic bounded seed census:

| Parameter d | Largest odd seed |
|---|---:|
| 5 | 4,000,001 |
| 7,11,13,29 | 2,000,001 |
| Other positive d<=97 coprime to6 | 200,001 |

Across 33 parameters, 8,800,033 odd seeds required 13,998,115 newly
evaluated arrows. The declared limits are 20,000 steps per new path,
512 state bits, and 10,000,000 new arrows per parameter. No seed was
capped or left unprocessed. Memoization stores only paths already
connected to exactly closed cycles. Separate cap tests check unresolved
behavior; this census makes no statement about seeds beyond its ranges.

The new census finds 180 source cycles and 89 distinct normalized cycles.
One was absent from C001: q29, minimum 7055, maximum 1,051,393, odd
period 41, total exponent 65, B7, J38, and cancellation factor
14,499,716,215,459,201. Seed 5859 reaches it after 12 raw odd steps.
Its full states, valuations, order and source seed are stored in
[height_denominator_audit.json](height_denominator_audit.json). Discovery
relative to the repository is not a novelty claim.

The combined set has 1,185 normalized cycles, 51 in the ordered domain.
The candidate survives every stored cycle, including the unordered
ones. Its broad finite success consequently does not identify circular
order as the decisive ingredient. The nearest existing ordered examples
remain the q5 period 17 cycles, with B/(q-1)=3/4. The new q29 cycle has
ratio1/4. Stronger logarithmic and half-linear candidates already fail
on exact controls.

## High-level goal recommendation

**Prove that every positive primitive rational cycle whose normalized
successor preserves circular order has reduced denominator greater than
one, apart from the trivial cycle. Allow arbitrary period, height and
number of height changes.**

This would eliminate an entire structural class at every size. It is a
genuine intermediate milestone: unordered cycles and divergent orbits
would remain unresolved. The proposed `B<=q-1` is one possible mechanism,
not a required theorem or evidence that this route will succeed.

The next bounded investigation should couple the full divisibility
`D|C_h` at q1 with legal odd numerator heights and rank inequalities.
A two-band calculation is useful only if it exposes an argument that
can handle unrestricted height complexity. Another wider seed census
currently has little discriminatory value. New searches should be
driven by a specific proposed obstruction or counterexample family.

Fable's reported Lean work strengthens confidence in earlier statements;
it does not supply the new arithmetic argument. The separate lane now
reports both directions of C004's narrow classification, while the R71
unit-gcd input and integer corollary remain pending in that report. Main
has not independently replayed those Lean builds. See
[SIDE_REVIEW.md](SIDE_REVIEW.md).

## Verification and preservation

The mathematical note has a separate agent review. The census has an
author replay and separate root replay. A second implementation checks
the modular identity, integer weighted intercept and exact shortcut
counterexamples; see [check_arithmetic_obstructions.py](check_arithmetic_obstructions.py)
and [arithmetic_obstructions.json](arithmetic_obstructions.json).
[ROOT_REVIEW.md](ROOT_REVIEW.md) records the final verification outcome.
These are written arguments and finite checks, not formal verification
or a novelty assessment.

C005/C006 publication recovered during this batch: commit
`1cb02fae9fb31e03cfc1ba7ec26b964995b3c1e2` was pushed successfully to
origin/main. Their earlier failed-attempt notes remain as historical
records. This batch preserves those proofs and receipts, R1-R94, the
dispatcher, and the open LaTeX document.
