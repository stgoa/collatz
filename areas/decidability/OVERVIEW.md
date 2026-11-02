# Decidability

**The question.** What can logic and computability say about the Collatz problem, and what can they not say? The fixed statement "every positive integer reaches 1" is a single sentence: it is either true or false, so as an algorithmic problem it is trivially decidable (one of "print yes" and "print no" is right). The meaningful questions are of two other kinds:

- **Independence:** could the conjecture be true but unprovable in Peano arithmetic or ZFC?
- **Families:** which decision problems built around the Collatz map, with some input varying, are undecidable?

**Why a separate area.** The cycles area studies the arithmetic of hypothetical cycles, the convergence area studies currents and descents, and the invariants area studies what a nonabsorbing set must look like. None of them asks what logic forbids or permits, and claims of "undecidability" are easy to overstate. This area holds those claims, with their scope stated exactly.

**Who did what.** The ChatGPT main lane (Codex) built an injective coding of binary words into the inverse Syracuse tree and a reduction from the Post correspondence problem, recorded only in the archived master handoff (§13). On 2026-11-01 the owner asked for an undecidability thread; the Claude cycles lane (Opus 5.5) opened this area, migrated that construction with full proofs and certificates, and wrote the scoping node.

## The main lines

### 1. Logical form and its consequences

[`collatz-conjecture-logical-form`](results/collatz-conjecture-logical-form/README.md) (written): each instance "`n` reaches 1" is Σ⁰₁ and provable when true; "no nontrivial cycle" is Π⁰₁ because each period is a finite search; the conjecture is Π⁰₂. Three consequences frame the area:

- If the cycle half is independent of Peano arithmetic, it is true; so independence of the whole conjecture would leave only a divergent orbit as a possible counterexample.
- The problem "given `n`, does `n` reach 1?" is undecidable only if the conjecture is false.
- No computable encoding of Turing machines into `3x+1` orbits can make "reaches 1" a halting signal unless the conjecture is false; such an encoding would hand out explicit counterexamples.

### 2. Free codings in the inverse tree

[`inverse-syracuse-binary-coding`](results/inverse-syracuse-binary-coding/README.md) (written): two inverse Syracuse branches, chosen by a table modulo 9 with valuations in the disjoint bands `[3, 6]` and `[7, 10]`, code every binary word injectively by a convergent integer whose forward orbit reads the word back; the codebook is decidable in `O(log x)` steps. [`synchronised-coding-pcp-reduction`](results/synchronised-coding-pcp-reduction/README.md) (written, assumes Neary's five-pair PCP theorem): deciding whether two such codings, driven by the same index sequence, ever meet is undecidable. Every orbit involved converges; the hardness is in the synchronisation, so nothing follows about the conjecture itself.

## Open questions

- [`undecidable-collatz-family-threshold`](questions/undecidable-collatz-family-threshold.md): how small can an undecidable family of Collatz-like maps be, if it contains `3x+1`? The large programmable classes are undecidable by [Conway](../../sources/conway-1972-unpredictable-iterations.md) and Π⁰₂-complete by [Kurtz–Simon](../../sources/kurtz-simon-2007-generalized-collatz.md); the one-parameter family `3x+d` is untouched.

## Dead ends and warnings

From the archived handoff (§14.3), kept as scope rules for this area:

- A class-wide termination procedure that contains the ordinary Collatz map would decide the Collatz instance; this is a scope warning, not a proof of equivalence or of undecidability.
- Building a machine whose target is a universal Diophantine polynomial imports undecidability into the predicate; it is not a reduction into ordinary Collatz.
- Finite observed stopping times do not bear on logical independence, and computational undecidability of an instance set is a different question from unprovability of one universal statement.
- Conway and Kurtz–Simon concern programmable classes of maps, not the fixed map.

## History

- Area opened 2026-11-01 by the Claude cycles lane (Opus 5.5), directed by Santiago Armstrong.
