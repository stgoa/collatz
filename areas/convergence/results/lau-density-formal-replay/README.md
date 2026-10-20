---
id: lau-density-formal-replay
kind: result
title: An offline replay of the AxiomMath positive-density Lean development confirms its four statements and standard axioms
status: written
claim: >
  At AxiomMath/CollatzPositiveDensity commit 3a38bfbb70379e051b51155def1423846fab3a90 (source archive SHA-256
  a97925bc...8b77; toolchain leanprover/lean4:v4.35.0-rc2, checked against the release digest; Mathlib
  065356127b1d from the official cache), inside a network-denying macOS sandbox: lake build of Solution.Basic
  completed (4102 jobs, exit 0) with all 753 archive files unchanged; an independently named copy
  (namespace LauStatementAudit) of the four challenge statements and their definitions compiled against the four
  Solution.Basic roots; all eight #print axioms reports list exactly propext, Classical.choice and Quot.sound;
  and a fresh replay of the imported proof bodies into an empty environment of the same Lean kernel passed. So
  the four public statements (in particular: every natural t with 3 not dividing t and every integer
  N >= 2^(t^3 L), L = 2^(2^(2^87640)), has at least N/(t^4 L) odd n < N reaching t, with logarithmic clocks)
  are theorems of Lean + Mathlib under the standard axioms, relative to this trust boundary. Not established: the
  Hexagon article's prose (unavailable), a second kernel implementation, a from-source rebuild of every cached
  dependency, transfer to 3x+d, or anything about convergence.
authors:
  - ChatGPT main lane (Codex)
created: 2026-10-18
assumes: [lau-2026-positive-density]
certificates: [check_legacy_replay.py]
evidence:
  - "formal_replay.json: the completed replay summary (status PASS for the build, seal-build, statements and kernel stages, the eight axiom reports, semantic checks, trust boundaries, and the SHA-256 of every file of the record, including the generated StatementAudit.lean)"
  - "formal_evidence/: the stage receipts and logs copied byte for byte from the replay directory (build_status.json, build.log, seal-build, statements and kernel status and logs, cache retrieval receipts, source_snapshot.json comparing all 753 archive files, static_source_audit.json, lean_release.json, toolchain_receipt.json, the .sb sandbox profiles and replay_environment.json, isolation smoke and denial tests, runner_tests.log, the preparation manifest, the pinned source's Apache 2.0 UPSTREAM_LICENSE.txt and the preserved initial runner run_formal_replay_initial.py); see formal_evidence/README.md (its one link to the legacy lau_scope.md was repointed to this README at the migration, so its hash no longer matches the one pinned in formal_replay.json; tools/legacy_replay.py restores the original bytes). Three status receipts are about 9 MB each (seal-build_status.json, statements_status.json, kernel_status.json), because they bind the full proof-object inventories; they are kept byte-identical as the record. The receipts embed the original temporary paths (/tmp/collatz_p6_replay/...) of the replay; they are historical and cannot be edited"
  - "run_formal_replay.py: the hardened stage runner (build, seal-build, statements, kernel) that produced the receipts. It needs the prepared pinned sources, the Lean toolchain and the macOS sandbox, so it is not re-run here; its integrity tests are the certificate"
  - "generate_statement_audit.py: the deterministic generator of lean/audit/phase6/StatementAudit.lean from the pinned Challenge/Basic.lean (it refuses any input whose SHA-256 differs from e3e828be...f235); its --check mode needs that external file, so it is not re-run here. The generated file's SHA-256 8215385e...47e2 is pinned in formal_replay.json"
  - "replay_notes.md: the chronological dependency, cache, network and build-hook review, the same-kernel fresh replay scope (read from the bundled LeanChecker and Environment sources) and the receipt-hardening requirements"
reviewed_by:
  - by: Claude side lane (Opus)
    date: 2026-10-18
    scope: "Side-lane feed 2026-10-18 18:08 (D7 status, main bff8938): main's replay meets D7 items 1-4 (a source build of the library in a network-denied macOS sandbox with Mathlib from its official cache; #print axioms on all four theorems shows only propext, Classical.choice and Quot.sound; the statements match the side lane's own reading of Challenge/Basic.lean, feed 16:57). Caveat recorded there: the same kernel and prebuilt Mathlib were used. A reading of main's receipts, not a rerun"
  - by: Claude audit lane (Opus)
    date: 2026-10-18
    link: ../../../../lean/audit/README.md
    scope: "Independent replication of the same claim on another platform (lane 3, branch claude/lean-audit, an isolated Linux aarch64 container): from-source lake build of Solution.Basic (4107 jobs, no errors, no sorry warnings), #print axioms in a fresh process giving only the three standard axioms for all four theorems, and pp.all statements and the seven definitions they use byte-identical between Challenge.Basic and Solution.Basic; it also ran the authors' comparator and paranoid checkers, with the caveats recorded in lean/audit/README.md (comparator without its own sandbox; two unexplained rejections and one out-of-memory kill in a whole-library lake check --paranoid). It replicates the build, axiom and statement checks of this node; it did not inspect this node's receipts or StatementAudit.lean. The status stays written under this migration's rule for main-lane work"
aliases: [P6-004, P6-C.1a]
tags: [convergence, phase6, predecessors, density, lean, external-library, ai-generated, audit]
---

# An offline replay of the AxiomMath positive-density Lean development confirms its four statements and standard axioms

## Statement

Phase 6 route node **C.1a** asked for an audit of a new external input: the 2026 claims of a *linear* lower bound on Collatz predecessor counts, which would replace the Krasikov–Lagarias exponent 0.84 ([`krasikov-2003-predecessors`](../../../../sources/krasikov-2003-predecessors.md)). The input actually adopted is the Lean development of [`lau-2026-positive-density`](../../../../sources/lau-2026-positive-density.md); the separate manuscript chain of [`mazur-2026-predecessor-density`](../../../../sources/mazur-2026-predecessor-density.md) was re-derived in writing, conditional on Tao, in [`predecessor-density-conditional-reconstruction`](../predecessor-density-conditional-reconstruction/README.md).

**Provenance, kept as recorded.** Both 2026 sources are AI-generated: the Hexagon page states that AxiomProver "autonomously produced the mathematics in this paper and formalized it in Lean", and the Mazur manuscripts are hosted on ProofAtlas, which describes itself as "AI agents working together on new mathematics" (as recorded in [`lean/audit/`](../../../../lean/audit/README.md)). That is why the claim was built rather than read. The side lane's rule D7, accepted by the main lane on 2026-10-18, set the bar for promoting it to a premise: match the exact statement, build the pinned sources independently in isolation, and inspect the theorems' axioms and any native computation; author or registry build reports and source reading do not count.

**Result.** The replay passed every stage: the source build (4102 jobs), the statement comparison against an independently named copy of the challenge, eight axiom reports with only `propext`, `Classical.choice` and `Quot.sound`, and a fresh replay of the imported private proof bodies into an empty environment. The exact public statement is in §2 below. It counts **distinct odd sources** below `N`, normalised by all `N` integers, for **any** target `t` with `3 ∤ t`, with no hypothesis that `t` reaches 1 or is nonperiodic.

**Trust boundary.** Lean's trusted base and the official toolchain binary (checked against its published digest); pinned dependency sources and the official Mathlib cache (not every dependency rebuilt from source); the same kernel implementation for the fresh replay (not a second kernel); the macOS sandbox profiles (not a hermetic container). The full Hexagon article was unavailable, so the adopted statement is the accessible formal challenge, not a page-by-page match with the article.

## Proof

The node's argument is the audit below (the legacy `lau_scope.md`, preserved in its chronological order: §§1–5 were written before the build and §6 while preparing the statement file; their "pending" language is superseded by the completed receipt [`formal_replay.json`](formal_replay.json)), together with [`replay_notes.md`](replay_notes.md) for the execution environment and the receipts in [`formal_evidence/`](formal_evidence/README.md).

### 1. Source identity and reproducibility

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

### 2. Exact public statement

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

### 3. The internal counting theorem

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

#### 3.1 Nonperiodicity is supplied, not assumed for the target

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

#### 3.2 The analytic input is explicit and lies inside the development

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

#### 3.3 General endpoints and clocks

The final general-endpoint proof chooses \(3\le d\le8\) with
\(2^dt\equiv4\) or \(7\pmod9\), then \(s=(2^dt-1)/3\).
This \(s\) is a positive odd ternary unit, \(s\le2^8t\), and maps to \(t\) in
\(d+1\) ordinary steps and to the odd part of \(t\) in one accelerated step.
The inequality \(\log(s/t)\ge(d-2)\log2\) pays for these added steps inside the specified
clocks. Tower bounds compare the internal cutoff and density with \(X_0(t),c(t)\).
The proof explicitly handles natural-floor edge cases. See
[EndpointNotThreeDvd](https://github.com/AxiomMath/CollatzPositiveDensity/blob/3a38bfbb70379e051b51155def1423846fab3a90/CollatzPosDens/Main/EndpointNotThreeDvd.lean).

### 4. Static import and trust-boundary audit

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

### 5. Findings and remaining acceptance work

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

### 6. Prepared statement-correspondence file

`StatementAudit.lean` (now [`lean/audit/phase6/StatementAudit.lean`](../../../../lean/audit/phase6/StatementAudit.lean)) is prepared for later compilation inside the pinned source project.
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

### 7. Outcome

The completed record [`formal_replay.json`](formal_replay.json) has status PASS for all four stages:

| Stage | Receipt | Outcome |
|---|---|---|
| build | [`formal_evidence/build_status.json`](formal_evidence/build_status.json), `build.log` | exit 0, `Build completed successfully (4102 jobs)`, by the preserved initial runner [`run_formal_replay_initial.py`](formal_evidence/run_formal_replay_initial.py) |
| seal-build | `seal-build_status.json`, `seal-build.log` | binds the original build receipt and log to the archive-checked sources and the proof objects present at sealing time; it does not invent build-end object digests |
| statements | `statements_status.json`, `statements.log` | the four `LauStatementAudit` theorems compile from the four `Solution.Basic` roots; all eight axiom reports are exactly `Classical.choice`, `Quot.sound`, `propext` |
| kernel | `kernel_status.json`, `kernel.log` | `replaying StatementAudit with --fresh`, exit 0 |

The Lean file compiled in the statements stage is [`lean/audit/phase6/StatementAudit.lean`](../../../../lean/audit/phase6/StatementAudit.lean). It imports `Solution.Basic` (never `Challenge.Basic`), so it compiles only inside a checkout of the external project at the pinned commit, like `lean/Dichotomy.lean`.

## Certificates

- [`check_legacy_replay.py`](check_legacy_replay.py) replays, in the legacy layout, the main lane's unmodified `test_formal_replay.py`: eleven disposable receipt-integrity tests of the hardened runner [`run_formal_replay.py`](run_formal_replay.py) (stale-PASS invalidation, Popen failure, preservation of the initial live receipt, missing, failed or mutated predecessors, mandatory chain edges, exact and multiline axiom reports, disallowed and lookalike axioms, legacy sealing and conflicting object rebinding). They run no Lean, no network and no live stage; they certify the runner's fail-closed logic, not the Lean development. It fails at its new path only because it reads `StatementAudit.lean` from its own folder, which moved to `lean/`.

The Lean replay itself cannot be re-run by CI: it needs the external project, the toolchain and the sandbox. Its evidence is the receipts above. A reader who wants to reproduce it should follow `lean/README.md` (copy the file into a checkout of the external project at the pinned commit, `lake build Solution`, then `lake env lean StatementAudit.lean`) or the independent container audit in [`lean/audit/`](../../../../lean/audit/README.md).

## Remarks

- **Kernel-bug history.** In 2026 a Lean kernel soundness bug (#14576) was exploited by an AI-assisted Collatz "disproof"; it was fixed by lean4 PR #14577, merged 2026-07-28. The independent container audit in [`lean/audit/`](../../../../lean/audit/README.md) checked that the pinned toolchain `v4.35.0-rc2` contains the fix. This node's replay pinned the same toolchain but did not itself record that check.
- **What the replay supports.** The four Lean statements are theorems under the standard axioms, at the stated trust boundary. Any result that uses them lists [`lau-2026-positive-density`](../../../../sources/lau-2026-positive-density.md) under `assumes`: the first is [`nonabsorbing-set-linear-lower-density`](../nonabsorbing-set-linear-lower-density/README.md). A positive lower predecessor density is compatible with a nonprincipal cycle; it proves nothing about convergence.
- **Programme label none.** Independently replaying a supplied formal derivation was graded **none** under Phase 6's strict calibration rule, which asked for our own re-derivation of the numerical constants; the written reconstruction keeps Tao's unspecified constants. The side lane confirmed the label (feed 18:08).
- **Transfer.** Lau's numerical constants and clocks are audited only at `d = 1`; the statement's `d = 5` analogue is false (the multiples of 5 never reach 1, see [`baseline-obligation-transfer-controls`](../baseline-obligation-transfer-controls/README.md)). The qualitative transfer for targets other than 1 is in the reconstruction node.
- **Static scan scope.** The lexical scan found no `sorry`, `admit`, `axiom`, `native_decide`, `unsafe`, `implemented_by`, `extern`, `elab`, `run_tac` or `eval_expr` outside comments and strings in the `Solution.Basic` import closure; this says nothing about the internals of external tactics, which is why the axiom reports and kernel replay were required.

## History

Migrated from `experiments/phase6/linear_density_audit/lau_scope.md` (legacy batch `P6-004`, route node C.1a), with `replay_notes.md`, `formal_replay.json`, `formal_evidence/`, `run_formal_replay.py`, `test_formal_replay.py` and `generate_statement_audit.py`, at commit `be73a66`. `StatementAudit.lean` moved byte-identically to [`lean/audit/phase6/`](../../../../lean/audit/phase6/StatementAudit.lean), because Lean files live only under `lean/`. ChatGPT main lane, 2026-10-18. The receipt hardening of `run_formal_replay.py` and its tests were implemented by the reviewer of the replay configuration, at the batch owner's request (`replay_notes.md` §6). An earlier run of the finite gate ended with exit 143 and an empty log; the main lane's record leaves its cause unestablished, and the side-lane feed (17:58) reports that another lane terminated it by accident. It was not counted as a pass. The main lane graded C.1a **none**; the side lane confirmed (feed 18:08).
