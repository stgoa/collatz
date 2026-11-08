"""Optional dual discovery with NumPy/SciPy; never a certificate or CI input.

This searches the same finite branch tree as check_sawtooth.py. Floating-point
LP results suggest rational supports only. Every recorded support must then
pass exact normalization, coefficient cancellation and sign checks. The
resulting data must still be replayed by the independent solver-free checker.

Run explicitly with --write-proof-data. This overwrites the proof data, so
follow it with check_sawtooth.py --write-receipt and inspect the change.
"""

from fractions import Fraction as F
import json
import sys

import numpy as np
from scipy.optimize import linprog

from check_sawtooth import DATA, EPS, MAX_ROTATION, R, Replay, need, row_key


def exact_weights(rows, support):
    matrix = [[F(rows[j][i]) for j in support] + [F(0)] for i in range(3)]
    matrix.append([F(1)] * len(support) + [F(1)])
    rank, pivots = 0, []
    for column in range(len(support)):
        pivot = next((i for i in range(rank, 4) if matrix[i][column]), None)
        if pivot is None:
            continue
        matrix[rank], matrix[pivot] = matrix[pivot], matrix[rank]
        factor = matrix[rank][column]
        matrix[rank] = [x / factor for x in matrix[rank]]
        for i in range(4):
            if i != rank:
                factor = matrix[i][column]
                matrix[i] = [x - factor * y for x, y in zip(matrix[i], matrix[rank])]
        pivots.append(column)
        rank += 1
    if rank != len(support):
        return None
    weights = [F(0)] * len(support)
    for i, column in enumerate(pivots):
        weights[column] = matrix[i][-1]
    if not weights or min(weights) < 0 or sum(weights) != 1:
        return None
    if any(sum(weight * rows[j][i] for weight, j in zip(weights, support))
           for i in range(3)):
        return None
    gap = sum(weight * rows[j][3] for weight, j in zip(weights, support))
    return (weights, gap) if gap <= 0 else None


class Discovery(Replay):
    def feasible(self, rows):
        self.calls += 1
        rows = tuple(dict.fromkeys(rows))
        if any(not any(r[:3]) and r[3] < 0 for r in rows):
            self.constant_prunes += 1
            return False
        rows = tuple(r for r in rows if any(r[:3]))
        if rows in self.cache:
            return self.cache[rows]
        array = np.array(rows, dtype=float)
        solution = linprog([0, 0, 0], A_ub=array[:, :3], b_ub=array[:, 3] - 1e-7,
                           bounds=[(None, None)] * 3, method="highs")
        if solution.success:
            self.cache[rows] = True
            return True
        need(solution.status == 2, "LP discovery did not return an infeasibility candidate")
        equations = np.vstack((array[:, :3].T, np.ones(len(rows))))
        candidate = linprog(array[:, 3], A_eq=equations, b_eq=[0, 0, 0, 1],
                            bounds=(0, None), method="highs")
        need(candidate.success, "no floating support candidate")
        support = [i for i, value in enumerate(candidate.x) if value > 1e-9]
        result = exact_weights(rows, support)
        need(result is not None, "floating support failed exact verification")
        weights, gap = result
        key = row_key(rows)
        self.proofs[key] = {
            "rows_hash": key,
            "support": [[i, str(weight)] for i, weight in zip(support, weights)],
            "gap": str(gap),
        }
        self.used.add(key)
        self.prunes += 1
        self.cache[rows] = False
        return False


def main():
    need(sys.argv[1:] == ["--write-proof-data"],
         "usage: explore_sawtooth_duals.py --write-proof-data")
    search = Discovery([])
    stats = search.run()
    data = {
        "schema": "single-sawtooth-exact-duals-v1",
        "row_hash_encoding": "compact-json-reduced-numerator-denominator-pairs",
        "height_coefficient": str(R), "strict_error": str(EPS),
        "maximum_rotation": MAX_ROTATION, "proofs": list(search.proofs.values()),
    }
    DATA.write_text(json.dumps(data, separators=(",", ":")) + "\n")
    print(json.dumps(stats, sort_keys=True))


if __name__ == "__main__":
    main()
