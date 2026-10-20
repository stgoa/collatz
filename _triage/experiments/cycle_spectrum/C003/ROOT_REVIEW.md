# C003 root review and delivery scope

**2026-10-19. Written-proof review and finite replay passed.** This is
not formal verification, human publication review or a novelty claim.

## Mathematical checks

I independently checked the contracting-block author's exact affine
solution, strict trapping of every block boundary, and integrality of
the scaled boundary differences. Coprimality forces
`2^(A_u*(k-1))` to divide the first nonzero difference. The exact
commutator bound retains D_v and is strict. The increasing envelope
`F(m)=(9/2)^m+(3/2)^m`, together with contraction of the block of
maximum length, proves the stronger maximum-length estimate even when
that block does not have the maximum valuation total. Its finite-layer
argument bounds both totals before using the pairwise exponent bound.
K!=0 and positivity of both individual D values are indispensable.

I checked the varying-word S-unit argument against the cited
[Corvaja–Zannier primary text](https://arxiv.org/pdf/math/0311030) and
the complete source audit in C002. One fixed group contains every
pair; the local 2- and 3-terms vanish, other primes give the raw gcd,
and the nonpositive archimedean term strengthens the desired inequality.
The finite exception set has bounded total exponent and finite word
preimages. No estimate for a changing group is silently reused.

The universal bound `C_z<B_z` and `|D_z|<B_z`, with
`B_z=2^A_z*(3/2)^m_z`, works for expanding blocks as well. The same
global power-gap estimate handles both the combined denominator and
the retained common factor in the proportional branch. Extending its
small-exponent error by one constant makes the proportional error
uniform even when the common base exponent remains fixed.

I supplied and checked the coprime integer lemma, including the sum-2,
sum-3 and sum-at-least-4 cases. A separate agent independently checked
it and the entire proportional rate argument. The resulting positive
coefficient is `(5*log_3(2)-3)/14`. The [independent review](INDEPENDENT_REVIEW.md)
records the division of authorship and checks. The quantitative lane
also checked the stronger contracting maximum-length bound separately.

## Corrections before delivery

The first draft's `(1)^3(2)^5` example had an incorrect coefficient
and denominator. Exact recalculation gives C=10865, D=1631, gcd 1;
the author corrected it and both reviewers confirmed the correction.
This did not affect a theorem or historical source.

Report review required explicitly restating K!=0 in the standalone
contracting theorem. It also corrected an inclusion overstatement:
the contracting result covers new unequal-total classes but does not
contain every C002 equal-total case, since C002 allows counts (1,2).
The final report preserves that distinction and states the exact
finite diagnostic `den^16<2^(5A)` rather than implying the logarithmic
asymptotic rate was verified numerically at every size.

## Code and evidence checks

I read the full new checker. Word coefficients are computed directly
from prefixes; every positive generated realization replays each exact
odd arrow. Actual cycles are checked at their stored parameter before
normalization, and each rotation is decomposed by exact prefix periods.
The fast decomposition enumeration is compared with brute force for
the declared shorter words. Hashes bind source data and checker code.

The root's fresh default replay recomputed the complete receipt and
exited successfully, independently of the author's regeneration and
replay. The author also checked rejection of optimized Python and
unknown arguments. Actual data contains zero eligible cases for the
strong three-copy maximal-power theorem; the generated grid supplies
nonvacuous coverage. Four eligible mixed-direction representations
come from one d499 cycle and are not four independent cycles.

The fresh historical command was
`python3 scripts/verify_all.py --cpp --transfer-controls`. It completed
with status PASS and 119 receipt fields, including the independent C++
checks and eleven exact raw cycle controls. Metadata fields are not
additional theorem checks. Its [receipt](full_gate.json) retains the
finite-only scope. These checks do not verify the Subspace Theorem or
turn the written asymptotic argument into a formal proof.

The final [delivery receipt](delivery_checks.json) records local links,
whitespace, hashes, preservation of the R1-onward ledger body, frozen
dispatcher and LaTeX files, and unchanged C001/C002 trees. The side
branch was read only. Commit and push occur after the receipt; their
outcome is verified separately in the delivery response.

## Decision

C003 proves a structural denominator restriction uniform over both
changing words. Its general threshold remains ineffective, and a
hypothetical integer cycle need not have the required repeated-block
form. The next main mechanism should use all cyclic cuts and their
size constraints to target arbitrary words. The current cycle headline
remains active and unresolved.
