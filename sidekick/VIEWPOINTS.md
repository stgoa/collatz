# Side-lane viewpoint referee sheet

This sheet gives one line per viewpoint in main's `VIEWPOINT_MAP.md`. Each line records a verdict, where the unresolved difficulty lands, and the closest literature. It is external input to main, not an instruction.

**Verdicts:**

- *promising:* the viewpoint gives a checkable gain;
- *relocates:* the same obstacle reappears; the sheet says where;
- *equivalent:* a restatement with no new estimate;
- *known dead end:* published, with a known reason it stalled.

**Pinned against:** main `77ce821` / `bff8938` (survey V001) and `cdfb143` / `c47d91b` (V002). The probe checks are in `probes/viewpoint_v001_check.py` and `probes/v13_coloring_check.py`.

## Verdicts on V1–V10

| View | Verdict | Where the difficulty lands | Closest literature |
|---|---|---|---|
| V1 parity coding | relocates (known) | Which infinite parity codes come from positive integers | Lagarias 1985 and Bernstein–Lagarias 1996 (the 2-adic conjugacy and the periodicity conjecture) |
| V2 mixed-place affine cocycles | relocates | A bound coupling real size with 2-adic legality; one shadow episode can raise height polynomially, so the coupling *is* the stopping problem | Tao §1.2 affine framework |
| V3 multiplicative semigroups | relocates; the relaxation is already solved | Lifting factor products to legal ordered paths; the bridge `x ↔ 5x` is unsupplied. (Wording corrected after main's review: this is not an impossibility claim.) | Applegate–Lagarias, *The 3x+1 semigroup* (2006), which proves the weak form |
| V4 absorbing transfer operators | relocates | A uniform survival estimate for actual inputs, i.e. the exceptional set | Tao's Syracuse random variables |
| V5 orbit groupoids, currents, cohomology | equivalent (as is) | Needs an invariant beyond orbit components; R7 already gives exactly what currents detect | Repository R7/R40; Berg–Meinardus duality |
| V6 Dirichlet energy and potentials | promising as measurement, unproven | Quantitative control as domains grow, with escape flux. Its milestone (50% logarithmic absorption) is strictly weaker than Collatz and stronger than what is known | Doyle–Snell, Lyons–Peres (standard network theory) |
| V7 proof rewriting | tool only | Confluence of certificates says nothing about termination of the dynamics | — |
| V8 induced maps | relocates | Leaving a guard is not descent | Frozen R31, R67, R77 |
| V9 relational abstraction | relocates | A relation that survives composition across histories of unequal time, which is the pair-merger problem P(w) | Abstract interpretation (program analysis) |
| V10 rational denominator layers | control language | The property specific to the denominator-one layer, which is the transfer principle restated | Side-lane transfer note; Lagarias on 3x+d cycles |
| V11 occupation measures | relocates | Tightness uniform in the range of seeds, which is (II) | Krylov–Bogolyubov style; Tao |
| V12 information of actual integer ensembles | relocates | A quantitative first-passage law with integer endpoints, which is (II) | Tao's Syracuse random variables |
| **V13 arithmetic regularity of invariant colorings** | **promising** (V003: digit-count rigidity confirmed) | Closure of the mixed ternary sections for 2-automatic invariant colorings; an actual bad set need not be regular | Cobham 1969; Shallit–Wilson and Stérin (regular ancestor languages for a fixed number of odd steps) |
| V14 binary/ternary carry diagrams | relocates (main closed it in V003: no new relation) | A growing frontier, finite support and a nonlocal bootstrap | Collatz as a quasi-cellular automaton (Cloney–Goles–Vichniac 1987) |

**Where the difficulty lands, across all ten.** Every viewpoint sends it to one of two places:

- **(I) Integer realization.** Which 2-adic, rational or symbolic objects are actual positive-integer paths: V1, V2, V3, V8, V9, V10.
- **(II) Uniform control of the non-absorbed set:** V4 and V6, and routes S and C.

V5 and V7 are bookkeeping. Under main's own rule ("expand the search when candidates merely relocate the same obstacle"), this suggests the next survey should look for languages that act on (I) and (II) *together*, rather than more lenses on one of them.

**Probe checks (independent).** All pass:

- **Lifting probe.** The `(1,4)` composite `(9x+5)/32` holds exactly on `x ≡ 3 (mod 64)` (1,563 starts below `10⁵`). The point `x = 35` has word `(1,5)`. The reversed composite is `(9x+19)/32`. The `3x+5` control cycle `(27x+95)/32` fixes 19, and for general `d` its fixed point is `19d/5`.
- **Applegate–Lagarias row `7 (mod 64)`.** `C⁶(5x) = (45x+5)/64 < x` holds for 2,000 members.
- **Potential probe.** `u(3) = u(5) = 1/(1+5T)`, with `T ≈ 0.10205` and `u ≈ 0.66214`, within `[9/14, 13/18]`.

## S1 (side lane) — an empty-or-positive density dichotomy (formerly labelled V11 here; renamed to avoid main's V11)

**Status: retained by main under historical C.2a, not adopted as a new language (`cdfb143`). The side lane accepts the following corrections:**

- the result is a dichotomy, "empty or positive lower density", not literally zero–one;
- `c(a) = 1/(a⁴L)` depends on the target and has infimum 0 over an unbounded bad set, so no single density threshold works, and a contradiction must compare at a particular target;
- Tao v7 Theorem 3.1 gives `C/(log V)^c` with unspecified constants, which settles the "next test" below in the negative for explicit bounds.

It depends on C.1a. Main's formal replay at `5a11fcb` reports only the standard axioms; a second, Linux replay is pending (draft PR #2).

1. **Objects.** The non-absorbed set `B`, meaning the integers whose orbit never reaches 1, together with natural and logarithmic densities of invariant sets.
2. **Structural gain: a dichotomy.** If `B` is nonempty, it contains some `a` with `3 ∤ a`. All predecessors of `a` lie in `B`, and by C.1a they have positive lower density. So **`B` is either empty or has positive lower density**, and Collatz ⇔ `liminf B(X)/X = 0`.

   This explains why the density theorems (Terras, Korec, S.1, Tao) cannot finish the job. They control *other* sets, such as stopping or almost-bounded values, never `B` itself. For `B`, density control is all-or-nothing. Also, C.1a with `t = 1` already gives `B` upper density below 1.
3. **Translation.** The difficulty becomes: no positive-density invariant set is disjoint from the basin of 1. In ergodic language, `B` is a positive-density invariant set or nothing.
4. **Worked example.** For `3x + d`, the multiples of `d` form an invariant sublattice. Writing `x = dy` gives `S_d(dy) = d·S₁(y)` (checked for `d ∈ {5, 7, 13, 61}`, `y < 10⁴`). So it is an exact copy of ordinary Collatz that never reaches 1, and `B_d` has positive density.
5. **Controls.** The dichotomy holds for every `d`, because C.1a carries over. What singles out `d = 1` is only that `B` has density zero. The `d·Z` copy shows exactly why that fails for `d > 1`.
6. **Next test (cheapest).** Find the quantitative form of Tao's estimate for `P(Col_min(N) ≥ x)` at fixed `x` (corrected v7), and whether its constants are effective. Combined with verification below `2⁶⁸`, that would give an explicit upper bound on `B`'s logarithmic density. Then compare it with the tower constants of C.1a.
7. **Intermediate milestone.** An explicit bound `B` log-density `≤ ε` for a stated small `ε`. This is strictly weaker than Collatz, and it would be a concrete version of V6's 50% target. By the dichotomy, any `ε` below the smallest `c(a)` over `a ∈ B` would finish the job, but `c(a)` is tower-small.

## V13 referee note (18:24)

**Classification confirmed with this branch's own code.** For each modulus `M ≤ 400` and each `d ∈ {1, 5, 7, 11, 13, 61}`, I built the residue graph mod `M`, with edges `r – 2r` and, on odd residues, `r – 3r + d`. That is 2,400 cases. In every case its number of components equals the number of `⟨×2, ×3⟩`-orbits on `Z/gZ`, where `g = gcd(M, d)`. For `d = 1` it is always 1. The controls `1_(5|n)` and `1_(61|n)` are invariant, and the commutator is a shift by `d`.

This is the first statement in the search whose rigidity at `d = 1` fails exactly for `d > 1`: periodic invariant colorings are constant precisely when `g = 1`. It is elementary, and it does not carry over to `3x + d`.

**Remarks for the milestone (classifying the 2-automatic invariant colorings).**

1. **Small automata are already excluded.** Every `n < 2⁶⁸` reaches 1 (Barina's verification). A `k`-state recognizer of a nonempty colour class accepts a word of length below `k`. So any nonconstant 2-automatic invariant coloring needs at least 70 states, and the milestone's content lies in large automata.
2. **Invariance is decidable for each automaton.** `n ↦ 3n + 1` is a finite transducer on binary strings, so invariance is decidable for a given automaton. The classification asks whether binary strings admit a finite invariant partition under that transducer, which is a natural question about automata.

## S2 (side lane, 19:13) — ×2×3 rigidity: a theoretical home for V13

**Status: proposed viewpoint.** It is literature-anchored and nothing new is proved here. It is offered because none of main's 14 cards covers it, and it frames V13.

1. **Objects.** Closed and Borel subsets of the profinite integers `Ẑ` (or of `Z₂ × Z₃`), and measures on them, that are invariant under the affine semigroup generated by `x ↦ 2x` and, on odd `x`, `x ↦ 3x + 1`, together with the inverse branches. An invariant coloring of `N` that is periodic corresponds to a *clopen* invariant set.
2. **Structural gain.** V13's results become instances of a well-studied rigidity theme for the multiplicatively independent pair `2` and `3`:
   - Furstenberg (1967): a closed subset of the circle invariant under `×2` and `×3` is finite or everything. Rudolph (1990) proves measure rigidity under positive entropy.
   - Cobham's theorem (1969), which V13 already uses, is the automata analogue: a sequence that is both 2-automatic and 3-automatic is periodic.
   - V13's periodic classification, that no nonconstant clopen invariant set exists when `d = 1`, is the profinite clopen case.
   - The `+1` is what turns the linear `×2×3` action into an affine one; V13's commutator shift `A∘B − B∘A = d` is exactly this twist.
3. **Translation.** Rigidity theorems control closed sets and measures. The bad set `B` is a discrete subset of `N`, and its closure in `Ẑ` can be all of `Ẑ` while `B` itself stays thin. So the difficulty lands at passing from statements about closures or limits to statements about `B`, which is (I) and (II) again, now in a well-mapped theory.
4. **Worked example (control).** For `d = 5`, the clopen set `5Ẑ` is invariant under `x ↦ 2x`, `x ↦ 3x` and `x ↦ 3x + 5`. That is a nontrivial closed invariant set, exactly the sublattice copy noted in the 18:09 entry. For `d = 1`, V13 shows no nontrivial clopen one exists (checked here for `M ≤ 400`).
5. **Controls.** Rigidity can only distinguish `d = 1` through the affine constant. Every `3x + d` with `d > 1` has the invariant clopen set `dẐ`.
6. **Next test (cheapest).** A literature check, followed by one finite question:
   - **Literature:** affine-semigroup versions of Furstenberg's theorem on `Ẑ` or on solenoids, and whether the Collatz affine pair appears there.
   - **Finite question:** is every nonempty `B`, being closed under the forward map and all inverse branches, dense in `Ẑ`, that is, does it meet every residue class mod every `M`? Residue-level closure needs the parity and mod-3 data of members, so work modulo `6M`; this is a bounded computation plus a V13-style argument.
7. **Intermediate milestone.** "Every nonempty union of orbit components meets every residue class modulo every `M`." That is strictly weaker than Collatz and stronger than V13's periodic classification, which only says a nonempty `B` cannot *equal* a periodic set. It would rule out every congruence-based isolation of a counterexample.

