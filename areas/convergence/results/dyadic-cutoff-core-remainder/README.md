---
id: dyadic-cutoff-core-remainder
kind: result
title: At dyadic cutoffs N = 2^b the core remainder is 6-periodic in b, so the transfer error lies in [−12, 1]
status: reviewed
claim: >
  Odd-only clock, absorbing at 1, right-aligned packets Π^R_N. For N = 2^b, b ≥ 3, the core remainder
  η_N depends only on b mod 6 (table (7): no mass at 11), and for every T ≥ 1,
  H_(T−1)(Π^R_(2^b)) − 12 ≤ 3E_T(2^b) ≤ H_(T−1)(Π^R_(2^b)) + 1. This is a statement about dyadic cutoffs
  only; it does not establish the every-cutoff hypothesis of qualitative-current-criterion, and packet work
  is not nonpositive in general (H_39(Π^R_32) = 57).
authors:
  - ChatGPT main lane (Codex)
created: 2026-10-17
depends_on: [right-aligned-fixed-core-remainder]
evidence:
  - "../right-aligned-fixed-core-remainder/right_aligned_packets.py (certificate of that node): checks table (7) and the correction range [−12, 1] for 3 ≤ b ≤ 1000, and H_39(Π^R_32) = 57"
  - "../locally-collatz-like-control-barrier/reduction_audit.py, reduction_audit.json: the PR1 lane's independent check of table (7) for b ≤ 1500"
reviewed_by:
  - by: Claude PR1 lane (Opus)
    date: 2026-10-17
    link: ../locally-collatz-like-control-barrier/NOTE.md
    scope: "Finite only (NOTE §6, ledger C1): independent code confirms the period-6 table and the correction range [−12, 1] for b = 3…1500. The written periodicity argument was not among the arguments the audit says it re-derived (Theorems 1 and 3), so the status stays written"
  - by: Claude review lane (Fable 5.1; directed by Santiago Armstrong)
    date: 2026-10-31
    link: REVIEW-2026-10-31-claude-review-lane.md
    scope: "Full argument re-derived (the shift identities q_(a+6) = 64 q_a + 21 and M_(a+6) = 64 M_a, the floor step, the coefficient invariance, the zero total of the six new valuations where b >= 3 enters, <1, nu> = -1 and the correction range) and checked by independent code: table (7) for b = 3..2000, the periodicity mechanism for b = 3..119, and (8) end to end from the definition of E_T for b = 3..12 at every horizon; the evidence certificate right_aligned_packets.py re-run (PASS, exit 0, 3 s); controls not applicable. Verdict HOLDS; two imprecisions and one remark, no correction"
aliases: [R4]
tags: [convergence, packet-currents, right-aligned, dyadic]
---

# At dyadic cutoffs N = 2^b the core remainder is 6-periodic in b, so the transfer error lies in [−12, 1]

## Statement

Notation of [`right-aligned-fixed-core-remainder`](../right-aligned-fixed-core-remainder/README.md). For `N = 2^b`, `b ≥ 3`, the core remainder `η_N` depends only on `b mod 6`:

```
b mod 6 | η_N(5)  η_N(7)  η_N(13)
   0    |   2      −1       0
   1    |  −1       1      −1
   2    |  −1       0      −2
   3    |  −1      −1       0
   4    |  −1      −2       2
   5    |   2      −3       1                                                              (7)
```

There is no mass at 11. Consequently, for every `T ≥ 1`,

```
H_(T−1)(Π^R_(2^b)) − 12 ≤ 3E_T(2^b) ≤ H_(T−1)(Π^R_(2^b)) + 1.                                (8)
```

## Proof

From §3 of [`papers/right-aligned-reduction`](../../../../papers/right-aligned-reduction/README.md), kept as written.

To prove periodicity, increase `b` and `a` by 6. The cutoffs multiply by 64, while `q_(a+6) = 64·q_a + 21` and `M_(a+6) = 64·M_a`. Since `n_i − q_a` is odd, subtracting `21/(64·M_a)` does not change the floor of its quotient. The shifted sources are `64·x_t + 21 ≡ x_t (mod 3)`, so their coefficients are unchanged. Thus each old valuation has the same lift count and residual coefficients at the shifted valuation. The six new valuations `a = 1, …, 6` contribute zero in total: odd `a` have no leftovers, and even `a` contribute the vectors `(−2, 1)`, `(1, −2)`, `(1, 1)` on `(7, 13)`, which sum to zero. Direct arithmetic at `b = 3, …, 8` gives (7).

Since `⟨1, ν_(2^b)⟩ = −1`, substituting the core hitting times `τ(5) = 1`, `τ(7) = 5`, `τ(13) = 2` into (7) gives (8) through the identity `3E_T(N) − H_(T−1)(Π^R_N) = ⟨1, ν_N⟩ + H_(T−1)(η_N)` of the fixed-core theorem. ∎

The "direct arithmetic at `b = 3, …, 8`" base cases are checked by [`right_aligned_packets.py`](../right-aligned-fixed-core-remainder/right_aligned_packets.py), which recomputes `η_(2^b)` for every `3 ≤ b ≤ 1000` and the correction `−1 + Σ_x η(x)·min(L, τ(x))` for `L = 0, …, 6`.

## Remarks

- **Scope.** The equivalence [`qualitative-current-criterion`](../qualitative-current-criterion.md) quantifies over every integer cutoff; this dyadic computation alone does not establish its hypothesis. The separate sampling theorem [`five-ray-current-criterion`](../five-ray-current-criterion/README.md) (legacy R5, five dyadic rays) handles that.
- **A sign guard.** Do not infer that all packet work is nonpositive: `H_39(Π^R_32) = 57`, checked exactly by the certificate above. The criterion is boundedness above for each cutoff, not a universal zero upper bound. The PR1 lane's table of the all-horizon work `W(N) = sup_L H_L(Π^R_N)` (legacy `NOTE.md` §7) shows `W(N)` small at dyadic `N` (`W(512) = 193`, `W(1024) = 8`, `W(2048) = 12`), consistent with (8), while the forced current cost is not (finite observation).
- Novelty undetermined.

## History

- Migrated from the legacy ledger entry R4 (`archive/docs/RESULTS.md`, legacy path) and §3 of `papers/right_aligned_reduction/right_aligned_reduction.tex`, now [`papers/right-aligned-reduction/right-aligned-reduction.tex`](../../../../papers/right-aligned-reduction/right-aligned-reduction.tex), at commit `be73a66`, by the B07 migration (Claude, Opus 5.5). Legacy status: "written exact formula; finite checks". The legacy ledger names the direct packet decomposition for every `8 ≤ N ≤ 2048` and `N = 4096, 10001, 262144` among R4's checks; it belongs to the fixed-core theorem and is listed there.
- Main lane (ChatGPT, Codex), 2026-10-17.
- 2026-10-31: reviewed by the Claude review lane (Fable 5.1; directed by Santiago Armstrong); status raised to reviewed. No correction to the claim or proof. The node was moved from `dyadic-cutoff-core-remainder.md` to `dyadic-cutoff-core-remainder/README.md` to hold the review file, with its relative links and the PR1 review link repointed; the review records two imprecisions (the zero total of the six new valuations is where b >= 3 enters; <1, nu_(2^b)> = -1 is asserted without derivation) and that both bounds of (8) are attained. See [`REVIEW-2026-10-31-claude-review-lane.md`](REVIEW-2026-10-31-claude-review-lane.md).
