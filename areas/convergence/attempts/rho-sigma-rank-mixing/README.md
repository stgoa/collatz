---
id: rho-sigma-rank-mixing
kind: attempt
title: "Mixing the rho and sigma dispatchers: finite dependency graphs are acyclic, but no common rank is found"
status: written
claim: >
  Tried: union the nine-rule rho dispatcher (low-block-continuation-prescribed-growth) and the separate sigma
  dispatcher (sigma-rank-removes-absorption-overhead) for odd-only 3x+1 W5 pair inputs, expanding both rules and
  following every requested child, to look for finite dependency cycles to solve jointly. The completed graphs
  from every W5 input below 16384 and below 131072 have 2075 and 16619 nodes and are acyclic. Verdict: no
  dependency cycle and no common global rank were found; finite acyclicity cannot prove that an unbounded union
  terminates, and the explicit incompatibility at w = 4629 stands. Further enlarging this survey was judged not
  the next step. Finite evidence for a rejected immediate cycle strategy, not a theorem against joint
  comparisons or other signed systems.
authors:
  - ChatGPT main lane (Codex)
created: 2026-10-17
depends_on: [sigma-rank-removes-absorption-overhead, low-block-continuation-prescribed-growth]
evidence:
  - "probe_rank_mixing.py, rank_mixing_audit.json: exploration probe, not a checker (resource cap 20000 nodes; reaching it fails the run; unhandled leaves remain premises, no orbit search or supplied input). The receipt hashes the complete finite graphs, including signed coefficient lists and rule names. Fails at its new path: it puts ../continued_rules/ and ../phase_rank/ (now ../../results/low-block-continuation-prescribed-growth/, ../../results/sigma-rank-removes-absorption-overhead/) on sys.path by their pre-migration folder names. Passed at be73a66 as experiments/residual_progress/rank_mixing/probe_rank_mixing.py inside scripts/verify_all.py (archive/legacy-checker-run-be73a66.md; the gate passed in full at 9dbc71a)"
aliases: [R57-c]
tags: [convergence, outer-residual, critical-rank, sigma-rank, dispatcher]
---

# Mixing the rho and sigma dispatchers: finite dependency graphs are acyclic, but no common rank is found

## Idea

[`sigma-rank-removes-absorption-overhead`](../../results/sigma-rank-removes-absorption-overhead/README.md) (R51) proves that an old `ρ`-decreasing rule can increase `σ`, so a union of the two dispatchers needs an additional termination argument. Perhaps their actual signed requests form finite dependency cycles that could be solved jointly, or a common rank exists on the inputs that occur.

## What happened

The legacy note "Mixing the two rank systems: finite survey and unresolved compatibility" follows, lightly edited (title moved to the node heading). Its command names the pre-migration path.

R51 proves that an old rho-decreasing rule can increase sigma. Thus a
union of the two dispatchers needs an additional termination argument.
We tested whether their actual signed requests form finite dependency
cycles that could instead be solved jointly.

The fixed dispatchers are the nine-rule rho union from R53 and the
separate R51 sigma union. Starting from every W5 input below16384 and
then below131072, the probe expands **both** available rules and follows
every requested child, including children beyond the starting interval.
The completed finite graphs have2075 and16619 nodes respectively and
are acyclic. The resource cap is20000 nodes; reaching it fails the run.
Unhandled leaves remain premises, with no orbit search or supplied input.

This found no dependency cycle to solve and no common global rank.
Finite acyclicity cannot prove an unbounded union terminates. In particular
the explicit R51 incompatibility at4629 remains valid. Repeatedly enlarging
this survey is not the next research step; the selected forward and inverse
interfaces offer new complete arithmetic domains directly.

Reproduce with:

```sh
python3 experiments/residual_progress/rank_mixing/probe_rank_mixing.py
```

The receipt hashes the complete finite graphs, including signed coefficient
lists and rule names. It is finite evidence for a rejected immediate cycle
strategy, not a theorem prohibiting useful joint comparisons or signed
systems built from other rules.

## Why it fails

It does not fail by a counterexample; it stalls. The surveyed graphs have no cycle to solve, so the hoped-for joint solution of cycles has nothing to act on, and acyclicity of finite completed graphs proves nothing about the unbounded union. The known obstruction is a theorem of R51: at `w = 4629` a valid old-`ρ` rule requests `2197` with `σ(2197) = 6591 > 6171 = σ(4629)`, so no single one of the two ranks orders all edges of the union.

## What survives

- The two separately valid inductions: [`low-block-continuation-prescribed-growth`](../../results/low-block-continuation-prescribed-growth/README.md) (the `ρ` dispatcher, later [`twelve-family-rho-dispatcher`](../../results/twelve-family-rho-dispatcher/README.md)) and [`sigma-rank-removes-absorption-overhead`](../../results/sigma-rank-removes-absorption-overhead/README.md).
- The exact compatibility criterion between them is the later R62 ([`absorption-defect-original-rank-resolution`](../../results/absorption-defect-original-rank-resolution/README.md)): a `σ`-valid plan at a returning parent is `ρ`-valid, and at a nonreturning parent the nondecreasing-`ρ` requests are exactly the returning `u` in an explicit window.
- The main lane's chosen direction after this survey: new complete arithmetic domains ([`selected-critical-five-forward-tables`](../../results/selected-critical-five-forward-tables/README.md), [`two-selected-inverse-choices`](../../results/two-selected-inverse-choices/README.md)).

## History

- Migrated from `experiments/residual_progress/rank_mixing/RANK_MIXING.md` (legacy ID: the R57 batch's rank-mixing survey; alias R57-c given at the migration) at commit `be73a66`, by the B11 migration (Claude, Opus 5.5). Note, probe and receipt moved byte-identical; the probe is exploration and stays evidence.
- Main lane (ChatGPT, Codex), 2026-10-17, from commit `7206f9c`.
