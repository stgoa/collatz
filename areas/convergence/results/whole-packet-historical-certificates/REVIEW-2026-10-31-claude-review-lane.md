# Review of whole-packet-historical-certificates

Independent review of [`README.md`](README.md) (author: ChatGPT main lane, Codex). Scope: finite statements about `Π^R_N` for ten cutoffs, odd-only `3x+1`, absorbing at 1. Every number below comes from my own script (`recompute_whole.py`, outside the repository: own `S`, own `Π^R_N` from the written grouping rule, own union-find search, own routing) or from the certificate runs.

## What I checked

- **Certificates.** `python3 tools/run_certificates.py --node whole-packet-historical-certificates`: `check_stored_currents.py` `PASS` (0 s), `check_legacy_replay.py` `PASS` (19 s); exit 0; 19.7 s wall for the call. The replay re-runs the unmodified `whole_packet_demo.py` (all ten searches, the synchronous comparison, the hitting times) and compares its receipt and the four tables byte for byte.
- **Part (a) against my own packets.** My grouping reproduces `Pν_N = Π^R_N + η_N` for `8 ≤ N ≤ 600`. `Π^R_65536` has 34,716 atoms and `Π^R_2053` 1,086. The stored exact table satisfies `Π^R_65536 = (I − P)J` with 53,621 rows and positive cost 74,725; the stored one-sided table satisfies `Π^R_2053 = (I − P)J + Z` with 1,532 rows, cost 1,950 and `Z = −2δ_2215 − δ_3227 − δ_3839 − δ_4127` (mass `−5`).
- **Parts (b), (c) by re-implementation.** Depth `d` exposes the first `d` arrows from every source; components by union-find over sources, exposed states and 1; exact success when every component without 1 has mass 0, one-sided when mass `≤ 0`. All twenty historical depths of the table are reproduced; the synchronous depths (first `d` with `P^d Π^R_N = 0`) are 44, 51, 61, 61, 78, 78, 86, 97, 101, 128 and equal the largest source hitting time at every cutoff (the first depth with `P^d Π^R_N < 0` everywhere is 39, 41, 50, 50, 62, 62, 77, 94, 99, 123). At 2053 the exact success leaves 27 sources unlinked to 1 in two mass-zero components of 18 and 9 sources; the one-sided success leaves 32 in six components of masses `0, 0, −2, −1, −1, −1` (18, 9, 2, 1, 1, 1 sources). At 65536 both modes succeed at depth 72 with every source linked to 1. Exact success links every source at the other eight cutoffs too; one-sided unlinked counts there are 0, 1, 3, 1, 8, 2, 1, 8.
- **The stored tables are the unique currents.** The synchronous current `Σ_(d≥0) P^d Π^R_65536`, computed directly, equals the stored exact table row for row, and so does my routed depth-72 current. At 2053 my routed one-sided current, with the residual anchored at each component's minimum state, equals the stored table row for row. At every cutoff the exposed graph at success is a forest (each component has exactly one vertex without an exposed arrow), so the routed current is determined by the depth and the anchor convention; row counts and costs are not search artefacts.
- **Uniqueness lemma, re-derived.** If `(I − P)J = 0` with `J` finite and `J(x) ≠ 0`, then `J(x) = Σ_(S(y)=x) J(y)` gives a predecessor with nonzero weight; the backward chain inside the finite support repeats, so some `y_i` is periodic and `x = S^i(y_i)` lies on the same cycle; predecessors off the cycle carry weight 0, so `J` is constant along each cycle. Both currents are supported on orbits of sources that terminate (checked, cap 1000), hence in the absorbing component, which has no cycle once the arrow out of 1 is removed; their difference is 0. Confirmed by equality of the exact historical and synchronous currents at all ten cutoffs.
- **Controls.** On `3x+5` the kernel is nontrivial: `J = δ_19 + δ_31 + δ_49` on the cycle `19 → 31 → 49 → 19` has `(I − P)J = 0`, so exact currents there are unique only up to cycle circulations, exactly as the proof says. For sources in the absorbing component of `3x+5` (`9, 41, 169`, each with `3x+5` a power of 2) the historical exact current equals the synchronous one. For `δ_19 − δ_23` (two distinct `3x+5` cycles) neither search succeeds within 200 depths, as [`orbit-component-current-criterion`](../orbit-component-current-criterion/README.md) predicts for component masses `+1, −1`. The node makes no cycle claim, so the actual `3x+d` cycles enter only this way.
- **Grid membership.** `120 = 30·4`, `236 = 59·4`, `480 = 30·16`, `1984 = 31·64`, `3008 = 47·64`, `15104 = 59·256`, `65536 = 32·2^11` lie on the 30-ray grid `{m·2^b : 30 ≤ m ≤ 59, b ≥ 2}`; `517`, `2053`, `8197` are odd, so they lie on no dyadic grid; `65536 = 16·2^12` is the only five-ray cutoff.

## What I did not check

- The semidecision theorem itself (reviewed node).
- The legacy demo line by line (re-implemented instead); its `ray_constants` block belongs to [`mesh-maximum-principle-alternative-grids`](../mesh-maximum-principle-alternative-grids.md) and was not examined.
- The legacy claim that 2053 was "deliberately chosen"; novelty.

## Findings

1. Statement (c) (imprecision): "At all the sampled earlier 30-ray cutoffs" describes 120, 236, 480, 1984, 3008 and 15104, but 517 and 8197 are odd and lie on no dyadic grid. The asserted fact, every source linked to 1 at exact success, holds for them as well; 2053 is the only cutoff with unlinked sources. **Correction applied:** a parenthetical in Statement (c) names the grid members and the three odd cutoffs; no wording removed.
2. Proof (imprecision): "finite currents on an absorbing functional component are unique" needs the arrow out of 1 excluded (the fixed point `1 → 1` is otherwise a cycle); the node's convention (no row at 1, `P` kills mass at 1) does this. No change.
3. Statement (b) (imprecision): the synchronous column is the first `d` with `P^d Π^R_N = 0`; it equals the largest source hitting time in all ten samples (Remark "Cost") but is in general only bounded by it. No change.

No error found.

## Verdict

HOLDS WITH CORRECTIONS. Corrections: (1) the parenthetical in Statement (c) on which cutoffs lie on the 30-ray grid.

Claude review lane (Fable 5.1; directed by Santiago Armstrong), 2026-10-31
