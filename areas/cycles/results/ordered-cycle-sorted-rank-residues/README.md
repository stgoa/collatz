# C008 — Sorted residue structure and the limit of primewise matching

**Status: written elementary structural results and exact counterexamples;
full height-residue matching and every ordered denominator-one exclusion
remain open.** Raw positive odd cycles are used throughout, with no
absorber. This batch tests one mechanism: assign different residues to
different dyadic height levels, modulo the actual reduced denominator.

## What changed

Let a primitive numerator cycle satisfy `3n_i+q=2^a_i n_(i+1)`, with
`q` reduced and coprime to 6. Let `L=min n_i`,
`h_i=floor(log_2(n_i/L))`, `B=max h_i`, and `z_i=n_i/2^h_i`.
The ordered domain requires `q<=L` and circular normalized successor
order, equivalently increasing images `3z_i+q/2^h_i` in sorted z order.
For a nonfixed cycle, C005 gives `A=m+s`, `gcd(A,m)=1`, where s is
the successor rank shift.

The [independent arithmetic note](INDEPENDENT_MATCHING.md) proves the
exact sorted-rank law. Choose `um+vA=1` and put `t=2^u3^v mod q`.
For `q>1`,

```text
t^m=2, t^A=3,
z_[j] = L t^j (mod q),
n_[j] = L t^(j+m H_j) (mod q).
```

Thus normalized collisions occur precisely at equal rank classes modulo
`T=ord_q(t)`. Distinct normalized ranks modulo T make normalized
matching automatic; this observation does not remove the height shift
from raw residues. Neither formula supplies a bound on the admissible
height profile.

The [main proof](MATCHING_ARITHMETIC.md) supplies a second consequence:
`<2,3>` modulo q must be cyclic. More generally, if a divisor d of q has
noncyclic `<2,3>`, q cannot occur in this ordered domain. In particular,
**35, 65 and 91 cannot divide q**, at any period or height. The proof
is elementary and follows from the already established coprime totals;
no novelty or new denominator-one exclusion is claimed. The exact
relation-lattice test is `e(d)=gcd(ord_d(2),a,b)>1`, with
`2^a=3^b mod d` and b the least positive exponent entering `<2>`.

For `q>1`, normalized height sets have distinct representatives when
`B<=2`; raw sets do when `B<=1`. The independent proof also shows these
small-band assertions for every divisor `Q>1` of q. They do not extend
to q1: its only residue is zero, so the central arithmetic case is
still missing. Minimal Hall failures can involve two nonadjacent bands,
even when B is larger than two.

## A precise failed shortcut

The assertion that each prime factor separately permits height matching
is false. Two exact ordered cycles have reduced
`q=2^27-3^17=5,077,565`, period17 and `q<=L`:

| Minimum L | B | Failure modulo the proper divisor5 |
| ---: | ---: | --- |
| 446400719 | 3 | Normalized levels {1,3} have only residue {4}; raw levels {1,2,3} have only {2,3}. |
| 365289811 | 2 | Every raw height set is {1,4}, so three heights cannot be matched. |

Both raw and normalized graphs match at the full reduced q. The first
counterexample even has four levels and four available units modulo5;
its failure concerns a proper subset, beyond a global cardinality test.
The second retracts the initially considered raw B2 general-divisor
extension. These are actual positive cycles with exact valuations and
verified order, not formal height profiles. Full words, states and
proofs are in the independent note and [finite receipt](height_matching_audit.json).

## Evidence and its limits

- Both full-q matchings pass on all 1,185 stored normalized cycles,
  including q1 with its sole residue0. Of these, 51 are nonfixed ordered
  cycles. Only 11 raw and 4 normalized ordered graphs have overlapping
  height sets; many other passes follow automatically from disjointness.
- All eleven raw transfer fixtures and all 2,459 source cycles across
  333 parameters are checked, including 1,275 scaled instances and
  36,912 source arrows. Primitive cycles and scaled copies stay separate.
- A targeted extension screens 946,001 positive profiles across 17
  selected coprime totals through period17. Only 13 realize reduced
  q<=31; all were already known. This adds **no new substantive finite
  evidence** for full-q matching. Bounds and selection are in the receipt.
- A [separate implementation](check_residue_spectrum.py) checks the
  exact relation lattice at 332 moduli through1000, in 477,552 finite
  cells, and independently checks all stored cycles and sorted residues.
  Actual cycles with factors35/65/91 survive outside the theorem domain.
- [Root review](ROOT_REVIEW.md), [checker review](CHECKER_REVIEW.md),
  [arithmetic review](ARITHMETIC_REVIEW.md), the historical gate and
  delivery receipt distinguish written reasoning, finite checking and
  preservation. No C008 formal verification is claimed.

## Decision and next mechanism

The high-level intermediate target remains: **exclude all nontrivial
ordered positive integer cycles, without bounds on period, height or
height-change complexity.** It is subordinate to the active all-cycle
headline. The new q>1 results do not close any q1 case.

The next bounded attempt should target the full integer obstruction:
combine `D|C_h` at q1 with all sorted-rank gap inequalities and the
height legality constraints. The primewise matching route is rejected;
the full-q Hall statement is retained only as an unproved sufficient
mechanism. Proving another fixed-band q>1 case may diagnose a proof,
but is not the next high-level goal. Repeatedly increasing B would
leave the central case untouched.

One bounded way to test the missing integer mechanism is to cut at a
positive-height excursion between height-zero states. Retain its exact
integer affine relation
`2^A_seg*n_exit=3^length*n_entry+q*C_seg`, its valuation cylinders,
the complementary path closing the cycle, and every sorted-rank
inequality. Valid open excursions alone cannot be excluded. The desired
gain is a consequence at q1 that is not just the original closure
identity or a bounded-height case. If one bounded symbolic pass merely
recovers `D|C_h` with no additional restriction, pivot the mechanism;
do not treat that reformulation as progress or expand a band ladder.

Fable's reported Lean work now includes C005's q1 three-band structural
theorem on actual odd cycles, not their exclusion. Main has not replayed
that build; it supplies no new premise here. See [side review](SIDE_REVIEW.md).
The [literature scope](LITERATURE.md) records primary-source checks and
the absence of a novelty or cycle-record claim.
