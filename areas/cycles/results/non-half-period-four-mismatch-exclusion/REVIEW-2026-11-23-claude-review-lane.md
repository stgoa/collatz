# Review of non-half-period-four-mismatch-exclusion, 2026-11-23

- **Reviewer.** Claude review lane (Fable 5.2; independent subagent; directed by Santiago Armstrong).
  I did not write this node and took no part in its authoring session (Codex lanes, GPT-6). I saw only the
  committed files. I read the certificate before writing my own scripts, since it is part of what is
  reviewed; my scripts are independent in code and in test data, not in ignorance of the node's code.
- **Version reviewed.** Working tree at commit `b549f61`; the node was last changed in `c2fd98a`. Blobs:
  `README.md` `20bb6dfa751b`, `check_non_half_period.py` `65ac1333fea8`, `check_non_half_period.json`
  `d1f2211cc8ff`. Its dependency `free-four-cut-eighteen-rotation-obstruction` was reviewed at the same commit
  (separate review, verdict HOLDS); the source `musson-collatz-gap-all` (EXT-1) was read, not re-checked.
- **Scope.** The whole node: frontmatter claim, Statement, Proof sections 1 to 8, the certificate and its
  receipt, the controls. The raw odd-only `3x+1` clock throughout; `m` is the full number of odd states.
- **Verdict.** HOLDS WITH CORRECTIONS. I found no mathematical error, no gap in the case split and no gap in
  the range of periods. The two corrections below are wording only; the theorem, its constants and the proof
  are unchanged. The result is conditional on EXT-1, which is used only for `m >= 2^22`.

## What I checked

1. **Statement and scope.** Map, clock, class of cycles (nontrivial, primitive, positive, integer), the shift
   `H`, the order `M = m/gcd(H, m)` and the conclusion `M = 2` are stated without ambiguity, and the
   frontmatter claim equals the Statement and what the proof proves. Primitivity gives `m` distinct states,
   so a shift `jH` not congruent to 0 modulo `m` pairs distinct states; this is the only use of it. No
   exclusion of the half-period case, of all cycles or of the conjecture is claimed.
2. **Section 1, the track partition.** The orbits of `i -> i + H` are the `g = gcd(H, m)` residue classes
   modulo `g`, each a cyclic sequence of `M` letters; a mismatch at `i` is a change between consecutive
   letters of the track of `i`; a cyclic sequence has 0 or at least 2 changes. So four mismatches are `4` on
   one track or `2 + 2` on two tracks, and `3 + 1`, `2 + 1 + 1`, `1 + 1 + 1 + 1` are impossible. Position `i`
   of track `r` is `(k + r/g)/M` with level `k = (i - r)/g`, and a shift by `H = a g` moves the level by `a`
   modulo `M` and keeps the phase. Replacing `H` by `m - H` translates the mismatch set by `H` and keeps the
   count and the order, so `0 < a < M/2` is no restriction. `gcd(H, m) > 1` is exactly the case of several
   tracks and needs nothing more.
3. **Sections 2 and 3, the finite lemma (6).** Rows (8) and (9) re-derived: for a cut `(k + z)/M` with
   predecessor `(k' + z')/M` and partner level `k'' = (k + j a) mod M`,
   `M D = k - k' + M I + z - z' - R (max(k, k'') + z)`. The order of the cuts is by level, then by track, for
   all `0 < x < y < 1`. Coincidences happen only inside a track and are removed in (7); cuts of different
   tracks never coincide. The enumeration `binom(M,4) + binom(M,2)^2` per shift contains every pattern of
   section 1. A strict solution would give positive area, so zero area of the closed polygon suffices. The
   clipping in the script is the standard exact Sutherland-Hodgman step with fractions.
4. **Section 4, phase zero.** A common small left translation keeps every gap, moves a point at 0 to just
   below 1 where `f` tends to `1 = f(0)`, and changes all other heights continuously; the zero-phase track
   becomes a track of phase just below 1 with levels lowered by one, which is again in the enumeration. I also
   tested the phase-zero configurations directly from the definition (table below).
5. **Section 5.** For `M > 18` the reduced denominator of `h = a/M` exceeds 18, `0 < h < 1/2`, the four cuts
   are distinct, and every `jH`, `j <= 18`, is a nonidentity shift: the hypotheses of (4*) of the dependency.
   For `3 <= M <= 18`, lemma (6) with `j <= M - 1`. In both cases `D_j(e) < epsilon` for all `j, e` gives
   `epsilon > 1/750`.
6. **Section 6, the transfer.** Re-derived line by line.
   - With `n_0 = L`: `log_2 n_i = ell + i alpha - sum_(k<i) w_k + sum_(k<i) log_2(1 + 1/(3 n_k))
     <= ell + (alpha - 1) i + delta`, because `w_k >= 1` and the partial sums of positive terms are at most
     `delta`. At `i = 0` the value `f(0) = 1` only weakens a bound that would hold with 0.
   - `w_i != w_(i+jH)` forces `w_(i+tH) != w_(i+(t+1)H)` for some `0 <= t < j`, so the mismatches of `jH` lie
     in `C_j = union(C - t h)`, the set of the geometric statement.
   - Between consecutive distinct cuts `b' < b` of `C_j` the arrows `b'+1, ..., b-1` agree; there are
     `r = mG - 1` of them; subtracting paired step equations gives `2^F d_b = 3^r d_(b'+1)` with
     `d_i = n_i - n_(i+jH)`; both differences are even and nonzero, so `3^r` divides `d_b/2` and
     `max(n_b, n_(b+jH)) > |d_b| >= 2 * 3^(mG-1)`. The witness sits at the end `e = b/m` of the gap and at its
     partner `e + j h`, which is the pairing of the geometric statement.
   - Logarithms: `1 + (mG - 1) alpha < ell + delta + (alpha - 1) m max(f(e), f(e + j h))`, hence
     `G < ((alpha-1)/alpha) max(f(e), f(e + j h)) + (ell + delta + alpha - 1)/(alpha m)`. Direction, coefficient
     and the dependence on `m` are right. `(alpha-1)/alpha = 0.36907... < 37/100` follows from
     `3^63 < 2^100`, and `alpha > 19/12` from `3^12 > 2^19`.
7. **Sections 7 and 8, the periods.** `delta/(alpha m) < 1/(3 L ln 3) < 1/393216` uses `L >= 2^17`; (17)
   follows with `1/alpha < 12/19`. (18) and EXT-1 applied to the pair `(m, E)` (legitimate since `3^m < 2^E`)
   give (19). The ranges are: `m >= 2^22` by EXT-1 (`A_22 < 1/750`, `A_d` decreasing); `24000 <= m < 2^22` by
   `eta > 2^-27`, which gives `L < 2^49/3`, `ell < 48` and the bound `595/(19 m) + 1/393216`, below `1/750`
   from `m = 23532` on; `1 <= m <= 23999` by `L < U_m`, which contradicts the local descent for 23,994
   periods and gives `ell < h` with a bound below `1/750` for the other five. There is no gap between the
   three ranges, and `E >= E_m` is handled by monotonicity of `1 - 3^m/2^E` in `E`.
8. **External inputs.** Only EXT-1, declared under `assumes`, and only for `m >= 2^22`. The local descent,
   the logarithm enclosure and the power comparisons are recomputed by the certificate; no convergence bound
   and no period bound is imported. The only repository input is the second parameter theorem (4*) of the
   dependency, used only for `M > 18`.
9. **Certificate.** `check_non_half_period.py` passes and reproduces its receipt under Python 3.9.6,
   3.10.17 with `-O`, 3.12.10 with and without `-O`, and 3.13.11 (30 to 62 s). Every number quoted in the
   README is in the receipt. The script does what the README says: the geometry loop has no cutoff and raises
   on a family with positive area; the scan of `m < 2^22` uses outward dyadic endpoints of `alpha`; the final
   loop covers `1 <= m <= 23999` and asserts the residual list; the descent follows every odd seed below
   18,000,000 to a smaller odd value. `tools/check.py` reports 413 nodes, 0 errors, 0 warnings.

## How

All scripts use the standard library only and import nothing from the repository. They are kept outside the
repository.

| Script | Content | Result |
|---|---|---|
| `n2_geometry.py lemma 3 18 37 100 1 750` | lemma (6) by a different exact method (no clipping): for a fixed family every row is one of four kinds of half-plane, `x > X`, `y > Y`, `y > (1-R) x + C1`, `y < x/(1-R) - C2`; the rows are summarised by four running maxima and strict feasibility in `0 < x < y < 1` is decided with fractions at the break points of a concave function | 50 shifts, 468,340 (shift, family) pairs, none feasible; the rotation at which a family closes has the same histogram as the receipt: 466,902 at `j = 1`, 1,389 at 2, 45 at 3, 4 at 5 |
| `n2_geometry.py direct` | my affine rows against the definition at random rational phases | 626,501 row values equal |
| `n2_phase_zero.py` | every phase-zero configuration, `3 <= M <= 18`, straight from the definition with `f(0) = 1`: one track at phase 0, and two tracks with phases `(0, y)`, `y` in `{1/2, 1/3, 2/3, 1/7, 6/7}` | 2,133,852 configurations, maximal deficit at least `1/750` on all; smallest `1/360` |
| `n2_geometry.py sharp 3 18 37 100`, then `lemma` at two exact margins | the best possible margin of (6): bisection with exact tests, then the exact value | the bisection gives the bracket `0.0014944444444427` to `0.0014944444444518`. At margin exactly `269/180000` no family has a strict solution; at `269/180000 + 1/1800000000` exactly one has, `M = 18`, `a = 7`, `K = {8, 12}`, `L = {3, 17}`, with the second phase tending to 1. Its limit, the phase-zero configuration `h = 7/18` with cuts `8.63/18, 12.63/18, 4/18, 0`, has maximal deficit exactly `269/180000` (rotations 5 and 13). So the optimal constant in (6) is `269/180000` |
| `n2_geometry.py lemma 3 18 3 8 1 750` | the same lemma with `R = 3/8` | exactly one family is feasible, the one above: this is the regression control of the Remarks (`293/270000`, replayed) |
| `n2_geometry.py lemma Mlo Mhi 37 100 1 750 18`, run on the ranges 19-26, 27-31, 32-35, 36-38, 39-40 | the special case of (4*) needed here (cuts on one or two tracks, eighteen rotations), without the dual data of the dependency | 56,845,798 pairs over 194 shifts, none feasible; at most 5 rotations needed; best possible margins `0.0050867` (`19 <= M <= 26`), `0.0083871` (27 to 31), `0.0085171` (32 to 35), `0.0088111` (36 to 38), at least `0.01` (39, 40) |
| `n2_crosscheck.py` | my method against the definition: direct minimisation over the phases for the three extremal families, and 1,500 random families with `19 <= M <= 40` at random rational phases | minima `0.0014944445`, `0.0050866898`, `0.0083870968`, in agreement with the exact brackets; 726,630 row values equal to the definition; maximal deficit `>= 1/750` on all, smallest `0.0328` |
| `n2_arith.py constants` | every rational constant of sections 6 to 8 | `1/750 - A_22 = 3591763/29884416000`, `1/750 - (595/(19*24000) + 1/393216) = 8083/311296000`, `A_d` first below `1/750` at `d = 22` |
| `n2_arith.py alpha` | `alpha` from the `decimal` module (120 digits) lies inside enclosure (21); scan of all `m < 2^22` with a 300-bit fixed point | minimal `ceil(m alpha) - m alpha` is `9.306465434894e-08` at `m = 190537`, above `2^-25`; it agrees with the README numerator; at that period `E = 301994` and `eta > 2^-27` by exact integers |
| `n2_arith.py periods` | `U_m` for `1 <= m <= 23999` from exact powers | 23,994 periods with `U_m < 18000000` (largest `U_m` below the limit: `17306922.3` at `m = 12276`); residual `12941, 13606, 14271, 14936, 15601` with the `E_m`, `ceil(U_m)` and `h` of the table; worst bound `125681783/96683556864` |
| `n2_arith.py descent` | first descent of every odd seed `3 <= s < 18000000`, my own loop | 8,999,999 seeds, 31,421,072 odd steps, longest 181 at seed 13421671 |
| `n2_controls.py corpus` | actual cycles of `3x+d` found by iteration, `d` coprime to 6: `d <= 999` with odd seeds `<= 5000` (2,459 cycles, the number of the repository corpus) and `d <= 9999` with seeds `<= 3000` (33,150 cycles); every shift with exactly four mismatches and `M >= 3` | 377 and 3,608 such shifts, orders 3 to 15, both track shapes; on each: track partition, inclusion of the mismatches of `jH` in `C_j`, agreement runs, `2^F d_end = 3^r d_start`, the witness, the envelope (13) in exact integers, the transfer inequality with the true coefficient, and maximal deficit `>= 1/750` on the actual cuts; 103,376 refined runs in the larger corpus; no failure |
| `n2_controls.py words` | 1,500 random words with a four-mismatch shift of order 19 to 84, on the actual `3x+den(w)` cycle, eighteen rotations | 1,588 shifts, 743,424 refined runs, 128,470 artificial cuts, 342,768 coincidences; no failure |

**Controls.** Non-half-period four-mismatch shifts exist on actual cycles. Among the four standard addends,
with odd seeds up to 200,001: `3x+5` (6 cycles), `3x+7` (2) and `3x+61` (3) have none; `3x+13` (10 cycles)
has six cycles of period 5 with one, of order `M = 5`, for example `(259, 395, 599, 905, 341)` with word
`(1, 1, 1, 3, 2)` and `H = 2`, and `(287, 437, 331, 503, 761)` with word `(1, 2, 1, 1, 3)` and `H = 1`.
The argument does not exclude them, for the following reason. Everything up to (16) holds for every `d`,
with `delta_d = E - m alpha = sum log_2(1 + d/(3 n_i))`, and the conclusion is

```
epsilon_d = (ell + delta_d + alpha)/(alpha m) > 1/750.
```

On all 3,608 control shifts `epsilon_d >= 0.5210` (about 391 times `1/750`; attained by a `3x+11` cycle
with `m = 8`, `L = 13`); on the `3x+13` cycle above `epsilon_d = 1.2211`. Since `epsilon_d > 1/m`, no cycle
with `m <= 750` can ever be excluded by the geometric step. What excludes `3x+1` cycles is the upper bound
on `epsilon`, and it uses `d = 1` in three places: the drift (12), the bound (18) and the local descent.
All three fail on the controls. For `(259, ...)`: `delta_d/(alpha m) = 0.0095` against `1/393216`;
`eta = 13/256 = 0.0508` against `m/(3L) = 5/777 = 0.0064` (the true bound is `m d/(3L) = 0.0837`); and
`L = 259` is not below the `U_5 = 1280/39` that a `3x+1` cycle of period 5 would need. (18) fails on all
eleven shared fixtures, while `eta < m d/(3L)` holds on all of them.

## Corrections

1. **Certificates, the paragraph "Every control retains its actual addend d" (wording).** It names two steps
   specific to `d = 1`, the drift budget and the local descent. There is a third: (18), `eta < m/(3L)`, which
   for `3x+d` reads `eta < m d/(3L)`, and on which (19), `L < 2^49/3` and every `U_m` of section 8 rest. It
   fails on every control I looked at (above). Proposed text: "Three steps are specific to `d = 1`: the drift
   bound (12), where `1/(3 n_i)` becomes `d/(3 n_i)`; the bound (18), which becomes `eta < m d/(3L)`, and with
   it (19), the bootstrap and every `U_m`; and the local descent, a statement about the `3x+1` map. The run
   identity, the envelope (13) with `delta_d` and the geometric conclusion
   `(ell + delta_d + alpha)/(alpha m) > 1/750` hold for every `d`; no actual `3x+d` cycle violates the last
   one."
2. **Notation (wording).** Three symbols are used twice inside the proof: `L` is the level set of the second
   track in (4b) and (7) and the cycle minimum from section 6 on; `h` is the rotation `a/M` in sections 2 to 6
   and the bit length of `ceil(U_m)` in section 8; `d` is the dyadic index in section 7, part of `d_start`,
   `d_end` in section 6, and the addend in the Certificates section. Each use is defined where it occurs, so
   nothing is wrong, but a reader checking (17) against the table of section 8 meets two different `h`.
   Suggested: another letter for the second level set, for the bit length and for the dyadic index.

## Remarks

1. **Where EXT-1 is used.** Only for `m >= 2^22`. For `m < 2^22` the conclusion `M = 2` is unconditional
   (sections 7, second half, and 8 use computations only). The Statement could say so.
2. **Margins.** Lemma (6) has room: the optimal constant at `R = 37/100` is `269/180000 = 0.00149444...`,
   against the `1/750 = 240/180000` that is used. It is attained when one mismatch track passes through
   index 0, the cycle minimum, where the pre-drop value `f(0) = 1` is what the hypothesis allows. At
   `R = 3/8` the lemma is false with margin `1/750` (the control of the Remarks) and true with margin
   `1/10000`; I checked both.
3. **What the certificate's cycle controls cover.** They use orders 3 to 18 only (`order in ORDERS`), so the
   transfer for `M > 18`, the case that calls the dependency, is not exercised by this certificate (the same
   algebra; my `words` check covers orders 19 to 84). On the eleven shared fixtures the certificate checks the
   step equations and the envelope (13) only; none of the eleven has a four-mismatch shift.
4. **Dependence on the dependency.** For `19 <= M <= 40` I verified the needed special case of (4*) without
   the stored duals of `free-four-cut-eighteen-rotation-obstruction`. For `M > 40` the argument rests on that
   node as reviewed.
5. **Section 7, title.** "EXT-1 reduces the full period below 24000": EXT-1 gives `m < 2^22`; the exact scan,
   which needs no external input, gives `m < 24000`.
6. **Structure.** Lemma (6) (sections 1 to 4) is unconditional pure geometry, like the dependency, but it
   lives inside a node that MAP.md lists as resting on EXT-1. It could be a node of its own ("one idea, one
   node"); this is a suggestion, not a defect.

## What I could not check

- **EXT-1.** Taken from `musson-collatz-gap-all` as stated. I checked only that it is applied to the pair
  `(m, E)` with `3^m < 2^E`, and that `eta >= 2^-172 m^-341` is its content.
- **The regime of the theorem.** No actual cycle reaches it: the argument bites only when
  `(ell + delta_d + alpha)/(alpha m) < 1/750`, and the smallest value over the control cycles of both corpora,
  with or without a four-mismatch shift, is `0.0702` (`d = 439`, `m = 126`, `L = 4513`), about 53 times
  `1/750`. So the numerical evidence supports every step (identities, inequalities, the two geometric
  statements), not the conclusion itself, which rests on the written argument that I re-derived.
- **The geometric input for `M > 40`.** It is statement (4*) of the dependency. In my review of that node I
  verified its duals exactly and rebuilt its branch tree with my own code, but I did not re-derive the
  infeasibility of its cells without the stored duals.
- **Lean.** There is none for this node.
- **Novelty.** Not assessed.
