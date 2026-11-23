# Review of half-period-s-unit-approximation-law, 2026-11-23

**Filing note (added by the authoring lane when the review was committed).** The three corrections below were
applied in the same pull request, and the suggested exact checks were added to the certificate as V5 and to V3.
The reviewer's script is committed in this folder as `explore_referee_check.py`, with its receipt
`explore_referee_check.json`. Where the text says `referee_check.py`, read that file. The reviewer's lane is
recorded as `Claude review lane` in `reviewed_by`.

- **Reviewer.** Claude referee lane (Fable 5.2; fresh-context subagent with an adversarial brief, launched by the
  authoring session, directed by Santiago Armstrong). Independence is at the level of context: I saw only the
  committed files, not the author's working notes. The model is the same as the author's.
- **Version reviewed.** Commit `c397de0`: `README.md` (blob `544d5e683142`), `check_s_unit_law.py`
  (blob `88eac5cb4cea`), `check_s_unit_law.json` (blob `a69d1892882d`). The mathematical text is the one of
  commit `ba7a51b`; `c397de0` only adds the `lean:` list and the `## Lean` section.
- **Verdict.** HOLDS WITH CORRECTIONS. No fatal and no mathematical error was found. The three corrections below
  are wording only; the theorem, its constants and the proof are unchanged.

## What I checked

I re-derived every step by hand, then tested it with a script written from the README alone.

1. **Section 1 (normal form).** The position and sign rules for a rotation by `k <= N`, the two rotation choices
   and the half exchange. Also that a word with exactly four half-period mismatches is primitive: for `W = w^k`,
   an even `k` gives zero mismatches and an odd `k >= 3` gives a multiple of `k`. So the states are distinct and
   the minimum is unique.
2. **Section 2.** Equations (1), (2), the integrality of `h`, `j`, `h > 0`, `j != 0`, identity (3) and
   `j < 0 => p < q`. Also `p = q => j > 0`, which (3) gives directly.
3. **Section 3.** Identities (4), (5) and the bounds (6).
4. **Section 4.** (7), the three slopes (8), the budget (9), `M >= 2^17`, the use of EXT-1 on the pair `(2N, E)`
   in (10) (`3^(2N) < 2^E` holds because `tau > 0`), and the step bound.
5. **Section 5.** The paired differences, the four cases, the two inequalities of Case B and of Case C, and (11).
   (11) follows from the exact identity
   `RHS - N = [ell + (kappa-1) b - a] + kappa [ell + (q-p)/2 + tau - b] + kappa [(alpha-1) N + tau - (p+q)/2] + kappa p`
   in Case B, and the same without the last term, with `a, b` exchanged and `(p+q)/2` in the second bracket, in
   Case C. Every bracket is nonnegative and the first two are positive.
6. **Sections 6 and 7.** (12) and (13) follow from exact identities with three slacks each:
   `(sA - 2X - p) - RHS(12) = [sA - (a + X - ell)] + [(X+q)/alpha - b] + (1 + 1/alpha) [(alpha-1) N + tau + ell - (p+q)/2 - X]`,
   `(sB - 2T) - RHS(13) = [sB - (b + T - ell)] + [(T+p)/alpha - a] + (1 + 1/alpha) [(alpha-1) N + tau + ell - (p+q)/2 - T]`.
   The first and third brackets are nonnegative, the second is positive. The exponent bookkeeping
   `c + 2 tau - (sA - 2X - p)` and `c' + 2 tau - (sB - 2T)` is right.
7. **Thresholds, with exact fractions.** `2911/63400 = 1 - 317/200 + 200/317`. On `2^k <= N < 2^(k+1)` the main
   margin `(2911/63400 - 1/25 - (3 + 10000/15849)/2^18) 2^k - (2 + 10000/15849)(514 + 342 (k+1))` is `2703.09` at
   `k = 22` and grows; it is negative at `k = 21`, so `2^22` is the least dyadic threshold for these constants.
   The exclusion margin of (11) is `283527.45` at `k = 22` and is already positive from `k = 18`.
8. **Section 8 and the remarks.** The isolation step, the Legendre remark (the bound `2^(N/25) - 3` follows from
   the complete quotient `3^N g^2/(Theta U) - Q_(k-1)/Q_k`; the extra convergent of the non-canonical expansion
   of a rational never satisfies Legendre's strict inequality), and the two consequences
   `p + q > sum(A) + N/25` (Case I) and `p - q > N/25 + log_2 z - 2 tau` (Case II).
9. **Certificate.** `check_s_unit_law.py` passes, also under `python3 -O`, and reproduces the receipt
   (Python 3.12, about 4 s). `tools/check.py` reports 410 nodes, 0 errors at `c397de0`.
10. **`## Lean`.** I read the ten Lean statements and compared them with the table. With (1) as hypothesis they
    match (2), `h > 0`, (3), `j < 0 => p < q`, (4), (5), (6) and section 8 in integer form. I did not rebuild
    `lean/`.

## How

`referee_check.py` (kept outside the repository, with its receipt `referee_check.json`) uses the standard library
only. It does not import or copy the author's certificate. Integer checks are exact. Real inequalities use
floats, with an 80-digit `decimal` re-evaluation whenever a margin is below `1e-6`.

| Part | Content | Count |
|---|---|---|
| P0 | constants, both thresholds on every dyadic block `k = 22..600` and the monotone step, descent below `2^17` | 65535 odd `n`, at most 85 odd steps |
| P1 | section 1 recipe on constructed words, `N = 2..5` | 48096 words |
| P1 | every word over `{1,2,3}`, `N = 2..4`, with four half-period mismatches normalises | 2304 words |
| P1 | proper powers never have four half-period mismatches | 540 words |
| P2 | actual `3x+d` cycles built from words `A B A[p] B[q]`, `d = D/gcd(C_W, D)` | 266922 instances |
| P3 | half-period four-mismatch cycles found by iterating `3x+d`, `d <= 999` coprime to 6, odd seeds `<= 3000` | 192 cycles |
| P3 | the `3x+47` cycle `(73, 133, 223, 179)` and the `3x+1631` cycle through `9145`, by iteration | 2 cycles |
| P4 | isolation step on competing fractions; Legendre form | 25791670 fractions; 3645 cases |
| P6 | the exact slack identities of (11), (12), (13) on random rationals, any `alpha` in `(1, 2)` | 20000 samples |

Families in P2: exhaustive blocks of length at most 3 over letters 1 to 3 with `p, q <= 8` (97113 cycles);
exhaustive blocks of length at most 2 over letters 1 to 5 with `p, q <= 10` (89983); random blocks of length up to
12 (36588); long words with `N` up to 400 (520) and up to 2221 (18); adversarial shapes such as `p = q`, `A = B`,
all-ones blocks and blocks of length 1 (2732); blocks with a large interior letter, to move the minimum off the
block boundary (39968). 3854 words with `2^E <= 3^(2N)` were skipped.

On all **267116 cycle instances** (256364 distinct cycles; the families overlap): 132 distinct checks, 38910343
evaluations, **0 violations**. Checked per cycle: (1),
(2), (3), (4), (5), (6), the four slopes, `h > 0`, `j != 0`, `h` and `j` odd, `j < 0 => p < q`, the paired
differences of section 5 with their exact formula, the placement of the minimum among the smaller copies, each
elementary inequality of Cases I, II, B, C, the step `eta < 2N d/(3M)` of (10), the step bound, and, in the
d-agnostic form with the actual `tau`, `ell`, `kappa` of the cycle: (11), each line of (12) and (13), and the
final inequality `Theta V < 2^(c - G)`.

Cases met, as instances: I 8772, II 115702, B 876, C 141766 (distinct cycles: 8083, 111694, 863, 135724).
Interior minima: I 366, II 18980, B 704, C 20911. `p = q`: 40603 instances, all with `j > 0`. `p > q` with
`j < 0`: none. Smallest margins: (12) 3.42, (13) 5.09, (11) 14.0.
Lines 1 and 3 of (12) and (13) reach equality on all-ones words, as the identities predict.

**Controls.** The identities and every elementary inequality hold on the controls with `d C` in place of `C`.
The conclusions of the theorem do not: Cases B and C occur on 142642 instances, and `Theta V < 2^(c - N/25)`
fails on all 124474 instances in Cases I and II. This is as it should be. The controls have `d > 1` and `N <= 2221`, and the two `d = 1` inputs
(`M >= 2^17` and (10)) are not available for them. No control is excluded by the argument.

## Corrections

1. **Statement, line 83-84.** "Both identities hold for every such cycle, of any length; only the gap needs EXT-1
   and `N >= 2^22`." The column "Minimum" also needs both: section 5 uses (10) and the threshold, and the
   placement fails on more than half of the `3x+d` test cycles. Corrected text: "Both identities, `h > 0`, `j != 0` and
   `j < 0 => p < q` hold for every such cycle, of any length and without EXT-1. The placement of the minimum and
   the gap are proved here under EXT-1 for `N >= 2^22`."
2. **Remarks, Controls, line 391.** "The gap needs (10), which bounds the minimum of a `3x+1` cycle by a power of
   its length." It also needs `M >= 2^17`, for `tau < N/2^18` and `kappa < 317/200`. Corrected text: "The
   placement and the gap need two facts special to `d = 1`: the minimum is at least `2^17` (V2), and (10)."
3. **Certificates, V4, line 340.** "on 11513 exact convergents" should read "on 11513 multiples `(gQ, gP)`,
   `g` in `{1, 5, 7}`, of exact convergents" (receipt key `convergent_multiples`).

Suggestion, not required: add identity (3) and the three slack identities of item 5 and 6 above to the
certificate. They turn (11), (12), (13) into exact checks.

## What I could not check

- **EXT-1.** Taken from `musson-collatz-gap-all` as stated. I checked only that it is applied with `k = 2N`,
  `L = E` and `3^(2N) < 2^E`.
- **The regime of the theorem.** No actual cycle reaches it. On every tested cycle the exponent `G` of the
  d-agnostic gap is not positive and (11) holds: the minimum is never small enough compared with `N`. A mutation
  test confirms the limit: wrong variants of the `ell` and `tau` coefficients are detected, but
  `c0 + 0.02` in (12) or a dropped `kappa` in (11) are not. So the numerical evidence supports the identities and
  each elementary step. The conclusion for `N >= 2^22` rests on the written argument, which I verified by hand
  and through the exact identities above.
- **Lean.** Not rebuilt. The receipts report the three standard axioms.
- **Novelty.** Not assessed.
