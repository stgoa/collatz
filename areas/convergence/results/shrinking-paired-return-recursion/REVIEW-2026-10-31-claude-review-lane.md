# Review of shrinking-paired-return-recursion

## What I checked

- Certificates, from the repository root with `python3 tools/run_certificates.py --node shrinking-paired-return-recursion`: `check_paired_return_recompute.py` PASS (3 s), `check_legacy_replay.py` PASS (7 s; replays `check_paired_return.py` and `batch_64fff1d_check.py` unmodified); exit 0, 10.5 s wall.
- The pair identity (3) with every valuation, from `3w = 1 + 2^h C`, `S(w) = 1 + 2^(h-1) C` and `S(1 + 2^e c) = 1 + 3·2^(e-2) c` for odd `c`, `e ≥ 3`: the exponents met along the two prefixes are `h, h-2, …, 4` and `h-1, h-3, …, 3`, all `≥ 3`.
- The terminal branch: for `z ≡ 1 (mod 8)`, `2z + 1 = 4·((z+1)/2) − 1` with `(z+1)/2 ≡ 1 ≡ 3^2 (mod 4)`, selected with `A = 2`; for a complementary climber `z = 2^b t − 1`, `2z + 1 = 2^(b+1) t − 1` with `t ≡ −3^b ≡ 3^(b+1) (mod 4)`, selected with `A = b + 1`. With `S(4z+1) = S(z)` this is (4). The recursive branch: `z ≡ 101 (mod 128)` is `5 (mod 8)`, never canonical, so the two branches are disjoint and the recogniser is deterministic; I recomputed the divergence of the current (7) row by row, the bounds (8) and the clock (9).
- The cylinders of §3: `229 R(w) − 7 = (27/256)(229 w − 7)`; integrality of `R^j(w)` from `256 ≡ 27 (mod 229)`; branch exactness from `(16v − 1)/9 ≡ 119 (mod 128)` (odd, so `h = 4`) and `(16v − 1)/3 ≡ 101 (mod 128)`; the final value `≡ 59 (mod 128)` with `z = (9w − 3)/16 ≡ 1 (mod 8)`.
- The lifting (15): the order of 3 modulo `2^n` is `2^(n−2)`, `{3^e : e ≡ 6 (mod 16)}` is exactly `{x ≡ 25 (mod 64)}` modulo `2^(M+3)`, and `1 + 8c ≡ 25 (mod 64)` for `c ≡ 3 (mod 8)`, so `e` modulo `2^(M+1)` and `c` modulo `2^M` correspond bijectively.
- The comparison (2) by the lifting-the-exponent lemma: `v₂(3^(a−1) − 1) = 2 + v₂(a−1) = 3` and `v₂(3^a − 1) = 1` for `a ≡ 7 (mod 16)`; then `S^(a+1)(x) = S(3w)` and `S^(a−1)(q) = w` give the same-clock merger (16) from (14), and `B_x` of (18) has divergence `δ_x − δ_q`. The extraction argument of §5: in a finite functional graph every weak component has one terminal (sink or cycle); the component of `x` has total divergence 1, so it contains the sink 1, and every row in it follows support edges to 1.
- Own scripts, in my scratch folder (`recheck_pairs.py`, `recheck_cylinders.py`, `controls.py`, 4 s in total), with their own `S`, canonical test and recogniser: all 65,536 values `w ≡ 3 (mod 8)` below `2^19` (identities with every valuation, (5), (6a–e), (8)); the recogniser accepts 10,979 of them (10,922 terminal, 57 with one recursive layer; 43,691 have odd `h`, 10,582 another noncanonical `z`), every accepted clock verified by direct iteration; `a = 7` (`w = 91`, `h = 4`, `z = 51` a selected climber) and `a = 23` (`h = 3`) unresolved. Cylinders `c_r` for `r = 0..12` on six random positive members each (multipliers up to `2^40`): exactly `r` recursive `k = 1` layers, final value `59 (mod 128)`, merger at `3r + 3`. The order of 3 modulo `2^n` for `n ≤ 60`. The table `a_r`, `r = 0..4`, reproduced by my own bit lifting with `3^(a_r − 1) ≡ 1 + 8 c_r (mod 2^(8r+10))`; the `a ≡ 39 (mod 2^20)` class (`h = 8`, `z ≡ 101`, child `59 (mod 128)`). Mersenne mergers (16) by direct iteration for `a = 39, 135, 199, 263, 423, 455, 711, 2887` and for the further class members `a = 967, 1223` (`r = 0`) and `a = 68423` (`r = 1`, 3 s); `a = 39 + 2^20` on the `w` side (`w` has 1,662,011 bits): `S^8(3w) = S^9(w)`. The earliest same-clock mergers for `a = 39, 199, 455` are 47, 202, 458, equal to the prescribed `a + 8`, `a + 3`, `a + 3`. The orbits of `x = 2^39 − 1` and `q = 2^38 − 1` both have 191 rows.
- Controls (`controls.py`): for `d = 5, 7, 13, 61` and all `w ≡ 3 (mod 8)` below `2^16`, the pair identity `S_d^k(3w) = 4z + 1` holds for 0 of the 2,730 even-`h` inputs (2,730 of 2,730 for `d = 1`); the prescribed merger holds for 257, 2, 374 and 1,041 of the 1,370 `d = 1`-accepted `w` (coincidences inside a common cycle); the pair `(w, 3w)` lands in different cycles for 1,722 (`d = 5`), 0 (`d = 7`), 1,707 (`d = 13`) and 347 (`d = 61`) values, e.g. `d = 5`: `w = 3` lies in the cycle of 19 and `3w = 9` reaches 1. The construction is `3x+1`-specific, as the Remarks say, and no claim excludes a control cycle.

## What I did not check

- That `x = 2^a − 1` is an actual weight-1 root of the residual profile `R_N` at `N = 12·2^(a−4)`: taken from [`complementary-run-bridges`](../complementary-run-bridges/README.md), Statement 4; the certificate checks only the range `(9N/8, 3N/2)` and `x ≡ 7 (mod 12)`.
- The signed bridge currents and hashes of the legacy constructor, and the side-lane probe `batch_64fff1d_check.py`, beyond their replay exiting 0.
- Class members with `r ≥ 2` on the `x` side (`3^(a−1)` for `a = 7768903` has about 12 million bits); their cylinder was checked on the `w` side only.

## Findings

1. Statement 1 and Proof §1 (imprecision): "actual weight-1 complementary root" is inherited from `complementary-run-bridges` without a pointer to its Statement 4; nothing in this node or its certificate establishes root status.
2. Statement 2 (imprecision): the terminal and recursive classes are not said to be disjoint; they are (`z ≡ 101 (mod 128)` is `5 (mod 8)`, never canonical), which is what makes the recogniser's output unique.
3. Proof, throughout (typo): the migrated legacy text lost the spaces before numerals ("absorbing at1", "modulo8", "a=7 modulo16").
4. Remarks, clock correction: consistent with my earliest-merger computation (202, 458, 47).

## Verdict

HOLDS. Every displayed identity, bound and clock re-derives; the finite claims recompute on larger ranges than the certificates use; the scope (odd-only clock, absorbing at 1, `w ≡ 3 (mod 8)`, even `h`, the named cylinders, supplied absorption below `N` as the input, `a = 7, 23` unresolved) is exactly what the proof delivers.

Claude review lane (Fable 5.1; directed by Santiago Armstrong), 2026-10-31
