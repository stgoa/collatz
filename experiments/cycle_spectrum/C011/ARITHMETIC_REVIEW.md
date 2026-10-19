# C011 — Independent arithmetic review and author checker account

**Result: PASS for the two reviewed mathematical notes, within their stated
dependencies.** No mathematical error was found. This is an agent review,
not a human referee report, formal verification, or novelty assessment.

## Independence and source versions

The reviewer independently read [ROTATION_DEFECTS.md](ROTATION_DEFECTS.md)
and [DEFECT_OBSTRUCTIONS.md](DEFECT_OBSTRUCTIONS.md), written by other
agents. The reviewer authored [check_rotation_defects.py](check_rotation_defects.py).
Its implementation inspection and successful write/replay runs are therefore
**author checks**, not independent replay. Separate agents performed their
own replays; those belong in their own reports and the root review.

| File | Reviewed SHA-256 |
| --- | --- |
| `ROTATION_DEFECTS.md` | `9b390b7f8e456bbf52f3563cf7fe4243cf052846a1175dc0d4098a11ba59c801` |
| `DEFECT_OBSTRUCTIONS.md` | `a769a6a5238b123dd561c3097adb00aaa6556c8cdfc18e535fd8234ad523ea79` |
| `check_rotation_defects.py` — author check | `ba9a2b7fb269d619378c4c7b25d3cb6430e5a8078ea5658e0d81b71ba2d855ad` |
| `rotation_defect_audit.json` — author replay | `1eee49577e35bf5f28aac0ba2a572c8a863266575c4a0e2a4babf2f233d9844d` |

This review treats the effective two-logarithm estimate cited through C006
as an explicit imported input. It checks the deductions from that input;
it does not independently reconstruct that published theorem. The evolving
explicit exclusion in `EXCLUSION.md`, its newer published integer-period
bound, and its constant checker are outside the pinned scope of this review.

## 1. Two complementary arcs and terminal valuations

Exactly two mismatches preserve the multiset of valuation letters, so the
two unequal letters must be swapped. A repeated word would multiply every
nonzero mismatch count by its repetition number; a base mismatch count
cannot be one. Thus this hypothesis already forces primitivity. The shift
graph has the stated residue-class components, and both nonzero changes
must lie in one component because the changes sum to zero on each component.

After cutting at the smaller initial letter, the prefix exponent changes
by `k` precisely on positions 1 through `ell`. Factoring the corresponding
intercept terms gives the displayed positive arc contribution. Recutting
at the other defect changes its last valuation. Since the intercept ignores
that final valuation, the complementary original arc has exactly the same
intercept. This justifies using the original totals summing to `A`.
The cancellation factor is coprime to 6, so both explicit powers may be
removed and

```text
g divides (2^k-1) gcd(C_u,C_v).
```

This is divisibility, not equality. The exact cut identity leaves
`gcd(q,2^P_r-3^r)` as an extra factor. The generated word `(3,7)` and
the actual `q=35` and `q=505` controls exhibit that distinction.

The stronger intercept envelope correctly keeps the terminal valuation:

```text
C_z <= 2^(S-l-(b-1)) (3^l-2^l).
```

The exponent is nonnegative, including one-letter arcs. The two terminal
letters `a+k` and `a` account for the complete improvement
`A-m-k-2a+2` in the product bound. Dropping only the nonnegative
`2a-2` term gives the weaker bound checked by the finite script.
The subsequent denominator inequalities and strict endpoints follow
by dividing the positive `D` and using the exact hyperbolic-sine identity.

## 2. Amplitude-free bounded-denominator finiteness

I checked each stage of the new argument, rather than stopping after a
period bound.

1. A positive word containing the upper defect letter has `k<=A-m`.
   Consequently the terminal-corrected estimate gives
   `g<2^A(sqrt(3)/2)^m` and
   `q>(1-3^m/2^A)(2/sqrt(3))^m`, without an amplitude assumption.
2. For `A<2m`, the cited effective lower bound on
   `delta=A log 2-m log 3` implies the displayed polynomial lower
   bound on `1-exp(-delta)`. After reducing its constant to at most
   one, the elementary inequality `1-exp(-x)>=x/2` on `[0,1]`
   supplies the claimed factor. Larger `delta` only strengthens it.
   For `A>=2m`, the separate bound `7/16` holds for all `m>=2`.
   Thus fixed `q<=Q` bounds the period effectively in principle.
3. Bounded period alone leaves the letters unbounded. In the branch
   `A<m log_2 3+1`, it already bounds `A`. In the complementary
   branch, `D>=2^(A-1)` and the stronger two-arc bound yield
   `q>(1/2)2^(S/2)(2/3)^(m/2)`, with `S=A-k`.
   Fixed `q,m` therefore bound `S`.
4. Rotate the upper defect letter to the final position. Its intercept
   is independent of that final valuation and satisfies
   `C_rot<2^(S-a-m+1)3^m<=2^(S-m)3^m`. Since `g<=C_rot`,
   bounded `q,m,S` bound `D=qg` and then `2^A=D+3^m`.
   This completes the missing bound on `A`, `k`, and every letter.

The argument is not circular: the stages bound `m`, then `S`, then `A`.
It proves effective finiteness of every bounded-denominator layer of the
two-defect class conditional on the declared classical input. It alone
leaves finite denominator-one exceptions; a separate explicit exclusion
must supply and check its additional quantitative inputs.

## 3. Classification and the marker family

For adjacent defects the active shift component contains adjacent indices,
forcing a coprime shift. The weighted binary-mask identity gives
`rt=1 mod m`; the displayed mechanical mask has the same difference
equation and total. Their difference is constant on a transitive shift,
and its zero total forces equality. The note correctly limits the
mechanical valuation conclusion to amplitude one: a larger alphabet gap
is a substitution of the mask and need not be mechanical.

For `(3,b_n,4,b_n)`, unique markers force primitivity, the half-period
rotation has two unit mismatches, and the odd total paired with the
power-of-two period gives coprime totals. The expansion ratio is
`2^A/3^m>128/9`, not a bound of that size on `D/3^m`.
The block intercept and prefix estimates imply the full rational
minimum is greater than `n/128`. Shortcut local minima are exactly
`2(A_0-n)+2`; this count is kept separate from odd-only local minima.

The comparisons with the scoped C001/C002/C003/C005 classes are valid:
unique markers exclude doubly repeated blocks, coprime totals exclude
multiple equal-total or common-base blocks, and growing distances between
markers obstruct one fixed defect block across an unbounded subfamily.
These observations do not establish novelty against all literature.

## 4. Counterfamily review

For `w_t=1^t 2^(2t)`, I independently checked the intercept and the
reduction to

```text
g_t=gcd(4^t-1,3^t-2^t).
```

The cancellation steps use only units modulo the original denominator.
Taking `t=phi(M)` for any `M` coprime to 6 makes both gcd entries
divisible by `M`. The finite-unit permutation proof establishes that
statement for arbitrary `M`, independently of the twelve checked moduli.
The elementary fifth-power valuation argument gives the asserted exact
`v_5(g_(4*5^k))=k+1`.

There is one cyclic `1->2` transition, so the word is primitive. Its
starting fixed point exceeds one; the valuation-1 block increases and
the valuation-2 block decreases above one to that starting point.
Thus the minimum and exact odd raw arrows are as claimed. The explicit
denominator lower bound is greater than one, so this family is a
cancellation obstruction, not a denominator-one counterexample.

The rotation-prefix discrepancy remains bounded while its nonzero
plateau grows. The formula for the one-step intercept difference and
its gcd with `D_t` are correct. No extra cut factor is used in this
counterfamily. In Section 1, its displayed signed differences are
`w-R_1 w`; the checker labels the opposite convention `R_1 w-w`.
Their amplitudes and divisibility statements agree.

## 5. Author checker verification

The frozen script's final `--write` run and separate receipt replay both
completed with exit code zero and `status=PASS`. The replay compared the
entire reconstructed JSON. These executions do not independently verify
the mathematical proofs above.

The inspected implementation checks all 2,459 raw source instances across
333 parameters, their scaling, all 1,185 normalized cycles, and all eleven
fixtures. Its core rotated intercept and signed prefix-power differences
are computed directly rather than inferred from the historical certificate
helper. The full audit covers 27,646 rotations and 1,481,154 compared word
positions. Among the actual cycles, 192 two-defect rotations supply 384
oriented arc identities. All weak, endpoint-adjusted, and amplitude-free
quadratic bounds pass. The optional sharper `2a-2` factor is established
by the written proof but is not separately counted by this frozen script.

The generated controls include 51 two-run words, twelve prescribed
moduli, nineteen explicit repeated-word controls, and eight marker cases.
Zero rotational differences are retained for repetitions, including every
listed repetition of `(2)`. The marker cases check 1,020 raw arrows,
1,012 rotations, 510 mechanical-prefix bounds and the exact minimum and
shortcut-count formulas. No new seed census is run.

## 6. A concrete obstacle to extending the proof term by term

Use the already stored actual `q=359` cycle with

```text
w=(1,1,2,3,1,1,2,4),       g=73.
```

Its rotation by one has six mismatches. In the exact signed
prefix-power difference, the four nonzero terms are

```text
972, 3888, 1536, 14336,
sum = 20732 = 73*284.
```

Their residues modulo 73 are respectively `23,19,3,28`, all nonzero.
After removing powers of 2 and 3, the individual terms are `1,1,1,7`.
Thus the full difference is divisible by `g` while none of these
separate plateau contributions is. I recalculated these four terms
directly from the displayed word; no scan was needed.

With more than two defects, multiple prefix plateaus enter a coupled
sum. The two-arc proof cannot be extended by asserting divisibility of
each contribution. A useful extension must control cancellation between
those contributions or obtain additional independent relations. This
example does not obstruct such a stronger coupled argument.
