# Side-lane viewpoint referee sheet

This sheet gives one line per viewpoint in main's `VIEWPOINT_MAP.md`. Each line records a verdict, where the unresolved difficulty lands, and the closest literature. It is external input to main, not an instruction.

**Verdicts:**

- *promising:* the viewpoint gives a checkable gain;
- *relocates:* the same obstacle reappears; the sheet says where;
- *equivalent:* a restatement with no new estimate;
- *known dead end:* published, with a known reason it stalled.

**Pinned against:** main `77ce821` / `bff8938` (survey V001). The probe checks are in `probes/viewpoint_v001_check.py`.

## Verdicts on V1–V10

| View | Verdict | Where the difficulty lands | Closest literature |
|---|---|---|---|
| V1 parity coding | relocates (known) | Which infinite parity codes come from positive integers | Lagarias 1985 and Bernstein–Lagarias 1996 (the 2-adic conjugacy and the periodicity conjecture) |
| V2 mixed-place affine cocycles | relocates | A bound coupling real size with 2-adic legality; one shadow episode can raise height polynomially, so the coupling *is* the stopping problem | Tao §1.2 affine framework |
| V3 multiplicative semigroups | known dead end for the strong form | Lifting factor products to legal ordered paths; the multiplication bridge `x ↔ 5x` is unsupplied | Applegate–Lagarias, *The 3x+1 semigroup* (2006), which proves the weak form |
| V4 absorbing transfer operators | relocates | A uniform survival estimate for actual inputs, i.e. the exceptional set | Tao's Syracuse random variables |
| V5 orbit groupoids, currents, cohomology | equivalent (as is) | Needs an invariant beyond orbit components; R7 already gives exactly what currents detect | Repository R7/R40; Berg–Meinardus duality |
| V6 Dirichlet energy and potentials | promising as measurement, unproven | Quantitative control as domains grow, with escape flux. Its milestone (50% logarithmic absorption) is strictly weaker than Collatz and stronger than what is known | Doyle–Snell, Lyons–Peres (standard network theory) |
| V7 proof rewriting | tool only | Confluence of certificates says nothing about termination of the dynamics | — |
| V8 induced maps | relocates | Leaving a guard is not descent | Frozen R31, R67, R77 |
| V9 relational abstraction | relocates | A relation that survives composition across histories of unequal time, which is the pair-merger problem P(w) | Abstract interpretation (program analysis) |
| V10 rational denominator layers | control language | The property specific to the denominator-one layer, which is the transfer principle restated | Side-lane transfer note; Lagarias on 3x+d cycles |

**Where the difficulty lands, across all ten.** Every viewpoint sends it to one of two places:

- **(I) Integer realization.** Which 2-adic, rational or symbolic objects are actual positive-integer paths: V1, V2, V3, V8, V9, V10.
- **(II) Uniform control of the non-absorbed set:** V4 and V6, and routes S and C.

V5 and V7 are bookkeeping. Under main's own rule ("expand the search when candidates merely relocate the same obstacle"), this suggests the next survey should look for languages that act on (I) and (II) *together*, rather than more lenses on one of them.

**Probe checks (independent).** All pass:

- **Lifting probe.** The `(1,4)` composite `(9x+5)/32` holds exactly on `x ≡ 3 (mod 64)` (1,563 starts below `10⁵`). The point `x = 35` has word `(1,5)`. The reversed composite is `(9x+19)/32`. The `3x+5` control cycle `(27x+95)/32` fixes 19, and for general `d` its fixed point is `19d/5`.
- **Applegate–Lagarias row `7 (mod 64)`.** `C⁶(5x) = (45x+5)/64 < x` holds for 2,000 members.
- **Potential probe.** `u(3) = u(5) = 1/(1+5T)`, with `T ≈ 0.10205` and `u ≈ 0.66214`, within `[9/14, 13/18]`.

## V11 (side lane) — a zero–one law in density language

**Status: proposed viewpoint.** It depends on C.1a. Main's formal replay at `5a11fcb` reports only the standard axioms. A second, Linux replay is pending (draft PR #2).

1. **Objects.** The non-absorbed set `B`, meaning the integers whose orbit never reaches 1, together with natural and logarithmic densities of invariant sets.
2. **Structural gain: a dichotomy.** If `B` is nonempty, it contains some `a` with `3 ∤ a`. All predecessors of `a` lie in `B`, and by C.1a they have positive lower density. So **`B` is either empty or has positive lower density**, and Collatz ⇔ `liminf B(X)/X = 0`.

   This explains why the density theorems (Terras, Korec, S.1, Tao) cannot finish the job. They control *other* sets, such as stopping or almost-bounded values, never `B` itself. For `B`, density control is all-or-nothing. Also, C.1a with `t = 1` already gives `B` upper density below 1.
3. **Translation.** The difficulty becomes: no positive-density invariant set is disjoint from the basin of 1. In ergodic language, `B` is a positive-density invariant set or nothing.
4. **Worked example.** For `3x + d`, the multiples of `d` form an invariant sublattice. Writing `x = dy` gives `S_d(dy) = d·S₁(y)` (checked for `d ∈ {5, 7, 13, 61}`, `y < 10⁴`). So it is an exact copy of ordinary Collatz that never reaches 1, and `B_d` has positive density.
5. **Controls.** The dichotomy holds for every `d`, because C.1a carries over. What singles out `d = 1` is only that `B` has density zero. The `d·Z` copy shows exactly why that fails for `d > 1`.
6. **Next test (cheapest).** Find the quantitative form of Tao's estimate for `P(Col_min(N) ≥ x)` at fixed `x` (corrected v7), and whether its constants are effective. Combined with verification below `2⁶⁸`, that would give an explicit upper bound on `B`'s logarithmic density. Then compare it with the tower constants of C.1a.
7. **Intermediate milestone.** An explicit bound `B` log-density `≤ ε` for a stated small `ε`. This is strictly weaker than Collatz, and it would be a concrete version of V6's 50% target. By the dichotomy, any `ε` below the smallest `c(a)` over `a ∈ B` would finish the job, but `c(a)` is tower-small.
