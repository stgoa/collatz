---
id: five-ray-profile-completion-suffices
kind: result
title: Completing the complementary outer profile at every interleaved five-ray cutoff would prove Collatz by induction
status: written
claim: >
  Odd-only 3x+1 map, absorbing at 1. Order all cutoffs a 2^b, a in (12, 14, 16, 18, 21), b >= 9; consecutive
  ratios are 7/6, 8/7, 9/8, 7/6, 8/7, all below 3/2, and every cutoff is divisible by 512. Suppose a rule
  certifies, at every such N and using only a supplied exact current for U_N, every root of the complementary
  profile R'_N of halving-coalescence-return (equivalently, by retained-graph-complement-constructor and
  halving-coalescence-return, every remaining outer root of R_N). Then absorption extends from U_N to
  U_(3N/2), which contains the next cutoff, and induction from the checked base U_6144 gives every positive
  seed: the Collatz convergence statement. This is a conditional sufficiency statement; the universal
  completion rule is not constructed. A single factor-64 ladder is too sparse for the step. Separate per-root
  certificates may reuse already certified paths, while blocks combined into one annular submeasure need
  joint capacity accounting. The cited sufficient-set and inverse-count theorems (Andaloro 2000, Monks 2006,
  Monks et al. 2013, Krasikov-Lagarias 2003, Tao 2019) do not supply the needed height-controlled witnesses.
  No novelty is claimed.
authors:
  - ChatGPT main lane (Codex)
created: 2026-10-17
depends_on: [retained-graph-complement-constructor, halving-coalescence-return, annular-complement-outer-descent]
certificates: [check_induction_recompute.py]
evidence:
  - "r24_check.py, r24_check.json: side-lane probe (Claude side lane, 2026-10-17): the ordered cutoffs' ratios and divisibility over 355 cutoffs and the base (every odd seed <= 6144 reaches 1). Fails at its new path: it imports affine_controls from experiments/packet_currents/negative_controls/ by repository-relative path (now ../locally-collatz-like-control-barrier/). Passed at be73a66 as reviews/side_lane/r24_check.py (archive/legacy-checker-run-be73a66.md, exit 0)"
  - "../halving-coalescence-return/halving_return_audit.json: the legacy receipt in which the main lane reconstructed and checked the base U_6144"
reviewed_by:
  - by: Claude side lane (Opus)
    date: 2026-10-17
    link: r24_check.py
    scope: "Finite arithmetic (side-lane feed entry 2026-10-17 19:59, VERIFIED, main 8e2b5eb): over 355 ordered cutoffs the consecutive ratios lie in 7/6, 8/7, 9/8, so 3N/2 reaches the next cutoff, every cutoff is divisible by 512, and every odd seed <= 6144 reaches 1. The conditional step itself rests on the written constructions of R17 and R23, which were not re-derived; the status stays written"
aliases: [R24]
tags: [convergence, packet-currents, outer-residual, induction, sufficiency, literature-audit, conditional]
---

# Completing the complementary outer profile at every interleaved five-ray cutoff would prove Collatz by induction

## Statement

Odd-only Syracuse map, absorbing at 1. For `8 | M` and `N = 64M`, the remaining outer roots are the profile `R_N` of [`retained-graph-complement-constructor`](../retained-graph-complement-constructor/README.md), whose selected part is certified by [`halving-coalescence-return`](../halving-coalescence-return/README.md), leaving the complementary profile `R'_N`.

**Conditional induction.** Order the cutoffs `12·2^b, 14·2^b, 16·2^b, 18·2^b, 21·2^b, 12·2^(b+1), …` from `b = 9`. Consecutive ratios are `7/6, 8/7, 9/8, 7/6, 8/7`, all at most `7/6 < 3/2`, and every cutoff is divisible by 512, so the annular-block transfer of [`annular-complement-outer-descent`](../annular-complement-outer-descent/README.md) (which needs `M = N/64` with `8 | M`) is available throughout. If at every such cutoff a rule certifies every root of `R'_N` from a supplied exact `U_N` current, then the retained-graph and halving constructions extend absorption to `U_(3N/2)`, which supplies the next cutoff's input by extracting already certified paths; from the checked base `U_6144`, induction gives every positive seed. No larger absorption input is needed. The rule has not been constructed.

**Scope distinctions.** A single factor-64 ladder has too large a gap for this step; it must not be confused with the interleaved union. A direct root-path rule for every `8 | N ≥ 16` would also suffice (steps of 8); the annular-block alternative is stated only for `512 | N`. Independent certificates of individual roots may reuse an already certified positive source; combining blocks into one submeasure of `A_M` needs joint capacity bounds.

**Literature audit.** The primary sources read (Andaloro 2000; Monks 2006; Monks, Monks, Monks and Monks 2013; Krasikov and Lagarias 2003; Tao 2019) prove qualitative sufficiency, residue reachability, eventual predecessor counts or almost-all descent; none supplies, for every `N` and every exit `t` of a remaining root, a witness already certified at that same `N`, inside the finite certified interval or the active annular bands, with sign and capacity control.

## Proof

The legacy note "Sufficient sets and the R20 residual: primary-source audit" follows, lightly edited (headings demoted one level, links pointed to nodes). Its commands name pre-migration paths; see Certificates.

2026-10-17. **Status: literature audit and scoped reduction, not a Collatz proof.**
This note checks whether published sufficient-set or inverse-tree results
certify any part of the remaining R17/R20 outer profile. No novelty claim is
made for the local constructions.

### 1. Exact local question and clock conversion

Use the odd-only Syracuse map `S(x)=(3x+1)/2^v2(3x+1)`, absorbed at 1.
For `8|M`, put `N=64M`, and assume the finite exact current for all odd
seeds at most `N` that R20 explicitly requires. The R17 residual `R_N` is
supported on odd roots `x` in `(N,3N/2)`, with coefficients 1 or 2 and
the exact classes in [R17](../retained-graph-complement-constructor/README.md),
§4. Every such root has the valuation-one exit

```
t = (3x+1)/2 in (3N/2,9N/4),
x = 3 (mod 12)  =>  t = 5 (mod 18),
x = 7 (mod 12)  =>  t = 11 (mod 18).
```

These exits each have `A_M(t)=-1`; R20's conditional transfer certifies a
root when an independently constructed capacity-checked annular block
includes its exit as a negative source. Covering **every** exit at every
required cutoff is unproved. The transfer may then reuse the certified
path with the root's full coefficient, without reusing annular capacity.

There is no one-arrow inverse shortcut from an unresolved exit to the
known interval. Since `t=2 mod3`, its complete set of positive odd direct
predecessors is

```
F^k(x) = 4^k*x+(4^k-1)/3,    k>=0,    F(z)=4z+1.
```

The least one is `x>N`; every other is larger. Any known-input merger must
therefore use deeper inverse history, a later forward descent, or an exact
signed annular block. R17's component classification already exhausts the
short inverse history inside its retained cutoff graph. Indeed, solving
`3y+1=2^a t` requires odd `a` because `t=2 mod3`; writing `a=1+2k`
gives the displayed formula, and `t` odd makes this valuation exact.

Clock conventions differ: Andaloro uses the odd-only map, while the Monks
papers use the shortcut map `T(y)=(3y+1)/2` for odd `y` and `T(y)=y/2`
for even `y`. For a shortcut or unaccelerated orbit from an odd start,
deleting the intervening even steps gives the same odd states as `S`.
Finite merger statements transfer, but step counts do not transfer
unchanged. An even-state residue claim also needs translation.

### 2. Verified primary theorems and exact mismatch

| Primary source | What is actually proved | Mapping to the R20 exit `t` | Missing property |
|---|---|---|---|
| [Andaloro (2000), *On Total Stopping Times Under 3x+1 Iteration*](https://www.mathstat.dal.ca/FQ/Scanned/38-1/andaloro.pdf), introduction, Lemmas 2–4, Theorem 2 | For odd-only `T=S`, the progression `1 mod 16` is sufficient: proving convergence on that entire infinite progression would prove it for all odd integers. The paper also proves finite common-tail identities, including `S(4x+1)=S(x)` for odd `x`. | The common-tail/inverse-sibling mechanism already occurs in the literature. It resembles the local `F(x)=4x+1` sibling used by R17 to certify seeds below `N`. | Sufficiency does not assert that a particular `t` merges with a **previously certified** seed at most `N`, nor that the witness is in one of the finitely many active annular source bands. |
| [K. M. Monks (2006), *The Sufficiency of Arithmetic Progressions for the 3x+1 Conjecture*](https://monks.scranton.edu/files/pubs/SufficiencyRev4.pdf), Theorem 1.1 and Lemma 3.8 | Every nonconstant infinite arithmetic progression is sufficient for the shortcut `T`: every positive orbit merges with the orbit of **some** member of that progression. Lemma 3.8 constructs a merger with a number in prescribed congruence classes modulo factors of `2`, `3`, and an integer coprime to `6`. | For each fixed exit `t`, one may backtrace/merge into a prescribed infinite residue class. This validates residue-directed inverse search as a legitimate technique. | There is no bound placing that witness at most `N` or in `A_M^+` below `9N/4`; an infinite progression is not the finite certified interval `(0,N]`. The proof does not preserve the annulus's signed source coefficient or source capacity. |
| [Keenan, Kenneth G., Kenneth M., and Maria Monks (2013), *Strongly Sufficient Sets*](https://www.mathematicalgemstones.com/maria/papers/mmmm.pdf), Corollary 5.8 and Theorem 6.4 | Every shortcut-`T` orbit contains a state `2 mod 9`. Every divergent orbit and nontrivial cycle contains `20 mod 27` (the latter is a conditional statement about those possible orbits). | For the `x=7 mod12` root class, `t=11 mod18` is **already** `2 mod9`, so Corollary 5.8 gives no forward motion. For `x=3 mod12`, it forces a later residue encounter without a height limit. | A modular hit is not a hit in `(0,N]`, a known absorption graph, or a negative annular source with checked capacity. It cannot by itself terminate an E0 plateau or a source-empty auxiliary component. |
| [Krasikov and Lagarias (2003), *Bounds for the 3x+1 Problem Using Difference Inequalities*](https://arxiv.org/html/math/0205002v1), abstract and §6 | For a fixed target `a` coprime to 3, inverse-basin counts have an `X^0.84` lower bound for all sufficiently large `X` (with threshold depending on `a`). | Every R20 exit is coprime to 3. The theorem supplies many eventual predecessors of each fixed exit at sufficiently large heights. | `a=t` itself grows with `N`; the theorem gives no uniform threshold `X=O(t)`, no predecessor in the particular finite annular bands, and no sign or source-capacity matching. Its exponent alone does not certify an R20 exit. |
| [Tao, *Almost All Orbits of the Collatz Map Attain Almost Bounded Values*](https://arxiv.org/html/1909.03562v7), Theorems 1.3 and 1.6 | For every function `f(n)->infinity`, almost all initial integers in **logarithmic density** have an orbit value below `f(n)`; Theorem 1.6 states the odd-only Syracuse version explicitly. | This is an exceptionally strong statistical descent theorem and confirms that height descent is typical. | Logarithmic-density exceptions may intersect infinitely many R20 cutoffs; the theorem gives no pointwise statement for each root and no exact finite current at a specified cutoff. |

The Krasikov–Lagarias assertion about a general fixed target is explicit in
their abstract. It is still an asymptotic, target-dependent statement. No estimate in the sources reviewed
has the joint quantifiers `for every N` and `for every t` in R20's finite
exit set with an input witness already certified at that same `N`.

### 3. Overlap and a useful logical barrier

**Precedented ingredients.** Finite parity/valuation words, inverse
branches, coalescing affine families, and arithmetic-progression merger
theorems predate this programme. Andaloro's common-tail identities and
Monks's backtracing formulas are direct precedents for the broad style of
R17/R20. Monks (2006), Lemmas 2.1–2.4, explicitly attributes backtracing
formulas to Wirsching. The R21 finite guard's use of exact residue words is
therefore not, by itself, a novelty claim. Its precise six-band source
window and sharp 63-arrow source-span are more specific; this audit found no
primary theorem with those exact hypotheses or conclusions, which is not a
proof of novelty.

**Why qualitative sufficiency cannot discharge the transfer.** The merger
witness in an infinite progression need not lie in the finite certified
input set or active positive annular bands. R20 still needs that
additional height control and a valid exact block.

**Strength of a universal completion.** It suffices to complete the
remaining R17 roots on the **five interleaved rays**, with a supplied
exact `U_N` current as the only absorption input. To see this, order

```
12*2^b, 14*2^b, 16*2^b, 18*2^b, 21*2^b, 12*2^(b+1), ...,
```

starting at b=9. Consecutive ratios are `7/6, 8/7, 9/8, 7/6, 8/7`,
all at most7/6<3/2. Each cutoff is divisible by512, as required by R20's
annular input `M=N/64` with `8|M`. A universal completion would extend
`U_N` to `U_(3N/2)`, hence supply the next cutoff's `U` current by
extracting its already certified paths. The finite base `U_6144` is
reconstructed and checked in the
[halving receipt](../halving-coalescence-return/halving_return_audit.json).
Induction on this increasing unbounded sequence would therefore prove
Collatz. By the [halving construction](../halving-coalescence-return/README.md),
one need only complete its complementary profile `R'_N` at every cutoff
in this sequence. That universal completion remains open.

A single factor64 ladder does have a gap too large for this extension.
It must not be confused with the interleaved union of all five dyadic
rays. No larger absorption input is needed once a valid universal
completion rule on that union is supplied. For comparison, a direct
root-path rule for every `8|N>=16` would also suffice by induction in
steps of8; R20's annular-block alternative is stated only for `512|N`.
These are conditional sufficiency statements, not constructions of the
missing rule.

Likewise, R21's bound finds all *original annular sources* in one restricted
E0 component in at most 63 arrows. A finite template count cannot be
iterated as a descent proof: R21 gives explicit positive mass entering a
source-empty auxiliary component, and its quarter-height inequality is
relative to the possibly enormous exit vertex. Any imported modular or
inverse theorem must also handle those auxiliary components.

### 4. Concrete research interface left by the audit

A potentially useful new theorem would be a **height- and capacity-controlled
inverse statement**, not merely residue reachability:

> For each `8|M` and each exit `t=(3x+1)/2` of a remaining `R_(64M)` root,
> construct a finite exact valuation-word witness that either reaches a
> seed at most `64M`, or belongs to a finite signed block
> `P-Q=(I-Push)J` with `0<=P<=A_M^+`, `0<=Q<=A_M^-`, `Q(t)=1`.
> Each block must satisfy its own source bounds and exact divergence.
> If blocks are combined as one annular submeasure, account for their
> source capacities jointly. If they are separate certificates of
> individual roots, the same already certified positive source may be
> used in more than one proof. Prove termination whenever the rule
> continues through source-empty E0 components.

This is a **candidate proof obligation**, not an available theorem. One
testable intermediate task is to partition the `t=5,11 mod18` exits by
exact valuation cylinders and record, for each cylinder, (i) the first
certified descent or merger word, (ii) its maximum height and first descent
cutoff, (iii) the annular coefficient of every attachment, and (iv) which
source capacity it consumes. Failed cylinders and growing required depths
must remain explicit. The unbounded annular exposure-depth theorem rules
out a bounded-depth annular constructor; it does not by itself rule out
every possible short comparison with an arbitrary supplied absorption graph.

### 5. Checks and source boundary

- Read `README.md`, `archive/docs/RESULTS.md` (R17, R20, R21), R17's retained-graph
  proof, R20's transfer proof, R21's source-cluster proof, and `AGENTS.md`.
- Read the cited author/publisher primary pages or PDFs, including the
  proofs around Monks (2006) Lemma 3.8 and Monks et al. (2013) Corollary 5.8.
  The modulo-18 mapping above is direct arithmetic from R17/R20.
- Attempted the required side-lane fetch. This checkout denies writing
  `.git/FETCH_HEAD`; the cached feed at commit
  `125dd1cf1c4ba41b48e43eb248028e8dbee969fd` was skimmed, but no
  finding from it is used in this note.
- This is a prose-only audit. It changes no mathematical implementation,
  stored certificate, shared result ledger, or LaTeX source.

## Certificates

- [`check_induction_recompute.py`](check_induction_recompute.py) (written at the B09 migration, under 1 s, standard library). Checks the 355 ordered cutoffs with `9 ≤ b ≤ 79` (ratio pattern `7/6, 8/7, 9/8, 7/6, 8/7`, all below `3/2`; divisibility by 512; the pattern is periodic in `b`, which is the general statement) and the base: every odd seed `≤ 6144` reaches 1 (cycle detection and a step cap).
- The legacy folder had no checker for this note; the side-lane probe `r24_check.py` is evidence only.

## Remarks

- **The open target** is [`five-ray-complementary-profile-completion`](../../questions/five-ray-complementary-profile-completion.md). Under Collatz the required certificates exist, so it is equivalent to the convergence statement, not a weakening.
- **Sources.** Monks 2006, Monks et al. 2013, Krasikov–Lagarias 2003 and Tao 2019 are [`monks-2006-sufficiency`](../../../../sources/monks-2006-sufficiency.md), [`monks-2013-strongly-sufficient`](../../../../sources/monks-2013-strongly-sufficient.md), [`krasikov-2003-predecessors`](../../../../sources/krasikov-2003-predecessors.md) and [`tao-2019-almost-all`](../../../../sources/tao-2019-almost-all.md); they are compared here, not assumed. Andaloro's paper has no source node (it is not an input). A displayed step of a further sieve paper was checked and fails: [`ansari-sieve-step-counterexample`](../ansari-sieve-step-counterexample/README.md).
- **Precedent.** Finite parity words, inverse branches, coalescing affine families and progression mergers predate this programme (Andaloro's common-tail identities, Monks's backtracing formulas, attributed there to Wirsching). The halving identity uses precedented common-tail arithmetic; no novelty claim is made.
- **The candidate interface of §4** ("a height- and capacity-controlled inverse statement") is a proof obligation, not an available theorem. The side lane's cylinder experiments on it are recorded in [`cylinder-certificates-outer-residual`](../../attempts/cylinder-certificates-outer-residual/README.md).

## History

- Migrated from `experiments/residual_progress/sufficient_sets/SUFFICIENT_SETS_AUDIT.md` (legacy ID R24; the folder's second note, `RECURSIVE_SIEVE_AUDIT.md`, became [`ansari-sieve-step-counterexample`](../ansari-sieve-step-counterexample/README.md), alias R24-b) at commit `be73a66`, by the B09 migration (Claude, Opus 5.5), with the side-lane probe `reviews/side_lane/r24_check.*`; `check_induction_recompute.py` was added at the migration. Legacy status: "elementary written conditional sufficiency, with a checked finite base; universal completion remains open" (the note itself: "literature audit and scoped reduction, not a Collatz proof").
- Main lane (ChatGPT, Codex), 2026-10-17, from commit `46198fb`. A draft confusion between one factor-64 ladder and the interleaved union was caught during review and corrected. The main lane's read-only check of §§3–4 (in [`side_lane_review_20261017_latest.md`](../outer-residual-strong-induction-support/side_lane_review_20261017_latest.md) §6) is its own and not independent. The side lane's finite check is recorded under `reviewed_by`. The note records that the side-lane feed at `125dd1cf` was skimmed and not used.
