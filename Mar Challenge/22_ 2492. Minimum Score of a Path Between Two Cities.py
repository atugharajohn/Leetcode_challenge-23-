# problem:
# https://leetcode.com/problems/minimum-score-of-a-path-between-two-cities/

# solution:
class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        parent = list(range(n))
        
        def find(p): 
            """Return the root of p."""
            if p != parent[p]: parent[p] = find(parent[p])
            return parent[p]
        
        mp = defaultdict(lambda : inf)
        for u, v, dist in roads: 
            uu = find(u-1)
            vv = find(v-1)
            parent[uu] = vv
            mp[uu] = mp[vv] = min(mp[uu], mp[vv], dist)
        return mp[find(0)] if find(0) == find(n-1) else -1