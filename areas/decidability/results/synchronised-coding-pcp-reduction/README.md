---
id: synchronised-coding-pcp-reduction
kind: result
title: "Deciding whether two synchronised inverse-Syracuse codings ever meet is undecidable (a PCP reduction)"
status: written
claim: >
  With the coding Γ of inverse-syracuse-binary-coding, the following problem is undecidable: given finitely many
  pairs (u_i, v_i) of binary words (five pairs suffice), decide whether some nonempty index sequence i_1, …, i_t
  satisfies Γ(u_(i_1)⋯u_(i_t)) = Γ(v_(i_1)⋯v_(i_t)), i.e. whether two compositions of the fixed inverse Syracuse
  branches G_0, G_1, applied to 1 under the same index sequence, land on the same integer. By injectivity of Γ this is
  exactly the Post correspondence problem on the same pairs, which is undecidable (Neary: already for five pairs of
  binary words). Every integer involved converges to 1 and every individual orbit question in the instance is
  trivially decidable; the undecidability is entirely in the existential synchronisation over index sequences.
  Nothing follows about the decidability or provability of the Collatz conjecture.
authors:
  - Claude cycles lane (Opus 5.5; directed by Santiago Armstrong)
  - ChatGPT main lane (Codex), the original reduction, archived in archive/handoff/COLLATZ_PROGRAMME_MASTER_HANDOFF.md §13.3
created: 2026-11-01
depends_on: [inverse-syracuse-binary-coding]
assumes: [neary-2015-binary-pcp-five-pairs]
evidence:
  - "the PCP equivalence is also checked numerically by V5 of inverse-syracuse-binary-coding (182,008 index sequences of 300 random instances)"
tags: [decidability, pcp, inverse-syracuse, reduction]
---

# Deciding whether two synchronised inverse-Syracuse codings ever meet is undecidable

## Statement

Let `Γ` be the coding of [`inverse-syracuse-binary-coding`](../inverse-syracuse-binary-coding/README.md): `Γ(b_1⋯b_m) = G_(b_1)(⋯G_(b_m)(1))` for the two fixed inverse Syracuse branches `G_0`, `G_1`.

**Problem SYNC.** Input: pairs `(u_1, v_1), …, (u_k, v_k)` of binary words. Question: is there a nonempty index sequence `i_1, …, i_t` with

```
Γ(u_(i_1) u_(i_2) ⋯ u_(i_t)) = Γ(v_(i_1) v_(i_2) ⋯ v_(i_t)) ?
```

**Theorem.** SYNC is undecidable, already for `k = 5`.

## Proof

By injectivity of `Γ` (part 3 of the coding node), the displayed equality holds iff `u_(i_1)⋯u_(i_t) = v_(i_1)⋯v_(i_t)`. So SYNC and the Post correspondence problem have the same positive instances, and the identity map on inputs is a reduction from PCP to SYNC. PCP is undecidable for five pairs of binary words ([`neary-2015-binary-pcp-five-pairs`](../../../../sources/neary-2015-binary-pcp-five-pairs.md)). ∎

## Remarks

- **Where the hardness lives.** Each `Γ(w)` converges, and for each fixed index sequence the equality is a finite computation. What is undecidable is the existential quantifier over index sequences, the same as in PCP. The reduction transports PCP into the language of the inverse Syracuse tree; it does not make the Collatz map compute.
- **What it does not say.** Not that "does `n` reach 1?" is undecidable, not that the conjecture is independent of any theory, and not that `3x+1` is Turing-universal. [`collatz-conjecture-logical-form`](../collatz-conjecture-logical-form/README.md) (d) shows that any reduction making "reaches 1" a halting signal would already disprove the conjecture; this reduction avoids that by keeping every orbit convergent. The archived note stated the same scope: "do not describe this as ordinary Collatz halting undecidability".
- **A related formulation (archived, not migrated).** With the blocks `κ(0) = (1, 1)`, `κ(1) = (1, 2)` and terminal delimiter `(2)`, two terminated valuation words are prefix-comparable iff the binary words are equal, and exact positive cylinders of valuation words intersect iff the words are prefix-comparable. This gives a cylinder-intersection version of the same reduction (`archive/handoff/COLLATZ_PROGRAMME_MASTER_HANDOFF.md` §13.3).
- **Novelty.** Undetermined. Encoding words into inverse Collatz trees is a natural idea, and the literature (in particular around [Conway](../../../../sources/conway-1972-unpredictable-iterations.md) and [Kurtz–Simon](../../../../sources/kurtz-simon-2007-generalized-collatz.md)) has not been searched for it.

## History

- Reduction by the ChatGPT main lane (Codex), recorded in the archived master handoff §13.3 (never a node). Migrated with full proof and scope 2026-11-01 by the Claude cycles lane (Opus 5.5), directed by Santiago Armstrong.
