---
id: actual-cycles-3x-d-corpus
kind: result
title: "Corpus of actual 3x+d cycles: every d ≤ 999 coprime to 6, odd seeds ≤ 5000"
status: reviewed
claim: >
  Exact finite enumeration, raw odd-only clock n → (3n+d)/2^v₂(3n+d) with state 1 not absorbing.
  For each of the 333 parameters d ≤ 999 coprime to 6 and every odd seed ≤ 5000 (832,500 seeds),
  the orbit reaches a cycle; all 832,500 seeds were resolved with no cap reached. The distinct cycles
  reached number 2,459 (1,184 after reducing the denominator and scaling), each stored with its
  complete integer states, exact valuations, numerator, denominator, scaling, discovery seed and
  replay certificate in actual_cycles.json. All eleven historical cycle fixtures are among them.
  This is not a complete census of cycles, even for these d.
authors:
  - ChatGPT main lane (Codex)
created: 2026-10-19
evidence:
  - "actual_cycles.json: the corpus (4.4 MB; kept because later results pin its SHA-256 28d067d3f82585a3701616adce3b57cae994541c4ddd3b4859d2bcf2307e44f2 and load it by path)"
  - "scan_cycles.py: scanner and replayer; default mode replays every saved certificate, --scan reruns discovery. It fails at its new path: it loads experiments/phase6/cycle_fixtures.json (now in ../../../convergence/results/baseline-obligation-transfer-controls/, byte-identical) relative to its old location (ROOT = HERE.parents[2]). Passed at be73a66 as experiments/cycle_spectrum/C001/scan_cycles.py (it does not appear in the be73a66 reference table archive/legacy-checker-run-be73a66.md; the legacy C001 delivery receipt records its replay and a fresh discovery as PASS)"
  - "../repeated-block-cancellation-bound/c001_spectrum_check.py, part 5: side-lane independent raw scan compared with this file"
  - "../repeated-block-cancellation-bound/delivery_checks.json: legacy delivery record (actual_cycle_replay and fresh_discovery PASS)"
reviewed_by:
  - by: Claude side lane (Opus)
    date: 2026-10-19
    link: ../repeated-block-cancellation-bound/c001_spectrum_check.py
    scope: "Side-lane feed (legacy archive/side_lane/FEED.md), entry 2026-10-19 00:18, REFEREE C001: an independent raw scan (state 1 not absorbing) over all 67 values d <= 199 coprime to 6 with odd seeds <= 5000 finds exactly the same cycles per d as this file, compared by minimum state. Parameters 199 < d <= 999 were not independently rescanned"
aliases: [C001-corpus]
tags: [cycles, 3x+d, controls, corpus, enumeration]
---

# Corpus of actual 3x+d cycles: every d ≤ 999 coprime to 6, odd seeds ≤ 5000

## Statement

The scanner [`scan_cycles.py`](scan_cycles.py) follows raw positive odd `3x+d` orbits under `n → (3n+d)/2^v₂(3n+d)`; state 1 is **not** absorbing. The persisted data [`actual_cycles.json`](actual_cycles.json) covers every positive `d ≤ 999` coprime to 6, starting from every positive odd seed `≤ 5000`.

| Quantity | Verified value |
|---|---:|
| Parameters `d` | 333 |
| Requested seeds | 832,500 |
| Distinct actual cycles found | 2,459 |
| Distinct cycles after reducing the denominator and scaling | 1,184 |
| Canonical two-block splits tested | 34,453 |
| Repeated-prefix decompositions tested | 2,371 |
| Capped or unprocessed seeds in this run | 0 |

Every cycle has its complete integer states, exact valuations, numerator, denominator, scaling, discovery seed and replay certificate. All eleven historical fixtures (legacy `experiments/phase6/cycle_fixtures.json`, now the fixture of [`baseline-obligation-transfer-controls`](../../../convergence/results/baseline-obligation-transfer-controls/README.md)) were independently rediscovered. **The finite discovery is not a complete census of cycles even for these fixed `d`:** a scan bounded by seed size misses cycles whose minimum exceeds the seed range. For example, the `3x+29` cycle with minimum 7055 is absent here and was found later ([`ordered-cycle-height-census`](../ordered-cycle-height-census.md)).

Some controls, including the principal fixed point at `d` itself:

| `d` | Cycles found | Cycles with reduced denominator exactly `d` | Longest odd-only period |
|---:|---:|---:|---:|
| 1 | 1 | 1 | 1 |
| 5 | 6 | 5 | 17 |
| 7 | 2 | 1 | 2 |
| 13 | 10 | 9 | 15 |
| 61 | 3 | 2 | 41 |
| 563 | 2 | 1 | 215 |

## Proof

Exact computation. All divisions and cycle arrows use exact integer arithmetic. Denominator invariance is checked at every state. The receipt records, for each cycle, the first discovery-seed connection, so a replay checks every cycle, its discovery path, its decompositions and every receipt count; the default replay does not rerun every scanned seed. `python3 scan_cycles.py --scan --output <file>` reruns discovery.

## Certificates

None runs at the new path: see `evidence`. The script binds its own SHA-256 and the fixture file's SHA-256 into the receipt, and refuses a mismatch.

## Remarks

- **Use as controls.** This is the shared corpus of actual `3x+d` cycles that the cycle results test against ([`conventions/NOTATION.md`](../../../../conventions/NOTATION.md) §3). Later scripts load it by path and pin its SHA-256 (`28d067d3…`): the checkers of [`equal-total-two-block-exclusion`](../equal-total-two-block-exclusion/README.md), [`two-block-uniform-denominator-growth`](../two-block-uniform-denominator-growth/README.md), [`narrow-cycles-are-mechanical`](../narrow-cycles-are-mechanical/README.md), [`rotation-block-exclusion`](../rotation-block-exclusion/README.md), [`ordered-cycle-sparse-forcing`](../ordered-cycle-sparse-forcing/README.md) and [`height-denominator-candidate`](../../questions/height-denominator-candidate/README.md), and later batches. Those scripts locate it as `C001/actual_cycles.json` relative to their old folders, so they no longer find it at its new path; the file itself is byte-identical.
- **Raw convention.** Cycles involving raw state 1 at generalised `d` are not nonconvergence witnesses under the absorbing convention.
- **Split counts.** The tested two-block decompositions use the orientation starting at each cycle's smallest state; they are not an all-rotation decomposition census.
- **Size.** The file is 4.4 MB, over the 1 MB guideline; it is kept because it is the pinned shared control fixture, and regenerating it would change its hash and the receipt fields (`discovery_seconds` records wall-clock time).

## History

- Split from `experiments/cycle_spectrum/C001/` (legacy ID `C001`; files `scan_cycles.py`, `actual_cycles.json`; `REPORT.md` §3) at commit `be73a66`, by the B03 migration (Claude, Opus 5.5). The scanner and corpus were kept together and apart from the C001 theorem, whose own certificate does not use them.
- Main lane (ChatGPT/Codex), 2026-10-19. The scanner was written by the main lane's independent reviewer and separately reviewed by its coordinating agent; the root reran the full discovery and every saved field matched except elapsed time.
