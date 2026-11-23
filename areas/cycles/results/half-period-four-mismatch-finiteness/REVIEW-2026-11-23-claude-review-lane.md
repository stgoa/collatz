# Review of half-period-four-mismatch-finiteness and ridout-1958-p-adic-roth, 2026-11-23

**Filing note (added by the authoring lane).** This is the reviewer's final text, including its addendum. An
earlier version was committed with pull request 104 before the reviewer had finished. The reviewer's script is
committed in the folder of `half-period-s-unit-approximation-law` as `explore_referee_check.py`, with its
receipt. Where the text says `referee_check.py`, read that file. The reviewer's lane is recorded as
`Claude review lane` in `reviewed_by`.

- **Reviewer.** Claude referee lane (Fable 5.2; fresh-context subagent with an adversarial brief, launched by the
  authoring session, directed by Santiago Armstrong). Independence is at the level of context: I saw only the
  committed files and the two text extracts of the secondary sources. The model is the same as the author's.
- **Version reviewed.** Commit `c397de0`: the finiteness `README.md` (blob `a87a15e62b42`) and
  `sources/ridout-1958-p-adic-roth.md` (blob `389258054a2b`). Both are unchanged since `ba7a51b`.
- **Verdict.** HOLDS WITH CORRECTIONS. No fatal and no mathematical error was found. The theorem is conditional on
  EXT-1 and on Ridout's theorem as cited; its corollary also rests on
  `non-half-period-four-mismatch-exclusion`, which I did not review. One correction concerns the paraphrase of
  Waldschmidt's statement in the source node; the others are wording.

## What I checked

1. **Input.** Inequality (1) is the corollary of `half-period-s-unit-approximation-law`, reviewed separately
   (same date, verdict: holds with wording corrections).
2. **Arithmetic nature of `U`, `V`.** `U` is a cycle state, so it is odd and coprime to 3. `V` is odd: in
   `2^p t - z = 3^a h` the state `z` is odd and `p >= 1`; in `y - 2^q x = 3^b j` the state `y` is odd and
   `q >= 1`. The node's valuation argument gives the same.
3. **Size bounds.** `c <= E < 4N` from the cycle product. `log_2 U <= (alpha-1) N + tau + ell - (p+q)/2 < N`.
   `c > N/3`: in Case I, `2^sum(A) < y < 2^((p+q)/2 + tau) x` gives `len(A) < (alpha-1) N + 2 tau + ell`; in Case II,
   `2^sum(B) < z < 2^((p-q)/2 + tau) t` gives `len(B) < (alpha-1) N + 2 tau + ell - q`. With exact fractions, on
   `2^k <= N < 2^(k+1)`, `k >= 22`: `2 tau + ell < 2^(k-16) + 514 + 342 (k+1) < 2^k/20`; then
   `(117/200 + 1/20) N < N` and `(83/200 - 1/20) N = 73N/200 > N/3`.
4. **Section 2.** `P = 3^N V/g` and `Q = 2^c U/g` are coprime (needs `V` odd, `3` not dividing `U`).
   `Q - P = Theta/g`, `0 < Q - P < Q/2`, `|Q|_2 = 2^(-c)` exactly, `|P|_3 <= 3^(-N)`. Chain (2) is right in every
   step and direction. `Q < 2^(5N)`, so `Q^(1/250) < 2^(N/50)` and (3) holds because `N > 50`. `epsilon = 1/250`
   does not depend on the cycle.
5. **The form of Ridout's inequality.** Checked against three statements in the extracts.
   - Waldschmidt, Théorème 2, with `alpha = beta = 1`, `(alpha_1, beta_1) = (1, 0)` at 2 and
     `(alpha_2, beta_2) = (0, 1)` at 3: the left side is `q |q - p| |q|_2 |p|_3`. This is (3) with `p = P`, `q = Q`.
   - Bilu, with `S = {infinity, 2, 3}` and targets `1, infinity, 0`: the factors are `(Q-P)/Q`, `|Q/P|_2 = 2^(-c)`
     (as `P` is odd) and `|P/Q|_3 = |P|_3` (as `3` does not divide `Q`); each is at most 1; `H = Q`. The product
     times `H^2` equals the left side of (3), so the two inequalities are the same.
   - Waldschmidt, Théorème 3 (the p-adic Subspace Theorem) for `m = 2`, with forms `x_1, x_1 - x_2` at infinity,
     `x_1, x_2` at 2 and `x_2, x_1` at 3, evaluated at `(Q, P)`: the same left side, and "finitely many proper
     subspaces of `Q^2`" means finitely many ratios `P/Q`. This is consistent with the two forms above.
6. **Section 3.** `P/Q` is in lowest terms with `v_2(Q) = c`, so it determines `c`. Finitely many `c`, then
   `N < 3c`, then finitely many words (length `2N`, total below `4N`), and a word has at most one cycle. A word
   with four half-period mismatches is primitive, so the period `2N` is determined by the cycle.
7. **Corollary and remarks.** The corollary follows from the claim of `non-half-period-four-mismatch-exclusion`
   as stated there. The abc remark is right (`rad <= 6 U V Theta / g^3`). The reading `rho >= 5` for all but
   finitely many cycles follows from the cited nodes as stated.
8. **Source node.** Bilu's and Waldschmidt's statements are quoted faithfully from the extracts (Bilu, section 1;
   Waldschmidt, Théorème 2). The two phrases in quotation marks appear in Bilu's text. The extract of Bilu
   carries the stamp `arXiv:0907.2098v1`, and its reference [50] is the 1958 paper. Crossref metadata confirm
   both citations: Mathematika 5 (1958), 40-48, DOI `10.1112/S0025579300001339`, and Mathematika 4 (1957),
   125-131.
9. **Claim discipline.** Map, clock and class of cycles are stated. Both inputs are under `assumes`. No sentence
   claims an exclusion or an effective bound; "No cycle length is excluded" is said explicitly.

## How

`referee_check.py` (kept outside the repository, with its receipt `referee_check.json`; standard library). Each
check implements a statement of the two READMEs. It does not import or copy the author's certificate, which I
had read first as part of the review.

- On the **124474** instances (119777 distinct cycles) of actual `3x+d` cycles of shape `A B A[p] B[q]` that fall
  in Case I or II, out of 267116 instances (256364 distinct cycles) tested: `gcd(P, Q) = 1`, `gcd(U, 6) = 1`, `V` odd, `v_2(Q) = c`, `v_3(P) >= N`, `Q - P = Theta/g > 0`,
  `c <= E`, and `Q |Q-P| |Q|_2 |P|_3 <= U Theta/(g^2 3^N)`, all in exact integers. `h` and `j` are odd on all
  267116 instances. 0 violations.
- The size inequalities of section 1 in their d-agnostic form (actual `tau`, `ell` of the cycle):
  `sum(A) < log_2 x + (p+q)/2 + tau < (alpha-1) N + 2 tau + ell` on 8772 Case I instances and
  `sum(B) < log_2 t + (p-q)/2 + tau` on 115702 Case II instances. 0 violations.
- **214** synthetic solutions of (1) with `N = 75, 100, ..., 400` (so `N/25` is an integer), `N/3 < c < 4N`,
  `U < 2^N` coprime to 6 and `V` odd, taken from convergents of `2^c/3^N`: coprimality, `Q/2 < P < Q`, chain (2),
  `Q < 2^(5N)`, inequality (3) with `epsilon = 1/250` as `(left side)^250 Q < 1`, and the identity between
  Bilu's product and Waldschmidt's left side, all in exact rationals. 0 violations.
- The constants of item 3 with exact fractions on every dyadic block `k = 22..600`, plus the monotone step.

**Controls.** I found 192 half-period four-mismatch cycles by iterating `3x+d` (`d <= 999` coprime to 6, odd
seeds up to 3000), and replayed the `3x+47` cycle `(73, 133, 223, 179)` and the `3x+1631` cycle through `9145`.
Of the 192, 104 are in Cases B and C, which the approximation law rules out only for `d = 1` and `N >= 2^22`.
The other 88 and the two named controls are in Cases I and II: they satisfy the algebra of section 2 but not
inequality (1), since `Theta V < 2^(c - N/25)` fails on every tested cycle. So Ridout's inequality is never
reached for them, and the argument makes no statement about `3x+d`.

## Corrections

1. **Source node, lines 46-47.** "For `1 <= i <= s` let `p_i` be a prime and `alpha_i, beta_i` rational numbers,
   not both zero." In Waldschmidt's text the `p_i` are the elements of a finite set `S = {p_1, ..., p_s}`, hence
   distinct. Without that the statement is false: take `s = 2`, `p_1 = p_2 = 2`, `alpha = beta = 1`,
   `(alpha_i, beta_i) = (1, 0)` twice and `p/q = (2^k - 1)/2^k`; the left side is `2^(-k)`, below
   `max(p, q)^(-epsilon)` for every `epsilon < 1`. Corrected text: "Let `S = {p_1, ..., p_s}` be a finite set of
   primes, so the `p_i` are distinct. For `1 <= i <= s` let `alpha_i, beta_i` be rational numbers, not both zero."
   The application uses the distinct primes 2 and 3 and is not affected.
2. **Finiteness, line 60 and lines 70-71.** "Two size bounds are needed" introduces three (`c < 4N`, `U < 2^N`,
   `c > N/3`). "which give `2 tau + ell < N/20` for `N >= 2^22`" is true but not shown, and no certificate prints
   it. Add the computation: "for `2^k <= N < 2^(k+1)`, `k >= 22`: `2 tau + ell < 2^(k-16) + 514 + 342 (k+1) < 2^k/20`;
   hence `log_2 U < (117/200 + 1/20) N < N` and `(2 - alpha) N - 2 tau - ell > 73N/200 > N/3`."
3. **Finiteness, line 116-117.** "agree to within a factor `1 + 2^(-N/25)/(U V)`". The exact statement is
   `0 < 1 - 3^N V/(2^c U) < 2^(-N/25)/(U V)`.
4. **Finiteness, line 131.** "It is now a finite, non-explicit set of possible exceptions." Prefix with "Under
   EXT-1 and Ridout's theorem".
5. **Optional, lines 12 and 39-40.** "Ridout's theorem bounds neither N nor the number of exceptional cycles" is
   true of the qualitative statement cited. I did not check whether a quantitative version would bound the number
   of large solutions; "Ridout's theorem in the form cited" is the safe wording.

## What I could not check

- **Ridout's theorem itself.** I did not read the 1957 and 1958 papers and cannot vouch for the theorem beyond the
  two secondary statements, which agree with each other in the case used and with the `m = 2` case of the p-adic
  Subspace Theorem as stated in the same lecture notes.
- **EXT-1.** Taken from `musson-collatz-gap-all`.
- **`non-half-period-four-mismatch-exclusion`.** Status `written`; not reviewed here. Only the corollary uses it.
- **The regime `N >= 2^22`.** No actual cycle reaches it, so the theorem cannot be tested numerically. The
  finiteness rests on the written argument, which I verified by hand.
- **Novelty.** Not assessed.

## Addendum, 2026-11-23: the corrected text at commit `7289b04`

The authoring lane applied the corrections while this review was being finished. I checked the result.

- Corrections 1 to 5 are applied as proposed: the distinct primes in Waldschmidt's form, "Three size bounds",
  the displayed computation of `2 tau + ell < N/20`, the exact form of inequality (1) in the remark, the
  conditional wording of "Status of the question", and "in the form cited".
- The new sentence "the certificate of the approximation law checks this" is backed: V1 of
  `check_s_unit_law.py` now checks `20 (2^(k-16) + 514 + 342 (k+1)) < 2^k` at `k = 22` with a monotone step. I
  re-ran it; it passes and matches its receipt.
- MAP.md shows this node as `reviewed` with chain strength `written`, because the corollary depends on
  `non-half-period-four-mismatch-exclusion`. That is the right reading: the theorem was checked here, the
  dependency of the corollary was not.
- Whether a fresh-context subagent launched by the authoring session, on the same model, is "independent of the
  authoring session" in the sense required for `reviewed` is for the maintainers to decide. The `scope` field
  discloses it.
