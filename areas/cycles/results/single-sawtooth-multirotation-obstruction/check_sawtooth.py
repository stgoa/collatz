"""Replay the complete open-cell obstruction using exact rational arithmetic.

The proof data contain only rational nonnegative linear combinations. This
checker uses no linear-programming package and treats every branch without a
known contradiction as potentially feasible. Boundary transfer is proved in
the README. Default execution checks the deterministic receipt; the explicit
--write-receipt option regenerates it.
"""

from fractions import Fraction as F
from hashlib import sha256
import json
from pathlib import Path
import sys


HERE = Path(__file__).resolve().parent
DATA = HERE / "sawtooth_duals.json"
R = F(3, 8)
EPS = F(1, 1000)
MAX_ROTATION = 11
ZERO = (F(0),) * 4
ONE = (F(0), F(0), F(0), F(1))
H = (F(1), F(0), F(0), F(0))
P = (F(0), F(1), F(0), F(0))
Q = (F(0), F(0), F(1), F(0))
VERTICES = ((0, 0, 0), (0, 0, 1), (0, 1, 1),
            (F(1, 2), 0, 0), (F(1, 2), 0, 1), (F(1, 2), 1, 1))


def need(condition, message):
    if not condition:
        raise RuntimeError(message)


def add(a, b):
    return tuple(x + y for x, y in zip(a, b))


def neg(a):
    return tuple(-x for x in a)


def sub(a, b):
    return add(a, neg(b))


def mul(a, factor):
    return tuple(x * factor for x in a)


def constant(value):
    return (F(0), F(0), F(0), F(value))


def row(expression):
    """An affine expression <0 becomes (coefficients, right-hand side)."""
    return expression[:3] + (-expression[3],)


def row_key(rows):
    """Canonical JSON of reduced numerator/denominator pairs, never repr()."""
    values = [[[value.numerator, value.denominator] for value in r] for r in rows]
    return sha256(json.dumps(values, separators=(",", ":")).encode("ascii")).hexdigest()


INITIAL = tuple(row(x) for x in (
    neg(H), sub(H, constant(F(1, 2))), neg(P), sub(P, Q), sub(Q, ONE)
))


class Replay:
    def __init__(self, proofs):
        self.proofs = {proof["rows_hash"]: proof for proof in proofs}
        need(len(self.proofs) == len(proofs), "duplicate proof-data row hashes")
        self.cache = {}
        self.used = set()
        self.calls = 0
        self.prunes = 0
        self.constant_prunes = 0
        self.counts = {}
        self.survivors = 0

    def feasible(self, rows):
        """Only an exact contradiction may discard a branch."""
        self.calls += 1
        rows = tuple(dict.fromkeys(rows))
        if any(not any(r[:3]) and r[3] < 0 for r in rows):
            self.constant_prunes += 1
            return False
        # Dropping any constant rows only relaxes the branch. A strict 0<0
        # row could also be pruned, but retaining it as feasible is harmless.
        rows = tuple(r for r in rows if any(r[:3]))
        if rows in self.cache:
            return self.cache[rows]
        key = row_key(rows)
        if key not in self.proofs:
            self.cache[rows] = True
            return True
        proof = self.proofs[key]
        support = proof["support"]
        indices = [index for index, _ in support]
        need(indices and len(set(indices)) == len(indices), "nonempty distinct support")
        need(all(isinstance(i, int) and 0 <= i < len(rows) for i in indices), "support indices")
        weights = [F(weight) for _, weight in support]
        need(min(weights) >= 0 and sum(weights) == 1, "dual signs and exact normalization")
        need(all(sum(w * rows[i][j] for i, w in zip(indices, weights)) == 0
                 for j in range(3)), "dual variable coefficients")
        rhs = sum(w * rows[i][3] for i, w in zip(indices, weights))
        need(rhs <= 0 and rhs == F(proof["gap"]), "exact dual contradiction")
        self.used.add(key)
        self.prunes += 1
        self.cache[rows] = False
        return False

    def wraps(self, expression, rows):
        if expression == ZERO:
            yield rows, ONE  # exact pre-drop value, not the post-drop limit
            return
        values = [sum(expression[j] * vertex[j] for j in range(3)) + expression[3]
                  for vertex in VERTICES]
        low, high = min(values), max(values)
        ceil_high = -((-high.numerator) // high.denominator)
        for integer in range(low.numerator // low.denominator, ceil_high):
            endpoint = sub(expression, constant(integer))
            more = rows + (row(neg(endpoint)), row(sub(endpoint, ONE)))
            if self.feasible(more):
                yield more, endpoint

    def rotation(self, rows, k):
        self.counts[k] = self.counts.get(k, 0) + 1
        raw = [(ZERO, i) for i in range(k + 1)] + [
            (base, i) for base in (P, Q) for i in range(k)
        ]

        def wrap_all(index, conditions, points):
            if index == len(raw):
                order_all(0, conditions, points, [])
                return
            base, i = raw[index]
            endpoint = sub(base, mul(H, i))
            partner = add(base, mul(H, k - i))
            for rows1, e in self.wraps(endpoint, conditions):
                for rows2, ep in self.wraps(partner, rows1):
                    difference = sub(ep, e)
                    if difference == ZERO:
                        wrap_all(index + 1, rows2, points + [(e, e)])
                        continue
                    for larger, condition in ((ep, neg(difference)), (e, difference)):
                        more = rows2 + (row(condition),)
                        if self.feasible(more):
                            wrap_all(index + 1, more, points + [(e, larger)])

        def order_all(index, conditions, points, ordered):
            if index == len(points):
                more = conditions
                for j, (endpoint, height) in enumerate(ordered):
                    gap = sub(endpoint, ordered[j - 1][0])
                    if j == 0:
                        gap = add(gap, ONE)
                    more += (row(sub(sub(gap, mul(height, R)), constant(EPS))),)
                if self.feasible(more):
                    if k < MAX_ROTATION:
                        self.rotation(more, k + 1)
                    else:
                        self.survivors += 1
                return
            point = points[index]
            for position in range(len(ordered) + 1):
                more = conditions
                if position:
                    more += (row(sub(ordered[position - 1][0], point[0])),)
                if position < len(ordered):
                    more += (row(sub(point[0], ordered[position][0])),)
                if self.feasible(more):
                    order_all(index + 1, more, points,
                              ordered[:position] + [point] + ordered[position:])

        wrap_all(0, rows, [])

    def run(self):
        self.rotation(INITIAL, 1)
        need(not self.survivors, "a strict open branch survived")
        need(self.used == set(self.proofs), "unused proof records")
        return {
            "branches_entered_by_rotation": {str(k): v for k, v in sorted(self.counts.items())},
            "feasibility_calls": self.calls,
            "verified_exact_duals": len(self.used),
            "exact_dual_prunes": self.prunes,
            "constant_contradiction_prunes": self.constant_prunes,
            "survivors": self.survivors,
        }


def run():
    raw = DATA.read_bytes()
    data = json.loads(raw)
    need(data["schema"] == "single-sawtooth-exact-duals-v1", "proof-data schema")
    need(data["row_hash_encoding"] == "compact-json-reduced-numerator-denominator-pairs",
         "canonical row encoding")
    need(F(data["height_coefficient"]) == R and F(data["strict_error"]) == EPS,
         "proof-data parameters")
    need(data["maximum_rotation"] == MAX_ROTATION, "rotation range")
    stats = Replay(data["proofs"]).run()
    return {
        "schema": "single-sawtooth-multirotation-obstruction-v1",
        "height_coefficient": str(R), "error_threshold": str(EPS),
        "maximum_rotation": MAX_ROTATION,
        "proof_data_bytes": len(raw), "proof_data_sha256": sha256(raw).hexdigest(),
        "checker_sha256": sha256(Path(__file__).read_bytes()).hexdigest(),
        "row_hash_encoding": data["row_hash_encoding"],
        **stats,
        "scope": "Complete strict open-cell replay; the README proves pre-drop boundary transfer. No cycle exclusion.",
    }


def main():
    need(sys.argv[1:] in ([], ["--write-receipt"]), "usage: check_sawtooth.py [--write-receipt]")
    result = run()
    output = json.dumps(result, sort_keys=True, indent=2) + "\n"
    receipt = HERE / "check_sawtooth.json"
    if sys.argv[1:]:
        receipt.write_text(output)
    else:
        need(receipt.read_text() == output, "receipt mismatch; regenerate deliberately")
    print(json.dumps(result, sort_keys=True))


if __name__ == "__main__":
    main()
