---
id: tao-2019-almost-all
kind: source
title: "Tao: almost all Collatz orbits attain almost bounded values"
status: cited
citation: >
  T. Tao, "Almost all orbits of the Collatz map attain almost bounded values", Forum of Mathematics,
  Pi 10 (2022), e12. arXiv:1909.03562 (corrected v7, 16 July 2026).
url: https://arxiv.org/abs/1909.03562v7
created: 2026-10-17
tags: [density, mixing, convergence]
---

# Tao: almost all Collatz orbits attain almost bounded values

## Citation

Terence Tao, *Almost all orbits of the Collatz map attain almost bounded values*, Forum of Mathematics, Pi 10 (2022), e12; [arXiv:1909.03562](https://arxiv.org/abs/1909.03562v7). The corrected **v7**, posted 16 July 2026, identifies a correction to Lemma 7.9; the main theorem is unchanged. New analytic imports must use v7. (The record names the work by its 2019 arXiv posting.)

Parts referenced:
- **Theorem 1.3:** for every `f(n) → +∞`, the minimum of the ordinary Collatz orbit of `n` is below `f(n)` for `n` in a set of logarithmic density one. **Theorem 1.6:** the odd-only (Syracuse) version. Remark 1.4: a constant `C_δ ≪ exp(δ^(−O(1)))` for lower logarithmic density `≥ 1 − δ`; the hidden constants are not numerical.
- **Proposition 1.14:** the finite-distribution mixing estimate for Syracuse valuations.
- Lemma 2.1, Remark 1.10 (valuation-word / cylinder context); Section 1.1 (why density-one descent cannot simply be iterated); equation (7.5), Lemma 7.2, Proposition 7.3 (paired envelope).

## What we use

- **P6-004 (route node C.1a):** Proposition 1.14 is the explicit external input of the written conditional reconstruction of linear predecessor density ([predecessor-density-conditional-reconstruction](../areas/convergence/results/predecessor-density-conditional-reconstruction/README.md); legacy `audit_notes.md`, `terminal_audit.md`, `transfer_scope.md`), with Tao's unspecified constants. A qualitative transfer to each fixed `d` coprime to 6 is argued in `transfer_scope.md`; no verbatim `3x+d` version of the full theorem is imported.
- **Explicit-Tao line** (`experiments/explicit_tao/`) and the earlier programme's analytic branch: the theorem is the calibration target and transport background; the analytic candidate needed the paired envelope around (7.5), Lemma 7.2 and Proposition 7.3, not just a marginal mixing statement.
- Elsewhere (Phase 6 audit L2, [route-literature-transfer-audit](../areas/convergence/results/route-literature-transfer-audit.md); the attempt [matched-density-gap-combination](../areas/convergence/attempts/matched-density-gap-combination.md); residual-progress sufficient-sets audit) it is comparison only: it concerns orbit minima in logarithmic density, not arrival at 1 within a horizon, and does not discharge C.2.

## How it is checked

`cited`. Taken as published; no constant was extracted or verified, and nothing is formal.
