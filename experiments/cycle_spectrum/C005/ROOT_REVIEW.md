# C005 — Root review and delivery scope

**2026-10-19. PASS within the scopes below.** This is an independent
agent argument and code review, not human peer review, formal verification
or a novelty claim. The all-cycle goal remains open.

## Mathematical review

I read the final [proof](ORDER_THEORY.md) and independently followed the
ratio-envelope argument. Each full rotation map contracts toward its own
base-cycle state, so the mixed block boundaries lie in the base interval.
For a positive affine prefix, its output ratio is between 1 and the input
ratio. Therefore all intermediate states lie in `[l/R,Rh]`, giving
`H/L<=R^3<8`. No independence assumption about phases is used.

The three-band integer step retains the exact odd gap
`3r-q*(2^k-1)`. At q1, k1 is strictly positive and k2 is nonnegative;
equality contradicts the distinct-successor property of a simple cycle.
Ordered normalized images give a transitive rank rotation and coprime
primitive totals. For r blocks repeated p times, coprimality of the base
totals gives p dividing r and primitive gcd r/p. The period-one endpoint
is handled separately. Denominator 1 therefore forces p=r, leaving just
the known base cycle. The fixed-point exception `(2)` is retained.

The prime-base high family uses cyclic periods dividing the full length.
Any such period must be a multiple of the reduced slope denominator m0;
the primitive phase word 001011 then forces six full blocks. Its minimum
bound and shortcut minimum count are separate from odd-only minima.

The q233, q5 and q11 controls establish the stated failure scopes.
Mechanical normalized exponents alone do not remove height weights from
the original intercept. The new theorem supplies neither denominator
growth nor a decomposition of arbitrary words. Its literature comparison
concerns the direct fixed-count and mechanical exclusions only.

## Code review and independent execution

I read both new checkers. They use exact integer and Fraction arithmetic,
replay raw valuations, distinguish primitive periods from repetitions,
and bind their stored receipts to source hashes. The block checker tests
every intermediate state against the envelope and explicitly recognizes
the common-base property. Actual-cycle matching tests every possible
alignment for the candidate primitive base totals. No finite search is
promoted to a theorem.

- `check_order.py`: separate root replay PASS, covering all 2,459 source
  cycles, 739,757 normalized state pairs, the declared generated-word
  grid, eleven fixtures and separate inversion controls.
- `check_mechanical_blocks.py`: separate root replay PASS, covering
  9,664 grid concatenations, 227,860 raw arrows, 36,700 boundaries,
  forty-eight fixed-base controls and twenty prime-base examples.
  All 2,459 actual source cycles are independently replayed again;
  22 normalized cycles match the rotation class, three with mixed blocks.
- `python3 scripts/verify_all.py --cpp --transfer-controls`: PASS.
  The independent C++ checks at 4096 and 262144 and all eleven raw
  transfer cycles pass. This gate checks the historical infrastructure;
  the new C005 tests above have their own receipts.

The final proof hash is
`bf1048e6de6c90bbc477c34b061b73435afc0d61553fd6309c4595c1ef929a44`.
The separate [review](INDEPENDENT_REVIEW.md) records another agent's
proof audit and exact arithmetic examples. The
[delivery receipt](delivery_checks.json) checks preservation, links and
the final file fingerprints.

## External and delivery limits

The side branch was read at the pinned commit in [SIDE_REVIEW.md](SIDE_REVIEW.md).
Repeated fetch attempts were not executed because automatic approval
review failed with its model at capacity. Freshness is unconfirmed.
The reported Lean results were not independently replayed on main;
they do not formally verify C005. No side branch or open LaTeX document
was edited. Commit and push status belongs to the delivery message and
is not implied by these mathematical checks.
