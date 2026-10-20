# Mixing the two rank systems: finite survey and unresolved compatibility

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
