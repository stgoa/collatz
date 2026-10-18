# Lau source scope and dependency audit

Status: **completed source audit and independent formal replay; the exact formal-source theorem is accepted as a supplied premise**.
The source build, eight statement/axiom reports and fresh replay into the same Lean kernel passed; see [formal_replay.json](formal_replay.json).
Batch: P6-004, C.1a. Date: 2026-10-18.

This note preserves the chronological source inspection, followed by preparation notes.
Statements below that checks were pending describe those earlier stages; the completed
receipt above supersedes them. The full article remains unavailable and no complete
human proof review is claimed. Collatz remains open.

## 1. Source identity and reproducibility

- Author: Kenny Lau, *Explicit positive lower density for the Collatz Conjecture*,
  [Hexagon 2610.00249v1](https://hexagonmath.org/2610.00249v1), 2026-10-14.
  **Hexagon is not arXiv**; the numerical identifier must retain its provider.
- [Pinned repository](https://github.com/AxiomMath/CollatzPositiveDensity/tree/3a38bfbb70379e051b51155def1423846fab3a90):
  `3a38bfbb70379e051b51155def1423846fab3a90`.
- [Downloaded source archive](https://codeload.github.com/AxiomMath/CollatzPositiveDensity/tar.gz/3a38bfbb70379e051b51155def1423846fab3a90):
  787477 bytes; SHA256
  `a97925bc3888a37476238c1d56de9e745b76a970a82e2771cbdc20c810828b77`.
- Temporary materialization: `/tmp/collatz_p6_lau_3a38bfbb7037`.
  Static scan receipt: `/tmp/collatz_p6_lau_static_audit.json`.
- Compressed comparison artifact:
  `/tmp/collatz_p6_lau_3a38bfbb7037_source.tar.gz`. The initial download was extracted
  in memory. This later re-download was accepted only after its SHA256 matched the
  originally recorded archive hash above; it supplies exact pinned archive bytes for
  comparing the files used by the replay.
- The latest independent side-lane input was reported by the batch owner as
  `e4f82311a804ecd1befaaa5e255e41c6d5d0c44c`; its proposed verification sequence is
  guidance reviewed by the owner, not evidence that the theorem is verified.

The primary landing-page abstract and the pinned author's README were accessible. Direct
access to the full Hexagon paper was unavailable during this audit. Thus the detailed
statement match below is to the primary formal challenge and repository definitions,
supported by the abstract; it is not a page-by-page comparison with the complete article.
The separate Mazur companion remains a different source and proof obligation.

## 2. Exact public statement

Put

\[
L=2^{2^{2^{87640}}},\qquad c(t)=\frac1{t^4L},\qquad X_0(t)=2^{t^3L}.
\]

The strongest public declaration takes **any natural target \(t\) with \(3\nmid t\)**
(therefore \(t>0\)) and **every integer \(N\ge X_0(t)\)**. It bounds below by \(c(t)N\)
the number of odd \(n<N\) that both:

1. reach \(t\) under the ordinary map within \(\lfloor10.46\log(n/t)\rfloor_+\) steps;
2. reach \(t/2^{v_2(t)}\) under the accelerated map within
   \(\lfloor3.4881\log(n/t)\rfloor_+\) steps.

There is no hypothesis that the target reaches 1, is nonperiodic, or belongs to a prechecked
finite set. The count is normalized by **all** \(N\) integers, while the counted sources are
odd. For odd targets coprime to 3 the accelerated endpoint is the target itself. Sources are
distinct integers, not weighted histories. See the
[formal challenge](https://github.com/AxiomMath/CollatzPositiveDensity/blob/3a38bfbb70379e051b51155def1423846fab3a90/Challenge/Basic.lean).

The four configured public theorem names are:

```text
positive_density_collatz_reaches_one
positive_density_collatz_and_collatzAccel_reaches_one
positive_density_collatz_and_collatzAccel_reaches_of_coprime_six
positive_density_collatz_and_collatzAccel_reaches_of_not_three_dvd
```

The definitions use ordinary \(C(n)=n/2\) for even \(n\), \(3n+1\) for odd \(n\),
and accelerated \(S(n)=(3n+1)/2^{v_2(3n+1)}\). `ReachWithin` means existence of a hitting
time at most the supplied bound. The ordinary map retains the 1–4–2 cycle; hitting 1 agrees
with the repository's absorbing convention. Accelerated iterates start odd. The logarithmic
quotient is **real division**, confirmed in the explicit casts of the internal and endpoint
proofs. Decimal coefficients denote exact rationals. Natural floor truncates negative inputs
to zero. See
[Definitions](https://github.com/AxiomMath/CollatzPositiveDensity/blob/3a38bfbb70379e051b51155def1423846fab3a90/CollatzPosDens/Definitions.lean).

Integer cutoffs suffice without a density loss: for a real \(X\ge X_0(t)\), choose
\(N=\lceil X\rceil\). Integer \(n<N\) is equivalent to \(n<X\), and \(c(t)N\ge c(t)X\).
The internal theorem also treats real cutoffs directly.

## 3. The internal counting theorem

`CollatzPosDens.densityConst_mul_le_ncard_reach` takes
\(s>0\), odd \(s\), \(3\nmid s\), and **every real** \(X\ge\operatorname{cutoff}(s)\).
Its result counts positive odd sources reaching \(s\) with both clocks. The construction's
constants are

\[
\begin{split}
\mathcal M(s)&=s\,4^{19+2\cdot3^{q_*}},\\
m(s)&=\left\lfloor(2^{39}\mathcal M(s)C)^{2/3}\right\rfloor+1,\\
c_M(s)&=\frac1{2^{33}\mathcal M(s)m(s)^{4097/2048}},\\
\operatorname{cutoff}(s)&=32\bigl(2^{B_{\rm ht}(s)}\mathcal M(s)+1\bigr).
\end{split}
\]

Here \(q_*\), \(B_{\rm ht}\) and \(C\) have definitions and bound lemmas; they are not
additional hypotheses. The proof picks one good seed, sets \(Z=X/32\), finds an admissible
generation, counts its sources in \([Z,32Z)\), and converts positive integer sources to
naturals injectively. See
[MnInternal](https://github.com/AxiomMath/CollatzPositiveDensity/blob/3a38bfbb70379e051b51155def1423846fab3a90/CollatzPosDens/Main/MnInternal.lean),
[CalM](https://github.com/AxiomMath/CollatzPositiveDensity/blob/3a38bfbb70379e051b51155def1423846fab3a90/CollatzPosDens/Recipe/CalM.lean),
[Mconst](https://github.com/AxiomMath/CollatzPositiveDensity/blob/3a38bfbb70379e051b51155def1423846fab3a90/CollatzPosDens/Recipe/Mconst.lean),
[CM](https://github.com/AxiomMath/CollatzPositiveDensity/blob/3a38bfbb70379e051b51155def1423846fab3a90/CollatzPosDens/Recipe/CM.lean), and
[X0](https://github.com/AxiomMath/CollatzPositiveDensity/blob/3a38bfbb70379e051b51155def1423846fab3a90/CollatzPosDens/Recipe/X0.lean).

### 3.1 Nonperiodicity is supplied, not assumed for the target

`GoodSeed s M` explicitly requires \(M\) to be nonperiodic under Syracuse.
`exists_goodSeed` proves such a seed for **every** positive \(s\) not divisible by 3.
It chooses two distinct predecessor candidates in the same favorable ternary residue class.
Both map in one accelerated arrow to the odd part of \(s\). A functional graph cannot have
two distinct periodic points with the same successor; therefore at least one candidate is
nonperiodic. Candidate magnitudes are explicitly bounded by \(\mathcal M(s)\).
This argument also works if \(s\) lies on a hypothetical nontrivial cycle. See
[GoodSeed](https://github.com/AxiomMath/CollatzPositiveDensity/blob/3a38bfbb70379e051b51155def1423846fab3a90/CollatzPosDens/Seed/GoodSeed.lean),
[GoodSeedExists](https://github.com/AxiomMath/CollatzPositiveDensity/blob/3a38bfbb70379e051b51155def1423846fab3a90/CollatzPosDens/Seed/GoodSeedExists.lean), and
[SyrPeriodicFiber](https://github.com/AxiomMath/CollatzPositiveDensity/blob/3a38bfbb70379e051b51155def1423846fab3a90/CollatzPosDens/Maps/SyrPeriodicFiber.lean).

For a nonperiodic seed, the same source cannot reach it at two distinct accelerated times.
Equal times and exact valuation words then give equal words, and the prefix-free central
blocks give equal history decompositions. Consequently the entire counted pair is recovered
from the integer source. The charge inequality is genuinely
\(Z\Upsilon\le M\#\mathcal S\), with no unexplained division by an orbit multiplicity.
See [SourceUniqueHistory](https://github.com/AxiomMath/CollatzPositiveDensity/blob/3a38bfbb70379e051b51155def1423846fab3a90/CollatzPosDens/Terminal/SourceUniqueHistory.lean) and
[Charge](https://github.com/AxiomMath/CollatzPositiveDensity/blob/3a38bfbb70379e051b51155def1423846fab3a90/CollatzPosDens/Terminal/Charge.lean).

### 3.2 The analytic input is explicit and lies inside the development

The traced chain is:

```text
primitive Fourier decay + gate mass/weight bounds
  -> high-regime oscillation -> telescoped mixing
  -> finite transfer + uniform residue pairing
  -> summable central increments -> surviving central mass
  -> terminal transport + length removal -> marked mass
  -> masked census + subdensity cap/deficit -> unweighted mass
  -> injective source charge + all-scale coverage -> MnInternal
  -> endpoint/time/tower comparisons -> public roots
```

Specific statements worth replaying or independently checking:

| Interface | Exact relevant assertion |
|---|---|
| `FourierDecay.ChPrimitiveDecay` | For every \(n\ge1\) and unit frequency \(\xi\bmod3^n\), \(|\widehat\mu_n(\xi)|\le C_*n^{-10241/4096}\), \(C_*=(160D_*)^{10241/4096}\). |
| `Mixing.Mixing` | For all \(2^{80000}\le m\le q\), \(\langle|\rho_q-\rho_m\circ\pi|\rangle_q\le2C/(3m^{3/2})\), where \(C=(477/20)(3200D_*)^{10241/4096}+159/10\). |
| `Seed.CentralIncrement` | For every odd positive integer \(M\) and \(n\ge6000000\), \(|Z_{n+1}(M)-Z_n(M)|\le F n^{5/2}\varrho^n\). The bound is independent of the numerical value of \(M\). |
| `Seed.ZTail` | For all these seeds and every \(n\ge N_*=6103914\), \(|Z_n-Z_{N_*}|<(47/32)2^{-24}\). |
| `Terminal.MarkLower` | A good seed, sufficiently large generation and admissible scale give \(\Theta>2^{-25}\). |
| `Terminal.Census` | \(\Theta\le(64/9)m^{4097/2048}\Upsilon+44M\) times the sum of mixing and subdensity-deficit errors. |
| `Terminal.ULower` | Under its stated fixed-target cutoff/generation conditions, \(\Upsilon>2^{-28}m(s)^{-4097/2048}\). |
| `Terminal.Coverage` | Every real scale above \(2^{B_{\rm ht}(s)}\mathcal M(s)\) is admissible for some sufficiently large generation. It is not restricted to a subsequence. |

These are source declarations, not axioms importing a qualitative theorem of Tao. The
explicit numerical mixing coefficient is proved within the source chain. Tao's corrected
[version 7](https://arxiv.org/abs/1909.03562v7), Proposition 1.14 and Section 6, provide the
published qualitative analytic context; their unspecified constants alone do not supply
Lau's displayed constants. The full low-level renewal/character-sum argument has **not**
been independently rederived in this note.

The table's pinned files can be located directly beneath
[CollatzPosDens](https://github.com/AxiomMath/CollatzPositiveDensity/tree/3a38bfbb70379e051b51155def1423846fab3a90/CollatzPosDens),
replacing each dot with `/` and appending `.lean`.

### 3.3 General endpoints and clocks

The final general-endpoint proof chooses \(3\le d\le8\) with
\(2^dt\equiv4\) or \(7\pmod9\), then \(s=(2^dt-1)/3\).
This \(s\) is a positive odd ternary unit, \(s\le2^8t\), and maps to \(t\) in
\(d+1\) ordinary steps and to the odd part of \(t\) in one accelerated step.
The inequality \(\log(s/t)\ge(d-2)\log2\) pays for these added steps inside the specified
clocks. Tower bounds compare the internal cutoff and density with \(X_0(t),c(t)\).
The proof explicitly handles natural-floor edge cases. See
[EndpointNotThreeDvd](https://github.com/AxiomMath/CollatzPositiveDensity/blob/3a38bfbb70379e051b51155def1423846fab3a90/CollatzPosDens/Main/EndpointNotThreeDvd.lean).

## 4. Static import and trust-boundary audit

A read-only Python scan stripped nested block comments, line comments and string literals,
then followed local Lean import declarations from `Solution.Basic`. It found:

| Quantity | Count |
|---|---:|
| Lean files in the pinned archive | 743 |
| Local modules in the `Solution.Basic` import closure, including its root | 738 |
| Distinct external import names directly encountered at that boundary | 146 |
| Closure from `Main.Main` | 736 |
| Closure from `Main.MainJoint` | 735 |
| Closure from `Main.EndpointJoint` | 734 |
| Closure from `Main.EndpointNotThreeDvd` | 732 |

The external boundary consists of 145 Mathlib module names and `Lean`. These are **module
import counts**, not the number of declarations in a proof term, not the transitive size of
Mathlib, and not an axiom report. A theorem's actual elaborated dependency graph remains a
formal-replay task.

The solution closure had zero lexical occurrences of `sorry`, `admit`, `axiom`,
`native_decide`, `unsafe`, `implemented_by`, `extern`, `elab`, `run_tac`, or `eval_expr`
outside comments/strings. `Challenge.Basic` contains four intentional `sorry` placeholders
and is outside this closure. Those placeholders are the comparison specification; they are
not by themselves evidence of a hole in the solution. `Attr.lean` registers a metadata tag
whose callback returns `pure ()`. Arithmetic `decide`/`norm_num` occurrences are present.
No claim about the internals of external tactics follows from this lexical scan.

Configuration read:

- `lean-toolchain`: `leanprover/lean4:v4.35.0-rc2`.
- `lake-manifest.json`: Mathlib commit
  `065356127b1dc0016f66b7283ce0ce2c4055aa55`; eight further pinned inherited packages.
- `lakefile.toml`: default target `CollatzPosDens`; Challenge and Solution are declared
  libraries but not default targets. No project build hook is declared there.
- `Comparator/comparator.json`: the four roots above, with only `propext`, `Quot.sound`,
  `Classical.choice` permitted and `enable_nanoda: true`.
- `formalization.yaml`: author-reported zero solution sorries and those same axiom roots.
  This is metadata, not our kernel output.
- `.github/workflows/lean.yml`: a general build workflow, not a comparator receipt. Its
  hosted-runner cleanup commands were read as data and were not executed here.

The observed axiom allowlist is not a measured theorem axiom set. A successful default build
alone would also not establish challenge/solution correspondence. Both distinctions must
remain visible in any later verification receipt.

## 5. Findings and remaining acceptance work

**No concrete mathematical statement mismatch was found in the inspected interfaces.**
In particular, arbitrary fixed targets, positive integer sources, real logarithmic division,
source uniqueness, explicit clocks and all sufficiently large cutoffs are represented in the
actual source. The potentially serious no-return issue is handled by the proved good-seed
selection rather than silently imposed on the target.

This supports continuing C.1a verification. It does not yet promote the claimed theorem to
a calibrated external premise. The acceptance checks for the precisely stated formal
source theorem are:

1. Review the pinned toolchain/dependency execution environment, then perform a clean
   isolated build explicitly including `Solution.Basic`.
2. Print the elaborated theorem types and actual transitive axiom sets for the four roots;
   compare challenge and solution, and retain complete exit codes/logs.
3. Check that these types express the mathematical statement adopted here, preserving
   domains, targets, cutoffs and clocks. The formal challenge and definitions suffice for
   adopting that exact statement; this does not assert complete correspondence with an
   unread article.

A clean source replay by this project, independent of the author's pipeline, using Lean's
kernel supplies independent replay in that sense. A second kernel implementation such as
Nanoda is **stronger optional evidence**, not an additional mandatory gate. The registry's
success badge is not our replay. Obtaining the complete primary article and comparing its
Theorem 1.3/Remark 1.4 remains desirable for the additional article-correspondence claim.

If those checks succeed, the lower-density conclusion applies to a hypothetical bad target
as well as to target 1. It would support the conditional reduction that a nonempty full bad
basin has positive lower density. It does **not** establish upper natural density one of
convergent seeds, a universal descent rule, or the Collatz conjecture.

## 6. Prepared statement-correspondence file

`StatementAudit.lean` is prepared for later compilation inside the pinned source project.
It imports `Solution.Basic`, never `Challenge.Basic`. The challenge's definitions and four
theorem types are copied into the independent namespace `LauStatementAudit`; each proof
placeholder is replaced by the corresponding `_root_` solution theorem applied to the same
explicit hypotheses. Successful compilation will check that the independently named
definitions and complete statements are definitionally equal to the supplied solutions.
This comparison does not substitute for the semantic review in Sections 2–3.

The deterministic text generator is `generate_statement_audit.py`. It refuses any input
whose SHA256 differs from the pinned challenge's
`e3e828be137de84f97cee84c4635f5f726fb975d1641dacff3b213130f5bf235`.
It changes the import, inserts the namespace, replaces the four proof terms, and appends
eight `#print axioms` commands and eight theorem displays with proof bodies suppressed.
There are no proof placeholders in the generated Lean file.

The generator's read-only `--check` passed against the saved file. Generated SHA256:
`8215385e2b8b10c7507f6587ba1aa53fd7f6825f2cd020eee13307b8bba447e2`.
**Lean compilation and its axiom/type reports remain pending at preparation time.**
The generator only processes source text and does not execute the external development.
