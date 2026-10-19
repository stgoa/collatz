# C007 — Overlapping residue sets still admit distinct representatives

**Exact finite pass; the sufficient matching mechanism remains open.**
This read-only audit checks the 1,185 distinct normalized cycles in the
combined C001/C007 evidence. It omits the denominator-one fixed point,
leaving 1,184 cycles with q>1, including 51 in the ordered domain.
No new seeds or valuation words were searched. The census checker and
receipt remain unchanged.

For each observed height h, form either the set of numerator residues
`n_i mod q` or the set of normalized residues `n_i*2^(-h) mod q` at that
height. Binary powers are invertible because q is odd. These give two
bipartite graphs, with heights on the left and residue classes on the
right. An augmenting-path algorithm finds a matching covering every
observed height in **all 2,368 graphs**. Every returned assignment is
checked for membership, distinct representatives and complete coverage.

| Domain | Cycles | Raw matching passes | Normalized matching passes |
| --- | ---: | ---: | ---: |
| All q>1 cycles | 1,184 | 1,184 | 1,184 |
| Ordered cycles with q<=L | 51 | 51 | 51 |

There are 371 unordered cycles missing some intermediate height labels.
For example, the q11 cycle `(1,7)` has heights `{0,2}`. The audit covers
observed labels in those cases; adding a nonexistent height-one vertex
would create an empty-neighbor failure. Every ordered cycle contains
all heights 0 through B, as proved in C006, and covers that full range.

## The q5 overlap controls

For q5 and L187 the raw residue sets at heights 0,1,2,3 are

```
{2,3}, {2,3}, {1,2,3}, {1,2,3,4}.
```

They overlap, yet height representatives `(3,2,1,4)` are distinct.
The normalized residue sets are

```
{2,3}, {1,4}, {2,3,4}, {1,2,3,4},
```

with distinct representatives `(3,4,2,1)`. The other q5 period-17 cycle,
at L347, also has complete raw and normalized matchings. Thus overlap
refutes disjointness; it does not refute the existence of a system of
distinct representatives or Hall's subset inequalities.

## Mathematical scope

A universal matching theorem for all heights of ordered q>1 cycles
would imply `B+1<=phi(q)`, since all these residues are units. Such a
theorem is an **open sufficient mechanism**, not an established result
or progress obtained merely by translating the target. The same finite
matching pass on unordered cycles does not yet identify what order
contributes to a proof.

**q=1 was omitted from this test.** A theorem intended to exclude
nontrivial q1 cycles must state and prove its behavior there while
preserving the fixed point. The present q>1 evidence supplies no such
extension, and establishes neither the proposed height bound nor
cycle exclusion at untested periods.

## Exact replay

Run the following Python code from the repository root. It reads the
frozen cycle receipts, constructs the matchings again, and verifies the
assignments. No census is repeated and no file is written.

```python
from collections import Counter
from hashlib import sha256
from math import gcd
from pathlib import Path
import json

source_path = Path('experiments/cycle_spectrum/C001/actual_cycles.json')
c007_path = Path('experiments/cycle_spectrum/C007/height_denominator_audit.json')
assert sha256(source_path.read_bytes()).hexdigest() == '28d067d3f82585a3701616adce3b57cae994541c4ddd3b4859d2bcf2307e44f2'
assert sha256(c007_path.read_bytes()).hexdigest() == 'b35a18cb4209b5d0afd104f5c9e38926dc2de5dbef890cc324cf05ae83ce4ceb'
source = json.loads(source_path.read_text())
c007 = json.loads(c007_path.read_text())
rows = {(r['reduced_denominator'], tuple(r['primitive_states']))
        for r in source['cycles']}
new = c007['small_parameter_census']['new_normalized_cycles']
rows.update((r['q'], tuple(r['states'])) for r in new)
ordered = {(r['q'], r['L']): r['candidate_domain']
           for r in c007['existing']['spectrum']}
ordered.update({(r['q'], r['L']): r['candidate_domain'] for r in new})
assert len(rows) == 1185
counts, certificates = Counter(), []

for q, n in sorted(rows):
    if q == 1:
        continue
    L = min(n)
    heights = [(x//L).bit_length()-1 for x in n]
    labels = set(heights)
    counts['cycles_q_gt1'] += 1
    counts['ordered_cycles'] += ordered[q, L]
    counts['missing_intermediate_heights'] += len(labels) != max(heights)+1
    if ordered[q, L]:
        assert labels == set(range(max(heights)+1))
    for mode in ('raw', 'normalized'):
        graph = {h: set() for h in labels}
        for x, h in zip(n, heights):
            residue = x % q if mode == 'raw' else x*pow(pow(2, h, q), -1, q) % q
            assert gcd(residue, q) == 1
            graph[h].add(residue)
        owner = {}

        def augment(h, seen):
            for residue in sorted(graph[h]):
                if residue in seen:
                    continue
                seen.add(residue)
                if residue not in owner or augment(owner[residue], seen):
                    owner[residue] = h
                    return True
            return False

        for h in sorted(graph):
            assert augment(h, set()), (q, L, mode, h)
        assert len(owner) == len(graph) and set(owner.values()) == labels
        assert all(residue in graph[h] for residue, h in owner.items())
        counts[mode+'_passes'] += 1
        assignment = [[h, residue] for residue, h in
                      sorted(owner.items(), key=lambda item: item[1])]
        certificates.append([q, list(n), mode, assignment])

assert counts == dict(cycles_q_gt1=1184, ordered_cycles=51,
                     missing_intermediate_heights=371,
                     raw_passes=1184, normalized_passes=1184)
certificate_hash = sha256(json.dumps(certificates, sort_keys=True,
    separators=(',', ':')).encode()).hexdigest()
assert certificate_hash == '00b0c0946d6cbba22d3239edaf4eb1a55869cc568a2e5f23d02a56df02e65f98'
print(dict(status='PASS', counts=dict(counts),
           matching_certificates=len(certificates), sha256=certificate_hash))
```

The author ran the audit and replayed this saved code successfully.
This is an exact finite computation, separate from an all-size proof,
independent mathematical review or formal verification.
