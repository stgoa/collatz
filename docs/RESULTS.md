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

## C1 — Independent audit of R2–R4 and of main's R5, R6, R9, R10

**Status: finite checks and model-assisted re-derivation; no discrepancy found.**

The audit re-derived Theorems 1 and 3 and rechecked them with an independent implementation. That implementation reproduces the repository packets exactly.

- **Theorem 1, (3):** the transfer identity holds exactly for every `8 <= N <= 160` and every horizon up to extinction.
- **Theorem 1, (2):** the core-remainder bounds hold for every `N <= 10^5` and for 3,132 sampled `N` up to `10^18`.
- **Table (7):** the dyadic table holds for `b <= 1500`.
- **(6):** the valuation partition passes a non-vacuous orbit-indicator test.

A least counterexample cannot be `2 mod 3`, so the least-exception route always gives pairing −1. **The `N^(3/2)` maximum principle is therefore load-bearing for statements 2 and 4.** It is not redundant.

The same independent construction also cross-checks two results committed on main in `8d62dcc`:

- **Five-ray criterion (main's R5):** its exact cutoffs, upper targets, comparison exponents, sub-96 boundary points, and `89/90` constant hold for all five rays and `3 <= b <= 400`.
- **Annular recursion (main's R6):** `Pi_(64N)=Pi_N+A_N` and `eta_(64N)=eta_N` hold, together with the supports, all 36 band coefficients, band totals, `||A_N||_1=99N/2`, `||A_N^+||_1=99N/4`, `|supp A_N|=267N/8`, and `sum y A_N(y)=63Q`. Checked for 68 cutoffs, up to expanded cutoff 262144.

The written five-ray proof was re-read and no gap was found.

This is not human peer review or formal verification. See the [negative-controls note](../collatz_research_20261017/negative_controls/NOTE.md), Sections 4, 6 and 10, and the receipts [reduction_audit.json](../collatz_research_20261017/negative_controls/reduction_audit.json) and [main_claims_audit.json](../collatz_research_20261017/negative_controls/main_claims_audit.json).

Main commit `ce56699` makes two further claims that were checked here as well:

- **R9:** `||P A_N||_1=||R A_N||_1=171N/4-|c_N|` for 68 cutoffs; the `2N` survivors; and `c_80000=0`, using an independent point evaluator.
- **R10:** `Phi(A_96)=17` at exposure depths 20–27, and `0` at depth 28.

Numbering note: the C-series comes from an independent lane (branch `claude/claude-vs-chatgpt-perf-8230f6`). It is kept separate from the R-series so the two numberings never collide.

## C2 — Negative controls on 3x+d and a scoped barrier

**Status: written lemmas plus finite certificates.**

Consider the maps `T_d(x)=(3x+d)/2^v` with `d=2^k-3`; these fix 1, and for `d>1` they also fix `d`.

- **The construction carries over.** The same right-aligned packets and a counting identity with explicit edge terms both transfer to `T_d`. The identity is checked non-vacuously.
- **The criterion fires where the conjecture is false.** Every surveyed map with nontrivial cycles has cutoffs where `<e,Pi_N> > 0`. At such a cutoff, no finite current with nonpositive residual exists and packet work grows linearly. Finite orbit certificates verify both facts.
- **`d=61` is a locally Collatz-like control.** All its core points and all seeds below 175 terminate, and the obligation holds for every `8 <= N <= 212`. It then fails at `N=213`, because of a 41-cycle with minimum 235.

Consequently, no argument that applies verbatim to `T_61` can discharge the primary obligation for `3x+1`. This includes induction on N that uses only those generic properties.

See [note](../collatz_research_20261017/negative_controls/NOTE.md), Sections 1–3, and [receipt](../collatz_research_20261017/negative_controls/negative_controls_audit.json).

## C3 — Certificate minimality

**Status: written proof; finite check against the archive.**

Suppose an exact finite current `J_0` exists for `mu`. Then every finite certificate `mu=(I-P)J+zeta` with `zeta<=0` satisfies `J>=J_0` pointwise, provided its difference support contains no nontrivial cycle. In particular `J_0` is unique and minimizes `||J^+||_1`.

When all atoms terminate, `J_0=sum_j P^j mu` is the time-aggregated forward push. The archive's stored currents equal this forward aggregate row for row: 2,736 rows at `N=4096` and 132,998 rows at `N=262144`.

**There are no cheaper certificates to search for.** A universal constructor must give a uniform description of the single object `J_N` and prove that it is finite. See [note](../collatz_research_20261017/negative_controls/NOTE.md), Section 5.

## C4 — Progress measures that do not separate 3x+1 from 3x+61

**Status: finite certificates.**

Consider the 64-fold increments `A'_N=Pi'_(64N)-Pi'_N` of `T_61`, at `N=8,16,24,32`.

- **Compression looks the same.** Their one-pass compression ratio is `0.849–0.863`, compared with `19/22≈0.864` at `d=1`.
- **Early exposure looks the same.** `Phi` falls by about 97% within 25 exposure depths.
- **But `Phi` never reaches zero.** At depths up to 400, `Phi` equals the pairing `<e,A'_N>`, which is 6–13. The surviving component contains the whole 41-cycle, so it can never join an absorber.

Hence neither one-pass contraction nor early `Phi` decay is evidence that `3x+1` plateaus end. See [note](../collatz_research_20261017/negative_controls/NOTE.md), Section 11, and [receipt](../collatz_research_20261017/negative_controls/progress_measures_audit.json).

## Open obligations and priorities

- **Primary:** construct a finite current (or one with nonpositive residual) for every integer cutoff in the revised family, and prove termination. Arbitrarily large finite cost is permitted.
- Find an arithmetic recursion or another structural mechanism that controls unresolved positive contributions. Finite successful trajectory searches alone do not prove universal existence. By C3, the per-cutoff certificate is forced, so the mechanism must describe `J_N=sum_j P^j Pi_N` uniformly. By C2 and C4, it must use arithmetic false for `T_61`. Run any candidate constructor or checker on the C2 controls; it must fail at `(d,N)=(61,213)` and `(-1,16)`.
- Independently audit the written reduction, including the cutoffs, absorption, every-integer quantifier, and maximum principle. C1 is a second, independent model-assisted pass that found no error; there is still no human peer review or proof-assistant verification.
- Treat the earlier analytic mixing extension as a separate candidate with its own external dependencies. It is not needed for R2–R4.
- Keep historical failures and scoped results in the master handoff available. No Collatz proof, logarithmic mean-work theorem, or general cheap-current theorem is established here.
