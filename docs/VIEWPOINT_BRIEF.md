# Goal — Find a better mathematical language for Collatz

Explore Grothendieck-style changes of viewpoint: seek mathematical objects, representations and questions that make the structure of Collatz easier to understand and work with.

The immediate objective is **to discover a promising language**, rather than pursue a complete proof within the current framework.

## Breadth before depth

- Begin with a broad survey of substantially different viewpoints. Use parallel exploration where useful.
- Keep first investigations short and bounded. Avoid extended proof development, large computations or expanding existing case catalogues.
- Consider established frameworks, unexpected connections and combinations of approaches. Do not privilege abstraction or sophisticated terminology by themselves.
- Treat the existing programme as evidence and infrastructure. Its current route map should inform exploration without restricting the available directions.

## Evaluate each viewpoint concretely

For each candidate, record:

1. **Objects:** What replaces or reorganizes integers, trajectories and the convergence question?
2. **Structural gain:** What becomes simpler, more natural or more visible?
3. **Translation:** Where does the unresolved difficulty appear in this language?
4. **Worked example:** Demonstrate the viewpoint on a concrete identity, obstruction or orbit family.
5. **Controls:** Explain how it behaves on related maps with known cycles. Identify what still needs to distinguish ordinary Collatz.
6. **Next test:** State the cheapest meaningful test that could strengthen or disqualify it.
7. **Intermediate milestone:** Identify a useful result short of solving Collatz, and check that it is not merely an equivalent reformulation.

An analogy is a starting point. A change of notation alone is not evidence of progress.

## Compare, combine and redirect

Maintain a living `VIEWPOINT_MAP.md` comparing candidates, connections, evidence, weaknesses and rejected ideas.

After the initial survey, select a small shortlist for slightly deeper probes. Expand the search when candidates merely relocate the same obstacle. Explore combinations when different viewpoints preserve complementary information.

Do not settle prematurely on a framework because it is familiar or elegant.

## What success means

A promising language should offer several of the following:

- Simpler or better organized proof obligations.
- An explanation of recurring failures in existing approaches.
- Useful structure that previous representations obscure.
- A concrete, checkable consequence.
- A credible intermediate milestone.
- A clear account of remaining assumptions and limitations.

The deliverable is a defensible recommendation of one or a few viewpoints, supported by comparisons and examples, together with a focused subsequent research programme. Finding such a viewpoint is not itself a proof of Collatz.

## Repository and research discipline

Preserve the frozen results and their counterexamples. Keep claims, exploratory hypotheses and verified results distinct.

Persist substantive findings, references, examples and rejection reasons in the repository. Maintain the top-level README. Continue reviewing the independent side lane as read-only input, recording source commits and independently checking adopted findings.

Commit and push completed exploration batches with verification appropriate to their claims. Report what changed our understanding, what remains uncertain, and which directions deserve the next probes.
