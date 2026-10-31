# Review of depth-32-aggregate-exposure-obstruction

Independent review (Claude review lane, Fable 5.1; directed by Santiago Armstrong). The node was a single file; it was moved into this folder for the review (see the History line in the node). Nothing of the node's own code was used: every number below comes from scripts written for this review in the reviewer's scratch folder, or from the node's own proof.

## What I checked

- **Definitions followed down.** `A_N` and its six-band table (`disjoint-annular-recursion`, reviewed), the exposed graph `G_D(N)` (an arrow `x -> S(x)` is present iff `x != 1` and some nonzero source reaches `x` in at most `D - 1` steps), and the component dual test (`orbit-component-current-criterion`, reviewed).
- **Dual test (Statement 1), re-derived.** Let `J` be supported on arrows of `G_D(N)` and `C` a component of `G_D(N)` with `1` not in `C`. Pairing `(I - P)J` with the indicator `1_C` gives `sum_{y in C} J(y) - sum_{y : S(y) in C} J(y)`; an arrow of `G_D(N)` joins two vertices of one component, and no arrow of `C` ends at `1`, so the two sums are equal and the pairing is `0`. Hence `A_N(C) = <1_C, zeta> <= 0`, contradicting `A_N(C) > 0`. For the catalogue remark: an arrow at distance `j <= D - 1` from a source of a packed tree lies in `G_D(N)` by definition.
- **Oracle (Statement 2), re-derived.** Height bound: `T(x) = (3x+1)/2` satisfies `T^r(x) + 1 = (3/2)^r (x + 1)`, `S <= T` and `T` is monotone, so `S^r(x) <= T^r(x) <= (3/2)^r 144N - 1`, hence `<= B_r = floor(3^r 144N / 2^r) - 1` for integer states. Predecessor rule: `p = (2^a y - 1)/3` is an integer iff `2^a y = 1 mod 3`, i.e. `a` odd for `y = 2`, even for `y = 1 (mod 3)`, none for `3 | y`; `p` is odd and `v_2(3p + 1) = a` exactly because `y` is odd. Exactness of `Reach(y, r)` by induction on `r` (a route of length `<= r` ending at `y` has its last predecessor `<= B_(r-1)`; conversely every recursive witness is an actual route from a source). Saturating outgoing and incoming exposed arrows from a vertex visits every incident arrow of every visited vertex, so it returns the whole component. Numerically: the bound `B_r` on 6000 random forward orbits (`N = 8, 96, 10368`, `r <= 8`); the predecessor rule against brute force for every odd `y < 4000`.
- **Two independent implementations agree.** A brute-force forward exposure graph built from every source of `A_N` with a union-find (no inverse reasoning) and a separately written inverse oracle give the same component in 192 comparisons (`N` in `{8, 16, 24, 40, 96, 136, 288, 520}`, `D` in `{1, 2, 3, 4, 6, 8}`, the top source and three random sources each).
- **Statement 3 (depth 32 at `N*`).** `N* = 96 * 2^24 = 12 * 2^27 = 1 610 612 736`, `X = 128 N* / 3 = 2^36`. My oracle at depth 32 from `144 N* - 1` returns exactly the 35 vertices `x_j = 3^j 64N*/2^j - 1`, `0 <= j <= 34` (all integral), the 34 consecutive arrows, all valuations `1`, the source table `103079215103 -> -2`, `154618822655 -> +2`, `231928233983 -> +2` (these are `64N* - 1`, `96N* - 1`, `144N* - 1`), mass `2`, `1` absent, last vertex `100063090197999413 = 2 * 3^35 - 1`, and `9171` memoised decisions, the number the node reports. `267 N* / 8 = 53 754 200 064`.
- **Statement 4 (`N = 10368 = 8 * 6^4`).** By brute force from all `267N/8 = 345 978` sources: at depth 1 the component of `1492991 = 144N - 1` has 5 vertices, 4 sources and mass `6`; at depth 2 it has 34 vertices, 33 arrows, 27 sources, positive mass `22`, negative mass `-22`, and does not contain `1` (my oracle agrees). The arrows `174761 -> 131071 -> 196607` (coefficients `-1, 0, +3`) and `196607 -> 294911 -> 442367 -> 663551 -> 995327 -> 1492991` are as stated. Here `X = 128N/3 = 27 * 2^14` is divisible by 3, so the residue pattern of the three-source chain does not apply.
- **Certificates.** None listed. The cross-node certificate `check_symbolic_lift.py` of `unbounded-exposure-depth-necessary`, which re-runs the integer oracle at `N*`, depth 32: PASS, 1 s (in `python3 tools/run_certificates.py --node unbounded-exposure-depth-necessary`, exit 0, total 28 s wall). The legacy checker `check_inverse_exposure.py` (evidence) is replayed unmodified by that node's `check_legacy_replay.py`: PASS, 26 s.
- **Controls.** Not applicable as a cycle test: the claim is a finite statement about one explicit signed measure on the `3x+1` graph and excludes no cycle of any `3x+d`. The oracle's two map-specific ingredients (height bound, predecessor rule) were tested directly as above.

## What I did not check

- The 48 forward-graph comparisons inside the legacy checker (replayed, not re-read).
- Behaviour beyond depth 32 is not claimed; for information, my oracle finds that at depths 33, 34 and 36 the component of `144N* - 1` has 117, 118 and 120 vertices, 43 sources and mass `18`, still positive and still without `1`.
- Novelty (the node claims none).

## Findings

1. (imprecision, corrected) Section "Certificates" said "This node has no folder of its own"; this review moved the node into a folder, so a parenthesis was appended. All relative links of the node gained one `../`, and the incoming links from `depth-32-obstruction-infinite-family`, `short-delay-all-phase-obstruction`, `unbounded-exposure-depth-necessary`, `uniform-aggregate-exposure-depth` and `exposure-absorption-giant-component` were repointed.
2. (remark) `X = 2^36` has `v_3(X - 1) = 3`, so the written theorem of `unbounded-exposure-depth-necessary` guarantees isolation of this chain only through depth 1 (through depth 4 with the refinement in `delayed-release-cancellation`). The depth-32 isolation at `N*` is therefore a computed fact about this cutoff, which the node presents correctly as such, and which `depth-32-obstruction-infinite-family` lifts to a congruence family.
3. (remark) The node's verification lives in another node's folder and is listed only as evidence; the recomputation above stands in for a certificate of this node.

## Verdict

HOLDS WITH CORRECTIONS. Corrections: the folder move with its link repairs and the appended parenthesis in "Certificates"; neither changes the claim.

Claude review lane (Fable 5.1; directed by Santiago Armstrong), 2026-10-31
