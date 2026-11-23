# Review of mismatch-chain-ridout-criterion, 2026-11-23

**Filing note (added by the authoring lane).** This is the reviewer's final text, filed after its final report.
It reviews the node as first submitted in the pull request. All its corrections were then applied before
merging: the hypothesis of pattern (ii) is strict, pattern (i) uses the sharper factor of the reviewer's last
paragraph, the redundant conditions of (2) are removed and explained, and the certificate, the remarks and the
question were reworded. The reviewer's main script is committed in this folder as
`explore_referee_chain_test.py`; where the text says `referee_chain_test.py`, read that file. Its two smaller
scripts are not committed.

**Reviewer.** A subagent launched and briefed by the authoring session, on the same model (Fable 5.2), with a
fresh context and an adversarial brief. It is not independent of the authoring session in the sense of the
contribution rules, so this review does not justify a status above `written`.

**Verdict.** Holds, with corrections. No fatal finding. Parts (a), (b) and (d) are correct as stated. Part (c)
is correct for pattern (i); for pattern (ii) the hypothesis must be strict (correction 1). The other corrections
are wording.

## What was read

- The node: `README.md` in full. Its certificate `check_chain_criterion.py`, both receipts and
  `explore_lp_half_period.py` were read only after the reviewer's main script had been written and run.
- `half-period-s-unit-approximation-law` (frontmatter, Statement, sections 1 to 4, and the lines of sections
  5 to 8 that carry the constants), `half-period-four-mismatch-finiteness` (in full) and the source node
  `ridout-1958-p-adic-roth` (in full).
- The question `rotation-distance-finite-exceptions` (in full), and for it the frontmatter claims of
  `three-mismatch-exclusion`, `two-mismatch-exclusion-via-gap`, `non-half-period-four-mismatch-exclusion`,
  `largest-letter-rho-reduction`, `rotation-distance-growth`, `rotation-distance-at-least-5`, and the rows on
  `rho(w)` and the controls in `conventions/NOTATION.md`. Their proofs were not reviewed.

## What was re-derived by hand

- Equation (3), the run of `a - 1` matched positions, `2^V (2^(w'_(i_0)) xi' - 2^(w_(i_0)) xi) = 3^a u`, hence
  the integer `G`; the two track equations and identity (1). The exponents and positions are right, also for
  `a = 1` and `n = 0`. With addend `d` the same steps give (1) with `d C`, `d C'`.
- `g = G/2^e` is odd, and `2^c U - 3^(a+n) g = Theta`.
- Part (b): `g <= -1` contradicts (2); `gcd(P, Q) = 1`; `|Q|_2 = 2^(-c)`; `|P|_3 <= 3^(-(a+n))`; the inequality
  chain; its match with the form recorded in the source node (`alpha = beta = 1`, the form `q` at 2, the form
  `p` at 3). From one rational `P/Q`: `c = v_2(Q)`, `a + n <= v_3(P)`, `U < 3^(a+n)`, one cycle per value of
  `U`, finitely many configurations per cycle (`a <= m` because a rotation by `H` has a mismatch in every
  window of `m` positions).
- Comparison (4): only the prefix totals over `i_0 + 1, ..., i_r - 1` enter the intercepts, so the letter at
  `i_r` is free. Both estimates of section 3.
- The dictionary of section 4, position by position, against identities (4) and (5) of the approximation law.
  Both cases are right. In Case II the criterion's `a` is `b = len(B)` and `n = len(A)`. The word
  `A B A[p] B[q]` is primitive (for a proper power `V^k` the rotation by `N` has no mismatch when `k` is even
  and a number of mismatches divisible by `k` when `k` is odd), so `m = 2N` there.

Hidden assumptions looked for, none harmful:

- `H` not a multiple of the primitive period is not needed for (a) and is implied by the mismatch in (b).
- `n < m` is not needed: (1) holds for every `n >= 0`, and the proof of (b) bounds `n` by `v_3(P)`.
- `Theta > 0` holds in every configuration, because `Theta = 2^(w_(i_0) - e) 3^n xi + 2^(w'_(i_0) - e) C'`.
- `c = 0` happens exactly when `w'_(i_0) < w_(i_0)` and `n = 0`, and then the third condition of (2) fails. So
  the first two conditions of (2) are redundant.

## What was run

All in exact integer or exact rational arithmetic, standard library only. The scripts are the reviewer's own
and import nothing from the certificate. They are kept outside the repository.

- `referee_chain_test.py`, written from the README alone. 2438 actual `3x+d` cycles with distinct states built
  from words (938 rotation classes of words of length 2 to 6 over letters 1 to 4, with ends up to `n = 2m - 1`;
  1500 seeded random words of length 7 to 12 with letters up to 9), every shift, start, admissible run length
  and end: 1965646 configurations for the divisibility by `3^a` and identity (1) with `d C`; 1544410 with a
  mismatched start for the oddness of `g`, the reduced identity and the closed form of `Theta`; 772205 with
  `g >= 1` for the arithmetic of part (b); 490635 for (4) and for `2^sigma zeta = 3^n xi Pi` with
  `Pi = product of 1 + d/(3x)`; 226034 for pattern (i) and 189910 for pattern (ii). Dictionary of section 4
  recomputed from the general definitions on 1500 cycles with word `A B A[p] B[q]`. No failure, also under
  `python3 -O`.
- `referee_controls_test.py`: the same checks on 193 cycles found by iteration for `d <= 151` (619066
  configurations) and on the 41-state cycle of `3x+61` (111192 configurations). On the cycles of `3x+5`,
  `3x+7`, `3x+13` and `3x+61` the least value of `U Theta / 3^(a+n)` is 18.33, so (2) is never met there.
- `referee_scan_small_product.py`: 1579 cycles for `d <= 999`. Exactly one has `U Theta < 3^(a+n)`: the
  29-state cycle of `3x+193` through 1, with `H = 26`, `i_0 = 2`, `a = 2`, `n = 0`, `xi = 7`, `U = 1`, `c = 4`,
  `g = 1` (`2^4 - 3^2 = 7`). It satisfies (2) for every `epsilon < 0.0906`. This is consistent with the node:
  part (b) is a finiteness statement for `d = 1` and excludes nothing.
- The author's certificate, with and without `-O`: passes and matches its receipt. `tools/check.py`: 412 nodes,
  0 errors. The exploration script reproduces its receipt (0 of 4, 0 of 32, 54 of 192), and the README
  describes it accurately as an exploration that supports no claim.

## Corrections

1. **Pattern (ii) needs a strict hypothesis.** Section 3 proves `Theta <= 3^n xi (2^delta + 2^(D') (Pi - 1))`,
   and this is an equality whenever `D' = 0` (95344 of the 189910 tested configurations, among them Case II of
   the half-period law). With `<=` in the hypothesis one gets only `U Theta <= 3^(a+n)/(2^c U)^epsilon`, while
   (2) is strict. Equality is impossible for rational `epsilon = s/t` (it would read
   `(2^c U)^s (U Theta)^t = 3^((a+n) t)`, with an even left side) but is not excluded for irrational `epsilon`.
   The finiteness itself is not at risk, since the non-strict inequality for `epsilon` implies the strict one
   for `epsilon/2`. Replace `<=` by `<` in row (ii) of the table and in the claim:
   `(2^(w_(i_0) - w'_(i_0)) + 2^(D') (Pi - 1)) * U * xi < 3^a / (2^c U)^epsilon`.
   Pattern (i) is fine: its bound on `Theta` is strict.
2. **Certificates section.** The loop over ends is `range(0, m - a + 1)`, so V1 covers the ends with
   `a + n <= m`, not every end, when `a > 1`. Suggested text: "every admissible run length `a - 1` and every
   end `i_r` with `a + n <= m`". V2 checks the two identities of the approximation law and the two quotients
   `2^p t - z = 3^a h`, `y - 2^q x = 3^b j`; it does not recompute `xi, xi', zeta, U, sigma, sigma', c, g,
   Theta` from the stated positions. Suggested text: "V2. The two identities of section 4 and the quotients
   `g = h`, `g = j`, on actual `3x+d` cycles with word `A B A[p] B[q]`", or call the code of V1 at
   `(H, i_0, n) = (N, a - 1, b)` and `(N, 2N - 1, a)`. The reviewer's script does the latter.
3. **Remark "Reading".** The last sentence follows from (b), not from form (i), which loses `2^(c+1)`.
   Suggested text: "With `n = 0` and `w'_(i_0) > w_(i_0)`, `Theta = xi`, and (b) says: apart from finitely many
   configurations, the two states right after a mismatch that follows a common run of `a - 1` positions have
   product at least `3^a / (2^c U)^epsilon`, with `U` the state on the track of the larger letter."
4. **Remark on the amplitudes.** The exact statement, checked on 151343 configurations with `n >= 1`, is
   `2^(delta + D' + 1) Pi U xi = 2 xi zeta 2^(rho_(i_0) - delta_last) * Pi' / (1 + 1/(3 x_(i_0)))`, with `Pi'` the
   product of `1 + 1/(3 x'_l)` over `l = i_0, ..., i_r`. So write "up to factors of the same kind as `Pi`",
   "`rho_before = rho_(i_0)`" and "for `n >= 1`".
5. **"Finitely many chains"** (Remarks, and the question). True for any rotation and not what is meant.
   Suggested text: "a rotation has at most `s^2` chains that start at a mismatch, take its whole common run and
   end at a mismatch".
6. **Scope.** "proved so far only in the half-period case": add "(under EXT-1, for `N >= 2^22`)".
7. **Question `rotation-distance-finite-exceptions`.**
   - "finitely many for s = 4 (EXT-1 and Ridout's theorem)": the cited nodes give this for exactly four
     mismatches. For at most four, either name the inputs of the line `s <= 3` as well, or add an argument that
     the cycles those results leave uncovered without the period and minimum imports are finite in number.
   - "any start position ... an exact identity relates `3^(a+n) g` to `2^c U`": `g` and `c` exist only at a
     mismatched start. "With finitely many exceptions": add "under Ridout's theorem, for each fixed
     `epsilon > 0`". The sentence omits the conditions `c >= 1`, `Theta > 0` of (2); that is correct only
     because they are redundant, which the node should say (see the list of hidden assumptions above).
   - "Actual cycles of 3x+d have small rho, so any proof must use d = 1": too strong for a finiteness
     statement, which finitely many actual cycles of one fixed `3x+d` do not contradict. Suggested text:
     "Across the family `3x+d` infinitely many actual cycles have small `rho`, so no proof can be uniform in
     `d`; the half-period case uses `d = 1` through the size of the minimum."
   - Every other factual sentence is supported by the claims of the nodes it cites, including the constant
     `1 - log_2 3 + 1/log_2 3` (approximation law, (12) and (13)), the height `O(log m)` of the minimum under
     EXT-1 (its (10)), the two sign classes for three changed positions, and the parity of the number of
     mismatches of a half-period rotation.

Optional: pattern (i) can be sharpened in the same way as (ii). Since `Theta = 3^n xi + 2^delta C'`,
`Theta <= 3^n xi (1 + 2^(delta + D') (Pi - 1))`, so `(1 + 2^(delta + D') (Pi - 1)) U xi < 3^a/(2^c U)^epsilon`
suffices (checked on the 226034 configurations of pattern (i)).

## Not checked

- Ridout's papers and the two secondary sources. Only the match between the inequality of section 2 and the
  form recorded in the source node was checked.
- EXT-1, the Lean build, and the proofs of every node other than the one under review.
- Whether the linear programme of the exploration is a valid relaxation. Only its counts were reproduced.
- Novelty.
