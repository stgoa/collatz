# C012 — Independent review of the coupled system

**Verdict: PASS for the stated elementary matrix claims and their
declared limitations.** Reviewed on 2026-10-19 by a separate agent from
the author of `COUPLED_SYSTEM.md`. This is an agent review, not human
review, formal verification or a novelty assessment.

The reviewer authored `COUPLED_OBSTRUCTIONS.md`; that note is outside
this independent proof verdict. Its mathematical review is recorded
separately by the root and the exact-checking agent. The present reviewer
independently inspected and executed the root's shared-arc checker.

## 1. Compression and determinant

The mismatch cuts are placed after each differing last valuation, so
the interiors agree and the two arc intercepts really are equal. The
full rotated intercept equations have the factor D on their right
sides. This is consistent with using unreduced intercepts rather than
integer cycle states.

The entries of `W=D B^(-1)` agree with direct concatenation. Both B
determinants have sign `(-1)^(s-1)` and magnitude D. The identity

```text
M = -D B'^(-1)(B'-B)B^(-1)
```

therefore gives

```text
|det M| = D^(s-2) product_i |beta'_i-beta_i|.
```

Each difference is nonzero, so M is nonsingular over the rationals.
For s>=3 the adjugate consequence `g|det(M)c_i` is automatic from
`g|D`. This conclusion concerns that particular elimination. It does
not show that the original coupled equations are redundant.

Inside a matching arc, the difference recurrence multiplies by a
ratio of powers of 2 and 3. Thus block-start divisibility is equivalent
to every internal difference divisibility for moduli coprime to six.
The statement retains all these difference congruences; it does not
assert that the difference system alone encodes every requirement on
an actual cycle.

## 2. Larger minors and local Smith form

The proof of the larger-minor divisibility is valid over the integers,
including composite D. Every beta is a unit modulo D, so consecutive
rows of W are scalar multiples of the first row modulo D. Integer
representatives give `W=u v mod D`, and likewise for W'. Thus

```text
M=D N+R,   rank_Q(R)<=2.
```

Multilinearity in columns of an arbitrary k-minor gives at least k-2
factors D in every nonzero term. Consequently every k-minor is
divisible by `D^max(k-2,0)`. This is stronger than merely observing
rank at most two modulo each prime dividing D.

For the local Smith claim, let `p|D` and suppose every beta difference
is a p-unit. Modulo p, B and B' each have rank s-1: their cyclic
recurrences have one free starting coordinate and all entries used
in propagation are units. Their adjugates have rank one. Their right
kernel lines are distinct because any common nonzero vector would
belong to the kernel of the invertible matrix `B'-B`. The same
argument applies to their left kernel lines.

It follows that W and W' have independent column lines and independent
row lines modulo p. The difference of those rank-one matrices has
rank exactly two, not just rank at most two. Therefore the first two
Smith exponents are zero. If `t=v_p(D)`, the three-minor divisibility
forces the third exponent to be at least t, hence every later one is
at least t. The determinant has valuation exactly `(s-2)t`, so all
the remaining exponents equal t. The s=2 case follows from its unit
determinant at p.

For unit-amplitude defects, all beta differences are signed powers of
2. The same local conclusion applies at every prime dividing D, and
the determinant has no other prime factors away from 2 and 3. The
stated Smith form over `Z[1/6]` follows. Its reduction modulo each
`g|D` leaves precisely two free-variable congruences. The theorem
explicitly preserves the further restrictions on lawful arc
intercepts; no independence of those variables is inferred.

## 3. Infinite actual-cycle family

The family

```text
(1^t 2^(2t))^(r-1) 1^t 2^(3t),   r>=2,t>=1,
```

has the claimed totals and positive D. The unique longest cyclic
run of twos rules out repetition. Rotation by one has exactly 2r
unit mismatches. At the run blocks, the minimum beta exponent sums
to A-r, giving the explicit determinant `2^(A-r)D^(2r-2)`.

The arbitrary-modulus argument also holds: for `M0` coprime to six,
choose t making both 2 and 3 have t-th power one modulo M0. Every
run length is a multiple of t, so each run intercept and the full D
are divisible by M0. Concatenation preserves the intercept divisibility.
The reduced numerators are positive odd integers, and every raw
valuation arrow is exact. Thus these are primitive actual generalized
cycles with unbounded possible cancellation, not formal matrix
solutions alone.

The argument does not compare that cancellation to an exponential
function of m/s. In particular it does not refute the proposed
relative-cancellation inequality. The two-defect case, fixed points,
and repeated words are handled with the stated separate scopes.

## 4. Independent shared-arc source review and replay

The root's `check_shared_arcs.py` was read in full, including its
imported helper functions. The direct weighted intercept calculation,
successive valuation recovery, raw-cycle reconstruction, primitivity
test, and all-rotation minimum-distance checks match their declared
claims. The recovery uses the fixed total to reconstruct the final
valuation; it does not incorrectly try to recover that last valuation
from the intercept alone.

The final checker includes both the older `{2,5}` backgrounds and the
stronger `(3,U,4,U,5,U)` family. For the latter it explicitly checks
`m=9t+3,A=15t+12,D>0,A<2m` at t=3,4,5. The finite tests do not
infer the written polynomial-versus-exponential counting argument.

The independent default replay

```text
python3 experiments/cycle_spectrum/C012/check_shared_arcs.py
```

exited with status 0 and printed PASS. It matched the final saved
receipt exactly and covered:

- 350 original fixed-total backgrounds;
- 3,582 backgrounds with positive total exponent below 2m;
- seven prescribed-prime sets;
- 177,288 exact raw arrows and 173,349 nonidentity rotations.

The full coupled checker was inspected here, including its independent
Bareiss determinant calculation and local prime-power tests. Its full
receipt replay is recorded by the separate theory-review agent; the
shared-arc execution above calls its helpers and is not presented as
a replay of that entire audit.

### Staging mismatch and draft correction

A premature shared-arc replay, before the coupled checker was frozen,
failed its final receipt comparison. Independent field comparison
found that only the pinned dependency hash had changed; all arithmetic
assertions had completed. The root regenerated the shared receipt
after the dependency freeze and extended the declared backgrounds.
The successful final replay above supersedes that staging failure;
the failure is not hidden as a PASS.

A later independent replay of the full coupled checker exposed a JSON
representation defect: an in-memory tuple/list distinction and numeric
mapping keys did not match their serialized forms. The coupled checker
normalized these representations, preserving the mathematical checks.
The root refreshed the shared receipt's dependency pin after that final
repair. This reviewer inspected the normalization and again ran the
default shared-arc replay successfully, with the same counts above.
The pins below identify that final source and receipt, superseding the
earlier successful shared replay's dependency versions.

An earlier chat draft of the prime-escape example had the leading
term `3^(n+1)` instead of `3^n` for `(k,2^n)`. The root caught this
off-by-one. The corrected formula is
`3^n+2^k(4^n-3^n)`, with residue 1, and is tested by the final checker.
The error and its unchanged qualitative conclusion are recorded in
`COUPLED_OBSTRUCTIONS.md`.

## 5. Reviewed source pins

| File | SHA-256 |
| --- | --- |
| `COUPLED_SYSTEM.md` | `c71362d09e2480971fd473f902f47387d2c31a482852d3f6d964d6d9ad9c46c2` |
| `check_coupled_system.py` | `bb0b9c27fc6ef0b116e302a369b33552f54c2a7efa4d94d4b44be8b9ea5e356c` |
| `coupled_system_audit.json` | `033f8f950498c208c7e446e3c46f467d3894adb752c43bba61200b60aee107fc` |
| `check_shared_arcs.py` | `a861866031610455a5179edce78685bddbc72a55993f5c1e86097dd768506a9c` |
| `shared_arc_audit.json` | `7e165c6da40336f5702315a671770325d3f5caf0e2af8494a43080eabb8cf61f` |

The review found no error in the final matrix theorem or shared-arc
checker. No unrestricted cycle exclusion, candidate denominator bound,
or increase in published cycle records is established by this audit.
