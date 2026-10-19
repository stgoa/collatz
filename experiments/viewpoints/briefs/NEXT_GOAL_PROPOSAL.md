# Proposed next goal — global rigidity of finite-state component descriptions

**Historical recommendation, 2026-10-18.** This target was subsequently
activated as the [global-rigidity goal](GLOBAL_RIGIDITY_BRIEF.md), and V004
supplies the [full classification](../V004/GLOBAL_RIGIDITY.md).
The text below records the assessment at the time of recommendation.
The preceding
arithmetic-regularity goal is complete under its stated partial-result
criterion. The user now asks for a more ambitious high-level objective.

## Assessment

V003 supplied an infinite digit-count subclass and a kernel reduction. It
has not established that this language can settle the full automatic class
or provide a convergence method. The previous goal explicitly allowed a
subclass theorem or structural lemma as completion. The next goal should
raise that threshold rather than count another subclass as sufficient.

## Recommended objective

Prove that every finite-valued, binary-automatic coloring h of the positive
integers satisfying

```
h(2n)=h(n)              for n>=1,
h(3n+1)=h(n)            for odd n>1
```

is constant, preserving absorption at1. In plain language: no finite
automaton reading binary digits can assign different persistent labels to
different Collatz components.

This covers arbitrary finite automata, with no bound on their number of
states and no restriction to a selected digit statistic. Further subclasses,
finite catalogues and conditional identities are progress toward the
objective; they do not complete it.

Compare three bounded mechanisms before choosing depth:

1. Extend V003's kernel reduction to all mixed ternary sections.
2. Use the full guarded equations to constrain an arbitrary automaton
   directly, aiming to force equal outputs or a constant section.
3. Derive a finite characteristic-zero 3-Mahler relation for each color
   indicator, with every auxiliary series retained. The published
   [Adamczewski–Bell theorem](https://arxiv.org/html/1303.2019)
   is a conditional destination; the required second-base relation is missing.

Prioritize a mechanism that proves an implication for arbitrary finite
state size. State its remaining obligation after each bounded pass. If
the passes repeatedly fail to add an implication, report the target as
unresolved and recommend a concrete pivot; do not relabel another small
lemma as completion of the full-classification goal.

Alongside the proof investigation, assess relevance to actual orbit
components. No automaticity of a hypothetical nonabsorbing set is known
here. The proposed theorem would exclude finite-state descriptions of such
a separation; connecting it to convergence needs an additional, justified
mathematical bridge. A bridge that simply reinstates the whole Collatz
problem is not a further reduction.

## Parallel work inspected for this recommendation

Fresh remote main is `dda3ee9` (merged PR2). The local checkout was advanced
to this already-merged state without altering the other branches.

- `claude/lean-audit` at `627584177a7abffc49871ac31c9d85848bdb8535`:
  read the audit README and completed comparator receipt. The receipt
  records acceptance by nanoda and Lean; the additional paranoid receipt
  records further acceptances and ends while con-ron is running. Its
  stale IN PROGRESS header does not replace the specific completed receipts.
  This strategy review did not rerun or independently extend that audit.
- `claude/explicit-tao` at `478a06982ccc926421bb4157a1be286568275e07`:
  read STATE, LOG and the L4 architecture note. The branch reports a
  fixed-parameter window obstruction and separately labels its broader
  re-optimization claim as a candidate. Neither claim was independently
  verified here or imported as a premise for automatic rigidity.
- `claude/sidekick` at `357c387c600f495041f86b79f447cb840b4a7785`:
  read DIRECTIONS and the newest FEED entries. Retain existing D1–D7
  dispositions. Record its new L4 checks as external input, deferred for
  independent verification if used; no blanket transfer claim is adopted.

These lanes supply verification and analytic investigations in parallel.
The main lane's proposed objective remains structural automatic rigidity.
No messages or instructions were sent to those lanes, no side branch was
edited, and no new goal was started by this recommendation.
