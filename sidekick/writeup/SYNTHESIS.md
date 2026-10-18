# The W5 reduction of the Collatz conjecture: a verified map

*This is a consolidated survey of the main programme (results R1–R92 and C1–C5 on `main`, through commit `61fd041`) and the independent side lane (`claude/sidekick`), as of 2026-10-18.*

Status labels follow the repository:

- **written proof**: a proof is written out in the repository.
- **finite check**: an exact computation over a stated finite range.
- **measurement**: sampled statistics, not a check.
- **heuristic**: a model argument.

No novelty claims are made. The side lane's contributions are independent checks, reformulations and measurements of the main programme.

---

## Summary

1. **One family of obligations.** Main reduces the Collatz conjecture to a single family of obligations: for every `w ≡ 5 (mod 8)`, a finite signed integer current exists whose divergence is `P(w) = [3w] − [w]` (written proof, R37–R40). Writing `w = 4u + 1`, this says: for every odd `u`, the orbits of `u` and `18u + 5` meet.
2. **Conditional rules.** Main then builds rules that reduce each `P(w)` to obligations of strictly smaller critical-image rank `ρ(w) = ν(3w)`, or of a second rank `σ` (R51). Seventeen families were in place by commit `793e835`. The twelve-family dispatcher accepts about 70% of sampled W5 inputs at every tested size from 10 to 64 bits (measurement).
3. **Scoped no-go theorems.** These explain why no fixed procedure finishes the job. Whole arithmetic progressions carry arbitrarily long growing prefixes (R54, R61 and others). The side lane identifies these as 2-adic shadows of the negative cycles through −1, −5 and −17, and more generally of negative rational cycles.
4. **The core equivalence.** A complete strict-ρ recursion is equivalent to a quotient stopping-time statement: the orbit of every `ν(3w)` drops below `(8ν(3w) − 5)/9`. That statement is equivalent to Collatz (written proof from R43, R51 and R62; confirmed in main's review of `33c3829`).
5. **Transfer.** Every local identity carries over verbatim to `3x + d` with `gcd(d, 6) = 1`, via `x ↦ x/d`. Arguments built only from such identities therefore cannot tell `d = 1` from other `d`, except through which classes hold the base and the cycles. A proof needs some input that does not transfer, such as exact integrality of whole valuation words. Main's R71 shows this input is effective at any height for mechanical words. This is where the literature also puts the remaining difficulty: the step from "almost all" orbits to "all" orbits (Tao 2019), and Diophantine bounds for cycles.

---

## 1. Setting and notation

- **The map.** `S(x) = (3x + 1)/2^v2(3x + 1)` is the odd-only Syracuse map on positive odd integers. The point 1 is absorbing: currents use killed atoms, with `[1] = 0`.
- **Currents.** A current is a finite integer combination of rows `e_x`, with `div e_x = [x] − [S(x)]`.
- **Elementary normal form `ν`.** Repeatedly apply `F⁻¹(x) = (x − 1)/4` when `x ≡ 5 (mod 8)`, and halve selected climbers. A climber is `x = 2^a t − 1` with `a ≥ 2` and `t` odd. It is selected when `t ≡ 3^a (mod 4)`, in which case `S^a(x) = S^a((x − 1)/2)` (R23). Each step has an exact finite current (R25).
- **Quotient map and canonical states.** `T = ν ∘ S` acts on canonical states, those with `ν(x) = x`. `quotient_bridge(q)` is the exact current with divergence `[q] − [T(q)]`.
- **Pair obligations.** `P(w) = [3w] − [w]`, on `W5 = {w ≡ 5 (mod 8)}` and `W9 = {w ≡ 9 (mod 16)}`.
- **Ranks.** The critical-image rank is `ρ(w) = ν(3w)` (R43). The σ rank of R51 is `σ(w) = 4w/3 − 1` on the returning class `E_ret = {w ∈ W5 : w ≡ 3 (mod 9), 3w selected}`, and `σ(w) = ρ(w)` elsewhere. On `E_ret`, `ρ = (9σ + 5)/8` (R62). Main's documents also use `E` for the larger class `{w ∈ W5 : 3 ∣ w, 3w selected}`, so this survey writes `E_ret`.
- **Formal absorption plan.** `H_s` is deterministic and satisfies `[s] = div H_s + Σ_u h_s(u) P(u)`, with signed requests `u ∈ W5`. Its rank bounds are:
  - `ρ(u) ≤ (9ν(s) + 5)/8` (R43);
  - `σ(u) ≤ ν(s)` (R51);
  - `ρ(u) ≤ ν(s)`, except on one explicit class where a single request with coefficient `+1` sits at `(9ν(s) + 5)/8` (R58).

## 2. The reduction chain

The programme reaches its final obligation through four layers. Each arrow below is a written equivalence unless marked otherwise.

**Packet layer (R1–R13).**

- **R3.** Collatz ⇔ bounded work at every cutoff ⇔ every right-aligned packet `Π^R_N` has an exact finite current ⇔ every `Π^R_N` has a current with nonpositive residual.
- **R5.** Five dyadic rays suffice: `N = a·2^b` with `a ∈ {12, 14, 16, 18, 21}`.
- **R6.** `Π^R_(64N) = Π^R_N + A_N`, so it is enough to treat the annular increments on 30 sequences.
- **R7.** An exact current exists iff every nonabsorbing orbit component has mass 0.
- **C5 (side lane).** The obligation splits exactly into "no nontrivial cycles" and "no divergent orbits", each at full strength.

**Absorption layer (R14–R24).**

- **R17.** Given absorption of the inner shell, the retained graph absorbs 47/72 of the outer shell.
- **R23.** The halving identity `S^a(x) = S^a((x − 1)/2)` holds for selected climbers. Together with R17 it certifies about 119/144 of the shell.
- **R24 (conditional sufficiency).** A rule for the complementary roots on the five rays would give Collatz by induction from a checked base.

**Quotient and pair layer (R25–R36).**

- **R25.** The elementary bridge classes are exactly `{F^k(q), F^k(2q + 1)}`, with `F(x) = 4x + 1`. The quotient `T = ν∘S` satisfies `T^n ν = ν S^n`. Collatz ⇔ `T` terminates from every canonical seed.
- **R26.** Complete run bridges.
- **R27.** Each fibre `{ν(x) ≤ N}` has `N/4 + O(log N)` members in every band `[X, 2X)`.
- **R28.** Exact undecided-cylinder rates: `ρ ≈ 0.9465046` per odd step and `β ≈ 0.9659066` per bit. The side lane contributed to this result.
- **R35.** Pair decomposition: universal doubling pairs ⇔ Collatz.

**Critical W5 layer (R37–R40).**

- **R37.** On `W = W5 ∪ W9`, the map `w ↦ ν(3w)` is a bijection onto the complementary canonical `q ≢ 2 (mod 3)`. Collatz ⇔ universal finite currents for `P` on `W`.
- **R40.** Every `P(w)` with `w ∈ W9` is eliminated by an explicit terminating compiler whose requests lie in W5. Hence:

> **Collatz ⇔ for every `w ≡ 5 (mod 8)`, `P(w) = [3w] − [w]` has a finite exact current.**

Historically the layers connect through R23's complementary roots, then R26, then R35's pair decomposition, then R37.

**Restatement (side lane).** Take `w = 4u + 1 ∈ W5`. Then `S(w) = S(u)`, and `S(3w) = 18u + 5` with valuation 1. A finite current for `P(w)` exists exactly when the orbits of `3w` and `w` meet. If they meet, the difference of the two prefixes is such a current. Conversely, divergence sums to zero on every weak component that avoids 1. With R40, this gives:

> **Collatz ⇔ for every odd `u`, the orbits of `u` and `18u + 5` meet.**

## 3. Ranks, rules and the induction

**The induction (R43).** Take `ρ(w) = ν(3w)`.

- Any finite signed rule whose requests all have strictly smaller `ρ` composes by strong induction.
- So it suffices to supply currents on `W5 \ A`, where `A` is the domain of any finite union of such rules applied in a fixed priority.
- Requests in `H_s` satisfy `ρ ≤ (9ν(s) + 5)/8`.

**Rank refinements.**

- **R51.** A separate rank `σ`, with `σ ≤ ν(s)` on all `H_s` requests. It cannot be mixed with `ρ` automatically.
- **R58.** An exact classification of when `H_s` requests a rank above `ν(s)`: a single request, with coefficient `+1`, on one explicit class.
- **R62.** σ/ρ compatibility. For a nonreturning parent, the bad requests of a σ-plan are exactly the returning `u` with `⌈(8ρ(w) − 5)/9⌉ ≤ σ(u) < ρ(w)`.

**The seventeen strict-ρ families**, in dispatcher priority order:

| result | mechanism | domain or test |
|---|---|---|
| R41 | inverse phase: ancestor `p = 2^h(2q + 1)/3^h − 1` via `1^(h−1),2` | `E_good`: `3 ∣ w`, `3w` selected, `w ≢ 3 (mod 9)` |
| R45 | base inverse phases, `k ∈ {4, 8}` | `w ≡ 20 (mod 27)` or `w ≡ 91 (mod 243)` |
| R44 | returning forward interface | `a = 3, 4` subdomains |
| R46 | variable-depth inverse escape | selected roots with `j ≥ 2` (so `w ≡ 1 mod 3`) |
| R47 | inverse interface for nonselected multiples of 3 | endpoint test, which forces `j ≥ 4` |
| R48 | complete forward blocks, accepted when `B(ν(f)) < q` | exact `a = 3, 4` tables |
| R50 | two inverse phases across an intermediate increase | `h + L ≥ 5` (k = 4) or `h + L ≥ 6` (k = 8) |
| R52 | second forward block for returning inputs | CRT families that R44 misses |
| R53 | low (2,2) blocks through prescribed growth, `G(x) = (9x + 5)/8` | for every `r`, a decreasing CRT exit |
| R55 | selected forward tables | exact for `A = 2, 3, 4`, plus second blocks |
| R56 | two selected inverse words | `w ≡ 718 (mod 729)` or `w ≡ 4255 (mod 6561)` |
| R57 | guarded −17 cycles and all their exits | for every `r`, a decreasing progression exiting at `e = 12` |
| R58 | exact absorption bound | e.g. `w ≡ 4021 (mod 294912)` |
| R59 | deferred original-rank test | `w = 245 + 1024n`; `w = 1301 + 32768l` (with a selection condition) |
| R60 | maximal inverse-cycle continuation | complete descent table in `(k, j)` |
| R62 | defect resolution | e.g. `w = 53173 + 65536k` |
| R64 | lifted inverse ray, rotated −17 cycle | whole subrows of R61's families |

**How the dispatcher grew.**

| stage | rules | families |
|---|---|---|
| original | R41, R45, R44, R46 | 4 |
| expanded | + R47, R48, R50 | 7 |
| continued | + R52, R53 | 9 |
| selected | + R55, R56, R57 | 12 |
| refined | + R58, R59, R60 | 15 |
| resolved | + R62, R64 | 17 |

The σ rules are not imported. The inner resolvers are frozen: R59 uses the twelve-family dispatcher and R62 the fifteen-family one.

**Finite window, `w < 8192` (main's counts).** Of the 1024 W5 inputs:

- the nine-family dispatcher accepts 493;
- the twelve-family dispatcher accepts 722;
- the fifteen-family dispatcher accepts 747, leaving 277 unresolved (for example `P(21) ↦ {21: 1}`).

**One rank for both rule collections (R75).** Keep the source basis `W = W5 ∪ W9`. The returning conversion `P(u) = div C_u + P(b) + Σ(Â_b − Â_u)P`, with `b = σ(u)/3 ∈ W9`, then turns every σ-valid W5 plan into a ρ-valid plan in `W`. Old ρ plans stay valid, so both collections run under one strict rank after translation. The remaining W9 obstruction is a positive self-request on the blocked row.

**A smaller-origin history (R80).** On a whole blocked-W9 cylinder, `q = 11547 + 2¹⁷·3^D·t`, the target `q` has no smaller canonical ancestor through depth `D`. The anchor `t = 0` has none at any depth. Yet the smaller seed `p = 11391 + 2³⁶·3^(D−12)·t` meets `q`'s future above `q`: `S²(q) = S¹⁴(p) = (9q + 5)/8`. This gives a strict original-rank comparison without inverse descent. It is main's current constructive priority.

**A normal-form tool (R73).** Two exact pair identities, `w ≡ 93 (mod 512) ↦ (9w − 5)/64` and `b ≡ 1285 (mod 2048) ↦ 9(b − 5)/256`, generate a terminating, idempotent, integer-linear normal form for signed request vectors. Its kernel is exactly the relation module of the two identities. On R69's reset family it removes both helper premises, leaving the smaller `P(u)`.

The side lane's size-stable rates are in §5.

## 4. Scoped obstructions

Every no-go result in the programme is **scoped**: it excludes a specified procedure, not other comparisons. R54's scope sentence is typical:

> "This rules out a fixed lookahead guarantee for the stated procedure; it does not rule out another current representation, a supplied-history argument, input-dependent unbounded depth, or another comparison, and gives no forever-growing positive orbit."

**Packet and annulus layer.**

- **R7.** No uniformly bounded per-packet catalogue works.
- **R13, R16, R22.** Exposure depth is unbounded, even at fixed ternary order 2. On the ladder, `d_*(96·64^k) ≥ v₃(k + 2) + 4`.
- **R19.** The bound `2h + 1` is refuted.
- **R31.** No height potential with finitely many labels decreases at every return.
- **R35, R38, R39.** Each of these excludes a specific catalogue or algorithm.

**W5 layer.**

| result | what it excludes |
|---|---|
| R41 | If `q ≡ 1 (mod 3^D)`, every T-predecessor within `D` steps exceeds `q` |
| R46 | Precision barriers for inverse escape |
| R49 | Inverse-only search as a complete method: `b = 39` and `b = 135` have no smaller canonical ancestor at any depth, yet descend in three forward arrows |
| R54 | Fixed lookahead: arbitrarily long growing prefixes on `w ≡ 3445 (mod 3456)` keep a unique unaccepted leading request at every lookahead |
| R61, R63 | Named continuations that return the original unfinished current exactly ("undo") |
| R65 | Progress by changing to the adjacent-source basis `D(q) = [q + 2] − [q]` |
| R66 | Full coverage by the named all-ray procedure: `accepted(N) ≤ S·N + O(T²)` with `S < 1/500` |
| R67 | Termination of mixed σ-then-ρ plans: accepted pairs chain into arbitrarily long growing blocks |
| R68 | Inverse ancestors crossing the native height (a separation result) |
| R69 | Any phase-dependent monomial "debt" potential: a reset family breaks decrease across mixed blocks |
| R70 | Finishing via the natural mixed exit: it can re-enter higher, `R(w) > w`, repeatably on complete cylinders |
| R71 | Integer cycles from mechanical words: every cycle state has reduced denominator `2^(A/g) − 3^(k/g)`, never 1 except for the all-2s word (published antecedents) |
| R72 | A finite affine-valuation rank on R69's two fixed mixed phases: infinitely many distinct centres defeat any finite centre list |
| R76 | A uniform fixed-word pair model on `w ≡ 40529845 (mod 2²⁶)`: two independent searches find no smaller affine partner with fixed words |
| R77 | Infinite survival in the V/R subsystem with low step-pattern complexity. A repeated factor forces both of its starting states into one 2-adic class, while growth is at most `Λ^j`. So any infinite survivor needs `liminf p(L)/L ≥ 18.285`. Also, no seed up to `2.6·10²⁶` makes 37 consecutive returns |
| R78, R79 | Finishing at the original rank via the native W9 continuation and the native return `U(b) = (729b + 223)/512`: exact return counts `⌊(v2(217b + 223) − 13)/9⌋`, and every longer chain keeps a higher leading request |
| R74 | Finite integrality alone: every finite word in the mixed exit-18 returns `V`, `R` is realized by integers on a complete cylinder. Eventually periodic words have negative rational points, so they are never positive integers. Aperiodic survivors remain open; their density is zero, with explicit count bounds |

**Interpretation (side lane, 23:32).** On negative odd integers, `T` has exactly three cycles with `|x| ≤ 4000`:

- `{−1}`, with return map `3/2`;
- `{−5, −7}`, with return map `9/8` (R53's `G(x) + 5 = (9/8)(x + 5)`);
- `{−17, −25, −37, −55, −21, −31, −23}`, with return map `3⁷/2¹¹` (R54's `Ψ(q) + 17 = (2187/2048)(q + 17)`).

Positive integers that are 2-adically close to these points follow them, and keep growing, for a number of steps proportional to the 2-adic agreement. Every periodic valuation word with `3^k > 2^m` has a negative rational 2-adic fixed point, and these points are dense in `Z_2`. So every residue class contains inputs that defeat any fixed lookahead. Running backward around the cycle gives the smaller ancestor `p = (2048q − 2363)/2187` whenever `q ≡ −17 (mod 3⁷)`. This coincides with R56's k4 domain `w ≡ 718 (mod 729)` (main's review of `bae3969`).

## 5. Measurements of the rule programme (side lane)

All rows below are measurements, not checks. Main notes that "size-stable" is not established beyond the sampled sizes.

| dispatcher (main commit) | one-step acceptance on W5, 10–64 bits |
|---|---|
| four rules R41/R44/R45/R46 (`a06ef3c`) | ~18%, size-stable |
| seven rules (`bcde58e`) | ~43%, size-stable |
| twelve rules (`7206f9c`) | ~70%, size-stable |

**Full signed closure of the fifteen-family dispatcher (`d265d94`).**

- Root accepted: 62–76%.
- Complete closures, with no remaining leaf: ~5.5% at every size from 24 to 64 bits. These are large trees, expanding 41–149 nodes at 64 bits, so the completions are structural.
- Every other closure keeps a leaf a median of 1.3–2.1 bits below `ρ(w)`.
- At modulus 576, no W5 class closes more than 31% of the time.

**Plain quotient-prefix plans.** Share of inputs needing lookahead at most `n`:

| n ≤ | 2 | 4 | 8 | 16 | 32 |
|---|---:|---:|---:|---:|---:|
| share | 13% | 49% | 76% | 92% | 98.7% |

The largest lookahead observed was 79. These shares are about the same in every class, including the selected classes that were hardest for the hand-built rules.

**Repeated-factor spacing for every orbit (side lane; written argument, reviewed by main).** R77's mechanism applies to any non-repeating odd-only orbit: `e + 1 < j·log₂(3/2) + log₂(x₀ + 1)` whenever a valuation factor of total `e` recurs at position `j`. Hence a divergent itinerary has `liminf p(L)/L ≥ 1/log₂(3/2) ≈ 1.7095`. This excludes Sturmian and other low-complexity itineraries, but not general ones.

**States with no smaller ancestor (exact census, R49's criterion).** Of the 499,998 canonical states below `2·10⁶`, 48.5% have no smaller canonical ancestor at any depth. The share is flat from `10³` up. By `q mod 3` it is 88.5% (for 0), 57.0% (for 1) and 0% (for 2). Every certificate for these states needs forward motion.

## 6. The core equivalence

**Theorem (side lane, written proof from main's R43, R51 and R62; reviewed in `side_lane_review_33c3829.md`).** Let `w ∈ W5`, `q = ν(3w) = ρ(w)` and `z = ν(w)`. Suppose some quotient prefix reaches `x = T^n(q)` with `9x + 5 < 8q`. Then

```
J = N_3w + Σ_{i<n} quotient_bridge(T^i q) + H_x − N_w − H_z
```

has divergence `P(w) − Σ_u (h_x(u) − h_z(u)) P(u)`, and every request satisfies `ρ(u) < ρ(w)`.

*Proof.* Requests of `H_x` have `σ(u) ≤ x` (R51). Hence `ρ(u) ≤ (9x + 5)/8 < q`, by R62's identity on `E_ret` and since `ρ = σ` off `E_ret`. Requests of `H_z` have `ρ(u) ≤ (9z + 5)/8` (R43), with `z ≤ (w − 1)/4` and `q > w`. ∎

**Corollary.** By strong induction on `ρ`, and then R40:

> Collatz ⇔ for every `w ∈ W5`, the quotient orbit of `ν(3w)` reaches a state below `(8ν(3w) − 5)/9`.

**What the corollary says about the programme.**

- **Rules as groupings.** The forward rule families act as CRT groupings of these certificates, and the inverse rules add thin progressions.
- **What a complete recursion must prove.** A recursion that is complete under strict ρ has to establish the stopping-time statement, uniformly.
- **What it does not say.** Main's review stresses this: the equivalence does not force every useful construction to follow this particular prefix.

**Validation.**

- Main's ρ validator accepts all 3,600 sampled plans (`sidekick/probes/rho_prefix_plans.py`).
- R62's compatibility theorem holds on 3,000 σ-plans. 99.8% of them are already strictly ρ-decreasing (`r62_compatibility_check.py`).

## 7. Controls and transfer

**Negative controls (PR1, merged).**

- The maps `T_d(x) = (3x + d)/2^v2(3x + d)` reproduce main's local machinery.
- `T_61` is locally Collatz-like, yet its primary obligation fails at `N = 213`, by a finite certificate. So no argument that applies verbatim to `T_61` can prove the primary obligation for `d = 1` (`negative_controls/NOTE.md`, §3).
- The broader claim that alternative minimum-cost certificates cannot help was withdrawn. Main's `PR1_REVIEW.md` gives counterexamples.

**Transfer (side lane, written proof plus checks).**

- For odd `d`, `T_d(d·y) = d·T_1(y)` on 2-adic integers. So 3x+d on the integers is 3x+1 on rationals with denominator `d`.
- Every valuation identity, normal-form step, halving bridge and cycle word carries over with `x` replaced by `x/d`. Checked for `d ∈ {1, 5, 7, 13, 61}`: the halving bridge, and R54's family `n₀ = 81·2^(11r+6)s − 17d`.
- Consequently, a whole-type theorem built only from such identities and rank comparisons also holds for every 3x+d with `gcd(d, 6) = 1`.
- Exact integrality of states does not transfer, because integers for `S_d` correspond to rationals in `d⁻¹Z`. It can therefore separate values of `d` at any height. Main's R71 is an example: every state of a mechanical word's cycle has reduced denominator `2^(A₀) − 3^(k₀)`.

**Rational cycles (side lane, finite check).** Every periodic word with `2^m > 3^k` gives a positive rational cycle of 3x+1, at `x = B_W/(2^m − 3^k)`.

- There are 3,889 primitive cycles with `k ≤ 9`, and the only integral one is `{1}`.
- They reproduce known integer cycles of 3x+d:

  | map | cycle minima |
  |---|---|
  | 3x+5 | 1, 19, 23 |
  | 3x+7 | 5 |
  | 3x+13 | 1, 211, 227, 251, 259, 283, 287, 319 |

These are control points for any whole-type claim (`sidekick/frameworks/rational_cycles.py`).

**The two halves.**

- **No nontrivial cycles** depends on `d`. It is decided by integrality: Baker-type bounds on `|2^m − 3^k|` combined with computation.
- **No divergence** is, by transfer, the `d = 1` slice of Lagarias's periodicity conjecture: no rational with an odd denominator has a divergent orbit.

Integrality does bound how long an integer can follow a contracting positive rational cycle, since `|x − c| ≥ 1/d`. It gives nothing against following expanding negative cycles, and those are what drive growth (`sidekick/frameworks/MEMO.md`).

## 8. Position in the literature

- **Stopping times.** Terras (1976) and Everett (1977) show that the set with finite stopping time has density 1. The residual at lookahead `L` in §5–§6 is a stopping-time residual of this kind.
- **Conjugacy and rational cycles.** Lagarias's 1985 survey describes the conjugacy of 3x+1 on `Z_2` to the shift and states the periodicity conjecture. Lagarias (1990) treats rational cycles. Bernstein (1994) and Bernstein–Lagarias (1996) study the 3x+1 conjugacy map. Section 7's transfer and catalogue are instances of this picture.
- **Functional equations and analytic structure.**
  - Berg–Meinardus (1994–95): Collatz as a functional equation for generating functions of invariant sequences. In one normalization (our derivation) the equation reads `f(z³) = f(z⁶) + (1/3z) Σ_k ω^(−2k) f(ω^k z²)`. Collatz is equivalent to its holomorphic solutions in the unit disk being only `c₀ + c₁ z/(1 − z)`, as summarized in Lagarias's annotated bibliography. This is the "dual obstruction space is trivial" formulation.
  - Bell–Lagarias (2015): inverse-orbit generating functions have the unit circle as a natural boundary for every `m` except possibly `1, 2, 4, 8`. Collatz is equivalent to their rationality at those `m`.
  - Siegel (2024): (p,q)-adic analysis recasts periodic points as values of `χ_H` at rational p-adic integers that are not nonnegative integers.
- **Almost all orbits.** Tao (2019/2022): almost all orbits, in logarithmic density, attain almost bounded values.
- **Cycles, predecessors and verification.**
  - Simons–de Weger (2005) and Hercher (2023): no m-cycles for small m.
  - Krasikov–Lagarias (2003): lower bounds on predecessor counts.
  - Barina (2021): convergence verified below `2⁶⁸`.
- **Limits.** Conway (1972): generalized Collatz problems are undecidable.

**Where the programme sits.** Its distinctive content is the exact signed-current reduction to W5 pair obligations, the two ranks, a large catalogue of explicit families with written proofs, and the scoped no-go theorems, all with executable certificates. The side lane adds three things:

- independent checks;
- the negative-cycle explanation of the obstructions;
- the stopping-time equivalence and transfer, which locate the remaining content at the same "all orbits" step the literature leaves open.

## 9. Outlook

**The open obligation (main's statement).** Supply finite exact currents for `P(w)` on all of `W5 \ A` within one coherent strict-ρ induction, or give a different noncircular argument. RESULTS.md records three equivalent re-encodings:

- the σ order together with R62;
- the adjacent-source basis (R65);
- the stopping threshold of §6.

**What the evidence supports.**

1. **Divergence half.** No local identity bounds arbitrarily long growing excursions (§4, §6, §7). A proof needs a uniform theorem of stopping-time type on the critical images `ν(3w)`. By transfer, that is the `d = 1` slice of Lagarias's periodicity conjecture. None of the known methods reaches "all orbits": Terras, Tao and analytic rigidity all stop short.
2. **Cycle half.** Integrality must enter here. The known tools are whole-word constraints such as R71 and bounds of Baker type. The W5 objects could host such arguments, but no step in that direction has been taken here yet.
3. **Standalone theorems worth stating (no novelty claims).**
   - The W5 equivalence, including its form `u ↔ 18u + 5`.
   - The exact cylinder rates of R28.
   - The infinite explicit families of R53 and R57, read through the −5 and −17 cycles.
   - The stopping-threshold equivalence of §6.
   - R49's all-depth inverse exclusions.

**Not established.** No result has human peer review or proof-assistant verification. Every written proof has been checked by its author's code, and many have also been checked independently by the side lane (Appendix A).

## Appendix A. Verification ledger

The appendix is pinned at side commit `7150f31` and main commit `ea3278e`. Times refer to `sidekick/FEED.md` entries, and probes live in `sidekick/probes/` unless noted. "PR1" means the merged negative-controls lane, `collatz_research_20261017/negative_controls/`.

### A.1 Main results and independent side-lane checks

| results | side-lane check | standing |
|---|---|---|
| R2–R6, R9, R10 | PR1 (C1, C4): Theorem 1 at `8 ≤ N ≤ 160` for all horizons, bounds for `N ≤ 10⁵`, dyadic table for `b ≤ 1500`, five rays for `3 ≤ b ≤ 400`, annular recursion on 68 cutoffs | independently checked (finite) |
| R13, R16, R22 | 19:03, 19:05, 19:13, 19:22, 19:44 (`depth_probe`, `release_families_check`, `delayed_release_check`, `chain_cancellation_scan`, `fixed_h_check`) | independently checked (finite) |
| R17, R20, R24 | 19:37–19:59 (`residual_vs_induction`, `r24_check`) | values and base checked; findings on R20's residual |
| R23, R26, R27 | 19:46, 20:23, 20:26 (`coalescence_check`, `fibre_count_check`, `run_bridge_check`); 01:04 (d-scaled halving) | independently checked |
| R28 | 20:22 reproduces `cylinder_audit.json`; the side lane's 19:48 entry anticipated the rate | reproduced |
| R30–R34, R36 | 20:44, 21:06 (`batch_64fff1d_check`, `batch_r33_r36_check`) | independently checked (R30 after main's clock correction; R33's 2M-sample rows not reproducible) |
| R35 | 21:09 (`pair_merge_controls`), generic-form control | controls only |
| R37–R39 | 21:31, 21:53 (`batch_436f51f_check`) | independently checked |
| R40, R43 | bound and planner checked at 21:53; used in the 00:53 proof | partially checked; compiler not rebuilt |
| R41, R46 | 21:53, 22:16 (`batch_r40_r41_check`, `batch_r43_r46_check`) plus meters | independently checked |
| R44, R45, R47, R48, R50, R52, R55, R59, R60 | coverage meters (22:21–00:22) | measured only |
| R51, R53, R54, R57 | 23:32, 23:45, 23:51 (`batch_r51_r54_check`, `batch_r53_check`, `batch_r57_check`, `negative_cycle_shadows`) | independently checked; R53 and R54 reinterpreted as −5 and −17 cycle shadows |
| R58, R62 | 00:16, 00:53 (`r58_excess_check`: 112,000 seeds; `r62_compatibility_check`), both against main's R43 implementation | checked (semi-independent) |
| R49 | 02:15 (`r49_ancestor_free`): both anchors, their three-arrow paths, and an exact census below `2·10⁶` | independently checked (finite) |
| R71 | 01:43 (`r71_mechanical_check`), 735 exact words | independently checked (finite) |
| R73, R74 | 02:19 (`batch_r73_r74_check`): 4,000 members of each pair identity (clocks), 600 random V/R words (domains, growth, negative periodic points) | independently checked (finite) |
| R75, R77 | 02:53 (`batch_r75_r77_check`): returning translation arithmetic (3,000 inputs); R77's growth bound, exact threshold, spacing lemma (2,188 repeats) and copy counts (200) | independently checked (finite) |
| R78, R79, R80 | 03:31 (`batch_r78_r80_check`): six-arrow native prefix (2,000), return counts (3,000), the R80 family (30 cases) and the all-depth anchor 11547 | independently checked (finite) |
| R56 | 04:30 (`r56_selected_inverse_check`): both inverse words, identity (2) and the thresholds `h ≥ 3` (k = 4) and `h ≥ 5` (k = 8) on 4,800 cases | independently checked (finite) |
| R88 | 05:52 (`r88_anchor_exhaustive.c`): the m = 0 anchor exclusion over all 33,426,246 canonical states below Q (exhaustive, in C); the 18-step comparison for 304 values of m | independently checked (anchor exhaustive; family finite) |
| R64 | 05:36 (`r64_lifted_cycle_check`): lifted-ray words and the full acceptance table at all 85 boundary cells (`k` up to 85) | independently checked (finite) |
| R86 | 05:13 (`r86_even_exit_check`): raw-target cone and exact inequality on 1,152 CRT cases | independently checked (finite) |
| R60 | 04:59 (`r60_cycle_inverse_check`): maximal cycle-inverse words, the exact height formula and the full acceptance table on all cells `k = 1..20`, `j = 0..4` | independently checked (finite) |
| R84, R85 | 04:36 (`batch_r84_r85_check`): R84's prefix and sharp 20-step descent; R85's clock barrier by brute force on 24 instances | independently checked (finite) |
| R81, R83 | 04:08 (`batch_r81_r83_check`): R80's merger cell (3,301 lifts), the cell theorem on 400 random anchor pairs with binary minimality (ternary minimality by coupled integrality, not executed), and R83's `(L, h)` | independently checked (finite) |
| R91, R92 | 06:34 and 07:02 (`c0_basin_classify.c`, `r92_inverse_tree_check`): R91's classification reproduced exactly; the full candidate interval of 176,754,119 origins, with the same 16 tails as R92; R92 confirmed at `ℓ = 0` (r = 0) and `ℓ = 398166` (r = 1) by inverse-tree search | independently checked (exhaustive finite certificate; two sources) |
| R25 (inverse table) | 07:02 (`r92_inverse_tree_check`): brute-force completeness for 750 targets below 3000 | independently checked (finite) |
| R90 | 06:27 (`r90_phi_return_check`): both twelve-arrow return words (2,000), `T¹²(3v) = 3Φ(v)` on the re-entry cylinder (500), re-entry counts (3,000) | independently checked (finite) |
| R61, R65, R66, R67 | 06:14 (`batch_r61_r67_check`): R61's exit and the `r ≥ 16` threshold (132), R65's triple bijection and arrows (10,000), R66's ternary identity (2,990), R67's count formula (3,000) | independently checked (finite) |
| R93, R94 (main working copy on `61fd041`) | 07:33 (`r93_r94_check`): R93's identities, the 53/7153 shadow certificate, departures for every exact order `n = 14..1000` plus 1,584 prescribed long branches, 209 joint upper/lower cases; R94's centers, shadow words and all 39 cylinders with 156 replayed pairs; later-target paths, ray cutoffs and endpoints | independently checked (finite; dispatcher claims not rebuilt) |
| R1, R7, R8, R11, R12, R14, R15, R18, R19, R21, R29, R42, R63, R68–R70, R72, R76, R82, R87, R89 | none | not touched |

### A.2 Main's reviews of side-lane claims

All of these are in `experiments/residual_progress/`.

| review (main commit) | outcome |
|---|---|
| `side_lane_review.json` (`65093c4`), `_2005.json` (`46198fb`) | PASS; depth and cluster findings scoped |
| `_latest.md/.json` (`8e2b5eb`) | PASS with seven scope corrections; one narrative ("3x−1 cycles protect the obstruction") rejected |
| `_e3111d3.json` (`1603bf3`), `_1a2dfc5.json` (`4a45eb0`), `_3d69784.json` (`bcde58e`) | PASS; R30 clocks corrected by main |
| `_bae3969.md` (`7206f9c`) | backward −17 word correct, and strict-ρ on its whole domain, which equals R56's k4 domain; positive-density inference rejected (already withdrawn) |
| `_767af32.md` (`d265d94`) | read; decision to prioritize a complete recursion |
| `_c2319c9.json` (`793e835`) | R58 probe reproduced with identical tallies |
| `_33c3829.md/.json` (`a489973`) | stopping-threshold argument and equivalence correct; both probes reproduced exactly |
| `_678e565.md/.json` (`ea3278e`) | transfer, `18u + 5` form and catalogue accepted; finite-base-only inference rejected (already withdrawn); halving renumbered R23 |
| `_13590c1.md/.json` (`aefdf60`) | R71 probe reproduced byte for byte, float bounds confirmed by integer bit lengths; 01:31 transfer correction accepted |
| `_d3a91fe.md` (`e9effe1`) | R73/R74 probe reproduced byte for byte |
| `_9849c53.md`, `_b9203ff.md`, `_64a5981.md` (`1d58f50`–`7d86314`) | probes reproduced byte for byte; R81 probe's ternary-minimality branch found unreachable (corrected) |
| `_fcc7e88.md` (`3b0c8a5`) | R75/R77 and general-spacing probes reproduced byte for byte; general spacing argument accepted; the informal average-valuation refinement not promoted |

`negative_controls/PR1_REVIEW.md` keeps C1–C5 at their stated scope. It rejects PR1's broad claims ("cheapest certificate is forced", "alternatives cannot succeed") with explicit counterexamples, including 56 equal-cost certificates on `A₇₆₈`.

### A.3 Side-lane corrections and withdrawals

1. **19:46.** The D+M+H coverage numbers were corrected at 20:22, after main found a bit-budget omission. The rate is unchanged.
2. **19:59.** A single `c/H²` density law for merge certificates was wrong. R27's fibres have density about `1/(2H)`. Corrected at 20:22.
3. **20:01.** "Must merge while high" was refuted by R32 and conceded at 20:44.
4. **23:32.** "A positive fraction of `q ≡ 1 (mod 3)` have no smaller ancestor" was withdrawn at 23:46: a moment bound does not imply it.
5. **01:04.** "`d = 1` can enter only through the finite base region" was corrected at 01:31: integrality does not transfer.
6. **01:04.** The halving bridge was mislabelled R27; it is R23 (corrected at 01:52).
7. **Other points main scoped, not amended in the feed:**
   - 22:21 and 22:46: the "scale-uniform" wording was not established beyond the samples.
   - 21:06: the 2M-sample rows are not reproducible from the committed probe.
   - 01:20: the control points apply only to claims that extend to the rational domain.
