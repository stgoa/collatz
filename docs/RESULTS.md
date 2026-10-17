# Result ledger

Last updated: 2026-10-17. This ledger summarizes scope; the linked proof notes and exact data contain the supporting arguments.

## R1 — Exact source transport and original packets

**Status: inherited written proofs and finite certificates.**

The master handoff develops exact cylinders, the stopping-work recurrence, the signed source measure `nu_N`, and the original packet decomposition. Finite currents cancel unknown common futures, including unequal arrival times. See [master handoff](../COLLATZ_PROGRAMME_MASTER_HANDOFF.md), Sections 2–10, and the [original research note](../collatz_research_20261017/collatz_packet_currents/research_note.md).

The original complete tables certify all-horizon packet work in `[-1406,2364]` at `N=4096`, depth 2, and `[-57661,63824]` at `N=262144`, depth 4. These are two finite source cutoffs, not a uniform theorem. Python and independently compiled C++ verification passed at both cutoffs.

Archive SHA-256: `025c8fafe25940951fe408b32b1ec806259725a6b4f8855d9f2b022911fe5447`. All 31 original manifest entries were checked.

## R2 — Right-aligned depth-one fixed-core remainder

**Status: written elementary proof; finite implementation checks.**

For every integer `N >= 8`, form complete triples from the right in each valuation cylinder and source component. Then

`P nu_N = Pi_right_N + eta_N`, with `supp(eta_N) ⊆ {5,7,11,13}` and `||eta_N||_1 <= 6 ceil(log2 N)`.

Over-budget one-step valuations map to 1 and are killed. The four residual states have odd-only hitting times `1,5,4,2`, respectively. Hence, for every `T >= 1`,

`|3 E_T(N) - H_(T-1)(Pi_right_N)| <= 8 + 30 ceil(log2 N)`.

This is a new grouping. The original current tables cannot be relabeled as certificates for it. Full argument: [current proof note](../collatz_research_20261017/right_aligned_reduction.tex), Theorem 1. Implementation and receipts: [script](../collatz_research_20261017/right_aligned_packets.py), [audit](../collatz_research_20261017/right_aligned_audit.json).

## R3 — Qualitative current criterion

**Status: written equivalence; its universal hypothesis remains open.**

The following are equivalent:

1. Collatz holds.
2. For every integer `N >= 8`, the right-aligned packet work has a finite upper bound over all horizons; this bound may depend arbitrarily on N.
3. Every such packet family has a finite exact current.
4. Every such packet family has a finite current with an everywhere nonpositive residual.

The proof uses the nonhalting indicator and its source-count recurrence. The count satisfies `B <= L B`; the comparison function obeys `L(N^(3/2)) < (505/512) N^(3/2)` for `N >= 16`. A positive global maximum of `B(N)/N^(3/2)` is impossible. A separate least-exception argument checks the exact-current implication.

See [current proof note](../collatz_research_20261017/right_aligned_reduction.tex), Lemma 2 and Theorem 3. No inverse-basin theorem or uniform current-cost estimate is needed for this route. No universal constructor or termination proof has been established. The equivalence does not reduce the logical strength of the unresolved conjecture.

## R4 — Dyadic remainder and a sign guard

**Status: written exact formula; finite checks.**

For `N=2^b`, `b >= 3`, the core residual is periodic in b modulo 6, and for every `T >= 1`:

`H_(T-1)(Pi_right_N) - 12 <= 3 E_T(N) <= H_(T-1)(Pi_right_N) + 1`.

The proof uses `q_(a+6)=64 q_a+21` and cancellation of the six new valuation classes. The full formula appears in the current proof note. The reproducible audit checks b from 3 through 1000, as well as direct packet decomposition for every `8 <= N <= 2048` and `N=4096,10001,262144`.

Do not infer that all packet work is nonpositive: the exact finite witness is `H_39(Pi_right_32)=57`. The criterion is boundedness above for each cutoff, not a universal zero upper bound.

## Open obligations and priorities

- **Primary:** construct a finite current (or one with nonpositive residual) for every integer cutoff in the revised family, and prove termination. Arbitrarily large finite cost is permitted.
- Find an arithmetic recursion or another structural mechanism that controls unresolved positive contributions. Finite successful trajectory searches alone do not prove universal existence.
- Independently audit the written reduction, including the cutoffs, absorption, every-integer quantifier, and maximum principle. Current review is computational and model-assisted; there is no human peer review or proof-assistant verification.
- Treat the earlier analytic mixing extension as a separate candidate with its own external dependencies. It is not needed for R2–R4.
- Keep historical failures and scoped results in the master handoff available. No Collatz proof, logarithmic mean-work theorem, or general cheap-current theorem is established here.
