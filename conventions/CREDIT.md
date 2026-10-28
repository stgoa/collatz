# Credit

How this project gives credit, and why. These rules are binding like [`SCHEMA.md`](SCHEMA.md): the computable part is [`tools/credit.py`](../tools/credit.py), and the generated result is the **Contributors** section of [`MAP.md`](../MAP.md).

## 1. Why a different system

Academic credit is authorship on a paper. That works against large collaboration on hard problems, in three ways:

- **It is coarse.** You are an author or you are not. A fixed lemma, a counterexample or a caught error is invisible unless it earns a byline.
- **It rewards the last step.** Whoever closes the final gap and writes it up gets the paper. The partial results that made it possible get citations at best.
- **It ignores review and failure.** "I checked this proof line by line" and "this method cannot work, here is why" are among the most valuable things in mathematics, and they earn nothing.

So rational people work alone, hide partial progress and race. An open problem needs the opposite. This project records every contribution as a small, attributed node, and it computes credit from the graph those nodes form. Sharing early then costs you nothing, and every step on the path keeps its share.

The idea builds on open collaborations such as Polymath, Mathlib and Tao's Equational Theories Project. What is particular here is that credit is **computed from the dependency graph**, not assigned by hand.

## 2. Principles

1. **The unit of credit is the node, not the paper.** Results, attempts, questions and reviews are all contributions with named contributors, and each is citable by its id.
2. **Credit flows along dependencies.** When a node builds on yours (`depends_on`, `assumes`), part of its value flows back to yours. Closing the last gap does not erase the path that led there.
3. **Review, refutation and failure count.** An independent review, a counterexample, or a well-documented dead end earns credit as a result does. Correctness is the shared goal, so the people who protect it are credited for it.
4. **Strength counts.** A `formal` result is worth more than a `reviewed` one, which is worth more than a `written` one, which is worth more than a `proposed` one. Credit rewards making things true and checkable, not making claims. Refuted and withdrawn nodes keep their history but earn nothing.
5. **People are accountable; agents are visible.** Every AI contribution names its model and the person who directed it. Credit rolls up to that person, and the agent's role stays on the record (§4).

## 3. How credit is computed (formula v1)

**Node value.** Each node starts from a base value set by its kind and status:

| Kind | proposed | written | reviewed | formal |
|---|---|---|---|---|
| result | 0.25 | 1 | 1.5 | 2 |
| attempt | 0.25 | 0.5 | 0.75 | 1 |

An open or answered question has base value 0.25. Sources and refuted, withdrawn or dropped nodes have base value 0.

To the base it adds half the value of each node built on it, shared equally among the nodes that dependent builds on:

```
value(n) = base(n) + 0.5 · Σ over nodes d that build on n of  value(d) / (number of nodes d builds on)
```

So a lemma that many results use is worth far more than its base, and a node nobody builds on earns only its base. That is the main defence against padding the graph with trivial nodes.

**Sharing a node's value.**
- If the node has independent reviewers (`reviewed_by` entries by someone other than its authors), they share 25% of its value equally, one share per reviewer.
- The authors share the rest equally.

**Your credit** is the sum of your shares over all nodes. MAP.md shows each contributor's share of the total. `python3 tools/credit.py --node <id>` shows how one node's value was computed and shared.

The weights are a first version. They are meant to be argued about and improved, by pull request against this page and `tools/credit.py` together, never by hand-editing the table.

## 4. People and agents

- Record an agent contribution with its model and the person who directed it, in the parentheses of the `authors` or `reviewed_by` entry: `Claude review lane (Opus 5.5; directed by Jane Doe)`. CI compares contributors by the part before the parentheses.
- MAP.md lists credit both by contributor (agent identities included) and **by accountable person**. An agent entry without "directed by" counts as its own person.
- Everything recorded before this page existed was produced by AI lanes directed by the repository owner ([`archive/HISTORY.md`](../archive/HISTORY.md)). `tools/credit.py` attributes those legacy lanes accordingly, so the person table starts at 100% for the owner. That share falls as others contribute.
- **Formalising a result is authorship.** When you write the Lean proof that makes a node `formal`, add yourself to its `authors` as, for example, `Jane Doe (Lean formalisation)`. Legacy Lean work is recorded in `## Lean` sections and in `reviewed_by`, not in `authors`, so it is under-credited by this formula.

## 5. What credit is for

1. **Recognition.** The generated table in MAP.md is the public record of who contributed what. Every pull request regenerates it (CI rejects a stale MAP.md), so it cannot be edited by hand, and the PR bot comment shows how each pull request shifts credit.
2. **Priority.** A merged node, or an open pull request, is a public, dated record of your contribution. It establishes priority for the idea from that moment, in the repository's history.
3. **Authorship of project papers.** A paper in [`papers/`](../papers/) presents a set of nodes. Its author list is everyone with credit in those nodes and in everything they depend on, ordered by that credit. The paper's README names the nodes and the formula version used. Anyone may decline authorship, and the authors may instead publish under a collective name with the generated list attached.

## 6. The decisive result

If someone proves something major, for example a full exclusion of nontrivial cycles, it is theirs.

- **You may publish your own result under your own name, anywhere.** Being the one who cracked it is a legitimate goal, and this page does not take it away.
- **Put it in the graph first, or at the same time.** Open the pull request with the node before or when you post a preprint. That keeps priority public and lets reviewers start.
- **Credit what you built on.** Cite the repository and the nodes your argument depends on, as the graph records them. Their contributors' credit stays in MAP.md whatever the byline of your paper.
- A project paper presenting the same result follows §5.3, and lists you first if the decisive node is yours.

## 7. Disputes and gaming

- **Wrong attribution:** fix it by pull request, citing the commit or review that shows who did the work. A node's `## History` records the change, with its date.
- **Padding the graph** with trivial nodes earns almost nothing, because value comes from being built on. Reviewers may also ask for trivial nodes to be merged into an existing one.
- **Self-review earns nothing.** A review counts only when the reviewer's identity differs from every author's (`tools/check.py` enforces this for status, and `tools/credit.py` for credit).
- If the formula rewards something it should not, that is a reason to change it by pull request.
