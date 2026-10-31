# Review of outer-profile-closure-obstruction

Independent review of [`README.md`](README.md) (legacy R9-b): the outer-profile theorem, the period statement and the scoped closure corollary, against the definition of `A_N` in [`disjoint-annular-recursion`](../disjoint-annular-recursion/README.md) (reviewed) and the pushforward `P` of [`right-aligned-fixed-core-remainder`](../right-aligned-fixed-core-remainder/README.md). Every number below comes from my own script (`check_outer_profile.py` in the review lane's scratch folder: own `S`, own `A_N` built from the six-band table and cross-checked against the representative `P·V_N`, exact pushforward) or from a derivation written out here.

## What I checked

- **Certificates.** None are listed. `python3 tools/run_certificates.py --node outer-profile-closure-obstruction`: "1 node(s) checked, 0 certificate failure(s)", exit 0, 0.3 s. The legacy evidence checker (`check_arithmetic_reductions.py`) belongs to `universal-annular-partial-current` and is replayed there; I did not rerun it.
- **Node conversion.** The node was a single file; it was moved to `outer-profile-closure-obstruction/README.md`, its six relative links were repaired, and the five links to it in four other files were repointed (Finding 4).
- **The bound for words with a letter at least 2 (re-derived).** With `T(x) = (3x+1)/2`, `T^t(x) = λ^t(x+1) − 1`. For odd `x` with `v2(3x+1) ≥ 2`, `S(x) ≤ (3x+1)/4 = T(x)/2`, and `T` is increasing. If the exceptional step is the `(k+1)`-st of `t`, the composed bound is `λ^t(x+1)/2 + λ^(t−1−k)/2 − 1`, largest at `k = 0`. With `x ≤ 64Q − 1` (all of `supp A_N`, lower bands included), `y + 1 ≤ 32λ^t Q + λ^(t−1)/2 = λ^t(32Q + 1/3)`, because `1/(2λ) = 1/3`. So in the strip only the all-one word contributes.
- **The all-one word.** `y + 1 = λ^t(x+1)` gives `x = 2^t(y+1)/3^t − 1`; for odd `y` this is an odd integer iff `3^t | y+1`, and then `v2(x_(t−1)+1) = v2(2(y+1)/3) ≥ 2`, which forces the first `t` valuations to be exactly 1, so `S^t(x) = y`. Strip bounds: `x + 1 > 32Q + 1/3` gives `x ≥ 32Q + 1` (odd integer, `32Q` even) and `x + 1 ≤ 64Q` gives `x ≤ 64Q − 1`: the top band `j = 5`. Its row of the reviewed table is `−1` at `x ≡ 5, 11` and `+2` at `x ≡ 17 (mod 18)`, 0 otherwise. Since `x + 1 = 2^t·(y+1)/3^t`, `x ≡ 17 (mod 18)` iff `3^(t+2) | y+1`, and `x ≡ 5, 11 (mod 18)` iff `3^(t+1) | y+1` but `3^(t+2) ∤ y+1`. This is the displayed formula, including both zero cases (`3^t ∤ y+1`: no source; `3^(t+1) ∤ y+1`: a source of coefficient 0). Absorption at 1 plays no role: the strip lies above `32·18 = 576` and the all-one path increases.
- **Period.** On odd `y` the profile depends on `(y+1) mod 3^(t+2)` only, so `2·3^(t+2)` is an even period; an even `M` with `3^(t+2) ∤ M` moves the value 2 at `y ≡ −1` to 0 or `−1`, so no smaller even period exists.
- **Closure corollary.** A fixed finite list of profiles has a common even modulus `M`; choose `t` with `v3(M) < t + 2`. The strip has length `λ^t(32Q − 1/3)`, unbounded along any dyadic ray; with at most `K(t)` pieces, one piece covers a sub-interval of the strip longer than `M + 2·3^(t+2)`, on which the represented function is `M`-periodic while the true profile is 2 at some `y ≡ −1 (mod 2·3^(t+2))` and 0 or `−1` at `y + M`. Overlapping pieces do not help, since a sum of `M`-periodic functions is `M`-periodic.
- **Computation** (`check_outer_profile.py 160 6`, 15.9 s). For every `N = 8, 16, …, 160` and `t = 0, …, 6`: `A_N` from the table equals `P·V_N` for `N ≤ 64`; `P^t A_N`, computed by exact pushforward, agrees with the formula at all 1,945,710 odd `y` of the strips; the least even period is `2·3^(t+2)` in all 133 cases where a strip holds at least two periods; the trajectory bound holds for all 336,420 (source, `t`) pairs; and the formula fails at the first odd `y` below the strip in every case, so the strip is sharp.
- **Controls.** Not applicable: `A_N` and the `×64` recursion are `3x+1` objects (the reviewed dependency records that `3x+61` has no such recursion), and the node claims nothing about other `d`.
- **Scope.** The claim blocks exactly what the proof reaches: a fixed finite modulus list under literal synchronous pushforward `P^t`, with a piece count uniform in `N` for each `t`. It does not, and the text says it does not, exclude growing moduli, piece counts growing with the scale, algebraic rewrites before transport or unequal-time cancellation, and it says nothing about aggregate exposure depths (proved separately in `unbounded-exposure-depth-necessary`). Consistent.

## What I did not check

- The legacy checker `check_arithmetic_reductions.py` (evidence, in `universal-annular-partial-current`).
- The written proof of the six-band table; I took it from the reviewed node `disjoint-annular-recursion` and re-derived only the cross-check `A_N = P·V_N`.
- The dependents (`annular-root-collapse-contraction` and the two questions) beyond repointing their links; they use only the existence of the `+2` atoms and the closure statement.

## Findings

1. **Statement and claim (imprecision).** "a finite fixed list of periodic residue profiles on intervals, with a number of interval pieces bounded independently of `N` for each fixed `t`" is exactly what the proof uses: the common modulus `M` is independent of `t` and `N`, and the piece count `K(t)` is independent of `N`. A representation whose moduli grow with `t` is not excluded, as the Remarks say. No change.
2. **Proof, "Outer profile" (imprecision).** "the divisibility conditions also guarantee integrality and the exact all-one branch" is correct but terse: the content is `v2(x_(t−1)+1) = v2(2(y+1)/3) ≥ 2`, which makes every earlier valuation 1. No change.
3. **Sharpness (remark, not claimed).** The formula fails at the first odd `y` below the strip for every tested `(N, t)`: the strip is exactly the region where the all-one word is the only contributor.
4. **Links changed by the folder move.** In this node the links to `disjoint-annular-recursion`, `universal-annular-partial-current`, `unbounded-exposure-depth-necessary`, `annular-root-collapse-contraction`, the question `uniform-aggregate-exposure-depth` and the archive report each gained one `../`. Repointed to `outer-profile-closure-obstruction/README.md`: `annular-root-collapse-contraction.md` (Remarks), `universal-annular-partial-current/README.md` (Remarks and History, two links), `questions/uniform-aggregate-exposure-depth.md` and `questions/five-ray-annular-current-supply.md`. `MAP.md` is generated and still shows the old path until it is rebuilt.

## Verdict

HOLDS. No correction to the claim or the proof; the node was converted to a folder; no certificates exist; status raised to `reviewed`.

Claude review lane (Fable 5.1; directed by Santiago Armstrong), 2026-10-31
