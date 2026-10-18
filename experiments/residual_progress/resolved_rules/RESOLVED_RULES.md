# Seventeen conditional families with fixed inner resolvers

**Status: composition of written strict-rank rules, with finite exact
substitutions.** The fifteen-family dispatcher keeps its exact priority.
The added defect-resolution and lifted-inverse rules use the same positive
integer rank. Unrecognized inputs remain explicit premises. Universal
current supply and Collatz remain open; this note makes no density or
novelty claim.

## Interface and priority

Use absorbed odd Syracuse, `P(w)=[3w]-[w]`, and `rho(w)=nu(3w)` for
positive `w=5 mod8`. The first successful rule wins:

1. The unchanged [fifteen-family dispatcher](../refined_rules/REFINED_RULES.md),
   preserving every internal priority and its complete returned plan.
2. [R62 defect resolution](../defect_resolution/DEFECT_RESOLUTION.md).
3. [R64 lifted inverse comparison](../refined_obstruction/LIFTED_CYCLE.md).

The separate sigma induction is not imported. R62 uses only plans that
pass the original-rho comparison after retaining and combining all signed
requests. R63 is an obstruction result and R65 is a reformulation; neither
is an additional dispatch rule.

`one_step(w)` returns `None` or a finite integer current and signed W5
request coefficients satisfying

\[
 \operatorname{div}J=P(w)-\sum_u c(u)P(u),\qquad
 \rho(u)<\rho(w)\quad\text{for every nonzero request}.       \tag{1}
\]

The [R43 validator](../critical_rank/CRITICAL_IMAGE_RANK.md) checks the
exact boundary and every strict inequality on each returned plan,
including an inherited plan. Equal requests and current rows combine
with their integer coefficients; negative requests remain negative.

### The inner resolvers remain fixed

R59 retains the old twelve-family resolver. R62's optional
`fixed_resolution` audit retains the old fifteen-family resolver.
Neither resolver calls this new dispatcher. R62's dispatched `one_step`
uses its exact first/second continuation plans and the original-rho test;
its optional fixed-resolver audit is a separate interface. This keeps the
proved fixed-fifteen obstruction separate from the broader seventeen-rule
closure.

The inherited R59 inner cap stays in force. A capped candidate is not an
accepted strict-rank step; later dispatch rules may still be tried.
No omitted request is treated as supplied.

## Finite formal composition and supplied currents

`close(w,max_nodes=None)` uses the R43 signed closure compiler. Each
recognized node has finite support and its children have strictly smaller
positive integer rank. Induction on rank gives finite formal composition,
with every unrecognized leaf kept as a signed input. Memoization and exact
cancellation may reduce the resulting expression.

This formal termination does not prove universal recognition or provide
unknown currents. An unrecognized root returns no current rows and the
request `{w:1}`. An optional outer node cap raises an unresolved
computation error.

`compile_plan(plan,supplied)` requires a finite exact current for every
remaining nonzero request. It checks each supplied boundary and adds the
current with its signed coefficient. Equation (1) then telescopes to
`P(w)`. Missing or incorrect supplied currents are rejected. The three
public APIs do not search for unknown absorption paths.

## Reproducible finite evidence

Run:

```sh
python3 experiments/residual_progress/resolved_rules/check_resolved_rules.py
```

The checker examines all 1024 W5 inputs below 8192. All 747 previously
accepted plans are preserved as full dictionaries, and their combined
current/request hash matches the stored fifteen-family receipt. This
window has 747 accepted inputs and 277 unresolved inputs; neither new rule
adds an input in this small window. These finite counts do not establish
asymptotic coverage.

Separate witnesses exercise both added winning arms:

| Input | First successful rule | Earlier fifteen rules |
|---:|---|---|
|53173|R62 defect resolution|all unrecognized|
|36641534965|R64 lifted inverse|all unrecognized|

The R64 witness is `parameter_family(0,14,remainder=1)`: it uses zero cycle
blocks and a maximal point depth 14, with an eighteen-arrow inverse word.
Its direct conditional plan has nine signed requests. A further overlap
check uses 20405: R62 recognizes it, but the older R45 plan retains
priority unchanged.

Six exact supplied-current demonstrations use
221,53173,85941,15224757,11432437,36641534965. Recognized descendants are
expanded before supplying the remaining leaves. The demonstrations use
fourteen distinct supplied pairs in total and produce respectively
41,92,65,59,133,102 current rows. Complete plans, supplied current tables,
and output currents for 15224757 and 36641534965 are retained in
`resolved_rules_audit.json`; the other examples retain exact hashes and
are reconstructed by the checker. The two stored examples retain five
and four signed input pairs respectively.

The unresolved root 21 remains `{21:1}`, with rank 31 and no current rows.
Five negative checks reject two invalid domains, a zero outer closure
cap, missing supply, and a supplied current with the wrong boundary.
Fixture discovery has cycle detection, a 10000-step cap and a 512-bit cap;
formal closure demonstrations have a 10000-node cap. These bounded
fixtures are evidence only for the displayed inputs.

`--write-receipt` regenerates the evidence. Default execution compares
the complete result, including local source hashes, with the stored
receipt. Every remaining signed input remains an explicit proof
obligation.
