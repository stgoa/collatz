# C011 — Published inputs and scope comparison

**Status: primary-source statement audit, 2026-10-19.** The proof notes
separate elementary deductions, imported analytic estimates, published
computational results and this repository's finite replays. None is
presented as independent formal verification or a novelty assessment.

## Analytic inputs inspected

- Bugeaud, [B′, Theorem 1.1(1.2), p.2](https://arxiv.org/pdf/2209.00275).
  With the fixed bases 2,3, degree one and coefficients A,-m, the theorem
  gives an effective polynomial lower bound on the nonzero logarithmic
  form when A<2m. C011 uses this to prove bounded-denominator finiteness.
  The separate A>=2m branch is elementary. No practical cutoff for the
  full bounded-q classification is computed.
- Languasco–Luca–Moree–Togbe,
  [Theorem 2.1](https://link.springer.com/article/10.1007/s12188-025-00293-9),
  states the positive rational product-minus-one version of Matveev.
  C011 applies it directly to `2^(-A)3^m-1`, retaining the explicit
  coefficient and using B=2m only after the integer-cycle product bound.
  The rational estimate replacing its coefficient by 600,000,000 is
  checked locally. The analytic theorem itself is imported.

## Integer-cycle input inspected

Hercher's [2023 paper, Corollary 29 and Remark 30](https://cs.uwaterloo.ca/journals/JIS/VOL26/Hercher/hercher5.pdf)
provides the odd-period implication from a specified convergence cutoff.
Barina's [2025 paper, section 6](https://link.springer.com/article/10.1007/s11227-025-07337-0)
reports a verification range strictly containing that cutoff. Exact
thresholds, endpoint containment and the clock translation are stated
once in [EXCLUSION.md](EXCLUSION.md). These published computations were
not rerun here. Barina's separate total-length number is not substituted
for an odd-only count.

The [corrigendum](https://cs.uwaterloo.ca/journals/JIS/VOL26/Hercher/corrigendum.pdf)
repairs a tail estimate in Theorem 21. Corollary 29 uses the separate
Lemma 26 method; the inspected correction does not change its statement.
Main and a separate reviewing agent checked this distinction. Reading a
published proof and correction is not independent execution of its code.

## Existing word and cycle structure

Gabrić's [Words that almost commute](https://arxiv.org/html/2110.01120v2)
studies words at Hamming distance two from a conjugate. Thus this
combinatorial class and its rotation viewpoint are established objects.
C011 gives its own shift-graph argument and does not import an unread
classification as a proof of the arithmetic estimate.

The affine word formula, rational realization and concatenation algebra
are classical background, audited in [C001's literature note](../repeated-block-cancellation-bound/LITERATURE.md).
The adjacent unit-defect case is the already covered mechanical class.
The two-arc proof explicitly distinguishes that case from separated
mismatches and from extra gcd factors.

## What goes beyond the earlier scoped exclusions

The marker family `(3,b_n,4,b_n)`, with n=2^r-1 and b_n a lower
mechanical block, is primitive with coprime total and length. Its
rational minimum is greater than n/128 and its shortcut local-minimum
count is `2(ceil(n log_2 3)-n)+2`. Both grow without bound.
The written elementary denominator exclusion therefore covers a family
outside fixed minimum and fixed local-minimum-count assumptions,
including the Simons–de Weger and Hercher scopes audited in C001.
This is a comparison of hypotheses, not a larger universal numerical
record or a claim that no published method could also treat the family.

Unique markers, coprime totals and growing marker separation distinguish
this family from the stated C001 fixed-block, C002 equal-total,
C003 doubly repeated and C005 common-base classes. Full literature
priority for the arithmetic theorem is unassessed. The main gain is an
all-period structural exclusion and a general bounded-denominator
finiteness theorem within the two-defect class; neither covers arbitrary
valuation words.
