"""Finite dependency survey of the fixed nine-rho and separate-sigma dispatchers.

No common global rank or universal termination is inferred from this survey.
The cap raises an error; it never silently omits a dependency.
"""
from collections import deque
import hashlib
import json
from pathlib import Path
import sys

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent / 'continued_rules'))
import continued_rules as RHO
sys.path.insert(0, str(HERE.parent / 'phase_rank'))
import sigma_rank as SIGMA


def survey(upper, max_nodes=20000):
    graph = {}
    pending = deque(range(5, upper, 8))
    while pending:
        w = pending.popleft()
        if w in graph:
            continue
        if len(graph) >= max_nodes:
            raise RuntimeError('Finite dependency survey reached its node cap')
        rules = []
        for name, dispatcher in (('rho', RHO.one_step), ('sigma', SIGMA.one_step)):
            data = dispatcher(w)
            if data is not None:
                rules.append((name, data['rule'], sorted(data['coefficients'].items())))
        children = sorted({u for _, _, coefficients in rules for u, _ in coefficients})
        graph[w] = (rules, children)
        pending.extend(children)
    # Kahn elimination is solely a finite acyclicity check. It supplies no
    # missing leaf current and claims nothing outside this complete finite graph.
    incoming = dict.fromkeys(graph, 0)
    for _, children in graph.values():
        for u in children:
            incoming[u] += 1
    ready = deque(sorted(w for w, degree in incoming.items() if degree == 0))
    order = []
    while ready:
        w = ready.popleft()
        order.append(w)
        for u in graph[w][1]:
            incoming[u] -= 1
            if incoming[u] == 0:
                ready.append(u)
    payload = [[w, *graph[w]] for w in sorted(graph)]
    return dict(root_upper_bound=upper, roots=len(range(5, upper, 8)),
                dependency_nodes=len(graph), removed_nodes=len(order),
                acyclic=len(order) == len(graph),
                unresolved_leaves=sum(not rules for rules, _ in graph.values()),
                node_cap=max_nodes,
                graph_sha256=hashlib.sha256(json.dumps(payload, separators=(',', ':')).encode()).hexdigest())


def main():
    result = dict(scope='Finite survey only; no common global rank or new pair certificate',
                  cases=[survey(16384), survey(131072)])
    path = HERE / 'rank_mixing_audit.json'
    if sys.argv[1:] == ['--write-receipt']:
        path.write_text(json.dumps(result, indent=2) + '\n')
    elif sys.argv[1:]:
        raise ValueError('Only --write-receipt is supported')
    else:
        assert result == json.loads(path.read_text())
    print(json.dumps(result, indent=2))


if __name__ == '__main__':
    main()
