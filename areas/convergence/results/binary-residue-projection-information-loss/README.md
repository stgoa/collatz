---
id: binary-residue-projection-information-loss
kind: result
title: Every fixed binary-residue view eventually sees each annular band as the zero measure
status: reviewed
claim: >
  Odd-only 3x+1 map; A_N the six-band annulus of disjoint-annular-recursion. Fix K ≥ 1. If 2^(K+2) | N, then
  in each of the six bands separately, Σ_(y in band j, y ≡ r mod 2^K) A_N(y) = 0 and
  Σ_(y in band j, y ≡ r mod 3·2^K) A_N(y) = 0 for every residue r. So any test function depending only on the
  band index and the residue modulo 2^K or 3·2^K pairs to zero with the annulus, and for each fixed K all
  sufficiently large cutoffs on the five rays satisfy the hypothesis. This is an information-loss statement
  for these quotients only; methods keeping residues modulo 9, exact offsets, carries, symbolic parameters or
  checked integer lifts are not excluded, and no unbounded aggregate-depth result is proved.
authors:
  - ChatGPT main lane (Codex)
created: 2026-10-17
depends_on: [disjoint-annular-recursion]
evidence:
  - "../exposure-potential-boundary-flux/check_duality.py, duality_audit.json (a certificate of that node): all eight materialised projection cases K = 1, …, 8"
reviewed_by:
  - by: Claude review lane (Fable 5.1; directed by Santiago Armstrong)
    date: 2026-10-31
    link: REVIEW-2026-10-31-claude-review-lane.md
    scope: "Full proof re-derived (row sums on the two classes mod 6, periods 9*2^K, residue-visiting lemma, complete periods per band) and verified by independent code in 42 cases K = 1..7 plus the nonvacuity of the hypothesis; node converted to a folder; evidence script check_duality.py re-run (exit 0); verdict HOLDS"
aliases: [R10-b]
tags: [convergence, packet-currents, annular, finite-state, information-loss]
---

# Every fixed binary-residue view eventually sees each annular band as the zero measure

## Statement

Odd-only clock; `A_N`, `Q = 9N/4` and the bands `2^j·Q < y < 2^(j+1)·Q` as in [`disjoint-annular-recursion`](../disjoint-annular-recursion/README.md). This is an aggregate identity for the actual six-band measures, not an argument about isolated triples.

**Theorem.** Fix `K ≥ 1`. If `2^(K+2) | N`, then in each of the six bands separately,

```
Σ_(y in band j, y ≡ r (mod 2^K)) A_N(y) = 0,       Σ_(y in band j, y ≡ r (mod 3·2^K)) A_N(y) = 0
```

for every residue `r`. In particular the source projects to the zero measure on either finite quotient.

## Proof

From §4 of the legacy note `aggregate_duality.md` (now [`exposure-potential-boundary-flux`](../exposure-potential-boundary-flux/README.md)), kept as written.

Each band has length `2^j·Q`, and its endpoints are multiples of `9·2^K`, because `Q = 9N/4`. In the annular table, every row sums to zero separately on the three residues `1, 7, 13 mod 18` and on the three residues `5, 11, 17 mod 18`; the coefficients at multiples of 3 are zero. The common period of the coefficient pattern and a residue condition modulo `2^K` is `9·2^K`. Within that period a fixed odd binary residue visits every odd residue modulo 18 exactly once, so the coefficients sum to zero. For the modulus `3·2^K`, a fixed odd residue instead visits the three classes in its fixed residue class modulo 6, whose coefficient sum is again zero. Every band contains an integral number of these common periods; its endpoints are even and outside the odd source support. ∎

## Remarks

- **Exact scope.** A finite-state compression retaining only these data sees the same source vector as it sees for the empty measure, so it cannot by itself certify matching of the actual integer states. It does not rule out finite-state methods carrying additional information, such as residues modulo 9, exact offsets, carry data, symbolic parameters, or checked integer lifting identities. The coefficient table itself already retains information modulo 18 that these coarser projections lose.
- **Negative-cycle shadowing.** A bounded-precision periodic shadow indicator, even with a separate value in each band, has zero annular pairing and cannot be a positive dual witness ([`exposure-potential-boundary-flux`](../exposure-potential-boundary-flux/README.md), Theorem 1). To prove that aggregate exposure depths are unbounded, a shadowing argument must also control all extra source atoms in the actual exposed component and produce a positive total after their cancellations; the isolated-triple obstruction [`bounded-packet-certificate-obstruction`](../bounded-packet-certificate-obstruction/README.md) does not perform that step. **No unbounded aggregate-depth result is proved here** ([`uniform-aggregate-exposure-depth`](../../questions/uniform-aggregate-exposure-depth.md)); the later [`unbounded-exposure-depth-necessary`](../unbounded-exposure-depth-necessary/README.md) performs that step for one three-source chain, controlling every extra source by an inverse-history invariant.
- The reflected negative annulus of [`reflected-negative-annulus-control`](../reflected-negative-annulus-control/README.md) has the same vanishing projections modulo `2, 4, 8, 6, 12, 24`, yet carries a positive component mass.
- Novelty undetermined.

## History

- Migrated from `experiments/annular_construction/duality/aggregate_duality.md` §4 (part of the legacy R10 round; alias `R10-b`) at commit `be73a66`, by the B08 migration (Claude, Opus 5.5). Legacy status: "written graph/arithmetic identities and exact scoped counterexamples".
- Main lane (ChatGPT, Codex), 2026-10-17, commit `ce56699`. No review from another lane is on record.
- 2026-10-31: reviewed by the Claude review lane (Fable 5.1; directed by Santiago Armstrong); status raised to reviewed. No corrections. At this review the node was converted from the single file `binary-residue-projection-information-loss.md` to this folder, with its relative links and the inbound links repaired. Review: [`REVIEW-2026-10-31-claude-review-lane.md`](REVIEW-2026-10-31-claude-review-lane.md).
