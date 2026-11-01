# Review of depth-32-obstruction-infinite-family

## What I checked

- Folder conversion. The single file `depth-32-obstruction-infinite-family.md` became `depth-32-obstruction-infinite-family/README.md`; its eight relative links and the three evidence paths gained one `../`; the incoming links in [`depth-32-aggregate-exposure-obstruction`](../depth-32-aggregate-exposure-obstruction/README.md) (2), [`short-delay-all-phase-obstruction`](../short-delay-all-phase-obstruction/README.md) (1), [`unbounded-exposure-depth-necessary`](../unbounded-exposure-depth-necessary/README.md) (2) and [`uniform-aggregate-exposure-depth`](../../questions/uniform-aggregate-exposure-depth.md) (1) were repointed. `MAP.md` is left to the generator.
- Definitions, from the nodes: `A_N` (six-band table mod 18 of `disjoint-annular-recursion`, `Q = 9N/4`, support `(Q, 64Q)`), `G_D(N)` and the recursion `Reach(y, r)` with `B_r = ⌊3^r·144N/2^r⌋ − 1` (`depth-32-aggregate-exposure-obstruction`).
- Statement arithmetic. `N_0 = 96·2^24 = 12·2^27`, `64N_0 = 3·2^35`, `2^33 | 144N_0`, `M = 3^22 = 31 381 059 609`. The slopes `a_j = 3^j·64N_0/2^j = 3^(j+1)·2^(35−j)` are even integers for `j ≤ 34`; `3x_j + 1 = 2x_(j+1)` with `x_(j+1) = a_(j+1)q − 1` odd for every integer `q`, so all 34 valuations are 1; `x_34 = 2·3^35 − 1 = 100 063 090 197 999 413` at `q = 1`. Sources: `64N − 1` lies in band 4 with residue 5 (coefficient −2), `96N − 1` and `144N − 1` in band 5 with residue 17 (+2, +2), for every `q ≡ 1 (mod 3)`.
- The dyadic subfamily. `pow(2, 2·3^21, 3^22) = 1` and `pow(2, 2·3^20, 3^22) ≠ 1`, so the order of 2 is exactly `2·3^21 = 20 920 706 406`; the cubing lemma `z ≡ 1 (mod 3^r) ⇒ z^3 ≡ 1 (mod 3^(r+1))` follows from `(1 + 3^r m)^3 = 1 + 3^(r+1)m + 3^(2r+1)m^2 + 3^(3r)m^3`.
- The dual test (section 1, inherited from the parent node). If `C` is a component of `G_D(N)` with `1 ∉ C`, every arrow with one end in `C` has both ends in `C` and none is killed, so `Σ_(x∈C) ((I − P)J)(x) = 0` for every `J` supported on arrows of `G_D(N)`; then `A_N(C) = Σ_C ζ ≤ 0` contradicts `A_N(C) = 2`.
- The lifting argument, line by line. The inverse branch `(a, b) ↦ (2^v a/3, (2^v b − 1)/3)` keeps slopes positive with even numerator and power-of-3 denominator. For a state whose denominators divide `3^h` and `q ≡ 1 (mod 3^(h+2))`, `x(q) − x(1) = a(q − 1) ∈ 18Z`, which preserves the residue mod 18 (the coefficient inside a band), the residue mod 3 (parity class of inverse valuations, exclusion at multiples of 3) and oddness. `B_r(q) = 3^r·144N_0·q/2^r − 1` is exactly affine because `2^33 | 144N_0`. Every comparison `f(q) = uq + v` is settled for all real `q ≥ 1` by `u ≥ 0` and its sign at `q = 1`; the first excluded predecessor bounds all later ones of its parity class because `2^v` grows by 4 and the target is positive. The maximal denominator `3^20` gives `K = 22`. I read `symbolic_component_lift.py` and `check_symbolic_lift.py`: `sign_stable`, `register_state`, `predecessors_stable` and the closure loop over the 35 states implement exactly these checks.
- Certificate. The node lists none under `certificates:`. Its finite certificate `check_symbolic_lift.py` (a certificate of `unbounded-exposure-depth-necessary`) was run from the repository root: exit 0, 1.0 s wall. Receipt: `K = 22`, maximal denominator power 20, 9171 queries, 42487 inequalities, 96 with zero slope, minimum positive slope 10 737 418 240, minimum positive margin 1, period 20 920 706 406, as in section 3 of the node.
- Independent recomputation (`recompute_depth32.py` with my own oracle `my_oracle.py`, written from the definitions above, in the review lane's scratch folder). The complete component of `144N − 1` in `G_32(N)` at `q = 1`, `q = 1 + 3^22` (even) and `q = 1 + 2·3^22` is the 35-vertex chain with 34 arrows, sources `(−2, +2, +2)`, mass 2, `1 ∉ C`, and exactly 9171 memoised decisions in each case.
- Probe outside the class (not part of the claim). At `q = 4` and `q = 7` the component is again the chain; at `q = 2, 3, 5, 10` it is not (42, 48, 39, 40 vertices; 9, 14, 6, 4 sources; masses 2, 8, 4, 1). The claim is restricted to `q ≡ 1 (mod 3^22)` and says nothing about other `q`; the congruence is sufficient, not necessary.
- Controls. The claim is a finite statement about one graph built from the `3x+1` annulus; it holds or fails independently of whether Collatz is true, so no actual `3x+d` cycle can contradict it, and no `d`-uniformity is asserted. Not applicable.

## What I did not check

- The SHA-256 comparison of the receipt against a fresh trace beyond running the certificate; I did not regenerate the 42487 inequalities by hand.
- The depth-2 instance at `N_0 = 384` beyond the certificate's own run.
- The corollary on packed common-tail covers of source-to-anchor depth at most 32 (proved in the parent node, reviewed separately).

## Findings

1. (imprecision, corrected) Section "Certificates" began "This node has no folder of its own"; the review created the folder, so a parenthesis was appended to that sentence. No other text was changed.
2. (remark) The node has no `certificates:` field; its verification lives in another node's folder and is listed only under `evidence`, so CI will not re-run `check_symbolic_lift.py` when this folder changes. The recomputation above stands in for a certificate run.
3. (imprecision, not changed) `check_symbolic_lift.py` and `symbolic_component_lift.py` check by `assert`, so they are vacuous under `python3 -O`, contrary to AGENTS.md section 6; the node of the certificate says to run them without `-O`. Recorded also in the review of `unbounded-exposure-depth-necessary`.

## Verdict

HOLDS WITH CORRECTIONS. Corrections: the folder move with its link repairs, and the appended parenthesis in "Certificates"; neither changes the claim.

Claude review lane (Fable 5.1; directed by Santiago Armstrong), 2026-10-31
