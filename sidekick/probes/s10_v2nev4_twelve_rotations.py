"""S10: the v2 != v4 four-mismatch pattern on the grid against rotations up to 12h (fixed model; ~10 min)."""
import sys
sys.path.insert(0, '/Users/armstrongsantiago/CodexWorkspace/.claude/worktrees/claude-vs-chatgpt-perf-8230f6/sidekick/probes')
from s10_multirotation_lp import margin, pts_for, grid
def run(step_h, step_p, K=12):
    n2, best = 0, None
    for h, p1, p2 in grid(step_h, step_p):
        if margin(pts_for(1, h, p1, p2, False), h % 1.0) < 0: continue
        if margin(pts_for(2, h, p1, p2, False), (2 * h) % 1.0) < 0: continue
        n2 += 1
        mn = min(margin(pts_for(k, h, p1, p2, False), (k * h) % 1.0) for k in range(3, K + 1))
        if best is None or mn > best[0]:
            best = (round(mn, 4), round(h, 4), round(p1, 4), round(p2, 4))
    return n2, best
print("coarse (h 0.0025, p 0.005):", run(0.0025, 0.005))
print("finer  (h 0.001, p 0.0025):", run(0.001, 0.0025))
