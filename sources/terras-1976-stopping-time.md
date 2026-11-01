---
id: terras-1976-stopping-time
kind: source
title: "Terras (1976): a stopping time problem on the positive integers"
status: cited
citation: >
  R. Terras, "A stopping time problem on the positive integers", Acta Arithmetica 30(3) (1976).
  Pages not stated in the legacy record.
url: https://www.impan.pl/en/publishing-house/journals-and-series/acta-arithmetica/all/30/3/101028/a-stopping-time-problem-on-the-positive-integers
created: 2026-10-17
tags: [stopping-time, parity-vectors, density, convergence]
---

# Terras (1976): a stopping time problem on the positive integers

## Citation

Terras, [*A stopping time problem on the positive integers*](https://www.impan.pl/en/publishing-house/journals-and-series/acta-arithmetica/all/30/3/101028/a-stopping-time-problem-on-the-positive-integers), Acta Arithmetica 30(3), 1976 (volume and issue as given by the publisher link in the record). Pages are not in the legacy record, and the author's initial is completed from general knowledge, not verified against the source. Theorem 1.2 and Corollary 1.3 identify length-`k` parity vectors with residues modulo `2^k`. The publisher's PDF was intermittently inaccessible during the Phase 6 audit; the theorem statements were seen through the primary search index, not as a complete proof audit.

## What we use

- **Parity-vector bijection** (Theorem 1.2): the first `k` shortcut parities of `n` are determined by `n mod 2^k`, and every parity vector occurs exactly once. In odd-only form (legacy explicit-Tao L1, recalled in [`explicit-valuation-large-deviations`](../areas/convergence/results/explicit-valuation-large-deviations/README.md)): the first `n` Syracuse valuations of `N` are determined by `N mod 2^(A+1)`, each word one odd class. This is classical background for the repository's cylinder facts, which are proved here directly.
- **Density one of finite stopping time** (with [everett-1977-stopping-time](everett-1977-stopping-time.md)): the calibration benchmark for Phase 6 audit L1 / S.1 / P6-001 and explicit-Tao L2–L3 ([`explicit-valuation-large-deviations`](../areas/convergence/results/explicit-valuation-large-deviations/README.md), [`explicit-one-round-descent`](../areas/convergence/results/explicit-one-round-descent/README.md)), which prove their own explicit versions.

Transfer: the parity encoding extends to each fixed odd `d` (3 is invertible mod powers of 2), but a parity bijection alone is not an all-integer stopping theorem.

## How it is checked

`cited`. The repository's results re-derive what they need ([`explicit-valuation-large-deviations`](../areas/convergence/results/explicit-valuation-large-deviations/README.md), explicit-Tao L2, has a finite certificate); the paper itself is not replayed.
