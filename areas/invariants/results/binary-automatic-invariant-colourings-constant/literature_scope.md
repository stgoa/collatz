# V004 — Published inputs and novelty boundary

**Status: bounded source check, 2026-10-18.** This note verifies the imported
theorems' scope. It does not claim a complete literature review or novelty.

## Main proof

The directly inspected primary research source is
[Adamczewski–Bell, *A problem about Mahler functions*](https://arxiv.org/html/1303.2019).
Theorem2.1 states Cobham's recognition theorem for multiplicatively
independent bases. Theorem7.1 gives the finite-kernel characterization.
Applying these to each finite color fiber of K_+ yields eventual
periodicity of its members. The main proof independently supplies K_+'s
two section closures and the elementary finish from its odd member.

Definition7.1's displayed offset range appears to contain a typographical
error: the standard range is0<=r<k^a, used throughout V004. We rely on the
classical finite-kernel theorem with that definition. No formal replay of
either classical input was performed.

The same paper's Theorem1.1 supplies the optional characteristic-zero
Mahler conclusion. The [Mahler note](mahler_route.md) derives both finite
systems and scalar relations before using it. This is an alternative
published implication, not a second independent proof of Cobham.

## Optional progression finish

[Monks–Monks–Monks–Monks, *Strongly sufficient sets and the distribution
of arithmetic sequences in the 3x+1 graph*](https://arxiv.org/html/1204.3904v2)
was directly inspected in this batch, especially §2 and Theorem4.1.
It supplies an alternative finish from a monochromatic arithmetic
progression; the [automaton audit](automaton_route.md) checks the positive
tail and ternary-unit representative conditions explicitly. This input
is not needed in the central proof, which uses elementary residue algebra.

## Bounded prior-work search

The [V003 literature note](../digit-count-invariant-colourings-constant/literature.md) remains the baseline,
including the distinction between fixed-depth ancestor languages, an
entire basin, and invariant color classes. That review did not locate
the exact single-base classification in primary literature.

This batch additionally searched combinations including:

- `Collatz automatic invariant coloring`
- `Collatz regular invariant sets automata`
- `"Collatz" "Cobham"`
- `"Collatz" "automatic" "invariant" "Cobham"`
- `"Collatz" "regular sets" invariant`
- `"Collatz" "automatic coloring"`

These searches did not identify an inspected primary source stating this
exact theorem. That is only a search outcome. A reference concerning
regular convergence classes is not automatically a theorem about the
unbounded invariant class; V003 documents that distinction. Unreviewed
claims and generic search snippets were not adopted as premises.

**Novelty remains undetermined.** The mathematical deliverable is the
complete written argument with explicit established inputs. A journal
submission or priority assertion would require a separate literature and
human review process.
