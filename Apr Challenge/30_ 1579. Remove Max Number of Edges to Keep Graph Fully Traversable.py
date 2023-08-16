# problem:
# https://leetcode.com/problems/remove-max-number-of-edges-to-keep-graph-fully-traversable/

# solution:
class UnionFind:
    def __init__(self, n):
        self.root = list(range(n))
        self.rank = [1] * n
        self.groups = n - 1
    
    def find(self, x):
        while x != self.root[x]:
            self.root[x] = self.root[self.root[x]]
            x = self.root[x]
        return self.root[x]
    
    def union(self, x, y):
        px, py = self.find(x), self.find(y)
        
        if px == py:
            return 0

        if self.rank[px] <= self.rank[py]:
            self.root[px] = py
            self.rank[py] += self.rank[px]
        elif self.rank[px] > self.rank[py]: 
            self.root[py] = px
            self.rank[px] += self.rank[py]
        self.groups -= 1
        return 1

class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        uf = UnionFind(n+1)
        alice, bob, common = 1, 2, 3
        output = 0
        graph = defaultdict(list)
        for t, a, b in edges:
            graph[t].append((a, b))
        
        # Common Graph
        for u, v in graph[common]:
            if uf.union(u, v) == 0:
                output += 1
        uf_alice, uf_bob = deepcopy(uf), deepcopy(uf)
        
        # Alice
        for u, v in graph[alice]:
            if uf_alice.union(u, v) == 0:
                output += 1
        # Bob
        for u, v in graph[bob]:
            if uf_bob.union(u, v) == 0:
                output += 1

        return -1 if uf_bob.groups > 1 or uf_alice.groups > 1 else output