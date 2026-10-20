# Constructing annular currents

Started 2026-10-17, after commit `8d62dcc`. Status: constructive partial results proved and checked; universal completion open.
The preceding goal turn made progress: five-ray and annular theorems were
proved in writing, independently checked, persisted, and pushed. Universal
current construction and Collatz remain open.

## Objective

Find a structural reason that every required annular measure admits a finite
current, possibly with nonpositive residual, and prove termination of a
construction. Reductions, failed candidates, and finite evidence will be kept
distinct from achieving this universal objective.

## Falsifiable directions

1. Whole annular measures have a recursively controlled pattern of positive
   unresolved components, unlike isolated triples.
2. Arithmetic transport of the six bands closes in a family with a genuinely
   decreasing parameter, or contracts an integer-valued residual potential.
3. The five-ray scalar comparison can be lifted to a finite graph certificate;
   otherwise identify the precise extra assumption such a lifting needs.

## Work plan

- [x] Revalidate repository standing and active goal.
- [x] Examine component structure and construct finite annular examples.
- [x] Investigate transport, residue profiles, and cancellation potentials.
- [x] Audit constructive lifting of the five-ray comparison.
- [x] Prove or refute the resulting concrete candidates.
- [x] Persist useful arguments and evidence; update standing as warranted.
- [x] Verify the integrated changes and compile the existing LaTeX note.

## Findings and pivots

### 1. Finite components become infinite partial certificates

The incremental historical graph search found actual cross-band cancellation before absorption was exposed. At N=168 an exact aggregate certificate appears at depth 41, while separate-band certification on the same graph requires depth 44. Three balanced sources remain unlinked to 1.

An affine lifting lemma now turns any checked finite common-tail tree into an infinite family of exact arithmetic current identities. Its slopes preserve every exact valuation. A five-source tree from A_96 admits two parameter classes that fit the actual annuli. All admissible copies can be packed simultaneously: 45 gcd obstructions prove the ten source progressions disjoint. Copies exist for every allowed N>=168 and for N=96..152; the specific family is empty at N=160.

Five short-chain families supply another universal partial current with zero positive cost. Their sources are disjoint from the packed five-source tree. The combined constructor deletes positive mass `D(N)+3C(N)=73N/48+O(1)` from an initial `99N/4`, with positive current cost at most `3C(N)`. It returns the full finite current and exact residual. Its remaining positive mass is not resolved.

Full proof: [affine components](components/AFFINE_COMPONENTS.md) and [arithmetic reductions](arithmetic/ARITHMETIC_RESULTS.md). Reusable entry point: [combined_partial_current.py](arithmetic/combined_partial_current.py), function `build_combined_partial_current(N)`.

**Pivot:** complete cancellation with an everywhere nonpositive current is false. Exact finite witnesses are `H_53(A_96)=699` and `H_9(A_384)=42`. Retain positive cost in the target.

### 2. A contraction exists, but its residual family is not closed

Collapse each `F(x)=4x+1` chain to its unique root, discarding root 1. The resulting R satisfies `PR=P`, so `mu=(I-P)(mu-Rmu)+Rmu` is an explicit partial current identity. For every annulus,

`||R A_N||_1=||P A_N||_1=171N/4-|c_N| <= (19/22)||A_N||_1`, with `|c_N|<=3`.

The proof counts six exact entry profiles, including absorption. The correction may vanish; N=80000 is a checked example. However, R is idempotent and its residual retains at least 4N positive mass. Repeating the same collapse cannot finish it.

**Pivot:** the original six-band fixed-modulus family is not closed under literal repeated pushforward. Its outer profile has least even period `2*3^(t+2)` after t steps. A successful closure must carry growing arithmetic information or change the representatives by exact currents. The scoped obstruction permits both.

Full proof: [arithmetic reductions](arithmetic/ARITHMETIC_RESULTS.md).

### 3. The scalar comparison leaves an explicit finite-graph obligation

On an exposed graph, every positive component indicator is an exact dual obstruction. The sum Phi of positive nonabsorbing component masses is a nonincreasing integer, with zero equivalent to an available nonpositive-residual current. It can remain positive on a plateau. At N=96, Phi=17 at depths 20..27 and Phi=0 at 28.

The source-scale quotient lifts to the exact measure identity `D_N=A_N+(I-P)K_N`. Pairing with a finite-component indicator includes the boundary flux `sum K_N(x)(q(x)-q(Sx))`. For the 83-vertex depth-27 component of A_96 containing 1819, the pairings are `10=17-7`. Every flux row and component vertex is stored. Exposing all K_96 rows kills the flux but leaves positive mass 17.

**Pivot:** neither dropping boundary flux nor closing it at one cutoff supplies termination. A proof must control further component mergers. Fixed binary residue projections are also insufficient: each band eventually projects to zero while retaining actual positive and negative integer atoms. A separate negative-domain certificate demonstrates why scalar work cannot replace componentwise information; it is not a positive Collatz counterexample.

Full proof and witnesses: [aggregate duality](duality/aggregate_duality.md).

## Next concrete proof obligation

For each required annulus on the 30 base-64 sequences, give a finite arithmetic rule that ends every positive exposed-component plateau: connect positive mass to sufficient negative mass or to 1. Since Phi is an integer, a strict decrease after each finite extension would prove termination. Alternatively, close the exact residuals of the partial constructions in a family with a proved decreasing parameter.

The current lemmas do not supply that rule. Infinite arithmetic template families, a one-pass norm contraction, and finite successful searches are substantive partial results, but none is a complete Collatz argument. Do not resume by assuming a generic tree lift covers an annulus, by reapplying 19/22 to an unproved residual class, or by treating coarse zero projections as integer matching.

## Verification and handoff

The scoped default checkers reproduce existing receipts and stored tables; `--write-receipt` deliberately regenerates them. All use exact integer arithmetic and explicit caps where trajectory discovery occurs.

- Components: two compiled templates, huge integer lift parameters, all 45 progression pairs, packing and cross-catalogue capacity at every 8|N through 4096; six graph diagnostics and full A_96/A_168 certificates.
- Arithmetic: 66 catalogue/norm cases, outer profiles at depths 0..4, and the logarithmic root-1 calculation at 80000. Combined full current/residual checked at 8, 72, 96, 160, 168, 384, 768, 6144.
- Duality: seven exact scale identities, binary projections at k=1..8, A_96 potential through depth 28, full boundary-flux and closure witnesses, the reflected negative-domain current, and independent norm calculations at nine cutoffs.
- Independent model reviews checked both capacity arguments, the norm proof, and transcription into the existing LaTeX document. No substantive gap was found; human review and formal verification remain outstanding.

The repository-wide command `python3 scripts/verify_all.py --cpp` passed on 17 October 2026, including all original archive/manifest checks, independent C++ certificates, prior audits, and the five new default checkers. The existing LaTeX note compiled successfully in the built-in editor. All 31 checked local Markdown links resolved, and `git diff --check` passed. Commit history records delivery of this research batch; the universal objective above remains open.
