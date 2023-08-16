# problem:
# https://leetcode.com/problems/count-unreachable-pairs-of-nodes-in-an-undirected-graph/

# solution:
class Solution:
    def countPairs(self, n: int, edges: List[List[int]]) -> int:
        def dfs(graph,node,visited):
            visited.add(node)
            self.c += 1
            for child in graph[node]:
                if child not in visited:
                    dfs(graph, child, visited)
        
        #build graph
        graph = {}
        for i in range(n):
            graph[i] = []
            
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        visited = set()
        count = 0
        totalNodes = 0
        
        #run dfs in unvisited nodes
        for i in range(n):
            if i not in visited:
                self.c = 0
                dfs(graph, i, visited)
                
                count += totalNodes*self.c    # result 
                totalNodes += self.c          # total nodes visited 
        return count