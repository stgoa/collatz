# The Collatz research trajectory: a short summary

*This is a snapshot taken at about 12:00 (UTC−3) on 2026-10-18. The repository is `stgoa/collatz`. The side lane (Claude, branch `claude/sidekick`) wrote it for readers who do not have the repository context. It makes no novelty claims, and Collatz is not proved.*

**In brief.** In about fifteen hours, an AI-driven programme did three things:

- It rigorously reduced the Collatz conjecture to one family of "pair obligations": for every odd `u`, the orbits of `u` and `18u + 5` must meet.
- It built a strict-rank induction over those obligations.
- It proved 94 scoped results around that induction.

Completing the induction turned out to be equivalent to a uniform stopping-time statement, which is the conjecture's classical core. Every obstruction found is a 2-adic shadow of a non-integer rational cycle of the `3x+1` map. That explains why local rule-building stalls.

---

## 1. Who did what

- **Main lane** (ChatGPT/Codex, branch `main`). From 17 Oct 16:55 to 18 Oct 07:33, its 39 commits produced results R1–R94. Each result comes with a written proof or a precisely stated finite certificate, an executable checker and a JSON receipt. There have been no main commits since R94.
- **Side lane** (Claude, branch `claude/sidekick`). It checks main's claims with independent code, runs negative controls and measurements, and offers reformulations. Its first audit lane was merged into main as PR1 (audits C1–C5). Its running log is `archive/side_lane/FEED.md`, and `archive/side_lane/writeup/SYNTHESIS.md` holds a longer survey.
- **Ground rules.** Every no-go result is scoped: it excludes a named procedure, not the conjecture and not the framework. Corrections are logged openly in both lanes.

## 2. The language in one paragraph

- **The map.** `S(x) = (3x+1)/2^v` is the odd-only Collatz (Syracuse) map, with 1 absorbing.
- **Normal form.** Two exact "bridge" identities identify states that have the same future: `S(4x+1) = S(x)`, and a halving rule for certain climbers `x = 2^a·t − 1`. Collapsing by them gives a normal form `ν(x)`, and the quotient map `T = ν∘S` acts on canonical states (R25).
- **Currents.** A *current* is a finite signed integer combination of Syracuse arrows. Its divergence telescopes, so `[x] − [y]` has a finite current exactly when the orbits of `x` and `y` meet.
- **Pair obligations.** The central objects are `P(w) = [3w] − [w]` on `W5 = {w ≡ 5 (mod 8)}`, ranked by `ρ(w) = ν(3w)`.

## 3. The main-lane trajectory in five phases

| phase | results | time, 17–18 Oct (approx.) | idea | outcome |
|---|---|---|---|---|
| 1. Annular currents | R1–R22 | 16:55–19:55 | Signed source measures on annuli, packets, and finite currents that move mass toward 1. | Finite certificates at fixed cutoffs. R7 shows exactly what currents detect. Exposure depth is unbounded (R13, R16, R22). No uniform closure. |
| 2. Bridges and normal form | R23–R36 | 19:55–21:07 | The exact identities behind `ν`, the quotient `T`, its complete inverse branches (one point and two rays), and shrinking pair rules. | The right coordinates, and the move from measures to pairs. |
| 3. W5 reduction | R37–R43 | 21:29–22:18 | Eliminate the `9 (mod 16)` pairs. | **R40:** Collatz ⇔ every `P(w)` with `w ∈ W5` has a finite current ⇔ for every odd `u`, the orbits of `u` and `18u + 5` meet. **R43:** rules whose requests all have smaller `ρ` compose by strong induction. |
| 4. Rule programme | R44–R76 | 22:18–02:50 | Conditional rules, each reducing `P(w)` to smaller-rank requests on explicit domains; 17 families. | Twelve rules accept about 70% of sampled inputs in one step. Full signed closure with 15 families completes only about 5.5%. Every attempt to finish meets a scoped obstruction. |
| 5. Histories and comparisons | R77–R94 | 02:50–07:33 | Compare a critical source with smaller histories, or with later targets, instead of local rules. | Clock barriers (R85, R94), computer-assisted precision barriers (R91, R92), and an exact two-source interface (R93). The missing merger remains open. |

**Typical obstructions (all scoped).**

- Growing prefixes on whole residue classes defeat any fixed lookahead (R54).
- Natural continuations undo themselves exactly (R61, R63, R87).
- The all-ray procedure has a coverage bound (R66).
- Mixed blocks and re-entries can keep growing (R67, R70).
- No finite-label or finite-centre potential decreases along the procedures (R31, R69, R72).
- No fixed clock budget suffices (R85, R94).
- Smaller origins are excluded inside precision windows (R41, R46, R49, R68, R91, R92).

On the positive side, R71 shows that whole-word integrality rules out integer cycles for mechanical (Sturmian-type) valuation words.

## 4. What the side lane added

- **Verification.** Of the 94 results:
  - 74 are independently checked, fully or in their arithmetic parts;
  - 8 are measured only;
  - 12 are untouched; these need main's internal planner or the annular source machinery.

  The highlights are an exhaustive C classification of 176.8 million rational origins, which reproduces R91 and R92 exactly, and inverse-tree confirmations of R92. Corrections went both ways (for example a clock in R30, and several side-lane overclaims), and all are logged.
- **The core equivalence (accepted by main).** Completing the strict-rank recursion is equivalent to a stopping-time statement for "critical images": for every `w ∈ W5`, the `T`-orbit of `ν(3w)` drops below `(8ν(3w) − 5)/9`. That statement is equivalent to Collatz. So the programme's remaining gap is exactly the classical one.
- **Why local rules stall: rational-cycle shadows.** The obstruction families, and the sources in R90–R94, are 2-adic shadows of rational cycles of `3x+1` that are not positive integers:
  - the negative cycles `{−1}`, `{−5, −7}` and the 7-cycle through `−17`;
  - a 12-step cycle through `−1792529/7153`, where `7153 = 3¹² − 2¹⁹`;
  - a 24-step quotient cycle with denominator `3²⁴ − 2³⁷`;
  - a positive, contracting 377-cycle through `7817/7153`.

  Expanding cycle points are dense in the 2-adic integers. A positive integer that agrees with one to `k` bits follows its word, and grows, for about `k` divided by the word's cost periods. So every residue class contains inputs that outlast any fixed lookahead or finite word catalogue.
- **Transfer principle.** Every local identity carries over verbatim to `3x + d` with `gcd(d, 6) = 1`, via `x ↦ x/d`. Arguments built only from such identities therefore cannot separate `d = 1` from maps that have extra cycles. A proof needs input that does not transfer, such as whole-word integrality or archimedean size. Negative controls on `3x + 61` illustrate this (C2, C4).
- **Smaller results.**
  - A divergent itinerary needs factor complexity `liminf p(L)/L ≥ 1/log₂(3/2) ≈ 1.7095`.
  - A catalogue of 3,889 positive rational cycles, within its search bounds, has `{1}` as its only integer cycle.
  - 48.5% of canonical states below `2·10⁶` have no smaller ancestor at any depth.
  - On the early annular layer, absorption is set by depth rather than size. 99% of positive mass joins 1's component by about depth 25 for every `N` tested, and only a thin tail needs depth around `7.3·log₂N`.

## 5. Where it stands

- Collatz is rigorously reduced to one family of pair obligations and one strict-rank induction. Completing that induction is equivalent to a uniform stopping-time theorem for the critical images, which is the conjecture itself.
- Main's latest standing says that universal construction "remains missing". Its stated next step is one of two things:
  - a comparison with input-dependent, unbounded clocks and a proved well-founded decrease;
  - a different smaller history whose whole parameter domain closes.
- This is the same wall the literature hits. "Almost all" results exist (Terras 1976; Tao 2019, almost all orbits attain almost bounded values), but none reaches "all". Cycle exclusions rest on Diophantine bounds (Simons–de Weger, Hercher) and on computation beyond `2⁶⁸` (Barina).

## 6. Questions for an outside reader

1. **Divergence half.** A positive integer can follow an expanding rational-cycle shadow only for a time proportional to its 2-adic agreement, which its size bounds. Can one rule out chaining infinitely many such episodes? That needs archimedean and 2-adic information together, which the local framework cannot combine.
2. **Cycle half.** Can whole-word integrality (R71), together with Baker-type bounds on linear forms in logarithms, be made to act on the W5 pair objects?
3. **A potential that does not transfer.** Is there a quantity that decreases along the W5 recursion for every input of `3x+1`, but provably not for `3x+61`?
4. **Framework.** Is there a known structure that organizes the rational-cycle shadows for all denominators `2^m − 3^k` at once? Candidates include 2-adic dynamics, automatic sequences, or a cohomological ("Langlands-style") bookkeeping of cycles.

## 7. Where to look

- `archive/docs/RESULTS.md`: every result R1–R94 and the audits C1–C5, each with its status and links.
- `experiments/residual_progress/REPORT.md`: main's working log and current standing.
- `archive/side_lane/writeup/SYNTHESIS.md`: the longer survey, including the verification ledger.
- `archive/side_lane/FEED.md`: the side-lane log; every entry gives a reproduction command.
- `archive/side_lane/frameworks/MEMO.md`: framework scouting and the literature check.
