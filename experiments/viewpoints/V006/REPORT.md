# V006 — Quadratic separation and the full graph constraints

**2026-10-18. Written scoped theorem; full quantitative goal active and
unresolved.** The previous goal turn made progress by delivering V005's
proofs, controls and next obligations in85a07c2. This batch makes further
progress through a quadratic separation theorem and exact checks of the
proposed generalizations. It does not lower the completion threshold.

**Dependency clarification (V008):** the distinctness theorem for
non-eventually-periodic F is elementary. Applying it to an arbitrary
nonconstant invariant with a digit-count section excludes eventually
periodic F via V005/V004, and therefore uses the published Cobham theorem.

## 1. A quadratic theorem, with its hypothesis explicit

For any finite-valued F which is not eventually periodic, all sequences

```
n -> F(t+s_2(3^a n)),        a,t>=0,
```

are pairwise distinct. Each is obtained from F(s_2(n)) by t binary
digit-1 sections followed by a ternary digit-0 sections. Thus the joint
section family through depth D has at least(D+1)(D+2)/2 members.

The [complete proof](overlap.md) uses two arithmetic identities. The
digit count of m(2^k-1), for fixed positive odd m, is exactly k for all
sufficiently large k. Also `(2^K-1)/3^r` has exactly K/2 ones whenever
K is a positive multiple of2*3^(r-1). Complementary binary blocks prove
the latter fact. Choosing shifted inputs2^k-c then separates different
ternary exponents; equality would force a nonzero eventual period of F.

This gives a consequence beyond generic infinite-kernel growth. If a
hypothetical nonconstant Collatz invariant has even **one** positive
binary section

```
h(2^K n+r)=F(s_2(n)),       K>=1, 0<r<2^K,
```

then

```
kappa_h(K+4D) >= (D+1)(D+2)/2,       every D>=0.
```

V004's exact mixed-section formulas account for the factor4. If F were
eventually periodic, this section would be automatic, and V005 would
force h constant. Hence the nonperiodicity premise is justified in this
conditional application. For all N>=K, use D=floor((N-K)/4); the bound
has quadratic leading coefficient1/32.

**Missing coverage:** no argument proves that an arbitrary invariant
contains such a section. The all-invariant goal remains open. The
independent [quadratic review](QUADRATIC_REVIEW.md) checks the precise
theorem; root also checked the final proof and the control below.

## 2. The next structural shortcuts fail

### Linear growth need not contain a digit-count section

Let N_11 count adjacent11 pairs and let F indicate positive powers of2.
The sequence z(n)=F(N_11(n)) has cumulative binary kernel count at most2D
for D>=1. It obeys doubling and z(8n+5)=z(2n+1), and every section has
an infinite binary kernel. Yet none of its sections depends only on
binary digit count. Whole-section formulas and equal-weight distinguishing
inputs prove these statements in [overlap.md](overlap.md).

The example fails full invariance at3: z(3)=1 and z(10)=0. It rejects
extraction from the reduced graph hypotheses, not extraction using the
complete Collatz equations or the active goal itself.

### Linear orbit growth does not give linear semigroup growth

The [primary-source audit](joint_literature.md) examines a genuine theorem
on semigroups of linear growth. Its hypothesis counts transformations,
whereas our bound counts the orbit of one sequence. The explicit maps

```
T(n)=n+1,
U(n)=n+1+1_(n is a positive power of2)
```

have at most2D+1 states reachable from0 through depth D, but all2^D
words of length D define distinct transformations. A distinguishing input
near a large power of2 proves this exactly. These maps are an abstract
action control, not a claimed joint affine-section system.

The audit likewise separates rooted orbit counts from global word-pattern
counts and from the dimension of the full operator algebra. No applicable
general automatic-section theorem was found in this bounded search.

## 3. Decision: retain every radix identity in the overlap problem

The [graph interface](graph_interface.md) records the exact structure
that the controls above omit. Every joint section graph has five digit
transitions, six binary/ternary reordering identities, and compatible
outputs on zero transitions. The root has three additional identities
equivalent to the full Collatz coloring equations.

Conversely, those universal graph identities reconstruct actual sequences
in both bases. Whole-function distinguishability identifies the correct
vertices. This avoids assuming that a rooted orbit is a semigroup quotient.

Linear growth would force arbitrarily distant separating layers of a
fixed finite size. The next bounded probe is whether the full radix and
root identities force an automatic section in such a graph. Start with
the repeated one-vertex case as a discrimination test, then retain the
obligation to cover every possible bound. A proof for one layer size
alone would not complete the goal. No structure theorem for all linear
graphs is being assumed.

| Route | This batch's evidence | Decision |
|---|---|---|
| Distinguish mixed descendants | Exact quadratic theorem from one digit-count section | Retain; extraction remains unproved |
| Extract a digit-count ray from binary growth and return | Exact11-pair counterexample | Reject these reduced premises |
| Import linear-semigroup or low-pattern-complexity structure | Wrong counted object; exact action counterexample | Reject direct import |
| Use the full affine graph | Faithful representation and necessary small-layer condition | Preferred next bounded overlap test; no growth theorem yet |

## 4. Verification and controls

The [verifier](verify_examples.py) and [receipt](verification.json) check
18 balanced blocks through r=6;756 explicit witnesses separating pairs
among28 mixed states at each of two offsets;65,280 exact11-pair section
evaluations;15 equal-digit-count witnesses; and10,795 transformation-word
witnesses through depth7. The concrete mixed-state witnesses use F equal
to the indicator of positive powers of2. The binary return identities are
checked through input4095. Arbitrary-F, whole-function and all-depth claims
rest on the written proofs, not these finite samples.

The actual d5/d61 divisibility invariants and odd fixed cycles are retained.
The verifier exercises failure of the named d1 identity b(3n)=b(4n) on
those controls. The quadratic theorem itself is a generic digit-count
statement; the step excluding eventually periodic F uses the d1 theorem.
These checks do not address hypothetical divergence.

Root replay and [independent verifier review](VERIFIER_REVIEW.md) passed.
During development, the local Python version required replacing bit_count
with an equivalent elementary helper. The independent replay then exposed
a tuple/list serialization mismatch in the draft receipt comparison;
it was fixed and the final unchanged receipt replayed successfully. Neither
issue changed the mathematics. No frozen mathematical code/evidence was
edited, so the historical Phase6 gate was not rerun.

## 5. External input and completion audit

The [side review](side_review.md) records the fresh read-only sidekick pin
b999b7b. Its newest Lean density-dichotomy report is retained as external
verification input, with no new local replay or quantitative-growth premise.
Earlier V004 conditional-formalization scope and D-numbered dispositions
remain unchanged.

The completion requirement is still: for **every** nonconstant finite-valued
Collatz invariant, `sup_D kappa_h(D)/(D+1)=infinity`. This batch proves a
stronger bound only under an additional section hypothesis, and supplies
no extraction theorem covering the full class. Therefore completion is
unproven and the goal stays active. There is no external blocker.

The [delivery checks](delivery_checks.json) record links and exact frozen
comparisons separately from the mathematical review and bounded verifier.
