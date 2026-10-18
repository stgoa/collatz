# V003 — Audit against the arithmetic-regularity goal

**Scope:** the unchanged [user goal](../../../docs/ARITHMETIC_REGULARITY_BRIEF.md)
asks for a demonstrated mathematical gain from arithmetic regularity, or a
decisive scoped reason to redirect it. Its principal research aim is the
binary-automatic classification. It explicitly accepts a rigorous partial
classification or structural gain as an outcome. We retain that full aim
and report it as open; we do not claim to have completed that classification.

The [report](REPORT.md) delivers the strongest justified results from the
bounded investigations and recommends the next investigation. The table
below separates substantive evidence from repository delivery. Completion
of the goal requires the delivery checks and push recorded in the log.

## Requirement-by-requirement evidence

| Requirement | Current-state evidence | Conclusion and limit |
|---|---|---|
| Study the exact finite-valued binary-automatic invariant problem | kernel_probe.md §1; literature.md exact-question section | Both equations, their domains, absorber exception and bookkeeping value at0 are fixed. The full class remains open here. |
| Obtain gain beyond periodic and supplied two-base cases | digit_sum.md complete proof; kernel_probe.md §§2–4; independent PROOF_REVIEW.md | Met: all F(s_2(n)) are constant, including every digit-count-modulo-m automatic family; the first ternary image and pure-zero orbit have rigorous bounds. These are all-input arguments, not finite catalogues. |
| Literature baseline from primary sources | literature.md L1–L5 and source-attribution qualifications | Met as a bounded source review: fixed-depth recognition, rational orbit series, Cobham, Mahler and progression sufficiency are compared with the exact target. No exact one-base classification was located; no claim of exhaustive search or novelty follows. |
| Distinguish fixed depth from entire basin | literature.md L1 | The unbounded union is explicitly an unsupplied regularity premise. |
| Test binary-to-ternary closure | kernel_probe.md §§2–5 and PROOF_REVIEW.md §2 | Met: all first ternary images of the original K lie in K union {f_1}; repeated T_0 has at most |K| states. Mixed iterates are identified and not assumed to close. |
| Make missing information explicit | kernel_probe.md §5; literature.md L6 exact CRT separation | Met: scaling invariance alone allows an infinite mixed kernel. The counterexample fails the full guarded equation, which a successful proof must retain. |
| Use Cobham only with its premises | kernel_probe.md §5; literature.md L3–L4 | Met: full second-base automaticity remains conditional. A finite characteristic-zero 3-Mahler relation is an alternative missing input, not an adopted theorem about h. |
| One bounded carry test with complete boundary | carry_boundary.md §§1–3; verify_examples.py check_carry_patch | Met: full rectangle, zero and undefined rays, nonlocal bootstrap and carry flush are explicit. The symbolic tail checks accompany the finite arithmetic; no parallel-update count is inferred. |
| Compare before deepening | REPORT.md §§4 and6; VIEWPOINT_MAP.md focused programme | Met: V13 earns a focused mixed-section follow-up; V14 closes after adding no relation. V12 is retained as an alternative if the next bounded probe adds no structure. |
| Exercise general claims against cycle controls | REPORT.md §5; PROOF_REVIEW.md §4; verifier check_controls and cylinder checks | Met at each claim's scope. Actual d5/d61 nonabsorbing cycles, divisible fixed points, invariant colors, failed d1 section identity and both colors in dyadic cylinders are checked. No d5 tile construction or divergence test is claimed. |
| Preserve exact clocks, domains and absorber | Each proof's domain section; carry clocks; actual predecessor replay | Met: source1 is excluded where necessary, raw shortcut prefixes stay above1, section operations are not orbit clocks, and exact valuation4 uses modulus32. |
| Keep novelty separate | Status labels and primary-source note; known cylinder result explicitly credited | Met: the independently written digit/kernel gains have undetermined novelty. The cylinder rederivation is not counted as a new result. |
| Persist proofs, failures, sources and checks | V003 directory, brief, logs and updated README/map | Met; executable receipt is separate from written proof and external theorem evidence. |
| Review independent side lane read-only | side_review.md at c583fc3e1adab7c15d6297a5acf55d7560fc5e08; VIEWPOINT_LOG.md | Met: DIRECTIONS/FEED and the relevant probe were read. Numerical cutoff/state bound remains conditional and encoding-dependent; no side files or branches were changed. |
| Preserve frozen results and open LaTeX | Delivery integrity check in VIEWPOINT_LOG.md | Requires the actual diff/hash check recorded there; no historical proof/code/evidence is part of this edit set. |
| Appropriate verification and commit/push | verification.json and delivery record in VIEWPOINT_LOG.md | Requires successful independent replay, link/whitespace/integrity checks and confirmed push to origin/main. No Phase6 infrastructure or frozen evidence was modified, so its full gate is not a new requirement for this standalone batch. |

## Why this is substantive progress

The digit-count result excludes an explicitly infinite class of descriptions,
including nonperiodic automatic examples. Its proof uses an unbounded
parameterized family of legal arithmetic inputs. The kernel result controls
the first ternary image of **every** binary state, not just a sample or the
initial coloring. The scaling counterexample supplies pairwise witnesses
for infinitely many mixed sections under a precisely weaker hypothesis.
These address three outcomes expressly listed in the original goal.

The prior goal turn that drafted wording supplied no additional research
evidence; it is classified as **no progress** for the research goal. This
continuation resumes saved proof work, corrects reviewed issues, adds
independent executable checks and persists the completed comparison. The
substantive V003 research and this delivery continuation are progress. There
is no external blocking condition and no verified wait is needed.

## Open boundaries after delivery

1. No complete classification of binary-automatic invariant colorings.
2. No finite closure of the arbitrary mixed ternary sections.
3. No supplied 3-Mahler equation for an arbitrary color indicator.
4. No periodicity, automaticity or digit-count description of a hypothetical
   nonabsorbing set.
5. No convergence, human peer review, formal verification or established
   novelty of the new elementary arguments.

These are retained research questions. The deliverable is the demonstrated
gain, precise limits and recommendation specified by the goal, with the
delivery record as its final completion evidence.
