---
id: nonabsorbed-fraction-arbitrarily-small
kind: question
title: Can the fraction of integers below X still unabsorbed after a finite horizon be made arbitrarily small?
status: open
claim: >
  Odd-only 3x+1 map S absorbing at 1; tau_1(n) the number of odd arrows from odd n to 1 (infinite if never).
  Prove: for every rational epsilon > 0 and every integer M >= 1 there are finite integers X >= M and H >= 0 such
  that at most epsilon X of the positive integers n < X have tau_1(oddpart(n)) > H. No uniform (e.g. logarithmic)
  bound on H is claimed. Assuming the audited lower theorem lau-2026-positive-density, this is equivalent to
  convergence of every positive integer (nonabsorbing-set-linear-lower-density); it fails for every 3x+d, d > 1.
  Phase 6 route node C.2a.
created: 2026-10-18
aliases: [P6-C.2a]
tags: [convergence, phase6, density, nonabsorbing-set, collatz-equivalent, frontier]
---

# Can the fraction of integers below X still unabsorbed after a finite horizon be made arbitrarily small?

## Question

Times count absorbed odd arrows; a general positive integer starts at its odd part, and the initial halvings are not charged. The target is the statistical condition in the claim, for every `epsilon > 0` and every lower cutoff `M`.

## Why it matters

[`nonabsorbing-set-linear-lower-density`](../results/nonabsorbing-set-linear-lower-density/README.md) shows, assuming the formal theorem of [`lau-2026-positive-density`](../../../sources/lau-2026-positive-density.md) (replayed in [`lau-density-formal-replay`](../results/lau-density-formal-replay/README.md)), that a nonabsorbing seed would force at least `c X` late starts at every sufficiently large `X`; choosing `epsilon < c` contradicts this condition. Conversely convergence gives a finite `H` at every finite cutoff. So this is an alternative universal obligation, equivalent to Collatz under the audited input. It is **not** a consequence of positive density of absorbed starts, of stopping below the initial value, or of Tao's theorem. It was Phase 6's last active node.

**Transfer.** For every supported `d > 1` it fails: multiples of `d` never reach 1 ([`baseline-obligation-transfer-controls`](../results/baseline-obligation-transfer-controls/README.md)). Any proof step must fail on those controls.

## Known progress

- The lower side is supplied (C.1a): [`lau-density-formal-replay`](../results/lau-density-formal-replay/README.md); qualitatively also [`predecessor-density-conditional-reconstruction`](../results/predecessor-density-conditional-reconstruction/README.md).
- Failed attempts at the upper side: the exact two-level residue system admits a positive-density leading profile ([`c2a-two-level-residue-relaxation`](../attempts/c2a-two-level-residue-relaxation.md)); combining the predecessor density with Tao's tightness gives only a non-strict comparison, and a countermodel shows those aggregate properties cannot suffice ([`matched-density-gap-combination`](../attempts/matched-density-gap-combination.md)).
- A stronger power-saving form is [`unabsorbed-count-power-saving`](unabsorbed-count-power-saving.md) (C.2); a transport premise that would imply this condition is [`bad-set-half-descent-transport`](bad-set-half-descent-transport.md).

## Suggested attacks

From the Phase 6 ledger: any new upper argument must distinguish actual Collatz absorption from the positive-density control sectors; do not repeat the failed leading-profile relaxation or infer the matched density comparison from Tao's qualitative tail limit. The side lane proposed bounding the logarithmic density of `B` explicitly from a quantitative form of Tao's estimate at a fixed height combined with verification below `2^68`; as [`matched-density-gap-combination`](../attempts/matched-density-gap-combination.md) §3 shows, this needs a strict quantitative comparison between target-dependent constants that no current input provides (speculative).
