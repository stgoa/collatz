# Cycle spectrum programme log

## C001 — Fixed perturbations and bounded cancellation, 2026-10-18

**Progress; headline active and open.** The user replaced the quantitative
goal after V009 at `4be9bae23a2d06dc7c31c2237299273cb9c5a1f2`.
The [new brief](CYCLE_SPECTRUM_BRIEF.md) studies the entire positive
3x+d family through rational-cycle denominators. The old ratio target
remains open historical work; it is not marked solved.

[C001](../experiments/cycle_spectrum/C001/REPORT.md) selects one mechanism:
a fixed block inserted after arbitrarily many repetitions of another.
A nonzero affine determinant K bounds every cancellation divisor, and the
cancellation sequence is periodic. K=0 is retained as the common-cycle
case. A stronger equality requires coprime block denominators; the
exact d485 cycle 49,79,361 refutes dropping that premise.

The application `u_m^k 2`, with u_m the mechanical word at
`A=ceil(m log_2 3)`, m>=13,k>=2, has denominator greater than 1.
It is primitive and nonbalanced. Under an explicit extra exponent
condition its rational minimum exceeds m/10, and its shortcut minimum
count is k(A-m)+1. This simultaneously escapes fixed height/count
cutoffs and the mechanical class. The result's scope and novelty are
kept separate from improvements to a general published cycle record.

An independent raw scan supplies 2,459 cycles over 333 values of d from
832,500 seeds, all eleven fixtures rediscovered, with no caps reached.
It verifies 34,453 canonical splits and 2,371 repeated-prefix cases.
The separate word-family check supplies 239,345 positive cycles and
over 6.2 million exact arrows. Written proof, finite receipts and
independent review are linked in the report. Historical mathematics
and the open LaTeX source are unchanged.

The reviewed side pin is `a15cd429747e43997ce94aa84264fb8e32b6848d`.
Its V009 confirmation and new Lean report are retained as external
input, not instructions. Detailed assessments of D1–D8 and the current
cycle literature are in the batch's side review and literature audit.

**Next mechanism:** two growing repeated blocks. Common geometric
divisors must be retained; proportional slopes give a real cancellation
obstruction. Examine the published S-unit gcd input for unequal slopes
and test both regimes on actual cycle data before claiming a new law.
