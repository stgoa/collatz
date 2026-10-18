# Goal — Turn arithmetic regularity into a useful Collatz research framework

Investigate whether arithmetic regularity of orbit-component colorings yields a substantive theorem or a sharper understanding of the obstruction to convergence.

The central question is:

**How complicated must a rule separating different Collatz orbit components be?**

## Main mathematical target

Study finite-valued functions \(h\) on the positive integers satisfying

\[
h(2n)=h(n)\quad(n\ge1),\qquad
h(3n+1)=h(n)\quad(n>1\text{ odd}).
\]

These equations preserve the absorber at 1.

**Aim to classify the solutions recognizable by a finite automaton reading binary digits. In particular, investigate whether every such solution must be constant.**

The existing periodic classification is the starting point. Do not assume that an arbitrary hypothetical nonabsorbing set has an automatic, periodic, or otherwise regular description.

## Research approach

1. **Establish the literature baseline.** Check primary sources on automatic sequences, Collatz functional equations, and predecessor languages. Determine what is already known about the precise target. Keep fixed-depth recognition distinct from recognition of an entire basin.
2. **Test the missing closure mechanism.** Starting from a finite binary kernel, derive the consequences of Collatz invariance for ternary sections. Identify exactly what would establish finite ternary closure and which steps remain unsupported. Cobham’s theorem becomes applicable only after its hypotheses are proved.
3. **Use complementary representations selectively.** Give binary/ternary carry diagrams one bounded test: determine whether their complete boundary data reveal a useful relation that the functional equations obscure. Retain finite-input conditions, carry information, and the nonlocal bootstrap.
4. **Compare before deepening.** After each bounded investigation, assess whether the language produced a new implication, eliminated an assumption, or exposed a precise obstruction. If it repeatedly reproduces existing equivalences, reconsider the statistical alternative or broaden the search.

## What counts as progress

Seek a result beyond the existing periodic and supplied two-base cases:

- A classification of all binary-automatic invariant colorings.
- A rigorous partial classification covering an explicitly defined infinite class.
- A structural lemma that genuinely advances the missing closure argument.
- A sharply scoped obstruction explaining why a specific proposed mechanism fails and what additional information it requires.

Finite automaton catalogues and successful examples alone do not establish these conclusions.

## Deliverable and discipline

Deliver the strongest justified result, its proof or exact counterexample, its limitations, and a recommendation to deepen, combine, or redirect the approach.

Exercise every general claim against the known-cycle controls. Preserve frozen results, exact domains, absorber conventions, and distinctions between evidence and proof. Check novelty separately.

Persist findings, failed claims, references, and reproducible checks in the repository; update the viewpoint map and README; review the independent side lane as read-only input; commit and push completed batches.

**Success is a demonstrated mathematical gain from this language, or a decisive, precisely scoped reason to redirect it. It is not a claim to have solved Collatz.**
