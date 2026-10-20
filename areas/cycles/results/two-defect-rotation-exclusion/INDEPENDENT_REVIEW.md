# C011 — Independent source audit and exact replay

**Outcome: PASS for the stated two-defect exclusion, subject to its named
published inputs.** Reviewed on 2026-10-19 by a separate agent from the
authors of `ROTATION_DEFECTS.md`, `EXCLUSION.md`, and the two checkers
below. This is an agent review and fresh execution, not human review,
formal verification, or a novelty assessment. The reviewer contributed
the terminal-valuation refinement during development; this audit is not
an independent discovery claim.

The reviewer authored `DEFECT_OBSTRUCTIONS.md`; that file is deliberately
outside the independent-proof verdict here. Its separate review is in
`ARITHMETIC_REVIEW.md`. No reviewed proof or checker was edited during
this review.

## 1. Mathematical audit

The domain is a positive valuation word, `D=2^A-3^m>0`, and a nonidentity
cyclic rotation differing at exactly two positions. The entries need
not be binary, the shift need not be coprime to the period, and the
defect amplitude is unrestricted.

The following steps were checked directly.

1. Rotation preserves the letter multiset, so the defects exchange
   `a,a+k`, with `a,k>=1`. Repetition would multiply the nonzero mismatch
   count by at least two, while one mismatch is impossible. Thus the
   word is primitive and has `m>=2`.
2. The difference of rotated intercepts factors over the arc between
   the defects. Recutting at the other defect supplies the complementary
   arc. The intercept ignores its terminal valuation, which is essential
   to keeping the original arc totals. Since `g=gcd(C,D)` is coprime to
   six, both factorizations give
   `g | (2^k-1) gcd(C_u,C_v)`.
3. For a positive arc of length `l`, total `S`, and terminal valuation
   `b`, the termwise prefix estimate gives
   `C_arc <= 2^(S-l-b+1)(3^l-2^l) < 2^(S-l-b+1)3^l`.
   This includes one-letter arcs. Applying it to terminal values
   `a+k,a` proves the stronger bound in equation (5), and hence

   ```text
   g^2 < (2^k-1)^2 2^(A-m-k)3^m.
   ```

4. Positivity gives `k<=A-m`. Therefore

   ```text
   g^2 < 2^(2A-2m)3^m,
   q > (1-3^m/2^A)(2/sqrt(3))^m.
   ```

   No amplitude ceiling is introduced in this implication.
5. The rotated intercepts have the same cancellation factor, and their
   reduced numerators are positive odd integers. Their affine equations
   therefore give the exact raw odd-only valuations. At `q=1` a primitive
   word of length at least two realizes a nontrivial integer cycle. It
   cannot contain 1; its exact product identity implies `A<2m`.
6. Applying the explicit product-minus-one logarithm estimate at
   `B=2m` gives

   ```text
   log q > m log(2/sqrt(3)) - 600000000(1+log(2m)).
   ```

   With `M=137500000000`, the rational bounds in the proof give a
   boundary margin of `2450000000` and a derivative lower bound of
   `373/2750>0` on the entire real interval `m>=M`. The published strict
   period bound `m>M` thus contradicts `q=1`.

The exact cut identity retains
`gcd(D,C_rot-C)=g gcd(q,2^P-3^r)`. The argument never replaces the
two-arc divisibility bound by an unjustified gcd equality.

The bounded-denominator finiteness proof in `ROTATION_DEFECTS.md` was
also checked. Its inherited effective logarithm input first bounds
`m`. In the range `2^A>=2*3^m`, equation (9) bounds `S=A-k`.
Putting the high defect letter last then bounds the intercept by a
quantity depending only on `m,S`, so `D=qg` bounds `A`. In the other
range, bounded `m` already bounds `A`. This completes the valuation
bound and avoids incorrectly inferring finitely many words from
bounded length alone.

The adjacent-unit-defect mechanical classification, the noncoprime
shift description, and the marker family's elementary denominator and
minimum estimates were checked for their stated domains. The marker
family's shortcut local-minimum count is kept distinct from the count
of minima in the odd-only clock.

## 2. Published-input audit

- [Matveev's rational version, Theorem 2.1 in Languasco–Luca–Moree–Togbe](https://link.springer.com/article/10.1007/s12188-025-00293-9)
  is a bound for `log|product(gamma_i^b_i)-1|`. With bases 2 and 3,
  coefficients `-A,m`, degree one and `B=2m`, it has exactly the
  coefficient used in `EXCLUSION.md`. Its hypotheses hold. No
  conversion from a logarithmic linear form, and no extra conversion
  constant, is needed. The classical theorem itself is imported.
- [Hercher 2023, Corollary 29 and Remark 30, printed pp.20–21](https://cs.uwaterloo.ca/journals/JIS/VOL26/Hercher/hercher5.pdf)
  give more than `137500000000` odd members after convergence through
  `3*2^69`. His `K` equals our odd-only period; his `m` counts shortcut
  local minima. His proof uses a published computation extending
  Lemma 26; that computation was not rerun here.
- [Barina 2025, Section 6](https://link.springer.com/article/10.1007/s11227-025-07337-0)
  supplies the required convergence interval, reporting verification
  up to `2^71`. Even the exclusive interpretation suffices because
  `3*2^69<2^71`. This computation was not rerun. The separate total-cycle
  length quoted there is not substituted for the odd-member count.
- [Hercher's corrigendum](https://cs.uwaterloo.ca/journals/JIS/VOL26/Hercher/corrigendum.pdf)
  repairs a tail estimate in Theorem 21. It leaves Corollary 29
  unchanged. Section 4 uses the separate Lemma 26 argument; its
  reference to the product reduction used for Theorem 21 does not
  invoke the corrected tail estimate.

## 3. Independent checker inspection and replay

Both checkers were read before execution. The rotation checker uses a
direct weighted intercept sum and checks it against a separate prefix
recurrence. It replays exact raw arrows, actual source scalings,
rotation identities, both arc factorizations, terminal accounting,
strong quadratic bounds, and the amplitude-free consequence. It
preserves the extra factor in the exact rotation gcd. Its default mode
recomputes and compares the whole receipt; it does not rewrite evidence.

Executed from the repository root, without `--write`:

```text
python3 experiments/cycle_spectrum/C011/check_rotation_defects.py
python3 experiments/cycle_spectrum/C011/check_exclusion_constants.py
```

Both processes exited successfully with `status=PASS`, `mode=replay`.
The rotation replay completed in independent process session `34737`.
Its coverage includes:

- All 2,459 stored raw instances, including 1,275 scaled instances;
  1,185 distinct normalized cycles and all 11 fixtures survive.
- 28,831 normalized arrows, 27,646 rotations, and 1,481,154 compared
  word positions.
- 108 actual cycles with two-defect rotations, giving 192 such
  rotations and 384 oriented arc identities. All 192 satisfy the
  stronger and amplitude-free quadratic bounds.
- 51 two-run words, twelve prescribed-modulus controls, nineteen
  repeated-word controls, the extra-factor word `(3,7)`, and eight
  marker-family cases with 1,012 checked rotations.
- Four invalid-input controls are rejected.

In particular the raw d5, d7, and d13 controls are retained. The q359
unit-defect example retains cancellation 73. Repeated `(2)` words
retain denominator one and have no nonzero rotation defect. These
checks are finite evidence, not a proof of the all-period theorem.

The constants replay checks exact rational Taylor bounds,
`K_0<598752000<600000000`, the published endpoint containment, the
positive boundary margin and derivative. Its scope does not include
the external proofs or computations.

## 4. Reviewed source pins

SHA-256 values after the successful replays:

| File | SHA-256 |
| --- | --- |
| `ROTATION_DEFECTS.md` | `9b390b7f8e456bbf52f3563cf7fe4243cf052846a1175dc0d4098a11ba59c801` |
| `EXCLUSION.md` | `0edfdb40ffbb05b43c1e88bd26555ceaf8311135ea31a5ff122761d045f68032` |
| `check_rotation_defects.py` | `ba9a2b7fb269d619378c4c7b25d3cb6430e5a8078ea5658e0d81b71ba2d855ad` |
| `rotation_defect_audit.json` | `1eee49577e35bf5f28aac0ba2a572c8a863266575c4a0e2a4babf2f233d9844d` |
| `check_exclusion_constants.py` | `f63bb7621e6e22d4fee13abea2f356a8871d1b07dcc3ad8ba4ba41642cad1ac7` |
| `exclusion_constants.json` | `bbf7e8616bff39574d05ca075fe26c78a0dc88ac6380f55e73861dc26407225f` |

## 5. Verdict and remaining scope

No mathematical error was found in the reviewed claims. Subject to the
identified published inputs, the written argument excludes denominator
one for every positive word with a two-defect cyclic rotation, without
an amplitude cap. It also supplies effective bounded-denominator
finiteness for that structural class.

This is a constant restriction on possible rotation mismatch counts.
It does not force those counts to grow with period. A primitive word
can have rotations with three or more mismatches, and divisibility of
a coupled signed sum does not imply divisibility of its individual
plateau terms. The proof neither covers all nontrivial cycles nor
addresses divergence. Published lower bounds are used as inputs;
their numerical records and the all-cycle goal are not claimed to
have been improved or completed.
