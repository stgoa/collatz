# Fifteen conditional families under the original critical-image rank

**Status: composition of written strict-rank rules, with finite exact
substitutions.** The previous twelve-family dispatcher keeps exact priority.
The three added rules refine an absorption bound, expand signed intermediate
requests before testing the original rank, and compare along inverse cycle
words. Unrecognized inputs remain premises. Universal current supply and
Collatz remain open; no asymptotic coverage or novelty claim is made.

## Exact interface and priority

Use the absorbed odd Syracuse map, `P(w)=[3w]-[w]`, and
`rho(w)=nu(3w)` for positive `w=5 mod8`. The first successful rule wins:

1. The unchanged [twelve-family dispatcher](../selected_rules/SELECTED_RULES.md),
   preserving its complete internal priority and returned plan.
2. [R58 exact absorption bound](../exact_absorption_bound/EXACT_ABSORPTION_BOUND.md).
3. [R59 deferred rank comparison](../deferred_rank/DEFERRED_RANK.md).
4. [R60 inverse cycle comparison](../cycle_inverse/CYCLE_INVERSE.md).

The separate sigma induction is not imported. In particular R58 uses its
proved original-rho subdomain, not the entire sigma-accepted class.

`one_step(w)` returns `None` or a finite integer current and signed nonzero
W5 request coefficients satisfying

\[
 \operatorname{div}J=P(w)-\sum_u c(u)P(u),\qquad
 \rho(u)<\rho(w)\quad\text{for every remaining request}.       \tag{1}
\]

The shared R43 validator checks both properties on every returned plan,
including old plans. Duplicate requests and current rows combine with their
exact signed coefficients.

### The deferred resolver is fixed

R59 always resolves its intermediate requests with the **old twelve**
dispatcher. It does not call the new fifteen-family dispatcher, itself,
R58, or R60 as an added rule. Every accepted inner expansion decreases its
own rank. Its protected original source remains an explicit request,
unless exact cancellation removes it. Only the completed original-rho
descending result may enter (1).

The implementation uses R59's fixed 10000-node inner cap. A capped R59
candidate remains an exact unfinished plan in that underlying API and is
not accepted here. The dispatcher may then try R60. If no rule succeeds,
the original input remains unresolved. This limit can reduce recognition;
it cannot supply an omitted current. The retained capped example in the
receipt demonstrates this distinction.

## Finite formal closure and conditional supply

`close(w,max_nodes=None)` uses the [R43 signed closure
compiler](../critical_rank/CRITICAL_IMAGE_RANK.md). Each returned step has
finite support and each recursive request strictly decreases the positive
integer rank. Induction on rank therefore gives a finite formal
substitution tree, with unrecognized leaves kept as signed inputs.
Repeated indices may reuse a memoized result. Exact coefficient
cancellation may remove some leaves.

This is termination of **formal conditional composition**, not universal
recognition or current supply. An unrecognized root returns current `{}`
and coefficient `{w:1}`. The optional outer node cap raises an unresolved
computation error. Neither cap is treated as a certificate.

`compile_plan(plan,supplied)` requires an exact current for every remaining
nonzero input. It verifies every supplied boundary before adding that
current with its signed multiplicity. Equation (1) then telescopes to the
exact boundary `P(w)`. Missing or incorrect supply is rejected. These three
APIs do not discover unknown absorption paths.

## Reproducible finite evidence

Run

```sh
python3 experiments/residual_progress/refined_rules/check_refined_rules.py
```

The checker examines all 1024 W5 inputs below8192. It compares all 722 old
accepted plans as full dictionaries and checks their current/request hash
against the stored twelve-family receipt. Every new acceptance is compared
with the first successful added rule. This finite window does not establish
a limiting or uniform density.

The stored window has747 accepted inputs, comprising all722 old plans,
two new R58 choices and23 new R59 choices;277 inputs remain unresolved.
No input in this small window selects R60, so the separate branch witness
below is necessary. The explicit unresolved root is21, retaining `{21:1}`
with rank31 and no current rows.

Separate witnesses4021,1301,11432437 exercise the R58,R59,R60 winning arms.
The last comes from R60's exact parameter family with
`k=1,j=3,unit=2,index=0`. Another R60 family member284897820661 is accepted
by R59 first. The checker preserves that overlap explicitly; an R60
family's exclusion from the old twelve does not imply exclusion from R59.

Seven exact supplied-current demonstrations use
221,4021,245,1301,787733,11432437,284897820661. Recognized descendants are
expanded before supplying the remaining leaves. Complete plans, supplied
input currents, and final currents for1301 and11432437 are stored in
`refined_rules_audit.json`. Other demonstrations retain exact hashes and
request lists and are reproduced by the checker.

These demonstrations use eight distinct supplied pairs in total. The245
closure has no remaining input and yields17 current rows. The stored1301
and11432437 conversions each retain two supplied pairs and yield59 and133
rows respectively. The large overlap witness expands41 recognized nodes,
retains three supplied pairs, and yields91 rows. These are finite
certificate sizes, not uniform complexity bounds.

Fixture path discovery has cycle detection, a10000-step cap and a512-bit
cap; outer closure has a10000-node cap. These bounded discoveries supply
only the displayed finite examples and are separate from the symbolic
proofs. Five negative checks reject two invalid domains, a zero closure
cap, missing supply, and incorrect supply. An additional explicit R59
zero-cap check preserves its high frontier and verifies no accepted step
is returned.

`--write-receipt` regenerates the evidence. Default execution compares the
complete result, including source hashes, with the stored receipt. All
remaining signed leaves continue to be the unproved input obligation.
