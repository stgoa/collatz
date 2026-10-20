---
id: capped-first-passage-power-bounds
kind: question
title: Power-saving bounds for the failure and collision mass of a capped first descent below X^(1/4)
status: open
claim: >
  Odd-only 3x+1 map S, time in odd arrows. Draw N logarithmically on the odd integers of [X, 2X]; follow its orbit
  until the first state <= X^(1/4), capped at ceil(10 log X) odd arrows, recording a failure symbol dagger if the cap
  is reached first; let p_X be the law of this endpoint. Find explicit C, eta > 0 and X_0 such that for every integer
  X >= X_0: p_X(dagger) <= C X^(-eta) and sum over odd 1 < y <= X^(1/4) of p_X(y)^2 <= C X^(-eta). A candidate
  estimate (quantitative non-concentration after a substantial descent), not a proved theorem; it supplies neither
  absorption of the endpoints nor convergence, and may hold for the 3x+d controls too.
created: 2026-10-18
aliases: [VP-V12]
tags: [invariants, viewpoints, first-passage, entropy, tao, open]
---

# Power-saving bounds for the failure and collision mass of a capped first descent below X^(1/4)

## Question

As in the claim: the "partial milestone" of viewpoint card V12 (information of actual integer ensembles; [`statistical_languages.md`](../attempts/viewpoint-language-survey/statistical_languages.md) §V12), stated there "as a candidate, not a proved estimate". Mass already at 1 is retained separately. Logarithms are natural.

## Why it matters

V12 replaces symbolic entropy by the distribution of **realised integer endpoints**, keeping path-selection bias: conditioning on survival or a first-passage event changes the law and is not a fresh uniform sample, and entropy loss is merger information, not absorption (at `d = 5`, uniform `N ∈ {19, 81}` maps to the single endpoint 31; at `d = 1`, `{13, 53}` maps to 5). The target asks for quantitative non-concentration after a substantial descent, the kind of input Tao's argument uses ([`tao-2019-almost-all`](../../../sources/tao-2019-almost-all.md): Propositions 1.9, 1.11 and §6, where finite-residue equidistribution, first-passage stability and collision entropy are separate substantive estimates).

## Known progress

None derived; the survey retained V12 as "a separate statistical alternative; literature comparison first" ([`viewpoint-language-survey`](../attempts/viewpoint-language-survey/README.md)). Side-lane calibration (feed 21:26, labelled assessments): the target asks for a better rate than Tao proves (his Theorem 3.1 gives `(log x)^(−c)` with `c` unspecified); a power saving would need improving the rate-limiting steps (the `O_A(m^(−A))` decay of Prop. 1.17 with `m ≍ log x`, and the `log^(0.6..0.8) x` windows of §5). The first `≍ ½ log₂ X` odd steps are governed by exactly equidistributed 2-adic bits and reach about `X^0.79` with power-small failure (Terras, Everett, Korec); descending further to `X^(1/4)` is Tao's mixing problem. The explicit-Tao lane found Tao's printed first-passage window empty below `log x ≈ 6.27·10^13` ([`tao-printed-window-vacuity`](../../convergence/results/tao-printed-window-vacuity/README.md)). The target is `d`-uniform, and an almost-all statement cannot exclude a single divergent orbit.

## Suggested attacks

The card's cheapest test: specify the first-passage law and its failure symbol, then locate the first step that assumes new independent bits or removes conditioning, and compare with Tao's exact hypotheses before any numerical work. Reject an entropy potential whose only content is the deterministic identity `H(N) = H(Y) + H(N | Y)` or frozen symbolic growth rates.

## History

- New node by the B16 migration (Claude, Opus 5.5) from the V12 card in `experiments/viewpoints/V002/statistical_languages.md` (legacy ID V002; card V12 of the viewpoint map) at commit `be73a66`. Main lane (ChatGPT/Codex), 2026-10-18.
