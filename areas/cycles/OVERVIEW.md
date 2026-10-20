# Cycles

**The question.** Does the Collatz map `3x+1` have a cycle other than the trivial one, `1 → 4 → 2 → 1`?

**The approach.** A candidate cycle is encoded by its word of halving counts (letters). It is an integer cycle exactly when the word's rational cycle has reduced denominator 1 ([`conventions/NOTATION.md`](../../conventions/NOTATION.md) §2). The work here studies that denominator across the whole `3x+d` family, and how far a cycle's word can be from periodic.

> This overview is filled in during the migration of the legacy material (see `_triage/`). It will summarise the main lines, the strongest results, the open questions and the dead ends, linking to the nodes.
