---
id: ordered-cycle-height-census
kind: result
title: "Bounded 3x+d census for d ≤ 97: a new 3x+29 cycle, and B ≤ q − 1 on all 1,185 normalised cycles"
status: reviewed
claim: >
  Exact finite computation, raw odd-only clock, no absorption. For the 33 parameters d ≤ 97 coprime
  to 6, every odd seed up to 4,000,001 (d = 5), 2,000,001 (d = 7, 11, 13, 29) or 200,001 (other d)
  reaches a cycle within the caps (20,000 steps per new path, 512 state bits, 10,000,000 new arrows
  per parameter): 8,800,033 seeds, none capped or unprocessed, giving 180 source cycles and 89
  normalised cycles. Exactly one is absent from the C001 corpus: q = 29, minimum 7055, maximum
  1,051,393, odd period 41, total exponent 65, B = 7, J = 38, cancellation factor
  14,499,716,215,459,201, reached from seed 5859; it is ordered. In the combined set of 1,185
  normalised cycles, 51 lie in the ordered domain (q ≤ L, circular order), and no cycle with
  q ≤ L, ordered or not, violates B ≤ q − 1; among ordered cycles the largest B/(q − 1) is 3/4.
authors:
  - ChatGPT main lane (Codex)
created: 2026-10-19
depends_on: [actual-cycles-3x-d-corpus]
evidence:
  - "../questions/height-denominator-candidate/check_height_denominator.py, height_denominator_audit.json: the census checker and receipt. Fails at its new path (loads the corpus, the phase-6 fixtures and C006's receipt by old relative paths); passed at be73a66 as experiments/cycle_spectrum/C007/check_height_denominator.py (archive/legacy-checker-run-be73a66.md)"
  - "../questions/height-denominator-candidate/RESIDUE_MATCHING.md, residue_matching_replay.json: matching audit of the same 1,185 cycles"
  - "../questions/height-denominator-candidate/c007_height_check.py: side-lane REFEREE check (needs the corpus path as argument)"
reviewed_by:
  - by: Claude side lane (Opus)
    date: 2026-10-19
    link: ../questions/height-denominator-candidate/c007_height_check.py
    scope: "Feed 2026-10-19 02:28, REFEREE C007 at main dddbe33: the q = 29 cycle reproduced from seed 5859 (minimum 7055, maximum 1,051,393, period 41, exponent 65, gcd 14,499,716,215,459,201, B = 7, J = 38, ordered); B <= q − 1 holds on all 194 normalised census cycles with q <= L, 51 of them ordered, largest ordered ratio 3/4. The full seed census was not rerun by the side lane"
tags: [cycles, census, 3x+d, height, evidence]
---

# Bounded 3x+d census for d ≤ 97: a new 3x+29 cycle, and B ≤ q − 1 on all 1,185 normalised cycles

## Statement

The checker first replays all 2,459 C001 source cycles across 333 parameters ([`actual-cycles-3x-d-corpus`](actual-cycles-3x-d-corpus/README.md)), yielding 1,184 distinct normalised cycles and retaining all 11 raw control fixtures. It then runs a new deterministic bounded seed census:

| Parameter `d` | Largest odd seed |
|---|---:|
| 5 | 4,000,001 |
| 7, 11, 13, 29 | 2,000,001 |
| Other positive `d ≤ 97` coprime to 6 | 200,001 |

Across 33 parameters, 8,800,033 odd seeds required 13,998,115 newly evaluated arrows. The declared limits are 20,000 steps per new path, 512 state bits, and 10,000,000 new arrows per parameter. No seed was capped or left unprocessed. Memoisation stores only paths already connected to exactly closed cycles. The census makes no statement about seeds beyond its ranges.

The census finds 180 source cycles and 89 distinct normalised cycles. One was absent from C001: `q = 29`, minimum 7055, maximum 1,051,393, odd period 41, total exponent 65, `B = 7`, `J = 38`, and cancellation factor 14,499,716,215,459,201. Seed 5859 reaches it after 12 raw odd steps. Its full states, valuations, order and source seed are stored in the receipt. Discovery relative to the repository is not a novelty claim.

The combined set has 1,185 normalised cycles, 51 in the ordered domain. The candidate `B ≤ q − 1` ([`height-denominator-candidate`](../questions/height-denominator-candidate/README.md)) survives every stored cycle, including the unordered ones (receipt fields `candidate_failures` and `outside_order_candidate_failures` both empty). The nearest ordered examples are the `q = 5` period-17 cycles, with `B/(q − 1) = 3/4`; the new `q = 29` cycle has ratio 1/4. Stronger logarithmic and half-linear candidates fail on exact controls (receipt fields `stronger_logarithmic_failures`, `stronger_half_linear_failures`).

## Proof

Exact computation by [`check_height_denominator.py`](../questions/height-denominator-candidate/check_height_denominator.py), receipt [`height_denominator_audit.json`](../questions/height-denominator-candidate/height_denominator_audit.json) (SHA-256 `b35a18cb…`). The author's census write and full replay and a separate root full census replay both passed at script hash `516ea313…`. It does not run at its new path (see `evidence`).

## Remarks

- **Scope.** A finite discrimination test only; it does not prove the candidate, nor exclude cycles outside the seed ranges. A census bounded by seed size misses cycles with large minima, as this `q = 29` cycle shows for the C001 corpus.
- **Discriminating power.** Because the candidate also holds on unordered cycles, its broad finite success does not identify circular order as the decisive ingredient. Most census cycles have small `B`, and the law is trivially weak for large `q`; the binding cases are small `q` with large `B`, and the two `q = 5` period-17 cycles are the only near-tight data (side-lane assessment).
- **Matching audit** (separate computation, [`RESIDUE_MATCHING.md`](../questions/height-denominator-candidate/RESIDUE_MATCHING.md)): for each of the 1,184 normalised cycles with `q > 1`, the height levels admit distinct raw and distinct normalised residue representatives (2,368 bipartite matchings, all pass; 51 ordered; 371 unordered cycles miss some intermediate height label). `q = 1` was omitted. Main-lane only; not reviewed by another lane.

## History

- Split from `experiments/cycle_spectrum/C007/` (legacy ID `C007`; `REPORT.md` "Actual-cycle discrimination", `RESIDUE_MATCHING.md`) at commit `be73a66`, by the B03 migration (Claude, Opus 5.5). Main lane (ChatGPT/Codex), 2026-10-19. Its files stay in the folder of [`height-denominator-candidate`](../questions/height-denominator-candidate/README.md), because the C007 scripts locate each other's files by path.
