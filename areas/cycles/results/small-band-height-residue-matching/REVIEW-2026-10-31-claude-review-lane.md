# Review of small-band-height-residue-matching

## What I checked

- Read the conventions, `areas/cycles/OVERVIEW.md`, the node ([`README.md`](README.md)), [`MATCHING_ARITHMETIC.md`](../ordered-cycle-sorted-rank-residues/MATCHING_ARITHMETIC.md) §§1–2, [`INDEPENDENT_MATCHING.md`](../ordered-cycle-sorted-rank-residues/INDEPENDENT_MATCHING.md) §§2–3, the dependencies [`dyadic-order-lemma`](../dyadic-order-lemma.md) (`c_i ∈ {1, 2}` when `q ≤ L`; order gives mechanical `c` and `gcd(A, m) = 1` for `m > 1`) and [`ordered-cycle-residue-law`](../ordered-cycle-residue-law.md) (numerators are units mod `q`), and the related nodes for context.
- **Re-derived the proof line by line, modulo any divisor `Q > 1` of `q`** (`2`, `3`, `L` and all `n_i` are units mod `Q`):
  - *Arrows.* `2^(c_i)·Z_(i+1) ≡ 3Z_i`. Equal endpoint residues would give `Q | 2^(c_i) − 3 ∈ {−1, 1}`: impossible. The two candidate successors `3r·2^(−1)` and `3r·2^(−2)` of a unit `r` differ, their difference `3r·2^(−2)` being a unit.
  - *Three values.* If the chronological normalised residues took exactly two values they would alternate (consecutive ones differ), so `m` is even and `c_i` is determined by `Z_i`, hence constant on each parity class: `c` has period `≤ 2`. For `c = (x, y, x, y, …)`, `A = (m/2)(x + y)`, so `gcd(A, m) = (m/2)·gcd(x + y, 2)` if `x ≠ y` and `m` if `x = y`; `gcd(A, m) = 1` forces `m = 2`, `{x, y} = {1, 2}`, `A = 3`, `D = 2^3 − 3^2 = −1 < 0`, no positive cycle. So at least three residues occur.
  - *`|Z_0| ≥ 2`.* The minimum has sorted rank 0 and `c_0 = floor(A/m) = 1` (`A = m + s`, `0 < s < m`); `h_0 = 0` and `a_0 ≥ 1` give `h_1 = c_0 − a_0 + h_0 ≤ 0`, so `h_1 = 0`, `a_0 = 1`, and the two height-0 residues differ by the arrow argument.
  - *Rising arrows.* `h_(i+1) − h_i = c_i − a_i ≤ 1`, so heights climb from 0 to `B` one level at a time and the first arrival at level `h + 1` comes from level `h`; such an arrow has `a_i = c_i − 1 ≥ 1`, so `c_i = 2`, and its endpoints differ. Hence `Z_h`, `Z_(h+1)` are never the same singleton, and every level `0, …, B` is occupied.
  - *`B = 2`.* A deficient pair would have a one-element union: `{0,1}` and `{1,2}` are excluded by rising arrows, `{0,2}` by `|Z_0| ≥ 2`; a deficient triple would have at most two residues in total, excluded by the three-value result. `B ≤ 1` are subcases. *Raw `B = 1`:* `n_0`, `n_1` are both at height 0 with `2n_1 = 3n_0 + q`, so `n_1 ≡ n_0` would give `Q | 1`; `|R_0| ≥ 2` excludes the only possible deficient pair.
  - *Lemma.* For `I` inclusion-minimal with `|N(I)| < |I|`, every `I∖{x}` satisfies Hall, so `|I| − 1 ≤ |N(I∖{x})| ≤ |N(I)| ≤ |I| − 1`; a residue in exactly one level `x` would give `|N(I∖{x})| ≤ |I| − 2`.
  - *Scope.* Every step uses `Q > 1`; nothing is claimed at `q = 1` or beyond the stated bands, as the claim says. The hypotheses `q ≤ L`, `m > 1`, order and reduced `q` are exactly what the two dependencies need.
- **Controls.** From my own enumeration of the `3x+d` cycles (odd seeds `≤ 5000`, all 333 `d ≤ 999` coprime to 6, reduced to lowest terms; 1,184 distinct cycles, the corpus count), exactly 50 lie in the ordered domain (`m > 1`, `q ≤ L`, sorted `F` increasing), all with `q > 1`; `B` histogram `0:4, 1:20, 2:11, 3:11, 4:3, 9:1`. On each of them, modulo every divisor `Q > 1` of `q`, I verified every lemma used (`c ∈ {1,2}`, `c = mech(A, m, 0)`, `gcd(A, m) = 1`, units, height rises `≤ 1`, `h_0 = h_1 = 0` with `a_0 = c_0 = 1`, all levels occupied, consecutive residues distinct, at least three residue values, `|Z_0| ≥ 2`, rising arrows with `c = 2` and distinct endpoints) and the theorem by brute-force Hall: 35 normalised instances with `B ≤ 2` and 24 raw instances with `B ≤ 1`, no failure. Beyond the stated bands: modulo the full `q`, all 15 normalised (`B ≥ 3`) and 26 raw (`B ≥ 2`) instances also match; modulo the proper divisor 5, the two ordered `q = 355` cycles (minima 14077 and 14429, `B = 4`) fail both the normalised and the raw Hall condition. So the divisor-wise statement really stops at the stated bands, consistent with [`primewise-height-residue-matching`](../../attempts/primewise-height-residue-matching.md).
- **The two period-17 cycles** of `INDEPENDENT_MATCHING.md` §3, reconstructed by iterating `3x+5077565` from the minima 446,400,719 and 365,289,811: `q = 2^27 − 3^17 = 5·1,015,513` is reduced (`gcd(L, q) = 1`), both are ordered with `q ≤ L`, `B = 3` and `2`; modulo 5 the stated failures appear (`{1,3} → {4}` normalised and `{1,2,3} → {2,3}` raw; all three raw sets `{1,4}`), and modulo `q` both matchings exist.
- **The Remark's control.** The ordered `q = 5` period-17 cycle with minimum 187 has raw residue 2 at every height 0–3, band maxima 283, 643, 1453, 2773, all `≡ 3 (mod 5)`, and full raw and normalised matchings. The other ordered `q = 5` period-17 cycle (minimum 347) also has residue 2 at every height, but its band maxima have residues 2, 3, 4, 2.
- The lemma was also brute-forced on 15,334 random inclusion-minimal deficient families.
- **Certificates.** None listed; nothing to run. My scripts (outside the repository): `controls.py` and `check_matching.py`, 0.7 s each, with printed receipts.

## What I did not check

- The historical receipt `height_matching_audit.json` and its counts (1,185 cycles, 51 ordered) were not re-run; my corpus-only count is 50 ordered cycles, the difference presumably being fixture cycles.
- The Lean side (none is claimed for this node).

## Findings

1. **Ambiguous control reference (imprecision; corrected).** The Remark cites "the ordered `q = 5`, period-17 control"; both `q = 5` period-17 cycles of the corpus (minima 187 and 347) are ordered with `B = 3`, and only the one with minimum 187 has raw residue 3 on all band maxima. Added "(minimum 187)".
2. **Redundant hypothesis (note; not changed).** "`q > 1` coprime to 6" is automatic for a reduced denominator, since `q | 2^A − 3^m`.
3. **Links (typo level; corrected).** After the move to a folder, six body links and three evidence paths needed one more `../`.

## Verdict

HOLDS WITH CORRECTIONS: (i) the `q = 5` control in the Remark identified by its minimum 187; (ii) relative links and evidence paths repaired after the move to a folder. The proof is complete and correct for exactly the stated scope. No certificates to run. Status raised to reviewed.

Claude review lane (Fable 5.1; directed by Santiago Armstrong), 2026-10-31
