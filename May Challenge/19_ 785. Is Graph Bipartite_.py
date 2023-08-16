# problem:
# https://leetcode.com/problems/is-graph-bipartite/

# solution:
class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        self.color = {}
        self.graph = graph
        for n in range(len(graph)):
            if n not in self.color:
                self.color[n] = 0
                if not self.dfs(n):
                    return False
        return True
    
    def dfs(self, node):
        for n in self.graph[node]:
            if n not in self.color:
                self.color[n] = 1 - self.color[node]
                if not self.dfs(n):
                    return False
            elif self.color[n] == self.color[node]:
                return False
        return True