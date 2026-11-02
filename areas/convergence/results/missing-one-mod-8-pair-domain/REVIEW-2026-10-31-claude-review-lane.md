# Review of missing-one-mod-8-pair-domain

Independent review (Claude review lane, Fable 5.1, directed by Santiago Armstrong) of the claim, Statement items 1–4 and the legacy proof (1)–(7), against the definitions of [`elementary-bridge-quotient-normal-form`](../elementary-bridge-quotient-normal-form/README.md) (selected partners, bridge currents, run length `a = v₂(x+1)`), [`mixed-shrinking-pair-rules`](../mixed-shrinking-pair-rules/README.md) (domain `w ≡ 3 (mod 8)`, branches `O`, `E1`, `E2`), [`shrinking-paired-return-recursion`](../shrinking-paired-return-recursion/README.md) (terminal rule, class `59 (mod 128)`), [`tripling-doubling-pair-decomposition`](../tripling-doubling-pair-decomposition/README.md) (counterfamily) and [`retained-graph-complement-constructor`](../retained-graph-complement-constructor/README.md) (root classes).

## What I checked

- Certificates: `python3 tools/run_certificates.py --node missing-one-mod-8-pair-domain` exit 0, wall 6.92 s (`check_pair_one_recompute.py` PASS, under 1 s; `check_legacy_replay.py` PASS, 6 s).
- Hand derivations. §1: `S^(a−2)(q) = 2·3^(a−2) − 1`, then `3^(a−1) − 1` has 2-adic valuation 3 for `a − 1 ≡ 2 (mod 16)`, so `S^(a−1)(q) = w`; `9^m ≡ 9 (mod 64)` for `m ≡ 1 (mod 8)` gives `w ≡ 1 (mod 8)`; `S^a(x) = (3^a − 1)/2 = F(3w)`; `x = 2^a·1 − 1` is complementary (`1 ≡ −3^a (mod 4)`). §2: `3(48u+3)+1 = 2(72u+5)`, `3(16u+1)+1 = 4(12u+1)`; `9u ≡ 1 (mod 8)` canonical, so `18u+1` is selected with `a = 1 + v₂(9u+1) = 2`; the left and right currents and `div L_A = P(w) − P(v)`; `v = 3u ≡ 3 (mod 8)`, `3u < 16u+1`; the clock bookkeeping `S^j(3w) = S^(j−1)(3v)` for `j ≥ 3`, `S^j(w) = S^(j−1)(v)` for `j ≥ 2`, so a child clock `l ≥ 2` gives `l + 1`. §3: `9w − 1 ≡ 944 (mod 2304)` gives `v ≡ 59 (mod 144)`, so `v ≡ 11 (mod 16)`, `v` complementary canonical, `3v ≡ 1 (mod 16)`; the valuations `(1, 2)` on `3w` and `(2, 1)` on `w` from `9w+1 ≡ 946`, `27w+5 ≡ 2840 (mod 6912)`, `3w+1 ≡ 316 (mod 768)`, `9w+7 ≡ 952 (mod 2304)`; `(27w+5)/8 = 2(3v)+1`, `(9w+7)/8 = 2v+1`, selected by the dichotomy, run lengths `2` and `3`; parent clock `l + 2` for `l ≥ 2`; `A` and `B` disjoint (`1` and `9 (mod 16)`). §4: `v = 3(w−1)/16 ≡ r (mod M) ⟺ 3w ≡ 16r + 3 (mod 16M)` and `v ≡ 3 (mod 8)` forces `w ≡ 17 (mod 128)`; `9w ≡ 16r + 1`; CRT witnesses (`v ≡ 0 (mod 3)`; `16v + 1 ≡ 0 (mod 9) ⟺ v ≡ 5 (mod 9)`); the lift (5): `3^(a−1) ≡ 1 + 8c ≡ 9 (mod 64)` forces `a − 1 ≡ 2 (mod 16)`, and the even exponents are unique modulo `2^(m+1)` for a target `≡ 1 (mod 8)` modulo `2^(m+3)`; `ν(3w) = (3w−1)/2` on `A` (`3w ≡ 3 (mod 16)` selected) and `3w` on `B` (`3w ≡ 11 (mod 16)`). §5: (7) by adding the three divergences.
- Own code (scratch `r36_check.py`, own `S`, canonical test, bridges): all 4096 inputs `w ≡ 1 (mod 8)` below `2^15`: domains 256 (`A`), 128 (`B`), 3712 unresolved; the identities; my own local currents `L_A`, `L_B` with `div = P(w) − P(v)` (the certificate checks the identities only, not the currents); parent clocks `l + 1` and `l + 2` wherever the child clock `l ≥ 2` exists (every input); the cylinder mergers `S^4(3w) = S^5(w)` on `w ≡ 1681 (mod 2048)` and `S^5(3w) = S^6(w)` on `w ≡ 105 (mod 2048)` for 4096 members each and not one step earlier, with the reason made explicit: the children `v = 315 + 384m` and `v = 59 + 1152m` lie in R30's terminal class (`h = v₂(3v−1) = 4`, `z = 177 + 216m` resp. `33 + 648m`, `≡ 1 (mod 8)` canonical, `A = v₂(2z+2) = 2`, so `S^3(3v) = S^4(v)` on the whole class; checked for `m < 3000`); the lifts `w ≡ 1681 (mod 2048)` for `a ≡ 1699 (mod 4096)` and `w ≡ 105 (mod 2048)` for `a ≡ 659 (mod 4096)` (four exponents each); the four Mersenne mergers `a = 659, 1699, 4755, 5795` at `a+5, a+4, a+5, a+4` by direct iteration, not earlier, with `q < N < x`, `x ≡ 7 (mod 12)` above `9N/8`, complementary; my own R33 recognizer accepts the four children as terminal with child clock 3, and finds the child of `a = 147` (branch `B`) unresolved, although that pair does merge at child clock 11.
- Controls: the branch identities hold for 0 of 128 `A`-inputs and 0 of 64 `B`-inputs below `2^14` under `3x+5` and `3x+13` (`3x+1` arithmetic; no cycle claim is made).

## What I did not check

- R30's terminal rule and R33's cylinder theorem in general (both reviewed separately); R22's classification of `R_N` roots; the legacy receipt's current hashes and the capped `a = 659` supplied-input conversion beyond the replay.

## Findings

1. §4, "complete parent cylinder" and the table of pair clocks — **imprecision** (reading aid, not an error): the mergers on the two cylinders hold with a uniform clock, but the intermediate valuation words are not fixed along the cylinder (on `w ≡ 1681 (mod 2048)` the maximal fixed word of `3w` has length 3 and that of `w` length 4, below the clocks 4 and 5); the uniformity comes from the halving identity's uniform run length `A = 2`. The node never claims fixed words.
2. Claim and §5, "a = 147 is an explicit unresolved child example" — **imprecision**: unresolved for the R33 recognizer, as the node's convention says; the actual pair `(3w, w)` for `a = 147` merges at child clock 11, so this is a statement about the rule, not about the orbit.

No error or gap found.

## Verdict

HOLDS.

Claude review lane (Fable 5.1; directed by Santiago Armstrong), 2026-10-31
