# problem:
# https://leetcode.com/problems/as-far-from-land-as-possible/

# solution:
class Solution:
    def maxDistance(self, grid: list[list[int]]) -> int:
        dist, n = [[0 if v == 1 else inf for v in row] for row in grid], len(grid)
        for r in range(n):
            for cp, c in chain(pairwise(range(n)), pairwise(range(n-1, -1, -1))):
                dist[r][c] = min(dist[r][c], dist[r][cp] + 1)
        for c in range(n):
            for rp, r in chain(pairwise(range(n)), pairwise(range(n-1, -1, -1))):
                dist[r][c] = min(dist[r][c], dist[rp][c] + 1)

        maxdist = max(dist for row in dist for dist in row)
        return -1 if maxdist in (0, inf) else maxdist