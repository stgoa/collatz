---
id: primewise-height-residue-matching
kind: attempt
title: Proving height-residue matching one prime factor of q at a time
status: reviewed
claim: >
  Tried: prove the full height-residue matching for ordered cycles (raw or normalised residue sets
  per dyadic height band, modulo the reduced denominator q) by showing that each prime factor of q,
  or each proper divisor, separately permits a matching. Verdict: false. Two actual ordered cycles
  of 3x+5,077,565 (q = 2^27 − 3^17, period 17, q ≤ L, minima 446,400,719 with B = 3 and 365,289,811
  with B = 2) have full matchings modulo q but Hall failures modulo the divisor 5.
authors:
  - ChatGPT main lane (Codex)
created: 2026-10-19
depends_on: [ordered-cycle-sorted-rank-residues]
evidence:
  - "../results/ordered-cycle-sorted-rank-residues/INDEPENDENT_MATCHING.md: full words, states and proofs of the two counterexamples"
  - "../results/ordered-cycle-sorted-rank-residues/height_matching_audit.json: exact finite receipt (historical; its checker no longer runs at the new path)"
  - "../results/ordered-cycle-sorted-rank-residues/c008_residue_check.py: side-lane reproduction of both counterexamples (run with the corpus path as argument)"
reviewed_by:
  - by: Claude side lane (Opus)
    date: 2026-10-19
    link: ../results/ordered-cycle-sorted-rank-residues/c008_residue_check.py
    scope: "Feed 2026-10-19 02:56, REFEREE C008: both counterexamples reproduced as actual raw cycles of 3x + 5,077,565, ordered, q ≤ L, with the stated Hall failures modulo 5"
tags: [cycles, dyadic-order, residues, hall-matching, counterexample]
---

# Proving height-residue matching one prime factor of q at a time

## Idea

The full matching proposal ([`height-residue-hall-matching`](../questions/height-residue-hall-matching.md)) asks for distinct representatives of the height-band residue sets modulo the reduced denominator `q`. Since the small-band theorem ([`small-band-height-residue-matching`](../results/small-band-height-residue-matching/README.md)) holds modulo every divisor `Q > 1`, a natural reduction is to prove matching modulo each prime factor of `q` separately.

## What happened

Two exact ordered cycles have reduced `q = 2^27 − 3^17 = 5,077,565`, period 17 and `q ≤ L`:

| Minimum `L` | `B` | Failure modulo the proper divisor 5 |
| ---: | ---: | --- |
| 446,400,719 | 3 | Normalised levels {1, 3} have only residue {4}; raw levels {1, 2, 3} have residue sets {3}, {2, 3}, {2}: three levels sharing two residues. |
| 365,289,811 | 2 | Every raw height set is {1, 4}, so three heights cannot be matched. |

Both raw and normalised graphs match at the full reduced `q`. The first counterexample has four levels and four available units modulo 5; its failure concerns a proper subset, beyond a global cardinality test. The second retracts the initially considered raw `B = 2` extension to general divisors. These are actual positive cycles with exact valuations and verified order, not formal height profiles.

## Why it fails

Matching is not inherited from the prime factors: Hall's condition modulo `q` can hold while it fails modulo a divisor, because collisions of residues modulo 5 need not be collisions modulo `q`. A proof must work with the full reduced `q`, and at `q = 1` (the case that matters) there is only one residue class.

## What survives

The two cycles, as controls for any future residue argument. The small-band theorem holds for every divisor `Q > 1`, but only for `B ≤ 2` (normalised) and `B ≤ 1` (raw).

## History

- Split from `experiments/cycle_spectrum/C008/` (legacy ID `C008`; `REPORT.md` "A precise failed shortcut", `INDEPENDENT_MATCHING.md`) at commit `be73a66`, by the B04 migration (Claude, Opus 5.5). Main lane (ChatGPT/Codex), 2026-10-19.
